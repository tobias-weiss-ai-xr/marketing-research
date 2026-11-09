---
title: 'CFaiRLLM: Consumer Fairness Evaluation in Large-Language Model Recommender System'
url: https://doi.org/10.1145/3725853
category: consumer-behavior
subcategory: empirical
date: 2025-03
venue: ACM Transactions on Intelligent Systems and Technology
authors:
- Yashar Deldjoo
- Tommaso Di Noia
source: openalex-oa
pdf_url: https://arxiv.org/pdf/2403.05668
pages: 25
chars: 112114
fetched_at: '2026-11-08T17:03:12+00:00'
kb_version: 1
---

# CFaiRLLM: Consumer Fairness Evaluation in Large-Language Model Recommender System

CFaiRLLM: Consumer Fairness Evaluation in Large-Language Model
Recommender System
YASHAR DELDJOO, Politecnico di Bari, Italy
TOMMASO DI NOIA, Politecnico di Bari, Italy
This work takes a critical stance on previous studies concerning fairness evaluation in Large Language Model (LLM)-based
recommender systems, which have primarily assessed consumer fairness by comparing recommendation lists generated with and
without sensitive user attributes. Such approaches implicitly treat discrepancies in recommended items as biases, overlooking
whether these changes might stem from genuine personalization aligned with true preferences of users. Moreover, these earlier
studies typically address single sensitive attributes in isolation, neglecting the complex interplay of intersectional identities.
In response to these shortcomings, we introduce CFaiRLLM, an enhanced evaluation framework that not only incorporates
true preference alignment but also rigorously examines intersectional fairness by considering overlapping sensitive attributes.
Additionally, CFaiRLLM introduces diverse user profile sampling strategies—random, top-rated, and recency-focused—to better
understand the impact of profile generation fed to LLMs in light of inherent token limitations in these systems. Given that
fairness depends on accurately understanding users’ tastes and preferences, these strategies provide a more realistic assessment
of fairness within RecLLMs.
To validate the efficacy of CFaiRLLM, we conducted extensive experiments using MovieLens and LastFM datasets, applying
various sampling strategies and sensitive attribute configurations. The evaluation metrics include both item similarity measures
and true preference alignment considering both hit and ranking (Jaccard Similarity and PRAG), thereby conducting a multifaceted
analysis of recommendation fairness. The results demonstrated that true preference alignment offers a more personalized and fair
assessment compared to similarity-based measures, revealing significant disparities when sensitive and intersectional attributes
are incorporated. Notably, our study finds that intersectional attributes amplify fairness gaps more prominently, especially in
less structured domains such as music recommendations in LastFM. These findings suggest that future fairness evaluations in
RecLLMs should incorporate true preference alignment to ensure equitable and genuinely personalized recommendations.
Additional Key Words and Phrases: Consumer Fairness, Recommender Systems, Large Language Models, Bias Mitigation,
Evaluation Framework, User Profile Sampling
ACM Reference Format:
Yashar Deldjoo and Tommaso di Noia. 2025. CFaiRLLM: Consumer Fairness Evaluation in Large-Language Model Recommender
System. ACM Trans. Intell. Syst. Technol. 1, 1 (February 2025), 25 pages. https://doi.org/XXXXXXX.XXXXXXX
1 INTRODUCTION
Recently, recommender systems driven by large language models (RecLLM), such as ChatGPT, have received
substantial attention from the research community, becoming an important research area in the fields of Informa-
tion Retrieval (IR) and Recommender Systems (RS). These sophisticated neural architectures utilize billion-scale
parameters trained through supervised and semi-supervised methods on extensive internet data. They have shown
significant potential in various sectors and tasks, including but not limited to healthcare [34, 46, 48], finance [25, 59],
conversational assistants [3, 32, 41], and many more, see e.g., recent surveys [ 9, 17, 18, 66] for a good frame of
reference. Despite the witnessed benefits of using these systems in top-𝑘 recommendation setting [32, 51], there
are rising concerns about their inherent biases [12, 19, 22]. The vast and unregulated nature of the Internet data
used to train Large Language Models (LLMs) raises alarms about possible biases against specific races, genders,
popular brands, and other sensitive attributes that could be encoded in these networks. For example, if an LLM is
predominantly trained on data from popular e-commerce sites, it might disproportionately recommend products
Authors’ addresses: Yashar Deldjoo, deldjooy@acm.org, Politecnico di Bari, Via Amendola 126/B, Bari, Italy, 70126; Tommaso di Noia,
deldjooy@acm.org, Politecnico di Bari, Via Amendola 126/B, Bari, Italy, 70126.
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that
copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page.
Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy
otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from
permissions@acm.org.
© 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM 2157-6904/2025/2-ART
https://doi.org/XXXXXXX.XXXXXXX
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.
arXiv:2403.05668v3  [cs.IR]  20 Feb 2025

2 • Yashar Deldjoo, and Tommaso di Noia
from more recognized brands, overlooking niche or emerging brands. Similarly, biases in language around gender
or race could skew recommendations in subtle but impactful ways. Hence,unchecked employment of these systems
in commercial RS may lead to unfair treatment of minority groups with societal impacts, such as reinforcing
existing stereotypes or exacerbating economic disparities.
Recent studies [17, 38, 62? ] highlight that recommender systems can harness Large Language Models (LLMs) in
three key ways: (i) as the core recommender, (ii) as a means of data augmentation, incorporating rich semantic
representations from textual data, and (iii) as simulators to refine system’s predictions. Our work focuses on the
first application, wherein an LLM provides personalized recommendations, given a textual query provided by the
user, in the form of a prompt. In such a case, users indicate their preferences through textual prompts, such as
requesting movie suggestions based on their recent views, e.g., "Based on the movies I have recently watched: Blade
(1998) (Genres: Action|Adventure|Horror), and Four Weddings and a Funeral (1994) (Genres: Comedy|Romance), please
provide me with 3 movie recommendations. " Utilizing their deep understanding of context, user preferences, and
an extensive knowledge base, LLMs can propose relevant movie suggestions. These recommendations are then
verified against the existing catalog to ensure availability before being presented to the user.
Building upon our focus on employing LLMs for personalized recommendations, our research particularly
emphasizes the fairness of RecLLMs. We can examine the broad literature and taxonomies presented in FairRS
from two perspectives: (i) evaluation and (ii) system design. Regarding the former evaluation perspective, the
literature on FairRS identifies numerous noteworthy dimensions. These include the stakeholder perspective
(consumer vs. producer), the nature of benefits being examined (effectiveness or exposure), the level of fairness
(individual or group), and the core definition of fairness, among others [1, 26]. This focus contrasts with the system
perspective, which concentrates on the core recommendation model. In contrast, from a system perspective – i.e.,
which core recommendation model is being employed —, a notable observation in the FairRS literature is that they
primarily investigate so-called conventional/traditional models, based on collaborative filtering models such as
matrix-factorization (MF), or variations thereon NeuMF, LightGCN, rather than those based on Large Language
Models (LLMs). As shown in Table 1, only a limited number of studies [13, 22, 38, 65] have explored the fairness
aspects of RecLLMs, not least due to their relative novelty and recent development.
The research work by Li et al . [38] focuses on issues of producer fairness and personalization in RecLLMs,
specifically examining ChatGPT in the context of news recommendations. Other recent work such as [13] focuses
on the producer’s perspective, scrutinizing the impact of prompt engineering on system personalization, item
fairness, and the tendency of GPT-based RecLLMs to favor more recent, post-2000 movie recommendations. The
research carried out by Zhang et al. [65] forms the basis of our research, in which the authors study the fairness
of zero-shot GPT recommendations. Their work introduces an evaluation framework called FaiRLLM, designed
to assess fairness in Large Language Model recommendations (RecLLM), particularly focused on the consumer
side. This framework provides specialized evaluation metrics and datasets for evaluating fairness across various
sensitive user attributes in different recommendation scenarios, such as music and movies. Their evaluation of
ChatGPT using FaiRLLM reveals notable biases toward certain sensitive attributes, underscoring the need for
further investigation and mitigation of these biases.
Our study advances the discourse in FairRS/FairLLM by introducing an enhanced framework for assessing
“Consumer Fairness in RecLLMs ”, with a particular emphasis on two aspects: (i) the definition of unfairness
(whether through similarity alignment or true preference alignment), and (ii) the granularity of groups (considering
both individual and intersectional prompts). We also study the “user-profile construction” strategies, as well as the
scope of recommendations prompted in the aforementioned study.
Our research builds on and meticulously refines the foundational framework suggested by Zhang et al . [65],
enhancing its evaluation foundation and application in several key ways. Our approach notably expands upon
the methodology proposed by these researchers, which involves comparing the recommendations generated by
LLMs under neutral conditions to those produced when sensitive attributes are revealed. For example, when a user
requests movie recommendations without disclosing sensitive attributes (e.g., “Please recommend movies you think I
would enjoy.”), the RecLLM might offer a diverse selection based on the user’s past interactions. However, if the user
specifies a sensitive attribute such as age or gender (e.g., “As a woman interested in movies, please recommend... ”),
the existing FairLLM framework would compare the similarity of this personalized recommendation list with the
original, using such discrepancies to flag potential consumer unfairness. At first glance, this approach aligns with a
widely accepted notion of fairness, positing that system performance should remain consistent and must not vary
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

CFaiRLLM: Consumer Fairness Evaluation in LLM Recommender Systems • 3
User
RecLLM
Neutral
Sensitive attribute (Gender)
User
Ground truth
Items (mostly)
Dissimilar
Quality gap
UnFair!
Fair Rec
1. Ghostbusters (1984) - Genres: Comedy|Fantasy
2. The Shawshank Redemption (1994) - Genre: Drama
3. Blade Runner (1982) - Genre: Drama|Sci-Fi
4. The Terminator (1984) - Genres: Action|Sci-Fi
5. Die Hard (1988) - Genres: Action|Thriller
The user likes the movies:
1. Blade Runner (1982) - Genre: Drama|Sci-Fi
2. The Shawshank Redemption (1994) - Genre: Drama
3. When Harry Met Sally... (1989) - Genre:
Comedy|Romance
4. The Princess Bride (1987) - Genre:
Comedy|Romance
RecLLM
1. The Matrix (1999) - Action|Sci-Fi
2. The Truman Show (1998) - Genre: Drama|Sci-Fi
3. The Shawshank Redemption (1994) - Genre: Drama
4. Blade Runner (1982) - Genre: Drama|Sci-Fi
5. Jurassic Park (1993) - Genres:
Action|Adventure|Sci-Fi|Thriller
Fair!
Intersectional attribute
User
True Pref.
  Similar
Fair!
RecLLM
1. Ghostbusters (1984) - Genres: Comedy|Fantasy
2. The Terminator (1984) - Genres: Action|Sci-Fi
3. Die Hard (1988) - Genres: Action|Thriller
4. Jurassic Park (1993) - Genres:
Action|Adventure|Sci-Fi|Thriller UnFair!
True Pref
Dissimilar
Items (mostly)
Similar
The user likes the genres (Comedy, Action) in the
years (1977 to 1998).
Based on the user's preferences for movies blade
(1998) (Genres: Action|Adventure|Horror, Rating: 5/5),
four weddings and a funeral (1994) (Genres:
Comedy|Romance, Rating: 5/5)
recommend k movies that the user will enjoy.
The user is Female. She likes the genres (Comedy,
Action) in the years (1977 to 1998).
Based on the user's preferences for movies blade
(1998) (Genres: Action|Adventure|Horror, Rating: 5/5),
four weddings and a funeral (1994) (Genres:
Comedy|Romance, Rating: 5/5)
recommend k movies that the user will enjoy.
The user is Teen and Female. She likes the genres
(Comedy, Action) in the years (1977 to 1998).
Based on the user's preferences for movies blade
(1998) (Genres: Action|Adventure|Horror, Rating:
5/5), four weddings and a funeral (1994) (Genres:
Comedy|Romance, Rating: 5/5)
recommend k movies that the user will enjoy.
Fig. 1. In the left figure, we showcase CFaiRLLM’s fairness evaluation in movie recommendations, comparing recommendation
similarity across sensitive (gender, age) and intersectional attributes to a neutral standard, emphasizing user preferences. Our
aim is equity, ensuring that sensitive attribute recommendations align with neutral benchmarks. The right details the sensitive
attributes explored.
based on sensitive attributes. Building upon this principle, the authors applied their framework to both music and
movie recommendations and identified numerous biases.
However, this approach presents certain limitations. First, the most crucial limitation is the presumption that
difference in recommendations inherently means unfairness, overlooking the possibility that such differences could
simply represent “personalization”, which is not inherently negative. Their methodology equates the disparity in
recommendation lists with fairness issues without scrutinizing the preference alignment gap – that is, whether the
recommendations accurately reflect the user’s actual preferences. Second, the framework gauges fairness based on
a single sensitive attribute class (e.g., gender or age group) in isolation, and overlooks the complexity of overlapping
identities. For example, a user known for favoring action movies receives a list of high-octane films like “Mad Max:
Fury Road” and “John Wick” in response to a generic prompt. However, when the prompt includes intersectional
features, such as “I am a middle-aged woman looking for good movies to watch, ” the system’s recommendations
shift toward stereo-typically gender- and age-associated films such as “Under the Tuscan Sun” and “Eat Pray
Love. ” If the user however adds only her gender to the prompt: “I am a woman interested in great movies. ” The
recommendations shift significantly, leaning towards movies like “Little Women, ” “Pride and Prejudice, ” and “The
Help, ” reflecting astereotypical assumption about gender-specific preferences. Overall, these examples and ideas
reveal a preference alignment gap where the personalization is skewed by demographic assumptions rather than
the user’s demonstrated taste for movies.
Example. In our CFaiRLLM framework depicted in Figure 1, we conduct an in-depth examination of recommen-
dation fairness by contrasting the impact of single sensitive with intersectional prompts. Let us consider a user
profile with a history of enjoying Comedy and Action movies from the period of 1977 to 1998.
• Gender-based Prompt. When the user’s gender is considered, RecLLM modifies the recommendation set. For
a female user, the system might recommend The Matrix (1999), The Truman Show (1998) , The Shawshank
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

4 • Yashar Deldjoo, and Tommaso di Noia
Redemption (1994), Blade Runner (1982) , and Jurassic Park (1993) which despite being high-quality movies
within the action and drama genres, they are (mostly) different from those given without considering gender.
This change is deemed unfair according to [65] for relying on gender-based assumptions rather than actual
interests. In contrast, we argue this recommendation is fair because both gender-specific and neutral prompts
yield only two movies, The Shawshank Redemption (1994) and Blade Runner (1982), that aligns with ground
truth. In other words, both gender-specific and neutral prompts share one commonaccurate recommendation
(Blade Runner), indicating no unfair advantage (here benefit is equal to proving better recommendation in
terms of relevance/quality).
• Intersectional-Prompt. When a user’s identity includes both Teen and Female sensitive attributes, RecLLM
changes its recommendations to reflect this intersectionality. The system suggests movies such asGhostbusters
(1984), The Terminator (1984), and Die Hard (1988), and Jurassic Park (1993), which closely resemble those
from a neutral recommendation. However, the recommendations tailored to these sensitive attributes do not
match any items in the ground truth, unlike the neutral recommendations, which include two items from the
ground truth. Consequently, despite the previous approach, in our work this system is considered unfair, as
it appears to favor the neutral recommendations by providing a more accurate reflection of user preferences.
The core insight behind our framework evaluates fairness by examining if the recommendations are truly
personalized or if they are biased by stereotypes associated with the sensitive attributes. For example, if the
intersectional approach yields recommendations for movies, which may align with stereotypical views of teen
girls’ preferences, the framework would flag this as potentially unfair. The fairness is adjudged by the degree to
which the recommendations align with the user’s actual, demonstrated preferences—such as their affinity for action
comedies from the late 20th century—regardless of their gender or age.
1.1 Contributions.
Our work offers the following list of contributions:
(1) Introduction of an Enhanced Evaluation Framework for Consumer Fairness in RecLLMs. Our work
improves the research on FairRS in RecLLMs by proposing, CfaiRLLM, a more detailed framework that
evaluates consumer fairness with an emphasis on the true alignment of recommendations when measur-
ing benefits in RS. This includes the analysis of intersectionality, or more precisely intersectional prompts,
encompassing overlapping groups.
(2) Investigation of Intersectional Prompts in RecLLMs. This work highlights the role of overlapping
groups in group fairness research specifically within RecLLMs. It studies how combining multiple sensitive
attributes (e.g., gender and age) with intersectional prompts affects recommendation fairness.
(3) Enhanced Understanding of Unfairness Through User Profile Sampling Strategies.Our work proposes
a suite of different user profile sampling strategies (‘random’, ‘top-rated’, ‘recent’), with the goal to study how
these strategies influence the fairness of recommendations. This contribution is essential within RecLLM
research for developing more equitable recommender systems that mitigate bias.
Our work designs and studies the impact of the following strategies through the course of experiments.
• Random Sampling: Examining the fairness and relevance of recommendations when a random set of movies
from the user’s history is used to generate new recommendations.
• Top-Rated Sampling: Analyzing how using the user’s top-rated movies to generate recommendations affects
the alignment with their preferences and potential biases.
• Recent Sampling: Investigate the impact of prioritizing movies most recently watched or rated by the user
on the fairness and relevance of recommendations.
(4) Comparison with Existing Work. The research builds upon and refines the foundational framework
suggested by Zhang et al. [65], enhancing its evaluation foundation and application. It provides a comparative
analysis that not only acknowledges the contributions of prior work but also identifies and addresses its
limitations.
In essence, the fairness of RecLLM recommendations is determined not just by the presence of similarity but by
the depth of alignment with the users’ true preferences. Our framework seeks to ensure that recommendations are
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

CFaiRLLM: Consumer Fairness Evaluation in LLM Recommender Systems • 5
fair and personalized, moving beyond stereotypes.
Note. As illustrated in Figure 1, one might question whether simply designing an LLM-based recommender system
to strip gender (or other sensitive attribute) terms from queries would effectively solve the problem. To answer this
quesry, we provide the following viewpoints:
• Users may not always use explicit phrases to convey their identity, but their interactions and preferences
can implicitly reflect sensitive attributes. By incorporating sensitive attributes in our prompts, we aim to
simulate scenarios where user identity influences recommendations, either explicitly or implicitly.
• In real-world applications, users exhibit a wide range of behaviors in how they express their preferences.
Some users might naturally include identity-related information in their queries to receive more tailored
recommendations. Our framework accounts for this diversity by evaluating how such expressions can surface
or mitigate biases.
Overall, even if explicit mentions of sensitive attributes are rare, biases can still permeate through the data and
influence recommendations in subtle ways. These considerations aim to ensure that our CFaiRLLM framework
provides a broader assessment of fairness, taking into account both overt and nuanced impact of sensitive attributes
on recommendation outcomes.
2 RELATED WORK
In this section, we briefly review some related work on recommendation systems and LLM techniques.
2.1 Fairness in Recommender Systems
In examining the landscape of FairRS research, we can categorize the literature along several dimensions: the
stakeholder focus, the core recommender system model , the dynamics of fairness evaluation , and the granularity of
fairness with respect to group and individual distinctions [19]. Table 1 provides an overview of how different papers
are categorized by stakeholder focus—consumer or producer— and RS models, whether traditional or employing
recent RecLLM advances. This table further elucidates the attributes used to operationalize fairness considerations
from both consumer and producer standpoints, underlining the relative scarcity of research focusing on RecLLMs
within the FairRS domain. Table 2 instead provide an additional discourse by underscoring the technical nuances
of fairness evaluation, differentiating between static and dynamic methodologies. It highlights the dominance
of group and static evaluations in the current literature, pointing to potential areas for further investigation and
development.
2.1.1 Core RS models and Stakeholder. In the current landscape of recommender systems (RS), in particular, on
FairRS, we observe a clear division between traditional models and those enhanced by recommendation-centric
large language models (RecLLM). Traditional RS principally operates on collaborative filtering (CF) mechanisms,
potentially supplemented by auxiliary user and item side information. These systems have been the subject of
numerous studies aimed at developing benchmarks for fairness evaluation and strategies for bias mitigation, as
studied in depth in [ 19, 26]. Traditional RS models serve as the backbone of recommendation systems, albeit
without the intricate natural language processing capabilities endowed by large language models (LLMs). The
‘RecLLM’ paradigm represents an innovative frontier in AI and RS research [35, 35]. Here they refer to models
that integrate complex NLP methods, such as those derived from GPT-like architectures, into the recommendation
process. While this integration promises enhanced personalization and a refined recommendation experience by
comprehending user nuances, it simultaneously poses the risk of inheriting and perpetuating biases present in
the extensive and unfiltered data used for LLM training. Concerns are particularly pronounced regarding biases
related to race, gender, and brand recognition, which could result in unbalanced exposure for emerging entities or
products. Consequently, a fundamental aspect of our ongoing research is the precise quantification of these biases,
setting the stage for the formulation of strategies that can effectively neutralize the inadvertent propagation of
these biases through (advanced) RecLLM systems.
In summary:
• Traditional RS. In ‘traditional RS’, the focus frequently lies on collaborative filtering (CF) algorithms that
utilize historical datasets within a train-predict paradigm, occasionally supplemented by user and item
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

6 • Yashar Deldjoo, and Tommaso di Noia
Table 1. Mapping of research papers to core models and stakeholder fairness. ✓** positions our work within the FairRS
literature.
Category attributes Core RS Model Stakeholder
Traditional RecLLM Consumer Producer CP Fairness
[31, 40, 61] consumer activity ✓ ✓
[1, 14, 27, 57, 58] consumer demographics ✓ ✓ [53, 65] ✓✓* ✓✓*
[30, 54] consumer merits ✓ ✓
[42, 56] other consumer attributes ✓ ✓
[10, 24, 28, 67] producer/item popularity ✓ ✓ [13, 39] ✓ ✓
[5, 36] producer demographics ✓ ✓
[7, 14, 44, 52] price/brand/location ✓ ✓
[8, 23, 45, 49, 50, 60] variate CP attributes ✓ ✓
metadata. Although these systems operate effectively, they lack the advanced natural language processing
(NLP) capabilities seen in large language models (LLMs). Research work in this area are dedicated to enhancing
frameworks for evaluating fairness and formulating strategies to mitigate biases inherent in these models.
For example, Hao et al. [31] tackle the issue of unfair discrimination by CF due to imbalanced data, proposing a
multi-objective optimization approach that seeks a Pareto optimal solution to balance subgroup performance
without sacrificing overall accuracy. Farnadi et al . [27] address inherent biases by introducing a hybrid
fairness-aware recommender system that merges multiple similarity measures and demographic information
to mitigate recommendation biases. Naghiaei et al . [45] highlight the two-sided nature of recommender
systems and present a re-ranking approach that integrates fairness constraints for both consumers and
producers, showcasing the algorithm’s ability to improve fairness without diminishing recommendation
quality. Lastly, Wan et al . [56] investigate the bias induced by marketing strategies in CF systems and
propose a framework that enhances fairness across different market segments, achieving more equitable
recommendation performance.
• RecLLM. These model address the integration of language models with RS, signifying a shift towards using
NLP techniques to refine the accuracy and pertinence of recommendations. Research in this domain is not
limited to the application of LLMs for classical top-𝑘 recommendation tasks but also extends to applications
such as conversational recommendation systems, personalized explanation generation, and multi-modal
recommendation scenarios.
For instance, Shen et al . [53] examine the unintended biases in language model-driven Conversational
Recommendation Systems (CRSs), showing how biases can influence the category and price range of recom-
mendations, and offer mitigation strategies that preserve recommendation quality. Li et al. [39] study the
application of ChatGPT in personalized news recommendation task and find that the system is sensitive
to input phrasing and signal the challenges in achieving provider fairness and fake news detection. They
suggest that ongoing, dynamic evaluation of ChatGPT’s recommendations is crucial for understanding and
improving its performance in real-world tasks. Another study by Zhang et al. [65] introduces the FaiRLLM
benchmark, as pointed out earlier, specifically designed to evaluate the fairness of recommendations produced
by RecLLM systems, highlighting the biases these models exhibit against certain sensitive user attributes in
music and movie recommendations. Recently, Deldjoo et al. [13] investigate prompt design strategies within
ChatGPT-based RecLMMs and assess their effect on recommendation quality, and provider fairness. They
find that assigning system role can mitigate popularity bias and enhance fairness, suggesting that combining
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

CFaiRLLM: Consumer Fairness Evaluation in LLM Recommender Systems • 7
these strategies with personalized models could lead to a more balanced recommendation experience. These
examples underscore the evolving nature of RS technology and the importance of considering biases and
fairness in the development of RecLLM systems.
In general, the comparison of these two RS methodologies in Table 1 highlights a critical moment in the evolution
of RS, where the quest for superior personalized recommendations must be meticulously weighed against the
essential need for fairness and other harms in every facet of the recommendation process.
2.1.2 Stakeholder Considerations. Earlier discussions have established the importance of market orientation in
classifying the corpus of group fairness research—whether they address concerns from the consumer perspective,
the provider’s angle, or a combination of both. In delineating these categories, literature often focuses on certain
sensitive attributes such as consumer demographics (including age and gender) and producer-related attributes
such as item popularity.
• Consumer Fairness. Research in this area aims to ensure equitable recommendations for consumers, where
fairness is typically measure based on the relevance (or effectiveness) of recommendations for user groups,
e.g., demographic groups. Typically, as illustrated in Table 1, consumer level of activity (e.g., active vs. inactive
users), demographics, or other metrics (e.g., education) are utilized to identify protected groups.
• Producer Fairness. This aims to achieve fairness for content or product creators within the recommender
system. Fairness could be measured at the item level (e.g., popularity of items) or the producer level (such as
artists, authors, brands), with popularity or recognition of artists/brands as examples. In technical terms,
a producer can be seen as a higher-level grouping of items. Several attributes have been used, including
popularity, demographics, and price/brand/location.
• CP Fairness. This encompasses research that considers both consumer and producer fairness, endeavoring
to achieve a balanced approach.
Positioning the current work. While fairness in traditional recommendation systems is well-established, we
observe a scarcity of research on fairness in LLMs. The present study seeks to address this gap by focusing
on evaluating fairness and biases within RecLLMs. Our attention is particularly drawn to the consumer aspect
of RecLLMs, building upon and refining previous works, especially since significant research has already been
conducted on demographics from the consumer perspective. However, we also aim to propose a similar framework
for the producer side and eventually explore a combined approach that integrates both consumer and producer
perspectives. Our work also addresses the static aspects of fairness in recommender systems, as shown in Table 2.
The purpose of presenting this table is to highlight the ample opportunities for further research in this field.
Table 2. Research papers classification by granularity and longitudinal criteria. * positions our work.
Static Dynamic
Individual [7, 43, 65] [23, 67]
Group [1, 13, 14, 31, 53, 58, 61]* [7, 8, 23, 28, 44]
2.2 Leveraging Pre-trained LMs and Prompting for Recommender Systems
The integration of natural language processing (NLP) techniques within RS, underscores the major role of LLMs in
enhancing recommendation accuracy through deep semantic understanding. For instance, Hou et al. [33] utilize
natural language descriptions and tags as inputs into LLMs to create user representations for more effective
recommendations. This contrasts with the narrative-driven recommendations [4] that rely on verbose descriptions
of specific contextual needs.
Regarding the evolution of prompting strategies, initial attempts often employed few-shot learning [6], guiding
LLMs using exemplary cases to refine task-specific outcomes. Through the progress of prompt learning, tasks
are adapted to align with LLM capabilities, rather than adapting LLMs to tasks, employing either discrete or
continuous/soft prompts to improve performance across various tasks. This strategy has demonstrated effectiveness
across a range of tasks, including recommendation tasks.
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

8 • Yashar Deldjoo, and Tommaso di Noia
At the core of these advances lies the personalization of LLMs for recommendation purposes. The P5 frame-
work [29] and its iterations, such as OpenP5 [ 63], showcase the integration of multiple recommendation tasks
into a unified LLM framework using personalized prompts. This approach reformulates recommendation tasks
as sequence-to-sequence generation problems, showing the adaptability of LLMs to various recommendation
contexts and emphasizing the importance of capturing user intent and personalized needs. Furthermore, exploring
prompt transfer techniques, such as SPoT [55] and ATTEMPT [2], represents a major step in applying the learned
knowledge from source tasks to target recommendation tasks. These methodologies, together with knowledge
distillation techniques, contribute significantly to the development of more efficient and effective LLM-based
recommendation models. They underscore the potential for intra-task prompt distillation and cross-task prompt
transfer, enhancing the efficiency and effectiveness of LLM-based recommendation models.
In sum, the integration of LLMs into recommender systems represents a paradigm shift towards leveraging
advanced NLP and innovative prompting strategies for delivering highly personalized and contextually rich
recommendations. These developments promise to reshape the landscape of recommender systems, making them
more adaptable, intuitive, and user-centric.
3 PROPOSED EVALUATION FRAMEWORK
The integration of Large Language Models (LLMs) into recommendation systems (RecLLMs) has underscored
the critical need for a thorough evaluation of fairness in the recommendations provided to users. We introduce
CFairLLM, a rigorous framework specifically designed to assess the fairness of RecLLMs from a consumer
perspective. This framework is an extension and enhancement of the FaiRLLM benchmark, originally proposed
by Zhang et al. [65]. It refines the conceptualization of fairness and systematically addresses the limitations inherent
in the FaiRLLM framework.
3.1 CFairLLM: Consumer Fairness Evaluation RecLLM
3.1.1 Fairness Definition. The concept of consumer fairness in our CFairLLM framework is predicated on the
impacts of sensitive attributes on the outcomes produced by RecLLMs. We use the original definition proposed
by [65] maintaining its original phrasing and intent.
According to Zhang et al. [65]:
Given a sensitive attribute (e.g., gender) of users, fairness of RecLLM on the consumer-side could be defined
as “the absence of any prejudice or favoritism toward user groups with specific values (e.g., male vs. female) of
the sensitive attribute when generating recommendations without using such sensitive information. ”
This definition essentially emphasizes the importance of treating user groups equally in the process of generating
recommendations, regardless of their values for sensitive attributes.
3.1.2 Limitations and Our Contributions. Our work builds on the established definition to highlight that prejudice
originates from the nature and distribution of benefits between user groups. We propose to evaluate fairness in
terms of the alignment between recommendations and users’ actual preferences. Unlike previous studies, such
as that of Zhang et al. [65], which assess fairness by comparing the results of recommenders with and without
sensitive data, we argue that fairness should be measured by the consistency of the benefits across different user
groups, defined by their true preferences.
In other words, the approach by [ 65], which focuses on the similarity between the ranking lists, might not
capture the full picture. Differences in recommendations can arise from personalization or stereotypes that affect
fairness. Our approach emphasizes understanding users’ genuine preferences to accurately assess fairness, moving
beyond mere list comparison to consider the actual benefits to users.
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

CFaiRLLM: Consumer Fairness Evaluation in LLM Recommender Systems • 9
Example 1. Imagine a movie streaming service designed to suggest films to its platform users, recom-
mending romantic or classical movies to females and action or sci-fi movies of a more recent vintage to
males, based on the stereotype that gender predicts movie taste. This stereotype can misalign with the true
preferences of users, as there may be a noteworthy number of females who like recent sci-fi movies. The
recommendation system, in this case, is unfair because it aligns its recommendations with stereotypes
rather than users’ true preferences. An ideal, fair system would align its recommendations with the actual,
diverse tastes of its users, regardless of their gender.
Furthermore, our framework introduces a nuanced consideration of “intersectional fairness, ” [19, 64] recognizing
that individuals may have multiple overlapping identities that can influence recommendation outcomes. For
example, a prompt that includes both ‘gender’ and ‘age’, such as “I am a Young Adult Woman, based on movies I
watched, recommend me𝑘 movies that I like. ”, requires a response that accounts for this intersection of attributes
(i.e., gender ‘woman’, and age ‘Young’), rather than focusing on a singular demographic attribute (e.g., gender
alone).
Example 2. Consider now an enhanced movie streaming service that integrates intersectional consid-
erations into its recommendation algorithms. This service understands that a user’s preferences cannot
be accurately predicted by a single demographic attribute, such as gender. Therefore, when a user who
identifies as a young adult woman interacts with the platform, the system extends beyond just suggest-
ing romantic movies. Instead, it explores a wider category of genres, including thrillers, documentaries,
and science fiction, acknowledging her intersectional identity. This approach tailors recommendations to
intersect her age group (young adult) and gender (female) with her user profile.
We discuss each of the above dimensions in Section 3.2 (prejudice and favoritism) and Section 3.3 (intersectional-
ity). For a detailed definition, please refer to Section 3.4.3.
3.2 Definition of Rankers and Benefits
For the purpose of fairness evaluation, we define two ranking lists provided by two different Large Language Model
Recommendation Models (RecLLMs) to assess fairness and bias within our CFairLLM framework:
• Neutral Ranking List (R𝑚): This list is generated by a RecLLM that operates without any explicit knowl-
edge of sensitive attributes (such as gender, age, ethnicity, etc.). The aim is to simulate a scenario where
recommendations are made purely based on user preferences and interactions, without bias or modification
influenced by sensitive demographic factors. This list serves as our baseline for fairness, reflecting the model’s
unbiased recommendations.
• Sensitive Attribute-Influenced Ranking List (R𝑎 𝑚): Contrary to the neutral list, this ranking is produced
by a RecLLM that incorporates sensitive attributes (the sensitive attribute here is denoted by 𝑎) into its
recommendation process. The intention here is to observe how the inclusion of such attributes affects the
recommendation outcomes. By comparing this list to the neutral ranking list, we can quantify the impact
of sensitive attributes on the fairness of recommendations, identifying potential biases introduced by their
consideration.
The core concept of fairness within the CFairLLM framework, as discussed in Section 3.2, is based on the we
define as benefit and prejudice. To facilitate analysis, we identify two particular types of benefits, represented by
the variableB, which represent the main metrics for comparison and evaluation of fairness in our framework.
(i) Alignment of Information Items (B𝑖𝑡𝑒𝑚 ): This metric assesses the consistency of recommended items
across (R𝑚,R𝑎 𝑚), i.e., the neutral and sensitive attribute-influenced ranking lists. The principle here, derived
from the work of [65], posits that the fairness of a recommendation system is compromised if the inclusion of
sensitive attributes leads to a significant change in thecomposition of the top-𝑘 recommendation list. Essentially,
this benefit measures the disparity in recommendations, whether any items are unduly favored or omitted,
when sensitive attributes are taken into account, treating such disparities as indicators of potential bias.
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

10 • Yashar Deldjoo, and Tommaso di Noia
(ii) True Preference Alignment (B𝑝𝑟𝑒𝑓 ): The notion of benefit introduced in this study is mainly examined
through the lens of user preference, rather than simply comparing the similarity of recommendation lists. It
assesses the extent to which the recommendations from both ranking lists correspond with the users’ genuine
tastes and interests. Through this metric, we aim to guarantee that both neutral and sensitive attribute
rankers deliver equitable recommendation quality to users, regardless of the users’ sensitive attributes. Unlike
previous approaches, this measure depends on the ground-truth data of the target user.
By leveraging these benefits,B𝑖𝑡𝑒𝑚 andB𝑝𝑟𝑒𝑓 , our framework assesses the impact of sensitive attributes on
recommendation systems, seeking to maintain the integrity of recommendations by ensuring they are both reflective
of true user preferences and consistent across different user groups.
3.3 Independent vs. Intersectional Fairness
Fairness in recommendation systems, or more precisely group fairness, could be studied through the nuances lens
of the granularity of the sensitive attributes considered [16, 64], an aspect less explored in the recomemdner system
community. Let us consider𝐴∈A , a set of sensitive attributes (such as gender, age), where each element𝐴∈A
represents one specific category of attributes, (e.g., gender) with associated values that these attributes can take.
Our framework acknowledges the complexities of intersectional groups and the nuances involved in multiple
identities, balancing two principal approaches to fairness: independent groups, which focus on individual sensitive
attributes, and intersectional groups [64], which examine the overlapping features and combined effects of these
attributes. To formalize:
(1) Independent Groups : Independent groups are formed based on single sensitive attributes, each with
multiple potential values. For a given attribute 𝐴∈A with possible values{𝑎1,𝑎 2,...,𝑎 𝑛} (e.g., gender
with values male and female), the independent groups are defined as Gindep ={𝐺𝑎1,𝐺𝑎2,...,𝐺 𝑎𝑛}, where
𝐺𝑎𝑖 includes individuals with the attribute value𝑎𝑖. This approach simplifies the assessment of fairness by
focusing on one attribute at a time. For clarity, let us assume:
• Gender as an attribute with values{𝑎1 : Male,𝑎 2 : Female},
• Age as a separate attribute with its own set of values{𝑏1 : Teen,𝑏 2 : Young,𝑏 3 : Adult}. Here,𝑏𝑖 directly
corresponds to specific age ranges, illustrating the framework for categorizing individuals based on singular
sensitive attributes.
(2) Intersectional Groups: For intersectional analysis, we consider the combinations of values from multiple
attributes withinA. This is formalized as A𝑖𝑛𝑡 ={𝑎𝑖∩𝑏𝑗 | 𝑎𝑖 ∈ 𝐴,𝑏𝑗 ∈ 𝐵,𝐴,𝐵 ∈A ,𝐴 ≠ 𝐵}, leading
to intersectional groupsGinters ={𝐺𝑎1𝑏1,𝐺𝑎1𝑏2,...,𝐺 𝑎𝑛𝑏𝑚}, where each𝐺𝑎𝑖𝑏 𝑗 represents individuals with a
specific combination of attribute values from𝐴 and𝐵. This approach acknowledges the complex interplay of
multiple attributes in shaping individuals’ experiences and potential biases in recommendations.
Evaluating fairness across these dimensions is crucial for ensuring that RecLLMs deliver fair and unbiased
outcomes, addressing both the simplistic views of independent attributes and the complex realities of intersectional
identities.
3.4 Evaluation Method
This section describes our approach to evaluating the fairness of RecLLMs in generating (personalized) recom-
mendations. Our evaluation method leverages natural language processing to understand user preferences and
generate recommendations that are both sensitive and relevant to the user’s interests.
3.4.1 Data Format for User Instructions. RecLLMs interpret user preferences expressed in natural language, enabling
a personalized recommendation process in a zero-shot setting. Following the methodology similar to that described
in Zhang et al . [65] we employ and improve a structured template designed to capture individual preferences
alongside relevant sensitive attributes. This structure ensures a nuanced understanding of the user’s needs. The
templates are structured as follows:
(1) Sensitive Demographic Information. This optional statement, tested within (R𝑚) in our framework,
identifies user-protected characteristics-such as age, gender, or cultural background—that might influence
recommendations. It serves as the basis for defining and measuring unfairness. Examples of such statements
include “The user is female” (individual) or “The user is a Female Teen. ” (intersectional).
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

CFaiRLLM: Consumer Fairness Evaluation in LLM Recommender Systems • 11
(2) User Profile. It is constructed based on the incorporation of two modules: the passion profile and the item
consumption profile.
(a) Passion Profile. Considering the token length limitation for movie inclusions within ChatGPT, we design
a module named “passion profile generator” whose role is to create a narrative profile encapsulating
the user’s interests, often derived from their consumption history. An example of a passion profile state-
ment taken from a random user in our dataset is: “The user mostly likes the genres (Drama|Sci-Fi, Drama,
Comedy|Romance) in the years (1951 to 1997) ”.
(b) Actual Consumption Profile. This part provides more detailed context by detailing the genres or types of
items (e.g., movies) preferred/consumed by the user, incorporating their genre and year. For instance,
“Based on the user’s preferences for the movies ’Chariots of Fire’ (1981) (Genres: Drama, Rating: 5/5), ’Sabrina’
(1954) (Genres: Comedy|Romance, Rating: 5/5) ... ”. It should be noted that a major aspect of our contribution
includes the design and implementation of various qualitative profile construction strategies, which are
tested for this section. These strategies are discussed in detail in Section 3.4.2.
(3) Actual Demand Statement for Recommendations. This specifies the user’s request, often quantified by
the number of recommendations sought (denoted as𝐾), e.g., “... Please suggest a list of 10 movie titles that the
user will enjoy.”
Example Templates for Recommendation Requests. In light of the prompt structure detailed earlier, the
following scenarios exemplify how to leverage user profiles for personalized recommendations in RecLLMs. These
templates demonstrate applications both with and without sensitive attribute considerations, designated as (R𝑎 𝑚)
and (R𝑚) scenarios, respectively.
(1) Basic Instruction Template. “Passion Profile + Recommendation Request”: In this basic scenario, the RecLLM
exclusively leverages the user’s passion profile to formulate a recommendation request.
Basic Neutral Instruction Template (R𝑚)
“The user mostly likes the genres (Drama|Sci-Fi, Drama, Comedy|Romance) in the years (1951 to 1997).
Please suggest a list of 10 movie titles that the user will enjoy. ”
when incorporating sensitive information, the recommendation process adapts to account for this additional
context,
Basic Sensitive Instruction Template (R𝑎 𝑚)
“The user is Female. The user mostly likes the genres (Drama|Sci-Fi, Drama, Comedy|Romance) in the
years (1951 to 1997). Please suggest a list of 10 movie titles that the user will enjoy. ”
(2) Detailed Instruction Template. “Passion Profile + Items Consumption Profile + Recommendation Request”:
This scenario combines the user’s passion profile with their item consumption history to design a more
detailed recommendation request.
Detailed Neutral Instruction Template (R𝑚)
“The user prefers genres such as Drama, Sci-Fi, Drama, Comedy, and Romance, from the years
(1951 to 1997). Considering the user’s enjoyment of movies like ’Chariots of Fire’ (1981, Drama,
Rating: 5/5), ’Sabrina’ (1954, Comedy|Romance, Rating: 5/5), and ’E.T. the Extra-Terrestrial’ (1982,
Children’s|Drama|Fantasy|Sci-Fi, Rating: 5/5), recommend 10 movies that the user will enjoy. ”
similarly, as with the previous scenarios, this approach is also tested with the inclusion of sensitive information,
designating it as (R𝑎 𝑚).
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

12 • Yashar Deldjoo, and Tommaso di Noia
Sensitive Detailed Instruction Template (R𝑎 𝑚)
“The user, identified as Female, has preferences for genres such as Drama, Sci-Fi, Comedy, and Romance,
notably from the years (1951 to 1997). Taking into account the user’s sensitive attribute (Female) and
their fondness for films like ’Chariots of Fire’ (1981, Drama), ’Sabrina’ (1954, Comedy|Romance), and
others, recommend 10 movies that align with the user’s taste. ”
In our study, we evaluated the scenarios labeled as detailed neutral instruction and sensitive detailed instruction,
which correspond toR𝑚 andR𝑎 𝑚, respectively. It is important to highlight that we developed a suite of item profile
sampling strategies to select a manageable and meaningful representation of user interest, thereby addressing the
constraints presented by ChatGPT, as elaborated in Section 3.4.2.
Moreover, to consider a user characterized by an intersectional identity (e.g., a young adult female) with a passion
for action and drama movies from the years 2000 to 2020. The prompt generated might be:
“The user isYoung Adult Female. She mostly likes the genres (Drama|Sci-Fi, Drama, Comedy|Romance)
in the years (1951 to 1997). Considering the user’s sensitive attribute (Young Adult Female) and
preferences for the movies chariots of fire (1981) (Genres: Drama, Rating: 5/5), sabrina (1954) (Genres:
Comedy|Romance, Rating: 5/5), ... recommend 10 movies that align with the user’s taste. ”
This approach would enable us to audit whether recommendations change by merely incorporating sensitive
characteristics, which, in this context, could be interpreted as either personalization or unfairness, depending on if
and how they differ with respect to other groups.
3.4.2 Sampling Strategies for Item Profile Construction. The consumption history of an individual user might
encompass over 160 movies in the ML-1M dataset (see Table 3), making the inclusion of their entire viewing
history, including titles and genres, impractical (and redundant) frequently surpassing the model’s token limit.
This situation highlights a main challenge in design of prompt-based RecLLMs: how to select a representative subset
of movies to form a concise yet impactful user profile? . We have designed a suite of item profile sampling strategies:
random, top-rated, recent. These strategies are specifically engineered to efficiently extract user preferences from
users’ extensive consumption data. The main idea behind this step comes from the practical constraints imposed
by the token limitations of large language models (LLMs) such as ChatGPT. The proposed sampling strategies
are meticulously designed to sift through user consumption history, ensuring that personalization remains both
personalized and achievable within the confines of technical limitations.
(1) Random Sampling: This strategy offers a straightforward solution to bypass the token limit issue by ran-
domly selecting movies from a user’s history. This method selects a diverse yet unpredictable representation
of user preferences.
Example: If a user has watched over 160 movies, the random sampling might select “Inception” (2010, Sci-Fi),
“The Godfather” (1972, Drama), and “Finding Nemo” (2003, Animation), providing a broad glimpse into varied
interests.
(2) Top-Rated Sampling: This strategy prioritizes movies that the user has highly rated, under the assumption
that these selections best reflect their preferences. This approach efficiently utilizes limited tokens to capture
high-satisfaction items.
Example: For the same user, the top-rated sampling could highlight “Schindler’s List” (1993, Drama, Rating:
5/5) and “The Shawshank Redemption” (1994, Drama, Rating: 5/5), focusing on movies that are favored by
the user.
(3) Recent Sampling: Adding a temporal dimension, this strategy selects movies based on their recent interaction
timestamps. It assumes that the most recently rated or watched movies are more indicative of current interests,
making the recommendations timely and relevant. This approach is particularly useful for capturing evolving
tastes and offering up-to-date suggestions.
By incorporating these strategies, we aim to explore and test various scenarios that involve the issue of selecting
the most representative movies from a potentially voluminous history. For the sake of our experiments and given
the extensiveness of these analyses, we focused our attention on creating profiles that include a fixed number of
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

CFaiRLLM: Consumer Fairness Evaluation in LLM Recommender Systems • 13
items, specifically𝑁𝑝𝑟𝑜𝑓 = 10, for profile inclusion. This standardization across different sampling strategies allows
for a controlled comparison, ensuring that the influence of each strategy on the recommendation quality can be
accurately assessed.
3.4.3 Evaluation Procedure. The evaluation of the CFairLLM framework is designed to assess the fairness of
recommendations generated by RecLLMs with respect toboth independent and intersectional groups. Our procedure
comprises several steps, aimed at examining how well the system aligns with our fairness objectives through the
lenses of neutral and sensitive attribute-impacted rankings. The steps are as follows:
(1) Collect Neutral and Sensitive Recommendations : For each user instruction set𝐼𝑚, generate two distinct
sets of recommendations, where𝑚 is the index of instruction.
•R 𝑚: Obtain the top- 𝐾 recommendations from the neutral model, which does not consider sensitive
attributes.
•R 𝑎 𝑚 &R𝑎𝑏 𝑚 : Modify𝐼𝑚 to include sensitive attributes, forming sensitive instructions for both independent
({𝐼𝑎 𝑚}) and intersectional groups ({𝐼𝑎𝑏 𝑚}). Gather the top-𝐾 recommendations (R𝑎 𝑠 andR𝑎𝑏 𝑠 ) for each.
(2) Evaluate Similarity of Information Items (B𝑖𝑡𝑒𝑚 ): Measure the consistency in the recommended items
between the neutral (R𝑚) and sensitive attribute-influenced (R𝑎 𝑚) ranking lists. This step involves calculating
similarity metrics (e.g., Jaccard similarity, PRAG) to identify any significant disparities, indicating potential
bias.
(3) Assess True Preference Alignment (B𝑝𝑟𝑒𝑓 ): Compare the recommendations from bothR𝑚 andR𝑎 𝑚 (or
R𝑎𝑏 𝑚 ) against the user’s genuine preference profile. This step is crucial for ensuring that the recommendations
reflect the users’ actual interests and preferences, irrespective of the inclusion of sensitive attributes.
3.4.4 Evaluation Metrics. The evaluation of fairness in recommendations requires a diverse set of metrics that
reflect various aspects of the recommendation process. These metrics are categorized into two main parts: item
similarity, true preference alignment. and genre consistency/calibration.
Item Similarity. Metrics under this category assess the consistency of recommended items between the neutral
ranker and the sensitive ranker, without considering the ground truth preference.
• Jaccard Similarity at K (JS@K) : This metric is calculated as
𝐽𝑆 @𝐾 = 1 𝑀 𝑀∑︁ 𝑚=1 |R𝑎 𝑚∩R𝑚| |R𝑎𝑚∪R𝑚|, (1)
whereR𝑎 𝑚 andR𝑚 are the sets of top-K recommendations for the sensitive and neutral instructions, respec-
tively, and𝑆 is the number of instructions. Fairness is denoted as ΔJS, where higher values of𝐽𝑆 @𝐾 indicate
more fairness.
• PRAG* Metric: This similarity metric is formulated by adapting the Pairwise Ranking Accuracy Gap metric,
which accounts for the relative rankings between two items. Explicitly, the similarity between the neutral
and sensitive groups concerning the top-𝐾 recommendations by a Large Language Model is defined as:
𝑃𝑅𝐴𝐺∗@𝐾 = 1 𝐾(𝐾+ 1)𝑆 ∑︁ 𝑚 ∑︁ 𝑣1,𝑣2∈R 𝑎 𝑚
𝑣1≠𝑣2
(I(𝑣1∈R 𝑚))× I(𝑟𝑚,𝑣1 <𝑟𝑠,𝑣2)× I(𝑟𝑎 𝑚,𝑣1 <𝑟𝑎 𝑠,𝑣2), (2)
where I(·) retains the meaning as defined previously,𝑣1 and𝑣2 signify two distinct recommended items in
R𝑎 𝑚 and𝑟𝑚,𝑣𝑖 (or𝑟𝑎 𝑚,𝑣𝑖 ) symbolizes the rank of𝑣𝑖 inR𝑚 (orR𝑎 𝑚 respectively). In particular, if𝑣1 is not listed in
R𝑚, then𝑟𝑚,𝑣1 is set to+∞, and similarly for𝑣2. As elucidated by the formula, a higher metric value not only
demands a substantial overlap of items but also necessitates that the pairwise ranking sequence of any given
item relative to another must be congruent inR𝑚 andR𝑎 𝑚. This criterion enables us to gauge the concordance
of pairwise rankings between the recommendation outputs for both neutral and sensitive instructions.
3.4.5 True Preference Alignment. To enhance the evaluation of recommendation systems, we adapt the approach
proposed by Zhang et al. [65] to more model fairness in terms of how well recommendations align with users’ true
preferences. We leverage test data to refine the accuracy of our evaluation metrics. Specifically, we introduce two
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

14 • Yashar Deldjoo, and Tommaso di Noia
modified variables,R𝑚′ andR𝑚′𝑎, to denote the items within the recommendation lists that are favored by users,
obtained from their interactions in the test data. Consequently, this adjustment results in a comprehensive list of
refined recommendation lists.
•R 𝑚: The set of items recommended to a user𝑚 by the neutral ranker.
•R 𝑎 𝑚: The set of items recommended to the same user by the sensitive ranker.
•R ′ 𝑚: The subset of𝑅𝑚, filtered on the basis of the test data to include only those items that align with the
user’s true preferences.
•R ′𝑎 𝑚 : Similarly, the subset of𝑅𝑎 𝑚, filtered to include only items genuinely preferred by the user, as per the test
data.
In our evaluation of fairness based on true preference alignment, we employ the same metrics, Jaccard similarity
and the PRAG metric, as means of quantifying unfairness. Essentially, we focus our attention towards the changes
in high-quality items – favored by the target user– between two recommendation lists to flag the system as unfair.
Fairness Metrics. Similar to Zhang et al. [65], we propose two fairness metrics — Sensitive-to-Neutral Similarity
Range (SNSR) and Sensitive-to-Neutral Similarity Variance (SNSV), which quantify the unfairness level by measuring
the divergence of{Sim(𝑎)|𝑎∈𝐴} from different aspects.
• Sensitive-to-Neutral Similarity Range (SNSR): This metric measures the disparity in similarity scores
between the most advantaged and disadvantaged sensitive groups. Formally, for the top-𝐾 recommendations,
it is defined as:
𝑆𝑁𝑆𝑅 @𝐾 = max
𝑎∈𝐴
Sim(𝑎)− min
𝑎∈𝐴
Sim(𝑎),
where Sim(𝑎) denotes the average similarity score for the sensitive group𝑎, and𝐴 represents the set of all
possible values of the studied sensitive attribute. A higher SNSR value indicates greater unfairness due to
larger disparities in similarity across groups.
• Sensitive-to-Neutral Similarity Variance (SNSV): This metric captures the variability in similarity scores
across all sensitive groups by computing the variance of Sim(𝑎). The formula for SNSV is:
𝑆𝑁𝑆𝑉 @𝐾 =
vut
1
|𝐴|
∑︁
𝑎∈𝐴

Sim(𝑎)− 1 |𝐴| ∑︁ 𝑎′∈𝐴 Sim(𝑎′) ! 2 ,
where|𝐴| denotes the total number of sensitive groups in𝐴. A higher SNSV value implies greater variability
in the similarity scores, reflecting higher levels of unfairness.
Both fairness metrics aim to assess the sensitivity of recommendations to different groups, with higher values
indicating greater disparities or inconsistencies.
3.5 Setup
3.5.1 Data. To evaluate the effectiveness of our recommendation systems, we utilized two widely recognized
datasets from different domains: ML-1M (movies) and LastFM-1K (music). These datasets were chosen because they
represent distinct domains and contain sensitive attributes, making them suitable for our analysis.
For ML-1M, we used users’ explicit movie ratings, while for LastFM-1K, we started with implicit feedback in the
form of user-song play counts. To make this dataset more similar to the movie domain, the implicit feedback was
converted to explicit feedback on a scale of 1 to 5, following the procedure proposed in [15, 37]. This conversion
ensured consistency in prompt construction and allowed for a more direct comparison between the two datasets.
We selected not to use the LastFM-360K dataset, as it is limited to artist-level interactions, whereas LastFM-1K
provides both artist and song-level data, making it better suited for our study. For each dataset, we partitioned the
data into training and testing sets using a temporal splitting strategy. Users’ own ratings or interactions were used
to construct their profiles in the training set, while the test set was reserved for evaluation. The statistics of the
final datasets are shown in Table 3.
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

CFaiRLLM: Consumer Fairness Evaluation in LLM Recommender Systems • 15
Table 3. Statistics of the datasets used in our work.
Dataset |U| |I| |R| Density (%) 𝑅 𝑈 𝑅 𝐼
ML-1M (train) 150 2,537 18,428 95.16 122.85 7.26
ML-1M (test) 150 1,590 4,023 98.31 26.82 2.53
LastFM-1K (train) 149 21,967 37,534 98.85 251.91 1.71
LastFM-1K (test) 150 7,308 9,460 99.14 63.07 1.29
Note: We used a temporal splitting strategy, so that train rat-
ings/interactions are only used for profile construction.
Given the complex nature of our experiments, each user in our dataset is exposed to various scenarios (in-
structions). These included evaluations with and without a sensitive attribute, alongside assessments employing
different user sampling strategies. This multi-faceted approach required overten distinct instructions per target user,
significantly increasing the communication and labor requirements when interfacing with OpenAI. To mitigate
these challenges and manage associated costs, a strategic sampling method was adopted, where we used a subset
of a representative group of 150 users from the dataset. For each user, we repeated the specified tasks, to make a
right balance between thoroughness and efficiency in our analysis.
3.5.2 Sampling Strategies and Sensitive Attributes. Our exploration of sampling strategies was comprehensive,
including options such as ‘random’, ‘top-rated’, ‘recent’, mentioned in Section 3.4.2 In parallel, we examined various
sensitive attributes to understand their impact on recommendation fairness. These attributes included ‘gender, ’
‘age group, ’ ‘intersectional’, and scenarios excluding sensitive attributes altogether.
3.5.3 NLP processing and databse search. In our methodology, we address the challenge of accurately searching
and identifying movie titles within a large catalog of movie database (with titles, genre, year).
After an initial text manipulation, we employ a regular expression-based approach to extract movie titles and
their respective release years from the structured text. This extraction process is designed to accommodate various
formats in which movie information might be presented, thereby enhancing the flexibility and robustness of our
method. The core of our search algorithm, similar to [22], utilizes the ‘difflib’ library,1 a Python module known
for its capability to perform sequence matching. ‘difflib’ enables us to find the best match for each movie title
within the database by comparing the preprocessed titles against the titles stored within the database. We apply
a threshold for match similarity to ensure a high degree of accuracy in the results. We performed a very similar
post-processing step for music data.
To accommodate the nuances of human language and potential discrepancies in movie title representations, our
methodology includes a step for converting all titles to lowercase and stripping any leading or trailing whitespace.
This normalization process ensures that the comparison between the input titles and the database is not hindered
by case sensitivity or extraneous characters. The outcome of this process is a list of matched titles, each associated
with its corresponding unique identifier within the database. This enables a seamless integration of the search
results with further analytical or recommendation-based processes, thereby contributing to the overall objective of
enhancing movie discovery and recommendation systems.
4 RESULTS AND DISCUSSION
Experimental Research Questions. Throughout this section, our objective is to answer the following set of
experimental research questions.
• RQ1: How does true preference alignment compare to similarity-based alignment in measuring fairness
within RecLLMs?
• RQ2: How do user profile sampling strategies impact fairness and accuracy in RecLLMs?
1https://docs.python.org/3/library/difflib.html
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

16 • Yashar Deldjoo, and Tommaso di Noia
• RQ3: How does the variability in consumer fairness measures differ across multiple RecLLM models and
datasets, and to what extent does the introduction of sensitive attributes—especially intersectional at-
tributes—amplify observed disparities in fairness?
• RQ4: How does increasing the scope of sampling strategies ( 𝑁 number of selected movies) impact the
computed similarities and fairness?
4.1 Answer to RQ1. How does true preference alignment compare to similarity-based alignment in
measuring fairness within RecLLMs?
Results for this RQ are summarized in Table 4, and Figure 2. The comparison between true preference alignment
(𝛽𝑝𝑟𝑒𝑓 ) and similarity-based alignment (𝛽𝑖𝑡𝑒𝑚 ) reveals distinct trade-offs in understanding and evaluating fairness
within RecLLMs. Overall, true preference alignment consistently results in lower similarity scores across all
sampling strategies and sensitive attribute groups, indicating a divergence between the two recommendation
approaches. For instance, under random sampling, the Jaccard similarity for the Sex category is 0.0313 for𝛽𝑝𝑟𝑒𝑓
compared to 0.1680 for𝛽𝑖𝑡𝑒𝑚 . Similarly, in the Age category, true preference alignment yields similarity scores of
0.0226 (Teen), 0.0199 (Young), and 0.0181 (Adult), markedly lower than their𝛽𝑖𝑡𝑒𝑚 counterparts of 0.1669, 0.1847,
and 0.1421 respectively. This reduction underscores that true preference alignment tailors recommendations more
closely to individual user interests, potentially enhancing personalized relevance at the expense of broader item
similarity.
Despite the lower similarity scores, true preference alignment demonstrates superior fairness as evidenced by
the SNSR and SNSV metrics. For example, under random sampling in the Sex category,𝛽𝑝𝑟𝑒𝑓 exhibits an SNSR of
0.0210 and SNSV of 0.0105, compared to𝛽𝑖𝑡𝑒𝑚 ’s SNSR of 0.0010 and SNSV of 0.0005. Although higher SNSR and
SNSV values generally indicate greater fairness discrepancies, the overall context suggests that true preference
alignment mitigates unfair biases by aligning recommendations more closely with genuine user preferences,
thereby promoting equitable treatment across different user groups. For instance, in all the tested scenarios, the
SNSR and SNSV values of𝛽𝑝𝑟𝑒𝑓 are consistently 3 to 10 times lower than those of𝛽𝑖𝑡𝑒𝑚 . For example, considering
SNSV across the Sex, Age, and Intersectional categories, the respective values are (0.0076 vs. 0.0318), (0.0179 vs.
0.0370), and (0.0305 vs. 0.0501). This highlights that, when fairness is assessed based on underlying norms and
the sensitive attributes at stake, true preference alignment demonstrates relatively lower levels of unfairness, a
discussion overseen in the findings of Zhang et al. [65].
A similar trend is evident in Figure 2 (compare the left and right panels). Switching to true preference alignment
reduces (in some case) the SNSR by approximately half (both for Jaccard and PRAG). This demonstrates that
emphasizing whether recommendations truly match user preferences significantly diminishes disparities across
different age groups.
Summary of Answer to RQ1.
In summary, true preference alignment in RecLLMs offers both more personalized and fairer recommen-
dations by closely aligning with individual user preferences, albeit at the expense of lower overall item
similarity. As hypothesized earlier in the paper, the perception of fairness and unfairness is significantly
influenced by the norms and values considered, as well as how these norms define and measure unfairness
[20].
4.2 Answer to RQ2. How do user profile sampling strategies and their scope impact fairness and
accuracy in RecLLMs?
When we examine fairness using SNSR (where lower is better) across different sampling strategies (e.g., random,
top-rated, recent) and metrics (e.g., Jaccard vs. PRAG), no single strategy consistently outperforms the others in all
scenarios, as shown in Figure 2. For instance, under item-level similarity (Jaccard), a random sampling strategy
often presents the lowest SNSR values, suggesting it excels in surface-level fairness. However, in ranking-based
scenarios (PRAG), random performs the worst across the three feature categories, indicating a lack of precision
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

CFaiRLLM: Consumer Fairness Evaluation in LLM Recommender Systems • 17
Table 4. Recommendation alignment between (R𝑚,R𝑎𝑚) based on Item Similarity𝛽𝑖𝑡𝑒𝑚 and True Preference Alignment𝛽𝑝𝑟𝑒𝑓 .
Detail results can be found in Appendix, Table 5 and 6.
Sim. Profile Sampling Sex Age Intersectional (Sex & Age)
𝑆𝑚𝑛 𝑆𝑓𝑛 SNSR↓ SNSV↓ 𝑆𝑡𝑛 𝑆𝑦𝑛 𝑆𝑎𝑛 SNSR↓ SNSV↓ 𝑆𝑚𝑡𝑛 𝑆𝑚𝑦𝑛 𝑆𝑚𝑎𝑛 𝑆𝑓𝑡𝑛 𝑆𝑓𝑦𝑛 𝑆𝑓𝑎𝑛 SNSR↓ SNSV↓
Jaccard
(𝛽𝑖𝑡𝑒𝑚)
random 0.1680 0.1670 0.0010 0.0005 0.1669 0.1847 0.1421 0.0426 0.0175 0.2047 0.1532 0.1630 0.1794 0.1256 0.0965 0.1082 0.0351
top-rated 0.6760 0.6125 0.0635 0.0318 0.5773 0.6548 0.6565 0.0793 0.0370 0.4734 0.5905 0.6021 0.5355 0.5297 0.4743 0.1288 0.0501
recent 0.6344 0.5920 0.0424 0.0212 0.5918 0.6556 0.6157 0.0639 0.0263 0.5499 0.6004 0.6065 0.4623 0.5675 0.4741 0.1442 0.0566
(𝛽𝑝𝑟𝑒𝑓)
random 0.0313 0.0103 0.0210 0.0105 0.0226 0.0199 0.0181 0.0045 0.0019 0.0342 0.0222 0.0325 0.0317 0.0159 0.0000 0.0342 0.0120
top-rated 0.0681 0.0529 0.0152 0.0076 0.0919 0.0481 0.0688 0.0437 0.0179 0.0919 0.0497 0.0744 0.1063 0.0567 0.0125 0.0938 0.0305
recent 0.0461 0.0375 0.0086 0.0043 0.0658 0.0445 0.0362 0.0296 0.0125 0.0825 0.0350 0.0358 0.0159 0.0398 0.0250 0.0666 0.0210
when ranking is considered. In these ranking scenarios, top-rated and recent strategies demonstrate stronger
performance, offering better alignment across sensitive groups.
When we focus on true preference alignment (right side of the plots), the outcomes differ. For Jaccard, random
again performs best, showing its ability to increase hits and capture user preferences broadly. However, in ranking-
based evaluations (PRAG), random typically falls behind recent, which achieves lower SNSR values, reflecting its
strength in scenarios where nuanced understanding of user profiles is essential for fair ranking.
Thus, we observe that while random sampling increases the number of hits and excels in surface-level item
similarity (Jaccard), it has the worst impact on ranking-based fairness (PRAG), where a more careful understanding
of user profiles is necessary. This arguable may highlight the importance of selecting sampling strategies tailored
to the specific fairness objectives being prioritized.
Summary of Answer to RQ2.
In summary, each sampling strategy exhibits different strengths depending on how fairness is defined and
measured. Top-rated and recent strategies are better suited for ranking-based scenarios (PRAG), while a
simple random strategy performs better for hits (Jaccard). Ultimately, the choice of strategy and evaluation
lens (item-level vs. true preference, Jaccard vs. PRAG) determines which approach appears “best, ” and no
single method universally outperforms the others in all fairness scenarios. These findings suggest that
much of the fairness discussion in RecLLMs may depend on bridging the semantic gap between systems’
understanding of user tastes and interest.
4.3 Answer to RQ3. Variability in consumer fairness across models and datasets, and overall what
extent does the introduction of sensitive attributes—amplify observed disparities in fairness?
Extending our exploration beyond the earlier questions, RQ3 focuses on how fairness varies across different RecLLM
models and datasets. Previous examinations often focused on a single model or domain, but here we aim to compare
multiple configurations—for example, contrasting GPT-3.5 with GPT-4.0 mini recommendations—and apply them
to different datasets, such as MovieLens (movies) and LastFM (music). By doing so, RQ3 probes whether particular
model architectures or data sources inherently lead to larger fairness gaps when sensitive attributes (e.g., age or
sex) are introduced. This question is especially pertinent since models trained on distinct text corpora or using
varied prompt-engineering strategies may respond differently to sensitive demographic cues, either amplifying or
attenuating underlying biases. Results are shown in Figure 3.
Two key observations emerge from comparing the results:
(1) Dataset Differences. Across all tested dimensions, SNSR metrics (both for Jaccard and PRAG) generally
indicate lower unfairness levels on the MovieLens dataset than on LastFM, regardless of the model type or the
sensitive feature considered. One possible interpretation is that MovieLens—focusing on a well-structured and
broadly familiar domain such as movies—allows LLMs to more consistently maintain fair recommendations
when sensitive attributes are revealed. The system may more easily base user tastes in well-defined genres,
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

18 • Yashar Deldjoo, and Tommaso di Noia
Sex Age Intersectional
Feature Category
0.00
0.02
0.04
0.06
0.08
0.10
0.12
0.14Jaccard SNSR
Sampling Strategy
Random
T op-Rated
Recent
Sex Age Intersectional
Feature Category
0.00
0.02
0.04
0.06
0.08
0.10
0.12
0.14Jaccard SNSR
Sampling Strategy
Random
T op-Rated
Recent
(a) Jaccard SNSR, Item-Level Similarity (Left) and True Preference Alignment (Right)
Sex Age Intersectional
Feature Category
0.00
0.02
0.04
0.06
0.08
0.10
0.12
0.14
0.16PRAG SNSR
Sampling Strategy
Random
T op-Rated
Recent
Sex Age Intersectional
Feature Category
0.00
0.02
0.04
0.06
0.08
0.10
0.12
0.14
0.16PRAG SNSR
Sampling Strategy
Random
T op-Rated
Recent
(b) PRAG SNSR, Item-Level Similarity (Left), True Preference Alignment (Right)
Fig. 2. Fairness and Accuracy Metrics Across Sampling Strategies on ML-1M dataset.
directors, or production years, reducing the risk that sensitive attributes (e.g., age group or sex) will skew the
final output. In contrast, music recommendations in LastFM may be more challenging to stabilize. Taste in
music can be more individualized and harder to categorize, potentially causing larger shifts in recommended
items once the model factors in sensitive demographics. In this scenario, the inclusion of sensitive attributes
might push the LLM to rely on stereotypical assumptions or less robust associations, leading to greater
unfairness.
For example, consider a female user in the MovieLens dataset who previously liked a variety of action
and drama films. When we reveal her gender, the GPT-based recommender still suggests a balanced set of
high-quality, relevant films—only slightly different from those recommended in a gender-neutral scenario.
By comparison, on LastFM, revealing that a user is a “young adult female” might cause the model to swing
more heavily toward certain music genres stereotypically associated with that demographic, causing more
pronounced shifts in the top recommended artists.
(2) Model Configuration and True Preference Alignment. Another key finding is that fairness outcomes
differ when we shift from surface-level similarity metrics (which merely check if recommended items match
those originally suggested) to true preference alignment metrics (which check if recommendations genuinely
align with the user’s known interests). Under this more stringent evaluation, GPT-4.0 mini generally exhibits
lower unfairness than GPT-3.5, even though at a surface level the reverse seems to be true. For instance,
GPT-3.5 might maintain a more consistent set of items between neutral and sensitive conditions at first
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

CFaiRLLM: Consumer Fairness Evaluation in LLM Recommender Systems • 19
Sex Age Intersectional
Feature Category
0.0
0.2
0.4
0.6
0.8
1.0SNSR Jaccard
Dataset and Model
MovieLens GPT-3.5
LastFM GPT-3.5
LastFM GPT-4o mini
Sex Age Intersectional
Feature Category
Dataset and Model
MovieLens GPT-3.5
LastFM GPT-3.5
LastFM GPT-4o mini
(a) Jaccard SNSR, Item-Level Similarity (Left) and True Preference Alignment (Right)
Sex Age Intersectional
Feature Category
0.0
0.2
0.4
0.6
0.8
1.0SNSR PRAG
Dataset and Model
MovieLens GPT-3.5
LastFM GPT-3.5
LastFM GPT-4o mini
Sex Age Intersectional
Feature Category
Dataset and Model
MovieLens GPT-3.5
LastFM GPT-3.5
LastFM GPT-4o mini
(b) PRAG SNSR, Item-Level Similarity (Left), True Preference Alignment (Right)
Fig. 3. Fairness and Accuracy Metrics Across Models and Datasets.
glance, but closer inspection reveals that it does so by suggesting less truly preferred items. GPT-4.0 mini, on
the other hand, might appear to vary recommendations more initially, but it ultimately provides suggestions
that better match the user actual tastes when sensitive attributes are considered.
The interpretation of the above can be as follows. Suppose a user who enjoys classic rock and indie bands
receives recommendations from GPT-3.5 that appear stable whether we mention their age group or not. At
first glance, this stability seems fair. However, looking at the user’s actual listening habits in the test data, we
might realize that GPT-3.5’s sensitive-attribute-influenced list includes fewer bands the user actually likes.
GPT-4.0 mini’s recommendations, while more noticeably changing once the age attribute is introduced, may
result in being closer to the user’s real tastes—i.e., fewer “filler” items and more genuinely preferred bands.
Thus, from a “true preference” fairness perspective, GPT-4.0 mini proves more equitable.
Finally, we Now we aim to focus our attention on another key questions, which Sensitive Attribute Produces More
Unfairness?
When we look at the charts, we typically find that intersectional attributes (e.g., combining age and sex)
result in the greatest disparities. For instance, a user described simply as “Female” may experience a slight
shift in recommendations, but a user described as a “Young Adult Female” might trigger a more pronounced
change—significantly lower similarity or alignment with true preferences. Such intersectional cues provide the
model with more demographic signals, potentially prompting stronger stereotypical assumptions. For example, a
“Young Adult Female” in the music domain might push the recommender to heavily favor trending pop artists,
moving it away from niche, user-preferred indie bands.
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

20 • Yashar Deldjoo, and Tommaso di Noia
Summary of Answer to RQ3.
In summary, RQ3 reveals that certain dataset-model combinations and particularly intersectional attributes
exacerbate fairness gaps. MovieLens tends to remain more stable, while LastFM exhibits greater sensitivity
to demographic signals. Moreover, while GPT-3.5 may look stable at a surface level, GPT-4.0 mini ultimately
shows fairer outcomes when we consider true user preferences. Intersectional attributes, adding multiple
layers of demographic identity, often produce the most pronounced unfairness, as they allow models to
lean more heavily on demographic stereotypes, especially in domains with less stable grounding.
4.4 RQ4: The impact of Scope of The Sampling Strategy and Its Interplay with Sampling Strategy Itself
Increasing the number of movies in the sampling strategies has an impact on the computed similarities and fairness
measures. The heatmap comparisons reveal a direct relationship between the sampling scope (‘N’) and outcome
metrics for both male and female profiles. While the scope (‘N’) and the type of sampling strategy (top-rated vs.
random) both play crucial roles, the strategy itself exhibits a more pronounced impact. Notably, the fairness values
substantially decrease, and similarities increase across all cases when observing the heatmaps vertically. However,
the impact of N on fairness remains slightly variable, with𝑁 = 10 often resulting in the lowest (hence, best) fairness
scores, while scores for𝑁 = 5 and𝑁 = 15 are slightly higher. Nonetheless, focusing on their interplay, it becomes
clear that higher values of ‘N’, especially with the top-rated sampling strategy, yield much better recommendation
fairness scores.
The results indicate that enhanced profile construction strategies can mitigate fairness issues arising from the
introduction of sensitive attributes to RecLLMs. This phenomenon could be explained due to improved system
personalization. By refining how profiles are constructed, it is possible to achieve a more nuanced understanding
of user preferences, leading to recommendations that are more fair and more personalized.
Answer to RQ4.
The findings from RQ4 underscore the impact of both the scope of sampling strategies and the choice
of sampling strategy itself on the fairness and accuracy of recommendations in RecLLMs. More detailed
profile construction strategies, particularly when increasing the scope for the user profile, and top-rated
sampling (as opposed to random), impact fairness and personalization.
5 CONCLUSION
In this study, we critically examine and advance the methodologies for evaluating fairness in Large Language
Model-based recommender systems (RecLLMs). Traditional approaches have predominantly focused on assessing
consumer fairness by comparing recommendation lists generated with and without sensitive user attributes.
5 10 20
Number of Movies
randomtop-rated
Strategy
0.0313 0.0311 0.0350
0.0681 0.0682 0.0713
Simulated Male
5 10 20
Number of Movies
randomtop-rated
Strategy
0.0103 0.0241 0.0375
0.0529 0.0675 0.0598
Simulated Female
5 10 20
Number of Movies
randomtop-rated
Strategy
0.0210 0.0070 0.0025
0.0152 0.0008 0.0114
SSNR
0.035
0.040
0.045
0.050
0.055
0.060
0.065
0.070
Value
0.02
0.03
0.04
0.05
0.06
Value
0.0025
0.0050
0.0075
0.0100
0.0125
0.0150
0.0175
0.0200
Value
Fig. 4. Heatmap Comparison of Recommendation Fairness and Similarity: The left heatmap shows the effect of increasing
movie counts with random sampling, the middle heatmap depicts the outcome of using a top-rated sampling strategy, and the
right heatmap presents fairness scores, highlighting the differential impact of sampling strategies on recommendation quality.
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

CFaiRLLM: Consumer Fairness Evaluation in LLM Recommender Systems • 21
However, such methods often conflate genuine personalization with biased outcomes, failing to discern whether
discrepancies arise from true alignment with user preferences or from inherent biases. To address these limitations,
we introduce CFaiRLLM, an enhanced evaluation framework that not only emphasizes true preference alignment
but also rigorously investigates intersectional fairness by considering overlapping sensitive attributes. Additionally,
CFaiRLLM incorporates diverse user profile sampling strategies—random, top-rated, and recency-focused—to
address the token limitations of LLMs, aiming for a more comprehensive and realistic assessment of fairness within
RecLLMs.
Our extensive experiments utilizing the ML-1M and LastFM-1K datasets reveal that true preference alignment
significantly improves the personalization and fairness of recommendations compared to traditional similarity-based
measures. Notably, our findings demonstrate that intersectional attributes exacerbate fairness gaps, particularly
in less structured domains such as music recommendations. These insights underscore the necessity for future
fairness evaluations in RecLLMs to prioritize true preference alignment, thereby fostering equitable and genuinely
personalized recommendation experiences. By refining the evaluation framework and highlighting the complex
interplay of intersectional identities, our work lays a foundational path for developing more ethical and user-centric
recommender systems in the era of large language models.
Key Insights from Results:
• True Preference Alignment Enhances (our Understanding of) Fairness : Evaluations based on true
preference alignment consistently showed lower unfairness scores compared to traditional similarity-based
metrics, indicating a more accurate reflection of user preferences.
• Intersectional Attributes Amplify Fairness Gaps: Incorporating multiple sensitive attributes simultane-
ously led to more pronounced disparities in recommendation fairness, especially noticeable in the LastFM
dataset.
• Sampling Strategies Influence Fairness Outcomes: Top-rated and recency-focused sampling strategies
outperformed random sampling in reducing bias and improving the alignment of recommendations with
user preferences.
• Domain-Specific Variations: Fairness improvements were more significant in structured domains like
movie recommendations (ML-1M) compared to less structured ones like music (LastFM-1K), highlighting the
influence of domain characteristics on fairness outcomes.
These findings advocate for a shift in fairness evaluation paradigms towards frameworks that prioritize genuine
user preference alignment and account for the multifaceted nature of user identities, thereby promoting more
equitable and personalized recommender systems. In the end, we would like to emphasize that the insights and
findings of this work are specific to the audited system. Additionally, we clarify that prompt engineering is not a
universal solution but rather one component of a broader framework. We hope this work offers valuable insights
into the evaluation of recommender systems from a trust perspective. We plan to continue this research by exploring
red teaming techniques for increasingly robust models , focusing on aspects such as security Nazary et al. [47],
privacy, hallucination, and emerging fairness scenarios.
5.1 Limitation and Future Directions
We acknowledge that using a commercial API, such as GPT, limits reproducibility due to its proprietary nature
and ongoing updates. While our previous work [13] shows semantic consistency over short time frames, future
work should explore open-access models like LLama, Bloom, etc. to promote reproducibility. Additionally, we
recognize that our sampling strategies—random, top-rated, and recent—do not explicitly address the distinctiveness
of highly-rated items, which could obscure individual user nuances. For instance, users with high ratings for widely
popular movies like Star Wars or Titanic may not have their unique preferences fully captured. Incorporating
diversity-focused sampling is an important direction for future research.
Furthermore, future work could extend this study by exploring additional sensitive attributes like ethnicity
or socioeconomic status, applying the CFaiRLLM framework to diverse domains such as e-commerce or music,
and conducting longitudinal studies to assess the impact of fairness on user satisfaction. Bias mitigation remains
another critical avenue, including developing bias-aware datasets and integrating fairness considerations into
model training. Additionally, leveraging content-based models offers potential for alignment with RecLLMs, given
their reliance on the target user’s own rating (just like how RecLLMs function) [ 11, 21]. Finally, investigating
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

22 • Yashar Deldjoo, and Tommaso di Noia
alternative approaches to intersectional fairness, is another interesting future direction, for understanding and
addressing unfairness in more complex identity overlaps (see Yang et al. [64].)
6 APPENDIX
Here we provide detailed experimental results for movielens dataset that substantiate our research findings across
previous questions. The data clearly demonstrate that user profile sampling strategies—impact recommendation
fairness and alignment with true user preferences compared to random sampling. Additionally, our intersectional
analysis reveals that combining multiple sensitive attributes, such as sex and age, intensifies fairness disparities,
arguably emphasizing the complex challenges in mitigating bias within RecLLMs.
Table 5. Recommendation alignment between (R𝑚,R𝑎𝑚) based on Item Similarity𝛽𝑖𝑡𝑒𝑚
Prompting
Strategy
Profile sampling
Strategy Sex Age Intersectional (Sex & Age)
𝑆𝑚𝑛 𝑆𝑓𝑛 𝑆𝑁𝑆𝑅 𝑆𝑁𝑆𝑉 𝑆 𝑡𝑛 𝑆𝑦𝑛 𝑆𝑎𝑛 𝑆𝑁𝑆𝑅 𝑆𝑁𝑆𝑉 𝑆 𝑚𝑡𝑛 𝑆𝑚𝑦𝑛 𝑆𝑚𝑎𝑛 𝑆𝑓𝑡𝑛 𝑆𝑓𝑦𝑛 𝑆𝑓𝑎𝑛 𝑆𝑁𝑆𝑅 𝑆𝑁𝑆𝑉
Jaccard
Sex
random 0.1680 0.1670 0.0010 0.0005 0.2069 0.1473 0.1836 0.0596 0.0245 0.2098 0.1438 0.1850 0.1985 0.1552 0.1780 0.0661 0.0230
top-rated 0.6760 0.6125 0.0635 0.0318 0.6620 0.6634 0.6465 0.0169 0.0077 0.6581 0.6874 0.6669 0.6733 0.6107 0.5648 0.1226 0.0425
recent 0.6344 0.5920 0.0424 0.0212 0.6373 0.6133 0.6329 0.0241 0.0105 0.6534 0.6119 0.6627 0.5913 0.6163 0.5138 0.1489 0.0488
Age
random 0.1696 0.1716 0.0020 0.0010 0.1669 0.1847 0.1421 0.0426 0.0175 0.1670 0.1879 0.1387 0.1666 0.1778 0.1557 0.0492 0.0157
top-rated 0.6372 0.6524 0.0152 0.0076 0.5773 0.6548 0.6565 0.0793 0.0370 0.5598 0.6391 0.6821 0.6272 0.6893 0.5543 0.1351 0.0530
recent 0.6162 0.6793 0.0631 0.0315 0.5918 0.6556 0.6157 0.0639 0.0263 0.5702 0.6338 0.6138 0.6534 0.7036 0.6233 0.1334 0.0404
Inters.
random 0.1655 0.1291 0.0364 0.0182 0.1981 0.1446 0.1497 0.0536 0.0241 0.2047 0.1532 0.1630 0.1794 0.1256 0.0965 0.1082 0.0351
top-rated 0.5724 0.5199 0.0525 0.0263 0.4895 0.5714 0.5766 0.0871 0.0399 0.4734 0.5905 0.6021 0.5355 0.5297 0.4743 0.1288 0.0501
recent 0.5929 0.5313 0.0616 0.0308 0.5272 0.5901 0.5800 0.0629 0.0276 0.5499 0.6004 0.6065 0.4623 0.5675 0.4741 0.1442 0.0566
PRAG
Sex
random 0.3937 0.3432 0.0505 0.0253 0.4125 0.3651 0.3887 0.0475 0.0194 0.4450 0.3655 0.4120 0.3197 0.3641 0.2958 0.1492 0.0507
top-rated 0.8668 0.8292 0.0376 0.0188 0.8909 0.8586 0.8290 0.0619 0.0253 0.8950 0.8732 0.8376 0.8790 0.8264 0.7946 0.1004 0.0346
recent 0.8637 0.8492 0.0145 0.0072 0.8809 0.8565 0.8520 0.0289 0.0127 0.8773 0.8612 0.8596 0.8912 0.8464 0.8214 0.0697 0.0221
Age
random 0.3817 0.4488 0.0670 0.0335 0.3679 0.4292 0.3613 0.0679 0.0306 0.3233 0.4156 0.3579 0.4952 0.4590 0.3750 0.1719 0.0591
top-rated 0.8638 0.8681 0.0043 0.0021 0.8485 0.8617 0.8829 0.0345 0.0142 0.8510 0.8505 0.8954 0.8414 0.8860 0.8330 0.0624 0.0230
recent 0.8476 0.8858 0.0381 0.0191 0.8409 0.8545 0.8770 0.0361 0.0149 0.8241 0.8429 0.8707 0.8888 0.8799 0.9023 0.0782 0.0268
Inters.
random 0.3872 0.2854 0.1018 0.0509 0.4210 0.3498 0.3375 0.0835 0.0368 0.4500 0.3719 0.3750 0.3381 0.3013 0.1875 0.2625 0.0807
top-rated 0.8329 0.7897 0.0432 0.0216 0.8340 0.7970 0.8624 0.0654 0.0268 0.8360 0.8108 0.8704 0.8286 0.7668 0.8304 0.1036 0.0311
recent 0.8144 0.8164 0.0020 0.0010 0.7932 0.8182 0.8228 0.0296 0.0130 0.8200 0.8093 0.8199 0.7168 0.8376 0.8345 0.1208 0.0412
Please note that the rows represent prompting strategies, and column tabs represent group results. To test the effect of
sex-based instruction prompting, we should mainly look at the results in the sex category. This is the reason the other boxes
are gray. However, we will also look at the cross effect in RQ3.
REFERENCES
[1] Enrique Amigó, Yashar Deldjoo, Stefano Mizzaro, and Alejandro Bellogín. 2023. A unifying and general account of fairness measurement
in recommender systems. Information Processing & Management 60, 1 (2023), 103115.
[2] Akari Asai, Mohammadreza Salehi, Matthew E Peters, and Hannaneh Hajishirzi. 2022. Attempt: Parameter-efficient multi-task tuning via
attentional mixtures of soft prompts. InProceedings of the 2022 Conference on Empirical Methods in Natural Language Processing . 6655–6672.
[3] Giovanni Maria Biancofiore, Yashar Deldjoo, Tommaso Di Noia, Eugenio Di Sciascio, and Fedelucio Narducci. 2024. Interactive Question
Answering Systems: Literature Review. ACM Computing Surveys (CSUR) (2024).
[4] Toine Bogers and Marijn Koolen. 2017. Defining and supporting narrative-driven recommendation. In Proceedings of the eleventh ACM
conference on recommender systems . 238–242.
[5] Ludovico Boratto, Gianni Fenu, and Mirko Marras. 2021. Interplay between upsampling and regularization for provider fairness in
recommender systems. User Modeling and User-Adapted Interaction 31, 3 (2021), 421–455.
[6] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish
Sastry, Amanda Askell, et al. 2020. Language models are few-shot learners. Advances in neural information processing systems 33 (2020),
1877–1901.
[7] Robin Burke, Nasim Sonboli, and Aldo Ordonez-Gauger. 2018. Balanced neighborhoods for multi-sided fairness in recommendation. In
Conference on fairness, accountability and transparency . PMLR, 202–214.
[8] Abhijnan Chakraborty, Aniko Hannak, Asia J Biega, and Krishna P Gummadi. 2017. Fair sharing for sharing economy platforms. (2017).
[9] Yupeng Chang, Xu Wang, Jindong Wang, Yuan Wu, Linyi Yang, Kaijie Zhu, Hao Chen, Xiaoyuan Yi, Cunxiang Wang, Yidong Wang, et al.
2023. A survey on evaluation of large language models. ACM Transactions on Intelligent Systems and Technology (2023).
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

CFaiRLLM: Consumer Fairness Evaluation in LLM Recommender Systems • 23
Table 6. True preference alignment
Sex Age Intersectional (sex & Age)
𝑆𝑚𝑛 𝑆𝑓𝑛 𝑆𝑁𝑆𝑅 𝑆𝑁𝑆𝑉 𝑆 𝑡𝑛 𝑆𝑦𝑛 𝑆𝑎𝑛 𝑆𝑁𝑆𝑅 𝑆𝑁𝑆𝑉 𝑆 𝑚𝑡 𝑆𝑚𝑦 𝑆𝑚𝑎 𝑆𝑓𝑡 𝑆𝑓𝑦 𝑆𝑓𝑎 𝑆𝑁𝑆𝑅 𝑆𝑁𝑆𝑉
Jaccard
Sex
random 0.0313 0.0103 0.0210 0.0105 0.0193 0.0271 0.0266 0.0078 0.0035 0.0261 0.0321 0.0332 0.0000 0.0162 0.0000 0.0332 0.0138
top-rated 0.0681 0.0529 0.0152 0.0076 0.0849 0.0535 0.0716 0.0314 0.0129 0.0846 0.0521 0.0863 0.0857 0.0565 0.0125 0.0738 0.0266
recent 0.0461 0.0375 0.0086 0.0043 0.0704 0.0398 0.0340 0.0365 0.0160 0.0824 0.0392 0.0359 0.0363 0.0413 0.0264 0.0560 0.0180
Age
random 0.0189 0.0225 0.0036 0.0018 0.0226 0.0199 0.0181 0.0045 0.0019 0.0206 0.0197 0.0164 0.0286 0.0202 0.0250 0.0122 0.0040
top-rated 0.0640 0.0549 0.0091 0.0046 0.0919 0.0481 0.0688 0.0437 0.0179 0.0890 0.0446 0.0829 0.1000 0.0558 0.0125 0.0875 0.0299
recent 0.0487 0.0394 0.0093 0.0047 0.0658 0.0445 0.0362 0.0296 0.0125 0.0771 0.0442 0.0390 0.0337 0.0453 0.0250 0.0521 0.0163
Inters.
random 0.0274 0.0155 0.0119 0.0060 0.0335 0.0202 0.0260 0.0133 0.0055 0.0342 0.0222 0.0325 0.0317 0.0159 0.0000 0.0342 0.0120
top-rated 0.0647 0.0566 0.0082 0.0041 0.0957 0.0519 0.0620 0.0438 0.0187 0.0919 0.0497 0.0744 0.1063 0.0567 0.0125 0.0938 0.0305
recent 0.0440 0.0328 0.0111 0.0056 0.0652 0.0365 0.0336 0.0316 0.0143 0.0825 0.0350 0.0358 0.0159 0.0398 0.0250 0.0666 0.0210
PRAG
Sex
random 0.0367 0.0000 0.0367 0.0183 0.0000 0.0241 0.0500 0.0500 0.0204 0.0000 0.0351 0.0625 0.0000 0.0000 0.0000 0.0625 0.02437
top-rated 0.0459 0.0488 0.0029 0.0015 0.1173 0.0321 0.0292 0.0881 0.0409 0.1083 0.0292 0.0365 0.1429 0.0385 0.0000 0.1429 0.0496
recent 0.0183 0.0000 0.0183 0.0092 0.0741 0.0000 0.0000 0.0741 0.0349 0.1000 0.0000 0.0000 0.0000 0.0000 0.0000 0.1000 0.0373
Age
random 0.0183 0.0244 0.0060 0.0030 0.0741 0.0120 0.0000 0.0741 0.0325 0.0500 0.0175 0.0000 0.1429 0.0000 0.0000 0.1429 0.0514
top-rated 0.0642 0.0325 0.0317 0.0158 0.1481 0.0361 0.0333 0.1148 0.0535 0.1833 0.0351 0.0417 0.0476 0.0385 0.0000 0.1833 0.0582
recent 0.0428 0.0244 0.0184 0.0092 0.0741 0.0321 0.0250 0.0491 0.0217 0.1000 0.0292 0.0312 0.0000 0.0385 0.0000 0.1000 0.0335
Inters.
random 0.0092 0.0000 0.0092 0.0046 0.0370 0.0000 0.0000 0.0370 0.0175 0.0500 0.0000 0.0000 0.0000 0.0000 0.0000 0.0500 0.0186
top-rated 0.0443 0.0366 0.0078 0.0039 0.0988 0.0361 0.0167 0.0821 0.0350 0.1083 0.0351 0.0208 0.0714 0.0385 0.0000 0.1083 0.0353
recent 0.0183 0.0000 0.0183 0.0092 0.0370 0.0000 0.0250 0.0370 0.0154 0.0500 0.0000 0.0312 0.0000 0.0000 0.0000 0.0500 0.0199
Please note that the rows represent prompting strategies, and column tabs represent group results. To test the effect of
sex-based instruction prompting, we should mainly look at the results in the sex category. This is the reason the other boxes
are gray. However, we will also look at the cross effect in RQ3.
[10] Diego Corrêa da Silva, Marcelo Garcia Manzato, and Frederico Araújo Durão. 2021. Exploiting personalized calibration and metrics for
fairness recommendation. Expert Systems with Applications 181 (2021), 115112.
[11] Marco De Gemmis, Pasquale Lops, Cataldo Musto, Fedelucio Narducci, and Giovanni Semeraro. 2015. Semantics-aware content-based
recommender systems. Recommender systems handbook (2015), 119–159.
[12] Yashar Deldjoo. 2023. Fairness of ChatGPT and the Role of Explainable-Guided Prompts. In COLLM@ECML-PKDD’23.
[13] Yashar Deldjoo. 2024. Understanding Biases in ChatGPT-based Recommender Systems: Provider Fairness, Temporal stability, and Recency.
ACM Transactions on Recommender Systems (2024).
[14] Yashar Deldjoo, Vito Walter Anelli, Hamed Zamani, Alejandro Bellogin, and Tommaso Di Noia. 2021. A flexible framework for evaluating
user and item fairness in recommender systems. User Modeling and User-Adapted Interaction (2021), 1–55.
[15] Yashar Deldjoo, Tommaso Di Noia, Eugenio Di Sciascio, and Felice Antonio Merra. 2020. How Dataset Characteristics Affect the Robustness
of Collaborative Recommendation Models. In Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in
Information Retrieval.
[16] Yashar Deldjoo, Tommaso Di Noia, and Felice Antonio Merra. 2022. A survey on adversarial recommender systems: from attack/defense
strategies to generative adversarial networks. Comput. Surveys 2 (2022), 1–38.
[17] Yashar Deldjoo, Zhankui He, Julian McAuley, Anton Korikov, Scott Sanner, Arnau Ramisa, René Vidal, Maheswaran Sathiamoorthy, Atoosa
Kasirzadeh, and Silvia Milano. 2024. A Review of Modern Recommender Systems using Generative Models (Gen-RecSys). In Proceedings of
the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining . 6448–6458.
[18] Yashar Deldjoo, Zhankui He, Julian McAuley, Anton Korikov, Scott Sanner, Arnau Ramisa, Rene Vidal, Maheswaran Sathiamoorthy, Atoosa
Kasrizadeh, Silvia Milano, et al. 2024. Recommendation with generative models. arXiv preprint arXiv:2409.15173 (2024).
[19] Yashar Deldjoo, Dietmar Jannach, Alejandro Bellogin, Alessandro Difonzo, and Dario Zanzonelli. 2023. Fairness in recommender systems:
research landscape and future directions. User Modeling and User-Adapted Interaction (2023), 1–50.
[20] Yashar Deldjoo and Fatemeh Nazary. 2024. A Normative Framework for Benchmarking Consumer Fairness in Large Language Model
Recommender System. In ROEGen@RecSys’24.
[21] Yashar Deldjoo, Markus Schedl, Paolo Cremonesi, Gabirella Pasi, et al. 2018. Content-based multimedia recommendation systems: definition
and application domains. In Italian Information Retrieval Workshop. 1–4.
[22] Dario Di Palma, Giovanni Maria Biancofiore, Vito Walter Anelli, Fedelucio Narducci, Tommaso Di Noia, and Eugenio Di Sciascio. 2023.
Evaluating chatgpt as a recommender system: A rigorous approach. arXiv preprint arXiv:2309.03613 (2023).
[23] Virginie Do, Sam Corbett-Davies, Jamal Atif, and Nicolas Usunier. 2021. Two-sided fairness in rankings via Lorenz dominance. Advances
in Neural Information Processing Systems 34 (2021).
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

24 • Yashar Deldjoo, and Tommaso di Noia
[24] Qiang Dong, Shuang-Shuang Xie, and Wen-Jun Li. 2021. User-item matching for recommendation fairness. IEEE Access 9 (2021),
130389–130398.
[25] Michael Dowling and Brian Lucey. 2023. ChatGPT for (finance) research: The Bananarama conjecture. Finance Research Letters 53 (2023),
103662.
[26] Michael D Ekstrand, Robin Burke, and Fernando Diaz. 2019. Fairness and discrimination in recommendation and retrieval. In Proceedings
of the 13th ACM Conference on Recommender Systems . 576–577.
[27] Golnoosh Farnadi, Pigi Kouki, Spencer K Thompson, Sriram Srinivasan, and Lise Getoor. 2018. A fairness-aware hybrid recommender
system. arXiv preprint arXiv:1809.09030 (2018).
[28] Yingqiang Ge, Shuchang Liu, Ruoyuan Gao, Yikun Xian, Yunqi Li, Xiangyu Zhao, Changhua Pei, Fei Sun, Junfeng Ge, Wenwu Ou, et al.
2021. Towards long-term fairness in recommendation. In Proceedings of the 14th ACM international conference on web search and data
mining. 445–453.
[29] Shijie Geng, Shuchang Liu, Zuohui Fu, Yingqiang Ge, and Yongfeng Zhang. 2022. Recommendation as language processing (rlp): A unified
pretrain, personalized prompt & predict paradigm (p5). In Proceedings of the 16th ACM Conference on Recommender Systems . 299–315.
[30] Elizabeth Gómez, Carlos Shui Zhang, Ludovico Boratto, Maria Salamó, and Mirko Marras. 2021. The winner takes it all: geographic
imbalance and provider (un) fairness in educational recommender systems. In Proceedings of the 44th International ACM SIGIR Conference
on Research and Development in Information Retrieval . 1808–1812.
[31] Qianxiu Hao, Qianqian Xu, Zhiyong Yang, and Qingming Huang. 2021. Pareto optimality for fairness-constrained collaborative filtering.
In Proceedings of the 29th ACM International Conference on Multimedia . 5619–5627.
[32] Zhankui He, Zhouhang Xie, Rahul Jha, Harald Steck, Dawen Liang, Yesu Feng, Bodhisattwa Prasad Majumder, Nathan Kallus, and Julian
McAuley. 2023. Large language models as zero-shot conversational recommenders. In Proceedings of the 32nd ACM international conference
on information and knowledge management . 720–730.
[33] Yupeng Hou, Shanlei Mu, Wayne Xin Zhao, Yaliang Li, Bolin Ding, and Ji-Rong Wen. 2022. Towards universal sequence representation
learning for recommender systems. In Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining . 585–593.
[34] Mingyu Jin, Qinkai Yu, Chong Zhang, Dong Shu, Suiyuan Zhu, Mengnan Du, Yongfeng Zhang, and Yanda Meng. 2024. Health-LLM:
Personalized Retrieval-Augmented Disease Prediction Model. arXiv preprint arXiv:2402.00746 (2024).
[35] Markus Kattnig, Alessa Angerschmid, Thomas Reichel, and Roman Kern. 2024. Assessing trustworthy AI: Technical and legal perspectives
of fairness in AI. Computer Law & Security Review 55 (2024), 106053.
[36] Ömer Kırnap, Fernando Diaz, Asia Biega, Michael Ekstrand, Ben Carterette, and Emine Yilmaz. 2021. Estimation of fair ranking metrics
with incomplete judgments. In Proceedings of the Web Conference 2021 . 1065–1075.
[37] Kibeom Lee and Kyogu Lee. 2015. Escaping your comfort zone: A graph-based recommender system for finding novel recommendations
among relevant items. Expert Systems with Applications 42, 10 (2015), 4851–4858.
[38] Lei Li, Yongfeng Zhang, Dugang Liu, and Li Chen. 2023. Large language models for generative recommendation: A survey and visionary
discussions. arXiv preprint arXiv:2309.01157 (2023).
[39] Xinyi Li, Yongfeng Zhang, and Edward C Malthouse. 2023. A Preliminary Study of ChatGPT on News Recommendation: Personalization,
Provider Fairness, Fake News. arXiv preprint arXiv:2306.10702 (2023).
[40] Yunqi Li, Hanxiong Chen, Zuohui Fu, Yingqiang Ge, and Yongfeng Zhang. 2021. User-oriented fairness in recommendation. In Proceedings
of the Web Conference 2021. 624–632.
[41] Lizi Liao, Grace Hui Yang, and Chirag Shah. 2023. Proactive conversational agents in the post-chatgpt world. In Proceedings of the 46th
International ACM SIGIR Conference on Research and Development in Information Retrieval . 3452–3455.
[42] Chen Lin, Xinyi Liu, Guipeng Xv, and Hui Li. 2021. Mitigating sentiment bias for recommender systems. In Proceedings of the 44th
International ACM SIGIR Conference on Research and Development in Information Retrieval . 31–40.
[43] Duen-Ren Liu, Yu-Shan Liao, Ya-Han Chung, and Kuan-Yu Chen. 2019. Advertisement recommendation based on personal interests and
ad push fairness. Kybernetes 48, 8 (2019), 1586–1605.
[44] Weiwen Liu, Feng Liu, Ruiming Tang, Ben Liao, Guangyong Chen, and Pheng Ann Heng. 2020. Balancing between accuracy and fairness
for interactive recommendation with reinforcement learning. In Advances in Knowledge Discovery and Data Mining: 24th Pacific-Asia
Conference, PAKDD 2020, Singapore, May 11–14, 2020, Proceedings, Part I 24 . Springer, 155–167.
[45] Mohammadmehdi Naghiaei, Hossein A Rahmani, and Yashar Deldjoo. 2022. Cpfair: Personalized consumer and producer fairness
re-ranking for recommender systems. In Proceedings of the 45th International ACM SIGIR Conference on Research and Development in
Information Retrieval. 770–779.
[46] Fatemeh Nazary, Yashar Deldjoo, and Tommaso Di Noia. 2023. ChatGPT-HealthPrompt. Harnessing the Power of XAI in Prompt-Based
Healthcare Decision Support using ChatGPT. In European Conference on Artificial Intelligence . Springer, 382–397.
[47] Fatemeh Nazary, Yashar Deldjoo, and Tommaso di Noia. 2025. Poison-RAG: Adversarial Data Poisoning Attacks on Retrieval-Augmented
Generation in Recommender Systems. arXiv preprint arXiv:2501.11759 (2025).
[48] Fatemeh Nazary, Yashar Deldjoo, Tommaso Di Noia, and Eugenio di Sciascio. 2024. XAI4LLM. Let Machine Learning Models and LLMs
Collaborate for Enhanced In-Context Learning in Healthcare. arXiv preprint arXiv:2405.06270 (2024).
[49] Gourab K Patro, Arpita Biswas, Niloy Ganguly, Krishna P Gummadi, and Abhijnan Chakraborty. 2020. Fairrec: Two-sided fairness for
personalized recommendations in two-sided platforms. In Proceedings of The Web Conference 2020 . 1194–1204.
[50] Hossein A Rahmani, Yashar Deldjoo, Ali Tourani, and Mohammadmehdi Naghiaei. 2022. The Unfairness of Active Users and Popularity
Bias in Point-of-Interest Recommendation. In Bias@ECIR’22.
[51] Scott Sanner, Krisztian Balog, Filip Radlinski, Ben Wedin, and Lucas Dixon. 2023. Large language models are competitive near cold-start
recommenders for language-and item-based preferences. In Proceedings of the 17th ACM conference on recommender systems . 890–896.
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.

CFaiRLLM: Consumer Fairness Evaluation in LLM Recommender Systems • 25
[52] Dougal Shakespeare, Lorenzo Porcaro, Emilia Gómez, and Carlos Castillo. 2020. Exploring artist gender bias in music recommendation.
arXiv preprint arXiv:2009.01715 (2020).
[53] Tianshu Shen, Jiaru Li, Mohamed Reda Bouadjenek, Zheda Mai, and Scott Sanner. 2023. Towards understanding and mitigating unintended
biases in language model-driven conversational recommendation. Information Processing & Management 60, 1 (2023), 103139.
[54] Tom Sühr, Sophie Hilgard, and Himabindu Lakkaraju. 2021. Does fair ranking improve minority outcomes? understanding the interplay of
human and algorithmic biases in online hiring. In Proceedings of the 2021 AAAI/ACM Conference on AI, Ethics, and Society . 989–999.
[55] Tu Vu, Brian Lester, Noah Constant, Rami Al-Rfou, and Daniel Cer. 2021. Spot: Better frozen model adaptation through soft prompt
transfer. arXiv preprint arXiv:2110.07904 (2021).
[56] Mengting Wan, Jianmo Ni, Rishabh Misra, and Julian McAuley. 2020. Addressing marketing bias in product recommendations. In
Proceedings of the 13th international conference on web search and data mining . 618–626.
[57] Leonard Weydemann, Dimitris Sacharidis, and Hannes Werthner. 2019. Defining and measuring fairness in location recommendations. In
Proceedings of the 3rd ACM SIGSPATIAL international workshop on location-based recommendations, geosocial networks and geoadvertising .
1–8.
[58] Chuhan Wu, Fangzhao Wu, Xiting Wang, Yongfeng Huang, and Xing Xie. 2021. Fairness-aware news recommendation with decomposed
adversarial learning. In Proceedings of the AAAI Conference on Artificial Intelligence , Vol. 35. 4462–4469.
[59] Shijie Wu, Ozan Irsoy, Steven Lu, Vadim Dabravolski, Mark Dredze, Sebastian Gehrmann, Prabhanjan Kambadur, David Rosenberg, and
Gideon Mann. 2023. Bloomberggpt: A large language model for finance. arXiv preprint arXiv:2303.17564 (2023).
[60] Yao Wu, Jian Cao, Guandong Xu, and Yudong Tan. 2021. TFROM: A Two-sided Fairness-Aware Recommendation Model for Both Customers
and Providers. arXiv preprint arXiv:2104.09024 (2021).
[61] Yang Xiao, Qingqi Pei, Lina Yao, Shui Yu, Lei Bai, and Xianzhi Wang. 2020. An enhanced probabilistic fairness-aware group recommendation
by incorporating social activeness. Journal of Network and Computer Applications 156 (2020), 102579.
[62] Lanling Xu, Junjie Zhang, Bingqian Li, Jinpeng Wang, Mingchen Cai, Wayne Xin Zhao, and Ji-Rong Wen. 2024. Prompting Large Language
Models for Recommender Systems: A Comprehensive Framework and Empirical Analysis. arXiv preprint arXiv:2401.04997 (2024).
[63] Shuyuan Xu, Wenyue Hua, and Yongfeng Zhang. 2023. OpenP5: Benchmarking Foundation Models for Recommendation. arXiv preprint
arXiv:2306.11134 (2023).
[64] Forest Yang, Mouhamadou Cisse, and Sanmi Koyejo. 2020. Fairness with overlapping groups; a probabilistic perspective. Advances in
neural information processing systems 33 (2020), 4067–4078.
[65] Jizhi Zhang, Keqin Bao, Yang Zhang, Wenjie Wang, Fuli Feng, and Xiangnan He. 2023. Is chatgpt fair for recommendation? evaluating
fairness in large language model recommendation. In Proceedings of the 17th ACM Conference on Recommender Systems . 993–999.
[66] Lemei Zhang, Peng Liu, Yashar Deldjoo, Yong Zheng, and Jon Atle Gulla. 2024. Understanding Language Modeling Paradigm Adaptations
in Recommender Systems: Lessons Learned and Open Challenges. In The 27th European Conference on Artificial Intelligence (ECAI’24) .
[67] Ziwei Zhu, Jingu Kim, Trung Nguyen, Aish Fenton, and James Caverlee. 2021. Fairness among new items in cold start recommender
systems. In Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval . 767–776.
ACM Trans. Intell. Syst. Technol., Vol. 1, No. 1, Article . Publication date: February 2025.
