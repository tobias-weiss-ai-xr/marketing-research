---
title: Automated Regulatory Compliance Question Answering in Financial Services with Domain-Adapted Retrieval-Augmented
  Generation
url: https://arxiv.org/abs/2609.30009
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Tobias Deußer
- Abhishek Pillai
- Aurelio F. Bariviera
- Dhananjay Bhardwaj
- Lorenz Sparrenberg
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.30009
pages: 15
chars: 57821
fetched_at: '2026-11-08T13:24:51+00:00'
kb_version: 1
---

# Automated Regulatory Compliance Question Answering in Financial Services with Domain-Adapted Retrieval-Augmented Generation

AUTOMATEDREGULATORYCOMPLIANCEQUESTION
ANSWERING INFINANCIALSERVICES WITHDOMAIN-ADAPTED
RETRIEVAL-AUGMENTEDGENERATION
Tobias Deußer*1,2, Abhishek Pillai 1, Aurelio F. Bariviera3, Dhananjay Bhardwaj 3,
Lorenz Sparrenberg 1,2, David Berghaus 2,4, Christian Bauckhage 1,2,4, and Rafet Sifa 1,2,4
1University of Bonn, Bonn, Germany
2Lamarr-Institute for Machine Learning and Artificial Intelligence, Bonn, Germany
3Universitat Rovira i Virgili, Reus, Spain
4Fraunhofer IAIS, Sankt Augustin, Germany
ABSTRACT
Financial institutions operate under dense, frequently amended rulebooks, and answering a compli-
ance question correctly requires not only fluency but verifiable grounding in the authoritative text.
Large language models are attractive for this task, yet the models that firms can realistically deploy
on-premise are compact ones, and compact models hallucinate obligations. We study whether a care-
fully domain-adapted retrieval-augmented generation pipeline closes that gap. Our retriever is built
in three stages on top of LegalBERT: entailment tuning that recasts question–passage matching as
premise–hypothesis reconstruction, contrastive tuning with in-batch negatives, and score-level fusion
with BM25. Our generator is a compact model (2B–12B parameters) served under 4-bit quantization,
either prompted or adapted with retrieval-aware fine-tuning (RAFT) through LoRA. On ObliQA,
a question-answering benchmark built from the Abu Dhabi Global Market rulebooks, the staged
retriever raises Recall@10 from 0.256 to 0.774 and outperforms BM25 (0.678) and E5-large-v2
(0.758), the strongest general-purpose dense encoder we tested. RAFT-LoRA then improves the
composite RePASs answer-quality score for every model we could adapt, with the largest gain on the
weakest one. However, the adapted models do not transfer to Australian case-law questions, and a
closed-book model that receives no passages at all scores within 0.011 RePASs of the full pipeline
while producing answers that cite nothing and misstate obligations. The retrieval gain is therefore
measured directly, the generation gain is a gain in RePASs rather than demonstrated grounding, and
grounding itself requires an evaluation protocol that RePASs does not provide.
Keywordsretrieval-augmented generation · regulatory compliance · legal NLP · hybrid retrieval · natural language
processing
1 Introduction
Regulated financial companies operate inside a body of rules that is large, cross-referential, and in constant flux [1]. A
single question is typically answered by locating a handful of facts scattered across chapters and reconciling them. These
financial companies currently do this through specialist staff and commercial research tools, which makes compliance
slow and, when a provision is missed, expensive [2–4].
Large language models (LLMs) are an obvious candidate for automating parts of this workflow [ 5–8]. Used out of
the box, however, they are a poor fit. Without access to the source text, an LLM has to rely on what it memorized
during training, and its recall of specific rulebook clauses is unreliable: it may paraphrase provisions that do not exist
or omit binding conditions, and it sounds equally confident in both cases [9]. In compliance work this is particularly
problematic, because such an answer cannot be traced to any provision and therefore cannot be checked.
∗tdeusser@uni-bonn.de, ORCID-ID: 0000-0003-4685-0847
arXiv:2609.30009v1  [cs.CL]  24 Sep 2026

Automated Regulatory Compliance Question Answering in Financial Services with Domain-Adapted RAG
Retrieval-augmented generation (RAG) [10] addresses this problem by retrieving relevant passages from an authoritative
corpus and supplying them as context, so that answers can be traced back to the source text. The quality of a RAG
system, however, depends heavily on its retriever. Provisions in different chapters of a rulebook often use nearly
identical wording while differing in scope, applicability, or exemptions. Lexical overlap is therefore a weak relevance
signal, and general-purpose dense encoders trained on web data are not designed to tell which of two similar clauses
applies to a given case [11].
A second constraint is a more practical one. Regulatory documents and the questions asked about them are often
confidential, so many institutions cannot send queries to a hosted frontier model and have to run models on their own
hardware [12]. In practice, this limits the choice to quantized models with up to roughly 12B parameters (depending
on the budget of the firm of course), which have the least legal knowledge and the weakest grounding behavior.
Improvements therefore have to come from the pipeline around the model rather than from model scale.
In this paper, we investigate how far such a pipeline can be improved. We build a RAG system for regulatory question
answering in which both halves, the retrieval and the generation, are domain-adapted, and we evaluate it on ObliQA
[13], a benchmark derived from the rulebooks of the Abu Dhabi Global Market (ADGM) and on Open Australian
LegalQA [14] as an out-of-domain control. Our contributions are:
• A three-stage retrieverthat starts from LegalBERT [15] and applies entailment tuning, contrastive tuning,
and linear score fusion with BM25. Each stage helps, and the composition lifts Recall@10 on ObliQA from
0.256 to 0.774, past BM25 (0.678) and past E5-large-v2 (0.758) despite using a far smaller encoder.
• A leakage-free re-splitof ObliQA. The published splits share source documents across train, validation, and
test; we rebuild them at document level and quantify what this costs in dataset size.
• A controlled comparison of prompting against retrieval-aware fine-tuningfor five compact generators.
Prompting effects are model-dependent and often negative, whereas RAFT-LoRA improves the composite
RePASs score for all three models we could adapt stably, most for the weakest one.
• Two negative results.Adapters trained on ADGM rulebook data do not transfer to Australian case law, and a
closed-book model without access to any passage scores within 0.011 RePASs of the full retrieval pipeline,
even though its answers are not grounded. We attribute the latter to a weakness of the metric and discuss what
this means for evaluating regulatory QA systems.
2 Related Work
2.1 Regulatory and Legal Question Answering
Regulatory NLP applies language technology to statutes, rulebooks, and compliance guidance, where texts are long,
heavily structured, and full of normative operators (obligations, permissions, prohibitions) whose scope is set by
conditions and exceptions [16]. Answering questions over them is closer to multi-passage aggregation than to span
extraction, since the governing conditions for one obligation are routinely stated elsewhere.
Progress in this area has been driven by datasets. CUAD [17] annotates contract clauses for review tasks; LexGLUE
[18] assembles legal understanding benchmarks; FinQA [19] targets numerical reasoning over financial filings. Closest
to our setting is ObliQA [ 13], which pairs questions with the ADGM provisions that answer them and introduces
RePASs, an obligation-aware answer metric; that work also defines the retrieve-then-generate task formulation we
adopt. [20] treat regulatory compliance as document-to-document retrieval over European legislation, and [21] study
synthetic data for the same domain. [ 22] generate question–answer pairs from German statutes and adapt LLMs
with parameter-efficient fine-tuning, reporting gains over unadapted baselines. That strategy is close in spirit to the
fine-tuning half of our pipeline, though it is applied to a different jurisdiction and without a retrieval-aware objective.
Earlier legal QA systems relied on rules and keyword matching [23–25], later on neural judgment and retrieval models
[26–28]. A broader and more detailed survey of LLM use in finance is given in [29].
2.2 Sparse, Dense, and Hybrid Retrieval
BM25 [30] remains a strong baseline wherever terminology is fixed, which describes regulatory text well, but it cannot
bridge paraphrase. Dense retrieval [31] embeds queries and passages into a shared space and handles paraphrase, and
general-purpose encoders such as E5 [ 32] and BGE [ 33] transfer well across many domains. Specifically domain-
pretrained encoders such as LegalBERT [15] know legal vocabulary but, as we confirm in Section 4.2, are not good
retrievers out of the box: masked-language pretraining optimizes token prediction, not the geometry of a similarity
space.
2

Automated Regulatory Compliance Question Answering in Financial Services with Domain-Adapted RAG
Two lines of work address this limitation. Contrastive training with in-batch negatives and a multiple-negatives ranking
loss [34–36] can reshape the embedding space directly. Entailment tuning [ 37] instead reformulates retrieval as an
inference task: a passage is relevant if it entails a claim derived from the question, which is a better match for legal text
where two passages can be topically identical yet only one legally supports the answer. Combining sparse and dense
scores recovers the strengths of both [38, 39]. Our retriever composes all three ideas in sequence rather than choosing
among them.
2.3 Retrieval-Augmented Generation
RAG [10, 40] conditions generation on retrieved evidence, reducing hallucination and making answers attributable
[41, 42]. Extensions target its failure modes: Self-RAG [ 43] adds self-critique, Robust-RAG [ 44] defends against
corrupted contexts, and RQ-RAG [45] refines ambiguous queries. RAFT [ 46] takes a different route and trains the
generator itself to read a retrieved context: each training instance mixes an oracle passage with distractors, and for a
fraction of instances withholds the oracle entirely, so the model learns to use evidence when present and to abstain from
inventing it when absent. We adopt RAFT because it specifically targets hallucinations caused by irrelevant retrieved
passages, which a high-recall retriever over regulatory text will inevitably return.
2.4 Parameter-Efficient Fine-Tuning
Full fine-tuning of a 7B model requires considerably more GPU memory than many compliance teams likely have
available. Adapter modules [47] and LoRA [48], which learns a low-rank update to frozen attention projections, reduce
the trainable parameter count by orders of magnitude, and QLoRA [49] adds 4-bit quantization of the frozen base so
that a 7B model can be adapted on a single commodity GPU. Refinements continue in this direction [50, 51]. We use
QLoRA throughout, which allows us to run all RAFT experiments on a single GPU and matches the on-premise setting
described in the Introduction section.
2.5 Positioning of this work
Each component of our pipeline is established: domain-pretrained legal encoders [15], entailment tuning [37], contrastive
tuning with in-batch negatives [34], sparse–dense fusion [39], and retrieval-aware fine-tuning [46]. We claim none of
them as new.
What is new is their composition into a single pipeline for financial-regulatory QA under an on-premise compute budget,
together with a controlled evaluation of that pipeline: a staged retriever ablation on a leakage-free re-split, a like-for-like
comparison of prompting against RAFT-LoRA across five compact generators, a transfer test of the resulting adapters to
a different legal genre, and a closed-book control that isolates how much of the measured answer quality is attributable
to retrieval at all. LLeQA [52] fixes a retrieve-then-read setup and varies the reader. CBR-RAG [53] varies the retrieval
representation for a fixed generator. CLERC [ 54] reports retrieval and generation separately but with off-the-shelf
retrievers. LegalBench-RAG [55] isolates retrieval rigorously while stopping short of generation. We instead vary both
halves over a single shared retrieval run, and add a closed-book control, so that the contribution of each stage, and the
point at which the metric stops tracking grounding, are separately identifiable.
3 Methodology
3.1 Task and Pipeline
Let P be a corpus of regulatory passages and q a natural-language compliance question. The system must return an
answer a that is entailed by P and that covers the obligations P imposes on the situation in q. We factor this into a
retriever R:q7→P k ⊂ Pand a generator L: (q, Pk)7→a , trained and evaluated separately so that the contribution of
each is identifiable. Figure 1 shows the arrangement.
3.2 Leakage-Free Data Construction
A precondition for every result below is that no passage seen at evaluation time was used in training. ObliQA does not
satisfy this. It ships with predefined splits, but the sets of source documents behind them intersect: |Dtrain ∩D eval|>0
for every pair. Because ObliQA questions are generated from passages, a model that has seen one question from
a document has effectively seen the passage that answers a different question from the same document. This is
passage-level train–test leakage, and it inflates retrieval scores in particular, since the gold passage is then an item the
3

Automated Regulatory Compliance Question Answering in Financial Services with Domain-Adapted RAG
Regulatory questionq
BM25 Dense encoder LegalBERT+ET+CT
retriever
corpus
shyb =αˆsdense + (1−α) ˆsbm25,α= 0.8
top-k(k=10)→score & gap filtering→P k
Base LLM
zero-/few-shot/CoT
RAFT-LoRA LLM
4-bit,r=16
generator
RePASs: entailment−contradiction+obligations
Figure 1: The regulatory QA pipeline. Retrieval and generation are separate modules over a shared top-k context, so a
single retrieval run can be reused across every generation strategy.
Table 1: Datasets after leakage-free re-splitting. ObliQA splits are disjoint at document level; Open Australian LegalQA
is grouped by legal citation.
Dataset Split Documents Questions Corpus passages
ObliQA (ADGM) train 32 20,573
13,705validation 6 3,191
test 2 3,116
Open Australian train – 1,695 2,114LegalQA evaluation – 427
encoder was optimised on rather than an unseen target. We therefore re-split at document level, which excludes this
form of leakage by construction.
We therefore pool all questions and re-split at document level. The 40 ADGM documents are shuffled under a fixed
seed and assigned 80%, 15%, and 5% to train, validation, and test, respectively. Single-passage questions follow their
document. Multi-passage questions are admitted only if all of their passages land in the same split, and are otherwise
discarded. This removes 989 question–passage pairs, which we consider an acceptable trade-off for a leakage-free
evaluation. All numbers in this paper are computed on these re-split sets and are therefore not directly comparable to
published ObliQA results measured on the original splits. Table 1 shows the resulting splits. Corpus construction is
independent of the split: all 40 documents contribute their 13,705 passages, keyed bydocumentID-passageID.
We then audited the new splits for residual overlap with exact matching, fuzzy matching at 85%, and embedding cosine
similarity at 0.85. The first two find nothing. The third flags 139 train–eval question pairs, but inspection shows these
are distinct obligations phrased alike (liquidity-risk stress testing appears under several rules), which is a property of
regulatory drafting rather than leakage, so we retain them.
Open Australian LegalQA is converted to the same schema. After removing 2 duplicate questions from 2,124 records,
we group by legal citation (e.g.Nasr v NRMA Insurance [2006] NSWSC 1018) as the document identifier and split
80/20 by group, giving 1,695 training and 427 evaluation items over a 2,114-passage corpus. The same overlap audit
finds 13 fuzzy and 16 semantic near-duplicates, all of which are distinct questions about parallel instruments, such as
consecutive tariff concession orders or successive airworthiness directives, and are likewise kept.
3.3 Stage 1: Entailment Tuning
The base encoder is LegalBERT [15]. Its pretraining objective gives it legal vocabulary but no notion of query–passage
geometry, so we first retrain it on a task that is structurally closer to retrieval in this domain: deciding whether a passage
supportsa claim.
4

Automated Regulatory Compliance Question Answering in Financial Services with Domain-Adapted RAG
Each question q is rewritten into a declarative claim c=f(q) by a rule-based mapping over six question types
(when,why,who,where,does,how) with a generic fallback, so that awhoquestion becomes an assertion about the
responsible entity. The gold passage p+ becomes the premise and c the hypothesis, giving every training instance the
natural-language inference form
X="⟨p +⟩entails that⟨H masked⟩".(1)
Each hypothesis token is independently replaced by [MASK] with probability β= 0.8, far above conventional MLM
rates, and the model is trained to reconstruct only the masked positions:
Lmlm =−
X
i∈{MASK}
logP( ˆhi =h i |X).(2)
The high masking rate is intentional. When most of the hypothesis is masked, the model cannot simply copy tokens and
has to use information from the premise to reconstruct it, which is the kind of query–passage matching that retrieval
requires [37]. Training runs for 5 epochs (4 on Open Australian LegalQA) with AdamW at 2×10 −5, mixed precision,
and gradient clipping at 1.0. The tuned encoder is converted into a bi-encoder by mean-pooling token embeddings
under the SentenceTransformer interface.
3.4 Stage 2: Contrastive Tuning
Entailment tuning teaches the model whether a passage supports a claim, but it does not explicitly separate relevant from
irrelevant passages in the embedding space. Stage 2 optimises the embedding space directly with the multiple-negatives
ranking loss over in-batch negatives [34]. For a batch ofNquery–passage pairs,
L=−log exp(sim(qi, p+ i )/τ)PN
j=1 exp(sim(qi, pj)/τ)
,(3)
with sim the cosine similarity and τ a temperature. Queries and passages carry the prefixes query: and passage:; the
same prefixes are used at inference, since mismatched prefixes degrade retrieval performance. Batch size is 16, learning
rate 2×10 −5 with 100 warm-up steps, 2 epochs on ObliQA and 3 on Open Australian LegalQA, selected on validation
Recall@10 from schedules up to 5 epochs.
We deliberately do not mine hard negatives, although we implemented mining with E5-large-v2 and a BGE reranker.
We made this choice for two reasons. First, ObliQA is a multi-passage dataset: a passage that is semantically adjacent to
the gold one is frequently a second valid answer, so labeling it negative pushes a relevant passage away. Second, in our
development runs mined negatives reduced Recall@10 rather than improving it, consistent with the high terminological
overlap of regulatory drafting. Equation (3) already supplies N−1 negatives per query at no additional cost and led to
more stable training.
3.5 Stage 3: Hybrid Fusion and Context Assembly
Dense retrieval alone under-weights the exact identifiers (rule numbers, defined terms, entity names) that regulatory
questions often hinge on. We therefore score each query with both retrievers, normalize each score by its per-query
maximum,
ˆs• = s• max(s•) +ϵ, ϵ= 10 −9,(4)
and fuse them linearly, as seen in [39]:
shybrid =αˆsdense + (1−α) ˆsbm25.(5)
We setα= 0.8, keeping the tuned dense retriever dominant while letting BM25 break ties on exact terminology.
The top k= 10 passages are filtered before they reach the generator: passages scoring below 0.7 are dropped, and if
consecutive ranked scores fall by more than 0.2 the remaining tail is truncated. At least one passage is always retained.
This filtering is important because RePASs measures obligation coverage against the supplied context. Weakly relevant
passages increase the number of obligations an answer is expected to cover and thus penalize the generator for retrieval
errors.
3.6 Generation with Prompting
The first generator variant conditions a frozen instruction-tuned model on (q, Pk). All models receive an identical
system instruction, namely to act as a regulatory compliance assistant and synthesize every obligation in the supplied
5

Automated Regulatory Compliance Question Answering in Financial Services with Domain-Adapted RAG
Table 2: RAFT dataset construction and QLoRA adaptation settings, shared across all adapted models.
Component Setting
Base models Qwen2.5-7B, Teuken-7B v0.6, Gemma-2-2B
Quantisation 4-bit NF4, FP16 compute
LoRA rankr/α/ dropout 16 / 32 / 0.05
Target modules q_proj,v_proj
Optimiser paged AdamW (8-bit)
Learning rate / warm-up 2×10 −4 / 0.05
Epochs / batch size 3 / 1
Teacher model (CoT labels) GPT-4o-mini
Oracle-passage probabilityP0.7
Loss completion-only cross-entropy
passages into one coherent answer, under three strategies: zero-shot; few-shot with three worked examples, one of
which demonstrates the correct response to a question the context does not answer; and few-shot with chain-of-thought
[56–58], adding explicit reasoning instructions and constraints while still emitting only the final answer. Decoding is
greedy with a 512-token budget.
3.7 Generation with RAFT-LoRA
The second variant adapts the generator. Following RAFT [ 46], we build training instances from our own hybrid
retriever so that the distractors the model learns to resist are the ones it will actually see. For a fraction P= 0.7 of
questions the context contains the oracle passage plus distractors; for the remaining0.3it contains distractors only:
70% :Q i +D ∗ i +D 1 +D 2 +D 3 →A ∗ i
30% :Q i +D 1 +D 2 +D 3 +D 4 →A ∗ i (6)
Passage order is shuffled to suppress positional bias. Targets A∗ i are produced by GPT-4o-mini [ 59] as a teacher,
prompted to emit a REASONsection followed by an ANSWERsection, to use only the supplied documents, and to state
explicitly when the documents do not settle the question.
Two properties of this setup should be stated explicitly. The targetsA∗ i are teacher outputs from GPT-4o-mini rather than
human-written gold answers, so what the adapted models learns is the teacher’s answer behaviour, namely exhaustive
enumeration of the obligations present in the supplied passages and explicit abstention when they are absent, over
contexts that our own retriever produced. The RAFT training sets are also deliberately small, at 150 to 200 instances per
corpus or under 1% of the available training questions. We therefore present this as an efficient adaptation recipe, one
teacher pass and a few hundred optimisation steps on a single GPU, and not as evidence that the resulting behaviour is
independent of the teacher model or of how the training contexts were assembled.
Adaptation uses QLoRA [49]: the base model is frozen in 4-bit NF4, and rank-16 LoRA adapters are injected into the
query and value projections. Loss is computed only over the reason and answer spans, with instruction, question, and
context tokens masked, so the model is not trained to reproduce its input. Adapters are merged into the base weights for
inference and also stored separately for reuse. Table 2 lists the configuration.
3.8 Evaluation
Retrieval is measured by Recall@10, MRR@10, and nDCG@10 against the annotated gold passages.
Generation is measured with RePASs [13], which scores an answer against the retrieved context rather than against a
reference string. For answer sentences ai and passage sentences pj, entailment and contradiction take the best-matching
passage sentence per answer sentence,
Es = 1 N X
i
max
j
Pent(pj, ai), C s = 1 N X
i
max
j
Pcon(pj, ai),(7)
while obligation coverage first classifies which context sentences state obligations, using a LegalBERT obligation
classifier, and then checks how many are entailed by some answer sentence above a 0.7 threshold:
OCs = 1 M X
k
1

max
l
Pent(ok, al)>0.7

.(8)
6

Automated Regulatory Compliance Question Answering in Financial Services with Domain-Adapted RAG
Table 3: Staged retriever ablation. Each stage is initialized from the previous one; the hybrid adds BM25 atα= 0.8.
Retriever stage R@10 MRR@10 nDCG@10
ObliQA (ADGM rulebooks)
LegalBERT (baseline) 0.256 0.158 0.181
+ entailment tuning (ET) 0.495 0.322 0.363
+ contrastive tuning (CT) 0.732 0.518 0.569
+ BM25 fusion (hybrid) 0.774 0.594 0.638
Open Australian LegalQA
LegalBERT (baseline) 0.190 0.120 0.137
+ entailment tuning (ET) 0.726 0.595 0.626
+ contrastive tuning (CT) 0.911 0.824 0.845
+ BM25 fusion (hybrid) 0.923 0.846 0.865
LegalBERT + ET + CT + BM250.0
0.2
0.4
0.6
0.8
1.0
LegalBERT + ET + CT + BM25
score
ObliQA (ADGM rulebooks) Open Australian LegalQA
Recall@10 MRR@10 nDCG@10
Figure 2: Retrieval quality after each adaptation stage. The ordering of stages is identical on both corpora, but their
relative contributions are not: entailment tuning is decisive on Australian case law, contrastive tuning on the ADGM
rulebooks. Values are those of Table 3.
The composite is
RePASs= Es −C s +OC s + 1 3 ∈[0,1].(9)
Entailment and contradiction come from nli-deberta-v3-xsmall and obligation matching from
deberta-large-mnli. We report all three components separately because Equation (9) combines terms
that can move in opposite directions, so two systems with the same composite score may behave quite differently.
4 Experiments
4.1 Setup
All experiments run on single NVIDIA T4, L4, or A100 GPUs, with A100s reserved for generation and LoRA training.
Generators are loaded in 4-bit NF4 quantization via bitsandbytes, so every model in Table 5 fits on one commodity
accelerator. We evaluate five compact instruction-tuned models: Qwen2.5-7B [60], Teuken-7B v0.6 [61], Gemma-2-2B
[62], Gemma-3-12B [63], and DeepSeek-R1-Distill-Llama-8B [64].
All reported numbers are computed on the validation split of each corpus; the two-document ObliQA test split is held
out and untouched. Retrieval is evaluated exhaustively against the complete corpora, on 3,733 ObliQA question–passage
pairs drawn from 3,191 questions and on 427 Australian queries. Generation is evaluated on a fixed sample of 150
validation questions per configuration, held constant across models and strategies; the sample is a concession to the cost
of scoring long-form answers with two NLI models, and we return to it in Section 4.6.
4.2 Retrieval
Table 3 reports the staged ablation and Figure 2 plots it.
7

Automated Regulatory Compliance Question Answering in Financial Services with Domain-Adapted RAG
Table 4: ObliQA retrieval against standard baselines, full validation split (3,733 question–passage pairs, 13,705-passage
corpus).
Retriever Type R@10 MRR@10 nDCG@10
BM25 lexical 0.678 0.504 0.546
BGE-M3 dense 0.711 0.544 0.584
BGE-base-en-v1.5 dense 0.719 0.549 0.590
E5-base-v2 dense 0.721 0.557 0.597
E5-large-v2 dense 0.7580.5950.635
Hybrid ET+CT (ours) lexical+dense 0.774 0.594 0.638
“Off-the-shelf” LegalBERT performs poorly as a retriever: it ranks the gold passage among the top ten for only one in
four ObliQA queries and one in five Australian queries. Therefore, Domain-specific pretraining alone does not yield an
embedding space suitable for retrieval.
Entailment tuning roughly doubles every ObliQA metric (Recall@10 0.256→0.495 ) and has a far larger effect on
Australian case law (0.190→0.726 ). We attribute this difference to the question types. Australian questions name a
case or instrument and ask what it provides, so a single passage decisively entails the answer and the premise–hypothesis
objective aligns almost perfectly with the task. ADGM questions ask what a class of regulated entity must do, and
several provisions bear on that, so entailment alone leaves ambiguity.
Contrastive tuning is the larger step on ObliQA (0.495→0.732 ) and consolidates the Australian gain (0.726→0.911 ).
We attribute this to the model learning to distinguish between passages with similar regulatory vocabulary, which is
the main difficulty in ObliQA. BM25 fusion adds a final +0.042 on ObliQA and +0.012 on Australian data, with a
disproportionate effect on ranking quality: on ObliQA, Recall@10 rises 5.7% relative while MRR@10 rises 14.7%,
i.e. BM25 mostly promotes passages the dense model had already retrieved but ranked too low. That is the expected
signature of exact-term evidence, and it is worth more than the recall number suggests, because a generator reads the
top of the list most attentively.
Table 4 places the hybrid retriever against standard alternatives on ObliQA. BM25 alone reaches 0.678, within 0.04
Recall@10 of BGE-M3 and BGE-base despite learning nothing about the domain, which underlines the importance
of exact terminology in regulatory retrieval. Among dense baselines E5-large-v2 is strongest at 0.758. Our hybrid
reaches 0.774 Recall@10 and 0.638 nDCG@10, above every baseline, while its dense component is a BERT-base
encoder, roughly a third of E5-large’s parameters, adapted on in-domain data alone. We note that E5-large-v2 attains a
marginally higher MRR@10 (0.595 vs. 0.594); the two systems are equivalent on first-hit rank and differ in the depth of
the ranking.
4.3 Generation on ObliQA
Table 5 reports RePASs and its components for every model and strategy; Figure 3 summarizes the base-versus-adapted
comparison on both corpora. Our four key findings on ObliQA are:
1. Prompting does not generalize across models.Qwen2.5 improves from 0.668 zero-shot to 0.725 with few-shot
examples. Teuken degrades (0.673→0.662 ), Gemma-2 degrades further (0.594→0.565 ), and DeepSeek-R1 also
loses ground (0.735→0.702 ). Adding chain-of-thought on top of few-shot helps only Gemma-3 (0.666→0.694 ) and
DeepSeek-R1 (0.702→0.713 ), and is neutral-to-negative elsewhere. The component columns explain why: for Teuken
and Gemma-2 the examples cut obligation coverage sharply (Teuken 0.332→0.259 , Gemma-2 0.167→0.128 )
without a compensating drop in contradiction. Our three demonstrations are short, and models with weaker instruction-
following imitate their length and shape rather than their reasoning, truncating the exhaustive obligation enumeration
that RePASs rewards. This is consistent with evidence that demonstrations mostly convey format [65], and it means that
few-shot prompting is not a safe default in this domain: it must be validated per model.
2. RAFT-LoRA improves every model it can be applied to.Qwen2.5 gains +0.057 (0.668 → 0.725), Teuken +0.040
(0.673 → 0.713), and Gemma-2 +0.072 (0.594 → 0.666). The mechanism is visible in the components and is the same
in all three cases: obligation coverage rises substantially (Qwen 0.301→0.409 , Teuken 0.332→0.397 , Gemma-2
0.167→0.277 ) while contradiction falls (Qwen 0.189→0.157 , Teuken 0.256→0.134 , Gemma-2 0.317→0.212 ).
This matches the goal of the RAFT objective, namely covering what the context supports without adding unsupported
claims. Interestingly, Teuken’s entailment scoredropsfrom 0.944 to 0.877 at the same time. Teuken’s base answers
are short and closely paraphrase one passage, which scores well on entailment and poorly on coverage; the adapted
model writes longer, multi-provision answers in which some sentences are aggregations rather than restatements. For
8

Automated Regulatory Compliance Question Answering in Financial Services with Domain-Adapted RAG
Table 5: Answer generation on ObliQA, 150 evaluation questions, hybrid retriever context. Best RePASs per model in
bold.
Model StrategyE s ↑C s ↓OC s ↑RePASs↑
Qwen2.5-7B zero-shot 0.894 0.189 0.301 0.668
few-shot 0.971 0.167 0.3710.725
few-shot + CoT 0.957 0.154 0.359 0.721
RAFT-LoRA 0.926 0.157 0.4090.725
Teuken-7B zero-shot 0.944 0.256 0.332 0.673
v0.6 few-shot 0.928 0.200 0.259 0.662
few-shot + CoT 0.929 0.225 0.261 0.655
RAFT-LoRA 0.877 0.134 0.397 0.713
Gemma-2-2B zero-shot 0.935 0.317 0.167 0.594
few-shot 0.908 0.342 0.128 0.565
few-shot + CoT 0.900 0.326 0.113 0.562
RAFT-LoRA 0.934 0.212 0.2770.666
Gemma-3-12B zero-shot 0.961 0.312 0.328 0.659
few-shot 0.930 0.264 0.333 0.666
few-shot + CoT 0.911 0.182 0.353 0.694
RAFT-LoRA unstable adaptation – excluded
DeepSeek-R1 zero-shot 0.693 0.3650.877 0.735
Distill-8B few-shot 0.605 0.335 0.836 0.702
few-shot + CoT 0.629 0.365 0.876 0.713
RAFT-LoRAunstable adapter merge – excluded
compliance use the adapted behaviour is preferable, and the composite metric agrees, but the raw entailment column
would have suggested a regression.
Gemma-2-2B, the smallest model, benefits most from adaptation. In practice, this means that a few hundred training
steps of retrieval-aware adaptation can noticeably improve grounding in a 2B model.
3. Adaptation is not universally available.Two of the five models could not be adapted. Merging LoRA adapters into
DeepSeek-R1-Distill produced inconsistent generation at inference, and Gemma-3 showed near-zero loss movement
across epochs, indicating that the target sequence was recoverable from the input and no useful gradient signal was
present. We exclude both models from the comparison. For deployment, however, this shows that LoRA adaptation and
adapter merging do not work equally reliably across architectures.
4. The strongest single ObliQA number belongs to an unadapted model.DeepSeek-R1-Distill reaches 0.735
zero-shot, above every RAFT-LoRA result. Its profile is unlike the others: obligation coverage 0.877, far higher than
any other system, with entailment of only 0.693 and contradiction of 0.365. A reasoning-distilled model enumerates
context obligations exhaustively, which RePASs rewards twice: directly through OCs, and indirectly because long
enumerations dilute the per-sentence contradiction average. Its lower entailment, meanwhile, shows that much of what
it writes is not directly supported by any single passage. The composite score cannot tell whether these answers are
more useful for compliance than Qwen’s more conservative ones.
4.4 Cross-Domain Transfer
The Australian results in Table 6 serve two purposes: they test whether the retriever and prompting conclusions hold on
a different legal genre, and they test whether the ObliQA-trained adapters transfer. The adapters are reused unchanged;
no Australian RAFT data was generated.
The findings on prompting are even clearer here: zero-shot is the best prompted strategy for Qwen, Teuken, Gemma-2,
and Gemma-3, and few-shot and chain-of-thought degrade every one of them. Only DeepSeek-R1 prefers chain-of-
thought (0.613), again through obligation coverage.
The adapters, however, mostly do not transfer. Qwen drops from 0.642 to 0.581 and Gemma-2 from 0.477 to 0.453;
only Teuken improves, 0.559 to 0.586. The component scores show why: Gemma-2’s obligation coverage collapses to
0.013, because the adapted model reproduces the terse rulebook-style answer it was trained to produce, which covers
almost nothing in a long case-law passage. Qwen’s coverage falls from 0.377 to 0.238 for the same reason. Teuken
is the exception because its adaptation gain came predominantly from contradiction reduction (0.552→0.463 ), and
learning not to assert unsupported claims is a genre-independent behaviour, whereas learning the shape of an ADGM
obligation answer is not.
9

Automated Regulatory Compliance Question Answering in Financial Services with Domain-Adapted RAG
Qwen2.5-7B Teuken-7B Gemma-2-2B0.0
0.2
0.4
0.6
0.8
0.668 0.673
0.594
0.725 0.713
0.666
Qwen2.5-7B Teuken-7B Gemma-2-2B
0.642
0.559
0.477
0.581 0.586
0.453
RePASs
ObliQA: in-domain adaptation Open Australian LegalQA: transferred adapters
base (zero-shot) RAFT-LoRA
Figure 3: RAFT-LoRA against the zero-shot base model. Left: adapters trained and evaluated on ObliQA improve
every model. Right: the same ObliQA-trained adapters evaluated on Australian case law, where only Teuken retains a
gain. Values are those of Tables 5 and 6.
Table 6: Answer generation on Open Australian LegalQA, 150 evaluation questions. † marks adapters trained on
ObliQA and applied without retraining.
Model StrategyE s ↑C s ↓OC s ↑RePASs↑
Qwen2.5-7B zero-shot 0.964 0.414 0.3770.642
few-shot 0.964 0.402 0.350 0.637
few-shot + CoT 0.952 0.492 0.242 0.567
RAFT-LoRA† 0.957 0.451 0.238 0.581
Teuken-7B zero-shot 0.943 0.552 0.288 0.559
v0.6 few-shot 0.941 0.578 0.212 0.525
few-shot + CoT 0.945 0.587 0.209 0.522
RAFT-LoRA† 0.951 0.463 0.271 0.586
Gemma-2-2B zero-shot 0.922 0.639 0.1510.477
few-shot 0.892 0.676 0.116 0.444
few-shot + CoT 0.881 0.676 0.104 0.436
RAFT-LoRA† 0.940 0.592 0.013 0.453
Gemma-3-12B zero-shot 0.964 0.515 0.237 0.562
few-shot 0.959 0.545 0.200 0.538
few-shot + CoT 0.955 0.571 0.176 0.520
RAFT-LoRA unstable adaptation – excluded
DeepSeek-R1 zero-shot 0.571 0.610 0.850 0.604
Distill-8B few-shot 0.552 0.563 0.844 0.611
few-shot + CoT 0.552 0.5730.862 0.613
RAFT-LoRAunstable adapter merge – excluded
We attribute this to two structural differences between the corpora. ObliQA passages are short numbered provisions with
an explicit normative operator, and the mapping from retrieved passage to answer is close to deterministic. Australian
passages are extended excerpts of judicial reasoning in which the answer is distributed across the passage and rarely
stated as an obligation at all. Contradiction scores are also consistently higher on the Australian data: every model
contradicts its context far more often on Australian data (0.40–0.68) than on ObliQA (0.13–0.37), even though retrieval
is much better there (Recall@10 0.923 vs. 0.774). Long argumentative passages contain positions the court ultimately
rejects, and an NLI model scoring a summary against every sentence of such a passage will find contradictions that
are not errors. This is a limitation of sentence-level NLI metrics on case law, and it means Table 6 should be read
within-column rather than against Table 5.
The practical implication is that RAFT-LoRA adapters are corpus-specific artifacts. A firm deploying this pipeline
across several regulatory regimes should expect to build RAFT data per regime rather than to reuse one adapter.
10

Automated Regulatory Compliance Question Answering in Financial Services with Domain-Adapted RAG
Table 7: Closed-book control on ObliQA. Scores are computed against retrieved passages that the closed-book models
did not receive. Closed-book runs cover 132 (Qwen) and 89 (Teuken) validation questions.
Model SettingE s ↑C s ↓OC s ↑RePASs↑
Qwen2.5-7B closed-book 0.8830.0810.169 0.657
RAG (zero-shot) 0.894 0.189 0.301 0.668
Teuken-7B v0.6 closed-book 0.8360.0960.247 0.662
RAG (zero-shot) 0.944 0.256 0.332 0.673
4.5 Is Retrieval Doing the Work?
To check that the retrieval pipeline is responsible for the answer quality we measure, we ran Qwen2.5 and Teuken
closed-book: same prompt, same questions, no passages. RePASs is still computed against the retrieved passages the
model never saw. These runs cover 132 and 89 validation questions respectively rather than the full 150, so they are
indicative rather than precise; the effect below is far larger than that sample difference can explain.
Table 7 shows the results. Closed-book Qwen scores 0.657 compared to 0.668 with retrieval, and closed-book Teuken
0.662 compared to 0.673. A difference of about 0.01 clearly understates the gap between an answer grounded in the
ADGM rulebook and one generated from parametric knowledge alone. Inspection of the closed-book outputs confirms
that they are plausible-sounding regulatory prose that misstates obligations, omits binding conditions, and cites nothing.
The components show how the score is obtained. Closed-book contradiction is very low (0.081 and 0.096, against
0.189 and 0.256 with retrieval), because an answer that never commits to a specific provision has little to contradict;
and Es takes a maximum over passage sentences, so generic regulatory statements find some sentence that entails them.
Obligation coverage does fall as expected (Qwen 0.301→0.169 ), but it is one of three terms in Equation (9) and the
contradiction reduction offsets most of it.
We draw two conclusions from this. First, RePASs should not be used on its own to rank regulatory QA systems, and
results should be reported together with a closed-book baseline. Second, the main benefit of retrieval in our setting
is attributability, i.e., the ability to trace an answer back to a specific provision. Compliance applications require this
property, but RePASs does not capture it. Of its three components, only obligation coverage clearly separates the
retrieval and closed-book settings.
4.6 Limitations
Several constraints bound these results. Generation is scored on 150 questions per configuration, and the closed-
book control on fewer still; differences of a few thousandths of RePASs, such as Qwen’s tie between few-shot and
RAFT-LoRA, are within noise, and we make no claims at that resolution. The leakage-free re-split discards 989 multi-
passage question–passage pairs, tilting ObliQA toward single-passage questions and away from the multi-provision
reasoning that real compliance work demands. RePASs, as Section 4.5 shows, is not a sufficient measure of grounding;
an attribution-sensitive metric or an LLM-as-judge protocol [ 66] would be a better instrument, and human expert
evaluation better still. Finally, the two corpora studied here are both English and both drawn from public sources;
internal policy documents, tabular disclosures, and multilingual rulebooks remain untested.
5 Conclusion
We investigated how much of the gap between compact language models and reliable regulatory question answering can
be closed by adapting the pipeline instead of scaling the model. The retrieval half of that gap closes substantially and is
directly measured: a LegalBERT encoder that ranks the correct Abu Dhabi Global Market (ADGM) provision among
its top ten for one query in four does so for three queries in four after entailment tuning, contrastive tuning, and BM25
fusion, ahead of E5-large-v2 at a fraction of the parameters. The generation half improves on the metric available to us,
in that retrieval-aware LoRA adaptation raises composite RePASs for every compact generator we could adapt, most for
the smallest, by increasing obligation coverage and reducing contradictions on a few hundred teacher-labelled examples.
We describe this as improved in-domain answer behaviour rather than as improved grounding, because our closed-book
control shows that RePASs does not distinguish the two.
Three conclusions are supported by these experiments. First, domain-adapted retrieval is effective: staged adaptation
of a small in-domain encoder outperforms both a strong lexical baseline and larger general-purpose dense encoders
on regulatory text. Second, RAFT-LoRA improves compact generators in-domain, and in-domain only: adapters
trained on ADGM rulebook data lost most of their benefit on Australian case law, so deployments spanning several
11

Automated Regulatory Compliance Question Answering in Financial Services with Domain-Adapted RAG
regulatory regimes should plan for regime-specific RAFT data rather than adapter reuse. Third, current evaluation
metrics can substantially understate the value of retrieval. A closed-book model that received no passages, cited nothing,
and misstated obligations scored within 0.011 RePASs of the full pipeline, so RePASs cannot on its own validate a
compliance system. Therefore, Retrieval remains essential for transparency and traceability, but regulatory NLP needs
evaluation protocols that can measure these properties.
Acknowledgments
This research has been partially funded by the Federal Ministry of Education and Research of Germany and the state of
North-Rhine Westphalia as part of the Lamarr-Institute for Machine Learning and Artificial Intelligence.
For this paper, Anthropic Claude Opus 5 [67] was employed to assist in refining and improving the text throughout all
sections of this paper. The authors retain full responsibility for the accuracy, integrity, and originality of the work.
References
[1] Dawoon Jeong, James Holehouse, Jisung Yoon, Christopher P Kempes, Geoffrey B West, and Hyejin Youn. A
dataset showing a century of evolution in the complexity of the united states legal code.Scientific data, 2026.
[2] Rafet Sifa, Anna Ladi, Maren Pielka, Rajkumar Ramamurthy, Lars Hillebrand, Birgit Kirsch, David Biesner,
Robin Stenzel, Thiago Bell, Max Lübbering, et al. Towards automated auditing with machine learning. InProc.
DocEng, 2019.
[3] Johan V on Solms. Integrating regulatory technology (regtech) into the digital transformation of a bank treasury.
Journal of Banking Regulation, 2021.
[4] Rajkumar Ramamurthy, Maren Pielka, Robin Stenzel, Christian Bauckhage, Rafet Sifa, Tim Dilmaghani
Khameneh, Ulrich Warning, Bernd Kliem, and Rüdiger Loitz. ALiBERT: improved automated list inspec-
tion (ali) with bert. InProc. DocEng, 2021.
[5] Armin Berger, Lars Hillebrand, David Leonhard, Tobias Deußer, Thiago Bell Felix De Oliveira, Tim Dilmaghani,
Mohamed Khaled, Bernd Kliem, Rudiger Loitz, Christian Bauckhage, et al. Towards automated regulatory
compliance verification in financial auditing with large language models. InProc. BigData, 2023.
[6] Tobias Deußer, David Leonhard, Lars Hillebrand, Armin Berger, Mohamed Khaled, Sarah Heiden, Tim Dil-
maghani, Bernd Kliem, Rüdiger Loitz, Christian Bauckhage, et al. Uncovering inconsistencies and contradictions
in financial reports using large language models. InProc. BigData, 2023.
[7] Humza Naveed, Asad Ullah Khan, Shi Qiu, Muhammad Saqib, Saeed Anwar, Muhammad Usman, Naveed Akhtar,
Nick Barnes, and Ajmal Mian. A comprehensive overview of large language models.ACM Transactions on
Intelligent Systems and Technology, 2025.
[8] Tobias Deußer, Gregor Ramien, Nico Weber, Maximilian Meidinger, Max Hahnbück, Christian Bauckhage, and
Rafet Sifa. Leveraging synthetically generated data for real estate document classification. InProc. BigData,
2025.
[9] Rishi Bommasani, Drew A. Hudson, Ehsan Adeli, Russ Altman, Simran Arora, Sydney von Arx, Michael S.
Bernstein, Jeannette Bohg, Antoine Bosselut, Emma Brunskill, et al. On the opportunities and risks of foundation
models, 2022. URLhttps://arxiv.org/abs/2108.07258.
[10] Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich
Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, et al. Retrieval-augmented generation for knowledge-
intensive nlp tasks. InProc. NeurIPS, 2020.
[11] Nandan Thakur, Nils Reimers, Andreas Rücklé, Abhishek Srivastava, and Iryna Gurevych. BEIR: A heterogeneous
benchmark for zero-shot evaluation of information retrieval models. InProc. NeurIPS Datasets and Benchmarks,
2021.
[12] Tobias Deußer, Max Hahnbück, Tobias Uelwer, Cong Zhao, Christian Bauckhage, and Rafet Sifa. Resource-
efficient anonymization of textual data via knowledge distillation from large language models. InProc. COLING,
2025.
[13] Tuba Gokhan, Kexin Wang, Iryna Gurevych, and Ted Briscoe. Rirag: Regulatory information retrieval and answer
generation, 2024. URLhttps://arxiv.org/abs/2409.05677.
[14] Umar Butler. Open australian legal corpus, 2025. URL https://huggingface.co/datasets/isaacus/
open-australian-legal-corpus.
12

Automated Regulatory Compliance Question Answering in Financial Services with Domain-Adapted RAG
[15] Ilias Chalkidis, Manos Fergadiotis, Prodromos Malakasiotis, Nikolaos Aletras, and Ion Androutsopoulos. LEGAL-
BERT: The muppets straight out of law school. InFindings of the ACL: EMNLP 2020, 2020.
[16] Haoxi Zhong, Chaojun Xiao, Cunchao Tu, Tianyang Zhang, Zhiyuan Liu, and Maosong Sun. How does NLP
benefit legal system: A summary of legal artificial intelligence. InProc. ACL, 2020.
[17] Dan Hendrycks, Collin Burns, Anya Chen, and Spencer Ball. Cuad: An expert-annotated nlp dataset for legal
contract review. InProc. NeurIPS Datasets and Benchmarks, 2021.
[18] Ilias Chalkidis, Abhik Jana, Dirk Hartung, Michael Bommarito, Ion Androutsopoulos, Daniel Katz, and Nikolaos
Aletras. LexGLUE: A benchmark dataset for legal language understanding in English. InProc. ACL, 2022.
[19] Zhiyu Chen, Wenhu Chen, Charese Smiley, Sameena Shah, Iana Borova, Dylan Langdon, Reema Moussa, Matt
Beane, Ting-Hao Huang, Bryan Routledge, et al. FinQA: A dataset of numerical reasoning over financial data. In
Proc. EMNLP, 2021.
[20] Ilias Chalkidis, Manos Fergadiotis, Nikolaos Manginas, Eva Katakalou, and Prodromos Malakasiotis. Regulatory
compliance through Doc2Doc information retrieval: A case study in EU/UK legislation where text similarity has
limitations. InProc. EACL, 2021.
[21] Yelaman Abdullin, Diego Molla, Bahadorreza Ofoghi, John Yearwood, and Qingyang Li. Synthetic dialogue
dataset generation using LLM agents, December 2023. URL https://aclanthology.org/2023.gem-1.16/.
[22] Ali Hamza Bashir, Muhammad Rehan Khalid, Kostadin Cvejoski, Jana Birr, Jule Berghaus, Armin Berger,
Sandra Halscheidt, Christian Temath, Rafet Sifa, and David Berghaus. Domain-adaptation through synthetic data:
Fine-tuning large language models for german law, 2026. URLhttps://arxiv.org/abs/2601.14160.
[23] Marek J. Sergot, Fariba Sadri, Robert A. Kowalski, Frank Kriwaczek, Peter Hammond, and H Terese Cory. The
british nationality act as a logic program.Communications of the ACM, 1986.
[24] Howard Turtle. Text retrieval in the legal world.Artificial Intelligence and Law, 1995.
[25] Paulo Quaresma and Irene Rodrigues. A question-answering system for portuguese juridical documents. InProc.
ICAIL, 2005.
[26] Ilias Chalkidis, Ion Androutsopoulos, and Nikolaos Aletras. Neural legal judgment prediction in English. InProc.
ACL, 2019.
[27] Haoxi Zhong, Chaojun Xiao, Cunchao Tu, Tianyang Zhang, Zhiyuan Liu, and Maosong Sun. Jec-qa: a legal-
domain question answering dataset. InProc. AAAI, 2020.
[28] Lucia Zheng, Neel Guha, Brandon R. Anderson, Peter Henderson, and Daniel E. Ho. When does pretraining help?
assessing self-supervised learning for law and the casehold dataset of 53,000+ legal holdings. InProc. ICAIL,
2021.
[29] Paul Moon Sub Choi, Seth H Huang, and Qishu Wang. Large language models in finance: An overview.Finance
and Large Language Models, 2025.
[30] Stephen E. Robertson, Steve Walker, Susan Jones, Micheline Hancock-Beaulieu, and Mike Gatford. Okapi at
TREC-3. InProc. TREC, 1994.
[31] Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, and
Wen-tau Yih. Dense passage retrieval for open-domain question answering. InProc. EMNLP, 2020.
[32] Liang Wang, Nan Yang, Xiaolong Huang, Linjun Yang, Rangan Majumder, and Furu Wei. Multilingual e5 text
embeddings: A technical report, 2024. URLhttps://arxiv.org/abs/2402.05672.
[33] Kun Luo, Zheng Liu, Shitao Xiao, Tong Zhou, Yubo Chen, Jun Zhao, and Kang Liu. Landmark embedding: A
chunking-free embedding method for retrieval augmented long-context large language models. InProc. ACL,
2024.
[34] Nils Reimers and Iryna Gurevych. Sentence-BERT: Sentence embeddings using Siamese BERT-networks. In
Proc. EMNLP-IJCNLP, 2019.
[35] Matthew Henderson, Rami Al-Rfou, Brian Strope, Yun hsuan Sung, Laszlo Lukacs, Ruiqi Guo, Sanjiv Kumar,
Balint Miklos, and Ray Kurzweil. Efficient natural language response suggestion for smart reply, 2017. URL
https://arxiv.org/abs/1705.00652.
[36] Ting Chen, Simon Kornblith, Mohammad Norouzi, and Geoffrey Hinton. A simple framework for contrastive
learning of visual representations. InProc. ICML, 2020.
[37] Lu Dai, Hao Liu, and Hui Xiong. Improve dense passage retrieval with entailment tuning. InProc. EMNLP, 2024.
13

Automated Regulatory Compliance Question Answering in Financial Services with Domain-Adapted RAG
[38] Man Luo, Shashank Jain, Anchit Gupta, Arash Einolghozati, Barlas Oguz, Debojeet Chatterjee, Xilun Chen,
Chitta Baral, and Peyman Heidari. A study on the efficiency and generalization of light hybrid retrievers. InProc.
ACL, 2023.
[39] Shuai Wang, Shengyao Zhuang, and Guido Zuccon. Bert-based dense retrievers require interpolation with bm25
for effective passage retrieval. InProc. ICTIR, 2021.
[40] Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yi Dai, Jiawei Sun, Meng Wang,
and Haofen Wang. Retrieval-augmented generation for large language models: A survey, 2024. URL https:
//arxiv.org/abs/2312.10997.
[41] Gautier Izacard and Edouard Grave. Leveraging passage retrieval with generative models for open domain
question answering. InProc EACL, 2021.
[42] Lars Hillebrand, Armin Berger, Daniel Uedelhoven, David Berghaus, Ulrich Warning, Tim Dilmaghani, Bernd
Kliem, Thomas Schmid, Rüdiger Loitz, and Rafet Sifa. Advancing risk and quality assurance: A rag chatbot for
improved regulatory compliance. InProc. BigData, 2024.
[43] Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, and Hannaneh Hajishirzi. Self-RAG: Learning to retrieve,
generate, and critique through self-reflection. InProc. ICLR, 2024.
[44] Chong Xiang, Tong Wu, Zexuan Zhong, David Wagner, Danqi Chen, and Prateek Mittal. Certifiably robust rag
against retrieval corruption, 2024. URLhttps://arxiv.org/abs/2405.15556.
[45] Chi-Min Chan, Chunpu Xu, Ruibin Yuan, Hongyin Luo, Wei Xue, Yike Guo, and Jie Fu. RQ-RAG: Learning to
refine queries for retrieval augmented generation. InProc. COLM, 2024.
[46] Tianjun Zhang, Shishir G Patil, Naman Jain, Sheng Shen, Matei Zaharia, Ion Stoica, and Joseph E. Gonzalez.
RAFT: Adapting language model to domain specific RAG. InProc. COLM, 2024.
[47] Neil Houlsby, Andrei Giurgiu, Stanislaw Jastrzebski, Bruna Morrone, Quentin De Laroussilhe, Andrea Gesmundo,
Mona Attariyan, and Sylvain Gelly. Parameter-efficient transfer learning for NLP. InProc. ICML, 2019.
[48] Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu
Chen. LoRA: Low-rank adaptation of large language models. InProc. ICLR, 2022.
[49] Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, and Luke Zettlemoyer. Qlora: Efficient finetuning of quantized
llms. InProc. NeurIPS, 2023.
[50] Haotong Qin, Xudong Ma, Xingyu Zheng, Xiaoyang Li, Yang Zhang, Shouda Liu, Jie Luo, Xianglong Liu, and
Michele Magno. Accurate LoRA-finetuning quantization of LLMs via information retention. InProc. ICML,
2024.
[51] Han Guo, Philip Greengard, Eric Xing, and Yoon Kim. LQ-loRA: Low-rank plus quantized matrix decomposition
for efficient language model finetuning. InProc. ICLR, 2024.
[52] Antoine Louis, Gijs Van Dijck, and Gerasimos Spanakis. Interpretable long-form legal question answering with
retrieval-augmented large language models. InProc. AAAI, 2024.
[53] Nirmalie Wiratunga, Ramitha Abeyratne, Lasal Jayawardena, Kyle Martin, Stewart Massie, Ikechukwu Nkisi-Orji,
Ruvan Weerasinghe, Anne Liret, and Bruno Fleisch. Cbr-rag: case-based reasoning for retrieval augmented
generation in llms for legal question answering. InProc. ICCBR, 2024.
[54] Abe Bohan Hou, Orion Weller, Guanghui Qin, Eugene Yang, Dawn Lawrie, Nils Holzenberger, Andrew Blair-
Stanek, and Benjamin Van Durme. CLERC: A dataset for U. S. legal case retrieval and retrieval-augmented
analysis generation. InFindings of the ACL: NAACL, April 2025.
[55] Nicholas Pipitone and Ghita Houir Alami. Legalbench-rag: A benchmark for retrieval-augmented generation in
the legal domain, 2024. URLhttps://arxiv.org/abs/2408.10343.
[56] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, brian ichter, Fei Xia, Ed Chi, Quoc V Le, and
Denny Zhou. Chain-of-thought prompting elicits reasoning in large language models. InProc. NeurIPS, 2022.
[57] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Nee-
lakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. InProc.
NeurIPS, 2020.
[58] Pengfei Liu, Weizhe Yuan, Jinlan Fu, Zhengbao Jiang, Hiroaki Hayashi, and Graham Neubig. Pre-train, prompt,
and predict: A systematic survey of prompting methods in natural language processing.ACM Comput. Surv.,
2023.
[59] OpenAI, Aaron Hurst, Adam Lerer, Adam P. Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow,
Akila Welihinda, Alan Hayes, et al. Gpt-4o system card, 2024. URLhttps://arxiv.org/abs/2410.21276.
14

Automated Regulatory Compliance Question Answering in Financial Services with Domain-Adapted RAG
[60] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei
Huang, et al. Qwen technical report, 2023. URLhttps://arxiv.org/abs/2309.16609.
[61] Mehdi Ali, Michael Fromm, Klaudia Thellmann, Jan Ebert, Alexander Arno Weber, Richard Rutmann, Charvi
Jain, Max Lübbering, Daniel Steinigen, Johannes Leveling, et al. Teuken-7b-base & teuken-7b-instruct: Towards
european llms. InProc. ECAI, 2025.
[62] Gemma Team, Morgane Riviere, Shreya Pathak, Pier Giuseppe Sessa, Cassidy Hardin, Surya Bhupatiraju, Léonard
Hussenot, Thomas Mesnard, Bobak Shahriari, Alexandre Ramé, et al. Gemma 2: Improving open language
models at a practical size, 2024. URLhttps://arxiv.org/abs/2408.00118.
[63] Gemma Team, Aishwarya Kamath, Johan Ferret, Shreya Pathak, Nino Vieillard, Ramona Merhej, Sarah Perrin,
Tatiana Matejovicova, Alexandre Ramé, Morgane Rivière, et al. Gemma 3 technical report, 2025. URL
https://arxiv.org/abs/2503.19786.
[64] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Peiyi Wang, Qihao Zhu, Runxin Xu, Ruoyu Zhang,
Shirong Ma, Xiao Bi, et al. Deepseek-r1 incentivizes reasoning in llms through reinforcement learning.Nature,
2025.
[65] Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh Hajishirzi, and Luke Zettlemoyer.
Rethinking the role of demonstrations: What makes in-context learning work? InProc. EMNLP, 2022.
[66] Dawei Li, Bohan Jiang, Liangjie Huang, Alimohammad Beigi, Chengshuai Zhao, Zhen Tan, Amrita Bhattacharjee,
Yuxuan Jiang, Canyu Chen, Tianhao Wu, et al. From generation to judgment: Opportunities and challenges of
LLM-as-a-judge. InProc. EMNLP, 2025.
[67] Anthropic. System card: Claude opus 5, 2026. URL https://www-cdn.anthropic.com/
ceaf5c7ff2783855203fde8208ec311252dced5b/Claude%20Opus%205%20System%20Card.pdf.
15
