---
title: 'Paid to Look Like Truth: The Prevalence and Dark Patterns of Advertorials in News Outlets'
url: https://arxiv.org/abs/2602.12810
category: digital-marketing
subcategory: empirical
date: 2026-02
venue: ''
authors:
- Emmanouil Papadogiannakis
- Panagiotis Papadopoulos
- Nicolas Kourtellis
- Evangelos Markatos
source: arxiv
pdf_url: https://arxiv.org/pdf/2602.12810
pages: 17
chars: 112014
fetched_at: '2026-11-08T13:15:45+00:00'
kb_version: 1
---

# Paid to Look Like Truth: The Prevalence and Dark Patterns of Advertorials in News Outlets

Paid to Look Like Truth: The Prevalence and Dark Patterns of
Advertorials in News Outlets
Emmanouil Papadogiannakis
FORTH & University of Crete
Heraklion, Greece
Panagiotis Papadopoulos
FORTH
Heraklion, Greece
Nicolas Kourtellis
Keysight AI Labs
Barcelona, Spain
Evangelos Markatos
FORTH & University of Crete
Heraklion, Greece
Abstract
Advertorials represent a marketing strategy where advertisements
are designed to resemble the style and tone of editorial content.
Despite their appearance, they are, in fact, paid content intended
to promote a product, brand or service. Studies indicate that adver-
torials are more effective (81%) and less intrusive than traditional
banner ads or pop-ups. Despite regulatory efforts for clear disclo-
sure of paid content, concerns persist about the deceptive nature of
advertorials. Advertorials can mislead readers into believing that
they are consuming unbiased editorial content. In doing so, they
gain undeserved legitimacy, by draping themselves in the credibility
of the publication’s design.
In this study, we conduct the first systematic large-scale study
of advertorials. We propose a novel automated methodology for
detecting problematic advertorials in the wild, and collect 186K ad
URLs over a period of 5 months. We investigate their prevalence
and explore their structural and linguistic characteristics, finding
that advertorials appear in 1 out of 3 news websites, including
popular and credible outlets (e.g., The Guardian, EuroNews, CNN).
Additionally, they often exhibit behavior associated with malicious
practices and deliberately obscure or make legal disclaimers difficult
to recognize, preventing users from identifying the promotional
nature of the content.
CCS Concepts
•Information systems → World Wide Web;Online advertising.
Keywords
Advertorials; Online Advertising; Regulation; Dark Patterns; Web
Monetization
ACM Reference Format:
Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Nicolas Kourtellis,
and Evangelos Markatos. 2026. Paid to Look Like Truth: The Prevalence
and Dark Patterns of Advertorials in News Outlets. InProceedings of the
2026 ACM Internet Measurement Conference (IMC ’26), October 12–16, 2026,
Karlsruhe, Germany.ACM, New York, NY, USA, 17 pages. https://doi .org/
10.1145/3777912.3839787
This work is licensed under a Creative Commons Attribution 4.0 International License.
IMC ’26, Karlsruhe, Germany
©2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2327-8/2026/10
https://doi.org/10.1145/3777912.3839787
1 Introduction
In the digital age, advertising has become deeply intertwined with
how users consume online content. Articles, blogs, applications and
media are provided free of charge precisely because the underlying
content is funded by advertisements rendered by publishers on
their platforms. In recent years, native advertising has emerged as
a response to the overly disruptive nature of traditional banner and
display ads [44], as well as the significant rise in Web ad-blocking,
which is used by a staggering 42.7% of internet users [10]. Native
advertisements are online ads purposefully designed to blend seam-
lessly with a website’s content, frequently mimicking its structure
and style. Native advertising yields 53% more views [ 60] and a
2− 3× higher Click-Through Rate (CTR) than traditional advertis-
ing [65]. Furthermore, 85% of internet users may find native ads
more trustworthy than conventional formats [62].
Advertorialsare a form of native advertising that blend editorial-
style content with sponsored material and have been explicitly
crafted to resemble the tone, format and language of genuine edito-
rial articles. Studies indicate that advertorials are 81% more effective
(and notably less intrusive) than traditional ads [29]. Consequently,
Web users can sometimes unknowingly encounter content that
appears to be a standard article but is, in fact, an advertisement
promoting a specific brand, product or service. Importantly, not
all native ads lead to advertorials. A native ad may instead direct
users to a conventional product page, publisher content or another
type of landing page. In the case of advertorials, however, clicking a
native advertisement on an ordinary website, may direct the user to
an external landing page that presents promotional content in the
style of editorial or journalistic content, as illustrated in Figure 1.
The concept of blending advertising with editorial content is
not new. Early newspapers and magazines employed this format to
bolster revenue without expanding traditional ad spaces. However,
it was the digital revolution that catalyzed the widespread growth
of advertorials [47]. This proliferation is primarily driven by their
higher engagement rates and lower intrusiveness. In fact, studies
confirm that 70% of users prefer learning about a brand through
blog posts and articles rather than traditional advertisements [58].
Despite these benefits, the increasing difficulty in distinguishing
between actual journalism and paid advertising makes advertorials
a particularly problematic form, as they can mislead readers into
unknowingly engaging with promotional content. Users frequently
fail to recognize promotional content embedded within editorial
material, with only 9% of people identifying such advertorials [3].
For instance, in 2013, The Atlantic published a story praising the
arXiv:2602.12810v2  [cs.CY]  14 Sep 2026

IMC ’26, October 12–16, 2026, Karlsruhe, Germany Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Nicolas Kourtellis, Evangelos Markatos
Figure 1: Example of advertorials; paid advertisements de-
signed to look like an article, blending informative content
with product promotion. Although they appear to present
general information, they ultimately serve to promote a spe-
cific product (pillows on the left and cameras on the right).
Church of Scientology’s leader, presented in the same format as its
regular editorial content, which was later revealed to be a spon-
sored post [ 17]. This advertorial’s focus on sensitive topics like
religion highlighted the risks of poorly disclosed sponsored con-
tent. More recently, various news outlets in Australia promoted
gas energy without disclosing that these articles were sponsored
by the fossil fuel industry [ 46]. Compounding this issue, studies
show advertorials can blend so seamlessly with website content,
deceiving older adults [4] or visually impaired people [33]. These
issues raise concerns about how the inherent lack of transparency
in advertorials can influence public opinion and shape perceptions.
Various regulatory bodies, including the Federal Trade Commis-
sion (FTC), the European Commission, the Advertising Standards
Authority (ASA) and similar organizations worldwide, have sought
to curb the unrestrained use of advertorials and ensure that they
are clearly distinguishable from editorial content [1, 16, 18]. These
efforts aim to protect users from sponsored content disguised as
impartial journalism. In the academic domain, while substantial re-
search has focused on native advertising and problematic ads [2, 69],
less attention has been paid to the deployment patterns of decep-
tive or misleading advertorials, as well as the extent to which they
comply with existing regulations.
In this work, we conduct the first large-scale and systematic
study of advertorials, investigating their prevalence, as well as their
typical characteristics. We set out to explore how frequently online
users encounterproblematic advertorialsthat exhibit deceptive or
potentially harmful characteristics and study the language, style
and structure used by advertorial operators to mislead users. We
examine how advertorials employ common malicious tactics to
defraud users, often mimicking financial scams, miracle cures and
fraudulent campaigns, while also using dark patterns to bypass reg-
ulations. Our study focuses on advertorial landing pages reached
through advertisements displayed on news websites. We focus on
ads on news websites because advertorials are designed to look like
news articles, which may make them more effective. Through a
systematic analysis of online ads, we (i) identify common structural
and stylistic features of advertorials, and (ii) assess the frequency
with which users are exposed to such content. We then examine
global regulations and identify systematic non-compliance by adver-
torial publishers. Finally, we propose a novel methodology capable
of detecting problematic advertorials at scale. To support further
research, enhance transparency and help prevent user deception,
we publicly release data used in this study [52].
The contributions of this work include the following:
(1) Large-scale analysis: We conduct the first large-scale and
systematic study of deceptive advertorial landing pages across
multiple countries, investigating their prevalence within the
programmatic advertising ecosystem as well as their struc-
tural and linguistic features.
(2) Advertorial detection methodology: We propose a novel
automated approach for detecting problematic advertorials
in the wild, leveraging both structural and semantic features.
We apply this methodology to over 186K ad URLs collected
over a five-month period.
(3) Global prevalence:We discover over 10K instances of prob-
lematic advertorials served as ads in 193 news websites. We
find that 1 in 3 news websites worldwide serve ads for ad-
vertorials, including some of the most popular and credible
outlets, ranked among the top 2,000 websites globally.
(4) Geographical disparities:Our analysis reveals clear re-
gional differences in advertorial exposure, with U.S. users
encountering2 .5× more distinct advertorial domains than
users in the EU. We find that European news websites are less
likely to host advertorials, whereas those based in Asia or
North America are 50% more likely to feature such content.
(5) Content focus:We show that advertorials contain more
text than both benign ads and news articles, while having
substantially smaller HTML footprints (2 .7× smaller than
benign ads) and interacting with fewer third parties. Among
identified advertorials, 44% address sensitive topics such as
health-related products, services or supplements.
(6) Deceptive design patterns:We identify dark patterns (e.g.,
font size, color and text placement) that obscure legal dis-
closures, making them difficult to recognize. Disclaimers
are often written in more sophisticated language than their
surrounding content.
2 Background
2.1 Advertorial Definition
AnAdvertorialis a form of advertising that has been purposefully
designed to look and feel like editorial content. That is, the tone,
style and format of an advertorial resembles content written by
journalists or writers to inform or educate their audience. However,
the true goal of an advertorial is to promote a specific product, brand
or service. Figure 1 presents representative examples of advertorial
content, in which the headlines imply informative intent, such as
offering solutions to specific problems, while the actual content is a
paid promotion for a specific product. The fundamental concept of
an advertorial is to provide promotional content within an engaging
narrative, a technique that dates back to the early 1900s [ 42, 59].
However, with the evolution of online advertising, advertorials have
become extremely popular [20], as they are a perfect candidate for
native advertisements because of their less intrusive nature.
More formally, in [69], product advertorials are defined as“Ads
for consumer products written in the style of a blog post or news article
that do not obviously disclose that they were written by the advertiser,

Paid to Look Like Truth: The Prevalence and Dark Patterns of Advertorials in News Outlets IMC ’26, October 12–16, 2026, Karlsruhe, Germany
other than in the fine print in the header or footer of the page”. A
key characteristic is the journalistic tone, which leads readers to
perceive it as a standard editorial piece, providing engaging con-
tent that retains the user’s attention. In addition, although various
regulatory bodies require that advertisements contain a banner or
disclaimer indicating that the content is sponsored, such disclosures
are often in the footer fine print, making them easy to miss [69].
In this work, we focus onproblematic advertorials: a subset of
advertorials that exhibit characteristics commonly associated with
deceptive or potentially malicious practices. Such advertorials in-
corporate deceptive design practices (i.e., dark patterns), misleading
or fabricated content signals (e.g., falsified testimonials or stolen
images), indicators of security risks (e.g., deceptive landing pages)
or data exploitation mechanisms. These characteristics are identi-
fied through observable features and security signals (Section 3)
and align with known deceptive Web practices.
2.2 Misleading Promotional Tactics
In our setting, advertorials are reached through ads displayed on
news websites. More precisely, the user first encounters an ad (of-
ten in the form of native advertising) on a news website and, upon
clicking it, is redirected to an advertorial landing page. Rather than
presenting a conventional product ad, this page is designed to re-
semble an editorial article while promoting a specific product or
service. We refer to this external landing page as an advertorial and
consider it a distinct item from the ad. The news website displays
the ad that attracts the user’s attention, whereas the advertorial
is the promotional landing page reached after the user clicks on
that ad. Our analysis focuses on theadvertorial domainsthat host
the promotional content rather than the ads displayed on the news
websites themselves. We also focus only on ads served on news
websites, as advertorials are inherently designed to mimic the pre-
sentation and tone of news articles or other editorial content.
Such ads are often served on popular and reputable news web-
sites (e.g.,credible-news.com). As illustrated in Figure 2, the native
ads are intentionally designed to blend seamlessly with the web-
site’s editorial content, making it difficult for users to distinguish
them from actual journalism. Although such content may be labeled
(e.g., as “sponsored”), disclosures may be visually inconspicuous or
cognitively overlooked (Section 6), leading users to misinterpret
ads as genuine editorial content. When users click on the native ad,
they are redirected to the advertorial hosted onhealth-product.com.
There, the content typically presents misleading information in
a format that appears factual and objective, often supported by
fabricated reviews, testimonials or comments intended to convince
consumers of the legitimacy and effectiveness of the promoted
products. A major concern is the authenticity of these testimonials
and whether they originate from real consumers [6, 22]. The above
strategy constitutes an exploitative tactic that hijacks the trust peo-
ple have in credible news websites. Advertorials look like news
articles, disrupting the user’s advertising filters and skepticism,
and people might assume that the ad is credible since it appears
on a reputable website. This tactic may also undermine the host
website’s credibility if users feel misled by the platform that hosted
the native ad. In this work we do not focus on paid editorial content
published directly as part of a news outlet’s own content.
Figure 2: Advertorials (highlighted in red) being subtly pro-
moted among articles of popular news websites. Ads are inte-
grated into the news feed of legitimate news platforms, mak-
ing them virtually indistinguishable from editorial content.
By assimilating into the publication’s design, they illegiti-
mately acquire credibility.
2.3 Regulation on Advertising
Various regulation frameworks regarding advertising aim to pro-
tect consumers from practices that may harm them or impair their
ability to distinguish advertising from other content. The Euro-
pean Union introduced the Unfair Commercial Practices Directive
(UCPD) to protect consumers from deceptive marketing tactics [16].
The directive prohibits several misleading actions or omissions that
could “limit the consumer’s ability to make an informed decision”.
Importantly, the directive explicitly classifies advertorials as mis-
leading commercial practices, defining them as “using editorial
content in the media to promote a product where a trader has paid
for the promotion without making that clear in the content or by
images or sounds clearly identifiable by the consumer”. Notably,
ads must not deceive or mislead consumers, even if the information
presented is factually correct.
Similar to the UCPD, the Federal Trade Commission (FTC) in the
United States has issued guidelines that explicitly prohibit deceptive
or unfair practices [18]. They outline how to prevent deception and
avoid misleading impressions by ensuring that disclosures are clear
and prominently displayed. In the United Kingdom, the Advertising
Standards Authority (ASA) notes that advertorials are particularly
difficult for users to recognize as advertisements due to their re-
semblance to editorial content, and therefore, must be explicitly
disclosed as ads “upfront, in a prominent and easily noticeable
place” [1]. Likewise, the Australian Competition and Consumer
Commission (ACCC) prohibits advertisements that mislead or de-
ceive consumers, emphasizing that promotional content should
include prominently displayed disclaimers [7]. The ACCC specifies
that misleading conduct cannot be excused by disclaimers buried
in fine print and explicitly prohibits the use of fake testimonials.

IMC ’26, October 12–16, 2026, Karlsruhe, Germany Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Nicolas Kourtellis, Evangelos Markatos
450 News
Websites
Web Crawling
Ad URLs Problematic Advertorials
Detection Methodology
Ad Landing
Pages
✔
✔
✔
www.
AD
d. . . . . .
Structure-based
detection
Domain Risk
detection
REPORT
SimilarWeb
Step 1
Step 2
Step 3 Step 4 Step 5
Step 6
Figure 3: Overview of methodology for detecting problematic advertorials on news websites.
3 Methodology & Data Collection
In this work, we focus on problematic advertorials that use mis-
leading or fabricated content, hidden disclaimers and manipulative
visual design to obscure their sponsored nature. Such advertorials
often use fake testimonials and images to give the appearance of
legitimacy, further complicating detection. Additionally, problem-
atic advertorials often incorporate indicators of security risk, such
as deceptive landing pages and bulk-registered domains.
To detect problematic advertorials and differentiate them from
other forms of banner or native ads, we propose a novel data-driven
automated methodology. Our methodology relies on structural, lin-
guistic and semantic features of advertorial text to discern it from le-
gitimate editorial content or other forms of advertising (i.e., benign
ads). We provide a high-level overview of the overall methodology
in Figure 3. After data collection and filtering is performed (Sec-
tion 3.1) we combine two complementary detection modules. First,
the landing page itself is analyzed to determine whether it exhibits
structural characteristics associated with advertorials (Section 3.2).
This stage focuses on page properties and its presentation. Second,
we assess the suspiciousness of the associated domain using in-
dependent behavioral, reputational and technical signals obtained
from external security and reputation services (Section 3.3). This
stage operates at the domain level and assesses the potential risk
associated with the hosting domain. By combining the structural
signal with the domain maliciousness signal we are able to identify
problematic advertorials. An ad is considered a problematic adver-
torial only if both modules concur. Finally, a manual evaluation
(Section 3.4) assess the efficacy of our methodology.
3.1 Data Collection
To study advertorials, we first collect ads from websites in the
wild. Given that advertorials are intentionally designed to resemble
journalistic content, we analyze advertorials reached through ads
displayed on news websites. News websites provide an important
entry point for such ads because users may encounter native or rec-
ommendation ads while browsing news content and subsequently
be directed to advertorial landing pages. To that end, we compile
a list of news websites from around the world, focusing on the
“News & Media” category provided by SimilarWeb [61] (Step 1 in
Figure 3). To capture geographic variations in the news advertising
ecosystem, we prioritize a wider range across countries rather than
sampling a larger number of websites from a smaller number of
countries. In September 2024, we collect for each country the top
five news websites, websites trending up in rank, websites trending
down in rank, websites entering the top 100 and websites dropping
out of the top 100 based on SimilarWeb data. Our dataset covers
the 59 countries for which SimilarWeb provides country ranking
data. This sampling strategy allows us to capture not only persis-
tently popular news websites, but also news websites gaining or
losing audience interest. We note that the same news website can
appear among the websites of multiple countries. This collection
process yields a list of over 1K news websites, out of which we
retain only websites for which SimilarWeb also provides traffic
and headquarters information, resulting in a final list of 450 news
websites worldwide. We make this list publicly available [52]. We
provide the distribution of their network traffic in terms of monthly
visits in Figure 5 (𝑥-axis in log scale). We observe that the list spans
a wide range of audience sizes. The estimated network traffic of the
websites ranges from approximately 150K to 3.6B monthly visits
(4 orders of magnitude difference), indicating that our list includes
both small or local news websites and highly popular news out-
lets. Thus, our dataset provides broad geographic coverage while
capturing substantial variations in website popularity.
Using the open-source scraping tool of [ 54], in Step 2 of Fig-
ure 3 we visit the list of 450 news websites from three different
user locations (EU#1, EU#2 and U.S.) and collect all displayed ads.
We use a VPN service to set user location (with two EU locations
corresponding to different countries) and geolocation services to
verify the crawler’s location. We visit each website with a clean
browser state to keep its behavior and that of the advertising ecosys-
tem independent of previously visited domains. We also employ
a browser extension [50] to automatically interact with consent
banners and accept all cookies by default. As internal pages may
differ from landing pages [5], we visit the landing page of each news
website, as well as 5 internal subpages, selected via uniform random
sampling. Upon visiting a webpage, we wait for it to fully load, and
then an additional 20 seconds to ensure complete ad transactions
and rendering. We then scroll down each page for 6 seconds (if
possible) and then to the bottom to display all banner and native
ads. For each webpage, we collect its HTML content, the generated
network traffic, cookie-jar (both first-party and third-party cook-
ies) and detected ads. To discover ads, we adopt the methodology
of [55], which extracts links from the rendered page and network
traffic and evaluates them against the EasyList and uBlock Origin
filter lists to determine whether they correspond to ads. We extend
this approach by additionally traversing all HTML elements in the
rendered DOM and evaluating them against cosmetic filtering rules
contained in the same filter lists. For each element that matches a
cosmetic filter, we examine whether the element (or an associated

Paid to Look Like Truth: The Prevalence and Dark Patterns of Advertorials in News Outlets IMC ’26, October 12–16, 2026, Karlsruhe, Germany
child element) contains a clickable URL. If so, we classify the el-
ement as an ad and collect the respective URL. We provide more
information about the ad detection filter lists in Appendix A.
We perform a repeated measures study and visit the entire list of
news websites five times for each user location, totaling 15 distinct
campaigns, from October 2024 to February 2025. Altogether, we
detect and process 186,124 distinct ad URLs, a considerable increase
compared to previous work [69] (×3 more ads collected during the
crawling process and×34 more ads successfully passed through
the subsequent analysis pipeline). Finally, we visit the collected
ad URLs and analyze their landing pages (Step 3 in Figure 3). We
discuss ethical considerations of our work in Appendix B.
3.2 Structure-based Detection
Following the collection of 186K advertisement URLs, it is neces-
sary to identify which ad landing pages correspond to advertorial
content (Step 4 in Figure 3). Advertorials have several character-
istics that distinguish them from both traditional advertisements
and editorial content, including legal disclaimers, user comments,
testimonials and customer reviews. We develop a structure-based
method to detect such common advertorial characteristics. Our
methodology relies on both the website’s structure (i.e., HTML
structure) and the legal text of disclaimers.
To build our system, we first assemble a formal collection of ad-
vertorial characteristics. We manually visit and analyze the landing
pages of 850 distinct ads found on news websites. The ads are ran-
domly selected from the entire set of all 186K distinct ads detected
in Section 3.1. The goal of this manual inspection is to understand
the structure of advertorials and identify HTML snippets that can
be used for automated detection of advertorial landing pages. The
ads are not selected to cover specific news websites since we do
not analyze how ads are placed on different news websites. Instead,
we focus on the landing pages that the ads lead to.
Next, on each ad landing page, we search for common patterns
in advertorial landing pages across sampled ads and manually iden-
tify sections corresponding to testimonials, comments or reviews,
and extract the HTML attributes that define these sections. Our
focus is on HTML class, ID and other HTML data attributes [ 45]
(e.g., data-element-type) that can serve as selectors to identify
these specific sections on other websites. For instance, we uncover
that multiple advertorials have a specific user reviews section that
can be singled out using specific HTML attribute. We also discover
some fake comments on advertorial domains that explicitly resem-
ble Facebook comments and can be identified using the attributes
class="comment-holder clearfix"andid="fbcomments". We
also consider the structural hierarchy of HTML elements, to identify
precise instances of webpage sections and prevent misclassifica-
tions of unrelated pages that simply share similar attribute names.
These observations are incorporated into our detection pipeline
(Step 4 in Figure 3) and each specific HTML attribute is tested
against each ad landing page.
For disclaimers that explicitly disclose an advertisement as an ad-
vertorial, we compile a list of legal vocabulary (i.e., key phrases) that
reveal the website’s true nature. An example of such a disclaimer is
shown in Figure 4. We further refine our system by collecting more
detailed advertorial data. Specifically, we emulate different browser
Advertising Disclosure
This is an advertisement and not an actual news article, blog, or consumer protection
update. This website is a marketplace. As such, you should know that the owner has
a monetary connection to the product and services advertised on the site. The owner
receives compensation whenever a qualified lead is referred, but that is the extent of
it. This compensation is used to help us continue to provide value to you. This does
not affect your overall experience and comes at no cost to you; we truly provide the
best possible deals we've found for every product listed.
Marketing Disclaimer: Any photographs of persons used on this site are models. All
product names, logos, and brands are intellectual property of their respective owners.
All company, product, and service names used on this website are for identification
purposes only. Using these names, logos, and brands does not imply endorsement.
The owner of this site and the products and services referred to on this site only
provides a service that consumers can obtain and compare.
Figure 4: Example of a legal disclaimer found on an adverto-
rial website, indicating that the page is an advertisement.
dimensions to detect responsive designs that present varied content
across devices, and we use a VPN service to access websites from
multiple countries, uncovering structural variations or disclaimers
translated into different languages. In total, we compile a list of 103
distinct legal disclaimer key phrases across seven languages (Eng-
lish, Dutch, German, Greek, Hebrew, Spanish and Portuguese) and
make this list publicly available to support further research [52]. We
do not make use of machine translation as our detection method-
ology relies on exact matching of language-specific phrases and
automatic translation can introduce inconsistencies or errors in the
matching process. We acknowledge that this list does not capture all
possible disclaimers. Our method provides a conservative estimate
and may miss disclaimers that use alternative wording.
We develop a detection module that visits an ad landing page and
extracts its text content and HTML structure. This module tests a
website against our dataset of disclaimer key-phrases and targeted
HTML elements or page structure and classifies the URL based on
whether its structure resembles the structure typically associated
with advertorial content. The module is then deployed on landing
pages of the 186K ad URLs detected in Section 3.1 to assess whether
they are candidate advertorials.
3.3 Domain Risk Detection
The structure-based detection methodology attempts to discover
ads that resemble editorial content (i.e., advertorials). Next, to explic-
itly label an ad as a problematic advertorial, we evaluate whether
it misleads, deceives or even defrauds users. Relying on impartial
Web engines, we build an automated classification system to as-
sess whether the domains hosting these pages exhibit suspicious
or malicious characteristics, based on behavioral and reputational
indicators (Step 5 in Figure 3). The advertorial landing pages in our
dataset are hosted on domains different from the news websites on
which the ads are displayed. As a result, the domain risk analysis
focuses on the advertorial providers rather than the news websites.
To build our automated advertorial filter, we first create a ground
truth dataset containing 1,000 ads, randomly selected from the ini-
tial dataset of ads on news websites (Section 3.1). Then, we conduct
a human annotation procedure to label instances of problematic
advertorial content. This manual annotation procedure is indepen-
dent of the one of Section 3.2 and provides ground-truth labels
for evaluating the resulting detection module. Keeping these steps

IMC ’26, October 12–16, 2026, Karlsruhe, Germany Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Nicolas Kourtellis, Evangelos Markatos
Target Accuracy Precision Recall F1
Weighted Avg 0.928 0.929 0.928 0.923
Suspicious Domains 0.928 0.854 0.677 0.738
Benign Domains 0.928 0.943 0.975 0.958
Table 1: Domain risk classifier that achieves∼93% accuracy
and F1 in detecting suspicious domains. The slightly lower
performance on suspicious domains does not affect its role
in the overall methodology.
separate ensures that we do not design the detection rules using
the same data that we later use to evaluate them. The annotation
phase involves 2 distinct reviewers that can label an ad as either
an advertorial or a benign ad for legitimate display ads. One of the
reviewers is an author of this work, while the second is a knowl-
edgeable (i.e., computer science background) but independent (i.e.,
not affiliated with this work) reviewer and is only informed about
the advertorial definitions of Section 2. Both reviewers are shown
screenshots of ad landing pages and may browse them or use any
translation tools they deem necessary. Reviewers are not informed
about where the ad was placed and perform the annotation tasks
independently, without interaction or shared decisions.
Following the manual annotation procedure, we analyze inter-
rater agreement and find that reviewers classify 820 ads as benign
and 157 as advertorials. Reviewers disagree on only 23 ads, resulting
in a 97.7% agreement. The Cohen’s kappa score is 0.92, indicating
almost perfect agreement. In the final dataset, an ad is labeled as
advertorial only when both reviewers agree, thereby increasing
confidence in the ground truth. The resulting dataset is imbalanced,
with more benign ads than problematic advertorials, reflecting
real-world conditions in which benign advertisements outnumber
advertorials [69]. A brief follow-up interview conducted after the
annotation task revealed that reviewers’ decisions were primarily
influenced by the presence of legal disclaimers and recurring struc-
tural patterns (e.g., page layout, comment sections and customer
review areas). These features served as strong indicators for distin-
guishing advertorials. Reviewers also noted that the editorial style
of advertorials differs substantially from that of conventional ads.
An illustrative example is provided in Appendix C.
The two detection modules of Figure 3 address different proper-
ties. The structure-based module identifies whether an ad leads to a
page that exhibits the characteristics of an advertorial. The second
module operates at the domain level and estimates whether the
domain hosting the landing page is suspicious or malicious based
on independent behavioral, reputational and technical signals. We
use this domain signal as an additional indicator of problematic ad-
vertorials. To that end, we build a classifier whose prediction target
is domain maliciousness and not whether an ad is an advertorial.
To extract behavioral, reputational and technical data about
domains, we build an oracle of 19 independent security, safety and
analytics Web engines. We select only reputable and trustworthy
services, such as VirusTotal, Norton Safe Web and ScamAdviser.
We report the list of Web engines in Appendix D and note that
the authors have no affiliation with these engines. We also build
a simple crawler that measures the size of the landing page in
Target Accuracy Precision Recall F1
Weighted Avg 0.874 0.894 0.874 0.864
Problematic Advertorials 0.874 1.000 0.598 0.749
Benign ads 0.874 0.845 1.000 0.916
Table 2: Manual evaluation of the detection methodology
on real and untested data. Detection accuracy is emphasized
over dataset size to ensure reliability.
HTML format. We make use of 20 signal sources (i.e., engines) and
extract 45 features per domain. For training the domain classifier,
the training instances are domains hosting the landing pages of ads
that were manually labeled as either benign ads or advertorials. To
improve model efficiency and reduce overfitting, we apply feature
selection using a random forest classifier. Following common best
practices, we encode categorical features as numerical values and
impute missing data. Feature importance is measured using Gini
impurity and 24 features are retained, accounting for 96% of total
importance. We discuss feature selection in Appendix D.
To build the detection module, we evaluate several classifiers
(including K-Neighbors, Multilayer Perceptron, Gaussian Process)
and find that a Random Forest Classifier performs best. We split the
labeled dataset of ad domains into training and test sets using an
80:20 random split performed at the domain level. No constraint is
imposed on the news websites on which the ads were served since
the classification task focuses on the domains associated with the
ads and not the source news websites. We also perform hyperpa-
rameter tuning and cross validation with 20 iterations to accurately
compute the model’s true performance. In Table 1, we demonstrate
that the classifier achieves accuracy and F1 score of almost 93%.
Although performance is slightly lower for suspicious domains,
this is not concerning, as the classifier is only one component of
the overall methodology. We further discuss this in Section 3.4. The
proposed filter is applied sequentially after the structure-based de-
tector (Section 3.2), providing increased certainty as to whether the
landing page of an ad URL corresponds to a problematic advertorial.
3.4 Manual Evaluation
As illustrated in Figure 3, the proposed advertorial detection method-
ology consists of two sequential components: structure-based and
domain risk detection. We consider their combination essential,
as the former identifies content with editorial structure, while the
latter detects domains that may mislead or deceive users. We group
the two components into a filter that detects problematic advertori-
als (Step 6 in Figure 3) and evaluate its performance in the wild. We
run the entire pipeline on all 186K ad URLs and manually evaluate a
subset of 1,000 URLs to measure its true performance. These ads are
randomly selected and have not been processed by the classifier at
any stage (training or testing). The classifier of Section 3.3 is trained
and tested on a different set of manually labeled ads, allowing us
to evaluate the detection pipeline on previously unseen ad landing
pages. The ad URLs correspond to 731 distinct ad landing pages, as
the same ad may appear on different websites or visits. We follow
the same procedure as in Section 3.3 and manually annotate 502
ads as benign ads (68.67%) and 229 as advertorials (31.33%).

Paid to Look Like Truth: The Prevalence and Dark Patterns of Advertorials in News Outlets IMC ’26, October 12–16, 2026, Karlsruhe, Germany
User Crawled # news websites % news websites # advertorial
Location Websites with advertorials with advertorials domains
EU#1 435 151 34.71% 93
EU#2 437 160 36.61% 88
USA 429 157 36.60% 223
Table 3: Advertorials served across different user locations
while visiting news websites. Websites containing advertori-
als are consistent across locations, but U.S. users encounter
2.5×more advertorials than EU users.
Then, we feed these 731 ads to our detection module and pro-
vide our findings in Table 2. We demonstrate that our detection
methodology achieves perfect precision in identifying problematic
advertorials, albeit with lower recall. This is a deliberate design
choice. A domain is classified as advertorial only when both the
structure-based and domain risk detection modules concur. Since
this study focuses on domains serving advertorials, maintaining
high confidence in detection accuracy is essential, even at the cost of
a smaller dataset. We argue that this conservative approach does not
undermine the correctness of our findings, but rather it establishes
a reliable lower bound on advertorial prevalence. This enables reli-
able conclusions about the nature and distribution of problematic
advertorials, while avoiding incorrectly labeling legitimate editorial
domains as advertorials. We acknowledge that feature-based detec-
tion methods may be subject to evasion, and we therefore position
our approach as a measurement tool for characterizing advertorials
rather than a fully adversarially robust detection system.
4 Advertorial Prevalence & Reach
Using the data collection methodology described in Section 3.1,
we identify 186K ad URLs corresponding to more than 11K dis-
tinct ad landing pages, which represent the pages users reach after
clicking on an advertisement. We then input these domains into
the detection methodology outlined in Figure 3, focusing exclu-
sively on domains that trigger both the structure-based and domain
risk filters. This process yields over 10K ads found in 193 distinct
news websites, directing users to 302 distinct domains that dissem-
inate advertorial content. We publicly release the list of advertorial
domains [52].
User location:We examine the advertorials encountered by users
located in different locations when visiting news websites. A news
website is considered to serve advertisements leading to problematic
advertorials if our detection methodology identifies at least one
such instance on either an internal page or the landing page during
any visit. Our findings, shown in Table 3, reveal that the number of
news websites containing advertorial ads is consistent across users
from different locations, with only minor fluctuations. In other
words, there appears to be no significant difference in the news
websites serving at least one advertorial to users within versus
outside the EU. Most importantly, we find that just over 1 in 3 news
websites worldwide (between 34.7% and 36.6%) serve ads that may
mislead or deceive their visitors (i.e., problematic advertorials).
Furthermore, we find that the number of domains serving adver-
torials is2 .5× higher for users visiting from the United States than
for users visiting from the European Union (last column of Table 3),
despite similar advertorial prevalence across news websites in the
two regions. This result highlights a geographical disparity in user
exposure to advertorial content. EU users tend to encounter the
same advertorials across multiple websites, whereas U.S. users are
exposed to a substantially larger and more diverse set of advertori-
als. This increased exposure may hinder users’ ability to distinguish
between journalistic and sponsored content, potentially affecting
unbiased decision-making. We also examine the total number of ads
served to EU and U.S. users and observe that the median number of
ad URLs per news website is 36% lower for U.S. users. This finding
indicates that the higher exposure to advertorials among U.S. users
is not driven by an overall increase in advertising volume.
We acknowledge that the use of vantage points may affect ad
delivery, with advertising platforms restricting ads from traffic as-
sociated with VPNs. However, this behavior does not affect the
correctness of our findings, but rather represents a conservative
lower bound. Finally, the observed differences in advertorial ex-
posure between EU and U.S. users may be influenced by factors
such as variations in regulatory pressure, enforcement and cul-
tural differences in consumer protection. Although our study does
not directly examine these, future work could investigate regional
differences in advertorial exposure.
Finding 1:1 out of 3 of news organizations internationally
serve ads for problematic advertorial content on their websites.
This is particularly evident for U.S. users that deal with ×2.5
more problematic advertorial domains compared to EU users.
Location of operation:Next, we investigate whether a website’s
location affects the presence of problematic advertorials on news
websites. While many news websites have a global presence and are
visited by users from multiple countries, we focus on the location of
each website’s headquarters since editorial standards and business
practices are often influenced by the hosting country. Headquarters
information is provided by SimilarWeb, as described in Section 3.1.
To better understand the effect of website location, we also group
websites by continent using data from the United Nations Statistics
Division [64].
Our findings are illustrated in Figure 6, focusing only on news
websites from Europe, Asia and North America. Websites from
other continents are excluded due to small sample sizes that do not
ensure statistical representativeness (e.g., only 11 websites from
Oceania). Every website is visited from each of the three vantage
points (i.e., EU#1, EU#2, U.S.). We find that European websites
contain the fewest advertorials, while websites hosted in Asia or
North America are more prone to serving them. Approximately
23% of European websites served an advertorial to their visitors,
compared to roughly 43% of Asian websites and 42% of North
American websites. Consequently, news websites hosted in Asia
or North America are almost twice as likely to serve problematic
advertorials to their users. The consistency of these results across
all user locations suggests that the findings are generalizable. An
examination of individual countries reveals that websites from India
serve the most ads for advertorials, regardless of user location.
Advertorial Prevalence in High-Traffic Sites:We further study
the news websites that promoted at least one problematic adverto-
rial to visitors in our data. We find that ads for problematic adver-
torials appear even on some of the most popular and credible news

IMC ’26, October 12–16, 2026, Karlsruhe, Germany Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Nicolas Kourtellis, Evangelos Markatos
100K 1M 10M 100M 1B
Network Traffic (Monthly Visits)
0.0
0.2
0.4
0.6
0.8
1.0ECDF
Min: 150K
Max: 3.6B
Median: 18.1M
Population: 450
Figure 5: Network traffic distribution
of news websites (monthly visits). The
dataset contains both low-traffic (unpop-
ular) and high-traffic (popular) sites, re-
flecting Web diversity.
EU#1 user EU#2 user USA user0
10
20
30
40
50% of news websites
21.8 23.9 24.0
43.1 43.8 43.2
39.7 41.3
45.2
Figure 6: News websites containing adver-
torial ads, grouped by website location.
News websites based in Asia or North
America are∼50% more likely to contain
advertorials.
0 10 20 30 40 50 60 70 80
% of advertorial ads
Microsoft Corp.
RevContent, LLC
Google LLC
Outbrain
T aboola, Inc.
0
2
0
34
64
0
1
0
32
67
1
0
7
28
61
Figure 7: Ad Networks placing adverto-
rial ads on news websites. Bars repre-
sent different user locations. Problem-
atic advertorials are mainly promoted by
Taboola and Outbrain.
websites worldwide, including The Guardian, EuroNews and CNN.
Examples are provided in [52]. Using the Tranco list [36], which
aggregates multiple sources to rank domains (ID: 998W2), we study
the popularity of news websites promoting problematic advertori-
als. We observe that 26.9% (i.e., more than 1 in 4) of news websites
with advertorials are ranked in the top 2,000 worldwide. Altogether,
these websites receive an aggregated traffic of∼11.8 billion monthly
visits, increasing the risk of exposing vulnerable populations and
impairing their ability to make informed decisions. We also find
no correlation between network traffic and advertorial presence
(Spearman correlation = 0.1, 𝑝 = 0.006), suggesting advertorials
appear on both popular and less popular news websites.
Finding 2:Advertorials are found even on the most popular
news websites around the world, with websites hosted in Asia
and North America being more prone to serving advertorials.
In Europe, advertorials are more restricted.
Advertorials Across Major Ad Networks:Given the complex
nature of programmatic advertising, publishers often cannot fully
control the type or quality of the ads displayed within their ad
inventory. As a next step, we examine the ad networks responsible
for serving the ads that lead users to problematic advertorials. For
each ad leading to a problematic advertorial, we analyze the URL,
extract its domain at the eTLD+1 level, and identify the operating
ad network using the DuckDuckGo Tracker Radar dataset [ 14].
Domains without ownership information are excluded. Figure 7
shows that Taboola and Outbrain serve the majority of ads that
lead to problematic advertorials (∼64% and∼31%, respectively)
consistently across user locations, which is aligned with previous
research [69]. Notably, even major ad networks such as Google and
Microsoft promote problematic advertorials. A manual analysis on
a random sample of 100 ads from these networks confirmed that
all were indeed problematic advertorials, showing that deceptive
ads can bypass even the largest, most reputable ad networks.
Repeated Exposure to Deceptive Advertorials:Finally, we study
the frequency with which certain advertorial domains appear as
ads on news websites, identifying domains repeatedly displayed
across dozens of sites. The domainushoppyworld.comappeared as
an ad on 116 distinct news websites for the EU#1 user. Similarly,
web.expertmarket.comappeared on 101 news websites for the EU#2
user. We observe that users are repeatedly exposed to the same
deceptive advertorials, often on credible, popular news websites,
increasing the likelihood they will believe them (i.e., manipulation
through familiarity). Additionally, we conduct a case-insensitive
search for these advertorial domains in two of the authors’ orga-
nization’s unsolicited email inboxes and discover seven detected
domains used the same advertorial narratives via spam emails.
This suggests that some operators attempt to reach users through
multiple communication channels. These channels are considered
“unwanted solicitations” under UCPD and are explicitly prohibited.
Finding 3:Ads for problematic advertorials are mainly served
by Taboola and Outbrain while some advertorials are repeatedly
displayed across numerous news websites and manage to bypass
filters of even the largest ad networks.
5 Characteristics and Content Analysis
5.1 Domain Characteristics & Lifespan
We study the domains that host or distribute problematic adverto-
rials to understand how such advertising operates at scale. These
domains may either be owned and operated by bad actors seeking
to serve problematic advertorials, or be legitimate websites that
have been compromised and unknowingly host problematic con-
tent, as observed in previous work [19]. Given that both scenarios
result in the distribution of similar advertorial content, we treat all
domains equivalently. Using the Registration Data Access Protocol
(RDAP) [24], we successfully collect registration information for
213 problematic advertorial domains. We observe that 81% of them
use the.comTLD, rather than less familiar alternatives. Following
that,.organd.shopTLDs are less common, representing only 3%
and 2% of advertorial domains, respectively. Evidently, advertorial
operators prefer the.comTLD. In contrast, fewer than 20 domains
use less common TLDs such as.shop,.online,.clubor.biz.
Next, we examine the registrars that registered the domain
names. We identify NameCheap as the most common registrar,
with 59% of problematic advertorial domains registered through it.

Paid to Look Like Truth: The Prevalence and Dark Patterns of Advertorials in News Outlets IMC ’26, October 12–16, 2026, Karlsruhe, Germany
2016-012017-072019-012020-072022-012023-072025-01
Timeline (trimmed)
0
2
4
6
8
10Number of advertorial domains
Figure 8: Registration date of advertorial
domains. 56% of these domains have been
registered less than two years prior to
data collection.
1 10 100 1K 10K 100K
T ext Length
0.0
0.2
0.4
0.6
0.8
1.0ECDF Median: 7.7K
Median: 5.5K
Median: 3.8K
Advertorials
News Websites
Benign Ads
Figure 9: Distribution of text length for
advertorials and other types of websites.
Advertorials contain notably more text
than benign ads and are closer in length
to news articles.
0 20 40 60
Number of Third Parties
0.0
0.2
0.4
0.6
0.8
1.0ECDF Median: 5
Median: 7
Median: 13
Advertorials
Benign Ads
News Websites
Figure 10: Distribution of third-party in-
teractions across website types. Adverto-
rial domains interact with fewer third-
party trackers than benign ads and news
websites.
Notably, ScamAdviser reports that NameCheap has a high propor-
tion of spammers and fraudulent sites, potentially due to a lenient
registration process. GoDaddy is the second most popular registrar,
accounting for 21% of domains. Together, these two registrars (re-
sponsible for 80% of problematic advertorial domain registrations)
appear to enforce advertising regulation policies ineffectively or
offer only loose verification. Both explicitly prohibit “wrongful de-
ception with the intent to gain a monetary benefit” and “misleading
or deceptive content” on registered domains. Prior work has also
shown that NameCheap and GoDaddy disproportionately register
misinformation websites [23].
Finally, we examine the lifetime of advertorial domains using
registration dates. Results are shown in Figure 8, with a truncated
𝑥-axis highlighting recent years. We find that most advertorial do-
mains are relatively new. More than half (56%) are less than two
years old at the time of writing (i.e., registered after May 2023), and
88% were registered after January 2020. Newly registered domains
can indicate low reputation or trustworthiness, or suggest malicious
intent [63]. A closer inspection of domain names reveals evident
patterns, such aswellnessguide103.comandwellnessguide104.com.
Bulk domain registrations over a short period may signal coordi-
nated campaigns designed to evade detection or content-blocking
systems. Manual examination reveals cases in which different do-
mains promote the same product, share identical structure and
appearance, or even reuse the same user testimonials for different
products. We provide example screenshots in [52].
Finding 4:Advertorial operators mostly register recently cre-
ated.comdomains, through registrars such as NameCheap and
GoDaddy, with evidence of coordinated registrations.
5.2 Advertorial Content & Structure
Next, we perform a deeper investigation into the content that prob-
lematic advertorial domains serve, that is, the text they use to
persuade users to purchase a product or service. A defining charac-
teristic of advertorials is that they are written to resemble editorial
or journalistic content. Towards that, we compare their text length
with that of other types of websites.
We construct a corpus of 300 problematic advertorials, 300 be-
nign ads and 300 news articles based on data from the repeated-
measures study (Section 3.1). Benign ads are randomly selected
from the manual annotation process (Section 3.3), while news arti-
cles are drawn from the pages visited by the crawler. We randomly
sample 300 instances from each category to obtain balanced and
comparable sets, avoid differences in set size from influencing our
analysis and maintain a manageable workload given our available
computational resources. We extract the full HTML and all visible
plain-text content of each page and in Figure 9 we plot the resulting
text-length distributions.
We find that advertorials contain significantly more text than
both benign ads and news articles. Two-sample KS tests across all
pairs of distributions show statistically significant differences, with
𝑝-values close to zero (< 1𝑒−6). Notably, advertorial text length is
closer to news articles than to benign ads, with a KS statistic of
0.22 versus 0.37. This supports the hypothesis that advertorials are
deliberately crafted to mimic editorial content rather than tradi-
tional ads. The logarithmic 𝑥-axis in Figure 9 reveals substantial
variation in advertorial text length. That is, some advertorials are
very brief, while others contain substantial content. Further inspec-
tion shows that short-text advertorials primarily rely on embedded
videos, whereas lengthy advertorials often cover multiple products.
Beyond the textual content presented to users, we also analyze
the size of the full HTML pages. Interestingly, although adverto-
rials contain more on-page text than both benign ads and news
articles, they exhibit the smallest HTML footprint. The median
advertorial page contains 106.3K characters:2 .7× smaller than the
median benign ad page (284.1K) and4 .6× smaller than the median
news article (484.8K). This observation suggests that advertorial
domains prioritize delivering user-facing text while largely avoid-
ing complex page structures, SEO-oriented markup or integrations
with advertising and tracking services. Such components typically
inflate HTML size and introduce additional dependencies.
To assess this hypothesis, we quantify the number of third-
party entities contacted during page loads. We visit the corpus
of 300 advertorials, 300 benign ads and 300 news articles, captur-
ing all HTTP(S) traffic generated during the initial landing-page

IMC ’26, October 12–16, 2026, Karlsruhe, Germany Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Nicolas Kourtellis, Evangelos Markatos
load. We wait 10 seconds after page load to capture dynamic re-
quests and automatically accept all consent banners to avoid block-
ing third parties. Then, we process all requests and group their
domains on the eTLD+1 level. For example, requests towardsre-
gion1.analytics.google.comandaccounts.google.comare all grouped
under thegoogle.comdomain. Figure 10 shows the number of third
parties each website type interacts with. We find that advertorial
domains interact with fewer third parties than benign ads and news
articles. The median problematic advertorial website contacts just
8 distinct third parties, compared with 12 for benign ads and 19
for news articles. When evaluating third-party domains against the
Disconnect list of known trackers [ 13], we find that the median
problematic advertorial domain interacts with 5 distinct third-party
trackers. This is still lower than the 7 trackers present on the me-
dian benign ad domain and the 13 trackers on the median news
website. Altogether, problematic advertorial domains focus on one-
time visitors and avoid deploying third-party trackers that yield
benefits for long-term or returning users.
Finding 5:Operators of problematic advertorials prioritize
the textual content of their webpages over complex designs or
additional functionality. They are often text-heavy and closely
resemble news articles rather than benign ads.
Next, we analyze the thematic content of advertorials to identify
the products or services being promoted. We perform language-
agnostic website classification using the pre-trained model of [40].
We classify the landing page of each advertorial domain in its origi-
nal language (i.e., without translation) and incorporate visual fea-
tures by providing a screenshot of the landing page to the classifier.
Each domain is assigned the category with the highest predicted
probability, with Figure 11 presenting the distribution of topics.
We find that the majority of advertorials (44.5%) promote prod-
ucts or services related to Health, with Shopping and Home being
the next most common categories. Together, these three categories
account for approximately 85% of all advertorial topics. Interest-
ingly, benign ads rarely promote the Health category. Instead, Busi-
ness and Shopping dominate, each accounting for roughly 21%
of benign ads. Health products rank only seventh, representing
only 6% of the benign ads analyzed. Advertorials addressing sensi-
tive topics such as health are particularly concerning, as they may
pose systematic risks to user safety. Indeed, the UCPD prohibits
deceptive claims regarding the benefits or risks of products.
Next, we examine the languages in which advertorials are served.
We observe that advertorials are typically shown in English, fol-
lowed by the user’s native language. Specifically, 52% and 64% of
advertorials were in English for users in EU#1 and EU#2, respec-
tively, while 42% and 33% appeared in the primary language of the
country from which the user endpoint accessed the website (i.e., na-
tive language). For users in the U.S., all advertorials were in English.
In a small number of cases (< 6%), the text appeared in a language
associated with the location of the news website rather than the
user. Finally, some advertorial domains automatically translate their
content based on the user’s location. We confirm this behavior using
VPN connections from different geographic regions.
Finding 6:Advertorials most often refer to sensitive issues
by promoting health products or services, while their text is
usually in English.
6 Patterns of Malicious Behavior
6.1 Deceptive and Coordinated Activity
Our analysis shows many advertorial domains display patterns
associated with suspicious, malicious or illicit websites.
Deceptive Landing Pages:We observe that some advertorial do-
mains have an empty or completely unrelated landing page. When
users directly type the advertorial domain name and navigate to it
(rather than arriving from a third-party website), they encounter ei-
ther a blank page or unrelated content. We identify cases where the
landing page corresponds to an architectural firm, a manufacturing
company, a generic privacy policy, etc., yet navigating to specific
URLs within the same domain leads to problematic advertorials.
In some instances, advertorial domains return a 404 error when
visiting the landing page. The domainushoppyworld.comdisplays a
generic WordPress template as its landing page but serves multiple
distinct advertorials on subpages. Altogether, we attribute such
behaviors to attempts to conceal advertorial campaigns and evade
detection, as documented by prior work (e.g., [53, 73]).
Content reuse:Using perceptual hashing, we discover nearly iden-
tical images reused across different advertorials promoting the same
product, including weight-loss results, product usage and customer
profile photos. We also identify “authors” publishing advertorials
on multiple seemingly unrelated advertorial domains. For example,
one author (same name and profile picture) has published different
problematic advertorials in at least 11 distinct domains. Another
author has published an identical advertorial (title, content, images,
structure) on the same day in 4 different domains, all of which
respond with a404error when users attempt to navigate to their
landing page. Manual verification shows that the listed authors
are fabricated personas. No verifiable social media or professional
accounts could be linked to these “authors” and reverse image
searches revealed that their photos appear on unrelated websites.
This behavior suggests that the domains may be controlled by the
same entity or a coordinated network. A similar pattern emerges in
the “user comments” sections. The same username appears across
7 problematic advertorial websites promoting weight-loss products.
These domains display identical comment threads with the same
users in the same order and matching timestamps. Even the user-
submitted photos in “testimonials” are identical. These patterns
indicate fake accounts designed to mimic engagement or approval.
Personal Data Harvesting:We perform a manual analysis on a set
of 10 problematic advertorial domains that receive the lowest scores
on the security-engine features of our detection risk detection mod-
ule (Section 3.3). Several of these domains are low quality and even
flagged as scams or potential malware by security engines. When
users attempt to place an order for the promoted product, some do-
mains collect sensitive personal information (name, address, email,
phone number, etc.) under the pretense that “a representative will
soon get in touch. ” Notably, the domainushoppyworld.com, which
exhibits multiple suspicious behaviors (e.g., unrelated landing page,
different advertorials per URL), also follows this pattern. Several
other domains present questionnaires that request personal details
such as age, weight, height and address, supposedly to recommend
the most suitable product. However, regardless of the responses
provided, the same product is promoted, revealing a deceptive and
non-personalized marketing approach.

Paid to Look Like Truth: The Prevalence and Dark Patterns of Advertorials in News Outlets IMC ’26, October 12–16, 2026, Karlsruhe, Germany
0 10 20 30 40 50
% of advertorials
Science
Games
Sports
Arts
Society
Recreation
Kids And T eens
Business
News
Computers
Home
Shopping
Health
Advertorial T opic
0.3
0.3
0.3
0.7
1.0
1.3
1.7
2.7
2.7
4.0
15.1
25.4
44.5
Figure 11: Distribution of advertorial top-
ics in news websites. Advertorials com-
monly promote health remedies and sup-
plements, whereas this is comparatively
rare in benign ads.
0 5 10 15 20
Contrast Ratio
0.0
0.2
0.4
0.6
0.8
1.0ECDF
Disclaimer Contrast Ratio
W3C AA Limit
W3C AAA Limit
Figure 12: Advertorial disclaimers con-
trast ratio. The AA value is W3C’s limit
for accessible text. 42% of disclaimers fall
below this threshold, reducing visibility
and readability.
0.0 0.2 0.4 0.6 0.8 1.0
T ype-T oken Ratio
0.0
0.2
0.4
0.6
0.8
1.0ECDF
Median: 0.55Median: 0.41
Disclaimers
Main T ext
Figure 13: Type-Token Ratio scores mea-
suring readability for advertorial text
and disclaimers. Median TTR is 34%
higher in disclaimers, suggesting linguis-
tic sophistication.
Finding 7:Some advertorial domains exhibit a variety of suspi-
cious patterns, including fake comments, fake authors, cloaked
(hidden) pages, image re-purposing, data harvesting, etc., that
suggest malicious intent.
6.2 Dark Patterns in Legal Disclaimers
Advertorial operators may appear compliant by disclosing their
intent, yet still violate regulations by mimicking news articles.
To assess this, we analyze disclaimer features in light of interna-
tional regulations, with a particular focus ondark patterns: design
choices that subtly steer users toward actions that benefit the ser-
vice provider [21]. We examine the legal wording that reveals the
true purpose of the content (to promote a product or service) and
differentiate between (i) disclaimers, typically written in a formal
style, explicitly describing the article’s nature and the publisher’s
monetary gain, and (ii) banners, usually a single word or short
phrase, labeling an article as advertorial or sponsored content. Fig-
ure 4 shows an example disclaimer, while the most common banners
are “Advertorial” or “Sponsored Content”. Our study focuses on the
advertorial pages reachedafterusers click on ads displayed on news
websites. We do not evaluate how clearly these ads are labeled or dis-
tinguished from editorial content on the news websites themselves,
as it is outside the scope of this work. However, we acknowledge
that since these ads are displayed through ad networks, they are
typically labeled as “Sponsored Content” or “Advertisement”.
Disclaimer Content:We examine the disclaimers published by
problematic advertorial domains to disclose that the content is, in
fact, an advertisement, even though it resembles editorial material.
These disclaimers are essential for advertorial operators, as they
help protect their operations against legal claims. We discover that
the most common disclaimers are “This website is an advertisement
and not a news publication” and “the owner has a monetary connec-
tion to the product and services advertised on the site”. This behavior
is consistent for visitors located both within and outside the EU.
The disclaimers appear on 52% and 45% of advertorial domains,
respectively, for EU#2 users and 43% and 44% for U.S. users. Vari-
ations of these disclaimers are also common in legal disclaimers,
for instance, the disclaimer “This is an advertisement and not an
actual news article” is found in 41% of the advertorials the U.S. user
visited. Interestingly, 30% and 25% of the advertorials that the U.S.
and EU#2 users came across, respectively, contain a very important
disclaimer that “This product is not intended to diagnose, treat, cure,
or prevent any disease”.
Disclaimer Position:We examine the locations of banners and
disclaimers on advertorial domains. We extract all text content from
advertorial pages and compute the relative position of each text
element based on its coordinates in the rendered page layout. We
filter out text that is not visible, either because it is contained within
hidden elements or because elements are placed outside the visible
and scrollable portion of the page. Our analysis shows that banners
are typically placed at the top of the page, while disclaimers appear
at the bottom. The median banner is located at the top 0.06% of
the page (standard deviation 1.42), whereas the median disclaimer
is at 96.12% from the top (i.e., at the bottom). Advertorials do not
prominently disclose their promotional nature, deceiving users and
hindering their ability to recognize the content as advertising [3].
Short top banners cannot convey all essential details and bottom-
page disclaimers are often overlooked, leaving users unaware of
critical information. FTC guidelines require disclosures to be placed
“as close as possible to where users will look first”. Similarly, the
UCPD prohibits providing information in an “untimely manner”
with users taking action before reading the disclaimer. Advertorials
fail these standards, placing disclaimers at the bottom of the page.
Visual Presentation of Disclaimer:The FTC guidelines also state
that “disclosures should stand out, so consumers can easily read or
hear them” and that they should be “in a font and color that is easy
to read” and “in a shade that stands out against the background”.
We study whether these guidelines are properly enforced, focusing
first on the visual presentation of text. For disclaimers, we measure
the Contrast Ratio, which quantifies the difference in luminance
between text and background colors. High contrast is necessary for
readability [66]. The contrast ratio ranges from 1:1, indicating no
contrast (e.g., black text on a black background), to 21:1, indicating
maximum contrast (e.g., white text on a black background). The
Web Content Accessibility Guidelines (WCAG) by W3C require a

IMC ’26, October 12–16, 2026, Karlsruhe, Germany Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Nicolas Kourtellis, Evangelos Markatos
contrast ratio of at least 4.5:1 for normal text (AA) and 7:1 for acces-
sibility to users with more severe visual impairments (AAA) [66].
Figure 12 shows the distribution of contrast ratios for all detected
disclaimers. We find that the median disclaimer has a contrast ratio
of only 4.76:1 and 41.92% of disclaimers have a contrast ratio below
the W3C minimum of 4.5. This indicates that text and background
colors are too similar, making the disclaimers difficult to notice
and read. The lowest contrast ratio we observe is gray text on a
background of a slightly different shade of gray (Appendix E).
Disclaimer Text Prominence:Next, we evaluate whether dis-
claimers or banners are clearly identifiable by users and whether
they stand out from other text on the page. To this end, we extract
all text elements from each advertorial page and compute their font
sizes. Analyzing the distribution of font sizes, we find that the ma-
jority of disclaimers and banners (69%) have a font size smaller than
the page’s median. As a result, disclaimers are deliberately smaller
and harder to notice, effectively functioning as “fine print”. Surpris-
ingly, only 5.5% of disclaimers have a larger font size, indicating
that only a small fraction stand out and can be easily identified.
Finding 8:Even though advertorials contain legal disclaimers,
they purposefully employ dark patterns to make these dis-
claimers hard to identify (e.g., small font size, faint font color,
placed at the bottom of the screen).
Finally, we focus on the FTC guideline that disclaimers should
be “understandable” and the UCPD requirement that information
should not be presented in an “unclear, unintelligible, or ambiguous”
manner. We acknowledge that assessing text understandability is
not trivial, as it depends on context and audience. However, we
employ two metrics to estimate how comprehensible and intelligible
disclaimers are. For each advertorial, we split its content into “Main
Text”, which contains the text promoting the product and written
in journalistic form, and “Disclaimer Text”, which contains the
actual legal disclosure. Text elements that do not constitute a legal
disclosure are categorized as main text (e.g., title, date, etc.). For
each type of text, we compute the Type-Token Ratio (TTR), which
measures lexical diversity. A high TTR indicates greater vocabulary
diversity, often found in academic papers or literature, while a low
TTR suggests repetitive vocabulary, typically found in informal
speech or simple text.
Figure 13 shows the distribution of TTR values for disclaimers
compared to main advertorial text. We find that disclaimers have
higher TTR values, with a median 34% higher than that of the
main text, suggesting that disclaimers are in a more sophisticated
style than the rest of the article. To verify this, we also compute
the Linsear-Write metric, which measures readability of technical
texts. This metric helps assess how accessible advertorial content
is to general audience. We find that the median disclaimer text
has a score of 8.57, while the median main text scores 5.6. These
correspond to an 8 th or 9 th grade reading level for disclaimers,
compared to a 5 th or 6th grade for main content. Consequently,
the main advertorial text is easier to read and more accessible to a
general audience than the more complex disclaimer text.
Finding 9:The legal disclaimer text in problematic advertorials
is more sophisticated than the rest of the website text and may
not be understandable by a general audience.
7 Related Work
Prior studies have examined online advertising ecosystems, includ-
ing ad targeting, bidding strategies and delivery optimization, high-
lighting how mechanisms influence what ads users are exposed to
(e.g., [28, 71]). Blending advertising with content is a long-standing
practice predating advertorials. Research shows users often struggle
to distinguish Google Search ads from organic results due to un-
clear labeling [38], leading to unintentional clicks. Similarly, native
ads in large language models (LLMs) are highly effective and well-
perceived when contextually relevant [68]. A study of 800 adults [4]
found only 9% recognized native ads, with recognition leading to
decreased trust in publishers. While health-focused advertorials
are well-documented [32], they are generally more effective than
traditional ads at manipulating purchase intent while remaining
unobtrusive. Content Recommendation Networks that distribute
sponsored links through widgets such as “Recommended For You”
have also been studied, showing that they often fail to clearly dis-
close the paid nature of content and highlighting the distribution
of ad content that can resemble editorial recommendations [9].
In [48], the authors discussed the prevalence of problematic ads
within Virtual Reality (VR) applications, which may require users
to perform controversial activities (e.g., simulating drug use) or
subject them to distressing experiences (e.g., depiction of death or
torture). They emphasized the necessity of explicitly labeling VR
advertisements to prevent deception and facilitate informed user
decisions. In [25], the authors developed a deep learning system to
detect misleading statements in advertisements for illegal cosmetics,
food and drugs. Similarly, a neural network that detects deceptive
ads by analyzing text, figures and HTML structures we developed
in [26]. In [69], the authors found that most problematic ads on news
and misinformation websites originate from native advertising.
Unlike our large-scale systematic analysis, their manual study used
a significantly smaller dataset (34× fewer ads) to compare display
and native formats. Both studies identified Taboola as the primary
source of problematic content, with Google contributing minimally.
A study of children’s websites [49] identified over 1K improper ads
(e.g., weight-loss and sexually suggestive ads).
Research also indicates that Google ads on Android can expose
users to malware [41] while fraudulent websites use Google and
Facebook to target their victims [ 11]. Studies show general user
hostility toward intrusive ads, particularly those that “blend in” or
promote “scammy” health supplements [70]. “Creepy” targeted ads
further drive demands for data transparency [37] and a large-scale
Facebook study confirms widespread user dislike for deceptive or
sensitive content [2]. Moreover, an analysis of 9K UK Advertising
Standards Authority complaints revealed that misleading ads domi-
nate the commercial sector [8]. Similarly, a study of 10K websites
found 10% non-compliant with Acceptable Ads Standards due to in-
trusive formats like pop-ups and autoplay videos [67]. Furthermore,
ad disclosures are frequently non-compliant on Facebook [15] or
absent on YouTube and Pinterest [43].
Similar to our approach, the authors in [ 31] developed an au-
tomated detection system for online survey scams by analyzing
website structure, content and word sequences. They found that
deceptive ads can lure users toward malicious survey gateways

Paid to Look Like Truth: The Prevalence and Dark Patterns of Advertorials in News Outlets IMC ’26, October 12–16, 2026, Karlsruhe, Germany
and then direct them to scam pages. Using a comparable methodol-
ogy, [35] investigated e-commerce scams. Much like our work, they
trained a Random Forest classifier using HTML features, though
they also incorporated robots.txt, network, HTTP and domain-level
features. Furthermore, utilizing telemetry data from millions of
devices, a study of 607,000 scam domains revealed that “Shopping”
is the most prevalent scam category [34]. Notably, 13.3% of users
reached these domains by following an advertisement, a behavior
similar to that observed with problematic advertorials. Scam cam-
paigns enticing users with gifts or investment opportunities are not
limited to advertorials, as they also appear within the comments
sections of various online platforms [39].
8 Discussion & Conclusion
Discussion:Problematic advertorials blur the line between jour-
nalism and advertising, intentionally deceiving users. Concerns
exist regarding whether the average consumer (or demographic
groups) can recognize them as paid promotions rather than impar-
tial articles. This misunderstanding can shape consumer opinions,
reducing their ability to make informed decisions. Furthermore,
advertorials are often hosted within coordinated networks to evade
detection, while showing suspicious, potentially malicious behavior.
Our findings highlight that there are significant weaknesses in the
practical protection of users by existing disclosure regulations. We
note that in this work we do not distinguish between limitations in
the regulations themselves and insufficient enforcement of those
regulations. Geographical differences in exposure suggest that reg-
ulatory frameworks and cultural factors shape user experiences,
underscoring the need for region-specific interventions.
Recommendations:To improve the detection and mitigation of
deceptive advertorials, monitoring should extend beyond low-traffic
or suspicious websites. Advertising platforms, publishers and mea-
surement systems should treat advertorial detection as a general
problem rather than an issue limited to obscure publishers. We be-
lieve the methodology presented in this work can help towards this
direction. In practice, monitoring systems can periodically crawl
ad landing pages and flag cases in which the destination resembles
editorial content but contains promotional material.
Moreover, detection systems should combine multiple signals in-
stead of attempting to identify problematic advertorials from visual
appearance or legal disclosures only. We demonstrate that struc-
tural features and the presence of specific components like user
comments can be used to distinguish ordinary advertising landing
pages from pages designed to imitate editorial content. Additionally,
the use of recently registered domains along with the relatively
small HTML footprint and limited third-party functionality of many
landing pages can contribute to a risk score that determines whether
a landing page receives additional analysis. Advertorials related
to health and disclosures that are difficult to understand should
be considered high risk cases. Since health products are often pro-
moted through advertorials (Section 5.2), advertising and publisher
review processes could apply stricter scrutiny to campaigns in this
category, particularly when claims are presented in an article for-
mat. Disclosure checks should also evaluate not only whether a
disclaimer is present, but whether it is sufficiently prominent and
understandable relative to the surrounding content (Section 6).
To address the challenges posed by advertorials, a combination of
policy, technological and community-driven measures is required.
Clearly defined and better-enforced regulations can have a signif-
icant impact, while increased commitment from the advertising
ecosystem is needed to prevent ads from appearing on legitimate
websites. Search engines, browsers and social media platforms can
contribute by improving filtering, annotation and warning systems
to reduce user exposure. Platforms like VirusTotal (see Appendix D)
can also support automated flagging and mitigation strategies. Due
to the prevalence of online advertising and the tools that filter
it [56], enhanced ad blockers or ML-based browser plugins that
automatically detect problematic advertorials can further increase
transparency and reduce exposure to hidden advertising.
Future Work:This study highlights several promising directions
for future work. First, a longitudinal analysis could examine how ad-
vertorials evolve over time, including their lifetime, disappearance
and reappearance and potential migration to new domains. Such
an analysis could also investigate how advertorial practices change
in response to regulation or novel detection mechanisms. Second,
future work could examine advertorials and paid editorial content
hosted directly on news websites. While ad-blocking tools can re-
duce exposure to many forms of online advertising, advertorials are
often indistinguishable from regular articles at the structural level,
while publishers often deploy anti-adblocking mechanisms [27]. As
a result, they might not be consistently addressed by traditional
ad-blocking mechanisms. Evaluating the extent to which existing
ad-blocking mechanisms mitigate problematic advertorials would
provide significant insight.
Conclusion:Advertorials are ads intentionally designed to re-
semble editorial articles, subtly promoting products without the
user’s awareness. In this work, we perform a large-scale, systematic
study of advertorials that draw user traffic from ads served on news
websites. We propose a novel detection methodology leveraging
structural, semantic and linguistic features, which accurately de-
tects problematic advertorials. We find that advertorials are both
widespread and frequently published, with∼35% of news websites
worldwide serving at least one ad for a problematic advertorial
domain. We also uncover that advertorial domains often exhibit
multiple suspicious behaviors, such as fake comments, fabricated
authors, hidden pages, image reuse and data harvesting, collectively
suggesting malicious intent. Finally, our findings highlight inconsis-
tent adherence to international regulations, with legal disclaimers
being purposefully difficult to recognize due to their size and place-
ment, while also containing sophisticated text. Overall, our work
emphasizes concerns regarding the effectiveness of regulations and
underscores the need for stronger consumer protection.
Acknowledgments
Funded by the European Union (ATHENA grant ID 101132686
and C-SOC grant ID 8515915). Views and opinions expressed are
however those of the author(s) only and do not necessarily reflect
those of the European Union, European Research Executive Agency
(REA), or the European Cybersecurity Competence Centre. Neither
the European Union, the granting authority, nor the European Cy-
bersecurity Competence Centre can be held responsible for them.

IMC ’26, October 12–16, 2026, Karlsruhe, Germany Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Nicolas Kourtellis, Evangelos Markatos
References
[1] Advertising Standards Authority. 2023. Recognising ads: Advertisement fea-
tures. https://www .asa.org.uk/advice-online/recognising-ads-advertisement-
features.html.
[2] Muhammad Ali, Angelica Goetzen, Alan Mislove, Elissa M Redmiles, and Pi-
otr Sapiezynski. 2023. Problematic Advertising and its Disparate Exposure on
Facebook. In32nd USENIX Security Symposium (USENIX Security 23). USENIX
Association, Anaheim, CA, 5665–5682. https://www .usenix.org/conference/
usenixsecurity23/presentation/ali
[3] Michelle A Amazeen and Bartosz W Wojdynski. 2019. Reducing Native Adver-
tising Deception: Revisiting the Antecedents and Consequences of Persuasion
Knowledge in Digital News Contexts.Mass Communication and Society22, 2
(2019), 222–247.
[4] Michelle A Amazeen and Bartosz W Wojdynski. 2020. The effects of disclosure
format on native advertising recognition and audience perceptions of legacy and
online news publishers.Journalism21, 12 (2020), 1965–1984.
[5] Waqar Aqeel, Balakrishnan Chandrasekaran, Anja Feldmann, and Bruce M.
Maggs. 2020. On Landing and Internal Web Pages: The Strange Case of Jekyll and
Hyde in Web Performance Measurement. InProceedings of the ACM Internet Mea-
surement Conference(Virtual Event, USA)(IMC ’20). Association for Computing
Machinery, New York, NY, USA, 680–695. doi:10.1145/3419394.3423626
[6] Kyle Asquith and Emily M Fraser. 2020. A critical analysis of attempts to regulate
native advertising and influencer marketing.International Journal of Communi-
cation14 (2020), 21.
[7] Australian Competition and Consumer Commission. 2016. Avoiding
unfair business practices: A Guide for Businesses and Legal Practi-
cioners. https://www .accc.gov.au/system/files/Avoiding%20unfair%20business%
20practices.pdf.
[8] Kristina Auxtova and Mary Brennan. 2025. Offensive and Harmful Advertising:
A Content Analysis of Official Complaints.Journal of Nonprofit & Public Sector
Marketing37, 1 (2025), 31–57.
[9] Muhammad Ahmad Bashir, Sajjad Arshad, and Christo Wilson. 2016. "Rec-
ommended For You": A First Look at Content Recommendation Networks. In
Proceedings of the 2016 Internet Measurement Conference(Santa Monica, Califor-
nia, USA)(IMC ’16). Association for Computing Machinery, New York, NY, USA,
17–24. doi:10.1145/2987443.2987469
[10] Joydeep Bhattacharya. 2025. Latest Ad Blocking Statistics for 2025: Current
Studies. https://seosandwitch.com/new-ad-blocking-stats/.
[11] Marzieh Bitaab, Alireza Karimi, Zhuoer Lyu, Adam Oest, Dhruv Kuchhal, Muham-
mad Saad, Gail-Joon Ahn, Ruoyu Wang, Tiffany Bao, Yan Shoshitaishvili, et al.
2025. SCAMMAGNIFIER: Piercing the Veil of Fraudulent Shopping Web-
site Campaigns. InProceedings of the NDSS Symposium 2025. Internet Society.
doi:10.14722/ndss.2025.230763
[12] Brave Software. 2026. Brave’s Rust-based adblock engine. https://github .com/
brave/adblock-rust.
[13] Disconnect. 2025. Tracker Protection lists. https://disconnect .me/
trackerprotection.
[14] DuckDuckGo. 2020. DuckDuckGo Tracker Radar Exposes Hidden Tracking.
https://spreadprivacy.com/duckduckgo-tracker-radar/.
[15] Laura Edelson, Tobias Lauinger, and Damon McCoy. 2020. A Security Analysis
of the Facebook Ad Library. In2020 IEEE Symposium on Security and Privacy (SP).
IEEE, IEEE, 661–678. doi:10.1109/SP40000.2020.00084
[16] European Union. 2005. Unfair Commercial Practices Directive. https://eur-
lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32005L0029.
[17] James Fallows. 2013. The Scientology Ad. https://www.theatlantic.com/national/
archive/2013/01/the-scientology-ad/267198/.
[18] Federal Trade Commission. 2015. Native Advertising: A Guide for Busi-
nesses. https://www .ftc.gov/business-guidance/resources/native-advertising-
guide-businesses.
[19] András Fittler, Péter Paczolai, Amir Reza Ashraf, Amir Pourhashemi, and Péter
Iványi. 2022. Prevalence of Poisoned Google Search Results of Erectile Dysfunc-
tion Medications Redirecting to Illegal Internet Pharmacies: Data Analysis Study.
Journal of Medical Internet Research24, 11 (2022), e38957. doi:10.2196/38957
[20] Arian Ghotbi. 2024. The Advertorial: A New Trend In Digital Advertis-
ing. https://www .forbes.com/councils/forbescoachescouncil/2025/05/16/ai-cant-
replace-your-leadership-skills/.
[21] Colin M. Gray, Yubo Kou, Bryan Battles, Joseph Hoggatt, and Austin L. Toombs.
2018. The Dark (Patterns) Side of UX Design. InProceedings of the 2018 CHI
Conference on Human Factors in Computing Systems(Montreal QC, Canada)
(CHI ’18). Association for Computing Machinery, New York, NY, USA, 1–14.
doi:10.1145/3173574.3174108
[22] Jamie L Grigsby. 2020. Fake ads: The influence of counterfeit native ads on brands
and consumers.Journal of Promotion Management26, 4 (2020), 569–592.
[23] Catherine Han, Deepak Kumar, and Zakir Durumeric. 2022. On the Infrastructure
Providers That Support Misinformation Websites. InProceedings of the Interna-
tional AAAI Conference on Web and Social Media(Atlanta, Georgia, USA), Vol. 16.
AAAI Press, Palo Alto, California, USA, 287–298. doi:10 .1609/icwsm.v16i1.19292
[24] Scott Hollenbeck and Andy Newton. 2021.Registration Data Access Protocol
(RDAP) Query Format. Technical Report 9082. doi:10.17487/RFC9082
[25] Hen-Hsen Huang, Yu-Wei Wen, and Hsin-Hsi Chen. 2017. Detection of False
Online Advertisements with DCNN. InProceedings of the 26th International Con-
ference on World Wide Web Companion(Perth, Australia)(WWW ’17 Companion).
International World Wide Web Conferences Steering Committee, Republic and
Canton of Geneva, CHE, 795–796. doi:10.1145/3041021.3054233
[26] TonTon Hsien-De Huang, Chia-Mu Yu, and Hung-Yu Kao. 2017. Data-Driven
and Deep Learning Methodology for Deceptive Advertising and Phone Scams
Detection. In2017 Conference on Technologies and Applications of Artificial In-
telligence (TAAI)(Taipei, Taiwan). IEEE, IEEE, New York, NY, USA, 166–171.
doi:10.1109/TAAI.2017.30
[27] Umar Iqbal, Zubair Shafiq, and Zhiyun Qian. 2017. The ad wars: retrospec-
tive measurement and analysis of anti-adblock filter lists. InProceedings of
the 2017 Internet Measurement Conference(London, United Kingdom)(IMC
’17). Association for Computing Machinery, New York, NY, USA, 171–183.
doi:10.1145/3131365.3131387
[28] Levi Kaplan, Nicole Gerzon, Alan Mislove, and Piotr Sapiezynski. 2022. Mea-
surement and analysis of implied identity in ad delivery optimization. InPro-
ceedings of the 22nd ACM Internet Measurement Conference(Nice, France)(IMC
’22). Association for Computing Machinery, New York, NY, USA, 195–209.
doi:10.1145/3517745.3561450
[29] Katalys Content Team. 2024. The Complete Guide to Writing Effective Adverto-
rials. https://katalys.com/growth/advertorials/.
[30] Erin Kenneally and David Dittrich. 2012. The Menlo Report: Ethical Principles
Guiding Information and Communication Technology Research.A vailable at
SSRN 2445102(2012).
[31] Amin Kharraz, William Robertson, and Engin Kirda. 2018. Surveylance: Auto-
matically Detecting Online Survey Scams. In2018 IEEE Symposium on Security
and Privacy (SP). IEEE, IEEE, 70–86. doi:10.1109/SP.2018.00044
[32] Sunny Jung Kim and Jeffrey T Hancock. 2017. How Advertorials Deactivate
Advertising Schema: MTurk-Based Experiments to Examine Persuasion Tactics
and Outcomes in Health Advertisements.Communication Research44, 7 (2017),
1019–1045.
[33] Satwik Ram Kodandaram, Mohan Sunkara, Sampath Jayarathna, and Vikas Ashok.
2023. Detecting Deceptive Dark-Pattern Web Advertisements for Blind Screen-
Reader Users.Journal of Imaging9, 11 (2023), 239.
[34] Platon Kotzias, Michalis Pachilakis, Javier Aldana Iuit, Juan Caballero, Iskander
Sanchez-Rola, and Leyla Bilge. 2025. Ctrl+Alt+Deceive: Quantifying User Expo-
sure to Online Scams. InProceedings of the Network and Distributed System Security
Symposium (NDSS). Internet Society. https://www .ndss-symposium.org/ndss-
paper/ctrlaltdeceive-quantifying-user-exposure-to-online-scams/
[35] Platon Kotzias, Kevin Roundy, Michalis Pachilakis, Iskander Sanchez-Rola, and
Leyla Bilge. 2023. Scamdog Millionaire: Detecting E-commerce Scams in the
Wild. InProceedings of the 39th Annual Computer Security Applications Conference
(Austin, TX, USA)(ACSAC ’23). Association for Computing Machinery, New York,
NY, USA, 29–43. doi:10.1145/3627106.3627184
[36] Victor Le Pochat, Tom Van Goethem, Samaneh Tajalizadehkhoob, Maciej Ko-
rczyński, and Wouter Joosen. 2019. Tranco: A Research-Oriented Top Sites
Ranking Hardened Against Manipulation. InNetwork and Distributed System
Security Symposium (NDSS 2019). Internet Society. doi:10 .14722/ndss.2019.23386
[37] Hao-Ping Hank Lee, Jacob Logas, Stephanie Yang, Zhouyu Li, Natã Barbosa, Yang
Wang, and Sauvik Das. 2023. When and Why Do People Want Ad Targeting
Explanations? Evidence from a Four-Week, Mixed-Methods Field Study. In2023
IEEE Symposium on Security and Privacy (SP). IEEE, IEEE, 2903–2920. doi:10.1109/
SP46215.2023.10179452
[38] Dirk Lewandowski, Friederike Kerkmann, Sandra Rümmele, and Sebastian Sün-
kler. 2018. An empirical investigation on search engine ad disclosure.Journal of
the Association for Information Science and Technology69, 3 (2018), 420–437.
[39] Xigao Li, Amir Rahmati, and Nick Nikiforakis. 2024. Like, Comment, Get
Scammed: Characterizing Comment Scams on Media Platforms. InProceedings
of the NDSS Symposium 2024. Internet Society. doi:10.14722/ndss.2024.24060
[40] Sylvain Lugeon, Tiziano Piccardi, and Robert West. 2022. Homepage2Vec:
Language-Agnostic Website Embedding and Classification. InProceedings of
the International AAAI Conference on Web and Social Media. AAAI Press, Palo
Alto, California, USA.
[41] Shang Ma, Chaoran Chen, Shao Yang, Shifu Hou, Toby Jia-Jun Li, Xusheng
Xiao, Tao Xie, and Yanfang Ye. 2025. Careful About What App Promotion Ads
Recommend! Detecting and Explaining Malware Promotion via App Promotion
Graph. InProceedings of the NDSS Symposium 2025. Internet Society. doi:10.14722/
ndss.2025.230051
[42] Joyce Manalo. 2025. A Brief History of Native Advertising. https://contently.com/
2014/03/28/a-brief-history-of-native-advertising/.
[43] Arunesh Mathur, Arvind Narayanan, and Marshini Chetty. 2018. Endorsements
on Social Media: An Empirical Study of Affiliate Marketing Disclosures on
YouTube and Pinterest.Proceedings of the ACM on Human-Computer Interaction
2, CSCW, Article 119 (Nov. 2018), 26 pages. doi:10.1145/3274388
[44] Scott McCoy, Andrea Everard, Dennis Galletta, and Peter Polak. 2004. A Study
of the Effects of Online Advertising: A Focus on Pop-Up and In-Line Ads. In2004

Paid to Look Like Truth: The Prevalence and Dark Patterns of Advertorials in News Outlets IMC ’26, October 12–16, 2026, Karlsruhe, Germany
Proceedings of the SIGCHI Conference on Human Factors in Computing Systems
(SIGCHI ’04).
[45] MDN Web Docs Contributors. 2026. Use data attributes. https://
developer.mozilla.org/en-US/docs/Web/HTML/How_to/Use_data_attributes.
[46] Amanda Meade. 2025. Nothing to see here, Press Council says after News
Corp tabloids’ front-page undisclosed advertorial gassing up fossil fuel.
https://www.theguardian.com/media/2025/apr/17/no-breach-found-after-
news-corp-tabloids-splashed-on-undisclosed-advertorial-gassing-up-fossil-
fuel-ntwnfb.
[47] Merriam-Webster.com Dictionary. 2025. Advertorial. https://www .merriam-
webster.com/dictionary/advertorial.
[48] Abraham Mhaidli, Shwetha Rajaram, Selin Fidan, Gina Herakovic, and Florian
Schaub. 2024. Shockvertising, Malware, and a Lack of Accountability: Exploring
Consumer Risks of Virtual Reality Advertisements and Marketing Experiences.
IEEE Security & Privacy22, 1 (2024), 43–52. doi:10.1109/MSEC.2023.3332105
[49] Zahra Moti, Asuman Senol, Hamid Bostani, Frederik Zuiderveen Borgesius,
Veelasha Moonsamy, Arunesh Mathur, and Gunes Acar. 2024. Targeted and
Troublesome: Tracking and Advertising on Children’s Websites. In2024 IEEE
Symposium on Security and Privacy (SP). IEEE, IEEE, 1517–1535. doi:10 .1109/
SP54263.2024.00118
[50] Midas Nouwens, Rolf Bagge, Janus Bager Kristensen, and Clemens Nylandsted
Klokmose. 2022. Consent-O-Matic: Automatically Answering Consent Pop-
ups Using Adversarial Interoperability. InExtended Abstracts of the 2022 CHI
Conference on Human Factors in Computing Systems(New Orleans, LA, USA)(CHI
EA ’22). Association for Computing Machinery, New York, NY, USA, Article 238,
7 pages. doi:10.1145/3491101.3519683
[51] Michalis Pachilakis, Panagiotis Papadopoulos, Nikolaos Laoutaris, Evangelos P.
Markatos, and Nicolas Kourtellis. 2022. YourAdvalue: Measuring Advertising
Price Dynamics without Bankrupting User Privacy. InAbstract Proceedings of
the 2022 ACM SIGMETRICS/IFIP PERFORMANCE Joint International Conference
on Measurement and Modeling of Computer Systems(Mumbai, India)(SIGMET-
RICS/PERFORMANCE ’22). Association for Computing Machinery, New York, NY,
USA, 41–42. doi:10.1145/3489048.3522629
[52] Emmanouil Papadogiannakis. 2026. Open-Source Data. https://gitlab .com/
papamano/advertorials-data.
[53] Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Evangelos P. Markatos,
and Nicolas Kourtellis. 2024. Ad Laundering: How Websites Deceive Advertisers
into Rendering Ads Next to Illicit Content. InCompanion Proceedings of the ACM
Web Conference 2024(Singapore, Singapore)(WWW ’24). Association for Com-
puting Machinery, New York, NY, USA, 782–785. doi:10.1145/3589335.3651466
[54] Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Evangelos P. Markatos,
and Nicolas Kourtellis. 2022. Leveraging Google’s Publisher-Specific IDs to Detect
Website Administration. InProceedings of the ACM Web Conference 2022(Virtual
Event, Lyon, France)(WWW ’22). Association for Computing Machinery, New
York, NY, USA, 2522–2531. doi:10.1145/3485447.3512124
[55] Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Evangelos P. Markatos,
and Nicolas Kourtellis. 2023. Who Funds Misinformation? A Systematic Analysis
of the Ad-related Profit Routines of Fake News Sites. InProceedings of the ACM
Web Conference 2023(Austin, TX, USA)(WWW ’23). Association for Computing
Machinery, New York, NY, USA, 2765–2776. doi:10.1145/3543507.3583443
[56] Enric Pujol, Oliver Hohlfeld, and Anja Feldmann. 2015. Annoyed Users: Ads
and Ad-Block Usage in the Wild. InProceedings of the 2015 Internet Measurement
Conference(Tokyo, Japan)(IMC ’15). Association for Computing Machinery, New
York, NY, USA, 93–106. doi:10.1145/2815675.2815705
[57] Caitlin M Rivers and Bryan L Lewis. 2014. Ethical research standards in a world
of big data.F1000Research3 (2014), 38. doi:10.12688/f1000research.3-38.v2
[58] Cece Serino. 2025. Did You Know? 70% of Consumers Prefer to
Learn About a Brand Through Articles Rather Than Ads! https:
//www.willowandsagemarketing.com/post/70-of-consumers-prefer-to-
learn-about-a-brand-through-articles-rather-than-ads.
[59] Jeff Sexton. 2023. Learning from the Legends — MacManus and The Penalty of
Leadership. https://wizardofads .org/learning-from-the-legends-macmanus-and-
the-penalty-of-leadership/.
[60] Sharethrough. 2013. Consumers Look At Native Ads More Than Display,
According To New Sharethrough Study. https://medium.com/nativeadvertising/
consumers-look-at-native-ads-more-than-display-according-to-new-study-
764843bd771d.
[61] Similarweb LTD. 2025. Similarweb: AI-Powered Digital Data Intelligence Solu-
tions. https://www.similarweb.com/.
[62] Monique Solomons. 2023. 130 advertising statistics: trends, automation, and
marketing strategies. https://www.linearity.io/blog/advertising-statistics/.
[63] Stijn Tilborghs. 2022. Flagging 13 Million Malicious Domains in 1 Month with
Newly Observed Domains. https://www .akamai.com/blog/security-research/
newly-observed-domains-discovered-13-million-malicious-domains.
[64] United Nations Statistics Division. 2025. Standard country or area codes for
statistical use (M49). https://unstats.un.org/unsd/methodology/m49/.
[65] Annie Wissner. 2019. What is a good CPM? Why cheap CPMs aren’t always the
best. https://choozle.com/blog/what-is-a-good-cpm/.
[66] World Wide Web Consortium (W3C). 2025. Contrast (Minimum) (Level AA).
https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.
[67] Ahsan Zafar and Anupam Das. 2025. Assessing Compliance in Digital Advertising:
A Deep Dive into Acceptable Ads Standards. InProceedings of the ACM on Web
Conference 2025(Sydney NSW, Australia)(WWW ’25). Association for Computing
Machinery, New York, NY, USA, 1536–1547. doi:10.1145/3696410.3714725
[68] Ines Zelch, Matthias Hagen, and Martin Potthast. 2023. Commercialized Gen-
erative AI: A Critical Study of the Feasibility and Ethics of Generating Native
Advertising Using Large Language Models in Conversational Web Search.arXiv
preprint arXiv:2310.04892(2023).
[69] Eric Zeng, Tadayoshi Kohno, and Franziska Roesner. 2020. Bad news: Click-
bait and deceptive ads on news and misinformation websites. InWorkshop on
Technology and Consumer Protection. 1–11.
[70] Eric Zeng, Tadayoshi Kohno, and Franziska Roesner. 2021. What Makes a “Bad”
Ad? User Perceptions of Problematic Online Advertising. InProceedings of the
2021 CHI Conference on Human Factors in Computing Systems(Yokohama, Japan)
(CHI ’21). Association for Computing Machinery, New York, NY, USA, Article
361, 24 pages. doi:10.1145/3411764.3445459
[71] Eric Zeng, Rachel McAmis, Tadayoshi Kohno, and Franziska Roesner. 2022. What
factors affect targeting and bids in online advertising? a field measurement study.
InProceedings of the 22nd ACM Internet Measurement Conference(Nice, France)
(IMC ’22). Association for Computing Machinery, New York, NY, USA, 210–229.
doi:10.1145/3517745.3561460
[72] Eric Zeng, Miranda Wei, Theo Gregersen, Tadayoshi Kohno, and Franziska Roes-
ner. 2021. Polls, clickbait, and commemorative $2 bills: problematic political
advertising on news and media websites around the 2020 U.S. elections. In
Proceedings of the 21st ACM Internet Measurement Conference(Virtual Event)
(IMC ’21). Association for Computing Machinery, New York, NY, USA, 507–525.
doi:10.1145/3487552.3487850
[73] Penghui Zhang, Adam Oest, Haehyun Cho, Zhibo Sun, RC Johnson, Brad Ward-
man, Shaown Sarker, Alexandros Kapravelos, Tiffany Bao, Ruoyu Wang, Yan
Shoshitaishvili, Adam Doupé, and Gail-Joon Ahn. 2021. CrawlPhish: Large-scale
Analysis of Client-side Cloaking Techniques in Phishing. In2021 IEEE Symposium
on Security and Privacy (SP). IEEE, 1109–1124. doi:10.1109/sp40001.2021.00021
A Ad Detection Filter Lists
We utilize the filter lists from EasyList and uBlock Origin for ad
detection. Following the methodology of [55], we use these lists to
identify ads in URLs extracted from rendered pages and network
traffic. We additionally extend this approach to identify ads based
on their representation in the rendered DOM. We download both
lists on October 7, 2024 (EasyList commit 3835a34, uBlock Origin
release 1.60.0). We use filter list versions that differ from those
employed in [55] in order to follow the latest ad rules. The filter
lists contain both network filtering rules and cosmetic rules (also
referred to as content rules). Cosmetic rules identify page elements
that should be hidden or modified based on properties of the HTML
element, such as its ID or class, as well as CSS selectors. As in [55],
we make use of the Brave ad-blocking engine [12] to enforce these
rules. Although EasyList and uBlock Origin use slightly different
syntactic conventions, their filtering rules follow largely similar
syntax and are parsed and applied by the ad-blocking engine. Finally,
we respect and apply exceptions for specific domains defined by the
filter lists, ensuring that rules are not applied to unrelated domains.
For cosmetic filtering, we traverse the entire DOM tree of each
rendered page and test each element against the cosmetic rules
from the EasyList and uBlock Origin filter lists. For each element
that matches a cosmetic rule, we examine whether the element
or an associated child element contains a clickable URL. If so, we
classify the element as an ad and collect the corresponding URL.
This complements the network and URL-based detection employed
in [55] by allowing us to detect ads whose presence is identifiable
from the rendered page structure.

IMC ’26, October 12–16, 2026, Karlsruhe, Germany Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Nicolas Kourtellis, Evangelos Markatos
Figure 14: Example of a traditional anti-wrinkle cream ad
using a direct persuasive approach, highlighting benefits and
encouraging purchase with concise text.
Figure 15: Example of an advertorial for an anti-aging serum,
written in a conversational, informative style and narrating
a personal story to promote the product.
ScamValidatorSuspicious
ScamAdviserScore
ScamValidatorMalware
LandingPageContentSize
ZscalerContentSize
LandingPageBodySize
ScamValidatorPhishing
ZscalerStatusCode
ScamValidatorScore
ScamValidatorSpam
GetSafeOnlineLabel
CyrenCategory
CyrenIsBadCategory
NortonSafewebFlag
ScamAdviserLabel
MywotScore
VirusT otalHarmless
TrendMicroLabel
MywotLabel
KasperskyHits
T alosReputation
VirusT otalUndetected
ZscalerScore
ScamDocClass
SucuriRiskRating
MaltiverseLabel
LandingPageStatus
KasperskyFlag
VirusT otalMalicious
UrlVoidHits
GetSafeOnlineDNSFilter
GetSafeOnlineIqGlobal
ZscalerLabel
VirusT otalSuspicious
GetSafeOnlinePulsedive
FortiguardIsBadCategory
GetSafeOnlineQuad9
NortonSafewebReviews
BlacklistAlertHits
NortonSafewebScore
T alosBlocklist
SpamhausHasIssues
SucuriInBlacklist
ScamGuardHits
VirusT otalTimeout
0.00
0.02
0.04
0.06
0.08
0.10Gini Importance
Threshold
Importance
Figure 16: Feature importance of the trained machine learn-
ing model for misleading website detection. Feature impor-
tance is measured via Gini impurity with 24 features being
retained, capturing 96% of the total importance.
B Ethics
This research was conducted in accordance with recognized eth-
ical standards and protocols for information studies [ 30, 57]. In
compliance with the GDPR and ePrivacy regulations, we do not
collect or process personal information of real users. We purpose-
fully configure our crawling systems to emulate the behavior of
real users, ensuring that all automated actions are rate-limited and
unobtrusive. Our system waits until the page fully loads, scrolls
and navigates through the website at a natural pace, and waits
for up to one minute before proceeding to the next webpage. Fi-
nally, we make a conscious effort to avoid impacting the advertising
ecosystem. We only click on each ad URL only once, and consid-
ering the thousands of distinct advertisers we identify (Section 4),
the 5-month duration of our analysis (Section 3.1), and the low
cost per thousand ad impressions [51], we believe our activity did
not meaningfully deplete any advertiser budgets. This approach is
consistent with prior work that has employed similar ad-clicking
methodologies to study advertising ecosystems. [72] acknowledges
the potential for minor financial impact due to impression- or click-
based pricing models, but empirically estimates the resulting costs
to be negligible at scale, particularly when distributed across a large
number of advertisers.
C Advertorial Linguistic Tone
Advertorials differ from traditional advertisements in both tone and
style. While regular ads are direct and promotional, advertorials
utilize a more informative or editorial voice, often resembling news
articles or feature stories. This approach engages the reader by
providing useful content or storytelling, subtly weaving in the
product or service rather than overtly selling it. We demonstrate the
distinctive difference of advertorials in Figures 14 and 15 where two
similar products (an anti-wrinkle cream and an anti-aging serum)
are promoted using different techniques. In Figure 14 the traditional
ad takes a direct persuasive approach. It focuses on highlighting
the benefits of the cream and urges the audience to buy the product
with concise text (i.e., “ADD TO CART”). On the other hand, the
advertorial of Figure 15, has a more conversational and informative
style. It reads like an article telling the emotional story of a woman
who suffered facial damage, only to be saved by the promoted
product. This journalistic tone is a fundamental characteristic of
advertorials and was one of the factors that helped annotators reach
a decision in the formation of the original dataset, as described in
Section 3.3. To maintain ethical integrity and academic neutrality, all
visible brand names and logos in the advertising screenshots have
been blurred. This prevents unintended promotion or endorsement
and avoids potential reputational implications for the depicted
companies.
D Security Web Engines
In order to discover websites that can mislead or deceive users, we
extract information from 19 independent security, safety and analyt-
ics Web engines (Section 3.3). The engines utilized in this work are
(in alphabetic order): (1) Blacklist Alert, (2) Cyren, (3) Fortiguard,
(4) GetSafeOnline, (5) Kaspersky, (6) Maltiverse, (7) MyWOT, (8)
Norton SafeWeb, (9) ScamAdviser, (10) Scamdoc, (11) ScamGuard,

Paid to Look Like Truth: The Prevalence and Dark Patterns of Advertorials in News Outlets IMC ’26, October 12–16, 2026, Karlsruhe, Germany
Figure 17: Example of a low-contrast disclaimer text in an
online advertorial discovered in this study.
Figure 18: Example of disclaimer in an online advertorial.
The disclaimer appears in a font size significantly smaller
than the surrounding editorial text.
(12) Scam Validator, (13) Spamhaus, (14) Sucuri, (15) Talos Intel-
ligence, (16) Trend Micro, (17) URLVoid, (18) VirusTotal, and (19)
Zscaler. Each web engine provides raw data relevant to the target
domain, which is then preprocessed to extract meaningful features.
The raw data from these sources are standardized and transformed
through a series of steps including cleaning, normalization and
encoding to generate a comprehensive feature set. To better under-
stand the decision-making process of our model, we compute the
feature importance values using Gini impurity and a random forest
classifier. Figure 16 presents the ranking of features according to
their contribution to the model’s classification performance. We
observe that features coming from engines focusing on scam de-
tection (i.e., Scam Validator, ScamAdviser) are the most important
when detecting misleading websites. Additionally, the content size
of the landing page is a significant feature since it can be associated
with malicious intent (Section 5.2). The feature selection process
retains only features with meaningful contribution to classification,
aiming to reduce noise and redundancy while preserving meaning-
ful information. The final training dataset consists of 24 features
derived from the Web engines.
E Examples of Dark Patterns
Users often rely on visual and textual signals in order to differentiate
between editorial and commercial content and that’s why regula-
tion explicitly requires that disclaimers are readily identifiable to
indicate the promotional nature of content. Figure 17 provides a
real-world example of theLow-Contrastdark pattern. In this exam-
ple, the disclaimer text is displayed in a color that closely matches
the background, making it harder to detect during casual browsing.
The text and background are both in slightly different shades of
gray, increasing the possibility that users will overlook the fact
they are reading an advertisement and not editorial content. Next,
Figure 18 illustrates how advertorials often present the disclaimer
text in a significantly smaller font than the surrounding editorial
text. Users scanning the page may miss the label entirely due to
its reduced size and placement at the bottom of the screen, prac-
tically turning disclaimers into the “fine print”. Both patterns can
be regarded as dark patterns because they deliberately reduce the
visibility of legally important information (i.e., disclaimers).
