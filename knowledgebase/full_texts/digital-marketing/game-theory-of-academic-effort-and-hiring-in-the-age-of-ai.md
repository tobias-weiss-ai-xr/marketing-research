---
title: Game theory of academic effort and hiring in the age of AI
url: https://arxiv.org/abs/2610.35802
category: digital-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Saptarshi Pal
- Peter S. Park
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.35802
pages: 30
chars: 63835
fetched_at: '2026-11-08T13:23:32+00:00'
kb_version: 1
---

# Game theory of academic effort and hiring in the age of AI

Game theory of academic effort and hiring in the age of AI
Saptarshi Pal1 and Peter S. Park2
1Department of Mathematics, Harvard University
2Department of Human Evolutionary Biology, Harvard University
October 27, 2026
Abstract
Many academic disciplines (in particular, mathematics and the theoretical sciences) face
difficult questions about how to adapt their practices to the rise of highly capable artificial
intelligence (AI). Before AI, a well-written research paper with a strong theoretical result
acted as a reliable signal that its authors understood their field in depth. Now that AI is widely
accessible, such signals have become cheaper to produce. As a result, they no longer reliably
sort academics by their level of understanding. This has direct consequences for academic
hiring. The age of AI raises a question for each side of the academic job market. Should an
early-career researcher invest in a deep understanding of their field, or instead use AI to build
a longer resume with many papers? Should a recruiter favor applicants with fewer papers who
pass an interview aimed at probing understanding, or insist on both publication volume and
a pass? In this paper, we develop a game-theoretic model of this two-sided dilemma. We
classify all pure-strategy equilibria that can arise in this game and use learning simulations to
identify the behaviors that populations of applicants and recruiters may learn to adopt. Our
analysis provides a framework for reasoning about how academic hiring can adapt to AI and
for evaluating practices that preserve the value of deep understanding.
1
arXiv:2610.35802v1  [cs.AI]  26 Oct 2026

1 Introduction
Academic publishing serves a dual purpose. First, it provides a lasting record of scientific
discoveries and a means for scholars to share, evaluate, and build upon others’ work. The
second purpose is less explicit. Publications have long served as an indicator of an author’s
understanding of their field. A paper in a respected peer-reviewed journal was generally
taken as evidence of expertise, often without closer examination. This particular aspect of
publishing shapes academic job prospects for early-career academics. Graduate students and
postdocs seek to publish in prestigious journals, motivated both by the scientific value of their
work and by the recognition that publication brings. For an early-career scientist, publishing
is thus both a means of advancing knowledge and a way to build the reputation needed to
compete for academic positions. Academic recruiters, in turn, have long relied on strong
publications as evidence of a candidate’s depth of understanding.
With the advent of highly capable and easily accessible AI, however, producing high-quality
research papers is no longer so rare. For example, AI models can now make progress on
long-standing problems across several mathematical fields [1–3]. Their users can therefore
produce impressive research without developing the depth of understanding that was once
necessary to produce the same output [4]. This effect is most pronounced in mathematics and
in the theoretical branches of science and engineering. Specifically in these domains, AI has
weakened the once-tight link between producing strong results and understanding one’s field.
In response to AI, academic communities are now reconsidering how they evaluate their re-
searchers. AsummitofmathematiciansdiscussingthefutureofthemathPh.D.recommended
placingless weighton dissertation texts, andmore weighton in-personassessments andthesis
defenses [5]. A working group in theoretical computer science proposed reviewing at most
three works per applicant, and also recommended ‘chalk talks’ to assess technical depth [6].
The free and open-access preprint server arXiv has introduced a monthly quota of two submis-
sionsperindividual[7]. Thesemeasuresechocallstocapresearchers’publicationrates[8–10].
Otherresponsesfocusonresearchnorms. Somemathematicianshavepledgedtoworkwithout
AI[11]. OthersopposehiringcolleagueswhosubstituteAIoutputfortheirownwork[12,13].
Joint statements and policies address attribution, disclosure, and AI’s effects on mathematical
practice [14–18]. Early-career mathematicians must navigate these changing expectations
2

while building their careers [19]. At the same time, departments and other recruiters of
researchers must decide how to evaluate applicants whose preparation responds to those very
decisions. Each side’s best choice therefore depends on that of the other, and neither can
be settled in isolation. Game theory is designed to analyze exactly this kind of strategic
interdependence.
In this paper, we study a game-theoretic model of the incentives on both sides of the academic
job market in the age of AI. Applicants differ in potential and choose one of two trajectories:
deep study or shallow study with AI. Deep study builds theoretical understanding but costs
more to the applicant than shallow study with AI. Furthermore, deep study may reduce paper
output for applicants who are not of high potential. Shallow study with AI is cheaper and
produces high output without building understanding. How much more deep study costs also
depends on the applicant’s potential. Recruiters observe only an applicant’s paper output
and the result of a possibly imperfect test of understanding, such as an interview, which
the applicant either passes or fails (the likelihood to pass is much larger if an applicant
understands). Because an applicant’s potential and their study choice remain hidden from re-
cruiters,recruitersmustinferunderstandingfromtwosignals: paperoutputandtheapplicant’s
performance in the test. The recruiters’ hiring decisions depend on how much they value
output and understanding, and they may reward either one or both. We ask how applicants of
different potentials should choose their study trajectories, and how recruiters should decide
when presented with a publication list and a test result.
We characterize all pure-strategy perfect Bayesian equilibria of this game. These equilibria
identify patterns of study and hiring that neither side has an incentive to unilaterally change.
We then examine which behaviors emerge under a learning process, such as payoff-based
imitation and rare exploration. This evolutionary analysis helps distinguish possible equilibria
from outcomes that tend to emerge through learning. We also relate proposed institutional
reforms [5–7] to changes in the model’s parameters. This yields conditional predictions about
how those reforms could affect study and hiring.
Section 2 defines the game, and Section 3 characterizes its equilibria. Section 4 examines
evolutionaryselectionamongoutcomes. Section5discussesinstitutionalimplications,related
work, and limitations. The Appendix (Section A) gives the evolutionary methods.
3

2 Game-theoretic model of academic effort and hiring
Game description.We study an effort-and-hiring signaling game between applicants and
recruiters. A candidate (say, a graduate student) shows up to a job interview with a resume
that highlights the academic papers they have under their belt. We classify profiles with a
binary variable𝑦, with𝑦=0 denoting few papers and𝑦=1 denoting many papers. We
assume it is impossible to fake a profile. That is, a hiring committee can reliably check if a
candidate is lying on their resume.
In addition to viewing their resume, the interviewing committee performs anunderstanding
teston the candidate (e.g., an interview). The result of this test is either𝑡=P (for ‘pass’) or
𝑡=F (for ‘fail’). An applicant with a rich (deep) understanding of the field has𝑢=1 , and
an applicant with partial (shallow) understanding of the field has𝑢=0 . A𝑢=1 candidate
passes the test with probability 1. A𝑢=0 candidate fails the test (i.e.,𝑡=F ) with probability
𝜏 and passes it (i.e.,𝑡=P ) with probability1−𝜏 . The variable𝜏∈(0,1) sets the accuracy of
the test. At𝜏=1 , the test perfectly sorts candidates based on understanding. At𝜏=0 , the
test is useless and everyone passes. Mathematically,
P(𝑡=P|𝑢=1)=1andP(𝑡=F|𝑢=0)=𝜏.
We exclude the𝜏∈{0,1}boundary cases.
Recruiter payoff.The interviewer decides whether to hire or to reject based on the joint
outcome(𝑦,𝑡) . If they accept a candidate, their payoff is𝐴𝑦+𝐵𝑢 , where𝑦 and𝑢 are the
paper and understanding values of the hired candidate. If they reject a candidate, they get an
opting-out payoff𝑟. Parameters𝐴 and𝐵 respectively capture how much the recruiter values
papers and understanding in their candidate, independently.
Applicant type and effort strategy.In this model, there are three kinds of applicants:(i)
high potential,𝐻,(ii)medium potential, 𝑀, and(iii)low potential,𝐿. Only the first two types
choose a strategy. Think of these strategies as pre-interview career trajectories. There are
two strategies:deepandshallow + AI. A deep trajectory guarantees full understanding, i.e.,
𝑢=1 , whereas a shallow trajectory yields partial or no understanding of the field, i.e.,𝑢=0 .
4

Nature Applicant Test Recruiter Payoffs
πH
high
potential
πM
medium
potential
πL
low
potential
deep
shallow + AI
pass
1 − τ
τ
deep
shallow + AI
pass
1 − τ
τ
1 − τ
τ
many papers
pass
accept
reject
many papers
fail
accept
reject
few papers
pass
accept
reject
few papers
fail
accept
reject
recruiter sees only papers and test,
not the applicant's type
accept
W − c
Ay + Bu
reject
−c
r
c = δθ if deep, else 0
y: papers (1 many, 0 few)
u: 1 if understands
understands
does not
Figure 1: The effort-and-hiring game.In Section 2, we describe the game in full detail. This figure
illustrates the textual description. First, nature produces an applicant that is either high-potential,
medium-potential, or low-potential, with probabilities𝜋𝐻,𝜋𝑀, and𝜋𝐿, respectively (each>0 ). The
high and medium-potential applicants then choose between two strategies: deep and shallow + AI.
ChoosingDeepyields a deep understanding of the field (𝑢=1 ), and choosingshallow + AIproduces
a shallow understanding of the field (𝑢=0 ). In addition to determining the understanding of an
applicant, a strategic trajectory (deep or shallow) also affects the volume of academic papers an
applicant produces pre-interview. In the baseline model, the high-potential individual produces many
papers regardless of their strategy (𝑦=1 ), but the medium-potential individual only produces many
papers if they choose shallow + AI. By going deep, the medium-potential individual earns few or no
papers (𝑦=0 ). The low-potential type is non-strategic: they have no understanding and they produce
no papers(𝑦,𝑢)=(0,0) . Recruiters receive the signal𝑦 from an applicant’s resume. In addition,
they conduct a hiring test (interview), which is meant to sort applicants based on their understanding.
However, this test is prone to false positives. Individuals with no understanding (i.e.,𝑢=0 ) fail the
test (𝑡=F ) with probability𝜏∈(0,1) and pass it (𝑡=P ) with probability1−𝜏 >0 . The recruiter
makes a decision based on the joint variable(𝑦,𝑡) coming from the candidate’s resume and interview
performance. If hired, an applicant receives𝑊−𝑐 , and if rejected,−𝑐, where𝑐=𝛿 𝜃 after deep study
and𝑐=0 after shallow study. If an applicant is hired, the recruiter gets payoff𝐴𝑦+𝐵𝑢 with𝐴,𝐵>0
representing how much the recruiter values the productivity and the understanding of their applicant,
respectively. If an applicant is rejected, the recruiter earns an opting-out payoff𝑟 >0.
When it comes to papers, a high-potential individual produces papers regardless of trajectory
5

choice (𝑦=1 ). A medium-potential individual, however, only produces papers with ‘shallow
+ AI’. (In a model extension, we study the case where a high-potential individual produces
many morepapers than a medium-potential individual when going the shallow + AI route.
We do this by making the variable𝑦 a ternary variable with𝑦 taking values0,1, and 2.) The
third and final applicant type (low-potential) is non-strategic. It has no understanding,𝑢=0 ,
and few (or no) papers,𝑦=0 . The population shares of these types are𝜋𝐻, 𝜋𝑀, and𝜋𝐿,
respectively (each>0), and𝜋 𝐻+𝜋 𝑀+𝜋 𝐿 =1.
Applicant payoff.Getting hired gives an applicant a payoff𝑊 >0. Deep study costs a
high-potential applicant𝛿𝐻 more than shallow study, and a medium-potential applicant𝛿𝑀
more, with0< 𝛿𝐻 < 𝛿𝑀 < 𝑊. Only this difference matters, so we normalize the cost of
shallow study to zero. An applicant therefore pays𝑐=𝛿 𝜃 after deep study and𝑐=0 after
shallow study, and receives𝑊−𝑐if hired and−𝑐if rejected.
Recruiterstrategy. Therecruiteremploysastrategy 𝜌(𝑦,𝑡)∈[0,1] ,theprobabilitytoaccept
an applicant with a resume worth𝑦 and a test result𝑡. The variable𝑦∈{0,1} (in the baseline
model) and𝑦∈{0,1,2} (in the extended model). The test result𝑡∈{ P, F}. We highlight
that a recruiter never sees the true type of the applicant. Nor do they know an applicant’s
understanding-level perfectly. They only get noisy signals of these through𝑦and𝑡.
We show a schematic figure of this game inFigure1. InTable1, we summarize our model
parameters and highlight which parameters are known to which players.
3 Equilibrium analysis of the effort-and-hiring game
Formally, our setup in Section 2 is called a sequential game with incomplete information. The
relevant game-theoretic equilibrium notion for this class of games is theperfect Bayesian
equilibrium.
What does this particular equilibrium notion mean? In plain terms, it represents a stable
pattern of behavior on both sides of the game together with a consistent way of reading
the evidence at hand. It has three ingredients: (a) each type of applicant chooses an effort
6

Symbol Meaning and values Applicant
knows?
Recruiter
knows?
Applicant type (drawn by Nature)
𝜃high (𝐻), medium (𝑀), or low (𝐿) potential✓(private)✗
𝜋𝐻, 𝜋𝑀, 𝜋𝐿 Population shares of types,𝜋𝐻+𝜋 𝑀+𝜋 𝐿 =1;𝜋 𝜃 >0✓ ✓
Applicant’s choice
𝑎Trajectory chosen by𝐻and𝑀:
deep (D) or shallow+AI (S);𝐿does not choose✓(own)✗
𝑢Understanding:𝑢=1afterD,𝑢=0afterSor for𝐿✓(own)✗
𝛿𝐻,𝛿 𝑀 Netcostofchoosingdeepovershallow, 0<𝛿 𝐻<𝛿 𝑀<𝑊✓ ✓
What the recruiter observes
𝑦Output in papers:
(Baselinemodel): 𝑦=1 ,manypapers; 𝑦=0 ,fewpapers.
(Extension): 𝑦=2 , super; 𝑦=1 , many;𝑦=0 , few
papers
✓ ✓
𝑡Test outcome: pass (P) or fail (F)✓ ✓
𝜏 Test accuracy: probability that an applicant without un-
derstanding fails; applicants with understanding always
pass
✓ ✓
Payoffs
𝑊Value of being hired to the applicant✓ ✓
𝐴Value to the recruiter of each unit of output𝑦✓ ✓
𝐵Value to the recruiter of a hire who understands (𝑢=1)✓ ✓
𝑟Recruiter’s outside option (value of rejecting)✓ ✓
Table 1: Elements of the effort-and-hiring game. This table summarizes the variables and
parameters in the effort-and-hiring game described in Section 2. The applicant’s type𝜃, trajectory
𝑎, and understanding𝑢 are private to the applicant. The recruiter observes only output𝑦 and the test
outcome𝑡 (whichmayproducefalsepositivesbypassing 𝑢=0 playerswithprobability 1−𝜏>0 ). All
other parameters are common knowledge. A high-potential applicant produces papers𝑦=1 regardless
of trajectory, but medium-potential applicants only get𝑦=1 with shallow+AI. If hired, the applicant
receives𝑊−𝑐 and the recruiter gets𝐴𝑦+𝐵𝑢 ; if rejected, the applicant receives−𝑐 and the recruiter,
𝑟, where𝑐=𝛿 𝜃 after deep work and𝑐=0 otherwise. In an extended model, we allow𝑦 to take
three values,𝑦∈{0,1,2} , representing different levels of research output. With AI, a high-potential
individual achieves𝑦=2 (called a super-output), whereas a medium-potential individual achieves
𝑦=1. Without AI, a high-potential individual also achieves𝑦=1.
7

trajectory that serves it best, given how recruiters respond; (b) the recruiter accepts or rejects
each kind of applicant in the way that serves the recruiter best, given what it believes about
that applicant; (c) these beliefs arecorrect on average: they follow from the share of each
type in the population and from what each type actually does.
For example, if in equilibrium only high-potential applicants work deeply, then a recruiter
who sees many papers and a passed test knows that this applicant is either a high-potential
deep worker or a medium-potential applicant who used AI and passed the test by luck. In
equilibrium, the recruiter weighs the two possibilities by the likelihood of their outcome. At
equilibrium, neither side has the payoff-incentive to change their (work or hiring) behavior
unilaterally. In this paper, we characterize the pure-strategy perfect Bayesian equilibria of this
game. Later, we also perform evolutionary simulations to study the behaviors that are learned
when multiple equilibria exist simultaneously.
The five pure-strategy equilibria of the baseline model
Baseline-model equilibria.In the baseline model, one of five behavioral patterns is stable at
a pure-strategy perfect Bayesian equilibrium.Table2B1 summarizes these five equilibria,
specifying each party’s behavior, the conditions for equilibrium existence, and the recruiter’s
beliefs at equilibria. To aid interpretation,Table2A provides the key terms and definitions.
The five equilibrium patterns of the baseline model, labeledE1–E5, are described below.
1.E 1: All strategic applicants choose shallow; recruiter hires nobody.
2.E 2: Only𝐻applicants choose deep; recruiters hire only if they see(𝑦,𝑡)=(1,P).
3.E 3: All strategic applicants choose deep; recruiter only hires if they see𝑡=P.
4.E 4: 𝐻 applicants go shallow,𝑀 applicants go deep; recruiter only hires(𝑦,𝑡)=(0,P) .
5.E 5: All strategic applicants choose shallow; all with𝑦=1hired.
The equilibriumE5, wherein strategic applicants choose the shallow route and the recruiter
hireseveryonewithpapers(i.e., 𝑦=1 , orbasicallyeverystrategicapplicant), istrivial. Itonly
appears when𝐴⩾𝑟 —that is, when the recruiter values a many-paper applicant more than
their opting-out payoff. In fact, in this parameter regime, this is the only equilibrium because
8

output alone already makes a hire worthwhile, which empties the test of any consequence.
Applicants too find no reason to invest in costly understanding.
When output alone does not justify a hire (𝐴 < 𝑟), the recruiter accepts an applicant only
if it believes the applicant understands, so every equilibrium rests on what a passed test is
believed to reveal. InE1, nobody works deeply, so a pass reveals nothing (𝜇1=𝜇 0=0 ) and
the recruiter rejects everyone. An applicant who deviates to deep work cannot be told apart
from lucky AI users. They bear the cost𝛿𝜃 for nothing, and thus the trap sustains itself. In
E2, only high-potential applicants work deeply. Applicants with many papers who pass are
then genuine understanders with probability¯𝜇1 (from the perspective of recruiters), and the
recruiter hires them provided understanding is valuable enough (𝐵⩾B 1). High-potential
applicants find depth worthwhile when the test catches enough AI users to make the job
premium𝑊cover the cost (𝜏𝑊⩾𝛿 𝐻).
In E3, medium-potential applicants also work deeply, accepting few papers in exchange for
beingrecognizedascompetent. ThisremovestheAIusersfromthemany-paperpool( 𝜇1=1 ),
and it requires the recruiter to hire few-paper passers (𝐵⩾B 0), who are mostly genuine but
include low-potential applicants who passed by luck.
E4 is the mirror image ofE2: only medium-potential applicants work deeply and are hired
through the few-paper-and-pass channel. Every many-paper applicant who passes is a lucky
AI user. Since the recruiter only hires those that have few papers but also pass the test,
high-potentialcandidatesarenottemptedtotrythecostlyrouteofgoingdeep. Thisisbecause
there is no way for them to escape their inherent productivity (remember that high-potential
applicants produce𝑦=1 regardless of effort). As a result, in this equilibrium, the high-
potential applicants end up shallow and unemployed. The four listed pure-strategy equilibria
for𝐴<𝑟 may simultaneously exist depending on the parameter values (Table2, Figure 2A).
In a later section, we discuss the evolutionary selection among these various equilibria.
Extra equilibria in the extended super-output model
In the extended model, we consider three levels of paper output,𝑦=0,1,2 . The𝑦=2 case
represents thesuper-outputwhich is achieved by high-potential applicants using AI. When
high-potential applicants go deep or when medium-potential applicants go shallow, they
9

Panel A. Notation
Symbol Definition
𝜎𝐻, 𝜎𝑀∈{0,1}Effort strategy of high-potential (𝐻) and medium-potential (𝑀) applicants:
deep work (=1) or shallow work with AI (=0).
𝜌1P,𝜌 1F,𝜌 0P,𝜌 0F Recruiterstrategy;probabilitytoacceptafterobserving 𝑦∈{0,1} and𝑡∈{ P, F}
𝜌2 Probability of accepting super-output,𝑦=2(in extended model only).
𝜇1, 𝜇0 Recruiter belief that an applicant who passed the test with many papers (𝜇1) or
few papers (𝜇0) truly understands.
¯𝜇1=𝜋 𝐻/[𝜋𝐻+(1−𝜏)𝜋 𝑀]Value of𝜇 1 when only high-potential applicants work deeply.
¯𝜇0=𝜋 𝑀/[𝜋𝑀+(1−𝜏)𝜋 𝐿]Value of𝜇 0 when medium-potential applicants work deeply.
B1=(𝑟−𝐴)/¯𝜇 1,B 0=𝑟/¯𝜇0 Value of understanding above which the recruiter hires applicants who passed
with many (B1) or few (B0) papers.
Panel B. Pure-strategy perfect Bayesian equilibria
Equilibrium
Applicant
strategy
(𝜎𝐻,𝜎𝑀)
Recruiter strategy
(𝜌 1P,𝜌 1F,𝜌 0P,𝜌 0F;𝜌 2)
Recruiter
belief
(𝜇 1,𝜇 0)
Exists if and only if
B1. Baseline (a high-potential applicant using AI produces𝑦=1)
Depth regime,𝐴<𝑟
E1: all shallow, no hires(0,0) (0,0,0,0;–) (0,0)always
E2: only𝐻deep(1,0) (1,0,0,0;–) (¯𝜇 1,0)𝐵⩾B 1 and𝜏𝑊⩾𝛿 𝐻
E3: all deep(1,1) (1,0 †,1,0;–) (1,¯𝜇 0)𝐵⩾B 0 and𝜏𝑊⩾max(𝛿 𝐻,𝛿𝑀)
E4: reverse sorting(0,1) (0,0,1,0;–) (0,¯𝜇 0)𝐵⩾B 0
Output regime,𝐴⩾𝑟
E5: shallow,𝑦=1hired(0,0) (1,1,0,0;–) (0,0)always; unique
B2. Extension (a high-potential applicant using AI produces super-output𝑦=2)
𝐴<𝑟/2
E1: shallow, no hires(0,0) (0,0,0,0; 0) (0,0)always
E2:𝐻deep(1,0) (1,0,0,0; 0 †) (¯𝜇 1,0)𝐵⩾B 1
E3: all deep(1,1) (1,0 †,1,0; 0 †) (1,¯𝜇 0)𝐵⩾B 0 and𝜏𝑊⩾𝛿 𝑀
E4: reverse sorting(0,1) (0 †,0†,1,0; 0) <𝑟−𝐴 𝐵 ,¯𝜇0  𝐵⩾B 0
𝑟/2⩽𝐴<𝑟
E6: shallow,𝐻hired(0,0) (0,0,0,0; 1) (0,0)always
E7: reverse sorting(0,1) (0 †,0†,1,0; 1) (< 𝑟−𝐴 𝐵 ,¯𝜇0)𝐵⩾B 0
(0,1) (1 †,0†,1,0; 1) (⩾ 𝑟−𝐴 𝐵 ,¯𝜇0)𝐵⩾B 0;𝜏𝑊⩾𝛿 𝑀
Output regime,𝐴⩾𝑟
E5: shallow,𝑦⩾1hired(0,0) (1,1,0,0; 1) (0,0)always; unique
Table 2: Pure-strategy perfect Bayesian equilibria of the effort-and-hiring game.PanelAdefines
notation. PanelBlists every pure-strategy equilibrium outcome for0<𝜏<1in the baseline (B1) and
super-output (B2) models; outcomes not listed in a regime do not exist there. Each row gives the
conditions under which its supporting profile is an ordinary perfect Bayesian equilibrium. Outcomes
with several supporting profiles, such asE7, have one row per profile. We assume0<𝛿 𝐻 <𝛿 𝑀 <𝑊
and break ties in favor of acceptance. A dash (–) marks an observation impossible in the baseline. A
dagger (†) in the strategy profile marks a decision after an observation that never occurs in equilibrium.
These actions rest on some off-equilibrium beliefs. We discuss them in Section 3.
10

E5
E1
E1, E2
E1, E2, E3, E4
E1, E3, E4
B = (r − A) / ̄μ1(τ)
B = r / ̄μ0(τ)
A = r
0 r/2 r
0
r
value of output, A
value of understanding, B
A Baseline model (high potential with AI produces y = 1)
E5
E1
E1, E2
E1, E2, E3, E4
E6
E6, E7
E1, E3, E4
B = (r − A) / ̄μ1(τ)
B = r / ̄μ0(τ)
A = r/2 A = r
0 r/2 r
0
r
value of output, A
value of understanding, B
B Super-output model (high potential with AI produces y = 2)
E1 all shallow, nobody hired
E2 only H deep; pass + many papers is hired
E3 all deep; only pass is hired
E4 M deep and H shallow; only few paper + pass is hired
E5 all shallow; every applicant with many or super output is hired (y ≥ 1)
E6 all shallow; only super-paper applicant hired.
E7 M deep; H shallow; few papers + pass and super output is hired.
Shading: 1 2 3 4 equilibria coexist; grey = output dominating regime A ≥ r
Figure 2: Existence regions of pure-strategy perfect Bayesian equilibria.Each region of the𝐴–𝐵
plane is labeled with the perfect Bayesian equilibrium outcomes that exist there, for the baseline model
(A) and the super-output model (B). The red line is𝐵=B 1, the dashed line is𝐵=B 0, and the vertical
lines mark𝐴=𝑟 and, inB,𝐴=𝑟/2 . These are all defined in Table 2A. As we see, several equilibrium
outcomes can coexist for a particular parameter combination. The shade of blue in the parameter plane
gives the number of distinct equilibrium outcomes for the underlying parameter (not strategy profiles).
Parameters are(𝜋𝐻,𝜋𝑀,𝜋𝐿)=(0.3,0.5,0.2),𝜏=0.9,𝛿 𝐻 =0.2,𝛿 𝑀 =0.4, and𝑊=𝑟=1.
produce𝑦=1 . We call𝑦=0,1,2 , few papers, many papers, and super-output, respectively.
Because super-output can only come from a high-potential AI user, it perfectly reveals that
the applicant lacks understanding and is worth2𝐴 to the recruiter, regardless of the test.
Whether the recruiter hires them therefore depends only on whether2𝐴⩾𝑟 , and this splits
the parameter space into three regimes.
When𝐴<𝑟/2 ,super-outputisnotworthhiring,sothehigh-potentialapplicantscannolonger
hide behind AI. A high-potential applicant who chooses shallow study is rejected outright,
and the same four equilibriaE1–E4 arise as in the baseline. However, depth is now easier to
sustain: high-potential applicants go deep whenever the recruiter trusts many-paper passers
(𝐵⩾B 1), irrespective of the test discernment𝜏. Reverse sortingE4 still exists, but only
11

because the recruiter holds a pessimistic belief about an observation that no one produces
(i.e.,𝑦=1 ). Under the D1 refinement, however, this belief is implausible, andE4 is ruled out
when depth is cheap enough for high-potential applicants,𝛿𝐻(1−𝜏)<𝑊−𝛿 𝑀. For more
details on the D1 refinement, see the note on off-equilibrium beliefs later in this section.
When𝑟/2⩽𝐴<𝑟 , super-output alone justifies a hire, and two new pure-strategy equilibria
replace E1–E4, both of which have the property that high-potential applicants do not invest in
understandingbecauseAInowguaranteesajobatnocost. In E6,medium-potentialapplicants
also stay shallow; their many papers arenot worth hiring, so onlythe high-potential applicants
are hired, on the strength of super-output. InE7, medium-potential applicants instead work
deeply and are hired through the few-paper channel (𝐵⩾B 0), while the high-potential
applicants are hired for their super-output. In both equilibria, understanding, if present at all,
is concentrated among medium-potential applicants.
Finally, when𝐴⩾𝑟 , the output-dominant regime of the baseline model reappears. Every
applicant with𝑦⩾1 is hired regardless of the test, nobody works deeply, andE5 is the
unique equilibrium. The super-output extension thus moves the threshold beyond which
high-potential applicants abandon understanding from𝐴=𝑟 down to𝐴=𝑟/2 . In other
words,themoreproductiveanAImakesthehigh-potentialapplicants,thelowertherecruiter’s
per-unitvaluationofoutputneedstobebeforedepthdisappearsamongthem. Theequilibrium
regions for the super-output model are summarized inFigure2B.
What is the likelihood that hired candidates possess understanding at each equilibrium?
Equilibria differ not only in who goes deep but also in the outcomes the recruiter cares about.
Wethereforecomparethemontwomeasures: theshareofallapplicantswhoarehiredandthe
hiring quality defined as the probabilityPr(𝑢=1|hired) that a hired candidate understands
the subject. This is summarized inTable3.
The share of hires who understand the subject is highest in eitherE2 or E3. Between these
two, which one has the higher share depends only on the type distribution𝜋:
Pr(𝑢=1|hired)

E3 ⩾Pr(𝑢=1|hired)

E2 ⇐⇒𝜋 𝐻𝜋𝐿 ⩽𝜋 𝑀(𝜋𝐻+𝜋 𝑀).
12

Eq. Who is hired Hire rateP(𝑢=1|hired)Example
Panel A: Baseline model
E1 nobody0– –
E2 H (deep); M (shallow) who pass𝜋𝐻+(1−𝜏)𝜋 𝑀
𝜋𝐻
𝜋𝐻+(1−𝜏)𝜋 𝑀
0.857
E3 H, M (deep); L who pass𝜋 𝐻+𝜋𝑀+(1−𝜏)𝜋 𝐿
𝜋𝐻+𝜋𝑀
𝜋𝐻+𝜋𝑀+(1−𝜏)𝜋 𝐿
0.976
E4 M (deep); L who pass𝜋 𝑀+(1−𝜏)𝜋 𝐿
𝜋𝑀
𝜋𝑀+(1−𝜏)𝜋 𝐿
0.962
E5 H, M (shallow)𝜋 𝐻+𝜋𝑀 00
Panel B: Super-output model
E1 nobody0– –
E2 H (deep); M (shallow) who pass𝜋𝐻+(1−𝜏)𝜋 𝑀
𝜋𝐻
𝜋𝐻+(1−𝜏)𝜋 𝑀
0.857
E3 H, M (deep); L who pass𝜋 𝐻+𝜋𝑀+(1−𝜏)𝜋 𝐿
𝜋𝐻+𝜋𝑀
𝜋𝐻+𝜋𝑀+(1−𝜏)𝜋 𝐿
0.976
E4 M (deep); L who pass𝜋 𝑀+(1−𝜏)𝜋 𝐿
𝜋𝑀
𝜋𝑀+(1−𝜏)𝜋 𝐿
0.962
E6 H (shallow,𝑦=2)𝜋 𝐻 00
E7
H (shallow,𝑦=2); M (deep);
L who pass
𝜋𝐻+𝜋𝑀+(1−𝜏)𝜋 𝐿
𝜋𝑀
𝜋𝐻+𝜋𝑀+(1−𝜏)𝜋 𝐿
0.610
E5 H, M (shallow)𝜋 𝐻+𝜋𝑀 00
Table 3: Rate of hiring and the probability that a hired candidate understands in each listed
pure-strategy equilibrium of the two models.PanelAreports the baseline results, and panelBthe
extended results. The last column gives values for𝜋𝐻 =0.3,𝜋 𝑀 =0.5,𝜋 𝐿 =0.2, and𝜏=0.9.
Thetwoequilibriamakedifferentmistakes. In E2, theerrorsare 𝑀 applicantswhogoshallow
and slip past the test. InE3, the errors are low-potential𝐿 applicants who slip past it.E3
therefore wins when low-potential applicants are scarce relative to medium-potential ones,
and E2 wins when they are common, becauseE2 screens them out entirely. The test accuracy
𝜏 scales both kinds of error by the same factor1−𝜏 , so it changes how large the errors are but
not which equilibrium does better.
13

Note on off-equilibrium-path beliefs in our equilibria characterization.In an equilibrium,
some observations never occur. For example, if every applicant works deeply (assuming that
there are no low-potential applicants, who do not have the strategic option of working deeply),
the recruiter never sees anyone fail the test. Because such an observation has probability zero,
Bayes’ rule cannot tell the recruiter what to believe if it were to happen. These are called
off-equilibrium-pathbeliefs. Theystillmatter,becausetheydeterminehowtherecruiterwould
respondtoadeviation,andthereforewhetheranyonewantstodeviate. Wedisciplinethemwith
twostandardrefinements.Consistencyrequiresthatifonlyonekindofapplicantcouldpossibly
have produced an observation, the recruiter attributes it to that kind. TheD1 criterionapplies
when several kinds of applicant could have produced an unexpected observation. It requires
the recruiter to attribute the observation to the kind that would gain from it under the widest
range of recruiter responses, that is, to the applicant with the strongest incentive to deviate.
InTable2,adagger( †)marksarecruiterdecisionthatrestsonsuchabelief. Thethreecasesare:
(i)Failed test with many papers(𝜌1F =0† in E3 of both models, and inE4 and E7 of the
extended model). Only an applicant without understanding can fail the test, so consistency
forces the belief𝑢=0. Since output alone is not worth hiring (𝐴<𝑟), the recruiter rejects.
(ii)Super-output( 𝜌2=0†in E2and E3oftheextendedmodel, 𝐴<𝑟/2 ). Onlyahigh-potential
applicant using AI can produce𝑦=2 , so consistency again forces𝑢=0 . Since super-output
alone is not worth hiring (2𝐴<𝑟), the recruiter rejects.
(iii)Manypaperswithapassedtest( 𝜌1P=0† in E4;𝜌1P=0/1† in E7 oftheextendedmodel).
In these equilibria, no applicant produces𝑦=1 , since high-potential applicants produce
super-output and medium-potential applicants produce few papers. Two deviators could
producethisobservation: ahigh-potentialapplicantwhoworksdeeply,andamedium-potential
applicant who uses AI. Consistency alone therefore does not pin down the belief𝜇1. Any
𝜇1<(𝑟−𝐴)/𝐵 supportsrejection,andany 𝜇1 ⩾(𝑟−𝐴)/𝐵 supportsacceptance. D1attributes
the observation to the type that would gain from deviating for the wider range of recruiter
responses. A high-potential applicant gains whenever the probability of acceptance after
this observation exceeds𝛿𝐻/𝑊, provided they are not already hired. A medium-potential ap-
plicantgainsonlywhenitexceeds (𝑊−𝛿 𝑀)/(𝑊(1−𝜏)) ,whichisimpossiblewhen 𝛿𝑀 ⩽𝜏𝑊 .
14

(a)In E4 (𝐴<𝑟/2 ), high-potential applicants are rejected for their super-output and may gain
from working deeply. If𝛿𝐻(1−𝜏)<𝑊−𝛿 𝑀, D1 attributes the observation to them (𝜇1=1 ).
The recruiter would then hire, high-potential applicants would deviate, andE4 is eliminated.
If𝛿𝐻(1−𝜏)⩾𝑊−𝛿 𝑀, D1 does not single out the high-potential type, andE4 survives. At
equality, the two thresholds coincide, so D1 cannot single out either type and the equilibrium
survives.
(b)In E7 (𝑟/2⩽𝐴<𝑟 ), high-potential applicants are already hired for their super-output and
can never gain by working deeply. If𝛿𝑀 >𝜏𝑊 , only a medium-potential AI user could gain,
so D1 sets𝜇1=0 and rejection is the only supported response. Acceptance would in any case
not be an equilibrium response here, since medium-potential applicants would then switch to
shallow study. If𝛿𝑀 ⩽𝜏𝑊 , neither type can gain from producing this observation, so D1
places no restriction on beliefs. Both acceptance and rejection are then consistent with D1,
which is why the table lists𝜌1P=0/1†. In every case,E7 survives, and the off-path response
does not affect who studies deeply or who is hired.
Every other entry inTable2 concerns observations that occur on the equilibrium path, and
the corresponding beliefs follow directly from Bayes’ rule.
4 Selection between simultaneously existing equilibria
Our equilibrium analysis shows that multiple equilibria can simultaneously exist, depending
on the game parameters (Figure2). To investigate which equilibria areattainable, we
study a learning process in populations of applicants and recruiters. Rather than assum-
ing that both parties coordinate on a particular equilibrium, we allow their strategies to
evolve through a myopic learning process, where individuals copy strategies from others
inthepopulationifthoseotherstrategiescurrentlyyieldahigherpayoffthantheirownstrategy.
To this end, we consider three populations: one for high-potential applicants, one for medium-
potential applicants, and one for recruiters. Each population is of size𝑁. Applicants
choose between D and S (for deep and shallow). Recruiters choose one of 16 pure strategies
(𝜌 1P,𝜌 1F,𝜌 0P,𝜌 0F)∈{0,1} 4 inthebaselinemodelandamong32intheextendedmodelwith
15

𝜌2∈{0,1}included in the strategy.
We study the imitation-and-exploration dynamic in these populations with exploration hap-
pening very rarely [20]. We assume that individuals learn strategies from within their
population (i.e., a high-potential applicant never imitates a medium-potential applicant and
vice versa). We set the applicant-pool distribution(𝜋𝐻,𝜋 𝑀,𝜋 𝐿), the type-sensitive costs
𝛿𝐻 and 𝛿𝑀, the job premium𝑊, and the test accuracy𝜏, exogenously for each simula-
tion. We use our simulations to quantify how often, in the long run, high-potential and
medium-potential applicants choose deep versus shallow strategies, and how often recruiters
adopt each of their 16 (or 32) strategies. The simulations thus reveal behavior that emerges
throughimitationandexplorationinbothapplicantsandrecruiters, ratherthanthroughcoordi-
nationonaparticularequilibrium. FulldetailsofthelearningprocessareprovidedinMethods.
Let us first discuss the learning outcomes inFigure3, which shows the long-run behavior
of applicants and recruiters in the baseline model. In the baseline model, test accuracy does
not matter once output alone justifies hiring (𝐴⩾𝑟 ). There, both strategic types learn to
go shallow, and recruiters learn to hire every applicant with many papers, whether or not
they pass the test (𝜌1𝑃,𝜌 1𝐹≈1 ). When the test is accurate, recruiters also occasionally hire
few-paper applicants who pass. These are only the low-potential applicants who get through
by luck, so accepting them is costly but only weakly selected against.
When𝐴<𝑟 , depth is chosen by candidates if understanding is valued sufficiently (𝐵>B 1)
andthe test is accurate enough. There are two interesting regimes in the intersection space
between𝐵>B 1 (the negatively sloped line) and𝐴<𝑟 (the vertical line). In the first regime,
B1 < 𝐵 <B0, the high-potential applicants learn to go deep, and recruiters learn to hire
applicants with many papers who pass the test. In the second regime,𝐵 >B0, recruiters
also learn to hire few-paper applicants who pass, which rewards depth by medium-potential
applicants. In this region, depth by medium-potential applicants dominates at low𝐴, where
the high-potential applicants go shallow (reverse sorting). Depth by high-potential applicants
dominates as𝐴 approaches𝑟. At low test accuracy (𝜏=0.5 ), the high-potential applicants
rarelygodeep,andthemedium-potentialapplicantsdosoonlywhen 𝐵isveryhighand 𝐴islow.
Next, we discuss the learning outcomes in the extended ‘super-output’ model.Figure4
shows the long-run learned behaviors. Overall, letting high-potential applicants produce
16

Baseline model:  pairwise imitation, rare exploration limit, β = 5, N = 30
0
r
2r
τ = 0.5
B
high potential
deep
high potential
shallow
medium potential
deep
medium potential
shallow
0
r
2r
τ = 0.9
B
0 r/2 r
A
0
r
2r
τ = 0.99
B
0 r/2 r
A
0 r/2 r
A
0 r/2 r
A
0.0 0.2 0.4 0.6 0.8 1.0
long-run probability of deep
0.0 0.2 0.4 0.6 0.8 1.0
long-run probability of shallow
A   Long-run behaviour of applicants
0
r
2r
τ = 0.5
B
ρ1P
many papers,
pass
ρ1F
many papers,
fail
ρ0P
few papers,
pass
ρ0F
few papers,
fail
0
r
2r
τ = 0.9
B
0 r/2 r
A
0
r
2r
τ = 0.99
B
0 r/2 r
A
0 r/2 r
A
0 r/2 r
A
0.0 0.2 0.4 0.6 0.8 1.0
long-run acceptance probability
B   Long-run acceptance probabilities
Figure 3: Long-run behavior of applicants and recruiters in a learning process (baseline model).
Westudyhowstrategiesevolveinpopulationsofhigh-potentialapplicants,medium-potentialapplicants,
and recruiters as a result of imitation and rare exploration. For full details of the learning process, see
Methods. In panelA, we plot the long-run likelihood that the high-potential and medium-potential
populationsuseadeep(orshallow)trajectory. InpanelB,weplotthelong-runlikelihoodthatrecruiters
accept after one of four possible outcomes of an evaluation(𝑦,𝑡)∈{(1, P),(1, F),(0, P),(0, F)}. We
plot this as we vary the parameters𝐴 and𝐵 in the horizontal and vertical axes, respectively, and the
accuracy of the test,𝜏, in rows. Game parameters are the same as those inFigure2. The population
size is set at𝑁=30and the strength of imitation, at𝛽=5.
17

Super output model:  pairwise imitation, rare exploration limit, β = 5, N = 30
0
r
2r
τ = 0.5
B
high potential
deep
high potential
shallow
medium potential
deep
medium potential
shallow
0
r
2r
τ = 0.9
B
0 r/2 r
A
0
r
2r
τ = 0.99
B
0 r/2 r
A
0 r/2 r
A
0 r/2 r
A
0.0 0.2 0.4 0.6 0.8 1.0
long-run probability of deep
0.0 0.2 0.4 0.6 0.8 1.0
long-run probability of shallow
A   Long-run behaviour of applicants
0
r
2r
τ = 0.5
B
ρ1P
many papers,
pass
ρ1F
many papers,
fail
ρ0P
few papers,
pass
ρ0F
few papers,
fail
ρ2
super output
y = 2
0
r
2r
τ = 0.9
B
0 r/2 r
A
0
r
2r
τ = 0.99
B
0 r/2 r
A
0 r/2 r
A
0 r/2 r
A
0 r/2 r
A
0.0 0.2 0.4 0.6 0.8 1.0
long-run acceptance probability
B   Long-run acceptance probabilities
Figure 4: Long-run applicant and recruiter behavior in a learning process (extended model).We
study the same process as the one in Figure 3 but for the super-output extension model. PanelAstays
the same as Figure 3. Here, in panelB, we plot the long-run likelihood that recruiters accept after one
of five outcomes of an evaluation(𝑦,𝑡)∈{(1, P),(1, F),(0, P),(0, F),(2,𝑥)} , where𝑥 can either be
Pass or Fail. In our super-output extension model, we assume that recruiters do not pay attention to
the test outcome if they see𝑦=2 . This is because seeing this outcome automatically implies that the
applicantishigh-potentialandshallow. Weplottheselikelihoodsaswevarytheparameters 𝐴and𝐵 in
the horizontal and vertical axes, respectively, and the accuracy of the test,𝜏, in rows. Game parameters
are the same asFigure2. The population size is set at𝑁=30 and the strength of imitation, at𝛽=5 .
18

super-output (𝑦=2 ) by going shallow sharply reduces depth. Recruiters accept𝑦=2 almost
exactly when it pays (𝐴⩾𝑟/2 ), so the threshold beyond which depth disappears moves from
𝐴=𝑟 to 𝐴=𝑟/2 . For𝜏=0.5 , neither type goes deep anywhere. At higher test accuracy,
high-potential applicants study deeply for𝐴 < 𝑟/2and high𝐵, but less often than in the
baseline. Thecauseisaweakpointinthelearningprocess. Whenhigh-potentialapplicantsgo
deep, no one produces𝑦=2 . The recruiter population can neutrally drift into accepting it at
nocost(providedtheyseeit,atall). Oncetheydo,high-potentialapplicantsdobetterbygoing
shallow,andasaresult,depthunravelsevenwhereitisanunderlyingequilibriumthatsupports
it. Depth is lost not because it stops paying, but because nothing protects the rule of rejecting
super-output at the outset. Indeed, when we repeat the simulations with recruiters barred from
accepting super-output, depth by high-potential applicants rises above even its baseline level
(we do not present this result in main text; please find our code in the repository). Finally,
for𝑟/2⩽𝐴 < 𝑟 , depth survives only among medium-potential applicants, at high test ac-
curacyand 𝐵>B 0,alongsidesuper-outputhiringofhigh-potentialapplicants(reversesorting).
5 Discussion
Our model links applicants’ study choices to recruiters’ hiring incentives. The model’s
predicted outcomes depend on the value recruiters place on output and understanding, the
cost of study, and the accuracy of assessment. These factors shape who studies deeply and
who gets hired. For departments seeking to encourage mathematical understanding, the
model points to two priorities: how they reward understanding and how reliably they assess it.
Here,wediscusssomeimportantinferencesfromtheanalysiswehaveperformedonourmodel.
(i) Valuing understanding does not automatically guarantee adoption of deep study.One
of our findings highlights that valuing understanding does not, by itself, create an incentive to
acquire it. Consider a market in which every strategic applicant studies shallowly. Recruiters
know this, either from reasoning or from experience. They therefore know that everyone who
passes the test got through by luck, so a pass carries no information about understanding.
If output alone does not justify hiring (i.e.,𝐴 is not high enough), recruiters reject every
applicant,nomatterhowhighlytheyvalueunderstanding( 𝐵). Nowsupposeasingleapplicant
studies deeply. That applicant passes the test, but a pass is all the recruiter sees, and it looks
exactlyliketheluckypassesofshallowapplicants. Therecruiterhasnowaytotellthemapart,
19

and so they reject both. Deep study therefore brings no reward, and no applicant has a reason
to change course. A pass means nothing because no one studies deeply, and no one studies
deeply because a pass means nothing. The trap persists even though recruiters interpret every
signal correctly.
(ii)Thestabilityofthedeep-studyequilibriadependsoninstitutionalexpectations.Every
pure-strategy equilibrium with deep study coexists with an equilibrium in which all strategic
applicants study shallowly (Figure2). Institutional expectations determine which of the two
outcomes takes hold. The same valuation of output,𝐴, and understanding,𝐵, and the same
test accuracy,𝜏, can support both a market in which no one studies deeply and one in which
many do. What separates them is not these fundamentals but what each side expects of the
other. Recruiters’ expectations shape how they read a pass. If they expect applicants to study
deeply, a pass signals understanding and they hire on it. If they expect shallow study, a pass
signals only luck and they reject. Applicants’ expectations shape whether deep study is worth
its cost. If applicants expect recruiters to hire those who pass, deep study pays. If they expect
recruiters to reject everyone, it does not. Each side’s expectation is confirmed by the other’s
behavior, so both outcomes sustain themselves. No single applicant or department can move
themarketalone. Adepartmentthatstartsrewardingpassesatfirsthiresonlyluckyapplicants.
Applicants change course only once enough departments do (a lone applicant who studies
deeplyalsogoesunrewarded). Escapingthetrapthereforerequirescoordination. Departments
mustcommittogether,andinadvance,torewardingdemonstratedunderstanding. Ourlearning
simulations suggest that such coordination is hard to reach. In the rare-exploration limit we
study, onlyonepopulationchangesatatime, andadepartmentorapplicantthatchangesalone
is penalized by the other side’s current behavior. Populations therefore often settle where no
one studies deeply, even when deep study could be sustained, especially when tests are less
accurate or when AI amplifies high-potential output. Faster exploration, which allows several
departments and applicants to change at once, may make coordination easier.
(iii) Existence of a reverse-sorting equilibrium.One of the more surprising outcomes from
our model is the reverse-sorting equilibrium, in which medium-potential applicants study
deeply while high-potential applicants rely on AI (equilibriumE4). The logic rests on what
eachsignalcomestomean. High-potentialapplicantsproducemanypaperswhethertheystudy
deeply or not. Medium-potential applicants who study deeply produce few papers but pass
the test. Suppose recruiters expect high-potential applicants to study shallowly. Then every
20

applicant with many papers is a shallow worker, and recruiters rationally reject them, even
those who pass. A high-potential applicant who studies deeply gains nothing, because they
cannot avoid producing many papers and so cannot escape this inference. Medium-potential
applicants face the opposite situation. Few papers combined with a pass now marks someone
who studied deeply, so recruiters hire on it, and deep study pays. High-potential applicants
are locked out by their own productivity. In this equilibrium, abundant output has become a
sign of shallowness rather than ability.
(iv) Applicants’ perception of test accuracy matters.In our model, applicants know the
accuracy of the test exactly. In practice, they may only hold a belief about it. Our conditions
show what would happen in that case. A high-potential applicant studies deeply only if
𝜏𝑊⩾𝛿 𝐻, and this decision rests on how accurate the applicant believes the test to be. If
applicants underestimate the test’s accuracy, they study shallowly even when the test would
catch them. A rigorous test that applicants consider easy to pass therefore deters no applicant.
Depth requires tests that are both accurate and known to be accurate. This gives transparent
assessment standards real value.
(v) A more accurate test by itself does not encourage understanding.Better assessment
alone does not protect understanding. When output by itself justifies hiring, recruiters hire
applicants with many papers even when they fail the test. Depth then disappears regardless of
how accurate the test is. A test shapes behavior only if a failed test actually costs the applicant
the job. Investment in assessment therefore matters only alongside hiring rules that use the
assessment’s results.
(vi) Hiring more does not guarantee hiring better understanding.Equilibria differ
both in how many applicants are hired and in how many of the hired understand their field.
Hiring every applicant who passes (E3) raises the hiring rate but also admits low-potential
applicants who passed by luck. Hiring only applicants with many papers who pass (E2) hires
fewer people but screens out low-potential applicants entirely, at the cost of admitting some
medium-potential AI users. Which rule yields more understanding per hire depends only on
the applicant pool, not on test accuracy (Table3). Hiring every applicant who passes does
better when low-potential applicants are rare relative to medium-potential ones: that is, when
𝜋𝐻𝜋𝐿 ⩽𝜋 𝑀(𝜋𝐻+𝜋 𝑀). When low-potential applicants are common, hiring only many-paper
21

applicants who pass does better.
(vii) Ongoing reforms through the lens of the model.Some of the ongoing reforms
discussed in the introduction of our paper can be conceptually mapped to elements in our
model. Oral defenses and chalk talks [5, 6] raise test accuracy𝜏, which helps both sides.
It makes a pass more informative to recruiters and makes deep study more rewarding to
applicants. Raisingthevalueplacedonunderstanding, 𝐵, helpsonlytherecruiter’sside. Caps
on publication counts [6, 7] lower the weight on output,𝐴, which moves departments away
from the output-dominant regime where test outcomes are ignored.
(viii) Commit in advance to rules for output no one yet produces.In the super-output
model,deptherodesthroughneutraldriftinthelearningprocess. When 𝐴<𝑟/2 ,super-output
alone does not secure a job, so high-potential applicants learn to study deeply. Recruiters
then never see a super-output application, and accepting or rejecting one makes no difference
to their payoff. A recruiter strategy that accepts super-output can therefore spread purely
by chance. Once it does, high-potential applicants switch to shallow study and abandon
depth. When recruiters are committed to rejecting super-output, even while no one produces
it, high-potential applicants study deeply more often. In other words, stating in advance that
output volume alone will not secure a job may therefore protect depth more effectively than
better tests when super-output is possible.
5.1 Related work
Ourmodelbuildsonjob-marketsignaling[21]andcareer-concernsmodels,inwhichemployers
inferabilityfrompastoutput[22–24]. Weuseevolutionarydynamicstostudywhichoutcomes
emerge through learning. This builds on past work applying evolutionary game theory to
humansocialsystems[25,26]. Forthegoalofmakingpredictionsaboutajob-market-signaling
model, the present paper applies evolutionary dynamics (a computational method) in addition
to static game theory (an analytical method), while past work has traditionally relied solely
on the latter. The application of evolutionary dynamics to job-market signaling is relatively
unexplored, although not entirely new [27].
22

Recent studies examine how AI changes the information conveyed by output. Galdin and
Silbert [28] estimate a structural model using data from a digital-labor platform. In their coun-
terfactual,employersbecomelessabletoidentifyhigh-abilityworkerswhenAImakeswritten
applications uninformative. Wang [29] models the pre-doctoral labor market. The model
predictsthatAIcanraiseroutineresearchoutputwhileweakeningitsvalueasasignaloftalent.
CetemenandOzdenoren[30]studyasettingwithabundantAIandopportunitiestoselloutput
on the side. They find that tradable AI output reverses the classic signaling rat race: effort
no longer signals ability, and every worker type under-invests in skill. Our model builds on
thisbodyofworkbyaddingunderstandingasasecondapplicant-sidevariableontopofoutput.
AI’s effects can also vary across settings. Using theory and empirical evidence, Cowgill et al.
[31] find that AI use by job-market and startup-investing applicants can both increase and
decrease screening accuracy depending on the circumstances. Yao [32] analyzes competitive-
programming data, finding that AI-style practice is associated with weaker skill growth in
some groups and stronger skill performance in others. In contrast, our model studies the
idealized setting where AI use by applicants always results in a missed opportunity to build
understanding.
5.2 Limitations
Themodelsimplifiesbothlearningandoutput.(i)Understandingisbinary: deepstudyalways
producesit, andshallowstudyneverdoes.(ii)Outputisalsodeterministic: differentapplicant
types can produce exactly the same output. This creates an idealized form of ambiguity in
the hiring signal, particularly in the baseline model. The super-output extension relaxes this
in part. There, a high-potential applicant produces more output than a medium-potential
applicant whenever both choose the same trajectory. Yet a deep-studying high-potential
applicant and a shallow-studying medium-potential applicant still produce the same output.
(iii)In this model, study costs, applicant composition, and test accuracy are fixed externally
and cannot respond to changes in behavior or hiring practices. Future models could allow
uncertain learning, variable output, and feedback between these factors.(iv)Finally, our
model does not allow applicants to gain understanding while using AI for research. One could
potentially study a model where interactions with AI when writing a paper lead to gaining a
deep understanding of the field. We have excluded this case from our model.
23

AI disclosure statement.We have used Claude Opus 5.5 for helping with writing computer
code and checking the equilibrium analysis of our model. We have also used GPT-6 Astra and
Claude Fable 5.1 for helping us review and revise our work.
Code availability.The code corresponding to this manuscript can be found in the online
repository: https://github.com/Saptarshi07/Effort-Hiring-AI-Game.
Acknowledgments.We are grateful to Harvard University for providing us with AI access.
24

References
[1] OpenAI. “On the Navier–Stokes Millennium Prize Problem,” Sep. 8, 2026. [Online]. Available:
https://openai.com/index/navier-stokes-solution
[2] OpenAI. “Sharing AI progress in mathematics,” Oct. 6, 2026. [Online]. Available:
https://openai.com/index/sharing-ai-progress-in-mathematics
[3] Anthropic. “Learning more about Claude’s mathematical capabilities,” Aug. 10, 2026. [Online].
Available: https://www.anthropic.com/research/riemann-zeta
[4] T. Tao, “Mathematics in the age of AI,” arXiv preprint arXiv:2608.16753, Aug. 17, 2026.
[Online]. Available: https://doi.org/10.48550/arXiv.2608.16753
[5] “Report of Summit on PhD Math Education in the Age of AI,” Harvard University, Department
of Mathematics and Center of Mathematical Sciences and Applications (CMSA), Report,
Sep. 17–18, 2026. [Online]. Available: https://cmsa.fas.harvard.edu/media/2026/09/Summit-on
-PhD-Math-Education-in-the-Age-of-AI.pdf
[6] September 2026 Working Group, “AI and TCS: The next six months,” Simons Institute for the
Theory of Computing, Report, Sep. 28, 2026. [Online]. Available:
https://simons.berkeley.edu/AITCSreport
[7] K. Boboris. “Fair moderation, equitable access, and AI: arXiv’s updated rate limit policy,”
arXiv Blog, Oct. 1, 2026. [Online]. Available:
https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy
[8] M. Pasquato. “What will become of us? Scientific papers in the AI world,” Mario’s Substack,
May 5, 2026. [Online]. Available:
https://mariopasquato.substack.com/p/what-will-become-of-us
[9] D. Craven. “Where will all the papers go?” Proofs and Prompts, Sep. 19, 2026. [Online].
Available: https://proofsandprompts.com/2026/09/19/where-will-all-the-papers-go
[10] T. Chu. “How we can win: A blueprint for the mathematical community,” The Blog of Tasmin
Chu, Sep. 1, 2026. [Online]. Available: https://tasmin.substack.com/p/how-we-can-win
[11] Begin Proof. “Declaration,” n.d. [Online]. Available: https://www.begin-proof.com/declaration
[12] V. Lazić. “Where I stand on AI,” Saarland University, n.d. [Online]. Available: https://www.uni-
saarland.de/lehrstuhl/lazic/prof-dr-vladimir-lazic/vladimir-lazic-where-i-stand-on-ai.html
[13] M. Weinreich, “The crisis of AI-generated mathematics,” arXiv preprint arXiv:2608.02859,
2026. [Online]. Available: https://doi.org/10.48550/arXiv.2608.02859
[14] J. Alper et al., “Leiden Declaration on Artificial Intelligence and Mathematics,” Public
declaration, Jun. 2, 2026. [Online]. Available: https://doi.org/10.5281/zenodo.20302944
[15] S. Roberts, “A call for action: The ‘Leiden Declaration on Artificial Intelligence and
Mathematics’,”Notices of the American Mathematical Society, vol. 73, no. 8, pp. 644–649,
2026. [Online]. Available: https://doi.org/10.1090/noti3386
25

[16] International Council for Industrial and Applied Mathematics (ICIAM). “Statement on
mathematics and artificial intelligence: Discovery, understanding and trust,” Sep. 24, 2026.
[Online]. Available:
https://iciam.org/news/26/9/24/iciam-statement-mathematics-and-artificial-intelligence
[17] Society for Industrial and Applied Mathematics (SIAM). “Editorial policy on artificial
intelligence.” Version 2.0, May 2026. [Online]. Available:
https://epubs.siam.org/artificial-intelligence
[18] Coalition of current and former California Institute of Technology (Caltech) mathematicians.
“Open letter about the Mathathon,” Proofs and Prompts, Sep. 10, 2026. [Online]. Available:
https://proofsandprompts.com/2026/09/10/open-letter-about-the-mathathon
[19] J. Taback. “What does the advent of powerful AI models mean for mathematicians like me?”
What’s New (Terence Tao’s Blog), Oct. 3, 2026. [Online]. Available:
https://terrytao.wordpress.com/2026/10/03/what-does-the-advent-of-powerful-ai-models-me
an-for-mathematicians-like-me
[20] D. Fudenberg and L. A. Imhof, “Imitation processes with small mutations,”Journal of
Economic Theory, vol. 131, no. 1, pp. 251–262, 2006. [Online]. Available:
https://doi.org/10.1016/j.jet.2005.04.006
[21] M. Spence, “Job market signaling,”Quarterly Journal of Economics, vol. 87, no. 3,
pp. 355–374, 1973. [Online]. Available: https://doi.org/10.2307/1882010
[22] B. Holmström, “Managerial incentive problems: A dynamic perspective,”Review of Economic
Studies, vol. 66, no. 1, pp. 169–182, 1999. [Online]. Available:
https://doi.org/10.1111/1467-937X.00083
[23] R. Gibbons and K. J. Murphy, “Optimal incentive contracts in the presence of career concerns:
Theory and evidence,”Journal of Political Economy, vol. 100, no. 3, pp. 468–505, 1992.
[Online]. Available: https://doi.org/10.1086/261826
[24] M. Dewatripont, I. Jewitt, and J. Tirole, “The economics of career concerns, Part I: Comparing
information structures,”Review of Economic Studies, vol. 66, no. 1, pp. 183–198, 1999.
[Online]. Available: https://doi.org/10.1111/1467-937X.00084
[25] D. D. P. Johnson and J. H. Fowler, “The evolution of overconfidence,”Nature, vol. 477,
no. 7364, pp. 317–320, 2011. [Online]. Available: https://doi.org/10.1038/nature10384
[26] M. Hoffman, C. Hilbe, and M. A. Nowak, “The signal-burying game can explain why we
obscure positive traits and good deeds,”Nature Human Behaviour, vol. 2, no. 6, pp. 397–404,
2018. [Online]. Available: https://doi.org/10.1038/s41562-018-0354-z
[27] J. Hofbauer and C. Pawlowitsch, “The evolutionary dynamics of costly signaling,”International
Journal of Game Theory, vol. 54, no. 1, 2025, Art. no. 23. [Online]. Available:
https://doi.org/10.1007/s00182-025-00927-5
[28] A. Galdin and J. Silbert, “Making talk cheap: Generative AI and labor market signaling,” arXiv
preprint arXiv:2511.08785, 2025. [Online]. Available:
https://doi.org/10.48550/arXiv.2511.08785
26

[29] S. Wang, “Hope, signals, and silicon: A game-theoretic model of the pre-doctoral academic
labor market in the age of AI,”Research Policy, vol. 55, no. 8, 2026, Art. no. 105568. [Online].
Available: https://doi.org/10.1016/j.respol.2026.105568
[30] D. Cetemen and E. Ozdenoren, “AI and the market for signals,” arXiv preprint
arXiv:2609.17752, 2026. [Online]. Available: https://doi.org/10.48550/arXiv.2609.17752
[31] B. Cowgill, P. Hernández-Lagos, and N. L. Wright, “Does AI cheapen talk? Theory and
evidence from global entrepreneurship and hiring,”Management Science, 2026, Advance
online publication. [Online]. Available: https://doi.org/10.1287/mnsc.2024.07027
[32] S. Yao, “When the scaffold stays on: AI, practice style, and screening in elite skill formation,”
arXiv preprint arXiv:2606.06253v4, Sep. 2, 2026. [Online]. Available:
https://doi.org/10.48550/arXiv.2606.06253
[33] A. Traulsen, M. A. Nowak, and J. M. Pacheco, “Stochastic dynamics of invasion and fixation,”
Physical Review E, vol. 74, no. 1, 2006, Art. no. 011909. [Online]. Available:
https://doi.org/10.1103/PhysRevE.74.011909
27

A Methods
Imitation and rare exploration in applicant and recruiter populations
Populations and payoffs.We model learning in three finite populations, each of size𝑁:
high-potential applicants (𝐻), medium-potential applicants (𝑀), and recruiters (𝑅). Each ap-
plicant chooses an action𝑎∈{𝐷,𝑆} (deep or shallow). Each recruiter uses a pure acceptance
rule𝜌, which specifies whether to accept (𝜌𝑜=1 ) or reject (𝜌𝑜=0 ) after each observation𝑜.
In the baseline model, the observations are(1,𝑃) ,(1,𝐹) ,(0,𝑃) , and(0,𝐹) , giving24=16
rules. In the super-output model, recruiters additionally respond to𝑦=2through𝜌2, giving
25=32 rules. We let recruiters condition on𝑦=2 alone, because super-output is produced
only by high-potential applicants who went shallow; the test result therefore carries no further
information about understanding.
Low-potential applicants are non-strategic and are not a learning population. They are a
fixed share𝜋𝐿 of every applicant pool and produce(𝑦,𝑢)=(0,0) , and pass the test with
probability 1−𝜏 . Their effect enters the dynamics only through the recruiters’ payoffs. A
recruiter who accepts few-paper applicants also hires low-potential ones, which lowers its
payoff by𝑟𝜋𝐿
(1−𝜏)𝜌 0𝑃+𝜏𝜌 0𝐹 .
Payoffs are expected values against the current composition of theotherpopulations. An
applicant of type𝜃∈{𝐻,𝑀}playing𝑎earns
𝑈𝜃(𝑎)=𝑊Pr(hired|𝜃,𝑎)−𝛿 𝜃1{𝑎=𝐷},
where the probability of being hired is averaged over the test outcome and the recruiters’ rule.
A recruiter using rule𝜌against applicant actions(𝑎𝐻,𝑎 𝑀)earns
𝑈𝑅(𝜌)=
∑︁
𝜃∈{𝐻,𝑀,𝐿}
𝜋𝜃 E

(𝐴𝑦+𝐵𝑢−𝑟)𝜌 𝑜

,
where the expectation is over the observation𝑜 produced by type𝜃. Population sizes are
therefore equal, but recruiters meet the three types in proportions𝜋𝐻, 𝜋𝑀, 𝜋𝐿, which are
exogenously set for the simulation. No agent’s payoff depends on the composition of its own
population.
28

Imitationandexploration.Ineachtimestep,onepopulationischosenwithprobability 1/3.
With probability1−𝜀 , a randomly chosen focal agent compares itself with a randomly chosen
role model from the same population. It adopts the role model’s strategy with probability
1+𝑒−𝛽(𝑈model−𝑈focal)−1 ,where 𝛽⩾0 istheselectionstrength. Thisisthepairwise-comparison
(Fermi)rule[33]. Withprobability 𝜀,thefocalagentinsteadexplores: itswitchestoastrategy
drawn uniformly from the other strategies available to its population.
Rare exploration.We analyze the limit𝜀→0 [20]. Exploration is then so rare that each
new strategy either takes over its population or disappears before the next one arises. The
process therefore spends almost all its time in monomorphic states𝑠=(𝑎 𝐻,𝑎 𝑀,𝜌) , of which
there are4×16=64 in the baseline model and4×32=128 in the super-output model.
Consider a single explorer whose payoff exceeds that of the residents byΔ. Because its own
population’s composition does not affect payoffs,Δ stays constant while the new strategy
spreads. Its probability of taking over the population is exactly
𝜙(Δ)=
 

1−𝑒 −𝛽Δ
1−𝑒 −𝑁𝛽Δ, 𝛽Δ≠0,
1/𝑁, 𝛽Δ=0.
From state𝑠, the process moves to a state that differs only in𝑎𝐻 with probability 1 3𝜙(Δ𝐻),
and similarly for𝑎𝑀. It moves to a state that differs only in the recruiter rule,𝜌→𝜌 ′, with
probability 1 3𝜙(Δ𝑅)/(|R|−1) , where|R| is the number of recruiter rules. Here, eachΔis the
payoff of the new strategy minus that of the resident, evaluated at𝑠. We compute the unique
stationary distributionΠof this chain exactly by solving a linear system.
Reported quantities.We report two kinds of quantities, with no classification of states
into equilibria. The first is the long-run probability that each applicant population plays each
action: for example,Pr(𝑎𝐻 =𝐷)= ˝ 𝑠:𝑎𝐻=𝐷Π(𝑠). The second is the long-run probability
that recruiters accept after each observation,˝ 𝑠Π(𝑠)𝜌 𝑜(𝑠), where𝜌𝑜(𝑠) is the response to
𝑜 under the rule in state𝑠. Two rules that differ only after an observation that no current
applicant produces earn identical payoffs. Switching between them is neutral (𝜙=1/𝑁 ),
which is the learning counterpart of the freedom in off-path beliefs. Observations that occur
only rarely, such as a passed test by a low-potential applicant, are not neutral; they are only
weakly selected.
29

Parameters for learning simulations.Unless stated otherwise,𝑁=30 ,𝛽=5 ,𝜋𝐻 =0.3 ,
𝜋𝑀 =0.5 ,𝜋𝐿 =0.2 ,𝛿𝐻 =0.2 ,𝛿𝑀 =0.4 , and𝑟=𝑊=1 . We use𝜏∈{0.5,0.9,0.99} and a
101×101grid with𝐴∈[0,1.5]and𝐵∈[0,2].
30
