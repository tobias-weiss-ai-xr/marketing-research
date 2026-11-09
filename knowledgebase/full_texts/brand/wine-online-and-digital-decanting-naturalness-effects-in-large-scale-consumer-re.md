---
title: 'Wine Online and Digital Decanting: Naturalness Effects in Large-Scale Consumer Reviews of Wine'
url: https://doi.org/10.36253/wep-19943
category: brand
subcategory: empirical
date: 2026-08
venue: Wine Economics and Policy
authors:
- Michał Folwarczny
- Magalie Dubois
- Vincent Clerc
source: openalex-oa
pdf_url: https://oaj.fupress.net/index.php/wep/article/download/19943/15334
pages: 29
chars: 79986
fetched_at: '2026-11-08T19:06:53+00:00'
kb_version: 1
---

# Wine Online and Digital Decanting: Naturalness Effects in Large-Scale Consumer Reviews of Wine

1

     Wine Online and Digital Decanting: Naturalness Effects in Large-Scale 1
Consumer Reviews of Wine 2
Michał Folwarczny1, Magalie Dubois2, Vincent Clerc3, Bruno Schivinski4, Tobias Otterbring5 3
 4
1 Discipline of Marketing, J.E. Cairnes School of Business & Economics, University of 5
Galway, Ireland, Email: michal.folwarczny@universityofgalway.ie 6
2 School of Wine & Spirits Business, Université Bourgogne Europe, Burgundy School of 7
Business, CEREN EA 7477, France, Email: magalie.dubois@bsb-education.com 8
3 Independent Researcher, Email: vincent.clerc.ucbl@gmail.com 9
4 School of Media and Communication, RMIT University, Australia; Gdansk University of 10
Technology, Gdansk, Poland, Email: bruno.schivinski@gmail.com 11
5School of Business and Law, Department of Management, University of Agder, Norway, and 12
School of Electrical Engineering and Computer Science, Division of Media Technology and 13
Interaction Design, KTH Royal Institute of Technology, Sweden , Em ail: 14
tobias.otterbring@uia.no 15
 16
Correspondence concerning this article should be addressed to Michał Folwarczny, Discipline 17
of Marketing, J.E. Cairnes School of Business & Economics, University of Galway, Ireland , 18
michal.folwarczny@universityofgalway.ie. This article has been accepted for publication and 19
undergone full peer review but has not been through the copyediting, typesetting, pagination 20
and proofreading process, which may lead to differences between this version and the Version 21
of Record. 22
 23
Please cite this article as: 24
 25
Folwarczny M, Dubois M., Clerc V., Schivinski B., Otterbring T. (2026),      Wine Online and 26
Digital Decanting: Naturalness Effects in Large -Scale Consumer Reviews of Wine , Wine 27
Economics and Policy, Just Accepted. 28
DOI: 10.36253/wep-19943 29

2

 30
Abstract 31
Purpose: This study investigates how the naturalness shapes online wine reviews through the 32
lens of information asymmetry and credence attributes. 33
Methodology: We analyze over six million consumer reviews from a global platform using 34
computational linguistics to compare evaluative and affective responses between natural and 35
conventional wines. 36
Findings: Compared to conventional wines, natural wines command a twenty percent price 37
premium and elicit longer consumer reviews; however, they systematically receive lower 38
quality ratings and yield less positive per-word sentiment. Further, they have a more polarized 39
emotional profile marked by increased negative emotions, such as disgust and anger, combined 40
with slightly higher levels of joy. 41
Originality: The current findings challenge the natural-is-better bias and advance authenticity 42
theory and wine economics by demonstrating that naturalness operates as a quality signal that 43
drives expectation disconfirmation rather than hedonic satisfaction. 44
Implications: Managers of natural wine brands should position naturalness as a credence 45
attribute and implement proactive expectation management regarding variable sensory profiles 46
to mitigate negative affective responses while leveraging the price premium associated with 47
authenticity. 48
 49
 50
Keywords: natural wine; naturalness bias; psychological essentialism; authenticity; sentiment 51
analysis; computational linguistics; electronic word-of-mouth 52
 53
 54
 55
 56
 57

3

1. Introduction 58
Current consumer demand is characterized by a pervasive preference for naturalness. This 59
preference has shifted from constituting a niche lifestyle choice to a dominant driver of market 60
value within the food and beverage sector [1]. The naturalness bias represents a tendency for 61
consumers to favor entities perceived as being of natural origin or produced through minimal 62
human intervention, and perceiving such entities as superior to conventional counterparts even 63
when objective quality remains ambiguous [2]. In the wine industry, natural has emerged as a 64
primary claim, acting as a powerful credence attribute to signal quality and safety to the public 65
[1,3]. Despite this ubiquity, the term remains remarkably unregulated and ill -defined by legal 66
standards [4]. As a case in point, within the European Union, no recognized definition exists at 67
the regulatory level, leaving natural wine largely absent from bottle labels as a protected 68
designation [5]. Yet consumers maintain a consistent internal prototype of what natural is and 69
is not [6,7]. Central to this conception is the idea that a product has not been transformed and 70
maintains a pure, untainted essence [8]. 71
Within the wine industry, the naturalness movement has developed into the natural wine 72
category. This segment is defined by a commitment to minimal intervention viticulture, 73
typically involving organic or biodynamic farming, the use of indigenous yeasts, and the 74
avoidance of additives such as sulfur dioxide [9]. Extensive literature has examined established 75
eco-friendly typologies, demonstrating that organic and biodynamic certifications command 76
significant price premiums and alter consumer quality perceptions [10,11]. Hedonic analyses 77
consistently find that certified organic wines command price premiums over conventional 78
counterparts [12,13]. Similarly, consumer willingness -to-pay studies establish a hierarchy 79
across minimal -intervention categories, with organic wines commanding the highest 80
willingness-to-pay, followed by natural wine, and biodynamic wines ranking lowest due to 81
lower consumer familiarity [14,15]. Building upon this foundation, natural wine represents a 82
more radical, albeit unregulated, extension of the minimal intervention ethos. This distinction 83
fundamentally shapes consumer perception. Consequently, recent evidence indicates that 84
consumers evaluate natural, organic, and biodynamic wines through partially overlapping but 85
distinct attribute structures. Specifically, naturalness signals a stronger ideological and process-86
based commitment than formal certification -based categories  [16,17]. Furthermore, natural 87
wine acts as a compelling subject for marketing and consumer research because its value is 88
derived not only from its sensory profile but also from its process history, the specific narrative 89
of what has not been done to the grapes [18]. As wine is an experience good, and natural wine 90

4

specifically a credence good whose defining attributes cannot be verified even after 91
consumption [16], consumers cannot easily assess its quality prior to consumption, leading 92
them to rely heavily on extrinsic cues (such as labels, certifications, and price) and word -of-93
mouth as mediated through digital platforms [19,20].      94
Consumers’ preference for naturalness is frequently justified through instrumental claims, such 95
as the belief that natural products are healthier, safer, or more environmentally friendly [1]. 96
However, evidence suggests that these justifications are often post -hoc rationalizations [21]. 97
Indeed, research in wine and food marketing has shown that preferences for natural, organic, 98
and minimally processed products are frequently driven by ideological and moral alignment 99
rather than purely sensory superiority [7]. Under this perspective, naturalness is not merely a 100
physical state but a marker of authenticity, reflecting an underlying essence that is preserved 101
through minimal contact with industrial modernity [22,23]. 102
However, a significant knowledge gap remains in the literature. A growing body of wine -103
specific studies has applied computational linguistics and large -scale review mining to map 104
consumer reviews across different contexts. Sentiment analysis has been used to examine the 105
internal consistency of expert wine guide reviews [24]. Text mining and topic modelling have 106
been applied to characterize the vocabulary of expert and amateur reviewers on specialized 107
wine websites [25]. Large -scale Vivino data have been used to examine factors influencing 108
consumer ratings across wine attributes and price points [26], the relationship between 109
expertise, emotionality, and review behavior [27], reputation inflation in numerical ratings 110
relative to text -based quality signals [28], and the link between wine label content and 111
consumer reviews [29]. Most recently, [30] and [7] applied computational linguistic methods 112
specifically to large-scale wine review data to examine flavor dynamics, vocabulary evolution, 113
and the transition from expert to peer review. However, none of these studies applied sentiment 114
analysis and emotion profiling to isolate the affective and evaluative consequences of a 115
credence-based category such as natural wine, nor to benchmark such a category against its 116
conventional counterpart at platform scale. As such, there remains a fundamental lack of 117
knowledge regarding how these metaphysical beliefs translate into affective and evaluative 118
structures of spontaneous consumer reviews [31]. Specifically, the literature does not 119
sufficiently explain how the perceived authenticity of a product's essence influences the 120
complex emotional tone in consumer reviews, such as the interplay between trust and disgust, 121
outside of artificial experimental conditions. Guided by recent calls for research from more 122
realistic consumption contexts [32,33,34,35], alongside signaling theory and the credence -123

5

goods framework from wine and applied economics, the current study integrates authenticity 124
theory with psychological essentialism. It aims to explain how minimal intervention signals 125
the preservation of a product's true self, while simultaneously functioning as a market signal 126
that justifies a price premium among engaged consumer segments [36]. Under this framework, 127
naturalness is both a prerequisite for authenticity and a credence -based quality signal, and 128
human intervention is perceived to dilute the valued essence of the origin [23]. This provides 129
a means to explain why consumers prioritize process history over objective content in 130
unconstrained digital environments, even when such prioritization coexists with lower 131
aggregate sensory ratings. 132
The current research uses a large -scale analysis of over 6 million consumer reviews through 133
computational linguistics to address this theoretical gap. While previous studies have 134
successfully utilized text -mining and large -scale review analysis to understand general wine 135
preferences, quality pricing, and regional typicity [30], this methodology has not yet been 136
explicitly applied to isolate the affective dimensions of the minimal -intervention movement, 137
nor to benchmark natural wine against its conventional counterpart at platform scale. By 138
identifying the specific emotional and evaluative patterns that distinguish natural wine from its 139
conventional counterparts, the study maps the linguistic signatures of perceived authenticity in 140
the digital marketplace. Theoretically, this research advances authenticity theory by 141
demonstrating how essentialist beliefs interact with credence-based market signaling to shape 142
value in digital marketplaces. Practically, the findings provide a strategic framework for 143
managers to navigate the delicate signals of purity and industrial aversion that drive value in 144
the natural wine segment. 145
2. Theoretical Background and Hypotheses 146
2.1. Authenticity and Psychological Essentialism 147
Over the last decades, authenticity has transitioned from a niche luxury attribute to a primary 148
purchasing criterion, often superseding objective quality cues as a determinant of consumer 149
choice [5,37]. In a marketing context, authenticity is defined as the extent to which a product 150
is perceived to be genuine, real, and true to its internal nature [38,39]. For natural wine, this 151
perception is not merely based on sensory performance but on a perceived alignment between 152
the brand's output and its proclaimed values of minimal intervention and environmental 153
stewardship [16]. In markets for credence goods, where defining attributes cannot be verified 154

6

by the consumer, such authenticity perceptions function simultaneously as a meaning -making 155
device and as a quality signal that supports market value [16]. 156
The cognitive mechanism driving these authenticity judgments is psychological essentialism, 157
the lay belief that certain categories possess an underlying, unobservable essence that 158
determines identity and value [23,40]. Consumers rely on such an essentialism framework to 159
evaluate products of natural origin, believing that the true self of a product is found in its 160
untainted state [36]. Within the wine domain, this essence is grounded in the terroir, 161
representing the unique combination of soil, climate, and topography [ 16,18]. From an 162
essentialist perspective, human intervention in the form of industrial processing or synthetic 163
additives may reduce the connection to the valued source, thereby reducing the product's 164
perceived authenticity, ultimately decreasing its perceived value [8,23,41]. 165
A critical principle of essentialism is that process dominates content [8]. This implies that the 166
perceived history of an object—what has or has not been done to it—is more diagnostic of its 167
naturalness than its final material composition [8]. For instance, an entity that undergoes a 168
transformation and is then restored to its original state is rated as less natural than one that was 169
never transformed, despite being chemically identical [1,8]. In the natural wine context, this 170
principle can be exemplified across a host of dimensions associated with authenticity, such as 171
production methods, transparency of practice, aesthetic qualities, historical traditions, and the 172
personal characteristics of the producer  [42].  The minimal intervention narrative serves as a 173
powerful authenticity cue because it signals the preservation of the original essence throughout 174
the production process [9,18]. Natural wine producers emphasize this logic explicitly, 175
describing their practice as maximizing terroir expression by minimizing cellar correction, a 176
philosophy in which the less the producer intervenes, the more authentic the wine is perceived 177
[43,44].  178
Furthermore, the perception of an authentic essence has significant affective consequences. 179
Authenticity is psychologically rooted in trustworthiness and sincerity; products perceived as 180
authentic are viewed as less risky and more aligned with the consumer's own moral identity 181
[39,45]. Conversely, the detection of inauthenticity or industrial processes during production 182
can trigger a moralized aversion, often manifesting as disgust, which serves as the primary 183
emotional defense against perceived contamination [23,46]. In the wine domain, this dynamic 184
is particularly salient: natural wine producers and their advocates explicitly frame conventional 185
winemaking additives and cellar interventions as contaminants that compromise the wine's 186
authentic essence [47]. Consumers of natural wine have been shown to evaluate sensory 187

7

compounds such as volatile acidity, turbidity or Brettanomyces markedly differently depending 188
on whether the wine is framed as natural or conventional, suggesting that the authenticity frame 189
itself modulates the affective response to the physical product [48]. 190
Although the hypotheses below are framed directionally, the natural -wine there might be also 191
substantial sensory heterogeneity and lower perceived quality relative to conventional 192
benchmarks (a competing mechanism we revisit in the Discussion). 193
2.2. Naturalness and Quality Ratings 194
Consumers’ preference for naturalness is driven by a pervasive cognitive default known as the 195
natural-is-better bias, wherein entities of natural origin are systematically favored over 196
synthetic counterparts [49]. According to authenticity theory and signaling economics, 197
naturalness serves as a primary heuristic and quality signal, as consumers associate the absence 198
of human intervention with the preservation of an uncorrupted, valuable state [50,51]. This 199
evaluative pattern is particularly salient in the food and beverage industry, where natural claims 200
function as a surrogate for overall excellence and safety [1]. 201
Psychological essentialism provides the mechanism for this quality attribution by suggesting 202
that consumers believe minimal processing allows a product to remain true to its inherent 203
essence [23,52]. For wine, which is categorized as an experience good, the lack of prior 204
knowledge regarding quality forces reliance on extrinsic signals [19]. Because the preservation 205
of this essence cannot be visually verified, the designation of a wine as natural acts as a crucial 206
credence signal of authenticity, prompting consumers to infer superior gustatory and technical 207
quality from the process history of minimal intervention [9,18]. 208
Recent research from experimental wine settings indicates that perceived naturalness 209
significantly alters sensory and quality perceptions, even after the product has been consumed 210
[31]. This effect is often characterized by a halo effect, where a positive impression of 211
naturalness spills over into other evaluative dimensions, such as perceived sustainability and 212
overall quality ranking [31,53,54]. Consequently, wines identified as natural are expected to 213
receive systematically higher evaluations in crowdsourced online environments compared to 214
conventional wines. Therefore, we hypothesize: 215
H1: Natural wines receive higher quality ratings compared to conventional wines. 216
2.3. Naturalness and Price Premiums 217

8

The valuation of authenticity and credence attributes is fundamentally reflected in consumers’ 218
willingness to pay a price premium [55]. Psychological essentialism suggests that the 219
preservation of an unobservable essence renders a product more desirable and unique, thereby 220
justifying a higher financial sacrifice [23], especially given the price -quality inferences made 221
by consumers within and beyond the wine market [56,57]. These general mechanisms translate 222
directly into the wine sector. Authenticity markers such as terroir and artisanal production 223
methods are closely linked to increased market value and prestige [5,58]. Research indicates 224
that consumers assign higher monetary value to products perceived as genuine and true to their 225
source of production, as the absence of industrial intervention is viewed as a form of natural 226
rarity [58,59]. Specifically, recent empirical evidence explicitly demonstrates that the presence 227
of natural attributes in wine significantly increases consumer willingness to pay a premium, 228
confirming the economic value of the naturalness signal [17]. 229
Furthermore, the literature supports that price often functions as an extrinsic signal that 230
reinforces perceptions of quality in high -risk purchase situations involving experience goods 231
[19], particularly at the point of purchase and in pre -consumption expectations. Because the 232
production of natural wine involves greater risk and potentially higher costs due to the rejection 233
of standardized chemical stabilizers, the resulting scarcity further enhances its premium 234
positioning [16,60]. According to this perspective, consumers are expected to accept higher 235
prices as a legitimate reflection of the product's authentic, unadulterated nature and its status 236
as a high-value credence good. Therefore, we posit: 237
H2: Natural wines command price premiums compared to conventional wines. 238
2.4. Naturalness and Review Length 239
The perception of authenticity is a fundamental driver of consumer engagement and elaboration 240
in digital environments [61]. Psychological essentialism suggests that when individuals 241
consume products with a perceived unadulterated essence, the experience is internalized as 242
more personally relevant and meaningful [23]. This heightened self -relevance often triggers a 243
desire to elaborate on the experience, leading to increased engagement [62], possibly also 244
manifested as a more extensive communication pattern. In the context of electronic word -of-245
mouth, review length serves as a primary indicator of the cognitive and emotional effort 246
consumers invest in sharing their evaluations [62]. 247
Further, because natural wine functions as a credence good with a highly variable and often 248
unconventional sensory profile, the consumption experience inherently demands greater 249

9

cognitive processing [7]. Because natural wine is characterized by a specific production history 250
of minimal intervention, it provides a more fertile ground for narrative storytelling than 251
standardized industrial products [63]. Consumers are more likely to provide detailed accounts 252
of the origin, production methods, and the complex sensory nuances when they perceive a 253
brand to be genuine and true to its source [64], especially when attempting to reconcile their 254
expectations with an unfamiliar gustatory reality [11]. Consequently, natural wines are 255
expected to elicit more extensive reviews than their conventional alternatives because 256
consumers should try to articulate the complexity and perceived authenticity of the product to 257
a greater extent in the former case. Importantly, longer reviews do not necessarily signal more 258
positive evaluations. The same elaboration that supports enthusiastic storytelling can also 259
support detailed criticism when the sensory experience fails to meet expectations. Thus, we 260
hypothesize: 261
H3: Natural wines elicit longer reviews compared to conventional wines. 262
2.5. Naturalness and Sentiment 263
The consumption of products perceived as natural or environmentally friendly is frequently 264
associated with distinct positive affective states [31]. Naturalness functions as a premium 265
credence attribute; this quality signal generates strong pre -consumption expectations of 266
hedonic superiority [17]. Recent research identifies a green consumption effect, wherein the 267
usage of products with sustainable or natural attributes enhances the overall enjoyment of the 268
consumption experience [65]. This effect suggests that the perceived moral value of the 269
product, derived from its minimal intervention or environmental benevolence, translates into 270
higher customer satisfaction [65]. Such internal states of enjoyment and satisfaction are 271
typically externalized through linguistic valence [66]. Studies analyzing social media 272
communications regarding organic and natural food products indicate a prevalence of positive 273
sentiment, driven by themes of health, safety, and ethical consumption [63]. When consumers 274
engage with natural wine, the authenticity of the production method acts as a positive cue that 275
frames the consumption experience as virtuous and pleasurable [67]. Consequently, the 276
terminology used to describe natural wines is expected to reflect this heightened state of 277
enjoyment and moral satisfaction. Thus, we predict: 278
H4: Natural wines elicit more positive sentiment compared to conventional wines. 279
2.6. Naturalness and Emotion Profiles 280

10

While sentiment analysis provides a measure of overall valence, it fails to capture the specific 281
discrete emotions that drive consumer behavior. Authenticity theory suggests that perceptions 282
of sincerity elicit a complex emotional response that extends beyond enjoyment and 283
satisfaction alone [68]. Specifically, the projection of a sincere, untainted essence is closely 284
linked to trust. Consumers view the absence of industrial intervention as a signal of honesty 285
and safety, acting as a quality signal that mitigates the information asymmetry and perceived 286
risk inherent to credence goods [31]. Consequently, narratives surrounding natural wine are 287
expected to contain a higher relative prevalence of trust -related words, reflecting the 288
consumer's confidence in the product's integrity. It is nonetheless worth noting that trust-related 289
terms in experiential consumer reviews may also be constrained by the descriptive vocabulary 290
consumers conventionally use for sensory evaluation, which can mask their underlying 291
confidence in the product [64,69]. 292
Conversely, the violation of naturalness is frequently processed through the psychological 293
mechanism of disgust. Disgust serves as an evolved defensive emotion designed to protect the 294
body from contamination [70]. For foods and beverages, synthetic additives or heavy industrial 295
processing are often perceived as contaminating the product's purity, thereby triggering 296
rejection [71,72]. Because natural wine is defined explicitly by the absence of such additives, 297
the signal of naturalness creates an expectation of purity. While the highly variable and 298
occasionally unconventional sensory profile of minimal intervention wines presents a 299
competing physical trigger for aversion [7], authenticity theory suggests that the overarching 300
expectation of purity should dominate the evaluative framing [23,59]. Therefore, reviews of 301
natural wines are likely to be characterized by a marked and proportional absence of disgust 302
markers compared to conventional wines, where critiques of chemical tastes or artificiality are 303
more common. An alternative possibility, however, arises from the contamination literature in 304
psychological science. Disgust is amplified when a stimulus is perceived to violate a purity 305
frame rather than occurring within a neutral one [70,73]. Because the naturalness designation 306
frames wines as categorically pure, any perceived sensory deviation from this frame may 307
generate a stronger disgust response than an equivalent deviation in conventional wines, where 308
no such purity frame has been established. 309
Finally, the discovery of unique, living products is often associated with the emotions of joy 310
and anticipation. The variability in natural winemaking, often framed as a defect in industrial 311
contexts, is reinterpreted by enthusiasts as a source of excitement and distinctiveness, 312
reinforcing the perceived value of the credence attribute [9]. Therefore, natural wine reviews 313

11

are expected to exhibit a distinct emotional signature characterized by elevated trust and joy, 314
and suppressed disgust. Hence, we predict: 315
H5: Natural wines elicit distinct emotion profiles characterized by higher levels of (a) 316
trust and (b) joy, but (c) lower levels of disgust compared to conventional wines. 317
3. Methodology 318
3.1. Data 319
The dataset consisted of consumer wine reviews sourced from the online wine platform Vivino, 320
a global wine community and marketplace with tens of millions of wines and users 321
(www.vivino.com). The data were collected using a custom Python scraping pipeline that 322
systematically retrieved publicly available information from the Vivino platform, including 323
wine properties, pricing information, and consumer reviews. All data collected were publicly 324
accessible without authentication at the time of extraction. No personal or identifying 325
information beyond pseudonymized user identifiers was retained. Data collection took place 326
between September 4 and October 2, 2025. The reviews in the dataset span the full history of 327
the platform, with a median review year of 2018. 328
Each observation represented a single consumer review and included 24 variables: unique 329
identifiers (wine ID, vintage ID, user ID), review text (tagged_note), consumer quality rating 330
(1–5 scale), wine price (recorded in both local currency and USD), wine characteristics (alcohol 331
by volume [ABV], acidity, body, tannin, sweetness, fizziness, intensity; all measured on 1 –5 332
scales), vintage year, region and country of origin, wine type, and binary indicators for natural 333
wine status and biodynamic certification. Each wine's natural status was taken from Vivino's 334
native ‘is_natural’ attribute, retrieved directly from the platform . Because Vivino does not 335
disclose the criteria underlying this flag, and natural wine lacks a universally accepted 336
definition, the variable reflects Vivino's own platform -level classification. The initial dataset 337
comprised 12,943,638 observations. 338
Prior to analysis, language detection was performed on all review texts using Google's Compact 339
Language Detector 2 for R (cld2) [74] to identify English -language reviews. Reviews with 340
missing or empty text fields were excluded (17.3%). The resulting analytic sample comprised 341
6,750,472 English-language reviews (63.1% of all reviews in the dataset), of which 116,747 342
(1.7%) pertained to natural wines and 6,278,838 (93.0%) to conventional wines. The remaining 343
354,887 reviews (5.3%) contained missing or unclassified values for natural wine status and 344

12

were excluded from subsequent analyses. Descriptive statistics for all quantitative variables in 345
the final sample are presented in Table 1. 346
The analytic sample comprised 697 natural wines and 9,9 17 conventional wines. Despite 347
representing 6.6% of wine labels, natural wines accounted for only 1.7% of total reviews, 348
reflecting their lower review volume per wine relative to conventional counterparts. Natural 349
wines generated a mean of 167 reviews per wine (SD = 571), compared to a mean of 633 350
reviews per wine (SD = 4,413) for conventional wines.  351
3.2. Dependent Measures 352
Rating. Each review included a quality rating assigned by the consumer. This served as the 353
dependent variable for H1. 354
Price. Wine prices were recorded in USD and natural log -transformed to account for right -355
skewed distributions. A constant of 1 was added before transformation as a standard precaution 356
to handle potential zero or near-zero values in the original dataset. Reviews with missing price 357
information were excluded from the analyses related to H2. 358
Review length. The number of words in each review text was computed as an indicator of 359
consumer engagement. This variable served as the dependent variable for H3. 360
Sentiment. Sentiment was assessed using the AFINN lexicon [75] from the tidytext package 361
for R [76], which assigns numeric valence scores ranging from −5 to +5 to words. Review texts 362
were tokenized into individual words, each token was matched against the AFINN lexicon, and 363
the mean sentiment score across all matched tokens within each review was computed. 364
Reviews containing no AFINN -matched words were excluded from H4 analyses to avoid 365
artefactual zero scores. The mean per-word sentiment score was used as the dependent variable 366
for H4. 367
To illustrate, consider the following review excerpt: "This wine is wonderful, vibrant and 368
lively, with an earthy finish that I found disappointing." Following tokenization, the AFINN 369
lexicon matches two words: wonderful (+4) and disappointing (−2), yielding a mean per-word 370
sentiment score of +1.00, indicating mildly positive overall valence. The NRC lexicon 371
additionally classifies wonderful as associated with joy, anticipation, and trust, while 372
disappointing activates sadness and disgust, producing a nuanced emotion profile that captures 373
the mixed evaluative content of the review beyond what the aggregate score alone conveys. 374

13

Emotions. Discrete emotion scores were derived using the NRC Emotion Lexicon [77], which 375
maps English words onto eight basic emotions —joy, trust, anticipation, surprise, anger, 376
disgust, fear, and sadness —as well as two general sentiment categories (positive, negative). 377
For each review, the count of words associated with each emotion category was computed 378
following tokenization and lexicon matching [76]. These emotion counts constituted the 379
dependent variables for H5a-c. 380
3.3. Predictor 381
Natural wine status. Each wine was classified as either natural or conventional based on the 382
binary indicator provided in the dataset. This classification served as the primary predictor 383
across all analyses. 384
3.4. Control Variables 385
Several variables were included as covariates in regression models to account for alternative 386
explanations. These included log-transformed price and quality rating (in all cases where price 387
or quality were not the principal outcome), vintage year, alcohol by volume, and wine sensory 388
characteristics (acidity, body, tannin). For the price model (H2), country of origin was 389
additionally included as a control. 390
3.5. Analytic Approach 391
All analyses were conducted using R [78]. Each hypothesis was tested in two stages. First, 392
independent samples t-tests were conducted to examine differences in each outcome variable 393
between natural and conventional wine reviews. Second, multiple regression models were 394
estimated to examine whether these differences remained unchanged after controlling for 395
relevant covariates. The specific analytic decisions for each hypothesis are described below. 396
H1: Ratings: An independent samples t-test was conducted to compare mean ratings between 397
natural and conventional wine reviews. A multiple linear regression was subsequently 398
estimated with rating as the outcome and natural wine status as the predictor of interest, 399
controlling for log-transformed price, vintage year, ABV, acidity, body, and tannin. 400
H2: Price: An independent samples t-test was conducted on log-transformed prices to compare 401
natural and conventional wines. A multiple linear regression was estimated with log -402
transformed price as the outcome and natural wine status as the predictor of interest, controlling 403
for rating, vintage year, ABV, acidity, body, tannin, and country of origin. The exponentiated 404

14

regression coefficient for natural wine status was used to derive the estimated price premium 405
(i.e., percentage difference) associated with naturalness. 406
H3: Review length: An independent samples t-test was conducted to compare mean review 407
lengths. Given the count -based nature of word count data and the expected overdispersion, a 408
negative binomial regression was estimated with review length as the outcome and natural wine 409
status as the predictor of interest, controlling for rating and log -transformed price. 410
Exponentiated coefficients (incidence rate ratios) were reported to facilitate interpretation. 411
H4: Sentiment: An independent samples t-test was conducted on mean per -word AFINN 412
sentiment scores, restricted to reviews containing at least one sentiment -bearing word. A 413
multiple linear regression was estimated with sentiment score as the outcome and natural wine 414
status as the predictor of interest, controlling for rating and review length. 415
H5a-c: Emotion profiles: Ten independent samples t-tests were conducted to compare emotion 416
word counts between natural and conventional wine reviews across the eight NRC emotions 417
(joy, trust, anticipation, surprise, anger, disgust, fear, sadness) and two general sentiment 418
categories (positive, negative). Effect sizes were reported as percentage change in mean 419
emotion word counts for natural relative to conventional reviews. Significance was assessed at 420
the conventional p < .05 threshold across all comparisons. 421
4. Results 422
4.1. Descriptive Statistics 423
Table 1 presents descriptive statistics for all quantitative variables in the analytic sample. 424
Table 1 425
Descriptive Statistics 426
Variable M SD Median Min Max Skewness Kurtosis
Rating 4.12 0.65 4.00 1.00 5.00 −1.07 2.67
Price (USD) 253.92 3,673.35 51.99 1.16 200,000 53.59 2,910.45
Review length
(words)
19.23 18.64 12.00 1.00 112.00 1.79 3.05
Sentiment (per
word)
1.68 1.39 2.00 −5.00 5.00 −0.56 −0.33
Alcohol by
volume (%)
13.38 2.24 13.50 0.00 19.00 −5.00 27.08
Acidity 3.71 0.79 3.50 1.00 5.00 −0.65 0.21

15

Variable M SD Median Min Max Skewness Kurtosis
Body 3.93 0.84 4.00 1.00 5.00 −0.63 0.02
Tannin 3.85 0.90 4.00 1.00 5.00 −0.72 −0.29
Sweetness 1.15 0.48 1.00 1.00 5.00 5.44 36.79
Fizziness 4.64 0.50 5.00 3.50 5.00 −0.75 −1.22
Intensity 4.03 0.88 4.00 1.00 5.00 −0.83 0.06
Vintage year 2013 14.03 2018 1806 2025 −3.13 20.83
Note. N  = 6,395,585 English -language reviews with valid natural wine classification. M = 427
mean, SD = standard deviation. Sensory characteristics (acidity, body, tannin, sweetness, 428
fizziness, intensity) measured on 1–5 scales. 429
4.2. Hypothesis Tests 430
H1: Ratings 431
An independent samples t-test revealed that natural wines (M = 4.09; SD = 0.58) received lower 432
ratings compared to conventional wines (M = 4.12; SD = 0.65), t(122252) = 14.61, p < .001. A 433
multiple linear regression with price, vintage year, ABV, and sensory characteristics included 434
as control variables confirmed the robustness of this finding, b = −0.02, SE = 0.00, p < .001. 435
As such, H1 did not receive empirical support.  436
H2: Price 437
Supporting H2, another independent samples t-test on log -transformed prices revealed that 438
natural wines were more expensive (Mdn = $55.00) than conventional wines (Mdn = $51.700),  439
t(123980) = −13.12, p < .001. Multiple linear regression controlling for rating, vintage year, 440
ABV, sensory characteristics, and country of origin further supported the robustness of this 441
pattern, b = 0.18, SE = 0.00, p < .001. Exponentiation of the regression coefficient indicated 442
that natural wines were priced approximately 20% higher than conventional wines, holding all 443
covariates constant. 444
H3: Review Length 445
In line with H3, natural wine reviews ( M = 23.0 words, SD = 20.8) were longer than 446
conventional wine reviews (M = 19.2 words, SD = 18.6), t(120235) = −62.96, p < .001. Given 447
the count-based nature of word count data and its evident overdispersion, the robustness of 448
these findings was tested using a negative binomial regression controlling for rating and price. 449
This analysis yielded an incidence rate ratio of 1.20, SE = 0.003, p < .001, indicating that natural 450

16

wine reviews contained approximately 20% more words than conventional wine reviews after 451
controlling for covariates. 452
H4: Sentiment 453
Sentiment analysis was restricted to reviews containing at least one sentiment -bearing word 454
from the AFINN lexicon ( n = 4,879,656). Mean per -word sentiment scores differed 455
significantly between natural (M = 2.05; SD = 1.20) and conventional wine reviews (M = 2.21; 456
SD = 1.18), t(92125) = 38.01, p < .001, indicating that conventional wine reviews contained 457
more positive sentiment than natural wine reviews. Multiple linear regression controlling for 458
rating and review length confirmed this pattern, b = −0.097, SE = 0.00, p < .001. As such, H4 459
was not supported.  460
H5a-c: Emotion Profiles 461
Table 2 presents the results of independent samples t-tests comparing emotion word counts 462
between natural and conventional wine reviews across eight NRC emotion categories and two 463
general sentiment categories. As seen based on these results, H5b was supported, whereas the 464
findings pertaining to H5a and H5c were in the opposite direction to our predictions.  465
Table 2 466
Emotion Word Counts in Natural Versus Conventional Wine Reviews 467
Emotion Type M
Conv.
SD
Conv.
M
Nat.
SD
Nat.
Difference t-value p-value
Joy Positive
Emotion
0.84 1.05 0.86 1.09 +2.5% −6.65 <.001
Trust Positive
Emotion
0.79 1.04 0.80 1.06 +0.6% −1.46 .145
Anticipation Positive
Emotion
0.68 0.95 0.66 0.95 −2.7% 6.54 <.001
Surprise Positive
Emotion
0.43 0.71 0.44 0.73 +1.8% −3.63 <.001
Anger Negative
Emotion
0.14 0.41 0.19 0.48 +31.8% −32.16 <.001
Disgust Negative
Emotion
0.28 0.59 0.39 0.71 +40.0% −53.21 <.001
Fear Negative
Emotion
0.12 0.38 0.16 0.44 +30.4% −28.32 <.001
Sadness Negative
Emotion
0.23 0.53 0.25 0.55 +7.5% −10.72 <.001

17

Emotion Type M
Conv.
SD
Conv.
M
Nat.
SD
Nat.
Difference t-value p-value
Positive General
Sentiment
1.94 2.01 2.06 2.05 +5.8% −18.65 <.001
Negative General
Sentiment
0.45 0.79 0.59 0.92 +31.3% −51.68 <.001
Note. Values represent mean emotion word counts per review. Percentage change calculated 468
as [(Natural − Conventional) / Conventional] × 100. 469
 470
Figure 1 471
Emotion Word Count Differences Between Natural and Conventional Wine Reviews 472
 473
     5. Discussion 474
Drawing on literature about the naturalness bias and essentialist beliefs about authenticity, the 475
current research compared consumer online reviews of natural and conventional wines using a 476
large-scale dataset of wine reviews to examine the evaluative and affective consequences of 477
naturalness. Contrary to predictions, natural wines received slightly lower quality ratings than 478
conventional wines (H1 not supported), though they commanded a substantial 20% price 479
premium after controlling for quality and wine characteristics (H2 supported). Moreover, 480
natural wine reviews were approximately 20% longer than conventional wine reviews (H3 481
supported), suggesting heightened engagement. However, sentiment analysis revealed that 482

18

natural wine reviews yielded a lower per-word sentiment score than conventional wine reviews 483
(H4 not supported). Most strikingly, emotion profiling demonstrated that natural wines elicited 484
significantly more negative emotions, including anger, disgust, sadness, and fear, alongside 485
modest increases in the positive emotions of joy and surprise (leaving H5a and H5c 486
unsupported for trust and disgust, respectively, while supporting H5b for joy).  487
Taken together, the fact that consumers pay a substantial premium and engage deeply with a 488
product, yet evaluate it with lower ratings, lower sentiment, and elevated disgust, indicates that 489
the appeal of a credence attribute does not seamlessly translate into hedonic satisfaction.  490
5.1. Theoretical Implications 491
The present findings advance the theoretical understanding of quality signaling and credence 492
attributes within digital market environments. The findings converge with a two-stage process 493
in which naturalness operates differently before and after consumption. At the point of 494
purchase, the naturalness designation functions as a credence signal of procedural integrity, 495
and consumers pay a premium for it , as manifested through our documented price effect. The 496
same signal also raises expectations of quality and purity. Minimal -intervention winemaking, 497
however, carries documented sensory heterogeneity (higher volatile acidity, turbidity, and 498
unconventional flavor profiles) that frequently departs from those expectations. The resulting 499
gap between these expectations and the wine that is experienced yields lower post-consumption 500
ratings, less favorable sentiment, and more polarized  emotion profiles, including elevated 501
disgust. As such, the price premium and the ratings penalty can be seen as two complementary 502
stages of the same process rather than as competing outcomes. Naturalness elevates valuation 503
ex ante through the credence signal and depresses evaluation ex post through expectation 504
disconfirmation, which accounts for the joint pattern of higher prices alongside lower ratings 505
and weaker sentiment . Notably, the results reported herein highlight clear constraints on 506
generality in the pervasive natural-is-better bias [1,49]. By integrating authenticity theory with 507
applied wine economics, this study demonstrates that the appeal of a credence attribute does 508
not uniformly translate into hedonic satisfaction. Specifically, the higher prevalence of discrete 509
negative emotions, such as the high-arousal states of disgust, anger, and fear, suggests that the 510
sensory reality of minimal-intervention products frequently violates the cognitive prototype of 511
purity held by consumers [6,31]. Because natural wine is defined by the explicit rejection of 512
standardized chemical stabilization [9], its highly variable and occasionally unconventional 513
gustatory profile might trigger evolved defensive psychological mechanisms, which manifest 514
as moralized aversion or disgust in consumer evaluations [8,71,79]. A plausible interpretation 515

19

of this pattern is that the purity frame established by the naturalness designation may heighten 516
consumer sensitivity to any sensory feature perceived as atypical. This is consistent with wine 517
research showing that natural wines exhibit significantly higher sensory variability, volatile 518
acidity, and turbidity than conventional wines, producing a broader range of features that can 519
occur as deviations from the expected profile [80]. Therefore, minor deviations that would pass 520
unnoticed in a conventional wine may be processed as contamination signals, which in turn 521
may amplify disgust responses [70,73]. 522
The paradox of diminished ratings alongside a substantial price premium can be explained 523
through the lens of information asymmetry and signaling theory [3]. Because natural wine 524
functions as a credence good whose defining attributes cannot be verified prior to, or even after, 525
consumption [81], consumers rely on the natural designation as a quality signal to mitigate the 526
risk inherent in such purchases [10]. Beyond this signaling function, the designation also places 527
weight on the producer's process history and commitment to minimal intervention, which 528
consumers reward financially as an expression of authenticity, independent of sensory 529
performance [55]. This corroborates authenticity theory by demonstrating that consumers 530
assign significant financial value to a product’s process history and perceived integrity, 531
irrespective of its functional performance [55]. Consumers reward quality signal prior to 532
purchase, resulting in the observed premium. However, this premium sets elevated pre -533
consumption expectations. When the physical product yields an unfamiliar sensory profile, a 534
pronounced disconfirmation occurs of those pre -consumption expectations, leading to lower 535
post-consumption ratings and elevated disgust. Consequently, naturalness functions as a high 536
value credence signal of procedural integrity rather than a reliable heuristic for gustatory 537
excellence.  538
The economic structure of the price premium is further illuminated by a systematic 539
decomposition of the focal coefficient (Table A12). Sequentially adding blocks of controls 540
reveals that the bare -model premium (≈ 4%) is suppressed by the lower sensory intensity of 541
natural wines; once sensory characteristics are introduced, the coefficient grows to 542
approximately 42% (β = 0.35), with body, tannin, and intensity acting as the principal 543
suppressors. Adding biodynamic certification leaves the coefficient effectively unchanged, and 544
a formal Sobel test confirms that biodynamic operates as a statistically valid but quantitatively 545
modest mediator (1.7% of the total effect). Including country of origin attenuates the premium 546
to approximately 27% (β = 0.24), consistent with the concentration of minimal -intervention 547
production in regions where overall price levels are above average. Importantly, 548

20

multicollinearity diagnostics rule out the alternative explanation that these patterns reflect 549
spurious specification sensitivity: all variance inflation factors are below 5, and the natural -550
wine indicator carries pairwise correlations no greater than |.15| with any other covariate. Thus, 551
the natural-wine premium reflects an independent economic signal: it cannot be reduced to the 552
co-occurrence of biodynamic practice, to compositional differences in country of origin, or to 553
multicollinearity among the sensory controls. 554
Finally, the findings advance the understanding of consumer engagement in digital 555
environments by demonstrating that perceived naturalness operates as a powerful amplifier of 556
elaboration. The significantly longer reviews associated with natural wines align with the 557
premise that authentic offerings fulfill a consumer drive for meaning, thereby prompting 558
extensive narrative storytelling [62,68]. The dual increase in certain positive emotions, such as 559
joy and surprise, alongside elevated negative emotions reflects a highly arousing and complex 560
consumption experience. Consumers utilize expanded linguistic effort to articulate the 561
variability and distinctiveness of these products [61,63], suggesting that disconfirmed 562
expectations drive electronic word-of-mouth through elaborate discursive reconciliation rather 563
than through straightforward satisfaction [82]. 564
5.2. Managerial Implications 565
The findings of this study offer strategic advice for marketing practitioners and wine producers 566
operating within the minimal intervention segment. Primarily, the discrepancy between quality 567
ratings and willingness to pay necessitates a shift in pricing and positioning strategies. Because 568
consumers demonstrate a willingness to accept a substantial price premium for natural wines 569
despite rating them as lower in quality, managers should avoid comparative advertising 570
strategies with conventional wines on traditional quality-to-price heuristics. As consumers are 571
financially rewarding the naturalness signal rather than the sensory outcome, marketing 572
communications should emphasize the symbolic value, process history, and inherent rarity of 573
the natural wine product, positioning naturalness as a premium credence attribute. By 574
anchoring the value proposition in authenticity and environmental stewardship, brands can 575
sustain premium pricing models independent of conventional sensory characteristics [55,58] 576
by successfully mitigating information asymmetry prior to purchase. 577
Further, the pronounced elevation of negative discrete emotions, such as disgust and anger, 578
together with diminished overall sentiment highlights a salient shortcoming in current 579
marketing practices. These negative affective responses likely originate from a fundamental 580

21

expectation violation driven by the strength of the quality signal. Consumers inherently 581
associate the term natural with purity and flawlessness [51], yet minimal intervention 582
winemaking frequently yields products with atypical, highly variable, and unconventional 583
sensory profiles. To mitigate this expectation disconfirmation, managers might need to 584
consider proactive educational campaigns prior to new product launches. For example, 585
practitioners can explicitly reframe potential sensory deviations (such as cloudiness or volatile 586
acidity) not as technical defects but as authentic signatures of a living terroir. Anticipated 587
outcomes of this proactive expectation management include the alignment of the sensory 588
reality with the cognitive prototype of the consumer, which is expected to attenuate disgust 589
responses and support post-purchase satisfaction [31,52]. 590
Finally, the observation that natural wines elicit significantly longer reviews and more 591
emotional arousal indicates a consumer base characterized by deep psychological involvement 592
and high cognitive effort. While the affective valence may be polarized, the sheer volume of 593
engagement presents a strategic asset. Managers should actively facilitate brand community 594
building online and encourage narrative storytelling within their lucrative segments as doing 595
so should theoretically create synergy effects on outcomes such as brand loyalty and electronic 596
word-of-mouth [62]. By providing platforms for consumers to articulate their complex 597
consumption experiences, brands can transform polarizing sensory encounters into a highly 598
engaging, community -driven acquisition tool [61,62]. Community strategies should 599
nonetheless be designed to accommodate the full range of consumer voices rather than only 600
the highly involved consumers, recognizing that the same elaborative engagement that 601
produces advocacy also produces detailed criticism [82]. 602
6. Limitations and Future Research 603
The current study has certain limitations, which might act as fruitful avenues for future 604
research. First, it should be noted that Vivino users do not constitute a representative sample 605
of general wine consumers. As an engaged online wine community, Vivino attracts users with 606
above-average wine involvement, including hobbyists, enthusiasts, and semi -experts who 607
actively seek out, evaluate, and document their wine experiences [26,27]. This self -selection 608
bias means that the evaluative and affective responses captured in this dataset likely reflect a 609
more knowledgeable and involved consumer segment than the broader wine -buying 610
population. 611

22

Second, the dataset is restricted exclusively to English -language reviews, which potentially 612
limits the generalizability of the findings across different geographic markets. Because food 613
and beverage preferences are deeply embedded within specific traditions, background 614
significantly shape consumer evaluations of sustainable and natural products [ 69,83]. Future 615
studies should adopt cross -cultural methodologies to examine whether the observed 616
expectation violation and negative emotional arousal associated with natural wines persist 617
across non-English languages. This is particularly important given that many of the world’s 618
most renowned producers of natural wines are based on countries where English is not the first 619
language, such as France, Spain, and Germany, with these countries also having a strong wine 620
culture among their consumers.   621
Third, reliance on lexicon-based sentiment and emotion analysis presents structural limitations. 622
While tools like the AFINN and NRC lexicons offer high scalability for large datasets, they 623
process words in isolation and frequently fail to capture complex linguistic nuances, including 624
sarcasm, contextual negation, and domain-specific terminology. To enhance construct validity, 625
future research should transition toward advanced computational linguistics. Specifically, the 626
application of transformer-based architecture allows for the processing of bidirectional context 627
and semantic relationships, yielding more accurate sentiment classifications in unstructured 628
texts [84]. 629
Fourth, another methodological concern pertains to the length dependency of raw emotion 630
word counts derived from the NRC lexicon. Because natural wine reviews are significantly 631
longer than conventional wine reviews (H3), they will mechanically yield a greater absolute 632
number of matched emotion words across all categories, independent of any genuine difference 633
in emotional content. It is important to note that the AFINN -based sentiment measure 634
employed in H4 is unaffected by this issue, as it is computed as a mean per -word score and is 635
therefore length-normalized by design. However, the NRC -based emotion counts used in H5 636
are raw totals and may consequently overstate the magnitude of observed differences. Future 637
research should address this by operationalizing emotion as a proportion of matched emotion 638
words relative to total review length, which would yield length -normalized rates directly 639
comparable across reviews of varying length. Alternatively, including review length as a 640
covariate in regression-based analyses of emotion would partially mitigate the confound. 641
Additionally, the observational design inherent to crowdsourced online reviews prohibits 642
explicit claims of causality. While the current data imply that the higher prevalence of negative 643
emotions might stem from sensory expectation disconfirmation, this mechanism remains 644

23

tentative at present. Future research should use controlled experimental designs that manipulate 645
both the pre -consumption product framing and the objective sensory profile of natural and 646
conventional wines. Such experimental isolation is necessary to explicitly map the causal 647
pathways of the expectancy disconfirmation process within the minimal intervention segment, 648
thereby confirming how metaphysical claims interact with physical gustatory experiences to 649
shape consumers’ emotions, cognitions, and ultimately their purchase decisions [7,85,86]. 650
An important alternative economic interpretation of the present findings warrants 651
consideration. The coexistence of lower ratings and higher prices may not reflect expectation 652
disconfirmation among natural wine believers, but rather a structural consequence of market 653
segmentation and channel separation. Natural wine is predominantly purchased through 654
specialist channels (natural wine bars, dedicated importers, and specialist retailers) by a 655
committed consumer segment whose evaluative criteria and sensory preferences are calibrated 656
to the minimal-intervention aesthetic [44]. If this core consumer segment is underrepresented 657
among Vivino users, then the lower ratings observed in this study may reflect not expectation 658
disconfirmation but a simpler consumer-product mismatch, with natural wine being evaluated 659
by consumers whose palate preferences and quality criteria are calibrated to conventional wine 660
production standards. The price premium would then reflect valuations set by the specialist 661
natural wine market rather than by the Vivino user base and the rating penalty would reflect 662
responses by conventional consumers encountering an unfamiliar sensory profile. However, 663
this interpretation conflicts with the sentiment and emotion findings reported herein. The 664
polarized affective signature observed (simultaneously elevated disgust and joy, combined 665
with substantially longer reviews) is difficult to attribute to disengaged conventional 666
consumers who simply dislike unfamiliar products. If anything, such consumers should 667
generate shorter, more uniformly negative reviews rather than longer and more emotionally 668
complex ones, as documented here. This suggests that the Vivino natural wine reviewer 669
population is heterogeneous, likely comprising both committed natural wine enthusiasts and 670
conventional consumers. The present observational design cannot explicitly distinguish 671
between these interpretations, as the platform does not allow identification of reviewers' prior 672
wine category preferences or purchasing channels. Future research should, therefore, examine 673
the profile of natural wine reviewers on digital platforms to determine the relative contribution 674
of each interpretation to the evaluative and affective patterns documented in the current 675
research. 676

24

Further, whether wine was classified as natural or not was based on Vivino's platform -level 677
designation. We acknowledge that, in the absence of a universally accepted definition of natural 678
wine, this classification reflects platform-specific criteria rather than a regulated standard. By 679
treating natural as a binary indicator derived from the platform’s classification, our analysis 680
collapses considerable within-category heterogeneity (in sulphite use, yeast practice, farming, 681
and cellar intervention) and carries a degree of producer self-selection, as producers cultivating 682
a natural-wine identity may be more likely to disclose it at registration than those who practice 683
minimal intervention without marketing it as such. The population is also conditioned on 684
Vivino's catalogue and may not overlap with wines classified as natural on specialist platforms, 685
sommelier-curated lists, or under voluntary industry charters. Our findings should therefore be 686
read as evidence of how the  platform’s user base evaluates wines that it classifies as natural, 687
rather than as claims about natural wine as a universal category. 688
A further limitation concerns the structure of the Vivino dataset. With approximately 6.7 689
million reviews distributed across over 10,000 unique wines, the review-per-wine distribution 690
is highly skewed, with some wines contributing numerous reviews and others only a handful. 691
This implies non -independence of observations within wines, as reviews of the same wine 692
share unobserved wine -level characteristics. We acknowledge this clustering structure as a 693
methodological caveat to bear in mind when interpreting the precision of our obtained results.   694

25

References 695
[1] S.E. Scott, P. Rozin, D.A. Small, Consumers prefer "natural" more for preventatives than 696
for curatives, J. Consum. Res. 47 (2020) 454–471. https://doi.org/10.1093/jcr/ucaa034 697
[2] S. Hemmerling, M. Canavari, A. Spiller, Preference for naturalness of European organic 698
consumers: First evidence of an attitude-liking gap, Br. Food J. 118 (2016) 2287–2307. 699
https://doi.org/10.1108/BFJ-11-2015-0457 700
[3] C. Aqueveque, P. Rodrigo, "This wine is dead!": Unravelling the effect of word -of-mouth 701
and its moderators in price-based wine quality perceptions, Br. Food J. 123 (2021) 869–702
883  https://doi.org/10.1108/BFJ-03-2020-0252 703
[4] A. Maehara, 100% all natural ambiguity: A comparative approach to food labeling 704
requirements for the term "natural" by the FDA and the EU, Wash. U. Global Stud. L. 705
Rev. 18 (2019) 263. https://openscholarship.wustl.edu/law_globalstudies/vol18/iss1/10 706
[5] M.B. Beverland, Crafting brand authenticity: The case of luxury wines, J. Manag. Stud. 42 707
(2005) 1003–1029. https://doi.org/10.1111/j.1467-6486.2005.00530.x 708
[6] S. Gonzalez Coffin, W. Eichhorst, A.R. Carrico, Y. Inbar, P. Newton, L. Van Boven, 709
Perceived naturalness predicts public support for sustainable protein technology, Clim. 710
Change 177 (2024) 29. https://doi.org/10.1007/s10584-024-03679-5 711
[7] M. Dubois, M. Folwarczny, J. Cao, Þ. Bender, Digital transformation of wine opinion: From 712
critics to peer reviews analysis, in: M. Visalli, M.V. Galmarini (Eds.), Collection and 713
Analysis of Text Data in Sensory and Consumer Science, Springer, Cham, 2026. 714
https://doi.org/10.1007/978-3-032-04851-6_9 715
[8] P. Rozin, The meaning of "natural": Process more important than content, Psychol. Sci. 16 716
(2005) 652–658. https://doi.org/10.1111/j.1467-9280.2005.01589.x 717
[9] P. Alonso González, E. Parga-Dans, Natural wine: Do consumers know what it is, and how 718
natural it really is? J. Clean. Prod. 251 (2020) 119635.  719
https://doi.org/10.1016/j.jclepro.2019.119635 720
[10] A. Stöckl, S. Tischler, D.F. Kleiss, K. Moser, Grapes and gains: the influence of farming 721
methods on Austrian wine ratings and prices, J. Wine Res. 35 (2024) 208 –217. 722
https://doi.org/10.1080/09571264.2024.2394036 723
[11] C. Mazzocchi, G. Ruggeri, S. Corsi, Consumers’ preferences for biodiversity in vineyards: 724
A choice experiment on wine, Wine Econ. Policy 8 (2019) 155 –164. 725
https://doi.org/10.36253/wep-7482 726
[12] P. Fanasch, B. Frick, The value of signals: do self -declaration and certification generate 727
price premiums for organic and biodynamic wines? J. Clean. Prod. 249 (2020) 119415. 728
https://doi.org/10.1016/j.jclepro.2019.119415 729
[13] A. Corsi, S. Strøm, The price premium for organic wines: estimating a hedonic farm-gate 730
price equation, J. Wine Econ. 8 (2013) 29–48. https://doi.org/10.1017/jwe.2013.4 731
[14] R. Vecchio, C. Annunziata, A. Lerro, E. Parga -Dans, P. Alonso González, Drivers of 732
consumer willingness to pay for sustainable wines: natural, biodynamic, and organic, 733
Org. Agric. 13 (2023) 177–190. https://doi.org/10.1007/s13165-023-00425-6 734
[15] G. Scozzafava, C. Casini, F. Boncinelli, L. Marinelli, A. Contini, How much is a bottle of 735
conventional, organic or biodynamic wine worth? Results of an experimental auction, 736
Food Qual. Prefer. 93 (2021) 104259. https://doi.org/10.1016/j.foodqual.2021.104259 737
[16] E. Parga -Dans, R. Vecchio, A. Annunziata, P. Alonso González, R. Otero Enríquez, A 738
certification for natural wine? A comparative analysis of consumer drivers in Italy and 739
Spain, Wine Econ. Policy 12 (2023) 23–35. https://doi.org/10.36253/wep-12890 740
[17] C. Bazzani, G. Maesano, D. Begalli, R. Capitello, Exploring the effect of naturalness on 741
consumer wine choices: evidence from a survey in Italy, Food Qual. Prefer. 113 (2024) 742
105062. https://doi.org/10.1016/j.foodqual.2023.105062 743

26

[18] R.E. White, The value of soil knowledge in understanding wine terroir, Front. Environ. 744
Sci. 8 (2020) 12. https://doi.org/10.3389/fenvs.2020.00012 745
[19] J. Bruwer, I. Lesschaeve, B.L. Campbell, Consumption dynamics and demographics of 746
Canadian wine consumers: Retailing insights from the tasting room channel, J. Retail. 747
Consum. Serv. 19 (2012) 45–58. https://doi.org/10.1016/j.jretconser.2011.08.008 748
[20] J.G. Lynch Jr, D. Ariely, Wine online: Search costs affect competition on price, quality, 749
and distribution, Mark. Sci. 19 (2000) 83–103.  750
https://doi.org/10.1287/mksc.19.1.83.15183 751
[21] T. Meas, W. Hu, M.T. Batte, T.A. Woods, S. Ernst, Substitutes or complements? 752
Consumer preference for local and organic food attributes, Am. J. Agric. Econ. 97 753
(2015) 1044–1071. 754
[22] M. Folwarczny, A. Gasiorowska, V. Sigurdsson, T. Otterbring, Renewable bites: How 755
energy sources shape food healthiness judgments, Judgm. Decis. Mak. 20 (2025) e35. 756
https://doi.org/10.1017/jdm.2025.10012 757
[23] G.E. Newman, An essentialist account of authenticity, J. Cogn. Cult. 16 (2016) 294–321. 758
https://doi.org/10.1163/15685373-12342181 759
[24] G.I. Penagos -Londoño, F. Ruiz -Moreno, R. Sellers -Rubio, S. Del Barrio -García, A.B. 760
Casado-Díaz, Consistency of expert product reviews: an application to wine guides, 761
Wine Econ. Policy 11 (2022) 51–60. https://doi.org/10.36253/wep-12400 762
[25] E. Calderón -Monge, V. Ripollés-Matallana, B. Baruque -Zanón, S. Porras Alfonso, Big 763
data analysis of Spanish wine consumers reviews, Int. J. Wine Bus. Res. 37 (2025) 55–764
86. https://doi.org/10.1108/IJWBR-12-2023-0084 765
[26] G. Gastaldello, I. Schäufele -Elbers, G. Schamel, Factors influencing wine ratings in an 766
online wine community: the case of Trentino–Alto Adige, J. Wine Econ. 19 (2024) 19–767
40. https://doi.org/10.1017/jwe.2024.2 768
[27] X. Qi, W. Chang, A. Liu, J. Sun, M. Fan, Exploring the influence of emotionality and 769
expertise on online wine reviews: does greater knowledge lead to less review? Int. J. 770
Contemp. Hosp. Manag. 36 (2024) 2842 –2869. https://doi.org/10.1108/IJCHM -08-771
2023-1302 772
[28] R. Janssen, M.K. Ribar, Expertise, accuracy, and reputation inflation in the wine market: 773
evidence from Vivino ratings, J. Wine Econ. 20 (2025) 348 –370. 774
https://doi.org/10.1017/jwe.2025.10090 775
[29] C. Rocuant Fuentes, P. Rita, N. Antonio, Assessing the nexus of label content and 776
consumer reviews: insights from premium wines on Vivino, Int. J. Wine Bus. Res. 37 777
(2025) 403–424. https://doi.org/10.1108/IJWBR-08-2024-0044 778
[30] H. Odendaal, E. Kerby, Plebs to pros: a data-driven dive into 60 million wine reviews, Int. 779
J. Wine Bus. Res. (2026) ahead-of-print. https://doi.org/10.1108/IJWBR-06-2025-0039 780
[31] B. Braut, M.A. Paissoni, B. Cavalletti, et al., Naturally biased? Experimental evidence on 781
how the term natural influences wine consumers' perceptions and preferences, J. Behav. 782
Exp. Econ. 121 (2026) 102527. https://doi.org/10.1016/j.socec.2026.102527 783
[32] P.N. Golder, M.G. Dekimpe, J.T. An, H.J. Van Heerde, D.S. Kim, J.W. Alba, Learning 784
from data: An empirics -first approach to relevant knowledge generation, J. Mark. 87 785
(2023) 319–336. https://doi.org/10.1177/00222429221129200 786
[33] W.D. Hoyer, E.W. Wan, K. Wilcox, Practical relevance in consumer research, J. Consum. 787
Res. 51 (2024) 428–438. https://doi.org/10.1093/jcr/ucae023 788
[34] T. Otterbring, G. Viglia, L. Grazzini, G. Das, Guest editorial: Favoring fieldwork makes 789
marketing more meaningful, Eur. J. Mark. 57 (2023) 1793 –1803. 790
https://doi.org/10.1108/EJM-07-2023-987 791

27

[35] H.J. Van Heerde, C. Moorman, C.P. Moreau, R.W. Palmatier, Reality check: Infusing 792
ecological value into academic marketing research, J. Mark. 85 (2021) 1 –13. 793
https://doi.org/10.1177/0022242921992383 794
[36] G.E. Newman, R. Dhar, Authenticity is contagious: Brand essence and the original source 795
of production, J. Mark. Res. 51 (2014) 371–386. https://doi.org/10.1509/jmr.11.0022 796
[37] J.H. Gilmore, B.J. Pine, Authenticity: What Consumers Really Want, Harvard Business 797
Press, Boston, 2007. 798
[38] M.B. Beverland, F.J. Farrelly, The quest for authenticity in consumption: Consumers' 799
purposive choices of authentic cues to shape experiences outcomes, J. Consum. Res. 36 800
(2010) 838–856. http://doi.org/10.1086/615047 801
[39] F. Morhart, L. Malär, A. Guèvremont, F. Girardin, B. Grohmann, Brand authenticity: An 802
integrative framework and measurement scale, J. Consum. Psychol. 25 (2015) 200 –803
218. https://doi.org/10.1016/j.jcps.2014.11.006 804
[40] S.A. Gelman, The Essential Child: Origins of Essentialism in Everyday Thought, Oxford 805
University Press, Oxford, 2003.  806
https://doi.org/10.1093/acprof:oso/9780195154061.001.0001 807
[41] R. Henkin, D. Perez, T. Otterbring, Phygital luxury: The influence of NFT -linked digital 808
twins on consumer responses to physical luxury products, J. Assoc. Consum. Res. 10 809
(2025) 165–179. https://doi.org/10.1086/734844 810
[42] E. Le Grand, On the authenticity of natural wine, in: M. Visalli, M.V. Galmarini (Eds.), 811
What Do Natural Wines Evoke in the Minds and Senses of Wine Drinkers?, Springer, 812
Cham, 2025, pp. 67–84. https://doi.org/10.1007/978-3-031-87857-2_5 813
[43] D. Burnham, O.M. Skilleas, The Aesthetics of Wine, Wiley-Blackwell, Oxford, 2012. 814
[44] R. Goldstein, M. Dubois, Don’t Call It Organic or Biodynamic: Natural Wine, Product 815
Certifications, and Alternative Signalling Mechanisms. In: Uncorked: Negotiating 816
science and belief in the natural wine movement. Cham: Springer Nature Switzerland, 817
99–113.  818
[45] H. Shoenberger, E. Kim, Explaining purchase intent via expressed reasons to follow an 819
influencer, perceived homophily, and perceived authenticity, I. J. Advert. 42 (2023) 820
368–383. https://doi.org/10.1080/02650487.2022.2075636 821
[46] P. Rozin, J. Haidt, C.R. McCauley, Disgust, in: M. Lewis, J.M. Haviland -Jones (Eds.), 822
Handbook of Emotions, 2nd ed., Guilford Press, New York, 2008, pp. 757–776. 823
[47] A. Galati, G. Schifani, M. Crescimanno, G. Migliore, “Natural wine” consumers and 824
interest in label information: An analysis of willingness to pay in a new Italian wine 825
market segment, J. Clean. Prod. 227 (2019) 405 –413. 826
https://doi.org/10.1016/j.jclepro.2019.04.219 827
[48] M.P. Sáenz-Navajas, C. Alemán-Jimeno, P. Nieto, Natural versus conventional production 828
of Spanish white wines: an exploratory study, J. Sci. Food Agric. 103 (2023) 7037 –829
7047. https://doi.org/10.1002/jsfa.12479 830
[49] B.P. Meier, A.J. Dillard, C.M. Lappas, Naturally better? A review of the natural-is-better 831
bias, Soc. Personal. Psychol. Compass 13 (2019) e12494. 832
https://doi.org/10.1111/spc3.12494 833
[50] B. Kovács, G.R. Carroll, D.W. Lehman, Authenticity and consumer value ratings: 834
Empirical tests from the restaurant domain, Organ. Sci. 25 (2014) 458 –478. 835
https://doi.org/10.1287/orsc.2013.0843 836
[51] L. Gagliardi, Naturalness seeking minds: The cognitive foundations of naturalness bias in 837
consumer food choice, Food Hum. 5 (2025) 100716. 838
https://doi.org/10.1016/j.foohum.2025.100716 839

28

[52] B.K. Cheon, Y.F. Tan, G.G. Forde, Food essentialism: Implications for expectations and 840
perceptions of the properties of processed foods, Food Qual. Prefer. 117 (2024) 105173. 841
https://doi.org/10.1016/j.foodqual.2024.105173 842
[53] M. Folwarczny, T. Otterbring, V. Sigurdsson, L.K. Tan, Naturally green, irrationally lean: 843
How background scenery affects calorie judgments, Food Res. Int. 164 (2023) 112339. 844
https://doi.org/10.1016/j.foodres.2022.112339 845
[54] O. Petit, T. Otterbring, The impact of fusion metaphors in health appeals on consumer 846
attitudes: Tasty but unhealthy, healthy but not tasty —duality considerations in health 847
messaging, J. Advert. Res. 64 (2024) 4–17. https://doi.org/10.2501/JAR-2024-005 848
[55] M. Fatma, I. Khan, Brand authenticity and consumers' willingness to pay a premium price: 849
The mediating role of brand identification, J. Brand Manag. 31 (2024) 469 –481. 850
https://doi.org/10.1057/s41262-024-00353-0 851
[56] J. Núñez, D. Martín -Barroso, J.A. Núñez -Serrano, F.J. Velázquez, How much are we 852
willing to pay for quality wine? A meta-analysis and meta-regression analysis, J. Econ. 853
Surv. 39 (2025) 1595–1629. https://doi.org/10.1111/joes.12668 854
[57] F. Völckner, J. Hofmann, The price-perceived quality relationship: A meta-analytic review 855
and assessment of its determinants, Mark. Lett. 18 (2007) 181 –196. 856
https://doi.org/10.1007/s11002-007-9013-2 857
[58] X. Wang, B. Sung, I. Phau, Examining the influences of perceived exclusivity and 858
perceived rarity on consumers' perception of luxury, J. Fash. Mark. Manag. 26 (2022) 859
365–382. https://doi.org/10.1108/JFMM-12-2020-0254 860
[59] J.G. Moulard, et al., Disentangling the meanings of brand authenticity: The entity-referent 861
correspondence framework of authenticity, J. of the Acad. Mark. Sci. 49 (2021) 96 –862
118. https://doi.org/10.1007/s11747-020-00735-1 863
[60] G. Negro, M.T. Hannan, H. Rao, Category reinterpretation and defection: Modernism and 864
tradition in Italian winemaking, Organ. Sci. 22 (2011) 1449 –1463. 865
https://doi.org/10.1287/orsc.1100.0619 866
[61] A. Kalogeraki, S. Kuester, S. von Janda, Leveraging member -initiated online 867
communities: The role of brand prominence, content authenticity and social capital, 868
Eur. J. Mark. 60 (2026) 1–26. https://doi.org/10.1108/EJM-05-2024-0394 869
[62] B. Schivinski, Eliciting brand -related social media engagement: A conditional inference 870
tree framework, J. Bus. Res. 130 (2021) 594–602.  871
https://doi.org/10.1016/j.jbusres.2019.08.045 872
[63] V. Santos, A. Dias, P. Ramos, A. Madeira, B. Sousa, The influence of wine storytelling 873
on the global wine tourism experience, Wine Econ. Policy 11 (2022) 3 –13. 874
https://doi.org/10.36253/wep-11454 875
[64] N. Depetris Chauvin, D. Valentin, J.H. Behrens, H. Rodrigues, Country -of-origin as bias 876
inducer in experts' wine judgments: A sensory experiment in a world wine fair, Int. J. 877
Gastron. Food Sci. 35 (2024) 100883. https://doi.org/10.1016/j.ijgfs.2024.100883 878
[65] A. Tezer, H.O. Bodur, The green consumption effect: How using green products improves 879
consumption experience, J. Consum. Res. 47 (2020) 25 –39. 880
https://doi.org/10.1093/jcr/ucz045 881
[66] S. Kavvadias, B. Schivinski, N. Arachchilage, T. Brown, V. Stavropoulos, Language of 882
change in online narratives of recovery from disordered gaming, Sci. Rep. (2026). 883
https://doi.org/10.1038/s41598-025-33991-8 884
[67] F. Septianto, J. Kemper, G. Northey, Thanks, but no thanks: The influence of gratitude on 885
consumer awareness of food waste, J. Clean. Prod. 258 (2020) 120591. 886
https://doi.org/10.1016/j.jclepro.2020.120591 887
[68] J.C. Nunes, A. Ordanini, G. Giambastiani, The concept of authenticity: What it means to 888
consumers, J. Mark. 85 (2021) 1–20. https://doi.org/10.1177/0022242921997081 889

29

[69] C. Gómez-Corona, T. Otterbring, Underrepresented populations in sensory and consumer 890
science, Food Qual. Prefer. 127 (2025) 105455. 891
https://doi.org/10.1016/j.foodqual.2025.105455 892
[70] C.A. Hutcherson, J.J. Gross, The moral emotions: A social–functionalist account of anger, 893
disgust, and contempt, J. Pers. Soc. Psychol. 100 (2011) 719 –737. 894
https://doi.org/10.1037/a0022408 895
[71] Y. Zhong, L. Wu, X. Chen, Z. Huang, W. Hu, Effects of food -additive-information on 896
consumers' willingness to accept food with additives, Int. J. Environ. Res. Public Health 897
15 (2018) 2394. https://doi.org/10.3390/ijerph15112394 898
[72] P. Rozin, M. Spranca, Z. Krieger, R. Neuhaus, D. Surillo, A. Swerdlin, K. Wood, 899
Preference for natural: Instrumental and ideational/moral motivations, and the contrast 900
between foods and medicines, Appetite 43 (2004) 147 –154. 901
https://doi.org/10.1016/j.appet.2004.03.005 902
[73] P. Rozin, C. Nemeroff, Sympathetic magical thinking: The contagion and similarity 903
"heuristics", in: T. Gilovich, D. Griffin, D. Kahneman (Eds.), Heuristics and Biases: 904
The Psychology of Intuitive Judgment, Cambridge University Press, Cambridge, 2002, 905
pp. 201–216. 906
[74] J. Ooms, cld2: Google's Compact Language Detector 2 [R package], 2025. 907
https://docs.ropensci.org/cld2/ 908
[75] F.Å. Nielsen, AFINN, 2011. https://github.com/fnielsen/afinn 909
[76] J. Silge, D. Robinson, tidytext: Text mining and analysis using tidy data principles in R, 910
J. Open Source Softw. 1 (2016) 37. https://doi.org/10.21105/joss.00037 911
[77] S.M. Mohammad, P.D. Turney, Crowdsourcing a word –emotion association lexicon, 912
Comput. Intell. 29 (2013) 436–465. https://doi.org/10.1111/j.1467-8640.2012.00460.x 913
[78] R Core Team, R: A Language and Environment for Statistical Computing, R Foundation 914
for Statistical Computing, Vienna, 2025. https://www.R-project.org/ 915
[79] M. Siegrist, C. Hartmann, Consumer acceptance of novel food technologies, Nat. Food 1 916
(2020) 343–350. https://doi.org/10.1038/s43016-020-0094-x 917
[80] J. Ballester, M. Belascoin, M. González-Hernández, E. Parga-Dans, P. Alonso González, 918
M.P. Sáenz-Navajas, Sensory attributes and quality perception of red natural wines: a 919
comparative study in Spain and France, OENO One 58 (2024). 920
https://doi.org/10.20870/oeno-one.2024.58.1.7737 921
[81] D. Moscovici, J. Gow, A. Alonso Ugaglia, R. Rezwanul, L. Valenzuela, R. Mihailescu, 922
Consumer preferences for organic wine – global analysis of people and place, J. Clean. 923
Prod. 368 (2022) 133215. https://doi.org/10.1016/j.jclepro.2022.133215 924
[82] D. Langaro, S. Loureiro, B. Schivinski, H. Neves, An investigation of social network users 925
engaging with eWOM: the role of social comparison and envy, J. Mark. Commun. 28 926
(2022) 301–317. https://doi.org/10.1080/13527266.2022.2109056 927
[83] J.P. Enriquez, J.C. Archila -Godinez, Social and cultural influences on food choices: A 928
review, Crit. Rev. Food Sci. Nutr. 62 (2022) 3698 –3704. 929
https://doi.org/10.1080/10408398.2020.1870434 930
[84] J. Hartmann, J. Huppertz, C. Schamp, M. Heitmann, Comparing automated text 931
classification methods, Int. J. Res. Mark. 36 (2019) 20 –38. 932
https://doi.org/10.1016/j.ijresmar.2018.09.009 933
[85] F. Fagioli, G. Gallesio, E. Viganò, Wineries communication strategies. A text mining 934
analysis, Wine Econ. Policy 11 (2022) 73–87. https://doi.org/10.36253/wep-11305 935
[86] S. Sillani, A. Miccoli, F. Nassivera, Different preferences for wine communication, Wine 936
Econ. Policy 6 (2017) 28–39. https://doi.org/10.1016/j.wep.2017.03.002 937
 938
