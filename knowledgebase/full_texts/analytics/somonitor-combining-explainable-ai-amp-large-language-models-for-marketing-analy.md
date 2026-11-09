---
title: 'SOMONITOR: Combining Explainable AI &amp; Large Language Models for Marketing Analytics'
url: https://arxiv.org/abs/2407.13117
category: analytics
subcategory: measurement
date: 2024-07
venue: arXiv (Cornell University)
authors:
- Aleksandr Farseev
- Qi Yang
- Marlo Ongpin
source: arxiv
pdf_url: https://arxiv.org/pdf/2407.13117
pages: 16
chars: 85395
fetched_at: '2026-11-08T12:57:22+00:00'
kb_version: 1
---

# SOMONITOR: Combining Explainable AI &amp; Large Language Models for Marketing Analytics

SOMONITOR: Combining Explainable AI & Large
Language Models for Marketing Analytics
Aleksandr Farseev
SoMin.ai Research
Singapore, Singapore
sasha@somin.ai
Qi Yang
SoMin.ai Research
Singapore, Singapore
yang@somin.ai
Marlo Ongpin
SoMin.ai Research
Kuala Lumpur, Malaysia
marlo@somin.ai
Ilia Gossoudarev
ITMO University
Saint Petersburg, Russia
goss@itmo.ru
Yu-Yi Chu-Farseeva
SoMin.ai Research
Singapore, Singapore
joy@somin.ai
Sergey Nikolenko
ITMO University,
St. Petersburg Department of the Steklov
Institute of Mathematics , Saint Petersburg, Russia
sergey@logic.pdmi.ras.ru
Abstract—Online marketing faces formidable challenges in
managing and interpreting immense volumes of data necessary
for competitor analysis, content research, and strategic branding.
It is impossible to review hundreds to thousands of transient
online content items by hand, and partial analysis often leads
to suboptimal outcomes and poorly performing campaigns. We
introduce an explainable AI framework SOMONITOR that aims
to synergize human intuition with AI-based efficiency, helping
marketers across all stages of the marketing funnel, from
strategic planning to content creation and campaign execution.
SOMONITOR incorporates a CTR prediction and ranking model
for advertising content and uses large language models (LLMs)
to process high-performing competitor content, identifying core
content pillars such as target audiences, customer needs, and
product features. These pillars are then organized into broader
categories, including communication themes and targeted cus-
tomer personas. By integrating these insights with data from the
brand’s own advertising campaigns, SOMONITOR constructs a
narrative for addressing new customer personas and simulta-
neously generates detailed content briefs in the form of user
stories that, as shown in the conducted case study, can be directly
applied by marketing teams to streamline content production
and campaign execution. The adoption of SOMONITOR in daily
operations allows digital marketers to quickly parse through
extensive datasets, offering actionable insights that significantly
enhance campaign effectiveness and overall job satisfaction.
Index Terms —Digital Advertising, Ads Performance Predic-
tion, Deep Learning, Large Language Model, Explainable AI
I. I NTRODUCTION
The contemporary online marketing landscape is bursting
with an overwhelming amount of content in the form of
databases of advertisements, marketing campaigns of various
competitors, properties of user audiences, and more. Marketers
must not only sift through this information but also extract
meaningful insights regarding audience segmentation, trending
topics, and customer needs. Recent advances in the field of
large language models (LLMs) have made them into tools
of choice in various domains (see Section II). These models,
trained on huge datasets, exhibit remarkable capabilities in
both content analysis and content generation. In online market-
ing, modern LLMs are already able to offer a promising solu-
tion by processing and analyzing large datasets to identify key
elements, facilitating a more targeted and effective marketing
strategy. Moreover, they can help generate new advertisement
content, both text-based and multimodal.
Despite all this progress, in this work we note that vanilla
LLMs also have limitations in content scoring , which is a
crucial aspect of effective marketing. We show that a small
neural network, specifically tailored for CTR prediction based
on advertising content, performs better at content scoring
than standard LLMs, even those enhanced with multimodal
capabilities, offering a more reliable tool for marketers.
Therefore, we propose a system, called SOMONITOR, that
combines predictive analytics and LLMs in a unified online
marketing assistant. Importantly, marketing strategies encom-
pass more than just data analysis; they involve understanding
and implementing effective communication styles. It is essen-
tial to utilize these communication styles not merely as classi-
fication labels but as dynamic personas. This approach enables
the identification of different communication schemas tailored
to diverse user personas. These schemas, and the user personas
themselves, can be analyzed in existing marketing campaigns
via a clustering procedure (Section IV). The next step involves
aligning these personas with appropriate communication styles
to craft compelling narratives. These narratives, or stories, are
essential content that marketers can directly employ in their
campaigns for brief production or content calendar building.
However, to construct these stories one has to use high-quality
data, including marketing communications and advertisements
that have previously proven to be successful in building rapport
with the corresponding user personas.
Thus, the core issue circles back to the need for an ad-
vanced, yet explainable, predictive model for content scoring
and improvement, presented in Section VII. This model can
be used to filter and identify “good” advertisements that can
then serve to enhance the efficiency of LLMs in generating
impactful marketing content. Our research addresses this need
by introducing a predictive model that refines data input
for LLMs, ensuring the generation of content that resonates
arXiv:2407.13117v2  [cs.CY]  10 Dec 2024

Fig. 1. General pipeline of the SOMONITOR advertising analysis framework.
well with target audiences and supports strategic marketing
initiatives; in Section V, we show how this model alone can be
used for iterative content improvement via interactive heatmap
generation but also fits together with an LLM in a unified
workflow that can generate complete user stories that being
used by real businesses drastically improve their productivity.
The overall pipeline of SOMONITOR is illustrated in Fig. 1.
II. R ELATED WORK
Large language models (LLMs) have been successful in
numerous applications [1], [2] and a wide variety of tasks,
from low-resource machine translation [3] to writing source
code for full-scale applications [4], [5] and solving prob-
lems that require mathematics and engineering design [6].
Importantly, the quadratic complexity bottleneck inherent in
the original Transformer architecture [7] is also being over-
come with sparse attention mechanisms [8], [9], low-rank
decomposition of attention weight matrices [10], [11], Mamba-
style models [12]–[14], and other modifications with linear
complexity [15], [16]. As a result, latest LLMs can extend
their context windows (i.e., input sizes) up to millions of
tokens [17], [18], which makes it possible to use LLMs
directly for mid- and large-scale analysis of text datasets.
Recently, LLMs have also obtained multimodal capabilities,
allowing to use them for video understanding [19]. The
recently released GPT-4o, where ’o’ stands for “Omni”, brings
seamless multimodality of image, audio, and video analysis
to state-of-the-art LLMs [20]. LLMs can be combined with
diffusion-based generative models [21]–[23] to achieve state-
of-the-art image and video generation capabilities [24]–[26].
Moreover, LLMs are increasingly used to process structured
data, both in order to clean and/or augment data for ML
model training and to directly improve the user experience.
Extensive datasets used to train LLMs themselves [27]–[30]
require rigorous filtering and ensuring data quality, for both
technical [31]–[34] and legal considerations [35]–[37]. High-
quality datasets are equally essential for LLM fine-tuning,
particularly for instruction tuning, which depends on well-
crafted full-text prompts and responses [38]–[40], and LLMs
themselves increasingly assist in improving dataset quality;
for instance, CoachLM [41] autonomously revises samples
in instruction tuning datasets, IterClean [42] introduces an
LLM-driven framework for cleaning data, and the Natural
Instructions dataset [43] has been expanded with synthetic
data in Unnatural Instructions [44]. Other efforts include
purifying datasets of copyright and poisoning issues with
smaller LLMs [45], among other approaches [46].
LLMs are also employed as tools for dataset preprocess-
ing and refinement; e.g., Jellyfish [47] specializes in data
preprocessing, LLMClean [48] focuses on cleaning tabular
data, CAAFE [49] generates meaningful features for tabular
datasets, and other works [50], [51] explore tabular data
processing, even showcasing how LLMs can synthesize re-
alistic synthetic data [52]. In the realm of databases and
data lakes, LLMs have been applied to generate structured
views [53], identify necessary data transformations [54], and
enable natural language access to relational databases [55]–
[59], e.g., for exploratory data analysis [60]. They also aid
in interacting with graph databases [61], answering questions
over relational datasets [62], and other related tasks [63], [64].
One important aspect of data processing with LLMs deals
with recommender systems, where LLMs can unify tabular
data processing and semantic understanding of items and con-
text [65]. LLMs can be used directly for recommendation [66],
[67], especially in conversational systems where the used is
engaged in a dialogue with the system [68]–[70], but usually
an LLM-based recommender is either trained fully with a sep-
arate Transformer-based architecture—such systems include
the P5 approach (Pretrain, Personalized Prompt & Predict
Paradigm) [71], [72], M6-Rec [73], and IRS [74]—or fine-
tuned with instruction tuning [75], as in RecLLM [76], LC-
Rec [77], TallREC [78], GLRec [79], or BERT-Trip [80]; text
and Transformer-based embeddings of text can be used as user
and item representations instead of ID embeddings [81], [82].
Multimodal LLMs have led to modality-based recommender
systems that fuse encoders for different modalities [83],
including sequence representations [84]; multimodality can
make recommenders more robust to domain transfer [85]–[87].

Interpreting data through human-perceivable dynamic cat-
egories, such as topics or audiences, represents a significant
step towards explainable AI. Nonetheless, the sheer volume
of content and its prioritization continue to pose challenges,
with limitations inherent in LLMs, in particular related to
their hallucination phenomena [88]. We will see below that
an LLM can say that the primary audience for 1000 pieces of
marketing content is, e.g., “families”, but without predictions
of the content’s popularity across this audience this insight is
not actionable; LLMs are known to perform poorly and incon-
sistently in ranking problems [89]. At the same time, online
content platforms such as social networks and search engines,
namely Facebook (Meta) [90], Google [91], Alibaba [92],
and Taobao [93], have invested considerable efforts towards
content prioritization and scoring. Unfortunately, these results
are based on private datasets, inaccessible to external content
creators such as digital marketers. Proprietary engagement
data used for content scoring models remains exclusive to the
platforms, so independent creators cannot accurately predict
or enhance the efficacy of their content.
From all the above, it is evident that the comprehensive
capabilities of LLMs position them as high-level assistants
across a myriad of tasks within the realm of online marketing.
However, there exist relatively few research papers devoted
to these potential applications [94]. The marketing industry is
currently only starting to incorporate LLMs into the work-
flows, with many recent whitepapers and business surveys
of possible applications, problems, and potential breadth of
adoption of LLMs [95], [96]. Our recent work [97] presented
a comprehensive online marketing analysis system based on
large language models; in this paper, we build upon this work
and combine and further improve LLM-based analysis with
predictive analytics. A key advantage noted in [97] was the fact
that LLM answers are understandable for humans and action-
able in terms of business results: LLMs such as GPT-3.5 [98]
and GPT-4 [99] were already able to explain the “reasoning”
behind recommender models and provide aggregate insights
about advertising campaigns. Before LLMs, text corpora in
the context of recommender systems had been aggregated via
topic modeling [100], [101], sometimes also with deep learn-
ing [102] and user profiling [103], [104], but topic modeling is
based on the bag-of-words assumption and cannot summarize
text as an LLM does. Visual understanding of ads has also
been explored with convolutional networks [105].
However, a robust technology that enables effective dif-
ferentiation of content sources for insight extraction, as well
as a cohesive framework for data exploration that integrates
both content differentiation and LLM-based explanations, is
still sorely needed. Our work aims to address these gaps by
developing methods that enhance the functionality of LLMs
in online marketing applications, facilitating more efficient
utilization of modern AI in real-world scenarios.
III. C ONTENT PILLAR IDENTIFICATION
As noted above, data handlers in digital marketing fre-
quently encounter large volumes of creative assets to an-
Fig. 2. General pipeline of our LLM-based analysis
alyze, along with numerous ongoing promotional activities
from competitors in an “always-on” environment. Given this
context, conducting detailed analyses for each advertisement
or even for every specific competitor campaign becomes
impractical, highlighting the need for automated analytical
tools. These tools are crucial for assisting marketers in quickly
assimilating, synthesizing, and driving inferences from exten-
sive data and information available to them.
To address this challenge, we propose to integrate a novel
method into our framework that leverages LLMs to provide
semantic insights into content, referred to as “content pillars”
below. We outline an analytical pipeline that incorporates ex-
planations and generations based on LLMs, demonstrating its
practical utility through an empirical scenario involving four
Singapore-based telecommunication companies. This compo-
nent of our framework aims to enhance the interpretability
and understanding of data, thereby supporting more informed
decision-making in these dynamic and competitive sectors.
The architecture of our analytics is illustrated in Fig. 2.
Initially, we employ an LLM to extract specific, well-defined
insights from the input content, such as the customer needs
addressed by the advertisement and the products being ad-
vertised. These insights are then archived as content pillars
in a tabular format. Next, these pillars are processed with
custom-crafted prompts to perform a generalized analysis of
a brand’s target demographics, personas, needs, and insights
conveyed by the advertisements, as well as the tone and
topical categories of both current and previous campaigns.
This comprehensive analysis mirrors the campaign assess-
ments typically conducted by marketing professionals and can
be further used to refine a brand’s messaging, tone, and target
demographics. Below we explore these elements in detail.
Figure 3 presents sample qualitative results of our experi-
ments on the analysis of content pieces. We curated batches
of advertisements from the Facebook Ad Library for the same
brand and processed them through an LLM with custom
prompts. As a result, the LLM successfully identified key
attributes of each advertisement, providing adequate responses
to ostensibly “human” inquiries such as pinpointing the human

Fig. 3. Sample ad analysis
need, insight, and predominant archetypes in a specific ad.
Note that responses to most queries are standardized (as di-
rected by the prompt) and amenable to automated processing.
This analysis has always been important in online marketing
but to our knowledge has not been automated and scaled
before, always requiring human labor and thus being limited
to a small sample of ads rather than an extensive dataset.
IV. M INING COMMUNICATION PERSONAS AND THEMES
A. Problem setting
In the field of marketing, utilizing explainable data de-
scriptors such as the content pillars is essential. However, to
significantly enhance a brand’s marketing and communication
strategies it is necessary to go beyond mere description and
engage in inferential data analysis. Unfortunately, marketers
often lack the necessary skills in data operations, hindering
their ability to derive meaningful conclusions from the data,
thereby requiring additional support. To bridge this gap, we
propose a unified framework SOMONITOR that unites LLM-
based analysis with content scoring, designed to provide
marketers with higher-level content observations.
In marketing, the narrative constructed by any content
emerges from an underlying story, which is a synthesis of a
communication theme and a specific customer persona that the
campaign aims to engage. We will come back to the stories in
Section V, illustrating this concept through a representative
example, highlighting the integral relationship between the
storytelling elements and the targeted persona. This approach
empowers marketers to craft more resonant and effective
communication strategies by aligning their messaging with the
expectations and needs of their intended audiences. But to get
to a good story, we need to extract two essential storytelling
components: personas and challenges.
B. Persona Identification
In marketing, the customer persona is developed based on
data about the audience of a brand, supported by other content
pillars such as customer needs, interests, and aspirations [106].
We have used X-Means clustering [107] to divide the con-
tent pieces into distinct customer personas based on brand
content, specifically clustering ADA embeddings [108] of the
“Audience” content pillar as the main semantic differentiator.
X-Means was run with 3 starting centroids and kmax = 50,
identifying the number of clusters with BIC values [107].
For this study, we analyzed data from the Gojek car-
hailing brand and its main competitor in Singapore, Grab,
focusing exclusively on the B2B business audience to limit the
number of personas. The data for this experiment, collected
over 2023 and 2024, comprised 5,967 content pieces, with
3,703 published as ads and 2,264 as organic social media
posts. Since most of the content related to B2B product
offerings for both brands was presented in ads, we focused
solely on the advertising content, totaling 1,120 ads related
to business products. Brand-wise, Gojek ran the majority of
the ads ( 76.8%, or 849 ads), while Grab accounted for the
remaining 23.2% ( 271 ads).
Next, we annotated the clusters, generating names and
descriptions by prompting an LLM to do so based on the
predominant parameters and content of the posts associated
with each cluster. Finally, an image for each persona was
generated by the LLM in accordance with the persona’s
description. Fig. 4 shows the resulting three distinct clusters,
each representing a unique customer persona along with their
associated characteristics: “Efficiency Enthusiasts” (Persona
1), “Financial Empowerment Champions” (Persona 2), and
“Efficiency Innovators” (Persona 3), with content counts of
206, 144, and 707 respectively. Note that some content items
did not correspond to any of the three identified personas (i.e.,
represented outliers) and were thus excluded from the final
tally, explaining the disparity with the initial 1,120 ads.
As a result, notable distinctions between the personas have
emerged. Both Persona 1 and Persona 3 focus on organiza-
tional efficiency, albeit through different approaches: Persona
1 advocates for efficiency through traditional methodologies,
while Persona 3 champions it through innovative strategies. In
contrast, Persona 2 stands apart by primarily emphasizing the
need for financial empowerment of employees.
C. Communication Theme: Challenges
A persona is an essential but not sufficient component
needed to come up with a marketing story and content briefs.
In particular, it is important to identify a communication
scheme to be combined with the persona’s key attributes such
as background or character, so that the story would get proper
context and would grab attention [106]. To explore this, we
have performed X-Means clustering based on the “Insights”
content pillar, again using ADA embeddings for text [108] and
running X-Means with 3 starting centroids and kmax = 50.
Similarly to persona clustering, we annotated the resulting
challenge clusters and generated parameters such as cluster

Fig. 4. Sample persona analysis results
name and cluster description by prompting an LLM to do
so based on predominant parameters and content of the posts
associated with each cluster. Figure 5 shows sample results:
in this case, we have identified three distinct clusters, each
representing a unique customer challenge along with their
associated characteristics: “Inefficient Corporate Expense and
Transportation Management” (Challenge 1), “Improving Busi-
ness Operations and Employee Satisfaction” (Challenge 2),
and “Streamlining Work Transport Processes” (Challenge 3),
with content counts of 672, 94, and 336 respectively.
V. D ATA-D RIVEN STORY GENERATION
In order to establish a data-driven narrative that would be
useful, easy to understand, and attractive to content marketing
professionals, it is essential to delineate the content and mar-
keting strategies a brand may deploy, guided by the analysis
of the best-performing content from competitive brands. At
this point, we have already discussed how the SOMONITOR
framework extracts personas and challenges based on advertis-
Fig. 5. Sample challenges mined by our system
ing content prefiltered by a CTR prediction and ranking model.
Now it is time to combine them into a unified marketing story.
Consider the scenario where we are part of a marketing team
at Gojek, tasked with identifying a suitable communication
theme and a target persona for a campaign aimed at market
expansion through new audience engagement. It is desirable to
opt for a persona and theme that are presently underexploited,
thereby expanding our audience reach. As illustrated in Fig. 4,
the analysis shows that Persona 1, labeled “Efficiency Enthu-
siasts”, is more heavily leveraged by Grab than by Gojek,
indicating a potential niche opportunity for Gojek. At the same
time, as shown in Fig. 5, the communication theme “Challenge
3: Streamlining Work Transport Processes” is more frequently
addressed by our competitor, Grab, but is underrepresented in
Gojek’s content. This observation advocates for adopting this
theme for persona-centric narrative generation.
Consequently, adhering to the framework outlined in Fig-
ure 6, we prompt an LLM to amalgamate the characteris-
tics of the selected persona and the chosen communication
theme to devise a narrative for a fictitious character, “Samuel
Tan”, a business owner in Singapore. The pipeline for this
generation is shown in Figure 6: character description is also
generated by a custom-prompted LLM, and then the character
and theme are combined to create a compelling story. The
story is abbreviated in Fig. 6, in reality it explains over
several paragraphs how Samuel prioritizes business efficiency
but often neglects employee satisfaction, leading to increased

Fig. 6. User story generation: pipeline and an example.
turnover rates. Recognizing this issue, Samuel opts for Gojek
not merely as an efficiency solution but as a means to reengage
with employees, enhance their efficiency, and improve overall
job satisfaction; the story ends with a conclusion (emphasized
in Fig. 6) that shows an important insight that Samuel has
obtained by engaging with Gojek. This narrative could serve
as a content brief for a creative agency or be utilized as a
pitch for a novel marketing campaign, previously unexplored
by the marketing team in such depth and with such rapid
production capability. In our professional opinion, content
briefs produced by SOMONITOR are on par with similar
human-written narratives and can be used just as effectively.
VI. C ASE STUDY: DATA-D RIVEN STORY GENERATION
This section presents a case study evaluating the impact
of the proposed story generation approach on marketing
workflows across four organizations: NEO360, Blak Labs,
Bit by Bit Marketing, and Mothercare. These organizations
implemented the system, documented the time required for
routine tasks before and after adopting the story generation
approach, and reported substantial reductions in time spent
TABLE I
TIME SAVINGS WITH SEMANTIC ENRICHMENT APPROACH
Task Before (Hours) After (Hours)
NEO360 (Performance Agency)
Social Media Proposal Preparation 3.0 0.75
Competitor Monitoring 3.0 0.25
Audience Research 5.0 0.50
Brainstorming Ad Angles 2.5 0.25
Blak Labs (Creative Agency)
Campaign Planning 5.0 2.0
Content Planning 10.0 3.0
Brand Analysis 10.0 1.0
Bit by Bit Marketing (Branding Agency)
Content Strategy 5.0 1.0
Mothercare (Consumer Brand)
Competitor Analysis 5.0 2.0
Ad Compilation 5.0 1.0
Customer Segmentation 5.0 2.0
on key tasks such as content strategy, campaign planning,
competitor monitoring, and audience research. This evaluation
was conducted across multiple brands within agency settings
and for various product categories at Mothercare.
1) NEO360: Streamlining Performance Marketing:
NEO3601, a performance agency, implemented the semantic
enrichment approach to enhance workflows for tasks such as
social media preparation, competitor monitoring, audience
research, and brainstorming ad angles. As summarized in
Table I, the system reduced task durations by 2x to 3x;
e.g., the time required for social media proposal preparation
was reduced from 3 hours to 45 minutes, while competitor
monitoring was shortened from 3 hours to just 15 minutes,
showing radical acceleration of research-intensive tasks.
2) Blak Labs: Optimizing Creative Workflows: Blak Labs2,
a creative agency, leveraged the system to streamline campaign
planning, content planning, and brand analysis. The results,
shown in Table I, demonstrate time reductions of 2x to 3x.
Notable gains include reducing the time for brand analysis
from 10 hours to 1 hour and content planning from 10 hours
to 3 hours, proving that the platform can handle resource-
intensive creative processes.
3) Bit by Bit Marketing: Enhancing Branding Strategies:
Bit by Bit Marketing 3, a branding agency, used the semantic
enrichment approach to optimize its content strategy workflow.
Table I shows that the agency achieved a 5x reduction in time
spent on this task, from 5 hours to 1 hour; in this case, the
system was able to streamline strategic processes, enabling
agencies to focus on higher-level planning and execution.
4) Mothercare: Improving Consumer Brand Efficiency:
Mothercare4, a consumer brand, applied the system to optimize
1https://neo360.digital/
2https://blaklabs.com/
3https://bitbybitmarket.com/
4https://www.mothercare.com.sg

TABLE II
EXPERIMENTAL RESULTS FOR SOMONITOR.
Brand nDCG@5 nDCG@10 Recall@3 Recall@5
A 0.498 0.796 0.333 0.4
B 0.541 0.821 0.333 0.4
C 0.588 0.829 0.6 0.6
TABLE III
PERFORMANCE EVALUATION AGAINST LLM BASELINES ; “ GD”
REPRESENTS A GROUNDED MODEL .
nDCG@5 nDCG@10 Recall@3 Recall@5
GPT4-gd 0.591 0.818 0.333 0.6
GPT4 0.465 0.755 0 0.4
GPT4o-gd 0.599 0.827 0.333 0.6
GPT4o 0.511 0.750 0.333 0.4
Gemini-gd 0.578 0.817 0.333 0.6
Gemini 0.564 0.769 0 0.6
SOMONITOR 0.588 0.829 0.6 0.6
competitor analysis, ad compilation, and customer segmenta-
tion workflows. Table I highlights the 3x to 5x improvements
achieved; e.g., ad compilation time was reduced from 5 hours
to 1h, and customer segmentation tasks were completed in
less than half the time. These results validate our approach’s
versatility in enhancing productivity across diverse domains.
Results of this case study highlight the transformative
impact of data-driven story generation in marketing workflows.
Our LLM-based system not only reduces task durations but
also provides actionable insights for optimizing operations.
The proposed platform can address real-world challenges and
enable marketers to achieve huge productivity gains while
maintaining high-quality outcomes. This evidence strongly
supports the adoption of semantic enrichment and data-driven
content optimization in marketing practices.
VII. C ONTENT SCORING
A. Problem setting and dataset
To make actionable recommendations, one has to enable
marketers to evaluate data and select which content to incor-
porate into analytics, ideally based on anticipated performance.
This leads to the need for content scoring, so in this section we
add to SOMONITOR a system for the scoring of advertising
content, developed in our previous work [97], and evaluate it
against state of the art LLMs to prove its continued relevance.
To assess the effectiveness of our recommender system,
we conducted a validation study using real ad creatives and
their performance data. We collected real-world ad creatives
and their performance data from three brands on Facebook,
each with distinct marketing objectives: sales, conversion, and
traffic, spanning from October 1, 2023 to December 31, 2023.
The dataset comprised text and images of their ads alongside
their performance measured as CTR values. We chose three
(anonymized) brands: Brand A (16 ads in the fitness industry),
Brand B (29 ads in the education industry), and Brand C (16
ads in the automobile industry).
The ads were assessed not just according to the brand affil-
iation, but also according to the Ad objective selected on the
Meta Ads platform, which is a crucial component of evaluation
in our scenario due to the fundamental differences in click-
through rates across various industries and marketing goals
that Ads achieve with different Ad objective settings [97]. For
instance, advertisements optimized for clicks may result in
lower costs per click and higher click-through rates, yet they
may not effectively convert customers. Conversely, ads aimed
at achieving better conversion rates might not exhibit as high
click-through rates as those optimized merely for clicks.
B. Content scoring models
We use our previously developed content scoring ap-
proach [97]; it was originally designed to predict CTR by
classifying ads into CTR performance categories but here
we operate in a recommendation setting, i.e., pose content
scoring as a ranking problem because (i) marketers do not
need precise CTR values to choose the best content but rather
a comparative assessment, (ii) CTR values undergo significant
distribution shift across platforms, time, and other external
factors, but the ranking of ads should be more stable, and
(iii) the LLM performance in qualitative ranking should be
significantly better than in numerical predictions.
Thus, we take the SODA model from [97] that predicts
a distribution over “High CTR”, “Average CTR”, and “Low
CTR” labels and add a linear layer that translates the proba-
bilities into a single score via a trainable linear combination:
Score =α · p(HighCTR) +β · (1 − p(HighCTR)),
converting a classification model into a ranking model.
On the side of LLMs, we used GPT-4 [99], its latest
multimodal variant GPT-4o, and Gemini 1.5 Pro [17] for com-
parison with SOMONITOR. A significant challenge in utilizing
LLMs for this task is their tendency to hallucinate, which
can result in generating inaccurate or nonsensical information
that compromises the reliability of their output. To mitigate
this issue and ground the LLM-based approach to ensure
the predicted data was trustworthy, we implemented several
measures to reduce randomness: (i) temperature adjustment,
setting the temperature parameter of the LLMs to 0.1, which
is known to improve stability by reducing the variability in the
model’s outputs; (ii) grounding, i.e., including another three
sample ads from the brand within the prompt, each with a
specified CTR rank: one with the best performance, one with
average performance, and one with the worst performance;
(iii) ensembling, running the ranking process with LLMs five
times in the same settings and ranking the ads by the (lowest
to highest) sums of their ranks from all runs.
C. Results
For evaluation, we use standard ranking-based metrics,
namely Recall@3 and Recall@5. Recall is very important in
practice, especially in resource-constrained domains such as
online advertising campaigns, where top k recommendations
should encompass a substantial portion of the truly relevant

items, so that marketers can focus their efforts on the most
promising opportunities. We have also computed normalized
discounted cumulative gain (nDCG) at cutoffs 5 and 10,
another commonly used way to assess ranking quality. Table II
shows a case study across three major industries. In the
fitness sector, SOMONITOR achieved moderate effectiveness
with nDCG@5 of 0.498 and nDCG@10 of 0.796, alongside
Recall@3 and Recall@5 scores of 0.333 and 0.4, respectively.
Brand B, representing education, showed improved perfor-
mance, with nDCG@5 of 0.541 and nDCG@10 of 0.821, but
recall stayed the same. In the automobile industry results im-
proved, achieving nDCG@5 of 0.588 and nDCG@10 of 0.829,
with recall@3 and recall@5 both scoring 0.6. These findings
show that content scoring quality varies across industries and
highlight the importance of industry-specific optimization to
enhance recommendation accuracy.
Then we evaluated SOMONITOR against LLM baselines.
In campaigns focused on driving traffic, the primary goal is to
maximize click-through rates (CTR), which serve as a measure
of user engagement and interaction with the advertisement,
which is particularly pertinent given the distinctive challenges
posed by traffic-driven campaigns as opposed to conversion-
oriented strategies. Thus, we evaluate the performance with
the data from Brand C, a traffic-oriented campaign. Table III
presents the results from a case study focused on Brand C,
comparing the performance of SOMONITOR against modern
LLMs. It shows a significant performance boost achieved by
knowledge grounding across various models and metrics; e.g.,
nDCG@5 for GPT-4 improved from 0.465 without grounding
to 0.591 with grounding, while its Recall@5 increased from
0.4 to 0.6. This also holds for GPT-4o and Gemini1.5 Pro,
showing that grounding is critical in enhancing the relevance
and quality of recommendations. Ungrounded LLMs exhibit
markedly lower performance, particularly in the Recall@3
metric: both Gemini and GPT-4 failed to place any high-
performance items within their top 3 results at all.
As a result, the prediction model outperforms LLMs in rec-
ommending relevant items, achieving the highest nDCG@10
of 0.829 and recall@3 of 0.6 among compared models.
SOMONITOR is better able to balance ranking accuracy and
item recall, delivering highly relevant and stable (especially
compared to individual LLM results) recommendations to
users. Notably, these outcomes are achieved without any
fine-tuning (grounding) using data from the actual industry-
specific distributions: we used a pretrained model. This offers
significant potential for further improvement of results should
such fine-tuning be implemented, a direction we intend to
explore in our future work. Improvements in LLMs’ Recall@k
due to grounding also hint at the critical role of domain
knowledge and context in enhancing the relevance and quality
of recommendations. Ungrounded LLMs, relying solely on
their pre-trained language models, struggle to capture the
nuances and specifics of the recommendation task, resulting
in sub-optimal item retrieval. By incorporating domain-specific
knowledge and grounding the models in the relevant context,
the recommendations become more tailored and relevant.
We note that our proposed SOMONITOR framework outper-
forms the baselines in both Recall@3 and Recall@5, achieving
a Recall@3 score of 0.6 which is higher than any LLM’s
result. This supports our conclusion that the online marketing
industry still cannot fully rely on LLMs for content scoring and
explains our decision to include a CTR prediction and ranking
model into the mostly LLM-based SOMONITOR framework.
VIII. Q UANTITATIVE EVALUATION AND CASE STUDY
We have shown that a small neural network can outperform
one-shot fine-tuned LLMs in predicting content performance
prior to the official release of advertisements. However, for this
solution to be practical for marketers it must not only identify
what works better but also provide actionable guidance on
how to improve the content. We have noted before [97] that
attention layers of the content scoring network can be visual-
ized to assist marketers in refining their content iteratively, but
have not tested it in real world conditions until now. In this
section, we evaluate this approach with the Meta advertising
engine, aiming (1) to assess whether regions highlighted by
attention heatmaps correlate with higher user engagement and
(2) to determine whether removing key objects identified by
heatmaps adversely affects campaign performance.
A. Experimental Setup and Methodology
We used a diverse dataset of advertising creatives with
multiple visual elements and processed them through our
predictive framework, which generated attention heatmaps to
identify areas likely to maximize user engagement.
Selection of Creative Assets: only creatives with high-
confidence predictions (above the model’s average confidence
threshold) were included in the experiment. This ensured that
selected assets featured impactful elements, allowing for a
focused assessment of the heatmap’s predictive capabilities.
We used the following experimental workflow:
1) heatmap generation: each creative was processed with
SoWide-v2, to generate heatmaps (Fig. 7), highlighting
elements expected to drive user engagement;
2) iterative object removal: based on the heatmaps, critical
objects were sequentially removed, and updated heatmaps
were generated after each iteration; this process produced
three modified versions of each original creative;
3) campaign deployment: original and modified creatives
were deployed in a real-world campaign on the Meta
platform with identical settings ( Objective: Landing Page
View; Placements: All; Budget Control : automatic; Ad
Copy: ”Unlock Game-Changing Marketing Insights in
Seconds with SOMONITOR”; Duration: 1 day);
4) performance metrics: key performance indicators such
as click-through rate (CTR), click-to-landing page view
(CTR-LPV), and landing page views (LPV) were moni-
tored for all creatives, with a total of 65,107 impressions,
2,243 clicks, and 1,162 landing page loads recorded;
5) performance analysis: to quantify the impact of object
removal, we counted the proportion of cases where per-
formance declined after object removal.

Fig. 7. Visualization of object removal guided by attention heatmaps.
Fig. 8. Example of an ad variant deployed on the Meta platform.
TABLE IV
EVALUATING OBJECT REMOVAL IN A REAL -WORLD CAMPAIGN
Layout LPV CTR-LPV CTR F1 Score
Layout 1 0.769 0.769 0.692 0.750
Layout 2 0.751 0.751 0.250 0.500
Layout 3 0.570 0.857 0.857 0.860
Overall 0.708 0.792 0.667 0.740
B. Results and Observations
Experimental results summarized in Table IV show the
efficacy of heatmaps for guiding ad optimization:
• Layout 1: Moderate performance with well-aligned LPV
and CTR-LPV values (0.769), indicating consistent user
engagement. The F1 score (0.750) suggests accurate
predictions of ad performance.
• Layout 2: Significantly lower CTR (0.250) shows prob-
lems in attracting initial clicks despite robust post-click
engagement (CTR-LPV 0.751), reflecting the model’s
limitations in detecting less impactful visual cues.
• Layout 3: The highest CTR-LPV (0.857) and F1 score
(0.860) demonstrate strong alignment between predicted
and actual user engagement. However, lower LPV (0.570)
indicates potential gaps in predicting post-click retention.

C. Impact of Object Removal
Systematic removal of key visual elements led to the fol-
lowing results: (i) removing the CTA Button caused a 22%
drop in CTR, showing its importance in driving engagement.
(ii) removing transparent background led to the most severe
performance decline, with a 64% drop in CTR, highlighting its
influence in guiding user attention; (iii) removing the primary
visual element resulted in a 58% CTR drop, demonstrating
its significance in capturing initial user attention. The model’s
predictions are closely aligned with observed performance.
IX. G EN-AI P ERFORMANCE MARKETING CONSULTANT
We have been exploring strategies that enable marketers to
enhance their content efforts, as well as prevalent trends in
content marketing. However, major companies like Procter
& Gamble or McDonald’s often undergo rigorous reviews
before altering creative materials or ad copy. This can make
proposed improvements to advertising content impractical,
as the targeted campaign may end before suggestions are
implemented. When creative changes are unfeasible, real-time
campaign optimization becomes essential. Even for campaigns
with high-quality creatives, this approach ensures precise
alignment of creatives with target audiences and helps identify
performance bottlenecks through detailed data analysis. In
this section, we discuss how LLM-based analysis can help
evaluate key performance metrics and guide strategic decisions
in campaign optimization, connecting the micro-level analysis
of ad creatives with the macro-level approach of the LLM
helping steer the course of the entire advertising campaign.
A. Metrics for Measuring Campaign Performance
We expand the focus from ad creative analysis to a holistic
view of campaign performance using several key metrics:
• Reach: total unique individuals exposed to the campaign,
indicating its audience breadth and potential impact on
brand visibility and awareness.
• Frequency: average number of times a user sees the ad;
tracking it is needed to avoid audience fatigue [109];
• Results: total targeted conversions (e.g., leads or pur-
chases), the primary measure of campaign success;
• Cost per Result : average cost per conversion, reflecting
campaign efficiency and guiding budget optimization;
• Amount Spent: total expenditure, needed for budget track-
ing and ensuring alignment with campaign goals;
• CPM (Cost per 1,000 Impressions): cost of reaching
1,000 users informs about market competition [110];
• CTR (Click-Through Rate), the prediction target for our
SoWide-v2 model (Section VII); it assesses ad engage-
ment and content effectiveness;
• CR for Link Clicks to LP Views : fraction of users who
click the ad and view the landing page, indicating landing
page effectiveness;
• CR for Link Clicks to Results : fraction of users clicking
the ad who achieve the targeted conversion, directly
reflecting campaign goal attainment.
These metrics collectively provide a comprehensive view of
campaign performance, encompassing audience engagement,
conversion rates, budget efficiency, and ad quality, enabling
informed optimization decisions.
B. Data Acquisition and Preprocessing
Metrics data for the Meta campaign were collected over a
three-month period (October 1, 2023 – January 23, 2024) at
three levels of granularity: (i) weekly, which provides a con-
solidated view by smoothing short-term fluctuations (Fig. 10);
(ii) daily, which offers detailed insights into day-to-day vari-
ations essential for detecting anomalies or immediate external
influences, and at the (iii) creative level, which evaluates the
contribution of individual creatives to campaign performance.
To adapt data for LLM analysis, it was preprocessed as
follows: (i) creative data represented as tabulated insights with
images resized to 512 × 512 pixels and encoded in base64;
(ii) numerical metrics , as percentage change rates between
consecutive data points to focus on trends and fluctuations
rather than raw values. This preprocessing ensures that metrics,
diverse in granularity and spanning over 115 days, are strate-
gically well-structured for comprehensive campaign analysis.
C. Prompt Engineering
Automated campaign performance analysis requires a well-
crafted prompt in order to guide the LLM through a compre-
hensive evaluation of key metrics and their interdependencies.
Our prompt format follows the convention of Knowledge +
Role + Task + Data and provides the necessary context and
information for the LLM’s analysis.
Knowledge of Campaign Metrics: Evaluation metrics span
different facets of an ad campaign, from audience engagement
to cost efficiency; they are explained in detail in the prompt
and include Reach, Frequency, Results, Cost per Result,
Amount Spent, CPM, CTR, CR Link Clicks to LP View, and
CR Link Clicks to Result (see Section IX-A). Each metric
serves a distinct purpose in evaluating campaign performance
and offers valuable insights into audience interaction, cost-
effectiveness, and conversion rates.
Role of the LLM: The prompt also defines the specific
role that the LLM is supposed to play, namely operate as
a surrogate performance marketing manager. The LLM is
expected to embody confidence in its analyses, refraining from
speculative language such as “could be” or “might be”. In this
simulated role, the LLM is entrusted with the responsibility of
scrutinizing performance metrics and providing well-founded
explanations for observed trends. This confidence aligns with
the typical expertise and authority of a seasoned performance
marketing professional, which improves the resulting analysis.
Task Definition for the LLM: The task assigned to the LLM
is explicitly outlined in the prompt. The primary objective is
to achieve a lower CPR, and the manager dynamically adjusts
the budget to optimize this metric. The task involves not only
tracking changes in key metrics such as CPR and Spend but
also understanding the trends in secondary metrics such as
CTR, CPM, CR, and CR Link Clicks to LP View.

Fig. 9. Performance comparison of creatives after object removal.
TABLE V
SAMPLE AD CAMPAIGN ANALYSIS RESULTS BY GPT-4
1) Key Metrics Change: Both CPR (Cost Per Result) and SPEND
did change over the course of the campaign.
2) Key Metrics Trend:
• CPR started at $57.01, decreased to $33.08 at its lowest point,
spiked to $208.28, and then decreased again to $27.68 before
rising to $115.98. The trend indicates a fluctuation in cost
efficiency, with an overall decrease towards the middle of the
campaign followed by a substantial increase towards the end.
• SPEND varied significantly, with an initial value of $2565.39,
rising to $4664.91, then dropping to $175.18, and finally in-
creasing to $695.91. The campaign budget was dynamically
adjusted, leading to these variations.
3) Secondary Metrics Trend :
• CTR (Click-Through Rate) fluctuated, starting at 2.68%, peak-
ing at 3.59%, and ending at 2.24%. Changes in CTR indicate
varying levels of user engagement with the ads.
• CPM (Cost per 1,000 Impressions) decreased to $9.98, spiked
to $14.06, and then dropped to $6.13 before rising again to
$11.75. This suggests that ad performance and competition for
audience attention were inconsistent.
• CR (Conversion Rate) and CR Link Clicks to LP View showed
fluctuations, with a general downward trend towards the end of
the campaign. This could indicate a decrease in ad relevance or
landing page effectiveness.
4) Relation between Key and Secondary Metrics : The increase in
CTR typically suggests more effective ad content, which should
lower CPR by generating more leads or purchases for the same
or less spend. However, the spike in CPM indicates a higher cost
to reach the audience, which can increase CPR if the rise in ad
costs is not offset by a proportionate increase in purchases. The
downward trend in conversion rates, both overall and from link
clicks to landing page views, directly contributes to a higher CPR,
as fewer users who click the ad proceed to purchase.
5) Impact of Secondary Metrics on Primary Metrics: CTR directly
influences CPR; a higher CTR means more clicks for the budget,
increasing the opportunity for conversions and potentially lowering
the CPR if the conversion rate is stable or improves. Conversely,
an increase in CPM raises the cost to gain impressions, potentially
increasing the CPR if not balanced by a rise in conversion rates.
The conversion rate from link clicks to landing page views is
pivotal; a decrease suggests that users are less compelled by the
landing page to make a purchase, thus increasing CPR.
The correlation is clear: while a higher CTR and improved landing
page conversion rates contribute to a lower CPR, increases in CPM
or declines in conversion rates can negate these benefits, leading
to a higher CPR. The data shows fluctuations in CTR and CPM,
alongside a general decrease in conversion rates, explaining the
observed changes in CPR.
6) Hypothesis for Changes in Primary Metrics :
• The initial decrease in CPR can be attributed to the campaign’s
optimization and improvements in ad targeting, leading to a
more engaged audience and more efficient spending.
• The spike in CPR could be due to market dynamics, such as
increased competition, leading to higher costs for reaching the
audience.
• The subsequent decrease in CPR and then increase suggests
that the audience may have experienced ad fatigue, resulting in
lower conversion rates and higher costs per purchase.
7) Analysis of Textual and Visual Data of Ads :
• The ad’s textual content is clear and direct, with a focus on the
Keto diet, which is relevant to the target audience. However,
the visual content, while appealing, does not directly link to the
desired action of taking a quiz or making a purchase.
• To improve the key metrics, I recommend testing variations of
the ad copy that directly address the benefits of the Keto diet
and include a strong call-to-action. Additionally, using visuals
that better represent the quiz or the benefits of following the
Keto diet may improve conversion rates.
8) Recommendation for Next Steps :
• Monitor the CTR and conversion rates closely and test different
ad creatives to find the most engaging content for the audience.
• Analyze the times when CPM spikes to determine if there are
patterns related to increased competition and adjust bidding
strategies accordingly.
• Review the landing page experience to ensure it is optimized
for conversions, with fast load times and clear calls-to-action.
• Consider retargeting campaigns to engage users who have
previously interacted with the ads but have not converted, using
tailored messaging based on their interaction stage.
• Allocate budget dynamically, but with caution during periods of
high CPM to avoid inefficiency, focusing more on periods with
lower CPM and higher engagement.

Fig. 10. Data for Section IX-B: (a) weekly performance; (b) a sample creative.
Key Questions for LLM Analysis: To guide the LLM
through a systematic analysis, we present in the prompt a set of
key questions inspired by the routine thought process of an ad
optimization manager. These questions include the following.
1) Did the key metrics (CPR, SPEND) change?
2) If they changed, summarize the trend of the key metrics.
3) What was the trend of secondary metrics (CTR, CPM,
CR, CR Link Clicks to LP View) during the same time?
4) Are the changes in key and secondary metrics related?
5) Which secondary metrics influence the key metrics?
6) Provide hypotheses to explain the changes in key metrics.
7) Analyze textual and visual data of ads to explain key
metric changes and recommend improvements.
8) Recommend the next steps for campaign performance
improvement based on the metrics.
Tabular Data Integration: The prompt is enriched with
tabular data that contains both numerical values of metrics
and detailed creative features of the ads. This allows the LLM
to analyze both quantitative and qualitative aspects, grounding
its understanding of the campaign performance and helping
generate actionable recommendations for optimization.
Visual Data Integration: In addition to text and tabular data,
we included the ads’ visuals to enrich contextual information
within the prompt. Thus, a multimodal LLM such as GPT-4
(that we used in the experiments) can not only comprehend
textual nuances but also mine insights from the visual contents
of the campaign, again leading to a more holistic understand-
ing of the relations between creative content and performance.
D. Analysis of the Results
Here, we present the LLM-based analysis for performance
metrics evaluation in the specified marketing campaign. The
examination primarily focuses on key metrics, such as CPR
and Amount Spent, alongside with secondary metrics like
CTR, CPM, CR, and CR Link Clicks to LP View. The goal
is to uncover insights into the dynamics of the campaign
and provide actionable recommendations for improvement.
LLM results are shown in Table V. The LLM’s outputs
demonstrate its proficiency in annotating data and accurately
detailing variations in key metrics, as seen in points 1, 2,
and 3. This capability is important for understanding recent
campaign performances and for summarizing critical data for
marketing managers in preparation for reporting meetings.
Moreover, the model is quite adept in identifying the root
causes of increasing the cost per result metric. It points
out the decline in conversion rates and the rise in CPM in
points 4 and 5 as contributing factors. In point 6, the LLM
goes further, recognizing potential issues such as ad fatigue,
ad targeting optimization, and market seasonality. This is
especially important because these aspects were not explicitly
input in the prompt or data, indicating the model’s ability to
extract new insights. In a manner similar to the analysis in
Section VII, point 7 discusses potential enhancements in visual
content and explores the reasons for its current inefficiency.
However, point 8 shows a limitation: suggestions provided
there are quite generic and may not fully align with the specific
needs of the keto diet campaign. These recommendations
should be customized to better suit the unique aspects of
the campaign. Despite these limitations, the analysis provided
by the LLM in this example proves to be a valuable asset
for digital marketing professionals, offering quick evaluations
and identifying potential areas for optimization across various
campaigns. Initial recommendations provided by our platform
are especially helpful for early-career marketers and serve well
for educational purposes. However, more advanced marketing
professionals may require more specific and detailed insights,
which we plan to explore in future research.
X. C ONCLUSION
In this work, we have introduced an innovative explainable
AI framework SOMONITOR that aims to combine human
intuition with the efficiency of modern AI to significantly
enhance the capabilities of marketers across all stages of the
marketing funnel, from strategic planning to content creation
and campaign execution. The challenges traditionally faced
by marketers, especially the need to manually sift through
immense quantities of transient online content, are addressed
by SOMONITOR’s ability to automate and refine the pro-
cess of competitor analysis, content research, and strategic
branding, which has been proven by a case study in the
real-world settings. SOMONITOR ranks advertising content
by its potential to achieve higher click-through rates via a
specially trained model and then employs LLMs to distill
core content pillars, which lead to communication themes and
targeted customer personas, providing a structured basis for
content and campaign planning. By integrating these insights
with brand marketing data, SOMONITOR not only constructs
compelling narratives for new customer personas but also
generates detailed content briefs in the form of customer per-
sona stories, empowering marketing teams to produce content
and execute campaigns in a guided manner, which has been
proven to help in prioritizing different content elements and
enhance real-world advertising performnace. We believe that
SOMONITOR can transform digital marketing operations, en-
abling marketers to quickly navigate through large datasets and
derive actionable insights that boost campaign effectiveness
and enhance job satisfaction, redefining traditional marketing
approaches [111].

XI. A CKNOWLEDGEMENT
This work was funded by the Russian Science Foundation
grant №. 22-11-00135, https://rscf.ru/en/project/22-11-00135/
REFERENCES
[1] S. Makridakis, F. Petropoulos, and Y . Kang, “Large language models:
Their success and impact,” Forecasting, vol. 5, no. 3, pp. 536–549,
2023. [Online]. Available: https://www.mdpi.com/2571-9394/5/3/30
[2] S. Minaee, T. Mikolov, N. Nikzad, M. Chenaghlu, R. Socher, X. Am-
atriain, and J. Gao, “Large language models: A survey,” 2024.
[3] M. Enis and M. Hopkins, “From llm to nmt: Advancing low-resource
machine translation with claude,” 2024.
[4] M. C. et al., “Evaluating large language models trained on code,” 2021.
[5] A. Q. J. et al., “Mistral 7b,” 2023.
[6] D. Kevian, U. Syed, X. Guo, A. Havens, G. Dullerud, P. Seiler,
L. Qin, and B. Hu, “Capabilities of large language models in control
engineering: A benchmark study on gpt-4, claude 3 opus, and gemini
1.0 ultra,” 2024.
[7] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones,
A. N. Gomez, L. Kaiser, and I. Polosukhin, “Attention is all
you need,” CoRR, vol. abs/1706.03762, 2017. [Online]. Available:
http://arxiv.org/abs/1706.03762
[8] I. Beltagy, M. E. Peters, and A. Cohan, “Longformer: The long-
document transformer,” 2020.
[9] R. Child, S. Gray, A. Radford, and I. Sutskever, “Generating long
sequences with sparse transformers,” 2019.
[10] S. Wang, B. Z. Li, M. Khabsa, H. Fang, and H. Ma, “Linformer: Self-
attention with linear complexity,” 2020.
[11] K. Choromanski, V . Likhosherstov, D. Dohan, X. Song, A. Gane,
T. Sarlos, P. Hawkins, J. Davis, A. Mohiuddin, L. Kaiser, D. Belanger,
L. Colwell, and A. Weller, “Rethinking attention with performers,”
2022.
[12] A. Gu and T. Dao, “Mamba: Linear-time sequence modeling
with selective state spaces,” in First Conference on Language
Modeling, 2024. [Online]. Available: https://openreview.net/forum?id=
tEYskw1VY2
[13] H. Qu, L. Ning, R. An, W. Fan, T. Derr, H. Liu, X. Xu,
and Q. Li, “A survey of mamba,” 2024. [Online]. Available:
https://arxiv.org/abs/2408.01129
[14] S. Bansal, S. A, M. P. J, M. S, S. Madisetty, M. Z. U. Rehman,
C. S. Raghaw, G. Duggal, and N. Kumar, “A comprehensive survey
of mamba architectures for medical image analysis: Classification,
segmentation, restoration and beyond,” 2024. [Online]. Available:
https://arxiv.org/abs/2410.02362
[15] X. Ma, C. Zhou, X. Kong, J. He, L. Gui, G. Neubig, J. May, and
L. Zettlemoyer, “Mega: Moving average equipped gated attention,”
2023.
[16] A. Orvieto, S. L. Smith, A. Gu, A. Fernando, C. Gulcehre,
R. Pascanu, and S. De, “Resurrecting recurrent neural networks for
long sequences,” in Proceedings of the 40th International Conference
on Machine Learning, ser. Proceedings of Machine Learning Research,
A. Krause, E. Brunskill, K. Cho, B. Engelhardt, S. Sabato, and
J. Scarlett, Eds., vol. 202. PMLR, 23–29 Jul 2023, pp. 26 670–26 698.
[Online]. Available: https://proceedings.mlr.press/v202/orvieto23a.html
[17] G. Team, “Gemini 1.5: Unlocking multimodal understanding across
millions of tokens of context,” 2024.
[18] Anthropic, “Introducing the next generation of claude,” https://www.
anthropic.com/news/claude-3-family, 2024.
[19] Y . Tang, J. Bi, S. Xu, L. Song, S. Liang, T. Wang, D. Zhang, J. An,
J. Lin, R. Zhu, A. V osoughi, C. Huang, Z. Zhang, F. Zheng, J. Zhang,
P. Luo, J. Luo, and C. Xu, “Video understanding with large language
models: A survey,” 2024.
[20] OpenAI, “Hello gpt-4o,” https://openai.com/index/hello-gpt-4o/, 2024.
[21] J. Ho, A. Jain, and P. Abbeel, “Denoising diffusion probabilistic
models,” in Advances in Neural Information Processing Systems ,
H. Larochelle, M. Ranzato, R. Hadsell, M. Balcan, and H. Lin, Eds.,
vol. 33. Curran Associates, Inc., 2020, pp. 6840–6851.
[22] J. Song, C. Meng, and S. Ermon, “Denoising diffusion implicit mod-
els,” in International Conference on Learning Representations , 2021.
[Online]. Available: https://openreview.net/forum?id=St1giarCHLP
[23] R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer,
“High-resolution image synthesis with latent diffusion models,” in
Proceedings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition (CVPR), June 2022, pp. 10 684–10 695.
[24] J. Ho, W. Chan, C. Saharia, J. Whang, R. Gao, A. Gritsenko, D. P.
Kingma, B. Poole, M. Norouzi, D. J. Fleet, and T. Salimans, “Imagen
video: High definition video generation with diffusion models,” 2022.
[25] W. Hong, M. Ding, W. Zheng, X. Liu, and J. Tang, “Cogvideo: Large-
scale pretraining for text-to-video generation via transformers,” 2022.
[26] Y . Liu, K. Zhang, Y . Li, Z. Yan, C. Gao, R. Chen, Z. Yuan, Y . Huang,
H. Sun, J. Gao, L. He, and L. Sun, “Sora: A review on background,
technology, limitations, and opportunities of large vision models,”
2024.
[27] D. Kocetkov, R. Li, L. B. allal, J. LI, C. Mou, Y . Jernite, M. Mitchell,
C. M. Ferrandis, S. Hughes, T. Wolf, D. Bahdanau, L. V . Werra,
and H. de Vries, “The stack: 3 TB of permissively licensed source
code,” Transactions on Machine Learning Research , 2023. [Online].
Available: https://openreview.net/forum?id=pxpbTdUEpD
[28] L. Gao, S. Biderman, S. Black, L. Golding, T. Hoppe, C. Foster,
J. Phang, H. He, A. Thite, N. Nabeshima, S. Presser, and
C. Leahy, “The pile: An 800GB dataset of diverse text for language
modeling,” CoRR, vol. abs/2101.00027, 2021. [Online]. Available:
https://arxiv.org/abs/2101.00027
[29] J. M. Patel and J. M. Patel, “Introduction to common crawl
datasets,” Getting structured data from the internet: running web
crawlers/scrapers on a big data production scale , pp. 277–324, 2020.
[30] Y . Tokpanov, B. Millidge, P. Glorioso, J. Pilault, A. Ibrahim,
J. Whittington, and Q. Anthony, “Zyda: A 1.3t dataset for open
language modeling,” 2024. [Online]. Available: https://arxiv.org/abs/
2406.01981
[31] A. S. Luccioni and J. D. Viviano, “What’s in the box? an analysis
of undesirable content in the common crawl corpus,” CoRR, vol.
abs/2105.02732, 2021. [Online]. Available: https://arxiv.org/abs/2105.
02732
[32] J. W. Rae, S. Borgeaud, T. Cai, K. Millican, J. Hoffmann, H. F.
Song, J. Aslanides, S. Henderson, R. Ring, S. Young, E. Rutherford,
T. Hennigan, J. Menick, A. Cassirer, R. Powell, G. van den
Driessche, L. A. Hendricks, M. Rauh, P. Huang, A. Glaese, J. Welbl,
S. Dathathri, S. Huang, J. Uesato, J. Mellor, I. Higgins, A. Creswell,
N. McAleese, A. Wu, E. Elsen, S. M. Jayakumar, E. Buchatskaya,
D. Budden, E. Sutherland, K. Simonyan, M. Paganini, L. Sifre,
L. Martens, X. L. Li, A. Kuncoro, A. Nematzadeh, E. Gribovskaya,
D. Donato, A. Lazaridou, A. Mensch, J. Lespiau, M. Tsimpoukelli,
N. Grigorev, D. Fritz, T. Sottiaux, M. Pajarskas, T. Pohlen, Z. Gong,
D. Toyama, C. de Masson d’Autume, Y . Li, T. Terzi, V . Mikulik,
I. Babuschkin, A. Clark, D. de Las Casas, A. Guy, C. Jones,
J. Bradbury, M. J. Johnson, B. A. Hechtman, L. Weidinger, I. Gabriel,
W. Isaac, E. Lockhart, S. Osindero, L. Rimell, C. Dyer, O. Vinyals,
K. Ayoub, J. Stanway, L. Bennett, D. Hassabis, K. Kavukcuoglu, and
G. Irving, “Scaling language models: Methods, analysis & insights
from training gopher,” CoRR, vol. abs/2112.11446, 2021. [Online].
Available: https://arxiv.org/abs/2112.11446
[33] Y . Elazar, A. Bhagia, I. H. Magnusson, A. Ravichander, D. Schwenk,
A. Suhr, E. P. Walsh, D. Groeneveld, L. Soldaini, S. Singh,
H. Hajishirzi, N. A. Smith, and J. Dodge, “What’s in my
big data?” in The Twelfth International Conference on Learning
Representations, 2024. [Online]. Available: https://openreview.net/
forum?id=RvfPnOkPV4
[34] K. Lee, D. Ippolito, A. Nystrom, C. Zhang, D. Eck, C. Callison-Burch,
and N. Carlini, “Deduplicating training data makes language models
better,” in Proceedings of the 60th Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Papers) , S. Muresan,
P. Nakov, and A. Villavicencio, Eds. Dublin, Ireland: Association
for Computational Linguistics, May 2022, pp. 8424–8445. [Online].
Available: https://aclanthology.org/2022.acl-long.577
[35] S. Min, S. Gururangan, E. Wallace, W. Shi, H. Hajishirzi, N. A.
Smith, and L. Zettlemoyer, “SILO language models: Isolating legal
risk in a nonparametric datastore,” in The Twelfth International
Conference on Learning Representations , 2024. [Online]. Available:
https://openreview.net/forum?id=ruk0nyQPec
[36] Z. Yu, Y . Wu, N. Zhang, C. Wang, Y . V orobeychik, and C. Xiao,
“CodeIPPrompt: Intellectual property infringement assessment of code
language models,” in Proceedings of the 40th International Conference
on Machine Learning, ser. Proceedings of Machine Learning Research,

A. Krause, E. Brunskill, K. Cho, B. Engelhardt, S. Sabato, and
J. Scarlett, Eds., vol. 202. PMLR, 23–29 Jul 2023, pp. 40 373–40 389.
[Online]. Available: https://proceedings.mlr.press/v202/yu23g.html
[37] P. Samuelson, “Generative ai meets copyright,” Science, vol.
381, no. 6654, pp. 158–161, 2023. [Online]. Available: https:
//www.science.org/doi/abs/10.1126/science.adi0656
[38] S. Longpre, L. Hou, T. Vu, A. Webson, H. W. Chung, Y . Tay, D. Zhou,
Q. V . Le, B. Zoph, J. Wei, and A. Roberts, “The flan collection: design-
ing data and methods for effective instruction tuning,” inProceedings of
the 40th International Conference on Machine Learning, ser. ICML’23.
JMLR.org, 2023.
[39] M. Conover, M. Hayes, A. Mathur, J. Xie, J. Wan, S. Shah,
A. Ghodsi, P. Wendell, M. Zaharia, and R. Xin. (2023) Free
dolly: Introducing the world’s first truly open instruction-tuned
llm. [Online]. Available: https://www.databricks.com/blog/2023/04/12/
dolly-first-open-commercially-viable-instruction-tuned-llm
[40] V . Sanh, A. Webson, C. Raffel, S. Bach, L. Sutawika, Z. Alyafeai,
A. Chaffin, A. Stiegler, A. Raja, M. Dey, M. S. Bari, C. Xu,
U. Thakker, S. S. Sharma, E. Szczechla, T. Kim, G. Chhablani,
N. Nayak, D. Datta, J. Chang, M. T.-J. Jiang, H. Wang, M. Manica,
S. Shen, Z. X. Yong, H. Pandey, R. Bawden, T. Wang, T. Neeraj,
J. Rozen, A. Sharma, A. Santilli, T. Fevry, J. A. Fries, R. Teehan,
T. L. Scao, S. Biderman, L. Gao, T. Wolf, and A. M. Rush,
“Multitask prompted training enables zero-shot task generalization,” in
International Conference on Learning Representations, 2022. [Online].
Available: https://openreview.net/forum?id=9Vrb9D0WI4
[41] Y . Liu, S. Tao, X. Zhao, M. Zhu, W. Ma, J. Zhu, C. Su, Y . Hou,
M. Zhang, M. Zhang, H. Ma, L. Zhang, H. Yang, and Y . Jiang,
“Coachlm: Automatic instruction revisions improve the data quality in
llm instruction tuning,” in 2024 IEEE 40th International Conference
on Data Engineering (ICDE) , 2024, pp. 5184–5197.
[42] W. Ni, K. Zhang, X. Miao, X. Zhao, Y . Wu, and J. Yin, “Iterclean:
An iterative data cleaning framework with large language models,”
in Proceedings of the ACM Turing Award Celebration Conference -
China 2024, ser. ACM-TURC ’24. New York, NY , USA: Association
for Computing Machinery, 2024, p. 100–105. [Online]. Available:
https://doi.org/10.1145/3674399.3674436
[43] Y . Wang, S. Mishra, P. Alipoormolabashi, Y . Kordi, A. Mirzaei,
A. Arunkumar, A. Ashok, A. S. Dhanasekaran, A. Naik, D. Stap,
E. Pathak, G. Karamanolakis, H. G. Lai, I. Purohit, I. Mondal,
J. Anderson, K. Kuznia, K. Doshi, M. Patel, K. K. Pal,
M. Moradshahi, M. Parmar, M. Purohit, N. Varshney, P. R. Kaza,
P. Verma, R. S. Puri, R. Karia, S. K. Sampat, S. Doshi, S. Mishra,
S. Reddy, S. Patro, T. Dixit, X. Shen, C. Baral, Y . Choi, N. A.
Smith, H. Hajishirzi, and D. Khashabi, “Super-naturalinstructions:
Generalization via declarative instructions on 1600+ nlp tasks,” 2022.
[Online]. Available: https://arxiv.org/abs/2204.07705
[44] O. Honovich, T. Scialom, O. Levy, and T. Schick, “Unnatural
instructions: Tuning language models with (almost) no human labor,”
in Proceedings of the 61st Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers) , A. Rogers,
J. Boyd-Graber, and N. Okazaki, Eds. Toronto, Canada: Association
for Computational Linguistics, Jul. 2023, pp. 14 409–14 428. [Online].
Available: https://aclanthology.org/2023.acl-long.806
[45] T. Li, Q. Liu, T. Pang, C. Du, Q. Guo, Y . Liu, and M. Lin, “Purifying
large language models by ensembling a small language model,” 2024.
[Online]. Available: https://arxiv.org/abs/2402.14845
[46] S. Zhang, L. Dong, X. Li, S. Zhang, X. Sun, S. Wang, J. Li,
R. Hu, T. Zhang, F. Wu, and G. Wang, “Instruction tuning
for large language models: A survey,” 2024. [Online]. Available:
https://arxiv.org/abs/2308.10792
[47] H. Zhang, Y . Dong, C. Xiao, and M. Oyamada, “Jellyfish:
Instruction-tuning local large language models for data preprocessing,”
in Proceedings of the 2024 Conference on Empirical Methods
in Natural Language Processing , Y . Al-Onaizan, M. Bansal,
and Y .-N. Chen, Eds. Miami, Florida, USA: Association for
Computational Linguistics, Nov. 2024, pp. 8754–8782. [Online].
Available: https://aclanthology.org/2024.emnlp-main.497
[48] F. Biester, M. Abdelaal, and D. Del Gaudio, “Llmclean: Context-
aware tabular data cleaning via llm-generated ofds,” in New Trends
in Database and Information Systems , J. Tekli, J. Gamper, R. Chbeir,
Y . Manolopoulos, S. Sassi, M. Ivanovic, G. Vargas-Solar, and
E. Zumpano, Eds. Cham: Springer Nature Switzerland, 2025, pp.
68–78.
[49] N. Hollmann, S. M ¨uller, and F. Hutter, “Large language models
for automated data science: Introducing CAAFE for context-aware
automated feature engineering,” in Thirty-seventh Conference on
Neural Information Processing Systems , 2023. [Online]. Available:
https://openreview.net/forum?id=9WSxQZ9mG7
[50] G. Badaro, M. Saeed, and P. Papotti, “Transformers for tabular data
representation: A survey of models and applications,” Transactions of
the Association for Computational Linguistics , vol. 11, pp. 227–249,
2023. [Online]. Available: https://aclanthology.org/2023.tacl-1.14
[51] Y . Sui, M. Zhou, M. Zhou, S. Han, and D. Zhang, “Table
meets llm: Can large language models understand structured table
data? a benchmark and empirical study,” in Proceedings of the
17th ACM International Conference on Web Search and Data
Mining, ser. WSDM ’24. New York, NY , USA: Association
for Computing Machinery, 2024, p. 645–654. [Online]. Available:
https://doi.org/10.1145/3616855.3635752
[52] V . Borisov, K. Sessler, T. Leemann, M. Pawelczyk, and G. Kasneci,
“Language models are realistic tabular data generators,” in The
Eleventh International Conference on Learning Representations , 2023.
[Online]. Available: https://openreview.net/forum?id=cEygmQNOeI
[53] S. Arora, B. Yang, S. Eyuboglu, A. Narayan, A. Hojel, I. Trummer,
and C. R ´e, “Language models enable simple systems for generating
structured views of heterogeneous data lakes,” Proc. VLDB Endow. ,
vol. 17, no. 2, p. 92–105, Oct. 2023. [Online]. Available:
https://doi.org/10.14778/3626292.3626294
[54] Y . Lou, C. Lei, X. Qin, Z. Wang, C. Faloutsos, R. Anubhai, and
H. Rangwala, “Datalore: Can a large language model find all lost scrolls
in a data repository?” in 2024 IEEE 40th International Conference on
Data Engineering (ICDE) , 2024, pp. 5170–5176.
[55] M. Ganti, L. Orr, and S. Wu, “Evaluating text-to-sql model failures on
real-world data,” in 2024 IEEE 40th International Conference on Data
Engineering (ICDE), 2024, pp. 1–1.
[56] T. Ren, Y . Fan, Z. He, R. Huang, J. Dai, C. Huang, Y . Jing, K. Zhang,
Y . Yang, and X. S. Wang, “Purple: Making a large language model
a better sql writer,” in 2024 IEEE 40th International Conference on
Data Engineering (ICDE) , 2024, pp. 15–28.
[57] Y . Fan, Z. He, T. Ren, D. Guo, L. Chen, R. Zhu, G. Chen, Y . Jing,
K. Zhang, and X. S. Wang, “Gar: A generate-and-rank approach for
natural language to sql translation,” in 2023 IEEE 39th International
Conference on Data Engineering (ICDE) , 2023, pp. 110–122.
[58] Y . Fan, T. Ren, Z. He, X. Wang, Y . Zhang, and X. Li, “Gensql: A
generative natural language interface to database systems,” in 2023
IEEE 39th International Conference on Data Engineering (ICDE) ,
2023, pp. 3603–3606.
[59] E. Veltri, G. Badaro, M. Saeed, and P. Papotti, “Data ambiguity
profiling for the generation of training examples,” in 2023 IEEE 39th
International Conference on Data Engineering (ICDE), 2023, pp. 450–
463.
[60] J.-P. Zhu, P. Cai, B. Niu, Z. Ni, K. Xu, J. Huang, J. Wan, S. Ma,
B. Wang, D. Zhang, L. Tang, and Q. Liu, “Chat2query: A zero-shot
automatic exploratory data analysis system with large language mod-
els,” in 2024 IEEE 40th International Conference on Data Engineering
(ICDE), 2024, pp. 5429–5432.
[61] Y . Peng, S. Lin, Q. Chen, S. Wang, L. Xu, X. Ren, Y . Li, and J. Xu,
“Chatgraph: Chat with your graphs,” in 2024 IEEE 40th International
Conference on Data Engineering (ICDE) , 2024, pp. 5445–5448.
[62] Z. Qin, C. Luo, Z. Wang, H. Jiang, and Y . Sun, “Relational
database augmented large language model,” 2024. [Online]. Available:
https://arxiv.org/abs/2407.15071
[63] G. Li, X. Zhou, and X. Zhao, “Llm for data management,” Proc.
VLDB Endow., vol. 17, no. 12, p. 4213–4216, Nov. 2024. [Online].
Available: https://doi.org/10.14778/3685800.3685838
[64] X. Zhou, Z. Sun, and G. Li, “Db-gpt: Large language model meets
database,” Data Science and Engineering , vol. 9, pp. 1–10, 01 2024.
[65] Z. Zhao, W. Fan, J. Li, Y . Liu, X. Mei, Y . Wang, Z. Wen,
F. Wang, X. Zhao, J. Tang, and Q. Li, “Recommender Systems in
the Era of Large Language Models (LLMs),” IEEE Transactions on
Knowledge & Data Engineering , vol. 36, no. 11, pp. 6889–6907,
Nov. 2024. [Online]. Available: https://doi.ieeecomputersociety.org/10.
1109/TKDE.2024.3392335
[66] J. Liu, C. Liu, P. Zhou, R. Lv, K. Zhou, and Y . Zhang, “Is chatgpt a
good recommender? a preliminary study,” 2023. [Online]. Available:
https://arxiv.org/abs/2304.10149

[67] J. Chen, L. Ma, X. Li, N. Thakurdesai, J. Xu, J. H. D. Cho,
K. Nag, E. Korpeoglu, S. Kumar, and K. Achan, “Knowledge graph
completion models are few-shot learners: An empirical study of
relation labeling in e-commerce with llms,” 2023. [Online]. Available:
https://arxiv.org/abs/2305.09858
[68] X. Wang, X. Tang, X. Zhao, J. Wang, and J.-R. Wen, “Rethinking
the evaluation for conversational recommendation in the era of
large language models,” in Proceedings of the 2023 Conference on
Empirical Methods in Natural Language Processing , H. Bouamor,
J. Pino, and K. Bali, Eds. Singapore: Association for Computational
Linguistics, Dec. 2023, pp. 10 052–10 065. [Online]. Available:
https://aclanthology.org/2023.emnlp-main.621
[69] Z. He, Z. Xie, R. Jha, H. Steck, D. Liang, Y . Feng, B. P.
Majumder, N. Kallus, and J. Mcauley, “Large language models
as zero-shot conversational recommenders,” in Proceedings of the
32nd ACM International Conference on Information and Knowledge
Management, ser. CIKM ’23. ACM, Oct. 2023, p. 720–730. [Online].
Available: http://dx.doi.org/10.1145/3583780.3614949
[70] Y . Gao, T. Sheng, Y . Xiang, Y . Xiong, H. Wang, and J. Zhang, “Chat-
rec: Towards interactive and explainable llms-augmented recommender
system,” 2023. [Online]. Available: https://arxiv.org/abs/2303.14524
[71] S. Geng, S. Liu, Z. Fu, Y . Ge, and Y . Zhang, “Recommendation as
language processing (rlp): A unified pretrain, personalized prompt &
predict paradigm (p5),” in Proceedings of the 16th ACM Conference
on Recommender Systems , ser. RecSys ’22. New York, NY , USA:
Association for Computing Machinery, 2022, p. 299–315. [Online].
Available: https://doi.org/10.1145/3523227.3546767
[72] S. Xu, W. Hua, and Y . Zhang, “Openp5: An open-source platform for
developing, training, and evaluating llm-based recommender systems,”
2024. [Online]. Available: https://arxiv.org/abs/2306.11134
[73] Z. Cui, J. Ma, C. Zhou, J. Zhou, and H. Yang, “M6-rec: Generative
pretrained language models are open-ended recommender systems,”
2022. [Online]. Available: https://arxiv.org/abs/2205.08084
[74] H. Zhu, H. Ge, X. Gu, P. Zhao, and D. L. Lee, “Influential recom-
mender system,” in 2023 IEEE 39th International Conference on Data
Engineering (ICDE), 2023, pp. 1406–1419.
[75] J. Zhang, R. Xie, Y . Hou, W. X. Zhao, L. Lin, and J.-R. Wen,
“Recommendation as instruction following: A large language model
empowered recommendation approach,” 2023. [Online]. Available:
https://arxiv.org/abs/2305.07001
[76] L. Friedman, S. Ahuja, D. Allen, Z. Tan, H. Sidahmed, C. Long, J. Xie,
G. Schubiner, A. Patel, H. Lara, B. Chu, Z. Chen, and M. Tiwari,
“Leveraging large language models in conversational recommender
systems,” 2023. [Online]. Available: https://arxiv.org/abs/2305.07961
[77] B. Zheng, Y . Hou, H. Lu, Y . Chen, W. X. Zhao, M. Chen, and J.-
R. Wen, “Adapting large language models by integrating collaborative
semantics for recommendation,” in 2024 IEEE 40th International
Conference on Data Engineering (ICDE) , 2024, pp. 1435–1448.
[78] K. Bao, J. Zhang, Y . Zhang, W. Wang, F. Feng, and X. He,
“Tallrec: An effective and efficient tuning framework to align
large language model with recommendation,” in Proceedings of
the 17th ACM Conference on Recommender Systems , ser. RecSys
’23. ACM, Sep. 2023, p. 1007–1014. [Online]. Available: http:
//dx.doi.org/10.1145/3604915.3608857
[79] L. Wu, Z. Qiu, Z. Zheng, H. Zhu, and E. Chen, “Exploring
large language model for graph data understanding in online job
recommendations,” 2023. [Online]. Available: https://arxiv.org/abs/
2307.05722
[80] A.-T. Kuo, H. Chen, and W.-S. Ku, “Bert-trip: Effective and scalable
trip representation using attentive contrast learning,” in 2023 IEEE 39th
International Conference on Data Engineering (ICDE), 2023, pp. 612–
623.
[81] L. Zhang, X. Zhou, Z. Zeng, and Z. Shen, “Are id embeddings neces-
sary? whitening pre-trained text embeddings for effective sequential
recommendation,” in 2024 IEEE 40th International Conference on
Data Engineering (ICDE) , 2024, pp. 530–543.
[82] Y . Hou, Z. He, J. McAuley, and W. X. Zhao, “Learning
vector-quantized item representation for transferable sequential
recommenders,” in Proceedings of the ACM Web Conference
2023, ser. WWW ’23. New York, NY , USA: Association for
Computing Machinery, 2023, p. 1162–1171. [Online]. Available:
https://doi.org/10.1145/3543507.3583434
[83] Z. Yuan, F. Yuan, Y . Song, Y . Li, J. Fu, F. Yang, Y . Pan, and
Y . Ni, “Where to go next for recommender systems? id- vs. modality-
based recommender models revisited,” in Proceedings of the 46th
International ACM SIGIR Conference on Research and Development
in Information Retrieval , ser. SIGIR ’23. New York, NY , USA:
Association for Computing Machinery, 2023, p. 2639–2649. [Online].
Available: https://doi.org/10.1145/3539618.3591932
[84] Y . Hou, S. Mu, W. X. Zhao, Y . Li, B. Ding, and J.-R. Wen, “Towards
universal sequence representation learning for recommender systems,”
in Proceedings of the 28th ACM SIGKDD Conference on Knowledge
Discovery and Data Mining , ser. KDD ’22. New York, NY , USA:
Association for Computing Machinery, 2022, p. 585–593. [Online].
Available: https://doi.org/10.1145/3534678.3539381
[85] J. Wang, F. Yuan, M. Cheng, J. M. Jose, C. Yu, B. Kong,
X. He, Z. Wang, B. Hu, and Z. Li, “Transrec: Learning transferable
recommendation from mixture-of-modality feedback,” 2022. [Online].
Available: https://arxiv.org/abs/2206.06190
[86] Y . Li, H. Du, Y . Ni, P. Zhao, Q. Guo, F. Yuan, and X. Zhou,
“Multi-modality is all you need for transferable recommender systems,”
in 2024 IEEE 40th International Conference on Data Engineering
(ICDE), 2024, pp. 5008–5021.
[87] L. Guo, C. Wang, X. Wang, L. Zhu, and H. Yin, “Automated prompting
for non-overlapping cross-domain sequential recommendation,” 2023.
[Online]. Available: https://arxiv.org/abs/2304.04218
[88] Y . Zhang, Y . Li, L. Cui, D. Cai, L. Liu, T. Fu, X. Huang, E. Zhao,
Y . Zhang, Y . Chenet al., “Siren’s song in the ai ocean: a survey on hal-
lucination in large language models,” arXiv preprint arXiv:2309.01219,
2023.
[89] Y . Chen, Q. Fu, Y . Yuan, Z. Wen, G. Fan, D. Liu, D. Zhang, Z. Li,
and Y . Xiao, “Hallucination detection: Robustly discerning reliable
answers in large language models,” in Proceedings of the 32nd ACM
International Conference on Information and Knowledge Management,
2023, pp. 245–255.
[90] X. He, J. Pan, O. Jin, T. Xu, B. Liu, T. Xu, Y . Shi, A. Atallah,
R. Herbrich, S. Bowers, and J. Q. Candela, “Practical lessons from
predicting clicks on ads at facebook,” in Proc. 8th International
Workshop on Data Mining for Online Advertising , ser. ADKDD’14.
ACM, 2014, p. 1–9.
[91] H. B. McMahan, G. Holt, D. Sculley, M. Young, D. Ebner, J. Grady,
L. Nie, T. Phillips, E. Davydov, D. Golovin, S. Chikkerur, D. Liu,
M. Wattenberg, A. M. Hrafnkelsson, T. Boulos, and J. Kubica, “Ad
click prediction: A view from the trenches,” in Proc. 19th ACM
SIGKDD, ser. KDD ’13. ACM, 2013, p. 1222–1230.
[92] W. Ouyang, X. Zhang, S. Ren, C. Qi, Z. Liu, and Y . Du, “Repre-
sentation learning-assisted click-through rate prediction,” in Proc. 28th
IJCAI, 7 2019, pp. 4561–4567.
[93] T. Ge, H. Liu, P. Yi, S. Huang, Z. Zhang, X. Zhu, Y . Zhang, K. Gai,
L. Zhao, G. Zhou, K. Chen, S. Liu, H. Yi, Z. Hu, B. Liu, and P. Sun,
“Image matters: Visually modeling user behaviors using advanced
model server,” 10 2018, pp. 2087–2095.
[94] S. Feizi, M. Hajiaghayi, K. Rezaei, and S. Shin, “Online advertisements
with llms: Opportunities and challenges,” 2024.
[95] E. Thackray and M. Northin, “Leveraging large language models in
advertising,” WPP Mindshare, https://www.wpp.com/wpp-iq/2023/11/
leveraging-large-language-models-in-advertising, 2023.
[96] P. Keni and M. ElBermawy, “Marketing generative ai report: A
comprehensive evaluation of leading llms,” NoGood, https://nogood.
io/2024/03/13/generative-ai-in-marketing/, 2024.
[97] Q. Yang, M. Ongpin, S. Nikolenko, A. Huang, and A. Farseev,
“Against opacity: Explainable ai and large language models for
effective digital advertising,” in Proceedings of the 31st ACM
International Conference on Multimedia , ser. MM ’23. New York,
NY , USA: Association for Computing Machinery, 2023, p. 9299–9305.
[Online]. Available: https://doi.org/10.1145/3581783.3612817
[98] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. L. Wainwright, P. Mishkin,
C. Zhang, S. Agarwal, K. Slama, A. Ray, J. Schulman, J. Hilton,
F. Kelton, L. Miller, M. Simens, A. Askell, P. Welinder, P. Christiano,
J. Leike, and R. Lowe, “Training language models to follow instructions
with human feedback,” 2022.
[99] OpenAI, “Gpt-4 technical report,” 2023.
[100] S. Koltcov, O. Koltsova, and S. Nikolenko, “Latent dirichlet allocation:
Stability and applications to studies of user-generated content,” in
Proceedings of the 2014 ACM Conference on Web Science , ser.
WebSci ’14. New York, NY , USA: ACM, 2014, p. 161–165.
[Online]. Available: https://doi.org/10.1145/2615569.2615680

[101] S. Nikolenko, “Svd-lda: Topic modeling for full-text recommender
systems,” in Advances in Artificial Intelligence and Its Applications ,
O. Pichardo Lagunas, O. Herrera Alc ´antara, and G. Arroyo Figueroa,
Eds. Cham: Springer International Publishing, 2015, pp. 67–79.
[102] E. Tutubalina and S. I. Nikolenko, “Exploring convolutional neural
networks and topic models for user profiling from drug reviews,”
Multimedia Tools and Applications , vol. 77, no. 4, pp. 4791–4809,
2018.
[103] K. Buraya, A. Farseev, and A. Filchenkov, “Multi-view personality
profiling based on longitudinal data,” Lecture Notes in Computer
Science, vol. 11018, pp. 15–27, 2018.
[104] E. Tutubalina and S. I. Nikolenko, “Demographic prediction based on
user reviews about medications,” Computaci´on y Sistemas , vol. 21,
no. 2, pp. 227–241, 2017.
[105] A. Savchenko, A. Alekseev, S. Kwon, E. Tutubalina, E. Myasnikov,
and S. Nikolenko, “Ad lingua: Text classification improves symbolism
prediction in image advertisements,” in Proceedings of the 28th
International Conference on Computational Linguistics . Barcelona,
Spain (Online): International Committee on Computational Linguistics,
12 2020, pp. 1886–1892. [Online]. Available: https://www.aclweb.org/
anthology/2020.coling-main.171
[106] A. Malik, “Persona based marketing strategies: creation of personas
through data analytics,” Master’s thesis, A. Malik, 2019.
[107] D. Pelleg, A. W. Moore et al. , “X-means: Extending k-means with
efficient estimation of the number of clusters.” inIcml, vol. 1. Stanford,
CA, 2000, pp. 727–734.
[108] A. Neelakantan, T. Xu, R. Puri, A. Radford, J. M. Han, J. Tworek,
Q. Yuan, N. Tezak, J. W. Kim, C. Hallacy et al., “Text and code em-
beddings by contrastive pre-training,”arXiv preprint arXiv:2201.10005,
2022.
[109] Z. Abrams and E. Vee, “Personalized ad delivery when ads fatigue:
An approximation algorithm,” in International Workshop on Web and
Internet Economics. Springer, 2007, pp. 535–540.
[110] G. Aggarwal, S. Muthukrishnan, D. P ´al, and M. P ´al, “General auction
mechanism for search advertising,” in Proceedings of the 18th inter-
national conference on World wide web , 2009, pp. 241–250.
[111] A. Farseev, “Redemptive marketing: The path to resolving transparency
and performance dilemmas in digital advertising,” Forbes.com, 2024.
