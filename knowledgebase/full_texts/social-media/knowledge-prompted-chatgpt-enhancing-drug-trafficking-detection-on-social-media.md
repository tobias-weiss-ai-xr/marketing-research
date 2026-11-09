---
title: 'Knowledge-prompted ChatGPT: Enhancing drug trafficking detection on social media'
url: https://doi.org/10.1016/j.im.2024.104010
category: social-media
subcategory: framework
date: 2024-07
venue: Information & Management
authors:
- Chuanbo Hu
- Bin Liu
- Xin Li
source: openalex-oa
pdf_url: https://arxiv.org/pdf/2307.03699
pages: 36
chars: 65326
fetched_at: '2026-11-08T17:34:04+00:00'
kb_version: 1
---

# Knowledge-prompted ChatGPT: Enhancing drug trafficking detection on social media

Highlights
Unveiling the Potential of Knowledge-Prompted ChatGPT for Enhancing Drug
Trafficking Detection on Social Media
Chuanbo Hu, Bin Liu, Xin Li, Yanfang Ye
• We conduct the first systematic study on leveraging large language models
(LLMs), such as ChatGPT, to detect illicit drug trafficking activities on social
media.
• We propose an analytical framework to compose knowledge-informed prompts,
which serve as the interface that humans can interact with and use LLMs for
the detection of drug trafficking activities.
• We design a prompt optimization method to further enhance the e ffective-
ness of the prompts.
• We demonstrate the e ffectiveness of the proposed framework through ex-
tensive experiments on an illicit drug tra fficking dateset we collected from
Instagram.
arXiv:2307.03699v1  [cs.CL]  7 Jul 2023

Unveiling the Potential of Knowledge-Prompted
ChatGPT for Enhancing Drug Trafficking Detection on
Social Media
Chuanbo Hua, Bin Liub, Xin Lia, Yanfang Yec
aLane Department of Computer Science and Electrical Engineering, West Virginia University, 395
Evansdale Dr, Morgantown, 26505, West Virginia, United States
bDepartment of Management Information Systems, West Virginia University, 83 Beechurst
Avenue, Morgantown, 26505, West Virginia, United States
cDepartment of Computer Science and Engineering, University of Notre Dame, 257 Fitzpatrick Hall of
Engineering, Notre Dame, 46556, IN, United States
Abstract
Social media platforms such as Instagram and Twitter have emerged as critical
channels for drug marketing and illegal sale. Detecting and labeling online illicit
drug trafficking activities becomes important in addressing this issue. However,
the effectiveness of conventional supervised learning methods in detecting drug
trafficking heavily relies on having access to substantial amounts of labeled data,
while data annotation is time-consuming and resource-intensive. Furthermore,
these models often face challenges in accurately identifying tra fficking activities
when drug dealers use deceptive language and euphemisms to avoid detection.
To overcome this limitation, we conduct the first systematic study on leveraging
large language models (LLMs), such as ChatGPT, to detect illicit drug tra ffick-
ing activities on social media. We propose an analytical framework to compose
knowledge-informed prompts, which serve as the interface that humans can inter-
act with and use LLMs to perform the detection task. Additionally, we design a
Monte Carlo dropout based prompt optimization method to further to improve
performance and interpretability. Our experimental findings demonstrate that
the proposed framework outperforms other baseline language models in terms of
drug trafficking detection accuracy, showing a remarkable improvement of nearly
Preprint submitted to Information and Management July 10, 2023

12%. By integrating prior knowledge and the proposed prompts, ChatGPT can
effectively identify and label drug tra fficking activities on social networks, even
in the presence of deceptive language and euphemisms used by drug dealers to
evade detection. The implications of our research extend to social networks, em-
phasizing the importance of incorporating prior knowledge and scenario-based
prompts into analytical tools to improve online security and public safety.
Keywords: Large language models, ChatGPT, Prompt engineering, Drug
trafficking, Social media
1. Introduction
Drug trafficking, the illegal sale or transport of prohibited drugs, is a global
issue that has far-reaching impacts on communities, families, and individuals.
Illegal drug trade and usage lead to addiction and health problems and have
broader social impacts. Drug tra fficking organizations are often associated with
violence, corruption, and other forms of criminal activity [1, 2, 3]. Social media
has provided drug dealers with a convenient platform to market and sell their
illicit products [4, 5]. Social media platforms o ffer a broad audience reach and
provide drug dealers with a level of anonymity that was previously unattainable.
These platforms also facilitate communication between dealers and customers,
enabling them to coordinate transactions [6]. Detection of drug tra fficking on so-
cial networks has become critical in tackling drug trafficking. However, detecting
drug trafficking activities on social media poses di fficulties due to the use of dis-
guised language and euphemisms by drug dealers [7]. Drug dealers employ code
words, acronyms, and other disguised language to avoid detection by law enforce-
ment agencies and social media platforms. Consequently, although social media
platforms have implemented some mechanisms to combat drug tra fficking, they
are ineffective due to the aforementioned challenges.
Several research studies are building task-specific machine learning models to
detect drug trafficking activities on social media, including detection of drug deal-
2

ers [8, 9], drug trafficking events [10, 7, 11], and drug-related hashtags [12]. The
problem of detection of illicit drug tra fficking can be formulated as a supervised
machine learning problem, where the input is typically the text or/and images on
social media, and the output is drug trafficking activities to be detected. As such,
different machine learning approaches, such as Convolutional Neural Networks
(CNN) [7, 8, 11], long short-term memory networks (LSTM) [9], and Transformer
networks [7], can be applied to process the social media data. However, such task-
specific models have several limits. First, task-specific models apply supervised
learning to train the models, requiring high-quality labeled data to achieve good
performance. Unfortunately, annotating a large dataset on social media can be
challenging and time-consuming. Second, as platforms improve their detection
capabilities, drug dealers constantly adapt their text-based trafficking techniques
to avoid detection. This poses a substantial challenge for supervised learning
models, as they may struggle to decipher disguised language and euphemisms,
potentially resulting in the oversight of crucial information related to drug traf-
ficking activities.
Meanwhile, recent years have observed the emergence of powerful large lan-
guage models (LLMs) such as GPT [13] and LLaMA [14]. These models, trained
on huge datasets, have demonstrated surprising capabilities in various natural
language processing (NLP) tasks, such as natural language understanding, gen-
erating coherent and contextually relevant responses, and solving complex tasks
through text generation. LLMs have shown promise in helping with various real-
world tasks, including complex math problems [15], clinical decision support
[16], public health [17], open education [18], and global warming [19]. Unlike
the supervised learning paradigm, which requires large labeled data to train a
task-specific model, LLMs can perform NLP tasks with just a few or no exam-
ples, achieving results similar to those of state-of-the-art supervised models [20].
Therefore, LLMs provide an alternative solution to detect illicit drug tra fficking
on social media.
3

Inspired by the advance in large language models (LLMs), in this paper, we
propose to apply LLMs to detect illicit drug tra fficking activities from text data
on social media (e.g., textual information of posts on Instagram). Although im-
ages often go with text data on social media, previous studies [7, 8] show that text
data dominate the detection of illicit drug trafficking activities. Unlike supervised
learning that trains a model with input-label pairs, the LLM-based approach per-
forms a downstream task by reformulating the task with an appropriate textual
prompt, which bridges the task and the LLMs to enable in-context learning in an
autoregressive manner [13]. To apply LLMs for prediction tasks, we must modify
the original text into a textual prompt [21]. Consequently, the problem of LLM-
based drug trafficking detection boils down to the design of appropriate prompts.
To this end, we propose an analytical framework to composeknowledge-informed
prompts, which serve as the interface that humans can interact with and use LLMs
for the detection of drug tra fficking activities. The prompt is the combination of
knowledge, question, and original text to detect. To construct meaningful prompt
knowledge, our proposed framework integrates prior domain knowledge regarding
drug tra fficking behaviors, terminologies, and strategies used by drug dealers,
and acquired knowledge extracted from an LLM, ChatGPT in particular, with a few
examples. We further design an optimization method to optimize the prompts.
The prompt optimization use an iterative strategy [22] to elicit more accurate
factual knowledge about drug tra fficking than manually created prompts on the
benchmark. Meanwhile, Monte Carlo dropout [23] is applied to e ffectively in-
corporate prior knowledge specific to drug tra fficking behaviors than supervised
relation extraction models.
Finally, we assess our proposed framework through extensive experiments on
an illicit drug tra fficking dateset we collected from Instagram. Our framework
demonstrates superior performance compared to baseline models. Furthermore,
through conducting thorough evaluations, including ablation experiments and
assessments with varying input shots, we demonstrate the importance of prompt
4

design, the value of domain knowledge integration, and the optimal threshold of
input shots to maximize performance.
In summary, our research makes the following contributions:
• We conduct the first systematic study on leveraging large language models
(LLMs), such as ChatGPT, to detect illicit drug trafficking activities on social
media.
• We propose an analytical framework to compose knowledge-informed prompts,
which serve as the interface that humans can interact with and use LLMs for
the detection of drug trafficking activities.
• We design a prompt optimization method to further enhance the e ffective-
ness of the prompts.
• We demonstrate the e ffectiveness of the proposed framework through ex-
tensive experiments on an illicit drug tra fficking dateset we collected from
Instagram.
Our research contributes to the broader objective of improving online security
and public safety. Through the integrated prompts of prior knowledge and Chat-
GPT knowledge, our approach provides an effective tool to detect drug trafficking
activity on social media. Our research offers a practical and applicable tool for law
enforcement agencies, social media managers, and other stakeholders concerned
with online security and public safety.
The remainder of this paper is organized as follows: Section 2 provides an
overview of related work in drug tra fficking detection and large language mod-
els, Section 3 describes the proposed method in detail, Section 4 presents exper-
imental results and analysis, and Section 5 concludes the article while outlining
potential future avenues of research.
5

2. Related Work
2.1. Drug tra fficking detection on social media
As social media platforms have emerged critical channels for drug marketing
and illegal sale, how to effectively and efficiently detect illicit drug trafficking ac-
tivities becomes important in addressing this issue. There are a few studies that
build task-specific machine learning models to detect drug tra fficking activities
on social media, including detection of drug dealers [8, 9], drug trafficking events
[10, 7, 11], and drug-related hashtags [12]. For example, Li et al. [9] applied
long short-term memory networks (LSTM) to process textual data of Instagram
posts to detect and characterize illicit drug dealers on Instagram. Similarly, Zhao
et al. [11] combined both SVM and TextCNN to detect illicit drug ads. Since
social media posts contain both textual and image data, there are some research
on apply multimodal approach to drug tra fficking detection [8, 7, 10]. Qian et
al. [24] employed heterogeneous graph to capture multi-modal content and rela-
tional structured information from social media to detect illicit drug tra ffickers.
More recently, Hu et al. [12] proposed a framework that combined Bidirectional
Encoder Representations from Transformers (BERT) with Graph Convolutional
Network (GCN) to classify drug-related hashtags on Instagram.
Existing studies that built task-specific models for drug tra fficking detection
have several limits. First, they need large amount of high-quality labeled data
to train the models, however, data annotation is time-consuming and resource-
intensive. Second, as drug dealers constantly update their deceptive language and
euphemisms to avoid detection, a well-trained model might fail to perform the
detection task. As large language models advance, the challenges associated with
drug trafficking detection in social media are expected to be effectively addressed.
2.2. Large language models
Large language model (LLMs) are sophisticated artificial intelligence models
trained on vast amounts of text data and demonstrate advanced language pro-
6

cessing capabilities [25]. Several notable large language models have been devel-
oped, including OpenAI’s GPT (Generative Pre-trained Transformer) series and
Google’s BERT (Bidirectional Encoder Representations from Transformers). These
large language models are typically pre-trained on massive datasets, often com-
prising billions of sentences from various sources such as books, websites, and
articles. During pre-training, the models learn to predict missing words in sen-
tences, thereby gaining a deep understanding of grammar, context, and semantic
relationships. One prominent example of a large language model is ChatGPT [13]
developed by OpenAI.
Once pre-training is completed, LLMs can can perform various natural lan-
guage processing (NLP) tasks with just a few or no examples, achieving results
similar to those of state-of-the-art supervised models [20]. LLMs also have shown
promise in helping with various real-world tasks, including complex math prob-
lems [15], clinical decision support [16], public health [17].
2.3. Prompt engineering based on language models
Prompts are the interface for humans to interact with and use LLMs. LLM-
based approach performs a downstream task by reformulating the task with an
appropriate textual prompt, which bridges the task and the LLMs to enable in-
context learning in an autoregressive manner [13]. Prompt engineering [21] has
received increasing attention in recent years. Researchers have explored different
methods to design prompts that can improve the performance of language models
on specific tasks. For example, Shin et al. [22] proposed a method for designing
prompts to improve the performance of language models on various natural lan-
guage processing tasks. Their approach, AutoPrompt, leverages a small set of la-
beled examples to automatically generate prompts that guide the language model
toward the desired task. They achieved significant performance gains across vari-
ous benchmarks by fine-tuning the model with task-specific prompts. A proposed
method facilitates a chain-of-thought prompting approach, enabling expansive
language models to tackle intricate reasoning tasks by generating a sequence of
7

intermediate steps [26]. This methodology sheds light on the emergent property
of model scale while expanding the repertoire of reasoning tasks language mod-
els can proficiently undertake. An interactive system called PromptChainer has
been developed to facilitate the visual programming of LLM chains, empowering
individuals without AI expertise to prototype AI-infused applications [27]. How-
ever, these methods fail to take advantage of domain knowledge to enhance the
performance of the large-language model.
3. Methodology
In this section, we first formulate the problem of drug trafficking detection on
social media, and then introduce the knowledge-prompted large-language model
approach to the problem.
3.1. Problem Formulation
Our goal is to design an effective system to detect drug trafficking activities on
social media platforms accurately. Specifically, our objective is to classify whether
a social media post (e.g., a post on Instagram or a tweet on Twitter) contains infor-
mation related to the marketing and sales of illicit drugs so that the classification
can be applied to monitor drug tra fficking activities on social media platforms.
In this paper, we use only the textual data from the posts. However, images often
go with text on social media, but textual data have a dominating role in detecting
illicit drug trafficking activities [7, 8]. Let x denote the textual data in a post, our
goal is to build a predictive model that takes x as input and predicts a drug traf-
ficking labely∈{ 0,1}, wherey = 1 denotes the post is related to drug tra fficking
activities andy = 0 otherwise. The block highlighted in green in Figure 1 shows
an example of the textual data of an Instagram post annotated as a drug tra ffick-
ing post. In particular, we propose to leverage large language models (LLMs),
such as ChatGPT, so that we can
(1) To leverage the rich knowledge of LLMs acquired through training with large
datasets, and
8

Figure 1: Illustration of the proposed knowledge-informed prompt, which is the interface for hu-
mans to interact with and use ChatGPT for drug trafficking detection. The prompt x′ : [K,Q,x ] is
a tuple of knowledge K, question Q, and original text x. The pink font represents knowledge K
with masked words in purple, the blue font represents questionQ, green font represents original
textx (e.g., Instagram post captions/comments).
(2) To enable the detection with a few (i.e., few-shot learning where the LLM
model is given a few demonstrations of the task) or even no (i.e., zero-shot
learning) examples.
Different supervised learning, which trains a model with large size of input-
label pairs{(xi,yi)}i∈[N], we need to modify the original textx into a textual prompt
x′ to perform the drug tra fficking task. However, how to design appropriate
prompts is not a nontrivial task, as the prompts have an important impact on
the effectiveness of LLMs. As a result, the problem of LLM-based drug trafficking
detection boils down to the design of appropriate prompts, which is the focus of
this paper.
3.2. Overview of Proposed Framework
As shown in Figure 1, our proposed knowledge-informed promptx′ : [K,Q,x ] is
composed of knowledgeK, questionQ, and original textx. Then the knowledge-
9

Table 1: List of symbols used to describe the proposed method.
Notation Meaning
Reqk Request knowledge discovery based on a few-shot Instagram comments.
Resk Response extracted knowledge from a few-shot Instagram comments.
Reqs Request the combination and summarization of the extracted knowledge.
Ress Response that combines and summarizes the extracted knowledge.
Reqfu Request the fusion of extracted knowledge and domain knowledge.
Resfu Response the fusion of extracted knowledge and domain knowledge.
Reqdi
Request the detection of Instagram comments using the prompt after
randomly dropping out the ith iteration.
Resdi Response for the prediction of each input Instagram comment data.
informed promptx′ is the interface that humans can interact with and use Chat-
GPT for the detection of drug trafficking. ChatGPT utilizes this prompt to gener-
ate responses that help detect drug trafficking activities. The response component
represents the system output, providing valuable insights and detection results.
Figure 2: Framework of our proposed knowledge prompted ChatGPT. Blue arrows represent re-
quests to ChatGPT, while red arrows signify the corresponding responses from ChatGPT. Inputs
to the framework are indicated by text in blue, whereas outputs are denoted by text in red.
To design effective knowledge-informed prompts so as to leverage the capabili-
ties of large language models (LLMs) for the detection of drug tra fficking activi-
ties on social media, we propose an advanced analytical framework that integrates
10

prior domain knowledge and acquired knowledge extracted from an LLM, ChatGPT
in particular. As shown in Figure 2, the framework builds upon ChatGPT as its
core, combining the power of the large language model with prior knowledge and
acquired knowledge extracted from ChatGPT. Di fferent notations in the frame-
work, as shown in Table 1, represent distinct meanings and functions in terms of
knowledge request and response. This framework encompasses a series of steps
to design effective prompts to improve the model’s effectiveness in detecting drug
trafficking activities.
1. Knowledge extraction from ChatGPT. In this step, we leverage the capa-
bilities of ChatGPT to extract knowledge with a few shots of labeled data
{(xi,yi)}i∈[N], where N is a small number. We input relevant text passages
or queries into ChatGPT and utilize its language comprehension and gen-
eration capabilities to extract key facts, insights, and relationships related
to drug tra fficking activities. Various sources such as news articles, online
forums, and social networks are used to extract valuable information.
2. Knowledge fusion. The knowledge extracted from ChatGPT is then inte-
grated with domain-specific knowledge to improve the drug tra fficking de-
tection capabilities of the framework. Domain-specific knowledge includes
information from experts, research articles, and curated databases, provid-
ing a deep understanding of drug tra fficking patterns, terminology, smug-
gling techniques, and key entities involved. The integration process aligns
and reconciles the extracted knowledge with the domain knowledge, cap-
turing nuanced insights from both sources.
3. Prompt design based on integrated knowledge. To effectively prompt the
ChatGPT model, we design prompts that leverage integrated knowledge and
exploit areas of potential confusion. Confusion knowledge refers to specific
aspects or concepts that ChatGPT might struggle to understand or disam-
biguate accurately. By addressing and clarifying these confusion points in
the prompts, we guide the model’s attention and enhance its understanding
11

of drug trafficking-related text. The prompts may involve specific questions,
context framing, or the inclusion of key keywords related to drug trafficking
activities.
4. Prompt optimization. Prompt optimization aims to fine-tune the designed
prompts to maximize the performance of the ChatGPT model on drug traf-
ficking detection tasks. Monte Carlo drop is employed to iteratively improve
the prompts’ effectiveness. By analyzing the model’s responses to di fferent
prompts and measuring their impact on performance, we iteratively refine
the prompts to align the model’s behavior more closely with the desired
drug trafficking detection outcomes.
The pipeline of knowledge extraction, knowledge fusion, prompt design based
on confusion knowledge, and prompt optimization is crucial in enhancing the
model’s understanding and performance in identifying drug trafficking activities.
We elaborate the details for each part in subsequent sections.
3.3. Incorporating Prior Domain Knowledge
Domain-specific knowledge holds an immense importance in improving the
detection of drug trafficking activities on social media platforms. Domain experts
possess specialized knowledge and insights into drug tra fficking behaviors, ter-
minologies, and strategies used by drug dealers. By integrating this knowledge
into the detection framework, we can improve the accuracy and e ffectiveness of
identifying drug tra fficking. To leverage domain knowledge, we focus on three
key aspects: hashtags, contact information, and special symbols commonly used
by drug dealers to avoid detection. Table 2 provides examples and meanings for
each aspect.
• Hashtag: Drug sale-related hashtags are frequently used on social media
platforms to facilitate communication and advertising among drug dealers
and potential buyers. By identifying and analyzing these hashtags, we can
gain valuable information about drug tra fficking activities. For example,
12

Table 2: Types of domain knowledge for drug trafficking detection.
Name Meaning Example
Hashtag Drug sale-related hashtags #MDMA #Cocaine #LSD
Contact
information
Telephone number, email
address, and other private
social media accounts
Txt/WhatsApp.+1,7**.***.9414
Wichr/snapchat james*****52
kik james*****52
Special
symbol
Using Punctuation,
special characters, and
emojis to evade detection
M.D.M.A, C.O.C.A.I.N.E, L.s.d
M.o.l.l.y, SHRΘΘMS
CΘKE
hashtags like "#MDMA" or "#Cocaine" often indicate the sale or discussion
of specific drugs.
• Contact Information: Drug dealers often share contact information, such
as phone numbers or alternative social media accounts, to establish commu-
nication with potential buyers. By monitoring and analyzing this contact
information, we can detect and track drug tra fficking activities. Examples
of contact information include phone numbers with specific area codes or
messaging app usernames like "Telegram" or "Wickr."
• Special Symbols: To evade detection, drug dealers frequently use various
techniques, including the use of punctuation marks, special characters, or
emojis, to mask content related to drug trafficking. When we recognize and
interpret these special symbols, we can reveal the underlying drug-related
messages. Examples include variations in drug names using special char-
acters such as "M.D.M.A" or "C.O.C.A.I.N.E," or substituting letters with
similar-looking symbols like "SHRΘΘMS."
Incorporating domain-specific knowledge related to hashtags, contact infor-
mation, and special symbols provides valuable contextual insights that help un-
cover drug-trafficking discussions and improve the precision and recall of the de-
tection system. This domain knowledge will be fused with acquired knowledge
extracted from ChatGPT to design prompts.
13

3.4. Knowledge Fusion and Prompt Engineering
Note that given a text data x, our proposed knowledge-informed prompt x′ :
[K,Q,x ] is the combination of knowledge K, questionQ, and original textx. Fig-
ure 3 shows the workflow to compose the prompt.
Figure 3: Illustration of the workflow to compose prompt x′ : [K,Q,x ], which is a tuple of knowl-
edgeK, question Q, and original text x. The pink font represents knowledge K, blue font repre-
sents questionQ, green font represents original textx (e.g., Instagram post captions/comments).
14

3.4.1. Prompt – Knowledge
In particular, we compose the knowledge part K with prior domain knowledge
and acquired knowledge extracted from ChatGPT with a few shots of labeled data.
Knowledge Discovery with ChatGPT. Beyond the prior domain knowledge as dis-
cussed in Section 3.3, we also extract relevant knowledge with ChatGPT since
ChatGPT is trained on very large datasets. Specifically, we query ChatGPT with
a few shots of labeled data {(xi,yi)}i∈[N], where N is a small number, to guide
ChatGPT to generate informative and relevant responses. During fine-tuning, the
model learns to identify patterns, relationships, and insights within the drug traf-
ficking domain. This allows the model to acquire implicit knowledge from the
dataset and generate informed responses when asked for drug-trafficking-related
queries.
Knowledge Fusion as Prompt. Knowledge fusion is a critical component of the
prompt design process. It involves integrating relevant information from domain
knowledge and knowledge discovered by ChatGPT into the prompts provided
to the model. By fusing knowledge into the prompts, we provide the ChatGPT
model with additional context and cues related to drug tra fficking. This integra-
tion helps the model to make more accurate predictions and generate responses
that align with the nuances of drug tra fficking detection tasks. For example, a
prompt could include a snippet of domain knowledge about common drug traf-
ficking routes or the characteristics of illicit drug concealment methods. This
prompts the model to focus its attention on these aspects and generate more in-
sightful responses.
3.4.2. Prompt – Question
To further enhance the design of knowledge prompts, we identify specific
types of questions that generate informative responses related to the detection
of drug tra fficking. These questions are designed to target key aspects of drug
trafficking activities, methods, or indicators. For instance, questions like "What
are the signs of drug tra fficking in online communications?" or "How can drug
15

smuggling be detected at border checkpoints?" guide the model to provide rel-
evant information in its responses. By incorporating carefully crafted questions
into the prompts, we guide the ChatGPT model to generate more focused and
informative outputs for drug trafficking detection tasks.
3.5. Prompt Optimization with Monte Carlo Dropout
In this section, we present the methodology for prompt optimization, lever-
aging the Monte Carlo dropout technique to enhance the performance of the
knowledge-prompt design framework for drug trafficking detection.
The prompt optimization process aims to fine-tune the designed prompts to
maximize the performance of the ChatGPT model on drug tra fficking detection
tasks. We can identify keywords that significantly influence the model’s decisions
by systematically analyzing the impact of individual words in the prompt. The
prompt optimization is shown in Algorithm 1.
The algorithm, "Prompt Optimization with Monte Carlo Dropout," takes the
designed prompt, the number of Monte Carlo dropout iterations, and the dropout
probability as input. The algorithm iteratively performs the following steps:
• Create a copy of the designed prompt, optimized_prompt, to preserve the
original prompt (Step 1).
• Split optimized_prompt into a list of words.
• For each word in the prompt, perform the Monte Carlo dropout by replacing
the word with a "MASK" token (Steps 4-6).
• Perform Monte Carlo simulation on the modified prompt to obtain perfor-
mance metrics.
• Calculate the change in F1 score, score_change, based on the original and
simulated F1 scores.
16

Algorithm 1 Word Importance Score Calculation with Monte Carlo Dropout for
Prompt Optimization.
1: procedure Calculate Importance Scores(paragraph,num_iterations,dropout_prob)
2: Initialize an empty dictionary word_scores
3: Split the paragraph into a list of words
4: for iter in 1 to num_iterations do
5: Create a copy of the list of words called masked_words
6: Initialize an empty list called dropout_list
7: for word_index in 0 to length(masked_words)− 1 do
8: if random.random()< dropout_prob then
9: Append word_index to dropout_list
10: Set masked_words[word_index] as "MASK"
11: end if
12: end for
13: Create a prompt_knowledge by joining masked_words into a string
14: Perform Monte Carlo on prompt_knowledge to get performance metrics
15: Compute the change in score_change
16: for word_index in dropout_list do
17: if word_index not in word_scores then
18: Set word_scores[word_index] as 0.0
19: end if
20: Increment word_scores[word_index] by score_change
21: end for
22: end for
23: Sort word_scores by value in descending order, resulting in sorted_scores
24: return sorted_scores
25: end procedure
• Update the importance score of each word in the prompt by incrementing it
with score_change.
• Repeat Steps 2-6 for the desired number of iterations.
By optimizing the prompt using Monte Carlo dropout, we can identify and refine
the words that significantly impact the model’s performance in drug tra fficking
detection tasks.
The resulting optimized prompt provides valuable insight into the specific
words and their contributions to the model’s decision-making process. This en-
17

hanced understanding enables us to fine-tune the prompt and align the model’s
behavior more closely with the desired drug trafficking detection outcomes.
4. Experiments
4.1. Experimental Settings
In this subsection, we describe the experimental setup used to evaluate the per-
formance of the knowledge-prompted ChatGPT framework for drug tra fficking
detection. The experimental setup encompasses the dataset, model configuration,
evaluation metrics, and baselines.
• Dataset. To evaluate the framework’s e ffectiveness, we carefully selected
a comprehensive dataset called IDDIG that contains text samples related
to drug tra fficking on Instagram. Similar samples were removed from the
IDDIG data, resulting in a final set of 886 samples for the evaluation ex-
periments. There are 486 positive samples (i.e., drug tra fficking) and 400
negative samples (i.e., non-drug tra fficking). We propose a framework for
identifying positive samples. The dataset consists of labeled data for vali-
dation and testing, facilitating the computation of performance metrics. It
is thoughtfully curated to encompass various drug trafficking scenarios, re-
gions, and languages, ensuring the framework’s generalizability. Specifi-
cally, a random set of 40 samples was selected as input for the design of
knowledge prompts in each experiment. In contrast, the remaining samples
were set aside as a test set to assess the performance of the proposed method.
• Model Configuration. Our framework is based on the ChatGPT API, specif-
ically using the GPT Turbo 3.5 model. This model undergoes pre-training
on a significant corpus of text data to establish a robust language under-
standing. To accurately detect drug tra fficking, we optimize the ChatGPT
request prompt by incorporating the knowledge prompt design and opti-
mization techniques mentioned earlier. The model configuration involves
18

Table 3: Performance Metrics of Different Models
Model Accuracy Precision Recall F1 Score
BERT [28] 76.23% 75.39% 85.91% 79.78%
XLNet [29] 76.13% 75.44% 86.76% 79.92%
ALBERT [30] 77.62% 78.06% 83.14% 80.13%
DistilBERT [31] 80.30% 80.73% 86.03% 82.68%
RoBERTa [32] 82.78% 83.29% 88.29% 85.02%
Ours 94.58% 96.60% 93.42% 94.98%
several parameters, such as the number of iterations for word dropout, the
number of input samples, and the number of words to be dropped out in
each iteration. Parameter tuning can be performed to enhance the model’s
performance.
• Evaluation Metrics. To evaluate the performance of the knowledge-prompted
ChatGPT framework, various metrics have been used. The chosen metrics
encompass precision, recall, F1 score, and accuracy. Precision evaluates the
accuracy of identifying drug trafficking instances, while recall measures the
effectiveness of correctly identifying actual drug tra fficking instances. The
F1 score combines precision and recall, o ffering a balanced measure of the
model’s performance.
• Baselines. To compare the performance of the knowledge-prompted Chat-
GPT framework, it is important to establish appropriate baselines. Base-
lines include BERT [28], XLNet [29], ALBERT [30], DistilBERT [31], and
RoBERTa [32] for the detection of drug trafficking. These baselines provide
reference points to evaluate the effectiveness and superiority of the proposed
framework. Baseline models are trained and evaluated on the same dataset
as the knowledge-prompted ChatGPT framework, using the same evalua-
tion metrics to ensure a fair comparison.
19

4.2. Evaluation of knowledge-prompted ChatGPT for drug tra fficking detection
This section presents the evaluation results of our knowledge-prompted Chat-
GPT framework for drug tra fficking detection. We compare the performance of
our framework with several baseline models, including BERT, XLNet, ALBERT,
DistilBERT, and RoBERTa. The evaluation metrics include accuracy, precision,
recall, and F1 score (See Table 3).
We noted a significant enhancement across all evaluation metrics after com-
paring the outcomes with the baseline models. Our framework demonstrated su-
perior performance in drug tra fficking detection tasks by achieving higher accu-
racy, precision, recall, and F1 scores than all other models. Notably, the proposed
framework exhibited exceptional improvements, with nearly a 12% increase in
drug trafficking detection accuracy and an approximately 10% improvement in
F1 score, surpassing other baseline language models.
The significant performance gains can be attributed to incorporating domain-
specific knowledge, e ffective prompt design, and knowledge optimization tech-
niques employed in our framework. The integration of relevant knowledge and
the guidance provided through carefully designed prompts contribute to the frame-
work’s ability to detect drug trafficking activities accurately.
4.3. Assessing the performance of knowledge prompt ChatGPT with varying input
shots
To evaluate the impact of varying input shots on the performance of the knowledge-
driven ChatGPT framework for drug tra fficking detection, we conducted exper-
iments using di fferent numbers of input shots. The evaluation metrics include
accuracy, precision, recall, and F1 score.
The framework’s performance consistently improved with an increasing num-
ber of input shots. Using 40 shots yielded the best results, achieving an accu-
racy of 89.84% and an F1 score of 90.24%, while using five shots resulted in an
accuracy of 86.23% and an F1 score of 86.94%. These results indicate that the
knowledge-driven ChatGPT framework benefits from increasing input shots up
20

Table 4: Performance Metrics of Different Models
Shot number Accuracy Precision Recall F1 Score
5 shots 86.23% 90.63% 83.54% 86.94%
10 shots 88.71% 91.77% 87.24% 89.45%
20 shots 87.81% 90.91% 86.42% 88.61%
30 shots 87.13% 95.15% 80.66% 87.31%
40 shots 89.84% 95.41% 85.60% 90.24%
Table 5: Performance Metrics of Different Models
Prompt source knowledge Accuracy Precision Recall F1 Score
No prompt No knowledge 87.81% 90.21% 87.24% 88.70%
Domain expert Hashtag 87.81% 92.76% 84.36% 88.36%
Domain expert Contact information 87.36% 97.46% 79.01% 87.27%
Domain expert Special symbol 90.52% 89.11% 94.24% 91.60%
Domain expert All Knowledge (AK) 90.74% 98.10% 84.77% 90.95%
Ours w/o dropout 40 shots 89.84% 95.41% 85.60% 90.24%
Ours w/o dropout 40 shots + AK 91.87% 99.52% 85.60% 92.04%
Ours w/ dropout 40 shots + AK 94.58% 96.60% 93.42% 94.98%
to a certain point, leading to improved performance in drug trafficking detection
tasks. However, after reaching the optimal point (in this case, around 40 shots),
further increases in input shots may not necessarily yield significant performance
gains.
4.4. Evaluating Model Components through Ablation Experiments
To assess the individual contributions of di fferent model components in the
knowledge-driven ChatGPT framework for drug tra fficking detection, we con-
ducted ablation experiments. We evaluated the performance when removing or
modifying specific prompt sources and knowledge components. The evaluation
metrics include accuracy, precision, recall, and F1 score. The evaluation results
are summarized in Table 5.
Removing the prompt knowledge components, resulting in no prompt and no
knowledge, led to an accuracy of 87.81%, and an F1 score of 88.70%. When the
domain expert provided a drug-related hashtag as the knowledge prompt source,
21

the performance remained consistent with an accuracy of 87.81%. Still, the pre-
cision increased to 92.76%, albeit with a slightly lower recall of 84.36% and an
F1 score of 88.36%. Using the domain expert’s contact information as the prompt
source improved precision significantly to 97.46%. However, this change resulted
in a decreased recall of 79.01% and a slightly lower accuracy of 87.36%, with an
F1 score of 87.27%. Replacing the prompt source with a special symbol guided
by the domain expert yielded an accuracy of 90.52%, precision of 89.11%, recall
of 94.24%, and an F1 score of 91.60%. These results indicate that the special
symbol prompt source e ffectively captures the model’s attention and improves
its ability to identify drug trafficking activities. When all knowledge components
provided by the domain expert were included, the performance further improved.
The framework achieved an accuracy of 90.74% and an F1 score of 90.95%. This
highlights the significance of incorporating comprehensive domain knowledge to
enhance the framework’s performance.
Removing prompt knowledge components resulted in an accuracy of 87.81%
and an F1 score of 88.70%. Utilizing a drug-related hashtag as the knowledge
prompt source maintained an accuracy of 87.81%, but precision increased to
92.76% with a slightly lower recall of 84.36% and an F1 score of 88.36%. Us-
ing the domain expert’s contact information as the prompt source significantly
improved precision to 97.46%, albeit with decreased recall of 79.01%, accuracy of
87.36%, and an F1 score of 87.27%. Replacing the prompt source with a special
symbol guided by the domain expert yielded an accuracy of 90.52%, precision of
89.11%, recall of 94.24%, and an F1 score of 91.60%. Including all knowledge
components provided by the domain expert further enhanced performance, re-
sulting in an accuracy of 90.74% and an F1 score of 90.95%. These results demon-
strate the effectiveness of different prompt sources and highlight the importance
of incorporating comprehensive domain knowledge to enhance the framework’s
performance in drug trafficking detection.
Next, we examine the effect of Monte Carlo dropout and the number of input
22

shots. Without dropout, our framework with 40 shots achieved an accuracy of
89.84%, precision of 95.41%, recall of 85.60%, and an F1 score of 90.24%. How-
ever, the performance significantly improved when incorporating dropout with
the same number of shots. The framework achieved an accuracy of 91.87%, preci-
sion of 99.52%, recall of 85.60%, and an F1 score of 92.04%. Finally, our complete
framework with 40 shots and all knowledge components achieved the best per-
formance, with an accuracy of 94.58%, precision of 96.60%, recall of 93.42%, and
an impressive F1 score of 94.98%.
These experiments demonstrate the significance of prompt sources, knowl-
edge components, and the utilization of Monte Carlo dropout in enhancing the
accuracy and e ffectiveness of our framework for drug tra fficking detection. The
comprehensive integration of domain knowledge and the optimization of model
components contribute to the superior performance of our proposed approach.
4.5. Drug Tra fficking Detection Case Studies
4.5.1. Leveraging Monte Carlo Dropout for a Knowledge Prompt Example
In this subsection, we present case studies to demonstrate the e ffectiveness
of our proposed method for drug tra fficking detection. The case studies involve
the use of positive words and negative words as prompts, highlighting the top 10
words ranked by their calculated importance scores (See Table 6).
The prompts are designed to capture the characteristics of drug tra fficking
discussions observed in comments on Instagram. The identified positive words,
represented in green font, indicate significant features associated with drug traf-
fickings, such as drug names, delivery, non-standard communication platforms,
and evasion of law enforcement. For example, "address" and "delivery" are con-
sidered strong positive words that express key features of drug trafficking. These
words play a crucial role in improving the performance of ChatGPT in the de-
tection of drug tra fficking. The presence of "address" signifies the use of email
addresses as a means of communication, while "delivery" emphasizes fast deliv-
ery. These features may have been missing in ChatGPT’s understanding of drug
23

Table 6: Example Prompts by the proposed method.Green font Represents Positive words, and
Red font Represents Negative words.
Prompt TopK P Words N Words
The characteristics of drug tra fficking observed in
comments on Instagram. These characteristics
Top1 addresses emojis
include the use of coded language and aliases, pro-
moting drug availability, employing drug-related
Top2 delivery Instagram
hashtags, utilizing non-standard communication
platforms, and encouraging discreet customer
Top3 enforcement contact
contact. The comments often lack legal verifica-
tions or prescriptions, while emphasizing fast
Top4 drug employing
delivery and anonymity. These characteristics sug-
gest a desire to operate covertly and evade law
Top5 operate payment
enforcement, indicating illegal drug tra fficking.
Specifically, drug dealers on Instagram sell
Top6 as Wickr
illicit drugs by commenting with various contact
information (such as Wickr, Kik, Snapchat,
Top7 evade anonymity
email addresses, and telephone numbers), utilizing
specific hashtags related to drug names, sale
Top8 Instagram promoting
location, and Bitcoin payment, and using obfus-
cated descriptions that are difficult to track,
Top9 trafficking including
including emojis, special symbols, and Greek char-
acters.
Top10 on-standard and
trafficking, and their inclusion enhances the model’s ability to identify drug traf-
ficking activities accurately. On the contrary, the negative words, represented in
red font, signify the words that negatively a ffect the performance of ChatGPT in
detecting drug trafficking activities. These words hinder the model’s ability to de-
tect illicit drug-related content on social media platforms accurately. To enhance
the performance of drug tra fficking detection, negative words will be removed
from the analysis.
The calculated importance scores provide information on the relevance and
significance of each word on the detection of drug tra fficking. The top-ranked
words offer valuable clues to identify and monitor drug tra fficking activities on
social media platforms. By utilizing these prompts, our method enables a more
24

targeted and effective approach to detecting drug-related content and identifying
potential drug dealers.
The case studies highlight the capabilities of our proposed method in captur-
ing key characteristics of drug trafficking discussions, shedding light on the covert
nature of such activities, and providing law enforcement agencies and social me-
dia managers with valuable insights for intervention and prevention efforts.
4.5.2. A Comparative Analysis: Proposed Framework vs. Alternative Prompts
In this subsection, we present a comparative analysis of our proposed method
for the detection of drug trafficking, contrasting it with alternative prompts. There
are three alternative prompts: a prompt with no specific topic, a prompt focused
on domain knowledge, and a prompt based on extracted knowledge.
• Prompt a. No prompt.
• Prompt b. Drug dealers on Instagram utilize various methods to sell illicit
drugs. They typically comment with contact information (such as wickr,
Kik, snapchat, telegram, or telephone number), employ specific hashtags
(including names, sale locations, or bitcoin payment), and use obfuscated
descriptions with emojis, special symbols, and Greek characters to evade
tracking, effectively showcasing the drugs they have for sale.
• Prompt c. The characteristics of drug tra fficking include using coded lan-
guage and aliases, promoting the availability of drugs, using non-standard
platforms, and encouraging customers to contact the seller discreetly. The
comments also often lack legal verifications or prescriptions for drug pur-
chasing and may emphasize fast delivery or anonymity. These character-
istics can indicate a desire to operate covertly and evade detection by law
enforcement, pointing to illegal drug trafficking.
• Prompt d. The characteristics of drug tra fficking include using coded lan-
guage and aliases, promoting drug availability, employing drug-related hash-
25

tags, utilizing non-standard communication platforms, and encouraging dis-
creet customer contact. The comments often lack legal verifications or pre-
scriptions while emphasizing fast delivery and anonymity. These charac-
teristics suggest a desire to operate covertly and evade law enforcement,
indicating illegal drug tra fficking. Specifically, drug dealers on Instagram
sell illicit drugs by commenting with various contact information (such as
Wickr, Kik, Snapchat, Telegram, email addresses, and telephone numbers),
utilizing specific hashtags related to drug names, sale location, and Bitcoin
payment, and using obfuscated descriptions that are di fficult to track, in-
cluding emojis, special symbols, and Greek characters.
Based on the alternative prompts and the proposed prompt (i.e., Prompt d.),
we utilize sample data and examine the effectiveness of different prompts in iden-
tifying drug tra fficking activities, as shown in Table 7. It illustrates the com-
parison by providing four different prompts: prompt a, representing no prompt;
prompt b, which includes all knowledge; prompt c, comprising extracted knowl-
edge; and prompt d, a fusion of prompt b and prompt c. Each sample in the
table is labeled with either a positive (P) or negative (N) indication based on the
presence or absence of drug trafficking elements.
In Case 1, ChatGPT-based methods accurately detect drug tra fficking despite
the presence of contact information (e.g., WhatsApp, Wickr, Kik, Snapchat) and
drug-related hashtags suggest potential drug tra fficking activity. This showcases
the e ffectiveness of our approach in identifying drug tra fficking activities even
when perpetrators employ deceptive techniques. However, there are instances
where ChatGPT makes mistakes. Case 2, although unrelated to drug tra fficking,
shares similarities that may lead to erroneous predictions without prompts. This
highlights the importance of prompts in guiding the model and minimizing false
positives. Interestingly, Case 3 reveals that ChatGPT can also make mistakes even
when provided with domain knowledge as a prompt. In some cases, including
domain knowledge may introduce noise and negatively impact the model’s per-
26

Table 7: Contrasting the Proposed Method with Alternative Prompts: A Comparative Analysis.
Prompt a. Represents no prompt, Prompt b. Represents Prompt with All Knowledge, Prompt c.
Represents Prompt with Extracted Knowledge, Prompt d. Represents Prompt that fusing Prompt
b. and Prompt c. "P" represents drug trafficking label or prediction, while "N" represents non-drug
trafficking. Red fonts indicate wrong predictions.
ID Cases
1
WHαTSαP // TEXT +1 760*****43ωICKR// KIK //Snαpchαt —X****ver
SECURED/DISCREET DELIVERY BUY LSD, MDMA, DMT,SHRΘΘMS,
PILLS, CΘKE & more #lsd#shrooms #shroomforsale #magicshrooms? #tabs
Label P Prompt a. P Prompt b. P Prompt c. P Prompt d. P
2
HOW TO AVOID RELIANCE ON PILLS ? #medication Synovation Medical
Group offers a Functional Restoration Program where our physicians help
patients overcome chronic pain through an interdisciplinary approach so
they can return to normal work and life. This program helps -Increasing
the reliance on one’s self-Decreasing pain medications #painmedication
#healthcare #medicalcare #chronicpain #healthiswealth #opioidcrisis "
Label N Prompt a. P Prompt b. N Prompt c. N Prompt d. N
3
#psychedelic #psy #psytime #psychedelicrock #magicmushrooms #lsdtabs
#shrooms #trippyvibes #mdmaofficials #microdot #purpleacid #blotteracid
Label P Prompt a. P Prompt b. N Prompt c P Prompt d. P
4
M.D.M.A n N.E.M.B.U.T.A.L, K.U.S.H, C.O.C.A.I.N.E,A.C.I.D,(L.s.d n C.a.r.t)
Txt/WhatsApp ..+1,*** Telegram:*** Wickr: *** M.Md,L.s.d n M.o.l.l.y ,a.d.i.e.s
Label P Prompt a. P Prompt b. P Prompt c. N Prompt d. P
5
Self Medicated ?#weed #marijuana #cbd #stoner #ganja #indica #sativa
#kush #maryjane #dank #medicalmarijuana #bong #hemp #stoned #bhfyp
Label N Prompt a. N Prompt b. P Prompt c. N Prompt d. P
formance compared to having no prompt at all. This suggests that the prompt
design and knowledge extraction must be carefully considered. When Instagram
drug trafficking events involve special characters such as punctuation marks, the
automatically extracted knowledge may hurt ChatGPT’s predictions. These cases
emphasize the need for robust methods to handle different types of input data and
ensure accurate detection. Prompt d, which includes prompt b (domain knowl-
edge), may sometimes lead to similar mistakes, as observed in Case 5. This high-
lights the complexity of balancing the inclusion of domain knowledge and avoid-
ing potential pitfalls associated with prompt-based approaches.
27

These case studies provide valuable insights into the performance of our method,
highlighting its ability to distinguish between positive and negative samples based
on the prompts used. The results showcase the importance of prompt design
and the integration of domain knowledge in enhancing drug trafficking detection
mechanisms.
5. Discussions
This section discusses the key findings and implications of our research on
the knowledge prompted ChatGPT framework for drug trafficking detection. We
address the framework’s performance, the e ffectiveness of di fferent model com-
ponents, and the potential limitations and future directions of the research.
5.1. Performance of the Framework
The evaluation results demonstrate the superior performance of our knowledge-
prompted ChatGPT framework compared to baseline models. Our framework
achieved an accuracy of 94.58%, precision of 96.60%, recall of 93.42%, and an F1
score of 94.98%. These results highlight the e ffectiveness of leveraging domain-
specific knowledge, well-designed prompts, and prompt optimization techniques
in enhancing drug trafficking detection capabilities.
Comparisons with state-of-the-art models such as BERT, XLNet, ALBERT, Dis-
tilBERT, and RoBERTa further validate the superiority of our framework. It con-
sistently outperformed these models regarding accuracy, precision, recall, and F1
score, indicating its ability to capture drug tra fficking activities accurately and
make informed predictions.
5.2. E ffectiveness of Model Components
The ablation experiments provided valuable insights into the e ffectiveness of
different model components. Removing the prompt source and knowledge com-
ponents significantly decreased performance, underscoring the importance of in-
corporating domain knowledge and well-crafted prompts. Our framework’s abil-
28

ity to fuse domain knowledge into the prompts, guided by request-related ques-
tions and knowledge optimization techniques, played a crucial role in achieving
the observed performance gains.
The analysis of varying input shots showed that the framework’s performance
improved with increasing shots up to an optimal point. Beyond that point, further
increases in input shots did not yield significant performance gains. This suggests
a threshold beyond which additional knowledge may not contribute substantially
to drug trafficking detection tasks.
5.3. Limitations and Future Directions
While our knowledge prompted ChatGPT framework demonstrated impres-
sive performance, several limitations should be considered. First, the framework’s
effectiveness heavily relies on the quality and comprehensiveness of the domain
knowledge integrated into the prompts. Further e fforts are required to continu-
ously update and refine the knowledge base to adapt to evolving drug trafficking
patterns and techniques.
Second, the evaluation focused on a specific dataset and task. Additional eval-
uations across different datasets and scenarios are needed to validate the general-
izability of the framework.
Furthermore, the interpretability of the framework can be enhanced by explor-
ing techniques such as attention mapping or explainable AI methods. This would
enable a better understanding of the model’s decision-making process and help
address potential biases or limitations.
Future research directions could involve exploring more advanced language
models, such as GPT-4 or similar architectures, to improve the framework’s per-
formance. Additionally, investigating multi-modal approaches that combine text
with other forms of data, such as images or network traffic, could provide a more
comprehensive understanding of drug trafficking activities.
29

6. Conclusions
This research presented a knowledge-prompted ChatGPT framework for drug
trafficking detection. The framework leverages domain-specific knowledge, well-
designed prompts, and prompt optimization techniques to improve the perfor-
mance of the ChatGPT model in accurately identifying and labeling drug traf-
ficking activities. Our framework demonstrates superior performance compared
to baseline models, achieving an accuracy of 94.58%, precision of 96.60%, recall
of 93.42%, and an F1 score of 94.98%. By integrating domain knowledge into
the prompts, our framework captures nuanced insights, identifies key indicators,
and provides actionable information for the detection of drug tra fficking. The
knowledge fusion technique, guided by request-related questions and knowledge
optimization, contributes to the interpretability and e ffectiveness of the frame-
work. We conducted thorough evaluations, including ablation experiments and
assessments with varying input shots, to understand the impact of different model
components and input variations. The results revealed the importance of prompt
design, the value of domain knowledge integration, and the optimal threshold of
input shots to maximize performance.
Although our framework exhibits promising results, there are limitations to
consider. The framework’s e ffectiveness is heavily dependent on the quality and
comprehensiveness of the domain knowledge integrated into the prompts. The
generalizability of the framework should be further validated by applying it to
diverse datasets and scenarios. Enhancing the interpretability of the framework
and exploring advanced language models are potential areas for future research.
The knowledge-prompted ChatGPT framework has great potential in address-
ing real-world challenges related to drug trafficking detection. By combining the
power of language models with domain expertise, the framework contributes to
advancing natural language processing techniques for combating illicit activities.
Its performance superiority over baseline models shows its practical applicability
and potential for implementation in real-world settings.
30

Overall, this research contributes to the growing body of knowledge-driven
approaches in natural language processing and highlights the importance of in-
corporating domain-specific knowledge to enhance model performance. The frame-
work of knowledge-prompted ChatGPT is a stepping stone for future advance-
ments in the field, with potential applications in various domains beyond drug
trafficking detection such as community and key player detection.
ACKNOWLEDGEMENTS
The NSF partially supports this work under grant CMMI-2146076 and CNS-
2125958.
References
[1] S. D. Morris, Corruption, drug tra fficking, and violence in mexico, The
Brown Journal of World Affairs 18 (2) (2012) 29–43.
[2] S. D. Morris, Drug tra fficking, corruption, and violence in mexico: mapping
the linkages, Trends in organized crime 16 (2013) 195–220.
[3] P . Doherty, P . Rudol, A uav search and rescue scenario with human body
detection and geolocalization, in: Australasian Joint Conference on Artificial
Intelligence, Springer, 2007, pp. 1–13.
[4] J. Demant, S. A. Bakken, A. Oksanen, H. Gunnlaugsson, Drug dealing on
facebook, snapchat and instagram: A qualitative analysis of novel drug mar-
kets in the nordic countries, Drug and alcohol review 38 (4) (2019) 377–385.
[5] B. A. Liang, T. K. Mackey, Prevalence and global health implications of social
media in direct-to-consumer drug advertising, Journal of Medical Internet
Research 13 (3) (2011) e1775.
31

[6] L. Moyle, A. Childs, R. Coomber, M. J. Barratt, # drugsforsale: An explo-
ration of the use of social media and encrypted messaging apps to supply
and access drugs, International Journal of Drug Policy 63 (2019) 101–110.
[7] C. Hu, M. Yin, B. Liu, X. Li, Y. Ye, Detection of illicit drug tra fficking
events on instagram: A deep multimodal multilabel learning approach, in:
Proceedings of the 30th ACM International Conference on Information &
Knowledge Management, 2021, pp. 3838–3846.
[8] C. Hu, M. Yin, B. Liu, X. Li, Y. Ye, Identifying illicit drug dealers on instagram
with large-scale multimodal data fusion, ACM Transactions on Intelligent
Systems and Technology (TIST) 12 (5) (2021) 1–23.
[9] J. Li, Q. Xu, N. Shah, T. K. Mackey, A machine learning approach for the
detection and characterization of illicit drug dealers on instagram: model
evaluation study, Journal of medical Internet research 21 (6) (2019) e13803.
[10] X. Yang, J. Luo, Tracking illicit drug dealing and abuse on instagram using
multimodal analysis, ACM Transactions on Intelligent Systems and Technol-
ogy (TIST) 8 (4) (2017) 1–15.
[11] F. Zhao, P . Skums, A. Zelikovsky, E. L. Sevigny, M. H. Swahn, S. M. Strasser,
Y. Huang, Y. Wu, Computational approaches to detect illicit drug ads and
find vendor communities within social media platforms, IEEE/ACM Trans-
actions on Computational Biology and Bioinformatics 19 (1) (2022) 180–191.
[12] C. Hu, B. Liu, Y. Ye, X. Li, Fine-grained classification of drug trafficking based
on instagram hashtags, Decision Support Systems 165 (2023) 113896.
[13] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P . Dhariwal, A. Nee-
lakantan, P . Shyam, G. Sastry, A. Askell, et al., Language models are few-
shot learners, Advances in neural information processing systems 33 (2020)
1877–1901.
32

[14] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux, T. Lacroix,
B. Rozière, N. Goyal, E. Hambro, F. Azhar, et al., Llama: Open and e fficient
foundation language models, arXiv preprint arXiv:2302.13971 (2023).
[15] I. Drori, S. Zhang, R. Shuttleworth, L. Tang, A. Lu, E. Ke, K. Liu, L. Chen,
S. Tran, N. Cheng, et al., A neural network solves, explains, and generates
university math problems by program synthesis and few-shot learning at hu-
man level, Proceedings of the National Academy of Sciences 119 (32) (2022)
e2123433119.
[16] S. Liu, A. P . Wright, B. L. Patterson, J. P . Wanderer, R. W. Turer, S. D. Nel-
son, A. B. McCoy, D. F. Sittig, A. Wright, Using AI-generated suggestions
from ChatGPT to optimize clinical decision support, Journal of the Ameri-
can Medical Informatics Association 30 (7) (2023) 1237–1245.
[17] S. S. Biswas, Role of chat gpt in public health, Annals of biomedical engi-
neering 51 (5) (2023) 868–869.
[18] M. Firat, How chat gpt can transform autodidactic experiences and open
education, Department of Distance Education, Open Education Faculty,
Anadolu Unive (2023).
[19] S. S. Biswas, Potential use of chat gpt in global warming, Annals of biomedi-
cal engineering 51 (6) (2023) 1126–1127.
[20] J. Wei, Y. Tay, R. Bommasani, C. Ra ffel, B. Zoph, S. Borgeaud, D. Yogatama,
M. Bosma, D. Zhou, D. Metzler, E. H. Chi, T. Hashimoto, O. Vinyals, P . Liang,
J. Dean, W. Fedus, Emergent abilities of large language models, Transactions
on Machine Learning ResearchSurvey Certification (2022).
[21] P . Liu, W. Yuan, J. Fu, Z. Jiang, H. Hayashi, G. Neubig, Pre-train, prompt,
and predict: A systematic survey of prompting methods in natural language
processing, ACM Comput. Surv. 55 (9) (jan 2023).
33

[22] T. Shin, Y. Razeghi, R. L. Logan IV, E. Wallace, S. Singh, Autoprompt:
Eliciting knowledge from language models with automatically generated
prompts, in: Proceedings of the 2020 Conference on Empirical Methods in
Natural Language Processing (EMNLP), 2020, pp. 4222–4235.
[23] P . Goel, L. Chen, On the robustness of monte carlo dropout trained with
noisy labels, in: Proceedings of the IEEE/CVF Conference on Computer Vi-
sion and Pattern Recognition, 2021, pp. 2219–2228.
[24] Y. Qian, Y. Zhang, Y. Ye, C. Zhang, et al., Distilling meta knowledge on het-
erogeneous graph for illicit drug tra fficker detection on social media, Ad-
vances in Neural Information Processing Systems 34 (2021) 26911–26923.
[25] W. X. Zhao, K. Zhou, J. Li, T. Tang, X. Wang, Y. Hou, Y. Min, B. Zhang,
J. Zhang, Z. Dong, et al., A survey of large language models, arXiv preprint
arXiv:2303.18223 (2023).
[26] J. Wei, X. Wang, D. Schuurmans, M. Bosma, E. Chi, Q. Le, D. Zhou, Chain
of thought prompting elicits reasoning in large language models, arXiv
preprint arXiv:2201.11903 (2022).
[27] T. Wu, E. Jiang, A. Donsbach, J. Gray, A. Molina, M. Terry, C. J. Cai,
Promptchainer: Chaining large language model prompts through visual pro-
gramming, in: CHI Conference on Human Factors in Computing Systems
Extended Abstracts, 2022, pp. 1–10.
[28] J. Devlin, M.-W. Chang, K. Lee, K. Toutanova, Bert: Pre-training of
deep bidirectional transformers for language understanding, arXiv preprint
arXiv:1810.04805 (2018).
[29] Z. Yang, Z. Dai, Y. Yang, J. Carbonell, R. R. Salakhutdinov, Q. V. Le, Xl-
net: Generalized autoregressive pretraining for language understanding,
Advances in neural information processing systems 32 (2019).
34

[30] Z. Lan, M. Chen, S. Goodman, K. Gimpel, P . Sharma, R. Soricut, Albert: A lite
bert for self-supervised learning of language representations, arXiv preprint
arXiv:1909.11942 (2019).
[31] V. Sanh, L. Debut, J. Chaumond, T. Wolf, Distilbert, a distilled version of
bert: smaller, faster, cheaper and lighter, arXiv preprint arXiv:1910.01108
(2019).
[32] Y. Liu, M. Ott, N. Goyal, J. Du, M. Joshi, D. Chen, O. Levy, M. Lewis,
L. Zettlemoyer, V. Stoyanov, Roberta: A robustly optimized bert pretraining
approach, arXiv preprint arXiv:1907.11692 (2019).
35
