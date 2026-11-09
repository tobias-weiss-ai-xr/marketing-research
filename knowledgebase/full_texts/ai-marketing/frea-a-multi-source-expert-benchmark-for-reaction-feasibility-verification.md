---
title: 'FREA: A Multi-Source Expert Benchmark for Reaction Feasibility Verification'
url: https://arxiv.org/abs/2610.06614
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Botao Yu
- Bo Zhou
- Daniel Adu-Ampratwum
- Frazier N. Baker
- Ziru Chen
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.06614
pages: 35
chars: 124720
fetched_at: '2026-11-08T13:34:58+00:00'
kb_version: 1
---

# FREA: A Multi-Source Expert Benchmark for Reaction Feasibility Verification

Preprint
FREA: A MULTI-SOURCEEXPERTBENCHMARK FOR
REACTIONFEASIBILITYVERIFICATION
Botao Yu1,†, Bo Zhou2,∗, Daniel Adu-Ampratwum3,∗, Frazier N. Baker1,4, Ziru Chen1,
Reza Averly1, Ye Liu4, Wenhao Gao5, Xia Ning1,3,4,6, Huan Sun1,†
1Department of Computer Science and Engineering, The Ohio State University
2Department of Pharmaceutical Sciences, University of Illinois Chicago
3College of Pharmacy, The Ohio State University
4Department of Biomedical Informatics, The Ohio State University
5Department of Chemical and Biomolecular Engineering, University of Pennsylvania
6Translational Data Analytics Institute, The Ohio State University
ABSTRACT
As generative models and AI agents propose chemical reactions at a scale be-
yond expert review, feasibility verifiers decide which proposals enter synthesis
planning. But do their decisions agree with chemists across different kinds of
candidates? We introduce FREA, a benchmark of751reactions labeled by ex-
pert chemists under an explicit feasibility criterion, drawn from retrosynthesis
model proposals, zero-yield experimental records, edits by large language models
(LLMs), and five negative candidate generation methods. Our evaluation finds that
no verifier leads across all sources: LLMs given only the criterion are competi-
tive with dedicated verifiers, while forward models perform best on retrosynthesis
proposals but reject most feasible edits of recorded reactions at the evaluated op-
erating points. Looking beyond aggregate scores, both forward models perform
below chance when separating infeasible alternative disconnections from feasi-
ble generated candidates. To study whether negative supervision addresses these
weaknesses, we also release a corpus of over 14 million recorded reactions and
generated negative candidates. In matched training comparisons, adding a mixture
of generated negatives to forward training raises mean AUROC across sources,
but these gains do not extend to retrosynthesis proposals. Varying the generation
method further shows that the largest gain on generated candidates coincides with
worse proposal screening. These findings motivate evaluating verifiers against ex-
perts across sources and designing negatives for transfer to model proposals. The
benchmark and corpus are publicly available.
1 INTRODUCTION
Generative models, search-based planning systems and language-model agents now propose chemi-
cal reactions at a scale that no chemist can review one by one (Segler et al., 2018; Long et al., 2025;
Baker et al., 2026). Within these pipelines, reaction feasibility verifiers act as gatekeepers that de-
cide which proposals survive into downstream planning (Segler et al., 2018; Genheden et al., 2020a;
Sadowski et al., 2025). Accepting an infeasible reaction can derail a plan, while rejecting a fea-
sible alternative can eliminate a useful route. Reliable verification therefore becomes increasingly
important as human review is removed from the loop.
Common verifiers include forward models, which use target-product recovery or likelihood as a
proxy for feasibility (Schwaller et al., 2019b; 2020), and classifiers trained to separate recorded
reactions from generated negatives (Segler et al., 2018; Genheden et al., 2020a; Gai´nski et al., 2025),
which are typically assessed by their effect on downstream search or on held-out generated reactions
(Section A). Here, we ask:do verifiers that appear reliable on recorded or generated reactions agree
with chemists on the reactions they are actually asked to screen?
*Equal contribution.
†Correspondence to:{yu.3737, sun.397}@osu.edu.
1
arXiv:2610.06614v1  [cs.AI]  5 Oct 2026

Preprint
Answering this question requires labels that are independent of how verifiers are built. Published
reaction data favor successful outcomes (V oinarovska et al., 2024), while automatically generated
negative candidates need not be infeasible. Expert-labeled reactions therefore provide a direct basis
for evaluating feasibility verifiers.
We introduce FREA, an expert-labeled benchmark of751reactions. A reaction is feasible if it lists
all substantive reactants and admits reasonable conditions that yield the target products in isolable
form (Section 3). The reactions come from four sources: proposals of eight retrosynthesis models,
zero-yield experimental records, edits of recorded reactions by large language models (LLMs), and
candidates from five negative candidate generation methods (Section 4). Annotators label each
reaction without seeing its source.
Comparing LLMs, forward models and verifiers trained on generated negatives, we find thatno
verifier leads across all sources(Section 6.1). LLMs given only the criterion are competitive with
dedicated verifiers, with Claude Opus 5 achieving the highest mean balanced accuracy. Forward
models are strongest on retrosynthesis proposals, yet at the evaluated operating points they reject
most feasible edits of recorded reactions.
Looking within the generated source reveals a sharper failure:the strongest verifiers of model
proposals can rank infeasible candidates above feasible ones. Both forward models score below
chance on alternative product disconnections, with AUROCs of 26.2 and 32.5 against the same fea-
sible reference reactions (Section 6.2). Adding generated negatives to forward training improves this
comparison and gives the highest mean AUROC across sources, but reduces performance on other
constructions. These selective gains leave open whether negative supervision improves verification
beyond particular constructions, especially on model proposals.
To test this, we use an accompanying corpus of over 14 million recorded reactions and generated
negative candidates, with no benchmark reaction in the training data (Section C.5). In matched com-
parisons with continued forward training,the mean AUROC gain from a mixture of generated
negatives does not extend to retrosynthesis proposals(Section 7). Varying the generation method
further shows that the largest gain on generated candidates coincides with a decline on model pro-
posals. The open challenge is therefore to generate negatives whose benefits extend to the proposals
verifiers must screen.
Our contributions are:
1.An expert benchmarkof341feasible and410infeasible reactions from four sources, labeled
under an explicit criterion and released with recorded failure reasons (Sections 3 and 4).
2.An evaluation of verifier strengths and failure modes, across reaction sources and candidate
generation methods (Sections 5 and 6).
3.A generated corpus and a controlled transfer study, with matched and pre-registered training
comparisons that test whether negative supervision improves screening of model proposals and
motivate hypotheses for negative-data design (Section 7).
The benchmark1 and generated corpus2 are available on Hugging Face.
2 RELATEDWORK
Feasibility filters.Classifiers trained on recorded reactions and constructed negatives have been
used in synthesis planning since the in-scope filter of Segler et al. (2018). AiZynthFinder uses
template-generated negatives (Genheden et al., 2020b;a). RetroGFN combines forward-template
negatives with replacements of the recorded product (Gai ´nski et al., 2025). RetroTrim combines
several scorers and evaluates both individual reactions and complete routes by expert review (Sad-
owski et al., 2025). These studies establish the value of filtering in planning, but evaluation on
generated negatives does not test whether the assigned negative labels agree with experts. FREA
evaluates individual reactions across four sources under a common expert criterion.
1https://huggingface.co/datasets/FREA-benchmark/FREA-benchmark
2https://huggingface.co/datasets/FREA-benchmark/FREA-corpus
2

Preprint
Expert and precedent-based evaluation.ChemCensor scores reactions by checking their reac-
tion centers and functional-group context against recorded reactions (Zagribelnyy et al., 2026b).
Concurrent work also evaluates retrosynthesis predictions against expert judgments (Zagribelnyy
et al., 2026a). FREA combines model proposals with experimental records and multiple forms of
controlled perturbation under an explicit feasibility criterion. This broader coverage supports both
diagnosis of source-dependent failures and evaluation of transfer from generated negative training
data.
Negative reaction data.Published failures are scarce (V oinarovska et al., 2024). Existing re-
sources include private laboratory records (Jiang et al., 2021), high-throughput experiments for
acid–amine couplings (Zhong et al., 2025), and data for enzymatic reactions (Chainani et al., 2025).
Experimental failures describe particular conditions. FREA uses zero-yield records as candidates
for expert annotation and combines them with model proposals and constructed reactions. Section A
gives a detailed comparison of these resources and adjacent approaches.
3 REACTIONFEASIBILITYTASKDEFINITION
Given reactantsR={r 1, . . . , rk}and productsP={p 1, . . . , pm}, a verifier predicts
f(R,P)∈ {0,1},(1)
where 1 denotes a feasible reaction and 0 an infeasible one. The input contains no reaction condi-
tions, andPneed not include every product of the reaction.
We define feasibility from the perspective of synthesis planning, in which a verifier screens retrosyn-
thesis proposals. Each reaction is treated as a proposal, which is feasible if a planning system could
keep it as a valid step of a route. Specifically, a feasible proposal must satisfy two conditions.
Completeness.Completeness asks whether the proposal lists everything the step needs, apart from
routine components. The proposal must list every substantive reactant required to produce the target
products, rather than only a transformation from a main reactant to a product. Auxiliary components,
which act in routine supporting roles such as catalysts, solvents, bases, reducing agents and water,
may be assumed. Any species outside these roles is substantive. For example, a Suzuki coupling
is incomplete without its organoboron partner and an esterification without its alcohol, whereas the
water of a hydrolysis may be left implicit.
Reactivity.Reactivity asks whether the listed reactants can actually give the target products. There
must be reasonable conditions, compatible with the listed reactants and products, under which the
listed reactants and any assumed auxiliary components give the target products in isolable form. The
target products need not be the major products. The reaction must take place in a single step or a
one-pot operation, without isolating an intermediate.
Rationale.Both conditions follow from how proposals are produced and used in synthesis plan-
ning. A step in a route must be executable from its listed starting materials, so a proposal that
omits a substantive partner cannot be kept. Retrosynthesis models, like the reaction databases they
are trained on, often omit routine components (Schneider et al., 2016; Wigh et al., 2024), which a
chemist supplies without comment. Requiring them would reject well-formed proposals, so auxil-
iary components may be assumed. Proposals also leave the conditions to the chemist, so reactivity
depends on whether reasonable conditions exist, not on whether any are stated. A route only needs
to isolate the products of a step and carry them forward, while the share of competing products
depends on conditions that the proposal does not fix, so the target products need not be the major
ones. A sequence that isolates an intermediate is two steps of a route, so a single step or a one-pot
operation is required. Finally, the assumptions are limited to what a chemist routinely supplies. If
any missing reactant, or any conditions however extreme, could be assumed, almost any product
would be reachable from almost any reactants, and an infeasible label would carry no information.
What the labels assert.The labels record expert judgments under this criterion, which follows
how a chemist reviews a proposed step. They do not predict yield or certify experimental success.
A zero-yield record can therefore be labeled feasible if other reasonable conditions could produce
3

Preprint
Table 1: Composition of the FREA benchmark.In practice: reactions produced by retrosynthesis
models or attempted in the laboratory.Controlled: candidates obtained from a recorded reaction
by a known negative candidate generation method. Table C.1 gives the per-model and per-method
breakdown, including the fraction judged infeasible for each GR generation method.
Source Produced by In practice Controlled Feas. Infeas. Total
Retrosynthesis proposals (RP) Eight retrosynthesis models✓197 85 282
Zero-yield records (ZR) Experimental records✓79 14 93
LLM perturbations (LP) Two LLMs editing recorded reactions32 55 87
Generated reactions (GR) Five generation methods✓33 256 289
Total 341 410 751
the target. Section B lists the permitted auxiliary roles and gives the full decision procedure and
annotation protocol.
4 THEFREA BENCHMARK
FREA provides a common test of whether verifiers agree with experts across different sources of
reaction candidates. It contains751expert-labeled reactions, with341feasible and410infeasible
under Section 3. The four sources connect practical screening, targeted diagnosis, and evaluation of
transfer (Table 1). Combining reactions encountered in practice with deliberate perturbations allows
us to test whether a verifier’s strengths extend beyond one source.
4.1 FOURREACTIONSOURCES
Retrosynthesis proposals (RP).We collect proposals from eight single-step retrosynthesis mod-
els for targets in ORDerly (Wigh et al., 2024), a curated dataset derived from the Open Reaction
Database (Kearnes et al., 2021). The models span template-based (Chen & Jung, 2021), semi-
template (Chen et al., 2023), and template-free approaches (Zeng et al., 2024; Han et al., 2024;
Irwin et al., 2022; Yu et al., 2024; Baker et al., 2026). Proposals are retained whether or not they
reproduce the recorded reactants. RP therefore tests the proposals that verifiers must screen during
planning, including valid alternatives to the recorded reaction.
Zero-yield records (ZR).These are ORDerly reactions with a reported yield of zero. They were
attempted experimentally, but failure under the recorded conditions does not determine feasibility
under our criterion. On the contrary, chemists presumably attempted them because they expected
them to work. We therefore include them as potentially feasible reactions and leave their labels
unsettled until expert annotation.
LLM perturbations (LP).GPT-5.4 (OpenAI, 2026a) and Claude Opus 4.6 (Anthropic, 2026a)
are instructed to edit recorded reactions to make them infeasible while keeping them superficially
coherent. This source challenges verifiers on identifying infeasible edits among superficially coher-
ent reactions.
Generated reactions (GR).We propose five methods for constructing negative candidates, build-
ing on earlier uses of template application and reaction component replacement (Segler et al., 2018;
Genheden et al., 2020a; Gai´nski et al., 2025). The methods differ in what they change (Figure 1):
•Random Addition (RA)adds atoms at reactant reaction centers.
•Random Replacement (RR)replaces the reactant set with a similar set from another recorded
reaction.
•New Center (NC)chooses a different product disconnection and completes the resulting frag-
ments into reactants (Chen et al., 2023; Baker et al., 2024).
•Forward Template (FT)applies an alternative forward template to the recorded reactants.
•Elementary Template (ET)applies a sequence of elementary reaction templates (Joung et al.,
2024) to obtain a different product.
4

Preprint
Recorded reaction Reaction center Changed molecules
Reactants Product
+
MODIFY REACTANTS Keep the product unchanged
RARandom Addition
Add atoms at a reaction center
RRRandom Replacement
Replace with similar reactants
NCNew Center
Choose another disconnection
MODIFY PRODUCTS Keep the reactants unchanged
FTForward Template
Apply an alternative forward template
ETElementary Template
Compose elementary reaction steps
+ + +
+ + ...
OO H2N HO O N
H
N
H
HOO
OO H2NOO
H
POH
HO N
H HOBOH
O-
N
H
O
OO
H2N
NO
OO
H2N
Figure 1: The five methods used to construct GR candidates, illustrated from a common parent
reaction (top). RA, RR and NC change the reactants while keeping the product; FT and ET change
the product while keeping the reactants. The methods generate intended negatives, whose feasibility
is determined by expert annotation.
RA, RR and NC change the reactants while keeping the product. FT and ET change the product
while keeping the reactants. We sample the same number of candidates from each method for
annotation, retaining both feasible and infeasible examples. The known generation methods allow
failures to be traced to specific constructions. Comparing GR with the other sources then tests
whether gains on these constructions extend to other reactions. Applying the same methods to
the curated ORDerly reactions also produces the generated corpus used for training in Section 7.
Sections C and D give data collection and generation details.
4.2 EXPERTANNOTATION
Two chemists, a pharmacy faculty member and a chemistry postdoctoral researcher with wet-
laboratory experience, labeled reactions without seeing their sources or model predictions. The
workflow combined guideline calibration, independent annotation and joint review of disagree-
ments, yielding751expert-labeled benchmark reactions. The release includes recorded failure rea-
sons and notes where available. Section B gives the calibration procedure, inter-annotator agreement
and adjudication details.
The expert labels illustrate why source alone cannot determine feasibility: 79 of 93 zero-yield
records are judged feasible, as are 33 of 289 generated candidates intended to be negative. Ex-
pert labels therefore provide a reference that neither recorded outcomes nor generation procedures
supply alone.
5 EVALUATIONPROTOCOL
Evaluated systems.We compare three groups of systems in the main results:
•LLMs.Claude Opus 5 (Anthropic, 2026b) and GPT-6 Astra (OpenAI, 2026b) receive the reac-
tants, products and feasibility criterion, and return a decision with an explanation.
•Forward models.Chemformer (Irwin et al., 2022) and BARTSmiles (Chilingaryan et al., 2024)
are fine-tuned on recorded reactions. Top-10 inclusion accepts a proposal if its target matches
5

Preprint
Table 2: Results on FREA by source (feasible/infeasible counts in parentheses). Avg. denotes the
four-source mean. Dashes indicate no continuous score. Best values per column are bold. Counts
describe the benchmark; one unparseable Claude response on LP is excluded from that model’s
metrics.
RP(197/85)ZR(79/14)LP(32/55)GR(33/256)Avg.
System AUROC BAcc AUROC BAcc AUROC BAcc AUROC BAcc AUROC BAcc
Large language models, criterion in the prompt
Claude Opus 5 – 69.9 – 64.3 –76.1– 61.8 –68.0
GPT-6 Astra – 66.8 – 63.7 – 69.6 –62.7– 65.7
Forward-model proxies
Chemformer (top-10) – 70.6 – 67.2 – 63.3 – 50.1 – 62.8
Chemformer (LL) 76.7 71.682.470.2 64.5 63.8 67.0 49.8 72.6 63.9
BARTSmiles (top-10) –73.1–74.4– 59.0 – 57.1 – 65.9
BARTSmiles (LL)78.971.5 79.5 72.5 66.1 60.4 66.9 53.4 72.8 64.4
Trained on our generated negative candidates
BARTSmiles (LL+neg.) 77.0 67.1 80.8 63.7 69.4 66.173.554.975.262.9
BARTSmiles (disc.) 67.8 62.5 79.0 60.1 66.0 54.8 66.0 56.6 69.7 58.5
Descriptor GBDT 70.3 64.0 72.2 56.375.470.2 64.7 62.4 70.7 63.2
one of the ten highest-ranked product predictions after canonicalization. Log-likelihood (LL)
scores the supplied target by its mean per-token log-probability given the reactants.
•Models trained on generated negatives.BARTSmiles (LL+neg.) continues the BARTSmiles
forward model with a loss that favors recorded reactions over generated negative candidates, and
is scored by LL. BARTSmiles (disc.) is trained to output a feasibility score directly. Descriptor
GBDT is a gradient-boosted tree using 58 chemical descriptors. All three use the training split
of the generated corpus, with no benchmark reaction in their training data (Section C.5).
We also evaluate a rule-based baseline and the released filter from the AiZynthFinder planning
tool (Genheden et al., 2020b), with results in Section G.
Metrics.The primary metric is AUROC. We also report balanced accuracy (BAcc), the mean of
the acceptance rate for feasible reactions and the rejection rate for infeasible reactions. BAcc covers
all systems, including the LLM and top-10 decisions for which we extract no continuous score.
Continuous-score thresholds are fixed on held-out generated pairs before application to FREA. We
report results for each source and their unweighted mean across the four sources.
Sections E and F provide implementation details and the full evaluation protocol, including inference
and training settings, model and threshold selection, and statistical tests.
6 RESULTS
6.1 PERFORMANCEACROSSSOURCES
We first ask whether verifiers agree with experts on each source, which determines how reliably they
can act as gatekeepers. Table 2 reports AUROC and BAcc within each source, together with their
unweighted means.
Frontier LLMs, given only the criterion, are strong candidate verifiers.Without examples from
FREA or parameter updates, Claude Opus 5 achieves the highest four-source mean BAcc (68.0) and
GPT-6 Astra reaches 65.7. They also lead on the two edited sources: Claude on LP (76.1 BAcc) and
GPT on GR (62.7). Criterion prompting thus yields performance competitive with dedicated veri-
fiers, together with textual rationales for expert inspection. However, they reject only 44.7–57.6%
of infeasible RP proposals, and each rejects only 4 of the 14 infeasible ZR records (Table G.2),
leaving substantial false acceptance on these sources. In addition, the binary outputs used here do
not support threshold tuning, while average API costs of US$0.040–0.059 per reaction limit their
practicality at scale (Section E.1.1).
6

Preprint
Table 3: AUROC on GR by the method that produced each candidate, with DeLong 95% confi-
dence intervals. Each column ranks the infeasible candidates of one method (count in parentheses)
against the same33feasible GR candidates, so 50 is chance and a value below 50 ranks infeasible
candidates above feasible ones. The measure is threshold-free, so it covers only systems that return a
score; rejection rates at each operating point, including those of the language models and the top-10
readouts, are in Table G.3.
Reactants changed Products changed
System RA(50)RR(53)NC(54)FT(44)ET(55)
Forward-model proxies
Chemformer (LL) 44.7[32, 57]83.5[75, 93]26.2[15, 37]87.5[79, 96]94.9[90, 100]
BARTSmiles (LL) 46.1[33, 60]79.8[70, 90]32.5[20, 45]83.5[74, 93]93.7[88, 99]
Trained on our generated negative candidates
BARTSmiles (LL+neg.) 72.7[62, 84]53.4[40, 66]94.2[90, 99]67.7[55, 81]78.1[67, 89]
BARTSmiles (disc.) 63.9[51, 77]46.5[33, 60]78.0[66, 90]68.5[56, 81]72.9[61, 85]
Descriptor GBDT 50.4[36, 65]45.6[32, 59]87.0[79, 95]67.8[56, 80]72.0[60, 84]
Forward models are the strongest verifiers of retrosynthesis proposals, but reject most feasible
edits of recorded reactions.BARTSmiles achieves the highest RP AUROC with likelihood scoring
(78.9) and BAcc with top-10 inclusion (73.1). Yet at the evaluated operating points, the four forward-
model readouts accept only 28.1–37.5% of feasible LP reactions and 12.1–33.3% of feasible GR
reactions, compared with 94.9–98.7% on ZR (Table G.2). A possible explanation is that forward
models are trained to reproduce recorded reactions, so they may penalize LP and GR departures
from recorded reaction patterns even when the edits preserve feasibility. Among the two readouts,
we recommend LL in practice: it offers comparable BAcc within each backbone, avoids the cost of
beam search, and supports threshold adjustment.
Generated negatives give the highest mean AUROC when added to a forward model’s train-
ing, whereas classifiers trained on them directly have the lowest.In Table 2, BARTSmiles (LL
+neg.) achieves 75.2 mean AUROC, while BARTSmiles (disc.) and Descriptor GBDT have lower
means than the original forward models. This contrast suggests that, in this comparison, generated
negatives are more useful for supplementing forward prediction than for training a feasibility classi-
fier directly. However, the gains of BARTSmiles (LL+neg.) come mainly from LP and GR and do
not extend to RP, so its mean lead does not imply better screening of retrosynthesis proposals. We
further study the effects of negative supervision in Section 7.
Overall,no verifier leads across all sources, indicating that agreement with experts varies by can-
didate source. For screening retrosynthesis proposals, BARTSmiles LL is a practical default among
the evaluated systems, while LLMs can provide rationales for selective expert review. Use FREA
as an initial benchmark, then validate the model and calibrate any score threshold on separate data
representative of the intended application.
6.2 PERFORMANCE BYGENERATIONMETHOD
The differences across sources in Section 6.1 leave open whether performance is consistent across
the constructions within a source. We examine this on GR, where each candidate’s generation
method is known. Table 3 compares each method’s infeasible candidates with the same 33 feasible
GR reactions drawn from all five methods.
Both forward models score below chance on NC negatives, ranking infeasible candidates
above feasible reference reactions.NC generates alternative product disconnections. Chemformer
achieves 26.2 AUROC (95% CI[15,37]) and BARTSmiles achieves 32.5 ([20,45]). Both intervals
lie entirely below 50, indicating an inversion of the desired ranking on this comparison. The same
models achieve 83.5–94.9 AUROC on FT and ET, which change the recorded product, and 79.8–
83.5 on RR, which replaces the reactant set. Both are near chance on RA, which makes local reactant
edits. Evaluation on FT, ET or RR alone would miss this failure on alternative disconnections.
BARTSmiles (LL+neg.) improves NC and RA scores but reduces RR performance relative
to BARTSmiles LL.NC increases from 32.5 to 94.2 and RA from 46.1 to 72.7, while RR decreases
7

Preprint
Table 4: One further epoch of training without and with generated negative candidates, with
matched positive reactions and training schedules. AUROC by source, log-likelihood readout.w/
neg.is BARTSmiles (LL+neg.) of Tables 2 and 3.
RP ZR LP GR Avg.
BARTSmiles 78.9 79.5 66.1 66.9 72.8
+w/o neg. 77.8−1.176.5−3.066.8+0.764.5−2.471.4−1.4
+w/ neg. 77.0−1.880.8+1.469.4+3.473.5+6.775.2+2.4
∆(w/−w/o)−0.7 +4.3 +2.6 +9.0 +3.8
from 79.8 to 53.4. The higher overall GR AUROC thus combines substantial gains and losses across
methods. The discriminative verifier exhibits a similar profile and scores below BARTSmiles (LL
+neg.) on four of the five methods.
To include systems that return only decisions, we also examine rejection rates (Table G.3). Claude
rejects at least 83% of infeasible candidates from each method, but also rejects two-thirds of the
feasible GR reactions. Its high negative rejection rates must therefore be considered together with
its rejection of feasible alternatives.
These comparisons show that source-level scores can conceal systematic failures on particular con-
structions. A separate analysis in Section G.1 shows that reaction-level performance also need not
preserve expert rankings of retrosynthesis models.
For reaction-level verification, the selective gains of BARTSmiles (LL+neg.) leave a training ques-
tion open: can generated negatives improve agreement with experts beyond specific constructions,
especially on RP? We address this with matched training comparisons in Section 7.
7 TRAINING WITHGENERATEDNEGATIVES
The preceding analyses locate failures tied to candidate construction. We now ask whether generated
negatives can improve verification across sources, particularly on RP. Using generated training pairs
that share no reaction with the benchmark (Section C.5), we first isolate the effect of adding negative
supervision (Section 7.1), then vary its generation method (Section 7.2). Each setting uses a single
training run, so the observed gains remain exploratory.
7.1 ADDINGNEGATIVESUPERVISION
The comparison in Section 6.1 does not isolate negative supervision from continued forward train-
ing. To separate their effects, we compare BARTSmiles (LL+neg.) with a control that starts from
the same BARTSmiles forward model and uses the same positive reactions and training schedule.
Both runs continue for one epoch over800,000pairs (Section E.2.3). The control optimizes only the
forward-prediction loss. BARTSmiles (LL+neg.) adds a preference loss that ranks each recorded
reaction above its generated candidate, using the same mean per-token log-likelihood as at evalu-
ation. This preserves forward-prediction training while introducing supervision from the negative
candidates.
The observed mean gain is concentrated outside retrosynthesis proposals.The four-source mean
AUROC increases from 71.4 for the continued-training control to 75.2 with negatives (Table 4). The
starting model scores 72.8, so the gain is not reproduced by the additional epoch of positive-only
training. Scores increase on ZR, LP and GR, but decrease slightly on RP.
Repeating the comparison with2,400,000pairs gives the same directions of change (Table G.1).
None of the within-source differences survives Holm correction (Section F.5). Because these runs
use a mixture of generated negatives, they leave open whether the lack of RP improvement is shared
across generation methods or depends on the mixture.
8

Preprint
Table 5: The same recipe with the negatives restricted to the candidates of one generation method,
and with an equal share of all five. AUROC by source, log-likelihood readout. Grey: difference
fromw/o neg., which is a separately trained control using the same positive-only recipe as Table 4
and the shared positive stream of this experiment (Section E.2.4).
RP ZR LP GR Avg.
w/o neg. 77.679.065.5 64.8 71.7
w/ only RA neg. 78.6+1.076.8−2.367.3+1.868.0+3.272.7+0.9
w/ only RR neg.78.9+1.379.0+0.074.4+8.967.4+2.674.9+3.2
w/ only NC neg. 74.8−2.876.4−2.667.4+1.976.9+12.173.9+2.2
w/ only FT neg. 70.7−6.976.2−2.862.2−3.452.4−12.465.4−6.4
w/ only ET neg. 77.3−0.377.3−1.768.5+3.064.5−0.371.9+0.2
w/ all-method neg. 75.3−2.377.3−1.771.0+5.572.5+7.774.0+2.3
7.2 CHOOSING THEGENERATIONMETHOD
To examine this possibility, we vary the generation method supplying the training pairs. This com-
plements Section 6.2, which varied test constructions for fixed verifiers: here we measure how
training on different negatives transfers across sources. We compare each method alone, an equal
mixture of all five, and a control without negatives. All seven runs share the initialization, positive
stream for forward prediction and training schedule. Each run with negatives uses800,000pairs;
only the pairs supplied to the preference loss change. We evaluate all runs at their final training step
under the pre-registered design (Section E.2.4).
The observed rankings of generation methods differ between GR and RP.In these runs, NC
raises GR AUROC by 12.1 points but lowers RP by 2.8 points (Table 5). RR raises mean AUROC
by 3.2 points, followed by the mixture at 2.3 points, while ET leaves the mean nearly unchanged.
Both RR and RA slightly improve RP over the control. The equal mixture has a lower mean than
RR and also lowers RP by 2.3 points.
Only the FT decline of 6.4 points in mean AUROC is significant after Holm correction (p adj =
0.001). The RR gain hasp adj = 0.08, leaving its benefit over the control inconclusive. FT also
has the lowest estimated negative purity—the fraction of candidates experts judge infeasible—at
77.2%, compared with about 93% for RR, NC and ET (Table C.1). FT’s decline therefore cannot be
attributed to its construction independently of label noise. Together with the differing outcomes of
RR, NC and ET, this motivates examining label reliability alongside other properties of the generated
candidates.
7.3 HYPOTHESES FORIMPROVINGGENERALIZATION
The method comparison shows that gains on generated constructions need not carry over to RP, but
leaves the reasons for this limited transfer open. We therefore combine the training results with
expert label audits and the descriptor-classifier analysis to formulate three hypotheses for improving
negative-data design. Each requires a separate test.
Validating negative labels may improve transfer by preserving feasible alternatives.FT com-
bines the lowest estimated negative purity with the largest performance decline. Since generated
candidates can remain feasible, assigning them negative labels can penalize valid alternatives to the
recorded reaction. This motivates expert audits of recurring labeling errors, followed by compar-
isons that filter or down-weight uncertain candidates while holding the generation method fixed.
Reducing simple descriptor differences may encourage more transferable learning.Label reli-
ability alone may not account for the outcomes: RR, NC and ET have comparable estimated purities
but different observed transfer patterns. Among these three, RR candidates are the hardest for the de-
scriptor classifier to separate from recorded reactions (Table E.1), and RR gives the largest observed
mean gain. This association motivates testing generation methods that match recorded reactions and
negative candidates on simple molecular descriptors while controlling label purity.
Targeting errors in model proposals may improve transfer more than simply mixing gener-
ation methods.Beyond label reliability and descriptor differences, useful negatives should ad-
9

Preprint
dress the errors encountered in model proposals. The NC and mixture runs both improve GR while
lowering RP, motivating a test of candidates targeted to those errors. Expert-reviewed proposals
from a separate development set could identify recurring errors and guide perturbations and method
weights. Held-out proposals would then test whether these targeted choices improve transfer.
8 CONCLUSION
FREA provides an expert reference for reaction feasibility verification across multiple candidate
sources. Its results reveal complementary strengths: criterion-prompted LLMs are competitive with
dedicated verifiers, while forward models lead on retrosynthesis proposals yet fail systematically on
some constructed candidates. No verifier leads across all sources, and strong aggregate performance
can conceal these failures. Verifiers should therefore be selected and calibrated on data representa-
tive of their intended screening task.
Our matched training experiments show how the benchmark can guide improvement: adding a mix-
ture of generated negatives raises mean AUROC without improving performance on model propos-
als, while transfer varies with the generation method. This makes performance on those proposals a
central test for negative-data design. The results motivate testing whether auditing negative labels,
controlling descriptor differences and targeting recurring proposal errors improve transfer. These
directions remain hypotheses given the benchmark’s limited coverage, judgment uncertainty and
single-run training comparisons (Section I). Together, the benchmark and accompanying corpus
support developing verifiers whose improvements are measured against expert judgments on the
reactions they must screen.
ACKNOWLEDGMENTS
This research was supported in part by NLM R01LM014385 and NSF #2435819. The content is
solely the responsibility of the authors and does not necessarily represent the official views of the
National Institutes of Health or the National Science Foundation.
REFERENCES
Anthropic. Introducing Claude 3.5 Sonnet.https://www.anthropic.com/news/
claude-3-5-sonnet, 2024.
Anthropic. Introducing Claude Opus 4.6.https://www.anthropic.com/news/
claude-opus-4-6, Feb 2026a. Accessed: 2026-05-01.
Anthropic. Introducing Claude Opus 5.https://www.anthropic.com/news/
claude-opus-5, July 2026b. Accessed: 2026-09-26.
Frazier N Baker, Ziqi Chen, Daniel Adu-Ampratwum, and Xia Ning. Rlsync: Offline–online rein-
forcement learning for synthon completion.Journal of Chemical Information and Modeling, 64
(17):6723–6735, 2024.
Frazier N Baker, Daniel Adu-Ampratwum, Reza Averly, Botao Yu, Huan Sun, and Xia Ning. Larc:
Towards human-level constrained retrosynthesis planning through an agentic framework. InPro-
ceedings of AI for Accelerated Research Symposium (AIAS), volume 3, pp. 153–176, 2026. doi:
10.29007/z3hb.
Yash Chainani, Zhuofu Ni, Kevin M Shebek, Linda J Broadbelt, and Keith EJ Tyo. Dora-xgb: an
improved enzymatic reaction feasibility classifier trained using a novel synthetic data approach.
Molecular Systems Design & Engineering, 10(2):129–142, 2025.
Shuan Chen and Yousung Jung. Deep retrosynthetic reaction prediction using local reactivity and
global attention.JACS Au, 1(10):1612–1620, 2021.
Ziqi Chen, Oluwatosin R Ayinde, James R Fuchs, Huan Sun, and Xia Ning. G 2 retro as a two-
step graph generative models for retrosynthesis prediction.Communications Chemistry, 6(1):
102, 2023.
10

Preprint
Gayane Chilingaryan, Hovhannes Tamoyan, Ani Tevosyan, Nelly Babayan, Karen Ham-
bardzumyan, Zaven Navoyan, Armen Aghajanyan, Hrant Khachatrian, and Lusine Khondkaryan.
Bartsmiles: Generative masked language models for molecular representations.Journal of Chem-
ical Information and Modeling, 64(15):5832–5843, 2024.
Connor W Coley, William H Green, and Klavs F Jensen. Rdchiral: An rdkit wrapper for handling
stereochemistry in retrosynthetic template extraction and application.Journal of chemical infor-
mation and modeling, 59(6):2529–2537, 2019.
Elizabeth R. DeLong, David M. DeLong, and Daniel L. Clarke-Pearson. Comparing the areas
under two or more correlated receiver operating characteristic curves: a nonparametric approach.
Biometrics, 44(3):837–845, 1988.
Piotr Gai ´nski, Michał Koziarski, Krzysztof Maziarz, Marwin Segler, Jacek Tabor, and Marek
´Smieja. Diverse and feasible retrosynthesis using gflownets.Information Sciences, 714:122194,
2025.
Samuel Genheden, Ola Engkvist, and Esben Bjerrum. A quick policy to filter reactions based on
feasibility in AI-guided retrosynthetic planning.ChemRxiv, 2020a. doi: 10.26434/chemrxiv.
13280495.v1.
Samuel Genheden, Amol Thakkar, Veronika Chadimov´a, Jean-Louis Reymond, Ola Engkvist, and
Esben Bjerrum. Aizynthfinder: a fast, robust and flexible open-source software for retrosynthetic
planning.Journal of cheminformatics, 12(1):70, 2020b.
Yuqiang Han, Xiaoyang Xu, Chang-Yu Hsieh, Keyan Ding, Hongxia Xu, Renjun Xu, Tingjun Hou,
Qiang Zhang, and Huajun Chen. Retrosynthesis prediction with an iterative string editing model.
Nature Communications, 15(1):6404, 2024.
Sture Holm. A simple sequentially rejective multiple test procedure.Scandinavian Journal of
Statistics, 6(2):65–70, 1979.
Ross Irwin, Spyridon Dimitriadis, Jiazhen He, and Esben Jannik Bjerrum. Chemformer: a pre-
trained transformer for computational chemistry.Machine Learning: Science and Technology, 3
(1):015022, 2022.
Shu Jiang, Zhuosheng Zhang, Hai Zhao, Jiangtong Li, Yang Yang, Bao-Liang Lu, and Ning Xia.
When smiles smiles, practicality judgment and yield prediction of chemical reaction via deep
chemical language processing.IEEE Access, 9:85071–85083, 2021.
Joonyoung F Joung, Mun Hong Fong, Jihye Roh, Zhengkai Tu, John Bradshaw, and Connor W
Coley. Reproducing reaction mechanisms with machine-learning models trained on a large-scale
mechanistic dataset.Angewandte Chemie International Edition, 63(43):e202411296, 2024.
Steven M Kearnes, Michael R Maser, Michael Wleklinski, Anton Kast, Abigail G Doyle, Spencer D
Dreher, Joel M Hawkins, Klavs F Jensen, and Connor W Coley. The open reaction database.
Journal of the American Chemical Society, 143(45):18820–18826, 2021.
Lanxin Long, Rui Li, and Jian Zhang. Artificial intelligence in retrosynthesis prediction and its
applications in medicinal chemistry.Journal of Medicinal Chemistry, 68(3):2333–2355, 2025.
Daniel Mark Lowe.Extraction of chemical structures and reactions from the literature. PhD thesis,
University of Cambridge, 2012.
Krzysztof Maziarz, Austin Tripp, Guoqing Liu, Megan Stanley, Shufang Xie, Piotr Gai´nski, Philipp
Seidl, and Marwin HS Segler. Re-evaluating retrosynthesis algorithms with syntheseus.Faraday
Discussions, 256:568–586, 2025.
Mistral AI. Mistral NeMo.https://mistral.ai/news/mistral-nemo, July 2024.
OpenAI. Introducing GPT-5.4.https://openai.com/index/
introducing-gpt-5-4/, March 2026a. Accessed: 2026-05-01.
11

Preprint
OpenAI. GPT-6 Astra.https://openai.com/index/gpt-6-astra/, September 2026b.
Accessed: 2026-09-26.
Fabian Pedregosa, Ga¨el Varoquaux, Alexandre Gramfort, Vincent Michel, Bertrand Thirion, Olivier
Grisel, Mathieu Blondel, Peter Prettenhofer, Ron Weiss, Vincent Dubourg, Jake Vanderplas,
Alexandre Passos, David Cournapeau, Matthieu Brucher, Matthieu Perrot, and ´Edouard Duch-
esnay. Scikit-learn: Machine learning in Python.Journal of Machine Learning Research, 12:
2825–2830, 2011.
Dmitrij Rappoport and Al ´an Aspuru-Guzik. Predicting feasible organic reaction pathways using
heuristically aided quantum chemistry.Journal of Chemical Theory and Computation, 15(7):
4099–4112, 2019.
RDKit. Rdkit: Open-source cheminformatics, 2024. URLhttps://doi.org/10.5281/
zenodo.14779836. Accessed on 20 April 2026.
Michal Sadowski, Tadija Radusinovi´c, Maria Wyrzykowska, Lukasz Sztukiewicz, Jan Rzymkowski,
Paweł Włodarczyk-Pruszy ´nski, Mikołaj Sacha, Piotr Kozakowski, Ruard van Workum, and
Stanislaw Kamil Jastrzebski. Trustworthy retrosynthesis: Eliminating hallucinations with a di-
verse ensemble of reaction scorers.arXiv preprint arXiv:2510.10645, 2025.
Nadine Schneider, Nikolaus Stiefl, and Gregory A Landrum. What’s what: The (nearly) definitive
guide to reaction role assignment.Journal of Chemical Information and Modeling, 56(12):2336–
2346, 2016.
Philippe Schwaller, Teodoro Laino, Th´eophile Gaudin, Peter Bolgar, Christopher A. Hunter, Costas
Bekas, and Alpha A. Lee. Molecular transformer: A model for uncertainty-calibrated chemical
reaction prediction.ACS Central Science, 5(9):1572–1583, 2019a.
Philippe Schwaller, Vishnu H Nair, Riccardo Petraglia, and Teodoro Laino. Evaluation metrics for
single-step retrosynthetic models. InSecond Workshop on Machine Learning and the Physical
Sciences (NeurIPS 2019), 2019b.
Philippe Schwaller, Riccardo Petraglia, Valerio Zullo, Vishnu H. Nair, Rico Andreas Haeuselmann,
Riccardo Pisoni, Costas Bekas, Anna Iuliano, and Teodoro Laino. Predicting retrosynthetic path-
ways using transformer-based models and a hyper-graph exploration strategy.Chemical Science,
11(12):3316–3325, 2020. doi: 10.1039/C9SC05704H.
Marwin HS Segler, Mike Preuss, and Mark P Waller. Planning chemical syntheses with deep neural
networks and symbolic ai.Nature, 555(7698):604–610, 2018.
Lukas M Sigmund, Tina Seifert, Riya Halder, Giulia Bergonzini, Magnus J Johansson, Per-Ola
Norrby, Kjell Jorner, and Mikhail Kabeshov. Predicting reaction feasibility and selectivity of
aromatic C–H thianthrenation with a qm–ml hybrid approach.Angewandte Chemie International
Edition, 64(44):e202510533, 2025.
Varvara V oinarovska, Mikhail Kabeshov, Dmytro Dudenko, Samuel Genheden, and Igor V Tetko.
When yield prediction does not yield prediction: an overview of the current challenges.Journal
of Chemical Information and Modeling, 64(1):42–56, 2024.
Daniel S Wigh, Joe Arrowsmith, Alexander Pomberger, Kobi C Felton, and Alexei A Lapkin. Or-
derly: data sets and benchmarks for chemical reaction data.Journal of Chemical Information and
Modeling, 64(9):3790–3798, 2024.
Botao Yu, Frazier N Baker, Ziqi Chen, Xia Ning, and Huan Sun. Llasmol: Advancing large language
models for chemistry with a large-scale, comprehensive, high-quality instruction tuning dataset.
InProceedings of the Conference on Language Modeling (COLM), 2024.
Bogdan Zagribelnyy, Ivan Ilin, Nikita Bondarev, Anton Morgunov, Arkadii Lin, Maksim
Kuznetsov, Rim Shayakhmetov, Vladimir Aladinskiy, Alex Aliper, and Alex Zhavoronkov.
URSA: Chemistry-aware benchmark for utilitarian retrosynthesis assessment.arXiv preprint
arXiv:2607.04688, 2026a. URLhttps://arxiv.org/abs/2607.04688.
12

Preprint
Bogdan Zagribelnyy, Ivan Ilin, Maksim Kuznetsov, Nikita Bondarev, Mathieu Reymond, Roman
Schutski, Thomas MacDougall, Rim Shayakhmetov, Zulfat Miftakhutdinov, Mikolaj Mizera,
Vladimir Aladinskiy, Alex Aliper, and Alex Zhavoronkov. When single answer is not enough:
Rethinking single-step retrosynthesis benchmarks for LLMs.arXiv preprint arXiv:2602.03554,
2026b.
Kaipeng Zeng, Bo Yang, Xin Zhao, Yu Zhang, Fan Nie, Xiaokang Yang, Yaohui Jin, and Yanyan
Xu. Ualign: pushing the limit of template-free retrosynthesis prediction with unsupervised smiles
alignment.Journal of Cheminformatics, 16:80, 2024.
Haowen Zhong, Yilan Liu, Haibin Sun, Yuru Liu, Rentao Zhang, Baochen Li, Yi Yang, Yuqing
Huang, Fei Yang, Frankie S Mak, et al. Towards global reaction feasibility and robustness predic-
tion with high throughput data and bayesian deep learning.Nature Communications, 16(1):4522,
2025.
13

Preprint
A RELATEDWORK, EXTENDED
This appendix expands Section 2 and compares the resources it mentions (Table A.1).
Filters trained on constructed negatives.Segler et al. (2018) introduced an in-scope filter: a neu-
ral classifier trained to distinguish recorded reactions from constructed ones. Its100million train-
ing negatives were generated by forward rule application and negative sampling; Genheden et al.
(2020a), who reimplemented the filter, describe the two strategies as taking the further products that
the recorded template yields on the recorded reactants (30million) and applying a randomly chosen
template to a random reactant set (70million). AiZynthFinder ships a filter built on the same prin-
ciple, and Genheden et al. (2020a) compare three ways of drawing the negatives, all template-based
and all keeping the recorded reactants: applying the recorded template to give a further product,
applying a random template, and applying a template suggested by a recommender. RetroGFN’s re-
action feasibility model is trained on negatives from two procedures, applying forward templates to
the recorded reactants to obtain a product that was not recorded, and swapping the recorded product
for another product of high Tanimoto similarity (Gai ´nski et al., 2025). The same paper separately
builds a set of hard negatives in the way our RR method does, pairing a template-generated product
with reactant sets of high Tanimoto similarity to the ones it was generated from, and uses that set
to estimate how often a forward model accepts an infeasible reaction, which is the measurement
Section 6 makes against expert labels instead. RetroTrim assembles an ensemble of scorers, some
learned and some derived from reaction databases, and shows that different scorers catch differ-
ent classes of hallucinated reaction. It evaluates reaction scores against expert labels and complete
routes for 32 targets (Sadowski et al., 2025). Its reaction-level evaluation treats Safe Bet as posi-
tive and Rather Not and Nonsense as negative, excluding Worthwhile reactions. Filters in this line
of work have been assessed on constructed test reactions and through their effects on downstream
search; Genheden et al. (2020a) also test transfer between negative generation methods.
Evaluation based on precedent.Zagribelnyy et al. (2026b) argue that scoring single-step ret-
rosynthesis by exact match against one recorded answer penalizes valid alternatives, and propose
instead to extract a proposed reaction’s reaction center and its surrounding functional-group context
and check both against a relational database of reported reactions, assigning a score of zero when
no precedent is found. They release CREED, a corpus of22,712,526reactions for1,493,715prod-
ucts generated from roughly 3,000 expert-written bidirectional templates. Precedent-based scoring
is complementary to our expert judgments, which can accept a sound proposal without a matching
recorded precedent. CREED supplies plausible generated reactions for training. FREA combines
feasible and infeasible expert-labeled candidates across four sources to evaluate verifiers and the
transfer of generated-negative training.
Negative reactions from experiment.Jiang et al. (2021) trained on failed reactions recorded in
a private industrial laboratory notebook, a resource that is not public. Zhong et al. (2025) released
high-throughput experimentation data for acid–amine couplings with Bayesian deep learning, in-
cluding observed failures under specified conditions for a single reaction class. DORA-XGB builds
an enzymatic reaction feasibility classifier, taking unreported reactions as infeasible (Chainani et al.,
2025); the assumption is strong and the domain is retrobiosynthesis. Zero-yield records are plentiful
in public databases (Kearnes et al., 2021; Wigh et al., 2024) but report an outcome under particular
conditions, so they cannot by themselves establish that a transformation is impossible. This is why
our ZR source enters the benchmark as candidates for annotation rather than as negatives.
Feasibility from first principles.Rappoport & Aspuru-Guzik (2019) explore reaction pathways
with heuristically aided quantum chemistry, and Sigmund et al. (2025) combine quantum-chemical
descriptors with machine learning to predict feasibility and selectivity for one reaction type. Mecha-
nistic datasets support models that reproduce elementary steps (Joung et al., 2024). Mechanistic and
energetic evidence from these approaches could complement expert review of difficult proposals in
future extensions.
Adjacent tasks.Yield prediction asks how much product forms under stated conditions rather
than whether a proposal is well formed, and its own difficulties are documented (V oinarovska
et al., 2024). Forward reaction prediction asks what products form (Schwaller et al., 2019a; Ir-
14

Preprint
win et al., 2022; Chilingaryan et al., 2024), and is repurposed for verification by the round-trip
convention (Schwaller et al., 2019b; Maziarz et al., 2025) that Section 6 evaluates.
Table A.1: Selected resources related to reaction feasibility.Expert labels: whether individual
reactions carry feasibility judgments by chemists.Negatives: whether the resource includes experi-
mental failures or reactions labeled infeasible.
Resource Scope Expert labels Negatives Source of negatives
Jiang et al. (2021) One laboratory —✓failed experiments
(private)
Zhong et al. (2025) Acid–amine
couplings
—✓high-throughput
experiments
DORA-XGB (Chainani
et al., 2025)
Enzymatic —✓unreported reactions
RetroGFN (Gai´nski et al.,
2025)
Small molecule —✓templates, product
swap
RetroTrim (Sadowski et al.,
2025)
Drug-like targets✓ ✓expert-rated proposals
CREED (Zagribelnyy et al.,
2026b)
Small molecule — — —
FREA (ours) Small molecule✓ ✓four sources
(Section 4)
B FEASIBILITYCRITERION ANDANNOTATIONPROTOCOL
This appendix states the criterion of Section 3 in full and gives its rationale (Sections B.1 and B.2),
specifies what annotators record (Sections B.3 to B.5), and describes how the evaluation set was
annotated (Sections B.6 to B.9).
B.1 CRITERION
For each reaction, the annotator decides whether, under some reasonable conditions, the listed reac-
tants can give the listed products in isolable form, in a single step or a credible one-pot operation.
Only the reactant and product lists are given; there are no separate fields for reagents, conditions or
yield. Any species explicitly listed on the reactant side remains part of the proposal. The judgment
combines the two conditions of Section 3, which are applied as follows.
Completeness.Every species on the left-hand side counts as a reactant, whether or not a reaction
database would record it as a reagent; what matters is whether an omitted species is essential. An
omitted species may be assumed only if it acts in one of the permitted roles of Table B.1, within
the scope stated there. Such a species isauxiliary. Anything else issubstantiveand may not be
assumed. A transformation evidently intended as a Suzuki coupling is not a complete proposal
without its organoboron partner, and an esterification written without its alcohol is not one either.
Status follows from the role a species plays here, not from its name, size or customary classification
(Table B.2), so methanol is auxiliary as a solvent and substantive as the source of a methyl ester. A
missing substantive reactant makes a reaction infeasible even when the intended transformation is
recognizable.
A proposal that is complete but for a permitted auxiliary carries a
missing auxiliary reagentnote naming the species and its role (Section B.5).
The test is structural, not stoichiometric.The test cannot be implemented by comparing ele-
ment counts, which fail in both directions. Counts can balance although a substantive partner is
missing, because leaving groups and other listed species routinely supply the same elements. In one
proposal from our pool, a substrate and the coupling reagent HATU are offered as giving a prod-
uct that bears a 2-picolylamine group; the element counts balance, since HATU supplies carbon,
nitrogen and oxygen, yet no listed species contains a picolylamine fragment, so the amine partner is
missing. Conversely, counts can fail to balance although nothing is missing: the test concerns only
15

Preprint
Table B.1: Permitted auxiliary roles. An omitted species may be assumed only when it acts in one
of these roles, within the stated scope. Any other species is substantive and must be listed.
Role Scope
Catalysis, ligation, solvation Species that supply no retained heavy atom.
Acid or base assistance Proton transfer or pH control.
Reduction, hydrogen donation Conventional reducing systems and hydrogen sources that transfer no
retained heavy atom.
Oxidation Conventional oxidants that transfer no retained heavy atom.
Water Water in conventional hydrolysis or workup.
Activation, dehydration,
coupling or deprotection
assistance
Species that enable these operations without supplying retained heavy
atoms, within the permitted single-step or one-pot operation.
Table B.2: The substantive–auxiliary boundary applied to common transformations. Within a row,
the species in the middle column acts in a permitted role and may be assumed when omitted. The
species in the right column is a reaction partner and must be listed.
Transformation Auxiliary (may be assumed) Substantive (may not)
Cross-coupling Pd catalyst, ligand, base, solvent organoboron or halide partner
Esterification acid catalyst, activating reagent alcohol
Amide coupling coupling reagent, base amine
Reductive amination NaBH 4, H2/Pd amine
Wittig olefination base ylide or phosphonium salt
Mitsunobu reaction DEAD, PPh 3 pronucleophile
Methylation base methyl source
Hydrolysis water, acid or base —
O-Demethylation BBr 3 —
Phthalimide cleavage hydrazine —
Transfer hydrogenation isopropanol as hydrogen donor —
Role dependence.The same species can fall on either side: methanol is auxiliary as a solvent and sub-
stantive as the source of a methyl ester, and isopropanol is auxiliary as a hydrogen donor and substantive
as the source of an isopropyl ester.
atoms retained in the products, so omitted by-products, unspecified stoichiometry and differences
in hydrogen count are not defects, provided a credible hydrogen source exists among the permit-
ted additions. Annotators are therefore asked where each fragment of the products comes from,
structurally, rather than whether the formula balances.
Reactivity.The annotator may assume any reasonable conditions that are not stated, including sol-
vent, temperature, time, atmosphere and order of addition, but may not replace, modify or disregard
a listed species. A reaction satisfies reactivity if, under some such conditions, the listed reactants,
completed only by auxiliary species, give the listed products in a form that can be isolated. They may
form alongside other products, which need not be listed. What is required is that the listed products
can be obtained and separated. Assumed conditions must remain compatible with the reactants and
products; hypothetical extreme conditions cannot rescue an otherwise unsupported transformation.
The reaction must take place in a single step or a credible one-pot operation, which may include
sequential addition and thein situformation of a reactive species; workup does not count as a sep-
arate step, whereas the isolation of an intermediate does. A reaction fails this condition only if no
reasonable conditions would yield the listed products.
B.2 RATIONALE AND SCOPE
Why an explicit definition is needed.Feasibility is used in the synthesis-planning literature in
at least four senses: a reaction may be called feasible because it is recorded in a database, recover-
able by a forward model from its reactants, precedented in its reaction center and functional-group
context, or executable in a laboratory. These senses agree on routine transformations but diverge
16

Preprint
on the cases that matter most for evaluation: an unprecedented but sound disconnection may be
executable, whereas a precedented transformation applied to an incompatible substrate is not. A
benchmark must therefore state which sense it measures. Ours is the validity of a retrosynthesis
proposal, judged by experts under the rules of this appendix.
Why the two conditions are defined this way.The criterion reflects chemical practice and the
requirements of synthesis planning.Chemical practice.A chemist reviewing a proposed step reads
everything on the left-hand side as reactants and judges an omission by whether the omitted species
is essential: a solvent, water or a routine additive is supplied without comment, a partner that builds
part of the product is not. Because a proposal specifies no conditions, the chemist likewise asks
whether reasonable conditions exist, not whether particular conditions are stated.Application.In
retrosynthesis planning, a proposal that omits a routine component still describes a usable step and
should be expanded, whereas one that omits the coupling partner does not describe a step at all and
should be pruned. A step is useful in a route if its product can be isolated and carried forward, and
how the material divides among competing products depends on conditions that a proposal does
not fix, so reactivity asks only that the listed products can be isolated.Informativeness.If any
unlisted species could be assumed, or any conditions however extreme, almost any product would
be reachable from almost any reactants, and a negative label would carry no information.
What the label asserts.A positive label requires more than a recognizable transformation, as the
completeness condition makes explicit. A negative label denotes a defect in the proposal as stated; it
does not assert that the transformation is impossible under every conceivable condition, a claim that
expert annotation cannot establish. Proposal feasibility is also distinct fromexperimentalfeasibility,
which additionally requires that suitable conditions be identified and that the reaction proceed in
acceptable yield in practice. Retrosynthesis proposals carry no conditions, and holding a model
that reads them responsible for experimental outcomes would penalize it for information it is not
given. The same reasoning applies to experimental records: a reported success provides evidence
that suitable conditions exist, whereas a reported failure records an unsuccessful attempt without
settling whether other reasonable conditions could work. Records of failed experiments therefore
enter the evaluation set as candidates and are labeled under the same criterion as every other source.
Independence from the source of a reaction.The criterion refers only to the listed reactants and
products, not to how the reaction was produced. It therefore applies unchanged to proposals from
retrosynthesis models, reactions edited by language models, experimental records and generated
candidates, which is what allows performance to be compared across the sources of the evaluation
set.
B.3 DECISION PROCEDURE AND RECORDED FIELDS
For each proposal, the annotator records a label (feasible,infeasibleoruncertain); one or more
failure reasons if the label is infeasible (Section B.4); one or more notes if it is feasible (Section B.5);
a difficulty rating; and a free-text note, which is required foruncertainand recommended otherwise.
Uncertainis not a softened negative. It is reserved for proposals on which the annotator genuinely
cannot decide, with the reason stated; an annotator who leans towards one label records that label.
Every proposal is taken through the ordered checks of Table B.3. Checks 1–3 take precedence: if
one fails, its reason is recorded and later checks are not applied. Otherwise, checks 4–6 are assessed
and all applicable reasons may be recorded. A proposal that passes all six is feasible. This prece-
dence is part of the protocol. A defective proposal can often be described in more than one way—a
missing amine partner, for instance, as an absent reactant or as a transformation without mechanistic
basis—and without a fixed precedence, two annotators who agree that a proposal is infeasible may
still record different reasons. Fixing the order makes the recorded reason reproducible. Two further
rules apply. The reasons at check 3 are alternatives:missing substantive reactantap-
plies when the intended transformation is recognizable and its only defect is an unlisted substantive
partner, andreactants cannot give productapplies otherwise; if both are selected, only
the latter is kept. Reasons from checks 4–6 may be recorded together when more than one applies.
17

Preprint
Table B.3: Ordered decision procedure. A failure at checks 1–3 ends the procedure; otherwise,
checks 4–6 are assessed and their reasons may be recorded together. Reasons are defined in Ta-
ble B.4. The two reasons at check 3 are alternatives (Section B.3).
# Check Reason recorded if the check fails
1 Can every listed species exist and be present?unstable or nonexistent reactant
2 Can the listed products exist as drawn?unstable or nonexistent product
3 Can the listed reactants give the products at all?missing substantive reactantor
reactants cannot give product
4 Can the intended pathway yield isolable products
despite competing processes?
reactivity conflict
5 Can the products be obtained with the specified
regio- and stereochemistry under some reasonable
conditions?
regio stereo violation
6 Can the products be obtained in one operation,
without isolating an intermediate?
requires isolated steps
— All checks passFeasible; one or more notes are recorded
(Section B.5).
B.4 FAILURE REASONS
Table B.4 defines the seven reasons. They map onto the two conditions of Section 3:
missing substantive reactantrecords a failure of completeness, and each of the other
six records a failure of reactivity. Two distinctions guide the choice of reason. First,
reactivity conflictapplies when the intended transformation is sound but a competing pro-
cess prevents the products from being isolated, whereasreactants cannot give product
applies when the transformation has no valid basis to begin with. Second, competing outcomes
do not by themselves make a proposal infeasible. If reasonable conditions could give the speci-
fied products in isolable form, even as a minor component, the proposal is feasible and carries a
selectivity concernnote. It is infeasible only if no reasonable conditions could do so. The
reason isreactivity conflictwhen a competing reaction consumes the reactants or the prod-
ucts before the target can be isolated, andregio stereo violationwhen no available mecha-
nism produces the specified isomer. Because catalysts and conditions may be assumed, a selectivity
that a known catalyst or set of conditions can achieve counts as obtainable. A stereocenter or substi-
tution pattern that the transformation does not touch, yet differs between reactants and products, is
not a question of selectivity and is recorded at check 3 asreactants cannot give product.
Thus, an isolable minor regioisomer remains feasible even when another isomer predominates.
B.5 NOTES ONFEASIBLEPROPOSALS
Notes document the components or conditions assumed when assigning a feasible label. The four
note categories are:
no identified caveatEvery species that must be physically added is already listed, and no
material concern is identified. It does not claim that a complete procedure is given or that the
experiment would succeed, and it excludes all other notes.
missing auxiliary reagentA species permitted by Table B.1 is required but not listed,
such as the base of an alkylation or the reductant of a reductive amination. The annotator names
it and its role.
selectivity concernCompeting chemo-, regio- or stereochemical outcomes are possible,
but reasonable conditions could still give the products in isolable form.
harsh conditionsCredible but demanding conditions, such as elevated temperature or pres-
sure, are required. The conditions must remain compatible with the reactants and the products;
hypothetical extreme conditions cannot rescue an otherwise unsupported transformation.
18

Preprint
Table B.4: Failure reasons recorded for infeasible proposals, in the order of the checks in Table B.3.
Reason Definition
unstable or nonexistent reactantA listed species, substrate or reagent, is drawn
incorrectly, cannot exist, or is too unstable to be present.
Lack of bottle stability alone does not qualify a species
that can credibly formin situ.
unstable or nonexistent productA listed product has a structural or stability defect that
prevents it from reasonably existing or being obtained as
drawn. Unfamiliarity, or failure of software to parse it,
does not qualify.
missing substantive reactantThe intended transformation is recognizable, but a
partner that is not a permitted auxiliary is not listed.
reactants cannot give productThe listed species can exist, but lack a credible
mechanistic route to the products: the skeletons do not
correspond, a listed reagent cannot perform its required
role, or there is a concrete mechanistic obstacle.
reactivity conflictA functional group or listed component causes a
competing reaction, quenching or decomposition that
intercepts the intended pathway, so that the products
cannot be obtained in isolable form within the permitted
single-step or one-pot operation.
regio stereo violationNo reasonable conditions give the products with the
specified regio- or stereochemistry in isolable form.
Typical cases are an outcome opposite to the one a
stereospecific or regiospecific mechanism fixes, and a
substitution pattern that no available mechanism
produces. An isolable minor isomer does not qualify.
requires isolated stepsObtaining the products requires an additional,
independent step with isolation of an intermediate.
These notes document the assumptions accompanying a feasible label; the evaluation target is the
binary feasibility label. Difficulty ratings record annotation effort and are not used in the reported
evaluations.
B.6 ANNOTATORS AND INTERFACE
Proposals were labeled by two annotators, a pharmacy faculty member and a postdoctoral researcher
in chemistry, both with extensive knowledge of organic chemistry and wet-laboratory experience.
Each proposal was presented in a web interface that renders the reactants and the products as struc-
tures from their SMILES, with the SMILES strings available on request. The annotators had no
access to proposal sources or model predictions. The41calibration reactions in the pool were set-
tled during calibration. The759reactions outside the calibration set were labeled independently
under the final protocol, without access to each other’s labels.
B.7 PROTOCOL CALIBRATION
Before the main annotation, both annotators labeled a calibration set of50proposals under a draft
of the guideline,41of which belong to the annotation pool. The other nine calibration proposals are
outside the pool and are not included in the released benchmark. Disagreements were discussed by
cause, and the discussion was used to amend the guideline and align the annotators’ understanding.
The labels of the calibration proposals were settled in the same discussion, so the41that belong to
the pool are part of the benchmark but are excluded from the agreement analysis of Section B.8. The
amendments made the substantive–auxiliary test and its structural reading explicit (Section B.1), in-
troduced the ordered decision procedure (Section B.3), and consolidated overlapping failure reasons
into the seven of Table B.4. These amendments were in force for the whole of the main annotation.
19

Preprint
Table B.5: Independent labels of the two annotators before adjudication, on the759reactions of the
annotation pool outside the calibration set. Rows give the first annotator’s label and columns the
second’s.
Annotator 2
Annotator 1 Feasible Infeasible Uncertain Total
Feasible255 77 0 332
Infeasible90 336 0 426
Uncertain0 1 0 1
Total345 414 0 759
B.8 AGREEMENT AND ADJUDICATION
Table B.5 gives the independent labels of the two annotators, before any adjudication, on the759
reactions of the pool that are not in the calibration set. Agreement was 77.9%, with Cohen’sκ=
0.55(95% CI [0.49, 0.61]). These statistics measure independent judgments before joint review.
Of the168disagreements,119were adjudicated by joint review against the written guideline. The
remaining49await adjudication and are excluded from the current benchmark and its reported
evaluations. The benchmark therefore contains591reactions with matching independent labels,
119with adjudicated labels, and the41calibration reactions, totaling751reactions from the800-
reaction pool. Recorded reasons and notes are provided as supporting metadata where available.
B.9 SCREENING
Before annotation, every reaction from every source was screened with the general validity rules
applied to the corpus (Table D.1). A reaction was discarded if its SMILES failed to parse or canoni-
calize, if it contained an unstable motif such as an O – O – O or B – O – O chain, if a product appeared
unchanged among its reactants, or if a product contained more heavy atoms of some element than
the reactants. The screen removes parsing failures and predefined structural patterns. The remaining
reactions still require expert judgment. No additional structural screening was applied after annota-
tion.
These filters define the structural scope of the benchmark; they do not implement the substantive–
auxiliary distinction. Reactions that pass them are evaluated by the experts for completeness and
reactivity under the stated criterion.
C CONSTRUCTION OF THEBENCHMARK
Section 4 presents the benchmark by source. This appendix describes how it was built, in the order
of construction: curating positive reactions from ORDerly (Section C.1), generating negative candi-
dates (Section C.2), collecting the reactions of each source (Section C.3), screening and annotation
(Section C.4), and checking overlap with the training data (Section C.5).
C.1 POSITIVE REACTIONS
Positive reactions are taken from ORDerly (Wigh et al., 2024), a curated subset of the Open Reaction
Database (Kearnes et al., 2021) with standardized atom mapping and yield annotations, starting from
its retrosynthesis train and test splits. All SMILES are canonicalized with RDKit (RDKit, 2024).
Reactions with a recorded yield of zero are removed from the positives and archived as candidates
for the benchmark (Section C.3). We then discard exact duplicates and every reaction that violates
a rule markedAllorPositivein Table D.1: reactions that fail parsing, reactions in which a product
component appears verbatim among the reactants, reactions containing an O – O – O or B – O – O
chain, reactions in which a product contains more atoms of some heavy element than the reactants,
and reactions with three or more highly similar reactant components. The curated corpus contains
801,276training and76,630test positives.
20

Preprint
C.2 NEGATIVE CANDIDATES
The five generation methods of Section 4.1 are applied to every positive reaction in both splits
(Section D). Each candidate inherits the split of the positive reaction from which it was derived
and passes the quality-control pipeline of Section D.7. Candidates derived from test-split reactions
supply the generated source of the benchmark; the full output forms the generated corpus analyzed
in Section 7 and Section D.8.
C.3 COLLECTING THE FOUR SOURCES
Table C.1 breaks the benchmark down by the model, language model or generation method that
produced each reaction.
Retrosynthesis proposals.For targets from the test split, we collected reactant proposals from
eight single-step retrosynthesis models: LocalRetro (Chen & Jung, 2021), G2Retro (Chen et al.,
2023), UAlign (Zeng et al., 2024), EditRetro (Han et al., 2024), Chemformer (Irwin et al., 2022),
LlaSMol (Yu et al., 2024), and LARC (Baker et al., 2026) with two backbone language models,
Claude 3.5 Sonnet (Anthropic, 2024) and Mistral NeMo (Mistral AI, 2024). Proposals were pooled
across models and deduplicated by canonical SMILES. They were retained whether or not they
reproduce the recorded reactants, since both kinds belong to the distribution a model faces in de-
ployment.
Zero-yield records.From ORDerly we retrieve the reactions with a recorded yield of exactly zero
that were removed during positive curation, apply the same canonicalization and validity rules, and
remove any reaction whose canonical reactant–product pair also occurs among the positives. A
zero-yield record shows only that the conditions tried did not give the product (Section B.2); these
reactions are labeled under the same criterion as every other source.
LLM perturbations.Recorded reactions from the test split were given to GPT-5.4 (OpenAI,
2026a) and Claude Opus 4.6 (Anthropic, 2026a), which were instructed to modify the reactants
or the product so that the reaction becomes infeasible while remaining superficially coherent. The
instruction states the models’ intent only; whether a modified reaction is infeasible is decided by the
annotators.
Generated reactions.Generated candidates were sampled in equal numbers from the test-split
output of each of the five generation methods (Section D). All289are outputs of these methods,
including those the annotators judged feasible.
C.4 SCREENING AND ANNOTATION
Before annotation, every reaction from every source passed the screen described in Section B.9. The
screened pool of800reactions was then labeled under the protocol of Section B. The calibration, in-
dependent annotation and adjudication procedure yields the751benchmark reactions (Section B.8).
C.5 SPLITS AND OVERLAP
The corpus follows the ORDerly retrosynthesis train/test split, and all benchmark reactions except
the zero-yield records derive from the test split. No benchmark reactant–product pair occurs in the
data used to train our models. Product overlap remains possible even when the complete reaction
differs.115benchmark reactions have a main product that is also the product of a training reaction,
97of them retrosynthesis proposals. BARTSmiles log-likelihood scores76.6AUROC on those97
proposals against80.8on the other185; this comparison is descriptive because the two subsets may
differ in difficulty.
D NEGATIVECANDIDATEGENERATION
The generated reactions in the benchmark and the training corpus are produced by five generation
methods. Each produces candidates intended to be infeasible, and whether a candidate is in fact
21

Preprint
Table C.1: Breakdown of the benchmark by the model, language model or negative candidate gen-
eration method that produced each reaction.Infeas. (%)is the share of a row’s reactions the experts
judged infeasible, which for a generation method is the share of its candidates that are genuinely
negative.
Source Origin Feasible Infeasible Total Infeas. (%)
RP LARC (Claude 3.5 Sonnet)43 12 5521.8
LARC (Mistral NeMo)42 12 5422.2
G2Retro17 13 3043.3
EditRetro18 12 3040.0
LlaSMol16 13 2944.8
UAlign14 15 2951.7
Chemformer22 6 2821.4
LocalRetro25 2 277.4
ZR ORDerly zero-yield records79 14 9315.1
LP GPT-5.415 30 4566.7
Claude Opus 4.617 25 4259.5
GR RA8 50 5886.2
RR4 53 5793.0
NC4 54 5893.1
FT13 44 5777.2
ET4 55 5993.2
Total341 410 75154.6
infeasible is established only by expert annotation (Section 4.2). This appendix summarizes the
procedures, their main settings, and the quality-control pipeline.
D.1 DESIGN
Each method perturbs a positive reaction(R ∗,P ∗)along one of two axes. Reactant perturbations
(RA, RR, NC) replaceR ∗ with ˜Rwhile holding the products fixed, whereas outcome perturbations
(FT, ET) replaceP ∗ with ˜Pwhile holding the reactants fixed. All five methods are applied to every
positive reaction in both splits, and each candidate retains a pointer to its parent positive, which
supports pairwise training and method-level analysis.
D.2 RANDOMADDITION(RA)
RA modifies one or more reactants at the reaction center. Each reactant is reduced to its synthon by
removing leaving groups, atoms drawn from a frequency-weighted distribution of common leaving-
group atoms (e.g., C, O, N, halogens) are appended iteratively at the reaction center under valence
constraints, for at most six addition steps per synthon, and the modified synthons are reassembled
into reactants ˜R, giving the candidate( ˜R,P ∗). Up to three candidates are generated per positive
reaction. The modification is intended to make a reactant incompatible with the required bond-
forming event. It does not guarantee a difficult candidate, and it can produce a reactant that still
undergoes a related transformation.
D.3 RANDOMREPLACEMENT(RR)
RR replaces the reactants with structurally similar reactants drawn from the positive training set. For
each positive reaction, we retrieve the 200 most similar reactions by Tanimoto similarity on a joint
reactant–product fingerprint and take as ˜Rthe reactants of the highest-ranked ones that are similar
to, but different from,R ∗. Up to nine candidates are formed per positive reaction, eight in this way
and one from a reactant set drawn at random from the training set. The procedure does not verify
that the replacement fails to giveP ∗, and it discards replacements whose Tanimoto similarity to the
original reactant falls below0.1(Table D.1).
22

Preprint
D.4 NEWCENTER(NC)
NC proposes an alternative disconnection of the product. The reaction-center model of
G2Retro (Chen et al., 2023) predicts the top-10 candidate centers forP∗, and up to three centers that
differ from the recorded one are retained, taken from the lowest-ranked end of the list. The resulting
synthons are completed by RLSynC (Baker et al., 2024), which returns ten completions ranked by
its value estimate, and the low-ranked completions are selected. A low rank indicates only that a
completion is unlikely under RLSynC, not that the resulting proposal is infeasible.
D.5 FORWARDTEMPLATE(FT)
FT applies forward reaction templates extracted from the positive training set to the recorded reac-
tants, using RDChiral (Coley et al., 2019). We apply every template that occurs at least ten times
in the training set together with up to ten randomly drawn rarer templates per reaction, and every
product ˜Pthat differs fromP ∗ under canonical SMILES comparison gives a candidate(R ∗, ˜P). A
product predicted by a template but not recorded for these reactants may nevertheless be feasible.
D.6 ELEMENTARYTEMPLATE(ET)
ET enumerates elementary steps with 739 templates from the library of elementary templates
of Joung et al. (2024). Starting fromR ∗, the templates are applied breadth-first for up to four
steps, and every product reached in at least two steps that differs fromP ∗ and is not recorded as a
product of these reactants gives a candidate, with at most 50 candidates per reaction. As for FT, an
unrecorded product is not necessarily infeasible.
D.7 QUALITY CONTROL
All candidates pass a unified pipeline of 16 rules in three tiers: general validity, negative–positive
consistency, and removal of method-specific artifacts (Table D.1). In particular, no candidate may
encode a product set that is a recorded outcome of the same reactants in the positive corpus.
D.8 SIZE OF THE GENERATED CORPUS
Table D.2 gives the size of the generated corpus by split and method. Per-method rows count can-
didates before cross-method deduplication, whereas theNegativerow counts unique canonical reac-
tions. The per-method rows therefore sum to20,772(train) and1408(test) more than theNegative
row. These excess counts arise from candidates produced by more than one method.
E SYSTEMIMPLEMENTATIONS
This appendix describes the evaluated systems and their training settings. Model selection, decision
thresholds and statistical tests are given in Section F.
E.1 LLMS ANDBASELINES
E.1.1 LARGELANGUAGEMODELS
We query Claude Opus 5 and GPT-6 Astra through their APIs with extended reasoning at thehigh
setting, one call per reaction, with no examples from FREA and no parameter updates. Both models
receive the same system prompt, verified identical byte for byte. It states the criterion of Section 3
operationally: what may be assumed without being listed, what may not, and six conditions under
which the reaction is not feasible, which correspond to the failure reasons of Section B.4 with the
third condition covering two of them. The user message carries the reactant and product SMILES.
The decision is read from the final answer tag. One Claude Opus 5 response contained no parsable
tag and is excluded from its metrics. Claude Opus 5 used on average1073prompt and532comple-
tion tokens per reaction, at a total cost of US$30.31 for the751reactions (US$0.040 per reaction).
23

Preprint
Table D.1: Summary of the 16 filtering rules used to construct the generated corpus. “All” denotes
filters applied to both recorded positives and generated candidates; these general filters also screen
the benchmark before annotation. Methods are described in Section D.
Rule Scope Condition for invalidation
General validity
all invalid smilesAll Canonical reactant or product SMILES is null
product in reactantAll Any product component appears verbatim among
the reactant components
unstable substructureAll Reactant or product contains an O – O – O or
B – O – O chain
atom conservationAll Products contain more atoms of any heavy element
than the reactants
reactant internal similarityPositive Median pairwise reactant Tanimoto>0.5with≥3
components
Negative–positive consistency
negative parent not noneNegativeparentfield is null
negative split match parentNegative Negative split̸=parent split, or parent not found
negative parent not invalidNegative Parent positive has been marked invalid
ra nc reaction centersRA, NC Parent has nullreaction centersannotation
neg is not posNegative Product set⊆some positive’s product set for the
same reactant SMILES
Method-specific artifacts
ft small productFT Product has<6heavy atoms
ft stereo onlyFT Product equals parent product after stripping stere-
ochemical annotations
ft et tautomer equivFT, ET Product is a strict tautomer of the parent product
rr reactant too dissimilarRR Tanimoto(replacement reactant, original reactant)
<0.1
nc small fragmentNC Reactant set contains a blacklisted, chemically un-
reasonable fragment
nc spurious ciNC Methyl iodide present in reactants but contributes
no net methylation to the product
Table D.2: Size of the generated corpus by split. Per-method rows count candidates before cross-
method deduplication; theNegativerow counts unique canonical reactions.
Train Test
Positive801,276 76,630
Negative (unique)12,047,157 1,189,994
RA1,705,924 163,253
RR3,024,969 295,737
NC1,433,340 149,175
FT1,781,362 181,411
ET4,122,334 401,826
Total (unique)12,848,433 1,266,624
GPT-6 Astra used on average709prompt and1032completion tokens,956of them for reasoning,
at a total cost of US$44.07 (US$0.059 per reaction) and 32.6 seconds per call.
E.1.2 FORWARD-MODELPROXIES
Chemformer (Irwin et al., 2022) and BARTSmiles (Chilingaryan et al., 2024) are fine-tuned for
forward prediction on the recorded reactions of the training split, so neither sees a negative candidate.
Chemformer starts from its released checkpoint and is trained for 20 epochs. BARTSmiles starts
from the Stage-1 checkpoint of Section E.2 and is trained for15,490steps. Each is taken at the
checkpoint with the lowest validation loss: epoch 17 for Chemformer (validation loss 0.04685,
against 0.04687 at the last epoch) and step12,000for BARTSmiles (0.04678, against 0.04811 at
24

Preprint
step15,000). The validation reactions of BARTSmiles largely overlap with those used in Stage 1,
so its validation loss is optimistic in absolute terms. It serves only to pick a checkpoint.
For the top-10 readout, each model generates 50 beams, and a reaction is accepted if the canonical
SMILES of its products matches one of the ten highest-ranked predictions. The log-likelihood
readout is the mean per-token log-probability of the product string given the reactant string under
teacher forcing, computed with a maximum length of1700tokens for BARTSmiles and the default
length of Chemformer.
E.1.3 THEAIZYNTHFINDERIN-SCOPEFILTER
Evaluation setup.We evaluate the released AiZynthFinder filter as an existing planning baseline.
The model embeds ECFP4 fingerprints of the product and the difference between product and re-
actant fingerprints, and scores them by cosine similarity. It has about 4.2M parameters and was
trained on911,869USPTO reactions and1,621,484template-generated negatives (Genheden et al.,
2020a). We useuspto filter model.onnxfrom version 4.4.1 without retraining, through
AiZynthFinder’s own reaction objects and filter implementation. No reactant failed to parse. We
report results using both the threshold rule of Section F.4 and the filter’s default cutoff of 0.05;
AUROC is independent of the cutoff.
Potential training-data overlap.The training set is not released. We check against Lowe’s raw
USPTO extraction (Lowe, 2012), a superset of the training data, to bound possible overlap. Matching
up to reagents,132benchmark reactions appear there: 92 of 93 ZR, 33 of 87 LP, 7 of 282 RP and
none of the 289 GR reactions. These matches indicate possible exposure, particularly for ZR and
LP, rather than verified membership in the filter’s training set. On the619reactions with no match,
its pooled AUROC is 63.3.
Performance across generation methods.On the held-out generated pairs of Section F.4, AU-
ROC is 89.0 for FT, 83.6 for ET and 58.0 for NC. Three additional released filters trained on indi-
vidual negative types show the same ordering.
Scope of the comparison.These results characterize how the released filter transfers to FREA.
Its training data and input conventions differ from ours: its inputs omit reagents, its fingerprints
ignore stereochemistry, and its negative labels come from template-generated candidates. Removing
carbon-free fragments from the benchmark’s reactant lists changes pooled AUROC from 65.9 to
65.3. The benchmark comparison therefore evaluates the existing tool under our criterion. Section 7
explores changes to negative training data using matched training runs.
E.1.4 FEATURE-BASEDCLASSIFIER
Features.Twenty-two additive descriptors are computed for the products and as the difference
between products and reactants: molecular weight, heavy atoms, rings, aromatic rings, rotatable
bonds, hydrogen-bond donors and acceptors, topological polar surface area, logP, formal charge,
bonds, stereocenters, and the counts of C, N, O, S, P, F, Cl, Br, I, and other heavy elements. To
these 44 features we add the numbers of reactants and products, the product-to-reactant ratios of
molecular weight and heavy atoms, the lengths of both SMILES strings and their ratio, the excess
of heavy atoms in the products and the number of elements whose count increases, the maximum,
mean, and minimum Tanimoto similarity between the Morgan fingerprints (radius 2,2048bits) of
the largest product and each reactant, and two indicators of whether the product is a substructure of
a reactant or the reverse, for 58 features in total, all computed with RDKit (RDKit, 2024).
Model and data.We train a histogram gradient-boosted tree classifier (Pedregosa et al., 2011)
with 400 iterations, learning rate 0.06, at most 31 leaves, at least 20 samples per leaf, L2 regulariza-
tion 1.0, and early stopping on an internal 10% split. The training data are100,000pairs from the
training split,20,000per method, in which every recorded reaction appears at most once. None of
the200,000rows coincides with a benchmark reaction, even after sorting reactant fragments. The
predicted probability of feasibility is the score, thresholded at0.510, the value that maximizes BAcc
on the held-out generated pairs of Section F.4.
25

Preprint
Benchmark performance.Descriptor GBDT reaches 70.7 mean AUROC on FREA. On the per-
method GR comparison, it reaches 87.0 on NC but is near chance on RA and RR (Table 3). The
descriptors therefore provide a useful reference, with performance varying substantially by candidate
type.
Separability of each method’s candidates.On the held-out 10% of the training pairs, about2000
candidates of each method are scored against10,000recorded reactions (Table E.1). Before running
this analysis we predicted that RR candidates, which use unmodified reactants from other recorded
reactions, would be the hardest to separate. The prediction holds among the three methods with
similar estimated negative purities. RA and RR have similar separability here, which may reflect
RA’s lower estimated purity or the limited descriptor changes caused by its edits.
Table E.1: AUROC of Descriptor GBDT in separating each method’s negative candidates from
recorded reactions on held-out training pairs, with DeLong 95% confidence intervals. Negative
purity is estimated separately from the expert-labeled GR subset (Table C.1).
Method Purity (%) Candidates AUROC
NC 93.1198198.5[98.2, 98.8]
FT 77.2197092.5[91.7, 93.2]
ET 93.2198591.5[90.8, 92.2]
RR 93.0200286.4[85.6, 87.2]
RA 86.2206285.9[85.1, 86.7]
What the model uses.Permutation importance on the benchmark ranks the change in bond count,
the change in carbon count, and the two substructure indicators highest. The heavy-atom excess
and the number of elements whose count increases have zero importance, consistent with the pre-
annotation screen removing these element-count excesses (Section B.9). Fitting the same model
directly on the benchmark by five-fold cross-validation gives a pooled AUROC of 75.0, compared
with 79.8 for the model trained on generated pairs. These scores reflect both reaction-level discrim-
ination and source composition (Section F.1), so they do not by themselves establish how well these
descriptors capture feasibility within a source.
E.1.5 RULE-BASEDBASELINE
Rule Check is a non-learning cascade implemented with RDKit. It rejects a reaction if (1) a product
cannot be parsed, (2) a molecule contains an unstable motif such as an O – O – O or B – O – O chain,
(3) the products contain more atoms of some heavy element than the reactants, (4) a product appears
unchanged among the reactants, (5) no reactant has a Morgan-fingerprint similarity to the product
above a small threshold, or (6) a functional group formed in the product, such as an amide, ester,
ether, imine, urea, carbamate, sulfonamide, nitrile, or nitro group, has no compatible precursor
among the reactants, unless the product is a substructure of a reactant or is highly similar to one.
Rules (1) to (4) coincide with the pre-annotation screen, so on FREA only rules (5) and (6) can reject
a reaction. The baseline averages 60.2 BAcc over the four sources (Table G.1), and we omit it from
the main text.
E.2 MODELSTRAINED WITHGENERATEDNEGATIVECANDIDATES
This appendix describes BARTSmiles (disc.), the six other discriminative verifiers reported in Ta-
ble G.5, and the controlled comparisons of Section 7. All models use random seed 42. The settings
held fixed within each experiment family are specified below.
E.2.1 THEDISCRIMINATIVEVERIFIER
Backbone and input.BARTSmiles (disc.) is built on BARTSmiles (Chilingaryan et al., 2024),
a BART-style encoder–decoder model pre-trained on SMILES strings. A reaction is written as
{reactants}[[>>]]{products}[[Judge]], where molecules are canonicalized with RD-
Kit (RDKit, 2024) and joined by periods. There are no separate reagent or condition fields; any
species listed among the reactants remains in the input. The tokens[[>>]],[[Judge]], and
26

Preprint
[[Yes]]are added to the vocabulary with randomly initialized embeddings. The whole string is
the encoder input. The decoder receives its start token, and the logit of[[Yes]]at the first de-
coding position is the feasibility scores(R,P)∈R. Scoring a reaction therefore costs one encoder
pass and one decoder step.
Stage 1: reaction denoising.Reaction strings are longer than the single molecules seen in pre-
training, so the model is first adapted to them by denoising. On the recorded reactions of the training
split, contiguous token spans with lengths drawn from a Poisson distribution (λ= 3.5) are corrupted,
up to 20% of the non-special tokens. Corrupted positions are replaced by a<mask>token or by
random tokens, and the decoder reconstructs the original string under the usual cross-entropy loss.
The checkpoint with the lowest validation reconstruction loss initializes Stage 2.
Stage 2: pairwise training.Each negative candidate in the training split is paired with the
recorded reaction from which it was generated. Candidates that coincide after canonicalization
are merged, and a candidate produced by several methods is assigned to one of them so that all
five methods contribute equally. All parent reactions in the resulting7,095,035pairs belong to the
positive training corpus of Section C.1. For a batch ofBpairs with scoress + i (recorded reaction)
ands − i (negative candidate), the loss is
L=α BT LBT +α BCE LBCE +α C LC,(α BT, αBCE, αC) = (0.8,0.1,0.1),(2)
with
LBT =− 1 B
BX
i=1
logσ

s+ i −s − i  ,(3)
LBCE =− 1 2B
BX
i=1

logσ

s+ i  + log  1−σ  s− i  ,(4)
LC =

1
2B
BX
i=1

s+ i +s − i 
!2
,(5)
whereσis the logistic function. The Bradley–Terry termL BT ranks each recorded reaction above its
candidate and is unchanged when a constant is added to all scores. The cross-entropy term removes
this invariance by tying the scores to a decision boundary at zero, and the centering term keeps the
mean score of a batch near zero. The cross-entropy term alone would not bound the scores, since
it keeps decreasing as they grow apart. The centering term controls the batch mean, while weight
decay regularizes the model parameters.
Dynamic re-weighting.Methods differ in how quickly the model learns their candidates. EveryT
steps, the pairwise accuracyacc m of the current model on held-out pairs of methodmis measured,
and pairs of methodmare then sampled with probability
wm ∝exp
 1−acc m
τ

,(6)
whereτis a temperature, and no method falls below a sampling probability of 0.05. BARTSmiles
(disc.) usesT= 5000steps.
Decision rule.A reaction is predicted feasible ifs(R,P)> t, wheretis the raw logit threshold
frozen on held-out generated pairs (Table F.4).
E.2.2 THEDISCRIMINATIVEVERIFIERFAMILY
Table E.2 lists the seven discriminative verifiers. All start from the same Stage-1 checkpoint and
use the same Stage-2 loss, optimizer settings, and effective batch of 512 pairs. They are compared
at step20,000, where each has seen10.24million pairs. The number of distinct recorded reactions
in the training pairs differs across methods. FT has the fewest, each appearing 8.6 times on average.
27

Preprint
Table E.2: Training configuration of the seven discriminative verifiers. All are evaluated at step
20,000. A balanced pool contains equal numbers of candidates from each method; dynamic re-
weighting changes their sampling probabilities during training.
Negative candidates Pairs Re-weighting Steps trained
One method (RA, RR, NC, FT, or ET)1,419,007none22,168
All five methods, balanced pool1,419,007every1000steps22,168
All five methods (BARTSmiles (disc.))7,095,035every5000steps41,571
E.2.3 THECONTROLLEDPAIRS
The models of Section 7 start from the BARTSmiles forward model of Section E.1.2 and are trained
for one epoch, with identical order, seed, learning-rate schedule, warmup, and numerical precision
within a pair. The smaller pair uses800,000pairs (6250steps) and the larger2,400,000(18,750
steps), at an effective batch of 128. The first optimizes the forward-prediction loss−logp θ(P|
R)on the recorded reaction of each pair, and its negative candidates are loaded but unused. The
second adds a weighted Bradley–Terry term likeL BT, computed on the score used at inference, the
mean per-token log-likelihood ¯ℓθ(R,P), of the recorded reaction and of its candidate. Every run is
evaluated at the end of its epoch, so no checkpoint is selected. Selecting by validation loss would
break the pairing, because the loss of the run with negatives contains the preference term and the loss
of the run without it does not, so the two are not the same quantity. Benchmark AUROC varies by at
most 1.0 point over the second half of each run. All four are thresholded like every other continuous
score.
E.2.4 THEPER-METHODCOMPARISON,ANDITSPRE-REGISTRATION
The seven groups of Table 5 share the recipe of Section E.2.3 at the800,000-pair scale and differ only
in the pairs the preference term sees: none (the reference),800,000from one method, or160,000
from each of the five. The forward-prediction loss is computed on one stream of recorded reactions,
in one order, shared by all seven. This holds the forward-prediction signal fixed while varying the
pairs supplied to the preference loss. In the discriminative family, positive examples are drawn from
each method’s own pairs, so the method comparisons also vary positive coverage. The mixture uses
plain concatenation with no re-weighting. Every group is trained for one epoch of6250steps from
the same initialization with identical optimizer settings and seed, and is scored at the final step.
The design, the endpoints and the analysis were written down before any training data was sampled
and before any run was launched. The primary endpoint is each group’s four-source mean AUROC
minus the reference group’s, tested by a paired bootstrap stratified by source with Holm correction
across the six groups. The registration also fixed the rule that conclusions about methods are drawn
from the three with similar estimated negative purities, RR, NC and ET, with FT and RA reported for
reference. It recorded three predictions: that RR would not be lower than any other group receiving
negatives, that FT would be the lowest of the five single-method groups, and that the mixture would
not exceed the reference on RP. The observed point estimates follow all three predictions.
One deviation is recorded. The registration required the sampled training pairs to contain no bench-
mark reaction and the experiment to stop otherwise. The first sample contained four such pairs, the
runs were stopped, and each was replaced by the next unused clean pair of the same permutation
before the runs were restarted. No stream shares a reaction with the benchmark.
The positive-only control is trained separately for this experiment using its shared positive stream.
Its mean AUROC is 71.7, compared with 71.4 for the smaller control in Table 4; the respective ZR
scores are 79.0 and 76.5. Each negative-supervision effect is therefore measured against the control
trained under the corresponding comparison design.
28

Preprint
F EVALUATIONPROTOCOLDETAILS
F.1 METRICS
AUROC is the probability that a randomly drawn feasible reaction receives a higher score than a
randomly drawn infeasible one, with ties counted as one half. We compute it within a source. TPR
is the share of feasible reactions a system accepts, TNR the share of infeasible reactions it rejects,
and BAcc their mean. Within a fixed source, BAcc weights the two classes equally. The average
of a system is the unweighted mean over the four sources and was fixed before the evaluation. It
includes GR, whose generation methods also supply the negative training data for several systems.
The AUROC of a negative candidate method on GR compares that method’s infeasible candidates
with all 33 feasible GR candidates, which come from all five methods (RA 8, RR 4, NC 4, FT 13,
ET 4).
Why we evaluate within sources.Feasible rates range from 11.4% in GR to 84.9% in ZR. To
illustrate the effect on a pooled score, each reaction receives the fraction of feasible labels in its
source in Table 1. We then compute AUROC over all reactions. Every within-source comparison
is tied and contributes one half, but the between-source comparisons raise pooled AUROC to 82.1.
These source rates are estimated from the benchmark labels; the calculation illustrates what pooled
AUROC can reward without assessing individual reactions. Pooling also reverses a model com-
parison: BARTSmiles (disc.) exceeds Chemformer LL in pooled AUROC (82.5 versus 81.9), but
is lower in four-source mean AUROC (69.7 versus 72.6). Evaluating within each source prevents
between-source comparisons from dominating the reported performance.
F.2 SENSITIVITY TOAUXILIARY-REAGENTANNOTATIONS
We assess the effect of auxiliary-reagent annotations by excluding the104feasible reactions car-
ryingmissing auxiliary reagentand evaluating all systems at the same frozen thresholds
(Table F.1). This subset is defined from annotation metadata without reference to model predictions.
The note records a permitted auxiliary omission under Section B.1.
Claude Opus 5 retains the highest mean BAcc, while some intermediate rankings change. The
four leading mean AUROCs range from 74.6 to 75.0 on the restricted subset: BARTSmiles (LL+
neg.) is comparable to the forward baselines here, rather than retaining its full-benchmark lead. Its
advantage over BARTSmiles (disc.) remains 4.2 points.
Table F.1: Source-mean scores after excluding the104feasible reactions annotated with
missing auxiliary reagent, using the same frozen thresholds. Full AUROC is reproduced
from Table 2; restricted AUROC and BAcc use the remaining reactions.
System Full AUROC Restricted AUROC Restricted BAcc
Claude Opus 5 – – 70.0
GPT-6 Astra – – 67.2
Chemformer (top-10) – – 64.5
Chemformer (LL) 72.6 74.6 65.7
BARTSmiles (top-10) – – 67.9
BARTSmiles (LL) 72.8 75.0 66.7
BARTSmiles (LL+neg.) 75.2 74.9 63.6
BARTSmiles (disc.) 69.7 70.7 59.6
Descriptor GBDT 70.7 74.7 66.6
F.3 CHECKPOINTS
Forward models are taken at the checkpoint with the lowest validation loss for forward prediction
(Section E.1.2). For the seven discriminative verifiers, we scored all 129 saved checkpoints on the
10,000held-out generated pairs of Section F.4. For every model, between 38.9% and 75.0% of the
checkpoints after step5000lie within the DeLong 95% confidence interval of the best checkpoint,
and for BARTSmiles (disc.) the best and the final checkpoints differ by only 0.002 AUROC points.
29

Preprint
In-domain validation provides little separation among these checkpoints. We report a common bud-
get of20,000steps, the latest step at which all seven runs saved a checkpoint. At this step every
model has seen10.24million pairs, whereas the final checkpoints of the runs differ by a factor of
1.9 in compute. For BARTSmiles (disc.), step20,000also gives the highest pooled AUROC on RP,
ZR, and LP among its nine checkpoints, which could favor it.
Table F.3 compares the reported checkpoints with the final ones and with an oracle chosen on the
benchmark labels. BARTSmiles (disc.) stays at or below 67.8 AUROC on RP at every checkpoint,
and even its oracle average (71.2) falls short of forward-model likelihood (72.6 and 72.8). The
verifier trained on RR candidates remains the best of the seven under all three rules, the one trained
on FT candidates remains near chance, and the small mixture stays close to the full one.
F.4 THRESHOLDS
Every continuous score is thresholded at the value that maximizes BAcc on10,000held-out pairs of
recorded reactions and negative candidates from the generated test split. The set is balanced between
recorded reactions and candidates and across the five methods, and shares no reactant or product
string with the benchmark. BAcc gives equal weight to the two classes, but the selected threshold
can still depend on the mixture of generation methods. The threshold is then frozen (Table F.4).
A frozen threshold loses some BAcc relative to one tuned on each source of the benchmark. For
BARTSmiles LL the loss is 1.8 points on RP, 1.9 on ZR, 7.3 on LP, and 15.0 on GR.
F.5 STATISTICALTESTING
Unless otherwise specified, confidence intervals on a single metric are percentile intervals from
10,000bootstrap resamples of the reactions in the evaluated subset. The method-specific AUROCs
in Tables 3 and E.1 instead use DeLong intervals, as stated in their captions. AUROC differences
between two systems on the same reactions are tested with the paired DeLong test (DeLong et al.,
1988). Table F.2 lists twelve paired DeLong tests, withp-values adjusted by the Holm proce-
dure (Holm, 1979) over the twelve of them together. One comparison survives correction: on RP,
BARTSmiles LL exceeds BARTSmiles (disc.) by 11.1 AUROC points. The difference between De-
scriptor GBDT and BARTSmiles (disc.) on RP is not significant; this does not establish equivalence.
Neither controlled pair of Section 7 reaches significance on any source, including the 9.0-point dif-
ference on GR, where only33feasible candidates are available. The per-method training comparison
uses the separate paired-bootstrap analysis and six-comparison correction specified in Section E.2.4.
Table F.2: Paired DeLong tests, within source.∆is AUROC(A)−AUROC(B) in points.p adj is
Holm-corrected over all twelve tests.
Source A B∆95% CIp p adj
RP BARTSmiles (LL) BARTSmiles (disc.)+11.1 [+4.3,+17.9]0.00150.018
RP Descriptor GBDT BARTSmiles (disc.)+2.5 [−4.3,+9.4]0.470 1.00
RP BARTSmiles (LL) Descriptor GBDT+8.6 [+0.8,+16.3]0.031 0.343
RP RR only BARTSmiles (disc.)+6.7 [+0.3,+13.2]0.042 0.418
RP BARTSmiles (LL+neg.) no negatives−0.7 [−4.2,+2.7]0.671 1.00
ZR BARTSmiles (LL+neg.) no negatives+4.3 [−2.5,+11.2]0.213 1.00
LP BARTSmiles (LL+neg.) no negatives+2.6 [−3.2,+8.5]0.381 1.00
GR BARTSmiles (LL+neg.) no negatives+9.0 [−3.0,+21.1]0.142 1.00
RP+negatives, 3×no negatives, 3× −4.0 [−8.0,−0.0]0.050 0.445
ZR+negatives, 3×no negatives, 3×+1.1 [−3.3,+5.4]0.624 1.00
LP+negatives, 3×no negatives, 3×+4.5 [−2.0,+11.0]0.178 1.00
GR+negatives, 3×no negatives, 3×+9.0 [−3.4,+21.4]0.154 1.00
For the ranking of the eight retrosynthesis models in Table G.6, the interval on Spearman’sρcomes
from5000bootstrap resamples of the proposals within each retrosynthesis model, which propagates
the uncertainty in both the expert accept rates and the system’s. The reference ordering is recom-
puted within each resample, so the intervals account for sampling uncertainty in the expert ranking
as well.
30

Preprint
Table F.3: Sensitivity of the discriminative verifier family to the checkpoint, in AUROC by source.
Reported: the fixed budget of20,000steps used for this family.Final: the last checkpoint of each
run.Oracle: the checkpoint with the highest average AUROC on FREA, chosen with the benchmark
labels. It is an optimistic upper bound over the evaluated checkpoints, rather than an independently
selected performance estimate.
Model Rule Step RP ZR LP GR Avg.
RA only Reported20,00051.0 72.8 57.9 54.3 59.0
Final22,16850.8 73.6 57.8 54.1 59.1
Oracle11,00053.4 74.2 63.0 54.9 61.4
RR only Reported20,00074.5 87.3 68.2 68.6 74.6
Final22,16874.7 87.6 68.3 68.4 74.7
Oracle500072.5 88.1 73.9 73.6 77.0
NC only Reported20,00054.1 68.9 60.5 58.3 60.4
Final22,16853.8 69.3 60.7 58.4 60.6
Oracle900055.4 65.0 62.7 60.7 61.0
FT only Reported20,00052.4 43.6 49.5 43.5 47.2
Final22,16852.3 42.9 49.8 43.4 47.1
Oracle600053.2 49.9 53.5 48.5 51.3
ET only Reported20,00052.0 50.3 58.1 58.0 54.6
Final22,16852.0 49.1 58.1 57.7 54.2
Oracle400059.8 63.6 61.2 60.4 61.2
Mixture, 1.42M pairs Reported20,00068.0 75.7 66.8 61.2 67.9
Final22,16867.8 76.0 67.1 60.3 67.8
Oracle700065.6 90.3 64.5 67.1 71.9
Mixture, 7.10M pairs Reported20,00067.8 79.0 66.0 66.0 69.7
Final41,57166.9 74.0 64.6 61.0 66.6
Oracle10,00066.8 79.4 65.5 73.2 71.2
Table F.4: Frozen decision thresholds. Each maximizes balanced accuracy on the10,000held-
out generated pairs and is applied unchanged to FREA. Scores are log-likelihoods for the forward
models, raw logits for the verifier models, and probabilities for the shallow baseline.
System Threshold
Descriptor GBDT0.5101
Chemformer (LL)−0.0787
BARTSmiles (LL)−0.0829
BARTSmiles (disc.)−0.0913
BARTSmiles (LL), extra epoch−0.0942
BARTSmiles (LL+neg.)−0.4863
BARTSmiles (LL), extra epoch, 3× −0.1354
BARTSmiles (LL+neg.), 3× −0.5464
Mixture, 1.42M pairs−0.0684
RA only3.3424
RR only2.1345
NC only5.4880
FT only3.8126
ET only3.7918
G ADDITIONALRESULTS
Full results by source.Table G.1 gives AUROC with bootstrap confidence intervals and BAcc
for every system, including the rule-based baseline and both controlled pairs, and Table G.2 gives
the TPR and TNR behind each BAcc. The intervals on ZR and LP are wide because these sources
contain only 14 and 32 examples of their minority label. For comparison with evaluation on con-
structed labels, BARTSmiles (disc.) reaches 98.8 AUROC on held-out generated pairs but 69.7
mean AUROC on FREA.
Generated reactions by method, at each operating point.Table G.3 gives the share of each
method’s infeasible candidates that every system rejects, and the share of the33feasible GR can-
didates it accepts, complementing the threshold-free comparison of Table 3. Systems calibrated on
generated pairs accept few feasible GR candidates. On the calibration data, generated candidates are
assigned negative labels by construction.
31

Preprint
LLM perturbations by producing model.LP was constructed with GPT-5.4 and Claude Opus
4.6, and we evaluate newer models of the same two families. Table G.4 splits LP by the model that
produced each perturbation. Neither evaluated LLM has higher BAcc on the perturbations of its own
family in this sample.
The verifier family by method.Table G.5 gives the AUROC of the discriminative verifiers of
Section E.2.2 and the controlled pairs on the candidates of each method. Unlike Table 3, each
column here uses only the feasible candidates from that same method, rather than the shared set of
33 references. The two tables therefore answer different comparison questions. A verifier is often
not the best on its own method. For example, the verifier trained on RR candidates scores higher on
RA candidates than the one trained on them.
Table G.1: AUROC with 95% bootstrap confidence intervals (10,000resamples) and BAcc by
source for all systems, including the two controlled pairs of Section 7.
RP ZR LP GR
System AUROC BAcc AUROC BAcc AUROC BAcc AUROC BAcc
Claude Opus 5 – 69.9 – 64.3 – 76.1 – 61.8
GPT-6 Astra – 66.8 – 63.7 – 69.6 – 62.7
Chemformer (top-10) – 70.6 – 67.2 – 63.3 – 50.1
Chemformer (LL) 76.7 [70.6, 82.2] 71.6 82.4 [69.9, 93.0] 70.2 64.5 [50.4, 77.6] 63.8 67.0 [58.8, 74.6] 49.8
BARTSmiles (top-10) – 73.1 – 74.4 – 59.0 – 57.1
BARTSmiles (LL) 78.9 [73.1, 84.2] 71.5 79.5 [64.8, 92.1] 72.5 66.1 [52.8, 78.6] 60.4 66.9 [57.5, 75.8] 53.4
AiZynthFinder filter 57.0 [49.6, 64.3] 56.6 74.0 [55.7, 89.5] 69.9 62.3 [49.6, 74.3] 57.1 43.1 [33.9, 52.8] 42.6
BARTSmiles (LL+neg.) 77.0 [71.1, 82.4] 67.1 80.8 [67.9, 92.0] 63.7 69.4 [56.8, 80.9] 66.1 73.5 [64.2, 82.4] 54.9
BARTSmiles (disc.) 67.8 [61.0, 74.4] 62.5 79.0 [63.1, 92.1] 60.1 66.0 [53.2, 78.4] 54.8 66.0 [55.1, 76.3] 56.6
Descriptor GBDT 70.3 [63.8, 76.4] 64.0 72.2 [59.4, 83.6] 56.3 75.4 [64.1, 85.3] 70.2 64.7 [53.9, 75.4] 62.4
Rule Check – 60.0 – 61.5 – 58.0 – 61.3
BARTSmiles (LL), extra epoch 77.8 [71.9, 83.3] 71.5 76.5 [59.9, 90.7] 70.2 66.8 [53.6, 79.3] 58.9 64.5 [55.3, 73.2] 49.1
BARTSmiles (LL), extra epoch, 3×78.2 [72.5, 83.5] 71.4 78.5 [63.1, 91.6] 74.4 65.3 [52.1, 77.8] 62.6 64.5 [55.3, 73.1] 50.7
BARTSmiles (LL+neg.), 3×74.2 [68.2, 80.0] 65.5 79.6 [65.6, 91.4] 64.3 69.8 [57.4, 80.9] 65.8 73.5 [64.3, 82.2] 56.6
Table G.2: TPR and TNR by source at each system’s operating point. TPR is the share of feasible
reactions accepted, TNR the share of infeasible reactions rejected.
RP (197/85) ZR (79/14) LP (32/55) GR (33/256)
System TPR TNR TPR TNR TPR TNR TPR TNR
Claude Opus 5 82.2 57.6 100.0 28.6 61.3 90.9 33.3 90.2
GPT-6 Astra 88.8 44.7 98.7 28.6 71.9 67.3 51.5 73.8
Chemformer (top-10) 77.7 63.5 98.7 35.7 37.5 89.1 18.2 82.0
Chemformer (LL) 64.5 78.8 97.5 42.9 31.2 96.4 12.1 87.5
BARTSmiles (top-10) 79.2 67.1 98.7 50.0 34.4 83.6 33.3 80.9
BARTSmiles (LL) 62.9 80.0 94.9 50.0 28.1 92.7 18.2 88.7
AiZynthFinder filter 57.9 55.3 68.4 71.4 46.9 67.3 12.1 73.0
BARTSmiles (LL+neg.) 73.1 61.2 98.7 28.6 59.4 72.7 12.1 97.7
BARTSmiles (disc.) 75.6 49.4 98.7 21.4 75.0 34.5 18.2 94.9
Descriptor GBDT 68.0 60.0 91.1 21.4 75.0 65.5 42.4 82.4
Rule Check 88.3 31.8 87.3 35.7 68.8 47.3 90.9 31.6
BARTSmiles (LL), extra epoch 62.9 80.0 97.5 42.9 25.0 92.7 9.1 89.1
BARTSmiles (LL), extra epoch, 3×67.5 75.3 98.7 50.0 34.4 90.9 15.2 86.3
BARTSmiles (LL+neg.), 3×72.1 58.8 100.0 28.6 62.5 69.1 15.2 98.0
G.1 RANKINGRETROSYNTHESISMODELS
Beyond screening individual reactions, verifiers can be used to compare retrosynthesis models. We
therefore examine whether their acceptance rates yield the same model ordering as expert labels. For
each of the eight models represented in the 282-reaction RP subset, we calculate verifier and expert
acceptance rates, then compare the resulting rankings using Spearman’s correlation (Table G.6).
Rank correlations cover the LLM decisions and thresholded continuous scores; the top-10 rows
report acceptance rate and precision only.
The LLM-based rankings agree most closely with the expert ordering among the evaluated
rankings.Experts accept 48.3–92.6% of each model’s sampled proposals. Spearman’sρis 0.93
for Claude (95% CI[0.31,0.96]) and 0.76 for GPT ([0.26,0.93]). These intervals incorporate un-
32

Preprint
Table G.3: Behavior on GR at each system’s operating point. The first five columns give the share
of each method’s infeasible candidates that a system rejects (counts in parentheses), the last the share
of the33feasible GR candidates it accepts. Both depend on where the threshold falls, and Table 3
gives the threshold-free comparison for the systems that return a score.
Reactants changed Products changed Feasible
System RA(50) RR(53) NC(54) FT(44) ET(55) (33)
Large language models
Claude Opus 5 84.0 98.1 83.3 90.9 94.5 33.3
GPT-6 Astra 54.0 96.2 40.7 84.1 94.5 51.5
Forward-model proxies
Chemformer (top-10) 70.0 98.1 44.4 100.0 100.0 18.2
Chemformer (LL) 82.0 100.0 57.4 100.0 100.0 12.1
BARTSmiles (top-10) 66.0 98.1 42.6 100.0 100.0 33.3
BARTSmiles (LL) 84.0 100.0 61.1 100.0 100.0 18.2
Deployed filter
AiZynthFinder filter 74.0 64.2 46.3 95.5 89.1 12.1
Trained on our generated negative candidates
BARTSmiles (LL+neg.) 96.0 94.3 100.0 97.7 100.0 12.1
BARTSmiles (disc.) 94.0 90.6 100.0 93.2 96.4 18.2
Descriptor GBDT 76.0 56.6 100.0 84.1 94.5 42.4
Table G.4: Results on LP split by the LLM that produced the perturbation (feasible/infeasible
counts in parentheses). The evaluated LLMs are newer models of the same two families. Neither
shows an advantage on perturbations produced by its own family. One Claude Opus 5 response on
a GPT-5.4 perturbation could not be parsed and is excluded.
Produced by GPT-5.4 (15/30) Produced by Claude Opus 4.6 (17/25)
System BAcc TPR TNR BAcc TPR TNR
Claude Opus 5 76.9 57.1 96.7 74.4 64.7 84.0
GPT-6 Astra 63.3 46.7 80.0 73.1 94.1 52.0
Chemformer (top-10) 65.0 46.7 83.3 62.7 29.4 96.0
Chemformer (LL) 66.7 40.0 93.3 61.8 23.5 100.0
BARTSmiles (top-10) 53.3 33.3 73.3 65.6 35.3 96.0
BARTSmiles (LL) 61.7 33.3 90.0 59.8 23.5 96.0
AiZynthFinder filter 55.0 46.7 63.3 59.5 47.1 72.0
BARTSmiles (LL+neg.) 66.7 60.0 73.3 65.4 58.8 72.0
BARTSmiles (disc.) 58.3 80.0 36.7 51.3 70.6 32.0
Descriptor GBDT 68.3 80.0 56.7 73.3 70.6 76.0
certainty in the expert ordering (Section F.5). The thresholded continuous-score systems have cor-
relations between−0.19and+0.17, with intervals spanning zero. They include BARTSmiles LL
(ρ= +0.01), whose RP BAcc of 71.5 is close to Claude’s 69.9. Thus, strong reaction-level RP
scores do not necessarily imply agreement with expert model rankings at the thresholds used here.
This analysis covers eight models and their sampled proposals at the evaluated operating points. The
wide intervals limit conclusions about the relative quality of verifiers as judges; these results do not
establish a general ranking for that use.
Filtering tradeoff.The same analysis quantifies the tradeoff when these decisions are used to filter
proposals. BARTSmiles LL retains 50.0% of RP proposals, of which 87.9% are feasible. Claude
retains 70.2%, of which 81.8% are feasible. Precision must therefore be considered together with
the fraction retained when evaluating a verifier for planning.
H DATACARD
Contents.The release has three parts. Thebenchmarkis the751expert-labeled reactions of
Section 4. Each record holds the canonical reactant and product SMILES, the binary feasibility
label, the source and the model or method that produced the reaction, a failure reason for infeasible
reactions where one was recorded (Section B.4), and free-text notes where the annotators left them.
Thegenerated corpuscontains negative candidates paired with their parent reactions, each carrying
33

Preprint
Table G.5: AUROC on GR by negative candidate generation method for the discriminative verifier
family of Section E.2.2 and the two controlled pairs of Section E.2.3. Each cell compares one
method’s infeasible candidates with the feasible candidates of the same method (4–13 of them), so
single cells are imprecise. Italic cells are a single-method model evaluated on its own method.
Trained on RA RR NC FT ET
RA only65.555.7 81.5 37.1 71.4
RR only 72.572.230.6 73.8 80.9
NC only 52.5 51.981.061.7 42.7
FT only 61.0 49.5 33.345.872.7
ET only 43.0 74.1 40.7 64.955.0
Mixture, 1.42M pairs 52.0 93.4 87.5 54.4 83.6
Mixture, 7.10M pairs 45.2 84.0 90.3 65.0 80.9
BARTSmiles (LL), extra epoch 66.5 57.1 25.5 84.3 82.3
BARTSmiles (LL+neg.) 51.7 75.0 92.1 83.0 77.3
BARTSmiles (LL), extra epoch, 3×68.0 56.6 29.6 83.7 80.9
BARTSmiles (LL+neg.), 3×54.2 78.8 94.4 82.0 77.7
Table G.6: Ranking the eight retrosynthesis models by the share of their RP proposals a system
accepts.Acceptis that share over all282proposals, against the69.9% the experts accept, and
Precisionthe share of accepted proposals that are feasible.ρis the Spearman correlation between
the system’s ranking of the eight models and the experts’ ranking; brackets give 95% intervals from
5000bootstrap resamples of the proposals within each model. Dashes denote unreported top-10
rank correlations.
System Accept (%) Precision (%)ρvs. experts
Expert labels 69.9 100.0—
Claude Opus 5 70.2 81.8+0.93[+0.31,+0.96]
GPT-6 Astra 78.7 78.8+0.76[+0.26,+0.93]
Chemformer (top-10) 65.2 83.2 —
Chemformer (LL) 51.4 87.6−0.04[−0.68,+0.69]
BARTSmiles (top-10) 65.2 84.8 —
BARTSmiles (LL) 50.0 87.9+0.01[−0.67,+0.67]
BARTSmiles (LL+neg.) 62.8 81.4−0.19[−0.67,+0.52]
BARTSmiles (disc.) 68.1 77.6−0.12[−0.47,+0.66]
Descriptor GBDT 59.6 79.8−0.07[−0.54,+0.69]
AiZynthFinder filter 53.9 75.0+0.17[−0.61,+0.64]
the method that produced it, split into training and test portions that share no reaction (Sections C.5
and D.8). Theprotocolis the annotation guideline given to the chemists, the decision procedure of
Section B.3, and the failure-reason taxonomy.
Collection and labeling.Reactions derive from ORDerly (Wigh et al., 2024), a curated subset of
the Open Reaction Database (Kearnes et al., 2021), which draws on patents and published literature.
No new experiments were run and no human subjects are involved. Two chemists among the authors
labeled reactions without seeing their sources, following the calibration, independent annotation and
adjudication procedure in Section B.
Intended use.The benchmark supports evaluation of reaction feasibility verifiers under Section 3.
The generated corpus supports training and comparisons of negative generation methods, as studied
in Section 7. Annotation quality is documented in Section B.8; coverage and application scope are
described in Section I.
Distribution and maintenance.The benchmark is available athttps://huggingface.
co/datasets/FREA-benchmark/FREA-benchmark, and the generated corpus athttps:
//huggingface.co/datasets/FREA-benchmark/FREA-corpus. The benchmark and
the generated corpus are released under CC BY 4.0. A changelog will record label corrections, and
we expect the benchmark to grow as annotation continues.
34

Preprint
I LIMITATIONS
Evaluation scope.FREA evaluates whether individual proposals admit reasonable conditions un-
der the stated completeness and reactivity criterion, without specifying those conditions or testing
the reactions experimentally. A feasible label therefore does not establish a practical procedure, an
acceptable yield, or the quality of a complete synthesis route, where compatibility between steps
and purification also matter.
Expert judgment and annotation boundaries.Even with a written criterion, chemists may dif-
fer on whether conditions are reasonable, a target is isolable, or an omitted component serves a
permitted auxiliary role in a particular reaction. Our labels rely on two chemists, whose indepen-
dent agreement was 77.9% with Cohen’sκ= 0.55before adjudication. Joint review produces a
shared reference, but does not eliminate possible annotation errors or establish agreement with other
experts; the final binary labels also do not express the uncertainty of borderline judgments.
Coverage and source composition.All four sources derive from ORDerly’s patent and literature
records, and screening removes parsing failures and selected structural defects before annotation,
so the benchmark does not represent the full range of chemistry or unfiltered planner outputs. The
source proportions are chosen for evaluation, rather than estimated from deployment, and the four-
source mean need not reflect performance in a particular planning workflow. GR also uses the same
generation methods as our negative training corpus, so gains on this source do not by themselves
demonstrate transfer to model proposals or experimental records.
Sample size and comparison design.Several comparisons depend on small minority classes:
ZR has only 14 infeasible reactions, and the per-method GR analyses share 33 feasible reference
reactions. Those references come from all five generation methods, so each per-method AUROC
measures discrimination against a mixed reference set and can reflect differences between generation
methods as well as feasibility. The reported confidence intervals condition on the fitted models and
final labels; they do not account for annotation errors or variation across training runs.
Generated labels and exploratory training.Generated candidates can remain feasible, and treat-
ing them as negatives during training can penalize valid alternatives; differences in candidate purity
also prevent us from attributing performance differences solely to the generation method. Our con-
trolled training comparisons use one backbone, one corpus and one seed per setting, and most ob-
served gains are not statistically significant after correction for multiple comparisons. The resulting
hypotheses about label reliability and transfer therefore require tests across seeds, architectures and
corpora.
Decision rules and model comparisons.Thresholds calibrated on generated pairs may transfer
poorly to other sources, so a low acceptance rate at these thresholds does not establish that a model
cannot achieve a different precision–recall tradeoff. The LLM results likewise describe two models
under one shared prompt, and may change with the prompt or inference settings. The retrosynthesis
ranking analysis covers eight models on their sampled proposals at the evaluated operating points,
rather than establishing a general ordering of planners or verifiers.
35
