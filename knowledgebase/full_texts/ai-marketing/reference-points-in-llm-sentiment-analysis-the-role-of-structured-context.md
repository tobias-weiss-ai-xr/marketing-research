---
title: 'Reference Points in LLM Sentiment Analysis: The Role of Structured Context'
url: https://arxiv.org/abs/2508.11454
category: ai-marketing
subcategory: empirical
date: 2025-08
venue: ''
authors:
- Junichiro Niimi
source: arxiv
pdf_url: https://arxiv.org/pdf/2508.11454
pages: 9
chars: 40478
fetched_at: '2026-11-08T13:12:11+00:00'
kb_version: 1
---

# Reference Points in LLM Sentiment Analysis: The Role of Structured Context

REFERENCE POINTS IN LLM S ENTIMENT ANALYSIS :
THE ROLE OF STRUCTURED CONTEXT
A PREPRINT
Junichiro Niimi* 1,2
1Meijo University
2RIKEN AIP
ABSTRACT
Large language models (LLMs) are now widely used across many fields, including marketing re-
search. Sentiment analysis, in particular, helps firms understand consumer preferences. While most
NLP studies classify sentiment from review text alone, marketing theories, such as prospect theory
and expectation–disconfirmation theory, point out that customer evaluations are shaped not only by
the actual experience but also by additional reference points. This study therefore investigates how
the content and format of such supplementary information affect sentiment analysis using LLMs.
We compare natural language (NL) and JSON-formatted prompts using a lightweight 3B parameter
model suitable for practical marketing applications. Experiments on two Yelp categories (Restau-
rant and Nightlife) show that the JSON prompt with additional information outperforms all baselines
without fine-tuning: Macro-F1 rises by 1.6% and 4% while RMSE falls by 16% and 9.1%, respec-
tively, making it deployable in resource-constrained edge devices. Furthermore, a follow-up analysis
confirms that performance gains stem from genuine contextual reasoning rather than label proxying.
This work demonstrates that structured prompting can enable smaller models to achieve competitive
performance, offering a practical alternative to large-scale model deployment.
Keywords Marketing · Natural Language Processing · Sentiment Analysis · Large Language Model · Prospect Theory
1 Introduction
1.1 Background
In recent years, with the rapid advancements in large lan-
guage models (LLMs) [1] , both industrial and academic
areas in wide range of domains have utilized LLMs for
data analytics, automation, and decision support. In par-
ticular, due to their high applicability in textual data, many
studies have implemented sentiment analysis using LLMs
[2].
LLMs indeed demonstrate remarkable capabilities in un-
derstanding textual context; however, the actual ‘context’
is referred to as a relationship between the tokens, which
is captured through Transformer [3] and attention mecha-
nisms [4] and most existing approaches limit their analy-
sis to the linguistic context within review texts alone. Re-
garding real-world marketing applications, the actual con-
text of consumer evaluation contains the factors which ex-
tend far beyond the written review, such as past purchas-
ing patterns, prior experiences with the business, compar-
ative evaluations against competitors, and opinions from
social media.
This gap is particularly relevant in customer relation-
ship management (CRM) [5, 6] , where understanding
customer sentiment accurately drives business decisions.
Marketing research has long established through prospect
theory [7] and expectation-disconfirmation theory (EDT)
[8] that consumers evaluate experiences relative to these
broader reference points. This insight remains largely un-
explored in LLM-based sentiment analysis.
Furthermore, in practical deployment scenarios, partic-
ularly for real-time recommendation systems, two criti-
cal challenges emerge. First, computational efficiency is
paramount—many businesses cannot deploy large mod-
els (70B+ parameters) due to latency and infrastructure
constraints. Second, despite having rich contextual data
(user histories, business metrics), current methods fail to
effectively incorporate this information into LLM-based
sentiment analysis.
1.2 Research Gap
Despite LLMs’ ability to process diverse input formats,
sentiment analysis studies predominantly focus on review
text alone [9, 10, 11]. However, real-world platforms pos-
sess rich contextual information. From these gaps, we se-
quentially derive four research questions (RQs 1–4):
arXiv:2508.11454v1  [cs.CL]  15 Aug 2025

Reference Points in LLM Sentiment Analysis: The Role of Structured Context A PREPRINT
RQ1 Reference-point utilization: Does supplying
user- and business-average ratings actually help
an LLM classify sentiment more accurately?
RQ2 Prompt format: If the same information is pre-
sented in a machine-readable structure or plain
texts, does the prompt format affect the model
performance?
RQ3 Proxy effect: If supplying the reference points
improve accuracy, is it due to their implicit en-
coding of the ground-truth labels?
RQ4 Reference interactions: How do interactions be-
tween multiple reference points affect prediction
accuracy?
We address these RQs by three experimental studies. In
Study 1, we set up two approaches for the prompts:
natural-language (NL) and machine-readability (JSON),
and several combinations of contextual factors: user aver-
age (U), business average (B), and other attributes (O). We
compare the model performance across these models. In
Study 2, we test whether such information reflect the la-
bel; average ratings may act as a proxy of ground truth.
Finally, in Study 3, we further examine how accuracy
changes according to the interactions of those two refer-
ence points. We progressively explore not only whether
reference points improve performance, but also how they
function within the model’s inference process.
The remainder of this study is constituted as follows: Sec-
tion 2 reviews related studies, Section 3 outlines the model
construction, and Section 4 presents empirical analyses.
We discuss the key findings and implications in Section 5.
Finally, we list our research limitations in Section 6.
2 Related Study
2.1 Sentiment Analysis
Sentiment analysis has been conducted with various
methodologies, including lexicon-based models [12], ma-
chine learning approaches with embeddings [13, 14],
and deep neural networks such as BERT and RoBERTa
[15, 16].
Recently, LLM-based approaches have gained attention
for sentiment analysis [2]. Models like GPT [1] and
Llama [17] demonstrate superior performance compared
to fully-supervised models and even fine-tuned RoBERTa
[18, 2]. Key advantages include broad applicability due to
pre-training and ability to process raw text without exten-
sive preprocessing, achieving high accuracy without fine-
tuning.
However, existing approaches predominantly focus on re-
view text alone, overlooking rich contextual information
available in real-world platforms.
2.2 A Role of Reference Point in Service Evaluation
In the field of marketing, extensive research has examined
how consumers evaluate the product and service quality.
Notable frameworks include prospect theory and EDT.
Prospect theory posits that consumers evaluate services by
comparing their actual experience to a pre-established ref-
erence point [7]. If their experience falls short of this ref-
erence point, they tend to feel dissatisfied; conversely, if
it exceeds the reference point, satisfaction is more likely.
Furthermore, EDT explains the evaluation process from
two perspectives. Absolute evaluation involves assess-
ing whether the perceived quality meets a fixed standard,
while relative evaluation is based on comparing prior ex-
pectations with the perceived quality [8]. In both cases,
prior expectations play a significant role in determining
overall customer satisfaction.
Prior studies on a wide range of products and services
have examined the factors that affect or shape expecta-
tions. Some of the key factors include consumers’ past
experiences [8, 19, 20, 21], reputations provided by other
customers [22, 23, 24], and perceived value [23, 25]. In
particular, reputations—such as an average rating and the
helpful reviews from other consumers—serve as impor-
tant reference points when comparing prior expectations
with actual experiences.
However, as noted above, because sentiment analysis is
predominantly based on actual review texts, few exist-
ing studies have taken these supplementary factors into
account. To more accurately capture customers’ prefer-
ences, it is crucial to incorporate such information into
sentiment analysis. Therefore, we propose a frame-
work that effectively leverages this additional information
within LLMs.
3 Proposed Model
3.1 Pre-trained Model
To implement LLM-based sentiment analysis, we adopt
Llama 3.2 with 3 billion (3B) parameters and is
instruction-tuned (Llama-3.2-3B-Instruct 2). Llama fam-
ily has been widely adopted in sentiment analysis [26].
In particular, the 3B architecture is a lightweight model
which is capable of on-device processing with maintain-
ing privacy. For hyper-parameters, this study adopt tem-
perature=1.0. The model will stop inference after gener-
ating one token (equivalent to underbar in the prompt).
3.2 Prompting Strategy
To obtain sentiment values, we use text-completion func-
tion which the model completes the continuous texts of
the given prompt.
As shown in [27], first, one-shot model is significantly
outperforms the zero-shot model. Additionally, few-shot
prompt clearly outperforms the one-shot; however, In
this study, using multiple examples introduces additional
variables (e.g., the reference points of example reviews,
their alignment patterns, example selection biases), mak-
ing it difficult to interpret core findings regarding struc-
2https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct
2

Reference Points in LLM Sentiment Analysis: The Role of Structured Context A PREPRINT
tured contextual information. Therefore, we use one-shot
prompt (Fig. 1) to maintain experimental clarity.
### Instruction
You are a helpful assistant evaluating the review texts about
the restaurant. Please evaluate the review text and assign an
integer score ranging from 1 for the most negative comment
to 5 for the most positive comment.  The output should be a
single integer from 1 to 5.
### Example
User review: {example_review}
Output: {example_label}
### Task
User review: {user_review}
Output: _
Figure 1: Basic prompt for sentiment analysis (one-shot
model)
3.3 Displaying Supplementary Information
To display additional information, the method of presen-
tation needs to be discussed. Learning structural infor-
mation is highly dependent on in-context learning, which
means that locating the explanations before the tabular
data improves the understanding of the structure [28].
Therefore, we set up and compare two display methods,
text and JSON format. We include the supplementary in-
formation, such as the average user rating and the average
venue rating after the review section of the prompt.
When evaluating the review, consider both the textual
sentiment and the supplementary information. Use user's
average score which user has given in their past reviews to
understand the user's typical rating behavior and
restaurant's average score which the restaurant has received
across all users to compare this restaurant's performance
relative to others. Additionally, use restaurant's name, open
hours (the total number of hours the restaurant is open in a
week), and open days (the total number of days the
restaurant is open in a week) to contextualize the review.
## Example
User review: This restaurant was...
Supplementary Information: The average of this user's past
ratings is 2.6. The average rating this restaurant has
received is 3.0
Output: 5
Figure 2: Natural language (NL) prompt for supplemen-
tary information
Display Method (NL) First, we adopt text method,
which displays the average evaluations with the explana-
tions. With this method, although the prompt gets longer,
any forms of information, including texts and numeric
values, can be input into the model as long as the infor-
mation can be explained in natural language. Thus, the
When evaluating the review, consider both the textual
sentiment and the supplementary information in JSON
format. Use ‘user_average' (the average score this user has
given in their past reviews) to understand the user's typical
rating behavior and ‘restaurant_average' (the average score
this restaurant has received across all users) to compare this
restaurant's performance relative to others. Additionally,
use ‘restaurant_name', ‘open_hours' (the total number of
hours the restaurant is open in a week), and ‘open_days'
(the total number of days the restaurant is open in a week)
to contextualize the review.
## Example
User review: This restaurant was...
Supplementary Information:  {"user_average_stars": 2.6,
"business_average_stars": 3.0}
Output: 5
Figure 3: Structured (JSON) prompt for supplementary
information
necessary amount of computing resources becomes larger.
Therefore, we set up the explanations and the input as Fig.
2.
Display Method (JSON) Second, we adopt JSON
method, which displays supplementary information with
JSON format. This method can provide information in
the structured form. One study [28] which investigates
the impact of using table data, such as CSV , JSON, and
HTML, on the understanding of the information indicates
that LLMs can comprehend the contents of the table un-
less the data structure is not too complex and the ability is
improved when explanations are added before the struc-
tured input. Therefore, we set up the explanations and the
structured input as Fig. 3.
3.4 Dataset
We adopt Yelp Open Dataset [29] which contains the
evaluations and reviews for the variety of establishments.
Some marketing studies in NLP field [30, 26] have uti-
lized Yelp dataset since . For the comprehensive analy-
sis, we set up the two different groups for the analysis:
Restaurant and Nightlife, which are extracted using the
category tags given for the establishments (Table 1). For
each group, we randomly select 500 English reviews from
unique users to unique restaurants for a test set, which
means that no duplicated users and establishments exist
across the overall samples.
For preprocessing the review texts, we at least remove the
line break codes to maintain the format of the prompt.
Table 2 shows the summary statistics of the dataset. A
number of tokens is counted with tiktoken [31] which is
adopted in Llama 3. As shown in the statistics, some sam-
ples have significantly long texts.
3

Reference Points in LLM Sentiment Analysis: The Role of Structured Context A PREPRINT
Table 1: Selected and excluded category tags for each
dataset. We avoid duplicate samples between datasets and
select business with fixed addresses.
Selected Excluded
Restaurant
Restaurant Fast Food, Food Truck,
Bar, Nightlife
Nightlife
Bar, Fast Food, Food Truck
Nightlife
Table 2: Summary Statistics of the Datasets
Mean Std Min Max
Restaurant
Stars 3.724 1.515 1 5
Chars 431.726 368.464 42 2552
Tokens 98.744 85.544 9 606
Nightlife
Stars 3.544 1.605 1 5
Chars 511.082 484.695 65 4998
Tokens 117.104 112.465 15 1118
4 Analyses and Results
4.1 Study 1: Impact of Reference Points and Display
Methods
First, to address RQ1 (reference-point utilization) and
RQ2 (prompt format), we implement sentiment analysis
in restaurant and bar evaluations. We compare evaluation
metrics across different models and assess the effective-
ness of incorporating additional information in two cat-
egories. The supplementary information consists of fol-
lowing three elements. U: the user’s average rating, in-
dicating the mean rating of the past evaluations given by
the user on Yelp, B: the business’ average rating, indi-
cating the mean rating which the restaurant has received
from all users, and O: other contextual factors, indicating
additional information both of textual and numerical at-
tributes, such as the restaurant name, operating hours and
the number of days the restaurant is open per week. Both
U and B are expected to serve as reference points that af-
fect user’s prior expectations.
The LLM-based approach is evaluated with multiple vari-
ations, considering the type of supplementary informa-
tion used and its machine-readability. Accordingly, the
LLM-based models are categorized as follows: JSON-
UBO / NL-UBO: Utilizing all supplementary informa-
tion, presented in JSON format or natural language, re-
spectively; JSON-UB / NL-UB: Incorporating only the
average ratings; JSON-O / NL-O: Incorporating only con-
textual factors; and LLM (None): A baseline model with-
out any supplementary information. We also establish
four well-established baselines: BERT [15], DistilBERT
[32], RoBERTa [16], and DeBERTa [33]. These pre-
trained models are fine-tuned for 5 epochs with addition-
ally extracted 1000 training samples and the test perfor-
mances are computed when the validation losses become
the lowest. Since the proposed model employs 3B model
which focused on lightweight and fast inferences, refer-
ence models are also base-sized (e.g., RoBERTa-Base-
Uncased).
Sentiment analysis has not only the classification aspect
but also the regression due to that the sentiment label is on
the ordinal scale, which means that the magnitude of pre-
diction error is important in addition to the concordance.
Therefore, we adopt both Macro-F1 score and root mean
square error (RMSE) for the evaluation metrics. For the
baseline models we extracted an additional training set
and fine-tuned each model. To prevent any data leakage,
we ensured that both user IDs and store IDs are mutually
exclusive between the training and test sets of the entire
Yelp dataset. Under this constraint, we use at most 500
unique user–business pairs for our evaluation set.
Table 3: Study 1 Results (Dataset 1: Restaurant). † in-
dicates the statistically significant difference ( p < .05)
by two-sided McNemar test against LLM (None). Bold
number indicates that the model surpasses all the refer-
ence models; shaded cells indicate the overall best value.
n = 500 UBO UB O
Macro-F1
LLM (JSON) 0.612† 0.598 0.588
LLM (NL) 0.593† 0.599 0.524
LLM (None) 0.587
DeBERTa 0.538
RoBERTa 0.533
BERT 0.474
DistilBERT 0.465
RMSE
LLM (JSON) 0.564 0.616 0.647
LLM (NL) 0.620 0.624 0.686
LLM (None) 0.675
DeBERTa 0.703
RoBERTa 0.742
BERT 0.758
DistilBERT 0.804
Table 3 and 4 report the results for the Restaurant and
Nightlife datasets, respectively. First, among the two
datasets, JSON-UBO achieves the highest score in both
datasets and improves significantly over LLM (None),
which receives no supplementary information. Among
the reference models, the strongest baseline differs by
domain: LLM (None) ranks first in Restaurant, whereas
RoBERTa-Base leads in Nightlife. In general, RoBERTa
and DeBERTa outperform BERT, followed by Distil-
BERT.
Comparing the models within each display format, first,
JSON prompts consistently improve performance as more
information is added. These results indicate that, sup-
plying a reference point in a machine-friendly format
helps the model capture the complex relationships among
factors, enabling effective inference. Increasing infor-
4

Reference Points in LLM Sentiment Analysis: The Role of Structured Context A PREPRINT
Table 4: Study 1 Results (Dataset 2: Nightlife). † in-
dicates the statistically significant difference ( p < .05)
by two-sided McNemar test against LLM (None). Bold
number indicates that the model surpasses all the refer-
ence models; shaded cells indicate the overall best value.
n = 500 UBO UB O
Macro-F1
LLM (JSON) 0.635† 0.622 0.592
LLM (NL) 0.602 0.628 0.580
LLM (None) 0.526
DeBERTa 0.523
RoBERTa 0.625
BERT 0.574
DistilBERT 0.481
RMSE
LLM (JSON) 0.597 0.613 0.665
LLM (NL) 0.672 0.647 0.666
LLM (None) 0.709
DeBERTa 0.688
RoBERTa 0.657
BERT 0.668
DistilBERT 0.746
mation from JSON-UB to JSON-UBO leads particularly
to reduce RMSE in both datasets. As a result, pre-
diction accuracy rises; for Restaurant, Macro-F1 rises
by 4.3% (from 0.587 to 0.612) and RMSE reduces by
16.44% (from 0.675 to 0.564) relative to both LLM
(None). For Nightlife, the improvements are even larger
relative to LLM (None), +20.7% (from 0.526 to 0.635)
and -15.8% (from 0.709 to 0.597), respectively, and
still effective compared with RoBERTa (+1.6% / -9.1%).
This result aligns with prospect theory and expectation-
disconfirmation theory, providing the clear answer to
RQ1. The user- and business-level average ratings act as
reference points for the LLM and improve the prediction
accuracy.
By contrast, the results of NL prompts do not follow this
pattern; increasing information from NL-UB to NL-UBO
does not contribute on the performance, and in Nightlife
the accuracy even decreases below the best baseline. This
suggests that, although LLMs can process natural lan-
guage using the large context window, the models still
struggle to capture their complex relationship particularly
when large quantities of contextual factors are embedded
as plain text.
These empirical results also provide the response to RQ2.
Supplying additional information in a machine-readable
structure allows the LLMs to effectively utilize those ref-
erence points and contextual factors for the prediction.
4.2 Study 2: Relationship with the Expectation
From the results of Study 1, a remaining concern is that
these reference points may have worked as proxies for the
labels. Therefore, to address RQ3 (proxy effect), Study
2 investigates whether model performance decreases as
the review score diverges from these reference points ac-
cording to the extent of the gaps. We use the JSON-UBO
results for the examination.
Since prior expectations are formed based on the user’s
past behavior and the reputations, we treat such aver-
age score as indicators of prior expectations. We define
expectation–evaluation gap for both user (U) and business
(B) average from user i to store j as follows:
gap(U ) i,j = ratingi,j − user_average i (1)
gap(B) i,j = ratingi,j − business_average j (2)
The data set is divided into five bins according to the ex-
tent of gaps, yielding groups that range from “far below
expectations” to “far above expectations.” For each bin,
we measure the Micro-F1 and RMSE. If the averages were
merely proxies for the labels, performance would peak
in the middle bin (where the gap is smallest) and decline
sharply as the gap widens.
The results are shown in Table 5 (Restaurant) and Table 6
(Nightlife). The leftmost group includes cases where the
actual rating falls below expectations, while the rightmost
group consists of cases where the actual rating exceeds
expectations.
Table 5: Study 2 Results (Dataset 1: Restaurant). Bold
number indicates that the group surpasses the expectation-
met group. Shaded cells indicate the overall best value.
Expectation
below ← met → beyond
User A verage
gap(U ) i,j -1.788 -0.185 0.224 0.748 1.653
Micro-F1 0.690 0.636 0.667 0.890 0.870
RMSE 0.700 0.621 0.619 0.374 0.436
Business A verage
gap(B) i,j -2.130 -0.640 0.415 0.945 1.565
Micro-F1 0.760 0.450 0.760 0.860 0.910
RMSE 0.624 0.819 0.490 0.447 0.300
First, in the Restaurant category, prediction performances
increase in the upper two quantile groups for both the
user’s and store’s average, compared to the middle group
where the actual rating was close to the reference point.
This suggests that the most accurate predictions were
made when the actual experience exceeded prior expec-
tations. In particular, when the experience was beyond
the expectation, the performance improved by +25.1%
for Micro-F1 and -39.6% for RMSE in user-average com-
pared with the middle group while +13.2% for Micro-F1
and -8.8% for RMSE in business-average.
Next, in the Nightlife category, as in Study 1, merely
meeting expectations did not consistently lead to better
predictions. However, unlike the Restaurant category, pre-
diction accuracy improved not only when experiences ex-
ceeded expectations, but also when they fell significantly
5

Reference Points in LLM Sentiment Analysis: The Role of Structured Context A PREPRINT
Table 6: Study 2 Results (Dataset 2: Nightlife).
Bold number indicates that the group surpasses the
expectation-met group. Shaded cells indicate the
overall best value.
Expectation
below ← met → beyond
User A verage
gap(U ) i,j -2.083 -0.312 0.133 0.523 1.375
Micro-F1 0.743 0.709 0.700 0.752 0.798
RMSE 0.507 0.660 0.548 0.554 0.611
Business A verage
gap(B) i,j -2.465 -0.995 0.350 0.975 1.520
Micro-F1 0.830 0.520 0.710 0.850 0.800
RMSE 0.412 0.911 0.566 0.510 0.447
short. Notably, the highest accuracy was observed in the
group where the actual rating was far below the prior ex-
pectation (the leftmost group).
Although there are substantial differences in business
nature and customer behavior between restaurants and
nightlife venues, at least, we do not confirm that the per-
formance metrics increase in the group with the closest
reference points to actual labels. In both cases, reference
points do not simply function as proxies for the correct la-
bels, but rather as relative evaluation values in inference,
meaning that they function literally as reference points,
which is a strong answer to RQ3.
4.3 Study 3: Error Analysis
To further understand how the model interacts with the
reference points, we finally combine user and business av-
erage scores to create a 5×5 matrix where each cell repre-
sents the Micro-F1 score.
Table 7: Error analysis by user average (UA) and business
average (BA) for restaurant dataset
Restaurant BA
1 2 3 4 5
1 - 1.000 0.812 0.750 -
2 1.000 0.833 0.771 0.643 0.000
UA 3 1.000 0.643 0.688 0.716 0.000
4 - 0.250 0.679 0.816 0.750
5 - 1.000 0.909 1.000 1.000
Table 7 (Restaurant) and 8 (Nightlife) show the results.
First, in both categories, the model achieves highest per-
formance (100% in most cases) when UA is 5. Second,
two different reference points show a clear interaction
for the prediction. The accuracy tends to improve when
two reference points align (along the diagonal), indicat-
ing that, when user’s past evaluation is close to other con-
sumers’ average ratings, the actual rating becomes easier
Table 8: Error analysis by user average (UA) and business
average (BA) for nightlife dataset
Nightlife BA
1 2 3 4 5
1 - 1.000 0.920 1.000 -
2 - 0.714 0.680 0.545 -
UA 3 - 0.750 0.623 0.756 -
4 - 0.556 0.682 0.746 1.000
5 - 1.000 1.000 1.000 1.000
to predict. Notably, in some combinations, the accuracy
results in 0%. This indicates cases where conflicting ref-
erences make prediction challenging. However, as shown
in Study 1, this accuracy even outperforms other models.
Therefore, our approach can identify unreliable or diffi-
cult samples to predict based on reference point conflicts.
These results clearly answer RQ4.
These interaction patterns enable practical deployment
strategies. Companies can employ adaptive inference
where samples with aligned reference points (UA ≈BA)
are processed on-device environment, while conflicting
cases are routed to larger cloud-based models. Addi-
tionally, low-confidence predictions can be systematically
collected as training data for fine-tuning domain-specific
models, enabling continuous performance improvement.
5 Conclusion
5.1 Key Findings
In this study, we enhance LLM-based sentiment analysis
by incorporating supplementary information as reference
points and other contextual factors, based on prospect the-
ory and EDT.
Study 1 compared two prompting strategies (NL and
JSON) with multiple combinations of contextual informa-
tion. The JSON-UBO model significantly outperformed
both NL prompts and four strong baselines. Notably,
while JSON prompts showed consistent gains with in-
creasing information, NL prompts failed to leverage the
same contexts despite the same context window.
Study 2 addressed the potential concern about reference
points serving as label proxies. Accuracy improved more
for reviews whose ratings deviated from the average than
for those close to the average, indicating that the model
was not simply copying the reference points for JSON-
UBO model.
Study 3 revealed that the interactions of two different ref-
erence points affect the model performance. Accuracy
improved when those ratings align while conflicting ref-
erences indicate inherently challenging cases.
These findings comprehensively answer our research
questions. RQ1 (Effect of reference points): We demon-
strated that the proposed model with U/B/O information
significantly improves performance with 4.3–20.7% gains
6

Reference Points in LLM Sentiment Analysis: The Role of Structured Context A PREPRINT
in Macro-F1 and 15.8–16.4% reductions in RMSE over
baselines without fine-tuning. RQ2 (Effect of machine
readability): NL prompts fail to leverage complex in-
formation, highlighting the importance of prompt design
even for models with large context windows. RQ3 (Vali-
dation of contextual reasoning): Follow-up analysis con-
firms that model performance improves when ratings de-
viate from expectations, indicating that reference points
assist contextual inference rather than serving as mere la-
bel proxies. RQ4 (Reference nteractions): We revealed
that aligned reference points improve prediction accu-
racy, while conflicting reference points indicate inherently
challenging prediction cases.
5.2 Implications
This study has both academic and practical implications.
Academic. First, by incorporating the theoretical ap-
proach into the LLM-based sentiment analysis, model
performance significantly improved, indicating that
LLM’s rich capability to handle complex context con-
tributes to the predictions. By using JSON format, it
is possible to input various information into LLMs, and
combining more abundant information may further im-
prove prediction accuracy. Second, even if the amount
of information is same across the several prompts, the re-
sults of the inferences, including the prediction and per-
formance, vary depending on the display methods, de-
spite the large context window of modern LLMs. Sec-
ond, simple scalar values, such as 1–5 star averages, can
be used directly in the JSON prompt; no discretization or
embedding tricks are required. These suggest that we can
flexibly employ various factors, including textual and nu-
meric information, into sentiment analysis. Furthermore,
although we employ sentiment analysis for the model ver-
ification, the proposed approach using JSON-based con-
textual information is transferable in wide domain of doc-
ument classification task, including marketing analysis.
Practical. Since the proposed method only relies
on prompt construction, companies can feed existing
database contents to LLMs with JSON prompt and imme-
diately construct their own extended models. As shown in
the results, our approach achieves RMSE of 0.564 (restau-
rant) and 0.597 (nightlife), meaning the average predic-
tion error is less than 1-star on a 5-point scale. This level
of accuracy is sufficient for practical applications such as
the simple recommendation systems, where distinguish-
ing between adjacent rating categories (e.g., 4 vs 5 stars) is
often less critical than identifying overall sentiment polar-
ity. Achieving this performance with a 3B parameter scale
without fine-tuning indicates that the company can im-
mediately deploy the recommendation agent on edge ap-
plication environments combined with the rich customer
database. Furthermore, our error analysis revealed that
samples with aligned reference points can be accurately
predicted while cases with conflicting references could be
routed to larger models or LLM-based ensemble strategy
[34, 35, 26]. This enables the energy efficient process-
ing where computational resources are allocated based on
prediction difficulty.
5.3 Limitations
This study has several limitations. First, while our ap-
proach is grounded in prospect theory and EDT, we did
not empirically test whether the psychological mech-
anisms underlying these theories actually explain the
model’s improved performance.
Second, our experiments were conducted using only a sin-
gle model architecture (Llama-3.2-3B-Instruct). The ef-
fectiveness of structured prompting may vary significantly
across different model families and sizes, limiting the gen-
eralizability of our findings. Particularly, we cannot con-
clude whether the benefits of JSON formatting extend to
larger models or different architectures.
Third, our evaluation is restricted to English-language re-
views from two categories within the Yelp Open Dataset
[29]. The effectiveness on other languages, domains, or
review platforms with different characteristics of supple-
mentary information remains untested.
Finally, while we argue that our approach is computation-
ally efficient due to the absence of fine-tuning, we did not
provide quantitative measurements of inference time or
memory usage across different prompt formats for the ac-
tual inferences.
Acknowledgments
The dataset used in this study consisted of open data for
academic use. As no additional information was col-
lected, the author did not obtain any information that
could lead to the identification of individuals. The large
language models used to construct the analysis model
were licensed for commercial and academic use. Both the
dataset and models were managed and used in an appro-
priate environments that comply with the terms of use of
the companies from which it was made available.
This study is supported by JSPS KAKENHI (Grant Num-
ber: 24K16472).
References
[1] Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, et al. Language models are few-shot learn-
ers. Advances in neural information processing sys-
tems, 33:1877–1901, 2020.
[2] Jan Ole Krugmann and Jochen Hartmann. Sentiment
analysis in the age of generative ai. Customer Needs
and Solutions, 11(1):3, 2024.
[3] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz
Kaiser, and Illia Polosukhin. Attention is all you
need. Advances in neural information processing
systems, 30:5998–6008, 2017.
7

Reference Points in LLM Sentiment Analysis: The Role of Structured Context A PREPRINT
[4] Dzmitry Bahdanau, Kyung Hyun Cho, and Yoshua
Bengio. Neural machine translation by jointly learn-
ing to align and translate. In 3rd International Con-
ference on Learning Representations, ICLR 2015 ,
2015.
[5] Richard L Oliver. Whence consumer loyalty? Jour-
nal of marketing, 63(4_suppl1):33–44, 1999.
[6] Werner Reinartz, Manfred Krafft, and Wayne D
Hoyer. The customer relationship management
process: Its measurement and impact on perfor-
mance. Journal of marketing research, 41(3):293–
305, 2004.
[7] Daniel Kahneman and Amos Tversky. Prospect the-
ory: An analysis of decision under risk. In Hand-
book of the fundamentals of financial decision mak-
ing: Part I, pages 99–127. World Scientific, 2013.
[8] Richard L Oliver. A cognitive model of the an-
tecedents and consequences of satisfaction deci-
sions. Journal of marketing research , 17(4):460–
469, 1980.
[9] Ya You, Gautham G Vadakkepatt, and Amit M Joshi.
A meta-analysis of electronic word-of-mouth elas-
ticity. Journal of Marketing, 79(2):19–39, 2015.
[10] Andrew J Flanagin and Miriam J Metzger. Trust-
ing expert-versus user-generated ratings online: The
role of information volume, valence, and consumer
characteristics. Computers in Human Behavior ,
29(4):1626–1634, 2013.
[11] Beverley A Sparks and Victoria Browning. The
impact of online reviews on hotel booking inten-
tions and perception of trust. Tourism management,
32(6):1310–1323, 2011.
[12] Clayton Hutto and Eric Gilbert. Vader: A parsi-
monious rule-based model for sentiment analysis of
social media text. In Proceedings of the interna-
tional AAAI conference on web and social media ,
volume 8, pages 216–225, 2014.
[13] Tomas Mikolov, Kai Chen, Greg Corrado, and
Jeffrey Dean. Efficient estimation of word rep-
resentations in vector space. arXiv preprint
arXiv:1301.3781, 2013.
[14] Piotr Bojanowski, Edouard Grave, Armand Joulin,
and Tomas Mikolov. Enriching word vectors with
subword information. Transactions of the associa-
tion for computational linguistics, 5:135–146, 2017.
[15] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. Bert: Pre-training of deep bidi-
rectional transformers for language understanding.
arXiv preprint arXiv:1810.04805, 2018.
[16] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du,
Mandar Joshi, Danqi Chen, Omer Levy, Mike
Lewis, Luke Zettlemoyer, and Veselin Stoyanov.
Roberta: A robustly optimized bert pretraining ap-
proach. arXiv preprint arXiv:1907.11692, 2019.
[17] Hugo Touvron, Thibaut Lavril, Gautier Izacard,
Xavier Martinet, Marie-Anne Lachaux, Timothée
Lacroix, Baptiste Rozière, Naman Goyal, Eric Ham-
bro, Faisal Azhar, et al. Llama: Open and effi-
cient foundation language models. arXiv preprint
arXiv:2302.13971, 2023.
[18] Zengzhi Wang, Qiming Xie, Yi Feng, Zixiang Ding,
Zinong Yang, and Rui Xia. Is chatgpt a good sen-
timent analyzer? In First Conference on Language
Modeling, 2024.
[19] Praveen K Kopalle and Donald R Lehmann. Strate-
gic management of expectations: The role of dis-
confirmation sensitivity and perfectionism. Journal
of Marketing Research, 38(3):386–394, 2001.
[20] Ruth N Bolton. A dynamic model of the duration
of the customer’s relationship with a continuous ser-
vice provider: The role of satisfaction. Marketing
science, 17(1):45–65, 1998.
[21] Bruce Cooil, Timothy L Keiningham, Lerzan Ak-
soy, and Michael Hsu. A longitudinal analysis of
customer satisfaction and share of wallet: Investi-
gating the moderating effect of customer character-
istics. Journal of marketing, 71(1):67–83, 2007.
[22] Timothy Lee Keiningham, Bruce Cooil, Edward C
Malthouse, Bart Lariviere, Alexander Buoye,
Lerzan Aksoy, and Arne De Keyser. Perceptions
are relative: an examination of the relationship be-
tween relative satisfaction metrics and share of wal-
let. Journal of Service Management , 26(1):2–43,
2015.
[23] Kisang Ryu, Heesup Han, and Tae-Hee Kim. The
relationships among overall quick-casual restaurant
image, perceived value, customer satisfaction, and
behavioral intentions. International journal of hos-
pitality management, 27(3):459–469, 2008.
[24] Barry J Babin, Yong-Ki Lee, Eun-Ju Kim, and Mitch
Griffin. Modeling consumer satisfaction and word-
of-mouth: restaurant patronage in korea. Journal of
Services Marketing, 19(3):133–139, 2005.
[25] G Qin and Victor R Prybutok. Determinants
of customer-perceived service quality in fast-food
restaurants and their relationship to customer satis-
faction and behavioral intentions. Quality Manage-
ment Journal, 15(2):35–50, 2008.
[26] Junichiro Niimi. A simple ensemble strategy for
llm inference: Towards more stable text classifica-
tion. In Proceedings of the 30th International Con-
ference on Natural Language & Information Sys-
tems (NLDB 2025), Lecture Notes in Computer Sci-
ence. Springer, 2025.
8

Reference Points in LLM Sentiment Analysis: The Role of Structured Context A PREPRINT
[27] Wenxuan Zhang, Yue Deng, Bing Liu, Sinno Jialin
Pan, and Lidong Bing. Sentiment analysis in the era
of large language models: A reality check. arXiv
preprint arXiv:2305.15005, 2023.
[28] Yuan Sui, Mengyu Zhou, Mingjie Zhou, Shi Han,
and Dongmei Zhang. Table meets llm: Can large
language models understand structured table data?
a benchmark and empirical study. In Proceedings
of the 17th ACM International Conference on Web
Search and Data Mining, pages 645–654, 2024.
[29] Yelp. Yelp Open Dataset, An all-purpose dataset for
learning. (https://www.yelp.com/dataset, accessed
Nov. 20th, 2023), 2022.
[30] Fillipe dos Santos Silva, Julio Cesar dos Reis, and
Marcelo S Reis. Seriema: A framework to enhance
clustering stability, compactness, and separation by
fusing multimodal data. In International Conference
on Applications of Natural Language to Information
Systems, pages 394–408. Springer, 2024.
[31] OpenAI. tiktoken: a fast BPE to-
keniser for use with OpenAI’s models .
(https://github.com/openai/tiktoken, accessed
May. 26th, 2024), 2023.
[32] Victor Sanh, Lysandre Debut, Julien Chaumond,
and Thomas Wolf. Distilbert, a distilled ver-
sion of bert: smaller, faster, cheaper and lighter.
10.48550/arxiv.1910.01108, 2019.
[33] Pengcheng He, Xiaodong Liu, Jianfeng Gao, and
Weizhu Chen. Deberta: Decoding-enhanced bert
with disentangled attention. In International Con-
ference on Learning Representations.
[34] Yichong Huang, Xiaocheng Feng, Baohang Li,
Yang Xiang, Hui Wang, Ting Liu, and Bing Qin.
Ensemble learning for heterogeneous large language
models with deep parallel collaboration. In The
Thirty-eighth Annual Conference on Neural Infor-
mation Processing Systems, 2024.
[35] Frank Xing. Designing heterogeneous llm agents for
financial sentiment analysis. ACM Transactions on
Management Information Systems, 2025.
9
