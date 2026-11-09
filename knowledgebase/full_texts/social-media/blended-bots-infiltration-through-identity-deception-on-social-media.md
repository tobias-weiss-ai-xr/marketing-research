---
title: 'Blended Bots: Infiltration through Identity Deception on Social Media'
url: https://arxiv.org/abs/2406.05246
category: social-media
subcategory: empirical
date: 2024-06
venue: ''
authors:
- Samantha C. Phillips
- Lynnette Hui Xian Ng
- Kathleen M. Carley
source: arxiv
pdf_url: https://arxiv.org/pdf/2406.05246
pages: 19
chars: 86706
fetched_at: '2026-11-08T13:09:06+00:00'
kb_version: 1
---

# Blended Bots: Infiltration through Identity Deception on Social Media

Blended Bots: Infiltration through Identity Deception on Social Media
Samantha C. Phillips1, Lynnette Hui Xian Ng1, Kathleen M. Carley1
1 Software and Societal Systems, Carnegie Mellon University
Pittsburgh, PA, United States
Abstract
Bots are automated social media users that can be used to am-
plify (mis)information and sow harmful discourse. In order to
effectively influence users, bots can be generated to reproduce
human user behavior. Indeed, people tend to trust information
coming from users with profiles that fit roles they expect to
exist, such as users with gender role stereotypes. In this work,
we examine differences in the types of identities in profiles
of human and bot accounts with a focus on combinations of
identities that represent gender role stereotypes. We find that
some types of identities differentiate between human and bot
profiles, confirming this approach can be a useful in distin-
guishing between human and bot accounts on social media.
However, contrary to our expectations, we reveal that gender
bias is expressed more in human accounts than bots overall.
Despite having less gender bias overall, we provide examples
of identities with strong associations with gender identities
in bot profiles, such as those related to technology, finance,
sports, and horoscopes. Finally, we discuss implications for
designing constructive social media bot detection.
Introduction
Social media provides wider and faster access to people and
information around the world. Concerningly, affordances of
social media, like anonymity, are leveraged by nefarious ac-
tors to spread misinformation and harmful narratives among
these online communication spaces (Kumar and Shah 2018;
Bradshaw and Howard 2018). These aims can be opera-
tionalized using automated accounts, that is, bots (Ferrara
et al. 2016). While bots are often useful (e.g., in crisis set-
tings (Hofeditz et al. 2019)) or benign, they can also be
used to deceive and manipulate users (Chang et al. 2021).
To effectively manipulate users, covert bots may attempt to
blend in as human accounts through presentation and be-
havior (Wischnewski et al. 2022; Freitas et al. 2015). Bots
that aim to imitate human behavior are often referred to as
“social bots” (Boshmaf et al. 2011; Stieglitz et al. 2017a,b;
Ferrara et al. 2016).
One common method social bots use to reproduce human
account behavior is to mimic user bios. A “bio” on a so-
cial media platform is a brief description of the account or
its owner (Madani et al. 2023). Users can select personal
Copyright © 2022, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
identifiers (any phrase that describes the owner of the so-
cial media account: social identities, preferences, activities,
and affiliations Pathak, Madani, and Joseph 2021) to put in
their profile (“self-presentation” Marwick and Boyd 2011)
that they believe are advantageous given their goals and per-
ceived audience. It follows that bots aiming to imperson-
ate human accounts can select certain identities to include
in their self-presentation, and therefore affiliate themselves
with their target community (Ng, Cruickshank, and Carley
2022).
Studies show that people tend to respond positively to in-
formation they are familiar with due to cognitive biases like
familiarity bias (Greul, Schweisfurth, and Raasch 2023). Fa-
miliarity is associated with increased trust in deceptive con-
tent (Zahari, Bilu, and Said 2019) and fellow social media
users (Shareef et al. 2020). Therefore, we propose that so-
cial media users may be less likely to classify another user
as a bot if their self-presentation contains expected combi-
nations of identities and attributes, that is, common stereo-
types. Gender role stereotypes are common combinations
of identities that are pervasive in news media (Armstrong,
Boyle, and McLeod 2012), entertainment (Ward and Grower
2020) and AI-generated content (Kotek, Dockum, and Sun
2023). Characterizing combinations of identities in the pro-
files of bot accounts informs training materials for both hu-
man and machine detection of bots (Kenny et al. 2023; Ng
and Carley 2023).
In this paper, we provide a large-scale quantitative com-
parison of identities in user profiles of accounts detected as
bots and not detected as bots. We focus this analysis on
gender role stereotypes by examining co-occurring identi-
ties with gender identities in bios. As such, we address the
following research questions:
RQ1: What types of identities are most and least
prevalent in bios of bot and human users?
RQ2: How do bot and human accounts present gen-
der in their bio?
RQ3: Is there more or less gender bias expressed in
bot or human user account bios? What types of iden-
tifiers are the most and least associated with gender
identities in bot accounts?
RQ4: What are the strongest associations with male
and female gender identities in bot accounts?
To address these research questions, we first employ a
arXiv:2406.05246v1  [cs.HC]  7 Jun 2024

bottom-up approach to extracting identifiers from a sam-
ple of approximately 50M X (formerly Twitter) users. We
then use 23 categories of identifiers including family, reli-
gion, age, ethnicity, and technology (Phillips, Carley, and
Joseph 2024). In RQ1, we confirm there are types of iden-
tities that are used disproportionately in profiles of human
accounts (family, religion, school, occupation, activism) and
types largely used by bots (relationship status, sex, technol-
ogy, finance).
In addition, we categorize gender identities into eight sub-
types: (female/male) pronouns, direct terms (e.g., woman,
lady), and family roles, as well as transgender and non-
binary/other. In RQ2 we find that human account bios con-
tain more female terms (e.g., woman, girl) and male pro-
nouns; and used more male and female family roles. Bots,
on the other hand, are more likely to include a male term in
their bio (e.g., man, boy, gentleman), suggesting limited use
of gender presentation to assimilate online.
Using the co-occurrences of extracted identifiers in bios,
we generate networks for bot and human users. We then
measure the difference in weighted log-odds with informa-
tive Dirichlet priors between male and female identities.
That is, we calculate the difference in co-occurrence of each
identity with male and female identities in bios while ac-
counting for the overall use of the identity. Contrary to our
initial assumptions, in RQ3, we show humans display more
bias along gender than bots overall and for the majority of
identifier types. Finally, in RQ4, we delve into specific ex-
amples of gender bias in bot accounts.
Contributions
Within this paper, we make the following contributions:
1. We describe a strategy for social bots to mimic human
users by including common combinations identities in
their profile, such as gender stereotypes.
2. We empirically demonstrate differences in identity use
and gender biases by human and bot accounts using a
large dataset of 50.1M X user profiles.
3. Our analyses reveal identities in bot profiles that reflect
gender biases, especially related to finance and technol-
ogy.
4. We discuss how the uncovered distinctions between bot
and human accounts from this work may be useful in au-
tomated and manual bot detection training.
Related works
Deception by Social Bots
Social bots have been observed using deception to effec-
tively spread disinformation (Varol and Uluturk 2019), and
promote propaganda (Jones 2019). In response to concerns
about the harmful effects of bots, many bot detection meth-
ods have been developed to differentiate real and fake ac-
counts using user meta data and behavior (Ng and Carley
2023; Morstatter et al. 2016; Varol et al. 2017; Beskow and
Carley 2018). Bots also have been shown to use specific lin-
guistic techniques in their messages (Addawood et al. 2019).
Relatedly, identity deception is prevalent on social media
(Alharbi et al. 2021; Van der Walt, Eloff, and Grobler 2018).
Identities in self-presentation can change how people per-
ceive that account. For example, there is evidence that bots
presented as female are more likely to be judged as human
(Borau et al. 2021). In other contexts, bots that present as
Black are judged as more trustworthy (Goble, Beattie, and
Edwards 2016).
Humans are generally inept at effectively distinguishing
between bot and human accounts (Kenny et al. 2024), gen-
erating feelings of uncertainty and lack of control. In these
contexts, people are more likely to rely on their (biased) in-
tuitions (Tversky and Kahneman 1974). Therefore, people
rely on overt signals of human-ness like holding certain so-
cial identities or stereotypes. In other words, they use famil-
iarity with the content to distinguish credible and incredible
information and sources (Greul, Schweisfurth, and Raasch
2023; Zahari, Bilu, and Said 2019; Shareef et al. 2020). This
work examines a pathway for bots to gain credibility and in-
filtrate online groups through use of commonly associated
identifiers concurrently with gender signals, as well as se-
lection of identifiers in their profile more broadly.
Measuring Gender Biases on Social Media
Research on gender bias in language and, more specifically,
descriptions of bios have been prominent. Numerous works
show pervasive gender biases in mainstream media (Asr
et al. 2021; Shor, Van De Rijt, and Fotouhi 2019), Wikipedia
(Graells-Garrido, Lalmas, and Menczer 2015), social media
(Usher, Holcomb, and Littman 2018; Marjanovic, Sta´nczak,
and Augenstein 2022), and search engines (Wijnhoven and
Van Haren 2021). Therefore, we expect gender bias in social
media content.
Gender bias can be operationalized as the extent to which
individual words and types of language are used by each
gender, or to describe the gender (Graells-Garrido, Lalmas,
and Menczer 2015; Guilbeault et al. 2024). Hence, gender
bias is determined by the association between words of iden-
tifiers and gender identities.
There are two broad approaches to measure associations
between words. The traditional approach is to use seman-
tic networks where nodes are words and edges denote co-
occurrence within a window of text. For example, previous
research measured associations between words and gender
terms using pointwise mutual information (Graells-Garrido,
Lalmas, and Menczer 2015). However, pointwise mutual
information over-weights scarcely used words and quanti-
fies association without considering the other side. Although
not directly applied to gender associations, work from the
late 2000s developed models to compare the associations of
terms in two or more sets of documents that include some
form of Bayesian prior (Monroe, Colaresi, and Quinn 2008).
For example, informative Dirichlet priors allow researchers
to account for overall use of a word in the corpus when
measuring associativity. In this way, the models proposed
by Monroe and colleagues provide a computationally inex-
pensive, interpretable approach that avoids over-weighting
of high- or low-frequency words.
Alternatively, in recent years, use of embeddings models

to represent words in a high-dimensional space has become
a popular way to assess associations between gender groups
and words (Charlesworth, Caliskan, and Banaji 2022; Guil-
beault et al. 2024). These methods typically involve fine-
tuning pretrained embeddings models using the texts of in-
terest. However, it can be difficult to assess the extent to
which the embeddings are based on the fine-tuning or ini-
tial training dataset.
Furthermore, there is evidence that these models innately
contain gender bias (Bhardwaj, Majumder, and Poria 2021;
Kotek, Dockum, and Sun 2023). Previous work demon-
strates that fine-tuned models largely preserve the structure
of the original model (Zhou and Srikumar 2021). For these
reasons, it may be challenging to determine what, if any,
gender bias in the fine-tuned model can be attributed to.
Therefore, it is not ideal for comparison of the degree of
gender bias of the same terms in different datasets. We could
train a word embedding model from scratch, like Word2Vec,
but we are still faced with possible weighting issues based
on the association measure selected. On the other hand, we
know directly using co-occurrences of identities are neces-
sarily sensitive to differences in language use and there are
network-based association measures that account for overall
use.
Data
This work uses the meta data of a sample of 50.1M X users
collected via Twitter API in June 2017. These users are a
sample of the most active users in 2010-2015, identified
using Twitter’s Decahose stream. In pre-processing, we re-
moved accounts with no bio or non-English bios.
Methods
Identity pre-processing
For each user in each time period, we extracted phrases from
bios using the method developed by Pathak, Madani, and
Joseph (2021). Their work develops the concept of a “per-
sonal identifier”—roughly, a phrase that signals identity—
and proposes a simple method to extract personal identifiers
from text. However, because their method generates noisy
phrases, we opt to develop methods to post-process the out-
put of their model, as well as methods to subsample to only
frequent phrases.
From the 11,141 phrases used by at least 1,000 users,
we extract 3,670 identifiers using labels from (Phillips,
Carley, and Joseph 2024). We evaluate identifiers cate-
gorized as: culture, nationality/location/ethnicity/race, oc-
cupation/industry, sports, school/subjects, technology/gam-
ing/cars, (social) media, horoscope, travel, religion, out-
doors/nature/animals, business/finance, activism, disabili-
ty/(mental) illness, sex, military, age, family, values, rela-
tionship status, sexuality/gender. A clarifying point: culture
refers to music, art, food, fashion, and other cultural prefer-
ences and roles. The category labels are also from (Phillips,
Carley, and Joseph 2024). Table 4 provides the identifiers in
each category.
Gender identities Of the selected identifiers, we labeled
those that explicitly reference gender; see Table 1. All au-
thors agreed on gender labels.
Associativity of Identities with Gender
We then measure the alignment of each identifier along gen-
der dimension (female - male) by calculating the difference
in weighted log-odds ratios with informative Dirichlet pri-
ors between the two groups (Monroe, Colaresi, and Quinn
2008) using the tidylo R package1. That is, the usage differ-
ence of identifier w between two groups i and j at time k is
calculated by
δ(i−j) kw = log
"
y(i) kw + α(i) kw
n(i) k + α(i) k0 − y(i) kw − α(i) kw
#
(1)
− log
"
y(j) kw + α(j) kw
n(j) k + α(j) k0 − y(j) kw − α(j) kw
#
(2)
where y(i) kw is the number of users that used an identifier in group i (e.g., left identifiers) and identifier w in time period
k, and n(i) k is the number of users that used an identifier in
group i. The informative prior is α(i) kw = y · α0 n , where α0 =P
w αw, α(i) k0 = P w α(i) w , y ∼ Multinomial(n, π) are the counts in the entire corpus,n = P w yw and π is a W -vector
of multinomial probabilities.
We can then divide by the standard deviation of δ(i−j) kw to obtain z-scores of the log-odds-ratios:
ζ (i−j) kw = ˆδ(i−j) kw /
q
σ2(ˆδ(i−j) kw ) (3)
Bot detection
We used BotBuster, a mixture-of-experts supervised ma-
chine learning architecture to differentiate bots and humans
(Ng and Carley 2023). This algorithm has been built and
tested on a variety of datasets, ranging from elections-based
data, fake follower bots and disinformation bots. In Bot-
Buster, bot probabilities of different data pillars are aggre-
gated together to classify the user. This dataset contains user
names, screen names and description but does not contain
the text of tweets. Therefore, only the BotBuster experts for
user meta data are activated and aggregated together. Bot-
Buster returns the probability of the account being a bot
(P (bot)), and the corresponding probability of the account
being a human ( P (human)). The account is classified as a
bot if P (bot) > P(human). Within our dataset, about 33%
of users are classified as bots.
Results
Comparison of types of identities in bios of bot and
human users (RQ1)
The difference in prevalence per 1 million users of each cat-
egory of identities in bot and human user profiles is pre-
sented in Figure 1. Human users tend to include family, re-
ligion, school/subjects, occupation, social activism, culture,
1https://github.com/juliasilge/tidylo

Category Identities
Female - pronouns she, her, hers
Female - roles woman, girl, lady, mrs, female, camgirl, happy girl, fangirl, small town girl, baby girl, babygirl,
businesswoman, country girl, blackgirlmagic, island girl, nasty woman, girly, crazy cat lady
Female - family sister, mummy, nana, aunt, momma, mom, stepmom, full time mommy, supermom, mompreneur,
grandma, housewife, mum, mother, devoted wife, teammommy, stay at home mom, house wife,
aunty, sahm, super mom, grandmother, mommy, big sister, being a mom, sis, mama, wife, mother-
hood, new mom, wifey, happy wife, granny, daughter, auntie, grammy, full time mom
Male - pronouns he, him, his
Male - roles gentleman, man, boy, mr, guy, male, country boy, renaissance man, outdoorsman, handyman, sports-
man, cameraman, businessman, simple man, common man, salesman, fisherman, it guy, all round
good guy, all around good guy, simple guy, all around nice guy, all round nice guy, nice guy
Male - family papa, lucky husband, father, devoted husband, uncle, proudfather, brother, godfather, grandfather,
happy husband, son, new dad, dad, grandad, hubby, nephew, full time dad, grandpa, daddy, husband
Transgender transgender, trans, ftm, mtf
Non-binary/other genderfluid, non-binary, nb
Table 1: Gender identities terms.
and health/illness identifiers more than bots. On the other
hand, bots include more relationship status, sex, technology,
and finance identifiers in their bio than human users.
Rather than attempt to describe a “human” behind the
screen, bots sometimes present the specific purpose of their
account. For example, bots have been documented spread-
ing financial (dis)information, which is reflected in the
disproportionate use of finance identities like “markets”,
“e-commerce”, “investing”, and “bitcoin” in bot profiles
(Tardelli et al. 2020). Moreover, bots are used to spread
pornographic content that may or may not be fake 2 with
identities in their bio like “porn”, “horny”, “nsfw”, and “18+
only”. Many of the technology identities in bot profiles re-
late to gaming: “gaming”, “call of duty”, “minecraft”. No-
tably, bots also include certain signals of relationship sta-
tus more than humans, such as “taken”, “in love with”, and
“happily taken”, which may be an attempt to adopt human-
like features. In sum, approximately 40% of the 23 cate-
gories of identities considered here clearly distinguish bot
and human users. This confirms (certain types of) identities
in bios can be a useful approach to differentiating between
human and bot accounts on social media.
Comparison of gender identities in bios of bot and
human users (RQ2)
Figure 2 indicates the difference in prevalence in gender
identities between the user types. As expected given RQ1 re-
sults, human accounts use far more male and female family
identities than bots. Interestingly, female terms like “girl”,
“woman” and “lady” are used more by human users, while
male terms like “male”, “boy”, “man”, and “mr” are used
far more by bots. However, male pronouns are used more by
human accounts and female pronouns are included at sim-
ilar rates for both types of users. Non-binary and transgen-
der identities also are largely not distinguished between user
2https://futurefive.co.nz/story/myspace-twitter-targets-for-
adult-spam
User type Top 20 gender identities
Bot girl, man, wife, guy, mother, father,
mom, husband, boy, he, her, she, his,
dad, mr, him, mommy, woman, daugh-
ter, son
Human girl, wife, father, mom, husband, man,
mother, guy, dad, he, her, his, she,
boy, daughter, woman, him, son, mr,
mommy
Table 2: Top gender identities used by user type
types, however, they also are very scarce in our dataset over-
all.
Table 2 contains the top used gender identities (in order)
for bot and human accounts. The order of use is not wildly
different for each user type, with the exception of male terms
included more by bots than human users. This may reflect
that bots have adapted to present themselves similarly to hu-
man accounts somewhat, although they are less likely to in-
clude gender signals than humans.
Comparison of gender bias in bios of bot and
human users (RQ3)
The distribution of differences in weighted log-odds along
the gender dimension are in Figure 3. Most notably, the dis-
tribution for identities in human profiles is wider than the
distribution for bots. In other words, we find stronger gen-
der bias in human accounts than bot accounts, contrary to
our initial assumptions.
Next, we consider the average absolute value of the
weighted difference in log-odds between male and female
edges (“strength of association”) for each type of identity in
Table 3. This provides a sense of the extent to which differ-
ent types of identities are divided in their use by gender—
and how it differs for human and bot accounts. Of the 23
types of identifiers, 15 showed significant differences in as-
sociation strengths between types of accounts ( α < 0.05).

Categoryˆ N Median (H) Median (B) T-statistic M/F
Family 46 10.7 6.2 3.21** F
Business/finance 34 8.8 5.5 2.65** M
Military 17 8.1 3.4 1.87 M
Technology/cars/gaming 170 7.8 5.1 4.23*** M
Occupation/industry 454 7.2 4.1 6.84*** M
Sports 424 7.0 3.9 7.81*** M
Sexuality 12 6.7 2.7 1.03 F
Relationship status 17 6.5 3.7 1.35 M
Religion 104 6.4 3.8 3.23** M
Nature/animals 125 5.9 3.3 3.89** M
Health 31 5.7 2.8 2.39* F
Culture 646 5.6 3.4 7.64*** F
Horoscope 26 5.4 3.3 2.82** F
Politics 60 4.9 3.1 2.05* M
Activism 63 4.4 2.8 2.3* F
School/subjects 231 3.6 2.1 4.74*** M
(Social) media 62 3.6 2.3 1.34 F
Travel 21 3.2 1.8 1.54 F
Race/ethnicity/location 373 3.1 1.9 6.17*** M
Values 17 2.8 2.1 0.91 M
Sex 19 2.8 2.6 0.82 F
Age 42 2.2 1.1 2.4* F
Table 3: ˆ Categories excluding gender identities. N is the number of identifiers in that category (excl. gender identities), median
(H) is the median absolute value of differences in co-occurrence with male and female signals for human accounts, median (B)
is the same for bot accounts, t-statistic is from a t-test comparing the strengths of associations with gender signals in human
and bot accounts for that category, and M/F represents if identifiers in that category are used with male (M) or female (F)
identities more on average. * signifies the significance at < 0.05, ** signifies significance at < 0.01, *** signifies significance
at < 0.0001.

Figure 1: Mean and 95% CI difference in prevalence per 1 million users for 23 types of identities. Lower (negative) values are
used more by bots, while higher (positive) values are used more by human users.
Figure 2: Mean and 95% CI difference in prevalence per 1M
for gender identities. Lower (negative) values are used more
by bots, while higher (positive) values are used more by hu-
man users.
Figure 3: Distribution of differences in weighted log-odds
with informative Dirichlet priors between male and female
identities for bot and human accounts.

These categories include family, finance, technology, occu-
pations, and culture. The remaining 8 categories, such as
sexuality and travel, were used to similar extents with both
genders across human and bot accounts. Therefore, while
gender bias is more prevalent in human accounts than bot
accounts overall, there is variation in the extent to which
they differ depending on the type of identifier.
For bots, the types of identifiers that are most biased by
gender are family, finance, technology, occupations, sports,
and religion. On the other hand, bot accounts with both male
and female gender signals include identifiers that reference
age, travel, race/ethnicity/location, school/subjects, and val-
ues in their profile to a similar extent. Echoing previous re-
sults, gender bias in bot accounts is not consistent across
types of identifiers and requires analysis of specific patterns
of associations.
Examples of gender bias in bot profiles (RQ4)
Gender role stereotypes can be expressed in a wide range of
forms, from occupations to cultural preferences. In this sec-
tion, we delve into the identifiers that co-occur the most with
gender signals in bot accounts. The identifiers used the most
in profiles with male identities (relative to female identi-
ties) are“sports”, “pastor”, “musician”, “golfer”, “engineer”,
“football”, “gamer”, “beer”, “dj”, “car”, and “god”. More
broadly, identifiers that relate to business/finance, technolo-
gy/cars/gaming, and sports are among the most used along-
side male identities of bot profiles.
On the other hand, the identifiers used the most in profiles
that contain female signals are “nurse”, “read”, “blogger”,
“beauty”, “fashion”, “makeup”, “actress”, “teacher”, “cat”,
and “crafter”. The types of identifiers that co-occur with fe-
male signals in bot profiles the most relate to health/illness,
travel, horoscope, and relationship status.
Discussion
Nefarious social bots are a social cyber-security threat (Car-
ley 2020) with the demonstrated ability to spread harm-
ful narratives (Chang et al. 2021) and facilitate fraud (Niz-
zoli et al. 2020). In this work, we describe and empirically
demonstrate a strategy for social bots to mimic human users
in an effort to effectively influence other users. Often, bots
are designed to amplify and disseminate messages quickly
and efficiently, rather than slowly infiltrate communities and
build credibility over time (Jacobs, Ng, and Carley 2023).
Many bots do not have any bio at all, hence we do not have
an estimate for this value. Here, we focus on bots that in-
clude identities in their profile, possibly to increase human-
like qualities and better blend in with a social network.
We use self-designated labels of binary gender (e.g., pro-
nouns, family roles) to examine existing identifier use and
gender biases in X user bios, where identifiers include so-
cial identities, preferences, activities, and affiliations. Using
self-designated labels provides the indication of the gender
that people affiliate themselves with, rather than a fully in-
ferred gender type.
Our findings reveal some types of identifiers are used
more in profiles of bots than human accounts, such as sex,
technology, and finance. This is especially relevant given the
recent influx of “porn bots” on X3. Profiles with these types
of identities, along with other attributes, may be among the
most recognizable by humans. Furthermore, bots often use
identities to refer to the purpose of the account rather than a
“human” behind the account.
Overall, bots do not use gender signals in their bio at the
same rate as human users. Moreover, humans use more iden-
tifiers that are strongly associated with one gender or the
other than bots. This contradicts our initial expectation that
bots will use exaggerated gender role stereotypes in an ef-
fort to invoke familiarity biases. However, we are still able
to find specific examples where bot profiles are biased by
gender. The most commonly co-occurring identifiers with
female identities in bot bios relate to beauty, art, and care-
taking occupations like nursing and teaching. Conversely,
the most commonly co-occurring identifiers with male iden-
tities are about sports, gaming, beer, and religion. The occu-
pations used with male signals in bot profiles the most are in
music or technical fields.
An aim of this paper is to encourage other researchers to
further investigate the ways social identities (e.g., gender,
age, religion) can be leveraged by malicious actors to in-
crease manipulation ability, especially in anonymous online
settings. It is also relevant to those studying AI-generated
content online, as many of the most popular models are rife
with biases (Kotek, Dockum, and Sun 2023). The content
generated by these models reflect the biases in the training
data, which is presumably mostly human generated. Iden-
tifying patterns of associations perpetuated by LLMs and
other forms of generative models may prove helpful in iden-
tifying AI-generated content from not.
Designing Constructive Bot Detection Guides Social
media platforms are conduits for individuals to share their
thoughts, however, this comes at a social cyber-security risk
(Carley 2020). In the digital world, where anonymity and
false identities are present, the analysis of the affiliation of
users and their behavior are important to differentiate truth
from false. It has been well-established that humans are not
very good at distinguishing between human and bot users
(Kenny et al. 2024) or AI- and human-generated (brief)
written self-presentations (Jakesch, Hancock, and Naaman
2023). This research contributes towards intelligent detec-
tion of deceptive entities (bots) on social media platforms.
Through understanding the self-presentation of bot and hu-
man identities, analysts can identify categories of identities
that clearly differentiate between both user types, like the
ones provided here. A multitude of tools have been devel-
oped to detect bots using certain characteristics such as the
rate of posting, follower/following ratio and so forth. Exam-
ples of such algorithms are Botometer and BotBuster (Ng
and Carley 2023; Yang, Ferrara, and Menczer 2022). Our
analysis can be used to inform future bot detection algo-
rithms, where detection models can be tuned to better lever-
age patterns of gender stereotypes to classify users as bots
and humans.
3https://www.rollingstone.com/culture/culture-features/
twitter-porn-bot-sex-meme-1234973030/

In addition, there is evidence that people can improve
their bot detection ability through training (Kenny et al.
2023). These trainings can be supplemented to include ex-
planations of how bots leverage human biases (e.g., con-
firmation bias) to gain influence, similar to existing mis-
information inoculation materials (Lewandowsky and Van
Der Linden 2021). Although many users who use gender
signals are indeed humans, profiles including gender role
stereotypes may warrant more consideration before being
trusted, especially if they relate to technology or business/-
finance.
Limitations and Future Work Gendered identities
evolve continually, and therefore the terms and identities
that we used may be outdated with the times (Levitt 2019).
Non-binary and transgender identities were very rare in this
dataset (<0.01% of bios) which may reflect the prevailing
gender trends of the time period in which the data is col-
lected; or the gaps in our extraction and/or labelling process;
or the trend of the inclusion of gender identities. Future work
involves exploring more divisions of gender identities, espe-
cially beefing up the set of terms that correspond to non-
binary or transgender identities within social media lingo.
Further, we do not attempt to classify the gender user pro-
file names or images. Name-based gender detection is not
straightforward, for a name can be representative as a fe-
male or male names (Van Buskirk, Clauset, and Larremore
2023; Lockhart, King, and Munsch 2023). While gender de-
tection in social media bios can be improved through image-
based gender detection (Schwemmer et al. 2020), studies
have shown that there are mismatches of gender from the
profile picture and the names, especially in bot accounts
(Yang, Singh, and Menczer 2024). The evolving definitions
of gender (Fraser 2015) and the displacement of gender be-
tween text and image makes gender detection in social me-
dia still an open research question. Future work should com-
pare gender identities presented through names, bios, and
images. Research shows a bio is not always necessary for a
bot to become influential (Aiello et al. 2012). Future work
should also empirically examine the extent of, if any, advan-
tage bots have by customizing their bio to include common
stereotypes.
Finally, the validity of the comparisons in this work hinge
on the correctness of BotBuster, the bot detection tool used
(Ng and Carley 2023). BotBuster was trained on several
manually annotated datasets with bot and human labels, sim-
ilar to other bot detection algorithms like Botometer (Varol
et al. 2017) and BotHunter (Beskow and Carley 2018). User
features, such as user bios, are used by these bot detection
algorithms to differentiate between human and bot users.
These algorithms consist of machine learning models, which
are generally black boxes. Recent work performed a feature
analysis study on BotBuster, showing that there are groups
of terms in bios that are more associated with bot accounts
(Ng and Carley 2024). These biases are perpetuated in clas-
sifications, biasing our analysis of differences in identity use
in bot and human profiles to some extent. Nonetheless, iden-
tities in bios is just one of many features used to differenti-
ate bot and human users by BotBuster. Future work should
compare differences in identities used by bot and human ac-
counts that are detected by other bot detection tools with our
results (e.g., Varol et al. (2017); Beskow and Carley (2018)).
Ethical statement The purpose of this work is to improve
understanding on how covert bots leverage gender biases in
their profile. We do not attempt to examine actual gender
differences in specific identities. While the work can inform
researchers building bot detection algorithms, this work can
also be used by nefarious bot operators to avoid detection
and build workarounds. Nonetheless, it is still important to
understand the existence of differences of identities between
bots and humans as a research problem, such that it can be
continually studied and used as indicators for the evolution
of bots and the need for algorithm refresh.
References
Addawood, A.; Badawy, A.; Lerman, K.; and Ferrara, E.
2019. Linguistic cues to deception: Identifying political
trolls on social media. In Proceedings of the international
AAAI conference on web and social media , volume 13, 15–
25.
Aiello, L. M.; Deplano, M.; Schifanella, R.; and Ruffo, G.
2012. People are strange when you’re a stranger: Impact
and influence of bots on social networks. In Proceedings of
the international AAAI conference on web and social media ,
volume 6, 10–17.
Alharbi, A.; Dong, H.; Yi, X.; Tari, Z.; and Khalil, I. 2021.
Social Media Identity Deception Detection: A Survey. ACM
Comput. Surv., 54(3).
Armstrong, C. L.; Boyle, M. P.; and McLeod, D. M. 2012.
A global trend: How news coverage of protests reinforces
gender stereotypes. Journalism Studies, 13(4): 633–648.
Asr, F. T.; Mazraeh, M.; Lopes, A.; Gautam, V .; Gonzales,
J.; Rao, P.; and Taboada, M. 2021. The gender gap tracker:
Using natural language processing to measure gender bias
in media. PloS one, 16(1): e0245533.
Beskow, D. M.; and Carley, K. M. 2018. Bot-hunter: a tiered
approach to detecting & characterizing automated activity
on twitter. In Conference paper . SBP-BRiMS: International
conference on social computing, behavioral-cultural model-
ing and prediction and behavior representation in modeling
and simulation, volume 3.
Bhardwaj, R.; Majumder, N.; and Poria, S. 2021. Investi-
gating gender bias in bert. Cognitive Computation , 13(4):
1008–1018.
Borau, S.; Otterbring, T.; Laporte, S.; and Fosso Wamba,
S. 2021. The most human bot: Female gendering increases
humanness perceptions of bots and acceptance of AI. Psy-
chology & Marketing, 38(7): 1052–1068.
Boshmaf, Y .; Muslukhov, I.; Beznosov, K.; and Ripeanu, M.
2011. The socialbot network: when bots socialize for fame
and money. In Proceedings of the 27th annual computer
security applications conference, 93–102.
Bradshaw, S.; and Howard, P. N. 2018. Challenging truth
and trust: A global inventory of organized social media ma-
nipulation. The computational propaganda project, 1: 1–26.

Carley, K. M. 2020. Social cybersecurity: an emerging sci-
ence. Computational and mathematical organization theory,
26(4): 365–381.
Chang, H.-C. H.; Chen, E.; Zhang, M.; Muric, G.; and Fer-
rara, E. 2021. Social bots and social media manipulation in
2020: the year in review. In Handbook of Computational
Social Science, V olume 1, 304–323. Routledge.
Charlesworth, T. E.; Caliskan, A.; and Banaji, M. R. 2022.
Historical representations of social groups across 200 years
of word embeddings from Google Books. Proceedings of
the National Academy of Sciences , 119(28): e2121798119.
Ferrara, E.; Varol, O.; Davis, C.; Menczer, F.; and Flammini,
A. 2016. The rise of social bots. Communications of the
ACM, 59(7): 96–104.
Fraser, L. 2015. Gender dysphoria: definition and evolution
through the years. In Management of gender dysphoria: A
multidisciplinary approach, 19–31. Springer.
Freitas, C.; Benevenuto, F.; Ghosh, S.; and Veloso, A. 2015.
Reverse engineering socialbot infiltration strategies in twit-
ter. In Proceedings of the 2015 IEEE/ACM International
Conference on Advances in Social Networks Analysis and
Mining 2015, 25–32.
Goble, H.; Beattie, A. J.; and Edwards, C. 2016. The impact
of twitterbot race on interpersonal impressions.Impressions,
48(1).
Graells-Garrido, E.; Lalmas, M.; and Menczer, F. 2015. First
women, second sex: Gender bias in Wikipedia. In Proceed-
ings of the 26th ACM conference on hypertext & social me-
dia, 165–174.
Greul, A.; Schweisfurth, T. G.; and Raasch, C. 2023. Does
familiarity with an idea bias its evaluation? Plos one, 18(7):
e0286968.
Guilbeault, D.; Delecourt, S.; Hull, T.; Desikan, B. S.; Chu,
M.; and Nadler, E. 2024. Online images amplify gender bias.
Nature, 1–7.
Hofeditz, L.; Ehnis, C.; Bunker, D.; Brachten, F.; and
Stieglitz, S. 2019. Meaningful Use of Social Bots? Possi-
ble Applications in Crisis Communication during Disasters.
In ECIS, 1–16.
Jacobs, C. S.; Ng, L. H. X.; and Carley, K. M. 2023. Track-
ing China’s cross-strait bot networks against Taiwan. In
International conference on social computing, behavioral-
cultural modeling and prediction and behavior representa-
tion in modeling and simulation , 115–125. Springer.
Jakesch, M.; Hancock, J. T.; and Naaman, M. 2023. Hu-
man heuristics for AI-generated language are flawed. Pro-
ceedings of the National Academy of Sciences , 120(11):
e2208839120.
Jones, M. O. 2019. The gulf information war— propaganda,
fake news, and fake trends: The weaponization of twitter
bots in the gulf crisis. International journal of communi-
cation, 13: 27.
Kenny, R.; Fischhoff, B.; Davis, A.; and Canfield, C. 2023.
Improving Social Bot Detection Through Aid and Training.
Human Factors, 00187208231210145.
Kenny, R.; Fischhoff, B.; Davis, A.; Carley, K. M.; and Can-
field, C. 2024. Duped by bots: why some are better than
others at detecting fake social media personas. Human fac-
tors, 66(1): 88–102.
Kotek, H.; Dockum, R.; and Sun, D. 2023. Gender bias and
stereotypes in large language models. In Proceedings of The
ACM Collective Intelligence Conference, 12–24.
Kumar, S.; and Shah, N. 2018. False information on web and
social media: A survey. arXiv preprint arXiv:1804.08559.
Levitt, H. M. 2019. A psychosocial genealogy of LGBTQ+
gender: An empirically based theory of gender and gender
identity cultures. Psychology of Women Quarterly , 43(3):
275–297.
Lewandowsky, S.; and Van Der Linden, S. 2021. Counter-
ing misinformation and fake news through inoculation and
prebunking. European Review of Social Psychology , 32(2):
348–384.
Lockhart, J. W.; King, M. M.; and Munsch, C. 2023. Name-
based demographic inference and the unequal distribution
of misrecognition. Nature Human Behaviour , 7(7): 1084–
1095.
Madani, N.; Bandyopadhyay, R.; Yoder, M. M.; and Joseph,
K. 2023. Measuring Stereotypes using Entity-Centric Data.
arXiv preprint arXiv:2305.09548.
Marjanovic, S.; Sta ´nczak, K.; and Augenstein, I. 2022.
Quantifying gender biases towards politicians on Reddit.
PloS one, 17(10): e0274317.
Marwick, A. E.; and Boyd, D. 2011. I tweet honestly, I tweet
passionately: Twitter users, context collapse, and the imag-
ined audience. New media & society , 13(1): 114–133.
Monroe, B. L.; Colaresi, M. P.; and Quinn, K. M. 2008.
Fightin’words: Lexical feature selection and evaluation for
identifying the content of political conflict. Political Analy-
sis, 16(4): 372–403.
Morstatter, F.; Wu, L.; Nazer, T. H.; Carley, K. M.; and Liu,
H. 2016. A new approach to bot detection: striking the bal-
ance between precision and recall. In2016 IEEE/ACM Inter-
national Conference on Advances in Social Networks Anal-
ysis and Mining (ASONAM), 533–540. IEEE.
Ng, L. H. X.; and Carley, K. M. 2023. Botbuster: Multi-
platform bot detection using a mixture of experts. In Pro-
ceedings of the International AAAI Conference on Web and
Social Media, volume 17, 686–697.
Ng, L. H. X.; and Carley, K. M. 2024. Assembling a multi-
platform ensemble social bot detector with applications to
US 2020 elections. Social Network Analysis and Mining ,
14(1): 1–16.
Ng, L. H. X.; Cruickshank, I. J.; and Carley, K. M. 2022.
Cross-platform information spread during the January 6th
capitol riots. Social Network Analysis and Mining , 12(1):
133.
Nizzoli, L.; Tardelli, S.; Avvenuti, M.; Cresci, S.; Tesconi,
M.; and Ferrara, E. 2020. Charting the landscape of on-
line cryptocurrency manipulation. IEEE access, 8: 113230–
113245.

Pathak, A.; Madani, N.; and Joseph, K. 2021. A method
to analyze multiple social identities in twitter bios. Pro-
ceedings of the ACM on Human-Computer Interaction ,
5(CSCW2): 1–35.
Phillips, S. C.; Carley, K. M.; and Joseph, K. 2024. Why do
people think liberals drink lattes? How social media afforded
self-presentation can shape subjective social sorting. arXiv
preprint arXiv:2404.02338.
Schwemmer, C.; Knight, C.; Bello-Pardo, E. D.; Oklobdz-
ija, S.; Schoonvelde, M.; and Lockhart, J. W. 2020. Diag-
nosing gender bias in image recognition systems. Socius, 6:
2378023120967171.
Shareef, M. A.; Kapoor, K. K.; Mukerji, B.; Dwivedi, R.;
and Dwivedi, Y . K. 2020. Group behavior in social media:
Antecedents of initial trust formation. Computers in Human
Behavior, 105: 106225.
Shor, E.; Van De Rijt, A.; and Fotouhi, B. 2019. A large-
scale test of gender bias in the media. Sociological Science,
6: 526.
Stieglitz, S.; Brachten, F.; Berthel ´e, D.; Schlaus, M.; Vene-
topoulou, C.; and Veutgen, D. 2017a. Do social bots (still)
act different to humans?–Comparing metrics of social bots
with those of humans. In Social Computing and Social Me-
dia. Human Behavior: 9th International Conference, SCSM
2017, Held as Part of HCI International 2017, V ancouver ,
BC, Canada, July 9-14, 2017, Proceedings, Part I 9 , 379–
395. Springer.
Stieglitz, S.; Brachten, F.; Ross, B.; and Jung, A.-K.
2017b. Do social bots dream of electric sheep? A cat-
egorisation of social media bot accounts. arXiv preprint
arXiv:1710.04044.
Tardelli, S.; Avvenuti, M.; Tesconi, M.; and Cresci, S. 2020.
Characterizing social bots spreading financial disinforma-
tion. In International conference on human-computer in-
teraction, 376–392. Springer.
Tversky, A.; and Kahneman, D. 1974. Judgment under Un-
certainty: Heuristics and Biases: Biases in judgments re-
veal some heuristics of thinking under uncertainty. science,
185(4157): 1124–1131.
Usher, N.; Holcomb, J.; and Littman, J. 2018. Twitter makes
it worse: Political journalists, gendered echo chambers, and
the amplification of gender bias. The international journal
of press/politics, 23(3): 324–344.
Van Buskirk, I.; Clauset, A.; and Larremore, D. B. 2023.
An open-source cultural consensus approach to name-based
gender classification. In Proceedings of the International
AAAI Conference on Web and Social Media , volume 17,
866–877.
Van der Walt, E.; Eloff, J. H.; and Grobler, J. 2018. Cyber-
security: Identity deception detection on social media plat-
forms. Computers & Security, 78: 76–89.
Varol, O.; Ferrara, E.; Davis, C.; Menczer, F.; and Flam-
mini, A. 2017. Online human-bot interactions: Detection,
estimation, and characterization. In Proceedings of the in-
ternational AAAI conference on web and social media , vol-
ume 11, 280–289.
Varol, O.; and Uluturk, I. 2019. Deception strate-
gies and threats for online discussions. arXiv preprint
arXiv:1906.11371.
Ward, L. M.; and Grower, P. 2020. Media and the develop-
ment of gender role stereotypes. Annual Review of Develop-
mental Psychology, 2: 177–199.
Wijnhoven, F.; and Van Haren, J. 2021. Search engine gen-
der bias. Frontiers in big Data, 4: 29.
Wischnewski, M.; Ngo, T.; Bernemann, R.; Jansen, M.; and
Kr¨amer, N. 2022. “I agree with you, bot!” How users (dis)
engage with social bots on Twitter. New Media & Society ,
14614448211072307.
Yang, K.-C.; Ferrara, E.; and Menczer, F. 2022. Botometer
101: Social bot practicum for computational social scien-
tists. Journal of computational social science , 5(2): 1511–
1528.
Yang, K.-C.; Singh, D.; and Menczer, F. 2024. Character-
istics and prevalence of fake social media profiles with AI-
generated faces. arXiv preprint arXiv:2401.02627.
Zahari, A. I.; Bilu, R.; and Said, J. 2019. The role of famil-
iarity, trust and awareness towards online fraud. Journal of
Research and Opinion, 6(9): 2470–2480.
Zhou, Y .; and Srikumar, V . 2021. A closer look at how fine-
tuning changes BERT. arXiv preprint arXiv:2106.14282.
Acknowledgments. This work was supported in part by
the Knight Foundation and the Office of Naval Research
grant Minerva-Multi-Level Models of Covert Online Infor-
mation Campaigns, N000142112765, N000141812106, and
N000141812108. Additional support was provided by the
center for Informed Democracy and Social-cybersecurity
(IDeaS) and the center for Computational Analysis of So-
cial and Organizational Systems (CASOS) at Carnegie Mel-
lon University. The views and conclusions contained in this
document are those of the authors and should not be inter-
preted as representing the official policies, either expressed
or implied, of the Knight Foundation, Office of Naval Re-
search, or the U.S. Government.

Identifier type Identifiers
(social) media [’news’, ’social media specialist’, ’twitch streamer’, ’vlogger’, ’food blogger’, ’content strate-
gist’, ’pjnet’, ’current affairs’, ’content creator’, ’broadcast journalist’, ’tyler oakley’, ’youtube
addict’, ’blogger’, ’tweeter’, ’journalism’, ’multimedia journalist’, ’bbc’, ’retweeter’, ’social
media addict’, ’kian lawley’, ’social media expert’, ’troll’, ’social media manager’, ’digitalmar-
keting’, ’wsj’, ’dolan twins’, ’cameron dallas’, ’streamer’, ’social media marketer’, ’youtube
content creator’, ’gab’, ’watching youtube’, ’blog’, ’columbiajourn’, ’columnist’, ’media’,
’politico’, ’youtube gamer’, ’social media guru’, ’content marketing’, ’social media consultant’,
’youtuber’, ’social media junkie’, ’youtubers’, ’social media enthusiast’, ’jacobsartorius’, ’joe
sugg’, ’reporter’, ’small youtuber’, ’social media strategist’, ’occasional blogger’, ’broadcaster’,
’journalist’, ’influencer’, ’make youtube videos’, ’npr’, ’cnn’, ’amazingphil’, ’camerondallas’,
’blogging’, ’nytimes’, ’tgdn’]
activism [’community activist’, ’revolutionary’, ’rotarian’, ’pacifist’, ’unity’, ’nationalist’, ’intersectional
feminist’, ’community manager’, ’advocate’, ’community builder’, ’woke’, ’loveislove’, ’hu-
manist’, ’environmentalist’, ’social issues’, ’feminism’, ’justice’, ’environmental’, ’ally’, ’con-
servationist’, ’freepalestine’, ’humanitarian’, ’jft96’, ’activist’, ’community organizer’, ’femi-
nist’, ’allblacklivesmatter’, ’blacklivesmatter’, ’2a’, ’alllivesmatter’, ’nodapl’, ’world changer’,
’social justice’, ’nra’, ’prolife’, ’concerned citizen’, ’advocacy’, ’theresistance’, ’guns’, ’so-
cialjustice’, ’freemason’, ’equity’, ’philanthropist’, ’community leader’, ’repealthe8th’, ’sus-
tainability’, ’humanrights’, ’activism’, ’community volunteer’, ’social activist’, ’bluelivesmat-
ter’, ’climate change’, ’volunteering’, ’giver’, ’change agent’, ’conservation’, ’1a’, ’volunteer’,
’human rights’, ’blm’, ’lovewins’, ’resistance’, ’tgdn’]
age [’class of 2018’, ’23 years old’, ”o ’17”, ’17 years old’, ’21 years old’, ’adult’, ’19 y’, ’11 years
old’, ’13 years old’, ’18 y’, ’gatornation’, ’18 years old’, ’millennial’, ’high school’, ’teen’, ’27
years old’, ’young’, ’8th grade’, ’25 years old’, ’teenager’, ’16 years old’, ’class of 2017’, ’13
years young’, ’o 2015’, ”class of ’18”, ’20 years old’, ’sophomore’, ’grown’, ’22 years old’, ’o
2016’, ’12 years old’, ’old’, ’class of 2016’, ’freshman’, ’24 years old’, ’19 years old’, ’26 years
old’, ’15 years old’, ”90’s baby”, ’14 years old’, ’16 years young’, ’senior’]
business/finance [’financial’, ’economy’, ’e-commerce’, ’investing’, ’brokerage’, ’management’, ’business’,
’starbucks’, ’entrepreneurship’, ’entrepreneurial’, ’fintech’, ’startup’, ’founder’, ’startups’,
’nike’, ’international business’, ’stock trader’, ’markets’, ’bitcoin’, ’trading’, ’investment’,
’mlm’, ’finance’, ’sony’, ’stocks’, ’investments’, ’investor’, ’marketing’, ’forex trader’, ’com-
pany’, ’billionaire’, ’microsoft’, ’ibm’, ’corporate’]

culture [’cheese lover’, ’weeknd’, ’cinephile’, ’dj’, ’caterer’, ’loves to cook’, ’justin bieber’, ’the-
weeknd’, ’remixer’, ’chris smith’, ’bibliophile’, ’foody’, ’louis tomlinson’, ’performing’, ’quil-
ter’, ’supergirl’, ’kdrama’, ’u2’, ’shawn mendes’, ’john cena’, ’shopaholic’, ’comic books’,
’voice’, ’food eater’, ’rihanna’, ’dexter’, ’tattoos’, ’sketching’, ’twenty one pilots’, ’curry’,
’bap’, ’gaga’, ’9teen’, ’ed sheeran’, ’bathroom singer’, ’sci fi’, ’playwright’, ’zayn malik’,
’poker player’, ’artists’, ’ofwgkta’, ’mumbaikar’, ’food blogger’, ’country music’, ’house mu-
sic’, ’cinematographer’, ’picture taker’, ’food lover’, ’shoe lover’, ’singers’, ’wonder woman’,
’anglophile’, ’freelance writer’, ’walking dead’, ’ahs’, ’dubstep’, ’reggae’, ’literature’, ’tak-
ing photos’, ’harry styles’, ’tv junkie’, ’ballet’, ’troye sivan’, ’spongebob’, ’renaissance man’,
’nct’, ’gypsy’, ’archivist’, ’portrait photographer’, ’cosplay’, ’writer’, ’alt’, ’zumba’, ’bts’,
’dancehall’, ’musicals’, ’twilight’, ’debate’, ’make stuff’, ’one direction’, ’janoskians’, ’poems’,
’blues’, ’fruit’, ’guitarist’, ’craft beers’, ’hobbit’, ’story teller’, ’writter’, ’booklover’, ’cine-
matography’, ’transformers’, ’crocheter’, ’composer’, ’divergent’, ’arianagrande’, ’watch tv’,
’knitter’, ’chess’, ’michael clifford’, ’fifth harmony’, ’drums’, ’disney’, ’pizza enthusiast’, ’de-
sign’, ’write’, ’lyricist’, ’sound designer’, ’ymcmb’, ’song-writer’, ’multi-instrumentalist’, ’be-
ingsalmankhan’, ’bookworm’, ’beatboxer’, ’bieber’, ’photog’, ’retro’, ’instrumentalist’, ’illus-
tration’, ’actress’, ’directioner’, ’films’, ’songwriters’, ’pianist’, ’sew’, ’classic rock’, ’riverdale’,
’wannabe writer’, ’photo editor’, ’song writter’, ’radio’, ’criminal minds’, ’loves reading’,
’wordsmith’, ’at the disco’, ’marching band’, ’visual designer’, ’flash’, ’cooking’, ’crafts’,
’audiophile’, ’podcast host’, ’ikon’, ’crochet’, ’author’, ’vocalist’, ’videographer’, ’tv host’,
’pop’, ’pll’, ’superman’, ’pizza lover’, ’pastry chef’, ’raver’, ’rockstar’, ’superhero’, ’shakira’,
’new music’, ’anime’, ’reiki master’, ’indie’, ’upcoming artist’, ’choreographer’, ’arianator’,
’weeb’, ’loves cooking’, ’photojournalist’, ’alternative’, ’artwork’, ’survivor’, ’dancing’, ’srk’,
”dylan o’brien”, ’punk’, ’selenagomez’, ’graphics designer’, ’play bass’, ’amwriting’, ’cup-
cake’, ’exo’, ’always hungry’, ’gluten free’, ’entertainment’, ’record producer’, ’harmonizer’,
’bollywood’, ’ukulele’, ’breaking bad’, ’painting’, ’gotham’, ’d&d’, ’cartoonist’, ’big brother’,
’drinker’, ’minimalist’, ’tv watcher’, ’novels’, ’roman reigns’, ’screenwriter’, ’superheroes’, ’tea
enthusiast’, ’drunk’, ’boybands’, ’artist’, ’create’, ’nani’, ’sherlockian’, ’taking pictures’, ’craft
beer enthusiast’, ’starbucks’, ’scotch’, ’art’, ’beat maker’, ’make music’, ’seuss’, ’books’, ’pi-
ano’, ’performing arts’, ’paint’, ’steampunk’, ’interior designer’, ’tea addict’, ’comic’, ’bbq’,
’loves music’, ’jack johnson’, ’pokemon’, ’beets’, ’debater’, ’copywriter’, ’bourbon’, ’watch
movies’, ’larry stylinson’, ’performer’, ’starwars’, ’sherlock’, ’paramore’, ’graphic design’,
’cameraman’, ’kanye west’, ’khan’, ’making videos’, ’funk’, ’cinema’, ’hamilton’, ’cigars’,
’otaku’, ’musicislife’, ’kiwi’, ’coco chanel’, ’3d artist’, ’trancefamily’, ’animation’, ’percus-
sionist’, ’knit’, ’ladygaga’, ’beer’, ’tv producer’, ’veggie’, ’podcasts’, ’comedian’, ’bmth’, ’tv
addict’, ’magcon’, ’occasional writer’, ’performing artist’, ’cartoons’, ’craft beer lover’, ’song
writer’, ’arctic monkeys’, ’read’, ’vagabond’, ’tv presenter’, ’seamstress’, ’vocals’, ’1975’, ’spn-
family’, ’captain of my soul’, ’rattpack’, ’classics’, ’cold beer’, ’illustrator’, ’harry styles’, ’pot-
terhead’, ’edm’, ’paleo’, ’gleek’, ’r&b’, ’halsey’, ’coldplay’, ’1d’, ’reading’, ’j cole’, ’graphic’,
’amateur chef’, ’designer’, ’taylor swift’, ’k-pop’, ’eater’, ’editing’, ’aspiring artist’, ’sneakers’,
’cole world’, ’bands’, ’die hard’, ’play guitar’, ’band obsessed’, ’thespian’, ’artiste’, ’wino’,
’justinbieber’, ’metallica’, ’brewer’, ’little mix’, ’taco bell’, ’loves photography’, ’kurt cobain’,
’sneaker head’, ’drinking’, ’novelist’, ’techno’, ’good book’, ’ariana grande’, ’sketch’, ’wood-
worker’, ’marvel’, ’play music’, ’dancer’, ’fashionista’, ’amateur photographer’, ’chocolate
addict’, ’interior design’, ’harrypotter’, ’skinhubsquad’, ’rap’, ’shawol’, ’image consultant’,
’dance’, ’documentary filmmaker’, ’cartoon’, ’mgk’, ’rapper’, ’zendaya’, ’chocoholic’, ’mu-
siclover’, ’deadpool’, ’taylorswift13’, ’drawer’, ’teenwolf’, ’keyboardist’, ’2ne1’, ’photogra-
phy’, ’coleworld’, ’drink beer’, ’peter pan’, ’good music’, ’lana del rey’, ’camera’, ’drink cof-
fee’, ’fashion’, ’loves to sing’, ’storyteller’, ’sag’, ’violinist’, ’good beer’, ’improv’, ’sneak-
erhead’, ’drum’, ’sam smith’, ’heavy metal’, ’music’, ’katy perry’, ’favorite movie’, ’bruno
mars’, ’dancers’, ’outlander’, ’animator’, ’rocker’, ’tattoo’, ’salsa’, ’voracious reader’, ’draw-
ing’, ’musician’, ’disneyland’, ’guitar’, ’trekkie’, ’potter’, ’musical’, ’avenged sevenfold’,
’swiftie’, ’snsd’, ’francophile’, ’zquad’, ’graphicdesigner’, ’selena gomez’, ’cook’, ’home-
brewer’, ’video’, ’lotr’, ’lovatic’, ’doctorwho’, ’salman khan’, ’melanie martinez’, ’percussion’,
’voiceover’, ’disco’, ’demi lovato’, ’gameofthrones’, ’belieber’, ’spoken word artist’, ’whovian’,
’oitnb’, ’published author’, ’teen wolf’, ’simba’, ’make beats’, ’watching movies’, ’staff writer’,
’baking’, ’movies’, ’mark twain’, ’linkin park’, ’liam payne’, ’diehard’, ’soprano’, ’reader’,
’union j’, ’podcaster’, ’poet’, ’melody’, ’hip hop’]

culture cont. [’oasis’, ’tv fanatic’, ’diyer’, ’visual artist’, ’harry potter’, ’elvis’, ’arts’, ’basshead’, ’sci-fi’,
’shakespeare’, ’frozen’, ’trumpet’, ’comics’, ’violin’, ’eminem’, ’tattoo artist’, ’cookie mon-
ster’, ’take photos’, ’rock’, ’vampire diaries’, ’movie’, ’ncis’, ’katyperry’, ’vocal coach’, ’loves
anime’, ’script writer’, ’enjoy reading’, ’cosplayer’, ’cheesecake’, ’americana’, ’beatles’, ’stand
up comedian’, ’poetry’, ’game of thrones’, ’film’, ’aspiring author’, ’star trek’, ’recording artist’,
’filmmaking’, ’salman’, ’red velvet’, ’tyga’, ”grey’s anatomy”, ’gossip girl’, ’culture’, ’brony’,
’stage manager’, ’artisan’, ’food addict’, ’theater’, ’book’, ’hard rock’, ’songwriter’, ’reality
tv junkie’, ’electro’, ’tolkien’, ’choir’, ’manga’, ’food enthusiast’, ’batman’, ’5 seconds of
summer’, ’baker’, ’imagine dragons’, ’saxophonist’, ’chef’, ’foodie’, ’hunger games’, ’band
geek’, ’bring me the horizon’, ’painter’, ’suits’, ’meditator’, ’jordy’, ’make videos’, ’rhian-
non’, ’pink floyd’, ’filmmaker’, ’acting’, ’vfx’, ’songs’, ’opera singer’, ’food junkie’, ’enter-
tainer’, ’drummer’, ’watching tv’, ’television’, ’tea lover’, ’onedirection’, ’jedi’, ’drama’, ’tv
personality’, ’barista’, ’whiskey’, ’battlestar galactica’, ’play the guitar’, ’niallofficial’, ’cof-
fee’, ’pizza expert’, ’real liam payne’, ’philadelphia’, ’fiction’, ’beyhive’, ’iamsrk’, ’costume
designer’, ’metal’, ’selenator’, ’foodlover’, ’eat’, ’bake’, ’shadowhunters’, ’comedy’, ’scrap-
booker’, ’adele’, ’ska’, ’fall out boy’, ’sound engineer’, ’videos’, ’singer’, ’michael jackson’,
’miley cyrus’, ’guitars’, ’harley quinn’, ’doodler’, ’chocolate lover’, ’cellist’, ’actor’, ’bey-
once’, ’craftbeer’, ’play piano’, ’scriptwriter’, ’trance’, ’mcfly’, ’nickiminaj’, ’star wars’, ’hor-
ror’, ’5sos’, ’diet’, ’moonchild’, ’book lover’, ’monsta x’, ’concept artist’, ’kpop’, ’r5’, ’draw-
ings’, ’nutrition’, ’troye’, ’food fanatic’, ’fusion’, ’technical writer’, ’master of none’, ’impro-
viser’, ’bass’, ’acoustic’, ’mcr’, ’play drums’, ’tea drinker’, ’blondie’, ’copy editor’, ’grunge’,
’watching anime’, ’teambreezy’, ’hip-hop’, ’thewalkingdead’, ’jetlife’, ’flute’, ’metalhead’,
’home brewer’, ’got7’, ’singing’, ’beef’, ’graphic designer’, ’hiphop’, ’draw’, ’uke’, ’broad-
way’, ’sculptor’, ’scifi’, ’blackpink’, ’nirvana’, ’visual arts’, ’brewers’, ’glee’, ’making music’,
’pineapples’, ’aspiring writer’, ’recording engineer’, ’chris brown’, ’crafter’, ’take pictures’,
’concert goer’, ’writing’, ’nash grier’, ’trap’, ’vegetarian’, ’superwoman’, ’cake decorator’,
’bassist’, ’photographer’, ’nicki minaj’, ’listen to music’, ’avid reader’, ’demi’, ’theatre’, ’make
art’, ’fine artist’, ’listening to music’, ’igot7’, ’wine’, ’jazz’, ’niall horan’, ’beatmaker’, ’lead
singer’, ’vegan’, ’home cook’, ’amateur writer’, ’illustrations’, ’sing’]
disability/(mental)
illness
[’adhd’, ’diabetic’, ’ocd’, ’hiv’, ’addict’, ’suicidal’, ’diabetes’, ’disabled’, ’disability’, ’anxi-
ety’, ’breast cancer survivor’, ’depressed’, ’autism’, ’autistic’, ’t1d’, ’self harm’, ’nfb’, ’depres-
sion’, ’ptsd’, ’type 1 diabetic’, ’mental health’, ’fuckcancer’, ’deaf’, ’caffeine addict’, ’spoonie’,
’bipolar’, ’alcoholic’, ’fibromyalgia’, ’addiction’, ’mentalhealth’, ’sober’]
family [’full time mom’, ’sister’, ’thefamily’, ’my wife’, ’mummy’, ’parent’, ’nana’, ’homemaker’,
’aunt’, ’family’, ’momma’, ’mom’, ’papa’, ’lucky husband’, ’stepmom’, ’genealogy’, ’loves
family’, ’milf’, ’spouse’, ’full time mommy’, ’father’, ’devoted husband’, ’uncle’, ’hap-
pily married’, ’proudfather’, ’supermom’, ’grandchildren’, ’cousin’, ’brother’, ’mompreneur’,
’widow’, ’grandma’, ’granddaughter’, ’two kids’, ’fiance’, ’godfather’, ’housewife’, ’grandfa-
ther’, ’niece’, ’mum’, ’savior’, ’my daughter’, ’mother’, ’devoted wife’, ’4 kids’, ’twins’, ’new-
born’, ’my kids’, ’happy husband’, ’parenting’, ’son’, ’married’, ’teammommy’, ’stay at home
mom’, ’new dad’, ’house wife’, ’twin’, ’aunty’, ’dad’, ’sahm’, ’grandad’, ’my children’, ’my
husband’, ’parents’, ’woman’, ’super mom’, ’grandson’, ’grandmother’, ’mommy’, ’3 kids’,
’big sister’, ’2 boys’, ’being a mom’, ’hubby’, ’2 kids’, ’rip dad’, ’sis’, ’mama’, ’grandkids’,
’grandparent’, ’bro’, ’wife’, ’nephew’, ’my family’, ’my son’, ’full time dad’, ’children’, ’moth-
erhood’, ’grandpa’, ’no kids’, ’my hubby’, ’spending time with family’, ’new mom’, ’spending
time with my family’, ’wifey’, ’happy wife’, ’granny’, ’daughter’, ’auntie’, ’grammy’, ’family-
first’, ’daddy’, ’brothers’, ’husband’]
horoscope [’sagittarius’, ’virgo’, ’pisces’, ’astrology’, ’teamsagittarius’, ’scorpio’, ’teampisces’, ’team-
cancer’, ’teamgemini’, ’aquarian’, ’libra’, ’aquarius’, ’cancerian’, ’teamtaurus’, ’teamlibra’,
’leo’, ’cancer’, ’astronomy’, ’taurus’, ’aries’, ’teamvirgo’, ’teamaries’, ’capricorn’, ’teamscor-
pio’, ’teamleo’, ’gemini’]
military [’usarmy’, ’marine’, ’usaf’, ’usn’, ’gunner’, ’navy’, ’usmc’, ’soldier’, ’sniper’, ’air force’,
’army’, ’armystrong’, ’military’, ’semper fi’, ’veteran’, ’veterans’, ’former marine’]

location/ethnicity/
race
[’cornwall’, ’rochester’, ’south africa’, ’new yorker’, ’birmingham’, ’ga’, ’global citizen’,
’pakistan’, ’minneapolis’, ’beach bum’, ’nc’, ’punjabi’, ’korean’, ’tulsa’, ’memphis’, ’mer-
ica’, ’urbanist’, ’louisville’, ’us’, ’la’, ’au’, ’yeg’, ’puerto rican’, ’african’, ’montana’, ’new
mexico’, ’minnesota’, ’boston’, ’northern ireland’, ’newyork’, ’nm’, ’southampton’, ’rich-
mond’, ’lebanese’, ’ghanaian’, ’lax’, ’dmv’, ’atx’, ’malaysia’, ’indy’, ’kenyan’, ’southern’,
’portland’, ’rva’, ’france’, ’glasgow’, ’va’, ’vietnam’, ’denmark’, ’english’, ’croatia’, ’milwau-
kee’, ’arkansas’, ’small town’, ’pennsylvania’, ’beaches’, ’chennai’, ’winnipeg’, ’uk’, ’ireland’,
’u k’, ’nola’, ’york’, ’greece’, ’mexican’, ’essex’, ’puertorican’, ’nj’, ’cambridge’, ’punjab’,
’bali’, ’detroit’, ’filipino’, ’sheffield’, ’philly’, ’miami’, ’seattle’, ’spanish’, ’indonesia’, ’turkey’,
’palestine’, ’hispanic’, ’san francisco’, ’florida’, ’indiana’, ’cardiff’, ’foreign’, ’aussie’, ’sd’,
’melanin’, ’paris’, ’citizen’, ’italy’, ’immigration’, ’l a’, ’malaysian’, ’mexico’, ’caribbean’,
’jamaican’, ’iowa’, ’kenya’, ’middle east’, ’china’, ’dorset’, ’tampa’, ’dc’, ’u s’, ’raleigh’, ’nz’,
’texan’, ’s c’, ’vancouver’, ’atlanta’, ’brooklyn’, ’chinese’, ’michigan’, ’german’, ’japan’, ’cali-
fornia’, ’lebanon’, ’pa’, ’mumbai’, ’alaska’, ’nv’, ’madridista’, ’dallas’, ’georgetown’, ’haitian’,
’japanese’, ’houston’, ’ghana’, ’columbus’, ’buffalo’, ’bangalore’, ’trinidad’, ’colorado’, ’viet-
namese’, ’north’, ’scotland’, ’portsmouth’, ’bay area’, ’russian’, ’mixed’, ’belfast’, ’cape town’,
’egyptian’, ’freepalestine’, ’hong kong’, ’dubai’, ’stl’, ’korea’, ’irish’, ’chicagoan’, ’usmnt’,
’americafirst’, ’san antonio’, ’las vegas’, ’brisbane’, ’louisiana’, ’alexandria’, ’toronto’, ’manch-
ester’, ’alabama’, ’lancashire’, ’colombian’, ’p a’, ’sweden’, ’europe’, ’fl’, ’cuban’, ’omaha’,
’fiji’, ’dutch’, ’htx’, ’delhi’, ’polish’, ’savannah’, ’french’, ’nottingham’, ’mi’, ’egypt’, ’indone-
sian’, ’brazilian’, ’nyc’, ’welsh’, ’persian’, ’latin’, ’arabic’, ’los angeles’, ’pdx’, ’india’, ’small
town girl’, ’de’, ’melbourne’, ’poland’, ’singapore’, ’immigrant’, ’arizona’, ’american’, ’cincin-
nati’, ’my india’, ’adelaide’, ’canada’, ’australian’, ’based in london’, ’ontario’, ’dominican’,
’asian’, ’amsterdam’, ’idaho’, ’iraq’, ’hyderabad’, ’nepal’, ’east coast’, ’nevada’, ’nashville’,
’jersey’, ’bronx’, ’philippines’, ’liverpool’, ’ct’, ’maine’, ’netherlands’, ’wales’, ’edinburgh’,
’delaware’, ’barcelona’, ’israel’, ’latina’, ’latino’, ’usa’, ’chicago’, ’plymouth’, ’lagos’, ’peru-
vian’, ’ny’, ’russia’, ’oregon’, ’mke’, ’new jersey’, ’phoenix’, ’midwest’, ’cleveland’, ’nigerian’,
’indian’, ’finland’, ’yorkshire’, ’boricua’, ’londoner’, ’hawaii’, ’proudly south african’, ’asia’,
’utah’, ’syrian’, ’celtic’, ’madrid’, ’kashmir’, ’living in london’, ’washington’, ’iran’, ’london’,
’long island’, ’made in the usa’, ’west coast’, ’aberdeen’, ’long walks on the beach’, ’tx’, ’sur-
rey’, ’leicester’, ’gbr’, ’nebraska’, ’uae’, ’kent’, ’wv’, ’mississippi’, ’brit’, ’kansas’, ’jakarta’,
’az’, ’australia’, ’san diego’, ’charleston’, ’wisconsin’, ’blackmafia’, ’oxford’, ’west ham’,
’massachusetts’, ’european’, ’wi’, ’vegas’, ’south’, ’portuguese’, ’filipina’, ’kentucky’, ’texans’,
’country girl’, ’fort worth’, ’denver’, ’africa’, ’germany’, ’oklahoma’, ’jacksonville’, ’oakland’,
’philadelphia’, ’orange county’, ’newcastle’, ’north carolina’, ’swedish’, ’eng’, ’brighton’,
’sf’, ’missouri’, ’indianapolis’, ’bulgaria’, ’bradford’, ’tucson’, ’belgium’, ’greek’, ’georgia’,
’norwich’, ’spain’, ’kc’, ’swansea’, ’connecticut’, ’texas’, ’british’, ’england’, ’bangladesh’,
’uganda’, ’ohio’, ’new delhi’, ’reno’, ’new zealand’, ’scottish’, ’blackgirlmagic’, ’jamaica’,
’dublin’, ’virginia’, ’hertfordshire’, ’pittsburgh’, ’kuwait’, ’karachi’, ’pakistani’, ’new york’,
’tennessee’, ’island girl’, ’beach lover’, ’nigeria’, ’syria’, ’canadian’, ’cali’, ’orlando’, ’switzer-
land’, ’sacramento’, ’redneck’, ’milan’, ’bristol’, ’austin’, ’america’, ’south african’, ’balti-
more’, ’berlin’, ’tokyo’, ’uswnt’, ’ca’, ’leeds’, ’socal’, ’illinois’, ’bournemouth’, ’managing
partner’, ’norway’, ’new orleans’, ’italian’, ’palestinian’, ’d c’, ’lahore’, ’maryland’]

occupation/industry [’risk management’, ’prof’, ’nasa’, ’nursing’, ’dean’, ’game designer’, ’dj’, ’caterer’, ’truck
driver’, ’magician’, ’ambassador’, ’events manager’, ’exec’, ’banker’, ’urban planner’, ’bee-
keeper’, ’researcher’, ’infosec’, ’psychiatrist’, ’social media specialist’, ’salon owner’, ’prod-
uct development’, ’communications consultant’, ’twitch streamer’, ’secretary’, ’talent man-
ager’, ’first grade teacher’, ’it manager’, ’playwright’, ’ceo’, ’counselor’, ’poker player’, ’boss’,
’worship leader’, ’logistics’, ’psychologist’, ’police’, ’webdeveloper’, ’lifeguard’, ’chartered
accountant’, ’managing director’, ’cinematographer’, ’e-commerce’, ’property manager’, ’de-
veloper’, ’adjunct professor’, ’auditor’, ’data scientist’, ’freelance writer’, ’sociologist’, ’it en-
gineer’, ’pediatrician’, ’agent’, ’productions’, ’hairstylist’, ’content strategist’, ’proofreader’,
’instructional coach’, ’security’, ’nurse’, ’archivist’, ’anthropologist’, ’portrait photographer’,
’writer’, ’reviewer’, ’ghostwriter’, ’specialist’, ’promoter’, ’lighting designer’, ’architecture’,
’announcer’, ’gambler’, ’faculty’, ’chiropractic’, ’guitarist’, ’medic’, ’mover’, ’composer’,
’marketer’, ’content creator’, ’community manager’, ’3rd grade teacher’, ’cpa’, ’rocket scien-
tist’, ’broadcast journalist’, ’online marketer’, ’data analyst’, ’freelancer’, ’executive director’,
’statistician’, ’sound designer’, ’civil engineer’, ’song-writer’, ’operations manager’, ’web de-
signer’, ’lecturer’, ’actress’, ’pr’, ’personal trainer’, ’trainer’, ’board member’, ’chairman’, ’en-
treprenuer’, ’plumber’, ’visual designer’, ’healthcare’, ’pe teacher’, ’consulting’, ’construction’,
’cto’, ’program manager’, ’doc’, ’producer’, ’event manager’, ’social studies teacher’, ’author’,
’vocalist’, ’videographer’, ’tv host’, ’pastry chef’, ’front end developer’, ’accountant’, ’mom-
preneur’, ’educationist’, ’administrator’, ’virtual assistant’, ’hvac’, ’public health’, ’engineer’,
’scientist’, ’pilot’, ’printmaker’, ’executive’, ’graphics designer’, ’model’, ’serial entrepreneur’,
’record producer’, ’beauty’, ’neuroscientist’, ’multimedia journalist’, ’cartoonist’, ’freelance’,
’software developer’, ’realestate’, ’screenwriter’, ’translator’, ’handyman’, ’builder’, ’deco-
rator’, ’massage therapist’, ’game developer’, ’aviator’, ’manager’, ’social worker’, ’inte-
rior designer’, ’digitalhealth’, ’contractor’, ’2nd grade teacher’, ’assistant professor’, ’emcee’,
’farmer’, ’event organizer’, ’copywriter’, ’account manager’, ’educator’, ’real estate’, ’public
relations’, ’medical’, ’dental’, ’performer’, ’datascience’, ’make up artist’, ’florist’, ’lawyer’,
’cameraman’, ’flight attendant’, ’hair stylist’, ’nanny’, ’hairdresser’, ’businessman’, ’web de-
veloper’, ’entrepeneur’, ’esq’, ’3d artist’, ’cfp’, ’tv producer’, ’self-employed’, ’network en-
gineer’, ’comedian’, ’performing artist’, ’ems’, ’pharma’, ’structural engineer’, ’judge’, ’song
writer’, ’life coach’, ’licensed cosmetologist’, ’physician’, ’tv presenter’, ’office manager’, ’ca-
reer coach’, ’seamstress’, ’founder’, ’accounting’, ’assistant director’, ’motivational speaker’,
’pharmacy’, ’law’, ’co founder’, ’illustrator’, ’founding member’, ’publicity’, ’future teacher’,
’biologist’, ’it consultant’, ’stock trader’, ’hotelier’, ’product management’, ’psychotherapist’,
’chemist’, ’doula’, ’librarian’, ’historian’, ’event coordinator’, ’mining’, ’dentist’, ’herbalist’,
’bartender’, ’primary school teacher’, ’owner’, ’inventor’, ’jewelry maker’, ’data science’, ’ad-
visor’, ’anchor’, ’electrical engineer’, ’banking’, ’occupational therapist’, ’registered dietitian’,
’cosmetologist’, ’social media marketer’, ’doctor’, ’image consultant’, ’youtube content cre-
ator’, ’former teacher’, ’mathematician’, ’documentary filmmaker’, ’social entrepreneur’, ’ar-
chitect’, ’rapper’, ’columnist’, ’instructional designer’, ’counsellor’, ’estate planning’, ’curator’,
’instructor’, ’hr’, ’networker’, ’violinist’, ’aviation’, ’farming’, ’realtor’, ’musician’, ’5th grade
teacher’, ’programmer’, ’meteorologist’, ’teacher’, ’graphicdesigner’, ’event planner’, ’man-
aging editor’, ’broker’, ’speaker’, ’audio engineer’, ’carpenter’, ’salesman’, ’vet’, ’ecologist’,
’public servant’, ’social media consultant’, ’ux designer’, ’youtuber’, ’sales’, ’it specialist’,
’published author’, ’veterinarian’, ’hospitality’, ’staff writer’, ’software engineer’, ’paramedic’,
’preschool teacher’, ’cosmetology’, ’genealogist’, ’recruiter’, ’account executive’, ’geogra-
pher’, ’podcaster’, ’waitress’, ’chiropractor’, ’esthetician’, ’dr’, ’communications specialist’,
’website designer’, ’visual artist’, ’project manager’, ’self employed’, ’electrician’, ’brand
strategist’, ’program director’, ’4th grade teacher’, ’diplomat’, ’socialite’, ’registered nurse’,
’tattoo artist’, ’co-owner’, ’officer’, ’makeup’, ’criminal justice’, ’retired’, ’webdesigner’, ’busi-
nesswoman’, ’co-founder’, ’script writer’, ’make-up artist’, ’aspiring author’, ’landlord’, ’co-
host’, ’assistant principal’, ’reporter’, ’stage manager’, ’archaeologist’, ’unemployed’, ’head
coach’, ’salesforce’, ’songwriter’, ’project management’, ’scicomm’, ’baker’, ’employed’, ’so-
cial media strategist’, ’saxophonist’, ’chef’, ’principal’, ’interpreter’, ’broadcaster’, ’painter’,
’public speaking’, ’user experience’, ’medicine’, ’marketeer’, ’production manager’, ’journal-
ist’, ’filmmaker’, ’microbiologist’, ’referee’, ’ibmer’, ’associate professor’, ’pharmacist’, ’en-
tertainer’, ’md’, ’mechanical engineer’]

occupations/industry
cont.
[’drummer’, ’astrologer’, ’physiotherapist’, ’publisher’, ’priest’, ’director’, ’future en-
trepreneur’, ’jewelry designer’, ’influencer’, ’special education teacher’, ’tv personality’,
’barista’, ’economist’, ’commentator’, ’editor’, ’entrepreneur’, ’costume designer’, ’co-
founder’, ’kindergarten teacher’, ’licensed massage therapist’, ’archaeology’, ’hypnotherapist’,
’brand manager’, ’astronomer’, ’forex trader’, ’private pilot’, ’communications professional’,
’linguist’, ’emt’, ’assistant’, ’ordained minister’, ’sound engineer’, ’mechanic’, ’barber’, ’cmo’,
’content writer’, ’ecommerce’, ’app developer’, ’biochemist’, ’insurance’, ’pmp’, ’math’, ’en-
terpreneur’, ’scriptwriter’, ’nutritionist’, ’innovator’, ’publicist’, ’therapist’, ’clinical psychol-
ogist’, ’cfa’, ’it professional’, ’mediator’, ’future doctor’, ’firefighter’, ’social commentator’,
’advertising’, ’biotech’, ’professor’, ’physical therapist’, ’information technology’, ’rocket ship
builder’, ’paralegal’, ’small business owner’, ’stylist’, ’general manager’, ’copy editor’, ’asst’,
’supply chain’, ’communications manager’, ’network marketer’, ’future nurse’, ’consultant’,
’graphic designer’, ’pastor’, ’social work’, ’restaurateur’, ’geologist’, ’future lawyer’, ’sculptor’,
’brand ambassador’, ’surgeon’, ’product manager’, ’recording engineer’, ’welder’, ’physicist’,
’midwife’, ’cfo’, ’public speaker’, ’teach’, ’tourism’, ’associate’, ’cake decorator’, ’analyst’,
’dietitian’, ’beautician’, ’attorney’, ’coaching’, ’chemical engineer’, ’keynote speaker’, ’con-
tentmarketing’]
outdoors/nature/animals [’nasa’, ’tree hugger’, ’beekeeper’, ’country boy’, ’stargazer’, ’sharks’, ’2 dogs’, ’my dog’,
’ecology’, ’angler’, ’animals’, ’bunnies’, ’space’, ’backpacking’, ’hiking’, ’loves nature’, ’loves
animals’, ’flower child’, ’outdoorsman’, ’mountain biker’, ’nature’, ’horses’, ’cat’, ’pandas’,
’anything outdoors’, ’kayaker’, ’climatechange’, ’animal lover’, ’doglover’, ’environmentalist’,
’kayak’, ’fishing’, ’loves dogs’, ’scorpion’, ’environmental’, ’conservationist’, ’outdoors’, ’an-
imal’, ’gardening’, ’gardner’, ’ponies’, ’eagle scout’, ’cats’, ’sailing’, ’hike’, ’scuba’, ’hunt’,
’my cats’, ’renewable energy’, ’astronaut’, ’pet’, ’ocean lover’, ’aerospace’, ’horse’, ’pets’,
’hunting’, ’pet lover’, ’agriculture’, ’fisher’, ’birds’, ’puppies’, ’owls’, ’dog’, ’birder’, ’huntin’,
’surfing’, ’sailor’, ’hunter’, ’hiker’, ’farming’, ’snowboarding’, ’scuba diving’, ’gardener’, ’vet’,
’ecologist’, ’crazy cat lady’, ’meow’, ’surfer’, ’veterinarian’, ’mountain’, ’cowboy’, ’rodeo’,
’shooting’, ’gearhead’, ’trekker’, ’mountain biking’, ’mountaineer’, ’kitten’, ’dinosaurs’, ’2
cats’, ’naturalist’, ’being outdoors’, ’equestrian’, ’environment’, ’gator’, ’skier’, ’boating’,
’puppy’, ’turtles’, ’archery’, ’astrologer’, ’animallover’, ’fly fishing’, ’climate’, ’penguins’,
’outdoor enthusiast’, ’tiger’, ’scuba diver’, ’sustainability’, ’astronomer’, ’loves cats’, ’bear’,
’fisherman’, ’kayaking’, ’mudding’, ’dog lover’, ’camper’, ’dogs’, ’climate change’, ’trail run-
ner’, ’all animals’, ’wildlife’, ’backpacker’, ’conservation’, ’scout’, ’my dogs’, ’surf’, ’farm’,
’camping’]
politics [’donald’, ’president’, ’make america great again’, ’covfefe’, ’constitutional conservative’,
’political’, ’trump’, ’obama’, ’constitution’, ’vote’, ’imwithher’, ’warren’, ’constitutionalist’,
’republican’, ’right’, ’reagan’, ’governance’, ’maga’, ’makeamericagreatagain’, ’left’, ’ameri-
cafirst’, ’nevertrump’, ’donald trump’, ’stillwithher’, ’vice president’, ’politics’, ’vp’, ’democ-
racy’, ’feelthebern’, ’neverhillary’, ’politician’, ’realdonaldtrump’, ’2a’, ’trumptrain’, ’naren-
dramodi’, ’conservative’, ’interested in politics’, ’bjp’, ’imran khan’, ’potus’, ’political junkie’,
’independent’, ’democrat’, ’socialist’, ’election2016’, ’campaigner’, ’public policy’, ’fiscal con-
servative’, ’uniteblue’, ’libertarian’, ’liberal’, ’brexit’, ’hillary’, ’gop’, ’notmypresident’, ’pro-
gressive’, ’trump2016’, ’1a’, ’geopolitics’, ’policy’]
relationship status [’dating’, ’single’, ’committed’, ’poly’, ’engaged’, ’teamtaken’, ’teamsingle’, ’forever alone’,
’taken’, ’divorced’, ’boyfriend’, ’in love with’, ’in a relationship’, ’newlywed’, ’happily taken’,
’girlfriend’, ’bachelor’]

religion [’believer’, ’follower of jesus’, ’teamgod’, ’faith’, ’proverbs 3:5-6’, ’worship leader’, ’mus-
limah’, ’theology’, ’creator’, ’pjnet’, ’god1st’, ’jesuschrist’, ’religion’, ’muslim’, ’my church’,
’loves jesus’, ’blessed’, ’wiccan’, ’saved’, ’john 3:16’, ’mohammed’, ’spiritualist’, ’mormon’,
’child of the most high’, ’jesus’, ’child of the one true king’, ’plans to prosper you’, ’disciple’,
’galatians 2:20’, ’worshipper’, ’loves god’, ’truly blessed’, ’teamblessed’, ’religious’, ’roman
catholic’, ’godisgood’, ’phil 4:13’, ’child of the king’, ’gospel’, ’godspeed’, ’evangelist’, ’god’,
’secular’, ’in god we trust’, ’romans 8:28’, ’catholic’, ’child of god’, ’visionary’, ’islam’, ’fol-
low jesus’, ’hindu’, ’christian’, ’romans 8:18’, ’jewish’, ’bible’, ’sinner’, ’witch’, ’youth leader’,
’church’, ’spiritual’, ’joshua 1:9’, ’my god’, ’godfirst’, ’my lord’, ’minister’, ’allah’, ’spiritual-
ity’, ’romans 1:16’, ’buddhist’, ’chosen one’, ’believe in god’, ’philippians 4:13’, ’declares the
lord’, ’preacher’, ’thomasian’, ’moslem’, ’born again christian’, ’teamjesus’, ’youth pastor’,
’prophet’, ’follower of christ’, ’godfearing’, ’priest’, ’born again’, ’jeremiah 29:11’, ’forgiven’,
’christ’, ’missionary’, ’ordained minister’, ’alhamdulillah’, ’lord’, ’theologian’, ’pagan’, ’christ
follower’, ’muhammad’, ’amen’, ’pastor’, ’atheist’, ’coventry’, ’lucifer’, ’agnostic’, ’pray’, ’can
do all things through christ who strengthens me’, ’worshiper’]
school/subjects [’class of 2018’, ’prof’, ’dean’, ’uni student’, ’ucla’, ’tamu’, ’lsu’, ”o ’17”, ’gamecocks’, ’ubc’,
’grad’, ’uconn’, ’buckeyes’, ’first grade teacher’, ’hailstate’, ’college student’, ’adjunct pro-
fessor’, ’all around nerd’, ’medical student’, ’fsu’, ’iu’, ’goblue’, ’nerdy’, ’h2p’, ’bsn’, ’fac-
ulty’, ’huskers’, ’3rd grade teacher’, ’duke’, ’stem’, ’geaux tigers’, ’clemson’, ’mizzou’, ’smu’,
’med student’, ’lifelong learner’, ’lecturer’, ’international relations’, ’go gators’, ’sdsu’, ’in
college’, ’university’, ’nerd’, ’penn’, ’alumni’, ’unc’, ’pe teacher’, ’gocougs’, ’masters’, ’uw’,
’uniofoxford’, ’engineering’, ’social studies teacher’, ’tcu’, ’alumna’, ’gatornation’, ’colleges-
tudent’, ’m ed’, ’educationist’, ’future educator’, ’science’, ’msw’, ’ucf’, ’roll tide’, ’wsu’,
’uoft’, ’high school’, ’geeky’, ’asu’, ’learner’, ’life-long learner’, ’uga’, ’mechanical engineer-
ing’, ’2nd grade teacher’, ’buckeye’, ’assistant professor’, ’cornell’, ’educator’, ’byu’, ’auburn’,
’8th grade’, ’beardown’, ’bama’, ’go blue’, ’school’, ’buckeyenation’, ’go cougs’, ’boomer
sooner’, ’word nerd’, ’penn state’, ’alum’, ’freshmen’, ’wareagle’, ’pvamu’, ’nyu’, ’genius’,
’college’, ’future teacher’, ’maths’, ’yale’, ’rolltide’, ’mit’, ’utsa’, ’sociology’, ’univ’, ’uofa’,
’sophmore’, ’historian’, ’psu’, ’perpetual student’, ’scholar’, ’primary school teacher’, ’war
eagle’, ’ph d’, ’geology’, ’class of 2017’, ’history’, ’ut’, ’bsc’, ’studying’, ’anthropology’,
’kappa delta’, ’graduate’, ’student’, ’former teacher’, ’mathematician’, ’educated’, ’gators’,
’o 2015’, ’physics’, ’umich’, ’unlv’, ”class of ’18”, ’baylor’, ’stanford’, ’philosopher’, ’aca-
demic’, ’uf’, ’junior’, ’5th grade teacher’, ’famu’, ’teacher’, ’polymath’, ’ncaa’, ’columbia’,
’fiu’, ’vols’, ’sophomore’, ’language’, ’ole miss’, ’uottawa’, ’polyglot’, ’super junior’, ’genet-
ics’, ’syracuse’, ’nursing student’, ’doctoral student’, ’godawgs’, ’preschool teacher’, ’purdue’,
’princeton’, ’chemistry’, ’pre-med’, ’wolfpack’, ’cal’, ’teaching’, ’4th grade teacher’, ’o 2016’,
’mba’, ’criminology’, ’philosophy’, ’hoosier’, ’students’, ’tarheels’, ’assistant principal’, ’edu-
cation’, ’geography’, ’linguistics’, ’gobucks’, ’psych’, ’principal’, ’geek’, ’class of 2016’, ’go-
ducks’, ’research’, ’edu’, ’usc’, ’associate professor’, ’huge nerd’, ’freshman’, ’special educa-
tion teacher’, ’wvu’, ’economics’, ’alumnus’, ’kindergarten teacher’, ’dawgs’, ’tar heel’, ’go
dawgs’, ’biology’, ’uva’, ’tutor’, ’badgers’, ’mpa’, ’hookem’, ’it student’, ’go vols’, ’terps’,
’phd’, ’mathematics’, ’neuroscience’, ’professor’, ’notre dame’, ’econ’, ’ksu’, ’msu’, ’home-
schooler’, ’aggie’, ’varsity cheer’, ’full time student’, ’mad scientist’, ’ncat’, ’life long learner’,
’sci’, ’psychology’, ’always learning’, ’teach’, ’knowledge seeker’, ’ucberkeley’, ’syracuseu’,
’learning new things’, ’senior’]
sex [’bdsm’, ’sex’, ’camgirl’, ’playboy’, ’porn’, ’milf’, ’tits’, ’slut’, ’boobs’, ’horny’, ’nsfw’, ’18+
only’, ’kinky’, ’sexy’, ’findom’, ’pussy’, ’erotica’, ’18+ rp’, ’fetish’, ’dirty’]
sexuality [’gaymer’, ’straight’, ’queer’, ’gay’, ’sapiosexual’, ’sexuality’, ’pansexual’, ’lgbt’, ’lgbtq’, ’bi-
sexual’, ’lesbian’, ’bi’]

sports [’manutd’, ’redsox’, ’afc’, ’safc’, ’cubs’, ’edtech’, ’skiing’, ’saints’, ’nffc’, ’play basketball’,
’badminton’, ’marathon runner’, ’buckeyes’, ’ac milan’, ’neymar’, ’victoria concordia crescit’,
’ball is life’, ’sporty’, ’braves’, ’hailstate’, ’athlete’, ’nufc’, ’mufc’, ’cristiano’, ’celtics’, ’golf’,
’capitals’, ’gospursgo’, ’halamadrid’, ’nhl’, ’nationals’, ’eagles’, ’ice hockey’, ’red wings’, ’pat-
snation’, ’chargers’, ’maverick’, ’ballet’, ’horse racing’, ’goblue’, ’mlb’, ’rower’, ’coyi’, ’dub-
nation’, ’football’, ’patriots’, ’sixers’, ’h2p’, ’stlcards’, ’rockets’, ’rams’, ’huskers’, ’lakersna-
tion’, ’backpacking’, ’motogp’, ’cowboysnation’, ’go tigers’, ’baller’, ’giants’, ’falcons’, ’jets’,
’hiking’, ’49ers’, ’ski’, ’nats’, ’teamlebron’, ’play sports’, ’raptors’, ’play baseball’, ’racing’,
’cpfc’, ’volleyball’, ’lfc’, ’mls’, ’gopackgo’, ’rangers’, ’cowboynation’, ’lakeshow’, ’ballislife’,
’kobe’, ’go gators’, ’mystic’, ’mobility’, ’xc’, ’nfl’, ’rider’, ’taekwondo’, ’field hockey’, ’moun-
tain biker’, ’athletics’, ’sox’, ’bowling’, ’workout’, ’fc barcelona’, ’birdgang’, ’hockey’, ’ar-
senal’, ’martial arts’, ’packers’, ’miamiheat’, ’racer’, ’kayaker’, ’run’, ’hawks’, ’gym’, ’cheer-
leader’, ’lufc’, ’pistons’, ’wizards’, ’clippers’, ’red devil’, ’bucs’, ’kayak’, ’sport’, ’nyk’, ’cross-
fitter’, ’nyr’, ’habs’, ’colts’, ’blackhawks’, ’tottenham hotspur’, ’triathlon’, ’cfc’, ’vfl’, ’jays’,
’mma’, ’nygiants’, ’muay thai’, ’cyclist’, ’swim’, ’trickshotter’, ’softball’, ’basketball’, ’yogini’,
’angels’, ’soccer’, ’sportsman’, ’buckeye’, ’nba’, ’browns’, ’ronaldo’, ’go pack go’, ’barca’,
’redskins’, ’manchester united’, ’lacrosse’, ’teamheat’, ’buckeyenation’, ’go cougs’, ’boomer
sooner’, ’titans’, ’usmnt’, ’tennis’, ’mariners’, ’sailing’, ’futbol’, ’golden state warriors’, ’triath-
lete’, ’gohawks’, ’gooner’, ’wareagle’, ’hike’, ’bruins’, ’vince lombardi’, ’fitness’, ’scuba’,
’warrior’, ’nike’, ’pilates’, ’yogi’, ’raidernation’, ’rolltide’, ’cheerleading’, ’steelers’, ’bullsna-
tion’, ’sfgiants’, ’loves football’, ’biker’, ’bodybuilder’, ’steelersnation’, ’mets’, ’cycling’, ’adi-
das’, ’swfc’, ’acmilan’, ’seahawks’, ’golfing’, ’fitfam’, ’chiefs’, ’spurs’, ’war eagle’, ’netball’,
’leafs’, ’ktbffh’, ’ducks’, ’lifting’, ’gymnastics’, ’huge sports fan’, ’pirate’, ’mcfc’, ’karate’,
’ball’, ’hala madrid’, ’gators’, ’mffl’, ’teamchelsea’, ’bicyclist’, ’thfc’, ’blue jays’, ’juventus’,
’play hockey’, ’reds’, ’surfing’, ’lakers’, ’milanisti’, ’efc’, ’go bucks’, ’archer’, ’sailor’, ’lcfc’,
’canucks’, ’sabres’, ’pga’, ’saint’, ’bulls’, ’avfc’, ’runner’, ’hiker’, ’cowboys’, ’manu’, ’skate’,
’martial artist’, ’teamcowboys’, ’snowboarding’, ’marathoner’, ’lakernation’, ’warriors’, ’work-
outs’, ’skating’, ’scuba diving’, ’arsenalfc’, ’sports’, ’vols’, ’caps’, ’lebron james’, ’hooper’,
’red sox’, ’yankees’, ’avid golfer’, ’diver’, ’goalkeeper’, ’surfer’, ’fcb’, ’bucks’, ’godawgs’,
’wwe’, ’ynwa’, ’afl’, ’broncos’, ’raiders’, ’real madrid’, ’bodybuilding’, ’big sports fan’, ’skate-
boarding’, ’ravensnation’, ’indians’, ’rodeo’, ’skateboarder’, ’powerlifting’, ’shooting’, ’niners’,
’figure skater’, ’wolfpack’, ’f1’, ’louis cardinals’, ’loves sports’, ’loves the giants’, ’manch-
esterunited’, ’teamceltics’, ’mountain biking’, ’climber’, ’baseball’, ’tottenham’, ’riding’, ’oil-
ers’, ’cr7’, ’beachbody coach’, ’tarheels’, ’everton’, ’pacers’, ’play golf’, ’bowler’, ’ajax’,
’weights’, ’snowboard’, ’packer fan’, ’swimming’, ’devils’, ’gobucks’, ’boxer’, ’head coach’,
’whodatnation’, ’dodgers’, ’equestrian’, ’phillies’, ’cavs’, ’ncfc’, ’crossfit’, ’exercise’, ’har-
vard’, ’weightlifting’, ’skater’, ’skier’, ’all sports’, ’evertonian’, ’season ticket holder’, ’go-
ducks’, ’shooter’, ’referee’, ’golfer’, ’archery’, ’paintball’, ’dive’, ’ufc’, ’parkour’, ’cardinals’,
’heatnation’, ’darts’, ’footy’, ’wrestling’, ’play softball’, ’penguins’, ’pats’, ’bikes’, ’patriotsna-
tion’, ’scuba diver’, ’bills’, ’dawgs’, ’flyers’, ’tar heel’, ’go dawgs’, ’go bears’, ’bball’, ’cricket’,
’dallascowboys’, ’iamunited’, ’messi’, ’badgers’, ’play soccer’, ’teamlakers’, ’varsity football’,
’snooker’, ’saintsfc’, ’hoop’, ’dolphins’, ’wrestler’, ’avid sports fan’, ’hookem’, ’new england
patriots’, ’cristian’, ’kayaking’, ’bengals’, ’bmx’, ’realmadrid’, ’go vols’, ’terps’, ’kickboxing’,
’royals’, ’biking’, ’bike’, ’cricketer’, ’judo’, ’trail runner’, ’mavs’, ’pirates’, ’orioles’, ’vikings’,
’bluejays’, ’running’, ’aggie’, ’gymnast’, ’panthers’, ’varsity cheer’, ’swimmer’, ’msdhoni’,
’squash’, ’track’, ’fcbarcelona’, ’chelsea’, ’carolina panthers’, ’flyeaglesfly’, ’whufc’, ’rusher’,
’knicks’, ’ncat’, ’fifa’, ’wolves’, ’water polo’, ’go hawks’, ’skateboard’, ’astro’, ’surf’, ’formula
1’, ’billsmafia’, ’powerlifter’, ’ucl’, ’liverpoolfc’, ’spursnation’, ’mancity’, ’flythew’, ’foot-
baller’, ’uswnt’, ’ride bikes’, ’chelseafc’, ’longboarding’, ’astros’, ’cheer’, ’teamlh’, ’yoga’,
’gunners’, ’hoops’, ’rugby’, ’snowboarder’, ’ravens’, ’steelernation’]

technology/ gam-
ing/cars
[’ps3’, ’android’, ’game designer’, ’edtech’, ’gaymer’, ’gta5’, ’robots’, ’computer’, ’webdevel-
oper’, ’motorcycle’, ’data scientist’, ’it engineer’, ’bmw’, ’it guy’, ’play xbox’, ’car’, ’elec-
trical’, ’motogp’, ’playstation’, ’coder’, ’civil engineer’, ’video games’, ’web designer’, ’play
video games’, ’halo’, ’skyrim’, ’motorbikes’, ’xb1’, ’trains’, ’airsoft’, ’vr’, ’avgeek’, ’engineer-
ing’, ’computers’, ’telecom’, ’gis’, ’front end developer’, ’gadget freak’, ’minecraft’, ’mvrp’,
’motorcyclist’, ’engineer’, ’electronics’, ’nascar’, ’gadget geek’, ’classic cars’, ’clash of clans’,
’digital’, ’software developer’, ’tech’, ’game developer’, ’ai’, ’mechanical engineering’, ’data-
science’, ’cybersecurity’, ’videogames’, ’ps4’, ’motorsports’, ’fintech’, ’web developer’, ’bat-
tlefield’, ’harley rider’, ’sims’, ’techy’, ’network engineer’, ’technophile’, ’gamer’, ’xboxone’,
’structural engineer’, ’motorcycles’, ’petrol head’, ’world of warcraft’, ’just a gamer’, ’faze’,
’rpg’, ’xbox’, ’league’, ’xbox360’, ’gamertag’, ’we are legion’, ’data science’, ’electrical en-
gineer’, ’league of legends’, ’board gamer’, ’bigdata’, ’programming’, ’nlp’, ’technology’,
’games’, ’blackjack’, ’programmer’, ’play minecraft’, ’audio engineer’, ’virtualization’, ’mo-
torcycle enthusiast’, ’ux designer’, ’technician’, ’it specialist’, ’web development’, ’gaming’,
’avid gamer’, ’gamedev’, ’software engineer’, ’minecrafter’, ’play cod’, ’jeeps’, ’website de-
signer’, ’cinchgaming’, ’petrolhead’, ’ffxiv’, ’sony’, ’board games’, ’web design’, ’automa-
tion’, ’webdesigner’, ’teamiphone’, ’techie’, ’casual gamer’, ’play games’, ’nintendo’, ’callof-
duty’, ’madden’, ’website development’, ’fast cars’, ’trucks’, ’cars’, ’forzamilan’, ’mod’, ’jeep’,
’ibmer’, ’industrial’, ’electronic’, ’mechanical engineer’, ’dota’, ’planes’, ’internet’, ’gadget
lover’, ’game dev’, ’mechanic’, ’motocross’, ’app developer’, ’gadgets’, ’it student’, ’bmx’,
’mudding’, ’microsoft’, ’software’, ’ibm’, ’auto’, ’biotech’, ’information technology’, ’rocket
ship builder’, ’technologist’, ’playing video games’, ’cod’, ’call of duty’, ’coding’, ’zelda’,
’motorsport’, ’fazeclan’, ’hacker’, ’it geek’, ’poker’, ’gta’, ’machinelearning’, ’car enthusiast’,
’saas’, ’warcraft’, ’chemical engineer’, ’im a gamer’, ’rv’]
travel [’nomad’, ’world traveller’, ’avid traveler’, ’will travel’, ’globetrotter’, ’adventurer’, ’wander-
lust’, ’travelling’, ’globe trotter’, ’road trips’, ’explorer’, ’travel’, ’traveler’, ’loves to travel’,
’traveller’, ’wanderer’, ’traveling’, ’loves travelling’, ’wanderluster’, ’world citizen’, ’world
traveler’]
values [’jai hind’, ’egalitarian’, ’patriot’, ’capitalist’, ’freethinker’, ’hedonist’, ’truth seeker’, ’peace’,
’independence’, ’patriotic’, ’humanity’, ’hakuna matata’, ’peacemaker’, ’radical’, ’freedom’,
’honesty’, ’liberty’]
Table 4: Labelled identifiers.
