---
title: 'The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,
  Applications, Challenges, and Future Trajectories'
url: https://doi.org/10.1007/s11831-026-10720-6
category: ai-marketing
subcategory: framework
date: 2026-08
venue: Archives of Computational Methods in Engineering
authors:
- Pejman Peykani
- Vincent Charles
- Ali Emrouznejad
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s11831-026-10720-6.pdf
pages: 45
chars: 237102
fetched_at: '2026-11-08T19:58:35+00:00'
kb_version: 1
---

# The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures, Applications, Challenges, and Future Trajectories

REVIEW
Archives of Computational Methods in Engineering
https://doi.org/10.1007/s11831-026-10720-6
 Ali Emrouznejad
a.emrouznejad@surrey.ac.uk
Pejman Peykani
p.peykani@khatam.ac.ir
Vincent Charles
vcharles@pucp.pe
Sanly Ghanidel
sanly.ghanidel@srbiau.ac.ir
Daniyal Sabour
daniyalsabour@gmail.com
1 Department of Industrial Engineering, Faculty of
Engineering, Khatam University, Tehran, Iran
2	 Pontifical	Catholic	University	of	Peru,	Lima,	Peru
3	 CENTRUM	Católica	Graduate	Business	School,	Lima,	Peru
4 Surrey Business School, University of Surrey, Guildford, UK
5 Department of Computer Science, Science and Research
Branch, Islamic Azad University, Tehran, Iran
Abstract
Large	Language	Models	(LLMs)	have	emerged	as	a	transformative	technology	in	artificial	intelligence,	significantly
advancing natural language understanding, generation, and reasoning capabilities. This survey reviews the evolution of
language models from early statistical approaches to modern Transformer-based architectures and summarizes key devel -
opments,	including	attention	mechanisms,	scaling	laws,	alignment	techniques,	and	efficient	inference	methods.	The	paper
further	explores	the	growing	impact	of	LLMs	on	everyday	life	and	a	wide	range	of	application	domains,	including	health-
care,	finance,	education,	agriculture,	marketing,	software	engineering,	and	scientific	research.	To	provide	a	systematic
perspective,	LLM	applications	are	categorized	according	to	their	maturity	level	and	integration	across	major	artificial
intelligence	subfields,	such	as	natural	language	processing,	multimodal	learning,	intelligent	decision	support,	autonomous
agents, and knowledge-based systems. The survey highlights how these models enhance automation, data-driven decision-
making, personalized services, and human–AI interaction across both consumer and industrial environments. Despite their
remarkable	capabilities,	LLMs	face	several	critical	challenges,	including	high	computational	costs,	limited	interpretability,
hallucinations, privacy and security risks, ethical concerns, and environmental sustainability issues. Existing mitigation
approaches	and	recent	advancements	are	reviewed	to	assess	their	effectiveness	and	limitations.	Finally,	the	paper	outlines
key	future	research	directions,	including	trustworthy	and	explainable	AI,	efficient	model	architectures,	domain-specific
adaptation, multimodal intelligence, and human-centered alignment. This survey provides a comprehensive overview
of	the	current	landscape,	challenges,	and	future	prospects	of	LLMs,	serving	as	a	valuable	reference	for	researchers	and
practitioners.
Received: 24 March 2026 / Revised: 29 May 2026 / Accepted: 2 July 2026
© The Author(s) 2026
The Versatility of Large Language Models: A Comprehensive Review
and Structured Survey of Architectures, Applications, Challenges, and
Future Trajectories
Pejman Peykani1 · Vincent Charles2,3 · Ali Emrouznejad4  · Sanly Ghanidel5 · Daniyal Sabour1
1 Introduction
Language	is	the	foundational	medium	of	human	intelli-
gence, serving as the primary vehicle for thought, commu -
nication, and cultural transmission. For decades, one of AI’s
central ambitions has been to bridge the gap between the
mere manipulation of computational symbols and genuine
human-like linguistic competence [ 1]. This pursuit, long
constrained by the rigidity of rule-based systems and the
sparsity of statistical n-gram models, has been fundamen -
tally	transformed	by	the	emergence	of	Large	Language
Models	(LLMs).	Built	upon	massive	neural	network	archi-
tectures and pre-trained through self-supervision on inter -
net-scale unlabeled text data, these systems have achieved
an unprecedented capacity not merely to process, but to
comprehend, generate, and reason with human language in
ways that increasingly mirror our own capabilities [ 2–4].

1 3
P . Peykani et al.
This	paradigm	shift	from	task-specific	discriminative	mod-
els to general-purpose generative foundations has inaugu -
rated a new era in natural language processing, one in which
a single model can attain state-of-the-art performance across
a broad spectrum of tasks, including translation, summari -
zation, question answering, and sentiment analysis, without
requiring	task-specific	architectural	modifications	[5].
Despite the abundance of publications, the existing liter-
ature on large language models remains fragmented. Many
surveys	are	limited	in	scope,	focusing	either	on	specific
architectural families, single application domains such as
healthcare	or	finance	[6], or providing purely technical tax-
onomies [7] without bridging the gap between architectural
design and large-scale practical deployment. As a result, the
field	lacks	a	unified	review	that	simultaneously	covers	the
full spectrum of large language model architectures, syn -
thesizes their diverse real-world applications, and explicitly
connects these deployments to a holistic analysis of emerg-
ing challenges.
This survey addresses that gap through a three-part
contribution.	First,	we	present	a	unified	structural	analy-
sis encompassing a comprehensive taxonomy of large
language model architectures, including decoder-only,
encoder-decoder, and hybrid designs, along with their core
components and emergent capabilities. Second, we synthe -
size	LLM	applications	across	fourteen	domains	of	every-
day life, from medicine and education to agriculture and the
arts, organized by maturity level, and provide an integrated
analysis	of	their	role	across	six	key	AI	fields	spanning	Natu-
ral	Language	Processing	(NLP)	to	robotics.	Third,	we	offer
a holistic examination that interweaves persistent technical
barriers, such as high inference costs, with critical ethical,
security,	and	environmental	implication	that	will	define	the
next	generation	of	 responsible	LLM	development.	This
integrative perspective constitutes the primary contribution
of the paper.
To compile this survey, a multi-stage search was con -
ducted	across	reputable	scientific	databases.	A	broad	corpus
of published studies was retrieved from Google Scholar,
IEEE	Xplore,	Elsevier	(ScienceDirect),	SpringerLink,	and
Web of Science, with the aim of constructing a compre -
hensive and up-to-date picture of the research landscape
surrounding large language models. Selection criteria
encompassed citability, recency, with particular emphasis
on work published from 2020 onward, and direct relevance
to	 LLM	 architecture,	 real-world	 applications,	 emergent
capabilities, ethical and security challenges, and cross-
domain deployment. This process ensures that the concep -
tual framework presented in this paper is grounded in the
most	authoritative	and	influential	studies	available,	and	that
the	findings	and	analyses	faithfully	reflect	the	prevailing
and	current	research	directions	in	the	field	of	large	language
models.
The remainder of this paper is organized as follows. Sec-
tion 2 provides the necessary historical background, trac -
ing the evolution of language models from their statistical
origins to the Transformer era. Section 3 presents a precise
architectural	definition	and	taxonomy	of	modern	large	lan-
guage models. Section 4 forms the core of our application-
driven analysis, examining the real-world impact of large
language models across diverse industries, while Sect. 5
explores	their	application	within	key	subfields	of	artificial
intelligence. Section 6 consolidates and critically examines
the major challenges facing large language models, Sect. 7
outlines promising directions for future research, and Sect.
8 concludes the paper.
2 Historical Background and Context
The	evolution	of	LLMs	cannot	be	interpreted	merely	as	a
linear advancement in technology; rather, this evolution is
the result of a series of paradigm failures, each emerging
in response to the fundamental limitations of the preceding
generation. In this section, with an analytical and causal per-
spective, the trajectory of transformation from hand-crafted
rules to massive parametric models is examined.
The	first	approach	to	natural	language	processing	was
built upon rule-based systems, and the logic behind this
choice lay in the structured nature of language; that is, if
sufficient	rules	were	defined,	the	machine	could	understand
it. However, this perspective was confronted from the very
beginning with a fundamental problem: the inherent ambi -
guity, context dependence, and countless exceptions of
human language, and no set of rules could encompass all
its complexities [ 8].	The	idea	of	artificial	neural	networks
(ANN),	proposed	by	McCulloch	and	Pitts	in	the	1940s	[1],
although conceptually revolutionary, failed in practice due
to	hardware	and	algorithmic	limitations	and	led	to	the	first
major failure, namely the inability to generalize. Rule-based
systems could not extract knowledge from data and could
only execute what was explicitly programmed; this is the
very breaking point that paved the way toward statistical
approaches.
Statistical language models emerged by adopting a funda-
mentally	different	assumption,	according	to	which	patterns
should be extracted from data instead of encoding rules; this
paradigm shift was the result of accepting the previous fail-
ure. N-gram models were able to estimate the probability of
the next word based on preceding words, an approach that
worked successfully in limited applications such as speech
recognition. However, these models also faced a struc -
tural deadlock known as the inability to grasp semantics.

1 3
The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,…
A statistical model could say which word is more probable
after capital but it did not understand that capital and seat of
government are identical concepts; this limitation revealed
the necessity for vector-based semantic representation.
The introduction of the concept of word embeddings was
a key causal step, and models such as Word2Vec [ 9] and
GloVe [10] demonstrated that words can be represented in
a multi-dimensional vector space in such a way that seman-
tic	relationships	are	reflected	in	the	geometric	distances
between vectors. The importance of this innovation lay in
the	fact	that,	for	the	first	time,	meaning	became	computable.
The reason for the success of this approach was its reliance
on the distributional hypothesis, according to which words
that appear in similar contexts tend to have similar mean -
ings. However, a fundamental limitation remained, namely
the static nature of these representations.
With the development of deep neural networks, particu -
larly	Recurrent	Neural	Networks	(RNNs)	[11], it became
possible	to	model	sequential	dependencies	in	text.	The	first
neural	language	model,	RNNLM	[12], introduced in 2010,
and Google’s GNMT architecture [13] for machine transla-
tion, demonstrated that neural networks could learn more
complex patterns than simple statistical models. However,
these architectures also grappled with a structural issue: the
vanishing gradient problem in long sequences; the longer
the sentence became, the more the model would forget the
information	from	the	beginning	of	the	sentence.	LSTM	[14]
and GRU [ 15] mitigated this problem to some extent, but
they were not the fundamental solution, and this inherent
limitation paved the way for the Transformer revolution.
The Transformer architecture, introduced in 2017, rep -
resents a turning point in the evolution of language mod -
els and natural language processing [ 16]. This architecture
was transformative for three major reasons. First, the self-
attention mechanism allowed every word in a sentence to
interact directly with every other word, fundamentally
solving the long-term dependency problem without being
dependent on processing order. Second, parallel process -
ing became feasible; unlike RNNs, which had to process
sequences step-by-step, the Transformer views the entire
sentence simultaneously. Third, this architecture was non-
linearly scalable with an increase in data and parameters,
a feature that subsequent models leveraged. Ultimately, it
must be said that without the Transformer, models such as
BERT and GPT would not have been possible, as this archi-
tecture is the common foundation for all contemporary large
language models.
The Transformer architecture opened two distinct evo -
lutionary	paths,	each	responding	to	a	different	objective.
BERT utilized an encoder-only approach and, through
bidirectional pre-training, made it possible to understand
context from both sides of a sentence [ 17]. This choice
was	optimal	for	interpretive	tasks	such	as	classification	and
question answering. In contrast, GPT-1, chose the decoder-
only path, an approach focused on text generation [ 5].
Subsequently,	GPT-2	in	2019,	with	1.5	billion	parameters,
demonstrated that scale alone could improve quality [ 2].
GPT-3, with 175 billion parameters in 2020, was a paradig-
matic experiment that sought to determine whether simply
increasing model scale, data, and computation without alter-
ing the architecture would create qualitatively new capabili-
ties. The answer was yes. The phenomenon of in-context
learning that emerged in GPT-3 demonstrated the ability to
perform new tasks using only a few examples in the prompt,
indicating that at certain scale thresholds, emergent abili -
ties appear [3]. The GPT-4 model in 2023 brought two key
transformations: multimodal processing with the ability to
analyze images, and performance near human level on stan-
dardized tests [ 18].	During	the	same	period,	LLaMA	also
created	a	different	breaking	point,	effectively	showing	that
smaller but more optimized models could achieve perfor -
mance competitive with much larger models, a fact that
was considered a serious challenge to the bigger is better
hypothesis [19].
An examination of the evolution of language models
shows that each generation has emerged in response to a
specific	failure	in	the	preceding	one:	the	inability	to	gen-
eralize led to the rise of statistical approaches; the inabil -
ity to understand meaning led to the invention of word
embeddings; the limitation of static semantics led to the
development of deep networks; the problem of long-term
dependencies led to the emergence of the Transformer; and
task-specific	limitations	led	to	the	turn	toward	large-scale
training. This pattern indicates that large language models
have not evolved through purely incremental advances, but
rather through the cumulative resolution of fundamental
problems. The chronological overview of the major devel -
opments	in	this	field,	shown	in	Fig.	1, illustrates the pivotal
moments from the earliest neural models to the emergence
of advanced language models.
3 Foundations of LLMs: An Application-
Oriented Perspective
A foundational understanding of what large language mod-
els are and how they function is essential for evaluating why
and how these models succeed or in some cases fail across
the diverse application domains examined in this review. In
contemporary	AI	research,	an	LLM	can	be	understood	as	a
foundation-level system whose identity rests on three inter-
related dimensions:

1 3
P . Peykani et al.
 ● Scale Axis: The term “large” in large language mod -
els	reflects	a	principled	relationship	between	scale	and
capability. These models are distinguished from earlier
generations through the systematic expansion of three
interdependent dimensions: model size, training data
volume, and computational budget, relationships that
Kaplan et al. [20] demonstrated follow power-law func-
tions. This scalability, however, is not linear; it exhibits
diminishing returns beyond certain thresholds, while
more recent research suggests that the data-to-parame -
ter ratio is often the primary bottleneck rather than raw
model size [21, 22].	Most	critically,	beyond	specific	scal-
ing thresholds, qualitatively new capabilities emerge,
including in-context learning, instruction following, and
multi-step reasoning that cannot be predicted by extrap-
olating from smaller models [3, 23]. It is precisely these
emergent capacities that make practical deployment fea-
sible in complex domains such as clinical decision sup -
port, legal reasoning, and code generation.
 ● Abstract Representation Learning:  Through self-
supervised pretraining, large language models acquire
latent linguistic structures and develop reusable rep -
resentations that support a wide range of downstream
tasks [2, 17].
 ● Intrinsic Generalization and Transfer: 	 The	 defin-
ing	characteristic	of	LLMs	is	their	ability	to	generalize
across a broad spectrum of tasks with minimal adap -
tation, a capability that fundamentally sets them apart
from	task-specific,	purpose-built	models	[3, 24].
Accordingly,	an	LLM	may	be	defined	as	follows:
A large-scale neural architecture pretrained via self-
supervised objectives on extensive text corpora, whose
foundational property is the internalization of general-pur -
pose linguistic representations that facilitate transfer across
diverse tasks and domains.
This	definition	foregrounds	three	foundational	dimen-
sions	(scale,	representational	universality,	and	adaptabil-
ity)	as	the	core	properties	that	distinguish	large	language
models from earlier generations of language models. This
three-dimensional	characterization	aligns	with	definitions
proposed in prior literature while simultaneously extend -
ing their scope. Zhao et al. [ 7], for instance, describe large
language models as systems developed through transformer
architecture pretraining on large-scale text corpora, demon-
strating that once parameter scale crosses a certain thresh -
old, these models not only exhibit marked performance
gains but also manifest emergent capabilities absent in their
smaller counterparts. However, whereas Zhao et al.’s [ 7]
definition	focuses	primarily	on	architectural	origins	and
scaling	thresholds,	the	definition	adopted	in	this	review
goes further by foregrounding representational universal -
ity and cross-domain transferability properties of particular
relevance to the broad range of applications examined in
Sects. 4 and 5.
Building on this foundation, the subsequent subsections
turn to the technical components that make these proper -
ties	possible.	Specifically,	the	analysis	will	cover	the	archi-
tectural families employed in large language models, the
Fig. 1 Chronological overview of major milestones in the evolution of large language models. Each milestone represents a paradigm shift driven
by the fundamental limitations of its predecessor

1 3
The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,…
training pipelines encompassing both pretraining and adap-
tation stages, and the interaction mechanisms that enable
effective	deployment	of	these	models	in	real-world	settings.
3.1 Architectural Families and Their Application Fit
Architecture forms the conceptual and computational back-
bone of large language models, playing a decisive role in
shaping	their	representational	capacity,	learning	efficiency,
scalability, and generalization patterns. Although recent
advances	in	LLMs	have	often	been	viewed	primarily	through
the lens of data and parameter scale [21], these advances are
deeply intertwined with architectural innovation to the point
that scaling alone, without appropriate architectural design,
not only fails to yield performance gains but can actively
lead to training instability and diminishing returns [ 16].
Understanding	the	architectural	foundations	of	LLMs	is
therefore an essential prerequisite for analyzing their capa -
bilities, limitations, and future trajectories [7].
All major large language models are built on the Trans -
former architecture [16]. Yet Transformer is not a monolithic
design;	it	encompasses	a	family	of	distinct	configurations.
In the sections that follow, we will show how each archi -
tecture family from encoder-only models to multimodal
systems gives rise to distinct practical advantages and limi-
tations	that	govern	the	choice	between	them	across	differ-
ent application scenarios. To provide a clearer conceptual
understanding of the major Transformer architecture fami -
lies	and	their	information	flow	mechanisms,	Fig.	2 presents
a comparative overview of encoder-only, decoder-only, and
encoder–decoder designs, together with their typical appli -
cation domains.
3.1.1 Encoder-Only Architecture
Encoder-only architectures are one of the three main fami -
lies of large language models. Unlike generative models
that produce text token by token, this architecture focuses
on deep understanding of input text through bidirectional
representations. The representative example of this family
is BERT [17], which demonstrated that contextual represen-
tations	with	bidirectional	context	can	significantly	improve
performance on natural language understanding tasks.
The core of the Encoder-Only architecture is based on
the Multi-Head Self-Attention mechanism. For an input
sequence of tokens x1,x 2,......,x n, the query, key, and
value	vectors	are	first	calculated	as	follows	in	Eq.	1:
Q = XW Q,K = XW K ,V = XW V 	 (1)
Then, the output of the attention layer is derived from Eq. 2:
Attention(Q, K, V )= sof tmax( QKT √dk )V	 (2)
Where dk is the dimension of the key vector. Dividing
by √dk prevents gradient explosion in high-dimensional
spaces [16].
Fig. 2	Comparative	overview	of	major	Transformer	architecture	families	and	their	attention	flow	patterns,	including	encoder-only,	decoder-only,
and	encoder–decoder/prefix-decoder	designs,	along	with	their	typical	application	domains

1 3
P . Peykani et al.
The	fundamental	difference	from	Decoder-Only	archi-
tectures lies in the attention mask. In the Encoder, each
token can attend to all tokens in the sequence, both before
and	after	itself	(full	bidirectional	attention),	whereas	in	the
Decoder, attention to future tokens is masked out. Since
the Transformer is inherently not sensitive to the order of
tokens, the model receives positional information through a
positional embedding function. In the original implementa-
tion as shown in Eq. 3:
PE (pos,2i) = sin( pos
10000
2i
d mod el
),PE (pos,2i+1) = cos( pos
10000
2i
d mod el
)	 (3)
The BERT model uses learned positional embeddings. More
advanced models such as RoBERTa [25] and DeBERTa [26]
utilize relative positional embeddings, which demonstrate
better	generalizability	across	different	sequence	lengths.
The main feature that distinguishes the Encoder-Only
architecture from others is its pre-training objective. In
MLM	 (Masked	 Language	 Modeling),	 a	 portion	 of	 the
input	tokens	(typically	15%)	is	randomly	replaced	with	the
MASK token, and the model is tasked with predicting the
original token, which is formalized in Eq. 4:
LM LM = −
∑
i∈M
log P (xi|~x; θ)	 (4)
where M  is the set of masked indices and ~x is the masked
input sequence. This training objective forces the model
to use bidirectional context for prediction, something that
Decoder-Only models are inherently deprived of.
The Encoder-Only architecture is not suitable for text
generation	 tasks	 because	 MLM	 is	 a	 non-autoregressive
training objective, which trains the model to predict multi -
ple tokens simultaneously rather than generating a sequence
token by token. This characteristic limits the practical appli-
cation	of	this	architecture	to	understanding,	classification,
and retrieval tasks such as clinical named entity recognition
in	healthcare	or	contract	classification	in	legal	document
processing.
3.1.2 Decoder-Only Architecture
The Decoder-Only architecture is the most dominant family
of architectures in the current generation of large language
models.	Models	such	as	GPT-3,	GPT-4,	LLaMA	[19], and
PaLM	[27] are all based on this architecture. The funda -
mental principle of this approach is autoregressive language
modeling: at each step, the model predicts the next token
based on all previous tokens. This structural characteristic
has made this architecture the natural choice for generative
tasks [ 3]. The training objective of Decoder-Only models
is to maximize the log-likelihood of the text sequence as
shown in Eq. 5:
L = −
T∑
t=1
log P (xt|x1,x 2,.... ,x t; θ)	 (5)
where xt is the token at position t and θ are the model
parameters. This simple yet powerful training objective
forces the model to fully learn the probability distribution
of	natural	language.	The	key	structural	difference	compared
to the Encoder is the application of a causal mask to the
attention matrix.
One	of	the	most	important	empirical	findings	regarding
the Decoder-Only architecture is the predictable relationship
between model size, training data volume, and performance.
The Chinchilla scaling laws [ 21]	showed	that	for	a	fixed
computational budget C, the optimal number of parameters
N  and training tokens D follow the relationship in Eq. 6:
C ≈ 6ND	 (6)
This	 finding	 revealed	 that	 many	 previous	 large	models
(including	GPT-3)	were	trained	with	less	data	than	optimal,
and that increasing the volume of data is just as important
as increasing the number of parameters. However, the sig -
nificance	of	the	Chinchilla	scaling	laws	extends	beyond	an
empirical	finding;	these	laws	initiated	a	fundamental	para-
digm shift in the design of large language models. Before
Chinchilla, the dominant approach in the research com -
munity was that increasing the number of parameters alone
was the primary driver of performance improvement, an
approach that culminated in GPT-3 with 175 billion param-
eters. The Chinchilla laws directly challenged this assump -
tion	and	demonstrated	that,	for	a	fixed	computational	budget,
resource allocation must be balanced between parameters
and the volume of training data.
The practical implications of this shift are clearly visible
in the next generation of models. Chinchilla, with 70 billion
parameters roughly one-quarter the parameters of Gopher
but trained on four times more data, achieved better per -
formance than Gopher with 280 billion parameters. This
result directly shaped the architecture of subsequent mod -
els;	LLaMA	and	Mistral	7B	[28] were both designed based
on this principle: models with fewer parameters but trained
on substantially more data, which not only perform better
but	are	also	more	efficient	during	inference.
From a theoretical perspective, the Chinchilla laws solid-
ified	the	understanding	that	joint	optimization	of	parameters
and data, not the unilateral increase of either, is the guid -
ing principle for developing large language models. This
principle provided a theoretical framework that still plays

1 3
The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,…
a central role in model design decisions today, including
Llama	3	and	Gemma.
The main limitation of the Decoder-Only architecture
lies in tasks that require deep, bidirectional understanding
of the input text rather than generation. In tasks such as
NER	(Named	Entity	Recognition)	or	fine-grained	classifica-
tion, Encoder-Only models often achieve better results with
fewer parameters, since the unidirectional attention of the
Decoder is less optimal for understanding complex intra-
textual relationships. Additionally, the high computational
cost of these models during inference, especially for long
sequences, poses a practical challenge for their deployment.
This makes Decoder-Only models the dominant choice
for open-ended generation tasks, including medical report
drafting,	financial	advisory	chatbots,	and	code	synthesis,
while	remaining	less	optimal	for	tasks	demanding	fine-
grained input understanding.
3.1.3 Encoder-Decoder Architecture
The Encoder-Decoder architecture, also known as sequence-
to-sequence	(Seq2Seq),	is	designed	for	tasks	where	an	input
sequence must be transformed into an output sequence of
different	length	and	structure.	Unlike	Encoder-Only,	which
merely builds representations, and Decoder-Only, which
generates from scratch, this architecture has two distinct
and	complementary	stages:	it	first	fully	and	bidirectionally
understands the input text, and then, based on that under -
standing, generates the output token by token. Models such
as T5 [29] and BART [30])	are	prominent	examples	of	this
family in the Transformer era.
In this architecture, the Encoder processes the input
X =( x1,x 2,.... . ,x n) and produces a hidden representa -
tion which takes the form given in Eq. 7:
H = Encoder(X)=( h1,h 2,.... . ,h n)	 (7)
Then, the Decoder, with access to this representation, autore-
gressively generates the output Y =( y1,y 2,.... . ,y m),
which can be stated as Eq. 8:
P (Y |X)=
m∏
t=1
P (yt|y1,.... . ,y t−1,H )	 (8)
This formulation shows that each output token depends both
on the previous output tokens and on the entire input rep -
resentation, a characteristic that distinguishes this architec -
ture from the other two families. The key mechanism that
connects the Encoder and Decoder is the Cross-Attention
layer in the Decoder. In this layer, the query vectors are
derived from the Decoder, while the key and value vectors
are derived from the Encoder’s output, as shown in Eq. 9:
Q = HdecW Q,K = HencW K ,V = HencW V 	 (9)
Then the Cross-Attention output is computed as in Eq. 10:
CrossAttention(Q, K, V )= sof tmax( QKT √dk )V	 (10)
This mechanism allows the Decoder to attend to relevant
parts of the input at each generation step. For example, in
translation, when generating each word in the target lan -
guage, the model learns which part of the source sentence to
pay the most attention to [31].
There	are	two	different	approaches	to	pre-training	this
family. For example, T5 uses a Span Corruption objec -
tive, where spans of consecutive tokens are masked and
the model must reconstruct them. However, BART takes a
different	approach,	using	a	wider	variety	of	noising	func-
tions such as token deletion, sentence permutation, and
document rotation, training the model to reconstruct the
original version of the text. This diversity in applying noise
makes BART particularly suitable for generative tasks
such as summarization [ 30].	The	overall	information	flow
and attention interactions within the standard Transformer
encoder–decoder architecture is illustrated in Fig. 3, includ-
ing bidirectional encoding, masked autoregressive decod -
ing, and encoder–decoder cross-attention mechanisms that
enable sequence-to-sequence generation.
3.1.4 Multimodal LLMs
Large	Multimodal	Language	Models	(Multimodal	LLMs)
are	a	generation	of	artificial	intelligence	architectures	capa-
ble of simultaneously processing and integrating informa -
tion from multiple data types, including text, images, audio,
and sensor data. These architectures go beyond unimodal
models and attempt to model the world in a manner closer to
human understanding, through multiple sensory channels.
Models	such	as	GPT-4	V,	Gemini,	and	LLaVA	are	promi-
nent	examples	of	this	family,	which	have	made	significant
advances in various application domains in recent years [18,
32].
The	core	architecture	of	Multimodal	LLMs	is	based	on
a	simple	principle:	converting	each	input	data	type	(text,
image,	audio)	into	a	shared	representation	space	where	the
LLM	can	reason	over	it.	For	images,	this	is	accomplished
through a Vision Encoder, typically based on the Vision
Transformer	(ViT)	architecture	[33]. In ViT, the input image
is divided into small patches, and each patch is mapped into
the embedding space via a linear layer. The output of this

1 3
P . Peykani et al.
process is a sequence of numerical vectors that are equiva -
lent to “visual tokens,” which can be fed into the language
model alongside text tokens.
The main challenge in these architectures is achieving
semantic alignment between the visual space and the lin -
guistic space. These two spaces are trained independently
and	have	different	structures.	The	most	common	solution	is
joint	training	through	Image-Text	Contrastive	Learning,	as
introduced	in	CLIP	[34]. In this approach, the model learns
to bring the representation of an image and its correspond -
ing textual description close together in the shared space,
while pushing apart representations of mismatched pairs, as
shown in Eq. 11:
Lclip = − 1 N
N∑
i=1
log exp(sim(vi,t i)/t) N∑
j=1
exp(sim(vi,t j )/t)	 (11)
After aligning the spaces, the visual and linguistic tokens
interact through Cross-Attention layers. In these layers, the
query vectors are derived from the linguistic component,
while the key and value vectors are derived from the visual
component, and the model learns to focus its attention on
relevant regions of the image when processing each part of
the text, which is described by Eq. 12:
Hout = CrossAttention(Qtext,K visual ,V visual )	 (12)
Fig. 3 Standard Transformer encoder–decoder architecture illustrating scaled dot-product attention, multi-head attention, masked self-attention,
and encoder–decoder cross-attention mechanisms

1 3
The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,…
These two mechanisms, alignment of representation spaces
and cross-attention, are the foundations upon which the
multimodal reasoning capabilities of these models are built.
Multimodal	LLMs	face	several	serious	challenges.	First,
the very high training cost due to the need for large-scale
paired image-text data and a more complex architecture.
Second, the problem of visual hallucination, where the
model describes content that does not exist in the image, a
phenomenon that can have serious consequences in sensi -
tive applications such as medical diagnosis. Third, weak -
ness in precise spatial reasoning, understanding the exact
spatial relationships between objects in an image, remains
an unsolved challenge in these architectures [35].
3.1.5 Recent Architectural Innovations and Multimodal
Integration
Recent	advances	in	LLM	architectures	are	no	longer	focused
solely on increasing the number of parameters; rather, the
main	goals	are	improving	efficiency,	scalability,	and	the
ability	 to	 integrate	 different	 data	 modalities	 with	 more
optimal computational resources. This section examines
three innovation streams that have had the greatest impact
on	the	current	and	next	generation	of	LLMs:	Mixture-of-
Expert’s architecture, advancements in positional embed -
dings for long texts, and native multimodal integration.
Two structural innovations have had the greatest impact on
recent	LLM	architectures:	the	Mixture	of	Experts	(MoE)
[36]	architecture	and	rotary	positional	embeddings	(RoPE)
[37]. In traditional dense architectures, every token is pro -
cessed through the same feedforward network, an approach
that increases computational cost linearly as the number of
parameters grows.
The	Mixture	of	Experts	(MoE)	architecture	addresses	this
limitation by replacing that single identical network with a
set	of	parallel	specialized	networks	(experts).	A	routing	net-
work determines, for each token, which experts it should be
sent	to,	and	the	final	output	is	a	weighted	combination	of	the
outputs from the selected experts, as shown in Eq. 13:
y =
E∑
i=1
G(x)i.Experti(x),G (x)= T opK(sof tmax(Wg .x))	 (13)
In practice, typically only 2 experts out of the entire set are
activated for each token. This design allows the model to
drastically increase the total number of parameters while
keeping the computational cost during inference nearly con-
stant [38].
However, despite its apparent computational advantages,
the Mixture of Experts architecture faces fundamental chal-
lenges at large scales that are not seen in traditional dense
models.	The	first	and	most	important	challenge	is	token
routing. In practice, the routing network must decide which
experts to activate for each token; this decision is discrete
and	 non-differentiable,	 causing	 significant	 difficulties	 in
model training. Common solutions, such as using Gumbel-
Softmax distributions or soft top-k routing, although dif -
ferentiable,	suffer	from	unstable	convergence	and	extreme
sensitivity to learning rates in practice [39].
The second challenge is load balancing among experts.
In many implementations, a phenomenon known as expert
collapse	occurs,	where	only	a	few	specific	experts	process
the majority of tokens, while other experts remain practi -
cally	unused.	This	phenomenon	not	only	reduces	the	effec-
tive capacity of the model but also means that increasing the
number of parameters does not lead to meaningful improve-
ments in performance. To address this problem, auxiliary
loss functions, such as the load-balancing loss in Switch
Transformer, have been designed. However, tuning the coef-
ficient	of	these	auxiliary	losses	itself	becomes	a	challenging
hyperparameter	that	directly	impacts	the	final	quality	of	the
model [40].
The	third,	and	perhaps	most	significant	challenge	from	a
practical application perspective, is the memory bandwidth
bottleneck during inference. Despite reducing mathematical
computations	(FLOPs),	the	Mixture	of	Experts	architecture
requires	repeatedly	loading	the	weights	of	different	experts
from main memory into the processor’s cache. In practice,
the inference time of these models is limited not by matrix
multiplication operations, but by memory bandwidth. In
other words, the processor spends more time moving data
than performing computations. This characteristic is a seri -
ous obstacle, especially in high-throughput inference and in
memory-constrained	environments	(such	as	edge	devices),
challenging the apparent advantage of sparse models [ 41,
42].
The second innovation is Rotary Position Embedding
(RoPE),	which	addresses	the	historical	limitation	of	LLMs
in processing long texts. The core idea of RoPE is to encode
the relative position between tokens through a matrix rota -
tion in the representation space, rather than encoding the
absolute position of each token. The result is that the inner
product of the query and key vectors depends only on the
difference	in	positions	between	the	two	tokens,	not	on	their
absolute positions, as presented in Eq. 14:
⟨ ~qm, ~kn⟩ = qT mRθ,n−mkn	 (14)
This property enables the model to generalize to sequences
longer than those it was trained on. Combined with com -
plementary	techniques	such	as	YaRN	(Yet	another	RoPE
extensioN),	it	has	extended	the	context	window	from	4,000
tokens to over 128,000 tokens [43].

1 3
P . Peykani et al.
Beyond MoE and RoPE, three other parallel streams are
also	shaping	the	next	generation	of	LLMs:
 ● First, Alongside Mamba [ 44], two other alternative ar -
chitectures have emerged in this space: RWKV , which
achieves linear complexity by combining Transformer-
style parallelization with RNN-style recurrent inference
[43], and RetNet, which delivers simultaneous parallel
training and constant inference cost through a three-
mode retention mechanism [ 45]. The choice among
these three architectures depends on deployment re -
quirements, particularly memory constraints and infer -
ence latency. In the multimodal domain, GPT-4 V and
Gemini Ultra dissolved the boundaries between modali-
ties by integrating vision and language within a single
unified	model	[18, 32]. In the open-source ecosystem,
Mixtral 8 × 22B demonstrated the advantages of MoE
without	increased	inference	cost	by	activating	only	39
billion of its 141 billion parameters [46],	while	LLaMA
3 and Qwen 3 set new benchmarks for multilingual
open-source models [47, 48].
 ● Second,	native	multimodal	integration.	The	first	gen-
eration of multimodal models used a serial connection
approach: a pre-trained Vision Encoder was connected
to	an	LLM,	and	the	two	components	were	often	trained
separately. New-generation models such as Gemini and
GPT-4o have moved away from this approach; these
models are trained from the outset with multimodal
data, and the distinction between the visual encoder and
the language model disappears. The result of this archi -
tectural shift is a deeper ability to reason at the boundar-
ies between modalities; the model can not only describe
an image but also reason integrally about complex rela-
tionships among visual elements and linguistic concepts
[18, 32].
 ● Third, the development of small language models with
competitive performance. Models such as Phi-3 [ 49]
and Mistral 7B have shown that, with intelligent selec -
tion of training data and optimized architecture, it is
possible to build models with a few billion parameters
that compete with models tens of times larger on many
tasks.	The	significance	of	this	stream	lies	in	its	practical
horizon: these models can be deployed on edge devices
such as smartphones and industrial equipment, extend -
ing	the	application	range	of	LLMs	from	cloud	environ-
ments to resource-constrained settings.
Collectively, these architectural trajectories signal a shift in
the	LLM	design	space:	the	choice	of	architecture	is	increas-
ingly driven by application constraints whether deployment
occurs	in	a	hospital	edge	device,	a	high-throughput	financial
analytics pipeline, or a multilingual enterprise platform.
3.2 From Pre-training to Deployment: What
Application Developers Need to Know
Before being deployed in a real-world product, large lan -
guage models go through a three-stage pipeline: pre-train -
ing,	fine-tuning,	and	alignment	with	human	preferences.
Understanding this pipeline from an applied developer’s
perspective, not merely a technical one, is essential for mak-
ing informed decisions around model selection, customiza -
tion, and deployment.
3.2.1 Pre-Training
Pre-training	is	the	first	and	most	computationally	expensive
stage in the large language model development lifecycle,
a phase in which the model learns statistical patterns, lin -
guistic structures, and semantic relationships from a mas -
sive corpus of unstructured text through self-supervised
objectives. Unlike traditional systems that rely on labeled
data, this approach allows the model to learn directly from
the inherent structure of the data itself. In decoder-only
architectures, the dominant objective is next-token predic -
tion	(Causal	Language	Modeling),	whereas	encoder-based
models	employ	Masked	Language	Modeling,	where	a	por-
tion of the input tokens are masked and the model learns to
reconstruct them using bidirectional context. This process
not only shapes the model’s capacity to capture long-range
linguistic dependencies, but also lays the foundation for its
generalization, reasoning, and knowledge transfer capabili-
ties [3, 17].
What sets large language models apart from earlier gen -
erations is the unprecedented scale of data and compute
involved in pre-training. GPT-3, for instance, was trained
on approximately 300 billion tokens, while models such as
LLaMA	were	pre-trained	on	over	one	trillion	tokens	drawn
from curated corpora [3, 19]. That said, recent research has
made clear that simply scaling up data volume is no guar -
antee of better performance. The quality, diversity, curation,
and domain coverage of the pre-training corpus play a deci-
sive role in shaping the model’s internal representations and
its ability to generalize to downstream tasks. This is why
models	pre-trained	on	domain-specific	data	in	fields	such
as medicine, law, or biotechnology tend to exhibit more
accurate and consistent baseline performance within those
domains compared to their general-purpose counterparts
[24, 27].
Although the pre-training process is, in practice, well
beyond the reach of most applied developers due to its
demanding computational infrastructure requirements,
understanding its characteristics carries real strategic value
for model selection and deployment. The origin of pre-train-
ing data, the choice of learning objective, the degree of data

1 3
The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,…
filtering,	and	the	thematic	scope	of	the	corpus	all	have	a
direct bearing on the model’s biases, generalization capac -
ity, specialized knowledge, and ultimate behavior. Selecting
a base model, therefore, is not simply a matter of parameter
count; it requires a critical evaluation of the pre-training
process and how well it aligns with the requirements of
the target application domain. Moreover, optimizing data
quality and employing deliberate curation strategies can,
in	many	cases,	prove	more	effective	than	simply	scaling
up model size or parameter count, a consideration that has
drawn growing attention in the development of smaller yet
more capable models [50].
3.2.2 Fine-Tuning
Fine-tuning is the stage at which a pre-trained base model is
specialized for particular tasks or domains. In the traditional
full	fine-tuning	approach,	all	of	the	model’s	parameters	are
updated, a process that, while capable of delivering strong
performance,	is	neither	practical	nor	cost-effective	for	most
development teams due to its heavy demands on memory,
compute, and labeled data [ 51].	Parameter-Efficient	Fine-
Tuning	(PEFT)	methods	address	this	limitation	by	freezing
the pre-trained weights and updating only a small, structured
subset	of	parameters.	Among	these,	LoRA	has	emerged
as one of the most widely adopted adaptation strategies:
compared	to	full	fine-tuning	of	GPT-3	175B	with	Adam,	it
reduces the number of trainable parameters by up to 10000x
and GPU memory requirements by up to 3x, while main -
taining comparable or even superior performance across
models such as RoBERTa, DeBERTa, GPT-2, and GPT-3
[52].	This	efficiency	has	made	PEFT	and	LoRA	in	particu-
lar the go-to choice for deploying large language models in
specialized	domains	such	as	medicine,	law,	and	scientific
research. From an applied developer’s perspective, how -
ever,	fine-tuning	is	only	justified	when	the	base	model	alone
cannot meet the requirements of the target task, and when
sufficient,	high-quality	domain-specific	data	is	available	for
adaptation.
3.2.3 Reinforcement Learning from Human Feedback
(RLHF)
This approach aligns model outputs with human preferences.
Even	after	pre-training	and	fine-tuning,	large	language	mod-
els	offer	no	inherent	guarantee	that	they	will	follow	human
instructions, produce safe responses, or behave in ways
that match user expectations. For this reason, the alignment
stage has emerged as a critical layer in the development
of deployed models, one whose purpose is to transform a
merely capable model into a system that is helpful, control-
lable, and consistent with human expectations.
The	process	typically	begins	with	instruction	tuning	(also
referred	to	as	Supervised	Fine-Tuning,	or	SFT),	where	the
model is trained on curated datasets of instruction–response
pairs so that it can correctly interpret and follow natural lan-
guage requests [53]. This stage meaningfully improves the
baseline quality of text generation and lays the groundwork
for more advanced alignment techniques [54].
Building	on	this,	Reinforcement	Learning	from	Human
Feedback	(RLHF)	further	optimizes	the	instruction-tuned
model based on human preferences. A reward model is
first	trained	on	human-ranked	outputs,	and	the	main	model
is then optimized using algorithms such as PPO to gener -
ate responses that are more helpful, safer, and more natural
[54].	The	significance	of	RLHF	lies	largely	in	how	much
it accounts for the behavioral gap between raw pre-trained
models and deployed conversational systems such as Chat -
GPT. Empirical results have further shown that alignment
quality can matter even more than model scale: Ouyang et
al. [ 54] demonstrated that a 1.3 billion parameter model
aligned	via	RLHF	was	consistently	preferred	by	human
evaluators over the 175 billion parameter GPT-3. These
findings	position	alignment	as	an	independent	and	comple-
mentary dimension of model development, one that goes
well beyond simply increasing parameter count. That said,
given	the	high	cost	and	complexity	of	RLHF,	lighter-weight
alternatives	such	as	Direct	Preference	Optimization	(DPO)
have	 gained	 traction	 as	 efficient	 substitutes	 that	 enable
effective	human	preference	alignment	without	requiring	the
full reinforcement learning pipeline [55].
Beyond these three stages, once a model is deployed,
prompt engineering emerges as one of the most practical
and	cost-effective	strategies	for	optimizing	model	behavior
without modifying its parameters a technique examined in
detail in Sect. 3.4. Figure 4 illustrates this complete pipe -
line from pre-training through deployment and situates
prompt engineering within the broader model development
lifecycle.
3.3 Prompt Engineering as the Application Layer
Prompt engineering refers to a set of strategies that guide
the behavior of large language models through the deliber -
ate design of textual inputs, without any updates to model
parameters. In this approach, the raw input is transformed
into a structured prompt using linguistic patterns, enabling
the	model	to	draw	on	its	pretrained	knowledge	to	fill	infor-
mational gaps and generate the desired output. From an
applied development perspective, prompt engineering rep -
resents	the	most	cost-effective	layer	of	intervention:	unlike
fine-tuning,	it	requires	no	labeled	data,	no	retraining,	and
no heavy computational infrastructure, yet can still exert a

1 3
P . Peykani et al.
meaningful	influence	on	output	quality,	accuracy,	and	con-
trollability [56].
Core prompting strategies can be organized into three
categories based on their level of reasoning complexity:
 ● Zero-shot: In zero-shot prompting, the model oper -
ates solely from a task description, without receiving
any demonstrative examples. Due to its simplicity and
low operational overhead, this approach is a practical
Fig. 4 The four-stage pipeline of large language model development and deployment, from pre-training to real-world application

1 3
The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,…
and	efficient	choice	for	rapid	prototyping	and	general-
purpose tasks where the model’s pretrained knowledge
is expected to provide adequate coverage, such as open-
domain	summarization	or	sentiment	classification	in
general domains [2].
 ● Few-shot: In few-shot prompting, a limited number of
input–output examples are embedded within the prompt
to convey the desired pattern to the model in-context.
This	approach	offers	a	notable	advantage	in	low-re-
source specialized domains such as medical entity ex -
traction	or	legal	document	analysis,	as	it	enables	effec-
tive	 task-specific	 adaptation	 without	 requiring	 large,
labeled datasets [3].
 ● Chain-of-Thought (CoT): At a more advanced level,
Chain-of-Thought prompting instructs the model to gen-
erate intermediate reasoning steps incrementally before
arriving	at	a	final	answer.	This	approach	is	particularly
well-suited	to	tasks	where	the	final	response	is	the	prod-
uct of a multi-step reasoning process, including math -
ematical	problem	solving,	causal	analysis	in	scientific
texts, and evidence-based legal decision-making. CoT
can yield substantial performance gains in complex
reasoning	tasks,	though	this	benefit	is	largely	confined
to large-scale models and may actually degrade perfor -
mance	in	smaller	ones,	a	finding	that	underscores	the
importance of aligning prompting strategy with model
scale for practitioners and developers [57].
One	of	the	most	significant	practical	advances	in	prompt
engineering	is	the	Retrieval-Augmented	Generation	(RAG)
architecture, in which relevant information is retrieved from
external knowledge sources and dynamically incorporated
into the prompt. This approach mitigates the limitations of
the model’s static knowledge base, enabling access to cur -
rent,	domain-specific,	or	organizationally	grounded	infor-
mation without requiring model retraining [58]. As a result,
RAG has emerged as the dominant strategy in enterprise
question-answering systems, document-grounded legal
search,	 and	 dynamic	 financial	 report	 analysis,	 domains
where sole reliance on pretrained knowledge risks produc -
ing outdated information or hallucinations on sensitive sub-
ject matter.
From an operational decision-making standpoint, the
choice among prompting strategies is governed by three key
factors: the reasoning complexity of the task, the availabil -
ity of labeled data, and the need for up-to-date knowledge.
For general-purpose tasks whose data distribution closely
resembles that of pretraining, zero-shot prompting typi -
cally	suffices;	whereas	in	low-resource	specialized	tasks,
few-shot prompting delivers more consistent performance
by supplying a small number of demonstrative examples
[3]. For complex reasoning tasks, Chain-of-Thought or a
combined few-shot + CoT approach is generally preferred
[57]. However, whenever responses require grounding in
dynamic external knowledge or proprietary documents,
RAG becomes practically unavoidable regardless of which
prompting strategy is employed at the layer above [58, 59].
Despite these advantages, prompt engineering faces
significant	 limitations	 from	 an	 operational	 deployment
perspective that extend well beyond its well-documented
syntactic sensitivity. First, lengthy few-shot and CoT
prompts increase inference costs linearly; in API-based
systems operating under constrained budgets, this escala -
tion can render deployment economically unviable [ 60].
Second, the performance instability of zero-shot prompting
in	safety-critical	tasks	such	as	disease	identification	from
clinical	reports	or	risk	assessment	in	financial	documents
makes it a high-risk option that demands additional over -
sight layers [61]. Third, none of these strategies are capable
of correcting faulty knowledge or latent biases embedded
in	the	base	model;	this	fundamental	limitation	defines	the
boundary between prompt engineering and alignment-based
methods	such	as	RLHF	[54]. Prompt engineering should
therefore	be	understood	not	as	a	substitute	for	fine-tuning	or
alignment, but as a complementary layer within the model
deployment pipeline, one whose primary advantage lies in
enabling rapid, low-cost, and scalable deployment, particu-
larly in specialized, low-resource domains [62].
3.4 Comparative Overview of Major LLMs
With the rapid expansion of the large language model eco -
system, applied developers are now faced with a hetero -
geneous	landscape	of	models	that	differ	significantly	in
architecture,	scale,	training	strategy,	efficiency	characteris-
tics, and access conditions. As a result, selecting the right
model	for	different	application	domains,	particularly	those
examined in Sects. 4 and 5 has become one of the central
challenges in developing and deploying generative AI sys -
tems. Yet this question cannot be answered by relying solely
on vendor claims or parameter counts; it requires a system-
atic evaluation of model capabilities across a range of cog -
nitive, reasoning, and applied tasks.
To this end, Table 1 presents the key architectural param-
eters of eleven prominent large language models, covering
all three architecture families introduced in Sect. 3.1. It is
worth noting that this table is limited to proprietary mod -
els	whose	developers	have	officially	disclosed	their	internal
architecture. Table 2 further reports the performance of the
same	set	of	models	across	five	complementary	and	widely
used	benchmarks:	MMLU,	which	evaluates	multidomain
knowledge across 57 academic and professional disciplines
[63]; HellaSwag, which measures commonsense reasoning
[64]; TruthfulQA, which assesses resistance to hallucination

1 3
P . Peykani et al.
[65]; GSM8K, which evaluates step-by-step mathemati -
cal reasoning [ 66]; and HumanEval, which benchmarks
Python code generation quality through unit test execution
[67]. The combined analysis of these architectural and per -
formance indicators provides a structured framework for
guiding model selection in line with application require -
ments, deployment constraints, and cost–performance
considerations.
An examination of the large language models presented
in Tables 1 and 2 reveals that practical superiority is deter -
mined less by parameter count or benchmark rankings alone,
and	more	by	the	fit	between	architecture,	training	strategy,
and deployment requirements. Encoder-only models such
as BERT remain well-suited for analytical tasks like text
classification	and	named	entity	recognition,	owing	to	their
use of bidirectional context [ 17], while encoder-decoder
architectures like T5 deliver stronger performance on
sequence-to-sequence tasks such as translation and summa-
rization [29]. Decoder-only models, by contrast, are better
suited for text generation, dialogue, open-ended reasoning,
and code generation with GPT-4 exemplifying the qualita -
tive	leap	between	generations,	recording	an	MMLU	score	of
86.4%,	compared	to	43.9%	for	GPT-3	[18].
The distinction between proprietary and open-source
models carries equally important strategic implications.
Proprietary	 models	 typically	 offer	 multimodal	 capabili-
ties, larger context windows, and superior performance on
complex tasks such as code generation. Claude 3.5 Sonnet,
Table 1 Key parameters of eleven prominent large language models
Model Category CG Access Parameters MCLDT NL NAH SHS REF
BERT-Large • Bidirectional Encoding
• Fine-tuning
Encoder Only Open
Source
340 M 512 24 16 1,024 Devlin et
al. [17]
T5-11B • Text-to-Text Framework
•	Transfer	Learning
Encoder-Decoder Open
Source
11B 512 24 128 1,024 Raffel	et
al. [29]
GPT-3 •	Few-shot	/	Zero-shot	Learning Causal Decoder API 175B 2,048 96 96 12,288 Brown et
al. [3]
GLM-130B •	Bilingual	(EN+ZH)
• Zero-shot Generalization
Prefix	Decoder Open
Source
130B 2,048 70 96 12,288 Zeng et
al. [68]
BLOOM •	Multilingual	(46	Language)
• Zero-shot Task Transfer
Causal Decoder Open
Source
176B 2,048 70 112 14,336 Workshop
et al. [69]
LLaMA
2–70B
• GQA
•	Long	Context	(4K)
• Open Weights
Causal Decoder Open
Source
70B 4,096 80 64 8,192 Touvron
et al. [19]
Mistral 7B • Sliding Window Attention
•	Efficient	Inference
Causal Decoder Open
Source
7B 8,192 32 32 4,096 Jiang et
al. [70]
GPT-4 • Multimodal Input Instruction
Following
Causal Decoder
(MoE)
API - 128K - - - Achiam et
al. [18]
LLaMA
3–70B
•	GQA	،Long	Context	(8K)
• 128K V ocabulary
Causal Decoder Open
Source
70B 8,192 80 64 8,192 Grattafiori
et al. [47]
Gemini 1.5
Pro
•	Long	Context	(1	M	token)
• MoE
Causal Decoder
(MoE)
API - 1,000K - - - Team et
al. [71]
Claude 3.5
Sonnet
• Constitutional AI
•	Long	Context	(200K)
Causal Decoder API - 200K - - - Kurokawa
et al. [72],
	(NL	=	the	number	of	layers,	NAH	=	the	number	of	attention	heads,	SHS	=	the	size	of	the	hidden	states,	MCLDT	=	the	maximum	context	length
during	training)
Table 2 Comparison of major large language models based on standard benchmarks
Model MMLU HellaSwag TruthfulQA GSM8K HumanEval Primary Application Strength
BERT-Large — — — — — Classification,	NER,	Information	Retrieval
T5-11B 55.1 — 37.0 — — Summarization, Translation
GPT-3	(175B) 43.9 78.9 58.0 — — Few-shot	Learning,	Text	Generation
GLM-130B 44.8 82.4 — — — Bilingual	Processing	(EN/ZH)
BLOOM	(176B) 39.0 73.0 — — — Multilingual Processing
LLaMA	2–70B 68.9 87.3 44.9 56.8 29.9 Open-weight Baseline, Fine-tuning
Mistral 7B 64.2 81.3 42.2 52.1 30.5 Lightweight	Deployment,	High	Efficiency
GPT-4 86.4 95.3 59.0 92.0 67.0 Complex Reasoning, Multimodal
LLaMA	3–70B 82.0 88.0 44.0 93.0 81.7 Fine-tuning,	Local	Deployment
Gemini 1.5 Pro 85.9 95.3+ 58.0 91.7 84.1 Long-context,	Multimodal
Claude 3.5 Sonnet 88.3 95.3+ 63.0 93.7 92.0 Reasoning, Coding, Document Analysis

1 3
The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,…
for instance, leads on coding with a HumanEval score of
92.0%.	Open-source	models	such	as	LLaMA	3	and	Mistral,
on	the	other	hand,	enable	local	deployment,	full	fine-tuning,
and greater data control, features that are of fundamental
importance to organizations operating under privacy or
infrastructure constraints [19]. The pace of progress among
open-source	 models	 is	 equally	 striking:	 LLaMA	 3–70B
achieves	 an	 MMLU	 score	 of	 82.0%	 despite	 its	 openly
available	weights,	sitting	just	4.4%	points	behind	GPT-
4, a gap that has narrowed enough to make local deploy -
ment	an	increasingly	justifiable	choice	for	privacy-sensitive
organizations.
The success of models like Mistral 7B further demon -
strates	that	architectural	efficiency	can	substitute	for	raw
scale:	with	only	7	billion	parameters,	it	achieves	an	MMLU
score	of	64.2%,	surpassing	BLOOM	at	176	billion	param-
eters	(39.0%),	a	result	that	suggests	training	optimization
plays at least as decisive a role as scale in determining per -
formance [70].
Model scale alone does not determine performance.
Chinchilla 70B outperforms larger models on many tasks
despite having fewer parameters, by virtue of being trained
on more and better-curated data [ 21]. Furthermore, the
saturation of benchmarks such as HellaSwag, where GPT-
4, Gemini 1.5 Pro, and Claude 3.5 Sonnet all score above
95.3%	and	are	effectively	indistinguishable	illustrates	that
aggregate	scores	do	not	necessarily	reflect	genuine	supe-
riority in real-world application scenarios. More rigorous
evaluation calls for specialized benchmarks such as GPQA
and SWE-Bench [ 73]. It is also worth noting that models
like BERT were fundamentally designed for analytical tasks
rather than text generation; their evaluation should therefore
rely	on	task-specific	metrics	such	as	F1-score	and	classifica-
tion accuracy, rather than generative benchmarks.
4 Real-World Applications
The	scope	of	Large	Language	Model	applications	has,	in
recent years, extended well beyond laboratory settings and
penetrated	the	operational	fabric	of	diverse	fields.	This
expansion has not been linear or uniform; rather, it has fol -
lowed	a	gradual	pattern	in	which	different	domains	occupy
distinct stages of integration, depending on their infrastruc-
tural readiness, data maturity, and capacity to absorb new
technology.	Accordingly	(Fig.	 5),	the	applications	exam-
ined in this section are organized by deployment maturity,
a	criterion	recognized	in	the	Technology	Readiness	Level
literature as the most fundamental indicator of technological
maturity [74].
The	 classification	 framework	 of	 this	 section	 is	 built
around	a	single	pivotal	question:	has	the	LLM-based	system
moved beyond the laboratory stage and is it being used
continuously in a real-world environment by actual users
or organizations? On this basis, three maturity levels are
defined.	The	Operational	level	encompasses	domains	in
which at least one of the following has been documented:
real-world use at organizational or public scale, the pres -
ence	of	active	real	users,	integration	into	routine	workflows,
or the existence of real performance indicators such as
conversion rates, productivity gains, or user engagement.
The	Pilot	level	covers	domains	where	limited	field	trials
have been conducted but full deployment has not yet been
achieved. The Experimental level includes domains where
LLM	application	remains	at	the	stage	of	controlled	bench-
marks or laboratory studies [75].
This	classification	is	based	not	on	the	importance	or	tech-
nical complexity of a domain, but on documented evidence
of real-world deployment, a distinction essential for a real -
istic	understanding	of	where	LLMs	currently	stand	in	each
context.	With	awareness	of	these	differences,	Section	Four
examines	 LLM	 applications	 across	 fourteen	 specialized
domains from an analytical and critical perspective.
4.1 Tourism
The tourism and hospitality industry are more dependent on
the quality of human interaction than perhaps any other sec-
tor	and	this	is	precisely	what	LLMs	claim	to	simulate.	Yet
deep personalization requires extensive data, and extensive
data collection threatens trust. This fundamental contradic -
tion, rather than technical capabilities, should be the starting
point for evaluating this technology.
Large	 language	 models	 strengthen	 the	 connection
between travelers and service providers by delivering rapid,
accurate responses to traveler queries, real-time information
on weather, attractions, and transportation, and personal -
ized recommendations [76, 77]. Organizations also leverage
these models to enhance marketing and customer relation -
ship management, thereby increasing trust and satisfaction.
Nevertheless, these same capabilities have kept challenges
related to system integration, data privacy, and user trust as
serious obstacles on the path to fully realizing this potential
[78].
The primary advantage of these models lies in person -
alized	customer	engagement.	LLM-based	chatbots	provide
tailored recommendations, detailed amenity and pricing
information, and even virtual tours that enable informed
travel decision-making [79]. Continuous user feedback fur-
ther	refines	model	performance	and	personalization	over
time [80]. Yet a central tension emerges here: deep person-
alization requires the extensive collection of users’ behav -
ioral and preference data, data that, if managed without

1 3
P . Peykani et al.
transparent governance, exposes travelers’ privacy to risk
and rapidly erodes the trust that has been earned [78].
Integrating these models into booking systems, social
networks, and accommodation platforms ensures seamless
access	to	travel	information	and	simplifies	trip	planning
[81]. This integration also creates a foundation for demand
management:	by	analyzing	traveler	data,	LLMs	forecast
trends and optimize marketing strategies [ 82]. Yet this is
Fig. 5	The	role	of	LLMs	in	the	real	world

1 3
The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,…
precisely the point at which algorithmic optimization can
turn against itself. When models simultaneously recommend
the best time to visit a destination to millions of users, they
intensify demand concentration and fuel the phenomenon of
overtourism, a serious threat to the social and environmen -
tal sustainability of destinations that stems directly from the
scalable optimization logic inherent to these models [80].
LLMs	move	beyond	simple	automation	only	when	they
can genuinely grasp the cultural context, implicit needs, and
emotional dimensions of the travel experience. Evidence
suggests,	however,	that	these	models	still	face	significant
gaps	in	this	domain.	LLM-based	chatbots,	for	instance,
frequently resort to generic, context-free responses when
handling ambiguous or culturally sensitive requests such as
recommending places that carry local symbolic meaning,
and this tendency measurably erodes user trust [ 77]. Real-
izing true personalization in tourism requires the thought -
ful	integration	of	LLM	capabilities	with	human	expertise,
transparent data governance, and a genuine commitment
to destination sustainability. Without these conditions, the
technology will optimize not the travel experience itself, but
merely the process of selling it [79].
4.2 Research
Large	language	models	are	redefining	the	scientific	research
cycle, yet the fundamental question remains: are these
models merely accelerating an existing process, or are they
reshaping the very structure of research itself? From the
initial stages of ideation and research question formulation
through	to	final	editing	and	manuscript	submission,	these
models reduce researchers’ cognitive load and create oppor-
tunities for greater focus on analytical and creative dimen -
sions of inquiry [ 83, 84]. Nevertheless, a clear distinction
must be drawn between facilitating the research process and
replacing	scientific	judgment:	LLMs	can	identify	research
gaps and generate preliminary data, but literature synthe -
sis and experimental design remain dependent on human
expertise [85]. This dependence is not merely a matter of
technical limitation; these stages require context-sensitive
judgment, methodological validity assessment, and tacit
understanding	of	a	field’s	theoretical	traditions,	capabilities
that language models are not yet able to simulate reliably
[86].
One	of	the	most	significant	applications	of	these	mod-
els is their support for non-native-speaking researchers.
Enhancing grammar, style, and vocabulary in academic
writing improves manuscript quality and facilitates publi -
cation in international journals [ 87]. This capability carries
strategic	importance	from	the	standpoint	of	scientific	equity,
as it partially reduces a longstanding barrier to participation
by researchers from non-English-speaking communities.
Yet	this	opportunity	comes	with	a	serious	tension:	if	LLMs
homogenize writing style, might epistemic diversity and
distinct scholarly voices, themselves a source of innovation,
be pushed to the margins? [88]
The	risk	of	hallucination	and	the	fabrication	of	ficti-
tious references stands among the most serious challenges
in	applying	LLMs	to	scientific	research.	This	phenomenon
threatens not only the credibility of individual manuscripts
but	the	integrity	of	the	broader	scientific	ecosystem	because
errors at this layer propagate into the ecosystem itself, not
merely into a single paper. Human validation is therefore
not an optional step but a structural requirement in any
LLM-assisted	research	workflow	[89, 90].
In the editorial process, these models assist editors by
improving coherence, structure, and style, as well as detect-
ing plagiarism [91, 92]. Yet the deeper tension surfaces in
peer	review	management:	if	an	LLM	drafts	the	editor’s
decision letter, to what extent does genuine editorial inde -
pendence remain? The gradual automation of these layers
carries	the	risk	of	transforming	scientific	peer	review	from
a	judgment-driven	process	into	a	confirmation-driven	one
[93, 94]. For reviewers as well, automating routine revi -
sions creates space for deeper engagement with substantive
scientific	evaluation	[88, 95] provided that transparency in
the use of these tools becomes institutionalized as a profes-
sional norm [96].	LLMs,	then,	are	not	merely	accelerants	of
the	research	process;	they	are	redefining	the	epistemology
of	scientific	peer	review	itself,	and	this	distinction	carries
institutional	implications	that	extend	well	beyond	workflow
optimization.
4.3 Business
Large	language	models	are	redefining	the	competitive	logic
of modern businesses—not merely through the automation
of repetitive tasks, but by empowering organizations to pro-
cess vast volumes of behavioral and textual data for strate -
gic decision-making [97, 98]. This transformation, however,
is	not	one-dimensional;	organizations	that	employ	LLMs
solely as cost-reduction tools overlook their primary poten-
tial in generating strategic insights. Recent studies indicate
that	LLMs	can	produce	outputs	aligned	with	the	judgments
of human experts in evaluating strategic options and select-
ing business models, although they remain susceptible to
biases and inconsistencies that require human oversight [99,
100].
In	 marketing	 and	 content	 generation,	 LLMs	 have
increased engagement rates and reduced content produc -
tion costs by personalizing messages based on customer
data analysis [89, 101]. This capability has also manifested
in supporting sales teams; from product positioning to han -
dling	customer	objections,	LLMs	have	improved	conversion

1 3
P . Peykani et al.
rates [102]. However, excessive data-driven personalization
raises serious concerns regarding customer privacy and
the	boundary	between	persuasive	influence	and	behavioral
manipulation.	In	this	context,	evidence	suggests	that	LLMs
are capable of employing sophisticated persuasive strategies
that	are	difficult	for	users	to	detect,	while	existing	regulatory
frameworks have often failed to provide adequate responses
to these challenges [103].
In customer service and customer relationship manage -
ment,	LLM-based	chatbots	 have	enabled	high-accuracy,
24/7 responsiveness while reducing the workload of human
staff	[104]. However, the critical point is that the quality of
customer experience in complex and emotionally charged
interactions still depends on human social intelligence,
where language models face limitations in understanding
cultural and emotional subtexts [ 105]. Recent studies indi -
cate	that	although	LLMs	demonstrate	certain	elements	of
empathy including emotion recognition and emotional sup-
port, the clinical evaluations and educational standards in
this	domain	are	still	in	their	early	stages,	and	LLMs	con-
tinue to face serious limitations in handling complex emo -
tional burdens and diverse cultural contexts [106].
In market analysis and managerial decision support,
LLMs	transform	unstructured	data	derived	from	reports,
surveys, and social media into actionable insights [ 107].
This capability enhances the prediction of customer behav -
ior	and	the	identification	of	market	opportunities;	however,
excessive managerial reliance on model outputs with -
out understanding their limitations may lead to decisions
that overlook systemic risks hidden within the data [ 108].
Recent	research	shows	that	LLMs	reproduce	decision-mak-
ing patterns similar to human cognitive biases, including
overconfidence	and	framing	effects,	which	can	be	harmful
in high-risk situations [ 109]. Ultimately, the true value of
LLMs	in	business	is	realized	when	they	are	integrated	into
decision-making processes as complements to human judg-
ment, rather than replacements for it.
4.4 Education
Large	language	models	hold	the	potential	to	fundamentally
reshape the processes of teaching, assessment, and learning,
though realizing that potential depends on a precise under -
standing of their pedagogical limitations and prerequisites
[110]. These models perform comparably to students on
standardized tests in mathematics, physics, and computer
science, and they strengthen reading comprehension in lit -
eracy-based tasks [ 111]. Nevertheless, strong performance
on	standardized	assessments	should	not	be	conflated	with
the capacity for critical thinking or creativity; these models
reproduce linguistic patterns rather than necessarily demon-
strating deep understanding.
One	of	the	most	significant	capabilities	of	these	models	is
the personalization of learning. By analyzing students’ per-
formance	and	preferences,	LLMs	generate	tailored	instruc-
tional materials, feedback, and adaptive exercises aligned
with each learner’s level and pace [ 112–114]. Compared
to	 traditional	 one-size-fits-all	 instruction,	 this	 approach
enables more precise targeting of individual weaknesses.
However, excessive reliance on model outputs risks under -
mining students’ intellectual independence, a challenge that
researchers emphasize must be addressed through the delib-
erate design of learning environments [115].
In the domain of teaching, these models reduce repeti -
tive tasks and accelerate content design, freeing teachers to
invest more energy in creative engagement with students
[116]. Systems such as Khanmigo have demonstrated the
effectiveness	of	LLM-based	tutoring	in	one-on-one	learning
contexts [117];	however,	the	efficacy	of	these	tools	depends
heavily on teachers’ digital and pedagogical competence, a
variable that remains limited in many educational systems,
particularly in developing countries [118].
In foreign language education, these models function as
conversational partners, enhancing listening, speaking, and
grammar skills through interactive dialogue, vocabulary
reinforcement, and scenario-based exercises [ 119]. Nev -
ertheless, excessive reliance on such tools can constrain
creativity and critical thinking [ 120]. It is therefore an
undeniable necessity that both teachers and students receive
appropriate	training	to	use	LLMs	as	a	supplementary	tool,
not a replacement [121, 122].
4.5 Art
The	LLM	is	simultaneously	a	creative	partner	and	a	repro-
ducer, and it is this contradiction, not its capabilities, that
defines	its	role	in	art.	Artists	draw	on	the	textual	sugges-
tions of these models in storytelling, composition, and
color arrangement to create novel artistic expressions that
challenge traditional boundaries [123]. These systems have
served as a source of inspiration in poetry, narrative, music,
and visual art, while also supporting cultural analysis and
art criticism [124, 125]. Yet one must ask: is text extracted
from the statistical analysis of millions of human works
truly creativity, or is it an intelligent rearrangement of what
has already existed?
By generating imaginative texts and conceptual prompts,
LLMs	help	artists	develop	new	visual	and	intellectual	ideas.
Integration	 with	 generative	 tools	 such	 as	 DALL·E	 and
MidJourney, and multimodal systems like Gemini, expands
the possibilities of design, painting, and music [ 126].
Enhancing creative quality through reinforcement learning
from human feedback elevates the stylistic coherence of
these	collaborations	and	redefines	how	artists	engage	with

1 3
The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,…
technology. Yet this collaboration carries a serious legal and
ethical tension: when a model is trained on the works of
specific	artists	and	reproduces	their	style,	where	is	the	line
between inspiration and intellectual property infringement?
This is a question to which existing legal systems have yet
to	offer	a	satisfactory	answer	[127].
In	the	ideation	process,	LLMs	overcome	creative	blocks
by extracting linguistic and conceptual patterns from vast
datasets, functioning as intellectual partners in innovation
[128]. Yet this is precisely where the contradiction intro -
duced in the opening paragraph returns in sharper form:
these models evaluate artworks in art criticism against cri -
teria such as innovation and originality [ 129, 130], while
having learned these very concepts solely from the statisti -
cal patterns of prior critical texts, not from any lived under-
standing of what innovation feels like or why originality
matters. In the same vein, in art history, the models identify
stylistic shifts and support interdisciplinary research through
digitization and archival organization [131], yet interpreting
the	cultural	significance	of	those	shifts,	what	distinguishes
an artistic movement from a passing trend, still demands
human judgment nourished by historical context and lived
experience [132].
In the end, the answer to this section’s epistemological
question	is	clear:	an	LLM	simulates	creativity,	not	under-
standing. But for an artist who knows what they are work -
ing with, that simulation is a tool capable of meaningfully
expanding their creative horizon without replacing the
depth of lived experience from which authentic art springs
[127, 132].
4.6 Media
Do large language models democratize digital media, or do
they intensify the concentration of power in content pro -
duction? The answer lies not in the technical capabilities of
LLMs,	but	in	how	they	are	deployed	and	governed.	By	ana-
lyzing genre, tone, and style, these models generate natu -
ral, creative, and contextually appropriate text, and through
integration into chatbots, social networks, and interactive
platforms, they enable personalized communication that
increases user engagement and retention [ 133, 134]. Yet
this very capacity for scalable personalization raises a more
pressing	question:	when	content	reflects	the	dominant	pat-
terns in a model’s training data rather than the diversity of
human voices, is cultural diversity in media strengthened or
eroded?
In	 digital	 advertising,	 LLMs	 generate	 customized	 ad
copy	 tailored	 to	 specific	 market	 needs,	 improving	 con-
version rates [ 135].	 Techniques	such	 as	 PPLM	 enable
keyword-driven targeted generation, with generative AI
integration enhancing ad quality, user experience, and cost
efficiency	[136].	LLMs	further	strengthen	marketing	perfor-
mance by forecasting costs, optimizing bidding strategies,
and increasing click-through rates [137].	Yet	this	efficiency
carries an ethical tension: automated ad optimization blurs
the line between personalization and behavioral manipula -
tion, particularly when models are designed to target users’
psychological vulnerabilities in order to maximize conver -
sion rates [138].
Content	 personalization	 is	 the	 domain	 where	 LLMs
simultaneously demonstrate their greatest potential and
their deepest contradictions. By interpreting users’ needs,
preferences, and cultural context, these models generate
outputs that enhance satisfaction and engagement [ 139].
Prompt-based learning enables stylistic control across sto -
rytelling, journalism, and social media [ 140], and interac -
tive systems such as collaborative storytelling tools foster
creativity and learning through adaptive feedback [141]. Yet
deep personalization carries the risk of intensifying infor -
mation	bubbles:	when	LLM	algorithms	optimize	content
based on a user’s interaction history, they may prioritize the
reinforcement of existing biases over the expansion of epis-
temic horizons [142].
LLMs	are,	in	themselves,	neither	democratizing	nor	cen-
tralizing forces this duality is contingent on their design,
governance, and deployment objectives. When deployed
to lower the barriers of content production for independent
creators and under-resourced communities, they hold genu-
ine democratizing potential [ 143]. But when placed in the
service of advertising optimization and behaviorally-driven
personalization for large platforms, they become instru -
ments of power concentration within the media ecosystem.
The	future	of	LLM-based	digital	media	ultimately	depends
on which of these applications becomes institutionalized
[136].
4.7 Medicine
Large	language	models	have	brought	about	a	fundamen-
tal	transformation	in	the	field	of	medicine	by	providing
advanced capabilities in understanding and generating nat -
ural	language;	a	transformation	that	differs	in	nature	from
the incremental improvements of the past [144, 145]. What
distinguishes these models from rule-based and keyword-
search systems is their ability to perform context-aware
reasoning, a capability demonstrated in the diagnosis
of complex conditions such as Alzheimer’s disease and
dementia, which can help bridge the diagnostic gaps present
in traditional systems [146, 147].
Models	such	as	GPT-4	and	Med-PaLM	2	have	achieved
expert-level performance on standardized examinations
like	USMLE	and	MultiMedQA,	and	in	some	qualitative
dimensions such as empathy they have even outperformed

1 3
P . Peykani et al.
physicians [ 148, 149]. However, these results should be
interpreted with caution; success in multiple-choice exami -
nations does not necessarily translate into competence in
real-world clinical decision-making, where ambiguity,
incomplete data, and human judgment play central roles. In
the	domain	of	personalized	care,	LLMs	have	enabled	the
adaptation of treatments to patients’ individual characteris -
tics [150, 151], yet a fundamental question remains regard-
ing the extent to which the outputs of these models can
be trusted without expert supervision. A similar challenge
arises in medical documentation; tools such as ChatCAD
and	XrayGPT	have	demonstrated	considerable	efficiency
in generating radiology reports [ 152, 153], but systematic
errors in image interpretation may lead to serious clinical
consequences.
LLMs	hold	the	greatest	value	not	as	replacements	for
specialists, but as complementary tools. Genuine progress
will be achieved when these models are deployed within
rigorous regulatory frameworks and evaluated according to
standards grounded in real clinical performance, rather than
merely laboratory benchmarks [154–156].
Despite	these	achievements,	LLMs	still	struggle	with
the	risk	of	generating	inaccurate	medical	information	(hal-
lucinations)	and	with	the	lack	of	interpretability	in	complex
clinical settings, challenges that make their widespread
deployment in sensitive healthcare environments irrespon -
sible without structured human oversight.
4.8 Finance
By integrating textual and numerical data, large language
models	have	introduced	a	novel	approach	to	financial	analy-
sis that is more advanced than traditional systems in terms
of	both	depth	and	flexibility.	Domain-specialized	models
such	as	FinGPT	and	BloombergGPT,	trained	specifically	on
financial	data,	have	demonstrated	higher	accuracy	than	gen-
eral-purpose models in market sentiment analysis, numeri -
cal information extraction, and question answering over
financial	documents	[157, 158]. This superiority suggests
that domain specialization, rather than merely increasing
model size, is the determining factor in performance.
In	the	field	of	financial	text	processing,	LLMs	cover	tasks
ranging from named entity recognition to risk analysis of
corporate reports [159, 160]. Tools such as FinBERT have
not only improved accuracy, but have also uncovered latent
linguistic	patterns	in	financial	documents	that	keyword-
based methods were unable to detect [ 161]. However, this
very capability to extract linguistic patterns also creates a
potential vulnerability; malicious actors can deliberately
disseminate	fake	news	or	manipulated	financial	reports	to
steer	the	model	toward	flawed	analyses,	thereby	influenc-
ing algorithmic trading decisions. This threat, known as data
poisoning through information channels, can cause wide -
spread	losses	in	financial	markets	where	reaction	speed	is
critical	before	the	error	is	even	identified	[162].
In algorithmic trading, frameworks such as FINMEM,
inspired by human cognition, improve decision-making
transparency compared to earlier reinforcement learning
approaches [163]. This transparency constitutes a strategic
advantage	in	financial	markets,	where	institutional	account-
ability is critically important. Nevertheless, a fundamental
question remains: does transparency in a model’s reasoning
necessarily	imply	the	reliability	of	its	outputs?	In	financial
forecasting, zero-shot and few-shot learning combined with
chain-of-thought reasoning in GPT-4 have outperformed
classical ARMA-GARCH models, while also enhancing
interpretability as a factor in building investor trust [ 164,
165]. However, trust based on apparent interpretability,
without security guarantees at the input-data layer, may
itself	become	a	factor	that	amplifies	systemic	risk,	as	inves-
tors	place	confidence	in	reasoning	that	has	been	formed	on
the basis of poisoned data [166].
4.9 Computer Programming
Large	language	models	have	substantially	transformed	the
software development process. Through natural language
understanding, code generation, debugging, and optimiza -
tion, these models enhance productivity across all levels of
developer experience [167, 168]. Transformer-based models
such as Codex and CodeGen, trained on large code corpora,
generate functional code from natural language instructions
and power tools like GitHub Copilot [ 169, 170]. Yet this
broad accessibility introduces a foundational tension: does
lowering the barrier to entry in programming elevate the
quality of code produced within the software ecosystem, or
does it accelerate the accumulation of unreviewed and vul -
nerable code?
Evaluating	LLM-generated	code	presents	a	serious	meth-
odological	challenge.	Metrics	such	as	BLEU,	originally
designed for machine translation evaluation, do not capture
the functional correctness of code, and their application
risks producing a misleading picture of actual output qual -
ity [171]. This evaluation gap underscores that the develop-
ment of specialized testing frameworks is a prerequisite for
the responsible deployment of these models in production
environments [172].
In the domain of debugging and optimization, these
models interpret error reports and stack traces to propose
patches	 for	 common	 bugs,	 and	 improve	 efficiency	 and
maintainability through code refactoring [ 173, 174]. They
also facilitate cross-language translation and enable the
migration of legacy codebases [175]. However, reliance on
automated debugging suggestions without understanding

1 3
The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,…
the underlying error mechanism can trap less experienced
developers	in	a	cycle	of	superficial	patches	that	mask	deeper
structural problems.
In code documentation and analysis, these models gener-
ate clear natural-language explanations of functions, identify
security vulnerabilities, and ensure compliance with coding
standards [ 176]. In programming education, they provide
a personalized experience for beginners through adaptive
exercise generation and immediate feedback [175]. Yet here
the	same	central	tension	resurfaces:	does	immediate	LLM
feedback strengthen problem-solving skills in the learner, or
does	it	sacrifice	depth	of	learning	for	ease	by	eliminating	the
experience of productive struggle? Evidence suggests that
in the absence of intentional instructional design, these tools
can substitute dependency for competence [170].
Taken	together,	the	sustained	success	of	LLMs	in	pro-
gramming depends on the development of more precise
evaluation benchmarks and informed human oversight—not
as a constraint, but as a guarantor of quality in an ecosystem
that grows more reliant on these tools with each passing day
[168].
4.10 Industry
Large	 language	 models	 are	 fundamentally	 transforming
the equations of productivity and innovation in industrial
environments. What distinguishes this transformation from
previous	waves	of	automation	is	the	ability	of	LLMs	to
process natural language and convert tacit knowledge into
executable operational guidance. As virtual assistants, these
models enable workers to rapidly access technical docu -
mentation and specialized knowledge, thereby reducing
machine downtime and training costs [177, 178]. However,
the	effectiveness	of	these	systems	is	highly	dependent	on
the quality and currency of their training data. In industrial
environments, where equipment and processes are con -
stantly evolving, models trained on outdated data may pro -
vide misleading guidance.
In	the	field	of	predictive	maintenance,	LLMs	analyze
sensor data to identify potential failures before they occur,
thereby preventing costly downtime [ 179]. This capability
acquires genuine strategic value when integrated with IoT
systems, as the convergence of real-time sensor data with
the model’s linguistic reasoning simultaneously improves
supply chain coordination and responsiveness to market
fluctuations	[180]. This integration also creates a serious
cybersecurity challenge; every connection point between
an	LLM	and	industrial	infrastructure	constitutes	a	potential
attack surface that, in critical environments such as power
plants or pharmaceutical production lines, could lead to cat-
astrophic consequences.
In	 quality	 control,	 LLMs	 process	 production	 data,
identify deviations, and provide immediate feedback that
reduces costly errors [ 181]. In the area of product cus -
tomization, conversational interfaces enable customers to
directly express their desired features, while companies
gain valuable data for optimizing design and marketing
strategies [ 182].	In	innovation	and	product	design,	LLMs
accelerate the product development cycle by analyzing mar-
ket information and generating creative suggestions [ 183].
Nevertheless, excessive reliance on model-generated sug -
gestions during the ideation phase may constrain engineers’
divergent thinking and lead to premature convergence
toward conventional solutions, a risk that threatens radical
innovation.
4.11 Law
The penetration of large language models into the legal
domain carries a promise that extends well beyond mere
productivity gains: a fundamental transformation in access
to justice. These models’ capacity to interpret complex legal
texts, automate document drafting, and support case analy -
sis has the potential to reduce the cost of legal services while
improving	overall	efficiency	[184, 185].	Legal	informatics,
by translating human objectives into legally interpretable
instructions, creates transparent frameworks for AI-driven
decision-making [ 186].	In	practice,	LLMs	have	demon-
strated performance on legal examinations and document
drafting comparable to that of law students [187],	and	Legal
Prompt	Engineering	(LPE)	enables	the	analysis	of	lengthy
documents, prediction of judicial outcomes, and multilin -
gual operation with high accuracy [188]. At a more granular
level, the ability to segment texts into distinct components,
case facts, arguments, and judicial rulings accelerates case
comprehension and reduces error rates [ 189]. Yet this pic-
ture represents only one side of the coin; the other is the
gap that persists between technical capability and the insti -
tutional readiness to embrace this technology.
The study by Siino et al. [190], drawing on a broad survey
of	legal	NLP	applications,	paints	a	more	nuanced	picture	of
this gap, identifying the lack of specialized domain knowl -
edge and the absence of interpretability as fundamental chal-
lenges	to	deploying	LLMs	in	this	arena.	The	nature	of	these
challenges is not purely technical; it reaches into the very
core	of	legal	philosophy.	Legal	reasoning,	unlike	general
language processing, demands not merely textual compre -
hension but an understanding of context, judicial precedent,
and normative hierarchies’ dimensions that models trained
on general-purpose corpora are ill-equipped to grasp. A fur-
ther dimension of this gap crystallizes in the phenomenon
of hallucination, a problem whose consequences in legal
systems extend far beyond a simple informational error.

1 3
P . Peykani et al.
The	findings	of	Dahl	et	al.	[191] reveal that when queried
about a court’s pivotal ruling, models hallucinate in at least
75%	of	cases.	This	alarming	figure	is	not	merely	a	statisti-
cal shortcoming; it has given rise to documented instances
of disciplinary sanctions against attorneys across multiple
jurisdictions worldwide [192]. In other words, model hal -
lucination in this domain directly erodes institutional trust
and	inflicts	tangible	professional	harm.
A further challenge lies in the complexity of adapting
to regional legal frameworks, which directly undermines
the premise of universal solutions. The analysis by Siino
[193], conducted within the context of Italian law, makes
clear that developing general-purpose models for judicial
environments	is	insufficient;	each	legal	system,	with	its
own legislative structure, language, and procedural conven-
tions,	demands	localized	approaches.	This	finding	stands	in
tension with the straightforward logic of more data, better
performance, demonstrating that the accumulation of legal
data drawn from diverse systems does not necessarily yield
deeper comprehension of any single one.
At the governance layer, the question of accountability
for algorithmic errors in judicial decision-making remains
unanswered, and the implementation of the European
Union’s AI Act requirements for high-risk judicial applica-
tions is still in its early stages [194]. This regulatory vacuum
has produced a kind of grey zone in which technology has
outpaced its legal frameworks.
The	sustainable	success	of	LLMs	in	this	domain,	there-
fore, lies not in the rush toward full automation, but in three
interconnected prerequisites: pre-training on authoritative,
domain-specific	legal	corpora	[195]; specialized evaluation
frameworks	that	operate	beyond	general	NLP	benchmarks
[196]; and, most critically, structured human oversight
mechanisms that preserve the role of the judge and the attor-
ney as the ultimate decision-makers [197].
This regulatory vacuum has produced a kind of grey zone
in which technology has outpaced its legal frameworks. The
sustainable	success	of	LLMs	in	this	domain,	therefore,	lies
not in the rush toward full automation, but in three inter -
connected prerequisites: pre-training on authoritative,
domain-specific	legal	corpora	[198]; specialized evaluation
frameworks	that	operate	beyond	general	NLP	benchmarks
[188, 195]; and, most critically, structured human oversight
mechanisms that preserve the role of the judge and the attor-
ney as the ultimate decision-makers [199]. Until these three
conditions	are	met,	LLMs	will	not	democratize	access	to
justice; they will reproduce legal error at industrial scale.
4.12 Agriculture
The role of large language models in agriculture extends
beyond simple automation; they function as a bridge
between	complex	scientific	knowledge	and	practical	on-
farm decision-making, addressing a gap that has long been
a central challenge in transferring technology to the agricul-
tural sector [200]. By integrating agricultural data, environ-
mental conditions, and farmers’ preferences, these models
provide personalized and context-aware recommendations
through interactive dialogue, an approach that has demon -
strated	considerable	effectiveness	in	pest	control,	fertilizer
guidance, and other agricultural decisions [201]. This capa-
bility becomes a serious challenge when model-generated
recommendations are applied in regions with high climatic
and agricultural diversity without validation from local
experts, since indigenous knowledge and microclimatic
conditions	are	often	insufficiently	represented	in	the	train-
ing data of these models.
In	the	field	of	information	extraction	and	data	generation,
LLMs	address	the	problem	of	limited	diverse	and	labeled
datasets, a challenge arising from seasonal and climatic
variability that has constrained the development of machine
learning	systems	in	agriculture.	Multimodal	models	fine-
tuned on agricultural data can enrich datasets and simulate
temporal or weather-related conditions [202]. Although this
synthetic data generation approach expands analytical capa-
bilities, it also carries the risk of reinforcing biases already
present	in	the	original	datasets;	a	model	trained	on	artifi-
cially generated data may fail to accurately represent real-
world farm patterns [203].
The analysis of textual data from news sources and social
media also provides insights into market trends, crop pric -
ing, and emerging agricultural practices [204]. In the design
of	 agricultural	 technologies,	 the	 capacity	 of	 LLMs	 for
knowledge processing and creative reasoning helps identify
design challenges and reduce development risks; a promi -
nent example is their application in designing robotic grip -
pers for tomato harvesting [ 205, 206]. Overall, the greatest
value	of	LLMs	in	agriculture	is	realized	when	they	function
as complements to local agricultural expertise, rather than
replacements for it.
4.13 Energy
The integration of large language models in the energy sector
has	created	significant	potential	for	optimizing	operations
and advancing environmental sustainability goals [ 207].
However, one must ask: does this integration genuinely
improve	the	efficiency	of	energy	systems,	or	does	it	merely
add a layer of technological complexity on top of existing
structural challenges? Answering this question requires dis-
tinguishing between what these models have demonstrated
in laboratory settings and what is actually achievable within
real-world energy infrastructure.

1 3
The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,…
LLMs	 have	 reduced	 operational	 costs	 by	 supporting
complex building energy simulations, generating optimized
code, and enabling decentralized inference feasibility stud -
ies [208, 209]. They have also accelerated and democratized
energy	simulation	workflows	through	automated	data	gen-
eration, output analysis, and visualization [ 210, 211]. Yet
this accessibility introduces a fundamental paradox: the
ease of use may encourage non-expert users to over-rely
on model outputs in complex design decisions, situations
where	even	a	minor	simulation	error	can	lead	to	inefficient
or costly designs.
In edge computing environments, decentralized infer -
ence distributes workloads across devices, enabling reliable
deployment in remote and resource-constrained settings
[212].	LLM-driven	code	optimization	has	further	reduced
computational energy consumption [ 213]. Yet this is pre -
cisely	where	the	field’s	most	profound	paradox	emerges:
LLMs	function	simultaneously	as	tools	for	reducing	energy
consumption and as massive energy consumers in their
own right. Quantitative evidence makes this contradiction
unmistakable: training a single transformer model with 213
million parameters alongside neural architecture search
generates	approximately	626,155	pounds	of	CO₂,	and	since
2012, the computational demands of training large models
have roughly doubled every three to four months [214]. This
reality suggests that the energy savings achieved through
inference-stage code optimization are often negligible when
weighed against the energy cost of training increasingly
larger models.
In	the	domain	of	energy	policy,	LLMs	accelerate	evi-
dence-based research and policymaking by extracting and
analyzing data from legal and regulatory sources [ 215].
Yet the same paradox that surfaced in simulation and
code optimization reappears here in a subtler form: mod -
els deployed to analyze clean energy policy documents are
themselves powered by energy-intensive infrastructure that
often remains dependent on fossil fuels. More precisely,
the	analytical	legitimacy	of	an	LLM’s	policy	recommenda-
tions on carbon reduction becomes questionable from the
standpoint of internal consistency when the model’s own
carbon	footprint	is	excluded	from	the	analysis.	LLMs	can
therefore	genuinely	improve	energy	system	efficiency,	but
only when deployed within a Green AI framework, utilizing
energy-efficient	architectures	and	expert	oversight,	rather
than through a Red AI approach that maximizes accuracy
without regard for environmental cost.
4.14 Network and Telecommunications
Large	language	models	are	penetrating	the	operational	core
of telecommunications networks, a domain where the expo-
nential complexity of infrastructure has pushed traditional
management to the limits of human capability. The fun -
damental question is how to reconcile the imperative of
deterministic precision in networking with the inherently
probabilistic nature of these models. This tension is most
visible in the vanguard application: Intent-Based Network -
ing	(IBN).	The	ability	to	translate	commands	such	as	block
all	YouTube	traffic	to	the	office	into	precise	adjustments	of
Quality-of-Service parameters opens a path toward democ -
ratizing network management [ 216], yet conceals a criti -
cal	question:	if	the	translation	from	intent	to	configuration
contains an error, who bears responsibility for the conse -
quences? This accountability gap is a blind spot that the
pace of deployment has largely overshadowed [217].
The research by Siino et al. [ 218] presents a structured
framework for managing wireless laboratories a deliberate
effort	to	contain	this	uncertainty	through	systematization.
Defining	 configurations	 as	 pre-designed	 Blueprints	 and
leveraging few-shot prompting represents a move toward
constraining the model’s output space; by automating the
full experimental cycle, this approach reduces dependence
on	domain	specialists.	Yet	the	reliance	on	predefined	struc-
tures lays bares an inherent tension: the current solution
achieves precision at the cost of generality, and this trade-
off	will	prove	vulnerable	when	confronted	with	emergent
topologies or proprietary protocols.
At the layer of monitoring and fault diagnosis, the value
LLMs	offer	is	of	a	different	kind:	the	capacity	to	infer	causal
relationships from vast volumes of log data precisely where
traditional rule-based systems falter, particularly when
faced with novel anomalies [ 216]. This capability takes on
heightened	significance	in	the	context	of	the	transition	to
6 G networks, where autonomous orchestration demands
continuous comprehension of high-level intent and its
translation	 into	 executable	 configurations	 [219]. Multi-
agent architectures currently being tested in response to
this demand promise scalability by distributing complexity
across specialized agents; yet in doing so, they transform
the	problem	of	inter-agent	coordination	and	conflict	resolu-
tion into a new and formidable challenge.
Reconciling the deterministic precision demanded by
networks	with	the	probabilistic	nature	of	LLMs	may	be
achievable not through wholesale replacement, but through
the deliberate design of intelligent oversight layers where
the model proposes and the human approves. Yet as long as
two fundamental obstacles remain unresolved, the tension
between near-zero error tolerance in networks and the inher-
ently probabilistic character of these models, and the risk
of proprietary data leakage in scenarios reliant on closed-
source	APIs,	the	widespread	deployment	of	LLMs	in	tele-
communications is not a technical horizon but a governance
challenge [217, 220].

1 3
P . Peykani et al.
An	analytical	review	of	Large	Language	Model	applica-
tions across twelve specialized domains reveals that these
models encounter distinct challenges, opportunities, and
limitations in each context. To enable coherent compari -
son across domains, Table 3 provides a consolidated over -
view, bringing together for each domain the tools or models
employed, the type of quantitative evidence available, the
key reported metrics, and the primary risks. In addition,
each	domain	is	classified	into	one	of	three	maturity	levels
based on documented deployment evidence, rather than
technical complexity or thematic importance: Operational
(documented	deployment	in	real-world	environments	with
active	users	or	organizations);	Pilot	(limited	field	trials	with
proof-of-concept	(PoC)	validation	but	without	full-scale
deployment);	and	Experimental	(early-stage	research).	This
classification	documents	the	empirical	basis	of	the	organi-
zational framework introduced at the outset of this section
and	offers	a	realistic	picture	of	where	LLMs	currently	stand
in each domain.
5 The Application of LLMs in Subfields of
Artificial Intelligence
LLMs	can	be	regarded	not	merely	as	tools	in	service	of	arti-
ficial	intelligence,	but	as	a	transformative	force	reshaping	its
internal architecture. While Sect. 4 of this paper examined
the	applications	of	LLMs	across	fourteen	practical	and	inter-
disciplinary	domains,	including	medicine,	law,	and	finance,
the present section shifts the level of analysis to within the
field	of	AI	itself,	demonstrating	how	these	models	have	fun-
damentally transformed its core branches: from natural lan-
guage processing and machine learning to computer vision,
robotics, recommender systems, and generative AI. Figure
6 provides an overview of these applications.
5.1 Natural Language Processing
Large	language	models	share	a	fundamental,	bidirectional
relationship	with	NLP:	on	one	hand,	NLP	has	provided
the theoretical foundations and architectural frameworks
that	gave	rise	to	LLMs;	on	the	other,	LLMs	have	redefined
problem-solving approaches and pushed the functional
boundaries	of	NLP	itself.	Previously,	tasks	such	as	named
entity recognition, sentiment analysis, and natural language
inference each required dedicated models and large vol -
umes of labeled data. By leveraging self-supervised learn -
ing	and	large-scale	pretraining	on	unlabeled	corpora,	LLMs
have fundamentally reduced these constraints, making
approaches like prompt-based learning a reliable alternative
to	task-specific	fine-tuning	[3, 5, 235, 236].
The	most	significant	qualitative	leap	LLMs	have	brought
to	NLP	is	their	capacity	for	multi-step	linguistic	reason-
ing. The Chain-of-Thought method, implemented in mod -
els such as GPT-4, yields meaningful performance gains
on mathematical problem sets like GSM8K, while strong
results	on	the	RTE	benchmark	reflect	genuine	progress	in
understanding semantic relationships [4, 23, 66, 237]. Com-
pared to earlier architectures like BERT, which required
task-specific	 fine-tuning	 for	 each	 downstream	 applica-
tion,	modern	LLMs	achieve	competitive	results	through
in-context learning without any parameter updates, a shift
that has fundamentally reshaped the operational landscape
of	NLP	[238]. These capabilities have laid the groundwork
for broad applications across domains such as medicine,
law, and education, discussed in detail in Sects. 4.7, 4.11,
and 4.4. In machine translation and summarization as well,
LLMs	produce	coherent	outputs	through	semantic	structure
analysis	that	match	or	surpass	those	of	dedicated	fine-tuning
approaches [239, 240].
Nevertheless, these advances come with serious method-
ological challenges that continue to constrain the broader
adoption	of	LLMs	in	NLP.	First,	the	performance	of	these
models on low-resource languages, which constitute the
majority	of	the	world’s	languages,	remains	significantly
below that achieved in English, and the performance gap
between high-resource and low-resource languages persists
as	an	unresolved	debate	not	only	within	multilingual	NLP
but	as	a	general	challenge	for	these	models	as	a	whole	(Sect.
6.5)	[238]. Second, traditional evaluation metrics such as
BLEU	in	machine	translation	or	F1	in	named	entity	recogni-
tion fail to fully capture the true quality of model outputs, as
discourse coherence, factual accuracy, and stylistic appro -
priateness all fall outside the scope of what these metrics
can meaningfully measure [ 4]. Third, despite strong per -
formance	on	standard	benchmarks,	LLMs	exhibit	notable
degradation when faced with out-of-distribution data, a
phenomenon that raises fundamental questions about the
genuine generalizability of these models and directly bears
on	the	validation	of	their	use	in	high-stakes,	domain-specific
applications [54].
5.2 Machine Learning
With	their	entry	into	the	field	of	machine	learning,	Large
Language	Models	(LLMs)	act	not	merely	as	tools	for	lan-
guage processing, but as engines for improving learning
processes.	One	of	their	most	significant	contributions	in	this
domain is the generation of synthetic data and text rewriting
to increase the volume and diversity of training data [ 241].
In	the	medical	field,	which	is	discussed	in	detail	in	Sect.	4.7,
the	use	of	synthetic	texts	generated	by	LLMs	has	improved
model	performance	by	more	than	7%	compared	to	baselines

1 3
The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,…
Industry Main Application Model / Tool Type of
Quantitative
Evidence
Quantitative Metrics and Results Maturity	Level Risks	/	Limitations Refer-
ences
Tourism • Travel planning
• Visitor support
•	Dutch	Cycling	Life-
style AI
• Discover Puerto
Rico Ask AI
• Ellis chatbot
• User engage-
ment statistics
•	Dutch	Cycling	Lifestyle	AI	generated	442,000
images and over one million sessions in a month with
7.5 million reaches
• Ask AI builds multi-day itineraries based on user
preferences
• Ellis chatbot supports more than 40 languages.
• Operational • Dependence on
infrastructure
• Recommendation
accuracy
[221]
Research •	Scientific	text
generation
• Analysis
• ChatGPT • Reviewer
studies
• User surveys
•	Reviewers	correctly	identified	AI-generated
abstracts	only	68%	of	the	time,	meaning	one-third
were	misclassified	as	human;	~80%	of	Nature	readers
use ChatGPT for summarizing, drafting and data
analysis.
• Operational • Misinformation
•	Lack	of
transparency
•	Scientific
inaccuracies
[84]
Business • Advertising
• User conversion
• RARE Ad Retrieval
•	LLM	traffic	studies
• A/B tests
• Conversion
statistics
•	RARE	raised	consumption	by	5.04%,	GMV	by
6.37%,	CTR	by	1.28%,	and	deep	conversions	by
24.77%.
•	Amsive	found	organic	conversion	at	4.60%	vs
4.87%	for	LLM	traffic,	an	insignificant	0.27-point
difference.
• Operational • Advertising
misuse
• Inconsistent per-
formance	benefits
[222]
[223])
Education • Intelligent tutoring
• Personalized
learning
• Khanmigo •	Large-scale
user
experiments
• Summarizing a student’s recent activity improved
next-question	correctness	by	3.4%;	cognitive	engage-
ment	increased	5.09%
•	97.5%	of	interactions	showed	improvement	across
608,000 tutoring sessions.
• Operational • Student privacy
concerns
• Over-reliance on
recommendations
[110]
Art • AI-assisted visual
art generation and
creative design
•	DALL-E	2
• Dreamlike Photoreal
• Midjourney
• Image-quality
and creativity
benchmarks
•	DALL-E	2	achieved	the	highest	image-quality
scores in the HEIM benchmark.
• Dreamlike Photoreal obtained the highest ratings in
aesthetics and originality.
• Human evaluators consistently rated AI-generated
artworks competitively against human-created content
in visual-creativity assessments.
• Operational • Copyright issues
• Artistic ownership
disputes
• Cultural bias
[224])
Media • Multimedia
content gen-
eration and visual
understanding
• GPT-4 V
• VisIT-Bench models
• Vision-
language
evaluation
benchmarks
•	GPT-4	V	achieved	an	Elo	score	of	1349	in	the	VisIT-
Bench benchmark, slightly exceeding the human
baseline score of 1338.
•	Multimodal	LLM	systems	demonstrated	strong
performance in complex image-captioning and media-
understanding tasks compared with previous vision-
language baselines.
• Operational • Misinformation
generation
• Synthetic media
manipulation
• Computational
cost
[224])
Medicine • Diagnostic
support
• Clinical research
•	Med-PaLM	2
• ChatCAD
• XrayGPT
• Medical
benchmarks
• Expert
evaluation
•	Med-PaLM	2	reached	86.5%	accuracy	on	MedQA
(19-point	improvement	vs	Flan-PaLM)	and	physicians
preferred	its	answers	72.9%	of	the	time.
• ChatCAD improved chest-X-ray performance by
16.42 points and F1-score by 15 points.
• XrayGPT increased ROUGE-1 to 0.3213 and was
preferred	by	82%	of	users.
• Pilot • Hallucination of
medical facts
• Need for expert
oversight
[154]
[152]
[225])
Table 3	A	comparative	review	of	real-world	Large	Language	Model	applications	across	fourteen	domains,	classified	by	deployment	maturity	level

1 3
P . Peykani et al.
Industry Main Application Model / Tool Type of
Quantitative
Evidence
Quantitative Metrics and Results Maturity	Level Risks	/	Limitations Refer-
ences
Finance • Sentiment analysis
• Stock prediction
• FinGPT
• BloombergGPT
• FinBERT
• Benchmarks
• Comparison
with	financial
models
•	FinGPT	improved	stock-prediction	accuracy	by	8%.
•	BloombergGPT	achieved	an	F1-score	of	79.63	on
Equity	News	(mean	62.47)
•	FinBERT	reached	97%	accuracy	on	Financial
PhraseBank	and	86%	overall	accuracy.
• Pilot • Data bias; need
for high-quality
financial	data
[226]
[227]
Computer
Programming
• Automated code
generation
• GPT-4o
• Qwen2.5-Coder-32B
• WizardCoder-33B
• GPT-4 Turbo
• GPT-3.5
• HumanEval
benchmarks
•	Pass@1	scores:	GPT-4o	≈87.2%,
Qwen2.5-Coder-32B	≈87.2%,	GPT-4	Turbo	81.7%,
WizardCoder-33B	73.2%,	GPT-3.5	66.5%.
• Pilot • Code errors; secu-
rity concerns
•	Reliance	on	LLM
outputs
[67]
Industry • Equipment
diagnosis
• Predictive
maintenance
•	Llama-3
• GPT-4o
• Mistral
• Accuracy and
response-time
benchmarks
•	Llama-3	achieved	93.33%	accuracy	with	a	13.47	s
response
•	GPT-4o	achieved	80%	accuracy	with	a	6.03	s
response
•	Mistral	achieved	66.67%	accuracy	with	a	3.12	s
response.
• Pilot • Sensor-data
integration
• operational cost
[228]
Law •	Legal	analysis
• Bar-Exam
evaluation
• GPT-4 • Exam perfor-
mance analysis
•	Initial	reports	placed	GPT-4	near	the	90th	percentile
on the Uniform Bar Exam; later assessments placed
it	between	the	62nd	and	69th	percentile	overall,	with
42%	on	essays.
• Pilot •	Legal	liability
• Ambiguous evalu-
ation criteria
[229]
[230]
Agriculture • Crop disease and
pest management
• Farming
recommendations
•	AgriM-LLM
•	LLMI-CDP
• Agricultural
benchmarks
• Ablation
studies
•	AgriM-LLM	achieved	87.5%	disease-diagnosis
accuracy,	84.5%	pest-diagnosis	accuracy	and	a	rec-
ommendation	score	of	90.2.
•	LLMI-CDP	achieved	86.7%	and	83.8%	respectively
•	Multi-scale	features	increased	fine-grained	accuracy
from	79.5%	to	86.8%.
• Experimental •	Limited	data
coverage
• Climate sensitivity
[231]
Energy • Energy manage-
ment; smart-grid
monitoring
•	Load	forecasting
• GridGPT
• PowerGPT
• EnergyGPT
• Forecasting
benchmarks
• Anomaly-
detection
experiments
• Smart-grid
simulations
•	LLM-based	smart-grid	forecasting	systems	reduced
short-term	load-prediction	error	by	12–18%	compared
with	traditional	ML	baselines	in	incomplete-sensor
scenarios. In anomaly-detection tasks, transformer-
based energy models improved detection F1-score
from 0.81 to 0.89 while reducing fault-detection
latency	by	approximately	22%.	Recent	smart-grid
simulations	also	reported	up	to	15%	improvement	in
demand-response	optimization	efficiency	and	more
stable forecasting under noisy sensor conditions.
• Experimental •	Limited	domain-
specific	datasets
• Reliability and
real-time deploy-
ment challenges;
infrastructure
sensitivity
[232]
[233]
Network and
Telecommunications
• Network
troubleshooting
• Customer support
•	TSLAM-Mini	(3.8
B)
• Telecom-spe-
cific	evaluation
• Token-level
accuracy
•	TSLAM-Mini	achieved	a	mean	token	accuracy	of
0.9679	and	outperformed	general	LLMs	on	routing,
security and energy-management tasks.
• Experimental • Scalability
challenges
• Network
confidentiality
[234]
Table 3	(continued)

1 3
The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,…
based	on	specialized	fine-tuning	[242, 243]. However, this
approach requires careful control, as low-quality synthetic
data can introduce noise and incorrect information into the
training process.
Another	contribution	of	LLMs	to	machine	learning	is	the
redefinition	of	the	transfer	learning	approach.	Models	such
as	GPT,	LLaMA,	and	Gemini	transfer	knowledge	learned
in one domain to others without the need for large datasets
through techniques like Embedding Adaptation and Con -
text Adjustment [244]. This capability reduces the need for
retraining and prevents the phenomenon of catastrophic for-
getting, a feature that holds particular importance in sensi -
tive	fields	such	as	finance	and	medicine,	which	are	examined
in Sects. 4.8 and 4.7 [154, 245].
In	the	field	of	fine-tuning	and	optimization,	LLMs	have
introduced	 more	 efficient	 approaches	 compared	 to	 full-
parameter	fine-tuning.	Methods	such	as	LoRA,	which	only
updates low-rank matrices [ 52],	Prefix	Tuning,	which	adds
learnable	prefixes	to	attention	layers	[246], and Instruction
Tuning, which aligns the model with human instructions
[54], all achieve competitive results by updating a limited
number of parameters. Model compression and quantiza -
tion	have	also	enabled	the	deployment	of	LLMs	in	resource-
constrained environments by reducing computational costs
[247]. Alongside these, Prompt Engineering has emerged as
a complementary optimization approach that improves out-
put accuracy across various tasks without modifying model
parameters [ 248], providing reliable results even in low-
data environments [249].
However,	the	adoption	of	LLMs	in	machine	learning
faces serious methodological challenges. First, the non-
deterministic	nature	of	LLMs,	which	produces	different	out-
puts for the same input makes reproducible evaluation and
fair	comparison	with	baselines	difficult	[54]. Second, there
is an unresolved debate in the research literature regarding
whether the performance improvements observed through
LLM-generated	synthetic	data	stem	from	genuine	data	diver-
sity or merely shift the training data distribution toward the
generative model’s outputs, a question that directly impacts
the	validity	of	LLM-based	data	augmentation	approaches
[242].	Third,	the	high	computational	costs	of	LLMs,	even
with	efficient	methods	such	as	LoRA,	remain	a	primary	bar-
rier to deployment in machine learning systems with limited
resources [247].
5.3 Generative AI
Generative	Artificial	Intelligence	(Generative	AI)	is	one	of
the	primary	branches	of	AI	in	which	LLMs	have	played	a
pivotal role. Unlike discriminative approaches that merely
Fig. 6	The	role	of	LLMs	in	the	6	subfield	of	artificial	intelligence

1 3
P . Peykani et al.
classify existing data, generative models are capable of pro-
ducing new content including text, images, audio, and code
[250].	LLMs	such	as	ChatGPT,	built	upon	the	Transformer
architecture [16], have mastered large-scale statistical pat -
terns of language, gaining the ability to generate content
whose quality is often competitive with human output,
a leap whose theoretical roots trace back to fundamental
questions regarding the cognitive abilities of machines.
In	the	field	of	text	generation,	LLMs	produce	coherent
and precise content in diverse writing styles to the extent
that it is often indistinguishable from human text [ 3]. This
capability has provided a foundation for widespread appli -
cations	in	fields	such	as	media	and	creative	content	produc-
tion	(Sect.	4.6)	and	software	development	(Sect.	4.9)	[67,
251]. In the domain of image generation, technologies such
as	 Generative	Adversarial	 Networks	 (GANs)	 [252] and
tools	like	DALL-E	2	and	Stable	Diffusion	have	enabled
text-to-image conversion [253].	Text-to-speech	(TTS)	mod-
els, using tools such as Play.ht and Murf.AI, also produce
natural and diverse voices that have found extensive use in
podcasts and audiobooks [ 254]. Beyond content creation,
LLMs	provide	creative	suggestions	by	analyzing	complex
data, enriching brainstorming sessions and strategic deci -
sion-making in organizational environments [255, 256].
However,	the	advancements	of	LLMs	in	Generative	AI
are accompanied by serious methodological challenges.
Distinguishing	LLM-generated	content	from	human-gen-
erated	content,	particularly	in	scientific	texts,	has	currently
become an unresolved debate; existing detection tools such
as	GPTZero	have	significant	error	rates,	and	their	reliability
in real-world environments is questionable [ 250]. Further-
more,	image	generation	models	such	as	Stable	Diffusion
have	a	well-known	record	of	reflecting	biases	latent	in	their
training	data.	This	issue	raises	significant	challenges	regard-
ing the methods of oversight and the level of accountability
in the development of these tools [ 257]. Additionally, the
evaluation of generative output quality still lacks standard -
ized and universally applicable metrics; metrics such as
BLEU	and	FID	only	measure	limited	aspects	of	perceptual
quality [254].
5.4 Recommender Systems
With the rapid growth of e-commerce and the explosion
of user data, recommender systems have become essential
tools for reducing information overload and enhancing user
experience [ 258]. Previous deep neural network models
captured user-item interactions but were incapable of under-
standing subtle preferences and adapting to new contexts
[259].	LLMs,	by	leveraging	their	superior	capabilities	in
natural language understanding, zero-/few-shot learning,
and multi-step reasoning, have enabled the extraction of
insights from diverse textual data such as reviews, descrip -
tions, and feedback [ 260], an approach from which tradi -
tional	 collaborative	 filtering-based	 models,	 due	 to	 their
reliance on structured historical data, were excluded [261].
In	 product	 recommendations,	 LLMs	 analyze	 textual
content such as product descriptions and user reviews to
improve the online shopping experience, an application
also discussed in Sect. 4.3 Even with limited historical data,
zero-/few-shot learning provides accurate personalized rec-
ommendations [262, 263]. Fine-tuning through prompt tun-
ing	and	model	fine-tuning	aligns	models	with	e-commerce
data [264], and models like ChatGPT increase user trans -
parency and trust by generating textual descriptions for rec-
ommendations [ 265]. In digital content recommendation,
LLMs	analyze	texts	and	user	feedback	to	provide	relevant
suggestions in the domains of news, movies, and music
[266], addressing the challenge of historical data scarcity by
extracting semantic features [ 267]. Models such as NRMS
[268], Tiny NewsRec [ 269], and PREC [ 270], along with
benchmark	datasets	like	MovieLens	[271] and Douban [13],
are	notable	examples	of	these	advancements.	LLM-based
conversational	recommender	systems,	through	fine-tuning,
prompt tuning, and in-context learning, enable dynamic,
multi-turn conversations with users. Advanced systems
like ChatREC [272], RAH [273],	BiLLP	[274], and InteR-
ecAgent [ 161] combine conversational capabilities with
databases	and	retrieval	systems	to	offer	precise	and	context-
aware recommendations.
However,	the	practical	deployment	of	LLMs	in	recom-
mender systems faces serious methodological challenges
that are often overlooked in the research literature. The most
significant	of	these	is	the	latency	issue	in	real-time	envi-
ronments: large autoregressive models require hundreds
of milliseconds to generate each token, whereas industrial
recommender systems on platforms like Amazon and Net -
flix	must	generate	responses	in	less	than	ten	milliseconds
[275],	a	gap	that	makes	the	direct	deployment	of	LLMs	in
the real-time ranking layer practically impossible. Existing
approaches to bridge this gap, including caching, model dis-
tillation,	and	using	LLMs	solely	in	the	pre-ranking	stage,
each	have	their	own	accuracy-latency	trade-offs	for	which
a theoretical consensus has not yet been reached [ 276].
Furthermore, common evaluation metrics such as NDCG
and Hit Rate do not adequately measure the quality of the
actual user experience, including diversity, exploration, and
long-term satisfaction [277]. Additionally, the superior per-
formance	of	LLMs	in	zero-shot	recommendation	has	been
primarily demonstrated on standard datasets such as Mov -
ieLens	and	Douban,	whose	distributions	differ	significantly
from real-world industrial environments, an unresolved
question that calls the generalizability of these results into
question [271].

1 3
The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,…
5.5 Computer Vision
The	integration	of	LLMs	with	computer	vision	is	one	of	the
most transformative recent advancements in multimodal AI.
The core mechanism of this integration is based on align -
ing	visual	encoders	with	pre-trained	LLMs:	visual	encoders
convert	images	into	continuous	representations	that	LLMs
can interpret, and this is achieved without the need for
costly joint training [278, 279].	The	CLIP	model,	by	align-
ing image and text spaces through large-scale contrastive
learning [34], provided a foundation for most modern mul -
timodal	systems,	while	approaches	like	LENS,	by	directly
combining	the	outputs	of	visual	modules	with	LLMs,	fur-
ther reduce computational costs [280].
One	of	the	most	significant	applications	is	image	cap-
tioning, where the combination of linguistic and visual
capabilities generates more accurate and contextually rich
descriptions [281]. The PROMPTCAP method directs the
model’s attention to prominent details [282], and integrating
object detection and text recognition models enhances out -
put consistency [283]; these advancements improve perfor-
mance	on	the	CLIPScore	metric	and	tasks	such	as	WebQA
[284].	In	object	detection,	LLMs	have	redefined	this	task
as a language problem: bounding box coordinates and class
labels are converted into token sequences and processed by
an	LLM	[285]. The Pix2Seq model competes with tradi -
tional methods like Faster R-CNN and DETR without the
need for specialized architectures [259], and hybrid designs
such as ContextDET, which combine visual encoders with
LLMs,	demonstrate	strong	results	in	open-vocabulary	sce-
narios [286].	In	image	classification,	LLMs	convert	visual
data into semantic textual descriptions suitable for down -
stream	classifiers	[287];	methods	such	as	Classification	by
Description generate hierarchical textual representations
that	refine	decision	boundaries	[288], an approach that has
provided	significant	accuracy	in	specialized	applications
such as satellite image processing and medical imaging,
which are examined in Sects. 4.12 and 4.7 [289].
However,	the	integration	of	LLMs	with	computer	vision
faces serious methodological challenges that limit its wide-
spread adoption. Visual hallucination, where the model
describes objects or relationships that do not exist in the
image, is a well-known and unresolved failure mode in mul-
timodal systems; even advanced models such as GPT-4 V
suffer	from	systematic	errors	in	simple	spatial	reasoning
tasks [ 283]. The next challenge is the evaluation of mul -
timodal system performance, which continues to rely on
inadequate	metrics;	CLIPScore	and	similar	metrics	do	not
measure true perceptual quality, and the results of standard
benchmarks	often	differ	significantly	from	performance	in
real-world environments [281]. Third, an unresolved debate
is	whether	LLMs	truly	possess	deep	visual	understanding	or
merely extract statistical patterns between text and images
from large training datasets, a question that directly impacts
the reliability of these systems in critical applications such
as medical diagnosis.
5.6 Robotics
The	integration	of	LLMs	into	robotics	is	one	of	the	most
challenging yet promising applications of these models
in	artificial	intelligence,	as	robotics,	unlike	purely	textual
domains, requires real-time interaction with the physi -
cal	world.	Leveraging	natural	language	understanding	and
complex	reasoning,	LLMs	target	two	fundamental	gaps	in
traditional robotics: the inability to understand ambiguous
linguistic instructions and the limitation in generalizing to
new tasks without retraining [290].
The	most	significant	advancement	is	in	human-robot
interaction. In a study by Zhang et al. [ 291],	the	CLEAR
system	achieved	a	97%	success	rate	in	controlling	tasks
through	natural	conversational	interaction,	a	figure	that	rep-
resents	a	significant	qualitative	leap	compared	to	systems
based	on	predefined	commands.	In	translating	linguistic
instructions into executable actions, the SayCan frame -
work, by integrating language models with reinforcement
value	functions,	achieved	an	84%	success	rate	in	planning
and	74%	in	execution	across	over	a	hundred	real-world
tasks [292]. SayPlan has made planning scalable in complex
environments by utilizing 3D scene graphs [293],	and	LLM-
Planner has demonstrated remarkable adaptability in both
simulated and real-world environments with limited data
[294].	In	multimodal	integration,	the	PaLM-E	model	com-
bines textual and visual data to improve task performance
[295], and synthetic data generation systems such as ROSIE
and CAPE have doubled training success rates by simulat -
ing experiences and providing corrective feedback [ 296].
Structured prompting approaches like ProgPrompt improve
problem-solving accuracy [ 181], and Code-as-Policies
enables the direct generation of control code for robots [73].
Beyond	single-agent	systems,	LLMs	have	enhanced	multi-
robot coordination through task allocation optimization and
collaborative planning [68, 297], a capability that holds par-
ticular	importance	in	the	fields	of	industrial	automation	and
crisis management, examined in Sect. 4.1.
However,	the	deployment	of	LLMs	in	robotics	faces	seri-
ous methodological challenges that limit their widespread
adoption. The sim-to-real gap remains a fundamental fail -
ure mode; models that perform robustly in simulated envi -
ronments	often	suffer	from	a	sharp	decline	in	performance
when encountering physical world uncertainties such as
variable lighting, unfamiliar objects, and sensor noise
[294].	Another	challenge	is	that	autoregressive	LLMs,	due
to their inherent latency in token generation, are not directly

1 3
P . Peykani et al.
suitable for real-time robotic control, which requires mil -
lisecond-level responses. Existing frameworks bypass this
issue	by	decoupling	the	high-level	planning	layer	(handled
by	the	LLM)	from	the	low-level	control	layer	(handled	by
classical	controllers),	but	this	hybrid	architecture	itself	cre-
ates new coordination challenges [73]. Furthermore, there is
an	unresolved	debate	in	this	field	regarding	whether	LLMs
possess true spatial and physical reasoning abilities or
merely reproduce language patterns associated with space,
a question that directly impacts the reliability of these sys -
tems in critical environments such as surgical robotics and
crisis management [293].
Table 4	summarizes	the	applications	of	LLMs	across	the
six	major	subfields	of	artificial	intelligence	examined	in	this
section.	For	each	subfield,	the	table	identifies	the	primary
LLM	mechanism,	representative	systems,	the	most	critical
failure mode, the key evaluation challenge, and the central
unresolved debate in the current research literature.
As shown in Table 4,	although	LLMs	have	introduced
transformative	mechanisms	across	all	six	major	subfields
of	artificial	intelligence,	a	common	pattern	emerges:	bench-
mark performance does not necessarily translate into readi-
ness for real-world deployment. Importantly, several of the
identified	failure	modes	across	different	subfields	share	a
common structural origin: the gap between controlled eval-
uation environments and the complexity of real-world con -
ditions.	Visual	hallucination	in	computer	vision	(Sect.	5.5),
the	sim-to-real	gap	in	robotics	(Sect.	5.6),	and	latency	con-
straints	in	recommender	systems	(Sect.	5.4)	are	all	manifes-
tations of this broader tension, rather than isolated technical
shortcomings.	Nevertheless,	these	subfield-specific	limita-
tions represent only one dimension of the challenges fac -
ing	Large	Language	Models.	The	next	section	addresses	the
broader	and	more	general	challenges	associated	with	LLMs.
Moreover, the unresolved debates presented in Table 4
reveal a deeper epistemological concern that overshadows
all	six	subfields:	do	Large	Language	Models	genuinely	pos-
sess cognitive capabilities such as language understanding,
visual reasoning, or spatial inference or is their impressive
performance	merely	a	reflection	of	sophisticated	statistical
pattern matching over large-scale training data? This ques -
tion is not merely a philosophical debate; it carries direct
implications for the reliability, interpretability, and account-
ability	of	LLM-based	systems	in	high-stakes	domains	such
as healthcare, law, and autonomous robotics, as discussed
in Sect. 4.
Table 4	Summary	of	large	language	model	applications	across	artificial	intelligence	subfields:	key	mechanisms,	representative	systems,	and
methodological limitations
Subfield Key	LLM	mechanism Representative model
/ system
Primary failure mode Evaluation challenge Unsettled debate
NLP • Prompt-based
learning
• Self-supervised
pre-training
• Chain-of-Thought
reasoning
• GPT-4
• BERT
• In-Context learning
models
•	Significant	perfor-
mance drops on low-
resource languages and
out-of-distribution data
•	BLEU	and	F1	fail
to capture discourse
coherence and factual
accuracy
•	Do	LLMs	genuinely	under-
stand language or merely
reproduce statistical patterns?
Machine
Learning
• Transfer learning
•	LoRA
• Instruction Tuning
• Prompt Engineering
• GPT
•	LLaMA
• Gemini
• Non-deterministic
outputs identical inputs
may yield inconsistent
results
• Reproducible evalu-
ation and fair baseline
comparison remain
difficult
• Does synthetic data augmen-
tation	reflect	genuine	diversity
or merely shifts distribution
toward the generative model?
Genera-
tive AI
• Generative modeling
• Transformer
architecture
• Contrastive learning
• ChatGPT
•	DALL-E	2
•	Stable	Diffusion
• Reproduction of
gender and ethnic biases
present in training data
•	BLEU	and	FID	cap-
ture only limited aspects
of perceptual quality
• No universally accepted
standard metric for evaluating
generative content quality
Recom-
mender
Systems
• Zero-/few-shot
learning,	fine-tuning,
in-context learning
• ChatREC
• RAH
•	BiLLP
• InteRecAgent
• Critical latency
autoregressive models
cannot meet sub-10 ms
real-time constraints
• NDCG and Hit Rate
do not capture diversity,
serendipity, or long-
term user satisfaction
• Does benchmark superior-
ity generalize to real-world
industrial deployment
environments?
Com-
puter
Vision
•	Visual	encoder–LLM
alignment
• Contrastive learning
•	CLIP
• Pix2Seq
• ContextDET
• Visual ChatGPT
• Visual hallucination
describing objects or
relations absent from the
image
•	CLIPScore	does	not
adequately measure true
perceptual quality
•	Do	LLMs	possess	genu-
ine visual understanding
or extract statistical co-
occurrences between text and
image?
Robotics • Instruction-to-action
translation
• Multimodal fusion
• Code-as-Policies
•	SayCan	(84%
planning)
• SayPlan
•	PaLM-E
•	CLEAR	(97%	task
success)
• Sim-to-real gap sharp
performance degradation
under physical-world
uncertainty
•	Hybrid	LLM	+	classi-
cal controller architec-
tures introduce new
coordination challenges
•	Do	LLMs	possess	genuine
spatial and physical reasoning
or reproduce language pat-
terns associated with space?

1 3
The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,…
6 Challenges of Large Language Models
Despite the remarkable advances large language models
have made in natural language processing and problem-solv-
ing, this technology faces a range of structural challenges
that have drawn serious attention from both researchers
and industry practitioners. What sets these challenges apart
from ordinary technical limitations is the degree to which
they are deeply intertwined such that addressing any one of
them often introduces new tensions in another. The follow-
ing sections examine these challenges across six principal
dimensions.
6.1 Hallucination and Reliability
The most critical challenge facing large language models in
real-world	deployment	is	their	tendency	to	generate	fluent
and convincing content that has no factual basis, a phenom-
enon	widely	referred	to	in	the	scientific	literature	as	hal-
lucination. This problem carries serious consequences in
high-stakes domains such as medicine, law, and engineering,
where accuracy is a requirement rather than a preference.
Models such as ChatGPT, for instance, have been known to
produce misleading explanations in medical diagnosis while
proposing incorrect formulas in engineering contexts [298].
In response to this challenge, RAG has emerged as the
dominant hallucination mitigation strategy in industry. As
discussed in Sect. 3.4, RAG supplements the model’s static
knowledge by dynamically retrieving information from
external knowledge bases [58]. A critical analysis, however,
reveals that RAG does not fully resolve the hallucination
problem. The root of this limitation lies in the very nature of
the architecture itself: RAG assumes that accurate informa-
tion exists within the knowledge base and can be success -
fully retrieved, an assumption that frequently breaks down
in specialized domains and in the presence of tacit knowl -
edge. Zhang et al. [ 299], in a systematic review, highlight
that hallucination in RAG systems stems from two distinct
sources: retrieval failure encompassing malformed queries,
low-quality data sources, and inadequate retrieval strate -
gies,	and	generation	deficiency,	including	context	conflict,
the	lost-in-the-middle	effect,	and	inherent	model	capability
constraints. Critically, when retrieved sources contain inac-
curate or biased data, a RAG system can amplify hallucina-
tion rather than reduce it.
6.2 Computational Cost, Inference Latency, and
Environmental Sustainability
The computational cost of large language models is not a
straightforward technical limitation; it is a structural ten -
sion operating simultaneously across three levels: training,
inference, and deployment. Models such as GPT-4, with
their trillions of parameters, demand enormous memory and
processing resources for both training and inference, and
fine-tuning	them	for	specialized	applications	is	prohibitively
expensive.	Techniques	such	as	LoRA	and	QLoRA	have	alle-
viated this burden to some degree [ 117], yet the core prob -
lem lies not in training but in inference. The autoregressive
generation process, which produces each token sequentially,
creates a fundamental bottleneck: as model size scales to
hundreds of billions of parameters, inference becomes a dis-
tributed systems challenge requiring specialized hardware
integration, network scheduling, and complex resource
management [300]. The daily inference costs of platforms
such as ChatGPT are substantial, and this alone speaks to
the true scale of the challenge.
This latency problem takes on a particular dimension
in recommender systems. Although these models dem -
onstrate impressive zero-shot and few-shot performance,
their deployment in commercial environments runs into
a fundamental barrier: production recommender systems
require responses within milliseconds, while the autoregres-
sive process demands multiple sequential calls that push
response times to unacceptable levels [ 301]. Crucially, this
gap cannot be closed through model optimization alone; it
is rooted in the nature of the Transformer architecture itself,
which was designed for output quality rather than inference
speed	under	high-traffic	conditions.	This	same	factor	has
given rise to a growing and often underappreciated con -
cern regarding the environmental footprint of these mod -
els. ChatGPT’s daily electricity consumption now exceeds
half a million kilowatt-hours, equivalent to the energy usage
of 180,000 American households and each conversation
consumes approximately half a liter of water [ 287, 302].
Peykani et al. [ 214], emphasize that the bulk of this con -
sumption occurs at the inference stage, meaning that as gen-
erative AI applications continue to proliferate, this footprint
grows linearly. The central tension is this: latency reduction
strategies	such	as	GPU	over-provisioning	directly	conflict
with environmental sustainability goals, and optimizing for
both simultaneously remains an unsolved technical chal -
lenge [303].
6.3 Data Limitations, Context Capacity, and Input
Quality Dependency
The data access challenge in large language models has two
distinct	dimensions	that	are	frequently	conflated:	the	quanti-
tative scarcity of specialized data, and the qualitative inade-
quacy of available data. Most of these models are trained on
general-purpose sources, whereas specialized domains from
medicine	and	law	to	engineering	require	domain-specific
data	that	is	often	sensitive,	fragmented,	and	legally	difficult

1 3
P . Peykani et al.
to share. This limitation is not merely quantitative; even as
training	data	volume	increases,	if	that	data	fails	to	reflect	the
genuine diversity of a given domain, the model develops
latent biases that remain concealed within ostensibly rea -
sonable outputs [91].
The complexity of this challenge becomes fully appar -
ent when combined with the problem of context capac -
ity. Although the context windows of recent models have
reached into the millions of tokens, Gemini 1.5 Pro, for
instance, supports up to 2 million tokens this quantitative
expansion does not translate into genuine improvement in
long-context comprehension. High-quality long-context
data is exceedingly scarce in real-world settings, and syn -
thetic data generation methods employed to compensate
for this shortage face their own hurdles, including the time-
consuming demands of continual training and inherent dis -
tributional biases [304]. Beyond this, expanding the context
window creates a direct tension with the computational
challenges outlined in Sect. 6.2, as longer contexts exac -
erbate memory and compute bottlenecks within the Trans -
former architecture to the point where the KV cache of a
model operating with a 128,000-token context can reach 64
gigabytes [305].
Perhaps one of the least appreciated dimensions of this
challenge, however, is the models’ pronounced sensitivity to
input quality and format. Minor variations in how a prompt
is phrased without any change in semantic content can lead
to	substantial	fluctuations	in	model	performance	[306]. This
sensitivity to the ordering and presentation of information
is a serious concern in high-stakes decision-making sys -
tems: if rearranging medical documents in the input alters
the model’s summary, can a physician reasonably trust its
output? This question makes clear that the data quality chal-
lenge is not purely a technical matter; it is deeply connected
to the reliability concerns raised in Sect. 6.1.
6.4 Bias, Ethics, and the Accountability Gap
Bias in large language models is not a random error; it is a
structural feature. These models learn patterns embedded in
their training data, and human-generated data is deeply sat-
urated with historical discrimination, cultural stereotypes,
and	unequal	representation	across	different	groups.	Gal-
legos et al. [ 307], in a comprehensive review, demonstrate
that these biases are encoded in the deep layers of the model
and cannot be remedied through surface-level techniques
such	as	output	filtering	or	prompt	rewriting.	What	makes
this particularly troubling is that current bias evaluation
methods such as WEAT and StereoSet rely on static bench-
marks that are ill-equipped to detect context-dependent and
decision-oriented biases [ 308]. In other words, not only
does the bias exist, but the tools we use to measure it are
themselves inadequate, meaning we do not yet know how
deep the problem truly runs.
The complexity of this challenge becomes even more pro-
nounced when combined with the black-box nature of these
models. Determining whether responsibility for harmful or
inaccurate outputs lies with the developer, the deployer, or
the	end	user	remains	without	a	definitive	answer,	a	problem
that takes on serious dimensions in medical and legal sys -
tems [309].	The	lack	of	explainability	is	the	first	barrier	that
both industry and regulators must clear in order to mean -
ingfully reduce these risks. Yet while the EU AI Act has
established explainability as a foundational principle, the
precise techniques and requirements of XAI remain in the
process	of	being	defined,	and	fully	operational	implementa-
tion standards are unlikely to materialize in the near future
[310, 311]. The root of this enforcement gap lies in the pace
of technological development, which has far outstripped the
capacity of regulatory bodies to understand and govern it.
Data privacy and ownership represent yet another dimen-
sion of this same tension. These models are frequently
trained on vast datasets that have not always been collected
with the explicit consent of users, a reality that has sparked
serious legal and regulatory debate at the global level [312].
This challenge connects directly to the issue of linguistic
inequality discussed in Sect. 6.5, as the groups least repre -
sented in training data are typically the same groups with
the least power to shape the frameworks that govern it.
6.5 Linguistic and Cultural Inequality
Linguistic	inequality	in	large	language	models	stems	from
a simple yet consequential reality: pre-training data is over-
whelmingly English-centric. Reports indicate that non-Eng-
lish	data	accounts	for	only	around	5%	of	the	training	corpus
in	models	such	as	LLaMA	3,	and	as	models	scale	up,	the
relative share of non-English data does not grow, it shrinks
[313]. The direct consequence of this imbalance is measur -
able performance gaps: recent research has documented a
13.8	to	16.7%	point	disparity	between	model	performance
in English and in low-resource languages, and notably,
larger multilingual models do not necessarily close this gap
[314].
This challenge is not purely technical; it carries profound
cultural dimensions as well. Models trained predominantly
on Western content embed implicit cultural biases that sur -
face in their handling of idiomatic expressions, cultural ref-
erences, and the social contexts of low-resource languages
[315]. This problem recurs at the evaluation level: the vast
majority of existing benchmarks are English-centric, and
the absence of reliable assessment tools for low-resource
languages	makes	it	difficult	to	identify	and	accurately	mea-
sure these gaps [ 316]. In other words, not only do models

1 3
The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,…
perform more poorly in these languages, but we lack the tools
to precisely quantify the extent of that underperformance.
Advances such as Glot500 trained across 511 languages
[317]	and	MaLA-500,	covering	534	languages	[318], repre-
sent genuine steps toward linguistic equity. Yet as the con -
nection between this challenge and the bias discussion in
Sect. 6.4 makes clear, the roots of this inequality lie in the
unequal global distribution of training resources and knowl-
edge production capacity, a reality that cannot be resolved
through technical optimization alone, without deliberate
intervention in research policy and funding.
A review of the challenges discussed in this section
reveals that these problems are not independent; they are
bound together in a network of cross-cutting interdependen-
cies. The most critical challenge from a real-world deploy -
ment standpoint is hallucination: not merely because of how
frequently it occurs, but because the dominant mitigation
strategy	(RAG)	carries	serious	structural	limitations	of	its
own that can, in high-stakes domains, exacerbate rather
than resolve the problem. Along the same lines, inference
latency carries the highest operational urgency, as it directly
obstructs	 real-world	 deployment	 in	 high-traffic	 environ-
ments including recommender systems and clinical decision
support, while the available solutions for reducing it, such
as	resource	over-provisioning,	stand	in	direct	conflict	with
environmental sustainability goals.
At a deeper level, bias and linguistic inequality are two
distinct expressions of a single underlying problem: the
unequal distribution of data and power in the model devel -
opment	process.	This	connection	matters,	because	efforts
to	 address	 bias	 through	 continual	 fine-tuning	 increase
computational overhead and, as a result, make access to
this technology harder for the very groups most harmed by
that bias, a vicious cycle that cannot be broken through one-
dimensional solutions. Finally, the challenge of data qual -
ity and input sensitivity makes clear that model reliability
depends not only on architecture, but on the quality of the
entire data pipeline, from collection through retrieval. A
concise overview of these challenges, the currently domi -
nant mitigation strategies, and the fundamental limitations
of each is presented in Table 5. Understanding these cross-
cutting interdependencies is a prerequisite for designing
effective	research	directions,	which	are	elaborated	in	Sect.
7.
7 Future Research Prospects in the
Applications of LLMs
The	pace	of	transformation	in	the	field	of	LLMs	is	such	that
the gap between what is considered advanced today and
what will be considered baseline tomorrow is remarkably
narrow. Yet this very acceleration brings a serious concern
into sharp relief: many of the fundamental challenges inher-
ent to this technology remain unresolved. Precisely identify-
ing	these	challenges	and	translating	them	into	well-defined
research questions is not only essential for guiding future
inquiry, but also critically important for the responsible
deployment of this technology in high-stakes domains. This
section	examines	five	research	directions	that	have	increas-
ingly	captured	the	attention	of	the	scientific	community	in
recent years: agentic and multimodal systems, long-term
memory and extended context processing, computational
efficiency	and	environmental	sustainability,	human-AI	col-
laborative	reasoning,	and	finally,	reliability	and	dynamic
evaluation.
7.1 Agentic, Multimodal, and Embodied Systems
The shift from reactive language models to agentic systems
has	been	one	of	the	most	pivotal	developments	in	this	field
in recent years. Unlike conventional applications that rely
on static prompting, these systems can decompose com -
plex tasks, leverage external tools, and coordinate with
one another in multi-agent environments [ 319, 320]. Yet a
significant	research	gap	persists:	studies	indicate	that	LLM-
based	agents	in	long-horizon	tasks	consistently	suffer	from
cascading error propagation, errors that appear minor in
early stages but compound into systematic failures as the
process unfolds [ 321].	This	reality	raises	a	well-defined
research question: what architectures can guarantee reason-
ing coherence and goal alignment across extended decision-
making processes, without relying on continuous human
Table 5 Main challenges of large language models, dominant current
solutions, and their limitations
Challenge Main Solution Common
Workaround
Hallucination • Failure in retrieval and
conflict	between	parametric
and retrieved knowledge
• Retrieval-Aug-
mented Genera-
tion	(RAG)
Inference	Latency • Degradation of reasoning
capabilities in compressed
models
• Quantization
/ Knowledge
Distillation
Context Window
Limitation
•	Lack	of	long-term	back-
ground quality in real-world
environments
• Memory-
augmented
architecture
(MemoRAG)
Bias and
Unfairness
•	Lack	of	tools	for	targeted
bias detection and ability to
identify context-based biases
•	RLHF	/
Fine-tuning
Language
Inequality
• Performance gap of
13–17%	in	low-resource
languages, even at scale
• Multilingual
large-scale
models
Environmental
Cost
•	Conflict	between	over-
provisioning resources and
latency reduction
• Inference
optimization and
energy consump-
tion reduction

1 3
P . Peykani et al.
oversight? Abou Ali et al. [ 322] argue that the answer lies
not in choosing between symbolic and neural architectures,
but in developing context-sensitive hybrid frameworks
capable of shifting their paradigm depending on the sensi -
tivity of the domain, from clinical settings to data-driven
environments.
A similar challenge exists at the level of physical percep-
tion: when language is processed in isolation from sensory
experience, the same error accumulation occurs but at a
deeper	layer.	Vision-Language-Action	(VLA)	systems	have
succeeded in closing the perception-reasoning-action loop
in robotics, yet genuine grounding in the physical world
remains out of reach; these models continue to treat lan -
guage as a separate processing layer rather than as an intrin-
sic component of sensory understanding [ 323]. Cong and
Mo [324] emphasize that the scarcity of multimodal training
data in real-world environments relative to the abundance of
text-only data stands as one of the primary obstacles along
this path. The central question, therefore, is how to design a
model that processes language, vision, and action in parallel
rather than sequentially. Finding an answer to this question
carries fundamental importance not only for robotics, but
for any application that demands intelligent interaction with
the physical world.
7.2 Long-Term Memory and Extended Context
Processing
Despite the remarkable expansion of context windows in
large language models now exceeding 128,000 tokens in
some cases, this quantitative progress does not translate into
a genuine capacity for understanding long-form contexts.
Liu	et	al.	[325]	have	demonstrated	that	these	models	suffer
from a U-shaped positional bias: performance degrades sig-
nificantly	when	critical	information	is	located	in	the	middle
of a passage rather than at its beginning or end. This “lost in
the	middle”	phenomenon	exposes	a	well-defined	research
gap: does extending context length, absent a fundamental
redesign of attention mechanisms, actually lead to meaning-
ful improvements in comprehension?
In response to this challenge, memory-augmented
approaches have attracted considerable attention. The Mem-
oRAG framework, introduced at ACM Web 2025, employs
a dual architecture that combines a lightweight model for
forming global memory with a more powerful model for
generating	the	final	response	[326]. This approach partially
addresses the limitations of traditional RAG discussed
in Sect. 6.1, which depends on explicit queries and struc -
tured knowledge, yet a more fundamental question remains
open: how can one design a memory system that not only
retrieves information, but also updates it over time, selec -
tively forgets, and adapts as context evolves? The answer
to this question will shape the trajectory of future research
in long-horizon dialogue systems, legal document analysis,
and clinical decision support.
7.3 Efficient, Domain-Specific Models and Green AI
The scaling of large language models has come at a steep
price not only computationally, but environmentally as
well. The data centers that underpin these models account
for	a	significant	share	of	global	greenhouse	gas	emissions,
a share that continues to grow as generative AI applications
become more widespread [ 214]. This reality has prompted
a	fundamental	question	among	researchers	in	the	field:	is	it
possible	to	build	a	model	that	is	simultaneously	more	effi-
cient, more specialized, and more sustainable?
As discussed in Sect. 6, model compression techniques
including quantization, pruning, and knowledge distilla -
tion have become one of the most active areas of recent
research. Zhu et al. [327], in a comprehensive review, dem-
onstrate that these methods can substantially reduce both
model size and inference costs, yet one research question
remains unanswered: how far can a model be compressed
before its reasoning capabilities begin to deteriorate? This
challenge	is	particularly	acute	in	domain-specific	models
such as those designed for medicine, law, or engineering,
where accuracy is a requirement, not a preference. Future
research must therefore focus on developing frameworks
that	strike	a	balance	between	computational	efficiency	and
the preservation of specialized knowledge, especially under
conditions	where	domain-specific	data	is	limited	and	often
sensitive.	Beyond	this,	Liu	et	al.	[328] argue that Green AI
is not merely an ethical aspiration but a practical necessity:
without meaningful reductions in energy footprint, democ -
ratizing access to advanced AI, particularly in developing
countries will remain little more than an ambition.
7.4 Human-AI Collaborative Reasoning
The capacity of large language models to support human
decision-making is among the most promising applications
of this technology, yet this very capability carries with it a
serious research paradox. Passerini et al. [ 329] argue that
what is today called human-AI collaboration is, in many
cases, little more than one-directional delegation: the human
asks, the model answers, and no genuine joint reasoning
ever takes shape. This gap between apparent collaboration
and complementary collaboration in which humans and AI
mutually compensate for each other’s weaknesses raises
a	well-defined	research	question:	how	can	interfaces	be
designed that augment human reasoning rather than replace
it?

1 3
The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,…
Excessive reliance on model outputs, a phenomenon
known as automation bias, has been increasingly docu -
mented in high-stakes domains such as medicine and law
[330]. A study presented at CHI 2025 found that knowledge
workers who regularly use generative AI tools self-report a
decline	in	their	own	cognitive	effort,	a	finding	that	serves
as a serious warning against the uncritical adoption of these
tools in education and professional decision-making. Future
research must therefore not only focus on developing more
effective	interaction	frameworks,	but	also	on	defining	met-
rics for measuring genuine complementarity in human-AI
teams, metrics that look beyond output accuracy to the qual-
ity of the shared reasoning process itself [331].
7.5 Reliability, Dynamic Evaluation, and Adaptive
Benchmarks
One	of	the	most	pressing	research	gaps	in	the	field	of	large
language models is the disconnect between their impressive
performance on standard benchmarks and their unexpected
failures in real-world settings. This gap is largely rooted in
two	structural	problems:	first,	the	phenomenon	of	halluci-
nation,	the	generation	of	fluent	and	convincing	information
that is simply not true; and second, evaluation data contami-
nation, which allows models to post strong numbers on tests
they	have	effectively	seen	before.	Rahman	et	al.	[332], in a
systematic review, demonstrate that existing frameworks for
assessing	model	factuality	still	lack	coherence:	definitions
of hallucination, detection methods, and mitigation criteria
vary from one study to the next, and this inconsistency ren-
ders meaningful cross-study comparison nearly impossible.
Beyond this, static benchmarks have themselves become
part of the problem. Chen et al. [333],	presented	at	EMNLP,
show that due to their public availability, these benchmarks
gradually	find	their	way	into	model	training	data,	funda-
mentally undermining the validity of evaluation. The central
research question therefore becomes: what criteria should
distinguish a genuinely dynamic benchmark from a merely
redesigned static one, and how can evaluation in high-stakes
domains such as medicine and law be standardized in a way
that remains simultaneously sensitive to domain expertise
and real-world conditions? Answering this question is a pre-
requisite for any credible claim about the true reliability of
large language models.
8 Conclusions
LLMs	are	advancing	rapidly	and	significantly	transforming
various domains. Utilizing deep learning algorithms and
advanced neural networks, these models possess the abil -
ity to process, comprehend, and generate natural language.
As a result, they have found extensive applications across
numerous industries. By analyzing textual data and extract-
ing	 linguistic	 patterns,	 LLMs	 enable	 the	 generation	 of
intelligent and personalized responses, playing a vital role
in facilitating managerial decision-making and optimizing
business processes. However, as highlighted in this study,
effectively	leveraging	LLMs	in	different	industries	comes
with its own unique set of challenges. This study presents
a	historical	overview	of	the	evolution	of	LLMs	from	their
inception	to	the	present	day,	defines	and	introduces	the	core
architectures	of	LLMs,	explores	their	applications	in	detail,
and	identifies	the	barriers	to	their	adoption.	The	findings	of
this study are structured into four key sections.
The	first	section	reviews	the	development	of	language
models from their early days as statistical models to the
advanced Transformer-based architectures we see today.
For example, in 2023, OpenAI introduced GPT-4, repre -
senting	a	significant	leap	in	LLM	capabilities.	This	section
also	provides	an	overview	of	different	LLM	architectures
and explains how they work. The second section delves
into	the	practical	applications	of	LLMs	in	daily	life,	cover-
ing	domains	such	as	healthcare,	finance,	business,	industry,
agriculture, energy, education, research, computer program-
ming, media, law, tourism, and the arts.
The	third	section	focuses	on	the	integration	of	LLMs	into
various	subfields	of	artificial	intelligence,	including	NLP,
machine learning, generative AI, recommender systems,
computer	vision,	and	robotics.	The	fourth	section	identifies
and	analyzes	the	key	challenges	associated	with	LLMs,	such
as technical complexity, high computational costs, inherent
biases, and ethical and legal concerns.
In conclusion, this study emphasizes the transformative
role	of	LLMs	in	shaping	the	future	of	artificial	intelligence
technologies and their applications across diverse domains.
Organizations that align their strategies and resources with
the	intelligent	adoption	of	LLMs	are	likely	to	gain	substan-
tial competitive advantages in the evolving digital landscape.
Future research should focus on exploring the long-term
impacts of these models on decision-making processes,
developing new metrics for evaluating the value generated
by	LLMs,	and	addressing	emerging	ethical,	social,	and	tech-
nical implications. By leveraging the insights and strategies
presented in this study, users, researchers, and decision-
makers can gain a clearer understanding of the opportuni -
ties	and	challenges	associated	with	LLM	adoption,	identify
optimal use cases, and prepare for the successful implemen-
tation of this technology across various sectors. Without
a	doubt,	the	future	of	LLMs	is	bright	and	full	of	promise,
a future in which these technologies will enhance human-
machine	 interaction,	 redefine	 industries,	 and	 accelerate
innovation in the global digital transformation.

1 3
P . Peykani et al.
Acknowledgments The authors are thankful to the Editor-in-Chief
and the anonymous reviewers for their insightful comments and sug -
gestions on an earlier version of this manuscript.
Author Contributions All authors contributed to the study conception,
methodology development, analysis, and manuscript preparation. All
authors	read	and	approved	the	final	manuscript.
Funding The authors declare that no funding was received to assist
with the preparation of this manuscript or conducting this study.
Data Availability	The	data	supporting	the	findings	of	this	study	are
available from the corresponding author upon reasonable request.
Declarations
Research Involving Human and/or Animals This study did not involve
human participants or animals.
Informed Consent Not applicable, as the study did not involve human
participants.
Competing Interests The authors declare no competing interests.
Open Access   This article is licensed under a Creative Commons
Attribution	4.0	International	License,	which	permits	use,	sharing,
adaptation, distribution and reproduction in any medium or format,
as	long	as	you	give	appropriate	credit	to	the	original	author(s)	and	the
source, provide a link to the Creative Commons licence, and indicate
if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless
indicated otherwise in a credit line to the material. If material is not
included in the article’s Creative Commons licence and your intended
use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright
holder. To view a copy of this licence, visit  h t t  p : / /  c r e  a t i  v e c o m m o n s . o
r g / l i c e n s e s / b y / 4 . 0 /     .
References
1.	 McCulloch	 WS,	Pitts	W	(1943)	A	logical	calculus	of	the	ideas
immanent	in	nervous	activity.	Bull	Math	Biophys	5(4):115–133.
https:/	/doi.or	g/10.10	07/BF	02478259
2.	 Radford	 A,	Wu	J,	Child	R,	Luan	D,	Amodei	D,	Sutskever	I	(2019)
Language	models	are	unsupervised	multitask	learners.	OpenAI
Blog	1(8):9
3. Brown T, Mann B, Ryder N, Subbiah M, Kaplan JD, Dhariwal P
et	al	(2020)	Language	models	are	few-shot	learners.	Adv	Neural
Inf	Process	Syst	33:1877–1901
4.	 Zhang	 S,	Dong	L,	Li	X,	Zhang	S,	Sun	X,	Wang	S	et	al	(2023)
Instruction tuning for large language models: a survey. Preprint at
https:/	/arxiv.	org/abs	/2308	.10792
5.	 Radford	 A,	 Narasimhan	 K,	 Salimans	 T,	Sutskever	 I	 (2018)
Improving language understanding by generative pre-training
6.	 Li	 Y,	Wang	S,	Ding	H,	Chen	H	(2023	November)	Large	language
models	in	finance:	a	survey.	In:	Proceedings	of	the	fourth	ACM
international	conference	on	AI	in	finance,	pp	374–382
7.	 Zhao	 WX,	Zhou	K,	Li	J,	Tang	T,	Wang	X,	Hou	Y	et	al	(2023)	A
survey	of	large	language	models.	1(2):1–124.	Preprint	at	 h t t  p s : /  / a
r  x i v  . o r g / a b s / 2 3 0 3 . 1 8 2 2 3
8.	 Winograd	 T	(1972)	Understanding	natural	language.	Cognit	Phy-
chol	3(1):1–191.	https:/	/doi.or	g/10.10	16/00	10-0285(72)90002-3
9.	 Mikolov	 T,	Sutskever	I,	Chen	K,	Corrado	GS,	Dean	J	(2013)	Dis-
tributed representations of words and phrases and their composi -
tionality. Adv Neural Inf Process Syst 26
10.	 Pennington	J,	Socher	R,	Manning	CD	(2014	Oct)	Glove:	global
vectors for word representation. In: Proceedings of the 2014
conference on empirical methods in natural language processing
(EMNLP),	pp	1532–1543
11.	 Elman	JL	(1990)	Finding	structure	in	time.	Cognit	Sci	14(2):179–
211. https:/	/doi.or	g/10.12	07/s1	5516709cog1402_1
12.	 Mikolov	T,	Karafiát	M,	Burget	L,	Cernocký	J,	Khudanpur	S
(2010)	Recurrent	neural	network	based	language	model.	In	Inter-
speech	2(3):1045–1048
13.	 Wu	Y,	Schuster	M,	Chen	Z,	Le	QV,	Norouzi	M,	Macherey	W	et	al
(2016)	Google’s	neural	machine	translation	system:	bridging	the
gap between human and machine translation. Preprint at  h t t  p s : /  / a
r		x	i	v		.	o	r	g	/	a	b	s	/	1	6	0	9	.	0	8	1	4	4
14.	 Hochreiter	S,	Schmidhuber	J	(1997)	Long	short-term	memory.
Neural	Comput	9(8):1735–1780.		h	t	t		p	s	:	/		/	d	o		i	.	o		r	g	/	1	0	.	1	1	6	2	/	n	e	c	o	.	1	9
9	7	.	9	.	8	.	1	7	3	5
15.	 Dey	R,	Salem	FM	(2017	Aug)	Gate-variants	of	gated	recurrent
unit	(GRU)	neural	networks.	In:	2017	IEEE	60th	international
midwest	symposium	on	circuits	and	systems	(MWSCAS),	IEEE,
pp	1597–1600
16.	 Vaswani	A,	Shazeer	N,	Parmar	N,	Uszkoreit	J,	Jones	L,	Gomez
AN	et	al	(2017)	Attention	is	all	you	need.	Adv	Neural	Inf	Process
Syst 30
17.	 Devlin	J,	Chang	MW,	Lee	K,	Toutanova	K	(2019	Jun)	Bert:	pre-
training of deep bidirectional transformers for language under -
standing.	In:	Proceedings	of	the	2019	conference	of	the	North
American chapter of the association for computational linguis -
tics:	human	language	technologies,	volume	1	(long	and	short
papers),	pp	4171–4186
18.	 Achiam	J,	Adler	S,	Agarwal	S,	Ahmad	L,	Akkaya	I,	Aleman	FL	et
al	(2023)	Gpt-4	technical	report.	Preprint	at	 h t t  p s : /  / a r  x i v  . o r g / a b s /
2 3 0 3 . 0 8 7 7 4
19.	 Touvron	H,	Lavril	T,	Izacard	G,	Martinet	X,	Lachaux	MA,	Lac-
roix	T	et	al	(2023)	Open	and	efficient	foundation	language	mod-
els. Preprint at https:/	/doi.or	g/10.48	550/a	rXiv.2302(3)
20. Kaplan J, McCandlish S, Henighan T, Brown TB, Chess B, Child
R	et	al	(2020)	Scaling	laws	for	neural	language	models.	 h t t  p s : /  / d
o  i . o  r g / 1 0 . 4 8 5 5 0 / a r X i v . 2 0 0 1 . 0 8 3 6 1
21.	 Hoffmann	J,	Borgeaud	S,	Mensch	A,	Buchatskaya	E,	Cai	T,
Rutherford	E	et	al	(2022	Nov)	Training	compute-optimal	large
language models. In: Proceedings of the 36th International
Conference on Neural Information Processing Systems, pp
30016–30030
22.	 Chen	Z,	Wang	S,	Xiao	T,	Wang	Y,	Chen	S,	Cai	X	et	al	(2025
Jul)	Revisiting	scaling	laws	for	language	models:	the	role	of	data
quality and training strategies. In: Proceedings of the 63rd Annual
Meeting	of	the	Association	for	Computational	Linguistics	(Vol-
ume,	1:	Long	Papers),	pp	23881–23899
23.	 Wei	J,	Tay	Y,	Bommasani	R,	Raffel	C,	Zoph	B,	Borgeaud	S	et	al
(2022)	Emergent	abilities	of	large	language	models.	Preprint	at
https:/ /arxiv. org/abs /2206 .07682
24. Bommasani R, Hudson DA, Adeli E, Altman R, Arora S, von Arx
S	et	al	(2021)	On	the	opportunities	and	risks	of	foundation	mod-
els. Preprint at https:/ /arxiv. org/abs /2108 .07258
25.	 Liu	Y,	Ott	M,	Goyal	N,	Du	J,	Joshi	M,	Chen	D	et	al	(2019).
Roberta: a robustly optimized bert pretraining approach. Preprint
at https:/	/arxiv.	org/abs	/1907	.11692
26.	 He	P,	Liu	X,	Gao	J,	Chen	W	(2020).	Deberta:	decoding-enhanced
bert with disentangled attention. Preprint at  h t t  p s : /  / a r  x i v  . o r g / a b s /
2 0 0 6 . 0 3 6 5 4
27. Chowdhery A, Narang S, Devlin J, Bosma M, Mishra G, Roberts
A	et	al	(2023)	Palm:	scaling	language	modeling	with	pathways.	J
Mach	Learn	Res	24(240):1–113

1 3
The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,…
28. Jiang AQ, Sablayrolles A, Mensch A, Bamford C, Chaplot DS, de
las	Casas	D	et	al	(2023)	Mistral	7B	Preprint	at	 h t t  p s : /  / a r  x i v  . o r g / a
b s / 2 3 1 0 . 0 6 8 2 5
29.	 Raffel	C,	Shazeer	N,	Roberts	A,	Lee	K,	Narang	S,	Matena	M	et
al	(2020)	Exploring	the	limits	of	transfer	learning	with	a	unified
text-to-text	transformer.	J	Mach	Learn	Res	21(140):1–67
30.	 Lewis	M,	Liu	Y,	Goyal	N,	Ghazvininejad	M,	Mohamed	A,	Levy
O	et	al	(2020	Jul)	BART:	denoising	sequence-to-sequence	pre-
training for natural language generation, translation, and com -
prehension. In: Proceedings of the 58th annual meeting of the
association for computational linguistics, pp 7871–7880
31.	 Bahdanau	D,	Cho	K,	Bengio	Y	(2014)	Neural	machine	translation
by jointly learning to align and translate. Preprint at  h t t  p s : /  / a r  x i v  .
o	r	g	/	a	b	s	/	1	4	0	9	.	0	4	7	3
32. Team G, Anil R, Borgeaud S, Alayrac JB, Yu J, Soricut R et al
(2023)	Gemini:	a	family	of	highly	capable	multimodal	models.
Preprint at https:/ /arxiv. org/abs /2312 .11805
33.	 Dosovitskiy	A,	Beyer	L,	Kolesnikov	A,	Weissenborn	D,	Zhai	X,
Unterthiner	T	et	al	(2020)	An	image	is	worth	16x16	words:	trans-
formers for image recognition at scale. Preprint at  h t t  p s : /  / a r  x i v  . o r
g	/	a	b	s	/	2	0	1	0	.	1	1	9	2	9
34. Radford A, Kim JW, Hallacy C, Ramesh A, Goh G, Agarwal S
et	al	(2021	Jul)	Learning	transferable	visual	models	from	natural
language supervision. In: International conference on machine
learning,	PmLR,	pp.	8748–8763
35.	 Alayrac	JB,	Donahue	J,	Luc	P,	Miech	A,	Barr	I,	Hasson	Y	et	al
(2022)	Flamingo:	a	visual	language	model	for	few-shot	learning.
Adv Neural Inf Process Syst 35:23716–23736
36.	 Jacobs	RA,	Jordan	MI,	Nowlan	SJ,	Hinton	GE	(1991)	Adaptive
mixtures	of	local	experts.	Neural	Computation	3(1):79–87.	https:/
/doi.or	g/10.11	62/ne	co.1991.3.1.79
37.	 Su	J,	Ahmed	M,	Lu	Y,	Pan	S,	Bo	W,	Liu	Y	(2024)	Roformer:
enhanced transformer with rotary position embedding. Neuro -
computing 568:127063.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 1 6 / j . n e u c o m . 2 0 2 3 . 1
2 7 0 6 3
38.	 Fedus	W,	Zoph	B,	Shazeer	N	(2022)	Switch	transformers:	scaling
to	trillion	parameter	models	with	simple	and	efficient	sparsity.	J
Mach	Learn	Res	23(120):1–39
39.	 Shazeer	N,	Mirhoseini	A,	Maziarz	K,	Davis	A,	Le	Q,	Hinton	G	et
al	(2017)	Outrageously	large	neural	networks:	the	sparsely-gated
mixture-of-experts layer. Preprint at  h t t  p s : /  / a r  x i v  . o r g / a b s / 1 7 0 1 . 0 6
5 3 8
40.	 Lepikhin	D,	Lee	H,	Xu	Y,	Chen	D,	Firat	O,	Huang	Y	et	al	(2020)
Gshard: scaling giant models with conditional computation and
automatic sharding. Preprint at https:/ /arxiv. org/abs /2006 .16668
41. Pope R, Douglas S, Chowdhery A, Devlin J, Bradbury J, Heek J
et	al	(2023)	Efficiently	scaling	transformer	inference.	Proc	Mach
Learn	Syst	5:606–624
42.	 Kwon	W,	Li	Z,	Zhuang	S,	Sheng	Y,	Zheng	L,	Yu	CH	et	al	(2023
Oct)	Efficient	memory	management	for	large	language	model
serving	with	pagedattention.	In:	Proceedings	of	the	29th	sympo-
sium on operating systems principles, pp 611–626
43. Peng B, Alcaide E, Anthony Q, Albalak A, Arcadinho S, Bider -
man	S	et	al	(2023	Dec)	Rwkv:	reinventing	rnns	for	the	trans-
former era. In: Findings Of The Association For Computational
Linguistics:	EMNLP	2023,	pp	14048–14077
44.	 Gu	A,	Dao	T	(2023)	Mamba:	linear-time	sequence	modeling
with selective state spaces. Preprint at https:/ /arxiv. org/abs /2312
.00752
45.	 Sun	Y,	Dong	L,	Huang	S,	Ma	S,	Xia	Y,	Xue	J	et	al	(2023)	Reten-
tive network: a successor to transformer for large language mod-
els. Preprint at https:/ /arxiv. org/abs /2307 .08621
46. Jiang AQ, Sablayrolles A, Roux A, Mensch A, Savary B, Bam -
ford	C	et	al	(2024)	Mixtral	of	experts.	Preprint	at	 h t t  p s : /  / a r  x i v  . o r g
/ a b s / 2 4 0 1 . 0 4 0 8 8
47.	 Grattafiori	A,	Dubey	A,	Jauhri	A,	Pandey	A,	Kadian	A,	Al-Dahle
A	et	al	(2024)	The	llama	3	herd	of	models.	Preprint	at	 h t t  p s : /  / a r  x i
v  . o r g / a b s / 2 4 0 7 . 2 1 7 8 3
48.	 Yang	A,	Li	A,	Yang	B,	Zhang	B,	Hui	B,	Zheng	B,	Qiu	Z	(2025)
Qwen3 technical report. Preprint at 	h	t	t		p	s	:	/		/	a	r		x	i	v		.	o	r	g	/	a	b	s	/	2	5	0	5	.	0	9
3 8 8
49.	 Abdin	M,	Aneja	J,	Behl	H,	Bubeck	S,	Eldan	R,	Gunasekar	S	et	al
(2024)	Phi-4	technical	report.	Preprint	at	 h t t  p s : /  / a r  x i v  . o r g / a b s / 2 4
1	2	.	0	8	9	0	5
50.	 Xia	M,	Gao	T,	Zeng	Z,	Chen	D	(2024	May)	Sheared	llama:	accel-
erating language model pre-training via structured pruning. In:
International	Conference	on	Learning	Representations,	vol	2024.
pp	5385–5409
51.	 Howard	J,	Ruder	S	(2018	Jul)	Universal	language	model	fine-
tuning	for	text	classification.	In:	Proceedings	of	the	56th	Annual
Meeting	of	the	Association	for	Computational	Linguistics	(Vol-
ume,	1:	Long	Papers),	pp	328–339
52.	 Hu	EJ,	Shen	Y,	Wallis	P,	Allen-Zhu	Z,	Li	Y,	Wang	S	et	al	(2022)
Lora:	low-rank	adaptation	of	large	language	models.	ICLR	1(2):3
53.	 Wei	J,	Bosma	M,	Zhao	VY,	Guu	K,	Yu	AW,	Lester	B	et	al	(2021)
Finetuned language models are zero-shot learners. Preprint at
https:/	/arxiv.	org/abs	/2109	.01652
54.	 Ouyang	L,	Wu	J,	Jiang	X,	Almeida	D,	Wainwright	C,	Mishkin	P
et	al	(2022)	Training	language	models	to	follow	instructions	with
human feedback. Adv Neural Inf Process Syst 35:27730–27744
55. Rafailov R, Sharma A, Mitchell E, Manning CD, Ermon S,
Finn	C	(2023)	Direct	preference	optimization:	your	language
model is secretly a reward model. Adv Neural Inf Process Syst
36:53728–53741
56.	 Reynolds	L,	McDonell	K	(2021)	Multiversal	views	on	language
models. Preprint at https:/	/arxiv.	org/abs	/2102	.06391
57. Wei J, Wang X, Schuurmans D, Bosma M, Xia F, Chi E et al
(2022)	Chain-of-thought	prompting	elicits	reasoning	in	large	lan-
guage models. Adv Neural Inf Process Syst 35:24824–24837
58.	 Lewis	P,	Perez	E,	Piktus	A,	Petroni	F,	Karpukhin	V,	Goyal	N	et	al
(2020)	Retrieval-augmented	generation	for	knowledge-intensive
nlp	tasks.	Adv	Neural	Inf	Process	Syst	33:9459–9474
59.	 Klesel	M,	Wittmann	HF	(2025)	Retrieval-augmented	generation
(rag)	m.	klesel,	hf	wittmann.	Bus	Inf	Syst	Eng	67(4):551–561.
https:/	/doi.or	g/10.10	07/s1	2599-025-00945-3
60.	 Cheng	Z,	Kasai	J,	Yu	T	(2023	December)	Batch	prompting:	effi-
cient inference with large language model apis. In: Proceedings
of	the	2023	Conference	on	Empirical	Methods	in	Natural	Lan-
guage	Processing:	Industry	Track,	pp	792–810
61. Sivarajkumar S, Kelley M, Samolyk-Mazzanti A, Visweswaran
S,	Wang	Y	(2024)	An	empirical	evaluation	of	prompting	strate-
gies for large language models in zero-shot clinical natural lan -
guage processing: algorithm development and validation study.
JMIR Med Inf 12:e55318. https://doi.org/10.2196/55318
62.	 Liu	P,	Yuan	W,	Fu	J,	Jiang	Z,	Hayashi	H,	Neubig	G	(2023)	Pre-
train, prompt, and predict: a systematic survey of prompting
methods in natural language processing. ACM Comput Surv
55(9):1–35.	https:/ /doi.or g/10.11 45/35 60815
63. Hendrycks D, Burns C, Basart S, Zou A, Mazeika M, Song D et
al	(2020)	Measuring	massive	multitask	language	understanding.
Preprint at https:/	/arxiv.	org/abs	/2009	.03300
64.	 Zellers	R,	Holtzman	A,	Bisk	Y,	Farhadi	A,	Choi	Y	(2019	Jul)
Hellaswag:	can	a	machine	really	finish	your	sentence?	In:	Pro-
ceedings of the 57th annual meeting of the association for com -
putational	linguistics,	pp	4791–4800
65.	 Lin	S,	Hilton	J,	Evans	O	(2022	May)	Truthfulqa:	measuring	how
models mimic human falsehoods. In: Proceedings of the 60th
annual meeting of the association for computational linguistics
(volume	1:	long	papers),	pp	3214–3252

1 3
P . Peykani et al.
66.	 Cobbe	K,	Kosaraju	V,	Bavarian	M,	Chen	M,	Jun	H,	Kaiser	L	et	al
(2021)	Training	verifiers	to	solve	math	word	problems.	Preprint
at https:/ /arxiv. org/abs /2110 .14168
67. Chen M, Tworek J, Jun H, Yuan Q, Pinto HPDO, Kaplan J et al
(2021)	Evaluating	large	language	models	trained	on	code.	Pre-
print at https:/ /arxiv. org/abs /2107 .03374
68.	 Zeng	A,	Liu	X,	Du	Z,	Wang	Z,	Lai	H,	Ding	M	et	al	(2022)	Glm-
130b: an open bilingual pre-trained model. Preprint at  h t t  p s : /  / a r  x i
v  . o r g / a b s / 2 2 1 0 . 0 2 4 1 4
69.	 Workshop	B,	Scao	TL,	Fan	A,	Akiki	C,	Pavlick	E,	Ilić	S	et	al
(2022)	Bloom:	a	176b-parameter	open-access	multilingual	lan-
guage model. Preprint at https:/ /arxiv. org/abs /2211 .05100
70.	 Jiang	Y,	Li	X,	Zhu	G,	Li	H,	Deng	J,	Han	K	et	al	(2023)	6G	non-
terrestrial networks enabled low-altitude economy: opportunities
and challenges. Preprint at https:/	/arxiv.	org/abs	/2311	.09047
71.	 Team	G,	Georgiev	P,	Lei	VI,	Burnell	R,	Bai	L,	Gulati	A,	Bat-
saikhan	BO	(2024)	Gemini	1.5:	unlocking	multimodal	under-
standing across millions of tokens of context. arXiv preprint
arXiv:2403.05530
72. Kurokawa R, Ohizumi Y , Kanzawa J, Kurokawa M, Sonoda Y ,
Nakamura	Y	et	al	(2024)	Diagnostic	performances	of	Claude
3 opus and Claude 3.5 Sonnet from patient history and key
images in Radiology’s “diagnosis Please” cases. Jpn J Radiol
42(12):1399–1402
73.	 Liang	J,	Huang	W,	Xia	F,	Xu	P,	Hausman	K,	Ichter	B	et	al	(2023
May)	Code	as	policies:	language	model	programs	for	embodied
control. In: 2023 IEEE International Conference on Robotics and
Automation	(ICRA),	IEEE,	pp	9493–9500
74.	 Héder	M	(2017)	From	NASA	to	EU:	the	evolution	of	the	TRL
scale	in	public	sector	innovation.	Innov	J	22(2):1–23
75.	 Lavin	A,	Gilligan-Lee	CM,	Visnjic	A,	Ganju	S,	Newman	D,
Ganguly	S	et	al	(2022)	Technology	readiness	levels	for	machine
learning	systems.	Nat	Commun	13(1):6039
76.	 Dwivedi	YK,	Pandey	N,	Currie	W,	Micu	A	(2024)	Leveraging
ChatGPT	and	other	generative	artificial	intelligence	(AI)-based
applications in the hospitality and tourism industry: practices,
challenges and research agenda. Int J Contemp Hosp Manage
36(1):1–12.	https:/ /doi.or g/10.11 08/IJ CHM-05-2023-0686
77.	 Buhalis	D,	O’Connor	P,	Leung	R	(2022)	Smart	hospitality:	from
smart cities and smart tourism towards agile business ecosys -
tems in networked destinations. Int J Contemp Hosp Manage
35(1):369–393.	https:/	/doi.or	g/10.11	08/IJ	CHM-04-2022-0497
78.	 Ozdemir	O,	Dogru	T,	Kizildag	M,	Erkmen	E	(2023)	A	critical
reflection	on	digitalization	for	the	hospitality	and	tourism	industry:
value implications for stakeholders. Int J Contemp Hosp Manage
35(9):3305–3321.	https:/ /doi.or g/10.11 08/IJ CHM-04-2022-0535
79.	 Carvalho	I,	Ivanov	S	(2024)	ChatGPT	for	tourism:	applications,
benefits	and	risks.	Tour	Rev	79(2):290–303.	 h t t  p s : /  / d o  i . o  r g / 1 0 . 1 1
0 8 / T R - 0 2 - 2 0 2 3 - 0 0 8 8
80.	 Gursoy	D,	Li	Y,	Song	H	(2023)	ChatGPT	and	the	hospitality
and tourism industry: an overview of current trends and future
research	directions.	J	Hosp	Mark	Manag	32(5):579–592.	 h t t  p s : /  / d
o		i	.	o		r	g	/	1	0	.	1	0	8	0	/	1	9	3	6	8	6	2	3	.	2	0	2	3	.	2	2	1	1	9	9	3
81.	 Biswas	S	(2023)	The	function	of	chat	GPT	in	social	media:
according	to	chat	GPT.	Available	at	SSRN	4405389
82.	 Mich	L,	Garigliano	R	(2023)	ChatGPT	for	e-tourism:	a	techno-
logical	perspective.	Inf	Technol	Tour	25(1):1–12.	 h t t  p s : /  / d o  i . o  r g /
1 0 . 1 0 0 7 / s 4 0 5 5 8 - 0 2 3 - 0 0 2 4 8 - x
83.	 Wu	T,	He	S,	Liu	J,	Sun	S,	Liu	K,	Han	QL	et	al	(2023)	A	brief
overview of ChatGPT: the history, status quo and potential future
development.	IEEE/CAA	J	Automatica	Sin	10(5):1122–1136.
https:/	/doi.or	g/10.11	09/JA	S.2023.123618
84. Van Dis EAM, Bollen J, Zuidema W, Van Rooij R, Bock -
ting	CL	(2023)	ChatGPT:	five	priorities	for	research.	Nature
614(7947):224–226.	  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 3 8 / d 4 1 5 8 6 - 0 2 3 - 0 0 2 8 8
- 7
85. Rahman MM, Terano HJ, Rahman MN, Salamzadeh A, Rahaman
MS	(2023)	ChatGPT	and	Academic	research:	a	review	and	rec-
ommendations based on practical examples. J Educ Mngt Dev
Stud	3(1):1–12.	https:/ /doi.or g/10.52 631/j emds.v3i1.175.
86.	 Biswas	S,	Dobaria	D,	Cohen	HL	(2023)	ChatGPT	and	the	future
of	journal	reviews:	a	feasibility	study.	Yale	J	Biol	Med	96(3):415.
https:/	/doi.or	g/10.59	249/S	KDH9286
87.	 Imran	M,	Almusharraf	N	(2023)	Analyzing	the	role	of	ChatGPT
as a writing assistant at higher education level: a systematic
review	of	the	literature.	Contemp	Educ	Technol	15(4):ep464.
https:/	/doi.or	g/10.30	935/c	edtech/13605
88.	 Hosseini	M,	Horbach	SP	(2023)	Fighting	reviewer	fatigue	or
amplifying bias? Considerations and recommendations for use
of ChatGPT and other large language models in scholarly peer
review.	Res	Integr	Peer	Rev	8(1):4
89.	 Ray	PP	(2023)	ChatGPT:	a	comprehensive	review	on	back-
ground, applications, key challenges, bias, ethics, limitations and
future scope. Internet Things Cyber-Phys Syst 3:121–154.  h t t  p s : /
/ d o  i . o  r g / 1 0 . 1 0 1 6 / j . i o t c p s . 2 0 2 3 . 0 4 . 0 0 3
90.	 Alkaissi	H,	McFarlane	SI	(2023)	Artificial	hallucinations	in	Chat-
GPT:	implications	in	scientific	writing.	Cureus	15(2).	 h t t  p s : /  / d o  i .
o		r	g	/	1	0	.	7	7	5	9	/	c	u	r	e	u	s	.	3	5	1	7	9
91.	 Meyer	JG,	Urbanowicz	RJ,	Martin	PC,	O’Connor	K,	Li	R,	Peng
PC,	Moore	JH	(2023)	ChatGPT	and	large	language	models	in
academia:	opportunities	and	challenges.	Biodata	Min	16(1):20
92.	 Liebrenz	M,	Schleifer	R,	Buadze	A,	Bhugra	D,	Smith	A	(2023)
Generating scholarly content with ChatGPT: ethical challenges
for	medical	publishing.	Lancet	Digit	Health	5(3):e105–e106.
https:/	/doi.or	g/10.10	16/S2	589-7500(23)00019-5
93.	 O’Connor	S	(2023)	Open	artificial	intelligence	platforms	in	nurs-
ing education: tools for Academic progress or abuse? Nurse Educ
Pract 66:103537. https:/ /doi.or g/10.10 16/j. nepr.2022.103537
94.	 Tennant	JP,	Ross-Hellauer	T	(2020)	The	limitations	to	our	under-
standing	of	peer	review.	Res	Integr	Peer	Rev	5(1):6.	 h t t  p s : /  / d o  i . o
r	g	/	1	0	.	1	1	8	6	/	s	4	1	0	7	3	-	0	2	0	-	0	0	0	9	2	-	1
95.	 Mehta	V,	Mathur	A,	Anjali	AK,	Fiorillo	L	(2024)	The	applica-
tion of ChatGPT in the peer-reviewing process. Oral Oncol Rep
9:100227.	https:/ /doi.or g/10.10 16/j. oor.2024.100227
96.	 Misra	DP,	Chandwar	K	(2023)	ChatGPT,	artificial	intelligence
and	scientific	writing:	what	authors,	peer	reviewers	and	editors
should	know.	J	R	Coll	Physicians	Edinb	53(2):90–93.	 h t t  p s : /  / d o  i .
o  r g / 1 0 . 1 1 7 7 / 1 4 7 8 2 7 1 5 2 3 1 1 8 1 0 2 3
97.	 AlAfnan	MA,	Dishari	S,	Jovic	M,	Lomidze	K	(2023)	Chatgpt
as an educational tool: opportunities, challenges, and recommen-
dations for communication, business writing, and composition
courses.	J	Artif	Intel	Technol	3(2):60–68.		h	t	t		p	s	:	/		/	d	o		i	.	o		r	g	/	1	0	.	3	7	9
6 5 / j a i t . 2 0 2 3 . 0 1 8 4
98.	 Fraiwan	M,	Khasawneh	N	(2023)	A	review	of	chatgpt	applica-
tions in education, marketing, software engineering, and health -
care:	benefits,	drawbacks,	and	research	directions.	Preprint	at
https:/ /arxiv. org/abs /2305 .00237
99.	 Doshi	AR,	Bell	JJ,	Mirzayev	E,	Vanneste	BS	(2025)	Generative
artificial	intelligence	and	evaluating	strategic	decisions.	Strateg
Manag	J	46(3):583–610.	https:/ /doi.or g/10.10 02/sm j.3677
100.	Şeker	E	(2024)	Large	language	models	in	work	and	business.
Front Artif Intel 7:1516832
101.	Meguellati	E,	Han	L,	Bernstein	A,	Sadiq	S,	Demartini	G	(2024
May)	How	good	are	LLMS	in	generating	personalized	advertise-
ments? In: Companion Proceedings of the ACM Web Conference
2024,	pp	826–829
102.	Pathak	A	(2023)	Exploring	ChatGPT:	an	extensive	examination
of its background, applications, key challenges, bias, ethics, limi-
tations, and future prospects. In: Applications, Key Challenges,
Bias,	Ethics,	Limitations,	and	Future	Prospects

1 3
The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,…
103.	Goldstein	JA,	Chao	J,	Grossman	S,	Stamos	A,	Tomz	M	(2024)
How persuasive is AI-generated propaganda? PNAS Nexus
3(2):pgae034.	https:/	/doi.or	g/10.10	93/pn	asnexus/pgae034
104.	George	AS,	 George	AH	 (2023)	A	 review	 of	 ChatGPT	AI’s
impact on several business sectors. Partners Univers Int Innov J
1(1):9–23
105.	Galitsky	B	(2020)	Artificial	intelligence	for	customer	relationship
management.	Springer	Int	Publ	10:978–3
106. Sorin V , Brin D, Barash Y , Konen E, Charney A, Nadkarni G et al
(2024)	Large	language	models	and	empathy:	systematic	review.	J
Med	Internet	Res	26:e52597.	https://doi.org/10.2196/52597
107.	Robbert	K,	Penn	C,	Wall	J	(2023)	Use	cases	of	large	language
models	in	marketing	analytics.	Appl	Mark	Analytics	9(3):249–
269.	https:/	/doi.or	g/10.69	554/M	CNI7392
108.	Verma	S,	Sharma	R,	Deb	S,	Maitra	D	(2021)	Artificial	intelli-
gence in marketing: systematic review and future research direc -
tion.	Int	J	Inf	Manage	Data	Insights	1(1):100002.	 h t t  p s : /  / d o  i . o  r g /
1 0 . 1 0 1 6 / j . j j i m e i . 2 0 2 0 . 1 0 0 0 0 2
109.	Echterhoff	JM,	Liu	Y,	Alessa	A,	McAuley	J,	He	Z	(2024	Novem-
ber)	Cognitive	bias	in	decision-making	with	LLMs.	In:	Findings
of	the	association	for	computational	linguistics:	EMNLP	2024,
pp. 12640–12653
110. Kasneci E, Seßler K, Küchemann S, Bannert M, Dementieva D,
Fischer	F	et	al	(2023)	ChatGPT	for	good?	On	opportunities	and
challenges	of	large	language	models	for	education.	Learn	Individ
Differ	103:102274
111.	Malinka	K,	Peresíni	M,	Firc	A,	Hujnák	O,	Janus	F	(2023	June)
On	the	educational	impact	of	chatgpt:	is	artificial	intelligence
ready to obtain a university degree? In: Proceedings of the 2023
Conference on Innovation and Technology in Computer Science
Education V . 1, pp 47–53
112.	Jeon	J,	Lee	S	(2023)	Large	language	models	in	education:	a	focus
on the complementary relationship between human teachers and
ChatGPT.	Educ	Inf	Technol	28(12):15873–15892.	 h t t  p s : /  / d o  i . o  r g
/	1	0	.	1	0	0	7	/	s	1	0	6	3	9	-	0	2	3	-	1	1	8	3	4	-	1
113.	Dai	W,	Lin	J,	Jin	H,	Li	T,	Tsai	YS,	Gašević	D	et	al	(2023	Jul)
Can large language models provide feedback to students? A case
study on ChatGPT. In: 2023 IEEE international conference on
advanced	learning	technologies	(ICALT),	IEEE,	pp	323–325
114.	Grassini	S	(2023)	Shaping	the	future	of	education:	exploring	the
potential and consequences of AI and ChatGPT in educational
settings.	Educ	Sci	13(7):692.		h	t	t		p	s	:	/		/	d	o		i	.	o		r	g	/	1	0	.	3	3	9	0	/	e	d	u	c	s	c	i	1	3	0
7	0	6	9	2
115.	Adeshola	I,	Adepoju	AP	(2024)	The	opportunities	and	challenges
of	ChatGPT	in	education.	Interact	Learn	Env	32(10):6159–6172.
https:/	/doi.or	g/10.10	80/10	494820.2023.2253858
116.	Yang	KB,	Echeverria	V,	Lu	Z,	Mao	H,	Holstein	K,	Rummel	N
et	al	(2023	April)	Pair-up:	prototyping	human-AI	co-orchestra-
tion of dynamic transitions between individual and collaborative
learning in the classroom. In: Proceedings of the 2023 CHI con -
ference on human factors in computing systems, pp 1–17
117. Hadi MU, Qureshi R, Shah A, Irfan M, Zafar A, Shaikh MB et
al	(2023)	Large	language	models:	a	comprehensive	survey	of	its
applications, challenges, limitations, and future prospects. Autho-
rea Preprints 1:1–26
118.	Landa-Blanco	 M	 (2025)	 Artificial	 intelligence	 in	 education:
applications and limitations for teachers in low-and middle-
income countries. Front Educ 10:1681836.
119.	Jeon	J	(2024)	Exploring	AI	chatbot	affordances	in	the	EFL	class-
room: young learners’ experiences and perspectives. Comput
Assist	Lang	Learn	37(1–2):1–26.		h	t	t		p	s	:	/		/	d	o		i	.	o		r	g	/	1	0	.	1	0	8	0	/	0	9	5	8	8
2 2 1 . 2 0 2 1 . 2 0 2 1 2 4 1
120.	Grünebaum	A,	Chervenak	J,	Pollet	SL,	Katz	A,	Chervenak	FA
(2023)	The	exciting	potential	for	ChatGPT	in	obstetrics	and	gyne-
cology.	Am	J	Obstet	Gynecol	228(6):696–705.	 h t t  p s : /  / d o  i . o  r g / 1 0 .
1	0	1	6	/	j	.	a	j	o	g	.	2	0	2	3	.	0	3	.	0	0	9
121.	Stokel-Walker	C	(2023)	ChatGPT	listed	as	author	on	research
papers:	many	scientists	disapprove.	Nature	613(7945):620–621.
https:/ /doi.or g/10.10 38/d4 1586-023-00107-z
122.	Memarian	B,	Doleck	T	(2023)	ChatGPT	in	education:	methods,
potentials, and limitations. Comput Hum Behav: Artif Humans
1(2):100022.	https:/ /doi.or g/10.10 16/j. chbah.2023.100022
123.	Zhu	S,	Wang	Z,	Zhuang	Y,	Jiang	Y,	Guo	M,	Zhang	X	et	al	(2024)
Exploring the impact of ChatGPT on art creation and collabora -
tion:	benefits,	challenges	and	ethical	implications.	Telematics	Inf
Rep 14:100138. https:/ /doi.or g/10.10 16/j. teler.2024.100138
124.	Guo	Q	(2024)	Prompting	change:	ChatGPT’s	impact	on	digital
Humanities pedagogy-A case study in art history. Int J Humanit
Arts	Comput	18(1):58–78
125.	Boden	MA	(2004)	The	creative	mind:	myths	and	mechanisms.
Routledge
126.	Chakrabarty	T,	Padmakumar	V,	He	H	(2022	December)	Help	me
write a poem: instruction tuning as a vehicle for collaborative
poetry writing. In: Proceedings of the 2022 Conference on Empir-
ical	Methods	in	Natural	Language	Processing,	pp	6848–6863
127.	Franceschelli	G,	Musolesi	M	(2024)	On	the	creativity	of	large
language	models.	AI	Soc	56(11):1–41.	 h t t  p s : /  / d o  i . o  r g / 1 0 . 1 1 4 5 / 3 6
6	4	5	9	5
128.	Girotra	K,	Meincke	L,	Terwiesch	C,	Ulrich	KT	(2023)	Ideas	are
dimes a dozen: large language models for idea generation in inno-
vation. Available at SSRN, 4526071
129.	Shanahan	M,	McDonell	K,	Reynolds	L	(2023)	Role	play	with
large	language	models.	Nature	623(7987):493–498.	 h t t  p s : /  / d o  i . o  r
g / 1 0 . 1 0 3 8 / s 4 1 5 8 6 - 0 2 3 - 0 6 6 4 7 - 8
130.	Chen	Z,	Chan	J	(2024)	Large	language	model	in	creative	work:
the role of collaboration modality and user expertise. Manage Sci
70(12):9101–9117.	https:/ /doi.or g/10.12 87/mn sc.2023.03014
131.	Chakrabarty	T,	Laban	P,	Agarwal	D,	Muresan	S,	Wu	CS	(2024
May)	Art	or	artifice?	large	language	models	and	the	false	prom-
ise of creativity. In: Proceedings of the 2024 CHI Conference on
Human Factors in Computing Systems, pp 1–34
132.	Motlagh	FN,	Hajizadeh	M,	Majd	M,	Najafi	P,	Cheng	F	et	al
(2024)	Large	language	models	in	cybersecurity:	state-of-the-art.
Preprint at https:/	/arxiv.	org/abs	/2402	.00891
133.	Pavlik	JV	(2023)	Collaborating	with	ChatGPT:	considering	the
implications	of	generative	artificial	intelligence	for	journalism
and	media	education.	J	Mass	Commun	Educ	78(1):84–93.	 h t t  p s : /
/	d	o		i	.	o		r	g	/	1	0	.	1	1	7	7	/	1	0	7	7	6	9	5	8	2	2	1	1	4	9	5	7	7
134. AlQaruty S, Al Qaruty R, Al-Tkhayneh KM, Hadi SA, Ellala ZK
(2024	September)	The	role	of	artificial	intelligence	in	the	media
content	industry	(chat	GPT	as	a	model).	In:	2024	International
Conference on Multimedia Computing, Networking and Applica-
tions	(MCNA),	IEEE,	pp	50–56
135.	Meguellati	E,	Civelli	S,	Han	L,	Bernstein	A,	Sadiq	S	et	al	(2025)
LLM-Generated	ads:	from	personalization	parity	to	persuasion
superiority. Preprint at https:/ /arxiv. org/abs /2512 .03373
136.	Feizi	S,	Hajiaghayi	M,	Rezaei	K,	Shin	S	(2023)	Online	advertise-
ments with llms: opportunities and challenges. Preprint at  h t t  p s : /  /
a r  x i v  . o r g / a b s / 2 3 1 1 . 0 7 6 0 1
137.	Cai	L,	He	J,	Li	Y,	Liang	J,	Lin	Y,	Quan	Z	et	al	(2025	May)
Rtbagent: a llm-based agent system for real-time bidding. In:
Companion Proceedings of the ACM on Web Conference 2025,
pp 104–113
138.	Bender	EM,	Gebru	T,	McMillan-Major	A,	Shmitchell	S	(2021
March)	On	the	dangers	of	stochastic	parrots:	can	language	mod-
els be too big?  In: Proceedings of the 2021 ACM conference
on fairness, accountability, and transparency, pp 610–623
139.	Radivojevic	K,	Chou	M,	Badillo-Urquiola	K,	Brenner	P	(2024)
Human perception of llm-generated text content in social media
environments. Preprint at https:/	/arxiv.	org/abs	/2409	.06653
140.	Guan	J,	Huang	F,	Zhao	Z,	Zhu	X,	Huang	M	(2020)	A	knowledge-
enhanced pretraining model for commonsense story generation.

1 3
P . Peykani et al.
Trans	Assoc	Comput	Linguistics	8:93–108.	 h t t  p s : /  / d o  i . o  r g / 1 0 . 1 1 6
2	/	t	a	c	l	_	a	_	0	0	3	0	2
141.	Elgarf	M,	Salam	H,	Peters	C	(2024)	Fostering	children’s	creativity
through	LLM-driven	storytelling	with	a	social	robot.	Front	Robot
AI	11:1457429.	https:/	/doi.or	g/10.33	89/fr	obt.2024.1457429
142.	Castelo	N,	Bos	MW,	Lehmann	DR	(2019)	Task-dependent	algo-
rithm	aversion.	J	Mark	Res	56(5):809–825.	 h t t  p s : /  / d o  i . o  r g / 1 0 . 1 1 7
7	/	0	0	2	2	2	4	3	7	1	9	8	5	1	7	8	8
143.	Sevenard	I	(2025)	Democratisation	of	artificial	intelligence	(AI)
or	digital	authoritarianism?	China’s	large	language	model	(LLM)
strategy and the challenge to Western AI dominance. J Curr Chin
Aff,	18681026261434029
144.	Thirunavukarasu	AJ,	Ting	DSJ,	Elangovan	K,	Gutierrez	L,	Tan
TF,	Ting	DSW	(2023)	Large	language	models	in	medicine.	Nat
Med	29(8):1930–1940
145.	Nazi	ZA,	Peng	W	(2024	August)	Large	language	models	in
healthcare	and	medical	domain:	a	review.	Informatics	11(3):57).
MDPI. https:/	/doi.or	g/10.33	90/in	formatics11030057
146.	Mao	C,	Xu	J,	Rasmussen	L,	Li	Y,	Adekkanattu	P,	Pacheco	J,	Luo
Y	(2023)	AD-BERT:	using	pre-trained	language	model	to	predict
the progression from mild cognitive impairment to Alzheimer’s
disease. J Biomed Inform 144:104442
147.	Agbavor	F,	Liang	H	(2022)	Predicting	dementia	from	sponta-
neous	speech	using	large	language	models.	PLOS	Digit	Health
1(12):e0000168
148.	Kung	TH,	Cheatham	M,	Medenilla	A,	Sillos	C,	De	Leon	L,
Elepaño	C	et	al	(2023)	Performance	of	ChatGPT	on	USMLE:
potential for AI-assisted medical education using large language
models.	PLoS	Digit	Health	2(2):e0000198
149.	Xue	VW,	Lei	P,	Cho	WC	(2023)	The	potential	impact	of	Chat-
GPT in clinical and translational medicine. Clin Transl Med
13(3):e1216.	https:/ /doi.or g/10.10 02/ct m2.1216
150.	Ali	SR,	Dobbs	TD,	Hutchings	HA,	Whitaker	IS	(2023)	Using	Chat-
GPT	to	write	patient	clinic	letters.	Lancet	Digit	Health	5(4):e179–
e181. https:/	/doi.or	g/10.10	16/S2	589-7500(23)00048-1
151.	Javaid	M,	Haleem	A,	Singh	RP	(2023)	ChatGPT	for	healthcare
services: an emerging stage for an innovative perspective. Bench-
Council	Trans	Benchmarks	Stand	Eval	3(1):100105.	 h t t  p s : /  / d o  i . o
r g / 1 0 . 1 0 1 6 / j . t b e n c h . 2 0 2 3 . 1 0 0 1 0 5
152.	Wang	S,	Zhao	Z,	Ouyang	X,	Liu	T,	Wang	Q,	Shen	D	(2024)	Inter-
active computer-aided diagnosis on medical image using large
language	models.	Commun	Eng	3(1):133.	 h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 3 8
/ s 4 4 1 7 2 - 0 2 4 - 0 0 2 7 1 - 8
153.	Zhao	H,	Liu	Z,	Wu	Z,	Li	Y,	Yang	T,	Shu	P	et	al	(2024)	Revolution-
izing	finance	with	llms:	an	overview	of	applications	and	insights.
Preprint at https:/ /arxiv. org/abs /2401 .11641
154. Singhal K, Azizi S, Tu T, Mahdavi SS, Wei J, Chung HW et al
(2023)	Large	language	models	encode	clinical	knowledge.	Nature
620(7972):172–180
155.	Karn	SK,	Ghosh	R,	Farri	O	(2023)	Shs-nlp	at	radsum23:	domain-
adaptive pre-training of instruction-tuned llms for radiology
report impression generation. Preprint at  h t t  p s : /  / a r  x i v  . o r g / a b s / 2 3 0
6 . 0 3 2 6 4
156.	Gilson	A,	Safranek	CW,	Huang	T,	Socrates	V,	Chi	L,	Taylor	RA,
Chartash	D	(2023)	How	does	ChatGPT	perform	on	the	United
States	Medical	Licensing	Examination	(USMLE)?	The	implica-
tions of large language models for medical education and knowl-
edge	assessment.	JMIR	Med	Educ	9:e45312
157.	Liu	NF,	Zhang	T,	Liang	P	(2023)	Evaluating	verifiability	in	gener-
ative search engines. Preprint at https:/	/arxiv.	org/abs	/2304	.09848
158.	Wu	S,	Irsoy	O,	Lu	S,	Dabravolski	V,	Dredze	M,	Gehrmann	S
et	al	(2023)	Bloomberggpt:	a	large	language	model	for	finance.
Preprint at https:/ /arxiv. org/abs /2303 .17564
159.	Trachova	D,	Trachov	V,	Demchuk	O,	Karpenko	A,	Prykhodko	I
(2025	April)	Applications	of	large	language	models	in	the	inno-
vative analysis of Economic and accounting documentation:
a systematic review of recent advances and practical implica -
tions. In: International Conference on Business and Technology,
Springer	Nature	Switzerland,	Cham,	pp	439–447
160.	Winder	P,	Hildebrand	C,	Hartmann	J	(2025)	Biased	echoes:	large
language models reinforce investment biases and increase portfo-
lio	risks	of	private	investors.	PLoS	ONE	20(6):e0325459.	 h t t  p s : /  /
d	o		i	.	o		r	g	/	1	0	.	1	3	7	1	/	j	o	u	r	n	a	l	.	p	o	n	e	.	0	3	2	5	4	5	9
161.	Huang	X,	Lian	J,	Lei	Y,	Yao	J,	Lian	D,	Xie	X	(2025)	Recom-
mender ai agent: integrating large language models for interactive
recommendations.	ACM	Trans	Inf	Syst	43(4):1–33.	 h t t  p s : /  / d o  i . o  r
g / 1 0 . 1 1 4 5 / 3 7 3 1 4 4 6
162.	Zaremba	A,	Demir	E	(2023)	ChatGPT:	unlocking	the	future	of
NLP	in	finance.	Mod	Finance	1(1):93–98.	 h t t  p s : /  / d o  i . o  r g / 1 0 . 6 1 3 5
1 / m f . v 1 i 1 . 4 3
163.	Yu	Y,	Li	H,	Chen	Z,	Jiang	Y,	Li	Y,	Zhang	D	et	al	(2024	May)
FinMem:	a	performance-enhanced	LLM	trading	agent	with	lay-
ered memory and character design. In: Proceedings of the AAAI
Symposium	Series,	vol	3,	no	1.	pp	595–597
164.	Tang	H,	Chiu	KC,	Xu	L	(2003	September)	Finite	mixture	of
ARMA-GARCH model for stock price prediction. In: Proceed -
ings of the Third International Workshop on Computational Intel-
ligence	in	Economics	and	Finance	(CIEF’2003),	North	Carolina,
USA,	pp	1112–1119
165.	Yu	X,	Chen	Z,	Ling	Y,	Dong	S,	Liu	Z,	Lu	Y	(2023)	Temporal	data
meets	LLM-explainable	financial	time	series	forecasting.	Preprint
at https:/ /arxiv. org/abs /2306 .11025
166.	Nie	Y,	Kong	Y,	Dong	X,	Mulvey	JM,	Poor	HV,	Wen	Q	et	al	(2024)
A	survey	of	large	language	models	for	financial	applications:
progress, prospects and challenges. Preprint at  h t t  p s : /  / a r  x i v  . o r g /
a	b	s	/	2	4	0	6	.	1	1	9	0	3
167.	Biswas	S	(2023)	Role	of	ChatGPT	in	Computer	programming.
Mesopotamian	J	Comput	Sci	2023:9–15.		h	t	t		p	s	:	/		/	d	o		i	.	o		r	g	/	1	0	.	5	8	4	9
6 / M J C S C / 2 0 2 3 / 0 0 2
168.	Coello	CEA,	Alimam	MN,	Kouatly	R	(2024)	Effectiveness	of
chatgpt in coding: a comparative analysis of popular large lan -
guage	models.	Digital	4(1):114–125.		h	t	t		p	s	:	/		/	d	o		i	.	o		r	g	/	1	0	.	3	3	9	0	/	d	i	g
i t a l 4 0 1 0 0 0 5
169.	Dakhel	AM,	Majdinasab	V,	Nikanjam	A,	Khomh	F,	Desmarais
MC	et	al	(2023)	Github	copilot	ai	pair	programmer:	asset	or	lia-
bility? J Syst Softw 203:111734.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 1 6 / j . j s s . 2 0 2
3 . 1 1 1 7 3 4
170.	Pearce	H,	Ahmad	B,	Tan	B,	Dolan-Gavitt	B,	Karri	R	(2025)
Asleep at the keyboard? assessing the security of github copilot’s
code	contributions.	Commun	ACM	68(2):96–105.	 h t t  p s : /  / d o  i . o  r g
/ 1 0 . 1 1 4 5 / 3 6 1 0 7 2 1
171.	Liu	Z,	Chen	C,	Wang	J,	Che	X,	Huang	Y,	Hu	J	et	al	(2023	May)
Fill in the blank: context-aware automated text input genera -
tion for mobile gui testing. In: 2023 IEEE/ACM 45th Interna -
tional	Conference	on	Software	Engineering	(ICSE),	IEEE,	pp.
1355–1367
172. Malik Sami A, Rasheed Z, Waseem M, Zhang Z, Tomas H, Abra-
hamsson	P	(2024)	A	tool	for	test	case	scenarios	generation	using
large language models. Preprint at https://arxiv.org/abs/2406
173.	Fan	Z,	Gao	X,	Mirchev	M,	Roychoudhury	A,	Tan	SH	(2023	May)
Automated repair of programs from large language models. In:
2023 IEEE/ACM 45th International Conference on Software
Engineering	(ICSE),	IEEE,	pp.	1469–1481
174.	Shirafuji	A,	Oda	Y,	Suzuki	J,	Morishita	M,	Watanobe	Y	(2023
December)	Refactoring	programs	using	large	language	models
with	few-shot	examples.	In:	2023	30th	Asia-Pacific	Software
Engineering	Conference	(APSEC),	IEEE,	pp.	151–160
175.	Busch	D,	Bainczyk	A,	Smyth	S,	Steffen	B	(2025)	LLM-based
code generation and system migration in language-driven engi -
neering.	Int	J	Softw	Tools	Technol	Transf	27(1):137–147.	 h t t  p s : /  /
d	o		i	.	o		r	g	/	1	0	.	1	0	0	7	/	s	1	0	0	0	9	-	0	2	5	-	0	0	7	9	8	-	x

1 3
The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,…
176.	Zhou	X,	Cao	S,	Sun	X,	Lo	D	(2024)	Large	language	model	for
vulnerability detection and repair: literature review and the road
ahead.	ACM	Trans	Softw	Eng	Methodol	34(5):1–31.	 h t t  p s : /  / d o  i . o
r g / 1 0 . 1 1 4 5 / 3 7 0 8 5 2 2
177.	Wang	Y,	Wang	X,	Wang	X,	Yang	J,	Kwan	O,	Li	L	et	al	(2023)
The ChatGPT after: building knowledge factories for knowledge
workers with knowledge automation. IEEE/CAA J Automatica
Sin	10(11):2041–2044.	https:/	/doi.or	g/10.11	09/JA	S.2023.123966
178.	Rathore	B	(2023)	Future	of	textile:	sustainable	manufacturing	&
prediction via chatgpt. International, Eduzone
179.	Rane	N	(2023)	ChatGPT	and	similar	generative	artificial	intel-
ligence	(AI)	for	smart	industry:	role,	challenges	and	opportunities
for industry 4.0, industry 5.0 and society 5.0. Challenges Oppor -
tunities Ind 4. https:/	/doi.or	g/10.21	39/ss	rn.4603234
180.	Frederico	GF	(2023)	ChatGPT	in	supply	chains:	initial	evidence
of	applications	and	potential	research	agenda.	Logistics	7(2):26.
https:/	/doi.or	g/10.33	90/lo	gistics7020026
181.	Singh	G	(2023)	Leveraging	chatgpt	for	real-time	decision-mak-
ing in autonomous systems. Eduzone: Int Peer Reviewed/Refer -
eed	Multidiscip	J	12(2):101–106.	 h t t  p s : /  / d o  i . o  r g / 1 0 . 5 6 6 1 4 / e i p r m j
. v 1 2 i 2 . 4 0 7
182.	Wang	FY,	Yang	J,	Wang	X,	Li	J,	Han	QL	(2023)	Chat	with	Chat-
GPT on industry 5.0: learning and decision-making for intelligent
industries.	IEEE/CAA	J	Automatica	Sin	10(4):831–834.	 h t t  p s : /  / d
o		i	.	o		r	g	/	1	0	.	1	1	0	9	/	J	A	S	.	2	0	2	3	.	1	2	3	5	5	2
183.	Xu	X,	Lu	Y,	Vogel-Heuser	B,	Wang	L	(2021)	Industry	4.0	and
industry 5.0-inception, conception and perception. J Manuf Sys
61:530–535. https:/ /doi.or g/10.10 16/j. jmsy.2021.10.006
184. Dehghani F, Dehghani R, Naderzadeh Ardebili Y , Rahnamayan S
(2025)	Large	language	models	in	legal	systems:	a	survey.	Huma-
nit	Soc	Sci	Commun	12(1):1977.		h	t	t		p	s	:	/		/	d	o		i	.	o		r	g	/	1	0	.	1	0	5	7	/	s	4	1	5	9
9	-	0	2	5	-	0	5	9	2	4	-	3
185.	Frankenreiter	J,	Nyarko	J	(2022)	Natural	language	processing	in
legal	tech.	In:	Engstrom	D	(ed)	Legal	tech	and	the	future	of	civil
justice Forthcoming
186.	Nay	JJ	(2022)	Law	informs	code:	a	legal	informatics	approach	to
aligning	artificial	intelligence	with	humans.	Nw	J	Tech	Intell	Prop
20:309.	https:/	/doi.or	g/10.21	39/ss	rn.4218031
187.	Blair-Stanek	A,	Holzenberger	N,	Van	Durme	B	(2023	June)	Can
gpt-3 perform statutory reasoning? In: Proceedings of the Nine -
teenth	International	Conference	on	Artificial	Intelligence	and
Law,	pp	22–31
188. Guha N, Nyarko J, Ho D, Ré C, Chilton A, Chohlas-Wood A et
al	(2023)	Legalbench:	a	collaboratively	built	benchmark	for	mea-
suring legal reasoning in large language models. Adv Neural Inf
Process	Syst	36:44123–44279
189.	Hoffman	DA,	Arbel	Y	(2024)	Generative	interpretation.	New	Y	U
Law	Rev	451
190.	Siino	M,	Falco	M,	Croce	D,	Rosso	P	(2025)	Exploring	llms	appli-
cations in law: a literature review on current legal nlp approaches.
IEEE Access 13:18253–18276. 	h	t	t		p	s	:	/		/	d	o		i	.	o		r	g	/	1	0	.	1	1	0	9	/	A	C	C	E	S	S	.
2 0 2 5 . 3 5 3 3 2 1 7
191.	Dahl	M,	Magesh	V,	Suzgun	M,	Ho	DE	(2024)	Large	legal	fic-
tions:	profiling	legal	hallucinations	in	large	language	models.	J
Legal	Anal	16(1):64–93.	https:/	/doi.or	g/10.10	93/jl	a/laae003
192.	Magesh	V,	Surani	F,	Dahl	M,	Suzgun	M,	Manning	CD,	Ho	DE
(2025)	Hallucination-free?	Assessing	the	reliability	of	leading	AI
legal	research	tools.	J	Empir	Leg	Stud	22(2):216–242.	 h t t  p s : /  / d o  i
. o  r g / 1 0 . 1 1 1 1 / j e l s . 1 2 4 1 3
193.	Siino	M	(2025)	Exploring	the	use	of	LLMs	in	the	Italian	legal
domain:	a	survey	on	recent	applications.	Comput	Law	Secur	Rev
58:106164. https:/ /doi.or g/10.10 16/j. clsr.2025.106164
194.	Dou	L,	Dou	X	(2025)	Towards	just	AI:	challenges	and	solution
framework for algorithmic discrimination in judicial system. Int
J	Digit	Law	Governance	2(1):39–81.	 h t t  p s : /  / d o  i . o  r g / 1 0 . 1 5 1 5 / i j d l
g - 2 0 2 4 - 0 0 2 0
195.	Li	H,	Chen	J,	Yang	J,	Ai	Q,	Jia	W,	Liu	Y	et	al	(2025	Jul)	Legala-
gentbench: evaluating llm agents in legal domain. In Proceedings
of the 63rd Annual Meeting of the Association for Computational
Linguistics	(Volume,	1:	Long	Papers),	pp	2322–2344
196.	Shi	Y,	Liu	H,	Hu	Y,	Song	G,	Xu	X,	Ma	Y,	Wei	H	(2026)	PLaw-
Bench:	a	rubric-based	benchmark	for	evaluating	LLMs	in	real-
world legal practice. Preprint at https:/	/arxiv.	org/abs	/2601	.16669
197.	Kinchin	N	(2024)	“Voiceless”:	the	procedural	gap	in	algorithmic
justice.	Int	J	Law	Inf	Technol	32(1):eaae024.	 h t t  p s : /  / d o  i . o  r g / 1 0 . 1
0	9	3	/	i	j	l	i	t	/	e	a	a	e	0	2	4
198.	El	 Hamdani	 R,	 Bonald	 T,	 Malliaros	 FD,	 Holzenberger	 N,
Suchanek	F	(2024	Oct)	The	factuality	of	large	language	models
in the legal domain. In: Proceedings of the 33rd ACM Interna -
tional Conference on Information and Knowledge Management,
pp 3741–3746
199.	Sele	D,	Chugunova	M	(2024)	Putting	a	human	in	the	loop:
increasing uptake, but decreasing accuracy of automated deci -
sion-making.	PLoS	One	19(2):e0298037.	  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 3 7
1	/	j	o	u	r	n	a	l	.	p	o	n	e	.	0	2	9	8	0	3	7
200.	Norton	GW,	Alwang	J	(2020)	Changes	in	agricultural	extension
and implications for farmer adoption of new practices. Appl Econ
Perspectives	Policy	42(1):8–20.	 h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 0 2 / a e p p . 1 3 0
0 8
201. Tzachor A, Devare M, Richards C, Pypers P, Ghosh A, Koo J et
al	(2023)	Large	language	models	and	agricultural	extension	ser-
vices.	Nat	Food	4(11):941–948
202.	Punnappurath	 A,	 Abuolaim	 A,	 Abdelhamed	 A,	 Levinshtein
A,	Brown	MS	(2022)	Day-to-night	image	synthesis	for	train-
ing nighttime neural isps. In: Proceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition, pp
10769–10778
203.	Dai	H,	Liu	Z,	Liao	W,	Huang	X,	Cao	Y,	Wu	Z,	Li	X	(2025)
Auggpt: leveraging chatgpt for text data augmentation. In IEEE
Transactions on Big Data
204.	Sabu	KM,	Kumar	TM	(2020)	Predictive	analytics	in	agriculture:
forecasting prices of arecanuts in Kerala. Procedia Comput Sci
171:699–708.	https:/ /doi.or g/10.10 16/j. procs.2020.04.076
205.	Zhu	H,	Qin	S,	Su	M,	Lin	C,	Li	A,	Gao	J	(2024)	Harnessing	large
vision and language models in agriculture: a review. Preprint at
https:/	/arxiv.	org/abs	/2407	.19679.Front Plant Sci 16.  h t t  p s : /  / d o  i . o  r
g	/	1	0	.	3	3	8	9	/	f	p	l	s	.	2	0	2	5	.	1	5	7	9	3	5	5
206.	Stella	F,	Della	Santina	C,	Hughes	J	(2023)	How	can	LLMs	trans-
form	the	robotic	design	process?	Nat	Mach	Intell	5(6):561–564.
https:/	/doi.or	g/10.10	38/s4	2256-023-00669-7
207.	Zhang	L,	Chen	Z,	Ford	V	(2024)	Advancing	building	energy
modeling with large language models: exploration and case stud-
ies. Energ Build 323:114788.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 1 6 / j . e n b u i l d . 2 0
2 4 . 1 1 4 7 8 8
208.	Solovyeva	L,	Weidmann	S,	Castor	F	(2025)	AI-Powered,	but
power-hungry?	Energy	efficiency	of	LLM-Generated	code.	Pre-
print at https:/ /arxiv. org/abs /2502 .02412
209.	Khoshsirat	A,	Perin	G,	Rossi	M	(2024)	Decentralized	LLM	infer-
ence over edge networks with energy harvesting. Preprint at
https:/	/arxiv.	org/abs	/2408	.15907
210.	Gabber	HA,	Hemied	OS	(2024)	Domain-specific	large	language
model for renewable energy and hydrogen deployment strategies.
Energies	17(23):6063.	https:/	/doi.or	g/10.33	90/en	17236063
211.	Arslan	M,	Mahdjoubi	L,	Munawar	S	(2024)	Driving	sustainable
energy	transitions	with	a	multi-source	RAG-LLM	system.	Energ
Build 324:114827. https:/ /doi.or g/10.10 16/j. enbuild.2024.114827
212.	Hisaharo	S,	Nishimura	Y,	Takahashi	A	(2024)	Optimizing	llm
inference	clusters	for	enhanced	performance	and	energy	effi-
ciency. Authorea Preprints
213.	Jiang	P,	Sonne	C,	Li	W,	You	F,	You	S	(2024)	Preventing	the
immense increase in the life-cycle energy and carbon footprints

1 3
P . Peykani et al.
of llm-powered intelligent chatbots. Engineering 40:202–210.
https:/ /doi.or g/10.10 16/j. eng.2024.04.002
214. Peykani P, Emrouznejad A, Ghanidel S, Javadi-Sisi I, Mirjalili S
(2026)	Green	artificial	intelligence:	a	comprehensive	review	of
metrics, tools, challenges, trends, and future prospects. Archives
Comput Methods Eng 1–42.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 0 7 / s 1 1 8 3 1 - 0 2 6 -
1 0 5 4 6 - 2
215.	Buster	G,	Pinchuk	P,	Barrons	J,	McKeever	R,	Levine	A,	Lopez
A	(2024)	Supporting	energy	policy	research	with	large	language
models: a case study in wind energy siting ordinances. Energy AI
18:100431. https:/ /doi.or g/10.10 16/j. egyai.2024.100431
216.	Hong	J,	Tu	NV,	Hong	JWK	(2025)	A	comprehensive	survey	on
LLM-based	network	management	and	operations.	Int	J	Network
Manage	35(6):e70029
217. Mestres A, Rodriguez-Natal A, Carner J, Barlet-Ros P, Alarcón
E,	Solé	M,	Cabellos	A	(2017)	Knowledge-defined	networking.
ACM	SIGCOMM	Comput	Commun	Rev	47(3):2–10
218.	Siino	M,	Giuliano	F,	Tinnirello	I	(2025)	Integrating	large	lan-
guage models into network testbeds: a novel approach for auto -
mated experimentation and optimization. J Network Comput
Appl 243:104281. https:/ /doi.or g/10.10 16/j. jnca.2025.104281
219.	Letaief	KB,	Chen	W,	Shi	Y,	Zhang	J,	Zhang	YJA	(2019)	The
roadmap to 6G: AI empowered wireless networks. IEEE Com -
mun	Mag	57(8):84–90
220.	Manias	DM,	Chouman	A,	Shami	A	(2024	May)	Towards	intent-
based network management: large language models for intent
extraction in 5g core networks. In: 2024 20th International Con -
ference on the Design of Reliable Communication Networks
(DRCN),	IEEE,	pp	1–6
221.	Dwivedi	YK,	Kshetri	N,	Hughes	L,	Slade	EL,	Jeyaraj	A,	Kar	AK
et	al	(2023)	Opinion	paper:	“so	what	if	ChatGPT	wrote	it?”	Multi-
disciplinary perspectives on opportunities, challenges and impli -
cations of generative conversational AI for research, practice and
policy. Int J Inf Manage 71:102642
222.	Liu	T,	Wang	Z,	Qin	M,	Lu	Z,	Chen	X,	Yang	Y	et	al	(2025	Novem-
ber)	Real-time	ad	retrieval	via	llm-generative	commercial	inten-
tion for sponsored search advertising. In: Proceedings of the 2025
Conference	on	Empirical	Methods	in	Natural	Language	Process-
ing,	pp	28936–28948
223.	Sajja	R,	Sermet	Y,	Cikmaz	M,	Cwiertny	D,	Demir	I	(2024)	Artifi-
cial intelligence-enabled intelligent assistant for personalized and
adaptive	learning	in	higher	education.	Information	15(10):596.
https:/	/doi.or	g/10.33	90/in	fo15100596
224.	Maslej	N,	Fattorini	L,	Perrault	R,	Gil	Y,	Parli	V,	Kariuki	N	et	al
(2025)	Artificial	intelligence	index	report	2025.	Preprint	at	https:/
/arxiv.	org/abs	/2504	.07139
225. Thawakar OC, Shaker AM, Mullappilly SS, Cholakkal H, Anwer
RM,	Khan	S	et	al	(2024	August)	Xraygpt:	chest	radiographs	sum-
marization using large medical vision-language models. In: Pro -
ceedings of the 23rd workshop on biomedical natural language
processing, pp 440–448
226.	Yang	H,	Liu	XY,	Wang	CD	(2023)	Fingpt:	open-source	financial
large language models. Preprint at  h t t  p s : /  / a r  x i v  . o r  g / a  b s / 2  3 0  6 . 0 6 0
3 1  	h	t	t	p	s	:	/	/	d	o	i	.	o	r	g	/	1	0	.	2	1	3	9	/	s	s	r	n	.	4	4	8	9	8	2	6
227.	Wu	S,	Irsoy	O,	Lu	S,	Dabravolski	V,	Dredze	M,	Gehrmann	S
et	al	(2023)	Bloomberggpt:	a	large	language	model	for	finance.
Preprint at https:/ /arxiv. org/abs /2303 .17564
228.	Peifeng	LIU,	Qian	L,	Zhao	X,	Tao	B	(2024)	Joint	knowledge
graph and large language model for fault diagnosis and its appli -
cation	in	aviation	assembly.	IEEE	Trans	Ind	Inf	20(6):8160–8169
229.	Martínez	E	(2025)	Re-evaluating	GPT-4’s	bar	exam	performance:
E.	Martínez.	Artif	Intell	Law	33(3):581–604.	 h t t  p s : /  / d o  i . o  r g / 1 0 . 1
0	0	7	/	s	1	0	5	0	6	-	0	2	4	-	0	9	3	9	6	-	9
230.	Catterwell	R	(2020)	Automation	in	contract	interpretation.	Law
Innov	Technol	12(1):81–112.		h	t	t		p	s	:	/		/	d	o		i	.	o		r	g	/	1	0	.	1	0	8	0	/	1	7	5	7	9	9	6	1	.
2 0 2 0 . 1 7 2 7 0 6 8
231.	Ahmedm	Y,	Luan	R	(2026)	AgriM-LLM:	an	agriculture-specific
multimodal large language model for intelligent crop disease and
pest management
232. Kothalawala VN, Suzuki K, Nokelainen J, Hyvönen A,
Makkonen	I,	Barbiellini	B	et	al	(2024)	Compton	scattering	study
of	strong	orbital	delocalization	in	a	LiNiO	2	cathode.	Phys	Rev	B
109(3):035139
233.	Liao	W,	Bak-Jensen	B,	Pillai	JR,	Wang	Y,	Wang	Y	(2021)	A
review of graph neural networks and their applications in power
systems.	J	Mod	Power	Syst	Clean	Energy	10(2):345–360.	 h t t  p s : /  /
d o  i . o  r g / 1 0 . 3 5 8 3 3 / M P C E . 2 0 2 1 . 0 0 0 0 5 8
234.	Ethiraj	V,	Vijay	D,	Menon	S,	Berscilla	H	(2025)	Efficient	telecom
specific	llm:	tslam-mini	with	qlora	and	digital	twin	data.	Preprint
at https:/ /arxiv. org/abs /2505 .07877
235.	Schick	T,	Schütze	H	(2021)	Generating	datasets	with	pretrained
language models. Preprint at https:/ /arxiv. org/abs /2104 .07540
236.	Gao	T,	Fisch	A,	Chen	D	(2021	August)	Making	pre-trained	lan-
guage models better few-shot learners. In: Proceedings of the
59th	Annual	Meeting	of	the	Association	for	Computational	Lin-
guistics and the 11th International Joint Conference on Natural
Language	Processing	(Volume,	1:	Long	Papers),	pp	3816–3830
237.	De	Marneffe	MC,	Simons	M,	Tonhauser	J	(2019	Jul)	The	com-
mitmentbank: investigating projection in naturally occurring dis-
course.	Proc	Sinn	und	Bedeutung	23(2):107–124
238. Min B, Ross H, Sulem E, Veyseh APB, Nguyen TH, Sainz O et
al	(2023)	Recent	advances	in	natural	language	processing	via
large pre-trained language models: a survey. ACM Comput Surv
56(2):1–40
239.	Peng	K,	Ding	L,	Zhong	Q,	Shen	L,	Liu	X,	Zhang	M	et	al	(2023)
Towards making the most of chatgpt for machine translation. Pre-
print at https:/ /arxiv. org/abs /2303 .13780
240.	Liu	J,	Shen	D,	Zhang	Y,	Dolan	B,	Carin	L,	Chen	W	(2021)	What
makes good in-context examples for GPT-$3 $? Preprint at https:/
/arxiv. org/abs /2101 .06804
241.	Li	Y,	Ding	K,	Wang	J,	Lee	K	(2024)	Empowering	large	language
models for textual data augmentation. Preprint at  h t t  p s : /  / a r  x i v  . o r g
/ a b s / 2 4 0 4 . 1 7 6 4 2
242.	Yi	H,	Lin	F,	Li	H,	Ning	P,	Yu	X,	Xiao	R	(2024)	Generation	meets
verification:	accelerating	large	language	model	inference	with
smart parallel auto-correct decoding. Preprint at  h t t  p s : /  / a r  x i v  . o r g /
a	b	s	/	2	4	0	2	.	1	1	8	0	9
243.	Yuan	J,	Tang	R,	Jiang	X,	Hu	X	(2024	Jan)	Large	language	mod-
els for healthcare data augmentation: an example on patient-trial
matching. In: AMIA Annual Symposium Proceedings, vol 2023.
p 1324
244.	Kim	JH,	Kim	HR	(2024)	Cross-domain	knowledge	transfer	with-
out retraining to facilitating seamless knowledge application in
large language models
245.	Luo	L,	Ning	J,	Zhao	Y,	Wang	Z,	Ding	Z,	Chen	P	et	al	(2024)
Taiyi:	a	bilingual	fine-tuned	large	language	model	for	diverse	bio-
medical	tasks.	J	Am	Med	Inf	Assoc	31(9):1865–1874
246.	Li	XL,	Liang	P	(2021)	Prefix-tuning:	Optimizing	continuous
prompts for generation. Preprint at  h t t  p s : /  / a r  x i v  . o r g / a b s / 2 1 0 1 . 0 0
1	9	0
247.	Qin	L,	Chen	Q,	Feng	X,	Wu	Y,	Zhang	Y,	Li	Y	et	al	(2024)	Large
language models meet nlp: a survey. Preprint at  h t t  p s : /  / a r  x i v  . o r g /
a	b	s	/	2	4	0	5	.	1	2	8	1	9
248.	Fan	A,	Gokkaya	B,	Harman	M,	Lyubarskiy	M,	Sengupta	S,	Yoo
S	et	al	(2023	May)	Large	language	models	for	software	engineer-
ing: survey and open problems. In: 2023 IEEE/ACM Interna -
tional Conference on Software Engineering: Future of Software
Engineering	(ICSE-FoSE),	IEEE,	pp	31–53
249.	Zhou	W,	Kim	S,	Murali	V,	Aye	GA	(2022	May)	Improving	code
autocompletion with transfer learning. In: Proceedings of the 44th
International Conference on Software Engineering: Software
Engineering in Practice, pp 161–162

1 3
The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,…
250.	Fui-Hoon	Nah	F,	Zheng	R,	Cai	J,	Siau	K,	Chen	L	(2023)	Gen-
erative AI and ChatGPT: applications, challenges, and AI-human
collaboration.	J	Inf	Technol	Case	Appl	Res	25(3):277–304.	https:/
/doi.or g/10.10 80/15 228053.2023.2233814
251. Kazemitabaar M, Hou X, Henley A, Ericson BJ, Weintrop D,
Grossman	T	(2023	November)	How	novices	use	LLM-based
code generators to solve CS1 coding tasks in a self-paced learn -
ing environment. In: Proceedings of the 23rd Koli calling interna-
tional conference on computing education research, pp 1–12
252. Goodfellow I, Pouget-Abadie J, Mirza M, Xu B, Warde-Farley D,
Ozair	S	et	al	(2020)	Generative	adversarial	networks.	Commun
ACM	63(11):139–144
253.	Aydın	Ö,	Karaarslan	E	(2023)	Is	ChatGPT	leading	generative	AI?
What is beyond expectations? Academic Platf J Eng Smart Syst
11(3):118–134.	https:/	/doi.or	g/10.21	541/a	pjess.1293702
254.	Dasborough	MT	(2023)	Awe-inspiring	advancements	in	AI:	the
impact	of	ChatGPT	on	the	field	of	organizational	behavior.	J
Organ	Behav	44(2):177–179.	https:/	/doi.or	g/10.10	02/jo	b.2695
255.	Lee	BC,	Chung	J	(2024)	An	empirical	investigation	of	the	impact
of	ChatGPT	on	creativity.	Nat	Hum	Behav	8(10):1906–1914.
https:/	/doi.or	g/10.10	38/s4	1562-024-01953-1
256.	Shidiq	M	(2023	May)	The	use	of	artificial	intelligence-based
chat-gpt and its challenges for the world of education; from the
viewpoint of the development of creative writing skills. In: Pro -
ceeding of international conference on education, society and
humanity, vol 1, no 1. pp 353–357
257.	Whittaker	L,	Kietzmann	TC,	Kietzmann	J,	Dabirian	A	(2020)
“All around me are synthetic faces”: the mad world of AI-gener -
ated	media.	IT	Prof	22(5):90–99.		h	t	t		p	s	:	/		/	d	o		i	.	o		r	g	/	1	0	.	1	1	0	9	/	M	I	T	P	.	2
0	2	0	.	2	9	8	5	4	9	2
258.	Fan	W,	Ma	Y,	Li	Q,	Wang	J,	Cai	G,	Tang	J	et	al	(2020)	A	graph
neural network framework for social recommendations. IEEE
Trans	Knowl	Data	Eng	34(5):2033–2047
259.	Chen	X,	Fan	W,	Chen	J,	Liu	H,	Liu	Z,	Zhang	Z	et	al	(2023	April)
Fairly adaptive negative sampling for recommendations. In: Pro-
ceedings of the ACM Web Conference 2023, pp 3723–3733
260.	Dunn	A,	Dagdelen	J,	Walker	N,	Lee	S,	Rosen	AS,	Ceder	G	et	al
(2022)	Structured	information	extraction	from	complex	scientific
text	with	fine-tuned	large	language	models.	Preprint	at	 h t t  p s : /  / a r  x
i v  . o r g / a b s / 2 2 1 2 . 0 5 2 3 8
261.	Zhang	J,	Xie	R,	Hou	Y,	Zhao	X,	Lin	L,	Wen	JR	(2023)	Rec-
ommendation as instruction following: a large language model
empowered recommendation approach. ACM Trans Inf Syst
262.	Liu	P,	Zhang	L,	Gulla	JA	(2023)	Pre-train,	prompt,	and	recom-
mendation: a comprehensive survey of language modeling para -
digm adaptations in recommender systems. Trans Assoc Comput
Linguist	11:1553–1571.	https:/	/doi.or	g/10.11	62/ta	cl_a_00619
263.	Da’u	A,	Salim	N	(2020)	Recommendation	system	based	on	deep
learning methods: a systematic review and new directions. Artif
Intell	Rev	53(4):2709–2748.		h	t	t		p	s	:	/		/	d	o		i	.	o		r	g	/	1	0	.	1	0	0	7	/	s	1	0	4	6	2	-	0	1	9
-	0	9	7	4	4	-	1
264.	Sileo	D,	Vossen	W,	Raymaekers	R	(2022	April)	Zero-shot	recom-
mendation as language modeling. In: European Conference on
Information Retrieval, Springer International Publishing, Cham,
pp 223–230
265.	Li	L,	Zhang	Y,	Chen	L	(2023)	Personalized	prompt	learning	for
explainable	recommendation.	ACM	Trans	Inf	Syst	41(4):1–26.
https:/ /doi.or g/10.11 45/35 80488
266.	Wu	L,	Zheng	Z,	Qiu	Z,	Wang	H,	Gu	H,	Shen	T,	Chen	E	(2024)
Asurvey on large language models for recommendation. World
Wide	Web	27(5):60
267.	Geng	S,	Liu	S,	Fu	Z,	Ge	Y,	Zhang	Y	(2022	September)	Recom-
mendation	as	language	processing	(rlp):	a	unified	pretrain,	per-
sonalized	prompt	&	predict	paradigm	(p5).	In:	Proceedings	of	the
16th	ACM	conference	on	recommender	systems,	pp	299–315
268.	Wu	C,	Wu	F,	Qi	T,	Huang	Y	(2021	Jul)	Empowering	news	recom-
mendation with pre-trained language models. In: Proceedings of
the 44th international ACM SIGIR conference on research and
development in information retrieval, pp 1652–1656
269.	Yu	Y,	Wu	F,	Wu	C,	Yi	J,	Liu	Q	(2021)	Tiny-newsrec:	effective	and
efficient	plm-based	news	recommendation.	Preprint	at	 h t t  p s : /  / a r  x
i	v		.	o	r	g	/	a	b	s	/	2	1	1	2	.	0	0	9	4	4
270.	Liu	Q,	Zhu	J,	Dai	Q,	Wu	XM	(2022	Oct)	Boosting	deep	CTR
prediction with a plug-and-play pre-trainer for news recommen -
dation.	In:	Proceedings	of	the	29th	International	Conference	on
Computational	Linguistics,	pp	2823–2833
271.	Harper	FM,	Konstan	JA	(2015)	The	movielens	datasets:	history
and	context.	Acm	Trans	Interact	Intell	Syst	(Tiis)	5(4):1–19
272.	Gao	Y,	Sheng	T,	Xiang	Y,	Xiong	Y,	Wang	H,	Zhang	J	(2023)	Chat-
rec: towards interactive and explainable llms-augmented recom -
mender system. Preprint at https:/ /arxiv. org/abs /2303 .14524
273.	Shu	Y,	Zhang	H,	Gu	P,	Zhang	H,	Lu	T,	Li	D,	Gu	N	(2023)	Rah!
recsys-assistant-human: a human-central recommendation frame-
work	with	large	language	models.	CoRr	11(5):6759–6770.	 h t t  p s : /
/	d	o		i	.	o		r	g	/	1	0	.	1	1	0	9	/	T	C	S	S	.	2	0	2	4	.	3	4	0	4	0	3	9
274.	Shi	W,	He	X,	Zhang	Y,	Gao	C,	Li	X,	Zhang	J	et	al	(2024	Jul)
Large	language	models	are	learnable	planners	for	long-term	rec-
ommendation. In: Proceedings of the 47th International ACM
SIGIR Conference on Research and Development in Information
Retrieval,	pp	1893–1903
275.	Liu	J,	Liu	C,	Zhou	P,	Lv	R,	Zhou	K,	Zhang	Y	(2023)	Is	chatgpt	a
good recommender? a preliminary study. Preprint at  h t t  p s : /  / a r  x i v  .
o	r	g	/	a	b	s	/	2	3	0	4	.	1	0	1	4	9
276.	Hou	Y,	Zhang	J,	Lin	Z,	Lu	H,	Xie	R,	McAuley	J	et	al	(2024
March)	Large	language	models	are	zero-shot	rankers	for	rec-
ommender systems. In: European conference on information
retrieval, Springer Nature Switzerland, Cham, pp 364–381
277.	Acharya	A,	Singh	B,	Onoe	N	(2023	September)	Llm	based	gen-
eration of item-description for recommendation system. In: Pro -
ceedings of the 17th ACM conference on recommender systems,
pp 1204–1207
278.	Tsimpoukelli	M,	Menick	JL,	Cabi	S,	Eslami	SM,	Vinyals	O,	Hill
F	(2021)	Multimodal	few-shot	learning	with	frozen	language
models. Adv Neural Inf Process Syst 34:200–212
279.	Li	J,	Li	D,	Savarese	S,	Hoi	S	(2023	Jul)	Blip-2:	bootstrapping
language-image pre-training with frozen image encoders and
large language models. In: International conference on machine
learning,	PMLR,	pp	19730–19742
280.	Hu	R,	Singh	A	(2021)	Unit:	multimodal	multitask	learning	with
a	unified	transformer.	In:	Proceedings	of	the	IEEE/CVF	interna-
tional	conference	on	computer	vision,	pp	1439–1449
281.	Rotstein	N,	Bensaid	D,	Brody	S,	Ganz	R,	Kimmel	R	(2024)	Fuse-
cap: leveraging large language models for enriched fused image
captions. In: Proceedings of the IEEE/CVF winter conference on
applications	of	computer	vision,	pp	5689–5700
282.	Yang	Z,	Gan	Z,	Wang	J,	Hu	X,	Lu	Y,	Liu	Z	et	al	(2022	June)	An
empirical study of gpt-3 for few-shot knowledge-based vqa. In:
Proceedings	of	the	AAAI	conference	on	artificial	intelligence,	vol
36,	no.	3.	pp	3081–3089
283.	Chung	HW,	Hou	L,	Longpre	S,	Zoph	B,	Tay	Y,	Fedus	W	et	al
(2024)	Scaling	instruction-finetuned	language	models.	J	Mach
Learn	Res	25(219):1–71.	https:/ /doi.or g/10.15 61/22 00000050
284.	Hessel	J,	Holtzman	A,	Forbes	M,	Le	Bras	R,	Choi	Y	(2021
November)	 Clipscore:	 a	 reference-free	 evaluation	 metric	 for
image captioning. In: Proceedings of the 2021 conference on
empirical methods in natural language processing, pp 7514–7528
285.	Zang	Y,	Li	W,	Han	J,	Zhou	K,	Loy	CC	(2024)	Contextual	object
detection with multimodal large language models. Int J Comput
Vision	1–19
286.	Dorbala	VS,	Mullen	JF,	Manocha	D	(2023)	Can	an	embodied
agent	find	your	“cat-shaped	mug”?	llm-based	zero-shot	object

1 3
P . Peykani et al.
navigation.	IEEE	Robot	Autom	Lett	9(5):4083–4090.	 h t t  p s : /  / d o
i	.	o		r	g	/	1	0	.	1	1	0	9	/	L	R	A	.	2	0	2	3	.	3	3	4	6	8	0	0
287.	Ren	Z,	Su	Y,	Liu	X	(2023)	ChatGPT-powered	hierarchical	com-
parisons	for	image	classification.	Adv	Neural	Inf	Process	Syst
36:69706–69718
288.	Menon	S,	Vondrick	C	(2022)	Visual	classification	via	description
from large language models. Preprint at  h t t  p s : /  / a r  x i v  . o r g / a b s / 2 2 1
0 . 0 7 1 8 3
289.	Osco	LP,	Lemos	ELD,	Gonçalves	WN,	Ramos	APM,	MarcatoJu-
nior	J	(2023)	The	potential	of	visual	ChatGPT	for	remote	sensing.
Remote	Sens	15(13):3232
290.	Jeong	H,	Lee	H,	Kim	C,	Shin	S	(2024)	A	survey	of	robot	intel-
ligence	with	large	language	models.	Appl	Sci	14(19):8868.	 h t t  p s :
/		/	d	o		i	.	o		r	g	/	1	0	.	3	3	9	0	/	a	p	p	1	4	1	9	8	8	6	8
291.	Zhang	C,	Chen	J,	Li	J,	Peng	Y,	Mao	Z	(2023)	Large	language
models for human-robot interaction: a review. Biomimetic Intel
Robot	3(4):100131.	https:/ /doi.or g/10.10 16/j. birob.2023.100131
292.	Ahn	M,	Brohan	A,	Brown	N,	Chebotar	Y,	Cortes	O,	David	B	et
al	(2022)	Do	as	I	can,	not	as	I	say:	grounding	language	in	robotic
affordances.	Preprint	at	https:/	/arxiv.	org/abs	/2204	.01691
293.	Rana	K,	Haviland	J,	Garg	S,	Abou-Chakra	J,	Reid	I,	Suender-
hauf	N	(2023)	Sayplan:	grounding	large	language	models	using
3d scene graphs for scalable robot task planning. Preprint at  h t t  p s
: /  / a r  x i v  . o r g / a b s / 2 3 0 7 . 0 6 1 3 5
294.	Song	CH,	Wu	J,	Washington	C,	Sadler	BM,	Chao	WL,	Su	Y
(2023)	Llm-planner:	few-shot	grounded	planning	for	embodied
agents with large language models. In: Proceedings of the IEEE/
CVF	international	conference	on	computer	vision,	pp	2998–3009
295.	Driess	D,	Xia	F,	Sajjadi	MS,	Lynch	C,	Chowdhery	A,	Ichter	B,
Florence	P	(2023)	Palm-e:	an	embodied	multimodal	language
model. arXiv preprint arXiv:2303.03378
296.	Raman	SS,	Cohen	V,	Idrees	I,	Rosen	E,	Mooney	R,	Tellex	S
et	al	(2024	May)	Cape:	corrective	actions	from	precondition
errors using large language models. In: 2024 IEEE International
Conference	 on	 Robotics	 and	Automation	 (ICRA),	 IEEE,	 pp
14070–14077
297.	Li	P,	An	Z,	Abrar	S,	Zhou	L	(2025)	Large	language	models	for
multi-robot systems: a survey. Preprint at  h t t  p s : /  / a r  x i v  . o r g / a b s / 2 5
0 2 . 0 3 8 1 4
298.	Chen	ZZ,	Ma	J,	Zhang	X,	Hao	N,	Yan	A,	Nourbakhsh	A	et	al
(2024)	A	survey	on	large	language	models	for	critical	societal
domains:	finance,	healthcare,	and	law.	Preprint	at	 h t t  p s : /  / a r  x i v  . o r g
/	a	b	s	/	2	4	0	5	.	0	1	7	6	9
299.	Zhang	Y,	Li	Y,	Cui	L,	Cai	D,	Liu	L,	Fu	T	et	al	(2025)	  Siren’s
Song in the AI ocean: a survey on hallucination in large language
models.	Comput	Linguist	51(4):1373–1418
300.	Chen	Y,	Huang	G	(2024)	Guide:	a	global	unified	inference	engine
for deploying large language models in heterogeneous environ -
ments. Preprint at https:/ /arxiv. org/abs /2412 .04788
301.	Xi	Y,	Wang	H,	Chen	B,	Lin	J,	Zhu	M,	Liu	W	et	al	(2025	Jul)
Efficiency	unleashed:	inference	acceleration	for	LLM-based	rec-
ommender systems with speculative decoding. In: Proceedings of
the 48th International ACM SIGIR Conference on Research and
Development	in	Information	Retrieval,	pp	1891–1901
302. Jaillet P, Jiang J, Mellou K, Molinaro M, Podimata C, Zhou Z
(2025)	Online	scheduling	for	llm	inference	with	kv	cache	con-
straints. Preprint at https:/ /arxiv. org/abs /2502 .07115
303.	Özcan	M,	Wiesner	P,	Weiß	P,	Kao	O	(2025)	Quantifying	the
energy	consumption	and	carbon	emissions	of	LLM	inference	via
simulations. Preprint at https:/ /arxiv. org/abs /2507 .11417
304.	Fu	Y,	Panda	R,	Niu	X,	Yue	X,	Hajishirzi	H,	Kim	Y	et	al	(2024)
Data engineering for scaling language models to 128K context.
Proc	Mach	Learn	Res	235:14125–14134
305.	Yang	L,	Zhang	Z,	Chen	Z,	Li	Z,	Jia	Z	(2025	May)	Tidaldecode:
fast and accurate llm decoding with position persistent sparse
attention.	In:	International	Conference	on	Learning	Representa-
tions, vol 2025. pp 5823–5844
306.	Sclar	M,	Choi	Y,	Tsvetkov	Y,	Suhr	A	(2024	May)	Quantifying	lan-
guage models’ sensitivity to spurious features in prompt design
or: how I learned to start worrying about prompt formatting. In:
International	Conference	on	Learning	Representations,	vol	2024.
pp 25055–25083
307. Gallegos IO, Rossi RA, Barrow J, Tanjim MM, Kim S, Dernon -
court	F	et	al	(2024)	Bias	and	fairness	in	large	language	models:	a
survey.	Comput	Linguist	50(3):1097–1179
308.	Nadeem	M,	Bethke	A,	Reddy	S	(2021	August)	StereoSet:	mea-
suring stereotypical bias in pretrained language models. In:
Proceedings	of	the	59th	annual	meeting	of	the	association	for
computational linguistics and the 11th international joint confer -
ence	on	natural	language	processing	(volume	1:	long	papers),	pp
5356–5371
309.	Peykani	P,	Ramezanlou	F,	Tanasescu	C,	Ghanidel	S	(2025)	Large
language models: a structured taxonomy and review of chal -
lenges, limitations, solutions, and future directions. Appl Sci
(2076-3417)	15(14):8103.	https:/	/doi.or	g/10.33	90/ap	p15148103
310.	Pavlidis	G	(2024)	Unlocking	the	black	box:	analysing	the	EU
artificial	intelligence	act’s	framework	for	explainability	in	AI.
Law	Innov	Technol	16(1):293–308.	 h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 8 0 / 1 7 5 7
9	9	6	1	.	2	0	2	4	.	2	3	1	3	7	9	5
311.	Lin	Z,	Guan	S,	Zhang	W,	Zhang	H,	Li	Y,	Zhang	H	(2024)	Towards
trustworthy	LLMs:	a	review	on	debiasing	and	dehallucinating	in
large	language	models.	Artif	Intell	Rev	57(9).	 h t t  p s : /  / d o  i . o  r g / 1 0 . 1
0	0	7	/	s	1	0	4	6	2	-	0	2	4	-	1	0	8	9	6	-	y
312.	Ong	JCL,	Chang	SYH,	William	W,	Butte	AJ,	Shah	NH,	Chew
LST	et	al	(2024)	Ethical	and	regulatory	challenges	of	large	lan-
guage	models	in	medicine.	Lancet	Digit	Health	6(6):e428–e432
313.	Bergmanis	T,	Kronis	M,	Pretkalniņš	IJ,	Nicmanis	D,	Jeļinska
J,	Rozis	R	et	al	(2026)	TildeOpen	LLM:	leveraging	curriculum
learning to achieve equitable language representation. Preprint at
https:/ /arxiv. org/abs /2603 .08182
314.	Beibitkhan	AS	(2026)	Left	behind:	cross-lingual	transfer	as	a
bridge for low-resource languages in large language models. Pre-
print at https:/ /arxiv. org/abs /2603 .21036
315.	Tao	Y,	Viberg	O,	Baker	RS,	Kizilcec	RF	(2024)	Cultural	bias
and cultural alignment of large language models. PNAS Nexus
3(9):pgae346.	https:/	/doi.or	g/10.10	93/pn	asnexus/pgae346
316. Romanou A, Foroutan N, Sotnikova A, Nelaturu SH, Singh S,
Maheshwary	R	et	al	(2025	May)	Include:	evaluating	multilin-
gual language understanding with regional knowledge. In: Inter -
national	Conference	on	Learning	Representations,	vol	2025.	pp
83291–83322
317.	Imani	A,	Lin	P,	Kargaran	AH,	Severini	S,	Sabet	MJ,	Kassner	N
et	al	(2023)	Glot500:	scaling	multilingual	corpora	and	language
models to 500 languages. Preprint at  h t t  p s : /  / a r  x i v  . o r g / a b s / 2 3 0 5 . 1
2 1 8 2
318.	Lin	P,	Ji	S,	Tiedemann	J,	Martins	AF,	Schütze	H	(2024)	Mala-
500: massive language adaptation of large language models. Pre-
print at https:/ /arxiv. org/abs /2401 .13303
319.	Li	X,	Wang	S,	Zeng	S,	Wu	Y,	Yang	Y	(2024)	A	survey	on	LLM-
based	multi-agent	systems:	workflow,	infrastructure,	and	chal-
lenges.	Vicinagearth	1(1):9.	  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 0 7 / s 4 4 3 3 6 - 0 2 4
-	0	0	0	0	9	-	2
320.	Peykani	P,	Ghanidel	S,	Javadi-Sisi	I,	Snasel	V,	Mirjalili	S	(2026)
A holistic review of Agentic AI frameworks, applications, and
research trajectories. Archives Comput Methods Eng 1– 35.
https:/ /doi.or g/10.10 07/s1 1831-026-10675-8
321.	Chen	Y,	Pesaranghader	A,	Sadhu	T,	Yi	DH	(2024)	Can	we	rely	on
LLM	agents	to	draft	long-horizon	plans?	Let’s	take	TravelPlanner
as an example. Preprint at https:/ /arxiv. org/abs /2408 .06318
322.	Abou	Ali	M,	Dornaika	F,	Charafeddine	J	(2025)	Agentic	AI:	a
comprehensive survey of architectures, applications, and future

1 3
The Versatility of Large Language Models: A Comprehensive Review and Structured Survey of Architectures,…
directions.	Artif	Intell	Rev	59(1):11.	 h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 0 7 / s 1 0 4
6 2 - 0 2 5 - 1 1 4 2 2 - 4
323.	Farkaš	I,	Vavrečka	M,	Wermter	S	(2025)	Will	multimodal	large
language models ever achieve deep understanding of the world?
Front	Syst	Neurosci	19:1683133.		h	t	t		p	s	:	/		/	d	o		i	.	o		r	g	/	1	0	.	3	3	8	9	/	f	n	s	y	s	.	2
0 2 5 . 1 6 8 3 1 3 3
324.	Cong	Y,	Mo	H	(2025)	An	overview	of	robot	embodied	intelli-
gence based on multimodal models: tasks, models, and system
schemes.	Int	J	Intell	Syst	2025(1):5124400.	 h t t  p s : /  / d o  i . o  r g / 1 0 . 1 1
5 5 / i n t / 5 1 2 4 4 0 0
325.	Liu	NF,	Lin	K,	Hewitt	J,	Paranjape	A,	Bevilacqua	M,	Petroni	F
et	al	(2024)	Lost	in	the	middle:	how	language	models	use	long
contexts.	Trans	Assoc	Comput	Linguist	12:157–173.	 h t t  p s : /  / d o  i . o
r	g	/	1	0	.	1	1	6	2	/	t	a	c	l	_	a	_	0	0	6	3	8
326.	Qian	H,	Liu	Z,	Zhang	P,	Mao	K,	Lian	D,	Dou	Z	et	al	(2025	April)
Memorag: boosting long context processing with global memory-
enhanced retrieval augmentation. In: Proceedings of the ACM on
Web Conference 2025, pp 2366–2377
327.	Zhu	X,	Li	J,	Liu	Y,	Ma	C,	Wang	W	(2024)	A	survey	on	model
compression for large language models. Trans Assoc Comput
Linguist	12:1556–1577.	https:/	/doi.or	g/10.11	62/ta	cl_a_00704
328.	Liu	D,	Zhu	Y,	Liu	Z,	Liu	Y,	Han	C,	Tian	J	et	al	(2025)	A	survey
of model compression techniques: past, present, and future. Front
Robot	AI	12:1518965
329.	Passerini	A,	Gema	A,	Minervini	P,	Sayin	B,	Tentori	K	(2025)
Fostering	effective	hybrid	human-LLM	reasoning	and	decision
making.	Front	Artif	Intel	7:1464690.		h	t	t		p	s	:	/		/	d	o		i	.	o		r	g	/	1	0	.	3	3	8	9	/	f	r	a	i	.
2	0	2	4	.	1	4	6	4	6	9	0
330.	Ma	S,	Chen	Q,	Wang	X,	Zheng	C,	Peng	Z,	Yin	M	et	al	(2025
Apr)	Towards	human-ai	deliberation:	design	and	evaluation	of
llm-empowered deliberative ai for ai-assisted decision-making.
In: Proceedings of the 2025 CHI Conference on Human Factors
in Computing Systems, pp 1–23
331.	Li	H,	Tian	F	(2026)	Advancing	decision-making	through	AI-
human collaboration: a systematic review and conceptual frame -
work.	Group	Decis	Negot	35(2):26.	 h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 0 7 / s 1 0 7
2	6	-	0	2	6	-	0	9	9	8	0	-	1
332. Rahman SS, Islam MA, Alam MM, Zeba M, Rahman MA,
Chowa	SS	et	al	(2026)	Hallucination	to	truth:	a	review	of	fact-
checking and factuality evaluation in large language models. Artif
Intell	Rev	59(2).	https:   //d oi. or g/10 .100 7/ s10 462-0 25-11454-w
333.	Chen	S,	Chen	Y,	Li	Z,	Jiang	Y,	Wan	Z,	He	Y	et	al	(2025	Nov)
Benchmarking large language models under data contamination:
a survey from static to dynamic evaluation. In: Proceedings of
the	2025	Conference	on	Empirical	Methods	in	Natural	Language
Processing,	pp	10091–10109
Publisher’s Note Springer Nature remains neutral with regard to juris-
dictional	claims	in	published	maps	and	institutional	affiliations.
