---
title: 'Hidden in Plain Sight: Finding MAHA on Reddit'
url: https://arxiv.org/abs/2605.20435
category: social-media
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Sabit Ahmed
- Subigya Nepal
- Henry Kautz
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.20435
pages: 9
chars: 23426
fetched_at: '2026-11-08T12:57:43+00:00'
kb_version: 1
---

# Hidden in Plain Sight: Finding MAHA on Reddit

Hidden in Plain Sight: Finding MAHA on Reddit
Sabit Ahmed1, Subigya Nepal1, and Henry Kautz1
University of Virginia, Charlottesville, VA 22903, USA
{bcw3zj,sknepal,rmw7my}@virginia.edu
Abstract. Make America Healthy Again (MAHA) is a national health
movement that encompasses a striking mix of beliefs, from broadly ac-
cepted concerns about good diet and exercise to controversial takes on
organic and genetically modified food, childhood vaccination, science, and
institutions. Various influencers and promoters of the MAHA movement
on social media are scattered throughout the online space. Investigat-
ing the structure, discourse, and contagion of MAHA beliefs requires
large-scale fine-grained digital footprints. Constructing structured data
covering different MAHA themes from vast unstructured social media
data is challenging. We introduce a Reddit dataset that spans six years
(2020–2025), comprising 18.5M posts from 4M users. Containing the nat-
ural and thematic context of 12 MAHA-aligned beliefs, this dataset offers
researchers from various domains the opportunity to study the dynamics
of the MAHA movement, its structural and functional components, and
the linguistic and behavioral patterns of its proponents.
Keywords:Social media·Large-scale data·Health discourse·Make
America Healthy Again (MAHA)·Large language models (LLMs)
1 Introduction
Make America Healthy Again (MAHA) is a national health movement that
encompasses many distinct themes, ranging from uncontroversial ones, such
as the importance of exercise, to controversial ones, such as increasing the
consumption of red meat, to dangerous ones, such as the claim that childhood
vaccinations cause autism. Social networking sites are one of the key components
for the growth of the MAHA community. Reddit is the largest social media
platform where posts are organized thematically, i.e., by subreddits. Therefore, it
would seem natural to study the rise and spread of MAHA on Reddit by analyzing
the appropriate subreddits. However, three challenges arise: the largest MAHA-
related subreddit (r/NoNewNormal) was banned, and many similar communities
were quarantined [3]; Reddit is highly dynamic with 1,500–1,700 new subreddits
created daily [7]; and the platform generates hundreds of millions of posts per
year [11].
Therefore, we cannot restrict our attention to a small set of subreddits to
find MAHA on Reddit. MAHA discourse is spread through thousands of different
subreddits, so we must search Reddit as a whole. Secondly, we must develop a
highly efficient pipeline to sift through terabytes of data and accurately identify
arXiv:2605.20435v2  [cs.SI]  22 Jul 2026

2 Ahmed et al.
Fig.1: Data collection and stance-labeling pipeline with worked examples for the
Vaccine theme across four stages.
the MAHA community that is “hidden in plain sight” on Reddit. With a multi-
stage keyword search and machine-learning pipeline, we narrowed billions of
Reddit submissions and comments down to millions with the strongest MAHA
signals across 12 themes. Using a tree-based, few-shot Large Language Model
(LLM) pipeline, we demonstrate an analytics pipeline to characterize each user’s
belief themes and stances.
2 Data Collection Pipeline
2.1 Reddit Data Archive Download
Historically, the Reddit platform offered access to rich natural-language text
exchanged across subreddit communities through the Pushshift API – an endpoint
widely used for large-scale behavioral research. After Reddit discontinued access
to Pushshift, we obtained historical archives via Arctic Shift, a third-party system
that mirrors Pushshift’s data. We collected all submissions and comments and
retained six years (January 2020 – December 2025), a window that begins with the
COVID-19 pandemic and captures the key period of MAHA-adjacent discourse.
We usepostto refer to both submissions and comments. An overview of the
pipeline is shown in Fig. 1.

Hidden in Plain Sight: Finding MAHA on Reddit 3
2.2 Defining Themes of MAHA communities
After careful assessment of recent studies and the report published by the White
House [2,15,13], we consider 12 MAHA-related themes that span lifestyle (e.g.,
exercise, food), controversial health topics (e.g., vaccines, fluoride), and broader
ideological domains (e.g., anti-science, climate skepticism).
– Exercise:Promotion of exercise and physical fitness.
– Food:Processed food criticism and promotion of whole foods.
– GMO:Skepticism toward genetically modified organisms and crops.
– Fluoride:Opposition to public water fluoridation.
– Vaccine:Criticism of vaccines (e.g., vaccine injury).
– Mask:Opposition to mask mandates in the context of COVID-19.
– Pharma:Criticism of industry and evidence-based medical practice.
– Science:Distrust of mainstream scientific consensus and institutions.
– EMF:Unproven effects of electromagnetic field (EMF) radiation.
– Environment:Concerns about pollutants (e.g., microplastics, toxic chemi-
cals, pesticides).
– Climate:Skepticism of mainstream climate science.
– Screen:Concerns about the health effects of phone and computer use.
Each theme can contain pro-MAHA, anti-MAHA, or neutral opinion stances.
The distinction between stances is demonstrated in Fig. 1 with example posts.
2.3 2-Stage Keyword Search and Cleaning
We performed a 2-stage keyword search with a list of keywords and regular
expressions. For the first stage, we combined all 12 sets of keywords into a single
regular expression to search through∼20 billion submissions and comments.
In the second stage, we applied the search to each individual keyword set and
obtained 12 distinct sets of thematic data. Following this, we removed any non-
English texts and posts from bots and admins. We kept only the posts that had
more than 3 words. This resulted in 234M submissions and 1.3B comments in
total.
2.4 Classifying MAHA-only Discussions
Keyword-matched data still contained many posts irrelevant to MAHA – e.g.,
“shot” captures both vaccine and gun discussions. Therefore, we trained a logistic
regression classifier on MAHA relevance. We randomly sampled 200 submissions
and 200 comments per theme per month over six years (2020–2025), yielding
28,800 samples per theme. Using 100 theme-specific seed queries, we ran semantic
search on each thematic sample, sorted those by cosine similarity, and kept high-
scoring ones (≥ 0.9) as candidate positives. We manually reviewed the top∼3,000
candidates per theme, yielding ∼14,000 MAHA-positive samples overall. For
negatives, we applied a low similarity threshold (< 0.2) along with the MAHA-
negative seed queries, obtaining∼68,000 MAHA-negative samples; a manual
inspection confirmed this similarity-based labeling was effective and captured

4 Ahmed et al.
Table 1: 10-fold cross-validation results for MAHA vs. generic classification. F1*
denotes the positive class (MAHA).
Negatives Model AUC Prec. Rec. F1 * F1Mac
Baseline LR + SBERT.999.959.982.970.982 SVM +n-grams .997 .973 .949 .961 .976
Hard-neg LR + SBERT .997.982.974.978.981 SVM +n-grams .992 .981 .935 .957 .963
a wide variety of generic discussions. We then applied hard negative mining
to replace easy negatives with the 20,000 most confusing examples around the
decision boundary. We evaluated two algorithms on two types of features: logistic
regression with Sentence-BERT embeddings (LR + SBERT) and a support vector
machine with TF-IDF-weighted unigrams, bigrams and trigrams (SVM + N-
grams), using 10-fold cross-validation. LR + SBERT achieved the highest recall
and F1 and was selected as the final classifier (precision= 0.982, recall= 0.974,
F1 = 0.978). The high F1 reflects the relative separability of MAHA-relevant
posts from irrelevant posts in the semantic embedding space; a baseline classifier
without hard negative mining achieved F1 = 0.970, indicating that hard negative
mining contributed a small but consistent improvement rather than driving the
headline performance. The selected model was then applied to all posts matched
with keywords to retain only MAHA-relevant content for downstream analysis.
Details of the classifier performance are reported in Table 1.
2.5 Identifying Themes and Stances from Posts
After obtaining the most relevant MAHA posts across all 12 themes, we applied
two post-processing steps: removing submissions with fewer than 10 comments
and removing all comments without parent submissions. This resulted in 1.2M
submissions and 45M comments mapped to one or more of the 12 themes. Reddit
discussions are organized as a tree-based thread, where people discuss or criticize
a theme-specific issue through submissions, comments, or replies. We identified
four challenges in classifying the stances from a post: First, a post that passed
through the initial logistic-regression-based MAHA filter may not substantively
discuss any theme, containing only spurious signals. Second, a post can take a
clear stance, no stance, or contain a mix of opinions, questions, or information on
a specific theme, either as a parent (i.e., submission, comment) or as a child (i.e.,
comment, reply). Third, a child comment or reply can agree or disagree with its
parent post or may not take a clear side. Fourth, a post may discuss multiple
themes and stances, requiring a predictive model to assign an independent stance
to each relevant theme.
To obtain relevant themes and stances from a post, we used a tree-based
few-shot in-context learning. We provided the LLM with a few-shot example to
predict the themes and stances of each post. We first applied a relevance gate,
using an LLM to determine whether a post was actually related to any MAHA
(Make America Healthy Again) theme, filtering out false positives that passed

Hidden in Plain Sight: Finding MAHA on Reddit 5
the initial logistic regression classifier. Posts that passed this filter were then
classified for theme and associated stance. We defined three stances a post could
take toward a theme — pro, anti, and neutral — allowing the model to assign
different stances to different themes within the same discussion.
Table 2: LLM theme and stance classification performance on the evaluation set.
Relevance F1 measures binary theme presence; Theme F1 is macro-F1 across
the 12 themes; and Stance F1 is macro-F1 across pro, anti, and neutral stances.
†Selected as the final production model.
Model Relev. F1 Theme F1 Stance F1
Qwen2.5-7B 0.67 0.48 0.42
Qwen2.5-14B0.78 0.600.54
Qwen2.5-32B† 0.760.60 0.61
We evaluated multi-theme-stance classification performance using the Qwen2.5
model family. Using stratified sampling across the 12 themes, we selected 500
submission trees, then sampled 500 comments from the pooled set of comments
across those trees. One researcher annotated all 1000 samples and a second
researcher independently annotated a stratified subsample of 100 to measure the
interrater agreement. Agreement (Cohen’sκ) was substantial for both theme (κ
= 0.86) and stance (κ = 0.75) classification. The best performing model achieved
an F1 of 0.60 for theme classification and 0.61 for stance classification and was
selected for large-scale theme and stance labeling. The resulting data comprises
∼478K submissions and∼18.1M comments. Table 3 shows the statistics on the
curated data. The data will be available for download upon request from the
authors’ website (link). The data analyzed in this study are publicly available on
Reddit and were accessed in accordance with the platform’s terms and conditions.
We report analyses exclusively at the aggregate community level; therefore, no
privacy concerns apply.
Table 3: Dataset Summary
Metric Count
Unique submissions 478,626
Unique comments 18,120,340
Unique users 3,964,483
Unique subreddits 18,096
2.6 Identifying User Stances and Distinctive Words
To obtain a fine-grained signal for downstream analyses, retained users who had
at least three posts in every year from 2020 to 2025. This resulted in a total
of 33,384 users. As an illustrative application of the constructed dataset, we
identified user stances and extracted distinctive words. We characterized each
user by their fraction of posts in each stance across all themes, using a weighted
opinion scoring, adjusted from Wu et al. [14]:
S(u, t) =ws (ns pro −n s anti) +wc (nc pro −n c anti) ws ns +w c nc (1)

6 Ahmed et al.
-1 -.5 -0.2 0 0.2 .5 1
10 1
100
density (log)
vaccine  (N=28,871)
-1 -.5 -0.2 0 0.2 .5 1
10 2
10 1
100
101
mask  (N=22,278)
-1 -.5 -0.2 0 0.2 .5 1
10 1
100
101
gmo  (N=1,052)
-1 -.5 -0.2 0 0.2 .5 1
10 1
100
101
density (log)
fluoride  (N=1,142)
-1 -.5 -0.2 0 0.2 .5 1
10 2
10 1
100
101
climate_denial  (N=13,674)
-1 -.5 -0.2 0 0.2 .5 1
100
101
emf  (N=586)
-1 -.5 -0.2 0 0.2 .5 1
10 2
10 1
100
101
density (log)
processed_vs_whole_food  (N=13,450)
-1 -.5 -0.2 0 0.2 .5 1
10 2
10 1
100
101
screen_digital_tech  (N=7,798)
-1 -.5 -0.2 0 0.2 .5 1
10 2
10 1
100
101
environmental  (N=9,746)
-1 -.5 -0.2 0 0.2 .5 1
10 2
10 1
100
101
density (log)
pharma_medicine  (N=15,322)
-1 -.5 -0.2 0 0.2 .5 1
10 2
10 1
100
101
anti_science  (N=21,609)
-1 -.5 -0.2 0 0.2 .5 1
10 2
10 1
100
101
exercise  (N=18,114)
Anti-MAHA  (score < 0.2)
 Neutral (excluded)  ( 0.2 < score < +0.2)
 MAHA  (score > +0.2)
Fig.2: User stance distribution on 12 themes.
Where ns pro, ns anti, ns neutral denote stance counts from submissions, andnc pro,
nc anti, nc neutral from comments, ns and nc are the total submission and comment
counts, andw s andw c are the weights for a useruand themet,
ws = nc ns +n c , w c = ns ns +n c (2)
Scores range from −1(anti-MAHA) to+1(MAHA). After careful inspection
on the distribution of opinion scores as shown in Figure 2, we label users as
MAHA if S≥ 0.2or anti-MAHA if S≤ −0.2; users with|S|< 0.2are excluded
from subsequent analyses, as their net stance signal is too weak to attribute
a clear position. After obtaining theMAHA and anti-MAHA user groups, we
statistically matched the unique users with four covariates: posts per year, number
of active themes, mean word count, and mean percentage of function words. We
then calculated a differential TF-IDF score for each word as the difference in
the mean TF-IDF between theMAHA and anti-MAHA groups, and extracted
the top five unique and most distinctive words per group for all 12 themes.
Table 4 shows thatMAHA users are more likely to criticize institutions (e.g.,
“monsanto”, “big pharma”, “cdc”, etc.), power dynamics and economic structures

Hidden in Plain Sight: Finding MAHA on Reddit 7
(e.g., “government”, “companies”, “money”) and exhibit negative sentiment against
vaccines, masks and conventional medical practices (e.g., “forced”, “control”). By
contrast, anti-MAHA users emphasize evidence and scientific consensus (e.g.,
“evidence”, “scientific”, “research”), are more likely to trust medical advice and
treatment (“vaccinated”, “effective”, “advice”, “treatment”), and use critical words
towards non-scientific claims (“conspiracy”, “anti-science”, “stupid”). This pattern
reflects not only the ideological divide between the two groups, but also the
internal diversity of topics within the MAHA community itself, such as discussions
linking vaccine skepticism with 5G – a unique conspiracy narrative [6] stemmed
from two otherwise distinct threads of MAHA.
Table 4: Top 5 unique, distinctive words.
Theme MAHA-distinctive words Anti-MAHA distinctive words
Vaccine vaccine, trump, pharma, mrna, government vaccinated, doses, risk, available, effective
Mask mask mandates, lockdowns, government,
evidence, forced
vaccinated, sick, n95, risk, indoors
GMO monsanto, roundup, anti, vaccine, mrna better, non-gmo, grown meat, selective
breeding, organic
Fluoride iq, gland, conspiracy, water supply, rfk teeth, dentist, use, toothpaste, dental
Climate co 2, global warming, science, temperature,
man
action, vote, fossil, republicans, need
EMF vaccine, gates, covid, chip, control radio, radiation, frequency, stupid, ionizing
Food sugar, fiber, weight, keto, carbs evidence, processed, plant, science, vegan
Screen Use algorithms, social media, dopamine, internet,
content
screen, kid, tv, vr, games
Environmentfood, lead, water, eat, chemicals energy, carbon, emissions, nuclear, tax
Pharma big pharma, vaccine, pfizer, money,
companies
medication, adhd, advice, need, treatment
Science government, covid, virus, media, cdc evidence, scientific, conspiracy, anti-science,
research
Exercise workout, training, started, good, home weight, calories, exercise, weight loss, diet
3 Applications
The released dataset enables a broad range of analyses on multi-theme belief
communities. Per-theme stance labels and per-user aggregate scores support
sentiment analysisof how MAHA-aligned and mainstream users frame health
topics, both within and across themes. The coexistence of mainstream and con-
tested themes in a single dataset enables study ofpolarization and narratives
— in particular, how supporters and detractors construct competing accounts
of the same topic through polarized lenses, and how narratives diffuse between
mainstream and fringe themes. Reddit’s reply structure, preserved in our dataset,
supports analysis ofnetwork structure and community, including interaction

8 Ahmed et al.
graphs between user groups, sub-community formation around specific themes,
and cross-themeco-engagement patterns.The six-yearwindow (2020–2025), which
spans the COVID-19 pandemic and the rise of MAHA as a political movement,
supportstemporal analysisof belief adoption, theme-to-theme transitions, and
shifts in stance composition over time. Finally, the large volume of stance-labeled
text enables fine-grainedlinguistic analysis, including psycholinguistic profil-
ing, framing differences, and characteristic vocabulary across user groups and
themes. Detailed analyses and relevant applications of the constructed dataset is
thoroughly discussed in a companion paper which is currently under review [1].
4 Related Work
The MAHA movement originated as a small community of vaccine skeptics,
critics of pesticides and toxic chemicals, and proponents of healthy and organic
food under the banner of “health freedom” [12]. However, it grew to a powerful
national movement with the appointment of Robert F. Kennedy Jr. as the
United States Secretary of Health and Human Services and took control of many
federal health policies. Numerous studies examined online discourse to understand
public sentiments and narrative shifts towards vaccines and anti-science attitudes.
Gyawali et al. [8] investigated how the perception of English-speaking X (former
Twitter) users evolves using millions of posts on vaccine discourse. Wu et al.
[14] found that Twitter communities are associated with users’ opinion shifts
towards the COVID-19 vaccine in Japan. In a Twitter-based analysis, Rao et
al. [10] examined the correlation between political partisanship and anti-science
attitudes. Paino et al. [9] examined factors that affect digital health literacy.
Dalege and Van Der Does [4] proposed a cognitive network model to investigate
interrelated beliefs on childhood vaccination and genetically modified (GM) food.
Fariello and Jemielniak [5] analyzed 16 years of Reddit discussions that span
11.5 billion posts to examine the language and sentiment surrounding climate
change. Recently, Charles Alba [2] leveraged pre-trained language models (PLMs)
to understand sentiments and topics commonly discussed in X’s (former Twitter)
MAHA community.
5 Conclusion and Future Work
We introduced a large-scale Reddit dataset to study the Make America Healthy
Again (MAHA) movement, covering six years (2020–2025) and 12 MAHA-aligned
belief themes. Using a three-stage pipeline that combines keyword search, a
relevance classifier, and a few-shot LLM stance classifier, we labeled 478K submis-
sions and 18.1M comments from 4M users by per-theme stance and aggregated
them into per-user stance scores, yielding MAHA, anti-MAHA, and mainstream
user groups. Keyword-based filtering, though two-stage and validated, may miss
MAHA-aligned engagement expressed implicitly — for example, brief agreement
comments (“agreed”, “same here”) that inherit stance from their parent posts but
lack MAHA vocabulary. More context-aware filtering could recover such cases.
By preserving the natural and thematic context of MAHA discourse at scale,

Hidden in Plain Sight: Finding MAHA on Reddit 9
the dataset opens avenues for studying the structural, temporal, linguistic, and
behavioral dimensions of contemporary health movements online.
References
1. Ahmed, S., Nepal, S., Kautz, H.: The structure and dynamics of the online MAHA-
sphere (2026). https://doi.org/10.48550/arXiv.2605.20457 , https://arxiv.
org/abs/2605.20457, under review
2. Alba, C.: Sentiments and discourse surrounding the make america healthy again
(#maha) movement on social media. Journal of Epidemiology and Population
Health74(1), 203167 (2026)
3. Brodkin, J.: Reddit bans r/nonewnormal and quarantines 54 “covid-denial subred-
dits”. Ars Technica (September 2021), accessed: 2026-04-29
4. Dalege, J., Van Der Does, T.: Using a cognitive network model of moral and social
beliefs to explain belief change. Science Advances8(33) (Aug 2022)
5. Fariello, G., Jemielniak, D.: The changing language and sentiment of conversations
about climate change in Reddit posts over sixteen years. Communications Earth &
Environment6(1) (Jan 2025)
6. Flaherty, E., Sturm, T., Farries, E.: The conspiracy of Covid-19 and 5G: Spatial
analysis fallacies in the age of data democratization. Social Science & Medicine
293, 114546 (Jan 2022).https://doi.org/10.1016/j.socscimed.2021.114546 ,
https://pmc.ncbi.nlm.nih.gov/articles/PMC8576388/
7. FrontPageMetrics: New subreddits by month: Reddit history.https://frontpagem
etrics.com/month/(2022), accessed 2026-04-29
8. Gyawali, N., Caragea, D., Caragea, C., Mohammad, S.M.: The shifting landscape
of vaccine discourse: Insights from a decade of pre- to post-covid-19 vaccine posts
on social media. PLOS ONE20(12) (2025)
9. Paino, M., Claggett, J.L., Kitchens, B.: Medical skepticism in the digital age: An
experimental study on digital health literacy. Sociological Inquiry (2025)
10. Rao, A., Morstatter, F., Hu, M., Chen, E., Burghardt, K., Ferrara, E., Lerman,
K.: Political Partisanship and Antiscience Attitudes in Online Discussions About
COVID-19: Twitter Content Analysis. Journal of Medical Internet Research23(6)
(Jun 2021)
11. Reddit, Inc.: Reddit, inc. 2024 form 10-k (2025),https://www.sec.gov/Archives
/edgar/data/1713445/000171344525000096/redditannualreport2024.pdf, sEC
filing, accessed 2026-04-29
12. Stolberg, S.G.: The ‘make america healthy again’ movement is cooling on trump
and republicans. The New York Times (Apr 2026),https://www.nytimes.com/20
26/04/23/us/politics/maha-voters-midterms.html, accessed: 2026-04-24
13. The White House: Make our children healthy again: Assessment. Technical report,
The White House (May 2025),https://www.whitehouse.gov/wp-content/uploa
ds/2025/05/MAHA-Report-The-White-House.pdf , “Make Our Children Healthy
Again Commission” (MAHA)
14. Wu, Q., Sano, Y., Takayasu, H., Havlin, S., Takayasu, M.: Twitter communities
are associated with changing user’s opinion towards COVID-19 vaccine in Japan.
Scientific Reports15(1) (Apr 2025)
15. Xue, H., Li, Y., Lyons, B.A., King, A.J.: #MakeBeefGreatAgain: A Cross-Platform
Analysis of Early #MAHA Discourse (2026).https://doi.org/10.48550/arXiv
.2604.23914,https://arxiv.org/abs/2604.23914
