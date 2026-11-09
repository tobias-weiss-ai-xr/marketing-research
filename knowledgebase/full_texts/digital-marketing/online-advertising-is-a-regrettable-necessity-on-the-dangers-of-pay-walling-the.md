---
title: 'Online Advertising is a Regrettable Necessity: On the Dangers of Pay-Walling the Web'
url: https://arxiv.org/abs/2409.00026
category: digital-marketing
subcategory: empirical
date: 2024-08
venue: ''
authors:
- Yonas Kassa
source: arxiv
pdf_url: https://arxiv.org/pdf/2409.00026
pages: 7
chars: 29080
fetched_at: '2026-11-08T13:17:57+00:00'
kb_version: 1
---

# Online Advertising is a Regrettable Necessity: On the Dangers of Pay-Walling the Web

Online Advertising is a Regrettable Necessity: On the
Dangers of Pay-Walling the Web
Yonas Kassa
ykassa@acm.org
ABSTRACT
The exponential growth of the web and its benefits can be
attributed largely to its open model where anyone with in-
ternet connection can access information on the web for free.
This has created unprecedented opportunities for various
members of society including the most vulnerable, as rec-
ognized by organizations such as the UN. This again can be
attributed to online advertising, which has been the main
financier to the open web. However, recent trends of pay-
walling information and services on the web are creating
imminent dangers to such open model of the web, inhibit-
ing access for the economically vulnerable, and eventually
creating digital segregation. In this paper, we argue that
this emerging model lacks sustainability, exacerbates digi-
tal divide, and might lead to collapse of online advertising.
We revisit the ad-supported open web business model and
demonstrate how global users actually pay for the ads they
see. Using data on GNI (gross national income) per capita
and average paywall access costs, we established a simple
income-paywall expenditure gap baseline. With this baseline
we show that 135 countries with a total population estimate
of 6.56 billion people cannot afford a scenario of a fully pay-
walled web. We further discuss how a mixed model of the
so-called “premium services” creates digital segregation and
poses danger to online advertising ecosystem. Finally, we
call for further research and policy initiatives to keep the
web open and more inclusive with a sustainable business
model.
1 INTRODUCTION
The advent of the World Wide Web has revolutionized the
way we access and share information, leading to an enor-
mous amount of accessible knowledge and opportunities for
individuals and societies globally. The open model of the
web which allows anyone with an internet connection to
access and contribute information for free, has been instru-
mental in creating a global information ecosystem that has
benefited billions of users worldwide [6]. This open model
of the web has provided unprecedented opportunities for
the most vulnerable members of society, enabling them to
access educational resources, connect with communities, and
participate in the digital economy and social development
[9]. It is important to note that getting access and staying
connected to the internet by itself is an expensive challenge
for most parts of the world [27]. Recognizing this challenge
(also referred to as first level digital divide) various efforts
have been made by governments, industry, and research bod-
ies to bring internet connection widely accessible[36]. The
UN has identified ICT access as one of sustainable develop-
ment goals [9]. Researchers have also studied approaches
to address the second challenge, such as creating low-cost
ICT devices, creating innovative solutions to make internet
reachable to farthest places, and lowering the user cost of
web traffic and improving user experience with low-speed
internet[18]. Despite the many challenges such as high cost
of connecting to internet [27], online privacy [28] and secu-
rity issues [34], the ad-supported web has generally been free
(arguably) and open without requiring payment beforehand,
until recently.
The primary financier of this open web has been online
advertising [17]. As such, online advertising has enabled
content creators and service providers to monetize their
offerings and sustain their businesses, providing global in-
ternet users with a wealth of free information and online
services. However, as we will see in the rest of the paper,
recent trends towards paywalling information and services
on the web pose imminent dangers to this open model.
The multifaceted benefits of the open web is enormous
and the advantages it has been offering to the least privileged
has been unprecedented. Multiple reports have underlined
its transformative power such as its effect on bridging em-
ployment inequality [19], reducing the proportion of house-
holds(particularly women) below the poverty line [2], and
helping eradicate illiteracy [39].
The emergence of paywalling an information content or
part of it as a business model can be linked to several fac-
tors, including the high costs of producing and operating a
large-scale information content and service, and the ad-tech
shift towards highly targeted advertising and entailed user
technologies to circumvent it [ 26]. While these emerging
paywalls may seem to provide short-term financial gains for
content platforms and service providers, they exacerbate the
digital divide and lack sustainability as a business-model in
the long term.
In this paper, we raise concerns about the sustainability
and inclusivity of the emerging trend towards paywalled
content and services on the web. We highlight dangers of
this emerging challenge contending that a fully paywalled
1
arXiv:2409.00026v2  [cs.CY]  4 Sep 2024

Yonas Kassa
web is unsustainable and poses significant risks to entire
advertising-supported ecosystem. After covering some of
important related work in the area, we begin with revisiting
the ad-supported open web business model and demonstrate
how global users actually pay for the ads they see. Using
results from previous research [29] and the GNI per capita
data, we then discuss how cost of accessing a small portion
of content on internet is impractical for most part of the
world. Next, we discuss how a mixed model of premium
services creates digital segregation and poses a danger to the
online advertising ecosystem. With these points we aim to
shed light on how this emerging business model exacerbates
existing inequalities and creates new ones. Then, we proceed
to call for research and policy efforts towards creating ethical
and desirable advertising systems that can keep the web open
and more inclusive. Finally, we conclude the paper pointing
limitations of our work and suggesting potential directions
for future work.
2 RELATED WORK
While online advertising has been widely acknowledged
as backbone of the open web [ 14, 20] enabling free global
information dissemination, its modus operandi has always
been the subject of user dissatisfaction [8]. The dissatisfac-
tion primarily emerges from embedded adverts between user
interactions that degrade user experience [25, 40], and the
increasing incorporation of sophisticated tracking mecha-
nisms. Advertisers use tracking techniques to collect user
activity data with the aim of bringing most relevant ads to the
users [4, 5]. In relation to this, multiple open platforms serv-
ing billions of users have been a subject of several scrutiny
[24, 31]. A particular example is the Cambridge Analytica
case [15], that attempted to influence US presidential elec-
tion analysing user behavior, which was widely covered by
mainstream media resulting in global awareness on privacy.
Even though the Cambridge Analytica study was performed
on Facebook, it is worth to note that the method can the-
oretically be replicated to other social platforms such as X
(formerly Twitter) and TikTok. Privacy risks associated with
online advertising have been widely documented [ 16, 22].
The advertising monetary value of user data has also been
documented in multiple studies [23, 28]. While these studies
showed the risks and undesirable sides of online advertis-
ing and collecting user data, other results have shown how
proper handling of user data such as via anonymization
and aggregation can effectively be used for societal bene-
fit [13, 32, 33]. Furthermore, multiple works have proposed
to improve user interaction with online advertising with
approaches such as bringing transparency and improving
user privacy [10, 30], and ad profit sharing with users [ 7].
A few research works have explored impact of advertising
on ad-supported open web [ 4, 29, 35]. Varian [38] studied
interplay between advertising costs and product prices and
has shown that when advertisers cut back on ad spending,
they do not necessarily change product prices accordingly.
A paper by Shiller et al. [ 35] studied the compounded im-
pact of ad-blocking on revenue concluding that ad blocking
poses a substantial threat to the ad-supported web. A more
recent article of high relevance to our discussion is a paper
by Papadopoulos et al. [29] which studies prevalence of pay-
walls and discussed their impacts. Their findings show that
paywall use has been increasing, and the median cost of an
annual paywall access is 108 USD per site.
3 REVISITING AD-SUPPORTED
INTERNET
A well-known architectural presentation to discuss modern
day online advertising systems involves putting advertisers
and end users on the two extremes that are connected via
online advertising system as intermediary. In this popular
scenario the online advertising system composed of parties
like supply side platform, ad exchange, and demand side
platforms tracks user activities to gather data that can be
used during Realtime Bidding (RTB). When a user visits
ad-supported platform RTB takes place, where potential ad-
vertisers bid for ad-slot to be displayed as part of the content
presented to the end user [ 41]. To build the most optimal
matching between advertisers and ad-slots to each individual
user advertising system uses a variety of sophisticated tech-
niques that heavily make use of personal data [37]. Though
it is widely known that user personal data is a tradable com-
modity, the fact that end users actually pay for the ads they
see is often overlooked.
Online advertising is a multibillion-dollar business. This
multibillion-dollar budget comes from advertisers which are
producers of goods and services that aim to reach their po-
tential clients or customers. Companies spend a significant
portion of their revenue to advertising, the average ad spend-
ing budget of small businesses ranges between 4-6 percent of
their gross revenue, while ad spending by some companies
rises up to 20% [12].
Let’s take a scenario of company X getting its customers
exclusively via online advertising. If gross revenue of com-
pany X (i.e. total sum of products and services sold) is R, then
a portion of this revenue goes to online advertising Ca. Let
X’s target cost after advertising be Cps.
Then,
𝐶𝑝𝑠 =𝑅−𝐶𝑎 (1)
This gross revenue, R, is the sum of total cost (TC) paid
by X’s clients/customers.
𝑇𝐶 =𝐶𝑝𝑠+𝐶𝑎 (2)
2

Online Advertising is a Regrettable Necessity: On the Dangers of Pay-Walling the Web
Online Advertising System Simplified Diagram
Advertiser (producer)
Online advertising
system
Publisher/platform
User (consumer)
A B
CD
E
F
B’
C’
Figure 1: Diagram Revisiting ad-supported Web: First, advertiser assigns a total cost (TC) to a product/service
by adding the advertising dollar (Ca) to the initial cost of a product/service. When a user visits ad-supported
publisher/platform (arrow A), the platform contacts ad-system (arrow B), which in turn performs RTB (arrow B’)
that leads to winning advertiser sending back ads and a dollar amount (arrow C’). the advertising system then
sends the winning ad along with a fraction of the dollar amount to the ad-slot on the platform (arrow C). The ad is
presented to the user (arrow D). Up on conversion, user eventually pays the dollar amount for ad they saw (arrow
E) plus Cps, finally product/service is delivered to user (arrow F).
𝑇𝐶 =
∑︁
𝑖𝜖𝑖𝑡𝑒𝑚𝑠
∑︁
𝑗𝜖𝑢𝑠𝑒𝑟𝑠

𝐶𝑝𝑠(𝑖) (𝑗)+𝐶𝑎(𝑖) (𝑗)

(3)
With this second equation, we can say that the advertising
budget is practically paid by end users. We can diagram-
matically see this model on Figure 1. The diagram can be
summarized as follows: initally advertiser assigns a total
cost (TC) to a product/service by adding the advertising cost
(Ca) to the initial target cost of a product/service. The ad-
vertiser places this ad with advertising dollar Ca on RTB.
The advertiser then sends the winning ad through the pub-
lisher/platform paying a fraction of Ca to the platform. Up
on conversion, user eventually pays for ad they saw. This
visualization demonstrates that the advertising cycle can
sustainably continue as long as the system is healthy and
end users find products/services advertised to them relevant
and appealing. It also suggests us to postulate that end users
practically pay for the ads they are exposed to.
4 PAY-W ALLING THE INTERNET
EXACERBATES DIGITAL SEGREGATION
Given there are over a billion websites in the world today,
users are faced with multiple alternatives of varying degrees
of utility for their digital needs. This information overload
also exposes users to multiple challenges such as disinfor-
mation [21], and malware [34]. Services such as Google Ad-
Words and SimilarWeb provide categorization of websites
into interest groups such as books, music, business services,
adult, games, etc. SimilarWeb1 for instance provides 250 such
categories. It is challenging to analyze and categorize each
individual website to decide which platform can be used as
a replacement (representative) for other websites in its cate-
gory. For example, CNN and Fox News fall under news and
media category, but it is known that one cannot replace the
other [11]. An interesting example of website uniqueness is
the case when the Seattle times temporarily had to lift its
paywalls during the 2014 Oso mudslide recognizing that it
was the main platform covering the disaster on its website
[1].
However, for our discussion we will assume that a user
can satisfy their information needs with one website from
each category (i.e. user can live with only 250 websites).
According to results from Papadopoulos et al. [29], median
annual paywall access is 108 per site, this gives that in a fully
paywalled scenario a user will need to budget 27,000 USD (i.e.
108 USD*250) just to get past paywalled services. Taking the
GNI (Gross national income) per capita, GNIpc, of countries
1https://support.similarweb.com/hc/en-us/articles/213856729-Top-
Websites
3

Yonas Kassa
150
 100
 50
 0 50 100 150
50
0
50
Income - Paywall Expenditure Gap
Negative
Positive
Figure 2: IPEG, income paywall expenditure gap (blue indicates IPEG value > 0, dark red indicates IPEG <0)
demonstrating majority of countries having negative IPEG value indicating that paywall budget cost is already
higher than the average before tax income of a country’s citizens.
from world bank, we can estimate a baseline income-paywall
expenditure gap, IPEG, for users per country.
𝐼𝑃𝐸𝐺 =𝐺𝑁𝐼𝑝𝑐 −𝑃𝑊𝐴𝐶 (4)
For paywall business model to be sustainable, the IPEG has
to be positive ( bare minimum). On Figure 2, we show that
IPEG is negative on 135 countries (amounting to 6.56 billion
people). Note that some of those countries don’t even have
online payment system even if a few of users can afford to pay
for the paywalls. Also, it is important to remember that even
in those countries with blue IPEG, a significant portion of
the population will have difficulty allocating paywall budget.
Now let’s discuss the hybrid model which is spearheaded
by large platforms such as YouTube, Twitter (X), and Tik-
Tok 2. Data on of some of the most popular platforms and
their premium fees is presented on appendix A. One of the
main incentives to go premium on such platforms is ad-free
experience or a service with fewer ads. Hybrid model gives
rich people option to avoid watching ads, get higher quality
information and experience. However, as we saw previously,
targeted advertising via RTB works by finding potential cus-
tomers for each advertiser. If certain groups of advertisers
can’t find their target users they will avoid investing in online
advertising (e.g. advertisers of cars, luxury watches, villas,
high end phones will pull their advertising budget for lack of
reaching potential customer) and hence reducing the market
capitalization of total advertising ecosystem. In other words,
if we rearrange equation 3 based on income, rich and affluent
2https://techcrunch.com/2023/02/27/social-media-apps-adopting-
subscription-models/
groups will disappear from equation 5.
𝑇𝐶 =(𝐶𝑝𝑠+𝐶𝑎)𝑟𝑖𝑐ℎ+(𝐶𝑝𝑠+𝐶𝑎)𝑎𝑓𝑓𝑙𝑢𝑒𝑛𝑡 +(𝐶𝑝𝑠+𝐶𝑎)𝑝𝑜𝑜𝑟 (5)
Note that advertisers pulling from platforms has immediate
effect with potential to kill the company (advertisers vs X
(formerly Twitter), for example3). Reduced advertising econ-
omy will discourage content generators and online service
providers from serving the poor, specifically people in least
developed regions will be at a high risk. On the other hand,
economically vulnerable people in developed regions will be
unable to access paywalled content and hence will be digi-
tally segregated getting less quality digital content, making
them less informed, and less competent in general.
5 CONCLUSION
5.1 We Need More Desirable and Ethical ads
So far we have discussed the important role ads play in
keeping the web open, and the impracticality of the emerging
premium-paywall business models. We have also raised some
of the concerns that make advertising undesirable part of the
web. However, there is not alternative business model that
is viable and as scalable as online advertising that can drive
an open and inclusive global scale information exchange. If
we address its undesirable issues, Online advertising can be
the most viable information super-highway that connects
producers with consumers, or act as a mechanism to deliver
timely information to the masses as it was proven during
COVID-19 pandemic [3]. Our position is that with enough
3https://time.com/6340905/elon-musk-advertiser-boycott-x/
4

Online Advertising is a Regrettable Necessity: On the Dangers of Pay-Walling the Web
research and strong policy, there is a possibility to device an
advertising framework that balances the needs of different
stakeholders while ensuring the sustainability and inclusivity
of the web. Rather than shifting towards paywalled services,
our focus should be on fixing and refining this incumbent
infrastructure to make advertising a desirable feature of the
web.
6 LIMITATIONS AND FUTURE WORK
While we cover several aspects of this emerging issue in
this short paper, our approach has several limitations. First,
in our IPEG calculation we didn’t take into account other
expenses which made our baseline highly generous. Second,
we relied on SemanticWeb categorization, a more detailed
and sophisticated content and traffic analysis could result
in a more accurate number of representative websites. Fi-
nally, we have not included the possible solutions to improve
online advertising. Future work could capitalize on these
limitations.
7 ACKNOWLEDGMENTS
Author(s) would thank reviewers for their valuable review
and insightful comments.
REFERENCES
[1] Mike Ananny and Leila Bighash. 2016. Why drop a paywall? Mapping
industry accounts of online news decommodification. International
Journal of Communication 10, 0 (2016), 3359–3380.
[2] Kalvin Bahia, Pau Castells, Genaro Cruz, Takaaki Masaki, Xavier Pe-
drós, Tobias Pfutze, Carlos Rodríguez-Castelán, and Hernan Winkler.
2024. The welfare effects of mobile broadband internet: Evidence from
Nigeria. Journal of Development Economics 170 (2024), 103314.
[3] Emily Breza, Fatima Cody Stanford, Marcella Alsan, Burak Alsan,
Abhijit Banerjee, Arun G Chandrasekhar, Sarah Eichmeyer, Traci
Glushko, Paul Goldsmith-Pinkham, Kelly Holland, et al. 2021. Effects
of a large-scale social media advertising campaign on holiday travel
and COVID-19 infections: a cluster randomized controlled trial.Nature
medicine 27, 9 (2021), 1622–1628.
[4] Ceren Budak, Sharad Goel, Justin Rao, and Georgios Zervas. 2016.
Understanding emerging threats to online advertising. In Proceedings
of the 2016 ACM Conference on Economics and Computation . ACM,
USA, 561–578.
[5] Claude Castelluccia, Lukasz Olejnik, and Tran Minh-Dung. 2014. Sell-
ing off privacy at auction. In Network and Distributed System Security
Symposium (NDSS). NDSS, USA, 16.
[6] Moumena Chaqfeh, Rohail Asim, Bedoor AlShebli, Muhammad Fareed
Zaffar, Talal Rahwan, and Yasir Zaki. 2023. Towards a world wide
web without digital inequality. Proceedings of the National Academy
of Sciences 120, 3 (2023), e2212649120.
[7] Yiling Chen, Arpita Ghosh, Randolph Preston McAfee, and David
Pennock. 2008. Sharing online advertising revenue with consumers.
In International workshop on internet and network economics . Springer,
USA, 556–565.
[8] Mark Yep-Kui Chua, George OM Yee, Yuan Xiang Gu, and Chung-
Horng Lung. 2020. Threats to online advertising and countermeasures:
A technical survey. Digital Threats: Research and Practice 1, 2 (2020),
1–27.
[9] Mauricia Abdol Tshilunda et al. 2022. Towards a New Social Contract
: reducing inequalities through digital public goods and youth collab-
oration for the Sustainable Development Goals (SDGs). UN digital
library 1, 1 (2022), 15 p. http://digitallibrary.un.org/record/4014948
[10] Casey Fiesler and Blake Hallinan. 2018. " We Are the Product" Public
Reactions to Online Data Sharing and Privacy Controversies in the
Media. In Proceedings of the 2018 CHI conference on human factors in
computing systems. CHI, USA, 1–13.
[11] James Flamino, Alessandro Galeazzi, Stuart Feldman, Michael W Macy,
Brendan Cross, Zhenkun Zhou, Matteo Serafino, Alexandre Bovet,
Hernán A Makse, and Boleslaw K Szymanski. 2023. Political polariza-
tion of news media and influencers on Twitter in the 2016 and 2020 US
presidential elections. Nature Human Behaviour 7, 6 (2023), 904–916.
[12] Thomas Frenkiel. 2023. Digital marketing budget allocation in six
steps. https://funnel.io/blog/allocate-digital-marketing-budget
[13] David Garcia, Yonas Mitike Kassa, Angel Cuevas, Manuel Cebrian, Es-
teban Moro, Iyad Rahwan, and Ruben Cuevas. 2018. Analyzing gender
inequality through large-scale Facebook advertising data. Proceedings
of the National Academy of Sciences 115, 27 (2018), 6958–6963.
[14] John Glenday. 2020. One in four Brits don’t realise the internet is
funded by advertising. https://www.thedrum.com/news/2020/10/19/
one-four-brits-don-t-realise-the-internet-funded-advertising. [Ac-
cessed 04-04-2024].
[15] Felipe González, Yihan Yu, Andrea Figueroa, Claudia López, and Ce-
cilia Aragon. 2019. Global reactions to the cambridge analytica scandal:
A cross-language social media study. In Companion Proceedings of the
2019 world wide web conference . world wide web conference, USA,
799–806.
[16] José González-Cabañas, Ángel Cuevas, Rubén Cuevas, Juan López-
Fernández, and David García. 2021. Unique on Facebook: formulation
and evidence of (nano) targeting individual users with non-PII data.
In Proceedings of the 21st ACM Internet Measurement Conference . ACM,
USA, 464–479.
[17] Jeremy Greenwood, Yueyuan Ma, and Mehmet Yorukoglu. 2021. ‘You
will:’A macroeconomic analysis of digital advertising. Technical Report.
National Bureau of Economic Research.
[18] Rumaisa Habib, Sarah Tanveer, Aimen Inam, Haseeb Ahmed, Ayesha
Ali, Zartash Afzal Uzmi, Zafar Ayyub Qazi, and Ihsan Ayyub Qazi. 2023.
A Framework for Improving Web Affordability and Inclusiveness. In
Proceedings of the ACM SIGCOMM 2023 Conference . SIGCOMM, USA,
592–607.
[19] Jonas Hjort and Jonas Poulsen. 2019. The arrival of fast internet
and employment in Africa. American Economic Review 109, 3 (2019),
1032–1079.
[20] Yonas Mitike Kassa, Rubén Cuevas, and Ángel Cuevas. 2018. A large-
scale analysis of Facebook’s user-base and user engagement growth.
IEEE Access 6 (2018), 78881–78891.
[21] Srijan Kumar, Robert West, and Jure Leskovec. 2016. Disinformation
on the web: Impact, characteristics, and detection of wikipedia hoaxes.
In Proceedings of the 25th international conference on World Wide Web .
www, USA, 591–602.
[22] Pedro Giovanni Leon, Ashwini Rao, Florian Schaub, Abigail Marsh,
Lorrie Faith Cranor, and Norman Sadeh. 2015. Privacy and behavioral
advertising: Towards meeting users’ preferences. In Symposium on
usable privacy and security (SOUPS) . SOUPS, USA, 22–24.
[23] Miriam Marciel, Jose Gonzalez, Yonas Mitike Kassa, Roberto Gonzalez,
and Mohamed Ahmed. 2016. The value of online users: Empirical
evaluation of the price of personalized ads. In 2016 11th International
Conference on A vailability, Reliability and Security (ARES). IEEE, IEEE,
USA, 694–700.
5

Yonas Kassa
[24] Sandra C Matz, Ruth E Appel, and Michal Kosinski. 2020. Privacy in
the age of psychological targeting. Current opinion in psychology 31
(2020), 116–121.
[25] Ben Miroglio, David Zeber, Jofish Kaye, and Rebecca Weiss. 2018. The
effect of ad blocking on user engagement with the web. In Proceedings
of the 2018 world wide web conference . www, usa, 813–821.
[26] Rishab Nithyanand, Sheharbano Khattak, Mobin Javed, Narseo Vallina-
Rodriguez, Marjan Falahrastegar, Julia E Powles, Emiliano De Cristo-
faro, Hamed Haddadi, and Steven J Murdoch. 2016. Adblocking and
counter blocking: A slice of the arms race. In 6th USENIX Workshop
on Free and Open Communications on the Internet (FOCI 16) . USENIX,
USA, 12.
[27] Panagiotis Papadopoulos, Nicolas Kourtellis, and Evangelos P
Markatos. 2018. The cost of digital advertisement: Comparing user and
advertiser views. InProceedings of the 2018 World Wide Web Conference.
WWW, USA, 1479–1489.
[28] Panagiotis Papadopoulos, Nicolas Kourtellis, Pablo Rodriguez Ro-
driguez, and Nikolaos Laoutaris. 2017. If you are not paying for it,
you are the product: How much do advertisers pay to reach you?. In
Proceedings of the 2017 Internet Measurement Conference . IMC, USA,
142–156.
[29] Panagiotis Papadopoulos, Peter Snyder, Dimitrios Athanasakis, and
Benjamin Livshits. 2020. Keeping out the masses: Understanding the
popularity and implications of internet paywalls. In Proceedings of The
Web Conference 2020. The Web Conference, USA, 1433–1444.
[30] Javier Parra-Arnau, Jagdish Prasad Achara, and Claude Castelluccia.
2017. Myadchoices: Bringing transparency and control to online
advertising. ACM Transactions on the Web (TWEB) 11, 1 (2017), 1–47.
[31] Sanjay Patnaik and Robert E Litan. 2023. TikTok shows why social
media companies need more regulation. The Brookings Institution,
Policy Brief, May 1, 1 (2023), 1–1.
[32] Simone Piaggesi, Serena Giurgola, Márton Karsai, Yelena Mejova,
André Panisson, and Michele Tizzoni. 2022. Mapping urban socioeco-
nomic inequalities in developing countries through Facebook adver-
tising data. Frontiers in big Data 5 (2022), 1006352.
[33] Daniele Rama, Yelena Mejova, Michele Tizzoni, Kyriaki Kalimeri, and
Ingmar Weber. 2020. Facebook ads as a demographic tool to measure
the urban-rural divide. In Proceedings of The Web Conference 2020. The
Web Conference, USA, 327–338.
[34] Muhammad N Sakib and Chin-Tser Huang. 2015. Automated collection
and analysis of malware disseminated via online advertising. In 2015
IEEE Trustcom/BigDataSE/ISPA, Vol. 1. IEEE, IEEE, USA, 1411–1416.
[35] Ben Shiller, Joel Waldfogel, and Johnny Ryan. 2017. Will ad blocking
break the internet? Technical Report. National Bureau of Economic
Research.
[36] Siddharth Singh, Vedant Nanda, Rijurekha Sen, Satadal Sengupta, Pon-
nurangam Kumaraguru, and Krishna P Gummadi. 2017. Leveraging
facebook’s free basics engine for web service deployment in develop-
ing regions. In Proceedings of the Ninth International Conference on
Information and Communication Technologies and Development . ICTD,
USA, 1–11.
[37] Till Speicher, Muhammad Ali, Giridhari Venkatadri, Filipe Nunes
Ribeiro, George Arvanitakis, Fabrício Benevenuto, Krishna P Gum-
madi, Patrick Loiseau, and Alan Mislove. 2018. Potential for dis-
crimination in online targeted advertising. In Conference on fairness,
accountability and transparency. PMLR, PMLR, USA, 5–19.
[38] Hal Varian. 2022. Advertising Costs and Product Prices. The Journal
of Law and Economics 65, S2 (2022), S419–S431.
[39] Mark West and Chew Han Ei. 2014. Reading in the mobile era: A study
of mobile reading in developing countries . UNESCo, USA.
[40] Eric Zeng, Tadayoshi Kohno, and Franziska Roesner. 2021. What makes
a “bad” ad? user perceptions of problematic online advertising. In
Proceedings of the 2021 CHI Conference on Human Factors in Computing
Systems. CHI, USA, 1–24.
[41] Weinan Zhang, Shuai Yuan, and Jun Wang. 2014. Optimal real-time
bidding for display advertising. InProceedings of the 20th ACM SIGKDD
international conference on Knowledge discovery and data mining. ACM,
USA, 1077–1086.
6

Online Advertising is a Regrettable Necessity: On the Dangers of Pay-Walling the Web
A APPENDIX A: PREMIUM COSTS OF
SOME OF THE POPULAR PLATFORMS
Platform Monthly Annual Name
youtube.com 13.99 167.88 YouTube premium
instagram.com 11.99 143.88 verified
twitter.com 16 192.0 premium+
x videos.com 9.99 119.88 premium
tikTok.com 4.99 59.88 premium
reddit.com 5.99 71.88 premium
openai.com 20 240 plus
netflix.com 22.99 275.88 premium
office.com 6.99 83.88 personal
Zoom.us 13.33 159.96 pro
Total 126.26 1515.12
Table 1: Paywall costs of some of the popular websites
from top 50 websites based on similarweb.com. Note
that some of the platforms offer discounts when pur-
chased in bulk or if paid for the full year plan.
7
