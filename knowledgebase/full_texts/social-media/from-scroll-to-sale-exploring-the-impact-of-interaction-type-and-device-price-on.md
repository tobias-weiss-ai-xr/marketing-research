---
title: 'From Scroll to Sale: Exploring the Impact of Interaction Type and Device Price on TikTok Advertisements'
url: https://arxiv.org/abs/2610.00684
category: social-media
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Nazanin Sabri
- Cat Mai
- Haodi Zou
- Isha Varada
- Damon McCoy
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.00684
pages: 18
chars: 74852
fetched_at: '2026-11-08T13:12:47+00:00'
kb_version: 1
---

# From Scroll to Sale: Exploring the Impact of Interaction Type and Device Price on TikTok Advertisements

From Scroll to Sale: Exploring the Impact of Interaction Type
and Device Price on TikTok Advertisements
Nazanin Sabri1, Cat Mai2, Haodi Zou1, Isha Varada1, Damon McCoy2, Deepak Kumar1, Kristen
Vaccaro1
1University of California San Diego
2New York University
{nsabri, h4zou, ivarada, d1kumar, kvaccaro}@ucsd.edu,{cat.mai, mccoy}@nyu.edu
Abstract
Companies and brands increasingly use dynamic pricing, in-
cluding targeting social media ads to users based on their in-
come. In this work we audit TikTok’s feed using 56 auto-
mated accounts, which collect data on over 80,000 videos,
across two studies. We test the impact of device price on ad
load and ad types, using 12 phones of low ($0-$250), medium
($400-$650), and high ($750-$1,000+) price as a proxy for
income. We also test the impact of interaction type (i.e., like,
comment, share), age, and gender on the frequency and con-
tent of ads. Overall, the ad load was 29.4%, but liking and
sharing content increased ad load significantly. We also found
that as accounts spend more time on TikTok, the ad load
steadily increases. We found some evidence that device price
impacts both ad load and content — more expensive devices
were targeted with fewer ads, while the least expensive de-
vices received more discounts.
1 Introduction
A recent TikTok video went viral after accusing retailers of
changing in store prices in real time (Sakina 2025). But on-
line this kind of dynamic pricing is already entrenched. Air-
lines and hotels, for example, have used dynamic pricing to
manage demand in online reservations for decades (McAfee
2008; Federal Trade Commission 2025; Mattioli 2012).
Companies argue that dynamic pricing allows motivated
consumers to seek out the best deals (Patterson, Laidlaw, and
Zhang 2025; McAfee 2008). However, this creates a risk that
low-income shoppers will face higher prices or lower qual-
ity goods when sellers believe they have less power to walk
away (Pacheco and Ramachandran 2019).
In this study, we examine the extent to which TikTok ad-
vertisements target users differentially based on income. De-
spite the large volume of work studying targeted advertising,
including its impacts on job opportunities, political informa-
tion, and the reach of scams, the focus has remained primar-
ily on demographics like age, race, and gender (Imana, Ko-
rolova, and Heidemann 2021; Ali et al. 2023; Silva et al.
2020). Short-form video platforms have also rarely been
the focus of advertising audits (Kaplan and Sapiezynski
2024; Min and Kim 2025), despite their increasing popu-
larity (Boeker and Urman 2022). The only study of targeted
Copyright © 2026, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
advertising on TikTok examined the impact of other demo-
graphics, specifically age and gender, on the kind of ads that
users are shown (Kaplan and Sapiezynski 2024). Our study
contributes the first measurement of the impact of income on
the volume, content, and prices of targeted advertisements.
Before studying the impact of income and other user
demographics, however, it is necessary to understand the
effects of engagement on ad load. Both on TikTok and
other platforms, users’ engagement with their feeds have
been shown to shape the content they subsequently en-
counter (Germano, G ´omez, and Sobbrio 2026; Shin and
Jitkajornwanich 2024). This phenomenon, however, has not
been studied for advertisements. This leads to our first
research question:RQ1: How does interaction type (i.e.,
scrolling, liking, commenting, sharing) affect the number
and content of ads?
Next, we focus on the impact of income. Marketing firms
have noted the value of targeting advertisements based on
income or wealth (John, Shobayo, and Ogunleye 2023), so
we examine the extent to which that is currently practiced
in targeted advertising campaigns on TikTok. While TikTok
offers an “About This Ad” explanation for each ad (TikTok
2022), prior work has shown that up to 40% of TikTok’s ex-
planations are incorrect (Mousavi, Gummadi, and Zannettou
2024). Instead, we opt to directly measure the impact of in-
come, which we experimentally vary using device price as a
proxy, on the number and type of ads shown. This forms our
second research question:RQ2: How does income affect the
number and content of ads?
Finally, age and gender are among the most commonly
exploited demographic signals in targeted advertising (Oko-
roafo, Koh, and Gammoh 2010). Prior work on other online
spaces has shown gender disparities in ad targeting (Imana,
Korolova, and Heidemann 2021; Lambrecht and Tucker
2019; Ali et al. 2023). This evidence from similar platforms
motivates our last research question:RQ3: How do age and
gender affect the number and content of ads?
To answer these questions, we performed two paired stud-
ies using an automated system to view, interact with, and
record TikTok content. Our first study tested four interaction
types (scroll, like, comment, and share) to identify whether
any interactions increased the ad load. Using 32 automated
accounts, we collected data on 42,819 videos. Overall, the
ad loadwas 29.4%. However, some more active forms of
arXiv:2610.00684v1  [cs.CY]  30 Sep 2026

engagement (liking and sharing) dramatically increased ad
load, up to 37.6% of the videos encountered. Surprisingly,
commenting did not lead to the same effect — in fact, the
platform seemed to treat frequently commenting very differ-
ently from all other forms of interaction.
Our second study tested the impact of device price (as
a proxy for income) and demographics (age and gender) on
the number and type of ads shown, to answerRQ2andRQ3.
To test device price, we used 12 phones, with prices rang-
ing from $80–$1,000. To test demographics, we created ac-
counts with two ages (26 and 46) and two genders, suggested
through the choice of account name. The 24 automated ac-
counts in Study 2 more closely emulated real user interac-
tions, based on interaction patterns obtained from TikTok
user data donations (Zannettou et al. 2023), eventually col-
lecting data on 37,350 videos. We found that our most ex-
pensive phone had the lowest ad load, but the least expensive
device received the largest discounts.
These findings suggest important implications for the ad
ecosystem, for example, that users who do not have the
means or desire to purchase more expensive devices may
face a higher advertisement burden, with ads taking up more
of their time and attention. However, the importance of in-
teractions, relative to demographic attributes, suggests ways
for everyday users to exert more power over what they see.
2 Related Work
Algorithmic feeds — like TikTok’s “For You” page or Insta-
gram’s “Explore” feed — are integral parts of modern social
media. These feeds rely on a content recommendation algo-
rithm that match users with content they might enjoy seeing.
However, these algorithms are usually not made visible nor
transparent to end-users (Mosnar et al. 2025; Edelson, Hau-
gen, and McCoy 2025). Given the prevalence of these plat-
forms and the high impact they can have, researchers (Bandy
2021) and regulators (European Commission 2023; Blumen-
thal et al. 2023) have become increasingly interested in au-
diting social media platforms.
Social Media AuditsAlgorithm audits, defined as “meth-
ods that systematically probe algorithms and observe
their output to draw conclusions about their inner work-
ings” (Lam et al. 2022), have emerged as means of evaluat-
ing algorithms’ problematic behavior. Sandvig et al. (Sand-
vig et al. 2014) established foundational frameworks for
detecting algorithmic discrimination, proposing systematic
approaches to reveal hidden biases in automated decision-
making systems.
Audits of Ad DeliveryAudits have been performed on a
variety of functions of social media platforms; one impor-
tant function is targeted advertising. Given the black box na-
ture of ad targeting systems, they can result in unintended
outcomes. Studies have found that the final audience of an
ad can significantly differ from what the advertiser orig-
inally intended after ad delivery optimization (Lambrecht
and Tucker 2019; Asplund et al. 2020; Ali et al. 2023).
Industry white papers have reported that users prefer rele-
vant ads to generic ones (McKinsey 2021), though other re-
searchers have found that users find targeted ads creepy (Re-
itinger et al. 2024; Ur et al. 2012; Wei et al. 2020) and view
the behavioral tracking required for ad delivery optimization
unfavorably (Reitinger et al. 2024). Social media users find
that current transparency mechanisms are unhelpful in un-
derstanding their ad composition (Ur et al. 2012; Mousavi,
Gummadi, and Zannettou 2024) and attempts to filter out
unwanted ads are ineffective (Kaplan et al. 2026).
Prior work has examined how ad delivery can be influ-
enced by user’s demographics such as gender, race, or sex-
ual orientation (Ali et al. 2023; Kofman and Tobin 2019; As-
plund et al. 2020; Gak, Olojo, and Salehi 2022). In 2012, in-
vestigations revealed that the travel website Orbitz directed
Mac OS users toward higher-priced hotels by ranking these
properties higher in search results (Mattioli 2012). There is
also an emerging line of work estimating how valuable users
are and the resulting ads that they see (Caba˜nas, Cuevas, and
Cuevas 2018; Mai et al. 2025). Mai et al. showed that private
users, arguably less valuable to advertisers, received a much
higher ad load than when their less private counterparts. To
the best of our knowledge, no prior work has investigated the
relationship between both user’s device price and behavior
and the resulting ads they get on TikTok.
Audits of TikTokAudits of TikTok have utilized a va-
riety of methods such as sockpuppet accounts (Mousavi,
Gummadi, and Zannettou 2024), data donations (Yang et al.
2024), and analysis of network traffic (Kaplan et al. 2026).
Most studies have focused on video recommendations,
though some have considered elements like auto complete
search suggestions, where misinformation is common (Gu-
nasekara et al. 2025).
Prior audits of TikTok have found that age impacts ad-
vertisements, showing that ads shown to two adult ac-
counts (18 years old) were more similar to one another than
those shown to child accounts (13 years old) (Kaplan and
Sapiezynski 2024). However, the majority (83%) of videos
shown on a child’s recommendation feed are not child di-
rected (Figueira et al. 2025) and the mechanisms meant to
limit exposure to harmful content on youth accounts are only
minimally effective, with little difference between adult and
youth accounts (Xue et al. 2025).
Researchers have also studied TikTok’s explanations
for recommended videos, finding that a large number
of explanations provided for why a content was shown
was incompatible with the behavior of the automated ac-
count (Mousavi, Gummadi, and Zannettou 2024). For ex-
ample, an account that never commented, yet, was provided
the explanation “You commented on similar videos”.
Methodologically closely related to our work is (Boeker
and Urman 2022) which investigated the impacts of in-
teraction type on content recommendation. In order, the
most influential interactions were follow, like, and watch
rate (Boeker and Urman 2022). While this work focused on
content recommendations, we extend the analysis to adver-
tisements and add additional interaction types.

Experimental Conditions
Device Price Interaction Demographics
Study 1– 42,819 videos and 12,608 ads
$80†
Pixel 3a
Scroll
Like
Comment
Share
1980 Michael or Jennifer
2000 Jacob or Emily†
Study 2– 37,350 videos and 11,647 ads
$80
Pixel 3a
$499
Pixel 8
$924
Galaxy S26+
All† 1980 Michael or Jennifer
2000 Jacob or Emily
Table 1: Experimental design overview. Study 1 tested the
impact of different interaction types, while Study 2 tested
the impact of device price (i.e., wealth) and demographics.
†While all settings were required to collect data (e.g., ac-
counts cannot be created without an age and name), results
use data only from the respective studies.
3 Experimental Design
In order to understand the factors that impact the delivery of
advertisements on TikTok, we conducted an audit of the plat-
form through two paired studies. In our first study, we inves-
tigated how varying types of user engagement with recom-
mendation feeds impacted the number and content 1 of ads
they received. In our second study, we explored how adver-
tising exposure differed across low- and high-income users,
revealing potential disparities in nature and price of ads de-
livered to different socioeconomic groups. Table 1 summa-
rizes the experimental conditions.
The device price condition was selected as a proxy for in-
come, because prior work has shown that ad targeting based
on income could disadvantage lower-income individuals,
who may have less flexibility to seek out better alternatives
if higher prices are shown to them (Patterson, Laidlaw, and
Zhang 2025). Demographics such as age and gender have
long been used by marketers (Okoroafo, Koh, and Gammoh
2010), so accounts were created with different names and
dates of birth to assess how these identity markers shape the
ads users receive. Finally, the interaction type condition was
examined, as prior work has shown users’ engagement with
algorithmic feeds to influence the content they subsequently
encounter (Germano, G´omez, and Sobbrio 2026).
To perform the audit, we built a system to automatically
scroll, interact with, and record content on TikTok’s rec-
ommendation feed. After we (1) manually created accounts
1Content is operationalized as visual representations, brands,
and price and is described in detail in Dependent Variables.
with matched ages and gender, the automated tool for each
account (2) scrolled TikTok’s recommendation feed, (3) per-
formed different kinds of interactions, and (4) collected and
stored screenshots of all videos. An analysis pipeline then
(5) identified ads and (6) analyzed their content. Data collec-
tion for each setting was duplicated, to control for random-
ness in TikTok’s algorithm, i.e., we created two accounts
with the exact same name, age, and interaction behavior.
Concurrent data collection across over a dozen devices con-
trolled for marketing campaigns over time. The data ana-
lyzed throughout this study was collected between March
12 and April 25, 2026. In total, 80,169 TikTok videos were
encountered, 24,255 (30%) of which were advertisements.
While many audits using sock puppet accounts are not
considered human subjects research, we obtained IRB ap-
proval for this study. One experimental condition (the like
and comment interaction types) created opportunities for in-
teractions with human users of the platform, including both
perceptions by content creators and the fact that some of our
automatically generated comments received likes or replies
from other users. To minimize potential deception or harm,
our comments consisted only of randomly selected emojis.
3.1 Independent Variables
We modified interaction type, age, gender (proxied through
name), and income (proxied through device price) to answer
our research questions. Study 1 examined the effects of in-
teraction behavior on ad load 2, while Study 2 explored the
effects of income, age and gender.
Interaction BehaviorsHow users interact with their feeds
on TikTok – through watch time, likes, comments, and
shares – can strongly influence the content they are recom-
mended, as these engagement signals are used to infer user
interests and preferences (Boeker and Urman 2022). How-
ever, these were measurements of content recommendations,
so our study extended the measurement to advertising.
Five interaction types were examined: scroll, like, com-
ment, share, and all interactions combined. In the first study,
interactions were isolated by performing only one interac-
tion per account to identify their individual effects. The sec-
ond study combined interactions to better simulate more re-
alistic user behavior.
Interaction Times Throughout The DayEach account col-
lected TikTok content for 2:15–3 hours, aligning with es-
timates of average social media use (Geuens 2025). Usage
was distributed across multiple sessions, rather than a sin-
gle continuous period, to reflect habitual checking behaviors
throughout the day. This type of behavior, where users come
back to the application throughout the day, has been shown
in prior data donations of the platform (Yang et al. 2025).
Usage was spread across five sessions: a 45–60 minute pe-
riod in the morning, three randomly timed 15–20 minute ses-
sions during the day, and a 45–60 minute period at night.
The time of day and duration of the five interactions were
selected at random at the beginning of each day.
2Ad load is operationalized as the percentage of ads.

Interaction ProbabilityIn every experiment there was a 10%
chance of interacting with each video. The type of interac-
tion depended on the study and experimental condition.
Interaction TypesStudy 1 tested interaction types inde-
pendently (though all accounts populated new content by
scrolling). Scrolling served as the baseline condition, in
which content was only viewed and no engagement with
the feed occurred. View time was selected at random rang-
ing from 1 to 25 seconds. If a video was shorter than the
length selected it would loop until the program scrolled
past it. Re-watching content is not uncommon behaviors for
users (Baumgartner 2025).
The other interactions were: liking, commenting, and
sharing content. Follow was initially included within our ex-
perimental conditions, but was later removed from the study.
This is due to a follow-ban placed on the device running this
interaction. Manual attempts at following users on the origi-
nal account performing this interaction, as well as new ones
created, were unsuccessful.
Study 2 aimed to replicate more realistic interaction be-
havior. All accounts liked 93% of the time, commented 5%
of the time, and shared 2% of the time. These percentages
were based on real TikTok usage statistics reported in prior
work using data donations (Zannettou et al. 2023).
IncomeIncome could be used by advertisers to tailor cam-
paigns toward users with higher purchasing power. It might
also be used to present higher prices or lower-quality goods
to lower income users who may have limited flexibility in
their options (Patterson, Laidlaw, and Zhang 2025).
To understand how income might be used by marketers
to target ads, we evaluated the impact of device price, as a
proxy for income on ad targeting. TikTok’s advertising plat-
form includes device price as one of the parameters adver-
tisers can adjust, supporting the idea that this variable may
be used for ad targeting.
Devices from three price ranges tested the effects of
price on ads received. These price ranges were: $0-$250,
$400-$650, and $750-$1,000+, which according to the plat-
form have approximately equivalent audience size estimates.
Large price differences ($150) were placed between the
ranges to allow for differentiation. Appendix A provides au-
dience counts for each group.
AgeMarketers have emphasized the importance of tai-
loring marketing campaigns to specific age (Amazon Ads
2024; Fromm and Read 2018). To investigate the potential
effects of age on ad targeting on TikTok, we tested two age
values within our experiments: 26 and 46.
Age 26 was selected because it is within the largest adult
age group (i.e., 25-34) on TikTok in 2025 (Duarte 2026).
The second age, 46, was then selected because it enabled
comparison between ads served to younger and older adults
(through a 20 year age gap) without being too old, as Tik-
Tok’s adoption among those 55+ is low. All accounts require
age input. For all accounts, the birth dates were [Month]
[Day], 2000 and [Month] [Day], 1980, where month and day
were selected at random.
GenderPrior work on targeted advertising has shown that
gender targeting can substantially increase ad engagement.
For example, gender and interest targeted ads on Tum-
blr’s achieved a 20% lift in engagement compared to untar-
geted campaigns (Grbovic et al. 2015). However this type
of targeting could result in users of some genders being
targeted disproportionately with beauty or weight loss ad-
vertisements which could negatively impact their mental
health (Blaine and McElroy 2002).
While TikTok’s account creation does not enable direct
gender input, users are prompted to share their name. Names
are correlated with gender and many systems for inferring
gender from names exist (Sharma et al. 2023), so we tested
two names (one man, one woman) for each account. Names
were selected based on Social Security Administration data
associated with the years selected: Jacob/Emily for the ac-
counts aged 26, and Michael/Jennifer for the 46 year old
accounts (Social Security Administration 2026).
3.2 Dependent Variables
Frequency and content (e.g., advertisement category and
price) of ads are our dependent variables. Screenshots of all
content were captured and analyzed.
System OutputsScreenshots were recorded for all con-
tent viewed by every account. While recording video IDs
or URLs would provide the most data for analysis, the
only way to access this information on TikTok is using the
“share” function. Since sharing was one of our independent
variables in Study 1, could be interpreted as signaling in-
terest, and is unlikely to reflect typical user behavior when
browsing, we used screenshots instead. Prior work has been
able to obtain video IDs, but only through intercepting net-
work traffic (Kaplan and Sapiezynski 2024). Screenshots
were taken immediately before scrolling to the next video.
Recently in an effort to increase transparency, TikTok
began offering an “About This Ad” explanation for each
ad (TikTok 2022). While the ad explanations have not been
studied directly, prior work found that TikTok’s explanations
for which videos are shown were incorrect up to 40% of the
time (Mousavi, Gummadi, and Zannettou 2024). Due to this
inaccuracy, as well as the fact that the menu to access the
explanations is found in the share tab (which similarly risks
contaminating our data collection), we do not collect or an-
alyze these explanations.
Each account was active for 3-4 days, or until at
least 1,000 screenshots had been collected. Collection was
stopped when all accounts running simultaneously reached
1,000+ consumed content. While users report having their
algorithm return personalized results within minutes of join-
ing the platform (V ombatkere et al. 2024), we set the lower-
limit of 1,000 consumed videos to increase the likelihood
that the algorithm was personalized for the accounts.
Ad DetectionA two-step process was used to identify ads,
starting with image processing and then, if the first step
was unsuccessful, using OCR and keyword matching. This
was due to the variability of visual representations and key-
words of TikTok ads. For each image, the presence of a red
call-to-action button is first detected. If no button is found,

OCR-extracted keywords such assponsored,creator
earns commission, andadare used to classify the con-
tent. The method achieved 99.6% accuracy on a balanced
sample and 100% accuracy on a random sample of screen-
shots. Additional details and the full keyword list are pro-
vided in Appendix B. Of the 80,169 screenshots, 24,255
(30.2%) were classified as ads.
Advertisement Content CategorizationAutomatically
detected logos and image labels (described below) were used
to categorize the content of each ad. Due to our focus on
advertising and commerce, all 49 final categories were gen-
erated on the basis of the logos. These included categories
likeRestaurants & Fast Food Chains,Beauty
& Cosmetics,Fashion & Apparel, andSports.
The 445 unique logos were first grouped into 52 higher-
level categories using large language model (LLM) prompt-
ing, with manual oversight (i.e., correcting, removing,
and merging) over the final categories. For example, the
Restaurants & Fast Foodcategory included logos
for brands includingSweetgreen,Jersey Mike’s
Subs, andIHOP. Appendix C provides the full prompt and
details of the annotation process. A second LLM prompt
mapped the 2,866 image-based labels to the same 49 cate-
gories. 563 labels (e.g., people, happiness, beard) were clas-
sified as “Other” due to their ambiguity.
Each ad was assigned a single category. If a logo was
present, the ad was assigned the most common category
among its logos (2,396 ads). If no logos were detected, the
ad was assigned the most common category among the im-
age labels (8,906 ads). If neither logos nor image labels were
identified, the image was classified as “Unknown” (345 ads).
Logo DetectionLogos were detected usingGoogle Cloud
Vision APIlogo detection on all advertisements and
interacted-with content. Logos allow us to identify brands
and industries that advertised on TikTok. Of the 11,647 ads
in Study 2, 2,396 (20.6%) contained at least one detected
logo. This processing identified 445 unique logos.
Image Label DetectionGoogle Cloud Vision API’s image
label function identified the visuals in ads, providing signals
about the advertisement’s industry when obvious informa-
tion (e.g., logo) was unavailable. All images were cropped
to avoid everything being labeled a screenshot, however, we
still perform post processing of labels to remove tags such as
screenshotandadvertisementwhen present. Ap-
pendix D includes additional details.
Price DetectionUsers of different income groups could
be targeted with differently priced items and advertisements.
In Study 2, to understand how the prices of ads differ by in-
come, all ads that contained $+Number or Number+% were
extracted (2,096 ads, 18%). One member of the research
team manually reviewed and labeled these ads, distinguish-
ing instances where dollar amounts were discounts or deals
rather than product prices. A similar separation, splitting dis-
counts from rates (e.g., a lender’s APR) was done for per-
centages. Incorrect detections, as well as cases in which the
$/% referred to a hypothetical income or use of a product
(e.g., “if you build a website with us, you could make $X”),
were also removed, leaving 1,675 ads. While some discounts
(e.g., “Buy 1 Get 1 Free”) are missed, this approach captured
any ad with explicit prices (i.e., any price preceded by a $
sign) or discounts.
3.3 Summary of Experimental Conditions
Study 1.To explore the effects of interaction type we cre-
ated 32 accounts: 1 device type×2 ages×2 names×4
interaction types×2 copies.
Study 2.To investigate the effects of device price we cre-
ated 24 accounts: 3 device types×2 ages×2 names×1
interaction type×2 copies.
While data associated with gender and age were collected
in both studies, due to the artificial interaction behaviors
in Study 1, the effects of gender and age were explored
only using Study 2 data. Data on accounts within one set-
ting (e.g., “Jacob” accounts performing different interaction
types) were collected simultaneously to control for any mar-
keting campaigns. Two accounts (i.e., two copies) were cre-
ated for each setting to control for randomness in recom-
mendations and targeting.
3.4 Auditing System Implementation
SoftwareWe developed a python and ADB script to au-
tomate interactions with the TikTok application on Android
devices. Code will be provided to researchers upon request.
HardwareWe selected identical low, medium, and high
price devices (four of each kind) to run our automated ac-
counts. The different prices allowed us to explore the ef-
fects of price on the advertisements received. Having four of
each device allowed us to conduct data collection in parallel,
helping us capture time-restricted advertising campaigns as
consistently as possible across all experimental conditions.
Android devices were used because they offer greater
support for large-scale automation and scripted interactions.
Apple devices impose restrictions making automated audit-
ing and resetting of ad IDs difficult to implement.
Switching Between AccountsAfter logging out of each
account and prior to creating the new one, we deleted the
TikTok app storage and reset the device’s advertiser ID.
These steps were taken to reduce the likelihood that the
platform could link the accounts with each other and rec-
ommend similar content or advertisements on them. Ac-
count creation, login, and logout were all performed manu-
ally due to TikTok’s bot-detection mechanisms, which made
automating these steps unreliable. All other interactions with
the TikTok feed were performed automatically.
3.5 Data Availability
Across both studies, we have collected 24,255 advertisement
screenshots. Researchers can request access to the data by
filling out a form3 or contacting the first author. The dataset
will not be made publicly available online because in ad-
dition to corporate advertisements, some users place ads to
increase the reach of their individual user accounts, which
often include identifiable information such as usernames.
3https://forms.gle/6HEVqeMJBqotyrWd8

4 RQ1: How does interaction type affect the
number and content of ads?
4.1 Liking and sharing increased ad load
Ad load varied considerably for the different interaction
types (like, comment, share, scroll). Table 2 displays the
number of videos viewed and ad load for each account, with
two unique accounts created for each demographic attribute.
Surprisingly,commenting, which is a very active form of
engagement, did not increase exposure to ads compared to
the scroll condition.LikeandShareconditions attracted the
highest proportions of ads, with overall means of 30.8% and
35.2% respectively, compared to 25.7% forscrolland 25.9%
forcomment. Thesharecondition produced the highest ad
rate across all participants and rounds, with individual ses-
sion rates ranging from 32.8% to 37.6%. Average ad load
of 29.4% across all interaction conditions is comparable to
cable at 13.3 minutes per hour (Friedman 2021), but more
than most streaming services (Sutton 2022).
To test for statistical significance of the differences ob-
served between interaction types we fit an OLS regression
model on the data extracted in Study 1: d#Adsi =β 0 +β 1 ·
#Videos Watched i +β 2 ·Liked i +β 3 ·Shared i +
β4 ·Commented i, for accounti∈ {1, ...,32}accounts.
where#Videos Watchedis the total number of videos
consumed on the account. Interaction type is represented
by three indicator variables —Liked,Commented, and
Shared— each coded 1 if the account performed that in-
teraction and 0 otherwise.Scrollserves as the reference
category, so when all three interaction indicators are 0, the
model reflects the scroll condition.
Liking and sharing significantly increased ads. Comment-
ing exhibited a small positive, but non-significant, relation-
ship with ad count. Overall, the model confirmed the sig-
nificance of interaction type as a predictor of ad exposure,
even after controlling for demographic variables and session
volume. Table 3 shows the results of the model. The model
explains approximately 88.5% of variance in ad counts. The
findings persisted in a model that included age and gender
(Appendix F).
4.2 As accounts viewed more content, they were
shown more advertisements
As accounts encountered more content, the ad load in-
creased. Figure 1 shows this increase over the lifetime of
each account. For each account, the proportion of ads in the
first 1,000 videos was calculated for each step n by dividing
the cumulative number of ads observed up to video n byn
(the number of videos viewed). For consistency, any videos
after the first 1,000 were discarded in this analysis. Median
and first and third quartiles are shown in Figure 1.
A general upward trend for all interaction types was ob-
served. This result indicates that TikTok’s ad delivery is not
uniformly distributed across an accounts’ lifetime. Instead,
the platform appears to serve advertisements at an increas-
ing rate as consumption continues, independent of how the
user is engaging with content. One interpretation is that the
algorithm treats sustained scrolling itself as a signal of en-
gagement, and increases ad load accordingly. Alternatively,
Figure 1: Ad rate over time. All accounts experienced an in-
creased ad load as more content was viewed. The comment
accounts were unusual in that the increase was delayed rela-
tive to other interaction types.
Figure 2: The relationship between ad load and the num-
ber of interactions with ads across Study 1 accounts. As the
number of interactions with ads increases, so does the per-
centages of advertisements encountered.
the pattern may reflect a deliberate pacing strategy in which
initial content is kept relatively ad-light to establish momen-
tum before monetizing the session more aggressively.
Interestingly, commenting exhibited a different pattern
from other interactions. While there was an eventual in-
crease in ad load, it occurred later and at a much slower rate.
This may be due to only commenting being categorized as
an unusual behavior by the platform. We leave further inves-
tigation of how different interaction start times, interaction
behaviors, or interaction rates affect ad load to future work.
4.3 More interactions with ads increased ad load
Users’ interaction with specific types of content could ex-
plain the prevalence of content they see. In other words, ac-
counts that interact with more ads over their lifetime, might
be exposed to more ads. Both ads and non-ads were inter-
acted with across all accounts. Figure 2 visualizes the rela-
tionship between ad load and number of ads interacted with.
When accounts interacted with more ads, their ad load
increased. The Pearson correlation between the values dis-
played is +0.759 (p <0.001). Thus, both the type (Table 3)
and target of the interaction impacted ad load.

Age Name Scroll Like Comment Share
26 Jacob 1 140026.0%101630.6%145127.6%134732.8% 2 119620.2%132436.6%166620.7%128034.9%
26 Emily 1 106525.0%150931.1%140225.4%103833.0% 2 186525.4%137231.3%131223.8%212737.6%
46 Michael 1 134126.6%100729.9%122226.9%106235.8% 2 162127.7%118424.5%147230.5%159836.3%
46 Jennifer 1 148726.9%125030.1%102526.0%146035.5% 2 122027.6%123031.9%102426.2%124636.0%
Mean 1399 25.7% 1236 30.8% 1322 25.9% 1395 35.2%
Median 1370 26.3% 1240 30.9% 1357 26.1% 1314 35.6%
Standard Deviation 257 2.4% 171 3.3% 224 2.8% 350 1.6%
Table 2: Study 1 result. Total number of videos captured and ad load per account & interaction type. Liking and sharing lead to
the highest ad load. Surprisingly, commenting which is a very active form of engagement, did not result in increased ad load.
PredictorβCoefficientp-value
β0 Intercept -113.0755 0.0141 ∗
β1 # Videos Watched 0.3384 0.0000 ∗∗∗
β2 Liked 75.9950 0.0009 ∗∗∗
β3 Shared 135.1902 0.0000 ∗∗∗
β4 Commented 5.7698 0.7756
n= 32,R 2 = 0.8847, Adj.R 2 = 0.8676
Significance: ∗∗∗p <0.001 ∗p <0.05
Table 3: OLS regression model predicting the number of ads
based on interaction and demographic variables. Liking and
sharing significantly increased ad count, while commenting
had a positive but non-significant relationship.
Device Mean Median
Pixel 3a 149333.9%151434.1%
Pixel 8 153131.5%144232.1%
Galaxy S26+ 164429.1%162430.4%
Table 4: Device price & ad load. More expensive devices
had slightly lower ad loads.
5 RQ2: How does income affect the number
and content of ads?
5.1 More expensive devices received fewer ads
In our second study, realistic user interactions were sim-
ulated to investigate the impact of income, approximated
through device price, on ad load and content. The mean and
median total number of content consumed and ad load for
all accounts on each device4 are displayed in Table 4.
Our results indicated that the least expensive device re-
4A total of 8 unique accounts are run on each device: 2 ages×
2 genders×2 copies.
ceived the highest ad load (33.9%), followed by the mid-
priced device (31.5%), and the most expensive device had
the lowest ad load (29.1%). These findings provide support
for the hypothesis that device price influences ad exposure.
To further investigate the factors driving ad exposure, we
fit an OLS regression model predicting the number of ads
received: d#Adsi =β 0 +β 1 ·#Videos Watched i +β 2 ·
Agei +β 3 ·Gender i +β 3 ·Device Price i, for account
i∈ {1, ...,24}accounts. The reference group forAgeis
26 and forGenderis Man. Device price is coded in U.S.
dollars. Table 5 displays the results of this model.
Device price had a negative, but non-significant relation-
ship with ad count. Age was the only significant demo-
graphic variable, with younger profiles receiving approxi-
mately 89 more ads per account than older profiles (a 5%
increase in ads).
PredictorβCoefficientp-value
β0 Intercept -41.4320 0.7789
β1 # Videos Watched 0.3263 0.0018 ∗∗
β2 Age 89.1423 0.0329 ∗
β3 Gender 43.2788 0.2720
β4 Device Price -0.0943 0.1149
n= 24,R 2 = 0.4608, Adj.R 2 = 0.3473
Significance: ∗∗p <0.01 ∗p <0.05
Table 5: OLS regression model predicting the number of ads
based on device and demographic variables. Age is the only
statistically significant demographic variable, with younger
users receiving more ads. Device price had a negative but
not significant relationship with number of ads.

Figure 3: Category distribution of advertisements across
the three phone types. Entertainment and Electronics were
the most common categories across devices. Travel ads ap-
peared less frequently on the cheapest device (Pixel 3a) than
on the more expensive phones.
5.2 Travel ads targeted wealthy consumers, but
most other categories were based on non-ad
interactions
Entertainment, electronics, and food were among the most
frequently advertised categories (Figure 3), across all device
types. While many of these categories are consistent with
prior work, TikTok seems to feature significantly less health-
care advertising than other media (Marketing Charts 2020).
Alternatively, the relevant visual features of categories such
as healthcare may have been harder to capture or unavailable
in our screenshots. Because healthcare ads often feature peo-
ple, and our ad categorization method removed visual cate-
gories such as people and happiness due to their ambiguity,
some advertisements in this category may be missed.
Travel was among very few categories which received no-
ticeably more ads in the more expensive phones. Otherwise
most categories were similarly frequent for accounts on all
phones, and pairwise Wilcoxon signed-rank tests conducted
on the ranked lists of ad categories across pairs of devices
found no statistically significant differences.
Instead, rather than device price, accounts’ interactions
with non-ad content was most predictive of the ad cate-
gories. For many categories, increased interaction led to an
increase in ads of that type. However, accounts received
advertisements for some categories (e.g., Restaurants, Fur-
niture, Arts) that had little to no interactions (Figure 4).
Pairwise Wilcoxon signed-rank tests on the ad and inter-
action categories were statistically significant (W=299.00,
p<0.001). Thus, it appears that some business sectors place
ads to uninterested users; future study is needed to test this.
Figure 4: Category distribution of advertisements across ad-
vertisements and interacted-with content. For many cate-
gories, increased interaction led to an increase in ads of that
type. However, accounts received advertisements for some
categories (e.g., Restaurants, Furniture, Arts) that had little
to no interactions.
5.3 The cheapest phone was shown the highest
discount percentages
Advertising the exact price of goods was relatively uncom-
mon across devices (14.4% of total ads in Study 2). The most
expensive phone received the fewest discounts in ads. Table
6 presents the median cost and discount of ads per device.
Pixel 3a Pixel 8 Galaxy S26+
Cost236 $31.20 369 $53.30 337 $50.37
Discount245 45.00% 296 28.50% 165 20.00%
Total Ads4,059 3,771 3,817
Table 6: Median costs and discounts of ads across devices.
Mid-range device received the most expensive ads. The
cheapest device received the highest discounts.
Accounts on the cheapest phone were shown the highest
discount percentages. It is important to note that this does
not necessarily translate to cheaper deals (many ads featur-
ing discounts do not include the product cost), only that the
advertisement presented itself as offering a greater discount
to the user. Accounts on more expensive devices were shown
advertisements for higher cost goods and services, consis-
tent with an assumption of higher spending power by users
on these devices. Surprisingly, however, higher price adver-
tisements were shown on the mid-range device compared to
the most expensive device.

Mean Median
Gender
Man 152132.9%156232.1%
Woman 159230.1%167430.8%
Age
26 150734.5%156235.0%
46 160528.4%164830.4%
Table 7: Demographics & ad load. Men had slightly higher
ad load. Younger accounts had higher ad load.
6 RQ3: How do age and gender affect the
number and content of ads?
6.1 Younger accounts received more ads
To assess the impacts of age and gender on ad load we com-
pared mean and median ad loads across accounts of the dif-
ferent age and gender in Study 2, shown in Table 7. We
found that younger users and men received more ads. How-
ever, age was the only statistically significant predictor of
ad count between the two (Table 5). This finding was con-
sistent with prior work which found a difference in content
recommendation across age, but found no significant differ-
ence between genders (Kaplan and Sapiezynski 2024).
Given the low quality of name-based gender detection al-
gorithms, specifically for racial minorities and non-binary
users (Sharma et al. 2023), the apparent lack of platform re-
liance on this feature for ad targeting is a positive finding.
However, the lack of observed gender differences may be
due to TikTok choosing not to use names as a proxy for gen-
der, given the low accuracy of such inferences and the ease
of providing false names. TikTok may still rely on other sig-
nals to infer gender, which future work should investigate.
6.2 Ad categories were consistent across age and
gender
To assess the differences in the content of advertisements,
we examined the differences in the prevalence of adver-
tisement category rankings between different ages and gen-
ders. Pairwise Wilcoxon signed-rank tests conducted on the
ranked lists of ad categories found no statistically significant
differences for either factor.
7 Discussion
7.1 A focus on behavior rather than
demographics
Our finding revealed that active engagement (i.e., liking and
sharing) substantially increases the rate at which users were
served advertisements. This pattern is consistent with prior
work on content recommendation systems, where engage-
ment signals have been found to influence content personal-
ization (Boeker and Urman 2022). On one hand, this type of
engagement-based targeting provides users with more power
to influence the ads they get by strategically interacting with
content, on the other hand it creates an adversarial environ-
ment in which users refrain from supporting content or cre-
ators they enjoy out of a fear of receiving excessively high
volumes of similar content (Eslami et al. 2016).
Given the importance of behavioral factors future stud-
ies of the topic are also required. In this work, interactions
were performed at a constant rate of 10%, yet we found that
the percentage of ads presented to users increased over time.
One interpretation is that TikTok’s ad delivery algorithm
treats longer engagement with the application as a signal or
investment or buy-in, and increases ad load. An alternative
explanation could be a feedback-loop dynamic: as accounts
were shown more ads, the 10% random interaction probabil-
ity meant they were statistically more likely to also interact
with ads, further reinforcing ad delivery. Future work should
investigate different engagement patterns with ads and non-
ad content. Additionally, impacts of changing behavior over
time should also be examined.
7.2 Device price as a weak and ambiguous signal
Our second study found that the cheapest device had the
highest ad load. This means that users who do not have the
means or desire to purchase more expensive devices may
face a higher advertisement burden, with ads taking up more
of their time and attention. While differences in ad load
and content were small, given the unfairness of such dif-
ferences, we believe further investigation is required. Thus,
future work should continue examining features that may act
as proxies for income and how platforms use them. For ex-
ample, our work explored TikTok’s Device Price feature, but
other features such as Spending Power remain unexplored.
8 Conclusion
This paper presented two paired studies auditing TikTok’s
advertising system, examining the effects of interaction type,
device price (as an income proxy), age, and gender on the
number and content of ads. Across the two studies, using
56 accounts, we collected data on 80,169 videos and 24,255
advertisements. We found that active engagement, specifi-
cally liking and sharing content, significantly increased ad
exposure. Commenting, however, did not increase ad load.
Lower-income accounts were shown higher discount per-
centages. Device price was also found to have a directional
effect with the least expensive device receiving more ads.
References
Ali, M.; Goetzen, A.; Mislove, A.; Redmiles, E. M.; and
Sapiezynski, P. 2023. Problematic Advertising and its Dis-
parate Exposure on Facebook. In32nd USENIX Security
Symposium.
Amazon Ads. 2024. Generational Marketing: How to Mar-
ket to Different Generations. https://advertising.amazon.
com/library/guides/generational-marketing#1. Accessed:
2026-05-15.
Asplund, J.; Eslami, M.; Sundaram, H.; Sandvig, C.; and
Karahalios, K. 2020. Auditing Race and Gender Discrim-
ination in Online Housing Markets.Proceedings of the In-

ternational AAAI Conference on Web and Social Media, 14:
24–35.
Bandy, J. 2021. Problematic Machine Behavior: A System-
atic Literature Review of Algorithm Audits.Proc. ACM
Hum.-Comput. Interact., 5(CSCW1).
Baumgartner, M. 2025. TikTok Statistics. https://www.
zebracat.ai/post/tiktok-statistics. Accessed: 2026-05-15.
Blaine, B.; and McElroy, J. 2002. Selling stereotypes:
Weight loss infomercials, sexism, and weightism.Sex Roles,
46(9): 351–357.
Blumenthal, R.; Blackburn, M.; Durbin, R.; Graham, L.;
Warren, E.; and Hawley, J. 2023. Letter to Mark Zucker-
berg.
Boeker, M.; and Urman, A. 2022. An Empirical Investiga-
tion of Personalization Factors on TikTok. InProceedings
of the ACM Web Conference 2022, WWW ’22. New York,
NY , USA: Association for Computing Machinery.
Caba˜nas, J. G.; Cuevas, ´A.; and Cuevas, R. 2018. Unveil-
ing and Quantifying Facebook Exploitation of Sensitive Per-
sonal Data for Advertising Purposes. In27th USENIX Secu-
rity Symposium (USENIX Security 18), 479–495. Baltimore,
MD: USENIX Association. ISBN 978-1-939133-04-5.
Duarte, F. 2026. TikTok User Age, Gender, & Demo-
graphics (2026). https://explodingtopics.com/blog/tiktok-
demographics. Accessed 2026-05-14.
Edelson, L.; Haugen, F.; and McCoy, D. 2025. A Compara-
tive Survey Of Algorithmic Feed Recommendation System
Designs.ACM Trans. Recomm. Syst.
Eslami, M.; Karahalios, K.; Sandvig, C.; Vaccaro, K.; Rick-
man, A.; Hamilton, K.; and Kirlik, A. 2016. First I ”like” it,
then I hide it: Folk Theories of Social Feeds. InProceedings
of the 2016 CHI Conference on Human Factors in Comput-
ing Systems. New York, NY , USA: ACM.
European Commission. 2023. Commission Delegated Reg-
ulation (EU) on the Performance of Audits for Very Large
Online Platforms and Very Large Online Search Engines.
Federal Trade Commission. 2025. FTC Surveillance Pricing
Study Indicates Wide Range of Personal Data Used to Set
Individualized Consumer Prices .
Figueira, O.; Chamarthi, P.; Le, T.; and Markopoulou,
A. 2025. When Kids Mode Isn’t For Kids: Investi-
gating TikTok’s” Under 13 Experience”.arXiv preprint
arXiv:2507.00299.
Friedman, W. 2021. TV Ad Load Spikes 6% In
Q2, With A+E On Top, Disney At The Bottom.
https://www.mediapost.com/publications/article/365761/tv-
ad-load-spikes-6-in-q2-with-ae-on-top-disne.html. Ac-
cessed 2026-05-15.
Fromm, J.; and Read, A. 2018.Marketing to Gen Z: The
rules for reaching this vast–and very different–generation of
influencers. Amacom.
Gak, L.; Olojo, S.; and Salehi, N. 2022. The Distressing Ads
That Persist: Uncovering The Harms of Targeted Weight-
Loss Ads Among Users with Histories of Disordered Eating.
Proceedings of the ACM on Human-Computer Interaction,
6(CSCW2).
Germano, F.; G´omez, V .; and Sobbrio, F. 2026. Ranking for
engagement: How social media algorithms fuel misinforma-
tion and polarization.Journal of Public Economics, 255:
105589.
Geuens, R. 2025. What’s the Average Time Spent on Social
Media Each Day? https://soax.com/research/time-spent-on-
social-media. Accessed: 2026-05-14.
Grbovic, M.; Radosavljevic, V .; Djuric, N.; Bhamidipati, N.;
and Nagarajan, A. 2015. Gender and interest targeting for
sponsored post advertising at tumblr. InProceedings of the
21th ACM SIGKDD International Conference on Knowl-
edge Discovery and Data Mining, 1819–1828.
Gunasekara, S.; Pareek, S.; Kelly, R. M.; Kostakos, V .;
and Goncalves, J. 2025. Auditing TikTok’s Recommenda-
tions: Understanding the Prevalence of Misinformation on
the Platform.Available at SSRN 5580515.
Imana, B.; Korolova, A.; and Heidemann, J. 2021. Audit-
ing for Discrimination in Algorithms Delivering Job Ads.
InProceedings of the Web Conference 2021, WWW ’21,
3767–3778. New York, NY , USA: ACM.
John, J. M.; Shobayo, O.; and Ogunleye, B. 2023. An explo-
ration of clustering algorithms for customer segmentation in
the UK retail market.Analytics, 2(4): 809–823.
Kaplan, L.; Patel, D.; Gerzon, N.; Mislove, A.; and
Sapiezynski, P. 2026. When ’For You’ Isn’t For You: Mea-
suring User Agency in TikTok’s Algorithmic Feed. InPro-
ceedings of the International AAAI Conference on Weblogs
and Social Media (ICWSM’26). Budapest, Hungary.
Kaplan, L.; and Sapiezynski, P. 2024. Comprehensively Au-
diting the TikTok Mobile App. InCompanion Proceedings
of the ACM Web Conference 2024, WWW ’24. New York,
NY , USA: Association for Computing Machinery.
Kofman, A.; and Tobin, A. 2019. Facebook Ads Can Still
Discriminate Against Women and Older Workers, Despite
Civil Rights Settlement.
Lam, M. S.; Gordon, M. L.; Metaxa, D.; Hancock, J. T.; Lan-
day, J. A.; and Bernstein, M. S. 2022. End-User Audits: A
System Empowering Communities to Lead Large-Scale In-
vestigations of Harmful Algorithmic Behavior.Proc. ACM
Hum.-Comput. Interact., 6(CSCW2).
Lambrecht, A.; and Tucker, C. 2019. Algorithmic Bias? An
Empirical Study of Apparent Gender-Based Discrimination
in the Display of STEM Career Ads.Management Science,
65(7): 2966–2981.
Mai, C.; Coelho, B.; Kieserman, J.; Matsumoto, L.; Spinelli,
K.; Yang, E.; Andreou, A.; Greenstadt, R.; Lauinger, T.; and
McCoy, D. 2025. More and Scammier Ads: The Perils of
YouTube’s Ad Privacy Settings.Proceedings on Privacy En-
hancing Technologies, 4.
Marketing Charts. 2020. Top 10 Advertising Categories in
Q1 2020. https://www.marketingcharts.com/charts/top-10-
advertising-categories-in-q1-2020. Accessed: 2026-05-14.
Mattioli, D. 2012. On Orbitz, Mac Users Steered to Pricier
Hotels.
McAfee, R. P. 2008. Price discrimination.Issues in Compe-
tition Law and Policy, 1: 465–484.

McKinsey. 2021. The value of getting personalization
right—or wrong—is multiplying.
Min, K. Z. L.; and Kim, S. H. 2025. The Impact of Influencer
Credibility and Short Video Attributes on User Attitudes and
Adoption of Instagram Reel Advertising.Asia pacific jour-
nal of information systems, 35(1): 119–145.
Mosnar, M.; Skurla, A.; Pecher, B.; Tibensky, M.; Jakub-
cik, J.; Bindas, A.; Sakalik, P.; and Srba, I. 2025. Revisit-
ing Algorithmic Audits of TikTok: Poor Reproducibility and
Short-term Validity of Findings. InProceedings of the 48th
International ACM SIGIR Conference on Research and De-
velopment in Information Retrieval, SIGIR ’25. New York,
NY , USA: Association for Computing Machinery.
Mousavi, S.; Gummadi, K. P.; and Zannettou, S. 2024. Au-
diting algorithmic explanations of social media feeds: A
case study of tiktok video explanations. InProceedings of
the International AAAI Conference on Web and Social Me-
dia, volume 18, 1110–1122.
Okoroafo, S. C.; Koh, A. C.; and Gammoh, B. S. 2010. Gen-
der differences in perceptions of the marketing stimuli of
family owned businesses (FOBs).International Journal of
Marketing Studies, 2(1): 3.
Pacheco, I.; and Ramachandran, S. 2019. Do You Pay
Too Much for Internet Service? See How Your Bill Com-
pares. https://archive.ph/csgu0#selection-1915.5-1915.74.
Accessed 2026-05-14.
Patterson, R. A.; Laidlaw, E.; and Zhang, J. 2025. Price dis-
crimination is getting smarter—and low-income consumers
are paying the price. https://theconversation.com/price-
discrimination-is-getting-smarter-and-low-income-
consumers-are-paying-the-price-252723. Accessed
2026-05-14.
Reitinger, N.; Wen, B.; Mazurek, M.; and Ur, B. 2024. What
Does It Mean to Be Creepy? Responses to Visualizations of
Personal Browsing Activity, Online Tracking, and Targeted
Ads.Proceedings on Privacy Enhancing Technologies.
Sakina. 2025. Walmart Shopper Goes Viral on Tik-
Tok After Claim About Pricing. https://www.yahoo.
com/news/articles/walmart-shopper-viral-tiktok-claim-
140701699.html. Yahoo News, accessed 2026-05-15.
Sandvig, C.; Hamilton, K.; Karahalios, K.; and Langbort, C.
2014. Auditing Algorithms: Research Methods for Detect-
ing Discrimination on Internet Platforms. InData and Dis-
crimination: Converting Critical Concerns into Productive
Inquiry, 1–23. Open Technology Institute.
Sharma, M.; McTavish, H.; Peng, Z.; Shah, A.; Agarwal,
V .; Sih, C.; Hogan, E.; Molina, I. V .; Raj, A. G. S.; and
Vaccaro, K. 2023. Engagement and Anonymity in Online
Computer Science Course Forums. InProceedings of the
2023 ACM Conference on International Computing Educa-
tion Research - Volume 1, ICER ’23, 48–62. New York, NY ,
USA: Association for Computing Machinery.
Shin, D.; and Jitkajornwanich, K. 2024. How algorithms
promote self-radicalization: Audit of TikTok’s algorithm us-
ing a reverse engineering method.Social Science Computer
Review, 42(4): 1020–1040.
Silva, M.; Santos de Oliveira, L.; Andreou, A.; Vaz de Melo,
P. O.; Goga, O.; and Benevenuto, F. 2020. Facebook Ads
Monitor: An Independent Auditing System for Political Ads
on Facebook. InProceedings of The Web Conference 2020,
WWW ’20, 224–234. New York, NY , USA: Association for
Computing Machinery.
Social Security Administration. 2026. Popular Baby Names.
https://www.ssa.gov/cgi-bin/popularnames.cgi. Accessed:
2026-05-14.
Sutton, K. 2022. Streaming services are still fighting to
have ultra-light ad loads. https://www.marketingbrew.com/
stories/2022/05/12/streaming-services-are-still-fighting-to-
have-ultra-light-ad-loads. Accessed 2026-05-15.
TikTok. 2022. Furthering our advertising transparency ef-
forts: Introducing ”“About this ad”’. https://ads.tiktok.com/
business/en-US/blog/introducing-about-this-ad. Accessed:
2026-05-15.
Ur, B.; Leon, P. G.; Cranor, L. F.; Shay, R.; and Wang, Y .
2012. Smart, useful, scary, creepy: perceptions of online
behavioral advertising. InProceedings of the Eighth Sym-
posium on Usable Privacy and Security. ACM.
V ombatkere, K.; Mousavi, S.; Zannettou, S.; Roesner, F.;
and Gummadi, K. P. 2024. TikTok and the Art of Personal-
ization: Investigating Exploration and Exploitation on Social
Media Feeds. InProceedings of the ACM Web Conference
2024, WWW ’24, 3789–3797. New York, NY , USA: Asso-
ciation for Computing Machinery.
Wei, M.; Stamos, M.; Veys, S.; Reitinger, N.; Goodman, J.;
Herman, M.; Filipczuk, D.; Weinshel, B.; Mazurek, M. L.;
and Ur, B. 2020. What Twitter Knows: Characterizing Ad
Targeting Practices, User Perceptions, and Ad Explanations
Through Users’ Own Twitter Data. 145–162.
Xue, L.; Corso, F.; Fontana, N.; Liu, G.; Ceri, S.; and Pierri,
F. 2025. Towards an Automated Framework to Audit Youth
Safety on TikTok. InProceedings of the Fourth Workshop
on Bridging Human-Computer Interaction and Natural Lan-
guage Processing (HCI+ NLP), 113–119.
Yang, C.; Mousavi, S.; Dash, A.; Gummadi, K. P.; and We-
ber, I. 2024. Coupling GDPR Data Donation and Crowd-
sourced User Survey: A Case Study on TikTok Addiction.
InCompanion Publication of the 16th ACM Web Science
Conference, Websci Companion ’24. New York, NY , USA:
Association for Computing Machinery.
Yang, C.; Mousavi, S.; Dash, A.; Gummadi, K. P.; and We-
ber, I. 2025. Studying behavioral addiction by combining
surveys and digital traces: A case study of TikTok. InPro-
ceedings of the International AAAI Conference on Web and
Social Media, volume 19, 2106–2123.
Zannettou, S.; Nemeth, O.-N.; Ayalon, O.; Goetzen, A.;
Gummadi, K.; Redmiles, E. M.; and Roesner, F. 2023.
Leveraging rights of data subjects for social media anal-
ysis: Studying TikTok via data donations.arXiv preprint
arXiv:2301.04945.

Gender OS Available audience
All All 146,115,000-178,586,000
Male All 76,208,000-93,144,000
Female All 69,907,000-85,443,000
All Android 36,889,000-45,087,000
Male Android 22,981,000-28,089,000
Female Android 13,907,000-16,998,000
Table 8: Estimate of users located in the US (Age≥18). OS
= operating system.
A TikTok Advertisement Platform
TikTok offers an advertising platform5 which allows adver-
tisers to select the characteristics of users (e.g., location,
age, interests, among many others) they would like to tar-
get. The platform provides advertisers with anAvailable
audienceestimate which is an “estimation of the number
of user accounts eligible” to see the ad based on the selected
criteria. This estimate is “the number of user accounts shown
ads [on TikTok] in the past 30 days”.
Among the demographics and variables on the website are
AgeandDevice Price. The age groups on the platform
are as follows: 13-17, 18-24, 25-34, 35-44, 45-54, and 55+.
The website, however, does not provide estimates for user
counts under the age of 18. The minimum and maximum
value of device prices can be selected in $50 increments. The
highest value advertisers can select is 1000+. We collected
audience estimates onMarch 10, 2026.
Table 8 displays the gender distribution of TikTok users
overall and those using Android devices. We can see that
iOS users are more common. However, our automated inter-
action system only operated on Android devices.
Advertisers can target users based on income using two
options: (i) Device price (Table 9) and (ii) Spending power
(Table 10). We focus on device price in this work. It is un-
clear to us what the criteria for “spending power” classifica-
tion are. Table 9 shows the number of users using devices
of specific prices. We find that the values are different if
the advertiser selectsany priceorspecific price
and selecting 0-1000+ as the range. This might be because
TikTok is unable to determine the price of some user’s de-
vices. We selected the device price ranges shown in the table
for our study because the number of users within the three
groups are roughly similar.
B Ad Detection
We perform a two-step ad identification process. In this sec-
tion, we will describe what ads can look like, our identifica-
tion process, and the performance of our method.
B.1 What do ads look like?
Ads can be identified on the platform using various
keywords, such as:Sponsored,Creator earns
commission,Ad,Paid partnership, and
5https://ads.tiktok.com/
Device Price Range Available audience
Any 36,889,000-45,087,000
0-1000+ 7,177,000-8,773,000
0-250 2,636,000-3,223,000
400-650 899,000-1,100,000
750-1000+ 1,845,000-2,256,000
Table 9: Estimate of users located in the US and using An-
droid devices of various prices (Gender=All,Age≥18).
SP OS Available audience
All All 146,115,000-178,586,000
All iOS 109,226,000-133,499,000
All Android 36,889,000-45,087,000
High All 24,638,000-30,114,000
High iOS 18,159,000-22,195,000
High Android 6,478,000-7,919,000
Table 10: Estimate of users located in the US and any gender
and any device price (Age≥18). SP = Spending power, OS
= operating system.
Promotional content. However, these keywords
are not always present and at other times the platform might
show deals using$+(Number)or(Number)+%to users.
As shown in Figure 5a, the existence of these tags is not
mutually exclusive. For instance, a post that has a Dollar
amount could have a creator earns commission tag too, but
that is not always the case. It is worth noting that the green
location icon is not always an ad as it might not be followed
by a Dollar or percentage off amount (see Figure 6).
As shown in Figure 5b there is sometimes a red call-
to-action button, but this button could be transparent or
non-existent in some ads. Additionally, if the screenshot
is taken at the end of the ad, the tags on the bottom (e.g.,
sponsored) will disappear and there will only be a red call
to action button in the middle of the page (see Figure 7).
The text on this button can be selected by the advertiser and
thus can take a variety of values. Some of these values we
identified in our manual review of the ads were as follows:
Shop now,Shop here,Transfer instantly,
Get tickets now,Find an attorney today,
Featured Item,Learn more,Interested,
Sign up,Order now,Order today,View now,
Limited time deal,Limited-time offer,
Free shipping,DEALS FOR YOU,Book now,
Free returns,Join to view hot products,
Download,Download app now,Install now,
File your claim here,Check it out,Go
to Google Play,Apply now,Pre-order now,
Watch now,Install app now. We believe this list is
not exhaustive.
It is important to note that there are some videos that are
ads but are not recognized by TikTok as being ads (see Fig-
ure 8). We try to write our ad detection code such that we

(a) Multiple tags might be present.
 (b) Red call to action button is not always present.
Figure 5: Different ways ads are displayed on TikTok.
Figure 6: Location icon is not always an ad.
Figure 7: The red button shown in the middle of the screen,
with some examples of the different texts it can have.
Figure 8: Posts that are ads but are not classified as such by
TikTok.
don’t identify these posts, because our focus is on ads offi-
cially classified by the platform.
B.2 B.2 Identification Process
To detect ads we rely both on the image and the outputs
of EasyOCR model. Each image is first analyzed using
opencvto see if a red box is visible in the middle of the
screen. If the box is identified, we label the screenshot as an
ad and move on. Otherwise, we perform keyword matching
for the different tags discussed in Appendix B.1. This code
was run on all 80,169 screenshots collected through our two
studies. A total of 24,255 were identified. Figure 9 displays
the method or tag by which ads were identified. As discussed
in Appendix B.1, it is important to note that since multiple
tags can be present for each ad, the high/low frequency of
tags does not necessarily mean other tags were not present,
it just shows how our code identified the ad.
When matching$+(Number)we only match
[f/F]rom [only] $+(Number),$+(Number)
off, andGet $+(Number). This is done because some

0 2,500 5,000 7,500 10,000
Interested+Search
Pre-order now
Install app now
Apply now
Order today
Go to Google Play
Install now
Check it out
Limited time deal
Shop here
Featured Item
View now
Free returns
Get tickets now
Free shipping
Sign up
Book now
Promotional content
Shop
Order now
(Number)+%
Creator earns commission
Shop now
Paid partnership
$+(Number)
Box Detected
Learn more
Ad
Sponsored
1
1
1
1
2
2
3
3
5
5
10
18
20
22
60
62
114
121
198
231
426
613
811
1,122
1,314
1,987
2,361
5,058
9,683
TikTok Ad Detection Methods
Figure 9: Frequency of tags identified through our ad detection method. The presented numbers reflect the method our code
used to identify ads and do not necessarily represent the overall distribution of tags, as some ads contained multiple tags. Each
ad is only counted once in this figure according to their detection method.

users might include $ in their post but the post is not an
ad identified by TikTok. The patterns for how ads use
$ were identified by one member of the research team
through manual review. For(Number)+%we only match
(Number)+% offdue to similar reasons.
B.3 Performance Evaluation
Evaluation on a True Random SampleTo evaluate the
performance of our method, we randomly sampled 500 im-
ages from our dataset of 80,169 viewed content. One mem-
ber of the research team then manually reviewed these im-
ages and verified the labels. Table 11 shows the performance
of our model.
Actual
Ad Not Ad
Predicted
Ad 142 0
Not Ad 0 358
Table 11: Performance of our ad identification method on a
random sample of 500.
Evaluation on a Balanced Random SampleTo further
evaluate the performance of our method, we randomly sam-
pled 250 posts classified as ads and 250 classified as not
being ads. One member of the research team then manually
reviewed these images and verified the labels. Table 12 dis-
plays the performance of our method.
Actual
Ad Not Ad
Predicted
Ad 249 1
Not Ad 1 249
Table 12: Performance of our ad identification method on a
balanced sample of 500.
The one mistake that occurred, the video that was not an
ad but was classified as such, was due to the word ”Shop”
being matched to an image that discussed being able to shop
for a product but did not refer to TikTok shop. Even though
we observed this issue, we decided to keep the keyword and
then manually review and remove any such posts. This was
because TikTok shop posts did not always have a $ amount
or % to match them all using those methods (see Figure 10).
C Analyzing Products Through Logo
Detection
We usedGoogle Cloud Vision API’s Logo detection func-
tion6 to extract the logos in the 11,647 ads.
6https://docs.cloud.google.com/vision/docs/detecting-logos
Figure 10: Example of an ad linking to TikTok shop.
C.1 Logos Removed From our Analysis
We removed TiV o from the results of our analysis, because
it was mistakenly detected for 5,244 (45.0%) of ads. We hy-
pothesize the mistake was due to the “Live” logo shown in
Figure 11 which is similar to the Tivo logo.
C.2 Statistics of Logo Detection Across Study 2
Our logo detection model identified 445 unique logos across
the 11,647 advertisements. We used a large language model
(LLM) to assign high-level industry categories to each of the
brands contained in our dataset. The model was prompted
with the following instruction:
“You are given a CSV file containing brand names.
For each row, determine the brand’s most appropriate
high-level category based on what the brand primarily
sells or is known for.
Examples of categories include: Fashion & Apparel,
Beauty & Cosmetics, Electronics, Restaurants & Fast
Food Chains, Food & Non-Alcoholic Beverages, Al-
coholic Beverages, Automotive, Insurance, Financial
Services, Healthcare, Travel & Hospitality, Software
/ SaaS, Social Media, Streaming Services & Cable,
Sports Teams, and Media & Entertainment.
Instructions:
• Read the CSV input.
• Add a new column calledcategory.
• Output the full CSV with the new column included.
• Use concise, standardized category names.
• Add additional categories beyond the examples
when appropriate.
• Preserve all existing columns and row order.”

Figure 11: Part of the image that might be mistaken for the
TiV o logo highlighted using a red box.
We then usedSonnet 4.6to create initial labels for
the logos. The model created 52 categories. Members of
the research team then manually reviewed and fixed the
categories outputted by the model. When unsure, the en-
tire research team was consulted. One category (“Labor &
Unions”) was removed because it only had 1 logo/brand, and
the logo/brand was merged into “Nonprofit & Advocacy”.
Three sports-related categories were also merged into a sin-
gle “Sports” category.
The full list of 49 categories is as fol-
lows:Advertising & Marketing,
Aerospace & Defense, Alcoholic
Beverages, Arts & Culture, Astrology
& Spirituality, Automotive, Beauty
& Cosmetics, Collectibles & Trading
Cards, Education, Electronics,
Energy & Utilities, Environmental
Services, Fashion & Apparel, Financial
Services, Flags & Symbols, Food &
Non-Alcoholic Beverages, Gambling
& Lottery, Government & Military,
Health & Nutrition Supplements,
Healthcare, Holidays & Observances,
Home Appliances, Home Furnishings, Home
Improvement, Home Security, Household
& Cleaning Products, Industrial &
Agricultural Equipment, Insurance,
Logistics & Delivery, Luxury Goods &
Jewelry, Media & Entertainment, Music,
Nonprofit & Advocacy, Pet Products,
Political Organizations, Real Estate,
Religious Organizations, Restaurants
& Fast Food Chains, Retail, Social
Media, Software / SaaS, Sports, Sports
& Fitness Equipment, Streaming Services
& Cable, Telecommunications, Toys
Figure 12: Example of ad with more than one logo.
& Games, Transportation, Travel &
Hospitality, Video Games.
C.3 Assigning Categories to Images
After assigning a category to each detected logo, we as-
signed a single category to each advertisement image. If
an advertisement contained one or more detected logos, we
first mapped each logo to its manually reviewed category.
We then assigned the advertisement to the category that ap-
peared most frequently among the detected logos in that
image. When multiple categories were tied for the highest
frequency, we randomly selected one of the tied categories.
Figure 12 shows an example of an advertisement containing
more than one detected logo.
D Categorizing Image Labels
We usedGoogle Cloud Vision API’slabel detection
function7 to automatically extract information about the en-
tities within our Ad screenshots. The model outputs a de-
scription, score, and topicality for each of the recognized en-
tities in the image. The model was run on the 11,647 screen-
shots identified as ads through our ad detection process.
The model was run on screenshots after the bottom 20%
and the top 9% of images were removed. The removal was
done to try to prevent the model from outputting “screen-
shot” or “mobile device” as entities (which were observed
when the full image was used as input).
We used a second LLM prompt to map the image-based
labels to the same 49 high-level categories used for logos,
7https://docs.cloud.google.com/vision/docs/labels

with an additionalOtherscategory used when none of the
49 categories applied. The prompt was:
“Add one CSV column namedcategory. Preserve
every existing row and field exactly. Return only CSV .
Allowed categories, exact spelling only:[Full
list of categories is then provided
here, one category on each line.
We also provide ‘‘Other’’ as an
option].
Decision rules:
• Pick one category per row. Never invent a category.
• UseOthersonly when absolutely none of the
non-Otherscategories can reasonably fit.
• If a label can plausibly fit any listed category,
choose that category instead ofOthers.
• Do not useOthersfor any recognizable prod-
uct type, media type, service, organization, team,
brand, place, activity, object, industry, or consumer
category.
• Categorize physical products by product type, not
by who uses them.”
The prompt also included examples and additional de-
cision rules for common ambiguous cases, such as map-
ping generic people, body, emotion, animal, weather, ma-
terial, and color labels toOthersunless they clearly re-
ferred to a product, service, industry, or consumer category.
The LLM mapped the 2,866 unique image-based labels into
the 49 substantive categories plusOthers. A member of
the research team then manually reviewed labels assigned to
Othersto verify that they did not reasonably fit any of the
49 substantive categories.
E Analyzing Interactions
E.1 Single Interaction Condition
Table 14 displays the number of content interacted with in
Study 1 in which we did a single interaction per account.
E.2 Multiple Interaction Condition
Table 13 displays the number of content interacted with in
Study 2, in which we performed a combination of interac-
tions within each account. Any interaction was programmed
to occur with a probability of 10%. Conditional on an inter-
action occurring, sharing was programmed to occur with a
probability of 2%. Given these probabilities, it is not unex-
pected that sharing never occurred.
F Study 1: Regression Model Including Age
& Gender
Table 15 displays a regression model for Study 1 data which
includes age and gender (in addition to interaction types and
total number of videos watched).Genderis coded 1 for the
“Jacob” and Michael” accounts and 0 for the “Emily” and
“Jennifer” accounts. The reference group forAgeis 26. The
impact of liking and sharing on increased ad load remains
statistically significant.

Round Device Jacob Emily Jennifer Michael
Like Comment Share Like Comment Share Like Comment Share Like Comment Share
1
Pixel 3a 94 – 58 7 – 1 0 – 0 119 – 63 8 – 0 0 – 0 94 – 49 8 – 5 0 – 0 111 – 70 3 – 1 0 – 0
Pixel 8 72 – 48 2 – 0 0 – 0 105 – 63 3 – 2 0 – 0 156 – 31 4 – 1 0 – 0 143 – 61 9 – 0 0 – 0
Galaxy S26+ 89 – 35 3 – 1 0 – 0 85 – 57 2 – 1 0 – 0 132 – 32 1 – 1 0 – 0 104 – 46 6 – 0 0 – 0
2
Pixel 3a 86 – 51 10 – 2 0 – 0 80 – 50 7 – 1 0 – 0 96 – 31 3 – 2 0 – 0 62 – 36 9 – 2 0 – 0
Pixel 8 55 – 43 0 – 2 0 – 0 81 – 40 3 – 2 0 – 0 89 – 29 1 – 0 0 – 0 90 – 58 2 – 1 0 – 0
Galaxy S26+ 100 – 23 2 – 1 0 – 0 123 – 44 7 – 0 0 – 0 115 – 50 6 – 1 0 – 0 109 – 54 5 – 5 0 – 0
Table 13: Number of Non-ad and ad content interacted with across our Study 2 data collection. Each cell shows (Non. Ad –
Ad) counts that have been interacted with.
Name Age Round Like Comment Share
Jacob 26 1 72 – 35 89 – 30 107 – 42
2 78 – 46 127 – 28 89 – 39
Emily 26 1 97 – 50 98 – 29 70 – 38
2 94 – 40 87 – 22 132 – 73
Michael 46 1 73 – 33 71 – 34 74 – 30
2 78 – 24 109 – 53 104 – 55
Jennifer 46 1 88 – 29 74 – 23 81 – 53
2 84 – 49 73 – 18 64 – 54
Table 14: Number of Non-ad and ad content interacted with
across our Study 1 data collection. Each cell shows (Non.
Ad – Ad) counts that have been interacted with.
PredictorβCoefficientp-value
β0 Intercept -112.0654 0.0171 ∗
β1 # Videos Watched 0.3480 0.0000 ∗∗∗
β2 Age -20.5270 0.1673
β3 Gender -8.1973 0.5636
β4 Liked 77.5491 0.0008 ∗∗∗
β5 Shared 135.2343 0.0000 ∗∗∗
β6 Commented 6.5105 0.7464
n= 32,R 2 = 0.8947, Adj.R 2 = 0.8695
Significance: ∗∗∗p <0.001 ∗p <0.05
Table 15: OLS regression model predicting the number of
ads based on interaction and demographic variables. Lik-
ing and sharing significantly increased ad count, while com-
menting had a positive but non-significant relationship.
