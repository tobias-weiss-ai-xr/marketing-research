---
title: 'Commercial Intent in Human-AI Conversations: A Corpus Audit and Architecture for Website Sales
  Agents'
url: https://arxiv.org/abs/2610.06205
category: ai-marketing
subcategory: framework
date: 2026-10
venue: arXiv (Cornell University)
authors:
- Benjamin Tannenbaum
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.06205
pages: 8
chars: 30803
fetched_at: '2026-11-08T13:35:28+00:00'
kb_version: 1
---

# Commercial Intent in Human-AI Conversations: A Corpus Audit and Architecture for Website Sales Agents

Commercial Intent in Human–AI Conversations:
A Corpus Audit and Architecture for Website Sales Agents
Benjamin Tannenbaum
Javo
getjavo.com
Abstract
Conversational sales agents must distinguish questions
about products from purchase commitments, preserve
explicit requirements, and ground the next action in
current business information. We report an aggregate
census of 725,219 records in an accessible conversation
table provided by Aiso and develop a reference architec-
ture for this setting. All records have distinct non-null
conversation hashes. Existing metadata labels identify
41,800 commercial records (5.76%) and 2,387 transac-
tional records (0.33%); their union contains 44,187 records
(6.09%). Within the commercial category, 54.31% are la-
beled English, 41.59% have recorded depth of at least two,
and 13.51% have depth of at least four. Commercial-label
prevalence varies from 4.87% to 6.35% across three source
batches. These measurements motivate explicit separa-
tion of corpus inventory, commercial relevance, training
eligibility, and observed business outcomes. The pro-
posed architecture combines business-grounded knowl-
edge, provenance-bearing conversation state, and a con-
strained next-action policy. A quality specification ad-
dresses source rights, privacy, label validation, deduplica-
tion, and training-test separation. The study is a meta-
data audit and technical design, not a validation of label
accuracy, model training volume, or sales conversion. No
raw conversation text or personal identifiers are released.
1 Introduction
A website visitor can ask about a price, add a location
or budget, reject an option, and request a call without
stating a complete buying brief in one message. A useful
conversational sales agent must interpret those updates,
answer from current business facts, and identify an ap-
propriate next step. The relevant behavior is therefore
broader than fluent response generation. It includes un-
certainty handling, requirement retention, clarification,
and human handoff.
Conversation data can inform these behaviors, but the
relationship between data quantity and commercial ca-
pability needs careful accounting. A corpus record may
contain a commercial question without a purchase, a trans-
action request without execution, or an assistant answer
that is unsuitable for training. Three claims should remain
distinct: the size of a stored corpus, the number of com-
mercially relevant examples, and the number of examples
actually used to train a particular model version. None of
these counts alone establishes conversion improvement.
This technical white paper pairs original aggregate anal-
ysis with a reference architecture for website sales agents.
The empirical contribution is a census of the accessible
main conversation table, with exact denominators, source-
batch comparisons, and metadata-quality checks. The
design contribution specifies how conversation data, busi-
ness knowledge, state tracking, and action policy can be
separated in a commercial agent.
Javo is the motivating product. Its public description
includes answering website questions, qualifying requests,
and collecting lead context [3]. Its product owner reports
that Javo’s team trains its model using conversation data.
This paper does not inspect model weights, training jobs,
training manifests, or deployed architecture. The reference
architecture and quality pipeline are specifications, rather
than verified descriptions of the current implementation.
This boundary preserves the usefulness of the design with-
out converting a product statement into an experimental
result.
2 Related Work
Research on e-commerce pre-sales dialogue studies the
combination of large language models and conversational
recommender systems. Liu et al. [4] investigate comple-
mentary roles for recommendation and language gener-
ation. That work motivates separating a conversation
model from domain-specific evidence, but it does not es-
tablish that a general commercial intent label identifies a
successful sale.
SalesLLM [5] evaluates multi-turn sales behavior
through curated scenarios, a customer simulator, and
scores for sales progress and buying intent. Its revised ver-
sion reports human calibration and distinguishes typical
human salespeople from experts. It illustrates the value of
evaluating process and outcome separately. Our audit nei-
ther runs this benchmark nor imports its reported results
as evidence for Javo. Simulated buying intent, human
preference, and a completed purchase remain different
endpoints.
The contribution here is narrower: explicit accounting of
a selected conversation corpus and a reference architecture
tied to those measurement boundaries. It is not a claim
1
arXiv:2610.06205v1  [cs.IR]  5 Oct 2026

of a new best-performing sales model.
Earlier work by the author distinguishes recorded rec-
ommendation content from observable buyer responses
[1] and experimentally compares full within-conversation
context with isolated final prompts [2]. These studies
motivate outcome separation and context retention, re-
spectively. Their samples and results are not treated as
new observations in the present metadata census, and
overlap with their underlying records was not audited.
2.1 Conversation, retrieval, and adapta-
tion
Conversational recommendation treats preference elicita-
tion, explanations, and feedback as parts of an interaction
rather than a single ranking [6, 7]. Its evaluation requires
attention to both component quality and users’ experience
of the complete system [8]. This distinction is directly
relevant to a website agent: producing a plausible recom-
mendation and identifying an appropriate business action
are separate responsibilities.
Retrieval-augmented generation combines a parametric
language model with external retrieved evidence [9]. This
provides a methodological basis for separating replaceable
business facts from learned conversational behavior. Re-
Act studies interleaved reasoning and actions [10], while
Toolformer investigates learning when to invoke tools [11].
These works motivate explicit interfaces between language
generation and external operations; they do not estab-
lish that an unconstrained action policy is appropriate
for sales. Our design therefore places business permis-
sions and evidence checks outside unrestricted response
generation.
DialoGPT studies conversational response generation
from large-scale dialogue [12]. Instruction tuning with
human feedback [13] and chat-model adaptation [14] illus-
trate that training data, behavioral objectives, and evalu-
ation need separate reporting. LoRA offers an approach
to parameter-efficient adaptation [15]; direct preference
optimization provides a method for learning from response
preferences [16]. These are possible methods for an imple-
mentation, not methods verified as used by Javo in this
study.
2.2 Documentation and evaluation
Datasheets for Datasets [17] motivate documenting collec-
tion, composition, intended uses, and limitations. Model
Cards [18] address the corresponding reporting of model
use and performance. We adopt this separation: the
present corpus audit documents an accessible inventory,
whereas a model report would require a specific checkpoint
and evaluation. Deduplication research [19] motivates
checks beyond unique record identifiers. Long-context
evaluation [20] shows why simply including more history
is not sufficient evidence that a model uses relevant re-
quirements reliably. Holistic evaluation [21] motivates a
set of distinct metrics rather than one aggregate success
score. Together, these sources support our quality specifi-
cation without supplying missing empirical validation for
this corpus or product.
3 Data and Audit Scope
3.1 Accessible corpus
On 5 October 2026, read-only database queries enumer-
ated the accessible main conversation table provided by
Aiso. The audit covers 725,219 records from three stored
source batches, anonymized as A, B, and C in public
outputs. Batch sizes are 233,619, 234,553, and 257,047.
These are administrative source groups, not randomized
experimental conditions or independent replications. The
table is an accessible inventory scope; it is not a verified
census of every conversation held by the provider or a
released training subset.
The audited schema includes a conversation hash, stored
intent, language, source batch, recorded turn count, and
a safety flag. Only aggregate counts were exported. Raw
conversation text, account and participant identifiers,
client names, and internal collection names are excluded
from the artifacts. No textual examples from private
records appear in the paper.
3.2 Provenance and disclosure
The corpus is privately maintained. That description
does not imply exclusive ownership of all underlying text:
third-party source material retains its applicable rights
and terms. Source identities, collection histories, and
source-specific research and training permissions belong in
a restricted provenance register. Such a register was not
inspected in this audit. Public reporting here is limited
to aggregate metadata. No claim is made that every raw
record is cleared for model training or redistribution.
The existing metadata labels are inherited, not newly
annotated for this study. The audit did not inspect the
intent classifier, its version, training data, or annotation
agreement. Missing intent is treated as an unlabeled cate-
gory. Recorded depth is the stored turn-count value; its
exact role and message-count semantics were not estab-
lished. A threshold of two is therefore not described as
proof of two buyer turns.
3.3 Accounting checks
A separate global query counted distinct conversation
hashes. Both row count and distinct non-null hash count
equal 725,219. This establishes identifier uniqueness in
the audited table, not semantic uniqueness. Translations,
rephrased copies, and overlapping sessions can have dif-
ferent hashes. Source-level distinct-hash totals reconcile
with the global total.
Recorded depth and the safety field are populated in all
2

audited records. The safety flag is false for every record.
This uniformity does not establish universal safety or
privacy: it may reflect upstream filtering, field construc-
tion, or source selection, none of which was independently
verified. A separate stored summary table differed from
the underlying-table totals; the underlying table supplies
every number reported here.
4 Measures and Estimation
Let N be the number of audited records andIi the stored
intent label of recordi. The primary commercial indicator
is
Ci =⊮(I i =commercial).(1)
The transactional indicatorTi is defined analogously. A
broader relevance sensitivity isBi = max(Ci, Ti). Because
each record has one stored label, the two categories are
disjoint. Their shares are
ˆpC =
∑
i Ci
N ,ˆp B =
∑
i Bi
N .(2)
These indicators operationalize category membership, not
latent buying intent or a realized transaction.
Forcategory k, wereporttheproportionwithanEnglish
label and the proportions whose recorded depth is at
least two and four. The denominator for each conditional
share is the number of records labeledk. We also report
commercial-label prevalence separately by source batch.
All estimates are descriptive ratios of an enumerated
table. We do not report sampling confidence intervals for
this census. Such intervals would not address unknown
collection selection, semantic dependence, or label error.
We do not infer intersections from marginal counts, and do
not interpret batch differences causally. No transcript cod-
ing, model generation, user simulation, or sales-outcome
linkage was performed.
5 Results
5.1 Commercial-label composition
Table 1 reconciles all categories with the corpus denomi-
nator. The informational category is largest, followed by
other. Commercial records account for 41,800 of 725,219
records (5.76%). Transactional records account for 2,387
(0.33%). Including both yields 44,187 (6.09%), compared
with the narrow commercial definition. This sensitivity
changes the numerator by 2,387 and the share by approx-
imately 0.33 percentage points.
5.2 Language coverage and recorded
depth
The commercial category contains 22,702 English-labeled
records (54.31%). It contains 17,384 records with depth
at least two (41.59%) and 5,649 with depth at least four
Stored intent Records Share (%)
Informational 376,889 51.97
Other 204,774 28.24
Productive 55,489 7.65
Creative 42,106 5.81
Commercial 41,800 5.76
Transactional 2,387 0.33
Navigational 1,764 0.24
Unlabeled 10 0.0014
Total 725,219 100.00
Table 1: Intent composition of the audited table. Per-
centages are rounded independently. Stored labels are not
independently validated ground truth.
0 20 40 60
Unlabeled
Navigational
Transactional
Commercial
Creative
Productive
Other
Informational
Share of audited records (%)
Figure 1: Stored intent distribution,N = 725,219. Table 1
gives exact category counts.
(13.51%). These are marginal counts; they do not establish
the size of an English, deep-conversation intersection.
Table 2 compares selected categories. Commercial
records are more often labeled English than informational
records (54.31% versus 45.33%), but are less often at depth
at least two (41.59% versus 43.69%). Neither difference
identifies why a conversation is long, whether it contains
objections, or whether a recommendation succeeded.
5.3 Source-batch heterogeneity
Batch A contains 14,837 commercially labeled records
out of 233,619 (6.35%); batch B contains 14,457 out of
234,553 (6.16%); and batch C contains 12,506 out of
257,047 (4.87%). The range is approximately 1.48 percent-
age points. Figure 3 makes the differing baselines visible.
Source populations, collection design, or annotation dif-
ferences could contribute to this variation; the audit does
not separate those mechanisms. The pooled rate should
not be interpreted as the prevalence of commercial intent
among all website visitors or all users of conversational
AI.
3

Intent English Depth≥2Depth≥4
Commercial 54.31 41.59 13.51
Transactional 53.83 43.49 12.78
Informational 45.33 43.69 14.88
Other 45.97 40.67 15.90
Table 2: Conditional shares (%) within each stored intent.
Depth semantics are not role-validated. Denominators
appear in Table 1.
Commercial Transactional Informational
Other
0
20
40
60
Within-category share (%)
English label Recorded depth≥2
Figure 2: Language coverage and recorded depth by in-
tent. Each bar uses the full size of its own category as
denominator.
5.4 Exclusive depth bands and language
labels
The nested depth thresholds permit an exact partition of
the commercial category. Of its 41,800 records, 24,416
(58.41%) have recorded depth below two, 11,735 (28.07%)
have depth from two through three, and 5,649 (13.51%)
have depth of at least four (Figure 4). The middle band is
obtained by subtracting the depth-at-least-four count from
the depth-at-least-two count. These bands are mutually
exclusive and exhaustive. They describe stored depth, not
verified stages in a sales funnel.
The complementary language partition contains 22,702
English-labeled commercial records and 19,098 records
with other or missing language labels (Figure 5). The
second group should not be interpreted as 19,098 vali-
dated non-English conversations: the audit does not sep-
arate missing labels from specific languages. Similarly,
a language label does not establish language quality or
monolingual content. A training selection that requires
both English and a minimum depth would need a joint
query. The available marginals alone cannot measure that
selection.
5.5 Contribution to the pooled commer-
cial subset
A batch’s contribution to the commercial subset depends
on both its size and its commercial-label prevalence. Batch
A supplies 32.21% of the full inventory but 35.50% of com-
A B C
0
2
4
6
8
6.35 6.16
4.87
Anonymous source batch
Commercial label (%)
Figure 3: Source-batch commercial-label prevalence.
Batch counts are 233,619, 234,553, and 257,047 for A,
B, and C, respectively. These are source groups, not ran-
domized treatments.
0 20 40 60
At least 4
2 through 3
Below 2
13.51
28.07
58.41
Commercial records (%)
Figure 4: Exclusive recorded-depth bands among 41,800
commercial records. Counts are 5,649, 11,735, and 24,416,
respectively.
mercial records; batch B supplies 32.34% and 34.59%,
respectively; batch C supplies 35.44% and 29.92%. Fig-
ure 6 compares these two denominators. Batch C is the
largest inventory source while contributing the smallest
commercial count. Consequently, selecting only commer-
cially labeled examples changes the source mixture even
without deliberate source weighting.
For each batch, the ratio of commercial-subset share
to inventory share also equals its commercial prevalence
divided by the pooled prevalence. The ratios are approx-
imately 1.10, 1.07, and 0.84 for A, B, and C. These are
descriptive composition ratios, not estimates of source
quality. They motivate preserving source membership in a
training manifest and reporting performance by held-out
source rather than assuming pooled results transfer.
6 Reference Architecture
The audit motivates explicit separation of commercial
labels, useful training examples, and live business actions.
We propose a modular architecture with four components:
business knowledge, conversation state, response gener-
ation, and constrained next-action selection. Figure 7
summarizes the specification. No claim is made that the
diagram describes an inspected production implementa-
tion.
4

English Other or missing
0
20
40
60 54.31
45.69
Commercial records (%)
Figure 5: English-label coverage and its complement
among commercial records. The complementary group
includes any missing language labels.
A B C
0
10
20
30
40
Anonymous source batch
Share of respective total (%)
All records (N= 725,219)
Commercial (N= 41,800)
Figure 6: Source mixture before and after commercial-
label selection. Each series sums to 100% before rounding.
6.1 Versioned business knowledge
The knowledge layer contains offers, prices, eligibility,
availability, service areas, and approved explanations.
Each item should retain its source, validity period, and
update version. Retrieval is conditioned on the visitor’s
current question and accumulated explicit requirements.
Conflicting or stale evidence should trigger qualification
or handoff, rather than an unsupported answer. Business
facts should be replaceable independently of conversation-
model weights.
6.2 Provenance-bearing conversation
state
Let ut be the visitor message at stept, st−1 the previous
state, and∆ t the explicit information extracted fromut.
A state update is represented as
st = Update(st−1,∆ t).(3)
The state stores needs, constraints, unanswered questions,
and contact preferences. Each value retains its supporting
turn and whether it was explicitly stated. Corrections
supersede conflicting values; unknown fields remain un-
known. Inferred preferences should not silently become
confirmed facts. A short follow-up can rely on prior state
without reproducing it.
Visitor question and explicit requirements
Provenance-bearing conversation state
Retrieve versioned business evidence
Apply action policy and uncertainty checks
Answer / clarify / next
step / human handoff
Figure 7: Proposed agent architecture. This is a design
specification, not a verified implementation or trained-
model evaluation.
6.3 Constrained next actions
The agent chooses among answering, clarifying, proposing
a relevant next step, and handing off. Given business
evidenceK t and policyP, its allowed action set is
At = Allowed(st, Kt, P).(4)
The response model selects within that set, rather than
treating all fluent continuations as permissible. A call
request should match the visitor’s goal; contact collection
should have a defined purpose; unavailable offers and
unsupported promises should be excluded. Regulated
advice and requests outside the configured scope should
route to a human.
6.4 Model adaptation
Conversation-based adaptation can target clarification,
appropriate evidence use, constraint retention, and hand-
off. Suitable examples are not selected solely because
they have a commercial label. Context-response pairs
require rights clearance, privacy review, and validation
of the response behavior. Preference pairs should encode
a defensible reason one response is better than another.
A model trained on such examples should be compared
with its base model under identical business knowledge,
prompts, and tools.
7 Collection and Quality Specifica-
tion
7.1 From inventory to training eligibility
An auditable pipeline distinguishes five objects: in-
gested records, deduplicated records, commercially rel-
evant records, cleared and quality-accepted records, and
records used in a named training job. A large inventory
cannot substitute for the last count. Messages, exam-
ples, tokens, unique conversations, and repetitions across
training epochs should be reported separately.
5

For each accepted record, a restricted register should
retain source, collection date, permitted research and
training uses, retention conditions, and redistribution re-
strictions. Source-specific requirements take precedence
over a generic proprietary-corpus description. The present
audit did not verify this register, and does not certify
training eligibility.
7.2 Privacy and minimization
Training and evaluation inputs should include only infor-
mation necessary for the intended task. Remove creden-
tials, account identifiers, contact details, and unnecessary
personal or location attributes before example construc-
tion. Pattern-based redaction alone may miss contextual
identifiers, so selected examples require contextual review.
Transformation logs and raw data should remain restricted.
Public reporting should use aggregate statistics or con-
structed examples; private transcript excerpts should not
be included by default. Neither an anonymous batch la-
bel nor a false safety flag establishes that the underlying
transcript is anonymized.
7.3 Deduplication and split integrity
Identifier uniqueness is the first check, not the final one.
A training pipeline should additionally compare normal-
ized exact text and detect near duplicates. Translations,
repeated prompts, or successive snapshots of one con-
versation can produce overlap even when hashes differ.
Partitioning must prevent those families from crossing
training and evaluation splits. When permitted partic-
ipant keys are available, user-level separation provides
an additional control. Source-level holdouts test transfer
rather than memorization of one collection’s style.
7.4 Label and response audits
Validate inherited commercial and transactional labels
with stratified human review. Sampling should include
each source batch, language group, relevant depth range,
positive labels, and apparent negatives. Reviewers need
an operational rubric that separates product research,
recommendation seeking, action requests, and completed
outcomes. Report disagreement, adjudication, and a con-
fusion matrix before treating the labels as ground truth.
Response quality needs a separate rubric: factual
grounding, consistency with explicit requirements, useful
clarification, appropriate next action, and handoff correct-
ness. A commercially labeled dialogue may contain poor
assistant behavior. The uniform safety field observed here
makes an independent review particularly important; it is
not a validated quality certificate.
7.5 Training manifests
Each model version should preserve its base model, source
versions, accepted and excluded counts, deduplication
rules, example construction, training settings, split defini-
tions, and output model identifier. This record is the basis
for a training-volume statement. The audited inventory
contains 725,219 records, and the narrow commercial cat-
egory contains 41,800; these figures do not verify a claim
that millions of commercial conversations trained a Javo
model. A larger separately documented training corpus
may exist, but it was not established by this audit.
8 Evaluation Boundaries and Lim-
itations
The corpus is selected and heterogeneous. Unknown col-
lection mechanisms and label error limit generalization.
Hash uniqueness does not exclude semantic duplicates
or participant dependence. Recorded depth is not role-
validated. The audit uses existing marginal metadata, so it
cannot reconstruct buying journeys, objection resolution,
or outcomes.
Javo training is reported by the product owner and at-
tributed to Javo’s team. No training manifest, checkpoint,
deployed endpoint, retrieval trace, or controlled evalua-
tion was inspected. The architecture and quality pipeline
remain proposed specifications. The findings establish
metadata composition, not model superiority, training
causality, or conversion uplift.
An evaluation of a trained model should freeze the
model version and compare it with the base model on
leakage-controlled held-out cases. Blind human review
should calibrate automated ratings. Primary endpoints
can include factual accuracy, explicit-constraint satisfac-
tion, useful clarification, appropriate next-action selection,
and correct handoff. Live lead quality, booking, and rev-
enue require separately linked outcomes and a controlled
comparison with consistent attribution. A simulated deci-
sion to buy should not be reported as an actual sale.
9 Conclusion
The audited table contains 725,219 identifier-unique
records, including 41,800 with a commercial label and
2,387 with a transactional label. Commercial-label preva-
lence differs across source batches, and substantial lan-
guage and recorded-depth variation remains within the
commercial category. These results support explicit ac-
counting of inventory, relevance, eligibility, and training
membership. The reference architecture separates busi-
ness facts, conversation state, and constrained actions;
the quality specification makes source rights, privacy, la-
bel validation, and split integrity inspectable. The work
provides a corpus audit and technical design rather than
evidence of sales improvement.
6

Data availability and reproducibil-
ity
The analysis uses database-side aggregate queries and
deterministic arithmetic. The accompanying ancillary
package includes anonymous aggregate counts, the query
specification, and a standard-library analysis script. It
contains no raw text, conversation hashes, participant
identifiers, or internal source names. Reproducing derived
counts and shares from that snapshot is public; repeating
the live census requires authorized access to the restricted
source.
Author and product disclosure
Benjamin Tannenbaum is affiliated with Javo for this
technical white paper. Aiso provided access to the audited
conversation data. Javo’s team is responsible for model
training, as reported by the product owner. The product
context creates a commercial interest in the subject. This
paper reports no independently verified training count or
model-performance result.
7

References
[1] Benjamin Tannenbaum. 2026.Purchase Advice and
Observable Buyer Responses in Real AI Conversa-
tions. arXiv:2609.09878. https://arxiv.org/abs/
2609.09878.
[2] Benjamin Tannenbaum. 2026.Beyond the
Final Prompt: Measuring the Effect of
Within-Conversation Context on AI Answers.
arXiv:2608.02556. https://arxiv.org/abs/2608.
02556.
[3] Javo.AI sales and support agent for your website.
https://getjavo.com/. Accessed 5 October 2026.
[4] Yuanxing Liu, Wei-Nan Zhang, Yifan Chen, Yuchi
Zhang, Haopeng Bai, Fan Feng, Hengbin Cui, Yong-
bin Li, and Wanxiang Che. 2023.Conversational
Recommender System and Large Language Model Are
Made for Each Other in E-commerce Pre-sales Di-
alogue. arXiv:2310.14626. https://arxiv.org/abs/
2310.14626.
[5] Xuanbo Su et al. 2026.Sell More, Play Less:
Benchmarking LLM Realistic Selling Skill.
arXiv:2604.07054v3. Revised 26 August 2026.
https://arxiv.org/abs/2604.07054v3.
[6] Dietmar Jannach, Ahtsham Manzoor, Wanling Cai,
and Li Chen. 2020.A Survey on Conversational
Recommender Systems. arXiv:2004.00646.https://
arxiv.org/abs/2004.00646.
[7] Dietmar Jannach and Li Chen. 2022.Conver-
sational Recommendation: A Grand AI Chal-
lenge. arXiv:2203.09126. https://arxiv.org/abs/
2203.09126.
[8] Dietmar Jannach. 2022.Evaluating Conversa-
tional Recommender Systems: A Landscape of Re-
search. arXiv:2208.12061.https://arxiv.org/abs/
2208.12061.
[9] Patrick Lewis et al.. 2020.Retrieval-Augmented
Generation for Knowledge-Intensive NLP Tasks.
arXiv:2005.11401. https://arxiv.org/abs/2005.
11401.
[10] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du,
Izhak Shafran, Karthik Narasimhan, and Yuan Cao.
2022.ReAct: Synergizing Reasoning and Acting in
Language Models. arXiv:2210.03629.https://arxiv.
org/abs/2210.03629.
[11] Timo Schick et al.. 2023.Toolformer: Lan-
guage Models Can Teach Themselves to Use
Tools. arXiv:2302.04761. https://arxiv.org/abs/
2302.04761.
[12] Yizhe Zhang et al.. 2019.DialoGPT: Large-Scale
Generative Pre-training for Conversational Response
Generation. arXiv:1911.00536. https://arxiv.org/
abs/1911.00536.
[13] Long Ouyang et al.. 2022.Training language
models to follow instructions with human feed-
back. arXiv:2203.02155. https://arxiv.org/abs/
2203.02155.
[14] Hugo Touvron et al.. 2023.Llama 2: Open Founda-
tion and Fine-Tuned Chat Models. arXiv:2307.09288.
https://arxiv.org/abs/2307.09288.
[15] Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan
Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and
Weizhu Chen. 2021.LoRA: Low-Rank Adaptation
of Large Language Models. arXiv:2106.09685.https:
//arxiv.org/abs/2106.09685.
[16] Rafael Rafailov, Archit Sharma, Eric Mitchell,
Stefano Ermon, Christopher D. Manning, and
Chelsea Finn. 2023.Direct Preference Optimiza-
tion: Your Language Model is Secretly a Reward
Model. arXiv:2305.18290.https://arxiv.org/abs/
2305.18290.
[17] Timnit Gebru, Jamie Morgenstern, Briana Vec-
chione, Jennifer Wortman Vaughan, Hanna Wal-
lach, Hal Daum’e III, and Kate Crawford. 2018.
Datasheets for Datasets. arXiv:1803.09010. https:
//arxiv.org/abs/1803.09010.
[18] Margaret Mitchell, Simone Wu, Andrew Zaldivar,
Parker Barnes, Lucy Vasserman, Ben Hutchin-
son, Elena Spitzer, Inioluwa Deborah Raji, and
Timnit Gebru. 2018.Model Cards for Model
Reporting. arXiv:1810.03993. https://arxiv.org/
abs/1810.03993.
[19] Katherine Lee et al.. 2021.Deduplicating
Training Data Makes Language Models Better.
arXiv:2107.06499. https://arxiv.org/abs/2107.
06499.
[20] Nelson F. Liu et al.. 2023.Lost in the Mid-
dle: How Language Models Use Long Con-
texts. arXiv:2307.03172. https://arxiv.org/abs/
2307.03172.
[21] Percy Liang et al.. 2022.Holistic Evaluation of
Language Models. arXiv:2211.09110.https://arxiv.
org/abs/2211.09110.
8
