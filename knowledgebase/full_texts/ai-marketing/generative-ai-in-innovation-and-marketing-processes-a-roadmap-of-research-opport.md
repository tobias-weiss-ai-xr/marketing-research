---
title: 'Generative AI in innovation and marketing processes: A roadmap of research opportunities'
url: https://doi.org/10.1007/s11747-024-01044-7
category: ai-marketing
subcategory: empirical
date: 2024-08
venue: Journal of the Academy of Marketing Science
authors:
- Paola Cillo
- Gaia Rubera
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s11747-024-01044-7.pdf
pages: 18
chars: 94927
fetched_at: '2026-11-08T13:40:04+00:00'
kb_version: 1
---

# Generative AI in innovation and marketing processes: A roadmap of research opportunities

ORIGINAL EMPIRICAL RESEARCH
Journal of the Academy of Marketing Science (2025) 53:684–701
https://doi.org/10.1007/s11747-024-01044-7
approximately $463 billion annually.1 While AI has changed
marketing activities in several ways, ranging from product
personalization (Chung et al., 2016) to service experience
(Noble & Mende, 2023), one of the most distinctive features
of GenAI is its capability to create novel content (Eapen
et al., 2023). Unsurprisingly, numerous firms have already
started using GenAI to perform key innovative marketing
activities. For instance, Coca Cola used GenAI to co-create
new beverages, such as its Coca-Cola Sugar Y3000. Simi -
larly, companies like Unilever, Nestlé, and Mondelez have
been using GenAI to create advertising.2 Despite the disrup-
tive potential of GenAI in marketing, the marketing litera -
ture that explores the impact of GenAI for consumers and
firms is still nascent (Huang & Rust, 2023; Li et al., 2024;
Reisenbichler et al., 2022), thus prompting this effort to pro-
pose a roadmap that describes both GenAI’s current status
as well as its potential to impact consumer and firm behav -
ior in innovation and marketing processes.
We start with a brief overview of the technical speci -
ficities of GenAI, as well as its capabilities and current
1 https://www.mckinsey.com/capabilities/growth-marketing-and-
sales/our-insights/.how-generative-ai-can-boost-consumer-marketing.
2  https://www.theverge.com/2023/8/18/23837273/
generative-ai-advertising-oreos-cadbury-watermarking.
Introduction
Generative AI (henceforth, GenAI) represents the latest
evolution in the field of Artificial Intelligence (AI) and is
a group of AI models designed to generate new content,
spanning text, images, and videos (Huang & Rust, 2023).
According to a recent McKinsey report, marketing is pro -
jected to be the most affected firm function by GenAI,
which is forecast to enhance marketing productivity by up
to 15% of the total marketing expenditure, amounting to
John Hulland served as Editor for this article.
  Paola Cillo
paola.cillo@unibocconi.it
Gaia Rubera
gaia.rubera@unibocconi.it
1 Department of Management & Technology, Bocconi
University, Via Roentgen 1, Milano 20121, Italy
2 DIR - Claudio Dematte’ Research Division, SDA Bocconi
School of Management, Via Sarfatti 10, Milano 20136, Italy
3 Department of Marketing, Bocconi University, Via Roentgen
1, Milano 20121, Italy
Abstract
Nowadays, we are witnessing the exponential growth of Generative AI (GenAI), a group of AI models designed to produce
new content. This technology is poised to revolutionize marketing research and practice. Since the marketing literature
about GenAI is still in its infancy, we offer a technical overview of how GenAI models are trained and how they pro -
duce content. Following this, we construct a roadmap for future research on GenAI in marketing, divided into two main
domains. The first domain focuses on how firms can harness the potential of GenAI throughout the innovation process.
We begin by discussing how GenAI changes consumer behavior and propose research questions at the consumer level.
We then connect these emerging consumer insights with corresponding firm marketing strategies, presenting research
questions at the firm level. The second set of research questions examines the likely consequences of using GenAI to
analyze: (1) the relationship between market-based assets and firm value, and (2) consumer skills, preferences, and role
in marketing processes.
Keywords Generative artificial intelligence · Innovation · Marketing strategy · Marketing capabilities · Firm value
Accepted: 22 July 2024 / Published online: 26 August 2024
© The Author(s) 2024
Generative AI in innovation and marketing processes: A roadmap of
research opportunities
Paola Cillo1,2 · Gaia Rubera2,3
1 3

Journal of the Academy of Marketing Science (2025) 53:684–701
limitations. Then, we propose research opportunities across
two main domains. First, we focus on GenAI’s potential to
alter both internal marketing activities that mainly deal with
innovation, as well those interface activities for which firms
try to leverage consumers’ creativity. With our research
questions, we aim to investigate how GenAI can impact
the entire innovation process, distinguishing among four
phases: developing, testing, communicating, and engaging
with the firm’s innovative output (Knight, 1967; Mumford
& Simonton, 1997; Rubera et al., 2016). We validate these
research questions via in-depth interviews with managers
from different industries, spanning from high-end fashion
and fast-moving consumer goods to insurance and utili -
ties. These interviews reveal that, beyond their interest in
understanding how to harness the innovative potential of
GenAI, managers are concerned with the effects of repeat -
edly using GenAI on marketing capabilities and consumer
behavior. Thus, we develop a second set of research ques -
tions to investigate the consequences of repeated GenAI use
by firms and consumers. For firms, we develop questions
related to the effects of employing GenAI on how marketing
contributes to create firm value. Similarly, for consumers,
we offer research questions related to the potential impact
of GenAI on consumer skills, preferences, and role in the
marketing processes.
This paper makes two main contributions to the market -
ing literature. First, several papers have offered a research
map for the applications of AI in marketing (Davenport et
al., 2020; Huang & Rust, 2021; Puntoni et al., 2021). These
papers mainly investigate either mechanical or thinking AI
(Huang & Rust, 2021). However, GenAI is a different type
of AI that is poised to transform marketing in a completely
different way. Recently, Huang and Rust ( 2023) have ana -
lyzed how GenAI can be used to move the customer along
the customer care journey. They consider GenAI as the most
advanced, so far, form of feeling AI. Complementing their
perspective, we analyze the impact of GenAI on a different
yet fundamental activity for firms (i.e., innovation). Sec -
ond, previous papers outlining research questions about the
effect of AI on marketing have focused on either the conse-
quences on firms’ activity (Davenport et al., 2020; Huang
& Rust, 2021, 2023) or consumer response (Puntoni et al.,
2021). This article aims to bridge these two perspectives
by developing research questions both at the consumer and
firm level. At the consumer level, we focus on how GenAI
can impact consumers’ creative behavior. Since firms try to
leverage consumer input throughout the innovation process,
we maintain that analyzing the potential impact of GenAI
on consumers’ creative behavior is a prerequisite for inves-
tigating the impact of GenAI on the firm innovation process
(Hamilton, 2016). In this way, we hope that this roadmap
can help marketing scholars pursue research across various
areas of specialization.
GenAI: A technical overview
In technical terms, we can define GenAI as deep neural
networks, pre-trained on large amounts of data to create a
foundation model, which is then fine-tuned to produce new
content by following human instructions (Bommasani et
al., 2021). In this section, we provide a technical overview
of how GenAI models are trained and how they produce
content. Given these technical specificities, we then explain
why the output of GenAI can be helpful for firms, as it is
both novel and appropriate–and, hence, creative (Amabile,
2018; Scopelliti et al., 2014).
Training on extensive, unannotated datasets: Self-
supervised learning
GenAI is the outcome of a renewed focus on self-super-
vised machine learning rather than the supervised learning
approach that characterized much previous AI develop -
ments (Bommasani et al., 2021). In a supervised learning
approach, during the training, machines learn by comparing
model output against a given correct answer. These correct
answers are provided in forms of “labels” or “annotations,”
which require human involvement in labor-intensive tasks.
The significant cost of annotation severely restricts the vol-
ume of data available for model training, limiting the ability
to generalize effectively to novel settings (Bommasani et al.,
2021).
In contrast, self-supervised learning models are trained
with no need for annotated datasets. Instead, training occurs
by removing parts of the data and asking the model to “pre-
dict” the missed parts. For instance, with textual data, we
can input a sentence like “This is a <…> article” and train
a model to predict the omitted word, given its surround -
ing text. At the end of the training, the model should have
learned that the words “review” or “scientific” are more
likely to be omitted compared to, say, “umbrella.” Similarly,
with images, we can mask some patches and train a model
to predict the content in the masked patches based on the
remaining image information.
Self-supervised training yields two direct consequences
that define GenAI’s ability to generate new, plausible con -
tent. First, since the original data contains the correct part
to predict (i.e., the missing part), the training process can
scale to very large datasets, which would be challenging
to annotate by hand. These large datasets come in many
forms, such as text, images, audio recordings, and videos.
Second, by being forced to predict parts of the inputs, self-
supervised learning models develop a deeper understanding
1 3
685

Journal of the Academy of Marketing Science (2025) 53:684–701
of the context. This enhanced understanding, coupled with
training on significantly larger datasets, makes it easier to
generalize to novel settings than was the case with past,
supervised AI models.
Producing new content: Inherently random and
conditional on the prompt
The adoption of a self-supervised learning approach, cou -
pled with advancements in computing power (e.g., GPU)
and a novel model architecture known as Transformer (Vas-
wani et al., 2017) that allows faster training, led to the emer-
gence of foundation models. A foundation model is a large,
pre-trained model used as a base for developing more spe -
cialized and task-specific models (Bommasani et al., 2021).
Foundation models underpin generative capabilities. Spe -
cifically, they create new content (e.g., text, image, video,
data) by using patterns learned during training to predict the
next item in a sequence. For instance, OpenAI and Micro -
soft have deployed GPT-3 in a variety of downstream tasks,
such as Bing, Duolingo, GitHub Co-pilot, and ChatGPT. To
understand how foundation models produce new content,
let us take the example of Large Language Models (LLMs),
a subset of foundation models that have gained significant
prominence as they are trained to facilitate user interac -
tion through natural language. A language model (LM) is
a statistical representation of a language, which computes
the probability of a given sequence (a word, phrase, or sen-
tence) occurring in this language. Similar to LMs, LLMs
are trained in a self-supervised logic to predict a masked
word within a sequence of words. Because they are trained
on large amounts of data as well as frequently trained on
different languages, they are called Large LMs. If we con -
sider words and punctuation signs as tokens, we can depict
an LLM as a conditional probability distribution p(xn|x1, …,
xn − 1) over tokens, in which each xi is drawn from a fixed
vocabulary. An LLM generates text by iteratively sampling
from the learned distribution to select the next token. At
each generative iteration, the model estimates a probability
distribution, indicating the likelihood that any token in the
vocabulary would be the next observed xi if the model were
reading a pre-existing text. To initiate text generation, an
LLM requires “conditioning,” meaning it must be supplied
with initial input tokens x1, …, xn − 1. Such input is called
prompt. The prompt conditions the probability of selecting
one token over another. For instance, if we input the prompt
“This is a review…,” the token “article” would have a higher
probability of selection than the token “bus.” Using a distri-
bution function, the model randomly selects among a list
of probable candidates (e.g., “article,” “paper”). The new
xi is then added to the text, initiating the repetition of the
entire process (Argyle et al., 2023). The generation of novel
images, music, videos, or data follow a similar approach.
Thus, GenAI outputs novel content that is conditional on
the prompt that it receives. Given how foundation models
choose the next word, note, or image feature, such content
however is random and different at each iteration, making it
possible to produce several, unique responses from the same
prompt. This inherent randomness explains why it is hard to
detect content generated by GenAI (Else, 2023).
In sum, training foundation models is a highly resource-
intensive process that demands substantial computational
power and can take months to complete. For instance, it is
estimated that the cost of training GPT-4 is over $100 mil -
lion (Korinek, 2023). However, while training GenAI is
financially viable for only a handful of companies, use costs
are very low. Thus, firms no longer compete on developing
proprietary machine learning and AI algorithms, but rather
on their ability to fully harness the capabilities of existing
foundation models.
The potential of GenAI for marketing and
innovation
Having reviewed how GenAI models are trained and how
they produce new content, we next describe the capabili -
ties and current limitations of these models. Huang and Rust
(2023) conceptualize GenAI as feeling AI, namely a type of
AI that can communicate and interact with humans based on
an emotional understanding derived from analyzing emo -
tion data. They argue that these models differ from previ -
ous AI models, which were better suited for mechanical
AI (i.e., performing repetitive tasks) and thinking AI (i.e.,
supporting analytical decisions) (Huang & Rust, 2021).
We embrace their view of GenAI as a novel type of AI; to
complement this view, we focus on GenAI’s capability to
create new content. Since we are interested in how firms
can leverage GenAI in their innovation and marketing pro -
cesses, we examine whether GenAI’s output can be both
novel and appropriate, two key elements that influence con-
sumer evaluations of new products, marketing programs,
and advertisements (Rubera et al., 2010).
The associate theory of creativity maintains that novelty
stems from the ability to connect weakly related concepts to
form novel ideas (Dahl & Moreau, 2002; Toubia & Netzer,
2017). Since foundation models have been trained on exten-
sive datasets, these models can retrieve concepts from a
vast array of diverse domains. Leveraging this capability,
scientists started exploring how LLMs can be used to dis -
cover new hypotheses to test (Hutson, 2023). The inherent
randomness in the way foundation models produce content
is a prerequisite for identifying this output as novel. Indeed,
throughout history, significant innovations have emerged
1 3
686

Journal of the Academy of Marketing Science (2025) 53:684–701
launched ChatGPT, OpenAI explicitly acknowledged that it
could make mistakes. The Bard and Galactica cases clearly
indicate the limitations of initial GenAI. It works better
when it is tasked with generating novel content for which
there are no right or wrong answers (e.g., artistic content,
novel product ideas).
To help marketers apply GenAI effectively, we provide
in Table 1 a summary of studies that investigate GenAI’s
emergent capabilities that are most closely related to inno -
vation. These capabilities include idea generation, diver -
gent thinking, analogical thinking, and inductive reasoning,
which are all traditionally considered prerequisites for cre -
ativity (Dahl & Moreau, 2002; Vartanian et al., 2003). Addi-
tionally, our interviews reveal that an increasing number of
managers rely on GenAI, or wish to, for decision-making
support. Therefore, we also focus on capabilities related to
reasoning, such as causal reasoning, logical reasoning on
new cases, and making causal inferences.
Since different foundation models are trained on differ -
ent data and have different architectures, and also since the
same released model can be updated over time, we report
the model used and time of the test. Table 1 indicates that
current models have limited reasoning capabilities with
respect to making causal inferences. Computer scientists
attribute hallucinations and these limitations to the absence
of physical data in most GenAI models, which constrains
their understanding of the world (Webb et al., 2023; Zečević
et al., 2023). Indeed, most studies conducted so far have
focused on LLMs trained exclusively on text-based inputs,
which lack embodiment, sensory stimuli, or grounded expe-
rience that are crucial for human decision-making (McClel-
land et al., 2020). However, the emergence of multimodal
models like GPT-4 V(ision) (i.e., capable of processing text,
image, sound, and other sensory data) may pave the way for
GenAI to develop a more integrated understanding of the
world (McClelland et al., 2020; Webb et al., 2023). Thus,
we note that GenAI is rapidly evolving and that these limita-
tions could potentially be addressed in the future.
Research opportunities
Given our focus on GenAI’s capability to create new con -
tent, we propose research opportunities related to how firms
can harness the innovative potential of GenAI throughout
the firm innovation process. Consistent with past views of
the innovation process (Knight, 1967; Mumford & Simon -
ton, 1997; Rubera et al., 2016), we depict this process as a
circular one that encompasses four main stages–developing,
testing, communicating, and engaging–during which firms
interact with customers to gain different types of input,
ranging from creativity to customer knowledge.
as serendipitous discoveries, ranging from medical break -
throughs (Meyers, 2007) to new consumer products like
Post-its or shatter-proof glass.
However, randomly connecting concepts from different
domains is not sufficient per se for generating something
that consumers appreciate; rather, this content must also be
appropriate (Rubera et al., 2010). Since foundation models
have been trained on extensive datasets, it is very likely that
they have memorized in the training phase what humans
consider to be appropriate. Girotra et al. ( 2023) conducted
a comparative study, pitting a pool of ideas generated by
MBA students against those generated by ChatGPT-4 in two
distinct conditions. In the baseline condition, ChatGPT-4
received an identical prompt to that of the MBA students
(i.e., generate ten ideas targeting college students in the
U.S.). In the “prompted with good examples” condition,
the authors supplemented the prompt with a set of highly
rated ideas. They find that ideas generated by ChatGPT-4,
regardless of the condition, exhibit higher average scores on
purchase intentions compared to ideas generated by MBA
students. Interestingly, they report no significant differ -
ence between the two GPT conditions (i.e., baseline versus
prompted with highly rated ideas). A possible explanation
for this finding is that GPT had already seen those highly
rated ideas (or, at least, similarly appropriate ideas) during
the training. Thus, providing further examples of good ideas
in the prompt is redundant, as GPT has already memorized
what humans consider to be appropriate.
In sum, the stochastic nature of foundation models
enables them to generate novel content. The extensiveness
of the data they have been trained on allows this novelty to
also be appropriate.
Current limitations of GenAI
Although GenAI is able to create new content, it sometimes
produces content that, while semantically or syntactically
plausible, is factually incorrect or nonsensical (i.e., halluci-
nations) (Huang & Rust, 2023). For instance, on February
6, 2023, Google announced its ChatGPT competitor named
Bard with an image of Bard answering the question “What
new discoveries from the James Webb Space Telescope can
I tell my 9 year old about?” As several astronomers pointed
out, one of the three replies that Bard provided was factually
wrong. As a consequence, Google stocks lost $100 billion.
Similarly, just two weeks before OpenAI launched Chat -
GPT, Meta released Galactica, which the company posi -
tioned as a “large language model for science.” The open
source LLM survived for only three days before Meta with-
drew it in response to criticism for releasing a model that
produced scientific-sounding text but that was nonetheless
factually wrong. Capitalizing on Galactica’s failure when it
1 3
687

Journal of the Academy of Marketing Science (2025) 53:684–701
initiatives aim to augment internal creativity with customer
ideas. In the testing stage, firms conduct market research to
gain customers’ perspective in order to select the one with
the best chances of meeting market needs, given the various
inputs generated in the previous phase (Kahn et al., 2006).
In the communicating stage, firms interact with customers
to persuade them to change their behavior and adopt the
firm’s offering (Castaño et al., 2008). After consumers buy
the firm’s novel offering, firms continue interacting with
customers to keep them engaged beyond economic trans -
actions (Blut et al., 2023; Pansari & Kumar, 2017). This
engagement enables firms to access key consumer resources
(e.g., knowledge stores, creativity) (Harmeling et al., 2017)
that offer further creative input to the innovation process,
thus constituting a continuous cycle, as illustrated in Fig. 1.
For each phase, we start by discussing the potential
impact of GenAI on consumer behavior and propose con -
sumer-level research questions. The only exception is the
testing stage in which, as we will discuss, GenAI can help
firms partially replace customer inputs when conducting
market research. These customer insights help us investigate
how firms can harness the innovative potential of GenAI.
In so doing, we bridge these emerging customer insights
with corresponding firm marketing strategies, presenting
research questions at the firm level (Hamilton, 2016). We
summarize our proposed research questions in Table 2.
We validated these research questions via in-depth inter-
views with managers from different industries, spanning
from high-end fashion and fast-moving consumer goods to
insurance and utilities. They point out that firms’ repeated
use of GenAI will fundamentally alter marketing capabili -
ties, for instance by making some of them obsolete or less
valuable. Also, they expect that consumers’ skills and pref-
erences will likely change as an effect of widespread GenAI
use. Thus, they fear that firms will necessarily face a very
different customer in the near future. The inputs from prac -
titioners motivated us to complement our framework with
research questions about the consequences of GenAI use,
both for a firm’s market-based assets, marketing capabili -
ties, and resources, as well as for consumer skills, prefer -
ences, and role in the marketing processes. We present our
roadmap in Fig. 1.
Harnessing the innovative potential of GenAI
Our framework views the innovation process as a circular
process that encompasses several interactions with custom-
ers throughout the four stages. In the developing phase,
firms frequently involve consumers in co-creation activi -
ties through open innovation platforms and crowdsourcing
initiatives (Bayus, 2013; Cillo et al., 2021; Luo & Toubia,
2015; Rubera et al., 2016; Stephen et al., 2016). These
Table 1 Emergent capabilities of GenAI
Capability Main finding Reason Source Model and Test-time
Generate ideas
for new products
GenAI generates ideas that receive higher
purchase intentions by potential consumers
In creative problem-solving, variability in
quality, and productivity (i.e., the number
of ideas generated) are more valuable than
consistency
Girotra et
al. (2023)
ChatGPT-4 (July
2023)
Divergent
thinking
GenAI is better than humans on average,
but not consistently better than best human
performers
Speed in accessing large data structures Koivisto
and Gras-
sini (2023)
ChatGPT3
(30.3.2023)
ChatGPT4 (5.4.2023)
Copy.Ai
(1.4.- 2.4.2023)
Analogical
reasoning
GenAI solve analogies through associa-
tive process (like children do) rather than
through relational mapping (like adults do)
LLMs relies on semantic similarity
between analogy terms
Steven-
son et al.
(2023)
Different LLMs
(October 2023)
Inductive
reasoning
GenAI matches human performance GenAI fails to reason about how the prem-
ises of an inductive argument are generated
Han et al.
(2024)
gpt-4-0314 (March
2024)
Causal
reasoning
GPT3 often showcase human-like biases in
causal reasoning tasks
LLMs might have memorized answers
during training or they could follow
human-like cognitive processes
Binz and
Schulz
(2023)
OpenAI GPT-3
models
Logical reason-
ing on new
cases
GenAI attains near-perfect accuracy on in-
distribution test examples while failing to
generalize to other data distributions over
the exact same problem space
Instead of learning the correct reasoning
function, LLMs have learned statistical
patterns in logical reasoning problems
Zhang et
al. (2022)
BERT (August 2023)
Making causal
inferences
LLMs perform well on causal inference
tasks only occasionally
Current LLMs are unable to process
physical data measurements to ground
their available textual facts
Zečević et
al. (2023)
GPT-3 (August 2023)
Luminous (August
2023)
OPT (August 2023)
Notes We report the date of the test because foundation models (such as GPT) change with no announcement and provide different results over
time
1 3
688

Journal of the Academy of Marketing Science (2025) 53:684–701
Table 2 Harnessing the innovative potential of GenAI: Research questions
Phase of the
innovation
process
Level of
analysis
Research questions
Developing Consumer • Through what cognitive mechanisms does GenAI influence the creativity of an individual consumer?
• Do different consumers follow different cognitive mechanisms?
• What individual traits and contextual factors influence consumer inclination to either conform to or diverge
from GenAI solutions?
Firm • How can firms design co-ideation platforms to reduce the AI-conformity effect?
Testing Firm • What market research can be conducted with GenAI rather than human participants or experts?
• What are the boundary conditions of GenAI’s capability to replace human subjects/experts in market
research?
• How can we assemble different LLMs to better replicate human /expert responses?
Communicating
(Persuading)
Consumer • Does variation in objective LLM parameters translate into differing subjective perceptions of persuasiveness?
• What are the theoretical mechanisms through which objective LLM parameters influence subjective
perceptions?
• What theoretical constructs cause heterogeneity in consumer responses to variations of objective LLM
parameters?
Firm • How can firms vary LLM parameters to create more persuasive messages?
• Which LLM parameter is most conducive to different marketing goals?
Communicating
(Disclosing)
Consumer • Do consumers respond differently to the disclosure of GenAI compared to the disclosure of other types of AI?
• What novel theoretical mechanisms explain consumer responses to a firm’s disclosure of GenAI-generated
content?
Firm • Which brand associations amplify the negative effect of GenAI disclosure on brand equity? Which associa-
tions mitigate this effect?
• How can firms align disclosure messages to their firm brand associations to mitigate the potential negative
effect of disclosing GenAI use?
Engaging Consumer • What are the consequences of employing GenAI tools for consumers working on customer engagement
initiatives?
Firm • What novel, task-based customer engagement strategies can firms pursue using GenAI?
• How can firms manage the trade-off between wider reach and customer engagement of GenAI, task-based
initiatives?
Fig. 1 GenAI in innovation and marketing processes

1 3
689

Journal of the Academy of Marketing Science (2025) 53:684–701
to empirically investigate the mechanisms that increase the
creativity of the final, GenAI-augmented solution for differ-
ent types of consumers:
RQ Through what cognitive mechanisms does GenAI influ-
ence the creativity of an individual consumer? Do differ-
ent consumers follow different cognitive mechanisms?
Luo and Toubia (2015) show that domain knowledge deter-
mines whether consumers fixate with others’ ideas or not.
Lysyakov and Viswanathan ( 2023) find that prior success
determines whether designers conform or diversify in
response to the introduction of an AI system for logo designs
in a crowdsourcing design platform. Thus, future research
should investigate the elements (individual or contextual)
that encourage consumers to either conform or diversify to
solutions proposed by GenAI:
RQ What individual traits and contextual factors influence
a consumer’s decision to either conform to or diverge
from GenAI solutions?
At the firm level, the path that consumers pursue (i.e., AI
conformity or diversification) has direct consequences on
the collective creativity of the pool of co-produced ideas
from which a firm can select, which is a key output of co-
ideation initiatives. Since consumers who conform select
solutions from the same (or similar) GenAI-generated con -
tent, it is likely that these conforming consumers end up
generating similar content, as they are anchored to the same
set of GenAI-generated ideas. Indeed, studies on ideation
platforms have shown that when customers draw inspira -
tion from similar sets of ideas, they tend to develop less
innovative ideas (Stephen et al., 2016). If this is the case,
then co- ideation initiatives bear ideas that are not creative
enough to warrant further internal development, a common
problem for these initiatives (Stephen et al., 2016). To curb
this drawback, scholars suggest that firms limit the quantity
of others’ ideas that participants can access (Luo & Tou -
bia, 2015; Stephen et al., 2016). Such a feature is clearly
not possible for GenAI, as consumers access it on their own
device. Further, the fact that consumers conform to solu -
tions proposed by GenAI defies the purpose of co-ideation
initiatives: employees within the firm can access these ideas
directly without tapping into consumers’ creative resources.
Huang and Rust ( 2023) propose an intriguing approach,
which they call response engineering , in which GenAI
probes consumers’ preferences iteratively through multiple
rounds of question-asking. Firms could employ a similar
response engineering approach in which GenAI asks ques -
tions (rather than provides answers) that would nudge con -
sumers to deviate from the original idea in order to help
Developing
In the past decade, firms have devoted much effort in involv-
ing consumers in the idea development phase through open
innovation platforms and crowdsourcing initiatives (Bayus,
2013; Luo & Toubia, 2015; Stephen et al., 2016). Through
these initiatives, firms outsource to consumers either part
of or the entire creative process, which comprises two
cognitive, iterative processes: generative and exploratory
(Moreau & Dahl, 2005). In the generative stage, prelimi -
nary mental representations of a solution are created. In the
exploratory stage, these representations are evaluated. If the
exploration is not successful, a new generative stage occurs
until a satisfactory idea is achieved.
While past studies investigated how AI can enhance idea
screening (Bell et al., 2023), GenAI can clearly support par-
ticipants in the idea-generation phase. Specifically, GenAI
can potentially decouple the two cognitive processes that
underpin creativity: it can create differing solutions (i.e.,
generation), while consumers then can be solely responsible
for modifying the proposed solutions (i.e., exploration). In
this case, we envision an iterative process in which con -
sumers engage in a conversation with GenAI to refine the
created solutions until a satisfactory idea emerges. Future
research is needed to investigate the consequences of this
decoupling at both the consumer and firm level.
At the consumer level, the literature indicates that peo -
ple’s ideas are influenced by those around them who are
working on the same task (Mason & Watts, 2012; Stephen
et al., 2016). Exposure to others’ ideas might lead consum -
ers to engage in either cognitive fixation (Bayus, 2013) or
cognitive stimulation (Luo & Toubia, 2015). Thus, we can
expect consumers to either conform to a GenAI suggestion
or further diversify in their efforts to reaffirm their diversity
from machines. We theoretically expect that both conform-
ing and diversifying consumers achieve higher levels of cre-
ativity when supported by GenAI, but through two different
mechanisms.
Conforming consumers outsource the generative stage to
GenAI. Since GenAI is trained on very diverse data, it can
provide conforming consumers with more diverse, initial
representations of a solution from which these consumers
can select in the exploratory stage. Since they can select
from a wider pool of ideas, doing so should translate to a
final solution that is more creative than if consumers had no
access to GenAI input (Dahl & Moreau, 2002). In contrast,
diversifying consumers engage further in the generative
stage in order to find more initial representations that differ
from GenAI input. This extra cognitive effort would encour-
age diversifying consumers to explore more distant alterna-
tives, thereby increasing the creativity of the final solution
(Luo & Toubia, 2015). However, future research is needed
1 3
690

Journal of the Academy of Marketing Science (2025) 53:684–701
to involve human subjects. Indeed, an emerging body of
studies has begun investigating how LLMs can substitute
for market research. Brand et al. ( 2023) show that when
prompted as if it were a randomly selected customer, GPT
generates responses that exhibit sloped demand curves,
lower sensitivity to changes in price as income increases,
and state dependency (i.e., inertia in their product choice),
all three of which are well-known features of real custom -
ers. Given these characteristics, the authors show that GPT
generates estimates that are similar to those generated by
human-based conjoint studies; they thus conclude that
GenAI can represent a viable alternative for learning about
consumer preferences in a fast, low-cost, and iterative way.
Similarly, Li et al. (2024) show that GPTNeo and GPT4 can
successfully match perceptual maps obtained from human
surveys. The authors also show that these two GenAI appli-
cations can replicate survey differences along demographic
variables and across time. Finally, Ringel ( 2023) investi -
gates whether ChatGPT-4 can act as a surrogate for human
expertise in classifying tweets that discuss marketing mix
variables. He finds strong agreement between labels pro -
vided by ChatGPT4 and those provided by experts across all
four metrics of the marketing mix, while labels provided by
Amazon mTurk workers exhibit substantially lower agree -
ment with expert labels. He concludes that “generative AI is
a viable alternative to scarce and costly domain experts for
labeling text.”
Collectively, this emerging research suggests that GenAI
can substitute, at least in some cases, for human subjects
and experts in marketing research. It is, thus, important to
investigate what other marketing variables or constructs
marketers can obtain through GenAI that will reduce the
need to refer to surveys, focus groups, or expert opinions.
Thus, we propose the following research question:
RQ What market research can be conducted with GenAI
rather than human participants or experts?
As research about GenAI’s capability to replace human
subjects emerges, it is important to keep in mind that this
capability depends on the training data of the foundation
model deployed to “conduct” market research. Indeed,
Horton (2023) infer from OpenAI’s GPT replies that these
LLMs must have been trained on a corpus more comparable
to revealed preferences than to stated ones. Also, Li et al.
(2024) report that LLMs work better for higher involvement
products and for some brands than others. We speculate that
this finding is due to the fact that GPT4 has more product
reviews for these products in its training sample. However,
future research is needed to determine which product cat -
egories/brands GenAI is better suited to replace human sub-
jects /experts:
them develop, at each iteration, more creative ideas. That
said, this is a workaround solution at the moment because
GenAI is not designed to ask questions (Huang & Rust,
2023). Thus, future research should investigate:
RQ How can firms design co-ideation platforms to reduce
the AI-conformity effect?
Testing
The generation phase is typically considered a variation
phase, during which firms are concerned with simply gen -
erating as much creative input as possible (Girotra et al.,
2010). In the next stage, a selection process starts, which
is aimed at selecting the idea with the highest chance of
gaining market acceptance once it is introduced in the mar-
ket (Girotra et al., 2010). To do so, firms conduct market
research (Kahn et al., 2006). The latest research on GenAI
suggests that this technology can offer firms several ways to
conduct market research.
Marketing research has shown how AI can lead to biased
outcomes in service (Ukanwa & Rust, 2020) or ad deliv -
ery (Lambrecht & Tucker, 2019). Such bias derives from
“algorithmic bias,” in which machine learning models tend
to replicate the gender, race, and economic biases of the data
upon which they have been trained (Davenport et al., 2020;
Plangger et al., 2022). However, LLMs have been trained
on a vast set of diverse data, which means that they poten -
tially could have memorized several biases, not just one. If
true, then researchers can take advantage of this variety of
biases to replicate different marketing sub-populations of
consumers (i.e., different consumer segments). Investigat -
ing this possibility, Argyle et al. (2023) show that LLMs are
characterized by what they call algorithmic fidelity: namely,
“by conditioning a model on simulated ’individuals’ with
targeted identity and personality profiles,” it is possible to
gain insights “into different patterns of attitudes and ideas
present across many groups (e.g., women, men, White peo-
ple, people of color, millennials, baby boomers) and also the
combination and intersection of these groups (e.g., Black
immigrants, female Republicans, White males) (p. 338).”
Leveraging algorithmic fidelity, Argyle et al. ( 2023) show
that, by providing a prompt that describes the sociocultural
characteristics of a specific demographic group, it is possi -
ble to generate response distributions that strongly correlate
with that group’s survey response distributions. Similarly,
Horton (2023) demonstrates that various LLMs from Ope -
nAI respond to economic scenarios in ways that are consis-
tent with intuition and experience.
Algorithmic fidelity paves the way for marketers to poten-
tially conduct market research with fewer requirements
1 3
691

Journal of the Academy of Marketing Science (2025) 53:684–701
marginal cost. Meta, for instance, has announced its inten -
tion to use GenAI for automatically creating ads. 4 So far,
there is limited research that explores consumer responses
to GenAI-generated content. Bai et al. ( 2023) and Kreps
et al. ( 2022) in political science, and Zhang and Gosline
(2023) in decision making represent notable exceptions.
Interestingly, these studies report differing findings. While
Bai et al. ( 2023) and Kreps et al. ( 2022) report no differ -
ence between GenAI and human-generated text, Zhang et
al. (2022) find that ChatGPT-4 creates messages associated
with higher satisfaction and willingness to pay than those
produced by humans, even experts.
These initial studies aside, we argue that further research
is necessary to examine the connection between GenAI’s
objective parameters and human subjective perceptions of
its output. For instance, users can control the behavior of
LLMs in three main ways. First, we have discussed ear -
lier the relevance of prompts. Second, users can adjust the
level of randomness (or creativity) in the output generated
by modifying the temperature parameter. A temperature
of 0 makes the model deterministic, always selecting the
most likely token. As the temperature increases, the model
becomes more random, leading to more diverse and creative
output. Third, users can employ top_p sampling to restrict
the model’s selection to a subset of tokens (the nucleus),
rather than considering all possible tokens. For instance,
setting a top_p value to 0.2 means that the model will only
select from those tokens that represent the top 20% of the
probability mass for the next token. Given these technical
nuances of GenAI, we identify avenues for future research,
both at the consumer and firm level.
At the consumer level, the limited research on persua -
siveness of GenAI-created messages has primarily focused
on prompt strategies (Karinshak et al., 2023), with limited
attention given to the role of temperature and top_p sam -
pling. Hence, future research should explore whether varia-
tions in the objective parameters of LLMs are associated
with variations in subjective evaluations of message per-
suasiveness. Learning more about this aspect could be cru -
cial for crafting messages that are consistent with recipients’
psychological characteristics. Thus, we propose the follow-
ing research question.
RQ Does variation in objective LLM parameters translate
into different subjective perceptions of persuasiveness?
Second, initial studies have started to explore differences
in GenAI-generated content compared to that generated by
humans. Bai et al. ( 2023) find that humans perceive mes -
sages crafted by GenAI to be more factual and logical but
4  https://techcrunch.com/2023/04/05/
meta-wants-to-use-generative-ai-to-create-ads/?guccounter=1.
RQ What are the boundary conditions of GenAI’s capability
to replace human subjects/experts in market research?
Finally, Hartmann et al. (2023) show that images generated
by different LLMs display significantly different perfor -
mance in terms of click-through rates. The classic approach
in marketing has been to compare different models in order
to select the best one. We propose a different approach
that is based instead on assembling predictions of different
LLMs. Indeed, each LLM has been trained using different
datasets, architectures, and hyperparameters, implying that
each LLM has heterogeneous expertise in different tasks
and domains, as well as idiosyncratic strengths and biases.
Thus, assembling different LLMs can potentially harness
the diverse strengths of each model, while exploiting the
complementarities between them. Although the computer
science community has started investigating different ways
to assemble LLMs (Jiang et al., 2023; Lu et al., 2023),
the ensemble method used always depends on the task at
hand (Yang et al., 2023). Hence, it is important that mar -
keters develop their own ensemble method that accounts
for domain-specific goals. Thus, we propose the following
research question:
RQ How can we assemble different LLMs to better replicate
human/expert responses?
This argument suggests that the true potential of GenAI
is represented by the combination of different LLMs, not
an individual model. As such, we warn scholars intending
to compare human performance with that of GenAI that a
fair comparison should always require assembling different
foundation models.
Communicating
Gartner predicts that GenAI will produce 30% of brands’
marketing messages by 2025, 3 thanks to GenAI’s ease of
use, multimodality (i.e., capability to integrate various types
of data like text and images), and scalability. We pinpoint
two crucial areas deserving further investigation: (1) the
extent to which firms can rely on GenAI to convincingly
persuade consumers, and (2) the consequences of disclosing
GenAI use for a firm’s brand equity.
Persuading consumers
A key marketing activity involves crafting persuasive mar -
keting content. GenAI potentially excels in this task due
to its ability to swiftly generate new content at minimal
3 https://www.gartner.com/en/topics/generative-ai.
1 3
692

Journal of the Academy of Marketing Science (2025) 53:684–701
It is hence important to account for such heterogeneity of
marketing performance metrics when assessing GenAI’s
capacity to craft persuasive messages.
To date, the computer science community has devoted
much effort to developing prompt strategies aimed at
improving LLMs’ performance in analytical tasks. We pres-
ent a summary of the most relevant strategies in Table 3.
Marketing research is needed to investigate and propose
innovative prompt strategies that can not only augment
LLMs’ efficacy in analytical tasks but also do likewise in
various relevant marketing endeavors, such as empathy
(Huang & Rust, 2021), recovering from negative events like
product recalls (Raithel et al., 2023), or convincing con -
sumers to adopt socially-relevant behavior (Winterich et al.,
2023). Thus, we propose the following research questions:
RQ How can firms vary LLM parameters to create more
persuasive messages?
RQ Which LLM parameter is most conducive to different
marketing goals?
Disclosing
Consumers appear to struggle in distinguishing GenAI-
generated content from human- generated content (Jakesch
et al., 2023). However, several governments (e.g., the U.S.
and its AI Disclosure Act) and social platforms (e.g., Tik -
Tok, YouTube) are increasingly enforcing clear disclosure
of AI-generated content. Therefore, research is warranted to
explore the implications of such disclosure requirements for
both consumers and firms.
At the consumer level, a growing body of marketing stud-
ies has focused on consumer responses to AI, such as robots
(Mende et al., 2019), chatbots (Luo et al., 2019), or applica-
tions in medicine (Longoni et al., 2019). This research has
unveiled the phenomenon of algorithm aversion , wherein
humans tend to distrust and reject algorithms, even when
also less angry and likely to rely on vivid story-telling. Kar-
inshak et al. ( 2023) report that GPT3-crafted pro-vaccina -
tion messages are perceived as more colloquial, authentic,
and positive. While these studies uncover some differences
between GenAI- and human-generated content, they do not
explain how objective parameters influence human subjec -
tive perception. Our preliminary analysis seems to show that
increasing the temperature causes ChatGPT-3 to generate
more verbose output, even when the model is constrained
to produce a maximum number of tokens. In the context
of idea generation, verbose ideas have been observed to
receive better evaluations (Kornish & Jones, 2021). This
verbosity effect potentially extends to evaluations of mes -
sage persuasiveness. As such, we call for future research
to investigate the theoretical mechanisms linking objective
LLM parameters to subjective perceptions. Additionally,
gaining a deeper understanding of why these parameters
influence persuasiveness in different ways could provide
insights with respect to consumer heterogeneity. Thus, we
propose the following two research questions:
RQ What are the theoretical mechanisms through which
objective LLM parameters influence subjective
perceptions?
RQ What theoretical constructs cause heterogeneity in
consumer responses to variations of objective LLM
parameters?
At the firm level, understanding the psychological mecha -
nisms that link objective LLM parameters to persuasiveness,
can help firms tailor messages to increase their customer
base’s purchase intention by defining message parameters
ex-ante. Furthermore, since the marketing field has transi -
tioned from transactional to relationship marketing (Mor -
gan & Hunt, 1994) and further still to customer-engagement
marketing (Blut et al., 2023; Harmeling et al., 2017; Pansari
& Kumar, 2017), marketers today have a plethora of goals
to pursue, all of which extend well beyond mere purchase.
Table 3 Overview of the main prompt strategies
Strategy Definition Example
Zero-shot Simply ask the model to do something Please generate a new social media post about our latest
product
Few-shot (Sewon et al., 2022) Provide demonstrations in the prompt This is awful! // Negative
The game was horrible! // Negative What a great day ! // …
Chain-of-thought (CoT) (Wei et al.,
2022)
Provide explanation of the reasoning to
get to the outcome
Q: Roger has 5 tennis balls. He buys 2 more cans of tennis
balls. How many tennis balls does he have now?
A: Roger started with 5 balls 2 cans of 3 tennis balls each is
6 tennis balls. 5 + 6 = 11. The answer is 11
Q: The cafeteria had 23 apples. If they used 20 to make lunch
and bought 6 more, how many apples do they have now?
Zero-shot CoT (Kojima et al., 2022) Add the magic sentence: Let’s think step
by step
Q: Roger has 5 tennis balls. He buys 2 more cans of tennis
balls. How many tennis balls does he have now?
A: Let’s think step by step
1 3
693

Journal of the Academy of Marketing Science (2025) 53:684–701
At the firm level, there is a need for research to explore
how firms can effectively balance the benefits of GenAI
use with potential negative consumer reactions to such use,
particularly in light of increasing enforcement of disclo -
sure by governments or social platforms. As the literature
that explores how firms can mitigate algorithm aversion
tends to analyze either consumer characteristics (Longoni
et al., 2019; Luo et al., 2019) or task characteristics (Cas -
telo et al., 2019; Morewedge, 2022), we advocate for future
research on the role that brand associations (i.e., beliefs that
consumers associate with a brand) play in mitigating or
amplifying the effect of GenAI disclosure on brand equity.
For instance, in terms of brand innovativeness (Brown &
Dacin, 1997), two reactions are equally plausible theoreti -
cally. On the one hand, disclosing GenAI use might help
amplify consumer perceptions of a firm’s innovativeness.
On the other hand, consumers might perceive inconsistency
between a firm’s self-described innovative image and that
firm’s use of GenAI to enhance internal creativity. Such a
contrasting effect might amplify the negative effect of dis -
closing GenAI use for innovative firms (Brown & Dacin,
1997). Brand innovativeness serves as just one example,
and future research is needed to investigate the moderat -
ing effect of this disclosure and other brand associations,
including brand authenticity (Moulard et al., 2021) or cor-
porate social responsibility. Thus, we propose the following
research question:
RQ Which brand associations amplify the negative effect of
GenAI disclosure on brand equity? Which associations
mitigate this effect?
Further, research has investigated ways to mitigate negative
reactions to a firm’s use of AI, such as postponing disclosure
time (Luo et al., 2019), framing AI as assisting rather than
replacing humans (Longoni et al., 2019), reframing tasks
as relatively objective (Castelo et al., 2019), and emphasiz-
ing the salience of utilitarian attributes (Longoni & Cian,
2022). We call for future research to investigate how firms
can align their disclosure messages with their brand associa-
tions. For instance, underdog brands (Paharia et al., 2011)
could frame the use of GenAI as a strategy for leveling the
playing field, while innovative brands could frame their
GenAI use as a demonstration of the firm’s commitment to
cutting-edge technology adoption. Hence, we propose the
following research question:
RQ How can firms align disclosure messages to their firms’
brand associations in order to mitigate the potential neg-
ative effect of disclosing GenAI use?
they outperform humans (Dietvorst et al., 2015). These
studies have identified factors such as uniqueness neglect
(Longoni et al., 2019), perceived lower empathy (Luo et
al., 2019), and cost-cutting motives (Castelo et al., 2023) as
drivers of consumers’ reluctance to adopt AI applications.
This research has also identified contextual conditions that
seem to mitigate algorithm aversion: consumers are more
inclined to trust algorithms for tasks perceived as objective
(Castelo et al., 2019; Longoni et al., 2019) and in contexts
with low identity relevance, such as numerical estimation
or forecasting tasks (Logg et al., 2019). Conversely, aver-
sion is exacerbated when AI performs tasks that consumers
deem central to their identity, thus invoking self-enhancing
and self-protective biases (Morewedge, 2022; Leung et al.,
2018).
Given this context, consumer responses to a firm’s dis -
closure of GenAI use appear ambiguous. On the one hand,
GenAI demonstrates superior capabilities in generating
empathy and unique content that is specifically tailored to
consumer needs, compared to other types of AI (Huang &
Rust, 2023). Therefore, algorithm aversion should theoreti-
cally be lower for GenAI than for other AI applications. On
the other hand, creating novel content is a subjective task
and creativity is widely regarded as a quintessential human
capability (Koivisto & Grassini, 2023). Thus, prior studies
suggest a negative response towards GenAI use (Castelo et
al., 2019; Morewedge, 2022). In light of such conflicting
predictions emerging from the literature, further research is
needed to investigate consumer responses to a firm’s use of
GenAI and how the disclosure of GenAI-generated content
differs from that generated by other types of AI.
Additionally, anecdotal evidence seems to suggest that
disclosing GenAI use triggers new considerations for con -
sumers, beyond those typically described in the algorithm
aversion literature. For instance, when Levi’s announced
its decision to use GenAI to create models of more diverse
body types and skin tones, the company faced strong criti -
cism from consumers who feared that this decision would
‘deprive people of opportunities’ 5. Thus, future research
should investigate whether novel theoretical mechanisms
drive consumer responses to the disclosure of GenAI-
generated content, beyond those that influence consumer
responses to the disclosure of other types of AI. Hence, we
propose the following research questions:
RQ Do consumers respond differently to the disclosure of
GenAI compared to the disclosure of other types of AI?
What novel theoretical mechanisms explain consumer
responses to a firm’s disclosure of GenAI-generated
content?
5 https://www.independent.co.uk/life-style/fashion/levis-ai-models-
diversity-backlash-b2310280.html
1 3
694

Journal of the Academy of Marketing Science (2025) 53:684–701
At the firm level, GenAI opens up brand new opportuni -
ties for firms to engage consumers by reducing the cognitive
resources consumers need to participate fully in task-based
CE initiatives. Firms adopt CE initiatives to access vari -
ous customer resources beyond creativity, including cus -
tomer network assets, persuasion capital, and knowledge
stores (Harmeling et al., 2017). With GenAI eliminating
the constraint for consumers to allocate creative resources,
firms can engage even those consumers with lower levels
of creativity. Thus, the potential risk of individual con -
sumers experiencing lower psychological ownership in
GenAI-driven CE initiatives may be counterbalanced by
the chance for firms to reach a broader audience and access
more relevant resources. Hence, there is a need for research
on how firms can devise innovative CE initiatives leverag -
ing GenAI. Specifically, future research could explore how
firms can navigate the trade-off between the potential risk
of generating lower individual CE and the advantages of
accessing a broader consumer base. Hence, we propose the
following research questions:
RQ What novel, task-based customer engagement strategies
can firms pursue using GenAI?
RQ How can firms manage the trade-off between wider
reach and lower psychological ownership in GenAI,
task-based CE initiatives?
Impact of GenAI for firms and consumers
Our previous discussion highlights both the opportunities
and threats for firms that use GenAI in their innovation pro-
cess. We expect that as more and more firms and consum -
ers use GenAI, their capabilities will undergo significant
changes. Our conversations with top executives across vari-
ous industries reveal that this is a major concern. Some of
the concerns expressed include: “The number one question
that everyone is asking is: What can we (marketing) con -
tribute to firm value in the future?” or “How can we con -
vince the boardroom that there is still need for a marketing
department? They have always viewed marketing as a cost
and now they have the opportunity to reduce that cost. What
value can we provide?”. These concerns reflect a broader
apprehension among executives regarding the evolving role
of marketing in an era increasingly influenced by GenAI.
To address these concerns, we propose research questions
that explore the effects of employing GenAI on: (1) the rela-
tionship between market-based assets and firm value; and
(2) consumer skills, preferences, and role in the marketing
processes. We summarize our research questions in Table 4.
Engaging
After consumers buy a firm’s offering, it is important to
maintain their engagement beyond mere transactions (Pan -
sari & Kumar, 2017). Customer engagement marketing rep-
resents “the firm’s deliberate effort to motivate, empower,
and measure a customer’s voluntary contribution to its
marketing functions, beyond a core, economic transaction”
(Harmeling et al., 2017, p.312). Among various initiatives
aimed at enhancing customer engagement (CE), a recent
meta-analysis reveals that task-based initiatives are particu-
larly effective (Blut et al., 2023). These initiatives “deliber-
ately exist to push customers’ resource contributions” (Blut
et al., 2023, p.497). Moreover, Harmeling et al. (2017) iden-
tify four key resources that consumers can voluntarily con -
tribute to the firm’s marketing function, including creativity.
We argue that GenAI and its use have implications for
both consumers and firms. At the consumer level, an indi -
vidual’s ability to participate in task-based customer engage-
ment (CE) initiatives is often limited by her own creativity
and skills. GenAI can alleviate this constraint as consum -
ers can employ different tools such as Midjourney or Stable
Diffusion6 to augment their limited creativity. For instance,
Coca-Cola partnered with OpenAI to launch the Real
Magic platform, which enables users to generate original
images cards using GPT-4, DALL·E, and historical pictures
from Coca-Cola’s archives. Winners of the competition
had their work featured on Coca-Cola’s digital billboards
in prominent locations like New York’s Times Square and
London’s Piccadilly Circus. By leveraging GenAI, even
users with minimal graphic design skills could participate
in Coca-Cola’s initiative. However, the marketing litera -
ture suggests that customer engagement stems from the
mental effort customers exert to create something novel,
which fosters a sense of psychological ownership (Blut et
al., 2023). In the absence of this sense of ownership, GenAI
may potentially have a negative effect on customer engage-
ment. Therefore, future research is essential to investigate
the net effect of employing GenAI-based tools on customer
engagement. Specifically, research should investigate the
optimal level of GenAI use from the consumer’s perspec -
tive, so firms may enhance creativity while preserving a
sense of ownership among consumers, ultimately promot -
ing sustained customer engagement. Accordingly, we pro -
pose the following research question:
RQ What are the consequences of employing GenAI-based
tools for consumers working on customer engagement
initiatives?
6  Midjourney and Stable Diffusion are text-to-image tools that allow
users to create images of new objects from text prompts.
1 3
695

Journal of the Academy of Marketing Science (2025) 53:684–701
assets. For instance, GenAI creates new content based on
its world knowledge at the time of training. As of Janu -
ary 2024, the latest knowledge available to some ChatGPT
models dates back September 2023. This limitation could
severely hinder GenAI’s ability to produce valuable output
in supporting new product development, given the frequent
shifts in consumer preferences. Firms can curb the risk of
creating something misaligned with current customer needs
by ensuring they have up-to-date market knowledge to feed
GenAI. From this perspective, GenAI necessitates comple -
mentary market-based assets to realize its full potential.
Initial empirical evidence in the literature is mixed. On
the one hand, research supports a complementary view, as
both Reisenbichler et al. ( 2022) and Reisenbichler et al.
(2023) show that GenAI alone is insufficient; instead, adopt-
ing a “human-in-the-loop” approach is necessary. On the
other hand, Girotra et al. ( 2023) find that ChatGPT-4 does
not require humans to generate more and better ideas than
MBA students. Thus, we conclude that the “jury is still out,”
underscoring the need for future research to investigate the
boundary conditions of the relationship between GenAI,
marketing capabilities, and firm value.
Marketing theory suggests that whether firms will use
GenAI to substitute or complement marketing depends on
the competitive advantage strategy that a firm pursues, as
this strategy directly influences the role of marketing in the
organization (McAlister et al., 2023). For firms that pursue
a cost-leadership strategy, marketing is typically viewed as
a staff function with no authority on marketing decisions; it
is likely that such firms will view GenAI as an opportunity
to reduce marketing costs. Even if GenAI were only capable
of producing synthetic content comparable to human-gener-
ated content, its ability to create such content at nearly zero
marginal cost is noteworthy. For instance, Reisenbichler et
al. ( 2022) demonstrate that LLMs can achieve 91% cost
saving in generating text-based SEO content. In these orga-
nizations, we anticipate that marketing will limit itself to the
use of off-the-shelf GenAI solutions. For firms that adopt a
differentiation strategy, marketing can take on either a staff
function role with control over brand image and communi -
cations only, or a line function role that is responsible for
delivering business results (McAlister et al., 2023). In the
latter case, we expect marketing to play a more prominent
role in the firm’s GenAI use. For instance, marketing might
be directly involved in fine-tuning GenAI foundational
The post-GenAI firm: How can marketing contribute
to firm value?
Our previous discussion suggests that GenAI has the poten-
tial to fundamentally transform the value of key market -
ing capabilities, spanning from new product development
to market information management to communication
(V orhies & Morgan, 2005). Hence, GenAI could redefine
the essence of marketing’s contribution to a firm’s sustain -
able competitive advantage.
Firms create value for shareholders by leveraging mar -
ket-based assets (Srivastava et al., 1998). These key assets,
whether capabilities or resources, stem from interactions
with customers (Srivastava et al., 1998; Slotegraaf et al.,
2003). Our previous discussion highlights how this tech -
nology reshapes interactions between firm and customers
throughout the innovation process. Similarly, Huang and
Rust (2023) show that GenAI changes firm-customer inter -
actions along the customer care journey. Thus, it is reason -
able to anticipate that the repeated use of GenAI by firms
in their innovation and caring processes will fundamentally
reshape the market-based assets available to them. For
instance, we discussed earlier the potential effect of disclos-
ing GenAI use on a key relational asset such as brand equity.
As another example, the reduced reliance on consumers to
conduct market research might impede the accumulation
of customer knowledge, which serves as a key intellec -
tual market-based asset. Thus, future research is needed to
investigate the following question:
RQ How does the use of GenAI alter the development and
evolution of relational and intellectual market-based
assets?
Second, for a market-based asset to confer a sustainable
competitive advantage, it must be convertible, rare, inimi -
table, and non-substitutable (Srivastava et al., 1998). The-
oretically, we envision two possible effects of GenAI on
market-based assets. On the one hand, the ability to generate
numerous messages or new product ideas at minimal cost
within minutes greatly diminishes the value of key market -
ing capabilities (e.g., communication, new product develop-
ment), making them more susceptible to imitation and less
rare. On the other hand, a unique aspect of GenAI is that
its output depends on the input that users provide, suggest -
ing a complementary relationship with key market-based
Table 4 The consequences of using GenAI
Level of analysis Research questions
Firm • How does the use of GenAI alter the development and evolution of relational and intellectual market-based assets?
• How does the use of GenAI in marketing activities vary across different marketing organizations?
Consumer • How will GenAI change consumer preferences?
• What is the new role of the post-GenAI consumer in the marketing procsses?
1 3
696

Journal of the Academy of Marketing Science (2025) 53:684–701
RQ How will GenAI change consumer preferences?
Finally, it is worth noting that the marketing literature has
evolved in its conceptualization of the customer’s role:
from being seen as the target of a firm’s offering, to being
viewed as the object of orientation (Narver & Slater, 1990),
and eventually to being recognized as a co-creator and co-
producer (Prahalad & Ramaswamy, 2004). As we discussed
in the co-ideation section, consumers’ role as co-creators
may become less relevant, especially if both consumers and
employees rely on the same GenAI input for their creative
output. This shift, combined with the changes in consumer’s
cognitive abilities and preferences previously discussed,
presents an opportunity for future research about the new
role that the post-GenAI consumer may assume in the mar-
keting processes:
RQ What is the new role of the post-GenAI consumer in
marketing processes?
Conclusion
This paper analyzes the latest type of artificial intelligence,
GenAI, and focuses on its capacity to create novel content.
We propose a roadmap of future research in two main areas.
First, we propose research that explores (a) how GenAI
could alter consumer creative behavior, and (b) how firms
consequently must re-adapt their strategies to fully harness
the innovative potential of GenAI throughout the innova -
tion process. Second, we propose research that analyzes the
consequences of using GenAI for how marketing can con -
tribute to firm value, as well as consequences with respect
to consumer preferences, skills, and role in the marketing
processes. We have chosen to focus our research roadmap
on innovation, which represents one of the novel elements
of GenAI compared to mechanical and thinking AI (Huang
& Rust, 2021). We conclude this paper by sketching three
further areas of potential interest for marketing research on
GenAI: privacy, disinformation, and contribution of market-
ing to GenAI research.
Previously, we discussed the technical feasibility of
fine-tuning existing foundational models with a firm’s pro -
prietary data, thus enabling firms to grasp the unique char -
acteristics of a brand’s image and customer base. However,
sharing proprietary data for fine-tuning raises privacy con -
cerns (Huang & Rust, 2023). While the marketing litera -
ture has primarily focused on consumer concerns regarding
data privacy (Martin & Murphy, 2017; Martin et al., 2017;
Thomaz et al., 2020), we highlight a major concern for firms:
sharing proprietary knowledge poses the risk of diminish -
ing the scarcity of a firm’s market-based assets, potentially
models. In sum, future research is needed to investigate the
following questions:
RQ How does the use of GenAI in marketing activities vary
across different marketing organizations?
The post-GenAI consumer: What role?
Given the described changes in consumer and firm behavior,
we conclude our roadmap of future research by offering an
initial portrayal of the post-GenAI consumer and by pre -
senting research questions regarding the role of this emerg-
ing customer in future marketing processes.
The marketing field has recognized that new technolo -
gies often alter consumer behavior (Giebelhausen et al.,
2014; Hoffman & Novak, 2018). Taking this idea a step
further, neuroscientists and cognitive scientists warn that
delegating human cognitive abilities to technologies could
lead to permanent changes in our brain structure and fun -
damentally alter the cognitive abilities that govern human
behavior (Fajnerová et al., 2018). For instance, relying on
GPS for navigation reduces hippocampus functioning and
related orientation skills (McKinlay, 2016), the invention of
the printing press made mnemonic capabilities and the use
of rhetoric for memorization obsolete (Eisenstein, 1979),
and the use of smartphones is linked to shorter attention
spans (Wilmer et al., 2017). Accordingly, we argue that
research at the intersection of marketing, neuroscience, and
cognition should investigate how GenAI will affect the cog-
nitive capabilities of consumers, especially with respect to
creativity.
Creativity is an integral part of consumers’ daily life
(Moreau & Dahl, 2005). Contrary to the idea of the cre -
ative genius, the cognitive literature suggests that every
individual has the potential for creativity. More frequent
involvement in creative cognitive processes enhances the
likelihood of generating creative ideas (Ward, 2001). GenAI
applications have been available to the general public for
approximately 19 months, so it is premature to observe any
significant changes. However, we anticipate that as more
individuals integrate GenAI applications into their daily
routines, humans may become less involved in the cognitive
processes responsible for creativity. Similar to the impact
of GPS on orientation skills (Fajnerová et al., 2018), an
over-reliance on GenAI for generating novel content could
potentially diminish consumers’ appreciation for creativity.
Research is hence necessary to investigate what customers
with lower levels of creativity will value. For instance, will
they still value innovation as much as current consumers
do? In sum, we propose the following research question:
1 3
697

Journal of the Academy of Marketing Science (2025) 53:684–701
LLMs are susceptible to technical biases, such as majority
label bias (i.e., the model produces content that frequently
appears in the prompt), recency bias (i.e., the model pro -
duces context appearing near the end of the prompt), and
availability bias (i.e., the model prefers answers that are fre-
quent in its pre-training data) (Zhao et al., 2021). Given the
marketing field’s history of developing strategies to mitigate
human biases in surveys (Hulland et al., 2018), we call for
research to explore how these strategies could be adapted to
calibrate prompts and enhance the quality of GenAI output.
Funding Open access funding provided by Università Commerciale
Luigi Bocconi within the CRUI-CARE Agreement.
Data availability This piece is theoretical and does not include data.
Declarations
Competing interests The authors declare that they have no conflicts
of interest.
Open Access   This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format,
as long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate
if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless
indicated otherwise in a credit line to the material. If material is not
included in the article’s Creative Commons licence and your intended
use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright
holder. To view a copy of this licence, visit http://creativecommons.
org/licenses/by/4.0/.
References
Amabile, T. M. (2018). Creativity in context: Update to the social psy-
chology of creativity. Routledge.
Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J. R., Rytting, C., &
Wingate, D. (2023). Out of one, many: Using language models
to simulate human samples. Political Analysis, 31(3), 337–351.
Bai, H., V oelkel, J., Eichstaedt, J., & Willer, R. (2023). Artificial intel-
ligence can persuade humans on political issues https://www.
researchsquare.com/article/rs-3238396/v1.ResearchGate
Bayus, B. L. (2013). Crowdsourcing new product ideas over time: An
analysis of the dell ideastorm community. Management Science,
59(1), 226–244.
Bell, J. J., Pescher, C., Tellis, G. J., & Füller, J. (2023). Can AI help in
ideation? A theory-based model for idea screening in crowdsourc-
ing contests. Marketing Science.
Binz, M. (2023). E. Schulz (Ed.), Using cognitive psychology to
understand GPT-3. Proceedings of the National Academy of Sci -
ences120(6) e2218523120.
Blut, M., Kulikovskaja, V ., Hubert, M., Brock, C., & Grewal, D.
(2023). Effectiveness of engage- ment initiatives across engage -
ment platforms: A meta-analysis. Journal of the Academy of Mar-
keting Science, pages 1–25.
Bommasani, R., Hudson, D. A., Adeli, E., Altman, R., Arora, S., von
Arx, S., Bernstein, M. S., Bohg, J., Bosselut, A., Brunskill, E.
compromising its ability to sustain a competitive advantage.
Thus, we call for future research that takes the firm perspec-
tive in order to investigate: (1) how firms can balance the
advantage of supplementing their proprietary data to fully
harness GenAI potential with the need to protect the sources
of their competitive advantage, and (2) which firms can ben-
efit the most from fine-tuning as well as which firms should
instead exercise caution in doing so.
Second, the ability of GenAI to rapidly produce varia -
tions of the same content en masse and at negligible cost
opens the floodgates to disinformation and diffusion of
conspiracy theories. Traditionally, these topics have been
considered a public policy issue, as political topics were
the main target of these campaigns. The limited marketing
research on this topic has mostly focused on providing psy-
chological theories to explain the diffusion of conspiracy
theories (Diaz Ruiz & Nilsson, 2023) or strategies to safe -
guard against it (Johar, 2022). However, anecdotal evidence
suggests the rise of coordinated disinformation campaigns,
orchestrated by ideologically motivated actors, to intention-
ally damage brands that take certain political stances or
to favor national brands at the expense of multinationals.
This has been observed, for instance, in media campaigns
against Western Covid vaccines, 7 Starbucks, 8 and H&M
(Sohn, 2021). GenAI will likely increase the frequency
and scope of similar types of attacks against brands, mak -
ing it a relevant topic for marketers as well. Against this
background, we call for future research to: (1) quantify the
impact of these orchestrated disinformation campaigns on
brand equity, sales, and stock performance, and (2) investi-
gate what mitigation strategies brands can adopt to nullify
disinformation campaigns.
Finally, this manuscript offers a roadmap to conduct
research about the likely contributions of GenAI to mar -
keting. The opposite paradigm–which we call “Marketing
for GenAI”–sounds equally promising. GenAI often oper -
ates like a black-box and even its creators have limited
understanding of its cognitive nature. Fully harnessing the
potential of GenAI requires a deeper understanding of the
cognitive mechanisms through which it creates new con -
tent; this deeper understanding will help users better under-
stand when GenAI is most likely to hallucinate, so they
may develop strategies to reduce hallucination instances.
Marketing has a rich tradition of decision making studies
that investigate human cognitive biases (Dowling et al.,
2020). Such knowledge can be fruitfully applied to gain rich
insights on GenAI cognition (Binz and Schulz, 2023). Fur-
ther, harnessing the full potential of GenAI requires proper
prompting (Huang & Rust, 2023). Research indicates that
7 https://shorturl.at/xH169.
8  https://www.nbcnews.com/business/business-news/
trolls-spread-hateful-fake-starbucks-coupon-n867501.
1 3
698

Journal of the Academy of Marketing Science (2025) 53:684–701
Harmeling, C. M., Moffett, J. W., Arnold, M. J., & Carlson, B. D.
(2017). Toward a theory of customer engagement marketing.
Journal of the Academy of Marketing Science, 45, 312–335.
Hartmann, J., Exner, Y ., & Domdey, S. (2023). The power of genera-
tive marketing: Can generative AI reach human-level visual mar-
keting content? Available at SSRN.
Hoffman, D. L., & Novak, T. P. (2018). Consumer and object experi -
ence in the internet of things: An assemblage theory approach.
Journal of Consumer Research, 44(6), 1178–1204.
Horton, J. J. (2023). Large language models as simulated economic
agents: What can we learn from homo silicus? Technical report,
National Bureau of Economic Research.
Huang, M. H., & Rust, R. T. (2021). A strategic framework for artifi -
cial intelligence in marketing. Journal of the Academy of Market-
ing Science, 49, 30–50.
Huang, M. H., & Rust, R. T. (2023). The caring machine: Feeling Ai
for customer care. Journal of Marketing.
Hulland, J., Baumgartner, H., & Smith, K. M. (2018). Marketing sur -
vey research best practices: Evidence and recommendations from
a review of jams articles. Journal of the Academy of Marketing
Science, 46, 92–108.
Hutson, M. (2023). Hypotheses devised by AI could find’blind spots’
in research. Nature.
Jakesch, M., Hancock, J. T., & Naaman, M. (2023). Human heuristics
for ai-generated language are flawed. Proceedings of the National
Academy of Sciences, 120(11):e2208839120.
Jiang, D., Ren, X., & Lin, B. Y . (2023). LLM-blender: Ensembling
large language models with pairwise ranking and generative
fusion. arXiv preprint arXiv:2306.02561.
Johar, G. V . (2022). Untangling the web of misinformation and false
beliefs. Journal of Consumer Psychology, 32(2), 374–383.
Kahn, K. B., Barczak, G., & Moss, R. (2006). Perspective: Establish -
ing an NPD best practices framework. Journal of Product Innova-
tion Management, 23(2), 106–116.
Karinshak, E., Liu, S. X., Park, J. S., & Hancock, J. T. (2023). Working
with AI to persuade: Examining a large language model’s ability
to generate pro-vaccination messages. Proceedings of the ACM
on Human-Computer Interaction, 7(CSCW1):1–29.
Knight, K. E. (1967). A descriptive model of the intra-firm innovation
process. The Journal of Business, 40(4), 478–496.
Koivisto, M., & Grassini, S. (2023). Best humans still outperform arti-
ficial intelligence in a creative divergent thinking task. Scientific
Reports, 13(1), 13601.
Kojima, T., Gu, S. S., Reid, M., Matsuo, Y ., & Iwasawa, Y . (2022).
Large language models are zero-shot reasoners. Advances in Neu-
ral Information Processing Systems, 35, 22199–22213.
Korinek, A. (2023). Generative ai for economic research: Use cases
and implications for economists. Journal of Economic Literature,
61(4), 1281–1317.
Kornish, L. J., & Jones, S. M. (2021). Raw ideas in the fuzzy front
end: Verbosity increases perceived creativity. Marketing Science,
40(6), 1106–1122.
Kreps, S., McCain, R. M., & Brundage, M. (2022). All the news that’s
fit to fabricate: Ai-generated text as a tool of media misinforma -
tion. Journal of Experimental Political Science, 9(1), 104–117.
Lambrecht, A., & Tucker, C. (2019). Algorithmic bias? An empirical
study of apparent gender-based discrimination in the display of
STEM career ads. Management Science, 65(7), 2966–2981.
Leung, E., Paolacci, G., & Puntoni, S. (2018). Man versus machine:
Resisting automation in identity- based consumer behavior. Jour-
nal of Marketing Research, 55(6), 818–831.
Li, P., Castelo, N., Katona, Z., & Sarvary, M. (2024). Frontiers: Deter-
mining the validity of large language models for automated per -
ceptual analysis. Marketing Science.
Logg, J. M., Minson, J. A., & Moore, D. A. (2019). Algorithm
appreciation: People prefer algorithmic to human judgment.
(2021). On the opportunities and risks of foundation models.
arXiv preprint arXiv:2108.07258.
Brand, J., Israeli, A., & Ngwe, D. (2023). Using GPT for market
research. Available at SSRN 4395751.
Brown, T. J., & Dacin, P. A. (1997). The company and the product:
Corporate associations and consumer product responses. Journal
of Marketing, 61(1), 68–84.
Castaño, R., Sujan, M., Kacker, M., & Sujan, H. (2008). Managing
consumer uncertainty in the adoption of new products: Temporal
distance and mental simulation. Journal of Marketing Research,
45(3), 320–336.
Castelo, N., Bos, M. W., & Lehmann, D. R. (2019). Task-dependent
algorithm aversion. Journal of Marketing Research , 56(5),
809–825.
Castelo, N., Boegershausen, J., Hildebrand, C., & Henkel, A. P. (2023).
Understanding and improving consumer reactions to service bots.
Journal of Consumer Research, 50(4), 848–863.
Chung, T. S., Wedel, M., & Rust, R. T. (2016). Adaptive personaliza-
tion using social networks. Journal of the Academy of Marketing
Science, 44, 66–87.
Cillo, P., Priem, R. L., Verona, G., & Zanella, P. (2021). Consumer-
CEO interaction as catalyst for business model innovation in
established firms. Journal of Business Research, 131, 241–253.
Dahl, D. W., & Moreau, P. (2002). The influence and value of analogi-
cal thinking during new product ideation. Journal of Marketing
Research, 39(1), 47–60.
Davenport, T., Guha, A., Grewal, D., & Bressgott, T. (2020). How arti-
ficial intelligence will change the future of marketing. Journal of
the Academy of Marketing Science, 48, 24–42.
Diaz Ruiz, C., & Nilsson, T. (2023). Disinformation and echo cham -
bers: How disinformation circulates on social media through
identity-driven controversies. Journal of Public Policy & Mar -
keting, 42(1), 18–35.
Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm aver-
sion: People erroneously avoid algorithms after seeing them err.
Journal of Experimental Psychology: General, 144(1), 114.
Dowling, K., Guhl, D., Klapper, D., Spann, M., Stich, L., & Yegoryan,
N. (2020). Behavioral biases in marketing. Journal of the Acad -
emy of Marketing Science, 48, 449–477.
Eapen, T. T., Finkenstadt, D., Folk, J., & Venkataswamy, L. (2023).
How generative AI can augment human creativity. Harvard Busi-
ness Review, 101(4), 76–85.
Eisenstein, E. L. (1979). Printing Press Agent of Change: Communi -
cations and Cultural transformations in Early-Modern Europe .
Cambridge University Press.
Else, H. (2023). By Chatgpt Fool Scientists. Nature, 613, 423.
Fajnerová, I., Greguš, D., Hlinka, J., Nekovářová, T., Škoch, A., Zítka,
T., Romportl, J., Žáčková, E., & Horáček, J. (2018). Could pro -
longed usage of gps navigation implemented in augmented real -
ity smart glasses affect hippocampal functional connectivity?
BioMed Research International, 2018.
Giebelhausen, M., Robinson, S. G., Sirianni, N. J., & Brady, M. K.
(2014). Touch versus tech: When technology functions as a bar -
rier or a benefit to service encounters. Journal of Marketing ,
78(4), 113–124.
Girotra, K., Terwiesch, C., & Ulrich, K. T. (2010). Idea generation and
the quality of the best idea. Management Science, 56(4), 591–605.
Girotra, K., Meincke, L., Terwiesch, C., & Ulrich, K. T. (2023). Ideas
are dimes a dozen: Large language models for idea generation in
innovation. Available at SSRN 4526071.
Hamilton, R. (2016). Consumer-based strategy: Using multiple meth -
ods to generate consumer insights that inform strategy. Journal of
the Academy of Marketing Science, 44, 281–285.
Han, S. J., Ransom, K. J., Perfors, A., & Kemp, C. (2024). Inductive
reasoning in humans and large language models. Cognitive Sys-
tems Research, 83, 101155.
1 3
699

Journal of the Academy of Marketing Science (2025) 53:684–701
Paharia, N., Keinan, A., Avery, J., & Schor, J. B. (2011). The underdog
effect: The marketing of disadvantage and determination through
brand biography. Journal of Consumer Research, 37(5), 775–790.
Pansari, A., & Kumar, V . (2017). Customer engagement: The con -
struct, antecedents, and consequences. Journal of the Academy of
Marketing Science, 45, 294–311.
Plangger, K., Grewal, D., de Ruyter, K., & Tucker, C. (2022). The
future of digital technologies in marketing: A conceptual frame -
work and an overview. Journal of the Academy of Marketing Sci-
ence, 50(6), 1125–1134.
Prahalad, C. K., & Ramaswamy, V . (2004). Co-creation experiences:
The next practice in value creation. Journal of Interactive Mar -
keting, 18(3), 5–14.
Puntoni, S., Reczek, R. W., Giesler, M., & Botti, S. (2021). Consumers
and artificial intelligence: An experiential perspective. Journal of
Marketing, 85(1), 131–151.
Raithel, S., Hock, S. J., & Mafael, A. (2023). Product recall effective-
ness and consumers’ participation in corrective actions. Journal
of the Academy of Marketing Science, pages 1–20.
Reisenbichler, M., Reutterer, T., Schweidel, D. A., & Dan, D. (2022).
Frontiers: Supporting content marketing with natural language
generation. Marketing Science, 41(3), 441–452.
Reisenbichler, M., Reutterer, T., & Schweidel, D. A. (2023). Applying
large language models to sponsored search advertising. Technical
report, MSI Working Paper Series.
Ringel, D. (2023). Creating synthetic experts with generative artificial
intelligence. Available at SSRN 4542949.
Rubera, G., Ordanini, A., & Mazursky, D. (2010). Toward a contin -
gency view of new product creativity: Assessing the interactive
effects of consumers. Marketing Letters, 21, 191–206.
Rubera, G., Chandrasekaran, D., & Ordanini, A. (2016). Open innova-
tion, product portfolio innovativeness and firm performance: The
dual role of new product development capabilities. Journal of the
Academy of Marketing Science, 44, 166–184.
Scopelliti, I., Cillo, P., Busacca, B., & Mazursky, D. (2014). How do
financial constraints affect creativity? Journal of Product Innova-
tion Management, 31(5), 880–893.
Sewon, M., Xinxi, L., Holtzman, A., Artetxe, M., Lewis, M., Han -
naneh, H., & Zettlemoyer, L. (2022). Rethinking the role of
demonstrations: What makes in-context learning work? arXiv
preprint arXiv:2202.12837.
Slotegraaf, R. J., Moorman, C., & Inman, J. J. (2003). The role of firm
resources in returns to market deployment. Journal of Marketing
Research, 40(3), 295–309.
Sohn, A. (2021). The future of disinformation operations and the com-
ing war on brands . Network Contagion Research Institute, Rut -
gers University.
Srivastava, R. K., Shervani, T. A., & Fahey, L. (1998). Market-based
assets and shareholder value: A framework for analysis. Journal
of Marketing, 62(1), 2–18.
Stephen, A. T., Zubcsek, P. P., & Goldenberg, J. (2016). Lower con -
nectivity is better: The effects of network structure on redundancy
of ideas and customer innovativeness in interdependent ideation
tasks. Journal of Marketing Research, 53(2), 263–279.
Stevenson, C. E., ter Veen, M., Choenni, R., van der Maas, H. L., &
Shutova, E. (2023). Do large language models solve verbal analo-
gies like children do? arXiv preprint arXiv:2310.20384.
Thomaz, F., Salge, C., Karahanna, E., & Hulland, J. (2020). Learning
from the dark web: Leveraging conversational agents in the era of
hyper-privacy to enhance marketing. Journal of the Academy of
Marketing Science, 48, 43–63.
Toubia, O., & Netzer, O. (2017). Idea generation, creativity, and proto-
typicality. Marketing Science, 36(1), 1–20.
Ukanwa, K., & Rust, R. T. (2020). Algorithmic discrimination in ser-
vice. SSRN.
Organizational Behavior and Human Decision Processes , 151,
90–103.
Longoni, C., & Cian, L. (2022). Artificial intelligence in utilitarian vs.
hedonic contexts: The word-of- machine effect. Journal of Mar-
keting, 86(1), 91–108.
Longoni, C., Bonezzi, A., & Morewedge, C. K. (2019). Resistance to
medical artificial intelligence. Journal of Consumer Research ,
46(4), 629–650.
Lu, K., Yuan, H., Lin, R., Lin, J., Yuan, Z., Zhou, C., & Zhou, J. (2023).
Routing to the expert: Efficient reward-guided ensemble of large
language models. arXiv preprint arXiv:2311.08692.
Luo, L., & Toubia, O. (2015). Improving online idea generation plat -
forms and customizing the task structure on the basis of consum-
ers’ domain-specific knowledge. Journal of Marketing , 79(5),
100–114.
Luo, X., Tong, S., Fang, Z., & Qu, Z. (2019). Frontiers: Machines vs.
humans: The impact of artificial intelligence chatbot disclosure
on customer purchases. Marketing Science, 38(6), 937–947.
Lysyakov, M., & Viswanathan, S. (2023). Threatened by Ai: Analyzing
users’ responses to the intro- duction of AI in a crowd-sourcing
platform. Information Systems Research, 34(3), 1191–1210.
Martin, K. D., & Murphy, P. E. (2017). The role of data privacy in
marketing. Journal of the Academy of Marketing Science , 45,
135–155.
Martin, K. D., Borah, A., & Palmatier, R. W. (2017). Data privacy:
Effects on customer and firm performance. Journal of Marketing,
81(1), 36–58.
Mason, W., & Watts, D. J. (2012). Collaborative learning in net -
works. Proceedings of the National Academy of Sciences, 109(3),
764–769.
McAlister, L., Germann, F., Chisam, N., Hayes, P., Lynch, A., & Stew-
art, B. (2023). A taxonomy of marketing organizations. Journal of
the Academy of Marketing Science, 51(3), 617–635.
McClelland, J. L., Hill, F., Rudolph, M., Baldridge, J., & Schütze,
H. (2020). Placing language in an integrated understanding sys -
tem: Next steps toward human-level performance in neural lan -
guage models. Proceedings of the National Academy of Sciences,
117(42):25966–25974.
McKinlay, R. (2016). Technology: Use or lose our navigation skills.
Nature, 531(7596), 573–575.
Mende, M., Scott, M. L., van Doorn, J., Grewal, D., & Shanks, I.
(2019). Service robots rising: How humanoid robots influence
service experiences and elicit compensatory consumer responses.
Journal of Marketing Research, 56(4), 535–556.
Meyers, M. A. (2007). Happy accidents: Serendipity in modern medi-
cal breakthroughs. Arcade Publishing.
Moreau, C. P., & Dahl, D. W. (2005). Designing the solution: The
impact of constraints on consumers’ creativity. Journal of Con -
sumer Research, 32(1), 13–22.
Morewedge, C. K. (2022). Preference for human, not algorithm aver -
sion. Trends in Cognitive Sciences, 26(10), 824–826.
Morgan, R. M., & Hunt, S. D. (1994). The commitment-trust theory
of relationship marketing. Journal of Marketing, 58(3), 20–38.
Moulard, J. G., Raggio, R. D., & Folse, J. A. G. (2021). Disentangling
the meanings of brand au- thenticity: The entity-referent corre -
spondence framework of authenticity. Journal of the Academy of
Marketing Science, 49, 96–118.
Mumford, M. D., & Simonton, D. K. (1997). Creativity in the work -
place: People, problems, and structures. The Journal of Creative
Behavior, 31(1), 1–6.
Narver, J. C., & Slater, S. F. (1990). The effect of a market orientation
on business profitability. Journal of Marketing, 55(4), 20–35.
Noble, S. M., & Mende, M. (2023). The future of artificial intelligence
and robotics in the retail and service sector: Sketching the field of
consumer-robot-experiences. Journal of the Academy of Market-
ing Science, 51(4), 747–756.
1 3
700

Journal of the Academy of Marketing Science (2025) 53:684–701
Yang, H., Li, M., Xiao, Y ., Zhou, H., Zhang, R., & Fang, Q. (2023).
One llm is not enough: Harnessing the power of ensemble learn -
ing for medical question answering. medRxiv, pages 2023–12.
Zečević, M., Willig, M., Dhami, D. S., & Kersting, K. (2023). Causal
parrots: Large language models may talk causality but are not
causal. arXiv preprint arXiv:2308.13067.
Zhang, Y ., & Gosline, R. (2023). Human favoritism, not AI aversion:
People’s perceptions (and bias) toward generative ai, human
experts, and human–GAI collaboration in persuasive content gen-
eration. Judgment and Decision Making, 18, e41.
Zhang, H., Li, L. H., Meng, T., Chang, K. W., & Broeck, G. V . (2022).
d. On the paradox of learning to reason from data. arXiv preprint
arXiv:2205.11502.
Zhao, Z., Wallace, E., Feng, S., Klein, D., & Singh, S. (2021). Cali -
brate before use: Improving few-shot performance of language
models. In International Conference on Machine Learning, pages
12697–12706. PMLR.
Publisher’s Note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional affiliations.
Vartanian, O., Martindale, C., & Kwiatkowski, J. (2003). Creativity
and inductive reasoning: The relationship between divergent
thinking and performance on Wason’s 2–4—6 task. The Quar-
terly Journal of Experimental Psychology Section A, 56(4), 1–15.
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez,
A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you
need. Advances in Neural Information Processing Systems, 30.
V orhies, D. W., & Morgan, N. A. (2005). Benchmarking marketing
capabilities for sustainable compet- itive advantage. Journal of
Marketing, 69(1), 80–94.
Ward, T. B. (2001). Creative cognition, conceptual combination, and
the creative writing of stephen r. donaldson. American Psycholo-
gist, 56(4), 350.
Webb, T., Holyoak, K. J., & Lu, H. (2023). Emergent analogical rea -
soning in large language models. Nature Human Behaviour, 7(9),
1526–1541.
Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E., Le,
Q. V ., Zhou, D., et al. (2022). Chain- of-thought prompting elicits
reasoning in large language models. Advances in Neural Informa-
tion Processing Systems, 35, 24824–24837.
Wilmer, H. H., Sherman, L. E., & Chein, J. M. (2017). Smartphones
and cognition: A review of research exploring the links between
mobile technology habits and cognitive functioning. Frontiers in
Psychology, 8, 605.
Winterich, K. P., Reczek, R. W., & Makov, T. (2023). How lack of
knowledge on emissions and psychological biases deter consum-
ers from taking effective action to mitigate climate change. Jour-
nal of the Academy of Marketing Science, pages 1–20.
1 3
701
