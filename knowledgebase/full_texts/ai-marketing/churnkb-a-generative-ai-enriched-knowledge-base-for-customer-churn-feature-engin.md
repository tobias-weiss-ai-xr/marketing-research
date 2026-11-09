---
title: 'ChurnKB: A Generative AI-Enriched Knowledge Base for Customer Churn Feature Engineering'
url: https://doi.org/10.3390/a18040238
category: ai-marketing
subcategory: empirical
date: 2025-04
venue: Algorithms
authors:
- Maryam Shahabikargar
- Amin Beheshti
- Wathiq Mansoor
source: openalex-oa
pdf_url: https://www.researchsquare.com/article/rs-3823738/latest.pdf
pages: 28
chars: 125559
fetched_at: '2026-11-08T16:57:48+00:00'
kb_version: 1
---

# ChurnKB: A Generative AI-Enriched Knowledge Base for Customer Churn Feature Engineering

Generative AI-enabled Knowledge Base Fine-tuning:
Enhancing Feature Engineering for Customer Churn
Maryam Shahabikargar 

Macquarie University
Amin Beheshti 
Macquarie University
Wathiq Mansoor 
University of Dubai
Xuyun Zhang 
Macquarie University
Jin Foo 
Prospa Pty. Ltd
Alireza Jolfaei 
Flinders University
Ambreen Hanif 
Macquarie University
Nasrin Shabani 
Macquarie University
Research Article
Keywords: Customer Churn, Textual Data mining, Cognitive and Behavioral Patterns, Feature Engineering,
Knowledge Base, Generative AI
Posted Date: January 4th, 2024
DOI: https://doi.org/10.21203/rs.3.rs-3823738/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.  
Read Full License
Additional Declarations: Competing interest reported. This research article is written as part of the PhD
project of the rst author, Maryam Shahabikargar. Her PhD project is supported and funded by Macquarie
University, Australia as well as the Prospa Pty. Ltd, Australia.

1

Generative AI-enabled Knowledge Base Fine-tuning:
Enhancing Feature Engineering for Customer Churn

Maryam Shahabikargar*,  School of Computing, Macquarie University, Sydney, NSW, Australia; maryam.shahabi-kargar@students.mq.edu.au
Amin Beheshti*, School of Computing, Macquarie University, Sydney, NSW, Australia; amin.beheshti@mq.edu.au
Wathiq Mansoor, College of Engineering and Information Technology, University of Dubai, Dubai, UAE; wmansoor@ud.ac.ae
Xuyun Zhang, School of Computing, Macquarie University, Sydney, NSW, Australia; xuyun.zhang@mq.edu.au
Jin Foo, Prospa Advance Pty Limited, Sydney, NSW, Australia; jin.foo@prospa.com
Alireza Jolfaei, College of Science and Engineering, Flinders University, Adelaide,  SA, Australia; alireza.jolfaei@flinders.edu.au
Ambreen Hanif, School of Computing, Macquarie University, Sydney, NSW, Australia; ambreen.hanif@students.mq.edu.au
Nasrin Shabani, School of Computing, Macquarie University, Sydney, NSW, Australia; nasrin.shabani@students.mq.edu.au

Abstract: Customers are the most critical component in a business’s success regardless of the industry or product. Companies
make significant efforts to acquire and, more importantly, retain their existing cus tomers. Customer churn is a significant
challenge for businesses, leading to financial losses. To address this challenge, understan ding customer’s cognitive status,
behaviors, and early signs of churn is crucial. However, predictive and ML- based analysis, being fed with proper features
that are indicative of a customer’s cognitive status or behavior, is extremely helpful in addressing this challenge. Having
practical ML-based analysis relies on a well-developed feature engineering process. Previous churn analytical studies mainly
applied feature engineering approaches that leveraged demographic, product usag e, and revenue features alone, and there is
a lack of research on leveraging the information-rich content from interactions b etween customers and companies.
Considering the effectiveness of applying domain knowledge and human expertise in feature engineering, and motivated by
our previous work, we propose a Customer Churn-related Knowledge Base (C hurnKB) to enhance the feature engineering
process. In the ChurnKB, we leverage textual data mining techniques for extracting churn-related features from texts created
by customers, e.g., emails or chat logs with company agents, reviews on the company’s website, and feedback on social
media. We use Generative AI (GAI) to enhance and enrich the structure of the Ch urnKB regarding features related to
customer churn-related cognitive status, feelings, and behaviors. We also lever aged feedback loops and crowdsourcing to
enhance and approve the validity of the proposed ChurnKB and apply it to develop a classifier for customer churn problems.

Keywords:
Customer Churn, Textual Data mining, Cognitive and Behavioral Patterns, Feature Engineering, Knowledge Base,
Generative AI

* Corresponding Author

2

1. Introduction
Customer churn is commonly used to describe a customer’s tendency to stop doing business with a company in a given time
or contract [1]. Most businesses can face customer churn. Fueled by a lack of visibility into customer data, companies are facing
customer relationship crises and churn while having trouble predicting when customers would churn [2]. Retained customers generate
larger profit margins than randomly pursuing new clients [3]. Attracting a new customer costs 5–10 times more than keeping an
existing one [4]. For example, based on a previous study, a 5 percent increase in customer retention rate achieved 35 percent and
95 percent increases in the net present value of customers for a software company and an advertising agency, respectively [3]. Also,
based on a recent study, customer churn is costing mid-market companies an average of $5.5 million per year, in Australia [2].
Therefore, it is crucial to prevent customer churn when operating services.   To properly deal with customer churn problems,
businesses need a good view of their customers’ cognitive status and behaviors. Businesses must understand why and when a
customer might stop using their services or switch to a competitor so they can take proactive measures by providing incentives
that could encourage the customer to stay with the business. With that necessity, it would be of great help for businesses to be
equipped with analytical technologies to help them identify the signs of customers’ tendency to churn.
Various studies have been done on customer churn predictions and identification, leveraging different analytical and ML-based
techniques to get insight into customers’ cognitive and behavioral patterns. Almost all of these analytical studies rely on feature
engineering as a main prerequisite of their model training and predictive analysis [3, 5, 6]. However, previous churn-related
analytical studies mainly applied feature engineering approaches that leveraged demographic, product usage, and revenue features
alone. Nonetheless, some limited recent research has used features related to social network analysis into churn models, leading
to satisfactory outcomes [5–7]. Moreover, there is a lack of research on leveraging the information-rich content from interactions
between customers and companies (e.g., email, chat logs). Remarkably, this area remains largely unexplored in literature [8].
On the other hand, leveraging knowledge bases, including the domain knowledge and the experience of experts in the field,
could be an excellent source for effective feature engineering processes [9–12]. Human expertise and intuition play a crucial role
in feature engineering, which is the process of designing and selecting suitable features in machine learning projects. While having
independent features that correlate well with the target class makes learning easier, complex relationships between features and the
classes pose challenges. To deal with this challenge, human intelligence, and domain-specific knowledge is highlighted to have an
indispensable role, as even irrelevant features can be meaningful when combined effectively [13].
In our previous work [14], we studied different psychological as well as cognitive science sources to develop a domain-specific
Knowledge Base associated with mental health disorders, called mental disorder Knowledge B ase (mKB). In that work, we
focused on depression-related concepts, instances, and behavioral patterns. We thoroughly examined different clinical and non-
clinical methods for identifying mental health disorders. We also proposed a weakly supervised learning approach to generate
training data by leveraging our developed domain-specific Knowledge Base (i.e., mKB). Ba sed on that work, depression is
closely associated with negative feelings and emotions such as sadness, anger, disgust, fear, anxiety, etc. Motiva ted by the
promising results of our previous study, and also because negative cognitive status, emotions and feelings such as dissatisfaction
about a product or service increase the likelihood of churn [1], in the present paper we propose developing a Customer Churn-
related Knowledge Base (ChurnKB).
Beyond what was previously considered achievable, businesses now have additional opportunities to use generative AI to add value
to their operations [15]. This can be seen in the way that generative AI is being used to create content, which is transforming fields
like journalism, visual arts, and customer service [16]. As our first contribution to this study, we propose a customer churn-related
knowledge base and leverage GAI to enhance its structure. Also, we leverage a feedback loop and crowdsourcing approach to
validate the structure of the developed ChurnKB as well as the capability of the GAI to improve its structure. Finally, as our
second contribution and in line with our previous work [ 14], we discuss injecting the ChurnKB into a learning model to
facilitate finding the feelings, cognitive status and behavioral patterns of customers who may tend to leave a company.
The remainder of this paper is organized as follows: In Section 02, the background studies on customer churn, feature
engineering and GAI are described. Then, the structure of the ChurnKB, as well as the way it is injected into the customer
churn classifier pipeline, is explained in Section 03. In Section 04 and Section 05, respectively, a motivating scenario and the
evaluation results are presented to help readers understand our approach before having some discussion around the results in
Section06. Finally, we conclude the paper with remarks for future directions in Section 07.

2. Background
Customer Journey, Cognitive Status and Behaviors
Customer Experience is a multidimensional construct focusing on a customer’s cognitive, emotional, behavioral, sensorial, and
social responses to a firm’s offerings during the customer’s entire purchase journey. Firm offerings are Any products or services
designed, developed, offered, provided, licensed, or otherwise distributed by or for the Company [ 17]. Customer experience
consists of individual contacts between the firm and the customer at distinct points in the experience, called touchpoints.
Customer experience is also built up through collecting these touchpoints in multiple phases of the customer’s decision process
or purchase journey. Customer experience, being a dynamic process, is conceptualized as a customer’s journey with a firm over
time during the purchase cycle across multiple touchpoints [18].
Customer Journey commonly refers to a process or sequence that a customer goes through to access or use an offering of a company.
It covers the entirety of a customer’s experience with a brand. Touchpoints are involved in all elements of the customer journey

3

and include interactions during marketing efforts, the purchasing process, and the post-purchase service. A bus iness needs to
identify all its touchpoints and optimize them to deliver a positive customer experience. On the other hand, channels are those
media through which those interactions occur. For example, advertising is a  touchpoint, while radio (if that is the medium
through which advertising is done) is a channel. While a brand may control most touchpoints, some of them are seen as being
uncontrollable. Advertisement, product attributes, sa les channels, store design, and customer services are some of those
controllable touchpoints [1].
Customer services are mainly about communication with customers and follow-up after sales. It refers to when customers interact
with customer service representatives. It offers valuable information about their thoughts and feelings toward a business and its
services. This qualitative data can be analyzed alongside quantitative factors to gain  insights into customer sentiment and
trends and to pinpoint important feedback on the company and its products [1]. Consequently, the customer journey, defined as
the entirety of a customer’s interactions with a company, plays a vital role in determining customer cognitive status, and
satisfaction with the product or service and could ultimately impact customer success and churn. A successful customer
journey can be achieved by implementing effective strategies that provide customers with the necessary support and guidance to
achieve their desired outcomes. Conversely, unsuccessful strategies can lead to negative outcomes and ultimately result in customer
churn [1, 19].
Customer (i.e., consumer) behavior refers to the activities, processes, and decisions individuals or companies make as they purchase,
consume, and discard goods and services to satisfy their needs and goals. It is a study of customer decision-making along the entire
process of purchasing and consumption  [20–22]. Understanding  this behavior is complex, as various factors can influence customers’
choices. These factors include personal and demographic attributes like gender [23], age, education, occupation, and income, as
well as psychological aspects like motivation, perception, beliefs, and attitudes. Additionally, social factors such as reference
groups, family, and social roles, along with cultural elements like culture and social class, also play a significant role in shaping
customer cognitive status and behavior [24]. A customer’s cognitive states as well as feelings are a major factor in defining the way
a customer behaves, i.e., whether they choose to leave or decide to continue with a brand/business. Feelings such as pleasure, joy,
fear, anger, sadness, and disgust form different customer experiences associated with purchasing behaviors [25].

Customer Churn from Business Perspective
Customer churn is commonly used to describe a customer’s tendency to stop  doing business with a company in a given time
or contract [1]. Most businesses can face customer churn. Many businesses lack the necessary tools to provide the kind of customer
experience that will keep them competitive. They are struggling to get a clear picture of their customers, leading to a loss of
revenue. Fueled by a lack of visibility into customer data, companies are facing customer relationship crises and churn while
having trouble predicting when customers would churn [2]. Due to its importance, customer churn research has been promoted in
various service businesses. Different businesses have their nature and characteristics. Because of that, the churn problem has
been studied separately in each of them, based on different churn measurement criteria.
Customer churn studies are done in industries such as telecommunication (e.g., mobile services), internet services, finance,
etc. [3]. Some studies have taken a psychological approach to customer churn. Based on a study by Bostan et al. and their
analysis in combination with motivation theory [26], customers who are using Massively Multiplayer Online Role-Playing Games
(MMO RPG), churned when their motivation to use games chan ged [ 27]. Additionally, according to another study that
surveyed about 250,000 gamers, customer views towards games were clustered by nation, race, and age [28].
The earliest research on churn was done from a management standpoint. Especially Customer Relationship Management (CRM)
has historically been the starting point for studies on customer attrition [ 29, 30]. CRM is a managerial method aiming at
increasing the efficiency of businesses [31]. CRM is a two-part system that includes both operational and analytical CRM.
Analytical CRM specifically concentrates on customers’ cognitive status and behavior, personal traits, and attitudes to generate
tailored marketing strategies and meet the needs of individual customers [ 29]. With churn analysis emerging as a vital,
personalized customer management method, IT-related technologies are used in analytical CRM, and businesses are
implementing those technology-derived solutions for customer selection, acquisition, and retention [3]. Hence, customer churn
prediction and analysis are vastly used as crucial personalized methods in the customer management field [32]. Also, organizations
are employing IT and knowledge management technologies to deploy a variety of approaches that help in the control of customer
churn and the improvement of client retention [33].

Customer Churn from Analytical Perspective
When compared to the amount of churn, the efficiency of customer acquisition in the past was favorable. Customer acquisition
costs, however, sharply increased when the market became saturated because of the globalization of products and services and
intense competition. Retained customers generate larger profit margins than randomly pursuing new clients [3 ]. Attracting a
new customer costs 5 –10 times more than keeping an existing one [4]. For example, based on a previous study, a 5 percent
increase in customer retention rate achieved 35 percent and 95 percent in creases in the net present value of customers for a
software company and an advertising agency, respectively [3]. Also, based on a recent study, customer churn is costing mid-
market1 companies an average of $5.5 million per year, in Australia [2]. Therefore, it is crucial to prevent customer churn when

1 Companies with revenues between $10 million and $1 billion per year.

4

operating services.
Due to the issue’s importance, studies on customer churn have been proposed in various service fields. In today’s data-driven
world, understanding, identifying, and predicting customer churn has become crucial. Analytical studies focused on churn,
which aims at finding patterns and reasons why customers stop using a product or service. By collecting and analyzing
customer data from different sources, businesses can get valuable insights into what makes customers leave. These studies
often use Machine Learning (ML) algorithms to create predictive models that can tell when a customer might leave, allowing
companies to act and keep their important customers happy and loyal [34].

Feature Engineering
Many applications, including data analysis, intelligent systems, and large-scale computation, depend on machine learning. To be
effective, ML workflows must have a good combination of data, features, and models [35]. Features and models lay between the
raw data and the desired insights in the machine learning workflow. In that workflow, we choose the features in addition to the
model. This approach has two joints, and selecting one affects the other. Appropriate features simplify the next modelling phase
and increase the effectiveness of the resultant model in achieving the intended outcome. To obtain the same level of performance
with bad features, a model may need to be considerably more complex [36].
A feature is a metric that expresses raw data. They are individual measurable proper ties or variables of a data set used in
machine learning. Naturally, the type of data that is provided would impact the features. They can take on a variety of forms
such as ‘numerical features’ (e.g., age, income, or temperature), ‘categorical features’ (e.g., gender, country, and occupation),
‘textual features’ (e.g., Bag-of-Words, TF-IDF, Word Embeddings, and text length or word count), ‘temporal features’ (e.g., date
and time), ‘geospatial features’ (e.g., Latitude and longitude, and distance or proximity), and ‘transactional features’ (e.g.,
products prices). Features are also influenced by the model, with certain models better suited to feature types than others. The
ideal features should be simple for the model to process and pertinent to the task. The number of features is also crucial. The
model would not be able to complete the task at hand if there are insufficient informative features. The model will cost more and
be more challenging to train if there are too many features or if the majority are useless [36].
The process of creating the most suitable features for the task, the model, and the data is known as feature engineering. Feature
engineering has emerged as a crucial technique in machine learning due to the challenges associated with raw data and the need
to extract meaningful information for effective model training and prediction. It refers to the process of transforming raw data into
a format that is suitable for machine learning algorithms to effectively learn patterns and make accurate predictions [36– 38]. It
involves creating new features, modifying, or transforming existing on es to enhance the predictive power of machine learning
models by providing them with more informative and representative features [39].

Various Feature Engineering Techniques
Feature engineering could be considered as a generic term for any tasks used between gathering raw data and starting model
training, and the selection of the appropriate approach is dependent on the ML model [ 34, 37, 40]. Feature engineering
encompasses the entire process of preparing and enhancing the features for machine learning. Different techniques of feature
engineering worth considering are data preprocessing, generating new features, extracting important information, transforming the
features, and selecting the most relevant ones. Each of these techniques could play a vital role in improving the quality and
effectiveness of the features, ultimately leading to better machine learning model performance.
 Feature Generation: Generating features that offer useful insights into multiple aspects of the data while taking the
unique characteristics and limits of the algorithms into consideration is necessary for the success of learning algorithms.
Feature generation involves generating new features from existing ones, either singly or in combination, to utilize them in machine
learning or statistical analysis [41]. This procedure enhances the available information to be leveraged during model development,
thereby aiming to yield a more precise model [42].
 Data Preprocessing and Feature Transformation: One of the techniques of feature engineering is data preprocessing
[36]. Data preprocessing is vital in every data science project, serving as a critical step in the workflow. Given the inherent
disorder and complexity of real-life data, data preprocessing becomes essential to ensure ef fective analysis [ 43]. Data
preprocessing involves cleansing and transforming raw data to facilitate feature engineering. Once a substantial amount of data
is obtained from various sources like databases, object stores, or data lakes, engineers need to preprocess it to enable data
scientists to extract meaningful features. This includes fundamental data cleaning operations, as well as aggregating and combining
different sets of raw data. In operational settings, data preprocessing can be executed as an ETL (Extract, Transform, Load) job
for batch processing, where data is processed in chunks, or as part of a streaming processing pipeline for real-time data, enabling
immediate analysis and feature extraction [44].
 Feature Extraction: The feature extraction task involves identifying a concise and meaningful collection of features,
enhancing data efficiency, and facilitating storage and processing [45]. Different feature extraction methods are used for image,
video, or textual data analysis. For example, Histogram of Oriented Gradients (HOG) and Speeded-Up Robust Features (SURF)
are powerful feature extraction techniques that capture distinctive information from images. Also, in text analysis, some of the
feature extraction techniques include Bag-of-Words [46], N-grams [47], word embeddings [48], Part of Speech (POS) tagging, and

5

named entity recognition [9].
 Feature Selection: A critical component of feature engineering is feature selection. It seeks to choose an appropriate subset
of features for the ML model from the available input. Reduced noise, storage needs, and tr aining time enhanced data
visualization and comprehension, and enhanced prediction performance are some of the possible advantages of feature selection
[34, 37]. A feature set is defined as A = { x1, x2, x3, ... xn}, where xi represents the i-th feature in the initial feature space
Rn. Due to the enormous number of hypotheses that must be considered, building an ideal ML model is theoretically challenging
when the dimensionality of a feature collection is high [ 49]. The feature selection method was first presented by practitioners
in the early days of machine learning to select a subset S from the initial feature set A. The objective was to compress the feature
space’s dimensionality to Rs, where Rs is a new, condensed dimension relative to n, the original dimension. Usually, a subset
of the features is selected as the new feature set after a certain technique is used to rank the features initially [50].
 Domain Knowledge-enabled Feature Engineering: To fully utilize the capabilities of machine learning, feature
engineering assists to leverage human creativity, experience, and knowledge [38]. Learning from experience is a key component
of intelligence. Knowledge professionals involved in knowledge-intensive operations gradually gather priceless domain-specific
experience and knowledge. Organizations must capture this knowledge to enable various applications. Examples of such applications
could be developing organizational knowledge bases and injecting them into the feature engineering processes, leading to the
development of more powerful machine learning algorithms. They could also help beginner or inexperienced knowledge workers
to proceed in a productive way [12].
To improve the feature engineering process, several studies have been conducted that focused on innovative approaches in this
regard. For instance, Beheshti et al. suggested a data curation foundry [9], Shahabikargar et al. proposed a weakly supervised
approach [14], and Brooks et al. developed FeatureInsight, a visual tool to support feature ideation process. They conducted
an exploratory study comparing human-generated features to features selected via two widely used baseline measures,
Information Gain and Chi-Squared [35].
Human expertise and intuition play a crucial role in feature engineering, which is designing and selecting suitable features in
machine learning projects. While having independent features tha t correlate well with the target class makes learning easier,
complex relationships between features and the clas s pose challenges. Despite attempts to automate feature engineering, a
significant amount of time is spent on tasks like data gathering, integration, cleaning, preprocessing, and iterative feature design.
This highlights the indispensable role of human intelligence and domain-specific knowledge in the process, as even seemingly
irrelevant features can be meaningful when combined effectively [13].
Several previous studies leveraged knowledge-based techniques, i.e., domain knowl edge or specialized expertise, into their feature
engineering process. Knowledge-based feature engineering could be applied through various approaches such as Rule-bas ed
feature engineering [10], expert-driven feature ideation [35], and incorporating external knowledge sources [ 14], etc. These
approaches seek to produce more relevant, understandable, and useful features for machine learning tasks by leveraging domain
knowledge [9–12, 14].

Chai et al., developed a knowledge-based approach for tracking events in social media streams. They used crowdsourcing as a
crucial component in developing a knowledge base and assessing events identified on social media. Additionally, they used the
knowledge base to extract and link entities from posts on social media, such as tweets, and categorize and tag them. The suggested
approach uses distributed processing, various heuristics to find event candidates, and crowdsourcing for event validation and
feature extraction [10].
Beheshti et al. proposed a feature extraction approach called DataSynapse for curating  social data in big data analytics.
DataSynapse utilizes scalable algorithms to transform social items, such as tweets or posts, into curated items with contextualized
knowledge. The approach offers customizable feature extraction from diverse data sources and allows for linking contextualized
information to domain knowledge through cross-document coreference resolution. Using low-level features like named entities,
keywords, synonyms, stem, and part- of-speech, higher-level features can be cascaded and deployed as microservices.
DataSynapse is a foundation for big data analytics and facilitates the exploration and analysis of social data, uncovering hidden
patterns and deriving targeted insights. It improves the quality of extracted knowledge compared to traditional curation pipelines
and provides a valuable tool for enhancing decision-making processes within organizations [9].
Shahabikargar et al. developed a knowledge-based approach for featur e extraction from textual data. They studied various
approaches to identifying mental health disorders, including clinical and non-clinical methods.  They utilized the domain
knowledge as well as the cognitive science expertise that was gained through those stu dies to construct a domain-specific
Knowledge Base for mental health disorders. Through their study, they proposed a knowledge-based textual data mining technique,
primarily focusing on depression, to identify patterns of mental disorders. By developing a mental disorder Knowledge Base
(mKB), they facilitated the process of developing a weakly supervised machine learning algorithm for labelling training data sets,
in a way that those data sets can be utilized in deep learning and analytical approaches to effectively identify mental disorder issues
[14]. In their work, Beheshti et al. also introduced the creation of an intelligent Knowledg e Base (KB), called ‘Knowledge
Base 4.0’, which simulates the knowledge of subject matter experts in knowledge-intensive operations and uses it to speed up
the automatic labelling of data for learning algorithms [12].

6

GAI and Feature Engineering
The capacity to learn knowledge and skills as well as use them is translated to Intelligence. Knowledge, experience, and creativity
are the three main elements that makeup intelligence. On the other hand, Artificial Intelligence (AI) refers to the simulation of
human intelligence processes by computer systems. One of the state-of-the-art AI systems is Generative Artificial Intelligence
(GAI), which explores the neural mechanisms engaged in creative thinking and problem-solving, aiming to improve the acquisition
and application of knowledge and skills [51]. GAI is a subset of AI techniques leveraged to produce content, data, or information
that’s like human creations. These methods employ complex algorithms, often rooted in deep learning structures, to learn and
replicate patterns from existing data. They mostly generate new and diverse outputs across different data analysis domains such as
text, images, and processes [16, 52]. GAI has a remarkable ability to create realistic and innovative outcomes in various fields.
By learning patterns from existing data, GAI excels at creating content that closely resembles human-generated data.
As mentioned before, feature engineering is the process of transforming raw data into features that represent the u nderlying
patterns in the data in a better way, leading to the improved performance of machine learning models. On the other hand,
Generative AI has the potential to change the way we do things. It provides a powerful set of tools, particularly models like
Generative Adversarial Networks (GANs) and Variational Autoencoders (VAEs) for feature engineering, especially in scenarios
involving unstructured data [53, 54] or anomaly detection [52, 55–58] or situations that need for data augmentation [53, 59, 60],
synthetic data generation [59–61], dealing with imbalanced data [62, 63], content generation and data imputation [54, 64], or the
desire for more interpretable and robust features. The capabilities of Generative AI can be combined with traditional feature
engineering techniques to create a comprehensive feature engineering strategy.
A GAN consists of two neural networks, the” generator” and the” discriminator”, which are trained together. The generator
produces fake data that looks like some real data, while the discriminator tries to ide ntify between real and fake data. Over
time, the generator becomes so skilled at creating fake data that the detective cannot tell  real from fake [65]. On the other
hand, a VAE is a probabilistic generative model that encodes input data into a latent space and then decodes it back. The
goal is to learn a compact representation of the data in latent space. Unlike traditional autoencoders, which map inputs to
fixed points in the latent space, VAEs map inputs to distributions (defined by parameters like mean and variance). This
introduces a probabilistic aspect, allowing the model to generate new, similar data by sam pling from the latent space [66].
As GAI continues to evolve, its potential impact on technology and creativity becomes increasingly important. DALL- E,
VALL-E, ProcessGPT, and ChatGPT are some examples of leveraging the power of GAI in different domains [16]. ChatGPT2
is a complex AI language model introduced by OpenAI in 2018. GPT stands for ‘Generative Pre-trained Transformer’, part of
a family of models known as transformers. Transformers are a type of neural network architecture that has revolutionized the
field of natural language processing (NLP). They excel at language translation, text generation, question answering, and more.
ChatGPT is one of the most popular and outstanding demonstrations of the GAI capabilities [54, 67–71, 71–74] in the form of a
conversational AI tool [ 67, 72]. Its primary function is understanding and generating human-like text based  on the input it
receives. Later, it was enhanced with bigger and more intricate versions.
DALL-E3 is a neural network-based image generation model also developed by OpenAI. It is a variation of the GPT
architecture and is designed to generate images from textual descriptions. It can generate creative images based on textual
prompts. VALL-E 4 is a language model for generating speech from text developed by Microsoft. It uses just one speech phrase
from the source language as a stimulus to produce high-quality speech in the destination language. ProcessGPT was introduced in
a recent paper by Beheshti et al., suggesting GPT technology to create innovative process models as necessary. It is a novel
approach to improve decision-making in data-focused and knowledge-intensive processes. Applying ProcessGPT involves training
a generative pre-trained transformer model on extensive business process data, followed by fine-tun ing on specific process
domains. This refined model can then produce process flows and decisions by context and user input, offering potential enhancements
to decision-making in complex processes [16].
Motivated by our previous study [14] as well as the widespread popularity of GAI power in revolutionizing different aspects of
industries (i.e., domain-specific tasks and processes) especially the education sectors [68, 70, 71, 75, 76], we come up with the
idea of leveraging ChatGPT on improving and facilitating feature engineering tas k for customer churn problems. Prompt
Engineering (PE) is one of the main challenges in getting the best results out of leveraging ChatGPT. PE, in the  context of
interacting with ChatGPT, refers to the strategic crafting of input messages or quer ies to elicit desired responses from the
model behind it, taking advantage of its strengths while keeping in mind its limitations. The main goal of PE is to achieve
accurate, relevant, and contextually appropriate answers. With this aim, we first did  a comprehensive literature review of
previous studies on cognitive and behavioral aspects of the customer journeys. Then, based on the acquired knowledge, we created
and used step-by-step prompts and fed into ChatGPT. Since there are some inherent limitations [69, 77] in the ChatGPT, such
as generating wrong information, we leveraged a feedback loop and asked  the experts in the field to confirm the reliability of
the generated content by ChatGPT.

2 https://openai.com/blog/chatgpt
3 https://openai.com/dall-e-2

4 https://www.microsoft.com/en-us/research/project/vall-e-x/

7

Churn-related Feature Engineering
Due to its importance, customer churn research has been promoted in various service businesses. Different businesses have their
nature and characteristics. Because of that, the churn problem has been studied separately in each of them, b ased on different
churn measurement criteria. Previous customer churn works are expanded in industries such as telecommunication (e.g., mobile
services), internet services, games, insurance, finance, management, music streaming, newspapers, and pay TV [3]. In this
section, we review customer churn studies across different domains, focusing on their feature engineering approaches and the
corresponding applied features.
Generally, a dictionary-based definition of churn is inactivity for a long time [78]. However, each business could have its own
definition of ‘long time’ and ‘inactivity’. This variety in definition arises from the intense market competition and non-strict
membership contracts and conditions in recent services offered to the customers. For example, in the industry of Internet services
(i.e., businesses that provide various services and products over the internet such as online Banking and Financial Services,
online Learning and Education, gaming and Online Entertainment), recurrent customer churn is happening because of the reduced
investment expenses for customers [32, 79], and slight switching costs when changing services [30].
Most contemporary churn prediction analyses are done utilizing log data. Log data refers to a record of events, actions, or
transactions within a system, application, or network5. In other words, the trace data left over after using On-line services is known
as a log. As a result, a variety of businesses can employ online services and churn prediction models that were created utilizing
log data [3]. Transaction logs (e.g., purchases, subscription renewals, or cancellations), communication logs (i.e., used to keep
track of email messages, phone calls, and other forms of communication), and login and activity logs (i.e., customer logins and
their subsequent activities) are some instances of log data. Focusing on some of the main industries (i.e., telecommunication, banking,
and insurance) affected by customer churn problem, in the following parts, churn definition in different industries and the way
various features are applied in customer churn analysis are reviewed.

Churn in telecommunication Industry
Most past churn studies have focused on the telecommunications sector (telecom),  being the most impacted by customer
churn6. Churn in telecom services refers to the change of service provider from one to another [3, 80, 81]. There are several
types of telecommunication service categories, such as telephone, mobile, and internet. Among them, mobile services have received
much more attention, and most previous studies have focused on it [82]. The costs of acquiring customers are significant for
these services. Therefore, it would greatly help if customer churn is avoided and proper incentives are offered [3, 80, 83, 84].
In their study, Amiri et al., for the first time, explored churn identification in the microblog (e.g., Twitter) contexts. To them,
identifying such churn-related content will enable companies to provide personalized assistance to those with a tendency to churn
and enable competitors to hunt new customers. The main feature categories used in their analysis ar e ‘Demographic Churn
Indicators’, ‘Content Churn Indicators’, and ‘Context Churn Indicators’. The top three most demographic indicators are in order
of average friend active days about competitors, average friend posts about competitors, and average friend active days about
the brand.
The demographic churn indicators category includes two feature sub-categories, namely activity ratio (e.g., average number
of posts about brand/competitors per day, ratio of active days about brand/competitor, average time gap between posts about
brand/competitor, ratio of URLs in posts about brand/competitor as well as average of friends’ activity ratios), and followers and
friends info (i.e., If user has bio information as well as If  bio contains URL). The content churn indicators i nclude
unigrams/bigrams, neighboring words of brand/competitors names, syntactic and Comparative m arker features, sentiment
features, tense of the tweet, and news indicator features. Finally, the context churn indicator category includes content features
of user/friends/brand/competitors posts in thread (i.e., posts from user/friends/brand/competitors in thread and posts in thread) as
well as reciprocity between user and brand/competitors posts [6].
Through their study, Lalwani et al. provided a comparative study of custo mer churn prediction in the telecommunication
industry with promising results, using famous machine learning techniques. Three main feature categories have been leveraged
in their models, i.e., demographic, product, and service-related features. Followings are every single feature named: customer’s
gender, senior citizen, partner, dependent, tenure, whether the customer has phone service, multiple lines, internet service, online
security, online backup device protection, tech support, streaming TV, streaming movies, contract, activated paperless billing or
not, also what are the payment method, monthly charges, and the amount of total charges[85].
Based on Agrawal et al. study on customer churn in the telecom industry, th ose customers that have long-term contracts or
those associated with the firm for a longer duration are more likely to be retained than those with short-term contracts and small
tenures. They concluded that if the monthly charges are high, the customer will likely be churned away. Demographic Data,
subscription details, user billing profile, and tenure are the four main feature categories in their study. Demographic Data includes
customer gender and whether they have partners and dependents or not. Subscription details refer to whether customers
subscribed for phone, internet security, online back up, multiple lines, device protection, tech support an d streaming TV and
Movies. Also, the user billing profile encompasses payment method, contract, paperless billing, Monthly Charges and Total

5 https://www.sumologic.com/glossary/log-file/
6 https://techsee.me/resources/surveys/state-of-customer-churn-telecom-survey-report/

8

charges, and finally, tenure was also leveraged as one of those feature lists [86].
Today, massive, networked data logs and information flows between interlinked entities are available. These data potentially hide
information highly valuable to companies and organizations and, as such, open new perspectives for innovative busines s
applications. Contributing to customer churn prediction using social network effects can provide valuable insights into customer
cognitive status and behavior and help improve the accuracy of predictive models. In their study, Verbeke et al. focused on
Understanding and leveraging social network effects in churn prediction. They used several feature categories in their analysis,
namely ‘network features’ and ‘local features’. Network features include the number of contacts between a customer and previous
churners and the number of contacts between a customer and customers of competing operators. Also, local variables include
subscription data, e.g., postal address, name [7].
Alboukaey et al. studied customer churn prediction, leveraging various telecom-related features. Those features are ‘Product
Usage Features’, ‘temporal behavioral features such as Key Performance Indicators (KPI) records, i.e., daily aggregated data
that summarizes customer spending on a specific day, including the amounts of money spent on different types of telecom services,
such as voice call, SMS, data)’, ‘detailed usage records’ as well as ‘RFM (i.e., customer interactions in terms of recency, frequency,
and monetary dimensions). In their work, they Proposed daily churn prediction instead of monthly, based on the daily dynamic
behavior of customer instead of their monthly one. The results showed that the daily models signif icantly outperform the
monthly models in predicting churners earlier and more accurately [87].
Based on a recent Systematic Literature Review (SLR) regarding customer churn in the telecommunication industry, age,
gender, satisfaction, switching costs and barriers, and service quality are the key factors influencing a customer’s propensity
to quit a service provider and switch to a competitor. Service quality indirectly impacts customer churn through satisfaction.
Socio-demographic variables like age and gender show mixed impacts on customer’s propensity to churn. Switching costs and
barriers, such as loyalty contracts and complex service plans, play a significant role in reducing customer churn. Customers with
more tenure (the length of time that customers have been using the services of a particular telecommunications company) are less
likely to switch to another service provider. Companies should correctly allocate customers to a tariff (attributes of pricing plans)
that match their consumption profile. Bundled services are effective  in reducing customer churn. Competitive environment,
advertising messages, and promotional campaigns of competitors impact churn and switching intentions [82].

Churn in Financial and Banking services
All industries are affected by the fast growth of service providers, with the banking sector experiencing a particularly large
increase. Customers have a wide range of options when deciding where to put their money in the banking industry. Therefore,
keeping active customer involvement levels and managing customer churn are major concerns for many banks [88]. In banking,
an individual who cancels all his accounts and ceases doing work with the bank is referred to as a churned customer. Customer
churn can have severe effects on the banking business and the loss of funds and revenues. As a result, a key component of customer-
oriented retention, which tries to reduce churn, is the search for and identification of customers who exhibit a high propensity
to quit the bank or forecast customers who would leave the company in the future [89]. Based on a recent study of credit card
services, customers are less likely to churn when they use their credit cards frequ ently. The top three features that have a
substantial impact on the customer churn prediction are total transaction a mount over the past 12 months, overall transaction
frequency over the past 12 months, and overall revolving balance7 [90].
In another study, Lariviere et al. explored customer retention patterns amon g savings and investment (SI) customers in a
Belgian financial services provider. This study focused on the distinct characteristics of SI products. Seven SI categories are
identified based on duration and risk dimensions. The risk dimension was categorized as capital risks (involving invested funds) and
revenue risks (about potential earnings), and the duration dimension looks at how long the SI product lasts. Some products do
not have a predefined time limit, while others end automatically on a specific date. To figure out churn, it is interesting to see if the
products with predefined time limit helps keep customers retained because customers with products that do not have a predefined
time limit are thought to stay customers forever unless they cancel their products themselves. For example, a type of product
could be those with ’fixed term short run’  (duration dimension) and ’some revenue risks plus no capital risks’ (risk dimension)
characteristics. Notably, savings accounts, despite infinite terms, exhibit high ch urn rates. The research underscores the
significance of offering a comprehensive range of financial products to meet diverse customer needs within a single provider. Hazard
and multinomial findings of this study suggest the potential to build relationships through satisfying products, enhancing both
customer satisfaction and the company’s market position [91].
In their study, Mavri et al. considered several factors, namely gender, bank’s credibility, customers’ satisfaction, service quality,
interest rates, and education, as potential determinants of customers’ propensity to leave a bank.  Based on their study, using
survival analysis, the quality of a bank’s products and its reputation are practical factors in stopping bank customers from
switching to another bank. However, things like gender and education do not matter as much. Also, people between 35 and 45
years old are more likely to leave. Based on these findings, they suggested th at banks should plan (i.e., a CRM strategy) to
group customers by their personal traits and special qualities. This can help stop people from leaving. It should also be figured
out which customers are similar and what kind of products and services can help prevent customer churn [92].
In a previous study, Rahman et al. came up with promising results in ter ms of developing machine learning algorithms for
dealing with customer churn problems in banking. They have used several features in their model to help with predicting the

7 The portion of credit card spending that goes unpaid at the end of a billing cycle.

9

intention of customers to churn. Those features are the customer’s credit score, geographical location, gender, and age. They
also considered other useful factors in this regard, such as tenure (number of years for which the customer has been with the
bank), balance, number of products used by the customer (savings account, mobile banking, internet banking, etc.), whether
the customer owns a credit card or not, whether customer is active or not, and estimated salary of the customer in Dollars [88].

Churn in Insurance Industry
When a customer terminates all their policies, whether due to changing insurance companies or no longer requiring insurance
coverage, this is called customer churn. Insurance companies can no longer depend on a consistent customer network due to
accessible insurance provider switching rules. In many countries, insurance regulations allow customers to terminate policies anytime,
not just on the due date. With numerous competitors and more aware customers, retaining customers is crucial. The expense of
acquiring new customers is significantly higher than keeping existing ones, and even a slight rise  in retention rates can
substantially boost premium revenue. Therefore, preventing custom er churn plays a vital role in insurance industries’ success
[93].
Zhang et al. have introduced a dynamic modelling technique to predict the monthly likelihood of individual customers churning in
an insurance company. They incorporated various explanatory featu res, including partner status, gender, customer lifetime
(i.e., years of an ongoing period of the customer-business relationship), age, annual premium, discounts, count of main insurance
types, count of home insurances, and recent changes in car insurance and discounts. The study highlights the significance of whether
a customer possesses a discount and the variations in this variable over time as key indicators. Although not available in their
data, authors suggested that the last price offered by the company before departure and information regarding external factors like
competitor campaigns could also contribute to higher churn rates [93].
Insurers are increasingly turning to personalized and omnichannel experiences, providing customers with a seamless experience
across any channel they use to communicate from in-office visits and phone calls to website visits, applications on mobile
devices and more [ 94]. Based on a recent study following are four main reasons for churn in the insurance industry: Broken
omnichannel flows, Poor Agent Service, Wasting Customer Time, and Ineffective Self-service [95].
To the best of our knowledge, there are limited studies that leveraged generative AI-enabled feature engineering approaches for
customer churn prediction. They mainly used GAN [62, 63] or VAE [59, 60, 96] models in that regard. Customer churn studies
mainly suffer from a lack of data in the target class (i.e., data with a ‘churned’ label), leading to the imbalanced data issue.
Variational Autoencoder could be an effective tool to extract the latent and meaningful features of diverse consumer
purchasing behaviors from purchase histories and then use these features as input var iables in traditional classifiers to predict
churn [ 96]. In their study, Wang et al. compared seven well-established tabular data s ynthesis models, namely SMOTE,
SMOTENC, SMOTE-Tomek, Copula, Synthpop, GAN, and VAE. Among them, the VAE was found to be the most effective,
evaluated by the area under the precision-recall curve (AUCPR).
In another study, Prateek Kate et al. presented a novel architecture of GAN based on chaos, called chaotic GAN. The primary
distinction between traditional GANs and Chaotic GANs is in how noise is generated for the generator. In Chaotic GAN, noise
is produced using chaotic maps, specifically the logistic map. This approach aims to leverage the properties of chaotic
systems to enhance the generation of synthetic data. The proposed ChaoticGAN and its hybrid with OCSVM (i.e., One-Class
Support Vector Machine) exhibited competitive performance in churn prediction and other analytical CRM tasks. They also
examined the combination of CTGAN (i.e., Conditional Tabular Generative Adversarial Network) with OCSVM and LGBM
(i.e., Light Gradient Boosting Machine) achieved an Area Under the Curve (AUC) of 0.878 [62].

3. Method
In this paper, we present a novel knowledge-based approach for enhancing fe ature engineering in customer churn problems.
This approach helps us extract customer churn features (i.e., focusing on feelings, cogn itive status leading to churn-related
behaviors) from textual data (i.e., customer’s chat log). We leverage our understanding  from previous studies and domain
knowledge as reviewed in the previous section, regarding the customer journey and their cognitive status. In the context o f
customer journey and experience, cognitive science helps understand how people perceive, process, and respond to various aspects
of their interactions with products, services, and a business. We also applied GAI to help construct a domain-specific
Knowledge Base (KB) associated with feelings, cognitive status, and behavioral patterns of customers who tend to churn,
called ‘ChurnKB’. Here, the main idea is to get insight into customers’ feelings by analyzing the chat logs or any communication
(i.e., convertible to the text) generated through any interactions between customers and the company (i.e., any touchpoints). In
addition, we develop a Knowledge Base (KB)-enhanced Classifier for Identifying Customer Churn-related Patterns.

Constructing a Domain-Specific Knowledge Base
In this section, we explain our proposed pipeline to leverage previous studies on the customer journey, cognitive science, and
consumer behavior to understand concepts and behavioral patterns associated with customer churn. We also discussed the way
we leveraged the power of Generative AI to help us enrich the structure as well as the content of our proposed ChurnKB, its
concepts, instances, and associated relationships.
As illustrated in Figure 1 (A), the process of constructing the proposed ChurnKB consists of six steps: Comprehensive

10

Literature Review, Feature Identification, Tax onomy Development, Taxonomy Validation/Modification, Dev eloping
instance2lexicon connector API, and Developing instance score calculator API. Each of those steps is explained as follows:

Step1) Comprehensive Literature Review:
Initially, a collection of previous studies in the fields of customer experience, customer journey, and customer churn are explored.
Reviewing customer journey studies helped us understand the emotional and behavioral aspects of customer churn. It provided a
holistic view of the customer’s experience, allowing us to identify the customer’s probable source of dissatisfaction, pain points,
emotions, and behaviors. Those studies are valuable sources of knowledge to realize the key feelings, behaviors, emotional
status, and key satisfaction points, affecting the customer’s decision to churn or not [1, 18, 97, 98].

Step2) Feature Identification:
The previous step, i.e., Comprehensive Literature Review, provides us with a set of customer churn-related features. Various
concepts and sub-concepts (e.g., customer feeling and dissatisfaction), instances and sub-instances (e.g., poor customer service,
anger), and various relationships that could indicate a customer’s tendency to churn are identified.

Figure 1: A) The proposed process of constructing a Customer Churn-related Knowledge Base (ChurnKB). B) illustrates a snapshot of the Customer churn
Knowledge base, indicative of inter-connected feelings and behaviors of customers at risk of churn. It contains different concepts and sub-concepts related to
customer churn-related instances and sub-instances, and the relationships among them.

11

Step3) Taxonomy Development:
In the third step, we leveraged our understanding of past studies on customer journey and consumer churn as well as GAI-enabled
conversations to create a taxonomy (i.e., A set of concepts, instances for each concept, and relationships among them, organized
into a hierarchical structure) [9, 10]. The taxonomy encompasses four levels, each of which corresponds to whether customer
churn-related concepts (level-1), sub-concepts (level-2), insta nces (level-3) or sub-instances (level-4). Level-1 includes two
main concepts, i.e., ‘customer feelings’ and ‘customer behavior’.  To progress in creating the taxonomy, we continue with
the process of question and answer with the GAI. Prompts8 are fed into the GAI were organized based on the previous studies
and our understanding of them. As a result, in this step, we came up with sever al new meaningful sub-concepts (e.g.,
‘dissatisfaction’ and ‘reduced usage’), instances (e.g., ‘poor customer service’ and ‘decreased frequency of use’), and sub-
instances (e.g., ‘anger’, and ‘disgust’) associated with feelings and behavior of customers with a propensity to leave a business.

Step4) Taxonomy Validation/Modification:
After creating the churn taxonomy with various concepts, instances, and corresponding relationships, we validated the structure of the
ChurnKB by using a crowdsourcing and feedback loop approach. For this aim, a questionnaire was designed to be filled out with
experts in the domain (i.e., sales experts). In the questionnaire, the respondents were asked to give us their feedback and
suggestions regarding the position and existence of each element in each level of the taxonomy. They were asked how relevant
they see each element of the taxonomy (i.e., concepts, sub-concepts, etc.) to the customer churn. We also asked them whether
any specific parts should be removed due to irrelevancy to customer churn or having their position changed. After receiving their
feedback on the design and structure of the ChurnKB, the taxonomy was modified by removing or replacing some of the
concepts or instances.

Step5) Developing instance2lexicon connector API:
There is a clear link between a set of words and the presence of distinctive content (e.g., profane [99], self-criticism [100],
negative emotion [101], and suicidal attempt/ideation [102]) in textual documents. As a result, at this step, we proposed to
use lexical resources for identifying customers with feelings such as dissatisfaction or frustration through analyzing text related
to any kind of communication between customers and a business. For instance, a voice call transcript, the content of an email or
feedback, a post in a specific business online platform, etc. Hence, to continue with the fifth step, various lexical resources (e.g.,
LIWC9, and ANEW (Affective Norms for English Words) [103], NRC [ 107] ) are fed into the ChurnKB taxonomy, aiming
at turning that taxonomy into a lexical-driven knowledge base, which facilitates tex tual data analysis. We also leverage the
GAI to come up with various words and phrases (each related to a specific sub-instance) that could probably be indicative of
the customer’s propensity to churn (e.g., ‘I’m leaving’, ‘discontinue’, and ‘This is  unacceptable’). Then, a unique API is
developed for each sub-instance and embedded into the ChurnKB. Each APIs is a Machine Lea rning (ML) algorithm that
links the corresponding sub-instance (i.e., included in the ChurnKB taxonomy) to one of the proper input lexicons, considered as
the source documents for further analysis in the next steps.

Step6) Developing instance score calculator API:
In the sixth step, several APIs have been developed, each associated with one of t he sub-instances in the customer churn
taxonomy. APIs are ML algorithms that calculate the sub-instance scores (e.g., anger score) , corresponding to each customer
churn-related feature  (e.g., feeling angry) via analy zing input textual data, considered as customer-related documents .
Calculated instance scores, that are in the form of cosine similarity scores, act as fundamental parts of our proposed ChurnKB,
which enables automated knowledge-based analysis. Algorithm 1 demonstrates the process of sub-instance score calculation
for those APIs that apply textual data mining techniques for this aim. In this step, the input for the score calculation process is
the curated textual data. The curation process is described in more detail in the next Section.

Algorithm 1 The process of sub-instance score calculation in API’s that work based on textual data mining techniques.

Data: Curated Input Textual Data
Result: Calculated Sub-instance Score
The ChurnKB Sub-instances;
Linked lexicons;
  for Each Sub-instance in the ChurnKB do
     Reading the Curated Input Textual Data;
     Reading the linked lexicon();
     Applying proper text mining techniques (e.g., TF-IDF and Cosine Similarity Calculation);
end

8 Inputs or questions provided by a user or a program to GAI.
9 http://www.liwc.net/

12

To calculate the cosine similarity scores, we leverage Term Frequency Inverse Document Frequency (TFIDF) technique, being a
textual data vectorizing method. It is used for extracting keyword information from the text as its feature. TFIDF is a popular statistical
technique in natural language processing, assessing the significance of a word in a given document or text relative to a broader corpus.
The significance of a word rises with its frequency in the document, while at the same time decreasing in inverse proportion to its
occurrence across the corpus. TFIDF effectively identifies distinctive words that occur frequently in a specific document but have lower
frequencies in other documents. 𝑇𝐹𝐼𝐷𝐹 of each word (i.e., word i in document k) is calculated as follows:

𝑇𝐹𝐼𝐷𝐹𝑘,𝑖 = 𝑇𝐹(𝑘, 𝑖)  ∗ 𝐼𝐷𝐹(𝑤𝑘,𝑖)
Where:
𝑇𝐹(𝑘, 𝑖) =  𝑐𝑜𝑢𝑛𝑡( 𝑤𝑘,𝑖 ) ∑ 𝑐𝑜𝑢𝑛𝑡( 𝑤𝑘,𝑖 )

In which, 𝑐𝑜𝑢𝑛𝑡( 𝑤𝑘,𝑖 ) means the number of times that i-th word appears in the k-th document, and ∑ 𝑐𝑜𝑢𝑛𝑡( 𝑤𝑘,𝑖 ) means the total
number of words in the k-th document.

Also:
𝐼𝐷𝐹(𝑤𝑖) =  𝑙𝑜𝑔
|𝐷|
|{ 𝑗 | 𝑤𝑖  ∈  𝐷𝑗 }|

In which, |𝐷|  represents the number of documents in the corpus, 𝐷𝑗 represents the j-th document in the corpus,  𝑤𝑖 represents the i-th
word in the document, and  { 𝑗 | 𝑤𝑖  ∈  𝐷𝑗 }  represents the number of documents in the corpus that contain the word  𝑤𝑖 [108]. On the
other hand, the cosine similarity is a metric to assess the similarity between documents (i.e., list of words), regardless of their respective
sizes. Cosine similarity, a widely utilized metric within the inner product family [109], gauges the extent of similarity between two
vectors. In the realm of text classification, it serves to quantify the similarity between two documents. The range of values spans from
0 to 1, with 0 denoting no similarity and 1 signifying identical documents. For a pair of documents, such as "doc1" and "doc2," the
similarity is expressed through the following formula:

Cosine Sim(𝑑𝑜𝑐1,  𝑑𝑜𝑐2) =  𝑑𝑜𝑐1.𝑑𝑜𝑐2 ||𝑑𝑜𝑐1|| ||𝑑𝑜𝑐2|| = ∑ 𝐴𝑖𝐵𝑖 𝑛 𝑖=1 √∑ 𝐴𝑖 2𝑛 𝑖=1 √∑ 𝐵𝑖 2𝑛 𝑖=1

Where 𝐴𝑖 and  𝐵𝑖 represent the components of vectors doc1 and doc2, respectively [110]. In this study, doc1 and doc2 correspond to
a customer-related document and a lexical/source document, respectively.

Figure 1 (B) illustrates a snapshot of the customer churn knowledge base, indicative of inter-connected feelings and behaviors of
customers at risk of churn. It contains different concepts and sub-concepts associated with churn-related feelings and behaviors,
instances and sub-instances, and the relationships among them. As shown, experiencing various feelings could end in different
behaviors in a customer. In this figure, solid connections mainly indicate relatio nships between concepts, sub-concepts, and
corresponding instances. For example, poor customer service could cause customers to feel they are unimportant, which in turn would
lead to a lack of interest in the service/product. As a reflection of lack of interest, different changes in customers’ behavior or
consumption patterns would be raised, e.g., decreased frequency of use, decreased duration of use, decreased spend or purchase
frequency. On the other hand, dotted arrows indicate the connection between the instances and the corresponding sub-instances
(i.e., considered to be instances for which scores have been calculated). For example, decreased spending or purchase frequency
could be raised by the sense of being unimportant.

Developing a Knowledge Base (KB)-enhanced Classifier for Identifying
Customer Churn-related Patterns
When it is time to address issues related to individuals (e.g., customers of a company) and their decision-making process, it is of
great importance to gain a correct understanding of their mental and psychological conditions. Those conditions can lead to
specific decisions that directly affect the company’s goals, e.g., when a customer is deciding whether to continue using products
or services of a company anymore or not. Nowadays, losing customers or customer churn problem is one of the main problems
that companies are dealing with. On the other hand, Machine Learning (ML) is becoming more essential to address various
problems in different fields, including data analysis and intelligent systems. Therefore, one of the ways that companies could
get insight into customer behavior and prevent it is by leveraging the power of ML for analyzing various data related to their
customers.
Being provided with appropriate features is one of the key aspects of leveraging an insightful and reliable ML algorithm. Features
must encompass essential aspects of the data to facilitate the machine in comprehending the intended concept, like the complex
customer behaviors that are indicative of a customer’s propensity to churn. However, features can hinder performance if they

13

inadequately depict the concept, focus on irrelevant data aspects, or overlap with one another. Although there are many elements
affecting the performance of an ML algorithm, such as suitable model selection and parameter adjustments, both researchers
and industry professionals acknowledge the pivotal role of feature engineering in the machine learning procedure. Industry
professionals typically start addressing the problems by exploring existing features from similar previous problems, using their
expertise and domain knowledge to develop appropriate features, or attempting to generate features for the provided dataset through
algorithms. While many tools exist for working with machine learning data and algorithms, support for cognitive and behavioral
features remains insufficient [35].
In this work, we leverage the Customer Churn-related Knowledge Base (ChurnKB), discussed in the previous section, to enhance
the functionality of an ML algorithm, i.e., XGBoost classifier. We link cognitive science and data science to discover essential
features that facilitate learning complex customer behavior. Using the cognitive and psychological knowledge behind customers’
feelings and behaviors that are embedded in the ChurnKB acts as a catalyst as well as a kind of domain expert knowledge to be used
as a feature extraction asset in classification tasks. The ChurnKB is empowered with several APIs, which are calculating churn-
related sub-instance scores. These scores are valuable features associated with specific cognitive, emotional, and behavioral signs
in customers, which enable the process of effectively classifying whether customers to be leaving a company or not.

Figure 2 illustrates the proposed pipeline for devel oping a KB-enhanced Classifier for Identifying Customer Churn-related
Patterns. There are several stages included in developing the proposed pip eline, as follows: (i) ‘Data curation’; (ii) Linking
extracted features to churn- related instances in ChurnKB’; (iii) Calculating scores for churn-related instances leveraging
ChurnKB APIs’; and (iv) Developing a KB-enhanced Classifier’.
Our proposed method presents a scalable framework by adopting a service-oriented architecture [104 ], facilitating the easy
integration of new analytical features into the system. In the initial phase, data curation is defined as a process that transforms
raw data into contextualized data and knowledge [9 ]. This process enhances the efficiency of machine le arning algorithms.
Inspired by two recent studies [9, 105], it is essential to prepare and curate the raw textual data before any further analysis. The
curation process comprises three stages: ’Data Cleaning’ (such as removing punctuation and stop-words, etc.), ’Feature
Extraction’ (including Part-of-Speech and Keywords), and ’Feature Enrichment’ (such as incorporating Synonyms and stemming).

Figure 2: The proposed pipeline for developing a Kn owledge Base (KB)-enhanced Classifier for identifying  customer churn-related patterns, leveraging
calculated scores for instances related to a customer’s propensity to churn from a company, generated by ChurnKB.

Each customer’s feeling and behavior included in the ChurnKB (e.g., dissatisfaction) could be caused by several reasons (e.g.,
‘poor customer service’ and ‘Ineffective communication’). Subsequently, each of those reasons could result in several feelings or
behaviors (e.g., ’anger’, ’blame’, and ’negative feedback’), considered as sub-instances in the ChurnKB. In the next stage, as
shown in Algorithm 2, to link these sub-instances to the curated data and extracted features, each instance is provided with an
empty list. Then, extracted features (e.g., stemmed keywords or phrases) are added to the corresponding sub-instance list. The kind
of added features to the list depend on the type of the related instance. In the third stage, the ChurnKB is empowered by several
APIs for calculating the sub-instance scores. Each of those APIs has a separate functionality. Some of them (e.g., the API related
to the ’Inconvenience’ instance) create scores that are indicative of the counted numbers of special phrases (e.g., ’this is a hassle’
and long wait times’).
In contrast, some of the others (e.g., ‘personality Trait’ API) could create a score that is the probability of having a special
personality trait (e.g., neuroticism), etc. The linked extracted features are the input for corresponding sub-instance-related APIs.
This input enables the score calculation processes for each of the churn-related sub-instances. In the fourth stage, the calculated
scores act as input features of the churn classifier. Several ML algorithms such as Random Forest, Logistic Regression, Support
Vector Machines (SVM), and XGBoost could be deployed to develop this classifier. After fe eding related scores, a binary
learning algorithm is developed to classify whether an input text is associated with a customer who has the intention to churn
or not.

14

Algorithm 2 Linking Extracted Features from input textual data to the Sub-instances in the Ch urnKB.

Data: Curated input textual data
Result: List of features that are linked to the Sub-instances of the Churn KB
Extract Features from textual data;
Churn-related sub-instances = Set up and Array for sub-instances in the ChurnKB;
%(e.g., ‘Negative Feeling’, ‘Anger’, ‘Intent to churn’, etc.)
  for Each Chun-related sub-instances do
        Generate an empty list;
           for Each feature in Extracted Feature do
Add the feature to the corresponding Sub-instance list;
               Link Extracted Features to the Sub-instances in ChurnKB;
         end
end

4. Result
To evaluate the proposed pipelines in the previous section, we implemented some experiments on a customer churn problem
in the telecommunication industry (i.e., our motivating scenario). Most past churn studies have focused on the telecommunications
sector. Based on a recent study, telecommunications experience the highest rates of churn am ong other industries. In that
study, close to half (46%) of the respondents reported that they cancelled a phone, internet, TV, or cable contract with a
company due to the quality of customer service they received 10. The costs of acquiring customers are significant for these
services. Therefore, it would greatly help if customer churn is avoided and proper incentives are offered [3, 80, 83, 84].
We will demonstrate how our model can help analysts and Customer Experience (CX) experts to get insight into the behavioral
patterns of those customers who have a propensity to leave a company and churn. First, we explain the process of constructing
the customer ChurnKB, developed through this work. Then, we describe the process of developing a Knowledge Base (KB)-
enhanced Classifier for churn problems, using the results derived from the constructed customer ChurnKB. For this aim, we
use a churn-related data set, including the numerical data (e.g., ‘total length/charge of day/evening/night calls’) and texts regarding
customers communications with agents in a telecom company11.
The dataset contains 21 columns, encompassing various types of features. These features consist of categorical variables such
as ‘state’, ‘international plan’, and ‘voice-mail plan’, as well as numerical variables like ‘account length’ and ‘area code’, among
others. Additionally, the dataset includes a specific column dedicated to text data, which sp ecifically holds the chat logs
between the customer and an agent. Hence, the dataset incorporates a diverse range of columns comprising categorical, numerical,
and textual information, providing a comprehensive data source for analysis.

Constructing a Customer Churn-related Knowledge Base
Leveraging previous studies and Generative AI to Identify the Customer Churn-
related Features.
In this section, we leveraged the GAI-power (i.e., ChatGPT [ 54, 67–71, 71–74], showing the outstanding capabilities as a
conversational AI) to enhance the quality of our study as well as to have more detailed churn-related features included there.
As previous customer journey studies shows [ 18, 97, 98] customers’ interactions and communications with a company to access or use
any of their offerings affect customers’ perceived value and decision-making process. The higher the customer’s perceived value,
the more the probability of feeling better and satisfied and deciding to continue working with that company. Hence, in
constructing the ChurnKB, two main concepts that coul d be indicative of customers’ propensity to leave a company are their
‘feeling’ and their subsequent ‘behavior’. Also, ‘Dissatisfaction’ is one of the most significant feelings that has been emphasized
in past studies. Dissatisfaction is mainly caused by factors like ‘Poor Customer Service’, ‘low Product or service quality’,
‘Ineffective communication’, ‘Lack of value for money’[1].
But, for the sake of our research, we needed detailed and integrated emotional/behavioral instances of each of those factors, which
were not available through previous studies. Hence, we decided to interact with ChatGPT to access more detailed instances to be
applied into our ChurnKB. For example, we asked ChatGPT ‘In addition to dissatisfaction, what are the main feelings that
could lead customers to leave a company or business?’ and part of the answer was ‘1. Frustration: Frustration occurs when
customers face obstacles, delays, or difficulties in their interactions with a company. This feeling can arise from various sources,
such as poor customer service and unresolved issues.... 2. Disconnection: Disconnection happens when customers no longer feel

10 https://techsee.me/resources/surveys/state-of-customer-churn-telecom-survey-report/
11 https://github.com/aws-samples/churn-prediction-with-text-and-interpretability/blob/main/README.md

15

emotionally or personally attached to a brand. This feeling can stem from changes in the company’s values and inconsistent
communication’. As another example, we asked, ‘What are the main probable behaviors of customers with a tendency to churn,
derived from those feelings?’ and part of the answer was ‘1. Reduced Usage: Customers who are dissatisfied, frustrated, or
feel disconnected from a company are likely to reduce their usage of the company’s products or services...  2. Seeking
Alternatives: Dissatisfied, frustrated, and disconnected customers are prone to seek alternatives actively. They might research
and explore other companies or businesses offering similar products or services... 3. Negative Word-of-Mouth: Customers
experiencing dissatisfaction, frustration, or disconnection are more likely to share their negative experiences with others. They may
express....’. We continued the question-answering process with ChatGPT to the point we came up with an organized hierarchical
structure for ChurnKB.
Integrating our understanding from customer journey studies with ChatGPT interactions, we noticed Disconnection could be caused
by ‘No emotional connection’, ‘Lack of interest in product/service’, ‘Concerns not being addressed’, etc. Also, frustration could
happen by ‘Difficulty in using the product/service’, ‘Complicated processes’, ‘Fre quent disruptions or downtime’, etc.
Besides, it is probable that behaviors such as ‘cancelling the subscription’ would be resulted from the ’intention to churn’.
Any of the above-mentioned feelings could be reflected on or predictable b y the content of their interactions and
communications with the company so those communications would be indicative of specific emotions such as ‘anger’, ‘disgust’,
‘sadness’, ‘resentment’, ‘disappointment’, ‘confusion’, etc.  They also could be indicative of ‘intent to churn’, ‘Customer’s
Personality Type’, or include ‘negative feedback’. Consequently, any combination of those feelings and emotions would lead to
‘Decreased frequency and/or duration of product/service usage’, ‘Seeking Alternatives’ or having ‘Negative Word-of-Mouth’,
etc., and finally being churned. On the other hand, other factors coul d add more complexity to customers’ feelings and
behaviors. Among them are social Factors’, ‘Customer Demographics’, and ‘Customer Psychological Factors’ which are
considered in this study.

Constructing the Validated Customer Churn-related Taxonomy and Linking
Lexical Sources
To form the ChurnKB, churn-related features (i.e., concepts, sub-concepts, instances, and sub-instances) are organized into a
hierarchical taxonomy. As we leveraged the GAI to enhance the structure of the developed taxonomy, we decided to validate
it through crowdsourcing and a feedback loop. For that aim, a questio nnaire has been developed to ask for the ideas and
suggestions of experts in the field. After receiving and applying their feedback, the taxonomy structure has been modified to be
used in subsequent steps. In the evaluation section, we explain more about the  process of getting expert feedback.
Then, several lexical sources are linked to it. For this aim, each sub-instance is provided by an ‘Instance to Lexicon Connector
API’, which links the related sub -instance to the proper lexical source. For example, there is a special API that connects the
‘Anger’ sub-instance to the ‘Anger word lexicon’, another API links the ‘intent to churn’ sub-instance to the list of phrases that
are showing the intention to churn, etc. Our final lexical database is in the form of an Excel file. It is constructed by merging
four lexicons, namely LIWC2015 [106] lexicon (i.e., categories related to churn sub-instances such as ‘anger’ and ‘negative
emotion’), NRC emotional lexicon [ 107]. Since some of the churn-related sub-instances such as ‘Ask for Compensation’,
‘Frustration’, ‘Neglect’, and ’intent to churn’ were not included in either LIWC2015 or NRC emotional lexicon, we leveraged the
GAI to help us create those lists and lexical sources. However, in the evaluation part, it would be explained how we validated that
GAI-generated list of phrases.

Developing Instance Score Calculator API
In addition to the Instance to Lexicon Connector API, most of the instances are linked to another API, which provides different
sub-instances with cosine similarity scores. This API, linked to the sub-instance-related lexical source, uses different NLP
techniques (e.g., TFIDF and Cosine Similarity) to calculate those scores.

Developing a Knowledge Base (KB)-enhanced Classifier for Identifying
Customer Churn-related Patterns
After constructing the ChurnKB, those calculated sub-instance scores allow the development of an automated machine learning
algorithm, i.e., customer churn classifier. This algorithm utilizes knowledge from the ChurnKB and can categorize various chat
log texts as either ’churned’ or ’not churned’. For instance, if a text is labelled as ’churned’, the writer was likely dissatisfied
with the services or products, prompting them to consider leaving. This method employs a data analytics tool to assess the
writer’s tendency to churn, as indicated in the chat log. Consequently, this classifier provides valuable insights to businesses,
particularly sales and retention professionals, enabling them to identify customers on the verge of leaving. Armed with this
information, businesses can proactively implement strategies and retention pro cesses to enhance customer satisfaction and
ultimately retain their customers, thereby minimizing actual customer churn.

To achieve this goal, the initial raw input data undergoes preprocessing to transform it into curated data, i.e., extracted features. This
transformation involves employing various NLP techniques and Python packages like ’regular expressions’, ’word tokenization,’
and the ’nltk.stem package’. Once the features are extracted, they are associated and joined with churn-related sub-instances in
the ChurnKB (i.e., the second step). For evaluation purposes, we utilize 31 sub-instances from the ChurnKB, which could be

16

supplied with an appropriate lexical source. These sub-instances are as follows: ‘intent to churn’, ‘ask for compensation’,
‘negative feedback or criticism’, ‘anger’, ‘frustration’, ‘disappointment’, ‘confusion’, ‘deception’, ‘inflexibility’, ‘skepticism’,
‘neglect’, ‘inconsistency’, ‘disgust’, ‘futility’, ‘disrespect’, ‘fear’, ‘blame’, ‘inconvenience’, ‘powerlessness’, ’injustice’ ,
‘unimportance’, ‘incompetence’, ‘abandonment’, ‘resentment’, ‘request’, ‘betrayal’, ‘negative-emotion’, ‘sadness, ‘certainty’,‘
absolute words’, ‘I’.
A list of stemmed words associated with each user is provided as linked data, and the  relevant sub-instance-related API
will use this data to determine a user’s score. In the third stage, several scores for churn sub-instances are generated, primarily
cosine similarity scores. These scores are subsequently entered into the customer churn classifier. We employed various simple
and complicated models to develop an efficient classifier. However, they were not able to man age our unbalanced data. For
instance, models such as KNN (k Nearest Neighbors) and SVM (Support Vector Machines) did not produce satisfactory
results. XGBoost (i.e., an ensemble model), in contrast to previous models, enabled us to give weights to both majority and
minority classes, addressing the problem of unbalanced data. Using ensemble approaches, predictions from various base
models are combined to improve accuracy.
The linked data is a list of stemmed words linked to each user, intended for  use by the corresponding instance-related API in
score calculation. In the third step, various scores for depression-related instances are computed, primarily as cosine similarity scores.
These scores are then input into the customer churn classifier. To create an effective classifier, we experimented with different
simple and complex models. Simple models like KNN and SVM did not yield promising results due to their inability to handle
our imbalanced data. Unlike these models, XGBoost allows us to assign weights to both majority and minority classes, addressing
the issue of imbalanced data. Ensemble techniques involve combining predictions from multiple base models to enhance accuracy.
Recognizing the strengths of ensemble methods, we opted for an XGBoost model as it is more robust than the previous ones.
As mentioned before, our data set for doing the experiments includes both numerical and textual data (i.e., customer’s chat log).
To test how effective is applying the features generated by ChurnKB on the final prediction results of the developed XGBoost
model, we ran the model on three different scenarios. We ran the model first with the data that just includes numerical data
(scenario A). Then we tried the data with just textual data (scenario B), and, finally, with both numerical and textual data
together (scenario C).
Several key evaluation metrics are used to assess the performance of binary classification models, namely Confusion Matrix,
accuracy (ACC), precision ( P), recall ( R), f1-score (F1), Confusion Matrix, and AUC Curve/Score. A ‘confusion matrix’
provides a detailed breakdown of the model’s predictions, showing the counts of true positives, true negatives, false positives,
and false negatives. ‘Accuracy’ is a common metric used to evaluate  the performance of a classification model. It calculates
the ratio of correctly predicted instances (True Positives and True Negatives) to the total numb er of instances. ‘Recall’, also
known as Sensitivity, measures the ability of a model to identify all relevant instances of a specific class correctly. It calculates
the ratio of True Positives to the total actual positives (True Positives + False Negatives). Higher recall in dicates that the
model is better at capturing all positive instances.
‘Precision’, or Positive Predictive Value, evaluates the accuracy of positive predictions made by the model. It calculates the ratio
of True Positives to the total predicted positives (True Positives + False Positives). Precision assesses how confident the model is
when it predicts a positive instance. A higher precision value means the mo del is more accurate when it predicts positive
outcomes. It calculates the ratio of true positive predictions to the total number of instances predicted as positive by the model.
The F1-score is the harmonic mean of Precision and Recall.  It balances Precision and Recall, considering both false
positives and false negatives. The F1 score ranges from 0 to 1, where 1 indicates a perfect balance between Precision and
Recall. It is a useful metric when there is an imbalanced class distribution. The formula to calculate the values  for
Acc, P, R, and F1 are as follows:

1. 𝐴𝐶𝐶 =  (𝑇𝑃 + 𝑇𝑁) (𝑇𝑃 + 𝑇𝑁 + 𝐹𝑃 + 𝐹𝑁)

2. 𝑃 =  𝑇𝑃 (𝑇𝑃 + 𝐹𝑃)

3. 𝑅 =  𝑇𝑃 (𝑇𝑃 + 𝐹𝑁)

4. 𝐹1 =  2 ∗ (𝑃  ∗  𝑅) (𝑃 + 𝑅)

On the other hand, ‘ AUC’ curve is a graphical representation of a model’s performance across various classification thresholds.
It plots the True Positive Rate against the False Positive Rate for different threshold values. AUC quantifies the overall ability of
the model to discriminate between positive and negative classes. A  higher AUC value (closer to 1) indicates a better ability to
distinguish between classes. Figure  3 ( A), (B), and (C) illustrate the experimental results  in a confusion matrix format
corresponding to each scenario. Figure 3 (D) also provides a visual representation of the AUC scores comparison for three scenarios
(i.e., data set with no textual data included, data set with just the textual data, data set with both the numerical and textual data)

17

used in assessing the performance of the model. As shown, when the features related to the textual data that is derived from
ChurnKB are applied along with the numerical data features, the classifier results in an outstanding AUC of %96, which is a
better result compared to using any of the numerical or textual data features separately.

Figure 3: The experiment results for three different  scenarios: A) The confusion matrix showing the resul ts for the churn classification task using the
numerical data. B) The confusion matrix shows the res ults for the churn classification task, using the numerical data.
C)The confusion matrix showing the best results for the  churn classification task, i.e., the model used both the numerical data and scores generated by
developed ChurnKB in this study. D) Comparison of th e AUC scores for three data sets (i.e., data set with n o textual data included data set with just the
textual data, data set with both the numerical and textual data) used in assessing the performance of the model

5.  Evaluation
Our two main contributions through this research are: (1) creating a Customer Churn-related knowledge base (ChurnKB) to be
leveraged in enhancing the feature engineering phase of customer churn analysis and (2) developing a classifier specifically designed
for customer churn-related tasks. Considering probable limitations of ChatGPT [69, 77], and also to assess the effectiveness of our
approach, we carried out a survey and received feedback from experts in the field. We formulated four hypotheses to test and validate
the information in the knowledge base and the proposed method. To accomplish this, we recruited participants who deal with
customers or/and customer experience (CX) matters in a financial institute, i.e. Prospa company’s12 sales experts. The four
hypotheses are outlined below:

H1: The structure of the knowledge base, including concepts and instances, etc., is relevant to the customer churn.
H2: The customer churn-related features (i.e., sub-instances) to be used for  developing the machine learning algorithm are
relevant to identifying customers’ churn-related cognitive and behavioral Patterns.
H3: Using pronounce ’I’, ‘absolute words’, and ‘certainty words’ by customers in their communications or feedback are relevant
to identifying customers’ churn-related cognitive and behavioral Patterns.
H4: The structure of the developed churn classifier leads to reliable results derived  from applying ChurnKB for enhancing
feature engineering phase.

To test the hypotheses, a questionnaire was created and distributed among the participants. The questionnaire consisted of four
sections comprising multiple-choice questions. The participants were instructed to choose one option best aligned with their
assessment. Furthermore, we requested each participant to assess the relevance of the hypotheses using the Likert scale system,
which employs a five-point scale to gather their opinions (5: Strongly relevant, 4: Relevant, 3: Neutral, 2: Weakly relevant, 1:
Irrelevant).
In this study, we aim to use feedback loop and crowdsourcing to validate our approach and the structure of developed ChurnKB.
Therefore, after each question, we asked participants to inform us if they suggested removing or changing the position of any of
the sub-instances in the ChurnKB. Since we are receiving feedback from experts in the field, there are two versions of the ChurnKB,
i.e., initial, and modified versions. The initial version of ChurnKB was developed by leveraging customer journey studies and
GAI capabilities. The modified version of the ChurnKB was created after having the questionnaires filled out by the experts.
The initial section of the questionnaire comprised some explanations about the goal of our research and how the proposed ChurnKB
could help with achieving that goal. We also described how the questionnaire is formalized in that section. The H1, H2, H3,

12 https://www.prospa.com/

18

and H4 hypotheses were put to the test in the subsequent four sections. Multiple questions were asked in the second to fifth
sections to examine H1, H2, H3, and H4 specifically. Questions regarding H1 and H2 aimed to assess the components and
the knowledge contained in the initial version of the developed customer ChurnKB. In section two (i.e., corresponding to
the H1), different parts of the initial version of ChurnKB, including different concepts and sub-conc epts, were illustrated
to the experts. They have been asked for their ideas about the relevancy degree of each element to the customer churn. In section
three (i.e., corresponding to the H2), questions related to the level-4 sub-instances of ChurnKB and their relevancy to customer
churn have been asked. They have been shown some of the example phrases related to each sub-instance.
For example, we asked the following question: “In the ChurnKB, phrases like ’I’m angry’, ’this is outrageous’, and ’I’m fed up’
are indicators of a customer being Angry. How do you find it relevant to identifying churn-related behavioral patterns?”. H3 and
the corresponding questions in the questionnaire (i.e., section four) were formed to validate the assumption derived from our
previous research, helping us to do some effective modifications to the initial version of the ChurnKB. To validate the H3, we
asked knowledge workers (i.e., sales experts) about their idea for adding some sub-instances to the ChurnKB, motivated by parts
of our previous studies [14] about the cognitive factors that could affect the mental status of individuals. Previous studies show that
using pronounce ’I’, ‘Absolute words, and ‘certainty words’ in communications could be indicative of specific psychological
and emotional status.
In this study, we assume that dissatisfied customers would be in such an emotional state that they are sure about their decision
to leave a company. Therefore, those individuals may u se the pronoun ’I’, ‘Absolute words’, and ‘certainty words’ in their
feedback, reviews and/or interactions with a company to emphasize a specific decision of theirs. Hence, we came up with the
idea of adding those three as sub-instances of the ‘Negative Word-of-Mouth’ sub-concept assumed to be probable behavioral
signs (sub-instances) of unhappy customers who wish to ‘Discouraging others from using the product/service’, ‘Posting negative
reviews online’, ‘Warning others about potential issues’, and ‘Sharing negative experiences with others’ (i.e., instances of
‘Negative Word-of-Mouth’ sub-concept in the ChurnKB).
Finally,  H4 helps us to validate the assumption that the developed churn classifier leads to reliable results derived from applying
ChurnKB for enhancing the feature engineering phase. The following is one the example questions used in this section: “We
assumed that it is possible that dissatisfied customers who want to leave a company, emphasis on their decisiveness to churn
by using absolute words. For example, ’This is Absolute chaos’, ’You are the worst company I have ever worked with’, or ’I
would Never Ever suggest you to others’. How do you find using Absolute words relevant to identifying ch urn-related
behavioral patterns?”.
After receiving the feedback, i.e., the sales experts’ answers to the questions regarding the structure o f the initial version of
ChurnKB, the modified version of the ChurnKB was leveraged to run the churn classifier. In section five, to validate the H4
and assess the results of applying the modified ChurnKB-driven features to the classifier. We demonstrated the analytical results
of the classifier to the sales experts. For that aim, we showed sales experts examples of customer chat logs and the churn status
of the corresponding customers. Sales experts were asked about their ideas reg arding the results. An example question is:
‘The prediction result shows the 0.81 probability of churn for this customer. How do you find this result reasonable/reliable?’.
Finally, participants were asked in the concluding section of the questionnaire to offer suggestions for improving the approach and
method. Figure 4 provides a visual representation of the evaluation results about the four hypotheses.

Figure 4: Evaluation of the hypotheses based on data collected during the survey. (A) Evaluation of the initial version of the ChurnKB
structure. (B) Evaluation of sub instances, to be used as features of churn classifier, originated from previous studies as well as GAI. (C) Evaluation of the
idea of adding three more sub instances developed motivated by our previous work. (D) Evaluation of churn classifier outcomes, leveraging the modified
version of the ChurnKB.

6.  Discussion
As Figure 4 demonstrates the responses from participants validate Hypotheses 1, 2, 3, and 4. In Part i), it is evident that all
participants found the components of the developed knowledge base relevant to customer churn. Part (ii) reveals that all the
experts, but one acknowledged the relevance of the sub-instances used for implementing the developed classifier in identifying churn-
related behavioral patterns. There is one expert who believes the sub-instances are weakly relevant. Additionally, Part (iii)
indicates that 10 participants perceived the three sub-instances (i.e., usage of pronounce ’I’, ‘Absolute words’, and ‘certainty words’)
relevant to the customer churn, and three of them saw them as neutral.
In terms of receiving feedback for position change or removal of any sub-instances, two of the participants did not find the sub-

19

concept ‘Alienation’ relevant and suggested removing it from the ChurnKB. In contrast, others found it neutral or weakly relevant.
Hence, we removed it from the first version of the ChurnKB. Regarding H3, which was related to adding new concepts, e.g.,
‘Absolute words’, since most of the participants found them relevant to churn, we decided to add it to the ChurnKB. Those
concepts were associated with the ‘Negative Word-of-Mouth’ sub-concept and corresponding instances. Part (iv), related to
the evaluation of churn classifier outcomes, leveraging the modified version of the ChurnKB, illustrates that except for one of the
participants, all others found the outcomes relevant.
However, it is essential to note that there are some validity concerns which should be considered before drawing conclusive results
from our study. Although the overall survey results support Hypotheses 1, 2, 3, and 4, there is still room for improvement in the
proposed approach. For instance, considering weights for some of the concepts and instances to be indicative of being more effective
on the churn decisions by customers. These matters will be further investigated in our future works.
We also notified that although at the beginning of the questionnaire, it had been cleared that the target knowledge base is
designed to be used as a general tool, not for a specific industry, two of the respondents had suggestions that were not generalized.
Some of those suggestions were as follows. ‘Usual  churn is attributed to saving on interest and fees for early payouts or
insufficient approvals/declines’ and ‘A majority of dissatisfaction that can result in churn stems whether funding amount
insufficient, the interest rate being high for them, or term length too short’. While those suggestions are not applicable to the
ChurnKB, they still could be insightful for decision-makers in the Prospa, i.e. a financial company .

7.  Conclusion
Customer churn refers to the situation where customers stop doing business with a company, either by discontinuing services, canceling
subscriptions, or switching to competitors. Addressing customer churn is very important for businesses as it directly impacts revenue
and profitability. Retaining existing customers is more cost-effective than acquiring new ones since loyal customers not only
provide consistent revenue but also serve as brand supporters. By understanding the reasons b ehind churn and taking proper
actions to retain customers, businesses can enhance customer loyalty, reduce customer acquisition costs, and ultimately improve
their financial performance.
Previous churn-related analytical studies mainly applied feature engineering approaches that leveraged demographic, product
usage, and revenue features alone. Nonetheless, some limited recent research has used features related to social network analysis
into churn models, leading to satisfactory outcomes [5–7]. Moreover, there is a lack of research on leveraging the information-
rich content from interactions between customers and companies (e.g., email, chat logs). Remarkably, this area remains largely
unexplored in literature.
Motivated by our previous work [14], we proposed leveraging a customer churn-related knowledge base (ChurnKB) to consider
the communications between customers and companies in the feature engineering step of churn analysis. This approach enables
getting insight into emotional and behavioral patterns of those customers with a propensity to churn and leave a company.
Considering the outstanding Generative AI (GAI) power, specifically the capabilities of ChatGPT, we proposed the
application of this technology in the form of ‘interactive GAI-enabled feature engineering’ to enrich the content and structure of
ChurnKB. Using ChurnKB enables churn studies to leverage the features originating from the content of communications
between customers and companies in the customer churn analytical models. Hence coming up with insightful results in that
regard. On the other hand, considering the probable limitations of GAI and ChatGPT, to address the validity issue of our
approach, we used the knowledge of sales experts in the form of a feedback  loop. For that aim, experts were asked to fill in
a questionnaire related to the relevancy of the ChurnKB structure, content, and resulting analytical outcomes. They were also
asked to give their suggestions for improving our approach.
We received the expert’s feedback, which approved the validity of our approach. Although applying their suggestions helped us to
come up with promising experimental results, there are still opportunities to improve it. For example, one of the experts found that
customer churn-related features being used for developing the machine learning algorithm, are weakly relevant to identifying
customers’ churn-related cognitive and behavioral Patterns. Also, two ex perts found that using ’I’, ‘absolute words’, and
‘certainty words’ by customers in their communications or feedback acts as neutral factors in identifying customers’ churn-related
cognitive and behavioral Patterns. These issues will be explored more in our future studies.

Authors Contribution:
Writing (i.e., the original draft preparation), Maryam Shahabikargar, and Amin Beheshti; Validation, Maryam
Shahabikargar, and Amin Beheshti; Formal analysis, Maryam Shahabikargar, and Amin Beheshti; Investigation, Maryam
Shahabikargar, Amin Beheshti, Xuyun Zhang, Wathiq Mansoor, Jin Foo, an d Alireza Jolfaei; Writing (i.e., review and
editing), Maryam Shahabikargar, Amin Beheshti, Wathiq Mansoor, Alireza Jolfaei; Visualization and Evaluation,
Maryam Shahabikargar, and Amin Beheshti, Ambreen Hanif, Nasrin Shabani; Supervision, Amin Beheshti, Xuyun Zhang,
and Jin Foo; Project administration, Maryam Shahabikargar, and Amin Beheshti. All authors have read and agreed to
the published version of the manuscript.

20

Funding and Acknowledgments:
We acknowledge the Center for Applied Artificial Intelligence 13 at Macquarie University (Sydney, NSW, Australia) a nd
Prospa Advance Pty Limited 14 (Sydney, NSW, Australia) for supporting and funding this research.

Data Availability Statement:
The dataset used for supporting the proposed approach in this paper is publicly available at the following web page address:
https://github.com/aws-samples/churn-prediction-with-text-and-interpretability/blob/main/README.md

8.   References

[1] Tueanrat Y, Papagiannidis S, Alamanos E. Going on a journey: A review of the customer journey literature. Journal
of Business Research. 2021 Mar 1;125:336-53.

[2] C. Knowles.   Customer churn costing australian businesses millions, r eport finds.
https://itbrief.com.au/story/customer-churn-costing-australian-businesses-millions -report-finds.

[3] Ahn J, Hwang J, Kim D, Choi H, Kang S. A survey on churn analysis in various business domains. IEEE Access.
2020 Dec 4;8:220816-39

[4] Wu X, Li P, Zhao M, Liu Y, Crespo RG, Herrera-Viedma E. Customer churn p rediction for web browsers. Expert
Systems with Applications. 2022 Dec 15;209:118177.

[5] Kim K, Jun CH, Lee J. Improved churn prediction in telecommunication industry by analyzing a large network.
Expert Systems with Applications. 2014 Nov 1;41(15):6575-84.

[6] Amiri H, Daume III H. Target-dependent churn classification in microblogs. InProceed ings of the AAAI Conference
on Artificial Intelligence 2015 Feb 19 (Vol. 29, No. 1).

[7] Verbeke W, Martens D, Baesens B. Social network analysis for customer churn prediction. Applied Soft
Computing. 2014 Jan 1;14:431-46.

[8] De S, Prabu P. Predicting customer churn: A systematic literature review. Journal of Discrete Mathematical
Sciences and Cryptography. 2022 Oct 3;25(7):1965-85.

[9] Beheshti A, Benatallah B, Tabebordbar A, Motahari-Nezhad HR, Barukh MC, Nouri R. Datasyn apse: A social data
curation foundry. Distributed and Parallel Databases. 2019 Sep 15;37:351- 84

[10] Chai X, Deshpande O, Garera N, Gattani A, Lam W, Lamba DS, Liu L, Tiwari M, Tourn M, Vacheri Z, Prasad ST.
Social Media Analytics: The Kosmix Story. IEEE Data Eng. Bull.. 2013;36(3):4-12.

[11] Beheshti A, Vaghani K, Benatallah B, Tabebordbar A. Crowdcorrect: A curation pipeline for social data cleansing
and curation. InInformation Systems in the Big Data Era: CAiSE Forum 2018, Tallinn, Estonia, June 11-15, 2018,
Proceedings 30 2018 (pp. 24-38). Springer International Publishing.

[12] Beheshti A. Knowledge base 4.0: Using crowdsourcing services for mimicking the knowledge of domain experts.
In2022 IEEE International Conference on Web Services (ICWS) 2022 Jul 10 (pp. 425-427). IEEE.

[13] Domingos P. A few useful things to know about machine learning. Communications of the ACM. 2012 Oct
1;55(10):78-87

[14] Shahabikargar M, Beheshti A, Khatami A, Nguyen R, Zhang X, Alinejad-Rokny H. Domain  Knowledge Enhanced
Text Mining for Identifying Mental Disorder Patterns. In2022 IEEE 9th International Conference on Data Science and

13 https://www.mq.edu.au/research/research-centres-groups-and-facilities/centres/centre-for-applied-artificial-intelligence

14 https://www.prospa.com/

21

Advanced Analytics (DSAA) 2022 Oct 13 (pp. 1-10). IEEE

[15] Barukh MC, Zamanirad S, Baez M, Beheshti A, Benatallah B, Casati F, Yao L, Sheng QZ, Schiliro F. Cognitive
augmentation in processes. Next-Gen Digital Services. A Retrospective and Roadmap for Service C omputing of the Future:
Essays Dedicated to Michael Papazoglou on the Occasion of His 65th Birthday and His Retirement. 2021:123-37.

[16] Beheshti A, Yang J, Sheng QZ, Benatallah B, Casati F, Dustdar S, Nezhad HR, Zhang X, Xu e S. ProcessGPT:
Transforming Business Process Management with Generative Artificial Intelligence. arXiv prepr int arXiv:2306.01771.
2023 May 29.

[17] lawinsider dictionary. Business offerings. https://www .lawinsider.com/ dictionary/business-offerings.

[18] Lemon KN, Verhoef PC. Understanding customer experience throughout the customer journey. Journal of
marketing. 2016 Nov;80(6):69-96.

[19] Kotni VD. Paradigm shift from attracting footfalls for retail store to getting hits for e-stores: An evaluation of
decision-making attributes in e-tailing. Global Business Review. 2017 Oct;18(5):1215- 37.

[20] Blackwell RD, Miniard PW, Engel JF. Consumer behavior (10th eds.). Masao, OH: Thomson/Sount. 2006.

[21] R. Solomon, G. Bamossy, S. Askegaard, and M. Hogg. Consumer behaviour: European perspective 4th edition
prentice hall. Harlow, England (2010).

[22] Valaskova K, Kramarova K, Bartosova V. Multi criteria models used in Slovak consumer market for business
decision making. Procedia Economics and Finance. 2015 Jan 1;26:174-82.

[23] Dittmar H, Beattie J, Friese S. Gender identity and material symbols: Objects and decision consider ations in impulse
purchases. Journal of economic psychology. 1995 Sep 1;16(3):491-5 11.

[24] Khawaja S, Zia T, Sokić K, Qureshi FH. The impact of emotions on consumer behaviour: Exploring gender
differences.

[25] Havlena WJ, Holbrook MB. The varieties of consumption experience: comparing two typologies of emotion in
consumer behavior. Journal of consumer research. 1986 Dec 1;13(3):394 -404.

[26] Bostan B. Player motivations: A psychological perspective. Computers in Entertainment (CIE). 2009 Jun 24;7(2):1-
26.

[27] Borbora Z, Srivastava J, Hsu KW, Williams D. Churn prediction i n mmorpgs using player motivation theories
and an ensemble approach. In2011 ieee third international conference on privacy, security, risk and trust and 2011
ieee third international conference on social computing 2011 Oct 9 (pp. 157-164). IEEE.

[28] Yee N. The gamer motivation profile: What we learned from 250,000 gamers. InProceedings of the 2016 Annual
Symposium on Computer-Human Interaction in Play 2016 Oct 15 (pp. 2-2) .

[29] Ngai EW, Xiu L, Chau DC. Application of data mining techniques in customer relationship management: A
literature review and classification. Expert systems with applications. 2009 Mar 1;36(2):2592-602.

[30] M. A. Lejeune.  Measuring the impact of data mining on churn management .
Internet Research (2001).

[31] Parvatiyar A, Sheth JN. Customer relationship management: Emerging practice, process, and discipline. Journal of
Economic & Social Research. 2001 Jul 1;3(2).
[32] Tamaddoni Jahromi A, Sepehri MM, Teimourpour B, Choobdar S. Modeling customer churn in a non-contractual
setting: the case of telecommunications service providers. Journal of Strategic Marketing. 2010 Dec 1;18(7):587-98.

[33] Bose R. Customer relationship management: key components for IT success. Industrial management & Data
systems. 2002 Mar 1;102(2):89-97.

22

[34] Chandrashekar G, Sahin F. A survey on feature selection methods. Computers & Electrical Engineering. 2014 Jan
1;40(1):16-28.

[35] Brooks M, Amershi S, Lee B, Drucker SM, Kapoor A, Simard P. FeatureInsight: Visual support for error-driven
feature ideation in text classification. In2015 IEEE Conference on Visual Analytics Science and Technology (VAST) 2015
Oct 25 (pp. 105-112). IEEE.

[36] Zheng A, Casari A. Feature engineering for machine learning: principles and techniques for data scientists. "
O'Reilly Media, Inc."; 2018 Mar 23.

[37] Xie J, Sage M, Zhao YF. Feature selection and feature learning in machine learning applications for gas turbines: A
review. Engineering Applications of Artificial Intelligence. 2023 Jan 1;117:105591.

[38] Bengio Y, Courville A, Vincent P. Representation learning: A review and new perspectives. IEEE transactions on
pattern analysis and machine intelligence. 2013 Mar 7;35(8):1798-828.

[39] G. T. Reddy, M. P. K. Reddy, K. Lakshmanna, R. Kaluri, D. S. Rajput, G. Srivastava, and T. Baker. Analysis of
dimensionality reduction techniques on big data. Ieee Access 8, 54776 (2020).

[40] Guyon I, Elisseeff A. An introduction to variable and feature selection. Journal of machine learning research.
2003;3(Mar):1157-82.

[41] Katz G, Shin EC, Song D. Explorekit: Automatic feature generation and selection. In2016 IEEE 16th International
Conference on Data Mining (ICDM) 2016 Dec 12 (pp. 979-984). IEEE.

[42] I. Cohen.  Optimizing feature generation . https://towardsdatascience.com/optimizing-feature-generation-
dab98a049f2e.

[43] javaTpoint. Feature transformation in data mining. https://www.javatpoint.com/feature-transformation- in-
data-mining.

[44] Mckinsey and Company. Data preprocessing vs. feature engineering .
https://www.iguazio.com/questions/data-preprocessing-vs-feature-engineering-whats- the-difference/.

[45] Guyon I, Gunn S, Nikravesh M, Zadeh LA, editors. Feature extraction: foundations and applications. Springer; 2008
Nov 16.

[46] Ahuja R, Chug A, Kohli S, Gupta S, Ahuja P. The impact of features extraction on the sentiment analysis. Procedia
Computer Science. 2019 Jan 1;152:341-8.

[47] Fauzi MA, Utomo DC, Setiawan BD, Pramukantoro ES. Automatic essay scoring system using n-gram and cosine
similarity for gamification based e-learning. InProceedings of the International Con ference on Advances in Image
Processing 2017 Aug 25 (pp. 151-155).

[48] Li Y, Yang T. Word embedding for understanding natural language: a survey. Guide to big data applications.
2018:83-104.

[49] Blum AL, Langley P. Selection of relevant features and examples in machine learning. Artificial intelligence. 1997
Dec 1;97(1-2):245-71.

[50] Pfingsten T, Herrmann DJ, Schnitzler T, Feustel A, Scholkopf B. Feature selection for troubleshooting in complex
assembly lines. IEEE transactions on automation science and engineering. 2007 Jul 2;4(3):465-9.
[51] Beheshti A. Empowering generative ai with knowledge base 4.0: Towards linking analytical, cognitive, and
generative intelligence. In2023 IEEE International Conference on Web Services (ICWS) 2023 Jul 2 (pp. 763-771). IEEE.

[52] Yao R, Liu C, Zhang L, Peng P. Unsupervised anomaly detection using variational auto-encoder based feature
extraction. In2019 IEEE International Conference on Prognostics and Health Management (ICPHM) 2019 Jun 17 (pp. 1-7).
IEEE.

23

[53] Radford A, Metz L, Chintala S. Unsupervised representation learning with deep convolutional generative adversarial
networks. arXiv preprint arXiv:1511.06434. 2015 Nov 19.

[54] Cao Y, Li S, Liu Y, Yan Z, Dai Y, Yu PS, Sun L. A Comprehensive Survey of AI-Generated Content (AIGC): A
History of Generative AI from GAN to ChatGPT 2023. arXiv 2023. arXiv preprint arXiv:2303.04226.

[55] Xia X, Pan X, Li N, He X, Ma L, Zhang X, Ding N. GAN-based anomaly detection: A review. Neurocomputing.
2022 Jul 7;493:497-535.

[56] Jiang W, Hong Y, Zhou B, He X, Cheng C. A GAN-based anomaly detection approach for imbalanced industrial
time series. IEEE Access. 2019 Sep 30;7:143608-19.

[57] Staffini A, Svensson T, Chung UI, Svensson AK. A Disentangled VAE-BiLSTM Model fo r Heart Rate Anomaly
Detection. Bioengineering. 2023 Jun 3;10(6):683.

[58] Shi Y, Wang B, Yu Y, Tang X, Huang C, Dong J. Robust anomaly detection for multivariate time series through
temporal GCNs and attention-based VAE. Knowledge-Based Systems. 2023 Jun 14:110725 .

[59] Wang AX, Chukova SS, Nguyen BP. Data-Centric AI to Improve Ch urn Prediction with Synthetic Data.
In2023 3rd International Conference on Computer, Control and Robotics (I CCCR) 2023 Mar 24 (pp. 409-413). IEEE.

[60] Wu J, Plataniotis K, Liu L, Amjadian E, Lawryshyn Y. Interpretation for Variational Autoencoder Used to Generate
Financial Synthetic Tabular Data. Algorithms. 2023 Feb 16;16(2):121.

[61] Park N, Mohammadi M, Gorde K, Jajodia S, Park H, Kim Y. Data synthesis based on generative adversarial
networks. arXiv preprint arXiv:1806.03384. 2018 Jun 9.

[62] Kate P, Ravi V, Gangwar A. FinGAN: Chaotic generative adversarial network for analytical customer relationship
management in banking and insurance. Neural Computing and Applications. 2023 Mar;35(8):6015-28.

[63] Li B, Xie J. Study on the Prediction of Imbalanced Bank Customer Churn Based on Generative Adversarial
Network. InJournal of Physics: Conference Series 2020 Oct 1 (Vol. 1624, No. 3, p. 032054). IOP Publishing.

[64] P. Hofmann, T. Ru¨ckel,  and N. Urbach. Innovating with artificial intelligence: capturing the constructive
functional capabilities of deep generative learning (2021).

[65] Creswell A, White T, Dumoulin V, Arulkumaran K, Sengupta B, Bharath AA. Generative adversarial networks: An
overview. IEEE signal processing magazine. 2018 Jan 10;35(1):53-65 .

[66] Jin XB, Gong WT, Kong JL, Bai YT, Su TL. PFVAE: a planar flow-based variatio nal auto-encoder prediction
model for time series data. Mathematics. 2022 Feb 16;10(4):610.

[67] Kocaballi AB. Conversational ai-powered design: Chatgpt as designer, user, and pro duct. arXiv preprint
arXiv:2302.07406. 2023 Feb 15.

[68] Tirado-Olivares S, Navío-Inglés M, O’Connor-Jiménez P, Cózar-Gutiérrez R. From Human to Machine:
Investigating the Effectiveness of the Conversational AI ChatGPT in Historical Thinking. Education Sciences. 2023 Aug
5;13(8):803.

[69] Aydın Ö, Karaarslan E. Is ChatGPT leading generative AI? What is beyond expectations?. What is beyond
expectations. 2023.

[70] Su J, Yang W. Unlocking the power of ChatGPT: A framework for applying generative AI in education. ECNU
Review of Education. 2023 Apr:20965311231168423.

[71] Eysenbach G. The role of ChatGPT, generative language models, and artificial intelligence in medical education: a
conversation with ChatGPT and a call for papers. JMIR Medical Education. 2023 Mar 6;9(1):e46885.

24

[72] Dwivedi YK, Kshetri N, Hughes L, Slade EL, Jeyaraj A, Kar AK, Baabdullah AM, Koohang A, Raghavan V, Ahuja
M, Albanna H. “So what if ChatGPT wrote it?” Multidisciplinary perspectives on opportunities, challenges and
implications of generative conversational AI for research, practice and policy. International Journal of Information
Management. 2023 Aug 1;71:102642.

[73] Atlas S. ChatGPT for higher education and professional development: A  guide to conversational AI. 2023

[74] Mattas PS. ChatGPT: A Study of AI Language Processing and its Implications. Journal homepage: www. ijrpr. com
ISSN. 2023;2582:7421.

[75] Baidoo-Anu D, Ansah LO. Education in the era of generative artificial intelligence (AI): Understanding the potential
benefits of ChatGPT in promoting teaching and learning. Journal of AI. 2023 Jan;7(1):52-62.

[76] Cooper G. Examining science education in chatgpt: An exploratory study of generative artificial intelligence.
Journal of Science Education and Technology. 2023 Jun;32(3):444-52.

[77] Azaria A. ChatGPT usage and limitations. 2022

[78] Periáñez Á, Saas A, Guitart A, Magne C. Churn prediction in mobile social games: Towards a complete assessment using
survival ensembles. In2016 IEEE international conference on data science and advanced analytics (DSAA) 2016 Oct 17 (pp. 564-
573). IEEE.

[79] Buckinx W, Van den Poel D. Customer base analysis: partial defection of behaviourally loyal clients in a non-
contractual FMCG retail setting. European journal of operational research. 2005 Jul 1;164(1):252-68.

[80] Hung SY, Yen DC, Wang HY. Applying data mining to telecom churn management. Expert Systems with
Applications. 2006 Oct 1;31(3):515-24.

[81] Dahiya K, Bhatia S. Customer churn analysis in telecom industry. In20 15 4th International Conference on
Reliability, Infocom Technologies and Optimization (ICRITO)(Trend s and Future Directions) 2015 Sep 2 (pp. 1-6).
IEEE.

[82] Ribeiro H, Barbosa B, Moreira AC, Rodrigues RG. Determinants of churn in telecommunication services: a
systematic literature review. Management Review Quarterly. 2023 Feb 28:1-38.

[83] Mozer MC, Wolniewicz R, Grimes DB, Johnson E, Kaushansky H. Predicting subscriber dissatisfaction and improving
retention in the wireless telecommunications industry. IEEE Transactions on neural networks. 2000 May;11(3):690-6.

[84] Au WH, Chan KC, Yao X. A novel evolutionary data mining algorithm with applications to churn prediction. IEEE
transactions on evolutionary computation. 2003 Dec;7(6):532-45.

[85] Lalwani P, Mishra MK, Chadha JS, Sethi P. Customer churn prediction system: a machine learning approach.
Computing. 2022 Feb 1:1-24.

[86] Agrawal S, Das A, Gaikwad A, Dhage S. Customer churn prediction modelling based on behavioural patterns
analysis using deep learning. In2018 International conference on smart computing and electronic enterprise (ICSCEE) 2018
Jul 11 (pp. 1-6). IEEE.

[87] Alboukaey N, Joukhadar A, Ghneim N. Dynamic behavior based churn prediction in mobile telecom. Expert
Systems with Applications. 2020 Dec 30;162:113779.

[88] Rahman M, Kumar V. Machine learning based customer churn prediction in banking. In2020 4th international
conference on electronics, communication and aerospace technology (ICECA) 2020 Nov 5 (pp. 1196-1201). IEEE.

[89] Karvana KG, Yazid S, Syalim A, Mursanto P. Customer churn analysis and prediction using data mining models in
banking industry. In2019 international workshop on big data and information security (IWBIS) 2019 Oct 11 (pp. 33-38).
IEEE.

[90] Miao X, Wang H. Customer churn prediction on credit card services u sing random forest method. In2022 7th

25

International Conference on Financial Innovation and Economic Developm ent (ICFIED 2022) 2022 Mar 26 (pp. 649-
656). Atlantis Press.

[91] Larivière B, Van den Poel D. Investigating the role of product features in preventing customer churn, by using
survival analysis and choice modeling: The case of financial services. Expert Systems with Applications. 2004 Aug
1;27(2):277-85.

[92] Mavri M, Ioannou G. Customer switching behaviour in Greek banking services using survival analysis. Managerial
Finance. 2008 Feb 15;34(3):186-97.

[93] Zhang R, Li W, Tan W, Mo T. Deep and shallow model for insurance churn prediction service. In2017 IEEE
International Conference on Services Computing (SCC) 2017 Jun 25 (pp.  346-353). IEEE.

[94] Liferay. Why the insurance industry needs omnichannel. https:
//www.liferay.com/en-AU/blog/customer-experience/why-the-insurance-industry-needs-omnichannel.

[95] TechSee. 2022 state of customer churn in insurance: The impact of the pande mic on churn trends .
https://techsee.me/resources/reports/state- of-customer-churn-insurance-survey-report/.

[96] Hasumoto K, Goto M. Predicting customer churn for platform businesses: using latent variables of variational
autoencoder as consumers’ purchasing behavior. Neural Computing and Applications. 2022 Nov;34(21):18525-41.

[97] D. Court, D. Elzinga, S. Mulder, and O. J. Vetvik. The consumer decision journey. McKinsey Quarterly. 2009
3(3), 96.

[98] Følstad A, Kvale K. Customer journeys: a systematic literature review. Journal of Service Theory and Practice. 2018
Feb 8;28(2):196-227.

[99] Rezvani N, Beheshti A, Tabebordbar A. Linking textual and contextual features for intelligent cyberbullying
detection in social media. InProceedings of the 18th International Conference on Advances in Mobile Computing &
Multimedia 2020 Nov 30 (pp. 3-10).

[100] Troop NA, Chilcot J, Hutchings L, Varnaite G. Expressive writing, self‐criticism, and self‐reassurance. Psychology
and psychotherapy: Theory, research and practice. 2013 Dec;86(4):374 -86.

[101] De Choudhury M, Counts S, Horvitz E. Major life changes and behavioral markers in social media: case of
childbirth. InProceedings of the 2013 conference on Computer supported cooperative work 2013 Feb 23 (pp. 1431-1442).

[102] Fernandes AC, Dutta R, Velupillai S, Sanyal J, Stewart R, Chandran D. Identifying suicide ideation and suicidal
attempts in a psychiatric clinical research database using natural language processing. Scientific reports. 2018 May
9;8(1):7426.

[103] Bradley MM, Lang PJ. Affective norms for English words (ANEW): Instruction manual and affective ratings.
Technical report C-1, the center for research in psychophysiology, University of Florida; 1999 Jan.

[104] Beheshti A, Benatallah B, Motahari‐Nezhad HR. Processatlas: A scalable and extensible platform for b usiness
process analytics. Software: Practice and Experience. 2018 Apr;48(4):842-66.

[105] A. Beheshti, B. Benatallah, R. Nouri, and A. Tabebordbar. Corekg: a knowledge lake service. Proceedings of the
VLDB Endowment 11(12), 1942 (2018).

[106] Pennebaker JW, Boyd RL, Jordan K, Blackburn K. The development and psychometric properties of
LIWC2015. 2015 Sep 15.

[107] Mohammad SM, Turney PD. Crowdsourcing a word–emotion association lexicon. Computational intelligence.
2013 Aug;29(3):436-65.

[108] Zhou H. Research of text classification based on TF-IDF and CNN-LSTM. InJournal o f Physics: Conference
Series 2022 (Vol. 2171, No. 1, p. 012021). IOP Publishing.

26

[109] Kocher M, Savoy J. Distance measures in author profiling. Information processing & management. 2017 Sep
1;53(5):1103-19.

[110] Park K, Hong JS, Kim W. A methodology combining cosine similarity with classifier for text classification.
Applied Artificial Intelligence. 2020 Apr 15;34(5):396-411.
