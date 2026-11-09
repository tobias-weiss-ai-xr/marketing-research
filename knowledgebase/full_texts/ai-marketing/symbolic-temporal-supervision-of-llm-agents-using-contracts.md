---
title: Symbolic Temporal Supervision of LLM Agents Using Contracts
url: https://arxiv.org/abs/2609.18128
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Yifeng Xiao
- Pierluigi Nuzzo
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.18128
pages: 13
chars: 55765
fetched_at: '2026-11-08T13:34:11+00:00'
kb_version: 1
---

# Symbolic Temporal Supervision of LLM Agents Using Contracts

Symbolic Temporal Supervision of LLM Agents Using Contracts∗
Yifeng Xiao1 Pierluigi Nuzzo1
1Department of Electrical Engineering and Computer Sciences, University of California, Berkeley, CA, USA
{yifeng_xiao, pierluigi.nuzzo}@berkeley.edu
Abstract
Large language model (LLM) agents augmented by tools can
automate complex, multi-step tasks, such as web navigation,
codegeneration,andworkfloworchestration,byactingonex-
ternalsystemsthroughtoolcalls.However,hallucinations,dis-
tributionalinstability,andadversarialmanipulationsinLLMs,
and the irreversible consequences of certain tool calls can
lead to harmful outcomes. Existing safeguards either grade
recorded trajectories post hoc with stochastic LLM judges or
blockunsafeactionsonecallatatime,andnosingledetermin-
istic artifact supports both roles. We presentContrAgent, a
contract-based framework for symbolic temporal supervision
of LLM agents.ContrAgentcaptures an agent’s behavior as
a sequence of tool calls and formalizes it as a trace over a
fixedsetofcheckablepredicates.Itthenspecifiesrequiredbe-
haviors using assume-guarantee contracts in linear temporal
logic over finite traces (LTLf). Each contract is compiled to
a deterministic finite automaton (DFA) that serves two roles:
gating agent actions online and evaluating recorded traces
offline. A contract library, acting as a reusable knowledge
base, is maintained independently of the agent’s model and
can be applied across different agents within the same task
domain. We show the effectiveness of our approach on four
benchmarksspanningbothroles,whereContrAgentmatches
state-of-the-artLLM-judgeandrule-basedguardrailbaselines
while producing deterministic, reproducible verdicts and, in
the online mode, orders-of-magnitude lower per-call latency.
1 Introduction
Recent tool-augmented large language model (LLM) agents
can automate complex, multi-step tasks in real-world do-
mains, including web navigation (Zhou et al. 2024), code
generation (Jimenez et al. 2024), and workflow orchestra-
tion (Wu et al. 2024). Agentic frameworks such as Open-
Claw (OpenClaw Project 2026), HermesAgent (Nous Re-
search 2026), and LangChain (Chase 2022) achieve these
capabilities through tool-call interfaces, ranging from shell
commandstoapplicationprogramminginterface(API)calls
and protocols such as the Model Context Protocol (MCP)
(Anthropic2024).Theseinterfacesletagentsactonexternal
systems, but they also introduce safety risks: the hallucina-
tions and distributional instability of LLMs combined with
possible adversarial manipulations and the irreversible con-
sequences of tool calls can lead to harmful outcomes. These
∗Preprint.
Figure 1:ContrAgentmonitors the tool-call interface be-
tween an LLM agent and its tools.
failuremodesincludeindirectpromptinjection,metricgam-
ing under performance pressure, dangerous code execution,
and identity confusion across delegating agents (Sotiropou-
los et al. 2025).
Several approaches grade a recorded trajectory post hoc
withanLLMjudgeoralearneddetector(Zhengetal.2023;
Sharma, Barke, and Zorn 2026; Wen et al. 2026), but their
verdicts are stochastic and hard to reproduce. Enforcement
mechanisms instead block unsafe actions in real time, yet
they judge each action in isolation and miss properties that
span the trajectory (Wang, Poskitt, and Sun 2026; Inan et al.
2023),attachtosemanticintentratherthantool-callbehavior
(Kamath et al. 2025; Miculicich et al. 2025), or depend on
a model of the specific agent (Wang et al. 2025). No single
deterministicartifactbothguardsanagentonlineandgrades
a recorded trajectory offline.
Inspired by assume-guarantee (A/G) contract-based de-
sign(Benvenisteetal.2018;Nuzzoetal.2015),whosecom-
positional reasoning has been applied to cyber-physical sys-
tems (Xiao et al. 2024; Xiao and Nuzzo 2026; Xiao et al.
2026), we presentContrAgent, a contract-based, model-
agnostic,deterministicframeworkforsymbolictemporalsu-
pervision of LLM agents. We formalize trajectory-level re-
quirementsasA/Gcontractsinlineartemporallogiconfinite
traces(LTL f)(DeGiacomoandVardi2013)overcheckable
atomic propositions (AP) on agent actions. Contracts are
compiled to deterministic finite automaton (DFA) checkers
that supervise the agent’s trajectory, by gating agent actions
online, as shown in Figure 1, or evaluating recorded traces
offline. Our contributions can be summarized as follows:
•WeintroduceA/Gcontractsasformalspecificationsofin-
tentrequirementsforLLMagents,usingasetofcheckable
arXiv:2609.18128v1  [cs.AI]  16 Sep 2026

AP over tool-call traces and forming a contract library.
•We presentContrAgent, a model-agnostic, deterministic
supervision framework for LLM agents using contracts
to both shield an agent online and score its traces offline.
•We evaluateContrAgentacross four benchmarks span-
ning both roles, showing it matches strong LLM-judge
andguardrailbaselinesatordersofmagnitudelowerper-
call latency, and provides a deterministic, reproducible
evaluator of recorded traces.
The remainder of the paper is organized as follows. Af-
ter discussing related work in Section 2, we provide back-
ground on agent frameworks, LTLf, and A/G contracts in
Section 3. Section 4 introduces interaction predicates and
agent contracts, while Section 5 provides details on contract
compilation and contract-based supervision. Section 6 re-
ports results from the four benchmarks, and is followed by
concluding remarks in Section 7.
2 Related Work
Most runtime safeguards for tool-based operation of LLM
agentsactatthetool-callboundary.Per-actionrulelanguages
suchasAgentSpec(Wang,Poskitt,andSun2026)checkeach
proposed call against a set of rules. They are fast and deter-
ministic but scoped to a single action rather than reasoning
aboutatrajectory’sactionordering,history,orcounts.Asep-
arateinformation-flowlineofworktracksdataandprivilege
acrosstheexecutiontostoppromptinjectionandexfiltration,
as in Progent (Shi et al. 2025), CaMeL (Debenedetti et al.
2025), RTBAS (Zhong et al. 2025), and Fides (Costa et al.
2025). The threat model considered in this line of work is,
however, orthogonal toContrAgent’s contracts.
A class of approaches uses logic to reason about the exe-
cution trace: Agent-C (Kamath et al. 2025) checks temporal
constraintswithsatisfiabilitymodulotheories(SMT)solving
duringgeneration,VeriGuard(Miculicichetal.2025)gener-
atespolicycodewithanLLMandformallyverifiesitbefore
use, and FORGE (Palumbo et al. 2026) weaves determinis-
tic Datalog policies into multi-agent deployments. However,
none of them maintains a symbolic verdict over the whole
trajectory. Safety Chip (Yang et al. 2024) compiles propo-
sitional linear temporal logic (LTL) to mask unsafe actions
of embodied robot agents, whereasContrAgentsupervises
general tool-calling LLM agents with A/G contracts over
checkable AP.
Another class of approaches aims to grade or shield be-
haviors using a learned model or an LLM judge. LLM-as-
judgegraders(Zhengetal.2023),AgentPex(Sharma,Barke,
and Zorn 2026), and learned detectors such as PolicyGuard
(Wen et al. 2026) score recorded trajectories, but their ver-
dicts are stochastic and hard to reproduce, particularly on
safetyjudgments(ChenandGoldfarb-Tarrant2025).Shield-
Agent(Chen,Kang,andLi2025)compilespolicydocuments
intoaction-basedprobabilisticrulecircuits,ABC(Bhardwaj
2026)enforcesbehavioralcontractsunderaprobabilisticsat-
isfactionrelation,andProbGuard(Wangetal.2025)predicts
violationsbyprobabilisticmodelcheckingofalearnedagent
model, so their verdicts are probabilistic and are not used to
deterministically block undesirable behaviors.
3 Preliminaries
As we aim to supervise an agent’s tool calls with A/G con-
tracts, we first give background on agent frameworks and
temporal logic, then state the supervision problem.
3.1 Agent Frameworks
An agent pairs an LLM backbone with a tool set, issuing
tool calls and folding their outputs into a reasoning loop
until task completion (Yao et al. 2023). Thetool-call inter-
faceis the set of tools the framework exposes to the agent,
together with their call and return conventions. Reasoning
steps carry the agent’s decision making, but they take exter-
naleffectonlythroughthetoolcallstheyissue,andtheclass
of irreversible consequences this paper targets arises at this
interface.ContrAgenttherefore tracks thetool-call trace,
theorderedsequenceoftool-calleventstheagentemits,now
often a long-horizon, multi-tool trajectory (Xu et al. 2026).
Definition 1 (Agent session)LetΣdenote the finite set of
tool-callevents. Each tool call produces two events: acall
eventa= (tool,args)when the agent issues the call, and
areturneventa ′ = (tool,result)when the executed tool
returns.Anagent’sexecutionisatransitionsystem(Baierand
Katoen 2008)T= (S, s 0,Σ, R). A states:= (τ, κ, ρ)∈S
comprises the traceτ∈Σ ∗ of events issued so far, a finite
mapκfrom context keys to values recorded from earlier
events,andavectorρofnumericsessioncounters,withs 0 :=
(ε, κ0, ρ0). Each eventainduces a transition(s, a, s′)∈R
that appendsatoτand updatesκandρ. An agentsession
is a finite paths0
a1
− → · · ·
ak
− →sk, with traceτ=a 1 · · ·ak.
A context key records a fact carried across events, such as
the caller’s identity or a document’s source, and a counter
tracks a cumulative quantity, such as the tokens consumed.
3.2 Finite-Trace LTL (LTLf)
LTL(Pnueli1977)extendspropositionallogictoreasonover
infinitesequencesofpropositionalinterpretations,ortraces.
LTLf (DeGiacomoandVardi2013)restrictsthislogictofi-
nitetraces.LetAPbeafinitesetofatomicpropositions.The
class of LTLf formulae overAPis defined by the grammar
φ::=P| ¬φ|φ∧φ ′ |X φ|F φ|G φ|φ U φ ′,where
P∈APis an AP andφ ′ is an LTLf formula, with tem-
poral operatorsX(next),F(eventually),G(always), andU
(until). Each LTLf formula compiles to an equivalent DFA
thatacceptsexactlythetracessatisfyingit(DeGiacomoand
Vardi 2013), which is the canonical monitor construction of
runtime verification (Bauer, Leucker, and Schallhart 2011;
Leucker and Schallhart 2009).
When an atomic predicate is used to compare an arith-
metic quantity read from the session states, such as a call
count or token total accumulated inρ, or an argument value
latched intoκ, against a bound, then it is better captured by
alinear-arithmeticconstraintthanbyaplainproposition.An
LTLf formula over such atoms is then taken modulo linear
arithmetic,i.e.,arithmeticLTL f (ALTLf)(Fellietal.2023),
an instance of LTLf modulo theories (Geatti, Gianola, and
Gigante 2022).ContrAgentevaluatesevery atompointwise,
i.e.,itstruthvalueateacheventiscomputedfromthecurrent
eventaand the session states.

3.3 Assume-Guarantee (A/G) Contracts
LetMdenote a component, i.e., an element of a system,
characterized by a set of variablesVc and a set of behaviors
JMKoverV c. A contractCformally captures a set of spec-
ifications forMusing a tripleC= (V c, A, G)(Benveniste
et al. 2018), whereAandGare sets of behaviors overV c.
Ais the assumptions on the environment ofMwhileGis
the guarantees provided byM, given that the assumptions
are satisfied. We say thatMis a valid implementation ofC,
i.e.,M|=C, if all the behaviors ofMare included in the
guarantees given the assumptions ofC, i.e.,JMK⊆G∪ A.
We say that componentEc is a valid environment ofCif
all the behaviors ofEc are contained in the assumptions of
C. A contract isconsistentif and only if there exists a valid
implementation,i.e.,G∪ A̸=∅,anditiscompatibleifthere
exists a valid environmentEc, i.e.,A̸=∅.
ContrAgentformalizescontractsovertheagent’stool-call
trace: the component is the agent, whose behaviorsJMKare
the tool-call traces it can produce (Def. 1), and the variables
Vc are the setAP. At runtime, a session exposes a single
behavior of this component, andContrAgentevaluates the
observed traceτby the three-valued valuation below.
Definition 2 (Runtime contract valuation)A contractC
is a pair(A, G)of ALTLf properties overAP. Against a
concrete traceτ, its valuation takes one of three values,
namedIDLE(1),ACTIVE(e), andF AIL(0), ordered as
0≤e≤1, following the multi-valued verdicts of runtime
verification (Bauer, Leucker, and Schallhart 2006):
J(A, G)K(τ) =



1, τ|= A,
e, τ|=A∧G,
0, τ|=A∧ G.
(1)
3.4 Agent Trajectory Supervision
An execution monitor can be used to halt a run at the
first policy-violating action, thus enforcing a safety prop-
erty(Schneider2000).Weadaptthisapproachtotheagent’s
tool-call trace.
Problem 1 (Agent Trajectory Supervision)Agent trajec-
tory supervision is the problem of monitoring an agent’s
tool-calltraceτagainstasetofcontractsC={C 1, . . . , Cn}
withC i = (A i, Gi). We define the monitor verdictv(τ) =
venv(τ), vag(τ)

is defined by the join and the meet of the
contract valuations as follows:
venv(τ) = W iJ(Ai, Gi)K(τ),(2)
vag(τ) = V iJ(Ai, Gi)K(τ).(3)
The environment is not valid for at least one contract if and
only ifvenv(τ) = 1; the agent violates at least one contract
if and only ifvag(τ) = 0. Therefore, trajectory supervision
provides deterministic maps overCas follows:
•Inonline enforcement, it provides a mapσ: Σ ∗ →
{pass,block}that, on the trace, returnsblockat the first
prefixτ k =a 1 · · ·ak withv(τ k)̸= (e, e)andpassat
every earlier prefix;
•Inoffline evaluation, it provides a mapµ: Σ ∗ →
{0, e,1}2 withµ(τ) =v(τ), the monitor verdict.
Type Predicate Meaning
Structural
Call(T)toolTis invoked
ArgHas(T, f, p)argumentfofTmatches patternp
OutHas(T, p)result ofTmatches patternp
Said(p),In(p)model output / input matches patternp
Match(f, k)argument fieldfequals context valuek
Subset(f, S)values in fieldflie within setS
Flow(s, d)data from sourcesreaches sinkd
Perm(P)caller holds permissionP
Numeric
Cnt(T)current number ofTcalls
Num(T, f)numeric value of argument fieldf
Tokcumulative tokens consumed
Table 1:ContrAgent’s interaction predicates (subset; full
vocabularyinAppendixA).Tisatool,fanargumentfield,
paregular-expressionorliteral-valuepattern,Papermission
set,San allowed-value set,s, dargument or result fields as
sourceandsink,andkacontextvalue.Numericrowslistthe
quantityθ; the predicate isθ ▷ ◁ cwith boundc.
ContrAgentsolves this problem using one checker per
contract, executed online forσand replayed offline forµ, as
shown in §5.2.
4 Agent Contracts
We introduce theinteraction predicate, the atomic proposi-
tion from which agent contracts are built. In the following,
weuse⊤and⊥todenotetheBooleanvaluestrueandfalse,
respectively.
Definition 3 (Interaction Predicate)We define aninterac-
tion predicateas a predicateP(s, a, c)over a session state
s, a tool-call eventa∈Σ(Def. 1), and a parameterc. Its
truth value,⊤or⊥, is a deterministic function ofs,a, and
c, evaluated by the monitor at each event (§5.1).
The parametercinstantiates a predicate with, for exam-
ple, a numeric bound or a string pattern. Given a session,
we define a set of interaction predicates monitored at run-
time.Theycoverawiderangeofpropertiesoverthetool-call
interface: predicates over the call and the session state are
evaluated at call events, and predicates over the result (e.g.,
OutHas) at return events. We categorize the predicates into
two families, as shown in Table 1.
Structural predicates.Astructuralpredicate is a deter-
ministicBooleantestofadiscretecondition:thepresenceor
absence of an event (e.g., a tool firing,Call, or a data flow,
Flow),orapattern,equality,ormembershipmatchonafield
(e.g.,ArgHas,Match), with no model in the loop.
Numericpredicates.Weextendthestructuralfamilywith
astateful, numericfamily that tracks cumulative quantities
over the session, such as counts and totals. Anumericpred-
icate has the formθ(s, a)▷ ◁ c, with▷ ◁∈ {≤, <,≥, >,=},
whereθextractsaquantityfromthecurrenteventaandstate
s, such as a count, a total, or an argument’s value, andcis a
constant bound. The predicate holds exactly when the com-
parison holds,P(s, a, c) =

θ(s, a)▷ ◁ c

, where[·]is the

Temporal Logic (ALTLf)
operatorsG F X Ulift predicates over the trajectory
¬Call(refund)UCall(approve)∧G

Call(refund)→
Num(refund,amount)≤42

Structural Predicates
presence or pattern match
Call(refund) =⊤
Match(account,appr) =⊤
Call(approve) =⊤
Numeric Predicates
threshold over accumulators
Cnt(refund) = 3≤5
Tok= 1200≤2000
amount= 50>42
tool-call eventa= (refund,{amount: 50, . . .})
extract / accumulate
Interaction PredicatesV
Figure 2: One tool-call event grounded into structural and
numeric predicates, then lifted by the ALTLf layer.
Iverson bracket, as inCnt(T)≤N. The monitor maintains
each accumulated quantity in acounter, one entry of the
vectorρof Def. 1, updated deterministically at each event.
Such arithmetic-constraint atoms are what lift a contract’s
logic from propositional LTLf to its arithmetic extension
ALTLf (Felli et al. 2023).
With the LTLf operators, we use interaction predicates to
define agent contracts for trajectory supervision as follows.
Definition 4 (Agent Contract)Anagentcontractisatriple
C= (V, φA, φG), where:
1.V=V ag ∪V env is a finite set of interaction predicates
(Def. 3), the AP of the contract’s formulas, whereVag
collectsthepredicatesdecidedbytheagent’sownactions
andV env those decided by its environment.
2. The assumptionφA is an ALTLf formula overVenv, and
the guaranteeφ G is an ALTLf formula overV, both
according to the grammar of §3.
The partition ofVmirrors the distinction between con-
trolled and uncontrolled variables in contract-based de-
sign(Benvenisteetal.2008).Forexample,Call,ArgHas,and
Cnttrack the tool calls that the agent itself issues (Def. 1),
their arguments, and the counts derived from them, so they
belong toVag.OutHas,In, andPermtrack tool results, user
input, and granted permissions, so they belong toVenv. The
actions of other agents also belong to the environment. Se-
mantically, an agent’s session satisfies the contract when its
trace satisfiesφ A →φ G, with(φ A, φG)instantiating the
pair(A, G)of Def. 2. Such contracts capture a wide range
oftrajectorypropertiesoverthetool-callinterface,including
order-, history-, and count-dependent ones (Appendix B).
Example 1Consider a contract whose guarantee, shown
in Figure 2, isφ G =¬Call(refund)UCall(approve)∧
G

Call(refund)→Num(refund,amount)≤42

, where
$42 is the approved amount recorded by an earlierapprove
call. Take the call eventa= (refund,{amount: 50, . . .}).
The structural predicates hold,Call(refund) =⊤and
Match(account,appr) =⊤, sinceapprovewas called
first and the account matches. The numeric predicate
Num(refund,amount)≤42evaluates to⊥atamount=
50, so the guarantee, and with it the contract, falls toF AIL.
5 TheContrAgentFramework
Giventheagentcontracts,asdefinedin§4,ContrAgentpro-
ceeds in two stages. In theofflinestage (§5.1), it abstracts
requirement artifacts into contracts and translates each con-
tract into a deterministic monitor, the DFA associated with
its ALTLf formula. In theonlinestage (§5.2), it supervises
theagentbyadvancingeverymonitoroverthetool-calltrace
and gating each call on the joint verdict (Problem 1).
5.1 Contract Compilation
Contractcompilationextractscontractsfromrequirementar-
tifacts (e.g., natural language, policy documents, recorded
traces) into ALTLf formulas over the interaction predicates
of §4, then compiles them into DFAs (Figure 3). The two
steps are described next.
Contract formulation.Besides manually written ALTLf
contracts, we support translating natural-language require-
mentsandextractingrulesfrompolicydocuments.Following
alift-then-grounddecomposition(Liuetal.2023),theLLM
firstliftseach utterance to an ALTL f formula with place-
holder leaves, and a deterministic step thengroundsthose
placeholderstointeractionpredicatesfromTable1,yielding
the closed formula. The LLM thus fills templates over the
fixed vocabulary of Table 1 (Wang et al. 2023) with a few
prompt examples. Each formula is translated back to natural
language for human review (Cosler et al. 2023).
Automaton construction.By the standard LTLf-to-DFA
construction (De Giacomo and Vardi 2013), every contract
formula overVcompiles to a DFA whose alphabet is the
set2 V of predicate valuations. The DFA reads a trace one
event at a time, taking a transition on the predicate valua-
tion at that event, and accepts exactly the finite traces that
satisfytheformula.Wecallgroundingthedeterministicstep
that evaluates each predicate on the current event and the
counters, producing the valuation read by the DFA. For a
numeric predicate, grounding evaluates the arithmetic con-
straintθ(s, a)▷ ◁ cagainst the session’s counters, and the
DFA construction stays standard. The counter state is read
onlyduringgroundingandisnotencodedintheDFA,which
keeps it finite. A contract carries two such formulas, the as-
sumptionφ A and the guaranteeφG, so each compiles to its
own DFA. We store the two DFAs as one checker corre-
sponding to the contract for agent supervision.
Contract library.The compiled checkers form acontract
librarythatContrAgentloadsatruntime.Becauseacontract
iswrittenoverinteractionpredicatesratherthananymodel’s
internals, the library is portable: the same checkers apply
unchanged across agents and LLM models that share a tool
interface, so a domain’s policies transfer between models.
For each contract,ContrAgentfirst checks consistency and
compatibility, and also checks the loaded library isconflict-
free: the conjunctionV i(Ai ∧G i)of its ALTLf formulas is satisfiable. When it is not, we extract a minimal unsatisfi-
able core (Roveri et al. 2024; Ielo et al. 2026) to locate the
contracts to repair.

Figure3:TheContrAgentframework:authoringinputscompileonceintoacontractchecker(top),readonlinetoblockthefirst
violating call (bottom left) and offline to score a recorded trace (bottom right).
5.2 Contract-Based Supervision
At each event,ContrAgentevaluates every interaction pred-
icate and advances each loaded contract’s two DFAs on the
resultingvaluation.Thetworunsdecidethecontract’svalue
in Def. 2, and the values of all loaded contracts give the
verdictv(τ)of Problem 1.
Becauseeachcontractisasingle(A, G)paircheckedinde-
pendently,aviolationisfullytraceable:itnamesthecontract
that violated and the event that triggered it, so an operator
cantellwhetherthefaultliesintheagentflow,initsenviron-
ment,orinacontractthatistoorestrictive,andrepairthelast
byrelaxingtheguaranteeorweakeningtheassumption.This
modularity also lets the system enforce multiple policies at
once, without merging them into a monolithic formula.
Runtime enforcement.At runtime,ContrAgentrealizes
the enforcement mapσof Problem 1. As shown in Figure 3,
before the tool executes, it advances every loaded contract
andreturnsblockatthefirsteventwhoseverdictisnot(e, e).
Every event is checked when it enters the trace and before
it takes effect (Def. 1), so the verdict is computed before
a call executes and before an incoming event reaches the
agent. A call that would falsify a guarantee is rejected, and
a return or input event that would falsify an assumption is
suppressed. Neither event is recorded, so the session contin-
ues from the last prefix whose verdict was(e, e). The first
keeps the agent a valid implementation of the contract and
the second keeps its environment a valid environment, as in
bidirectional runtime enforcement (Aceto et al. 2021). The
checkisincremental:ratherthansynthesizingeachcontract’s
DFAs in full,ContrAgentkeeps a residual formula and pro-
gresses it one event at a time (Roşu and Havelund 2005),
so the per-event cost isO(|C|), whereCis the set of loaded
contracts, independent of the trace length. Supervision thus
scales to long horizons.
When the blocked event is a call, the enforcement action
is decided by the strategy carried by the violated contract:
blockthe call (the default),redirectit to a safe alternative,
orescalatetoahuman.Theoutcomereturnstothemodelas
a structured message: the identifier of the contract involved,
a short explanation, and, where it applies, the suggested re-
placement or required next action, so the agent can steer
its trajectory back into the safe region. For example, a con-
tract that forbids issuing a refund before approval can return
a message like “the actionissue_refundwas rejected:
callcheck_policyfirst”.
Prompting for a requested action letsContrAgentact
proactively, on a satisfied trigger rather than on a violation.
Consider a prescriptive guaranteeG(trig→Xtool); when
thetriggertrigissatisfiedandgetspass,afeedbackmessage
canasktheagenttocalltherequiredtoolnext.Anunbounded
liveness guaranteeG(trig→Fresp)cannot be refuted by
any finite prefix: aftertrigis satisfied, it stays pending until
respoccurs. At the end of the agent session,ContrAgent
surfaces every still-pending guarantee as a feedback mes-
sage asking the agent to performresp, and a guarantee left
unsatisfied collapses toF AIL.
Offlineevaluation.Contractsalsoserveasadeterministic
evaluation engine for recorded traces:µ: Σ∗ → {0, e,1}2

of Problem 1, as shown in Figure 3.ContrAgentreplays
a recorded trace and returns its end-of-trace verdictµ(τ) =
v(τ)insteadofgatingactions,onevaluefortheagentandone
for its environment. The difference from enforcement is that
thetraceisfixed,sothereisnointervention;andbecauseeach
vi dependsonlyonthetrace,theofflinereplayandtheonline
monitor traverse the same states and agree on the verdict at
everyprefix.Whenmanytracesarecheckedagainstthesame
contracts, the DFAs are built once and reused, turning each
event into a single table lookup (O(1)). Offline evaluation is
thus deterministic and reproducible: the same trace always
yields the same verdict and per-contract attribution, not a
single pass/fail rate.
6 Evaluation
Our implementation1 is in Python 3.12; it exports contract
libraries to CHASE (Nuzzo et al. 2018) for design-time
contract analysis, and usesmus2muc(Ielo et al. 2026) for
conflict-coreextractionandZ3(deMouraandBjørner2008)
for the numeric consistency check. The contract library is
built with an LLM following the formulation pipeline of
§5.1, over the interaction predicates of Table 1. Integration
hooks intercept each event and ground it deterministically
through pattern matches and counter updates. Latency mea-
surements reported below were taken on an Apple M4 Pro
laptop (24GB).
Benchmarks.We evaluateContrAgenton four bench-
marks, each isolating one claim. The enforcement role is
tested by SOPBench (Li et al. 2025) (§6.1) and Agent-
Dojo (Debenedetti et al. 2024) (§6.2); the evaluation role
by R-Judge (Yuan et al. 2024) (§6.3) andτ2-bench (Barres
et al. 2025) (§6.4).
6.1 Standard Operating Procedure Enforcement
SOPBench (Li et al. 2025) evaluates whether a language
agent follows an explicit standard operating procedure
(SOP)acrosssevencustomer-servicedomains(bank,DMV,
healthcare,hotel,library,university,online market),
whereeachtaskprovidesaconstraintgraph,numericthresh-
olds, an initial database, and a label indicating whether the
policypermitsthegoal.WecomparedContrAgentwiththree
baselines:(1)thebasemodelwithnoSOP,(2)thebasemodel
prompted with the SOP, and (3) a second LLM that judges
each call against the SOP. We reportsuccessandsafetymet-
rics, representing goal completion on tasks the SOP permits
and correct blocking on tasks the SOP forbids, respectively.
We build each domain’s agent contracts from its public
SOP, compiling the SOP’s gate/chain tree. As shown in Ta-
ble2,ContrAgentenforcementholdssuccessatthebaselevel
whileraisingsafetyfrom32%to98%,aboveprompt’s94%.
Prompting and LLM-guard also achieve high safety (94%
and98%),butreducemeansuccessto64%and24%,respec-
tively, because of over-blocking. Both residual gaps trace to
the agent rather than the enforcement layer: inhealthcare
it fails to retry after a block, and inuniversityit makes a
1https://github.com/yfxiao16/ContrAgent
domain(Su./Sf.)base prompt LLM-grdContrAgent
bank70/65 58/100 42/10070/100
DMV100/60 72/98 20/100100/100
healthcare90/48 52/95 20/10083/100
hotel100/0 30/98 15/100100/100
library80/25 48/95 22/9880/100
university100/8 92/82 33/88100/83
online mkt.100/20 92/90 15/98100/100
mean91/32 64/94 24/9890/98
avg. runtime1.96s+0.905s+1.34s+0.135s
Table 2: SOPBench results (gemini-2.5-flash, 40
tasks/domain);eachcellissuccess(Su.)/safety(Sf.)%.avg.
runtime: thebasecell is its median runtime per task; the
other cells are the medianextratime over base.
1–2 3–4 5–6 7–9 10+
0
25
50
75
100
# SOP constraints
success %
base prompt LLM-grd ContrAgent
1–2 3–4 5–6 7–9 10+
# SOP constraints
safety %
Figure4:SOPBenchsuccess(left)andsafety(right)vs.SOP
constraint count, pooled over seven domains.
permittedchangetoatargetthebenchmark’soutcome-based
scoring cannot distinguish from the forbidden one.
TheruntimecostofContrAgentislowerthanbothprompt
andLLM-guard,sinceitneitherincreasesthepromptlength
norcallsasecondmodeloneveryaction.Eachentryisamean
over three seeded trials;ContrAgent’s enforcement is stable
across trials, with per-domain deviation≤0.4percentage
points(pp),versus2to4ppforthemodel-drivenconditions.
Model-agnostic supervision.With the same contract li-
brary, ongemini-2.5-flash-lite, where the un-
guarded base stays at27%, prompt’s mean safety collapses
from94%to45%, whereasContrAgent’s enforced safety
is unchanged at98%, because the verdict does not depend
on the agent’s model. Moreover, replaying the same con-
tractlibraryoverSOPBenchtracesfrom23basemodels,the
false-positiverateonsafetracesstaysbelow1%for19of23
models (max4.5%, Llama-3.1-8B), even as the per-model
violation rate varies widely with capability (Appendix C).
SOP constraint scaling.Binning tasks by the number of
SOP constraints (which run from1to17; pooled over the
sevendomains)exposesthesuccess/safetytradeoffthatasin-
glestrategyhides.AsshowninFigure4,withthenumberof
constraints increasing, prompting increasingly over-refuses:
its success on permitted tasks collapses from87%to18%
in the10+bin, while the unguarded base’s safety collapses
from79%to0%. The LLM-guard keeps safety high, but

base no detector trace-learned
0.1 1 10
gemini-2-flash
gemini-2-flash-exp
gemini-1.5-pro-2
llama-3-70b
claude-3-sonnet
gpt-4o-mini
gemini-1.5-pro
gpt-4-turbo
gpt-4o
claude-3.5-sonnet
gpt-4-0125
0.1 1 10
claude-3.5-sonnet-2
meta-secalign-70b
command-r
gemini-1.5-flash-2
command-r-plus
claude-3.7-sonnet
claude-3-haiku
gpt-3.5-turbo
claude-3-opus
gemini-1.5-flash
llama-3.3-70b
Prompt-injection attack-success rate (%, log scale)
Figure5:Indirectprompt-injectionpreventionacross22LLMsonAgentDojo;left
and right are the higher- and lower-ASR halves.
pass4 joint4
0 20 40 60
o4-mini
GPT-4.1-mini
GPT-4.1
Claude 3.7
o4-mini
GPT-4.1-mini
GPT-4.1
Claude 3.7
o4-mini
GPT-4.1-mini
GPT-4.1
Claude 3.7
Retail
Airline
Telecom
Task-level success rate (%,k= 4)
Figure6:Theτ 2-benchproceduralreliabil-
ity across three domains and four models.
with steep success reduction.ContrAgentholds success at
77%or above and safety at89%or above across all bins,
andthegapwidensastheconstraintcountgrows.Exactper-
bin values and the weak-model robustness breakdown are in
Appendix D.
6.2 Indirect Prompt Injection Prevention
AgentDojo (Debenedetti et al. 2024) embeds attacker text
inside tool outputs (email bodies, calendar entries, search
results) and measures whether the agent is steered into an
unsafeaction.ContrAgentpreventsindirectpromptinjection
byfilteringtooloutputsandblockinganysubsequentcallthat
would violate the contract, regardless of whether the agent
was tricked into issuing it. The contract library is built from
the task and environment specifications of AgentDojo’s four
suites, without knowledge of the attacks. It tags any value
carried in by a tool output as untrusted, and blocks a side-
effecting call whose target is both untrusted-introduced and
outside the task’s legitimate set.
Figure 5 reports three results per model. The baseline re-
sultsarefromAgentDojo’spublishednumbers(Debenedetti
et al. 2024). We callno-detectorthe setting in which no
component flags the injected text, so that a value counts as
untrusted whenever a tool output introduces it and the user
hasnotnamedit.Inthissetting,thelibraryreducesthepooled
attack success rate (ASR) from18.0%to5.3%at0.8%util-
ity false positive (FP). Contracts can also be mined from the
recordedtracesoftheattacksthemselves(attackerrecipients,
unsafeactions,andtheinjectedtextastheuntrustedsource),
whichwecalltrace-learnedcontracts.Thislowersthepooled
ASR to1.7%at0.3%FP. The attacksContrAgentmisses
fall into two kinds. Most (82%) issue no malicious tool call
at all, e.g., denial-of-service injections that only divert the
agent or text-response attacks answered in the agent’s own
reply, outside what a tool-call shield can do. The remaining
18%arepromptinjectionsthatsteertheagentintoatoolcall
whose arguments are themselves legitimate values, leaving
the deterministic guard no untrusted target to flag.
Table 3 comparesContrAgentwith the defenses bundled
withAgentDojoongpt-4ounderitsmaininjectionattack.
Only theContrAgentrows are measured here; the baseline
rates are AgentDojo’s published numbers, and every util-
Defense Type ASR Utility Overhead
No defense raw agent 47.7% 72.6% 0
spotlighting prompt-side 41.7% 75.0% prompt
repeat_user_prompt prompt-side 27.8% 85.5% prompt
ContrAgent(ND)data-flow11.1% 71.8% 0.16 ms
pi_detector classifier 7.95% 41.9%∼50ms
tool_filter LLM prune 6.84% 71.8%∼500ms
LlamaFirewall guardrail 1.75% n/a∼100ms
ContrAgent(TL)data-flow0.79% 72.6% 0.16 ms
Table 3: AgentDojo defenses ongpt-4o(ND: no detector,
TL: trace-learned).
ity value is computed from the published runs. Utility is
the fraction of injection-free tasks completed. Overhead is
the per-call runtime added by a defense, and prompt-side
defenses add prompt text rather than a call.ContrAgentre-
plays the recorded runs, so its utility cannot exceed that of
the undefended agent. With no detector,ContrAgentlow-
ers the ASR from47.7%to11.1%and completes71.8%of
the injection-free tasks, one task fewer than the undefended
agent. The classifier reaches7.95%but completes41.9%of
thetasks.Thetrace-learnedvariantreaches0.79%attheutil-
ity of the undefended agent. Both variants add0.16ms per
call,against50to500msfortheclassifierandtheLLMfilter,
and run no model. The per-workload latency breakdown is
in Appendix E.
6.3 Agent Safety Risk Evaluation
R-Judge (Yuan et al. 2024) tests whether an evaluator can
detect unsafe agent behaviorpost hocacross ten operational
risk types in571multi-turn agent records (301unsafe /270
safe).ContractscomefromR-Judge’srisktaxonomy,apolicy
document(§5.1).ContrAgentreachesanaverageF 1scoreof
91.8%(97.0%precision,87.0%recall)acrossmultipletrials.
ThisexceedsGPT-4o(74.4%)andtheR-Judgehumanbase-
line (≈89%). AgentAuditor (Luo et al. 2025) outperforms
ourmethodatthecostofaGemini-2judgewithretrievalover
an experiential memory. The records we miss are semantic
ratherthanprocedural,outsidewhatadeterministictool-call
check can decide.

6.4 Procedural Violation and Outcome Scoring
τ 2-bench (Barres et al. 2025) runs customer-service agents
throughmulti-turndual-controlconversationsagainstawrit-
tenpolicydocumentinthreedomains.Itsnativepass k met-
ricisoutcome-only(finaldatabasestate).AgentPex(Sharma,
Barke, and Zorn 2026) showed83%of reward-1.0Claude
traces still violate a procedural rule. With contract libraries
builtfromthepolicydocuments,ContrAgentmeasurespro-
ceduralcompliancedeterministically,whileLLMjudgescan
only approximate it. We report ajointk metric that com-
bines outcome and zero contract violations acrosskretries.
Figure 6 exposes the gap this creates: across the4,464-trace
matrix Claude 3.7 reaches an outcomepass4 of25–60%
yet ajoint 4 of0%in all three domains, i.e., no task is
completedreliablywithoutatleastoneproceduralviolation,
a form of reward hacking. Per-cell values for every domain
and model are in Appendix F.
Limitations.ContrAgentenforces only what the tool-call
structureexposes,andfree-formsemanticharmsneedasepa-
ratecontent-levelcheck.Inthispaper,thelibraryisinspected
byhumansbeforeuse;autoformalizationofnatural-language
policies is out of the scope of this work and left as a future
direction. The counters that ground numeric predicates (§4)
trusttheframeworktoreporteventsfaithfully,anddefending
this observation channel itself is beyond our scope.
7 Conclusion
We presentedContrAgent, a contract-based framework that
formalizes trajectory-level specifications of large language
model (LLM) agents as assume-guarantee (A/G) contracts
over checkable tool-call predicates, expressed in arithmetic
linear temporal logic on finite traces (ALTLf), and com-
piles each into a deterministic finite automaton (DFA) for
online enforcement and offline evaluation. The contract li-
brary acts as a model-agnostic knowledge base of agent
policies. We illustrated the effectiveness of our approach
onfourbenchmarksspanningbothroles,whereContrAgent
matchesLLM-judgeandguardrailbaselineswhileproducing
deterministic, reproducible verdicts at orders of magnitude
lower per-call latency. Future work includes compiling con-
tractsintorewardmachinesforpost-trainingandconstrained
decoding, and investigating contract-based decomposition
mechanisms for multi-agent systems.
References
Aceto, L.; Cassar, I.; Francalanza, A.; and Ingólfsdóttir, A.
2021. OnBidirectionalRuntimeEnforcement. InProc.For-
mal Techniques for Distributed Objects, Components, and
Systems (FORTE), LNCS. Springer.
Anthropic. 2024. Introducing the Model Context Protocol.
Anthropic; open protocol specification.
Baier,C.;andKatoen,J.-P.2008.PrinciplesofModelCheck-
ing. Cambridge, MA: MIT Press.
Barres, V.; Dong, H.; Ray, S.; Si, X.; et al. 2025.τ2-Bench:
Evaluating Conversational Agents in a Dual-Control Envi-
ronment. ArXiv preprint arXiv:2506.07982.
Bauer,A.;Leucker,M.;andSchallhart,C.2006. Monitoring
of Real-Time Properties. InProc. Foundations of Software
Technology and Theoretical Computer Science (FSTTCS),
volume 4337 ofLecture Notes in Computer Science, 260–
272. Springer.
Bauer, A.; Leucker, M.; and Schallhart, C. 2011. Runtime
Verification for LTL and TLTL.ACM Transactions on Soft-
ware Engineering and Methodology (TOSEM), 20(4): 14:1–
14:64.
Benveniste,A.;Caillaud,B.;Ferrari,A.;Mangeruca,L.;etal.
2008. MultipleViewpointContract-BasedSpecificationand
Design. InProc. Formal Methods for Components and Ob-
jects (FMCO), volume 5382 ofLNCS, 200–225. Springer.
Benveniste, A.; Caillaud, B.; Nickovic, D.; Passerone, R.;
et al. 2018. Contracts for System Design.Foundations and
TrendsinElectronic DesignAutomation,12(2–3):124–400.
Bhardwaj, V. P. 2026. Agent Behavioral Contracts: For-
mal Specification and Runtime Enforcement for Reliable
Autonomous AI Agents. ArXiv preprint arXiv:2602.22302.
Chase, H. 2022. LangChain: Building Applications with
LLMs through Composability. Open-source software.
Chen, H.; and Goldfarb-Tarrant, S. 2025. Safer or Luckier?
LLMs as Safety Evaluators Are Not Robust to Artifacts. In
Proc. Annual Meeting of the Association for Computational
Linguistics (ACL), 19750–19766.
Chen,Z.;Kang,M.;andLi,B.2025. ShieldAgent:Shielding
Agents via Verifiable Safety Policy Reasoning. InProc.
International Conference on Machine Learning (ICML).
Cosler, M.; Hahn, C.; Mendoza, D.; Schmitt, F.; et al. 2023.
nl2spec:InteractivelyTranslatingUnstructuredNaturalLan-
guage to Temporal Logics with Large Language Models. In
Proc. Computer Aided Verification (CAV), volume 13965 of
Lecture Notes in Computer Science, 383–396. Springer.
Costa, M.; Köpf, B.; Kolluri, A.; Paverd, A.; et al. 2025.
Securing AI Agents with Information-Flow Control. ArXiv
preprint arXiv:2505.23643.
De Giacomo, G.; and Vardi, M. Y. 2013. Linear Temporal
Logic and Linear Dynamic Logic on Finite Traces. InProc.
International Joint Conference on Artificial Intelligence (IJ-
CAI), 854–860.
de Moura, L.; and Bjørner, N. 2008. Z3: An Efficient SMT
Solver. InProc. Tools and Algorithms for the Construction
and Analysis of Systems (TACAS), volume 4963 ofLecture
Notes in Computer Science, 337–340. Springer.
Debenedetti,E.;Shumailov,I.;Fan,T.;Hayes,J.;etal.2025.
Defeating Prompt Injections by Design. ArXiv preprint
arXiv:2503.18813.
Debenedetti, E.; Zhang, J.; Balunović, M.; Beurer-Kellner,
L.;etal.2024. AgentDojo:ADynamicEnvironmenttoEval-
uatePromptInjectionAttacksandDefensesforLLMAgents.
InProc. Conference on Neural Information Processing Sys-
tems (NeurIPS), Datasets and Benchmarks Track.
Felli,P.;Montali,M.;Patrizi,F.;andWinkler,S.2023. Mon-
itoring Arithmetic Temporal Properties on Finite Traces. In
Proc. AAAI Conference on Artificial Intelligence (AAAI),
6346–6354. AAAI Press.

Geatti, L.; Gianola, A.; and Gigante, N. 2022. Linear Tem-
poral Logic Modulo Theories over Finite Traces. InProc.
International Joint Conference on Artificial Intelligence (IJ-
CAI), 2641–2647. ijcai.org.
Ielo, A.; Mazzotta, G.; Peñaloza, R.; and Ricca, F. 2026.
Enumerating Minimal Unsatisfiable Cores of LTLf Formu-
lae. InProc. AAAI Conference on Artificial Intelligence
(AAAI), 19160–19168. AAAI Press.
Inan,H.;Upasani,K.;Chi,J.;Rungta,R.;etal.2023. Llama
Guard: LLM-based Input-Output Safeguard for Human-AI
Conversations. ArXiv preprint arXiv:2312.06674.
Jimenez, C. E.; Yang, J.; Wettig, A.; Yao, S.; et al. 2024.
SWE-bench: Can Language Models Resolve Real-World
GitHubIssues? InProc.InternationalConferenceonLearn-
ing Representations (ICLR).
Kamath,A.;Zhang,S.;Xu,C.;Ugare,S.;etal.2025. Enforc-
ing Temporal Constraints for LLM Agents. ArXiv preprint
arXiv:2512.23738.
Leucker, M.; and Schallhart, C. 2009. A Brief Account of
Runtime Verification.The Journal of Logic and Algebraic
Programming, 78(5): 293–303.
Li, Z.; Huang, S.; Wang, J.; Zhang, N.; et al. 2025. SOP-
Bench: Evaluating Language Agents at Following Stan-
dard Operating Procedures and Constraints. ArXiv preprint
arXiv:2503.08669.
Liu,J.X.;Yang,Z.;Idrees,I.;Liang,S.;etal.2023. Ground-
ing Complex Natural Language Commands for Temporal
Tasks in Unseen Environments. InProc. Conference on
Robot Learning (CoRL). System name “Lang2LTL”.
Luo, H.; Dai, S.; Ni, C.; Li, X.; et al. 2025. AgentAudi-
tor: Human-Level Safety and Security Evaluation for LLM
Agents. InProc.ConferenceonNeuralInformationProcess-
ing Systems (NeurIPS).
Miculicich, L.; Parmar, M.; Palangi, H.; Dvijotham,
K. D.; et al. 2025. VeriGuard: Enhancing LLM Agent
Safety via Verified Code Generation. ArXiv preprint
arXiv:2510.05156.
Nous Research. 2026. Hermes Agent: A Self-Improving
Open-Source Agent Framework. Open-source software.
Nuzzo, P.; Lora, M.; Feldman, Y. A.; and Sangiovanni-
Vincentelli, A. L. 2018. CHASE: Contract-based require-
mentengineeringforcyber-physicalsystemdesign. InProc.
Design, Automation & Test in Europe Conference (DATE),
839–844.
Nuzzo, P.; Sangiovanni-Vincentelli, A. L.; Bresolin, D.;
Geretti, L.; et al. 2015. A Platform-Based Design Method-
ology with Contracts and Related Tools for the Design of
Cyber-PhysicalSystems.ProceedingsoftheIEEE,103(11):
2104–2132.
OpenClaw Project. 2026. OpenClaw: An Open-Source Per-
sonal AI Agent. Open-source software.
Palumbo, N.; Choudhary, S.; Choi, J.; Amir, G.; et al. 2026.
FormalPolicyEnforcementforReal-WorldAgenticSystems.
ArXiv preprint arXiv:2602.16708.
Pnueli,A.1977. TheTemporalLogicofPrograms. InProc.
Annual Symposium on Foundations of Computer Science
(FOCS), 46–57. IEEE.
Roşu, G.; and Havelund, K. 2005. Rewriting-Based Tech-
niques for Runtime Verification.Automated Software Engi-
neering, 12(2): 151–197.
Roveri,M.;DiCiccio,C.;DiFrancescomarino,C.;andGhi-
dini,C.2024.ComputingUnsatisfiableCoresforLTLfSpec-
ifications.Journal of Artificial Intelligence Research, 80:
517–558.
Schneider, F. B. 2000. Enforceable Security Policies.ACM
Transactions on Information and System Security (TISSEC),
3(1): 30–50.
Sharma,R.K.;Barke,S.;andZorn,B.2026. WillfulDisobe-
dience: Automatically Detecting Failures in Agentic Traces.
InProc.ACMConferenceonAIandAgenticSystems(CAIS).
Shi, T.; He, J.; Wang, Z.; Li, H.; et al. 2025. Progent: Se-
curing AI Agents with Privilege Control. ArXiv preprint
arXiv:2504.11703.
Sotiropoulos, J.; Del Rosario, R. F.; Kokuykin, E.; Oakley,
H.; et al. 2025. OWASP Top 10 for LLM Apps & Gen AI
Agentic Security Initiative. OWASP Foundation.
Wang,B.;Wang,Z.;Wang,X.;Cao,Y.;etal.2023.Grammar
Prompting for Domain-Specific Language Generation with
Large Language Models. InProc. Conference on Neural
Information Processing Systems (NeurIPS).
Wang, H.; Poskitt, C. M.; and Sun, J. 2026. AgentSpec:
Customizable Runtime Enforcement for Safe and Reliable
LLMAgents. InProc.IEEE/ACMInternationalConference
on Software Engineering (ICSE).
Wang, H.; Poskitt, C. M.; Wei, J.; and Sun, J. 2025.
ProbGuard: Proactive Runtime Monitoring for LLM Agent
Safety via Probabilistic Prediction. ArXiv preprint
arXiv:2508.00500.
Wen, X.; Mo, W. J.; Xie, Y.; Qi, P.; et al. 2026. Learning
Efficient Guardrails for Compliance. InProc. International
Conference on Machine Learning (ICML).
Wu, Q.; Bansal, G.; Zhang, J.; Wu, Y.; et al. 2024. Auto-
Gen:EnablingNext-GenLLMApplicationsviaMulti-Agent
Conversation. InProc. Conference on Language Modeling
(COLM).
Xiao,Y.;Lutz,C.D.;Castillo-Effen,M.;andNuzzo,P.2026.
Contract-Based Consistency and Availability Analysis for
Distributed Cyber-Physical Systems. InProc. ACM/IEEE
International Conference on Formal Methods and Models
for System Design (MEMOCODE). To appear.
Xiao, Y.; and Nuzzo, P. 2026. Contract-Based Architec-
tureExplorationofCyber-PhysicalSystemsviaSatisfiability
ModuloConvexProgramming. InProc.Design,Automation
& Test in Europe Conference (DATE), 1–7. IEEE.
Xiao, Y.; Oh, C.; Lora, M.; and Nuzzo, P. 2024. Efficient
Exploration of Cyber-Physical System Architectures Using
ContractsandSubgraphIsomorphism. InProc.Design,Au-
tomation & Test in Europe Conference (DATE).

Xu,H.;Li,C.;Ma,X.;Ou,X.;etal.2026. TheEvolutionof
Tool Use in LLM Agents: From Single-Tool Call to Multi-
Tool Orchestration. ArXiv preprint arXiv:2603.22862.
Yang, Z.; Raman, S. S.; Shah, A.; and Tellex, S. 2024. Plug
in the Safety Chip: Enforcing Constraints for LLM-driven
Robot Agents. InProc. IEEE International Conference on
Robotics and Automation (ICRA).
Yao, S.; Zhao, J.; Yu, D.; Du, N.; et al. 2023. ReAct: Syn-
ergizing Reasoning and Acting in Language Models. In
Proc.InternationalConferenceonLearningRepresentations
(ICLR).
Yuan, T.; He, Z.; Dong, L.; Wang, Y.; et al. 2024. R-Judge:
Benchmarking Safety Risk Awareness for LLM Agents. In
Proc. Findings of the Association for Computational Lin-
guistics: EMNLP.
Zheng, L.; Chiang, W.-L.; Sheng, Y.; Zhuang, S.; et al.
2023. JudgingLLM-as-a-JudgewithMT-BenchandChatbot
Arena. InProc.ConferenceonNeuralInformationProcess-
ing Systems (NeurIPS), Datasets and Benchmarks Track.
Zhong, P. Y.; Chen, S.; Wang, R.; McCall, M.; et al. 2025.
RTBAS: Defending LLM Agents Against Prompt Injection
and Privacy Leakage. ArXiv preprint arXiv:2502.08966.
Zhou, S.; Xu, F. F.; Zhu, H.; Zhou, X.; et al. 2024. We-
bArena: A Realistic Web Environment for Building Au-
tonomous Agents. InProc. International Conference on
Learning Representations (ICLR).

A Full Interaction-Predicate Catalogue
Table 4 lists the complete interaction-predicate vocabulary ofContrAgent. The main text (Table 1) shows the representative
subsetthattheexamplesandexperimentsuse;theremainingpredicatesextendthesametwofamiliestomodeloutputs,response
lengths, and delegation depth.Since(e)reads a wall-clock timestamp the framework records with each event; time is an
implementation-level extension and does not enter the formal model of Def. 1.
Type Predicate Meaning
Structural
Call(T)toolTis invoked
ArgHas(T, f, p)argumentfofTmatches patternp
Path(T, P)T’s file paths lie withinP
Subset(f, S)values in fieldflie within setS
OutHas(T, p)result ofTmatches patternp
Said(p),In(p)model output / input matches patternp
Match(f, k)argument fieldfequals context valuek
Ctx(k, v)context keykholds valuev
Flow(s, d)data from sourcesreaches sinkd
Has(f)a produced value contains fieldf
Perm(P)caller holds permissionP
Numeric
Cnt(T)current number ofTcalls
Run(T)length of the current consecutive run ofT
Num(T, f)numeric value of argument fieldf
Len(T, f)character length of argument fieldf
InLencharacter length of the model input
Words,Charsword / character length of the response
Tokcumulative tokens consumed
Depthagent-delegation depth
Since(e)time elapsed since evente
Table 4: Complete interaction-predicate vocabulary ofContrAgent.Tis a tool,fan argument field,pa regular-expression or
literal-valuepattern,Papathorpermissionset,Savalueset,s, dargumentorresultfieldsassourceandsink,andk, vacontext
key/value.
B Temporal Expressiveness
Table 5 lists four temporal property classes that distinguishContrAgent’s trajectory-level enforcement from a stateless, single-
callguard(§4).Foreachweconstructaminimalviolatingtraceinwhicheveryindividualcallislocallylegitimate(thesamecalls
occur in a compliant trace), so the violation is purely temporal.ContrAgent’s DFA catches all four and raises no false positive
on the compliant control; a stateless guard catches none by construction. The fourth class, “after reading untrusted content,
a side-effecting send requires reconfirmation,” is exactly the indirect-prompt-injection contract that drives the AgentDojo and
R-Judge results (§6.2, §6.3).
Property (NL) ALTL f statelessContrAgent
Refundonlyafterapolicycheck
(order)
(¬Call(r)UCall(c))∨G¬Call(r)misscatch
After the AML check, the file is
immutable (history)
G(Call(a)→G¬Call(m))misscatch
At most two transfers (count)G(Cnt(t)≤2)misscatch
Send needs reconfirm after un-
trusted read (injection)
(¬Call(s)UCall(k))∨G¬Call(s)misscatch
Table 5: Temporal expressiveness: each violating trace’s every call is individually legitimate, so the violation is detectable only
fromorder,history,orcount.Astatelessguardcatchesnone;ContrAgent’sDFAcatchesallfour,cleanonthecompliantcontrol.
Tool names in the formulas are abbreviated per row.

C Per-Model Violation Profiles and Grounding Ablation
This appendix expands the grounding and per-model robustness summary in §6.1.
Theresidualgapiscoverage,notgrounding.SOPBench’sdecisivepredicatesarestructural(atoolwascalled,acallreturned
success), read directly off the trace, so grounding is exact by construction. We confirm this with an oracle ablation over5,435
recorded unsafe traces: perfecting the single most influential AP, the goal action’s success flag, moves pooled detection recall
from75.1%to75.4%(a+0.3pp delta). There is essentially no grounding error to remove; the residual∼25%is contract
coverage(§6.1).Oraclegroundingthusmattersforcontentandsemanticsensors(e.g.,R-Judge’ssemanticresidualcases,§6.3),
not for structural enforcement.
Per-model violation profiles.Table 6 profiles the contract library across base models on their recorded traces. The violation
ratetracks capability: the strongest models almost never complete a forbidden action (gpt-5:14unsafe traces in the sample;
o1:3), whereas mid-tier models do so routinely (Claude-3.5:417), a direct, model-specific “willful-disobedience” measure.
ContrAgent’s behaviour on those violations stays stable regardless: recall sits in the54.7–100%band and the dominant family
of caught violations is value/threshold for every model (74–100%of its catches), at<1%false positives, so the supervision
behavior does not depend on the backbone model.
base model recall FPR n uns
gpt-5 100.0% 0.0% 14
o1 100.0% 0.0% 3
gpt-5-mini 92.9% 0.0% 42
gemini-2.0-flash 81.0% 0.5% 420
llama3.1-8b-instruct 79.3% 4.5% 416
gemini-2.0-flash-thinking 79.2% 0.2% 101
llama3.1-70b-instruct 79.0% 1.4% 415
qwen2.5-72b-instruct 78.4% 0.5% 398
o4-mini 78.0% 0.0% 41
qwen2.5-7b-instruct 77.9% 2.5% 408
gpt-4o-mini 77.3% 2.9% 299
gemini-1.5-pro 75.9% 0.7% 332
qwen2.5-14b-instruct 75.8% 0.0% 372
qwen2.5-32b-instruct 75.2% 0.2% 359
claude-3.5-sonnet 74.3% 0.0% 417
gpt-4o 74.2% 0.0% 322
claude-3.7-sonnet 71.7% 0.5% 240
gpt-4.1-mini 66.4% 0.0% 220
claude-3.7-sonnet-thinking 66.1% 0.0% 189
gpt-4.1 63.7% 0.0% 179
o4-mini-high 61.2% 0.2% 80
deepseek-r1 56.2% 0.3% 73
gemini-2.5-flash 54.7% 0.0% 95
Table 6: Per-model violation profiles on SOPBench recorded traces (deterministic,0LLM calls; all23base models).recall=
unsafe caught,FPR= safe wrongly blocked,nuns = sampled unsafe traces. FPR stays below1%for19of23backbones (max
4.5%, llama3.1-8b).
D SOPBench Live Enforcement: Per-Constraint Scaling and Robustness
Table 7 gives the exact per-bin values plotted in Figure 4: SOPBench success (on permitted tasks) and safety (on forbidden
tasks) as a function of the number of SOP constraints, pooled over the seven domains, for the base, prompt, LLM-guard, and
ContrAgent-enforceconditionsongemini-2.5-flash.ContrAgentistheonlyconditionthatstayshighonbothaxesacross
the whole range: prompt’s success collapses from87%to18%as the policy grows, and the unguarded base’s safety collapses
from79%to0%, whileContrAgent-enforce holds success≥77%and safety≥89%throughout, with its safety matching or
exceeding prompt at every bin.
Robustness to a weaker base model.The weak-model result in §6.1 reports the mean over domains; the effect is consistent
across domains. On the weakergemini-2.5-flash-liteagent, prompt’s mean safety falls from94%to45%(the agent
stops reliably reading and obeying the prompted SOP), whereasContrAgent-enforce reproduces its strong-model safety (98%,
unchanged) because the monitor verdict is computed deterministically from the trace, not inferred by the agent. Success drops
for every condition under the weaker agent (enforce mean90→68), confirming that success tracks model capability while
ContrAgent’s safety does not. This confirms the distinction between deterministic and probabilistic supervision. A prompted
SOP’s assurance degrades with the model that carries it, whereas a compiled contract’s does not.

metric condition 1–2 3–4 5–6 7–9 10+
success
base 93 82 84 90 100
prompt 87 62 73 48 18
LLM-grd 68 26 12 12 6
ContrAgent78 77 86 83 100
safety
base 79 44 29 10 0
prompt 100 98 83 90 84
LLM-grd 100 98 100 100 96
ContrAgent100 98 100 93 89
Table 7: Exact per-bin values for Figure 4: SOPBench success (permitted) and safety (forbidden) % vs. SOP constraint count,
pooledoverthesevendomains(gemini-2.5-flash).Asthepolicygrows,prompt’ssuccessandbase’ssafetybothcollapse;
ContrAgent-enforce stays high on both axes.
E Hot-Path Latency Breakdown
Table 8 gives the per-workload before-call latency of the online verifier.
Workload C p50 p95 p99
Synthetic (1 contract) 1 0.0052 – 0.012
SOPBench (per call) 38 to 65 0.097 0.171 0.272
AgentDojo (per call) 8 to 14 0.162 0.620 0.933
R-Judge (per record) 7 0.040 0.085 0.141
τ 2-bench (per call)∼53 0.828 1.500 1.889
Table 8: Hot-path before-call latency (ms) on the incremental online verifier (O(|C|)per call).Cis the number of contracts
evaluated.
F Per-Cellτ 2-bench Reliability Matrix
Figure 6 plots thepass4 andjoint 4 endpoints of theτ 2-bench reliability matrix. Table 9 gives the exact per-cell values,
includingtheintermediateproc-clean 4column(allfourretrieshadzeroContrAgentrulefires).pass 4isthenativeoutcome
metric,joint 4 requires both outcome and procedure-clean on every retry, and thepass4-to-joint4 gap quantifies the loss
of procedural reliability.
Domain Model pass 4 proc-clean4 joint4
retail Claude 3.7 59.60.00.0
GPT-4.1 52.6 78.1 43.9
GPT-4.1-mini 38.6 17.5 9.6
o4-mini 45.6 77.2 34.2
airline Claude 3.7 36.00.00.0
GPT-4.1 40.0 34.0 24.0
GPT-4.1-mini 26.0 14.0 14.0
o4-mini 38.0 48.0 30.0
telecom Claude 3.7 25.40.00.0
GPT-4.1 19.3 4.4 2.6
GPT-4.1-mini 17.5 0.9 0.9
o4-mini 26.3 7.0 7.0
Table 9:τ 2-bench task-level reliability (k= 4, percentages).pass 4 is the native outcome metric (all four retries reach the
correct final state);proc-clean4 requires zeroContrAgentrule fires on all four retries;joint4 requires both. Claude 3.7
reachesproc-clean 4 = 0%in every domain, so itsjoint4 is 0% despite a 25 to 60% outcomepass4.
