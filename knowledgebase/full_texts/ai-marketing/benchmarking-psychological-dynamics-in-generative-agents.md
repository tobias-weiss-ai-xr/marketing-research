---
title: Benchmarking Psychological Dynamics in Generative Agents
url: https://arxiv.org/abs/2610.04246
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Sumer S. Vaid
- Ashley V. Whillans
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.04246
pages: 18
chars: 67307
fetched_at: '2026-11-08T13:24:03+00:00'
kb_version: 1
---

# Benchmarking Psychological Dynamics in Generative Agents

Published at the AI Measurement Science Workshop at COLM 2026
Benchmarking Psychological Dynamics in Generative Agents
Sumer S. V aid∗
AI Institute
Harvard Business School
Ashley V . Whillans
Negotiation, Organizations & Markets Unit
Harvard Business School
Abstract
Large language models (LLMs) are increasingly deployed to simulate hu-
man behavior, acting as computational replicas of human subjects. Yet
the lived psychological experience of humans is difficult to benchmark,
particularly as it unfolds over time. We introduce a psychometric bench-
mark forcomputational replicas: personas that carry a fixed identity through
an evolving sequence of events. Built entirely from published norms and
meta-analytic effects, the benchmark scores two dimensions of psycho-
logical realism. The first, internal validity, quantifies whether generated
trajectories reproduce the internal structure of repeated human measure-
ment: distributions, the between- versus within-person variance partition,
temporal dependence, and range. The second, external validity, quantifies
whether replicas recover established trait, state, and indicator relations.
Across 36 open-weight and proprietary LLMs from nine developers (1B–
671B parameters), most recover thedirectionof established relations (84.3%
mean agreement) and the variance partition (26 of 34), yet thewithin-person
correlationand distributional structure elude recovery. Internal validity is
independent of scale and capability: a mid-size open LLM (Gemma-3-27B)
strikes the best trade-off between the two dimensions. The benchmark is a
precondition for using computational replicas in causal inference across do-
mains (e.g., marketing, healthcare), and identifies within-person grounding
as the central challenge ahead.
1 Introduction
One of the most promising applications of AI is the ability to simulate how humans think,
feel and behave (Argyle et al., 2023; Grossmann et al., 2023; Serapio-Garc ´ıa et al., 2023).
Large language models are increasingly deployed to model cognitive processes, economic
behaviors, and social interactions, effectively acting as computational replicas for human
subjects (Horton et al., 2023; Binz et al., 2025; Park et al., 2023). The scientific standards
governing the evaluation and quantifying the realism of computational replicas have re-
ceived surprisingly limited empirical attention (Ye et al., 2025). Despite the proliferation
of benchmarks that peg the performance of AI on specific tasks, it remains challenging to
quantify the relative success of different technical approaches in recreating the psychological
richness of humans’ lived experiences (Santurkar et al., 2023; Atari et al., 2023).
Historically, the evaluation of personas has relied on static, cross-sectional measurements
(Hu et al., 2026). LLMs are prompted to adopt an identity and respond to an isolated query,
yielding a single-point estimate of behavior (Park et al., 2024). Yet human psychology is in-
trinsically dynamic (Nesselroade, 1991), continuously adapting to accumulating contextual
feedback. Relying on isolated snapshots limits our capacity to build valid computational
models of complex behavior. For LLMs to function as reliable simulators of human psychol-
ogy, they must demonstrate realism in how their patterns of thinking, feeling and behaving
change over time (Gonnermann-M ¨uller et al., 2026). They must possess the capacity to
mimic how humans process sequences of interlaced events, integrate various contextual
changes, and reflect the cumulative impact of time on psychological states.
∗Corresponding author:svaid@hbs.edu
1
arXiv:2610.04246v1  [cs.HC]  3 Oct 2026

Published at the AI Measurement Science Workshop at COLM 2026
We introduce a new paradigm to benchmark the psychological dynamics of computational
replicas. In this paradigm, computational replicas are endowed with a stable identity and
exposed to an evolving sequence of environmental events. By measuring the persona’s
psychological state at each timestep, we capture a continuous trajectory rather than a static
snapshot. As AI-based systems scale from isolated experimental replications (Argyle et al.,
2023; Aher et al., 2023; Horton et al., 2023) to person-specific computational replicas (Park
et al., 2024), isolating computational cognition from statistical artifact becomes a paramount
scientific necessity. A scientifically viable persona must demonstrate both core psychological
stability and adaptive, contextually grounded dynamics. This verification lets the field
ground a science of synthetic behavior in valid simulations of human mechanics rather than
the biases of the underlying LLM.
We introduce a comprehensive psychometric benchmark designed to evaluate longitudinal
psychological state trajectories within synthetic populations. We define psychological
realism through two distinct dimensions: whether generated trajectories reproduce the
internal dynamics of repeated human measurements, and whether they recover established
psychological relations documented in the past literature. We execute this benchmark
on a simulated cohort of 300 population-grounded synthetic employees observed across
6 continuous workdays. By evaluating 36 open-weight and proprietary LLMs—drawn
from nine developers and spanning nearly three orders of magnitude in scale (1B–671B
parameters)—tasked with generating daily measures of work engagement, psychological
safety, creativity, and team trust, we establish a highly auditable baseline. This framework
provides the necessary computational infrastructure to compare how accurately temporal
computational replicas and other generative simulations reproduce valid, context-sensitive
psychological states over time. Validating these individual dynamics is a strictly necessary
precursor to robust causal inference, a core use case for these emerging technologies. Valid
counterfactual simulation requires an accurate structural representation of the underlying
temporal data-generating process (Pearl, 2009; Hern ´an & Robins, 2020). With validated
within-person dynamics, a persona can address causal questions about change over time,
such as how a shift in workload would move employee engagement over a week (Vaid &
Whillans, 2026).
2 Related Work
2.1 The Limits of Cross-Sectional Evaluation
The computational modeling of human behavior initially demonstrated remarkable success
in replicating static population distributions. Early frameworks established that LLMs could
output survey responses and replicate behavioral experiments by matching macroscopic
cross-sectional data (Argyle et al., 2023; Aher et al., 2023; Horton et al., 2023; Binz & Schulz,
2023). This capacity quickly expanded into generating synthetic data for human-computer
interaction research (H¨am¨al¨ainen et al., 2023), where LLMs effectively substituted for hu-
man crowdsource workers on discrete tasks (Dillion et al., 2023). However, recent method-
ological critiques highlight that evaluating these LLMs frequently defaults to single-trial,
response-level elicitation (Cummins, 2025). This reliance on isolated snapshots introduces
unconstrained analytic flexibility, masking whether a LLM possesses stability or merely
outputs context-dependent artifacts tailored to a specific prompt string.
This limitation is particularly evident in recent comprehensive cross-sectional benchmarks.
Frameworks such as SimBench (Hu et al., 2026) and OdysSim (Zhou et al., 2026) pro-
vide extensive infrastructure for evaluating how well LLMs replicate human behavior
across diverse populations and tasks. Yet, investigations into survey-response consis-
tency (Dominguez-Olmedo et al., 2024) and one-shot persona expression (Jiang et al., 2024)
demonstrate that matching a cross-sectional distribution leaves temporal continuity an open
question. These static paradigms successfully validate localized demographic matching
but conflate a LLM’s capacity to output a probable text string with the possession of a
stable, underlying behavioral architecture (Lin, 2025; Vendrow et al., 2025). Static framing
also stands apart from interactive measurement, where adaptive psychometric methods
select items by their information content and estimate a LLM’s trait position as responses
accumulate (Li et al., 2025; Kipnis et al., 2025).
2

Published at the AI Measurement Science Workshop at COLM 2026
2.2 Alignment Compression and Statistical Priors
Transitioning from static generation to longitudinal simulation exposes trade-offs in the
underlying alignment of these architectures. As LLMs undergo instruction tuning and
safety alignment, they suffer a measurable reduction in conceptual and behavioral diversity
(Murthy et al., 2025; Kirk et al., 2024; Rios-Sialer, 2026). We define this compression as a mea-
surable loss of behavioral diversity: alignment forces the distribution of generated responses
toward a normative consensus. This phenomenon mirrors the alignment-simulation tradeoff
identified in cross-sectional benchmarks, where instruction tuning improves performance
on consensus-driven questions but actively degrades the LLM’s ability to simulate diverse
edge cases (Hu et al., 2026).
This compression is a consistent bias rather than random variance. The resulting loss of
variance is observable in LLMs exhibiting pronounced sycophancy (Sharma et al., 2024) and
artificially elevated baseline rationality (Liu et al., 2025), and in the documented compression
of opinion and trait distributions toward the center of the training corpus (Santurkar et al.,
2023; Bisbee et al., 2024). Because alignment naturally reduces cognitive diversity, the
generated personas cluster at the center of the training distribution. When applied to
complex environments like organizational simulation, the erasure of individual variance
eliminates the diversity necessary to model realistic human dynamics (Wang et al., 2025;
Kolluri et al., 2025). Recent work reframes this failure as a problem of support coverage
rather than density matching, evolving persona generators that span the full landscape of
human traits and recover the variance that standard alignment removes (Paglieri et al., 2026).
Rigorous longitudinal measurement is what lets researchers distinguish valid simulated
behavior from the generative compression inherent to the base LLM (Gao et al., 2025). A
related validity threat arises under strategic optimization: a persona that infers it is under
evaluation may skew its self-reports toward desirable poles (Needham et al., 2025; Salecha
et al., 2024) or deliberately underperform when an objective rewards it (van der Weij et al.,
2024; Meinke et al., 2024; Greenblatt et al., 2024).
2.3 Architectural Bottlenecks Over Time
Preliminary attempts to sustain personas reveal architectural constraints in processing
long-term state changes. While LLMs can express specific personality traits in isolated
evaluations (Jiang et al., 2024; Serapio-Garc´ıa et al., 2023; Shanahan et al., 2023), simulating
these traits over extended interactions exposes systematic drift (Gonnermann-M ¨uller et al.,
2026; Mooney et al., 2025). Formal analyses of agent-based social simulations indicate that
personas reliably decay toward an average, homogenous identity as context lengths increase
(Taillandier et al., 2025; Luo & Laban, 2026). This homogenization suggests that current
LLMs struggle to maintain specialized, individual-level variance over extended temporal
horizons.
Mechanistic investigations attribute this decay directly to inherent working-memory limits
within transformer architectures (Gong & Zhang, 2024). Although constrained repeated-
game scenarios show initial promise in following path-dependent variables like trust (Xie
et al., 2024), discrete prompt engineering can stabilize specific value alignments (Rozen et al.,
2025), and multi-turn reinforcement learning can reduce persona inconsistency (Abdulhai
et al., 2025), these interventions act as localized patches rather than structural solutions.
More recent training approaches target internal state alignment rather than surface imitation
(Wu et al., 2026), yet they optimize for response accuracy and stop short of certifying coher-
ence across time. The broader absence of temporal stability complicates the deployment
of complex synthetic populations. Moving from heuristic prompt adjustments to formal
psychometric validation (Ye et al., 2025) is a mandatory step to ensure personas maintain
coherent identity trajectories.
2.4 The Necessity of Longitudinal Measurement
Despite these limitations, the field is rapidly advancing toward multi-agent paradigms
(Park et al., 2023; Piao et al., 2025). Theoretical frameworks increasingly position multi-agent
systems as a new paradigm for social science (Haase & Pokutta, 2025; Anthis et al., 2025).
Furthermore, researchers hypothesize that single LLMs can act as universal substrates to pre-
3

Published at the AI Measurement Science Workshop at COLM 2026
dict and capture cross-domain human cognition (Binz et al., 2025). These theoretical LLMs
presume that the underlying personas possess the capacity to integrate experience, update
their internal states, and exhibit path-dependent development over time. They assume the
existence of a stable temporal architecture that still awaits psychometric verification.
In practice, applied systems are already being deployed in high-stakes longitudinal con-
texts. Computational replicas are increasingly utilized in prolonged educational simulations
(Mannekote et al., 2025) and continuous psychological counseling frameworks (Hu et al.,
2025). These deployed systems operate under the unvalidated assumption of continuous
temporal coherence, and they contend with an instrument that itself drifts: deployed LLMs
change across silent updates (Chen et al., 2024) and the preferences they encode shift over
time (Son et al., 2025), so a longitudinal standard must separate intended development from
artifactual movement of the underlying LLM. A nascent literature on validating simulations
as behavioral evidence has begun to formalize what such validation requires, distinguishing
several strategies and their limits (Hullman et al., 2026; Hewitt et al., 2024), while related
analyses caution that distributional realism can coexist with incorrect causal effects (Cui
et al., 2025; Li & Ji, 2026). Our framework addresses this precise methodological void. By
establishing a rigorous standard for measuring longitudinal coherence, we provide the
computational precondition required to advance beyond static evaluations. This auditing
infrastructure secures the architectural foundation necessary to validate temporal compu-
tational replicas (Park et al., 2024; Toubia et al., 2025; Koaik et al., 2026) and ensure they
function as reliable engines for longitudinal simulation.
3 Creating the Benchmark
3.1 Population Initialization
We initialize synthetic populations from published norms rather than LLM guesswork,
so every seed parameter traces to a human dataset rather than the generation LLM’s
assumptions (Gao et al., 2025). Each persona’s Big Five traits are drawn from a multivariate
normal grounded in population norms and meta-analytic intercorrelations (Soto et al., 2011;
van der Linden et al., 2010), and state baselines are linear functions of those traits using
established coefficients (Christian et al., 2011; Frazier et al., 2017; Feist, 1998; Colquitt et al.,
2007). We decompose each state’s total variance into stable between-person and dynamic
within-person components by scaling its standard deviation with published intraclass
correlations, following the experience-sampling tradition (Nesselroade, 1991; Podsakoff
et al., 2019). The benchmark targets four workplace states: work engagement, the vigor
and absorption a person brings to work (Schaufeli et al., 2002); psychological safety, a
shared confidence that the team tolerates interpersonal risk (Edmondson, 1999); workplace
creativity, the generation of novel and useful ideas (Amabile, 1988); and team trust, a
willingness to be vulnerable to a team’s actions (Mayer et al., 1995). A rich tradition in
personality and organizational psychology separates such states from traits: traits are stable
between-person dispositions, while states fluctuate within the individual around a personal
baseline and aggregate over time into the trait (Fleeson, 2001; Molenaar, 2004; Curran &
Bauer, 2011). The benchmark measures whether generative digital twins reproduce realistic
within-person fluctuation in these psychological states under salient daily context. Daily
contextual indicators are sampled forward as inputs while the target state columns stay
unpopulated, so any recovered indicator-state relation is emergent rather than seeded (Gao
et al., 2025). We initialize 300 personas over 6 simulated days; the full seeding construction
appears in Appendix B.
3.2 Persona Generation
We employ a shared-event architecture to strictly control environmental variance (Hu et al.,
2026). For each seeded persona, we generate an identity portrait and a continuous sequence
of daily narratives conditioned on the evolving contextual inputs. This generation occurs
exactly once using a fixed event LLM. During the evaluation phase, every benchmarked
LLM processes these identical narratives under a uniform prompt structure.
4

Published at the AI Measurement Science Workshop at COLM 2026
Each LLM is tasked with quantifying the four psychological states in the workplace at the
conclusion of each daily timestep, outputting values on their native psychometric scales.
Because all LLMs rate identical narratives, differences in ratings reflect the capability of the
LLM rather than the events. For every evaluated LLM, this procedure yields a complete
behavioral trajectory spanning 6 discrete state vectors across the entire 300 persona cohort.
3.3 Two Dimensions of Psychological Realism
The benchmark scores a synthetic population on two dimensions, following the construct-
validity distinction between a measure’s internal structure and its relations to other measures
(Cronbach & Meehl, 1955; Campbell & Fiske, 1959).
Internal validitycompares the synthetic corpus to published human norms on the statistical
properties of experience-sampling data, using two one-sided equivalence tests with persona-
level resampling (Lakens, 2017). The criteria are the mean and spread of each state, the
between- and within-person variance partition, within-person variability, cross-state corre-
lations, the within-person autoregressive coefficient, latent dimensionality, and scale-range
use; Appendix C defines each. Together these properties describe how a psychological state
behaves under repeated measurement, and a faithful computational replica must match
them all. We report two criteria in adjusted form because the design limits their identifica-
tion: a one-factor model over four indicators is under-identified (Kline, 2016), so we report
multilevel eigenstructure in its place, and over 6 days the autoregressive coefficient is biased
by the short panel (Nickell, 1981; Hamaker et al., 2015), so we treat it as directional.
External validityexamines whether the relationships in the synthetic data match those
established in human research, at two levels. Between persons, we test whether a persona’s
traits predict their average states (theirtrait–staterelations), as meta-analyses report; for
example, more conscientious personas should be more engaged. Within persons, we test
whether a persona’s daily context predicts the state they report that day (theirindicator–state
relations), by correlating each day’s indicators with each day’s states after subtracting the
persona’s own average (Enders & Tofighi, 2007; Curran & Bauer, 2011). A known-groups
test adds a final check: more neurotic personas should report lower engagement on average
and larger day-to-day swings (Fleeson, 2001).
4 Experimental Setup
We deploy this benchmark across a broad roster of 36 LLMs drawn from nine developers
and spanning 1B–671B parameters, nearly three orders of magnitude in scale. This cohort
spans dense parameter ladders, state-of-the-art mixture-of-experts architectures, specialized
reasoning engines, and both open-weight and proprietary frontier systems. We analyze the
34 LLMs that produced complete longitudinal corpora.
As established in the shared-event protocol, identity portraits and sequential daily narratives
are generated exactly once using a fixed event model. Every benchmarked LLM then
processes this shared corpus under a strictly uniform prompt architecture. To execute this
at scale, the generation and rating pipelines operate concurrently and are fully resumable.
The orchestration infrastructure includes integrated budgetary halts and an automated
error-rate circuit breaker to ensure systemic stability during large-scale inference.
We quantify external nomological convergence using direction agreement, defined as the
proportion of simulated relations where the algebraic sign correctly matches the established
literature, alongside signed rank correlations across the complete relation set. Internal
validity is summarized through rigorous two one-sided tests equivalence verdicts (Lakens,
2017) and continuous distance metrics. The primary continuous diagnostic is thewithin-
person variance error: the absolute log-ratio of the synthetic within-person standard deviation
to the target human standard deviation. In this formulation, lower absolute values indicate
a closer match to the human within-person variance structure.
5

Published at the AI Measurement Science Workshop at COLM 2026
5 Results
We report the outcomes of our diagnostic framework across the 34 evaluated LLMs along
two axes.Internal validityexamines whether a synthetic population reproduces the longi-
tudinal structure of repeated human measurement—most directly, whether its day-to-day,
within-person variability matches the human norm.External validityexamines whether the
population recovers established psychological relations in the correct direction. Figure 1
reports internal validity by psychological state for the leading LLMs; Figure 2 reports both
axes against LLM scale.
5.1 The Divergence of Scale and Internal V alidity
A naive observer, extrapolating from scaling laws (Kaplan et al., 2020; Hoffmann et al., 2022)
and the broad capability gains larger models display (Kipnis et al., 2025; Binz et al., 2025),
would assume that larger and more capable LLMs produce synthetic populations whose
psychological states display high internal validity (e.g., human-like day-to-day variability)
and external validity (e.g., higher neuroticism predicting lower engagement). A larger
LLM attains lower predictive loss by capturing more of what its training data contains: the
documented relations that external validity measures, and the distributional and temporal
regularities that internal validity measures. On both axes, a higher parameter count should
therefore buy more faithful trait–state relations and more realistic within-person dynamics.
Our benchmark shows otherwise. Fitting each validity metric against log parameter count
within LLM families, we find that general capability and internal validity move largely
independently.
We observe sharp divergences in how different architectures process temporal sequences.
The smallest within-person variance error is attained by a mid-size open LLM (Gemma-2-
27B, 0.043, where lower values indicate closer alignment to human targets), narrowly ahead
of the most mathematically capable frontier LLM (0.061). Conversely, the most compact
Gemma architecture exhibits the largest variance error in the clean roster (0.427) while still
matching the direction of established relations at a rate comparable to far larger LLMs
(74.6% pooled directional agreement). No single architecture leads across both internal and
external metrics. External validity remains remarkably constant across the capability range,
whereas internal validity fluctuates unpredictably; across the roster the two axes are largely
independent (Appendix Figure 3, r≈ 0.17). The internal battery separates what LLMs
reproduce from what they miss. The between- versus within-person variance partition
(L2) and the range criterion (L7) are met by most of the roster (26, 34 of 34 populations);
distributional shape (L1), cross-state correlations (L3), the full multilevel eigenstructure (L6)
are met by few. The best population clears 3 of the 6 levels, so the synthetic populations
reproduce the variance architecture of repeated human measurement while stopping short
of its distributional and relational detail. Two criteria warrant added caution: the cross-state
(L3) targets remain literature placeholders rather than verified anchors, and the within-
person temporal criterion (L4) is reported as directional evidence only—at 6 days the
autoregressive coefficient is non-identifiable, so credible estimation of personadynamics
requires longer trajectories than the experience-sampling horizon used here.
5.2 Compression of the Within-Person Correlation
While the synthetic populations demonstrate a robust capacity to recover the directional
signs of established psychological relations, they systematically fail to recover the within-
person correlation that these effects imply. Recovering direction is distinct from recovering
that correlation. The trait–state network is recovered well: signs align with published
coefficients in a mean 84.3% of cases (range 75%–100%), the strongest external-validity
signal in the benchmark. Within persons, daily indicators move states in literature-consistent
directions in approximately three-quarters of relations (72.6%).
Yet the simulated effects are compressed toward zero. The pooled within-person correlations
hover near an absolute value of 0.05, whereas the published human effects range from 0.20 to
0.70. This compression of the within-person correlation is uniform across the entire capability
spectrum, rather than a localized failure of smaller LLMs. These LLMs correctly identify that
a specific environmental indicator should push a psychological state in a particular direction,
6

Published at the AI Measurement Science Workshop at COLM 2026
Engagement Psych. safety Creativity Team trust
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40
Within-person variance error
|ln(SDsynth/SDtarget)| (lower better)
equiv. margin (1.5×)
Within-person variance error by state (top-5 models)
Gemma-2-27B
GPT-5-5
Gemma-3-27B
Qwen-2-5-Coder-32B
Claude-Sonnet-4
Figure 1: Internal validity by psychological state for the top-five LLMs: the absolute log-ratio
of synthetic to human within-person SD, where lower is closer to the human norm. The
dashed line marks the equivalence margin (1.5×). LLMs match the within-person variance
of engagement and trust more closely than psychological safety.
100 101
Parameters (B, log scale)
50
60
70
80
90
100Nomological direction agreement (%)
chance
Gemma-2
Gemma-3
Llama-3.x
Mistral
Phi
Qwen2.5
Qwen3
100 101
Parameters (B, log scale)
0.1
0.2
0.3
0.4Within-person variance error
Validity vs. model scale, by family
Figure 2: Validity versus LLM scale, by family. External validity (left, direction agreement)
is high and roughly flat across parameter count; internal validity (right, within-person
variance error) varies sharply and is led by mid-size LLMs rather than the largest.
yet they lack the capacity to drive that state change with the appropriate statistical force.
Between persons, indicator–state convergence falls to 55.5%, near chance, because the seeded
daily indicators carry no trait-linked between-person variance by construction; the trait–state
network, rather than the indicator network, is therefore the population-level external check.
We probed whether this compression is an artifact of the rating protocol. Re-rating identical
narratives yields a single-rating reliability of 0.97, so the reliability correction is negligible;
the within-person correlation is moreover invariant to rating temperature and to a battery of
prompt interventions that de-anchor the rater from its trait baseline. Across every condition
the within-person correlation is unmoved and sits at the sampling noise floor (0.023 at 1,800
person-days). The compression is therefore an inherent property of the synthetic process
rather than an instrument effect: the within-person daily signal is intrinsically faint. Its
direction and rank are nonetheless recovered (71%–77% sign agreement, ρ= 0.38–0.46
against meta-analytic effects), and removing the baseline anchor sharpens this directional
recovery while leaving the within-person correlation untouched. The quantity at issue is
thus the within-personstructureof the synthetic trajectories measured against published
effects; recovering the realized state movements of specific human individuals is a distinct
7

Published at the AI Measurement Science Workshop at COLM 2026
and harder problem that demands longitudinal ground truth and lies beyond an all-silico
evaluation.
5.3 Cross-Cultural Invariance and Demographic Simulation
To test the resilience of the generated trajectories across diverse populations, we re-initialized
the personas for six distinct nations using Hofstede-informed trait offsets and re-executed
the diagnostic battery. The resulting measurement invariance is exceptionally strong. The
per-culture cross-state correlational structures depart from the baseline global structure by a
mean absolute difference of 0.014 to 0.038.
This deviation sits far below conventional threshold limits for breakdown. Furthermore,
the simulated cross-group differences match the published Hofstede-anchored directions
in up to 75% of the evaluated cases, with power-distance effects on psychological safety
and creativity recovered consistently. The capability divergence recurs: the larger Gemma-
3-27B barely differentiates cultures, whereas the smaller Gemma-3-4B differentiates them
strongly. These results indicate that when personas are anchored with precise demographic
priors, the LLMs keep a consistent cross-state correlation pattern across cultures while still
distinguishing one from another.
6 Discussion
The LLMs we evaluate recover the direction of established psychological relations with high
accuracy. Building upon the foundational cross-sectional matching demonstrated in past
research (Argyle et al., 2023; Aher et al., 2023; Horton et al., 2023), our diagnostic framework
confirms that LLMs successfully internalize the established trait–state relations we test
(Serapio-Garc´ıa et al., 2023; Binz et al., 2025; Park et al., 2023). Moreover, the evaluated
cohort achieved high external validity, recording a mean direction agreement of 84.3%
across all meta-analytic targets. Furthermore, precise demographic priors kept the cross-
state correlation pattern consistent across cultures while preserving the differences between
them. These findings indicate that current LLMs correctly identify how an environmental
indicator should influence the workplace states we study (Grossmann et al., 2023).
However, this qualitative success masks a critical architectural bottleneck regarding lon-
gitudinal variance. We observe a systematic divergence between general computational
capability and internal validity. While LLMs correctly predict the direction of a psycholog-
ical shift, they consistently fail to reproduce the within-person correlation and temporal
variance of these states. This systemic compression of the within-person correlation is a
consistent bias rather than random noise. As shown in past research (Murthy et al., 2025),
instruction tuning actively reduces cognitive diversity. This aligns with limitations iden-
tified across related work on alignment and automated simulation (Santurkar et al., 2023;
Atari et al., 2023; Manning et al., 2024), where the optimization gradient forces generated
responses toward a normative consensus, thereby compressing the variance required for
dynamic population simulation.
Securing temporal coherence is a strictly necessary precondition for conducting robust causal
inference with synthetic computational replicas. Valid counterfactual simulation requires an
accurate structural representation of the underlying temporal data generating process, as
established in foundational work on causal inference (Pearl, 2009; Hern´an & Robins, 2020).
Applied frameworks frequently deploy computational replicas in longitudinal contexts
under the unvalidated assumption of continuous stability (Park et al., 2024; Gonnermann-
M ¨uller et al., 2026). Yet our results illustrate that distributional realism and directional
accuracy can easily coexist with incorrect causal effect sizes (Hu et al., 2026). Moving from
heuristic prompt adjustments to formal psychometric validation ensures that the science of
synthetic behavior rests on verified psychological dynamics rather than LLM artifacts.
7 Conclusion
Transitioning from static personas to longitudinal computational replicas exposes a gap
between directional and quantitative fidelity when LLMs rate an extended record of experi-
ence (Park et al., 2024; Gonnermann-M ¨uller et al., 2026). By framing longitudinal coherence
8

Published at the AI Measurement Science Workshop at COLM 2026
as a rigorous measurement problem, we establish a highly auditable standard for validating
synthetic psychological trajectories. The demonstrated success in directional alignment
proves that LLMs hold immense promise for organizational and psychological simulation
(Argyle et al., 2023; Grossmann et al., 2023; Vaid & Whillans, 2026). However, the simul-
taneous divergence between LLM scale and within-person variance recovery mandates a
shift in how the field evaluates these systems. Researchers must verify the stability of the
underlying LLMs before deploying them to simulate populations over time.
Reproducibility Statement
The validation battery, generation pipeline, LLM scoring code, generated corpora for all
36 models, result tables with provenance manifests, and random seeds are released as
PsyDyBench at https://github.com/sumervaid/PsyDyBench. A single script regenerates
every table, figure, and reported number from the released corpora without API access.
References
Marwa Abdulhai, Ryan Cheng, Donovan Clay, Tim Althoff, Sergey Levine, and Natasha
Jaques. Consistently simulating human personas with multi-turn reinforcement learning,
2025. URLhttps://arxiv.org/abs/2511.00222.
Gati Aher, Rosa I. Arriaga, and Adam Tauman Kalai. Using large language models to
simulate multiple humans and replicate human subject studies. InProceedings of the 40th
International Conference on Machine Learning (ICML), 2023. URL https://arxiv.org/abs/
2208.10264.
Teresa M. Amabile. A model of creativity and innovation in organizations.Research in
Organizational Behavior, 10:123–167, 1988.
Jacy Reese Anthis, Ryan Liu, Sean M. Richardson, Austin C. Kozlowski, Bernard Koch,
James Evans, Erik Brynjolfsson, and Michael Bernstein. LLM social simulations are a
promising research method. InProceedings of the 42nd International Conference on Machine
Learning (ICML), 2025. URLhttps://arxiv.org/abs/2504.02234.
Lisa P . Argyle, Ethan C. Busby, Nancy Fulda, Joshua R. Gubler, Christopher Rytting, and
David Wingate. Out of one, many: Using language models to simulate human samples.
Political Analysis, 31(3):337–351, 2023. doi: 10.1017/pan.2023.2.
Mohammad Atari, Mona J. Xue, Peter S. Park, Dami´an E. Blasi, and Joseph Henrich. Which
humans?PsyArXiv preprint, 2023. doi: 10.31234/osf.io/5b26t.
Marcel Binz and Eric Schulz. Using cognitive psychology to understand GPT-3.Proceedings of
the National Academy of Sciences, 120(6):e2218523120, 2023. doi: 10.1073/pnas.2218523120.
Marcel Binz, Elif Akata, Matthias Bethge, et al. A foundation model to predict and capture
human cognition.Nature, 644:1002–1009, 2025. doi: 10.1038/s41586-025-09215-4.
James Bisbee, Joshua D. Clinton, Cassy Dorff, Brenton Kenkel, and Jennifer M. Larson.
Synthetic replacements for human survey data? the perils of large language models.
Political Analysis, 32(4):401–416, 2024. doi: 10.1017/pan.2024.5.
Donald T. Campbell and Donald W. Fiske. Convergent and discriminant validation by the
multitrait-multimethod matrix.Psychological Bulletin, 56(2):81–105, 1959. doi: 10.1037/
h0046016.
Lingjiao Chen, Matei Zaharia, and James Zou. How is ChatGPT’s behavior changing over
time?Harvard Data Science Review, 2024. arXiv:2307.09009.
Michael S. Christian, Adela S. Garza, and Jerel E. Slaughter. Work engagement: A quan-
titative review and test of its relations with task and contextual performance.Personnel
Psychology, 64(1):89–136, 2011. doi: 10.1111/j.1744-6570.2010.01203.x.
9

Published at the AI Measurement Science Workshop at COLM 2026
Jason A. Colquitt, Brent A. Scott, and Jeffery A. LePine. Trust, trustworthiness, and trust
propensity: A meta-analytic test of their unique relationships with risk taking and job
performance.Journal of Applied Psychology, 92(4):909–927, 2007. doi: 10.1037/0021-9010.92.
4.909.
Lee J. Cronbach and Paul E. Meehl. Construct validity in psychological tests.Psychological
Bulletin, 52(4):281–302, 1955. doi: 10.1037/h0040957.
Ziyan Cui, Ning Li, and Huaikang Zhou. A large-scale replication of scenario-based experi-
ments in psychology and management using large language models.Nature Computational
Science, 2025. doi: 10.1038/s43588-025-00840-7. arXiv:2409.00128.
Jamie Cummins. The threat of analytic flexibility in using large language models to simulate
human data: A call to attention, 2025. URLhttps://arxiv.org/abs/2509.13397.
Patrick J. Curran and Daniel J. Bauer. The disaggregation of within-person and between-
person effects in longitudinal models of change.Annual Review of Psychology, 62:583–619,
2011. doi: 10.1146/annurev.psych.093008.100356.
Danica Dillion, Niket Tandon, Yuling Gu, and Kurt Gray. Can AI language models replace
human participants?Trends in Cognitive Sciences, 27(7):597–600, 2023. doi: 10.1016/j.tics.
2023.04.008.
Ricardo Dominguez-Olmedo, Moritz Hardt, and Celestine Mendler-D¨unner. Questioning
the survey responses of large language models. InAdvances in Neural Information Processing
Systems (NeurIPS), 2024. URLhttps://arxiv.org/abs/2306.07951.
Amy Edmondson. Psychological safety and learning behavior in work teams.Administrative
Science Quarterly, 44(2):350–383, 1999. doi: 10.2307/2666999.
Craig K. Enders and Davood Tofighi. Centering predictor variables in cross-sectional
multilevel models: A new look at an old issue.Psychological Methods, 12(2):121–138, 2007.
doi: 10.1037/1082-989X.12.2.121.
Gregory J. Feist. A meta-analysis of personality in scientific and artistic creativity.Personality
and Social Psychology Review, 2(4):290–309, 1998. doi: 10.1207/s15327957pspr0204 5.
William Fleeson. Toward a structure- and process-integrated view of personality: Traits as
density distributions of states.Journal of Personality and Social Psychology, 80(6):1011–1027,
2001. doi: 10.1037/0022-3514.80.6.1011.
M. Lance Frazier, Stav Fainshmidt, Ryan L. Klinger, Amir Pezeshkan, and Veselina Vracheva.
Psychological safety: A meta-analytic review and extension.Personnel Psychology, 70(1):
113–165, 2017. doi: 10.1111/peps.12183.
Yuan Gao, Dokyun Lee, Gordon Burtch, and Sina Fazelpour. Take caution in using LLMs as
human surrogates.Proceedings of the National Academy of Sciences, 122(24):e2501660122,
2025. doi: 10.1073/pnas.2501660122.
Dongyu Gong and Hantao Zhang. Self-attention limits working memory capacity of
transformer-based models, 2024. URLhttps://arxiv.org/abs/2409.10715.
Jana Gonnermann-M ¨uller, Jennifer Haase, Nicolas Leins, Thomas Kosch, and Sebastian
Pokutta. Stable personas: Dual-assessment of temporal stability in LLM-based human
simulation, 2026. URLhttps://arxiv.org/abs/2601.22812.
Ryan Greenblatt, Carson Denison, Benjamin Wright, Fabien Roger, Monte MacDiarmid, Sam
Marks, Johannes Treutlein, et al. Alignment faking in large language models, 2024. URL
https://arxiv.org/abs/2412.14093.
Igor Grossmann, Matthew Feinberg, Dawn C. Parker, Nicholas A. Christakis, Philip E.
Tetlock, and William A. Cunningham. Ai and the transformation of social science research.
Science, 380(6650):1108–1109, 2023. doi: 10.1126/science.adi1778.
10

Published at the AI Measurement Science Workshop at COLM 2026
Jennifer Haase and Sebastian Pokutta. Beyond static responses: Multi-agent LLM systems
as a new paradigm for social science research, 2025. URL https://arxiv.org/abs/2506.
01839.
Ellen L. Hamaker, Rebecca M. Kuiper, and Raoul P . P . P . Grasman. A critique of the cross-
lagged panel model.Psychological Methods, 20(1):102–116, 2015. doi: 10.1037/a0038889.
Perttu H¨am¨al¨ainen, Mikke Tavast, and Anton Kunnari. Evaluating large language models
in generating synthetic HCI research data: A case study. InProceedings of the 2023 CHI
Conference on Human Factors in Computing Systems, 2023. doi: 10.1145/3544548.3580688.
Miguel A. Hern´an and James M. Robins.Causal Inference: What If. Boca Raton: Chapman &
Hall/CRC, 2020.
Luke Hewitt, Ashwini Ashokkumar, Isaias Ghezae, and Robb Willer. Predicting results of
social science experiments using large language models. https://www.treatmenteffect.
app/paper.pdf, 2024. Working paper.
Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai,
Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark,
et al. Training compute-optimal large language models.arXiv preprint arXiv:2203.15556,
2022. URLhttps://arxiv.org/abs/2203.15556.
John J. Horton, Apostolos Filippas, and Benjamin S. Manning. Large language models as
simulated economic agents: What can we learn from Homo Silicus? NBER Working
Paper 31122, National Bureau of Economic Research, 2023.
He Hu, Chiyuan Ma, Qianning Wang, Lin Liu, Yucheng Zhou, Laizhong Cui, Fei Ma,
and Qi Tian. TheraMind: A strategic and adaptive agent for longitudinal psychological
counseling, 2025. URLhttps://arxiv.org/abs/2510.25758.
Tiancheng Hu, Joachim Baumann, Lorenzo Lupo, Nigel Collier, Dirk Hovy, and Paul
R¨ottger. SimBench: Benchmarking the ability of large language models to simulate
human behaviors. InThe Fourteenth International Conference on Learning Representations
(ICLR), 2026.
Jessica Hullman, David Broska, Huaman Sun, and Aaron Shaw. This human study did not
involve human subjects: Validating LLM simulations as behavioral evidence, 2026. URL
https://arxiv.org/abs/2602.15785.
Hang Jiang, Xiajie Zhang, Xubo Cao, Cynthia Breazeal, Deb Roy, and Jad Kabbara. Person-
aLLM: Investigating the ability of large language models to express personality traits. In
Findings of the Association for Computational Linguistics: NAACL 2024, pp. 3605–3627, 2024.
URLhttps://arxiv.org/abs/2305.02547.
Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon
Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural
language models.arXiv preprint arXiv:2001.08361, 2020. URL https://arxiv.org/abs/
2001.08361.
Alex Kipnis, Konstantinos Voudouris, Luca M. Schulze Buschoff, and Eric Schulz.
metabench: A sparse benchmark of reasoning and knowledge in large language models.
InThe Thirteenth International Conference on Learning Representations (ICLR), 2025.
Robert Kirk, Ishita Mediratta, Christoforos Nalmpantis, Jelena Luketina, Eric Hambro,
Edward Grefenstette, and Roberta Raileanu. Understanding the effects of RLHF on
LLM generalisation and diversity. InThe Twelfth International Conference on Learning
Representations (ICLR), 2024.
Rex B. Kline.Principles and Practice of Structural Equation Modeling. Guilford Press, 4th
edition, 2016.
11

Published at the AI Measurement Science Workshop at COLM 2026
Fatima Koaik, Aayush Gupta, and Farahan Raza Sheikh. LLM-powered social digital twins:
A framework for simulating population behavioral response to policy interventions, 2026.
URLhttps://arxiv.org/abs/2601.06111.
Akaash Kolluri, Shengguang Wu, Joon Sung Park, and Michael S. Bernstein. Finetuning
LLMs for human behavior prediction in social science experiments. InProceedings of the
2025 Conference on Empirical Methods in Natural Language Processing (EMNLP), 2025.
Dani¨el Lakens. Equivalence tests: A practical primer for t tests, correlations, and meta-
analyses.Social Psychological and Personality Science, 8(4):355–362, 2017. doi: 10.1177/
1948550617697177.
Peiyu Li et al. Adaptive testing for LLM evaluation: A psychometric alternative to static
benchmarks, 2025. URLhttps://arxiv.org/abs/2511.04689.
Zonghan Li and Feng Ji. When simulations look right but causal effects go wrong: Large
language models as behavioral simulators, 2026. URL https://arxiv.org/abs/2604.
02458.
Zhicheng Lin. From prompts to constructs: A dual-validity framework for LLM research in
psychology, 2025. URLhttps://arxiv.org/abs/2506.16697.
Ryan Liu, Jiayi Geng, Joshua C. Peterson, Ilia Sucholutsky, and Thomas L. Griffiths. Large
language models assume people are more rational than we really are, 2025. URL https:
//arxiv.org/abs/2406.17055.
Han Luo and Guy Laban. SPASM: Stable persona-driven agent simulation for multi-turn
dialogue generation, 2026. URLhttps://arxiv.org/abs/2604.09212.
Amogh Mannekote, Adam Davies, Jina Kang, and Kristy Elizabeth Boyer. Can large lan-
guage models reliably simulate human learner actions? a simulation authoring framework
for open-ended learning environments. InProceedings of the AAAI Conference on Artificial
Intelligence, volume 39, pp. 29044–29052, 2025. URL https://arxiv.org/abs/2410.02110.
Benjamin S. Manning, Kehang Zhu, and John J. Horton. Automated social science: Language
models as scientist and subjects.NBER Working Paper No. 32381, 2024. URL https:
//arxiv.org/abs/2404.11794.
Roger C. Mayer, James H. Davis, and F. David Schoorman. An integrative model of
organizational trust.Academy of Management Review, 20(3):709–734, 1995. doi: 10.2307/
258792.
Alexander Meinke, Bronson Schoen, J ´er´emy Scheurer, Mikita Balesni, Rusheb Shah, and
Marius Hobbhahn. Frontier models are capable of in-context scheming, 2024. URL
https://arxiv.org/abs/2412.04984.
Peter C. M. Molenaar. A manifesto on psychology as idiographic science: Bringing the
person back into scientific psychology, this time forever.Measurement: Interdisciplinary
Research and Perspectives, 2(4):201–218, 2004. doi: 10.1207/s15366359mea0204 1.
James Mooney, Josef Woldense, Zheng Robert Jia, Shirley Anugrah Hayati, My Ha Nguyen,
Vipul Raheja, and Dongyeop Kang. Are LLM agents behaviorally coherent? latent profiles
for social simulation, 2025. URLhttps://arxiv.org/abs/2509.03736.
Sonia K. Murthy, Tomer Ullman, and Jennifer Hu. One fish, two fish, but not the whole
sea: Alignment reduces language models’ conceptual diversity. InProceedings of the 2025
Conference of the North American Chapter of the Association for Computational Linguistics
(NAACL), 2025. URLhttps://arxiv.org/abs/2411.04427.
Joe Needham, Giles Edkins, Govind Pimpale, Henning Bartsch, and Marius Hobbhahn.
Large language models often know when they are being evaluated, 2025. URL https:
//arxiv.org/abs/2505.23836.
12

Published at the AI Measurement Science Workshop at COLM 2026
John R. Nesselroade. Interindividual differences in intraindividual change. In Linda M.
Collins and John L. Horn (eds.),Best Methods for the Analysis of Change, pp. 92–105.
American Psychological Association, 1991. doi: 10.1037/10099-006.
Stephen Nickell. Biases in dynamic models with fixed effects.Econometrica, 49(6):1417–1426,
1981. doi: 10.2307/1911408.
Davide Paglieri, Logan Cross, William A. Cunningham, Joel Z. Leibo, and Alexander Sasha
Vezhnevets. Persona generators: Generating diverse synthetic personas for arbitrary
contexts, 2026. URLhttps://arxiv.org/abs/2602.03545.
Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, and
Michael S. Bernstein. Generative agents: Interactive simulacra of human behavior. In
Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology
(UIST). Association for Computing Machinery, 2023. doi: 10.1145/3586183.3606763.
Joon Sung Park, Carolyn Q. Zou, Aaron Shaw, Benjamin Mako Hill, Carrie Cai, Mered-
ith Ringel Morris, Robb Willer, Percy Liang, and Michael S. Bernstein. Generative agent
simulations of 1,000 people, 2024. URLhttps://arxiv.org/abs/2411.10109.
Judea Pearl.Causality. Cambridge University Press, 2009.
Jinghua Piao, Yuwei Yan, Jun Zhang, et al. AgentSociety: Large-scale simulation of LLM-
driven generative agents advances understanding of human behaviors and society, 2025.
URLhttps://arxiv.org/abs/2502.08691.
Nathan P . Podsakoff, Trevor M. Spoelma, Nitya Chawla, and Allison S. Gabriel. What pre-
dicts within-person variance in applied psychology constructs? an empirical examination.
Journal of Applied Psychology, 104(6):727–754, 2019. doi: 10.1037/apl0000374.
Ian Rios-Sialer. The homogenization problem in LLMs: Towards meaningful diversity in AI
safety, 2026. URLhttps://arxiv.org/abs/2601.06116.
Naama Rozen, Liat Bezalel, Gal Elidan, Amir Globerson, and Ella Daniel. Do LLMs have
consistent values? InInternational Conference on Learning Representations (ICLR), 2025. URL
https://arxiv.org/abs/2407.12878.
Aadesh Salecha, Molly E. Ireland, Shashanka Subrahmanya, Jo˜ao Sedoc, Lyle H. Ungar, and
Johannes C. Eichstaedt. Large language models display human-like social desirability
biases in big five personality surveys.PNAS Nexus, 3(12):pgae533, 2024. doi: 10.1093/
pnasnexus/pgae533.
Shibani Santurkar, Esin Durmus, Faisal Ladhak, Cinoo Lee, Percy Liang, and Tatsunori
Hashimoto. Whose opinions do language models reflect? InProceedings of the 40th
International Conference on Machine Learning (ICML), volume 202 ofProceedings of Machine
Learning Research. PMLR, 2023.
Wilmar B. Schaufeli, Marisa Salanova, Vicente Gonz´alez-Rom´a, and Arnold B. Bakker. The
measurement of engagement and burnout: A two sample confirmatory factor analytic
approach.Journal of Happiness Studies, 3(1):71–92, 2002. doi: 10.1023/A:1015630930326.
Greg Serapio-Garc´ıa, Mustafa Safdari, Cl ´ement Crepy, Luning Sun, Stephen Fitz, Peter
Romero, Marwa Abdulhai, Aleksandra Faust, and Maja Matari ´c. Personality traits in
large language models, 2023. URLhttps://arxiv.org/abs/2307.00184.
Murray Shanahan, Kyle McDonell, and Laria Reynolds. Role play with large language
models.Nature, 623(7987):493–498, 2023.
Mrinank Sharma, Meg Tong, Tomasz Korbak, David Duvenaud, Amanda Askell, Samuel R.
Bowman, Newton Cheng, Esin Durmus, Zac Hatfield-Dodds, Scott R. Johnston, Shauna
Kravec, Timothy Maxwell, Sam McCandlish, Kamal Ndousse, Oliver Rausch, Nicholas
Schiefer, Da Yan, Miranda Zhang, and Ethan Perez. Towards understanding sycophancy
in language models. InInternational Conference on Learning Representations (ICLR), 2024.
URLhttps://arxiv.org/abs/2310.13548.
13

Published at the AI Measurement Science Workshop at COLM 2026
Seongho Son, William Bankes, Sayak Ray Chowdhury, Brooks Paige, and Ilija Bogunovic.
Right now, wrong then: Non-stationary direct preference optimization under preference
drift, 2025. URLhttps://arxiv.org/abs/2407.18676.
Christopher J. Soto, Oliver P . John, Samuel D. Gosling, and Jeff Potter. Age differences in
personality traits from 10 to 65: Big five domains and facets in a large cross-sectional
sample.Journal of Personality and Social Psychology, 100(2):330–348, 2011. doi: 10.1037/
a0021717.
Patrick Taillandier, Jean Daniel Zucker, Arnaud Grignard, Benoit Gaudou, Nghi Quang
Huynh, and Alexis Drogoul. Integrating LLM in agent-based social simulation: Opportu-
nities and challenges, 2025. URLhttps://arxiv.org/abs/2507.19364.
Olivier Toubia, George Z. Gui, Tianyi Peng, et al. Twin-2k-500: A data set for building
digital twins of over 2,000 people based on their answers to over 500 questions.Marketing
Science, 44(6):1446–1455, 2025.
Sumer S. Vaid and Ashley V . Whillans. Toward an ai-powered computational testbed for
workforce policy.arXiv preprint arXiv:2605.19064, 2026. URL https://arxiv.org/abs/
2605.19064.
Dimitri van der Linden, Jan te Nijenhuis, and Arnold B. Bakker. The general factor of
personality: A meta-analysis of big five intercorrelations and a criterion-related validity
study.Journal of Research in Personality, 44(3):315–327, 2010. doi: 10.1016/j.jrp.2010.03.003.
Teun van der Weij, Felix Hofst¨atter, Ollie Jaffe, Samuel F. Brown, and Francis Rhys Ward.
AI sandbagging: Language models can strategically underperform on evaluations, 2024.
URLhttps://arxiv.org/abs/2406.07358.
Joshua Vendrow, Edward Vendrow, Sara Beery, and Aleksander Madry. Do large language
model benchmarks test reliability?, 2025. URLhttps://arxiv.org/abs/2502.03461.
Angelina Wang, Jamie Morgenstern, and John P . Dickerson. Large language models that
replace human participants can harmfully misportray and flatten identity groups.Nature
Machine Intelligence, 7:400–411, 2025. doi: 10.1038/s42256-025-00986-z.
Shirley Wu, Evelyn Choi, Arpandeep Khatua, Zhanghan Wang, Joy He-Yueya,
Tharindu Cyril Weerasooriya, Wei Wei, Diyi Yang, Jure Leskovec, and James Zou. Hu-
manLM: Simulating users with state alignment beats response imitation, 2026. URL
https://arxiv.org/abs/2603.03303.
Chengxing Xie, Canyu Chen, Feiran Jia, Ziyu Ye, Shiyang Lai, Kai Shu, Jindong Gu, Adel
Bibi, Ziniu Hu, David Jurgens, James Evans, Philip Torr, Bernard Ghanem, and Guohao Li.
Can large language model agents simulate human trust behavior? InAdvances in Neural
Information Processing Systems (NeurIPS), 2024. URL https://arxiv.org/abs/2402.04559.
Haoran Ye, Jing Jin, Yuhang Xie, Xin Zhang, and Guojie Song. Large language model
psychometrics: A systematic review of evaluation, validation, and enhancement, 2025.
URLhttps://arxiv.org/abs/2505.08245.
Xuhui Zhou, Weiwei Sun, Weihua Du, Jiarui Liu, Haojia Sun, Qianou Ma, Tongshuang
Wu, Yiming Yang, and Maarten Sap. Odyssim: Building foundation models for human
behavior simulation.arXiv preprint arXiv:2606.14199, 2026. URL https://arxiv.org/abs/
2606.14199.
A The Within-Person Correlation: Why It Compresses and How to
Recover It
The benchmark recovers the direction of within-person relations, yet the within-person
correlation stays near zero, and this gap is the central puzzle of this work. In this appendix
we explain why a generative rater returns a small, central deviation when the day calls for
a larger one, a pattern we call the safe-deviation tendency, and we set out the factors that
enlarge it. Throughout, we separate the routes available to an all-silico evaluation from the
routes that require longitudinal human data.
14

Published at the AI Measurement Science Workshop at COLM 2026
0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40
Within-person variance error
(lower = closer to human norm)
75
80
85
90
95
100Nomological direction agreement (%)
r = + 0.17
Internal vs. external validity
Figure 3: Internal versus external validity, one point per model. The near-zero slope
(r≈ 0.17) shows the two axes are largely independent: gains in internal validity leave
external validity unchanged.
A.1 The safe-deviation tendency
We trace the timid response to four mechanisms that reinforce one another. First, the rating
a model returns is closer to an average than to a single draw: asked for an end-of-day
state, the model reports its central expectation over plausible responses, and an average is
smoother than the responses it summarizes, so the reported series carries less within-person
variance than the day-to-day state it stands for. The near-deterministic ratings we observe,
with single-rating reliability 0.97, confirm that the rater commits to this average, which is
also why the within-person correlation holds at 0.059 under rating temperature 0.8 and 0.060
under temperature 0.0. Second, alignment rewards the modal answer: instruction tuning
and preference optimization favor moderate, broadly acceptable outputs and discourage
commitment to scale extremes, so the rater settles toward the middle of each range, a pattern
we make concrete in Section A.2, where general capability and within-person recovery
move in opposite directions. Third, the supplied baseline acts as a prior: when we hand
the rater its own trait baseline and typical range, the model shrinks each day toward that
prior, and removing the anchor sharpens directional recovery, lifting sign agreement from
71% to 77% and rank correlation from 0.38 to 0.46 while the within-person correlation holds
steady, which marks anchoring as one contributing cause among several. Fourth, the signal
weakens across two mappings: a day’s drivers pass from seeded indicators to narrative and
from narrative to rating, and because each mapping pulls toward its own average, the link
between an indicator and the state it should move has been smoothed twice by the time
we measure it. Taken together, these mechanisms leave a rater that names the correct sign
of a day’s effect and renders it as a small, safe deviation, faithful in direction and timid in
magnitude.
A.2 Capability and within-person recovery
We test the role of capability directly, holding the prompt and the data fixed while re-rating
the shared narratives with three models that span the gpt-4.1 family. As capability falls, the
within-person rank signal strengthens: the rank correlation against meta-analytic effects
rises from 0.38 for gpt-4.1, through 0.45 for gpt-4.1-mini, to 0.48 for gpt-4.1-nano, and sign
agreement reaches 75% for the smallest model. The within-person correlation, by contrast,
stays near the sampling floor across the whole ladder, between 0.023 and 0.028. We read this
as evidence that the lighter-aligned model preserves the day-to-day variation the structure
requires, while the within-person correlation remains governed by the construct’s variance
rather than by model capability.
15

Published at the AI Measurement Science Workshop at COLM 2026
A.3 Construct variance and within-person recovery
The variance available for any within-person relation is set by the intraclass correlation, and
because the four headline states are trait-saturated, with ICC near 0.75, little within-person
variance is left for an indicator to move. We therefore test three constructs with a more even
between- and within-person split, re-rating the same narratives for daily exhaustion (ICC
0.34), fatigue (ICC 0.40), and flow (ICC 0.48). The within-person correlation rises in step
with the within-person variance share: pooled |r| reaches 0.058 for exhaustion, 0.075 for
fatigue, and 0.069 for flow, roughly three times the 0.023 of the trait-saturated set, with sign
agreement of 100% and 100% and rank correlation up to 0.95. These estimates rest on 8
anchored pairs per state and serve as a directional demonstration, yet the pattern is clear:
the limit on the within-person correlation sits in the construct rather than in the model,
and where a state carries real day-to-day variance, the synthetic population reproduces
within-person structure at a size the literature recognizes.
A.4 In-silico achievability of the internal-validity targets
We next ask whether the internal-validity targets are reachable by optimization that draws
on published norms alone, holding measured human states out of the objective entirely. We
optimize the rating prompt with MIPROv2 against a literature-only objective that combines
the within-person standard deviation implied by published ICC values, use of the full
scale range, avoidance of ceiling and floor pileup, and the cross-state coherence band on
the 5 verified meta-analytic pairs. We optimize on 30 training personas and report the
composite on 30 personas held aside from optimization. The tuned prompt raises the held-
out composite from 0.693 to 0.702 for gpt-4.1-mini and from 0.660 to 0.673 for gpt-4.1-nano.
We read the small and consistent gains two ways: the uniform off-the-shelf prompt already
sits close to the in-silico ceiling for these targets, and optimization against published norms
still produces a measurable improvement on held-out data. The instruction the optimizer
selects encodes the same anti-anchoring move we identify in Section A.1, directing the rater
to let a strong day move each rating toward the ends of its scale. These results establish
reachability on a fully all-silico footing, separate from the question of predicting realized
individual trajectories.
A.5 A principled bound and the routes that remain
We close with two readings. First, the ceiling on the within-person correlation is structural:
when between-person variance dominates the partition, the recoverable within-person
correlation is bounded, and a weak within-person correlation on trait-saturated states is
the expected outcome. Second, the routes that raise the within-person correlation in an
all-silico setting act on variance and structure, and they include a lighter-aligned rater
(Section A.2), constructs with a larger within-person share (Section A.3), de-anchored rating,
and narratives that encode the day’s drivers more vividly. Routes that condition on an
individual’s measured history, namely personalized exemplars, neighbor retrieval, and
fitted statistical predictors, raise pooled coefficients while their within-person component
stays near chance, and because they depend on measured human states they belong to
the companion problem of predicting realized individual trajectories. We therefore set the
honest target for an all-silico benchmark as matching within-person variance, range, and
direction to published effects, and treating the within-person correlation as a value the
construct’s variance bounds.
B Seeding construction
We initialize each persona by drawing five trait scores from a multivariate normal N(µ , Σ),
where µ holds the published Big Five means andΣ assembles published standard deviations
and the meta-analytic intercorrelation matrix (Soto et al., 2011; van der Linden et al., 2010);
when the assembled Σ departs from positive definiteness, we project it to the nearest positive-
definite matrix before sampling. We then set each state’s person-level baseline as a linear
function of the standardized traits, b=β ⊤z, with β extracted from the cited meta-analyses
(Christian et al., 2011; Frazier et al., 2017; Feist, 1998; Colquitt et al., 2007), and we split total
state variance with the published intraclass correlation, so that the between-person standard
16

Published at the AI Measurement Science Workshop at COLM 2026
deviation is σb =σ
√
ICC and the within-person standard deviation is σw =σ
√
1−ICC .
Baselines sit on each state’s native scale, and we leave the target state columns unpopulated
so that any recovered indicator-state relation emerges from generation.
C Internal validity criteria
We score six internal criteria, each as two one-sided equivalence tests (Lakens, 2017) against
literature targets with persona-cluster bootstrap intervals.L1 Distributions:state means
and spreads match published norms (Hedges’ g equivalence).L2 V ariance partition:the
within-person standard deviation and the between- versus within-person ICC split match
literature targets (log-ratio equivalence).L3 Cross-state structure:between- and within-
person cross-state correlations match meta-analytic pair targets (a |∆r| margin), scored on
the sourced pairs.L4 T emporal dependence:the within-person AR(1) coefficient matches
its target band, reported as directional evidence given short-panel non-identifiability at six
days.L6 Latent dimensionality:multilevel eigenstructure (between- and within-person
leading components) stands in for a four-indicator factor model, which is under-identified.
L7 Range utilization:ceiling and floor pileup stays within the human range. The numbering
omits L5, an affect-specific check outside the present scope.
D Rating prompt
Every benchmarked LLM receives the identical prompt below, assembled from the persona’s
identity portrait, the day’s narrative, and a fixed rating instruction. The system message
places the model inside the persona and the instruction asks for a first-person end-of-day
self-report; the models do not annotate a third party’s text. No part of the prompt is tuned
per model.
SYSTEM: You are the person described. Respond in first person, honestly.
USER:
=== WHO YOU ARE ===
You are{first} {last}.
{psychological portrait}
=== YOUR REACTIVITY PATTERNS ===
{reactivity patterns}
=== TODAY (Day{d},{weekday}) --- DAY TYPE:{type}===
{narrative}
=== SCALE GUIDANCE ===
{per-state scale, this persona’s baseline and typical range}
=== RATE YOUR END-OF-DAY STATE ===
You have just lived this day. It is 5:30pm. Report your ACTUAL internal
state right now - not how you should feel, how you do feel. Honor the
texture of the day.
OUTPUT EXACTLY this block and nothing else (one number each, within the
stated scale):
STATES:
- Work Engagement: [1-7] - [one sentence why]
- Psychological Safety: [1-4] - [one sentence why]
- Work Creativity: [1-6] - [one sentence why]
- Team Trust: [1-5] - [one sentence why]
E Model leaderboard
Table 1 ranks every evaluated model on both criteria at once. We order by internal validity,
computing the within-person variance error against the human norm as the sort key, and
we place the external-validity columns beside it. Reading down the table, internal validity
ranges widely across the roster, from a tight match to the human norm down to corpora that
miss it by close to an order of magnitude, while trait–state direction agreement and rank
correlation stay high and roughly flat throughout. A model’s rank on one axis predicts little
about its rank on the other axis.
17

Published at the AI Measurement Science Workshop at COLM 2026
Table 1: Model leaderboard across both validity criteria, ranked by internal validity (within-
person variance error, lower is closer to the human norm). External validity (trait–state
direction agreement and rank correlation ρ) stays high and roughly flat as internal validity
varies, the central split of the benchmark.
Model Params (B) Var. error↓Levels Dir. (%)ρ
Gemma-2-27B 27 0.043 2/6 80 0.81
GPT-5-5 – 0.061 2/6 80 0.69
Gemma-3-27B 27 0.065 3/6 90 0.84
Qwen-2-5-Coder-32B 32 0.090 2/6 80 0.65
Claude-Sonnet-4 – 0.115 2/6 80 0.63
Qwen3-5-27B – 0.135 3/6 – –
GPT-4-1 – 0.140 2/6 85 0.63
Llama-3-1-8B 8 0.145 2/6 85 0.65
Qwen-2-5-72B 72 0.146 2/6 90 0.80
Gemma-3-12B 12 0.147 3/6 90 0.70
Mistral-Small-3-2-24B 24 0.150 3/6 75 0.66
Qwen3-14B 14 0.160 2/6 80 0.68
Deepseek-V3-2 671 0.161 3/6 85 0.79
Qwen3-30B-A3B-Thinking 30 0.175 2/6 90 0.64
Deepseek-R1-0528 671 0.186 3/6 85 0.71
Gemini-2-5-Flash – 0.196 2/6 85 0.78
Qwen3-8B 8 0.206 2/6 90 0.57
Deepseek-R1-Distill-Llama-70B 70 0.210 2/6 90 0.74
Llama-4-Maverick 400 0.216 2/6 80 0.71
Qwen3-30B-A3B 30 0.232 2/6 85 0.68
Qwen3-32B 32 0.236 2/6 85 0.72
Llama-3-2-3B 3 0.240 2/6 80 0.61
Llama-3-8B 8 0.242 2/6 85 0.58
Gemini-2-5-Pro – 0.247 2/6 85 0.75
Qwen3-235B-A22B 235 0.250 1/6 90 0.68
GPT-Oss-20B 21 0.270 1/6 75 0.78
GPT-Oss-120B 117 0.287 1/6 85 0.77
Llama-3-2-1B 1 0.309 3/6 75 0.50
Granite-4-1-8B 8 0.315 2/6 90 0.72
Qwen-2-5-7B 7 0.325 1/6 85 0.71
Llama-3-1-70B 70 0.354 2/6 80 0.60
Phi-4 14 0.362 1/6 85 0.59
Llama-3-3-70B 70 0.363 1/6 80 0.55
Gemma-3-4B 4 0.427 3/6 100 0.83
18
