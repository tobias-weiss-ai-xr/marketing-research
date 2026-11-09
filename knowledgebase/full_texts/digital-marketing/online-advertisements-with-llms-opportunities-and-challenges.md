---
title: 'Online Advertisements with LLMs: Opportunities and Challenges'
url: https://arxiv.org/abs/2311.07601
category: digital-marketing
subcategory: empirical
date: 2023-11
venue: ''
authors:
- Soheil Feizi
- MohammadTaghi Hajiaghayi
- Keivan Rezaei
- Suho Shin
source: arxiv
pdf_url: https://arxiv.org/pdf/2311.07601
pages: 22
chars: 81508
fetched_at: '2026-11-08T13:17:01+00:00'
kb_version: 1
---

# Online Advertisements with LLMs: Opportunities and Challenges

Online Advertisements with LLMs: Opportunities and Challenges ∗
Soheil Feizi † MohammadTaghi Hajiaghayi† Keivan Rezaei † Suho Shin †
Abstract
This paper explores the potential for leveraging
Large Language Models (LLM) in the realm of
online advertising systems. We introduce a gen-
eral framework for LLM advertisement, consist-
ing of modification, bidding, prediction, and auc-
tion modules. Different design considerations for
each module are presented. These design choices
are evaluated and discussed based on essential
desiderata required to maintain a sustainable sys-
tem. Further fundamental questions regarding
practicality, efficiency, and implementation chal-
lenges are raised for future research. Finally, we
exposit how recent approaches on mechanism de-
sign for LLM can be framed in our unified per-
spective.
1 Introduction
In the vast landscape of online search engines, the
role of advertisements has become pivotal, shap-
ing the digital experience for users globally. The
enormity of the market, with trillions of dollars at
play, shows the economic significance of advertis-
ing, e.g., the market size of search advertisement
as of 2020 was valued at USD 164 .12 billion (In-
sight, 2022).
Online advertising not only brings revenue to
platform companies but also plays a crucial role
in subsidizing the free access to information and
services to every individual. The democratization
of education, information, and other resources
is made possible through ad-driven models, en-
abling individuals to not only consume content
for free but also contribute to the digital ecosys-
tem. Additionally, the symbiotic relationship be-
∗Alphabetical author ordering.
†University of Maryland College Park, MD USA. Email:
(sfeizi,hajiagha,krezaei,suhoshin)@umd.edu
tween advertisements and content creation cre-
ates a feedback loop, fostering economic growth.
As a side note, even subscription-based streaming
platforms like Netflix are starting ad-supported
plans (Netflix, 2022).
On the other hand, recently, large lan-
guage models (LLMs) (Brown et al., 2020; Anil
et al., 2023; Thoppilan et al., 2022) have gained
widespread adoption among users, serving vari-
ous functions including question answering, con-
tent generation, translation, code completion, and
more (Nijkamp et al., 2022; Fried et al., 2022;
Wang and Komatsuzaki, 2021; Liu et al., 2023a).
The proliferation of AI-driven assistant language
models, such as ChatGPT, has contributed to
a growing trend wherein individuals increasingly
use such models to address their inquiries, oc-
casionally replacing traditional search engines as
their primary information-seeking tool. Accord-
ing to PCMag (2023), even for now, 35% of ca-
sual users say they find LLMs to be more helpful
in finding information than search engines. It is
obvious that such a trend will be accelerating in
the near future as well. The substantial usage
volumes stemming from diverse users would in-
duce companies offering these tools, which we call
LLM providers , to contemplate revenue genera-
tion through advertising (AdWeek, 2023; Crunch,
2023; Microsoft, 2023). Consequently, an inter-
esting and fundamental question arises:
How can LLM providers make revenue
by running an online advertisement on
their services?
The concept of online advertising has been ex-
tensively studied within the realm of search en-
gines, where auctions are conducted among ad-
vertisements from advertisers when a user inputs
a query. This paper focuses on the prospect
1
arXiv:2311.07601v4  [cs.CY]  9 Sep 2024

of transposing this online advertising model and
auction framework to the context of large lan-
guage models. We further discuss technical chal-
lenges and potential framework to run online ad-
vertisement system in LLM, thereby calling aca-
demic and industrial researchers to the area of
importance.
Search advertising. To better explain
fundamental differences between the standard
search advertising (SA)1 and the LLM advertising
(LLMA), we briefly introduce how the standard
SA works (Lahaie et al., 2007) in what follows. (1)
Bidding: in the SA, the owner of each ad i writes
bid bi ∈ R≥0 on targeting keyword for i∈ [n],
which can possibly a set of keywords. (2) Output
generation: the platform first decides how many
slots to allocate for ads in the search engine re-
sults page (SERP), say k. (3) Prediction: given
k slots in SERP, the platform then predicts the
click-through-rate (CTR) αij when ad i is allo-
cated in slot j. (4) Auction: then it optimizes
max
x∈[0,1]n×k
n∑
i=1
k∑
j=1
αijbixij, (1.1)
where x = ( xij)i∈[n],j∈[k] is the (possibly ran-
domized) allocation vector such that xij = 1 if
ad i is allocated in slot j given the constraint∑n
i=1xij≤ 1 for everyj∈ [k],i∈ [n], and charges
each ad by the committed payment rule.
Overall, whenever a user arrives in the platform
and searches a keyword, the set of ads related
to the keyword are getting involved in the mech-
anism. Specifically, the platform collects corre-
sponding bids, decides the number of slots k, pre-
dicts CTR, and the auction runs.
Motivating example. How would the LLMA
be fundamentally different from the SA? We start
with illustrative scenarios where a user asks a
technical question about computers (Figure 1).
Without advertisement, LLM would typically
generate a response to address the user’s query.
(a) can be deemed as display ads, and would be
relatively easy to handle given the vast amount of
techniques in display ads. However, (b) is more
1Its mechanism design problem is often called as spon-
sored search auction (SSA).
similar to search ad or native ad. 2 We will focus
on the approach (b), which will entail fundamen-
tal challenges that have not arisen in the tradi-
tional SA. 3
SA versus LLMA. Recall the process of bid-
ding, output generation, prediction, and auction
in the SA mentioned before, and imagine imple-
menting those modules for LLMA.
For the bidding module, how could the adver-
tisers write bid ? What would they actually bid
for? This is not straightforward to answer, since
the user query in LLM cannot be simply specified
as a keyword. Further, given that the marketing
impact will be significantly dependent to how the
LLM incorporate the ad in the output, it is not
even clear what is the advertiser’s value for be-
ing included in the ad. In fact, the advertiser’s
value would be dependent to the generated out-
put, then again, how could the advertiser reflect
their willingness-to-pay with respect to the out-
put, which might not be accessible in advance?
Even further, how can we generate output that
smoothly incorporates the ad without hurting the
user experience while satisfying the advertiser?
For prediction module, most SA run an online
learning algorithm to update the ad’s feature vec-
tor with respect to the user context (McMahan
et al., 2013). This was possible because the ad
images, hyperlinks, and more generally how they
appear in the SERP remain the same across many
user interactions. LLM, however, would incorpo-
rate ad in a very different manner for each query,
e.g., see Figure 5, then how can the LLMA learn
the CTR fundamentally? Also, since the ads are
merged into the generated output, it significantly
affects the user experience, then how can we guar-
2Search/native ads usually capture user attention better
than display ads, e.g., almost 50% more views (Outbrain,
2023).
3Also, in case the ads are included within the generated
output, there are several possibilities such that the ads may
replace one of the element in a list of elements ( e.g., Fig-
ure 3 in the appendix, denoted by structured output), or
the ads itself is incorporated within the original text/figure
without hurting/changing the context of the original out-
put (e.g., Figure 1, denoted by unstructured output). We
focus on the unstructured output, as this would be broadly
applicable in various scenarios, and the structured output
may be able to handled with the standard SA framework.
2

Original LLM Output
Prompt:How do CPU and RAM interact within a computer?
Output:The CPU (Central Processing Unit) processes data and
instructions, and RAM (Random Access Memory) provides fast,
temporary storage for the data the CPU is actively working on,
enabling quick access and manipulation of data, resulting in faster
and more efficient computing.
Modified Output
Prompt:Can you promote laptop L of brand B in the previous response?
Output:The CPU (Central Processing Unit) processes data and
instructions, and RAM (Random Access Memory) provides fast,
temporary storage for the data the CPU is actively working on, enabling
quick access and manipulation of data, resulting in faster and more
efficient computing. Notably, "Laptop L" from "Brand B" is optimized for
this synergy, offering a powerful CPU and ample RAM, ensuring a
seamless and high-performance computing experience.
Figure 1: An example of providing unstructured advertisement in the LLM. Left column refers to
the case where we ask above question from ChatGPT 4, and to incorporate the ads we use queries
specified in the right column.
antee the user satisfaction and measure them?
Finally, which kind of auction format should
LLMA run? How can LLMA adapt for advertis-
ing multiple ads in a single output? What would
be a reasonable analogue of the autobidding sys-
tem prevalent in the modern online ad system?
All these questions are not straightforward to
answer, yet, have not been formally discussed in
any literature to the extent of our knowledge.
Our contribution. In this paper, we introduce
a vast amount of research questions to operate
LLMA in practice. Similar to SA, our framework
consists of four modules, though the implementa-
tion of each module will be very different from SA:
(i) modification in which the original output of
LLM is modified; (ii) bidding that advertisers uti-
lize to bid on the modified outputs; (iii) prediction
in which LLMA computes required information
about advertisements; and (iv) auction in which
the advertises compete and the final output is se-
lected. We introduce several design choices avail-
able for each module, which are evaluated based
on a reasonable set of criteria required to main-
tain a sustainable online platform. We further dis-
cuss specific research challenges inherent to each
module, and finally propose a unified perspective
in how on could interpret recent approaches for
LLM advertisement platform within our frame-
work. Although we believe that our framework
may be grounded as an initial stepping stone for
future research, our primary purpose is to discuss
research questions that should be addressed for
the practical operation of LLM advertisement. 4
2 Related works
Here, we discuss related works on LLMs, online
ads, and their intersection. Further discussion can
be found in Appendix A.
Large Language Models. Advancements in
AI, NLP, and conversational agents, driven by
Transformer architecture (Vaswani et al., 2017),
have given rise to models like GPT-3 (Brown
et al., 2020) and BERT (Devlin et al., 2019).
These models revolutionize chatbots, enabling
context-aware, human-like interactions across di-
verse domains (Abd-Alrazaq et al., 2020; Nico-
lescu and Tudorache, 2022). Everyday use of lan-
guage models has led researchers to investigate
the content generated by these models to ensure
that they do not hallucinate (Guerreiro et al.,
2023; Ji et al., 2023; Li et al., 2023; Zhang et al.,
2023) in their outputs, and do not generate harm-
ful or biased content (Liang et al., 2021; Navigli
et al., 2023; Kirk et al., 2021; Shen et al., 2023;
4As an independent interest, in Appendix D, we discuss
how LLM (more generally generative model) can empower
the online advertisement system to tailor the content of
ads itself to individual users, leveraging their specific con-
texts to generate more appealing content, which is called as
dynamic creative optimization (DCO) or responsive ad in
the literature. The incorporation of DCO into the SA, es-
pecially for LLMA, would bring further challenges in each
module and we propose corresponding research questions
therein.
3

Weidinger et al., 2021; Liu et al., 2023b). In fact,
trustworthy of LLMs is actively studied by re-
searchers (Liu et al., 2024).
Online Advertisement. Online advertis-
ing, particularly within the context of sponsored
search auctions, has evolved in recent years, with
notable contributions from prior research. Spon-
sored search auctions have been a subject of ex-
tensive investigation, emphasizing the optimiza-
tion of bidding strategies and keyword relevance.5
Edelman et al. (2007) provided valuable insights
into the economics of sponsored search auctions,
shedding light on the dynamics of keyword auc-
tions. Goel et al. (2009) proposed a contract auc-
tion between the advertiser and the publisher, and
introduce impression-plus-click pricing for spon-
sored search auction as an application. We refer
to the book by Roughgarden (2010) for more de-
tails.
Mechanism design with LLM agents. Duet-
ting et al. (2023) recently proposes a mechanism
design problem when the bidders are LLM agents.
More specifically, the bidders bid on desired dis-
tributions of the next token , given the history of
the tokens. They denote this problem by token
auction, and provide theoretical foundations of
what a reasonable mechanism should look like.
Indeed, their model can be considered as a ver-
sion of our advertiser modification and dynamic
bidding framework. Notably, they require the ad-
vertisers to provide their desired distribution and
corresponding bidding for every token, which may
require significant communication burden to run
the mechanism in practice. In contrast, the ad-
vertisers in our framework only bid once for the
modified output, thereby inducing less communi-
cation cost.
3 Framework for LLMA
We here present a potential framework for LLMA.
We introduce several feasible types of frameworks
for LLMA, each of which has its own pros and
cons. Mainly, we focus on a scenario in which
a user provides a query q to the LLM, and the
5Online advertisement can be categorized by either of
search or display ads. We here focus on search ads.
Original output generation
LLM Advertisement System
𝑎𝑑! 𝑎𝑑" 𝑎𝑑#…User context 𝑐
Query 𝑞
𝑞,𝑐→𝑋
Modification
Bidding
Prediction
Auction
𝑞,𝑐,𝑋,𝑎𝑑$→𝑋$
𝑞,𝑐,𝑋,𝑋$→𝑏$
𝑞,𝑐,𝑋,𝑋$→𝑠𝑟$,𝑐𝑡𝑟$
𝑠𝑟$,𝑐𝑡𝑟$,→𝑥⃗,𝑝⃗
Figure 2: Overall framework of LLMA.
original output by LLM is given by X. Further,
a contextc captures a variety of features that are
relevant to the advertisement recommendation,
e.g., history of the previous queries, user segment,
region, and date. 6 Although the number of ad-
vertisers varies from time to time, when the user
inputs the query q, we suppose that there are n
advertisers (bidders) indexed by adv 1,..., advn,
each of which is equipped with a single advertise-
ment (ad) ad i he/she wants to post.
Overall, we divide the LLMA as follows based
on their functionalities 7 into 4 modules: (i) out-
put modification, (ii) bidding, (iii) prediction, and
(iv) auction. This overall framework is illustrated
in Figure 2. In short,
1. The user writes query q possibly with context
c;
2. The LLMA generates the original output X;
3. Modification module creates modified output
Xi per ad.
4. Bidding module generates corresponding bid
bi.
5. Prediction module predicts user satisfaction
rate (SR) sr i and click-through-rate (CTR)
ctri.
6Note here that we assume LLMA could collect such
information from the user similar to the standard search
engines, but our model accommodates the setting without
such data. An illustrative example using such context is
provided in Figure 5 in the appendix.
7These functionalities may be distributed to multiple
market players such as supply side platform, display side
platform, or ad exchange, as does in the current online ad
eco-system.
4

6. Auction module determines the final output
and corresponding payment to charge the se-
lected advertiser.8
For the rest of the section, we will explain each
module and its responsibility/functionality in a
sequential manner.
3.1 Modification module
The modification module takes responsibility for
generating modified output based on the ads’ tex-
tual information. This module takes the pair of
(q,X,c ) and a set of advertisements as the input,
and returns (Xi)i∈[n] where Xi denotes the mod-
ified output for ad i.
Overall, we consider two design choices: 9
1. In advertiser modification model, the role of
generating the modified output is delegated
to each advertiser.
2. In LLMA modification model, LLMA di-
rectly generates the modified output.
In Section 5.1, we explore ways to reduce the com-
putational load of generating candidate outputs.
Comparison to SA. Note that the standard SA
does not have modification module explicitly as
it is trivial to incorporate ads in each slot. Thus,
it is the unique challenge appearing in LLMA.
Further, we note that LLM is only directly used in
the modification module as well as in generating
the original output X, whereas other modules do
not require LLM to operate them. Nevertheless,
they entail specific technical challenges adhered
to LLMA, which will be elaborated accordingly.
3.2 Bidding module
The bidding module generates bids based on mod-
ified outputs. It takes the query q, contextc, and
modified outputs ( Xi)i∈[n] as input and outputs
8We first focus on presenting a single advertisement in
the LLM output, however, generalization of the proposed
framework to incorporate multiple ads at once is discussed
in Section 5.4.
9For either cases, one can generate the modified output
by giving an additional query to the LLM as presented in
Figure 1.
bids (bi)i∈[n], representing each advertiser’s pri-
vate valuation of impressions, clicks, or conver-
sions. We consider two design choices.
1. In the dynamic bidding model, we provide
the query q, context c, original output X,10
and modified outputXi to the bidder for each
query, who then returns the bid.
2. In the static bidding model, each bid is based
on keywords from a pre-committed contract,
without further communication with the ad-
vertiser.
The static bidding model operates by extracting
keywords from q, determining relevant ads, and
requiring advertisers to set targeted keywords. In
Section 5.2, we discuss extensions of these bidding
models that allow more flexible bidding strategies.
This approach can be preferred when the bid unit
accurately represents the advertiser’s true valua-
tion, regardless of output quality, such as clicks
or conversions.
Dynamic bidding models interest advertisers
with their measures to estimate the quality of
modified output. For instance, if LLMA only con-
siders CTR and ignores user experience, advertis-
ers may wish to adjust bids based on their output
quality assessment. Despite a high likelihood of
clicks or conversions, poor user experience with
low-quality outputs could harm satisfaction with
the advertised product.
Comparison to SA. In SA, since the context
of user query is more explicit represented as key-
words, advertisers can safely bid on each keyword.
In LLMA, however, it might be difficult to extract
proper keywords from the query as the query it-
self tends to be much longer than the traditional
SA due to the flexibility of LLM. On the other
hand, one can instruct the LLM to extract core
keywords or use word embeddings to calculate
the similarity between the modified output and
query. Further, the generated output significantly
affects the marketing impact of the ads in LLMA,
whereas it is typically independent from other ads
/ contents shown within SERP in SA. Finally, the
10An encrypted context ˆc or no context could be consid-
ered for privacy.
5

dynamic bidding model exhibits unique challenges
of dynamically adjusting the bid with respect to
the output, which could further be delegated to
another market player or LLM agent.
3.3 Prediction Module
The prediction module computes the user’s satis-
faction rate (SR) and click-through rate (CTR).
The SR measures user satisfaction with the out-
put and influences the decision-making process of
the language model to avoid disappointing out-
puts. The CTR represents the likelihood of the
user clicking on the ad link in the output and is
crucial for determining auction winners, as it di-
rectly impacts the LLMA’s revenue. Specifically,
if an advertiser’s bidding method is cost-per-click
(CPC), the expected revenue from the ad is cal-
culated as CPC multiplied by the CTR. Overall,
both of SR and CTR are functions of original out-
putX, modified output X′, query q, and context
c, which returning a real value in [0 , 1].
Comparison to SA. Different from the tradi-
tional SA whose output is static (ad image/hy-
perlinks), LLMA constructs textual outputs in a
complicated manner. This makes the prediction
module more difficult to learn the CTR. More-
over, in LLMA, the prediction of user satisfaction
is much more directly affected by the incorpora-
tion of the ads in the output. This is in stark
contrast with SA, whose user experience is usu-
ally affected only by the number of ad slots/po-
sitions in SERP. Detailed methodologies for esti-
mating/learning these functions will be discussed
in Section 5.3.
3.4 Auction module
Having computed all the required parameters, we
run the auction module to determine the auc-
tion winner and the advertiser’s charge. The
input to the auction module is the tuples
(bidi, sri, ctri)i∈ [n], representing bid amount,
satisfaction rate, and click-through rate. The auc-
tion module outputs an (possibly randomized)
allocation ⃗ x∈ [0, 1]n and payments ⃗ p∈ Rn ≥0.
Specifically, the module determines the auction
format, including the allocation function, which
selects the ad, and the payment function, calcu-
lating the advertiser’s payment to LLMA. 11
The main goal of LLMA is to maximize its
long-term revenue by balancing short-term rev-
enue with user retention. The objective is mod-
eled as a function from bid amount, CTR, and
SR to a nonnegative score for a modified output,
i.e., selecting i∗ = argmax i∈[n] Obj(sri, ctri, bidi).
We do not detail the objective function choice,
given the extensive literature on sponsored search
auctions. After designing the score function, an
auction format should be determined, with many
mechanisms available, such as VCG auction or
generalized second price auction as desired.
Comparison to SA. The main difference to the
SA is, similar to what is discussed in the previ-
ous subsection, the user satisfaction is much more
important measure to account for. For example,
the allocation function in SA represented by (1.1)
is social welfare which only accounts for platform
and advertisers’ utility. In LLMA, however, one
might also need to consider user’s utility as a func-
tion of predicted SR, which would change the al-
location function of the mechanism and the pay-
ment correspondingly.
4 Market Players and Desider-
ata
Given the potential framework for LLMA and the
presented design choices, we outline several cru-
cial aspects for evaluating each design choice’s fea-
sibility and practicality.
In modern search or display ad auctions, nu-
merous market players are involved, including ad-
vertisers, users, and platforms. The platform it-
self is often divided among several players like
the demand-side platform, supply-side platform,
publisher, and ad exchange. In essence, the ad
platform must balance these players’ utilities to
create a sustainable ecosystem. For example, if
the platform shows too many ads in response to
11This form doesn’t allow for adjusting the final output
to balance multiple advertisers’ preferences, unlike auctions
that consider bids and preferences, as in Duetting et al.
(2023). However, our framework can be extended for such
cases, elaborated in Appendix B.
6

a user’s query, user retention will likely decrease,
discouraging advertisers from using the platform,
and eventually harming the ecosystem. Similarly,
for LLMA to sustain long-term revenue growth, it
must balance the utilities of market players. We
will outline the key aspects of the most crucial
players: the user, the advertiser, and the plat-
form.
4.1 Player’s incentive
User experience. When adding advertise-
ments to LLM output, maintaining high content
quality is crucial. Users dislike excessive or ir-
relevant ads, which can degrade the output and
reduce user satisfaction and retention. In mod-
ern online ad systems, floor prices are used to
filter out irrelevant ads and preserve user expe-
rience quality. Similarly, for LLM services, we
must ensure that the final output, including ads,
remains a high-quality response and closely aligns
with what the LLM would originally generate.
Advertiser experience. Advertisers pay
LLMA to include ads in outputs, expecting their
products or services to be showcased compellingly.
Ads should be engaging and interesting to users,
efficiently driving revenue for the advertisers at
smaller costs. It is worth noting that advertise-
ments may potentially reduce the overall number
of users engaging with the system, which could
have adverse effects on LLM itself.
Platform revenue. Revenue is LLMA’s pri-
mary goal, so it must ensure that the additional
cost of advertisements is covered by the revenue
from advertisers. This is especially critical for
LLMA compared to SA, due to the higher compu-
tational costs and infrastructure required to run
LLMs.
4.2 Desiderata
To balance the utilities of all players and ensure
a sustainable LLMA, the following criteria should
be considered from the platform’s perspective.
Output quality. The LLM’s textual output
should align with the user’s preferences and the
query. This involves (a) ensuring the ad is rele-
vant to the user’s query and (b) making sure the
LLM output aligns with the user’s preferences.
This includes standard LLM evaluation criteria
like accuracy, relevance, coherence, and compre-
hensiveness.
Additionally, the output should reflect adver-
tisers’ preferences, ensuring their ads are inte-
grated as desired and their bids accurately repre-
sent their preferences for the query and modified
output.
Allocational objective and revenue. As a
mediator, LLMA can optimize social welfare to
achieve allocational efficiency, i.e., allocate ads to
maximize social welfare deterministically or try
to maximize its revenue. On the other hand,
probabilistic retrieval of textual information as
prompts, as shown by Lewis et al. (2020), en-
hances LLM performance by managing ambigu-
ity, diversifying output, and improving robust-
ness to noise and errors. Therefore, LLMA’s al-
location objective should balance these aspects
while ensuring sufficient revenue to avoid oper-
ating deficits.12
Latency. In LLMA, users expect rapid inter-
actions, similar to search auctions, where prompt
responses are typical. Adding advertisements to
LLM output introduces some latency, but this
should be minimal to avoid disrupting the user
experience. The latency requirement for LLMA
can be less strict than for search auctions because
LLMA generates output word-by-word, whereas
search auctions need to retrieve all ads and re-
sults immediately upon a query.
Reliability and privacy. LLMA must also
address potential risks from advertisers, ensuring
system reliability and alignment by considering all
possible adversarial behaviors (Hendrycks et al.,
2020), e.g., harmful contents or spam links in ads.
Additionally, maintaining user privacy is crucial.
All user context, information, and data must be
kept secure (or encoded) to prevent privacy risks
from inadvertent disclosure.
12This is also largely discussed in Hajiaghayi et al.
(2024), where we refer to Appendix B for more details.
7

5 Challenges
Recall that our overall framework consists of four
modules: modification, bidding, prediction, and
auction module. For each module, we address
characteristics, technical challenges, and research
questions relevant to practical implementation
and evaluation based on the criteria defined in
Section 4. Further discussions are provided in Ap-
pendix C.
5.1 Modification module
Challenges: An advertiser modification
model should ensure alignment with user
preferences and satisfaction while address-
ing privacy, reliability, and latency issues.
In the advertiser modification model, LLMA must
provideq,X, andC to each advertiser advi, which
can lead to privacy issues by disclosing user infor-
mation. Addressing this involves partial or indi-
rect information disclosure, possibly using encryp-
tion or differential privacy to protect user data
while ensuring high-quality outputs.
Additionally, the model faces reliability issues
as advertiser-modified outputs might include il-
legal or spam content, which may degrade user
satisfaction compared to original LLM outputs.
LLMA may require an additional module to en-
sure robustness against such adversarial behavior,
but this adds cost of computational resources and
latency.
Moreover, increased communication between
LLMA and advertisers can raise latency. There-
fore, developing efficient protocols is crucial for
managing a functional online ad system. The ad-
vertiser modification model thus requires novel so-
lutions to address privacy, reliability, and latency
concerns.
Challenges: Effectively reflecting advertiser
preference on the output for LLMA modi-
fication model. The LLMA modification model
generally faces fewer privacy, reliability, and la-
tency issues compared to others and focuses on
enhancing user experience. However, it may not
fully align with advertiser preferences in the out-
put modification process, potentially reducing ad-
vertiser satisfaction. Thus, it is important to ex-
plore methods for better incorporating advertis-
ers’ preferences into the modified output, ensur-
ing that it meets their expectations while still im-
proving the user experience.
Prospect: Balancing the trade-off between
LLMA and advertiser modification models.
To improve advertiser satisfaction in the LLMA
modification model, one approach is to let adver-
tisers submit indirect indicators of their prefer-
ences. Specifically, after receiving the query q,
the original output X, and possibly context c,
the advertiser provides a documentY (or a list of
it) reflecting its preferences. LLMA can then use
Y as a prompt to generate the modified output
as per RAG framework, allowing more flexibil-
ity in capturing advertiser preferences. However,
this method introduces additional communication
costs, potentially increasing latency.
Challenges: Reducing the computational
burden of generating every potential candi-
date outputs. Both the advertiser and LLMA
modification models require generating all possi-
ble output candidates for each potential ad. In
the LLMA modification model, this involves mul-
tiple runs of the LLM’s token sequence generation
for each ad in the auction. Given the high cost of
LLM operations, this approach may not scale well
as the number of ads on the platform increases.
Prospect: Ex-ante allocation without gen-
erating potential candidate outputs One
feasible approach is to implement a prefiltering
process to reduce the number of ads competing by
filtering out less relevant ads. Alternatively, the
auction can be run without generating every pos-
sible candidate output by using a modular compo-
nent to predict the characteristics of the modified
output for each candidate ad.
For instance, features can be extracted from the
query and ad text, and semantic distances can be
computed based on text similarity. Advertisers
should be aware of this indirect measure and bid
accordingly, assuming the semantic distance will
represent the expected output quality. The mech-
anism then uses submitted bids and semantic dis-
tances to determine the ad and generate the final
8

output, requiring only a single generation for the
allocated ad. Hajiaghayi et al. (2024) takes this
approach, elaborated further in Appendix B.
5.2 Bidding module
Challenges: Implementing dynamic bidding
model without privacy and latency issue.
The main advantage of the dynamic bidding
model is its potential to increase advertiser sat-
isfaction, as advertisers can adjust their bids af-
ter seeing the modified output. This flexibility
can be appealing to advertisers with the tech-
nical capability to dynamically set bids. How-
ever, the dynamic bidding model may introduce
privacy issues if LLMA discloses private informa-
tion to advertisers. It may also lead to additional
latency since the entire set of modified outputs
must be delivered to advertisers. Reliability con-
cerns are minimal, as only the bid amount is com-
municated. In contrast, the static bidding model
avoids privacy, latency, and reliability issues but
may reduce advertiser satisfaction because adver-
tisers cannot adjust their bids based on the mod-
ified output.
Research should focus on the practicality of
dynamic bidding, including developing protocols
and algorithms that address privacy and latency
concerns. One may also investigate how the ad
market would comprise of, when there is a pos-
sibility that the advertisers hire a proxy agent to
submit bids on behalf of them, and how the proxy
agent (or advertisers themselves) can optimize
bids in such scenario. In addition, the emergence
of autobidding system can be expected, which we
detailed in Appendix C.
Prospect: Balancing the trade-off between
static/dynamic bidding models. In the static
bidding model, improving advertiser satisfaction
can be achieved by defining a more flexible static
function as the contract between the advertiser
and LLMA. Specifically, LLMA could propose a
contract where bids are determined by an indi-
rect measure of the modified output. For exam-
ple, LLMA and the advertiser might agree on a
contract where the bid is inversely proportional
to the similarity distance d between the original
output X and the modified output Xi. If Xi sig-
nificantly deviates fromX, the similarity distance
will be large, leading to a lower bid from the ad-
vertiser due to concerns about user experience.
Advertisers will need to understand how LLMA
estimates and defines this distance measure.
LLMA could also develop a more refined method
for assessing user interest, attention, and rele-
vance for the modified output from the adver-
tiser’s perspective, allowing advertisers to choose
contracts based on their preferences.
5.3 Prediction module
Challenge: Efficient and precise implementa-
tion of prediction module. Estimating CTR
in LLMA can follow principles similar to those in
modern online advertising. We can train a predic-
tion system to estimate ctri∈ [0, 1] based on input
Xi,q, andc, using user feedback data. For exam-
ple, factorization machines and online algorithms
can be used after feature extraction from user
data, context, and queries, as described in McMa-
han et al. (2013). Given the sparse frequency of
eachXi in the family of possible outputs, features
from q, Xi, and c should be extracted to map to
CTR values. User actions like regenerating re-
sponses, clicking ads, or exiting the LLM can be
used to refine the prediction module.
Challenge: Relevance/similarity distance
measure to estimate user satisfaction. To
estimate SR, one approach is to assume that the
original output X is optimal. In this case, the
distance between X and the modified output Xi
can serve as a measure of SR, since the closer
Xi is to X, the higher the expected user satisfac-
tion. For example, one might define the output
distance as d(X,X i) :=||Pr(X|q)− Pr(Xi|q)|| us-
ing a suitable norm. Here, Pr(X|q) represents the
marginal probability of X given q, which can be
computed using standard methods from the liter-
ature (Vaswani et al., 2017).
More general functions, such as semantic sim-
ilarity between documents or phrases (Mikolov
et al., 2013; Cer et al., 2018; Conneau et al., 2019),
can be used. One can further implement a calibra-
tion layer to maintain well-calibrated with higher
9

accuracy (McMahan et al., 2013). The key re-
search question is to identify effective measures
for predicting user satisfaction when ads are in-
corporated into the output.
Prospect: Incorporating distance measure
and online learning. As discussed, one may
consider combining similarity measure and online
learning from user feedback for prediction. To
online learn SR (or CTR) estimates from user
feedback, a useful indicator of whether the user
is satisfied with the output is whether the user
re-generates the output. One may aim to learn
a function which outputs the sr, given the query
q, modified output X′, and context c. This ap-
proach does not assume that the original output
X is indeed optimal, thereby allowing the possi-
bility that the user may be satisfied with a mod-
ified output Xi even though its distance from X
is measured is large. This comes at the cost of
additional modular component for learning pro-
cess. One could further consider an online learn-
ing model where the similarity distance is also
integrated as one of the features for prediction.
If the similarity distance has some positive cor-
relations with the true user satisfaction rate, this
would increase the accuracy of the prediction. Es-
sentially, an effective way to capture the both ad-
vantages of online learning and distance measure
should be studied thoroughly.
5.4 Auction module
Challenge: Incorporating multiple ads in a
single output. Recall that our framework is pre-
sented for single-ad allocation setting. One ap-
proach to generalize our framework is to repeat-
edly run the overall procedure and allocate a sin-
gle at once. That is, one can determine an ab-
stract unit that partitions the output, e.g., para-
graph, and run our framework for each unit. An-
other direct approach to extend our framework
is, to let the final output to be displayed the
one that does not necessarily belong to {Xi}i∈[n],
but rather a new output X′ that interpolates
{Xi}i∈[n]. This resembles the approach of aggre-
gating the preference by Duetting et al. (2023);
Soumalias et al. (2024). More discussions can
be found in Appendix B. By doing so, it might
be possible to deliver multiple advertisements in
a fair manner, thereby allowing LLMA to bring
more revenue by charging multiple advertisers at
once. 13
One subtle issue is that, since each advertiser
bids bi on delivering Xi, they may not want to
write the same bid for the balanced output X′,
thus it may degrade the advertiser’s experience.
In the static bidding model, as discussed in Sec-
tion 5.2, this might be handled by committing
to a contract based on measures that represents
the advertiser’s preferences more in a refined man-
ner. In the dynamic bidding model, one approach
would be to append an additional step of asking
for bids for the final output again to the advertis-
ers.
5.5 Discussion on Recent Approaches
Several recent theoretical approaches have pro-
posed game-theoretic models for ad auctions in
LLMs. We here discuss how these can be seen as
implementations of our framework. 14
First, Duetting et al. (2023) propose a model
where bidders submit bids and distributions over
tokens. This aligns with a tokenized version of
our model with (i) LLMA modification by aggre-
gating token distributions, (ii) dynamic bidding
with adjustments for each query, (iii) no predic-
tion module as it focuses on advertiser perspec-
tives, and (iv) running a token auction. This ap-
proach might suffer from latency and reliability
issue, but could possibly maintain high advertiser
experience.
Hajiaghayi et al. (2024) integrate the RAG
framework for segment-based ad auctions, where
ads are probabilistically retrieved for segments
like paragraphs using bids and a notion of rel-
evance. This corresponds to (i) LLMA modifi-
cation without pre-generating outputs, (ii) static
bidding based on clicks, (iii) indirect CTR predic-
tion by measuring ad relevance, and (iv) running a
segment auction. Their approach has less privacy,
latency and reliability, but advertiser’s experience
13Another way to display multiple ads at once will is
discussed in Appendix C under our original framework.
14Further details are deferred to Appendix B.
10

could be largely dependent on how modular com-
ponents to compute relevance is designed.
Dubey et al. (2024) introduce a framework that
generalizes position auctions by determining pay-
ment and a notion of prominence as allocation
function. This aligns with (i) LLMA modification,
(ii) static bidding, (iii) no prediction required, as
prominence serves as a CTR proxy, and (iv) run-
ning a prominence auction. Similar toHajiaghayi
et al. (2024), advertiser’s experience highly de-
pends on how LLM well constructs the output
with desired prominence.
Soumalias et al. (2024) propose an auction that
truthfully aggregates advertiser preferences us-
ing RLHF framework. This can be viewed as
(i) LLMA modification, (ii) static bidding, (iii)
no prediction needed, focusing only on advertiser
perspectives, and (iv) running an RLHF-based
auction. This requires relatively larger latency is-
sue since every potential candidate output needs
to be created and advertiser’s reward function
should be communicated accordingly, however, it
could possibly reflect advertiser’s preference bet-
ter.
6 Conclusion
This paper addresses the opportunities and chal-
lenges for leveraging an online advertisement sys-
tem with LLM. We first discuss essential require-
ments which a reasonable LLM advertisement sys-
tem should satisfy. To fulfill such desiderata,
we introduce several frameworks and substantiate
their validity. We compare proposed frameworks
with their advantages and limitations. Then we
discuss further technical and practical challenges
in designing efficient online advertising with LLM.
Finally, as a usecase of independent interest, we
present the potential of advanced dynamic cre-
ative optimization by using LLM.
References
Alaa Ali Abd-Alrazaq, Asma Rababeh, Mohan-
nad Alajlani, Bridgette M Bewick, and Mowafa
Househ. Effectiveness and safety of using chat-
bots to improve mental health: systematic re-
view and meta-analysis. Journal of medical In-
ternet research, 22(7):e16021, 2020.
AdWeek. Microsoft advertisements on
AI driven chat based search. https:
//www.adweek.com/media/microsoft-
details-how-advertising-works-on-
bings-ai-driven-chat-based-search , 2023.
Rohan Anil, Andrew M Dai, Orhan Firat, Melvin
Johnson, Dmitry Lepikhin, Alexandre Passos,
Siamak Shakeri, Emanuel Taropa, Paige Bailey,
Zhifeng Chen, et al. Palm 2 technical report.
arXiv preprint arXiv:2305.10403 , 2023.
Lennart Baardman, Elaheh Fata, Abhishek Pani,
and Georgia Perakis. Dynamic creative opti-
mization in online display advertising.Available
at SSRN 3863663 , 2021.
Tom Brown, Benjamin Mann, Nick Ryder,
Melanie Subbiah, Jared D Kaplan, Prafulla
Dhariwal, Arvind Neelakantan, Pranav Shyam,
Girish Sastry, Amanda Askell, et al. Lan-
guage models are few-shot learners. Advances
in neural information processing systems , 33:
1877–1901, 2020.
S´ ebastien Bubeck, Varun Chandrasekaran, Ro-
nen Eldan, Johannes Gehrke, Eric Horvitz, Ece
Kamar, Peter Lee, Yin Tat Lee, Yuanzhi Li,
Scott Lundberg, Harsha Nori, Hamid Palangi,
Marco Tulio Ribeiro, and Yi Zhang. Sparks
of artificial general intelligence: Early experi-
ments with gpt-4, 2023.
Daniel Cer, Yinfei Yang, Sheng-yi Kong, Nan
Hua, Nicole Limtiaco, Rhomni St John, Noah
Constant, Mario Guajardo-Cespedes, Steve
Yuan, Chris Tar, et al. Universal sentence en-
coder. arXiv preprint arXiv:1803.11175 , 2018.
Hana Choi, Carl F Mela, Santiago R Balseiro, and
Adam Leary. Online display advertising mar-
kets: A literature review and future directions.
Information Systems Research , 31(2):556–575,
2020.
Alexis Conneau, Kartikay Khandelwal, Naman
Goyal, Vishrav Chaudhary, Guillaume Wenzek,
Francisco Guzm´ an, Edouard Grave, Myle Ott,
11

Luke Zettlemoyer, and Veselin Stoyanov. Un-
supervised cross-lingual representation learn-
ing at scale. arXiv preprint arXiv:1911.02116 ,
2019.
Tech Crunch. That was fast! Microsoft slips
ads into AI-powered Bing Chat. https:
//techcrunch.com/2023/03/29/that-was-
fast-microsoft-slips-ads-into-ai-
powered-bing-chat/, 2023.
Giannis Daras and Alexandros G Dimakis. Dis-
covering the hidden vocabulary of dalle-2.
arXiv preprint arXiv:2206.00169 , 2022.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. Bert: Pre-training of deep
bidirectional transformers for language under-
standing, 2019.
Kumar Avinava Dubey, Zhe Feng, Rahul Ki-
dambi, Aranyak Mehta, and Di Wang. Auc-
tions with llm summaries. arXiv preprint
arXiv:2404.08126, 2024.
Paul Duetting, Vahab Mirrokni, Renato Paes
Leme, Haifeng Xu, and Song Zuo. Mecha-
nism design for large language models. arXiv
preprint arXiv:2310.10826, 2023.
Benjamin Edelman, Michael Ostrovsky, and
Michael Schwarz. Internet advertising and the
generalized second-price auction: Selling bil-
lions of dollars worth of keywords. American
economic review, 97(1):242–259, 2007.
Yiding Feng, Brendan Lucier, and Aleksandrs
Slivkins. Strategic budget selection in a com-
petitive autobidding world. In Proceedings of
the 56th Annual ACM Symposium on Theory
of Computing, pages 213–224, 2024.
Daniel Fried, Armen Aghajanyan, Jessy Lin,
Sida Wang, Eric Wallace, Freda Shi, Ruiqi
Zhong, Wen-tau Yih, Luke Zettlemoyer, and
Mike Lewis. Incoder: A generative model for
code infilling and synthesis. arXiv preprint
arXiv:2204.05999, 2022.
Sharad Goel, S´ ebastien Lahaie, and Sergei Vassil-
vitskii. Contract auctions for sponsored search.
In International Workshop on Internet and
Network Economics , pages 196–207. Springer,
2009.
GoogleDisplayAd. About responsive search ads
. https://https://support.google.com/
google-ads/answer/7684791?hl=en, 2024.
GoogleSearchAd. About responsive display
ads . https://support.google.com/google-
ads/answer/6363750?hl=en, 2024.
Nuno M. Guerreiro, Duarte Alves, Jonas Walden-
dorf, Barry Haddow, Alexandra Birch, Pierre
Colombo, and Andr´ e F. T. Martins. Hallucina-
tions in large multilingual translation models,
2023.
MohammadTaghi Hajiaghayi, S´ ebastien Lahaie,
Keivan Rezaei, and Suho Shin. Ad auctions for
llms via retrieval augmented generation. arXiv
preprint arXiv:2406.09459, 2024.
Dan Hendrycks, Collin Burns, Steven Basart, An-
drew Critch, Jerry Li, Dawn Song, and Jacob
Steinhardt. Aligning ai with shared human val-
ues. arXiv preprint arXiv:2008.02275 , 2020.
Million Insight. Global Search advertis-
ing. https://www.millioninsights.com/
snapshots/search-advertising-market-
report, 2022.
Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu,
Dan Su, Yan Xu, Etsuko Ishii, Ye Jin Bang,
Andrea Madotto, and Pascale Fung. Survey
of hallucination in natural language generation.
ACM Computing Surveys , 55(12):1–38, March
2023. ISSN 1557-7341. doi: 10.1145/3571730.
URL http://dx.doi.org/10.1145/3571730.
Hannah Rose Kirk, Yennie Jun, Filippo Volpin,
Haider Iqbal, Elias Benussi, Frederic Dreyer,
Aleksandar Shtedritski, and Yuki Asano.
Bias out-of-the-box: An empirical analysis of
intersectional occupational biases in popular
generative language models. In M. Ranzato,
A. Beygelzimer, Y. Dauphin, P.S. Liang, and
J. Wortman Vaughan, editors, Advances in
Neural Information Processing Systems , vol-
ume 34, pages 2611–2624. Curran Associates,
12

Inc., 2021. URL https://proceedings.
neurips.cc/paper_files/paper/2021/
file/1531beb762df4029513ebf9295e0d34f-
Paper.pdf.
S´ ebastien Lahaie, David M Pennock, Amin
Saberi, and Rakesh V Vohra. Sponsored search
auctions. Algorithmic game theory , 1:699–716,
2007.
Patrick Lewis, Ethan Perez, Aleksandra Piktus,
Fabio Petroni, Vladimir Karpukhin, Naman
Goyal, Heinrich K¨ uttler, Mike Lewis, Wen-
tau Yih, Tim Rockt¨ aschel, et al. Retrieval-
augmented generation for knowledge-intensive
nlp tasks. Advances in Neural Information Pro-
cessing Systems, 33:9459–9474, 2020.
Junyi Li, Xiaoxue Cheng, Wayne Xin Zhao, Jian-
Yun Nie, and Ji-Rong Wen. Halueval: A
large-scale hallucination evaluation benchmark
for large language models. In Proceedings of
the 2023 Conference on Empirical Methods in
Natural Language Processing, pages 6449–6464,
2023.
Paul Pu Liang, Chiyu Wu, Louis-Philippe
Morency, and Ruslan Salakhutdinov. Towards
understanding and mitigating social biases in
language models. In Marina Meila and Tong
Zhang, editors, Proceedings of the 38th In-
ternational Conference on Machine Learning ,
volume 139 of Proceedings of Machine Learn-
ing Research, pages 6565–6576. PMLR, 18–24
Jul 2021. URL https://proceedings.mlr.
press/v139/liang21a.html.
Haotian Liu, Chunyuan Li, Qingyang Wu, and
Yong Jae Lee. Visual instruction tuning. arXiv
preprint arXiv:2304.08485, 2023a.
Wenhao Liu, Xiaohua Wang, Muling Wu, Tian-
long Li, Changze Lv, Zixuan Ling, Jianhao Zhu,
Cenyuan Zhang, Xiaoqing Zheng, and Xuan-
jing Huang. Aligning large language models
with human preferences through representation
engineering, 2023b.
Yang Liu, Yuanshun Yao, Jean-Francois Ton,
Xiaoying Zhang, Ruocheng Guo, Hao Cheng,
Yegor Klochkov, Muhammad Faaiz Taufiq, and
Hang Li. Trustworthy llms: a survey and guide-
line for evaluating large language models’ align-
ment, 2024.
Brendan Lucier, Sarath Pattathil, Aleksandrs
Slivkins, and Mengxiao Zhang. Autobidders
with budget and roi constraints: Efficiency, re-
gret, and pacing dynamics. In The Thirty Sev-
enth Annual Conference on Learning Theory ,
pages 3642–3643. PMLR, 2024.
Aman Madaan, Niket Tandon, Prakhar Gupta,
Skyler Hallinan, Luyu Gao, Sarah Wiegreffe,
Uri Alon, Nouha Dziri, Shrimai Prabhumoye,
Yiming Yang, et al. Self-refine: Iterative re-
finement with self-feedback. Advances in Neu-
ral Information Processing Systems, 36, 2024.
H Brendan McMahan, Gary Holt, David Scul-
ley, Michael Young, Dietmar Ebner, Julian
Grady, Lan Nie, Todd Phillips, Eugene Davy-
dov, Daniel Golovin, et al. Ad click prediction:
a view from the trenches. In Proceedings of
the 19th ACM SIGKDD international confer-
ence on Knowledge discovery and data mining ,
pages 1222–1230, 2013.
Meta. Meta Advantage. https://www.facebook.
com/business/news/drive-business-
results-with-meta-advantage, 2023a.
Meta. Meta AI Sandbox. https:
//www.facebook.com/business/news/
introducing-ai-sandbox-and-expanding-
meta-advantage-suite, 2023b.
Microsoft. Monetize AI powered chat experiences.
https://about.ads.microsoft.com/en-us/
blog/post/may-2023/a-new-solution-to-
monetize-ai-powered-chat-experiences ,
2023.
Tomas Mikolov, Kai Chen, Greg Corrado, and
Jeffrey Dean. Efficient estimation of word rep-
resentations in vector space. arXiv preprint
arXiv:1301.3781, 2013.
Roberto Navigli, Simone Conia, and Bj¨ orn Ross.
Biases in large language models: origins, inven-
13

tory, and discussion. ACM Journal of Data and
Information Quality, 15(2):1–21, 2023.
Netflix. Netflix Started Ad-supported plan.
https://help.netflix.com/en/node/
126831/, 2022.
Luminit,a Nicolescu and Monica Teodora Tudo-
rache. Human-computer interaction in cus-
tomer service: the experience with ai chat-
bots—a systematic literature review. Electron-
ics, 11(10):1579, 2022.
Erik Nijkamp, Bo Pang, Hiroaki Hayashi, Lifu Tu,
Huan Wang, Yingbo Zhou, Silvio Savarese, and
Caiming Xiong. Codegen: An open large lan-
guage model for code with multi-turn program
synthesis. arXiv preprint arXiv:2203.13474 ,
2022.
Outbrain. Native is better than display.
https://www.outbrain.com/blog/native-
ads-vs-display-ads/, 2023.
PCMag. LLM is replacing search engine.
https://www.pcmag.com/news/when-will-
chatgpt-replace-search-engines-maybe-
sooner-than-you-think, 2023.
Tim Roughgarden. Algorithmic game theory.
Communications of the ACM , 53(7):78–86,
2010.
Tianhao Shen, Renren Jin, Yufei Huang, Chuang
Liu, Weilong Dong, Zishan Guo, Xinwei Wu,
Yan Liu, and Deyi Xiong. Large language
model alignment: A survey. arXiv preprint
arXiv:2309.15025, 2023.
Ermis Soumalias, Michael J Curry, and Sven
Seuken. Truthful aggregation of llms with
an application to online advertising. arXiv
preprint arXiv:2405.05905, 2024.
Romal Thoppilan, Daniel De Freitas, Jamie Hall,
Noam Shazeer, Apoorv Kulshreshtha, Heng-
Tze Cheng, Alicia Jin, Taylor Bos, Leslie
Baker, Yu Du, et al. Lamda: Language mod-
els for dialog applications. arXiv preprint
arXiv:2201.08239, 2022.
Kenneth E Train. Discrete choice methods with
simulation. Cambridge university press, 2009.
Ashish Vaswani, Noam Shazeer, Niki Parmar,
Jakob Uszkoreit, Llion Jones, Aidan N Gomez,
/suppress Lukasz Kaiser, and Illia Polosukhin. Attention
is all you need. Advances in neural information
processing systems, 30, 2017.
Ben Wang and Aran Komatsuzaki. Gpt-j-6b:
A 6 billion parameter autoregressive language
model, 2021.
Laura Weidinger, John Mellor, Maribeth Rauh,
Conor Griffin, Jonathan Uesato, Po-Sen
Huang, Myra Cheng, Mia Glaese, Borja Balle,
Atoosa Kasirzadeh, Zac Kenton, Sasha Brown,
Will Hawkins, Tom Stepleton, Courtney Biles,
Abeba Birhane, Julia Haas, Laura Rimell,
Lisa Anne Hendricks, William Isaac, Sean
Legassick, Geoffrey Irving, and Iason Gabriel.
Ethical and social risks of harm from language
models, 2021.
Yue Zhang, Yafu Li, Leyang Cui, Deng Cai,
Lemao Liu, Tingchen Fu, Xinting Huang, Enbo
Zhao, Yu Zhang, Yulong Chen, et al. Siren’s
song in the ai ocean: a survey on hallucina-
tion in large language models. arXiv preprint
arXiv:2309.01219, 2023.
Daniel M Ziegler, Nisan Stiennon, Jeffrey Wu,
Tom B Brown, Alec Radford, Dario Amodei,
Paul Christiano, and Geoffrey Irving. Fine-
tuning language models from human prefer-
ences. arXiv preprint arXiv:1909.08593 , 2019.
14

A Further Related Works
Chatbot advertisement. With emergence of chat-bot in various websites, several companies started
to run a chat-bot advertisement, which is often referred to as sponsored message. In the chat-bot
advertisement, the companies send some private messages on the chat-bot conversation to advertise
some products. This is very different from operating an online advertisement system over LLM, since
chat-bot advertisement simply sends some messages, but our model captures the scenario in which the
user asks a query and then LLM provides a output including some advertisements. Notably, Microsoft
Bing started to operate an online advertisement with Bing chat-bot ( e.g., see articles AdWeek (2023);
Crunch (2023); Microsoft (2023)). Indeed, once the user inputs a query in the chat-bot, the output
often includes advertisements with explicit flags that indicates this is an advertisement.
Dynamic creative optimization. Dynamic Creative Optimization (DCO) is an online advertising
strategy that involves dynamically tailoring the content of an ad based on user behavior, demographics,
and user context Baardman et al. (2021). Instead of displaying a static, one-size-fits-all ad, DCO allows
advertisers to create and serve personalized and relevant ad content to different audience segments. By
doing so the platform can improve the likelihood of user engagement, click throughs, and conversions.
DCO typically involves the use of technology and algorithms to automate the process of selecting and
assembling ad elements, such as images, copy, and calls-to-action, in real-time. This customization is
done based on user data, collected either in real-time or from previous interactions. Unlike DCO has
been typically used only in display advertising not search advertising Choi et al. (2020) since the tailored
ad creatives, e.g., personalized hyperlinks to websites, would not have much impact for structured
output of standard search engines. Due to the unstructured nature of LLM advertisement, the use of
techniques similar to dynamic creative optimization would be highly likely to be present in future. Our
paper suggests the use of LLM, more generally generative AI, to personalize the advertisement itself
to improve the relevance and quality of the advertisement.
LLM-assisted Ad Creation. Beyond using LLM for DCO, one may use it to implement a system
that can help the advertisers generating the ads itself. Indeed, there already exists a tons of online
platforms such as Japser AI for copywriting, Lexica Art for blog thumbnails, and Attentive for mobile
messaging, to help marketers construct their static ads. Further, the multi-modal capability of the
very recent ChatGPT-4o by OpenAI opens the possibility of supporting advertisers creating ad assets
with text-based interactions. In addition, Meta recently introduced an AI sandbox in their Meta
(2023a) that can help advertisers from several perspectives, including creating a variant of the given
ad, constructing an ad based on text prompts or quickly changing the ad format with respect to
specified ad channels (Meta, 2023b).
B Recent Works on Mechanism Design for LLMs
Duetting et al. (2023). The approach we discussed at the end of Section 5.4 (Auction module
part) is similar to the token auction model proposed in Duetting et al. (2023), under which the adver-
tisers equipped with their own LLM directly provide a desired distribution over the subsequent token
and corresponding bid, and then the mechanism finally decides the final distribution by running a
token auction. They provide a methodology to aggregate distribution and commits to the final one,
while constructing a reasonable payment scheme to respect the reasonable properties of auction in the
mechanism design perspective. Importantly, however, their model does require the advertisers to bid
on their preference for each token, thereby requiring more communication cost to construct the entire
output. Our advertiser modification and dynamic bidding model can be thought as a version of their
model, but the advertiser only bids on the final deterministic output. In this context, one may consider
15

Original LLM Output
Prompt:Can you give me the top 5 smartphone brands?
Output:Here are the top 5 smartphone brands:
•Apple: Known for the iPhone series and iOS operating system.
•Samsung: Offers a wide range of Android smartphones,
including the Galaxy series.
•Huawei: Known for its innovative smartphones and high-quality
cameras
•Xiaomi: Known for producing feature-rich smartphones at
competitive prices
•OnePlus: Renowned for high-performance Android phones with
a focus on speed and user experience
Modified Output
Prompt:Put brand B with its high-performance smartphones as the second item.
Output:Certainly, here's the updated list with "Brand B" and its high-
performance smartphones as the second item:
•Apple: Known for the iPhone series and iOS operating system.
•Brand B: Renowned for its high-performance smartphones, which offer
cutting-edge technology and exceptional speed
•Samsung: Offers a wide range of Android smartphones, including the Galaxy
series.
•Huawei: Known for its innovative smartphones and high-quality cameras
•Xiaomi: Known for producing feature-rich smartphones at competitive prices
Figure 3: An example of providing structured advertisement in the LLM. Left column refers to the
case where we ask above question from ChatGPT 3.5, and to incorporate the ads we use queries
specified in the right column.
Advertise to teenage boy
Prompt:Promote laptop L of brand B to teenage boy.
Output:In a computer, the CPU and RAM work together like a
supercharged gaming team. The CPU is like the team captain, making all
the fast decisions and executing plays, while the RAM holds onto the
game data that needs to be accessed quickly, like maps or player stats.
This awesome duo shines in the Laptop L from Brand B, designed to
keep up with your fast-paced games and multitasking. With this laptop,
you're always equipped to win, whether you're gaming, streaming, or
just hanging out online.
Advertise to teenage girl
Prompt:Promote laptop L of brand B to teenage girl.
Output:In a computer, the CPU and RAM are your ultimate multitasking
team. The CPU handles all the tasks you throw at it, from editing videos
to scrolling through social media, while the RAM keeps everything
running smoothly without any lag, storing all your apps and files for
quick access. Check out Laptop L from Brand B—it’s not only powerful
but also stylish, perfect for keeping up with your studies, your creative
projects, and your social life. This laptop is a must-have tool that fits
your dynamic lifestyle and lets you do it all, effortlessly and in style.
Figure 4: An example of ChatGPT 4 providing different output tailored to the user context. We keep
the context provided in Figure 1, but asks again to advertise again to the specified user segment.
16

generalizing this model by letting the advertisers to bid on a distribution over the final output, thereby
allowing the advertisers to represent their preferences more in a refined way. Note, however, that since
the entire space of possible output may be extremely large, let the advertisers bid a distribution over
such space might be practically/computationally infeasible. Alternatively, one can consider a version in
which each advertiser provides a potential set of outputs, (partial) ordering over it with corresponding
bid, and then the auction module determines the final output based on designed mechanism. Overall,
their approach can be viewed as (i) LLMA modification that aggregates the preference reported by
advertisers and (ii) dynamic bidding model where the advertisers bid on their desired preference.
Hajiaghayi et al. (2024). Recent work by Hajiaghayi et al. (2024) considers the integration of RAG
framework into the ad auctions for LLMs. In essence, they consider a single-dimensional mechanism
design problem where each advertiser has a private value on each click, and a notion of relevance
between the query and the ad’s textual information the plays as a proxy for the click-through-rate of
an allocated ad in the final output. Formally, they assume that the module to calculate the relevance
is calibrated to be proportional to the expected click-through-rate over the possible outputs given the
context of ad and query. Mainly their mechanism determines the allocation and payment function
given the bids and relevance of advertisers. Precisely, their mechanism first computes a perturbed
score inspired by discrete choice methods Train (2009), randomly retrieves an (or a set of) ad with
respect to the probabilities given by RAG framework, and charges the ad based on the perturb scores.
Interestingly, they take an approach of reverse-engineering the objective function that the allocation
function given by RAG framework tries optimize. They show that the linearly probabilistic allocation
from RAG in hindsight maximizes logarithmic social welfare. From our LLMA framework’s perspective,
their approach can be viewed as the combination of (i) LLMA modification but without generating
all the potential candidate outputs as discussed in Section 5 (Modification module part), (ii) static
bidding, (iii) CTR prediction is indirectly done by measuring relevance and (iv) running an auction
with perturbed scores.
Dubey et al. (2024). Dubey et al. (2024) considers an ad auction framework for LLMs as a
generalization of position auction in the standard SA. Similar to the relevance in Hajiaghayi et al.
(2024), they introduce a notion of prominence that captures how much each ad takes portion in the
output. In their approach, each advertiser writes a single-dimensional bid, given a collection of features
for each ad, their mechanism determines the prominence of each ad within the output. Alternatively
speaking, they calculate a desired CTR for each ad as a mechanism’s output. Then, their LLM module
retrieves the calculated prominence for each ad as an input, and it generates the entire output that is
consistent with the calculated prominence. If one deems the positional effect in the standard position
auction used in SA as the prominence, their approach can be viewed as a generalization of the position
auction. They formalize such correspondence, and characterize several theoretical properties of their
prominence auction. One subtlety in their framework is that LLM might not reliably produce an
output that is exactly consistent with the desired output. In our framework’s language, their approach
can be viewed as (i) LLMA modification, (ii) static bidding, (iii) CTR is not required for the payment
but instead prominence plays this role, and (iv) auction module calculates the prominence required for
LLM to generate the output.
Soumalias et al. (2024). Finally, Soumalias et al. (2024) proposes an auction framework to
truthfully aggregate the advertisers’ preferences. Each advertiser’s preference can be represented via
its own LLM or a reward function. Given multiple advertisers’ reward functions, the mechanism’s
objective function is to maximize the summation of the advertisers’ rewards minus a normalization
term to not too much deviate from the reference output with no advertisement. They observe an
intricate connection of such objective function to the reinforcement learning from human feedback
(RLHF) approach by Ziegler et al. (2019), and use these devices to construct a dominant-strategy
17

incentive-compatible mechanism. From our perspective, their approach can be viewed as (i) LLMA
modification, (ii) static bidding, (iii) prediction module is not required as the advertiser’s preference is
completely determined by the output, and (iv) an auction with allocation function based on the RLHF
with aggregated reward functions.
C Further challenges and practical concerns
Autobidder. In the modern search ad or display ad auction in ad platforms, significant amount of
advertisers use an autobidding system provided by the ad platforms to delegate the role of dynamically
optimizing the bids with respect to the user. The autobidding system, usually referred to as autobidder,
is even more crucial for advertisers who do not have sufficient budget to run a market research to
determine the appropriate amount of bids. In autobidder, each advertiser only is required to determine
a high level objective it wants to achieve. For instance, they may specify that they want to maximize the
number of clicks subject to the budget constraint of $100 per day, or that they want to spend at most
two bucks per each click on average. The former is typically referred to as autobidder with the budget
constraint, and the latter as with the return-on-investment (ROI) constraint. Due to its centralized
nature, autobidding intrinsically enables the platform to dominate the decentralized bidding scenario
in social welfare as well as the platform’s revenue. Correspondingly, a long line of works (Lucier et al.,
2024; Feng et al., 2024) aim to explore an efficient autobidding algorithm, analyze the dynamics of
the platform with autobidding and manual bidding advertisers, identify the resulting outcome of each
auction format under autobidders.
In a similar vein, we expect that autobidder could also play an essential role to optimize the markets
in several directions for LLMA as well. The platform may allow the advertisers to specify budget
or ROI constraint as in the standard search or display ad auction, and the set of feasible objective
functions as impression or click. Due to more complicated nature of ad appearance in the output,
it might allow alternative objective functions compared to the standard autobidding system such as
number of sentences or paragraphs dedicated to the ads, etc. The platform can also have broader
optimization space over bids sequences since it can dynamically adjust how much portion it would
spend on the output for each ad and corresponding ad. As the autobidder system inevitably emerges
as a solution in the modern search ad auction, we expect that a similar device, but perhaps with a
complicated design, would necessarily emerge in ad auctions for LLMs.
Agentic Workflow. One notable approach to implement each module of LLMA is to construct
a dedicated LLM agent to help serve the module in a similar vein with Agentic Workflow (Madaan
et al., 2024). For instance, in the LLMA modification model, LLMA might implement an LLM agent
specialized to each segment of the ads to generate the ad-incorporated output. For the prediction mod-
ule, it could exploit an LLM agent that can perform a feature extraction task to deliver useful features
from the user’s query and possibly context to the prediction module. This agent could further collab-
orate with another LLM agent that can compute the predicted CTR and SR or any other dedicated
machine learning module. Even for the bidding module, from the autobidding perspective presented
above, LLMA could utilize an LLM agent that determines each ad’s bid on behalf of the advertiser.
As the use of such dedicated LLM agent might be costly, there could be several options for contract
between LLMA and advertisers, e.g., whether the advertiser wants to use an entirely dedicated agent
specialized at higher cost or a cheaper general-purpose agent. These LLM agents do not necessarily
solve the entire task at hand, but could greatly improve the efficiency of each module once equipped
with a proper prompt engineering.
Parallelizing the process and adapting multiple types of advertisers. Recall that our
overall architecture consists of (i) modification, (ii) bidding, (iii) prediction, and (iv) auction modules.
18

Although each of the process should be serialized in order to handle a single advertiser’s process, it is
important to observe that the process (i)-(iii) is totally independent between the advertisers. Hence,
one efficient to way to minimize the latency is to process steps (i) to (iii) in an asynchronous manner
between the advertisers. To fit the desired latency requirement, one may consider excluding some
advertisers such that the steps (i) to (iii) are not completed within some maximal delay. It’s common
to have timeouts in display ads, because bids can come from real-time bidders outside the system, but
not as much for search ads as far as I’m aware. After collecting all the feasible parameters, LLMA can
pass the required parameters to step (iv) and run the auction.
One additional advantage of this procedure is that, one can easily adapt to multiple types of advertis-
ers. In practice, several advertisers may want to dynamically bid or modify the output by themselves,
while others with small businesses may not want to take too much of responsibilities. For instance,
consider the following scenario.
1. adv 1 wants to modify the output by itself, and dynamically bids on it.
2. adv 2 does not want to modify the output by itself, but wants to dynamically bid.
3. adv 3 does not want to modify the output by itself, and wants to bid in a static manner.
If one conceptually separates the steps (i), (ii) and (iii) between the advertisers, we can adapt all of
these advertisers by running a separate procedure for each advertiser, and then finally runs the step
(iv).
Displaying multiple ads simultaneously. We may want to make it clear in the intro that the
paper focuses on displaying a single ad, and that multiple ads bring their own challenges discussed
briefly at the end. One common feature in the modern sponsored search auction is that, it usually
display multiple ads upon a single query, which is mostly to maximize the search engine’s revenue.
Given the architecture we proposed, it is not straightforward to allow this feature, so we here discuss
several approaches to deal with it.
First, consider a simple case in which all advertisers use LLMA modification and static bidding
model. In this case, one can consider every combination of advertisements as a subset of [ n], and
then generate modified output with corresponding bid. Further, if there is an advertiser with dynamic
bidding, LLMA can simply delegate the bid generating process to that advertiser for every combination
that includes this advertiser’s ad.
Obviously, these approaches are not computationally feasible if one consider every possible com-
binations of the subset. Therefore, the technical challenge lies in how one can optimally decide a
subcollection of the entire power set to balance the trade-off between computational burden with cor-
responding latency and revenue of the auction.
D Dynamic Creative Optimization via LLM
Now, we discuss about the possibility of advanced dynamic creative optimization by using LLM. Dy-
namic creative optimization (DCO) 15, in the traditional search and display ad markets, refers to the
technique of dynamically adjusting the combination of ad assets and constructing an advertisement
that best fits the customer’s preference. It can markedly enhance the quality and relevance of the ad to
the user by tailoring the contents of ad in a personalized manner. Many online advertisement platforms
15This is often called as dynamic product ads (DPA), but DPA typically refers to the process of selecting which item
to advertise from a given catalog of an advertiser, whereas DCO denotes the process of modifying the ad itself.
19

Q: Car recommendation, Ad: BMW 3 Series Q: Conference in Florida, Ad: Travel with SunShine
not personalized user: 60-year-old woman user: 60-year-old man user: 20-year-old
unmarried living in DC
user: 40-year-old married
living in California
not personalized
Figure 5: Integrating responsive advertisement in the images generated by ChatGPT 4. In the
left panel , a user requests car recommendations within the price range of $40,000 to $60,000, and
the chat bot, when capable of advertising, generates a “BMW 3 Series” image (left). Personalized ads
modify this image for a 60-year-old woman (middle) or man (right) based on user context like age and
gender. Note that it includes an image of woman for man in the output, and vice versa. In the right
panel, a user seeks machine learning conferences in Florida. The chat bot advertises “SunShine Travel”
with its logo on a generic Florida image (left). With personalized ads, the model tailors promotions,
offering flight tickets from the user’s location and showing more relevant Florida images. For example,
for a young unmarried person from DC, the output advertises DC to Florida flights (middle) and
features an image of beach there, while for a married person in California, it promotes California to
Florida flights with images of amusement parks. This enhances user experience with targeted and
appealing content.
adopt DCO-based ads, which is often called asresponsive ad (GoogleDisplayAd, 2024; GoogleSearchAd,
2024). 16
In the canonical DCO framework, a static ad consists of a single image file that can only be displayed
in a specific set of ad channels, whereas dynamically optimized ad consists of a single ad template and
multiple options for each asset that fills in the ad template. This is typically done by the advertiser
registering multiple options for each asset given an ad template, and then the system picks the optimal
combination. This procedure aims at increasing the CTR and SR, which would eventually improve the
welfare efficiency of the online ad ecosystem (McMahan et al., 2013) as well as the revenue of the ad
platform.
Unlike from the traditional DCO techniques, the arise of LLM, especially those support the output
with image such as ChatGPT 4, enables more involved process of dynamic creation of ads, as well
as replaces the role of traditional DCO in online ad platforms. For example, given a user query and
context, the platform may send a query to LLM to customize the image of ad to attract the user
by capturing user preference. We provide representative examples in Figure 5 where two scenarios of
personalizing ads is depicted. Note that the use of LLM-based DCO is not restricted to LLMA, but
can be broadly applied to SA and display ad.
Challenge: Refining each module. To integrate responsive ads, a more advanced modification
module is imperative. This module should not only enable the alteration of the original response to
include ads but also incorporate them in a manner that takes into account user preferences. This entails
utilizing user contexts, e.g., gender/location/the current device used for the query, in the ad generation
process. To be more specific, the modification module should incorporate user context in the process
of modifying the original response. This makes ads more appealing to the user by considering their
16As traditional DCO is restricted to dynamically construct the complete image file of ad, we here restrict our attention
to the image-based ads as well. However, it is apparent that LLM based DCO would work beyond image-based ads.
20

preferences. Leveraging language models, we can prompt them to factor in various elements related to
user context during the generation of modified outputs. As illustrated in Figure 5, information about
users’ context can be utilized to create more captivating advertisements for them.
Further, the prediction module may interact with the modification module to commit to the modified
output that mostly increases user’s experience, i.e., CTR and SR. Even for SA, the prediction module
may need to be made more sophisticated to predict the CTR and SR of the responsive ads. This is in
stark contrast to the standard DCO since it may not significantly change the ad image overall, but only
slightly changes the part of it by replacing some ad assets. Correspondingly, the advertiser may value
the generated ad differently, i.e., write different bid, with respect to the quality of the ad generated by
LLM-based DCO. Overall, a vast amount of studies should be done to clearly investigate a plausible
framework for LLMA, even for SA, to adapt the LLM-based DCO.
Challenge: Meeting system requirements. Obviously, running LLM-based DCO should not entail
the failure of the system requirements discussed in Section 4. For instance, in terms of latency, we
observed that generating an image with the GPT4 takes almost about 10s for Figure 5. Given that
the online advertising typically requires the ad latency up to 100ms, the required latency is almost
100 times the conventional threshold. Thus, the fundamental research challenge is to enable a fast
production of an ad image to meet the conventional latency requirement in the online advertising
system. Further, it will be technically interesting to balance the tradeoff between the ad’s quality and
latency which governs the advertiser and user utility, respectively.
Interestingly, as acute readers may have noticed, Figure 5 includes some technical issues in the
images themselves. For example, the first image in the car ads generate a word that is not easily
understandable. Indeed, LLM-based DCO may induce the reliability issue due to the hallucinating
nature of LLM (Ji et al., 2023; Guerreiro et al., 2023; Bubeck et al., 2023). 17 Thus, LLM-based DCO
should ensure that it does not generate a hallucinated ad that may hurt the advertiser satisfaction.
A simple approach might be to require LLM to minimally revise the reference images, requesting the
advertisers to submit several images for reference.
Challenge: Cost sharing model. Unlike from the traditional DCO technique that simply determines
the efficient combination of ad assets, LLM-based responsive ad can do much beyond by creating
truly new content. On the other hand, such process necessarily entails increased use of computational
resource, especially since more queries to LLM will be required to customize the ads. We here discuss
several plausible cost sharing models that LLMA might adopt.
The simplest one will be to charge the advertisers whenever the contents are dynamically modified.
For example, the advertiser and LLMA commit to a mutual contract on how much the advertiser pay
the LLMA for each responsive ad, and LLMA charges the advertiser whenever it responsively modifies
the ad contents. As the advertiser might hope to use responsive ad only if the user context is sufficiently
relevant to its ads, the contract might specify when the advertiser’s ads will be responsively changed.
Also, LLMA may provide several options for advertiser to determine how frequently and largely it
should responsively modify the ads.
This model would work well for those charged by cost-per-impression, however, advertisers with cost-
per-click or cost-per-conversion may not willingly commit to the contract since they desire to pay the
platform only if the actual click or conversion happen, even though the platform indeed responsively
modified its ads for every impression. LLMA might give several options to the advertisers under which
event they will be charged to pay for responsive ad. Ads with cost-per-click model may still want to
pay for responsive ads per impression or per click. For the latter, LLMA may offer a larger amount of
17One might view this as a simply inability of a model tailored to the text-to-image generation. We refer to Daras and
Dimakis (2022) for a discussion on it.
21

commission per click by predicting the average CTR of the ads.
LLMA must also decide whether or not to account the increased amount of payment for each adver-
tiser as the increment of the actual bid or just regard it as a separate commission. For the former case,
the advertisers who are willing to charge more for the responsive ad commission fee will take advantage
of getting higher chance of delivering their ads, compared to those who do not use responsive ad option.
By doing so, the auction module can select the ad that truly maximize the total revenue expected from
delivering a single advertisement, thereby increasing the platform’s revenue.
22
