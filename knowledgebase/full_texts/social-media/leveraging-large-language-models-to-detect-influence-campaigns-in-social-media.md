---
title: Leveraging Large Language Models to Detect Influence Campaigns in Social Media
url: https://arxiv.org/abs/2311.07816
category: social-media
subcategory: empirical
date: 2023-11
venue: ''
authors:
- Luca Luceri
- Eric Boniardi
- Emilio Ferrara
source: arxiv
pdf_url: https://arxiv.org/pdf/2311.07816
pages: 13
chars: 48207
fetched_at: '2026-11-08T13:02:36+00:00'
kb_version: 1
---

# Leveraging Large Language Models to Detect Influence Campaigns in Social Media

Leveraging Large Language Models to Detect Influence Campaigns in Social
Media
LUCA LUCERI∗, ERIC BONIARDI, and EMILIO FERRARA, University of Southern California & USC
Information Sciences Institute, Los Angeles, CA, USA
Social media influence campaigns pose significant challenges to public discourse and democracy. Traditional detection methods fall
short due to the complexity and dynamic nature of social media. Addressing this, we propose a novel detection method using Large
Language Models (LLMs) that incorporates both user metadata and network structures. By converting these elements into a text
format, our approach effectively processes multilingual content and adapts to the shifting tactics of malicious campaign actors. We
validate our model through rigorous testing on multiple datasets, showcasing its superior performance in identifying influence efforts.
This research not only offers a powerful tool for detecting campaigns, but also sets the stage for future enhancements to keep up with
the fast-paced evolution of social media-based influence tactics.
1 INTRODUCTION
While AI’s potential in diverse fields is unprecedented, its ethical implications, especially in the context of shaping
reality, cannot be understated [6, 39]. For example, within the modern digital ecosystem, malicious actors who aim at
reshaping public opinion using influence campaigns have acquired a new powerful weapon: Tools such as ChatGPT can
significantly complicate the task of distinguishing between human-generated content or AI content [3]. Large Language
Models (LLMs) can be used to manufacture certain narratives or spread disinformation [8]. The use of automation and
synthetic personas to steer public opinion on social networks is of particular concern [9]. Furthermore, the emergence
of Generative AI brings about a new layer of complexity, enabling the creation of potentially highly persuasive messages
whose detection is a technical challenge that is almost insurmountable [3, 7].
This paper addresses the complexities of AI-driven influence campaigns, underscoring the need for diligent research,
adherence to ethical AI practices, and the creation of robust countermeasures to maintain the integrity of online
dialogue. In particular, we explore the use of open-source LLMs for detecting influence campaigns, introducing novel
methods capable of recognizing such campaigns that originate from various nations. Our goal is to surpass the current
state-of-the-art in detecting influence campaigns by leveraging content metadata and network information, such as
retweet networks and network centralities. To this end, we use a manually labeled dataset to construct supervised
models, drawing from a wide spectrum of sources, including Twitter’s Information Operations datasets [10, 24] and
data related to Russian Twitter trolls [1]. Our paper addresses the following research questions (RQs):
RQ1: To what extent are current state-of-the-art methods effective in detecting information operation campaigns and do
these methods experience any degradation in performance when applied to new (unseen) influence campaigns and tactics?
We find that although state-of-the-art methods are effective, their performance diminishes when they are applied to
newer datasets, suggesting that LLMs’ potential to adapt may enable them to evade these techniques. This highlights
the imperative for innovative dynamic detection methods.
∗LL, EB, and EF contributed equally to this research.
Authors’ address: Luca Luceri, lluceri@isi.edu; Eric Boniardi, boniardi@isi.edu; Emilio Ferrara, emiliofe@usc.edu, University of Southern California &
USC Information Sciences Institute, Los Angeles, CA, USA.
1
arXiv:2311.07816v1  [cs.SI]  14 Nov 2023

2 Luceri, Boniardi, and Ferrara
RQ2: Do techniques based on LLMs offer superior classification performance compared to state-of-the-art methods, and
does the integration of various types of information, such as content, network information, and user metadata, enhance
classification performance?
Our findings indicate that LLM-based techniques achieve comparable, and often superior, performance in unseen
influence campaigns and tactics. Nonetheless, the performance declines when multiple information types are combined
as a single input, underscoring the need for further research to refine the integration of multi-inputs that enhance
overall results.
Summary of contributions: In this article, we conduct an analysis of influence campaigns emanating from four distinct
countries. We propose innovative methods for detecting drivers of influence operations and benchmark them against
state-of-the-art methods. In doing so, we contribute valuable insights and directions for future research, particularly
focusing on the application of open-source LLMs to identify malicious entities within influence campaigns.
2 RELATED WORK
The landscape of social media is increasingly shaped by influence operations, often orchestrated by bots and coordinated
accounts, representing a key concern in today’s digital environment. The COVID-19 pandemic underscored the tangible
effects of influence operations [ 23], with Rao et al. [ 28] examining the relationship between political biases and
antiscience sentiment in online discourse, proposing that influence operations may have contributed to shaping these
discussions. Similarly, Jiang et al. [13] investigated the amplification of polarization and echo chambers on social media
during the pandemic, underscoring the role of influence operations in establishing beliefs and limiting the diversity
of information. The significance of bot-driven influence and the need for sophisticated detection mechanisms were
highlighted by Yang et al. [38], emphasizing the urgency of advanced tools to identify and comprehend bot activities
that frequently spearhead these operations [17].
Based on the narrative of bot influence, the detection of coordinated accounts, which serve as vectors for influence
operations, has emerged as a critical research area [11, 19, 22, 26, 36]. Previous work introduced pioneering methodologies
to identify such accounts, underlining their importance in concealed influences [18, 32] and coordinated online campaigns
[6, 33]. While these approaches have primarily concentrated on identifying coordinated malicious accounts based on
behavioral similarities, Addawood et al. [1] introduced a content-based approach, which extracts linguistic cues from
the messages shared by inauthentic actors to enable their detection. Complementing this class of approaches, Sapienza
et al. [29] presented DISCOVER, a tool designed to glean insights from online conversations, stressing the need for
vigilance against potential malicious operations.
In the realm of employing language models for social media analysis, Kumar et al. [16] developed a combined neural
network ensemble comprising Text CNN and LSTM models with BERT embeddings to categorize tweets, showcasing
the capability of language models in bot detection based on textual content. Advancing the field, Malik et al. [ 20]
used BERT, augmented by fine-tuning, to detect propaganda on social media platforms, signifying the effectiveness of
semantic and fine-tuned language models.
Acknowledging the vital role of network information in social network analysis and the inherent textual processing
nature of language models, it becomes imperative to devise methodologies that can adeptly convert network data into
text. Cai et al. [4] introduced LM Bot, illuminating the feasibility of entering network information into a language model
for Twitter bot detection. Ye et al. [40] provided a formalization to translate graph knowledge into text, demonstrating

Leveraging Large Language Models to Detect Influence Campaigns in Social Media 3
that natural language processing can efficiently interpret graph data, thus forging new pathways for research in
detecting influence campaigns where graph information is crucial.
The advent of new and more potent large language models has carved a niche for their application in the detection
of influence campaigns, particularly the open-source variants, which offer the advantage of usage without the need for
data sharing, preventing malicious entities from exploiting these models in controlled settings for adversarial learning.
3 DATA
3.1 Twitter Information Operations
In line with recent studies [15, 19, 24], this investigation uses data from the Twitter’s Information Operations archive
[10]. Twitter has released more than 141 datasets detailing information operations, comprising tweets from operators
in 21 countries, collected from 2008 to 2021. Operators involved in these campaigns take advantage of a variety of
strategies on the platform [19], aimed at different user communities with a wide range of objectives.
These operations are inherently complex, orchestrated by entities ranging from small groups to large collectives,
and may involve human agents, automated bots, or compromised accounts. The targets and objectives are equally
diverse, encompassing specific groups, entire nations, or broad geopolitical regions, employing tactics from simple
spam to sophisticated strategies like coordination, rotation, obfuscation, all adaptable and primarily political in nature.
Furthermore, these operations extend beyond Twitter, indicating a widespread challenge in the digital ecosystem.
Researchers at Indiana University have provided access to a control dataset they constructed, which aids in the
identification of operators involved in information campaigns [24]. They assembled tweets from accounts not directly
involved in information operations, but engaging in related discussions concurrently. The hashtags used by the operators
were extracted and used to query Twitter’s academic search API, identifying accounts with tweets that match the dates
and hashtags of the operators. The timelines for these accounts were then reconstructed, collecting up to 100 tweets
from the same dates as the operators.
3.2 Twitter Dataset on Russian Troll Activity
The secondary data set used in this investigation was derived from the work of Addawood et al. [1], examining the
operations of Russian trolls on Twitter around the time of the 2016 U.S. Presidential election. The dataset encompasses
information from 2,752 Russian troll accounts identified and released by the U.S. Congress. Using Crimson Hexagon, a
social media analytics tool, the researchers collected a significant volume of tweets and retweets (1,226,185 in total),
produced by these trolls, with approximately 27% of this content in the Russian language.
The dataset was further enriched by incorporating non-troll tweets, collected through two distinct methodologies.
Initially, tweets were collected using a compilation of hashtags and keywords directly associated with the 2016 election.
The second method involved collecting tweets from the same users while purposely omitting the aforementioned election-
related terms, with a careful exclusion of any user who had retweeted troll-affiliated content. This comprehensive
approach resulted in an extensive corpus of 12.36M tweets, generated by 1.17M unique user accounts.
3.3 Dataset Generation for LLM Analysis
For the purpose of our analysis, the datasets were selectively curated to focus on five countries: Egypt, UAE, Ecuador
and Venezuela, from the Twitter Information Operations archive, and Russia, from the Twitter Dataset on Russian
Troll Activity. We group together the accounts that Twitter associated with Egypt and the UAE influence campaigns,

4 Luceri, Boniardi, and Ferrara
based on Twitter’s reports [10] and previous work [6, 35] that revealed that their activity was primarily linked to an IO
originating from both countries and targeting Iran and Qatar.
The data set generation process was implemented as follows. Initially, we calculate the median time interval between
the first and last tweets for each influence operation. Tweets preceding and including this median time constitute the
training set, with a capping mechanism limiting each user to a maximum of 100 randomly selected tweets to curtail the
dataset’s volume. Tweets after the median time serve as the basis for the test set. To maintain the integrity of the data
set and avoid information leakage, any users featured in the training set were omitted from the test set. The selection
criteria for the test set mirrored those of the training set, with an identical cap on tweets.
In our study, we perform both tweet and user classification tasks. For the former, we further distill the dataset
due to computational constraints, leveraging only a random subset of ten tweets for every user. For both tasks, we
comprehensively include original tweets and retweets. Tables 1 and 2 offer an in-depth breakdown of the datasets,
cataloging the total user counts and distinguishing between driver of information campaigns and organic, control
accounts, in addition to detailing the aggregate tweet counts.
Country Train/Test Driver Organic Driver %
Russia Train 200 10,000 2%
Russia Test 200 10,000 2%
Egypt&UAE Train 1,000 4,000 20%
Egypt&UAE Test 625 2,500 20%
Ecuador Train 325 1,625 20%
Ecuador Test 250 1,250 20%
Venezuela Train 500 2,500 25%
Venezuela Test 325 1,625 25%
Table 1. Number of users for each dataset. For each country, the table reports the division into training and test sets, the number of
driver and organic users, and the percentage of driver users.
Country Train/Test Driver Organic Driver %
Russia Train 1,782 71,922 2.48%
Russia Test 2,159 92,602 2.33%
Egypt&UAE Train 8,898 35,983 24.73%
Egypt&UAE Test 7,234 29,000 24.95%
Ecuador Train 5,276 32,199 16.39%
Ecuador Test 7,832 36,387 21.52%
Venezuela Train 10,057 50,949 19.73%
Venezuela Test 8,950 42,084 21.26%
Table 2. Number of tweets for each dataset. For each country, the table reports the division into training and test sets, the number of
driver and organic tweets, and the percentage of driver tweets.
4 METHODS
In a scenario where social media platforms are increasingly leveraged for influence campaigns, text, user information,
and network structures are essential to detecting and understanding the dynamics of these operations. The key to

Leveraging Large Language Models to Detect Influence Campaigns in Social Media 5
effective detection and analysis of influence campaigns lies in comprehending and modeling the interconnections
between these crucial components. Motivated by this requirement, our study undertakes two different tasks: (i) tweet
classification, and (ii) user classification. The former involves examining individual tweets to identify those that are
part of an influence campaign. The latter focuses on distinguishing key actors who are actively driving these influence
efforts from genuine, legitimate users. Large Language Models (LLMs) [21] are utilized for classification purposes. The
following sections provide a more detailed exploration of how our methodologies leverage this technology.
4.1 Tweet Classification via LLMs
For tweet classification, we envision the utility of employing LLMs to analyze and understand the structure and
distinctive features of tweet messages associated with an influence campaign. In particular, the classification is carried
out using the open-source LLM Llama 2 released by Facebook [34]. The advantage of this open-source model lies in its
ability to run locally, thereby eliminating the need to share data with external parties. We utilize the Microsoft Guidance
[2] repository to implement both zero-shot [14] and few-shot prompting techniques [27]. This repository comes with a
comprehensive set of tools and guidelines, specifically designed to facilitate the execution of these prompting techniques.
A key feature of this repository, is its ability to enforce a binary output as a response.
As a final technique, we implemented a more sophisticated approach known as fine-tuning [37], which is a training
technique that learns the structure of the data, rather than solely relying on prompting. It employs a form of supervised
learning where both tweets and labels are provided. For carrying out the fine-tuning process, we utilized the LLaMA
Factory repository [12].
4.1.1 Zero-Shot Prompting. Zero-Shot Prompting is a technique that allows our model to generate responses without
having seen any examples of the task at hand [14]. This is achieved by providing the model with a “prompt” in the form
of a plain question or statement, which guides the model’s response generation. The model then uses its understanding
of language and context to generate a response, which in this case is a binary variable. This approach is particularly
useful for tasks where the context can be easily encapsulated in a single prompt, and where the model’s pre-existing
knowledge and understanding of language are sufficient to generate an appropriate response.
In Figure 1, we display the prompts utilized in our Zero-Shot Prompting approach. These prompts specifically
incorporate the term “Influence Campaign”, presented in two variations - with and without a definition. Similarly, Figure
2 illustrates prompts that include the term “InfoOps” (abbreviation commonly used to indicate information operations),
also here showcased in two formats - with and without a definition. The definitions are sourced from ChatGPT [25].
4.1.2 Few Shots Prompting. According to the principles of few-shot prompting [ 27], we can adjust our model to
incorporate some labeled examples. By doing so, we aim to enhance the model’s ability to generalize from these
examples to unseen instances of the task. Specifically, we form our prompts to include two examples of tweets for
classification: one from an organic user and one from an information operation driver. In doing so, we aim to provide
our model with a clearer understanding of the task and improve its performance in detecting influence campaign
messages. An example of prompt is illustrated in Figure 3.
4.1.3 Fine-tuning. Fine-tuning is a key step in adapting LLaMa 2 to the specific task of detecting influence campaign
messages on Twitter. This process involves tuning the model to recognize the specific patterns associated with messages
belonging to influence campaigns or grassroots conversations. Notably, this process involves adjusting only a subset of

6 Luceri, Boniardi, and Ferrara
Prompt 1: Determine if the following tweet is part of an influence campaign. Please answer with a
single word, either “True” or “False”.
Prompt 2: An influence campaign, is a coordinated and organized effort by individuals, groups,
or governments to manipulate, shape, or sway public opinion, beliefs, behaviors, or
policies through various forms of communication and media. These campaigns can take
place in both online and offline environments and typically involve the dissemination of
information, disinformation, propaganda, or other persuasive tactics to achieve specific
objectives. These objectives can range from promoting a particular ideology, supporting
a political candidate, destabilizing a rival nation, or undermining trust in institutions.
Influence campaigns can employ a variety of methods, including social media manipulation,
spreading fake news or false narratives, conducting psychological operations, using
targeted advertising, and leveraging networks of individuals or bots to amplify messages.
These campaigns often aim to exploit vulnerabilities in the information ecosystem and
exploit cognitive biases in order to achieve their goals. Given this context, determine if
the following tweet is part of an influence campaign. Please answer with a single word,
either “True” or “False”.
Fig. 1. Prompts in the zero-shot setting related to Influence Campaigns
Prompt 3: Determine if the following tweet is part of an InfoOps campaign. Please answer with a
single word, either “True” or “False”.
Prompt 4: InfoOps refer to a coordinated effort by individuals or groups to manipulate or shape
public opinion on Twitter by spreading false or misleading information. These operations
can have various objectives, including: - Political Manipulation: Some information opera-
tions aim to influence political events, such as elections or policy decisions, by spreading
misinformation or promoting particular candidates or ideologies. - Social Division: Others
may seek to sow discord and amplify existing social or political divisions by disseminating
inflammatory content or exploiting sensitive issues. - Brand or Reputation Management:
Some businesses or organizations may use Twitter information operations to manage
their online reputation by spreading positive narratives or suppressing negative ones. -
Malicious Activities: In some cases, these operations can involve cyberattacks, identity
theft, or the dissemination of harmful malware through links shared on Twitter. - Am-
plification of Propaganda: State-sponsored actors or non-state actors may use Twitter
to amplify propaganda, particularly in the context of geopolitical conflicts. Given this
context, determine if the following tweet is part of an InfoOps campaign. Please answer
with a single word, either “True” or “False”.
Fig. 2. Prompts in the zero-shot setting related to InfoOps Campaigns
the model’s weights to better fit our task, rather than retraining all the weights, which could be both computationally
and economically daunting [31].
We create JSON files for both the training and testing phases, specifically structured to fine-tune the model on tweet
textual content. Every JSON file encapsulates the essential information needed for fine-tuning, including the input
(tweet text), the instruction (prompt), and the label. We then employ the repositoryLLaMa Factory [12], to fine-tune the

Leveraging Large Language Models to Detect Influence Campaigns in Social Media 7
Example: The truth that USA is in a real problem because #Tamim want to deal with #USA and
#Qatar funds terrorism! https://t.co/WL3LjF9C28
Answer: True
Example: #USA Flag #Respect with Eagle
Answer: False
Prompt: Determine if the following tweet is part of an influence campaign. Please answer with a
single word, either “True” or “False”.
Fig. 3. Example of prompt in the few-shots setting
model and adjust the weights to our specific task. Upon completion of the fine-tuning process, the adapted model can
then be employed to predict labels, enabling us to classify unseen tweets and identify potential influence campaigns.
4.2 LLM-empowered User Classification
To perform user classification, we use a modified version of LLaMa 2, specifically LLaMA-2-7B-32K, developed by
Together Computer [5]. This enhanced model is designed to accommodate a larger input space of 32,000 tokens,
surpassing the standard model’s maximum context limit of 8,000 tokens. This key enhancement is instrumental in
managing the extensive information associated with user classification.
We fine-tune multiple models using the LLaMa Factory by incorporating various types of information. The fine-tuned
models are then used for classification purposes. We propose four different models, and their combination in a unified
model, leveraging users’ interactions, centralities in the interaction network, metadata, and shared content. In the
next sections, we provide a detailed description of this process, discussing the diverse types of information used for
fine-tuning, and the application of the models for classification.
4.2.1 Interaction-based User Classification. The core idea of this model is to extract the structure of the interaction
network based on the retweets exchanged between Twitter users. As LLaMa 2 models the relationships in text, it can be
used to represent the network once its description is converted into words. This allows us to directly use the output of
the model, bypassing the complexity of traditional network extraction methods. In order to transcribe the network into
text, we followed the paradigm developed by Ye et al. [40].
We construct a network of retweets to capture the interactions between users. In this network, each user is represented
as a node, and an edge represents a retweet from the user who retweets to the author of the original tweet. The training
retweet network is created using all the tweets from the training set. In this network, user i is connected to user j if
user i has retweeted at least once user j. Similarly, the test retweet network is constructed using all retweets at our
disposal. It is important to note that users in the training set do not overlap with users in the test set.
Given this formulation, we generate JSON files with specific instructions and inputs. The instruction is to “Determine
if the user is actively driving an influence campaign. ” The input is structured as “Useri is connected to j, k, m, ... ” and the
output is a binary variable (True vs. False) indicating whether the user is driving an influence campaign. Accordingly,
we fine-tune our model and classify accounts based on the model outputs.

8 Luceri, Boniardi, and Ferrara
4.2.2 Centrality-based User Classification. Centralities measures are a crucial element in identifying coordinated
actions [19]. In this work, we employ different properties of network centrality [30] to identify drivers of influence
campaigns. In particular, we compute the degree, eigenvector, and PageRank centralities based on the retweet network
(cf. §4.2.1). These metrics are used to generate JSON files for training and testing. Each JSON file contains the following
information: The instruction “Determine if the user is actively driving an influence campaign”; the input “User i has a
degree centrality of x, an eigenvector centrality of y, and a PageRank centrality of z”; and the output is either “True” or
“False”. These JSON files are used for fine-tuning and classification.
4.2.3 Metadata-based User Classification. Metadata can also play a crucial role in enhancing the performance of our
model [1]. Specifically, for each tweet, we extract metadata that provides additional context about the tweet, which can
help our model better understand the context in which the user operates. The analyzed metadata includes hashtags, URLs,
and user mentions derived from the user’s tweets. The processing of this metadata involves the removal of duplicates.
Specific modifications are considered for URLs. For Twitter and Telegram URLs, the process involves extracting the last
segment of the link. For example, ‘https://t.me/1234’ becomes ‘1234’ and ‘https://t.co/5678’ becomes ‘5678’. For all other
URLs, we consider only their domain, e.g., ‘www.foxnews.com/politics’ becomes ‘www.foxnews.com’.
The construction of the JSON files is similar to the models previously discussed: The instruction is “Determine
whether the user is actively driving an influence campaign”; The input is “The user has the following metadata: hashtags,
URLs, and mentions”. The expected output is a binary variable that indicates whether the user is driving an influence
campaign. As before, we use this framework to fine-tune the model and perform our classification task.
4.2.4 Content-based User Classification. This model leverages the tweet classification task to generate a score to classify
users as either drivers of influence campaigns or organic users. This process involves multiple steps, starting from the
division of training tweets into train and validation sets, where 90% is assigned to the train set and 10% to the validation
set. JSON files are then generated for the tweets, with the aim of determining if a given tweet is part of an influence
campaign. The input of the model is the text of the tweet, and the output is a binary variable indicating whether the
tweet belongs to an influence campaign.
Fine-tuning is performed on the tweets in the train set, and predictions are made on the validation and test set. The
user score is computed by taking the average of test outcomes (0 for False and 1 for True) of user’s classified tweets.
The score for control users is expected to be near zero, while it should be close to one for driver users. The threshold
for determining if the user is driving an influence campaign is tuned by maximizing the AUC on the validation set. The
classification on the test set uses the threshold established in the validation step to perform user classification.
4.2.5 Multi-Input Model. Finally, we develop a model that combines different input sources. This approach aims
to leverage the strengths of each individual data source, potentially enhancing the overall predictive power of our
model. As in the models described above, the instruction in the JSON files aims to determine if a user is driving an
influence campaign. As input, we use a combination of the inputs utilized in the other models, i.e., retweet connections,
centralities, metadata, and content-based score. This diverse suite of features is concatenated, forming a multi-input
model that is fine-tuned to perform user classification.
5 RESULTS
In our empirical analysis, we engage in two main tasks aimed at uncovering the messages and actors driving influence
campaigns. The first task is tweet-centric and aims at classifying content as belonging or not to influence operations.

Leveraging Large Language Models to Detect Influence Campaigns in Social Media 9
Test Precision (%) Recall (%) F1-Score (%) AUC (%)
Zero-Shot Prompt 1 16.56 ±9.93 55.80 ±10.99 22.95 ±12.02 49.16 ±7.07
Zero-Shot Prompt 2 14.21 ±7.19 95.61 ±5.03 23.94 ±11.69 49.66 ±0.54
Zero-Shot Prompt 3 13.56 ±7.36 35.92 ±9.01 18.14 ±9.69 46.79 ±4.41
Zero-Shot Prompt 4 9.90 ±7.89 98.84 ±0.42 17.12 ±13.10 49.90 ±0.18
Few-Shot 0.00 ±0.00 0.00 ±0.00 0.00 ±0.00 49.99 ±0.01
Fine-Tuning 64.74 ±15.56 46.93 ±28.24 46.95 ±14.52 69.61 ±9.68
Linguistic Cues [1] 91.20 ±6.47 97.41 ±2.98 94.08 ±3.90 69.23 ±12.73
Table 3. Comparative classification performance of the tweet classification task for different
methods across four influence campaigns.
Fig. 4. Comparative analysis of five methods across four influence campaigns. The best-performing technique is highlighted.
The second task focuses on users, assessing their involvement in such campaigns by examining their tweets, metadata,
connections, and position in the interaction network. We use the linguistic approach proposed by Addawood et al. [1]
as our baseline model and benchmark this technique against our proposed models. Our investigation spanned four
distinct influence campaigns, as described in Section 4.1.
5.1 Tweet Classification
For the tweet classification task, we compare our proposed zero-, few-shot, and fine-tuned models with a linguistic
approach [1]. The results of the tweet classification task are presented in Table 3 by averaging the classification
performance across the four datasets.
The linguistic approach exhibits superior performance in terms of precision and F1-score compared to our proposed
methods. The results concerning zero- and few-shot methods demonstrate the considerable challenge of this task when
limited or no information is provided for training a model. Interestingly, when definitions are supplied (Prompt 2 and
Prompt 4) in a zero-shot setting, our models attain near-perfect recall. However, this achievement is coupled with
limited precision. Additionally, it is important to emphasize the challenges encountered in the few-shot setting. When

10 Luceri, Boniardi, and Ferrara
Test Precision (%) Recall (%) F1-Score (%) AUC (%)
Linguistic Cues [1] 89.43 ±6.71 96.71 ±3.60 92.76 ±3.73 67.55 ±13.81
Centrality 46.92 ±16.69 47.98 ±33.56 43.48 ±25.07 69.17 ±13.39
Content 94.74 ±5.84 92.12 ±9.61 92.92 ±4.55 76.37 ±12.04
Interaction 41.14 ±18.89 53.82 ±35.92 41.65 ±24.79 69.18 ±13.33
Metadata 85.94 ±13.02 84.82 ±24.07 84.67 ±19.03 91.18 ±12.67
Table 4. Comparative classification performance of the user classification task for different
methods across four influence campaigns.
examples of driver and organic tweets are given, the model often predicts false outcomes almost consistently. This
results in precision, recall, and F1 scores dropping to zero, given the minimal or nonexistent count of true positives.
Nevertheless, the subpar classification performance could stem from the manual selection of tweets provided to the
LLM. This process may either lack representativeness of influence messages or introduce inherent biases. Future efforts
will be directed towards addressing this issue.
Finally, when assessing the AUC, our fine-tuned based on Llama Factory allows us to achieve superior results
compared to the baseline technique, highlighting its potential for the user classification task, and in particular for the
content-based model.
5.2 User Classification
We conducted a series of experiments to assess the performance of our proposed methods versus the baseline approach
[1]. The results of these experiments are illustrated in Figure 4, whereas Table 4 aggregates the results of the different
campaigns.
There are a few noteworthy observations. First, among the proposed models, the content-based approach consistently
demonstrates strong classification accuracy across various campaigns, either outperforming the state-of-the-art approach
based on linguistic cues [1] or delivering comparable results. Second, the metadata-based model also achieves promising
classification results, with the highest average AUC among the evaluated approaches. Other models, such as those
based on interactions and centralities, show limited classification capabilities across campaigns. Finally, the baseline
approach excels in identifying the 2016 Russian campaign but experiences diminishing efficacy with more recent
influence operations, such as those from Egypt & UAE, Venezuela, and Ecuador. Overall, these results indicate the
potential of LLMs to adapt to more sophisticated and unseen campaigns in which malicious actors could evade existing
detection solutions.
Ablation Study. We conduct an ablation study to evaluate the effectiveness of different types of information and
identify the most relevant feature. In each ablation test, we use models based on retweet interactions, centralities,
content, metadata, and their combinations, as described in Section 4.2.5.
The results of these tests are shown in Figure 5. A test marked as “-X” indicates that we use a model with all features
except “X”. Notably, classification performance remains consistent when we employ all features or exclude just one.
However, models based on a single feature at a time generally achieve superior performance (cf. Fig. 4). This prompts
questions about potential interferences between these combinations and underscores the need for further research to
enhance the adaptability of LLMs to diverse inputs.

Leveraging Large Language Models to Detect Influence Campaigns in Social Media 11
Fig. 5. Ablation study: performance of models using all feature dimensions, and respectively after removing interaction, centrality,
metadata, or content features.
6 CONCLUSIONS
In this study, we introduced novel methodologies to identify influence campaigns on social media building upon the
general-purpose language modeling strengths of LLMs. We found that while current state-of-the-art methods are
effective, their performance diminishes when applied to new influence campaigns, highlighting the need for innovative
dynamic detection methods. Our methodology addresses this shortfall by incorporating elements such as content,
network structures, and user metadata. These elements are subsequently transformed into a textual format compatible
with Large Language Models (LLMs). Empirical results indicate that our model not only successfully identifies influence
campaigns but also adapts to the multilingual and multifaceted dimensions of social media, thereby enhancing the
robustness of influence detection mechanisms.
Despite the encouraging results, we recognize the need for continuous improvement. Future research should focus
on enhancing the flexibility of LLMs to accommodate multiple input data sets to improve overall results. Furthermore,
the potential to broaden the scope of this research utilizing different and larger models, such as those with 40B and
70B parameters, underscores an exciting avenue for future exploration. This presents a compelling trajectory for the
advancement of this field.
Limitations. This research is not exempt from limitations. First, we utilize only a subset of influence campaigns
released in the Twitter information operations archive [10]. This limitation is due to constraints related to computational
resources and the computing time required for our experiments. Nevertheless, the diversity of the analyzed campaigns
ensures the robustness of our results.

12 Luceri, Boniardi, and Ferrara
Second, for the same resource-related reasons, the models developed for both the text and user classification tasks rely
on only a subset of available tweets. The presented performance may, therefore, potentially improve when employing a
larger set of tweets.
Third, we adopted a manual approach for selecting few-shot examples. This involved reviewing and choosing tweets
that best represented our two classes of accounts. However, we recognize that this selection method may introduce
biases. The selection of tweets is subjective and may not precisely capture the distinction between messages generated
by drivers and organic users. These factors could have impacted the results associated with the few-shot approach,
demonstrating poor classification performance. Future work will explore alternative methods for selecting few-shot
examples to address these issues.
Finally, our identification of influence campaign drivers relies on users recognized by Twitter, and the precise methods
behind this identification remain undisclosed. Potential biases in data collection and the potential misclassification of
accounts can affect our models’ detection effectiveness.
Ethical considerations. Prioritizing user privacy, we ensured that all control data were anonymized before any analysis
was performed. It is essential to recognize that, despite the rigor of our approach, there is a possibility that our model
may inadvertently misidentify legitimate user accounts as those involved in influence campaigns. This requires a
careful and critical analysis of the results obtained. Furthermore, it is conceivable that the actors behind influence
campaigns could be mistakenly classified as regular control accounts, which could allow the continued propagation of
misinformation or fraudulent activities. Therefore, we recommend using our model within a broader toolkit designed to
incorporate other behavioral, textual, and metadata features to improve the classification accuracy between authentic
users and those engaged in influence operations.
ACKNOWLEDGMENTS
Work supported in part by DARPA (contract #HR001121C0169).
REFERENCES
[1] Aseel Addawood, Adam Badawy, Kristina Lerman, and Emilio Ferrara. 2019. Linguistic cues to deception: Identifying political trolls on social media.
In Proceedings of the international AAAI conference on web and social media , Vol. 13. 15–25.
[2] Guidance AI. 2023. Guidance AI Repository. https://github.com/guidance-ai/guidance
[3] Isabelle Augenstein, Timothy Baldwin, Meeyoung Cha, Tanmoy Chakraborty, Giovanni Luca Ciampaglia, David Corney, Renee DiResta, Emilio
Ferrara, Scott Hale, Alon Halevy, et al. 2023. Factuality Challenges in the Era of Large Language Models. arXiv preprint arXiv:2310.05189 (2023).
[4] Zijian Cai, Zhaoxuan Tan, Zhenyu Lei, Hongrui Wang, Zifeng Zhu, Qinghua Zheng, and Minnan Luo. 2023. LMBot: Distilling Graph Knowledge
into Language Model for Graph-less Deployment in Twitter Bot Detection. arXiv preprint arXiv:2306.17408 (2023).
[5] Together Computer. 2023. LLaMA-2-7B-32K Model. https://huggingface.co/togethercomputer/LLaMA-2-7B-32K. Accessed: 2023.
[6] Fatima Ezzeddine, Luca Luceri, Omran Ayoub, Ihab Sbeity, G Nogara, Emilio Ferrara, and Silvia Giordano. 2023. Exposing influence campaigns in
the age of LLMs: a behavioral-based AI approach to detecting state-sponsored trolls. EPJ Data Science 12, 46 (2023).
[7] Emilio Ferrara. 2023. GenAI Against Humanity: Nefarious Applications of Generative Artificial Intelligence and Large Language Models. arXiv
preprint arXiv:2310.00737 (2023).
[8] Emilio Ferrara. 2023. Should ChatGPT be Biased? Challenges and Risks of Bias in Large Language Models. First Monday 28, 11 (2023).
[9] Emilio Ferrara. 2023. Social bot detection in the age of ChatGPT: Challenges and opportunities. First Monday 28, 6 (2023).
[10] Vijaya Gadde and Kayvon Beykpour. 2020. Additional steps we’re taking ahead of the 2020 US election. Social Media. Twitter.
[11] Fabio Giglietto, Nicola Righetti, Luca Rossi, and Giada Marino. 2020. It takes a village to manipulate the media: coordinated link sharing behavior
during 2018 and 2019 Italian elections. Information, Communication & Society 23, 6 (2020), 867–891.
[12] hiyouga. 2023. LLaMA Factory. https://github.com/hiyouga/LLaMA-Factory.
[13] Julie Jiang, Xiang Ren, Emilio Ferrara, et al. 2021. Social media polarization and echo chambers in the context of COVID-19: Case study. JMIRx med
2, 3 (2021), e29570.

Leveraging Large Language Models to Detect Influence Campaigns in Social Media 13
[14] Takeshi Kojima, Shixiang (Shane) Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. 2022. Large Language Models are Zero-Shot Reasoners.
In Advances in Neural Information Processing Systems , S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh (Eds.), Vol. 35. Curran
Associates, Inc., 22199–22213. https://proceedings.neurips.cc/paper_files/paper/2022/file/8bb0d291acd4acf06ef112099c16f326-Paper-Conference.pdf
[15] Quyu Kong, Pio Calderon, Rohit Ram, Olga Boichak, and Marian-Andrei Rizoiu. 2023. Interval-censored transformer hawkes: Detecting information
operations using the reaction of social systems. In Proceedings of the ACM Web Conference 2023 . 1813–1821.
[16] Shubham Kumar, Shivang Garg, Yatharth Vats, and Anil Singh Parihar. 2021. Content based bot detection using bot language model and bert
embeddings. In 2021 5th International Conference on Computer, Communication and Signal Processing (ICCCSP) . IEEE, 285–289.
[17] Luca Luceri, Ashok Deb, Silvia Giordano, and Emilio Ferrara. 2019. Evolution of bot and human behavior during elections. First Monday (2019).
[18] Luca Luceri, Silvia Giordano, and Emilio Ferrara. 2020. Detecting troll behavior via inverse reinforcement learning: A case study of Russian trolls in
the 2016 US election. In Proceedings of the International AAAI Conference on Web and Social Media , Vol. 14. 417–427.
[19] Luca Luceri, Valeria Pantè, Keith Burghardt, and Emilio Ferrara. 2023. Unmasking the Web of Deceit: Uncovering Coordinated Activity to Expose
Information Operations on Twitter. arXiv preprint arXiv:2310.09884 (2023).
[20] Muhammad Shahid Iqbal Malik, Tahir Imran, and Jamjoom Mona Mamdouh. 2023. How to detect propaganda from social media? Exploitation of
semantic and fine-tuned language models. PeerJ Computer Science 9 (2023), e1248.
[21] Humza Naveed, Asad Ullah Khan, Shi Qiu, Muhammad Saqib, Saeed Anwar, Muhammad Usman, Nick Barnes, and Ajmal Mian. 2023. A comprehensive
overview of large language models. arXiv preprint arXiv:2307.06435 (2023).
[22] Leonardo Nizzoli, Serena Tardelli, Marco Avvenuti, Stefano Cresci, and Maurizio Tesconi. 2021. Coordinated behavior on social media in 2019 UK
general election. In Proceedings of the International AAAI Conference on Web and Social Media , Vol. 15. 443–454.
[23] Gianluca Nogara, Padinjaredath Suresh Vishnuprasad, Felipe Cardoso, Omran Ayoub, Silvia Giordano, and Luca Luceri. 2022. The Disinformation
Dozen: An Exploratory Analysis of Covid-19 Disinformation Proliferation on Twitter. In 14th ACM Web Science Conference 2022 . 348–358.
[24] Alexander C Nwala, Alessandro Flammini, and Filippo Menczer. 2022. A General Language for Modeling Social Media Account Behavior. arXiv
preprint arXiv:2211.00639 (2022).
[25] OpenAI. 2023. ChatGPT [Large language model]. https://chat.openai.com.
[26] Diogo Pacheco, Alessandro Flammini, and Filippo Menczer. 2020. Unveiling Coordinated Groups Behind White Helmets Disinformation. In
Companion Proceedings of the Web Conference 2020 . ACM. https://doi.org/10.1145/3366424.3385775
[27] Archit Parnami and Minwoo Lee. 2022. Learning from Few Examples: A Summary of Approaches to Few-Shot Learning. arXiv:2203.04291 [cs.LG]
[28] Ashwin Rao, Fred Morstatter, Minda Hu, Emily Chen, Keith Burghardt, Emilio Ferrara, and Kristina Lerman. 2021. Political partisanship and
antiscience attitudes in online discussions about COVID-19: Twitter content analysis. Journal of medical Internet research 23, 6 (2021), e26692.
[29] Anna Sapienza, Sindhu Kiranmai Ernala, Alessandro Bessi, Kristina Lerman, and Emilio Ferrara. 2018. DISCOVER: Mining Online Chatter for
Emerging Cyber Threats. In Companion of the The Web Conference 2018 . International World Wide Web Conferences Steering Committee, 983–990.
[30] Akrati Saxena and Sudarshan Iyengar. 2020. Centrality measures in complex networks: A survey. arXiv preprint arXiv:2011.07190 (2020).
[31] Or Sharir, Barak Peleg, and Yoav Shoham. 2020. The Cost of Training NLP Models: A Concise Overview.CoRR abs/2004.08900 (2020). arXiv:2004.08900
https://arxiv.org/abs/2004.08900
[32] Karishma Sharma, Yizhou Zhang, Emilio Ferrara, and Yan Liu. 2021. Identifying Coordinated Accounts on Social Media through Hidden Influence
and Group Behaviours. In KDD ’21: Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery & Data Mining .
[33] Vishnuprasad Padinjaredath Suresh, Gianluca Nogara, Felipe Cardoso, Stefano Cresci, Silvia Giordano, and Luca Luceri. 2024. Tracking Fringe and
Coordinated Activity on Twitter Leading Up To the US Capitol Attack. InProceedings of the International AAAI Conference on Web and Social Media .
[34] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava,
Shruti Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton Ferrer, Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernandes, Jeremy Fu, Wenyin
Fu, Brian Fuller, Cynthia Gao, Vedanuj Goswami, Naman Goyal, Anthony Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Viktor
Kerkez, Madian Khabsa, Isabel Kloumann, Artem Korenev, Punit Singh Koura, Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Diana Liskovich,
Yinghai Lu, Yuning Mao, Xavier Martinet, Todor Mihaylov, Pushkar Mishra, Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy Reizenstein, Rashi
Rungta, Kalyan Saladi, Alan Schelten, Ruan Silva, Eric Michael Smith, Ranjan Subramanian, Xiaoqing Ellen Tan, Binh Tang, Ross Taylor, Adina
Williams, Jian Xiang Kuan, Puxin Xu, Zheng Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan, Melanie Kambadur, Sharan Narang, Aurelien Rodriguez,
Robert Stojnic, Sergey Edunov, and Thomas Scialom. 2023. Llama 2: Open Foundation and Fine-Tuned Chat Models. arXiv:2307.09288 [cs.CL]
[35] Xinyu Wang, Jiayi Li, Eesha Srivatsavaya, and Sarah Rajtmajer. 2023. Evidence of inter-state coordination amongst state-backed information
operations. Scientific reports 13, 1 (2023), 7716.
[36] Derek Weber and Frank Neumann. 2021. Amplifying influence through coordinated behaviour in social networks. Social Network Analysis and
Mining 11, 1 (2021), 1–42.
[37] Jason Wei, Maarten Bosma, Vincent Y. Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan Du, Andrew M. Dai, and Quoc V. Le. 2021. Finetuned
Language Models Are Zero-Shot Learners. CoRR abs/2109.01652 (2021). arXiv:2109.01652 https://arxiv.org/abs/2109.01652
[38] Kai-Cheng Yang, Emilio Ferrara, and Filippo Menczer. 2022. Botometer 101: Social bot practicum for computational social scientists. Journal of
computational social science 5 (2022), 1511–1528.
[39] Kai-Cheng Yang and Filippo Menczer. 2023. Anatomy of an AI-powered malicious social botnet. arXiv preprint arXiv:2307.16336 (2023).
[40] Ruosong Ye, Caiqi Zhang, Runhui Wang, Shuyuan Xu, and Yongfeng Zhang. 2023. Natural Language is All a Graph Needs. arXiv:2308.07134 [cs.CL]
