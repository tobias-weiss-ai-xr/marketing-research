---
title: 'SalesRLAgent: A Reinforcement Learning Approach for Real-Time Sales Conversion Prediction and
  Optimization'
url: https://arxiv.org/abs/2503.23303
category: ai-marketing
subcategory: measurement
date: 2025-03
venue: arXiv preprint arXiv:2503.23303
authors:
- Nandakishor M.
source: arxiv
pdf_url: https://arxiv.org/pdf/2503.23303
pages: 6
chars: 28451
fetched_at: '2026-11-08T13:30:55+00:00'
kb_version: 1
---

# SalesRLAgent: A Reinforcement Learning Approach for Real-Time Sales Conversion Prediction and Optimization

arXiv:2503.23303v1  [cs.LG]  30 Mar 2025
SalesRLAgent: A Reinforcement Learning
Approach for Real-Time Sales Conversion
Prediction and Optimization
Nandakishor M
Deepmost Innovations
nandakishor@deepmostai.com
Abstract—Current approaches to sales conversation analysis
and conversion prediction typically rely on Large Language Mod-
els (LLMs) combined with basic retrieval augmented generat ion
(RAG). These systems, while capable of answering questions , fail
to accurately predict conversion probability or provide st rategic
guidance in real time. In this paper , we present SalesRLAgen t,
a novel framework leveraging specialized reinforcement le arning
to predict conversion probability throughout sales conver sations.
Unlike systems from Kapa.ai, Mendable, Inkeep, and others t hat
primarily use off-the-shelf LLMs for content generation, o ur
approach treats conversion prediction as a sequential deci sion
problem, training on synthetic data generated using GPT-4O
to develop a specialized probability estimation model. Our
system incorporates Azure OpenAI embeddings, turn-by-tur n
state tracking, and meta-learning capabilities to underst and
its own knowledge boundaries. Evaluations demonstrate tha t
SalesRLAgent achieves 96.7% accuracy in conversion predic tion,
outperforming LLM-only approaches by 34.7% while offering
signiﬁcantly faster inference. Furthermore, integration with ex-
isting sales platforms shows a 43.2% increase in conversion rates
when representatives utilize our system’s real-time guida nce.
SalesRLAgent represents a fundamental shift from content g ener-
ation to strategic sales intelligence, providing moment-b y-moment
conversion probability estimation with actionable insigh ts for
sales professionals.
Index Terms —reinforcement learning, sales conversion pre-
diction, conversation analysis, meta-learning, sequenti al decision
making, real-time guidance, embeddings, sales intelligen ce
I. I NTRODUCTION
The sales profession has increasingly embraced AI tools to
enhance performance, with numerous platforms now offering
chatbots, knowledge assistants, and conversation analyti cs.
Despite these advances, existing solutions primarily focu s on
retrieving information or generating responses rather tha n pro-
viding strategic sales intelligence. Most commercial syst ems
from providers like Kapa.ai, Mendable, and Inkeep function
essentially as gloriﬁed RAG (Retrieval Augmented Genera-
tion) systems, connecting Large Language Models (LLMs) to
company knowledge bases without truly understanding sales
dynamics [1].
These approaches face several fundamental limitations in
sales contexts:
• They cannot accurately predict conversion probability in
real time
• They lack turn-by-turn tracking of how conversation
dynamics affect likelihood of sale
• They provide generic rather than strategically-timed guid -
ance
• They operate reactively to queries rather than proactively
guiding sales strategy
• They have no meta-learning capability to understand the
boundaries of their knowledge
In this paper, I present SalesRLAgent, a novel framework
that reimagines sales AI as a specialized reinforcement lea rn-
ing system focused on conversion prediction and optimizati on.
Rather than treating sales conversations as simple informa tion
retrieval problems, SalesRLAgent models them as sequentia l
decision processes where each exchange impacts conversion
probability.
The key contributions of this work include:
• A reinforcement learning architecture speciﬁcally de-
signed for sales conversation analysis and conversion
prediction
• A synthetic data generation pipeline leveraging GPT-4O
to create diverse and realistic sales conversations
• Novel state representation techniques using Azure Ope-
nAI embeddings (3072 dimensions) with sales-speciﬁc
features
• A meta-learning approach enabling the system to express
conﬁdence in its predictions based on conversation simi-
larity to training data
• Integration mechanisms providing real-time guidance
within existing sales platforms
• Extensive comparative evaluation demonstrating signif-
icant performance improvements over LLM-based ap-
proaches
Our ﬁndings show that specialized reinforcement learning
models signiﬁcantly outperform even the most advanced LLM-
based systems in sales conversion tasks, with SalesRLAgent
achieving 96.7% prediction accuracy compared to 62% for
state-of-the-art LLM solutions. More importantly, when de -
ployed in real-world sales environments, the system demon-
strated a 43.2% improvement in actual conversion rates.
II. R ELATED WORK
A. LLM-Based Sales Assistants
Several commercial platforms have developed LLM-based
sales assistants, including Kapa.ai [2], Mendable [3], and

Inkeep [4]. These systems primarily utilize APIs from
providers like OpenAI, Anthropic, and Google to connect
their models with company knowledge bases. While effective
for question answering, their architecture fundamentally limits
their ability to model the complex, sequential nature of sal es
conversations [5].
Gong’s revenue intelligence platform [6] offers conversat ion
analytics but relies primarily on pattern recognition rath er than
predictive modeling. Similarly, Chorus.ai [7] provides po st-
conversation analysis but lacks real-time capabilities.
B. Reinforcement Learning in Conversational AI
Reinforcement Learning (RL) has shown promise in con-
versational tasks. Work by Li et al. [8] demonstrated how
RL can optimize dialogue policies, while Asghar et al. [9]
explored using RL for dialogue generation. However, these
applications focused on general conversational quality ra ther
than the speciﬁc dynamics of sales conversion.
In the sales domain, Takanobu et al. [10] proposed an RL
framework for dialogue policy in task-oriented scenarios b ut
did not address conversion prediction or real-time guidanc e.
Henderson et al. [16] highlighted the importance of proper
experimental methodology in reinforcement learning appli ca-
tions, which guided our rigorous evaluation approach.
C. Conversion Prediction Models
Traditional conversion prediction models, as surveyed by
Sakar et al. [11], typically use classiﬁcation approaches w ith
features extracted from customer behavior data. The closes t
work to ours is from Y ang et al. [14], who applied deep
learning to optimize conversion funnels in e-commerce. How -
ever, their approach focused on web navigation rather than
complex conversation dynamics, and lacked the meta-learni ng
capabilities we’ve developed for uncertainty estimation.
To the best of my knowledge, no existing system has
successfully combined reinforcement learning, Azure Open AI
embeddings, and meta-learning for real-time sales conver-
sion prediction and guidance, making SalesRLAgent a novel
contribution to both academic research and practical sales
technology.
III. D ATA GENERATION AND PROCESSING
A. Dataset Construction
Creating a high-quality dataset of sales conversations
presented signiﬁcant challenges. Unlike academic dialogu e
datasets, real sales conversations contain sensitive info rmation
and are rarely publicly available. To address this challeng e, I
developed a synthetic data generation approach:
• Synthetic data generation using advanced prompting of
GPT-4O
• Carefully designed templates for different sales scenario s
across 15 industries
• Programmatic variation of conversation parameters
(length, style, objection types)
• Controlled simulation of conversations using multiple
LLM agents
Our ﬁnal dataset comprised over 1.2 million synthetic
conversations. I found that the quality of GPT-4O’s output
was sufﬁcient to train effective models without requiring a ctual
sales data. Each conversation included:
• Complete conversation transcript
• Speaker information (customer vs. sales representative)
• Conversion outcome (binary)
• Timestamped conversion probability at each turn
• Simulated customer engagement metrics
• Product/service category and industry
Conversation lengths varied from 3 to 27 turns, with a me-
dian of 8 turns. The dataset had a roughly balanced distribut ion
of positive (converted) and negative (non-converted) outcomes,
with a slight bias toward negative outcomes (56%) that reﬂec ts
real-world sales dynamics.
B. Data Processing and Embedding
Raw conversation data required substantial preprocessing to
create useful training examples for our reinforcement lear ning
approach. Our pipeline included:
1) Text cleaning and normalization
2) Entity standardization across generated conversations
3) Conversation segmentation into turns
4) Feature extraction for each conversation turn
5) Embedding generation using Azure OpenAI’s embedding
model
For embeddings, we used Azure OpenAI’s embedding
model, which provides 3072-dimensional embeddings that
effectively capture semantic relationships. Honestly, I i ni-
tially wanted to build a custom embedding model, but after
experimenting with the Azure OpenAI model, I found its
performance was surprisingly good for our use case, so we
stuck with it.
We processed both:
• Semantic content (what was said)
• Conversational dynamics (how it was said)
This approach used the standard 3072-dimensional embed-
dings without customization, but with domain-speciﬁc feat ure
engineering layered on top.
C. State Representation Design
A critical innovation in our approach is the state represen-
tation used for reinforcement learning. Rather than treati ng
each conversation turn independently, we designed a state
representation that captures the evolving dynamics of the
conversation:
1) Conversation history embeddings (weighted by recency
and importance)
2) Turn-speciﬁc features (speaking time, question density ,
sentiment)
3) Customer engagement signals (response time, message
length, question asking)
4) Sales technique identiﬁcation (SPIN selling, value sell ing,
etc.)
5) Objection and interest detection

The complete state vector combined these elements into a
comprehensive representation that enabled our RL agent to
accurately model the sales process as a sequential decision
problem.
IV. R EINFORCEMENT LEARNING ARCHITECTURE
A. Modeling Approach
We formulate the sales conversion prediction task as a
sequential decision problem where:
• States represent the conversation at each turn
• Actions correspond to conversion probability estimates
• Rewards measure the accuracy of these predictions
This formulation allows us to leverage reinforcement learn -
ing to train a model that not only predicts ﬁnal conversion
outcomes but tracks conversion probability throughout the
conversation.
I personally found that this sequential approach captured
sales dynamics much more effectively than traditional clas -
siﬁcation models. Sales conversations often pivot on speci ﬁc
exchanges, and our model learned to identify these critical
moments.
B. Model Architecture
The core of SalesRLAgent is a reinforcement learning
architecture consisting of:
• A state encoder network that processes Azure OpenAI
embeddings and features
• A policy network that estimates conversion probability
based on the current state
• A value network that estimates the expected cumulative
reward
• A meta-learning module that assesses prediction conﬁ-
dence
We experimented with several RL algorithms, ultimately
ﬁnding that a specialized reinforcement learning algorith m
with the following characteristics performed best:
1) Strong policy regularization to prevent overﬁtting
2) Conservative policy updates to maintain stability
3) Adaptive learning rates based on prediction difﬁculty
4) Distribution-aware learning to handle uncertainty
The model architecture includes several specialized compo -
nents:
C. Meta-Learning for Uncertainty Estimation
A key innovation in SalesRLAgent is its meta-learning
capability [15]. Unlike typical black-box models, our syst em
can estimate its own conﬁdence in predictions based on:
• Similarity to conversations in the training data
• Consistency of predictions across model ensembles
• Pattern recognition of conversation structures
• Identiﬁcation of novel elements not present in training
This meta-learning component allows SalesRLAgent to
know when it doesn’t know—a critical capability for produc-
tion systems. When the system encounters conversations wit h
Algorithm 1 Conversion Probability Estimation
1: function ESTIMATE CONVERSION (conversation, turn)
2: history← ExtractHistory(conversation, turn)
3: embeddings← GenerateAzureEmbeddings(history)
4: f eatures← ExtractFeatures(history)
5: state← CombineState(embeddings, f eatures)
6: policy← PolicyNetwork(state)
7: value← V alueNetwork(state)
8: conf idence← ConﬁdenceEstimation(state, policy)
9: return {probability : policy, conf idence :
conf idence}
10: end function
unfamiliar patterns, it can explicitly communicate lower c on-
ﬁdence rather than making potentially misleading predicti ons.
I spent countless late nights tuning this meta-learning ap-
proach, motivated by early deployments where I noticed the
model sometimes made conﬁdent but incorrect predictions
on unusual conversation patterns. The resulting uncertain ty
estimation has proven invaluable in production systems.
D. Training Methodology
Training SalesRLAgent required a carefully designed ap-
proach to handle the diverse and sometimes noisy nature
of synthetically generated conversation data. Our trainin g
procedure included:
1) Initial supervised learning phase to establish reasonab le
policy initialization
2) Reinforcement learning with carefully constructed rewa rd
functions
3) Curriculum learning, starting with simpler conversatio ns
4) Adversarial training with challenging counter-example s
5) Ensemble techniques to improve robustness
6) Specialized batch construction to balance conversation
types
We trained on a standard CPU infrastructure, which honestly
surprised me by how well it performed. The entire training
process took approximately 6 hours, which was much faster
than I initially expected given the complexity of the model
and the size of our dataset.
V. S YSTEM INTEGRATION AND DEPLOYMENT
A. Real-time Inference Pipeline
Converting our trained model into a production system
required careful engineering. The complete inference pipe line
includes:
1) Conversation capturing and preprocessing
2) Incremental embedding generation using Azure OpenAI
3) State tracking and update
4) Probability prediction and conﬁdence estimation
5) Strategic guidance generation
6) CRM and communication tool integration
To meet stringent latency requirements (under 100ms), we
implemented several optimizations:

• Model quantization (8-bit precision with minimal accu-
racy loss)
• Embedding caching for repeated conversation elements
• Incremental state updates rather than full recalculation
• CPU optimization for multi-user environments
• Asynchronous guidance generation
B. Advanced Orchestration Layer
A critical component of our system is a sophisticated
orchestration layer that handles multi-node context retri eval
and processing. This directed graph architecture routes co nver-
sations through specialized processing nodes for contextu ally
relevant information retrieval.
Our implementation integrates:
• High-performance vector search for similarity matching
• Caching layers for optimized retrieval
• State-based workﬂow orchestration for complex conver-
sation patterns
• Dynamic prompt engineering based on conversion prob-
ability
The orchestration architecture enables the system to make
sophisticated decisions about what information to retriev e and
how to process it, signiﬁcantly outperforming simple RAG
approaches used by competing systems.
C. CRM and Communication Platform Integration
SalesRLAgent was designed to integrate with existing sales
tooling rather than requiring wholesale replacement of inf ras-
tructure. We developed connectors for:
• Popular CRM platforms (Salesforce, HubSpot, etc.)
• Communication tools (Zoom, Teams, Google Meet)
• Email platforms (Outlook, Gmail)
• Chat systems (Slack, Intercom, Drift)
Integration options include:
• Real-time overlay for sales representatives
• Post-call summary and analytics
• Manager dashboards for team performance
• API access for custom integrations
VI. R ESULTS AND EVALUATION
A. Conversion Prediction Accuracy
We evaluated SalesRLAgent against several baseline ap-
proaches:
• Traditional ML classiﬁers (Random Forest, XGBoost)
• LLM-based prediction (GPT-4 with specialized prompt-
ing)
• Commercial systems (anonymized due to licensing re-
strictions)
• Hybrid approaches combining LLMs with traditional ML
Table I shows the prediction accuracy across these ap-
proaches:
SalesRLAgent achieved 96.7% accuracy, outperforming the
best commercial alternative by 23.7 percentage points and t he
best LLM approach by 34.7 percentage points.
TABLE I
CONVERSION PREDICTION ACCURACY
Approach Accuracy AUC-ROC
Random Forest 0.67 0.71
XGBoost 0.69 0.74
GPT-4 (zero-shot) 0.59 0.63
GPT-4 (few-shot) 0.62 0.68
Commercial System A 0.71 0.76
Commercial System B 0.73 0.78
Hybrid LLM+ML 0.75 0.81
SalesRLAgent (base) 0.92 0.94
SalesRLAgent (full) 0.967 0.98
TABLE II
INFERENCE PERFORMANCE COMPARISON
Approach Latency (ms) Throughput (req/s)
GPT-4 (API) 3450 0.3
GPT-3.5 (API) 980 1.0
Claude (API) 2750 0.4
Local LLM 1650 0.6
SalesRLAgent (CPU) 85 12
More importantly, SalesRLAgent demonstrated superior
performance in tracking conversion probability throughou t
conversations, not just predicting ﬁnal outcomes.
B. Real-W orld Impact on Sales Performance
Beyond technical metrics, we evaluated SalesRLAgent in
real-world sales environments through A/B testing. Sales r ep-
resentatives were randomly assigned to use either:
• Traditional sales tools only (control group)
• Traditional tools + SalesRLAgent guidance (test group)
After 90 days across 217 representatives and 12,433 con-
versations, we observed:
• 43.2% increase in conversion rate for the test group
• 22% reduction in sales cycle length
• 14% improvement in average deal size
• 9% increase in customer satisfaction scores
Qualitative feedback from sales representatives highligh ted
several key beneﬁts:
1) Early identiﬁcation of promising leads, allowing better
time allocation
2) Real-time awareness of conversation turning points
3) Speciﬁc guidance on addressing objections
4) Increased conﬁdence in forecasting
5) Better alignment between perception and reality of con-
versation quality
C. Inference Performance
For practical sales tools, inference speed is critical. We
benchmarked SalesRLAgent against LLM-based approaches:
SalesRLAgent achieved dramatically faster inference
times—85ms compared to seconds for LLM
approaches—making it suitable for real-time guidance
without disrupting conversation ﬂow. We currently only

TABLE III
ABLATION STUDY RESULTS (A CCURACY )
Conﬁguration Accuracy
Full SalesRLAgent 0.967
- Azure OpenAI embeddings 0.89 (-0.077)
- Sequential modeling 0.86 (-0.107)
- Meta-learning 0.94 (-0.027)
- Advanced orchestration 0.92 (-0.047)
- Caching optimization 0.95 (-0.017)
- All specializations (basic ML) 0.68 (-0.287)
offer CPU deployment options, which has proven more than
sufﬁcient for our throughput needs.
D. Ablation Studies
To understand the contribution of each component, we
conducted ablation studies removing key elements of SalesR -
LAgent:
These results highlight the signiﬁcant contribution of se-
quential modeling and Azure OpenAI embeddings, which
together account for the majority of SalesRLAgent’s perfor -
mance advantage over traditional approaches. The advanced
orchestration and caching optimization also contribute su bstan-
tially to overall system performance.
VII. D ISCUSSION AND INSIGHTS
A. Comparative Analysis with Existing Solutions
Through extensive testing, I’ve identiﬁed several key ad-
vantages of our reinforcement learning approach compared t o
LLM-based systems like those from Kapa.ai, Mendable, and
Inkeep:
1) Specialized vs. Generic : While LLMs excel at general
text generation, they lack the specialized training on
sales dynamics that our RL approach provides. This
specialization results in signiﬁcantly higher prediction
accuracy and more relevant guidance.
2) Sequential vs. Static : LLM-based systems typically treat
each interaction independently, missing the crucial se-
quential dynamics of sales conversations. Our RL frame-
work explicitly models how conversations evolve over
time.
3) Computationally Efﬁcient vs. Resource-Intensive :
LLM inference requires signiﬁcant computational re-
sources and incurs high latency. SalesRLAgent delivers
predictions in milliseconds rather than seconds, enabling
truly real-time guidance.
4) Quantitative vs. Qualitative : LLM systems typically
provide qualitative guidance without concrete probabilit y
estimates. SalesRLAgent offers precise conversion prob-
abilities with conﬁdence intervals, enabling more data-
driven sales strategies.
5) Meta-Learning vs. Black Box : Our system’s meta-
learning capability allows it to express uncertainty when
appropriate, unlike LLM systems that often present spec-
ulation as fact.
These differences reﬂect fundamentally different approac hes
to sales AI. While LLM-based systems function primarily
as information retrieval and text generation tools, SalesR LA-
gent operates more like a chess engine for sales—analyzing
conversation position, evaluating conversion probabilit y, and
recommending optimal moves.
B. Limitations and Future W ork
Despite its strong performance, SalesRLAgent has several
limitations that represent opportunities for future work:
• Multilingual Support : The current model primarily sup-
ports English, with only limited capabilities in other lan-
guages. Expanding to a truly multilingual model presents
unique challenges in both data generation and modeling.
• Multimodal Analysis : The system currently analyzes
only text, missing important signals from voice tone,
facial expressions, or gestures in video calls. Incorpo-
rating these signals represents a promising direction for
improvement.
• Personalization: While the model adapts to conversation
dynamics, it does not yet personalize to individual sales
representatives’ styles and strengths. Adding this layer o f
personalization could further enhance effectiveness.
• Causality vs. Correlation : The current model identi-
ﬁes correlations between conversation patterns and out-
comes but has limited capability to determine causality.
Strengthening causal reasoning represents an important
frontier.
• Long-term Relationship Modeling : The system cur-
rently focuses on individual conversations rather than
modeling customer relationships over multiple interac-
tions. Extending to relationship-level prediction presen ts
interesting challenges.
I’m particularly excited about the potential for multimoda l
analysis, as my preliminary experiments suggest that incor po-
rating audio features could improve accuracy by an addition al
2-3% beyond our current 96.7% benchmark.
VIII. C ONCLUSION
This paper presented SalesRLAgent, a novel reinforcement
learning approach to sales conversion prediction and optim iza-
tion. Unlike existing LLM-based systems that rely on genera l
text generation capabilities, SalesRLAgent treats sales c on-
versations as sequential decision processes, enabling acc urate
conversion probability tracking and strategic guidance.
The key innovations in our approach include:
• A reinforcement learning framework speciﬁcally de-
signed for sales conversion dynamics
• Synthetic data generation using GPT-4O to create diverse
training scenarios
• Azure OpenAI 3072-dimensional embeddings for conver-
sation representation
• Advanced orchestration for complex conversation ﬂow
management
• Optimized vector similarity search with caching for
millisecond-level retrieval

• Meta-learning capabilities for conﬁdence estimation and
uncertainty quantiﬁcation
• Real-time integration with existing sales tools and plat-
forms
Our evaluation demonstrated that SalesRLAgent achieves
96.7% accuracy in conversion prediction, signiﬁcantly out -
performing both traditional machine learning approaches a nd
LLM-based alternatives. More importantly, when deployed
in real-world sales environments, the system drove a 43.2%
increase in conversion rates and a 22% reduction in sales cyc le
length.
These results suggest that specialized reinforcement lear n-
ing approaches have signiﬁcant advantages over generic LLM
solutions for domain-speciﬁc applications like sales. Whi le
large language models excel at general text generation, the
complex, sequential nature of sales conversations beneﬁts from
the targeted optimization that reinforcement learning pro vides.
Looking ahead, I believe this work opens new possibilities
for AI in sales—moving beyond simple automation and in-
formation retrieval toward strategic partnership that enh ances
human capabilities rather than replacing them. The future o f
sales AI lies not in increasingly large language models, but in
increasingly specialized intelligence that deeply unders tands
the dynamics of effective selling.
ACKNOWLEDGMENT
I would like to express my sincere gratitude to the team
at Deepmost Innovations who endured countless iterations o f
model design and my incessant whiteboard sessions about re-
inforcement learning architecture. Special thanks to the a nony-
mous reviewers whose constructive feedback signiﬁcantly i m-
proved this paper, though any remaining errors or oversight s
are entirely my own. I’d also like to acknowledge OpenAI
for providing the GPT-4O model that made our synthetic
data generation possible, and Microsoft for the Azure OpenA I
embedding model that formed the foundation of our system’s
conversational understanding. Finally, I must acknowledg e the
thousands of cups of coffee that fueled late-night debuggin g
sessions and the patient family members who supported this
work, even when they couldn’t quite understand my excited
ramblings about conversion probability distributions at t he
dinner table.
REFERENCES
[1] L. Gao, X. Ma, J. Lin, and J. Callan, “Precise zero-shot de nse retrieval
without relevance labels,” in Proc. 46th Int. ACM SIGIR Conf. Res.
Develop. Inf. Retr ., 2023, pp. 2196–2206.
[2] Kapa.ai, “Enterprise knowledge assistant platform,” K apa.ai, Tech. Rep.,
2023. [Online]. Available: https://kapa.ai
[3] Mendable, “AI search for technical documentation,” Men dable, Tech.
Rep., 2023. [Online]. Available: https://mendable.ai
[4] Inkeep, “Conversational AI for customer support,” Inke ep, Tech. Rep.,
2023. [Online]. Available: https://inkeep.com
[5] T. Zhang et al., “Benchmarking large language models for news sum-
marization,” arXiv, 2023, arXiv:2301.13848.
[6] Gong, “Revenue intelligence platform methodology,” Go ng.io, Tech.
Rep., 2022. [Online]. Available: https://gong.io
[7] Chorus.ai, “Conversation intelligence for sales teams ,” Chorus.ai, Tech.
Rep., 2021. [Online]. Available: https://chorus.ai
[8] Z. Li, J. Kiseleva, and M. de Rijke, “Guided dialog policy learning:
Reward estimation for multi-domain task-oriented dialog, ” in Proc. 2020
Conf. Empir . Methods Natural Lang. Process. , 2020, pp. 100–120.
[9] N. Asghar et al., “Affective neural response generation ,” in Proc. Eur .
Conf. Inf. Retr ., 2017, pp. 154–166.
[10] R. Takanobu, H. Zhu, and M. Huang, “Guided dialog policy learning:
Reward estimation for multi-domain task-oriented dialog, ” in Proc. 2019
Conf. Empir . Methods Natural Lang. Process. , 2019, pp. 2308–2319.
[11] C. O. Sakar et al., “Real-time prediction of online shop pers’ purchasing
intention using multilayer perceptron and LSTM recurrent n eural net-
works,” Neural Comput. Appl. , vol. 31, no. 10, pp. 6893–6908, 2019.
[12] J. Devlin et al., “BERT: Pre-training of deep bidirecti onal transformers
for language understanding,” in Proc. NAACL-HLT , 2019, pp. 4171–
4186.
[13] N. Reimers and I. Gurevych, “Sentence-BERT: Sentence e mbeddings
using Siamese BERT-networks,” in Proc. 2019 Conf. Empir . Methods
Natural Lang. Process. , 2019, pp. 3980–3990.
[14] Y . Y ang, Y . Li, and H. Wang, “Sequential deep learning fo r online
conversion prediction with user behavior,” Inf. Process. Manage. , vol.
59, no. 1, p. 102751, 2022.
[15] C. Finn, P . Abbeel, and S. Levine, “Model-agnostic meta -learning for
fast adaptation of deep networks,” in Proc. 34th Int. Conf. Mach. Learn. ,
2017, pp. 1126–1135.
[16] P . Henderson et al., “Deep reinforcement learning that matters,” in Proc.
AAAI Conf. Artif. Intell. , vol. 32, no. 1, 2018.
