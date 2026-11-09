---
title: Making Large Language Models Better Knowledge Miners for Online Marketing with Progressive Prompting
  Augmentation
url: https://arxiv.org/abs/2312.05276
category: ai-marketing
subcategory: empirical
date: 2023-12
venue: ''
authors:
- Chunjing Gan
- Dan Yang
- Binbin Hu
- Ziqi Liu
- Yue Shen
source: arxiv
pdf_url: https://arxiv.org/pdf/2312.05276
pages: 10
chars: 66545
fetched_at: '2026-11-08T13:10:54+00:00'
kb_version: 1
---

# Making Large Language Models Better Knowledge Miners for Online Marketing with Progressive Prompting Augmentation

Making Large Language Models Better Knowledge Miners for
Online Marketing with Progressive Prompting Augmentation
Chunjing Gan∗
Ant Group
cuibing.gcj@antgroup.com
Dan Yang∗
Ant Group
luoyin.yd@antgroup.com
Binbin Hu∗
Ant Group
bin.hbb@antgroup.com
Ziqi Liu
Ant Group
ziqiliu@antgroup.com
Yue Shen
Ant Group
zhanying@antgroup.com
Zhiqiang Zhang
Ant Group
lingyao.zzq@antgroup.com
Jinjie Gu
Ant Group
jinjie.gujj@antgroup.com
Jun Zhou†
Ant Group
jun.zhoujun@antgroup.com
Guannan Zhang
Ant Group
zgn138592@antgroup.com
ABSTRACT
Nowadays, the rapid development of mobile economy has pro-
moted the flourishing of online marketing campaigns, whose suc-
cess greatly hinges on the efficient matching between user prefer-
ences and desired marketing campaigns where a well-established
Marketing-oriented Knowledge Graph (dubbed as MoKG) could
serve as the critical “bridge” for preference propagation. In this
paper, we seek to carefully prompt a Large Language Model (LLM)
with domain-level knowledge as a better marketing-oriented knowl-
edge miner for marketing-oriented knowledge graph construction,
which is however non-trivial, suffering from several inevitable
issues in real-world marketing scenarios, i.e., uncontrollable rela-
tion generation of LLMs, insufficient prompting ability of a single
prompt, the unaffordable deployment cost of LLMs. To this end, we
propose PAIR, a novel Progressive prompting Augmented mIning
fRamework for harvesting marketing-oriented knowledge graph
with LLMs. In particular, we reduce the pure relation generation
to an LLM based adaptive relation filtering process through the
knowledge-empowered prompting technique. Next, we steer LLMs
for entity expansion with progressive prompting augmentation,
followed by a reliable aggregation with comprehensive consider-
ation of both self-consistency and semantic relatedness. In terms
of online serving, we specialize in a small and white-box PAIR
(i.e.,LightPAIR), which is fine-tuned with a high-quality corpus pro-
vided by a strong teacher-LLM. Extensive experiments and practical
applications in audience targeting verify the effectiveness of the
proposed (Light)PAIR 1.
1Source code and datasets will be released upon acceptance.
* Equal contribution.
† Corresponding author.
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than ACM
must be honored. Abstracting with credit is permitted. To copy otherwise, or republish,
to post on servers or to redistribute to lists, requires prior specific permission and/or a
fee. Request permissions from permissions@acm.org.
Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
© 2018 Association for Computing Machinery.
ACM ISBN 978-1-4503-XXXX-X/18/06. . . $15.00
https://doi.org/XXXXXXX.XXXXXXX
CCS CONCEPTS
• Computing methodologies→ Artificial intelligence.
KEYWORDS
Knowledge Graph; Online Marketing Campaign; Large Language
Model
ACM Reference Format:
Chunjing Gan, Dan Yang, Binbin Hu, Ziqi Liu, Yue Shen, Zhiqiang Zhang,
Jinjie Gu, Jun Zhou, and Guannan Zhang. 2018. Making Large Language
Models Better Knowledge Miners for Online Marketing with Progressive
Prompting Augmentation. In Proceedings of Make sure to enter the correct
conference title from your rights confirmation email (Conference acronym ’XX).
ACM, New York, NY, USA, 10 pages. https://doi.org/XXXXXXX.XXXXXXX
1 INTRODUCTION
Nowadays, the rapid growth of mobile economy has established the
prosperity of online marketing campaigns [7, 9, 28, 55], which at-
tracts a variety of Internet companies or merchants to promote their
products / services. Taking Alipay as an example, as an integrated
service platform in China, numerous merchants conduct marketing
campaigns (e.g., offering coupons, vouchers, and bonuses) through
so-called mini-apps each day [64, 66], in which efficient informa-
tion delivery plays a crucially important role. Fundamentally, the
core is to perform intelligent matching between user preference
and desired campaigns[ 14, 29, 36, 52], where a well-established
Marketing-oriented Knowledge Graph (dubbed as MoKG) could
serve as the critical “bridge”, allowing flexible and effective prefer-
ence propagation. Although SupKG [56]2 has made considerable
efforts in connecting users and various services in Alipay, product-
related entities with hierarchical and spatiotemporal relations are
at its heart, while MoKG emphasizes more on the marketing-related
relations between users and merchants (A snapshot of MoKG is
illustrated in Fig. 1), as a kind of complementary knowledge to
enrich the original SupKG graph (More details in Sec. 4.3.3).
Intuitively, we could directly graft the construction pipeline of
SupKG, which is a mixture of multiple text mining techniques (e.g.,
NER [12, 30, 37, 51, 60] and RE [ 10, 19, 49, 63]), to supplement
2SupKG involves more than ten millions of entities, more than one hundred relations,
and more than one hundred million of triplets.
arXiv:2312.05276v2  [cs.AI]  2 Apr 2025

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY Chunjing Gan, Dan Yang, Binbin Hu, Ziqi Liu, Yue Shen, Zhiqiang Zhang, Jinjie Gu, Jun Zhou, and Guannan Zhang
营销图谱Schema
Brandrelatedproducts
商品-【拥有权益】-优惠券，品牌-门店，品牌-商品，地点--门店等非世界知识的，
scene_related_brand
提供该类型活动场所的品牌
festival_related_product
节日相关商品
festival_related_activity
节日相关活动
折扣券-奥尔良烤翅
超市券-步步高南城百货
中影-观影资格券
权益关联的商品
官方补贴-香型洗衣液
&RQVXPHUJRRGVYRXFKHU>SUL]HUHODWHGSURGXFW@VKDPSRR
权益适用的意图prize_applied_intent
租车抵扣券-自驾租车
SUL]HUHODWHGSURGXFW
SUL]HUHODWHGSURGXFW
Movievouvher
Consumergoodsvoucher
ShampooRelated product
Related
food
Biscuits
Discountcoupons
Issue
vouchers
Brandof
product
Relatedbrand
Oreo
IssuevouchersUncleFruit
Similarfood Cookies
Related
food
DigitalService
Relatedproduct
Xiaomiphone
Popcorn
Related
scene
Related
product
WandaCinema
Litchi
Dry Fruits
Related
food
Schwarzkopf
Issuevouchers
MovieService
TheThreeBodyCouponofmovie
Relatedscene
Issuevouchers
Movievoucher
Figure 1: An example of the marketing-oriented knowledge
graph.
marketing-related entities and relations. Unfortunately, its success
greatly hinges on manual labeling and evaluation, which is rather
expensive. On the other hand, Large Language Models (LLMs) (e.g.,
ChatGPT [33], GPT4 [34], Llama [44, 45], ChatGLM [16, 57]) have
shown remarkable and even superhuman capabilities on various
NLP tasks. Learning from a vast corpus of Internet text, LLMs have
encoded a huge amount of open-world knowledge [1, 11, 35], which
are naturally excellent helpers to harvest factual information for
knowledge graphs [11, 20, 65]. However, the effectiveness of LLM
based mining approaches cannot be always guaranteed in real-
world marketing scenarios, since pure LLMs may be unfamiliar
with the marketing-oriented entities and relations[ 15, 43]. Thus,
can we bridge both worlds, i.e., carefully prompting LLMs with prior
knowledge (e.g., SupKG or other knowledge) as a better marketing-
oriented knowledge miner ?
With this in mind, we decompose the whole mining process of
MoKG as the following three stages: Prior Knowledge→ Relation
Generation→ Entity Expansion. With the help of prompting en-
gineering, domain-level prior knowledge could be easily injected
into LLMs for relation generation and entity expansion, whereas
the performance is still far from optimal for real-world marketing-
oriented scenarios due to the following unresolved issues: (i) Pure
relation generation is uncontrollable. Despite the impressive perfor-
mance of LLMs in various generative tasks, it is undeniable that the
capabilities of LLMs can get out of control very quickly in relation
exploration. In other words, LLMs may inevitably generate several
useless / fallacious [24, 59, 61] relations for given entities (e.g., Take
the entity “The Three Body” in Fig. 1 as an example, the LLM would
tell several undesired relations towards marketing, e.g., “Related
scientists” and “Related organizations”.) so that the following entity
expansion would be greatly confused. (ii) A single prompt is insuf-
ficient. Intuitively, the performance of entity expansion depends
highly on the quality of the prompt used to steer the LLMs. Un-
fortunately, due to the variety of prior knowledge, coupled with
the sensitivity of prompting under slight modifications [2, 8, 41],
a single painstakingly crafted prompt may not always produce
the desired results. (iii) A white-box and smaller model is preferred.
Generally, real-world marketing scenarios involve millions of seed
entities, which brings far beyond affordable cost to directly serve
(or call open API of) a performant LLM (e.g., GPT 3.5). On the other
hand, the growing concerns for privacy demand to circumvent a
black-box LLM in realistic applications.
To address the above problems, we propose a novel Progressive
prompting Augmented mIning fRamework for harvesting marketing-
oriented knowledge with LLMs (dubbed as PAIR). To perform rela-
tion generation in a controllable manner, we restrict this procedure
in a finite relation space, which is thus reduced to an LLM based re-
lation filtering process (i.e., adaptively determining which relations
deserve expansion for each entity). In terms of entity expansion,
we steer LLMs with well-designed progressive prompting augmen-
tation (i.e., from coarse-grained to fine-grained prompts), followed
by a reliable aggregation with comprehensive consideration of both
self-consistency and semantic relatedness. To remedy the short-
coming of LLMs in mastering marketing-oriented knowledge, we
collect relevant evidence from SupKG and available knowledge
bases to empower LLMs in both relation filtering and entity expan-
sion stages. And then, we specialize in a small and white-box model
(dubbed as LightPAIR) with a high-quality corpus provided by a
strong teacher-LLM involving 175 billion parameters. At last, exten-
sive experiments and practical applications in audience targeting
verify and justify the effectiveness of the proposed (Light)PAIR.
2 RELATED WORK
2.1 Traditional knowledge graph construction
Currently, traditional construction process of well-known knowl-
edge bases / KGs usually requires heavy human labor for label-
ing and evaluation or multiple text mining-based procedures. In
the line of manual labor-intensive research [5, 21], WordNet [18]
is a database that links words with semantic relations, Concept-
Net [42] is a large commonsense knowledge graph consists of
a large set of knowledge triples while ATOMIC [ 39] is a crowd-
sourced social commonsense KG of inferential knowledge which
is organized as typed if-then relations. On the other hand, text
mining-based approaches usually consist of sub-procedures such as
named entity recognition[12, 26, 60], relation extraction[10, 19, 63],
semantic parsing[25, 27, 62] that require to collect different text cor-
pus to train independent model for each procedure. Among them,
Quasimodo [38], TransOMCS [ 58], DISCOS [ 17], ASCENT [ 32],
SupKG [56] construct commonsense or practice-oriented knowl-
edge graphs by making use of linguistic patterns and huge manual
processing.
Open issues. These research works usually hinge on collecting
different text samples to train multiple independent models for each
procedure (e.g., named entity recognition and relation extraction)
and require huge manual resources for labeling. However, the lim-
ited manual resources and text corpora usually restrict the scale of
constructed knowledge graph.
2.2 Language model-driven knowledge graph
construction
For works in this direction, they tend to 1) distill knowledge graphs
from LMs, 2) incorporate the power of LMs to enhance knowl-
edge graph construction. In COMET [6], implicit knowledge from
deep pre-trained language models is transferred to generate explicit

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
knowledge in commonsense knowledge graphs. MAMA [47] pro-
poses to use learned knowledge stored in pre-trained LMs in an un-
supervised manner to construct a knowledge graph and compares
the quality of it with human-labeled knowledge graph. BertNet [20]
generates multiple prompts for KG generation and weights them
by the likelihood of prompts given by an LLM. In LMCRAWL [11],
relation paraphrases and object paraphrases are utilized for KG
generation. On the other hands, [46] compares the advanced LLM
e.g., ChatGPT with the specialized pre-trained models e.g., REBEL
for entity and relation extraction.
Open issues. In these research works, they tend to generate knowl-
edge graphs or knowledge bases towards world knowledge / contain
knowledge stored in the parameters of LMs, while in industrial sce-
narios, for example, commercial marketing scenarios, usually pure
LMs may be unfamiliar with the marketing-oriented entities and
relations hence those approaches cannot meet the requirements.
3 THE PROPOSED PAIR FRAMEWORK
In this section, we dive into the elaboration of the proposed PAIR,
a novel Prompting Augmented mIning fRamework for harvesting
marketing-oriented knowledge with LLMs.
3.1 Formulation
Essentially, a mining procedure of a knowledge graph could be
formulated as follows: with the given source entity𝑠, the likelihood
of target entity𝑡 and its corresponding relation𝑟 is calculated as
P(𝑟,𝑡|𝑠) =
∫
𝜅
P(𝜅|𝑠)P(𝑟,𝑡|𝑠,𝜅)
=
∫
𝜅
P(𝜅|𝑠)P(𝑟|𝑠,𝜅)P(𝑡|𝑠,𝜅,𝑟)
(1)
•P( 𝜅|𝑠): Prior Knowledge. Intuitively, the knowledge miner com-
monly struggles to perceive the real meaning of the given entities
in the marketing-oriented applications, e.g., sneaker-related enti-
ties might be preferred with the given entity “Air”. Hence, the
usage of prior knowledge 𝜅 occupies a critical position in the
guidance of knowledge mining.
•P( 𝑟|𝑠,𝜅): Relation Filtering. Based on the enormous knowledge𝜅,
the pure process of relation generation is ideal but generally un-
controllable, especially in marketing-oriented applications where
a bundle of relations might be undesired, e.g., relation “Related
scientists” w.r.t. entity “The Three Body”. Therefore, we resort to
the powerful capability of LLMs for filtering desired relations𝑟
from the pre-defined relation setR.
•P( 𝑡|𝑠,𝜅,𝑟): Entity Expansion. With careful prompting engineer-
ing, we communicate with LLMs to complete the entity expansion
task. However, due to the variety of prior knowledge𝜅, coupled
with the sensitivity of prompting under slight modifications, a
single painstakingly crafted prompt may not always produce
the desired results. Instead, we prompt the LLMs for entity ex-
pansion with multiple prompting augmentations via a reliable
aggregation strategy.
In the following, we will delve into the instantiation of each part
with the help of the recent emerging LLMs.
Figure 2: Overall architecture of PAIR.
3.2 The Usage of Prior Knowledge
In practice, LLMs commonly struggle to perceive the real meanings
of the given entities due to the lack of domain-level knowledge,
which severely hinders the capabilities of LLMs in both relation
filtering and entity expansion stages. Hence, it is of crucial impor-
tance to introduce prior knowledge to specialize in a general LLM
for marketing-oriented scenarios. In short, for each entity 𝑒, we
mainly collect the following two complementary knowledge to
serve as key evidence of LLMs for reasoning.
• Structural Knowledge. The collection of structural knowledge
benefits from the establishment of SupKG [56], which involves
abundant side information of entities, including brand, category
and so on. In order to maintain the reliability of structural knowl-
edge and introduce as less noise as possible, for each entity, we
only collect the one-hop neighbors in the SupKG, coupled with
the entity type for disambiguation (e.g., The type of entity “Apple”
could be “Brand” or “Food”).
• Descriptive Knowledge. Due to the incomplete and noisy fact of
SupKG, we are unable to collect all the convincing evidence for
steering LLMs. Hence, we resort to descriptive knowledge from
public (i.e., Wikipedia) and private knowledge bases. Taking the
entity “The Three Body” as an example, the SupKG only provides
its entity type “Book” and its category “Science Fiction”, while the
descriptive summary in Wikipedia offers stronger evidence (i.e.,
author information and brief introduction) to support effective
knowledge mining.

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY Chunjing Gan, Dan Yang, Binbin Hu, Ziqi Liu, Yue Shen, Zhiqiang Zhang, Jinjie Gu, Jun Zhou, and Guannan Zhang
3.3 LLM as a Relation Filter
As mentioned above, to make the whole procedure of relation gen-
eration under control, we restrict the process to a finite relation
space. Hence a relation filter is encouraged since not all relations in
the whole relation setR are helpful / appropriate for a given entity
to expand marketing-oriented entities (e.g., given the brand entity
“Apple”, the relation “Related Food” may confuse the LLMs for entity
expansion). Therefore, we resort to the powerful capability of LLMs
for filtering desired relations from the pre-defined relation setR.
Given a source entity 𝑠 with an LLMM, we define the relation
filtering as follows:
𝑠
𝜙(· ;K),R
−−−−−−−−→
(1)
RT 𝑠 M(· ;𝜌R(𝑠,𝜅)) −−−−−−−−−−−−→ (2) RF 𝑠 . (2)
(1) Retrieval. Considering that the whole relation setR (includes
relations of all entity types in SupKG and marketing ex-
perts defined relations for each given entity type) cannot
be fed into a single prompt, we first locate the type of the
entity by querying the SupKG K, defined as 𝜙(·;K), e.g.,
𝜙(“Air”;K) = “Brand”. With the entity type 3, we would
retrieve a sub-relation setRT𝑠 fromR for entity 𝑠, where
|RT𝑠|≪|R| (e.g., “Related brand”, “Target audience” and so
on for the Brand “Air”).
(2) Filtering. We come up with applying the LLM as a relation
filter with structural / descriptive knowledge augmented
prompting engineering𝜌R(𝑠,𝜅), i.e., denoted as “{Struc_KG}”
and “{Desc_KG}” in Fig. 2. With the designed prompt, an LLM
would provide i) desired relationsRF𝑠 that align with the
source entity and corresponding prior knowledge, allowing
for more reasonable entity expansion; ii) a potential target
entity corresponding to each desired relation, which could
be regarded as a kind of inheritable knowledge for entity
expansion.
3.4 LLM as an Entity Expansionist
Due to the variety of prior knowledge, coupled with the sensitivity
of prompting under slight modifications, simply employing a single
painstakingly crafted prompt may not always produce the desired
results. To this end, we steer LLMs with careful progressive prompt-
ing augmentation, followed by a reliable aggregation that takes
both self-consistency and semantic relatedness into consideration.
Given a source entity𝑠 and the corresponding relation𝑟, a pipeline
of the entity expansion with an LLMM(·) is formulated as follows:
(𝑠,𝑟)
M(· ;𝜌E(𝑠,𝜅1,𝑟)) −−−−−−−−−−−−−−→T1𝑠,𝑟
M(· ;𝜌E(𝑠,𝜅2,𝑟)) −−−−−−−−−−−−−−→T2𝑠,𝑟
M(· ;𝜌E(𝑠,𝜅...,𝑟)) −−−−−−−−−−−−−−→
(1)
T...𝑠,𝑟
A( ;)
−−−−→
(2)
TF 𝑠,𝑟. (3)
(1) Progressive prompting augmentation. It is designed for navi-
gating an LLMM to different aspects of prior knowledge𝜅, making
the expansion procedure more diverse and robust. In particular, we
mainly prepare three kinds of knowledge: structural knowledge𝜅S,
3For simplicity, the retrieved relation set is the same for different entities of the same
entity type.
descriptive knowledge𝜅D and inheritable knowledge from rela-
tion filtering𝜅I, i.e., denoted as “{Struc_KG}”, “{Desc_KG}” and “{In-
her_KG}” in Fig. 2. By incorporating various knowledge, we progres-
sively construct prompts from coarse-grained to fine-grained man-
ner as{𝜌E(𝑠,𝑟 ;𝜅S),𝜌E(𝑠,𝑟 ;𝜅D),𝜌E(𝑠,𝑟 ;𝜅I),𝜌E(𝑠,𝑟 ;𝜅S,𝜅D),··· ,
𝜌E(𝑠,𝑟 ;𝜅S,𝜅D,𝜅I)}, and query a performant LLM repeatedly for
stability (Fig. 2 presents one of the prompts for entity expansion,
while more detailed examples of prompting augmentation will be
shown in Sec. A.). As a result, we define the mined entities from
the progressive prompt augmentation as

T 1𝑠,𝑟,T 2𝑠,𝑟,··· ,T...𝑠,𝑟 	 .
(2) Reliable aggregation. After entity expansion with progressive
prompting augmentation, we aim at seeking an aggregation mecha-
nismA(·) in a reliable manner to obtain the final entity expansion
result, which takes into consideration the following main aspects:
• Semantic relatedness of the knowledge tuple (𝑠,𝑟,𝑡). Here, we
plug in a small language model, i.e., KG-BERT [54], which is pre-
trained on the hybrid corpus of Wikipedia and SupKG. Subse-
quently, we tokenize the knowledge tuple(𝑠,𝑟,𝑡) as{<𝐶𝐿𝑆 >,𝑧𝑠 1,
··· ,𝑧𝑠𝑎, <𝑆𝐸𝑃 >,𝑧𝑟 1,··· ,𝑧𝑟 𝑏, <𝑆𝐸𝑃 >,𝑧𝑡 1,··· ,𝑧𝑡𝑐, <𝑆𝐸𝑃 >}, where the
source entity is represented as a sentence containing tokens
𝑧𝑠 1,··· ,𝑧𝑠𝑎, the relation is represented as a sentence containing to-
kens𝑧𝑟 1,··· ,𝑧𝑟 𝑏 and the target entity is represented as a sentence
containing tokens𝑧𝑡 1,··· ,𝑧𝑡𝑐, and feed it into the pre-trained KG-
BERT for contextualized representation of each token. We regard
the output of token <CLS> as the representation of the knowl-
edge tuple (denoted as 𝒙𝑠,𝑟,𝑡 ), and the semantic relatedness could
be obtained through a linear projection MLP(·).
• Self-consistency of the knowledge. Specifically, it aims at finding
the most consistent entities when the LLM performs reasoning in
multiple ways. Intuitively, when an entity appears across multiple
expansion results, it indicates the higher confidence of LLMs
towards the particular target entity, which can then be utilized to
reward the highly self-consistent target entities. Here, we denote
the total number that𝑡 appears across multiple entity expansion
procedure as ˝ 𝑘 I(𝑡∈T 𝑘𝑠,𝑟), where𝑘 indicates a specific round
in progressive prompt augmentation and I(𝑡∈T 𝑘𝑠,𝑟) returns 1 if
𝑡 inT𝑘𝑠,𝑟 else 0.
By integrating both aspects, we define the final score for aggre-
gation as follows:
𝜏𝑠,𝑟,𝑡 = log(1+
∑︁
𝑘
I(𝑡∈T 𝑘 𝑠,𝑟))· MLP(𝒙𝑠,𝑟,𝑡) (4)
Finally, given a source entity 𝑠 and relation𝑟, we only keep top
𝐾4 mined entities with the highest scores from aggregation as the
entity expansion result, denoted asTF𝑠,𝑟 .
3.5 LightPAIR: Towards Deployment with a
Strong Teacher-LLM
In general, the effectiveness of PAIR greatly hinges on the remark-
able advancements of LLMs, whereas, equipping PAIR with today’s
state-of-the-art LLMs (i.e., GPT 3.5 with 175 billion parameters) is
rather difficult even impractical to most of the real-world applica-
tions due to far beyond the affordable cost of memory and com-
pute. Meanwhile, inspired by the common insight that the corpus
4In our experiment, we set𝐾 to 8 w.r.t. the trade-off between multiple metrics.

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
Figure 3: The finetuning and inference pipeline of LightPAIR.
generated by a strong teacher-LLM is highly valuable for enhanc-
ing smaller task-specific models via careful fine-tuning[22, 40, 50],
we seek to conduct a lightweight and white-box pipeline of PAIR
(i.e.,LightPAIR) for large-scale MoKG mining from the complete
PAIR. In particular, we collect a group of seed entities (i.e., around
4K∼ 10K) from SupKG and feed them into the complete PAIR. Sub-
sequently, we perform a human evaluation (detailed in Sec.4.1) on
the output entity set, followed by bad-case filtering, e.g., remove
relations / target entities that are annotated as incorrect by human
annotators. To obtain a high-quality corpus for fine-tuning the
smaller language models, we follow the prompt template of rela-
tion filtering and entity expansion to construct questions, coupled
with corresponding responses. Based on theMoKG-oriented corpus,
current lightweight LLMs (e.g., Bloomz [31], GLM [16], ChatGLM
[57], Baichuan-7B [4]) could be easily fine-tuned (i.e., supervised
fine-tuning, short as SFT) via the parameter-efficient Lora [23] strat-
egy. Finally, we inject the smaller fine-tuned LLM into the relation
filtering and entity expansion procedure of PAIR, and adopt the
LightPAIR for mining large-scale MoKG.
3.6 Discussion: Diving into the Progressive
Prompting Augmentation
Merits From the specific examples of progressive prompting aug-
mentation presented in Sec. A, we can find that when compared
with the non-augmented prompt output, the progressive prompting
augmentation has the following virtues:
• Triggering a more reliable knowledge mining in the in-
dustrial setting. Usually, pure LLMs may be unfamiliar with
many marketing-oriented entities and relations such that they
tend to hallucinate in their output, e.g., "Uncle Fruit power bank"
in the case of entity "Uncle Fruit", however, the appropriately
injected knowledge can provide the right context for LLMs and
steer them to the right reasoning direction, hence the output can
be closely related to a brand that sells fruit products.
• Capable of navigating an LLM to different aspects. Take
"Uncle Fruit" as an example, since different knowledge has its
emphasis, the output of an LLM w.r.t. different prior knowledge
varies from each other (e.g., the output of prompt 1 focuses on
common fruit products while the output of prompt 2 focuses
more on the product of service) and results in a more diversified
output, which we carefully evaluate with two metrics in a coarse-
grained to a fine-grained manner and encouraging results can be
found in the “Experiments” part.
About time consumption Intuitively, the progressive prompting
augmentation requires multiple calls to LLMs, incurring more time
consumption compared to the original methods. However, this ad-
ditional time investment is deemed acceptable due to the following
three reasons: i) The progressive prompting augmentation earns
remarkable performance gains compared to original prompting
methods, detailed in Table 1. ii) The knowledge mining task solely
relies on offline inference, and there is no requirement for daily
inference. As a result, the increased time consumption has no im-
pact on downstream applications. iii) Since LightPAIR is capable of
being deployed on a single A100, we can seamlessly accomplish the
overall inference task by utilizing multiple GPUs, thereby meeting
the time requirements efficiently.
4 EXPERIMENTS
4.1 Experimental Setup
4.1.1 Datasets. Since PAIR aims to mine diverse marketing-oriented
knowledge using a group of seed entities and a candidate rela-
tion set, we randomly collect two seed entity sets from the well-
established SupKG. These entity sets consist of 181 entities (i.e.,MoKG-
181) and 500 entities ( i.e.,MoKG-500). With domain knowledge,
we meticulously gather 105 relations (e.g., “Related Food”, “Issue
Voucher”, “Prize of Food” and “Brand of Product”) as the candidate
relation set for entity expansion.
4.1.2 Baselines and Variants. We mainly compare PAIR with the
following baselines and variants:
• KG Completion based , which attempts to mine knowledge in
the established SupKG through textual matching and structural
matching: i) BERT [13], which completes an existing knowledge
graph by textual matching using semantic-based representation.
ii) TRMP [53], which constructs a knowledge graph by retrieval
and ranking of entity pairs in a progressive manner and en-
sembles the entity representation across time to enhance the
knowledge graph stability.
• KG Construction based, which aims at exploring commonsense or
open-world knowledge with deep pre-trained language models:
i) COMET [6], which learns from existing knowledge bases and
generates novel nodes and edges in commonsense descriptive
natural languages. ii) LMCRA WL [11], which designs multiple
prompts to mine a knowledge graph out of a large language model
(GPT 3.5 in this paper) by following the procedure of Subject
Paraphrasing→ Relation Generation→ Relation Paraphrasing
→ DK Object Generation.
• Variants of PAIR : To further examine the merits of each well-
designed part in PAIR, we prepare three variants: i) PAIR -Agg,
which discards the Aggregation operation and it is equivalent to
the most performant version of Progressive prompting. ii) PAIR
-Agg & Pr, which discards the Aggregation operation and the
Progressive prompting and it is equivalent to directly utilize the
output of Relation Filtering. iii) PAIR -Agg & Pr & Rf, which
discards the Aggregation operation, the Progressive prompting
and the Relation filtering and it is equivalent to directly utilize
an LLM for the task of knowledge mining.
For PAIR, we equip it with today’s state-of-the-art LLM (i.e., GPT
3.5 with 175 billion parameters). During the progressive prompting

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY Chunjing Gan, Dan Yang, Binbin Hu, Ziqi Liu, Yue Shen, Zhiqiang Zhang, Jinjie Gu, Jun Zhou, and Guannan Zhang
Table 1: Overall performance comparison of different methods towards mining MoKG. We mark the best and runner-up
performance in bold and “-” means these methods fail to mine novel entities.
MoKG-181 MoKG-500
Methods Accuracy Novelty Diversity Accuracy Novelty Diversity AEE ILAD AEE ILAD
KG Completion BERT 58.4% - 43.0 4.86 57.7% - 42.7 4.97
TRMP 91.1% - 13.8 3.12 91.3% - 14.1 3.07
KG Construction LMCRAWL 86.3% 41.2% 36.3 5.98 85.2% 41.7% 37.1 6.00
COMET 86.7% 35.9% 26.1 5.06 85.9% 34.6% 25.3 4.95
OURS
PAIR 90.1% 40.4% 43.7 5.88 90.7% 43.6% 42.8 5.78
- Agg 88.7% 39.6% 30.8 5.89 88.9% 36.4% 31.3 5.84
- Agg & Pr 86.9% 36.8% 30.8 5.82 87.2% 34.2% 31.4 5.87
- Agg & Pr & Rf 84.9% 39.2% 46.3 6.15 84.3% 39.4% 47.2 6.20
augmentation process, we call the LLM for each specific prompt
for 3 times. For reliable aggregation, the KG-BERT [54] consists of
110 million parameters, which is the same as BERT [13].
4.1.3 Evaluation Protocols and Metrics. We mainly evaluate the
quality of the knowledge mining with human annotation, where
three annotators are involved using a correctness / incorrectness
judge for each extracted knowledge tuple. A tuple is considered
“accepted” if at least two annotators deem it to be true knowledge,
and “rejected” if at least two annotators vote it as false. To ensure
the credibility of human evaluation, we initially gather all predicted
tuples from both baselines and our method. These tuples are then
randomly shuffled before being presented for human annotation.
In this way, the annotators are unaware of which model a specific
knowledge tuple is derived from, which helps to ensure the fairness
in the evaluation process.
Overall, we comprehensively measure the quality of mined knowl-
edge from the following aspects: i)Accuracy refers to the proportion
of accepted tuples. ii) Novelty refers to the proportion of extracted
entities that do not appear in the SupKG. iii) Diversity is evalu-
ated with two metrics from coarse-grained to fine-grained manner.
AEE (Average Entity Expansion) refers to the average number of
target entities expanded from seed entities. ILAD (Intra-List Aver-
age Distance) [48] is a distance-based diversity metric, calculating
the average pair-wise (Euclidean) distance among all the target
entities given a source entity in representation space5. In general,
when evaluating the quality of mined knowledge, the accuracy
metric comes first. With accuracy guarantee, we hope the mined
knowledge with higher novelty and diversity thus better facilitating
downstream tasks in real-world environment.
4.2 Performance Overview
In this part, we report the evaluation results of different knowledge
mining approaches for mining MoKG in Table 1 and the major
findings can be summarized as follows:
5The representations are derived from BERT that are pre-trained on Wikipedia and
SupKG.
• (Superior performance) The proposedPAIR consistently achieves
remarkable performance across all datasets and key metrics, indi-
cating its effectiveness in mining marketing-oriented knowledge
graphs. Besides, beyond its considerable performance in accu-
racy metric, its superior performance in novelty and different
aspects of diversity further indicates that the harvested knowl-
edge graph can provide considerable complementary knowledge
to the original knowledge graph, i.e., SupKG, thus further facili-
tating broader applications to downstream tasks in real-world
environments.
• (Compared with KG completion based methods) It is worth-
while to note that KG completion based methods, especially
TRMP, yield impressive performance w.r.t. the accuracy metric.
However, these methods fail to offer extra knowledge since they
fail to mine novel entities, which is unacceptable for the mining
of MoKG in real-world applications.
• (Compared with KG construction based methods) Not sur-
prisingly, KG construction based methods (i.e., LMCRAWL and
COMET) generally bring a considerable amount of novel knowl-
edge with the help of deep pre-trained language models. How-
ever, the proposed PAIR still surpasses them, attributed to the
following well-designed components tailored for mining MoKG:
adaptive relation filtering and progressive prompting augmenta-
tion, empowered by domain-level knowledge (More case studies
are presented in Section 4.3.2).
• (Ablation studies of PAIR) Clearly, the performance of PAIR
would drop a lot once the corresponding module is discarded, in-
dicating that all of our elaborate designs occupy critical positions
in mining high-quality and high-diversity MoKG for online mar-
keting. It is noted that the variant PAIR -Agg & Pr & Rf (namely
basic prompting method which means directly utilizing an LLM)
ranks highest w.r.t. the diversity metric, demonstrating the abil-
ity of a performant LLM in finding potential target entities for
knowledge graph construction. However, directly utilizing an
LLM for this task results in a rapid decrease of accuracy and nov-
elty as compared to PAIR and its other variants, which further
justifies our model design.

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
Table 2: Performance evaluation of LightPAIR instantiated by different student LLMs. We mark the best and runner-up
performance of student LLMs in bold.
Models PAIR LightPAIR
LLMs(Size) GPT 3.5(175B) GLM(10B) GLM(10B) Bloomz(7B) ChatGLM2(6B) Baichuan2(7B) Qwen2(7B)
SFT ? - % " " " " "
Accuracy 90.1% 79.2% 89.0% 80.8% 86.3% 90.3% 80.6%
Train- Novelty 40.4% 39.9% 31.0% 29.0% 28.8% 31.5% 25.8%
25K Diversity AEE 43.7 27.44 35.71 48.47 39.21 41.08 25.02
ILAD 5.88 6.14 5.77 6.12 5.82 5.96 5.74
Accuracy 90.1% 79.2% 90.7% 82.7% 88.9% 92.2% 80.6%
Train- Novelty 40.4% 39.9% 31.5% 30.2% 29.5% 34.3% 29.1%
100K Diversity AEE 43.7 27.44 37.10 48.03 38.94 41.13 25.89
ILAD 5.88 6.14 5.83 6.14 5.88 5.79 5.49
4.3 Further Probe
4.3.1 LightPAIR with Different Student-LLMs. In this part, we in-
vestigate into the effectiveness ofLightPAIR, augmented by different
student-LLMs.
Data collection for SFT. With the help of GPT 3.5, we generate
two datasets for fine-tuning the smaller LLMs towards relation
filtering and entity expansion, consisting of 25K (i.e., Train-25K) and
100K (Train-100K) samples constructed from (4K-10K) seed entities
, respectively. In detail, we carefully choose various types of entities
and relations from SupKG and utilize the teacher LLM (GPT 3.5) to
do relation filtering, and entity expansion by progressive prompting
and reliable aggregation. Subsequently, we select 3 annotators to
perform a thorough manual verification of the results derived from
the teacher LLM, which ensures the creation of a high-quality
training dataset. On the other hands, we utilize the MoKG-181 as
the evaluation dataset in this experiments 6.
Experimental settings of student-LLMs. With the collected
training corpus derived from the strong teacher-LLM, we adopt
several currently popular open-source LLMs to instantiate theLight-
PAIR, i.e., GLM [16], Bloomz [31] and ChatGLM2 [57], Baichuan-
7B [4], Qwen-7B [3], and set the optimizer, maximum context size,
batch size, and learning rate to Adam, 4096, 8 and 5e-5 respectively.
Results and analysis. From Table 2, by comprehensively taking
multiple metrics into consideration we could find that LightPAIR
with GLM(10B) and Bainchuan2(7B) could achieve comparable per-
formance of the complete PAIR with GPT 3.5(175B), implying that
high-quality corpus generated by a strong teacher-LLM can greatly
enhance smaller task-specific models. Besides, as the training cor-
pus accumulates, an increasing trend among multiple metrics can
be observed which also depicts the significance of collecting high-
quality task-oriented corpus for enhancing task-specific models.
When compared with those student-LLMs with SFT (short for Super-
vised Fine-Tuning), though a pure student-LLM without SFT ranks
6Due to the space limit, we omit the experimental results on MoKG-500 in this paper.
However, it is worth mentioning that similar trends are observed as well.
Product Prize Activity Brand Book Food Game Media Scenery Person Disease
Entity Type
0
10
20
30
40
50
60
70Novelty
Original
w/ PAIR
Figure 4: Illustration of the knowledge graph enriched by
the PAIR.
highest w.r.t. ILAD, the lowest accuracy of the collected knowledge
prohibits its application in real-world industrial environments.
4.3.2 Case Study I: How the Prior Knowledge Improves PAIR. In this
section, we concentrate on the effectiveness of prior knowledge
towards PAIR, which is expected to serve as strong evidence for
relation filtering and entity expansion. We present the results of en-
tity expansion for PAIR w/ knowledge and PAIR w/o knowledge in
Table 3, respectively. Clearly, we find that target entities produced
by the complete PAIR are more related to the corresponding source
entities. On the contrary, PAIR w/o knowledge usually mine hallu-
cinative entities (e.g., “Fruit Education” and “Tuxi Catering”) and
fallacious entities (e.g., “Canon” with the entity “Uncle Fruit” and
relation “related brand”), severely hindering the quality of MoKG.
4.3.3 Case Study II: How the Original Knowledge Graph is Enriched
with PAIR. Since several efforts have been made for connecting
users and various services / products in Alipay through hierarchical
and spatio-related relations, PAIR could provide another comple-
mentary knowledge, i.e., marketing-related knowledge. Here, we
take a close look at the novelty at the entity level by randomly
selecting several specific entity types and presenting the average
novelty in the original knowledge and MoKG with PAIR in Fig. 4.
We find that the original knowledge graph is greatly enriched by

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY Chunjing Gan, Dan Yang, Binbin Hu, Ziqi Liu, Yue Shen, Zhiqiang Zhang, Jinjie Gu, Jun Zhou, and Guannan Zhang
Table 3: Case study towards the usage of prior knowledge in PAIR. We bold the hallucinative entities and fallacious entities in
red and blue, respectively.
Source entity Relation type Target entities
Mi Xiao Quan related media name w/o knowledge Journey to the West ( 西游记)
(米小圈上学记) w/ knowledge Tom and Jerry(猫和老鼠), Boonie Bears(熊出没)
CKA target audience w/o knowledge System Administrator (系统管理员)
(空手道协会) w/ knowledge Karate Enthusiasts(空手道迷), Wushu Master(武术师)
Uncle Fruit related brand w/o knowledge Fruit Education(果儿教育), Canon(佳能)
(果叔) w/ knowledge Xianfeng Fruit(鲜丰水果), Fruitday(天天果园)
The Three Body similar movie w/o knowledge The Wandering Earth(流浪地球)
(三体) w/ knowledge Interstellar(星际穿越), Star Trek(星际迷航)
Gas Coupon product of prize w/o knowledge Fuel Card (加油卡)
(加油券) w/ knowledge Diesel(柴油), Gasoline(汽油), Gas Gift Card(加油礼品卡)
Tuxi Living Plus related company w/o knowledge Tuxi Catering(兔喜餐饮)
(兔喜生活+) w/ knowledge Carrefour(家乐福), CR Vanguard(华润), Walmart(沃尔玛)
Figure 5: Deployment of LightPAIR (i.e., “Offline A”) for audi-
ence targeting and its comparison to the original EGL system
with TRMP framework [53]( i.e., “Offline B”).
Table 4: Performance comparison for audience targeting with
the metric # TAC (thousand). “RI” means the relative im-
provement of LightPAIR w.r.t. EGL.
Scenarios EGL LightPAIR RI
Uncle Fruit 7*1 8*7 +15.3%
The Three Body 3*3 3**6 +98.1%
Schwarzkopf 2*7 4*9 +93.1%
Biscuits voucher 1*2 1*3 +31.2%
Land Lords 9*2 2**2 +122.0%
Gas Coupon 3*8 6*1 +89.2%
PAIR, especially for the entity types “Book”, “Game” and “Disease”,
which are rather rare before.
4.3.4 Application: Audience Targeting. At last, we will demystify
the practical application of MoKG in audience targeting, one of
the fundamental issues of conducting marketing campaigns [66],
which aims at effectively and efficiently locating target audiences
who are interested in certain products / services / campaigns. As
shown in Fig. 5, similar to the original EGL system with TRMP
framework [53], the deployment of LightPAIR is decoupled with
the online serving, thus satisfying the requirements of scalability
and timeliness in industrial environments. We report the perfor-
mance of LightPAIR and EGL based audience targeting in Table
4 with the metrics # TAC ( i.e., the number of Target Audiences
Covered). In Table 4, each scenario could be abstracted as several
entities. Compared to the deployed EGL system, LightPAIR could
achieve performance gains over the EGL by 15% - 122% in different
marketing scenarios w.r.t.the number of Target Audiences Covered.
Both of the observations show the effectiveness and efficiency of
the proposed LightPAIR towards practical online marketing.
5 CONCLUSION
In this paper, we propose a novel PAIR and its lightweight version
LightPAIR for harvesting marketing-oriented knowledge with LLMs,
which are equipped with LLM based adaptive relation filtering
and progressive prompting augmentation based entity expansion
followed by a reliable aggregation that takes both self-consistency
and semantic relatedness into consideration. Towards lightweight
online serving, we specialize in a small and white-box (Light)PAIR,
which is fine-tuned with high-quality corpora provided by a strong
teacher-LLM. Extensive experiments demonstrate the effectiveness
of the proposed (Light)PAIR via several key metrics for knowledge
graph evaluation and practical applications in audience targeting
also verify its applicability in real-world marketing scenarios. In
the future, we would like to equip the proposed (Light)PAIR with
the metapath-oriented entity expansion such that the expansion
process can be more controllable and explainable.

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
A EXAMPLES OF PROGRESSIVE PROMPTING
AUGMENTATION
To further demonstrate the usage of different aspects of prior knowl-
edge in the entity expansion procedure, we present a series of spe-
cific examples of progressive prompting augmentation in Figure 6 -
8, where different types of knowledge is distinguished by color, i.e.,
Struc_KG, Desc_KG and Inher_KG.
1161
1162
1163
1164
1165
1166
1167
1168
1169
1170
1171
1172
1173
1174
1175
1176
1177
1178
1179
1180
1181
1182
1183
1184
1185
1186
1187
1188
1189
1190
1191
1192
1193
1194
1195
1196
1197
1198
1199
1200
1201
1202
1203
1204
1205
1206
1207
1208
1209
1210
1211
1212
1213
1214
1215
1216
1217
1218
Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
1219
1220
1221
1222
1223
1224
1225
1226
1227
1228
1229
1230
1231
1232
1233
1234
1235
1236
1237
1238
1239
1240
1241
1242
1243
1244
1245
1246
1247
1248
1249
1250
1251
1252
1253
1254
1255
1256
1257
1258
1259
1260
1261
1262
1263
1264
1265
1266
1267
1268
1269
1270
1271
1272
1273
1274
1275
1276
Table 5: An example (source entity: Uncle Fruit, relation: related product) of calling an LLM to carry out progressive prompting
augmentation, where different types of knowledge is distinguished by color, i.e., Struc_KG, Desc_KG and Inher_KG.
Augmented Prompt 1 Please list at least 8 related products of the brand "Uncle Fruit", separated by commas, and output the result
in the following format: Related product: [fruit, , ,].
Output 1 Related product: [fruit, dried fruit, jam, fruit vinegar, fruit juice, fruit and vegetable juice,nuts, fruit tea].
Augmented Prompt 2 Please list at least 8 related products of the brand "Uncle Fruit", separated by commas, and output the result
in the following format: Related product: [fruit sales, fruit, grocery shopping, fresh produce, , , ].
Output 2 Related product: [fruit sales, fruit, grocery shopping, fresh produce, fruit delivery service, fruit gift boxes,
fruit juice drinks, fruit delivery].
Augmented Prompt 3 Some keywords related to the brand "Uncle Fruit" are: fruit sales, fruit, grocery shopping, and fresh produce.
Please list at least 8 related products of the brand "Uncle Fruit", separated by commas, and output the result
in the following format: Related product: [fruit, , , ].
Output 3 Related product: [fruit, vegetables, nuts, dried fruit, fresh meal packs, fruit gift boxes, fruit platters, fruit ice
cream].
Augmented Prompt 4 Some keywords related to the brand "Uncle Fruit" are: fruit sales, fruit, grocery shopping, and fresh produce.
Please list at least 8 related products of the brand "Uncle Fruit", separated by commas, and output the result
in the following format: Related product: [fruit sales, fruit, grocery shopping, fresh produce, , , ].
Output 4 Related product: [fruit sales, fruit, grocery shopping, fresh produce, fruit platters, fruit and vegetable delivery,
fresh fruit juice, fruit gift boxes].
Augmented Prompt 5 Some keywords related to the brand "Uncle Fruit" are: fruit sales, fruit, grocery shopping, and fresh produce.
Please list at least 8 related products of the brand "Uncle Fruit", separated by commas, and output the result
in the following format: Related product: [, , , ].
Output 5 Related product: [fruit sales, fruit gift boxes, fruit platters, fresh vegetables, seafood, poultry and eggs, dairy
and beverages, snacks].
Non-augmented Prompt Please list at least 8 related products of "Uncle Fruit", separated by commas, and output the result in the
following format: Related product: [, , ,].
Output Related product: [Uncle Fruit watch, Uncle Fruit earphones, Uncle Fruit smart bracelet, Uncle Fruit power
bank, Uncle Fruit selfie stick, Uncle Fruit data cable, Uncle Fruit insulated cup, Uncle Fruit electric skateboard].
11
Figure 6: An example (source entity: Uncle Fruit, relation:
related product) of calling an LLM to carry out progressive
prompting augmentation.
1277
1278
1279
1280
1281
1282
1283
1284
1285
1286
1287
1288
1289
1290
1291
1292
1293
1294
1295
1296
1297
1298
1299
1300
1301
1302
1303
1304
1305
1306
1307
1308
1309
1310
1311
1312
1313
1314
1315
1316
1317
1318
1319
1320
1321
1322
1323
1324
1325
1326
1327
1328
1329
1330
1331
1332
1333
1334
Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
1335
1336
1337
1338
1339
1340
1341
1342
1343
1344
1345
1346
1347
1348
1349
1350
1351
1352
1353
1354
1355
1356
1357
1358
1359
1360
1361
1362
1363
1364
1365
1366
1367
1368
1369
1370
1371
1372
1373
1374
1375
1376
1377
1378
1379
1380
1381
1382
1383
1384
1385
1386
1387
1388
1389
1390
1391
1392
Table 6: An example (source entity: CKA, relation: related organization) of calling an LLM to carry out progressive prompting
augmentation.
Augmented Prompt 1 Please list at least 8 related organizations of the event "CKA", separated by commas, and output the result in
the following format: Related organization: [China Wushu Sanda Super League Organizing Committee, , ,].
Output 1 Related organization: [China Wushu Sanda Super League Organizing Committee, Chinese Sanda Association,
World Sanda Federation, Chinese Wushu Research Institute, General Administration of Sport of China Wushu
Sports Management Center, Asian Sanda Federation, Chinese Wushu Association, Chinese Wushu Artists
Association].
Augmented Prompt 2 Information related to the event "CKA" includes: Gene granule cell therapy CKA, Chinese Karate Association
CKA, China Wushu Sanda Super League. From 1960, when Bruce Lee brought Chinese Kung Fu to the world,
to 1994 when Jackie Chan successfully entered Hollywood, Chinese Kung Fu has become the best window for
China to showcase its 5000-year culture to the world. Please list at least 8 related organizations of the event
"CKA", separated by commas, and output the result in the following format: Related organization: [ China
Wushu Sanda Super League Organizing Committee, , , ].
Output 2 Related organization: [Gene Granule Cell Therapy Research Institute, Chinese Karate Association, China
Wushu Sanda Super League Organizing Committee, Chinese Wushu Association, Chinese Wushu Artists
Association, Chinese Kung Fu Association, General Administration of Sport of China Wushu Sports
Management Center, Beijing Wushu Association].
Augmented Prompt 2 Information related to the event "CKA" includes: Gene granule cell therapy CKA, Chinese Karate Association
CKA, China Wushu Sanda Super League. From 1960, when Bruce Lee brought Chinese Kung Fu to the world,
to 1994 when Jackie Chan successfully entered Hollywood, Chinese Kung Fu has become the best window for
China to showcase its 5000-year culture to the world. Please list at least 8 related organizations of the event
event "CKA" , separated by commas, and output the result in the following format: Related organization: [, , , ].
Output 3 Related organization: [Chinese Karate Association, China Wushu Sanda Super League, General Administration
of Sport of China Wushu Sports Management Center, Chinese Wushu Association, Chinese Karate Union,
World Wildlife Fund, National Martial Arts Grading Examination Committee,International Wushu Federation].
Non-augmented Prompt Please list at least 8 related organizations of "CKA", separated by commas, and output the result in the following
format: Related organization: [, , ,].
LLM Output Related organization: [Linux Foundation, CNCF, Red Hat, IBM, Kubernetes official, CoreOS, Tencent Cloud,
Alibaba Cloud].
12
Figure 7: An example (source entity: CKA, relation: related
organization) of calling an LLM to carry out progressive
prompting augmentation.
1393
1394
1395
1396
1397
1398
1399
1400
1401
1402
1403
1404
1405
1406
1407
1408
1409
1410
1411
1412
1413
1414
1415
1416
1417
1418
1419
1420
1421
1422
1423
1424
1425
1426
1427
1428
1429
1430
1431
1432
1433
1434
1435
1436
1437
1438
1439
1440
1441
1442
1443
1444
1445
1446
1447
1448
1449
1450
Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
1451
1452
1453
1454
1455
1456
1457
1458
1459
1460
1461
1462
1463
1464
1465
1466
1467
1468
1469
1470
1471
1472
1473
1474
1475
1476
1477
1478
1479
1480
1481
1482
1483
1484
1485
1486
1487
1488
1489
1490
1491
1492
1493
1494
1495
1496
1497
1498
1499
1500
1501
1502
1503
1504
1505
1506
1507
1508
Table 7: An example (source entity: air, relation: related brand) of calling an LLM to carry out progressive prompting augmenta-
tion.
Augmented Prompt 1 Please list at least 8 related brands of the product "air", separated by commas, and output the result in the
following format: Related brand: [Puma, Adidas, Nike, , , , ].
Output 1 Related brand: [Air Jordan, Airwalk, Air Max, Air Force 1, Airtech, Airwalk, Airbourne, Air Step].
Augmented Prompt 2 Please list at least 8 related brands of the product "air" , separated by commas, and output the result in the
following format: Related brand: [footwear, , , ].
Output 2 Related brand: [Nike, Adidas, Puma, Reebok, Converse, Under Armour, Vans, New Balance].
Augmented Prompt 3 A keyword related to the product "air" is: footwear. Please list at least 8 related brands of the product "air",
separated by commas, and output the result in the following format: Related brand: [Puma, Adidas, Nike, , , , ].
Output 3 Related brand: [Nike, Jordan, Airwalk,Reebok, Skechers, New Balance, Fila, Converse].
Augmented Prompt 4 A keyword related to the product "air" is: footwear. Please list at least 8 related brands of the product "air",
separated by commas, and output the result in the following format: Related brand: [footwear, , , ].
Output 4 Related brand: [Nike, Adidas, Jordan, Puma, New Balance, Converse, Reebok, Vans].
Augmented Prompt 5 A keyword related to the product "air" is: footwear. Please list at least 8 related brands of the product "air",
separated by commas, and output the result in the following format: Related brand: [, , , ].
Output 5 Related brand: [Nike, Jordan, Adidas, Puma, Reebok, Converse, New Balance, ASICS].
Non-augmented Prompt Please list at least 8 related brands of the product "Air", separated by commas, and output the result in the
following format: Related brand: [„,].
Output Related brand: [Air Jordan, AirPods, Air Max, Air Force 1, Air Wick, Air France, AirAsia, Air Canada].
13
Figure 8: An example (source entity: air, relation: related
brand) of calling an LLM to carry out progressive prompting
augmentation.
REFERENCES
[1] Badr AlKhamissi and Marjan Ghazvininejad. 2022. A Review on Language Models
as Knowledge Bases. arXiv preprint arXiv:2204.06031 (2022).
[2] Simran Arora, Avanika Narayan, Mayee F. Chen, Laurel J. Orr, Neel Guha, Kush
Bhatia, Ines Chami, and Christopher Ré. 2023. Ask Me Anything: A simple
strategy for prompting language models. In ICLR.
[3] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan,
Wenbin Ge, Yu Han, Fei Huang, Binyuan Hui, Luo Ji, Mei Li, Junyang Lin, Runji
Lin, Dayiheng Liu, Gao Liu, Chengqiang Lu, Keming Lu, Jianxin Ma, Rui Men,
Xingzhang Ren, Xuancheng Ren, Chuanqi Tan, Sinan Tan, Jianhong Tu, Peng
Wang, Shijie Wang, Wei Wang, Shengguang Wu, Benfeng Xu, Jin Xu, An Yang,
Hao Yang, Jian Yang, Shusheng Yang, Yang Yao, Bowen Yu, Hongyi Yuan, Zheng
Yuan, Jianwei Zhang, Xingxuan Zhang, Yichang Zhang, Zhenru Zhang, Chang
Zhou, Jingren Zhou, Xiaohuan Zhou, and Tianhang Zhu. 2023. Qwen Technical
Report. arXiv preprint arXiv:2309.16609 (2023).
[4] Baichuan. 2023. Baichuan 2: Open Large-scale Language Models. arXiv preprint
arXiv:2309.10305 (2023).
[5] Kurt D. Bollacker, Colin Evans, Praveen K. Paritosh, Tim Sturge, and Jamie Taylor.
2008. Freebase: a collaboratively created graph database for structuring human
knowledge. In SIGMOD. 1247–1250.
[6] Antoine Bosselut, Hannah Rashkin, Maarten Sap, Chaitanya Malaviya, Asli Ce-
likyilmaz, and Yejin Choi. 2019. COMET: Commonsense Transformers for Auto-
matic Knowledge Graph Construction. In ACL. 4762–4779.
[7] Tianchi Cai, Jiyan Jiang, Wenpeng Zhang, Shiji Zhou, Xierui Song, Li Yu, Lihong
Gu, Xiaodong Zeng, Jinjie Gu, and Guannan Zhang. 2023. Marketing Budget
Allocation with Offline Constrained Deep Reinforcement Learning. In WSDM.
186–194.
[8] Mohna Chakraborty, Adithya Kulkarni, and Qi Li. 2023. Zero-shot Approach to
Overcome Perturbation Sensitivity of Prompts. In ACL. 5698–5711.
[9] Xuanying Chen, Zhining Liu, Li Yu, Sen Li, Lihong Gu, Xiaodong Zeng, Yize Tan,
and Jinjie Gu. 2021. Adversarial Learning for Incentive Optimization in Mobile
Payment Marketing. In CIKM. 2940–2944.
[10] Xiudi Chen, Hui Wu, and Xiaodong Shi. 2023. Consistent Prototype Learning for
Few-Shot Continual Relation Extraction. In ACL. 7409–7422.
[11] Roi Cohen, Mor Geva, Jonathan Berant, and Amir Globerson. 2023. Crawling
The Internal Knowledge-Base of Language Models. In EACL. 1811–1824.
[12] Sarkar Snigdha Sarathi Das, Arzoo Katiyar, Rebecca Passonneau, and Rui Zhang.
2022. CONTaiNER: Few-Shot Named Entity Recognition via Contrastive Learning.
In ACL. 6338–6353.
[13] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT:
Pre-training of Deep Bidirectional Transformers for Language Understanding. In
NAACL. 4171–4186.
[14] Stephanie deWet and Jiafan Ou. 2019. Finding Users Who Act Alike: Transfer
Learning for Expanding Advertiser Audiences. In KDD. 2251–2259.
[15] Shehzaad Dhuliawala, Mojtaba Komeili, Jing Xu, Roberta Raileanu, Xian Li, Asli
Celikyilmaz, and Jason Weston. 2023. Chain-of-Verification Reduces Hallucina-
tion in Large Language Models. arXiv preprint arXiv:2309.11495 (2023).
[16] Zhengxiao Du, Yujie Qian, Xiao Liu, Ming Ding, Jiezhong Qiu, Zhilin Yang, and
Jie Tang. 2022. GLM: General Language Model Pretraining with Autoregressive
Blank Infilling. In ACL. 320–335.
[17] Tianqing Fang, Hongming Zhang, Weiqi Wang, Yangqiu Song, and Bin He. 2021.
DISCOS: Bridging the Gap between Discourse Knowledge and Commonsense
Knowledge. In WWW. 2648–2659.

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY Chunjing Gan, Dan Yang, Binbin Hu, Ziqi Liu, Yue Shen, Zhiqiang Zhang, Jinjie Gu, Jun Zhou, and Guannan Zhang
[18] Christiane Fellbaum. 1998. WordNet: an electronic lexical database. MIT Press.
[19] Sireesh Gururaja, Ritam Dutt, Tinglong Liao, and Carolyn P. Rosé. 2023. Linguistic
representations for fewer-shot relation extraction across domains. In ACL. 7502–
7514.
[20] Shibo Hao, Bowen Tan, Kaiwen Tang, Bin Ni, Xiyan Shao, Hengzhe Zhang,
Eric P. Xing, and Zhiting Hu. 2023. BertNet: Harvesting Knowledge Graphs with
Arbitrary Relations from Pretrained Language Models. In ACL. 5000–5015.
[21] Johannes Hoffart, Fabian M. Suchanek, Klaus Berberich, and Gerhard Weikum.
2013. YAGO2: A spatially and temporally enhanced knowledge base from
Wikipedia. In Artif Intell, Vol. 194. 28–61.
[22] Cheng-Yu Hsieh, Chun-Liang Li, Chih-Kuan Yeh, Hootan Nakhost, Yasuhisa Fujii,
Alexander Ratner, Ranjay Krishna, Chen-Yu Lee, and Tomas Pfister. 2023. Distill-
ing Step-by-Step! Outperforming Larger Language Models with Less Training
Data and Smaller Model Sizes. In ACL. 8003–8017.
[23] Edward J Hu, yelong shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean
Wang, Lu Wang, and Weizhu Chen. 2022. LoRA: Low-Rank Adaptation of Large
Language Models. In ICLR.
[24] Zhengbao Jiang, Frank F. Xu, Luyu Gao, Zhiqing Sun, Qian Liu, Jane Dwivedi-
Yu, Yiming Yang, Jamie Callan, and Graham Neubig. 2023. Active Retrieval
Augmented Generation. arXiv preprint arXiv:2305.06983 (2023).
[25] Aishwarya Kamath and Rajarshi Das. 2019. A Survey on Semantic Parsing. In
AKBC.
[26] Guillaume Lample, Miguel Ballesteros, Sandeep Subramanian, Kazuya Kawakami,
and Chris Dyer. 2016. Neural Architectures for Named Entity Recognition. In
NAACL. 260–270.
[27] Zhenwen Li, Jiaqi Guo, Qian Liu, Jian-Guang Lou, and Tao Xie. 2022. Exploring the
Secrets Behind the Learning Difficulty of Meaning Representations for Semantic
Parsing. In EMNLP. 3616–3625.
[28] Dugang Liu, Xing Tang, Han Gao, Fuyuan Lyu, and Xiuqiang He. 2023. Explicit
Feature Interaction-aware Uplift Network for Online Marketing. In KDD. 4507–
4515.
[29] Zhining Liu, Xiao-Fan Niu, Chenyi Zhuang, Yize Tan, Yixiang Mu, Jinjie Gu, and
Guannan Zhang. 2020. Two-Stage Audience Expansion for Financial Targeting
in Marketing. In CIKM. 2629–2636.
[30] David Mueller, Nicholas Andrews, and Mark Dredze. 2020. Sources of Transfer
in Multilingual Named Entity Recognition. In ACL. 8093–8104.
[31] Niklas Muennighoff, Thomas Wang, Lintang Sutawika, Adam Roberts, Stella
Biderman, Teven Le Scao, M Saiful Bari, Sheng Shen, Zheng-Xin Yong, Hailey
Schoelkopf, et al. 2022. Crosslingual generalization through multitask finetuning.
arXiv preprint arXiv:2211.01786 (2022).
[32] Tuan-Phong Nguyen, Simon Razniewski, Julien Romero, and Gerhard Weikum.
2021. Refined Commonsense Knowledge from Large-Scale Web Contents. arXiv
preprint arXiv:2112.04596 (2021).
[33] OpenAI. 2023. Chatgpt: Optimizing language models for dialogue.
[34] OpenAI. 2023. GPT-4 Technical Report. arXiv preprint arXiv:2303.08774 (2023).
[35] Fabio Petroni, Tim Rocktäschel, Patrick Lewis, Anton Bakhtin, Yuxiang Wu,
Alexander H. Miller, and Sebastian Riedel. 2019. Language Models as Knowledge
Bases?. In EMNLP. 2463–2473.
[36] Md Mostafizur Rahman, Daisuke Kikuta, Satyen Abrol, Yu Hirate, Toyotaro
Suzumura, Pablo Loyola, Takuma Ebisu, and Manoj Kondapaka. 2023. Exploring
360-Degree View of Customers for Lookalike Modeling. In SIGIR. 3400–3404.
[37] Shruti Rijhwani, Shuyan Zhou, Graham Neubig, and Jaime Carbonell. 2020. Soft
Gazetteers for Low-Resource Named Entity Recognition. In ACL. 8118–8123.
[38] Julien Romero, Simon Razniewski, Koninika Pal, Jeff Z. Pan, Archit Sakhadeo,
and Gerhard Weikum. 2019. Commonsense Properties from Query Logs and
Question Answering Forums. In CIKM. 1411–1420.
[39] Maarten Sap, Ronan Le Bras, Emily Allaway, Chandra Bhagavatula, Nicholas
Lourie, Hannah Rashkin, Brendan Roof, Noah A. Smith, and Yejin Choi. 2019.
ATOMIC: An Atlas of Machine Commonsense for If-Then Reasoning. In AAAI.
3027–3035.
[40] Weijia Shi, Sewon Min, Michihiro Yasunaga, Minjoon Seo, Rich James, Mike
Lewis, Luke Zettlemoyer, and Wen tau Yih. 2023. REPLUG: Retrieval-Augmented
Black-Box Language Models. arXiv preprint arXiv:2301.12652 (2023).
[41] Taylor Shin, Yasaman Razeghi, Robert L. Logan IV, Eric Wallace, and Sameer
Singh. 2020. AutoPrompt: Eliciting Knowledge from Language Models with
Automatically Generated Prompts. In EMNLP. 4222–4235.
[42] Robyn Speer, Joshua Chin, and Catherine Havasi. 2017. ConceptNet 5.5: An Open
Multilingual Graph of General Knowledge. In AAAI. 4444–4451.
[43] Kai Sun, Yifan Ethan Xu, Hanwen Zha, Yue Liu, and Xin Luna Dong. 2023. Head-
to-Tail: How Knowledgeable are Large Language Models (LLM)? A.K.A. Will
LLMs Replace Knowledge Graphs? arXiv preprint arXiv:2308.10168 (2023).
[44] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne
Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal
Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, and Guillaume Lam-
ple. 2023. LLaMA: Open and Efficient Foundation Language Models. arXiv
preprint arXiv:2302.13971 (2023).
[45] Hugo Touvron, Louis Martin, Kevin R. Stone, Peter Albert, Amjad Almahairi,
Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti
Bhosale, D. Bikel, Lukas Blecher, Cristian Cantón Ferrer, Moya Chen, Guillem
Cucurull, David Esiobu, Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller,
Cynthia Gao, Vedanuj Goswami, Naman Goyal, A. Hartshorn, Saghar Hosseini,
Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa, Isabel M.
Kloumann, A. Korenev, Punit Singh Koura, Marie-Anne Lachaux, Thibaut Lavril,
Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning Mao, Xavier Martinet, Todor
Mihaylov, Pushkar Mishra, Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy
Reizenstein, Rashi Rungta, Kalyan Saladi, Alan Schelten, Ruan Silva, Eric Michael
Smith, R. Subramanian, Xia Tan, Binh Tang, Ross Taylor, Adina Williams, Jian Xi-
ang Kuan, Puxin Xu, Zhengxu Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan,
Melanie Kambadur, Sharan Narang, Aurelien Rodriguez, Robert Stojnic, Sergey
Edunov, and Thomas Scialom. 2023. LLaMA: Open and Efficient Foundation
Language Models. arXiv preprint arXiv:2307.09288 (2023).
[46] Milena Trajanoska, Riste Stojanov, and Dimitar Trajanov. 2023. Enhancing
Knowledge Graph Construction Using Large Language Models. arXiv preprint
arXiv:2305.04676 (2023).
[47] Chenguang Wang, Xiao Liu, and Dawn Song. 2020. Language Models are Open
Knowledge Graphs. arXiv preprint arXiv:2010.11967 (2020).
[48] Haolun Wu, Yansen Zhang, Chen Ma, Fuyuan Lyu, Fernando Diaz, and Xue Liu.
2022. A Survey of Diversification Techniques in Search and Recommendation.
arXiv preprint arXiv:2212.14464 (2022).
[49] Benfeng Xu, Quan Wang, Yajuan Lyu, Dai Dai, Yongdong Zhang, and Zhendong
Mao. 2023. S2ynRE: Two-stage Self-training with Synthetic data for Low-resource
Relation Extraction. In ACL. 8186–8207.
[50] Canwen Xu, Daya Guo, Nan Duan, and Julian J. McAuley. 2023. Baize: An Open-
Source Chat Model with Parameter-Efficient Tuning on Self-Chat Data. arXiv
preprint arXiv:2304.01196 (2023).
[51] Vikas Yadav and Steven Bethard. 2018. A Survey on Recent Advances in Named
Entity Recognition from Deep Learning models. In ACL. 2145–2158.
[52] Hua Yan, Yingqiang Ge, Haotian Wang, Desheng Zhang, and Yu Yang. 2023.
Logistics Audience Expansion via Temporal Knowledge Graph. In CIKM. 4879–
4886.
[53] Dan Yang, Binbin Hu, Xiaoyan Yang, Yue Shen, Zhiqiang Zhang, Jinjie Gu, and
Guannan Zhang. 2023. Who Would be Interested in Services? An Entity Graph
Learning System for User Targeting. In ICDE. 3248–3254.
[54] Liang Yao, Chengsheng Mao, and Yuan Luo. 2019. KG-BERT: BERT for Knowledge
Graph Completion. arXiv preprint arXiv:1909.03193 (2019).
[55] Li Yu, Zhengwei Wu, Tianchi Cai, Ziqi Liu, Zhiqiang Zhang, Lihong Gu, Xiaodong
Zeng, and Jinjie Gu. 2021. Joint Incentive Optimization of Customer and Merchant
in Mobile Payment Marketing. In AAAI. 15000–15007.
[56] Xiaoling Zang, Binbin Hu, Jun Chu, Zhiqiang Zhang, Guannan Zhang, Jun Zhou,
and Wenliang Zhong. 2023. Commonsense Knowledge Graph towards Super
APP and Its Applications in Alipay. In KDD. 5509–5519.
[57] Aohan Zeng, Xiao Liu, Zhengxiao Du, Zihan Wang, Hanyu Lai, Ming Ding,
Zhuoyi Yang, Yifan Xu, Wendi Zheng, Xiao Xia, Weng Lam Tam, Zixuan Ma,
Yufei Xue, Jidong Zhai, Wenguang Chen, Zhiyuan Liu, Peng Zhang, Yuxiao Dong,
and Jie Tang. 2023. GLM-130B: An Open Bilingual Pre-trained Model. In ICLR.
[58] Hongming Zhang, Daniel Khashabi, Yangqiu Song, and Dan Roth. 2020. Tran-
sOMCS: From Linguistic Graphs to Commonsense Knowledge. In IJCAI. 4004–
4010.
[59] Muru Zhang, Ofir Press, Will Merrill, Alisa Liu, and Noah A. Smith. 2023. How
Language Model Hallucinations Can Snowball. arXiv preprint arXiv:2305.13534
(2023).
[60] Sheng Zhang, Hao Cheng, Jianfeng Gao, and Hoifung Poon. 2023. Optimizing
Bi-Encoder for Named Entity Recognition via Contrastive Learning. In ICLR.
[61] Yue Zhang, Yafu Li, Leyang Cui, Deng Cai, Lemao Liu, Tingchen Fu, Xinting
Huang, Enbo Zhao, Yu Zhang, Yulong Chen, Longyue Wang, Anh Tuan Luu, Wei
Bi, Freda Shi, and Shuming Shi. 2023. Siren’s Song in the AI Ocean: A Survey on
Hallucination in Large Language Models. arXiv preprint arXiv:2309.01219 (2023).
[62] Yusen Zhang, Jun Wang, Zhiguo Wang, and Rui Zhang. 2023. XSemPLR: Cross-
Lingual Semantic Parsing in Multiple Natural Languages and Meaning Represen-
tations. In ACL. 15918–15947.
[63] Hao Zhu, Yankai Lin, Zhiyuan Liu, Jie Fu, Tat-Seng Chua, and Maosong Sun. 2019.
Graph Neural Networks with Generated Parameters for Relation Extraction. In
ACL. 1331–1339.
[64] Yongchun Zhu, Yudan Liu, Ruobing Xie, Fuzhen Zhuang, Xiaobo Hao, Kaikai
Ge, Xu Zhang, Leyu Lin, and Juan Cao. 2021. Learning to Expand Audience via
Meta Hybrid Experts and Critics for Recommendation and Advertising. In KDD.
4005–4013.
[65] Yuqi Zhu, Xiaohan Wang, Jing Chen, Shuofei Qiao, Yixin Ou, Yunzhi Yao, Shumin
Deng, Huajun Chen, and Ningyu Zhang. 2023. LLMs for Knowledge Graph
Construction and Reasoning: Recent Capabilities and Future Opportunities.arXiv
preprint arXiv:2305.13168.
[66] Chenyi Zhuang, Ziqi Liu, Zhiqiang Zhang, Yize Tan, Zhengwei Wu, Zhining
Liu, Jianping Wei, Jinjie Gu, Guannan Zhang, Jun Zhou, et al. 2020. Hubble: An
industrial system for audience expansion in mobile marketing. In KDD. 2455–
2463.
