---
title: 'Finfluencers on TikTok: A Longitudinal Analysis of Content, Engagement, and Disclaimer Practices'
url: https://arxiv.org/abs/2607.05203
category: social-media
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Essam Ghadafi
- Panagiotis Andriotis
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.05203
pages: 16
chars: 42881
fetched_at: '2026-11-08T12:58:00+00:00'
kb_version: 1
---

# Finfluencers on TikTok: A Longitudinal Analysis of Content, Engagement, and Disclaimer Practices

UK Finfluencers on TikTok: A Longitudinal
Analysis of Content, Engagement, and
Disclaimer Practices
Essam Ghadafi1 and Panagiotis Andriotis 2
1 School of Computing, Newcastle University, Newcastle upon Tyne, UK
essam.ghadafi@newcastle.ac.uk
2 Department of Computer Science, University of Birmingham, Birmingham, UK
p.andriotis@bham.ac.uk
Abstract.The rise of social media financial influencers (finfluencers)
has transformed how financial information is disseminated to broad and
often inexperienced audiences. While these creators may contribute to fi-
nancial literacy, concerns remain regarding the reliability of their content
and the adequacy of risk disclosures.
Using data collected through TikTok’s Research API, we analyze UK
finfluencer content, engagement dynamics, disclaimer practices, audi-
ence sentiment, and network structure. The primary dataset comprises
13,215 videos and 104,097 comments posted by 71 UK-based finfluencers
between April and September 2024, while a follow-up dataset covering
October 2025 to March 2026 enables longitudinal analysis of disclaimer
practices, engagement trends, and hashtag usage.
Using topic modeling, we identify four dominant themes: Entrepreneur-
ship & Side Hustles, Property Investing, Active Trading, and Saving &
Budgeting. Sentiment analysis of audience comments reveals predomi-
nantly neutral-to-positive responses, while engagement analysis shows
only a negligible association between video duration and engagement
rate. Social network analysis indicates a collaborative ecosystem in which
mid-tier finfluencers frequently act as bridges between creator groups.
Explicit disclaimers and risk-related language remain relatively uncom-
mon overall and are concentrated primarily in trading-related content.
The findings highlight challenges related to financial transparency and
disclosure practices within short-form financial content ecosystems. We
discuss implications for consumer protection and the design of clearer and
more standardized financial risk disclosures on social media platforms.
1 Introduction
The rise of social media has transformed the dissemination of financial infor-
mation, with so-called financial influencers (or for short finfluencers) playing an
increasingly significant role in shaping public investment behaviour. Platforms
such as TikTok and Instagram have become key sources of financial content,
arXiv:2607.05203v1  [cs.SI]  6 Jul 2026

2 Essam Ghadafi and Panagiotis Andriotis
where influencers promote investment strategies, trading platforms, and cryp-
tocurrency ventures to wide audiences, often without proper regulatory over-
sight [20,22]. While these influencers have the potential to democratise access to
financial knowledge, concerns over misinformation, misleading promotions, and
the risk of financial harm have drawn growing scrutiny from regulators.
In response to these challenges, the UK’s Financial Conduct Authority (FCA)
has strengthened its oversight of financial promotions on social media, empha-
sising that all investment-related content must be fair, clear, and not misleading.
Recent enforcement actions, including interviews under caution and legal pro-
ceedings against finfluencers, signal a move towards stricter regulation [9]. This
paper analyzes finfluencer content, disclaimers, topics, and audience sentiment to
assess how financial advice, marketing, and regulation interact in digital spaces.
TikTok remains one of the world’s most popular social media platforms,
recording 773 million downloads in 2024 [7]. Previous research has examined
influencer marketing effectiveness on TikTok, often focusing on entertainment-
oriented traits such as humour and originality (e.g., [2]), as well as the plat-
form’s structural impact on creative labour and content commodification [13].
Our study examines UK TikTok finfluencers, analysing their content, engage-
ment, audience interactions, and disclosure practices to better understand finan-
cial communication and consumer protection on the platform. Given TikTok’s
popularity among youth [12], examining finfluencers, whose financial advice may
lead to harm or regulatory breaches, is vital for safeguarding financial well-being
and ensuring proper oversight of social media content.
A preliminary preprint version of this study [11] analyzed only the April–
September 2024 observation period and did not include the follow-up analysis
or revised disclaimer framework adopted here.
1.1 Research Questions
This study investigates the following research questions:
– RQ1:To what extent are explicit disclaimers, weak disclaimers, and risk-
oriented language present in UK finfluencer content?
– RQ2:What engagement and audience interaction patterns are associated
with videos containing disclaimer-related language?
– RQ3:How do disclosure practices vary across different financial content
themes?
– RQ4:What structural patterns characterize the UK finfluencer follower net-
work, and how are interactions distributed across influencer tiers or thematic
categories?
1.2 Our Contributions
This paper makes the following contributions:

Finance and UK Finfluencers 3
–We construct and analyze a longitudinal dataset of UK TikTok finfluencers
comprising 21,781 videos and 104,097 comments across two observation pe-
riods (April–September 2024 and October 2025–March 2026), enabling lon-
gitudinal analysis of disclosure practices, engagement, and hashtag trends.
–We propose a rule-based framework for detecting explicit disclaimers, weak
disclaimers, and risk-related language in finfluencer content using keyword
matching, contextual filtering, and regular expressions.
–We conduct an empirical analysis of engagement dynamics, disclosure prac-
tices, sentiment, hashtags, and thematic content within the UK finfluencer
ecosystem.
–We analyze follower-network structure using centrality and connectivity mea-
sures, identifying bridging roles and interaction patterns across influencer
tiers.
–We provide longitudinal insights into the evolution of finfluencer behavior,
including evidence of evolving hashtag usage and changing content patterns
over time.
2 Related Work
Promotions and giveaways are commonly used by influencers to grow their fol-
lower base, but similar tactics are also exploited by cybercriminals to attract
victims and promote illicit content [24]. In cryptocurrency ecosystems, invest-
ment scams remain among the most widespread forms of fraud [19], often in-
volving deceptive websites that promise unrealistic returns [19]. Prior studies
additionally show that influential online figures can significantly amplify at-
tention toward investment opportunities and speculative assets [25]. Existing
research has documented a broad range of cryptocurrency-related frauds, in-
cluding pump-and-dump schemes, phishing attacks, fake crypto services, NFT
scams, and fraudulent ICOs [18]. These findings highlight the importance of
examining the credibility, motivations, and transparency practices of financial
influencers operating on social media platforms.
Recent studies emphasize the growing role of social networks in shaping finan-
cial behavior, particularly among Millennial and Gen Z populations [1, 8]. Social
media platforms are increasingly used for financial education, peer-to-peer pay-
ments, crowdfunding, social commerce, and investment-related discussions [1].
At the same time, concerns have emerged regarding financial misinformation
and fraud, with reports suggesting that a substantial proportion of young adults
obtain financial advice directly from social media [27]. Prior work additionally
shows that teens are increasingly exposed to cryptocurrency-related content and
speculative investment narratives through online communities and influencer-
driven content [6].
Several studies investigate the influence of finfluencers on investor behavior
and financial decision making. Researchers propose finfluencer quality indica-
tors and scoring approaches to distinguish trustworthy influencers from mislead-
ing or manipulative actors [31]. Other work demonstrates that finfluencers can

4 Essam Ghadafi and Panagiotis Andriotis
significantly influence retail investors’ trading behavior, portfolio decisions, in-
vestor attention, and market activity [5, 14, 16]. However, researchers also ques-
tion the expertise and credibility of many finfluencers, particularly those pro-
moting speculative or high-risk investments [26]. Existing studies suggest that
recommendations promoted by finfluencers are frequently associated with poor
post-recommendation performance and elevated risks for investors [10, 17].
Researchers have examined factors influencing investor attitudes toward fin-
fluencer content, highlighting the roles of expertise, credibility, transparency,
and content quality in shaping financial decision making [21, 28]. Other studies
explore how authenticity, disclosure practices, and presentation characteristics
(e.g., accreditation, gender, and race) influence follower perceptions and engage-
ment [22, 30]. The legal implications of finfluencer disclaimers have also received
increasing attention, particularly regarding transparency and the management
of consumer expectations [23]. Finally, Hayes and Ben-Shmuel [13] emphasize
the growing societal influence of finfluencers and the need for continued research
into their disclosure practices and associated risks.
While prior work has explored the influence of finfluencers on investment be-
havior, financial literacy, and market dynamics, limited research has examined
longitudinal disclosure practices, engagement characteristics, audience interac-
tions, and network relationships of TikTok-based finfluencers within a unified
empirical framework. Our work addresses this gap through a large-scale longi-
tudinal analysis of UK TikTok finfluencers, focusing on engagement patterns,
disclaimer usage, audience sentiment, and network structure.
3 Methodology
This section describes our study methodology.
Ethical Considerations.Prior to data collection, ethical approval was ob-
tained from the authors’ universities and funding body. Data was collected using
TikTok’s official Research API [29] in accordance with its terms of service and
relevant ethical guidelines.
Data Collection.To classify finfluencers, we collected 10,000 TikTok videos
for each month from April to September 2024 using the TikTok Research API.
We searched for UK TikTok videos containing finance-related keywords and
hashtags associated with investing, budgeting, cryptocurrency, passive income,
financial literacy, and wealth-building themes. The complete keyword list is
as follows: “budgeting”, “crypto”, “cryptocurrency”, “debtfree”, “debtpayoff”,
“finance”, “financetiktok”, “financialeducation”, “financialfreedom”, “financial-
literacy”, “fintok”, “investing”, “investingtips”, “money”, “moneygamemoney-
mindset”, “moneymanagement”, “moneytok”, “passiveincome”, “personalfinance”,
“realestateinvesting”, “retirementplanning”, “richmindset”, “savemoney”, “stock-
market”, “stocks”, “wealth”, “wealthbuilding”.

Finance and UK Finfluencers 5
We identified users who accumulated at least 50 comments across their videos
and posted at least one video in each month of the April–September 2024 ob-
servation period. This threshold excluded low-activity accounts, yielding 71 fin-
fluencers for analysis. A six-month observation period was chosen to capture
sustained creator activity. From these accounts, we collected 13,215 videos, in-
cluding 4,650 containing spoken transcripts in thevoice to textfield, together
with 104,097 associated comments.
To assess whether observed patterns persisted over time, we collected a
follow-up dataset from the same finfluencer cohort covering October 2025 to
March 2026. During this period, 12 of the original 71 accounts were no longer
accessible through TikTok or the API, resulting in a final cohort of 59 active
accounts. The follow-up dataset contains 8,565 videos and was used for analyses
of disclaimer usage, engagement, and hashtag trends. Comment-level analyses
were restricted to the April–September 2024 dataset because follow-up comments
were not collected.
Due to TikTok Research API governance requirements, the raw dataset and
identifiers are not publicly redistributed.
4 Social Graph and Profile Characteristics of Finfluencers
This section addresses RQ4 through analysis of network structure and connec-
tivity patterns among finfluencers.
Beyond thematic content, we examined credibility signals and disclosure
practices. Only two finfluencers included a bio disclaimer stating that their con-
tent did not constitute financial advice, while three accounts were verified. The
limited use of profile-level disclaimers suggests relatively low emphasis on trans-
parency and risk communication despite the financial nature of the content.
To investigate relationships between finfluencers, we constructed a directed
social graph based on mutual interactions. Figure 1 illustrates follower relation-
ships between anonymized users represented using pseudonyms (e.g.,useri) and
follower-count ranges.
We computed closeness and betweenness centrality to identify structurally
influential accounts within the network.user2anduser35exhibited the highest
closeness centrality, indicating efficient connectivity to other users, whileuser32
anduser12showed the highest betweenness centrality, suggesting important
bridging roles between communities.
Overall, the network exhibited a relatively well-connected structure with sev-
eral users acting as central hubs. Influencers in the 10k–100k follower ranges
appeared most central, suggesting that mid-tier creators play an important role
in maintaining connectivity across the UK finfluencer ecosystem.
5 Video Data Analysis
In this section, we analyse video-level data. Unless otherwise stated, topic model-
ing and comment-level sentiment analysis use the April–September 2024 dataset,

6 Essam Ghadafi and Panagiotis Andriotis
Fig. 1: Directed follower network among finfluencers.
while the follow-up dataset is used for longitudinal analyses of engagement, dis-
claimer practices, and hashtag trends. This section addresses RQ1–RQ3.
5.1 Video Duration vs. Engagement
This analysis contributes to RQ2 by examining engagement characteristics within
finfluencer videos. Engagement rate was computed as the ratio of likes, shares,
and comments to total views. Figure 2 illustrates the relationship between video
duration and engagement rate across videos from both observation periods. Most
videos were relatively short in duration, with a median duration of 47 seconds
and an interquartile range between 19 and 80 seconds. The figure also highlights
substantial variability in engagement across all duration ranges.
To reduce the influence of anomalous records and atypical long-form uploads,
videos with missing metadata, zero views, zero duration, or durations exceeding
600 seconds were excluded from the analysis. Due to the non-normal distribution
of engagement metrics, Spearman’s rank correlation coefficient was used to assess
the relationship between video duration and engagement.
The statistical analysis revealed only a negligible overall association between
duration and engagement (ρ= 0.015,p <0.05). While the correlation was
statistically significant, the observed effect size was negligible, indicating that
video duration alone was not meaningfully associated with engagement outcomes
within the analyzed finfluencer dataset. Engagement is therefore likely influenced
by multiple interacting factors beyond duration alone.
5.2 T opic Modeling and Thematic Consolidation of Videos
To uncover latent thematic structures, we applied Latent Dirichlet Allocation
(LDA) [4] with optimized hyperparameters to our dataset of 13,215 videos. The

Finance and UK Finfluencers 7
Fig. 2: Video duration vs. engagement rate across finfluencer videos.
model was trained on a combination of thevideo description,hashtag names,
andvoice to textfields. Preprocessing included stopword removal, lemmati-
zation, and filtering of general terms.
The LDA model initially identified eight semantically related topics. The
eight initial topics (along with the top five keywords for each) were:
–Topic 0 – Digital Entrepreneurship & Online Income:entrepreneur, digi-
tal products, howtomakemoneyonline, passive income, digitalmarketingtips
–Topic 1 – Property Investment & Wealth Building:investment, prop-
erty investing, propertyportfolio, moneytips, wealthbuilding
–Topic 2 – Forex & Crypto Trading Education:forextrading, trading, trad-
ingforex, investment, crypto trading
–Topic 3 – Property Buying & Real Estate Tips:propertyinvesting, buytolet,
residential, deposit, isa
–Topic 4 – Success Mindset & Startup Motivation:mindset, liquidity, suc-
cesstips, startupstories, entrepreneurialjourney
–Topic 5 – Budgeting & Personal Finance:saving, cashstuffingenvelopes,
debtfree, loudbudgeting, pennysavingchallenge
–Topic 6 – Side Hustles & Work-from-Home:sidehustleforbeginners, wfh,
reseller, sideincome, savemoney
–Topic 7 – Crypto & Beginner Investing:btc, crypto, crypto trading, xrp,
education
To improve interpretability and reduce overlap between closely related themes,
these topics were consolidated into four broader thematic categories:
–Entrepreneurship & Side Hustles: Topics 0, 4, 6
–Property Investing: Topics 1, 3
–Active Trading (Forex & Crypto): Topics 2, 7

8 Essam Ghadafi and Panagiotis Andriotis
–Saving & Budgeting: Topic 5
To further evaluate topic consistency, we also conducted a separate topic
analysis using a BERT-based topic modeling approach. The identified themes
were highly similar to the four merged categories adopted in this study.
Each video was then assigned to its most relevant LDA topic based on key-
word overlap within the tokenized text fields. These assignments were subse-
quently mapped to the merged thematic categories for final analysis.
The topic categorization of the 13,215 analyzed videos is presented in Table 1.
T opic Number of Videos
Entrepreneurship & Side Hustles 6447
Property Investing 1670
Active Trading (Forex & Crypto) 3458
Saving & Budgeting 1640
Table 1: Categorization of the 13,215 videos based on LDA topic assignment.
5.3 Analysis of Disclaimers in Videos
This section primarily addresses RQ1 and RQ2 by examining the prevalence,
characteristics, and engagement-related patterns of disclaimer usage.
To differentiate between finfluencers who clearly encourage their followers to
conduct their own research, take independent action, or include other appropri-
ate disclaimers, we analysed the videos for the presence of such disclaimers.
We analysed the fieldsvideo description,voice to text, andhashtag names
for keywords or hashtags associated with disclaimers. A video was classified as
containing a disclaimer if any of these fields contained either a keyword or a
hashtag associated with disclaimers. We emphasize that the disclaimer analysis
was based on the aforementioned fields, and we did not examine the videos for
visual or voice disclaimers. Therefore, some videos lackingvoice to textmay
still contain disclaimers.
Disclaimers were identified using a rule-based text analysis applied to the
aforementioned fields. This multi-source approach captures both formal dis-
claimers and informal disclaimer-related expressions embedded in social media
content. The primary keyword dictionaries used in the analysis are summarized
in Table 2.
A three-category classification framework was developed:
– Explicit disclaimersare statements denying the provision of financial ad-
vice or encouraging independent verification (e.g., “not financial advice”,
“DYOR”). See Table 2 for the complete keyword dictionary.
– W eak (implicit) disclaimersare indirect responsibility-limiting state-
ments that shift decision-making to the viewer without explicitly denying

Finance and UK Finfluencers 9
financial advice (e.g., “invest at your own risk”, “for educational purposes
only”). Context-sensitive weak keywords were only retained when nearby
advisory or responsibility-related terms were present.
See Table 2 for the complete keyword dictionary.
– Risk languagerefers to statements describing financial uncertainty without
limiting responsibility (e.g., “trading involves risk” and “high risk”). These
were treated separately from disclaimers.
The finance-context filter additionally incorporated trading-, pension-, and property-
related terminology.
Category T ext Keywords Hashtag Keywords
Explicit not financial advice; this is not finan-
cial advice; not investment advice; not
trading advice; not a recommenda-
tion; do your own research; consult a
financial advisor; i am not a financial
advisor; nfa; dyor
#nfa; #dyor; #notfinancialadvice;
#notinvestmentadvice; #notadvice;
#notarecommendation; #cryptotip-
snotadvice; #stocktipsnotadvice;
#cryptonfa; #tradingnfa
Weak at your own risk; invest at your own
risk; only invest what you can afford
to lose; not responsible for losses; no
liability accepted; results not guaran-
teed; for educational purposes only;
you are responsible for your own deci-
sions; take responsibility for your own
decisions; for entertainment purposes
only; for entertainment only; educa-
tional only; not responsible for any
losses; no responsibility for losses
#investatyourownrisk; #entertain-
mentpurposesonly; #education-
alpurposesonly; #tradingdisclaimer;
#pleaseconsult; #onlyyoucanrisk;
#notliable
Context-
sensitive weak seek financial advice; seek advice
Risk capital at risk; trading involves risk;
risk involved; high risk; risky; market
is volatile; this is risky
Table 2: Keyword dictionaries used for disclaimer classification.
Text was pre-processed through lowercasing, punctuation removal, and con-
traction standardisation to improve matching consistency. Disclaimer detection
was implemented using keyword-based matching with regular expressions. For
ambiguous expressions (e.g. “seek advice”), a context-sensitive approach was ap-
plied, requiring nearby advisory or responsibility-related terms (e.g. “consult”,
“advisor”, “responsible”) within a defined textual window.
Disclaimer hashtags were identified both within hashtag fields and embedded
video-description text.
To reduce false positives, exclusion rules were applied to filter out general fi-
nancial discussion (e.g. “risk management”, “portfolio”, “stock market”) where

10 Essam Ghadafi and Panagiotis Andriotis
risk-related terms do not function as disclaimers. Because the follow-up dataset
was collected from all videos posted by the original creator cohort rather than
through finance-specific keyword retrieval, some videos in the later observation
period were unrelated to finance. To reduce false positives in disclaimer analy-
sis, we additionally applied a finance-context filter based on finance-related key-
words, hashtags, and trading or investment terminology extracted from video
descriptions, transcripts, and hashtags. Table 3 therefore reports both total de-
tections and finance-context detections.
V alidation.The classification approach was evaluated through manual review
of a stratified random sample of 100 videos from each month, spanning explicit
disclaimers, weak disclaimers, risk-only videos, and videos with no detected dis-
claimer. Manual inspection indicated a high level of agreement between the auto-
mated classifications and the human assessment, providing confidence that the
rule-based framework achieves high precision for explicit disclaimer detection
while substantially reducing false positives through contextual filtering and ex-
clusion rules. Nevertheless, implicit or highly contextual disclaimer expressions
remain inherently difficult to detect using rule-based approaches and may require
machine-learning methods in future work.
M/Y Videos Exp. W eak Risk Users
T F T F T F T F
Apr-24 2203 2203 12 12 1 1 2 2 5
May-24 2475 2475 31 31 1 1 7 7 15
Jun-24 2023 2023 27 27 0 0 12 12 14
Jul-24 2205 2205 40 40 1 1 10 10 15
Aug-24 2301 2301 20 20 1 1 9 9 11
Sep-24 2008 2008 41 41 0 0 9 9 9
Oct-25 1714 684 7 7 0 0 10 10 9
Nov-25 1450 589 12 12 3 3 20 17 9
Dec-25 1762 742 15 15 0 0 11 11 10
Jan-26 1844 817 5 5 1 1 25 23 10
Feb-26 1633 665 10 9 39 20 19 19 13
Mar-26 1876 703 15 15 35 2 9 9 12
Table 3: Monthly disclaimer statistics across the two observation periods. T
and F denote detections before and after finance-context filtering, respectively.
Users denotes the number of distinct finfluencers posting finance-context videos
containing disclaimer-related language.
Disclaimer-related language varied across both observation periods. Explicit
disclaimers remained relatively infrequent overall, while the follow-up period
showed noticeably higher counts of weak disclaimers and general risk-related
language compared with the April–September 2024 observation window.

Finance and UK Finfluencers 11
M/Y T op 5 Hashtags & Their Occurrence
Apr-24 investingtips (7); investing101, investingforbeginners, investingexplained,
crypto, bitcoin (4); cryptonews, cryptotok (3); ai, ripple, xrp, bitcoinnews,
notfinancialadvice (2)
May-24 crypto (23); bitcoin (11); xrp (9); notfinancialadvice (8); investingforbeginners
(7); turbo, investing, ripple, money, memecoin (6)
Jun-24 crypto (14); cryptocurrency (8); xrp, investing, investing101 (7)
Jul-24 cryptocurrency (15); personalfinance, investing (13); crypto (12); notfinancial-
advice, bitcoin (11)
Aug-24 cryptocurrency (17); bitcoin (16); investing (14); crypto (10); notfinancialad-
vice (9)
Sep-24 bitcoin (32); cryptocurrency (24); notfinancialadvice (23); trading (18); crypto,
investingforbeginners (17)
Oct-25 etf, indexfund (3); stockmarket, stocksandshares, investwithconfidence, yesiin-
vest (2)
Nov-25 personalfinance (4); femaleentrepreneur, abundancemindset, spiritualen-
trepreneur, budgeting, budget, tesla, trading, advice, retirement, mentor, in-
vest, investing, sipp, nvidia, pension, exxonmobil, hedgefunds, advicetok, fund-
smith, gold, moneytiktok, fintiktok, stockmarketinvesting (2)
Dec-25 pension (8); personalfinance, sipp, finance, nvidia, trading, investing (5)
Jan-26 investing, stockmarket, investingtips (5); ai (3); trading, bitcoin, propertyin-
vesting, pension, finance, aiinvestments, landlord, hmo (2)
Feb-26 personalfinanceuk (9); pension (7); investing101, investingmadesimple, crypto,
finance (5)
Mar-26 personalfinance, taxyear, capcut (4); isaallowance, stockmarket (3)
Table 4: Top 5 hashtags and their occurrences in videos with disclaimers.
Table 4 summarizes the most frequent hashtags in disclaimer-related videos.
Hashtags were lowercased, grouped by semantically equivalent variants, and
ranked monthly by frequency.
Across both observation periods, disclaimer-related hashtags were dominated
by cryptocurrency and investment-related terms (e.g., #crypto, #bitcoin, #cryp-
tocurrency, #investing, and #trading), indicating that disclaimer-related lan-
guage was concentrated primarily in trading-oriented content.
T opic Number of Videos with Disclaimers
Entrepreneurship & Side Hustles 24
Property Investing 21
Active Trading (Forex & Crypto) 162
Saving & Budgeting 8
Table 5: Distribution of the 215 videos containing disclaimer-related language
across the four topic categories.

12 Essam Ghadafi and Panagiotis Andriotis
Disclaimers by T opic Category .This analysis addresses RQ3 by examining
how disclaimer practices vary across thematic categories.
We examined how disclaimer-related videos were distributed across the four
topic categories. Of the 215 videos containing disclaimer-related language, Ta-
ble 5 shows the number assigned to each topic. Note that because topic modeling
was conducted on the April–September 2024 dataset, this disclaimer-by-topic
analysis is limited to the original observation period.
It is notable thatActive Trading (Forex & Crypto)had the highest num-
ber of disclaimers, which may reflect the influence of recent guidance issued by
regulatory bodies such as the Financial Conduct Authority (FCA).
Analysis of Disclaimers by User.In the April–September 2024 dataset,
33 finfluencers used disclaimers in at least one video; among them, two also
included profile-level disclaimers, three held verified accounts, and one account
was no longer active.
5.4 Sentiment Analysis of Comments
We have performed a sentiment analysis of the finfluencers’ video comments
for the April–September 2024 dataset. We used the Vader SentimentIntensity-
Analyzer [15] to calculate sentiment scores for cleaned comments. V ADER was
selected because it is computationally efficient and widely used for short-form
social media text containing slang, emojis, and informal expressions.
To clean (pre-process) the comments, we removed URLs, mentions, and hash-
tags. We also normalized repeated characters and kept only alphabetic charac-
ters. We finally removed stop words using NLTK [3].
Our sentiment analysis process involved calculating a sentiment score for the
text and a separate score for the emojis for each cleaned video’s comment. A
final sentiment score for each comment was computed as a weighted sum: 0.8×
text score + 0.2×emoji score. A higher weight was assigned to textual sentiment
because emojis typically supplement rather than replace semantic meaning. This
was repeated for all comments, and the average of the combined scores was used
to determine the video-level sentiment. The video-level sentiment was classified
as negative (−1≤x <−0.05), neutral (−0.05≤x≤0.05), or positive (0.05<
x≤1), wherexdenotes the average sentiment score. These thresholds follow
commonly used polarity boundaries in V ADER-based sentiment classification.
We also separately calculated the classification based solely on the text score
in order to compare the two approaches. The combined approach was adopted
because emojis may also convey sentiment.
We present the summary of our analysis per month in Table 6. Note that the
difference in the monthly video count here and in earlier sections is due to videos
with no comments or videos whose comments are not accessible (e.g., they have
been deleted). The figure next to each month indicates the number of videos
that month with at least one accessible comment.
Most videos exhibited neutral or positive sentiment, with relatively few strongly
negative videos. Disclaimer prevalence remained low across sentiment categories,

Finance and UK Finfluencers 13
with no consistent relationship between disclaimer usage and comment engage-
ment. The most frequently occurring hashtags were broadly similar across the
negative and neutral sentiment categories, with #money, #crypto, and #forex
appearing consistently in both. Overall, the findings highlight the limited use
of disclaimers in financial TikTok content despite the prevalence of investment-
related discussions.
Mon. Sentiment #V (C/T)VDC Avg. C. VD Avg. C. T op Hashtags
Apr Negative 102/118 1 3.1 1 money (35), forex (28), crypto (28), investing (27), trading (22)
(1465) Neutral 313/319 2 7.2 1.5 money (133), forex (85), trading (73), finance (59), crypto (57)
May Negative 110/129 5 2.4 2.4 forex (35), money (34), trading (32), crypto (30), forextrading (23)
(1609) Neutral 343/360 3 5.3 3.3 money (106), crypto (79), forex (66), investing (58), trading (57)
Jun Negative 70/91 3 2.4 4.3 money (26), crypto (21), forex (21), trading (19), wifimoney (18)
(1339) Neutral 294/305 4 4.3 1.3 money (92), crypto (65), trading (51), investing (49), forex (46)
Jul Negative 101/125 3 2.2 3.3 trading (35), crypto (34), money (33), forex (32), forextrading (26)
(1461) Neutral 329/342 9 5 3.3 money (124), crypto (79), investing (58), entrepreneur (58), trading (57)
Aug Negative 77/97 2 3.2 3 money (31), trading (25), forex (23), crypto (22), forextrading (21)
(1599) Neutral 250/259 3 9.9 3 money (110), trading (42), investing (41), crypto (39), viral (38)
Sept Negative 39/52 2 2.3 4.5 money (20), investing (15), trading (12), forex (9), forextrading (7)
(1368) Neutral 190/196 6 10.6 11.5 money (82), investing (52), trading (46), crypto (43), forex (41)
Table 6:Summary of sentiment analysis of videos. The number of videos (#V) is shown in the format (C/T), where C is the Combined score
(i.e., Text and Emoji) and T is Text Only. Hashtag counts are based on the Combined score.VDCdenotes the number of videos containing
disclaimers.Avg. C.refers to the average number of comments per video, whileVD Avg. C.is the average number of comments on videos
that include a disclaimer.
6 Conclusion
This study provides a longitudinal analysis of UK TikTok finfluencers, examining
engagement dynamics, disclosure practices, hashtag trends, sentiment patterns,
and network structure across two observation periods. Topic modeling of the
April–September 2024 dataset identified four dominant themes:Entrepreneur-
ship,Property Investing,Active Trading, andSaving & Budgeting, reflecting the
core narratives in financial discourse on the platform.
Engagement levels varied substantially across the dataset, although video
duration showed only a negligible association with engagement rate. Social net-
work analysis indicated a collaborative ecosystem in which mid-tier finfluencers
frequently acted as bridges between creator groups.
Sentiment across videos skewed neutral to positive, with few instances of
negative tone. Explicit disclaimers remained relatively uncommon across both
observation periods, although weak disclaimers and general risk-related language
became more prevalent in parts of the follow-up dataset. Notably, disclaimers
were predominantly associated with active trading content (e.g., forex and cryp-
tocurrency), likely reflecting recent regulatory guidance emphasizing the im-
portance of risk disclosure in financial content. However, their presence showed
limited association with engagement patterns, while financial hashtags such as
#crypto and #bitcoin remained common in disclaimer-related content.

14 Essam Ghadafi and Panagiotis Andriotis
These findings suggest that transparency remains limited within the UK
finfluencer ecosystem, with explicit disclaimers remaining relatively uncommon
despite the prominence of trading-related content.
This study has several limitations. The analysis focuses on UK-based Tik-
Tok finfluencers identified through finance-related keywords and therefore may
not generalize to other platforms, regions, or influencer categories. Some anal-
yses, including topic modeling and sentiment analysis, were restricted to the
original observation period due to data availability constraints. Videos lacking
transcribed speech may also contain undetected disclaimers.
Overall, the findings highlight the need for stronger transparency and regu-
latory oversight of finfluencer content. Based on the low prevalence of explicit
disclaimers, platforms and regulators should encourage clearer risk disclosures,
particularly for trading-related content. Social media platforms could also im-
plement standardized content labeling or financial literacy prompts to help users
better assess the reliability of financial information.
Acknowledgement
This work was supported in part by the REPHRAIN National Research Centre
on Privacy, Harm Reduction and Adversarial Influence Online.
References
1. Baird, S.: Social media for personal finances: A new trend for millennials and gen
Z. Payments System Research Briefing pp. 1–6 (October 2023)
2. Barta, S., Belanche, D., Fern´ andez, A., Flavi´ an, M.: Influencer market-
ing on TikTok: The effectiveness of humor and followers’ hedonic expe-
rience. Journal of Retailing and Consumer Services70, 103149 (2023).
https://doi.org/https://doi.org/10.1016/j.jretconser.2022.103149,https://www.
sciencedirect.com/science/article/pii/S0969698922002429
3. Bird, S., Loper, E., Klein, E.: Natural Language Processing with Python. O’Reilly
Media, Inc. (2009),https://www.nltk.org/book/
4. Blei, D.M., Ng, A.Y., Jordan, M.I.: Latent dirichlet allocation. Journal of Machine
Learning Research3, 993–1022 (2003),https://www.jmlr.org/papers/volume3/
blei03a/blei03a.pdf
5. Bongini, P., Maurino, A., Osborne, F., Rossolini, M.: Influencers and investors:
Social media’s role in shaping market movements (2025), available at SSRN:https:
//dx.doi.org/10.2139/ssrn.5110329
6. Bouma-Sims, E., Hassan, H., Nisenoff, A., Cranor, L.F., Christin, N.: “It was
honestly just gambling”’: investigating the experiences of teenage cryptocurrency
users on reddit. In: Proceedings of the Twentieth USENIX Conference on Usable
Privacy and Security. SOUPS ’24, USENIX Association, USA (2024)
7. Business of Apps: Most popular apps.https://www.businessofapps.com/
data/most-popular-apps/(2024),https://www.businessofapps.com/data/
most-popular-apps/, accessed: 2026-06-30
8. Cao, Y., Gong, F., Zeng, T.: Antecedents and consequences of using social media
for personal finance. Journal of Financial Counseling and Planning (2020)

Finance and UK Finfluencers 15
9. Financial Conduct Authority: FCA cracks down on illegal finflu-
encers - Press Release.https://www.fca.org.uk/news/press-releases/
fca-cracks-down-illegal-finfluencers(2024), accessed: 2026-06-30
10. Gerritsen, D., de Regt, A.: Influencers and consumer financial decision-
making. International Journal of Consumer Studies49(2), e70037 (2025).
https://doi.org/https://doi.org/10.1111/ijcs.70037,https://onlinelibrary.
wiley.com/doi/abs/10.1111/ijcs.70037, e70037 IJC-PA-2024-464.R6
11. Ghadafi, E., Andriotis, P.: UK finfluencers: Exploring content, reach, and respon-
sibility. arXiv preprint arXiv:2505.01941 (2025),https://arxiv.org/abs/2505.
01941
12. Haenlein, M., Anadol, E., Farnsworth, T., Hugo, H., Hunichen, J., Welte,
D.: Navigating the new era of influencer marketing: How to be successful
on Instagram, TikTok, & Co. California Management Review63(1), 5–25
(2020). https://doi.org/10.1177/0008125620958166,https://doi.org/10.1177/
0008125620958166
13. Hayes, A.S., Ben-Shmuel, A.T.: Under the finfluence: Financial influencers, eco-
nomic meaning-making and the financialization of digital life. Economy and
Society53(3), 478–503 (2024). https://doi.org/10.1080/03085147.2024.2381980,
https://doi.org/10.1080/03085147.2024.2381980
14. Hull, I., Qi, Y.: The impact of finfluencers on retail investment (2024), available
at SSRN:https://dx.doi.org/10.2139/ssrn.4922031
15. Hutto, C.J., Gilbert, E.: V ADER: A parsimonious rule-based model for sentiment
analysis of social media text. In: Proceedings of the International AAAI Conference
on Web and Social Media. ICWSM ’14, vol. 8, pp. 216–225. AAAI Press (2014).
https://doi.org/10.1609/icwsm.v8i1.14550
16. Keasey, K., Lambrinoudakis, C., Mascia, D.V., Zhang, Z.: The im-
pact of social media influencers on the financial market performance
of firms. European Financial Management31(2), 745–785 (2025).
https://doi.org/https://doi.org/10.1111/eufm.12513,https://onlinelibrary.
wiley.com/doi/abs/10.1111/eufm.12513
17. Krause, D.: The impact of financial influencers on crypto markets: Systemic risks
and regulatory challenges (2025), available at SSRN:https://dx.doi.org/10.
2139/ssrn.5144847
18. Liu, E., Kappos, G., Mugnier, E., Invernizzi, L., Savage, S., Tao, D., Thomas,
K., Voelker, G.M., Meiklejohn, S.: Give and take: An end-to-end investigation of
giveaway scam conversion rates. In: Proceedings of the 2024 ACM on Internet
Measurement Conference. p. 704–712. IMC ’24, Association for Computing Ma-
chinery, New York, NY, USA (2024). https://doi.org/10.1145/3646547.3689005,
https://doi.org/10.1145/3646547.3689005
19. Muzammil, M., Pitumpe, A., Li, X., Rahmati, A., Nikiforakis, N.: The poorest man
in babylon: A longitudinal study of cryptocurrency investment scams. In: THE
WEB CONFERENCE (2025),https://openreview.net/forum?id=P0x8J5gCPP
20. Olajide, O., Pandey, S., Pandey, I.: Social media for investment advice and fi-
nancial satisfaction: Does generation matter? Journal of Risk and Financial Man-
agement17(9) (2024). https://doi.org/10.3390/jrfm17090410,https://www.mdpi.
com/1911-8074/17/9/410
21. Pokhrel, L., Bhattarai, P., and, S.K.P.: Are financial influencers helping us
with financial decision-making? an application of structural equation modeling
and artificial neural networking approach. Journal of Promotion Management
31(3), 485–514 (2025). https://doi.org/10.1080/10496491.2025.2466591,https:

16 Essam Ghadafi and Panagiotis Andriotis
//doi.org/10.1080/10496491.2025.2466591
22. de Regt, A., Cheng, Z., Fawaz, R.: Young people under ‘finfluencer’: The rise
of financial influencers on instagram: An abstract. In: Optimistic Marketing in
Challenging Times: Serving Ever-Shifting Customer Needs. pp. 271–272. Springer
Nature Switzerland, Cham (2023)
23. Rogge, N., Vanden Eynde, S.: The legal implications of disclaimers used by finflu-
encers. In: Kerckaert, Julie and Geiregat, Simon (ed.) Social media influencers and
the #Law, pp. 129–162. LeA Publishers (2024)
24. Roy, S.S., Vafa, E.P., Khanmohammadi, K., Nilizadeh, S.: DarkGram: A large-
scale analysis of cybercriminal activity channels on telegram. In: Proceedings of
the 34th USENIX Security Symposium (USENIX Security ’25). pp. 4839–4858.
USENIX Association, Seattle, W A, USA (Aug 2025)
25. Saha Roy, S., Das, D., Bose, P., Kruegel, C., Vigna, G., Nilizadeh, S.: Un-
veiling the risks of nft promotion scams. Proceedings of the International
AAAI Conference on Web and Social Media18(1), 1367–1380 (May 2024).
https://doi.org/10.1609/icwsm.v18i1.31395,https://ojs.aaai.org/index.php/
ICWSM/article/view/31395
26. Singh, S., Sarva, M.: The rise of finfluencers: A digital transformation in invest-
ment advice. Australasian Accounting, Business and Finance Journal18(3) (2024).
https://doi.org/https://doi.org/10.14453/aabfj.v18i3.14
27. Sortlist Data Hub: Finance Influencers Have a Positive Impact on 50% of People
(2022),https://www.sortlist.com/datahub/reports/finance-influencers/
(accessed July 4, 2026)
28. Symbiosis, A.R., Gandhi, A.: Finfluencer: Exploring the untapped influ-
ence of financial influencers. In: 2024 14th International Conference on
Advanced Computer Information Technologies (ACIT). pp. 190–196 (2024).
https://doi.org/10.1109/ACIT62333.2024.10712618
29. TikTok for Developers: Getting Started - Research API.https://developers.
tiktok.com/doc/research-api-get-started(2024), accessed: 2026-06-30
30. Zhu, L., and, Y.W.: Acting real: a cross-cultural investigation of finflu-
encer strategic authenticity. International Journal of Advertising44(1), 164–
183 (2025). https://doi.org/10.1080/02650487.2024.2437289,https://doi.org/
10.1080/02650487.2024.2437289
31. Z¨ ulch, H., M¨ olders, M., Hoffmann, C.P.: Navigating the rise of fin-
fluencers: a multidimensional quality framework for strategic part-
nerships. Journal of Financial Services Marketing31(1), 26 (2026).
https://doi.org/https://doi.org/10.1057/s41264-025-00334-7
