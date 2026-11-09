---
title: Privacy-Preserving Personalized Recommender Systems
url: https://doi.org/10.1287/msom.2023.0271
category: consumer-behavior
subcategory: empirical
date: 2025-08
venue: Manufacturing & Service Operations Management
authors:
- Xingyu Fu
- Ningyuan Chen
- Pin Gao
source: openalex-oa
pdf_url: https://utoronto.scholaris.ca/bitstreams/95e18167-2f8c-4949-bbce-e15729e25e17/download
pages: 42
chars: 114693
fetched_at: '2026-11-08T17:06:23+00:00'
kb_version: 1
---

# Privacy-Preserving Personalized Recommender Systems

TSpace Research Repository    tspace.library.utoronto.ca

Privacy-Preserving Personalized
Recommender Systems
  Ningyuan Chen, Xingyu Fu, Pin Gao, Yang Li

Version Accepted Manuscript

Citation
(published version)
Chen, N., Fu, X., Gao, P., Li, Y. (2025) Privacy-Preserving Personalized
Recommender Systems. Manufacturing & Service Operations
Management 28(1):271-289.

Copyright / License Copyright © 2025, INFORMS
DOI https://doi.org/10.1287/msom.2023.0271
Publisher’s Statement This is an accepted manuscript of an article published by INFORMS in
Manufacturing & Service Operations Management:
https://doi.org/10.1287/msom.2023.0271

How to cite TSpace items

Always cite the published version, so the author(s) will receive recognition through services that track
citation counts, e.g. Scopus. If you need to cite the page number of the author manuscript from TSpace
because you cannot access the published version, then cite the TSpace version in addition to the published
version using the permanent URI (handle) found on the record page.

This article was made openly accessible by U of T Faculty.
Please tell us how this access benefits you. Your story matters.

Privacy-Preserving Personalized Recommender Systems
Xingyu Fu
School of Marketing, UNSW Business School, University of New South Wales, Sydney, NSW 2052, Australia,
xingyu.fu@unsw.edu.au
Ningyuan Chen
Rotman School of Management, University of Toronto, Toronto, Ontario, Canada, ningyuan.chen@utoronto.ca
Pin Gao
School of Data Science, The Chinese University of Hong Kong, Shenzhen 518172, China;
School of Management and Economics, The Chinese University of Hong Kong, Shenzhen 518172, China, gaopin@cuhk.edu.cn
Yang Li
Ivey Business School, Western University, London, Ontario, Canada, yangli@ivey.ca
Problem Definition: Personalized product recommendations are crucial for online platforms but pose
privacy risks. To address these concerns, we propose recommendation policies that adhere to differential
privacy constraints. Methodology/Results: We develop a theoretical model where the recommendation
policy selects products based on consumers’ preference rankings, learned from personal data. Unlike con-
ventional recommendation policies that primarily focus on prospering from meeting consumer satisfaction,
our approach applies differential privacy to mitigate the risk of exposing personal information to man-in-
the-middle attackers during the transmission of recommendations over communication networks, such as the
Internet. As a result, this policy accounts for the trade-off between personalization and privacy. Our analysis
shows the optimal policy is a coarse-grained threshold policy, where products are randomly recommended
with either high or low probability based on whether their preference rankings are above or below a certain
threshold. We further explore the comparative statics of this threshold in an asymptotic regime with a large
number of products, as is typical for online platforms. Moreover, we examine the economic implications of
privacy protection. When product prices are exogenous, privacy protection reduces consumer surplus due
to lower match values between consumers and recommended products. However, when retailers set prices
endogenously, the impact on consumer surplus is non-monotonic, reflecting a trade-off between recommen-
dation accuracy and price inflation. Managerial/Regulatory Implications: Our findings offer insights
for practitioners developing privacy-preserving personalized recommendation policies and provide regulators
with a deeper understanding of the economic consequences of privacy protection in recommender systems.
Key words : differential privacy, personalization, product recommendations, socially-responsible operations
1. Introduction
In the rapidly evolving digital economy, personalized recommendations have become the cornerstone
of modern marketing strategies. By leveraging each consumer’s vast amounts of data, including demo-
graphics, geolocation, social networks, and search/purchase histories, firms can gain valuable insights
into her/his preference. This enables them to generate recommendations tailored to each consumer’s
unique needs. By showcasing relevant products to the right audience, personalized recommendations
substantially reduce economic waste in traditional marketing campaigns. Consequently, such prac-
tices have become commonplace across various platforms. For instance, Amazon attributes 35% of
1

2 F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems
its product sales, Netflix credits 75% of its content views, and Meta (formerly Facebook) relies on
personalized recommendations for 98% of its revenue. 1 Figure 1 illustrates how social media like
Meta and WeChat, the leading social network in China, offer personalized recommendations.
(a) Meta 2
 (b) WeChat3
Figure 1 (Color online) Personalized product recommendations by social media platforms.
However, as the ancient Greek tragedian Sophocles noted “Nothing vast enters the life of mortals
without a curse. ” Personalized product recommendations, despite their advantages, pose significant
privacy risks. These risks typically center on direct access to consumers’ private data during person-
alized recommendations’ collection and processing stages. To address this, modern privacy-preserving
techniques like federated learning (see, e.g., Yang et al. 2019) allow data to be stored and processed
locally on users’ devices rather than being centrally collected. Major platforms like Google and Apple
have already implemented these approaches, enabling on-device personalization while minimizing
privacy risks. 4 Even if a data breach occurs, the fragmented and unstructured nature of locally
stored data — such as location history, social connections, and search queries — makes extracting
meaningful insights difficult and limits potential harm.
However, a critical vulnerability remains at the downstream recommendation stage. Unlike raw
data, recommendation outcomes distill consumer preferences into a compact yet highly revealing
form. These outcomes can be exposed in multiple scenarios: third-party retailers may partner with
the platform to collect them for conversion analysis (see Liu et al. 2021) to infer consumer interests;
malicious actors may intercept them over compromised Wi-Fi networks 5; and casual observers catch
glimpse of recommendations on some user’s screen. As these exposures accumulate over time, they
gradually reveal a consumer’s complete preference — transforming implicit personal choices into an
explicit, exploitable profile. Figure 2 illustrates the privacy concern of personalized recommendations.
This exposed preference ranking creates immediate opportunities for economic exploitation. Third
parties can impose precise price discrimination, charging consumers their maximum willingness-to-
pay for top-ranked products while strategically discounting lower-ranked alternatives to maintain an

F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems 3
Product RecommendationMachine  Learning
Intercept & Infer
Personal Raw Data
0
0.1
0.2
0.3
0.4
1 2 3 4
Product Preference
4≻2≻3≻1
!
Rec.
Figure 2 (Color online) The recommendation process and privacy risks. Raw data and learned preferences are
typically safe, but recommendations are susceptible to privacy breaches. The numbers refer to product indices.
illusion of choice. Even more concerning, these rankings may enable the inference of highly sensitive
personal attributes without explicit disclosure — revealing political affiliations from merchandise
selections, health conditions from supplement recommendations, financial status from luxury item
rankings, and religious beliefs from content preferences. This type of information leakage can facilitate
various criminal activities, such as discrimination, fraud, and harassment.
Beyond these immediate concerns, the granularity of preference rankings facilitates sophisticated
psychological profiling in the long run. By analyzing how consumers rank similar products with vary-
ing attributes — risk vs. reward, immediate vs. delayed benefits, functional vs. status-driven features
— third parties can infer decision-making traits such as risk aversion, temporal discounting tenden-
cies, and status consciousness. These inferred psychological profiles enable targeted manipulation:
fraudsters could craft deceptions that align with specific consumer values to increase credibility, while
marketers may fine-tune messaging to trigger emotional responses that influence purchases.
This vulnerability at the recommendation stage presents a distinct privacy challenge that persists
even when upstream data remains protected through techniques like federated learning. While raw
data may remain secure on local devices, exposed preference rankings at the point of recommendation
continue to leak substantial personal information. Protecting these rankings is, therefore, not merely
about preserving abstract privacy rights but about preventing concrete harms in an era of hyper-
personalized digital marketplaces.
Our study is motivated by the privacy concerns in personalized product recommendations. Specif-
ically, we focus on protecting the consumer’s preference ranking of products from being inferred from
recommendation outcomes when they are transmitted through communication networks. We aim to
address the following questions:
(1) How can we design a privacy-preserving personalized product recommendation policy that miti-
gates privacy risk in recommendations while still providing relevant recommendations?
(2) What are the economic implications of having privacy preservation in recommendations?

4 F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems
It is important to note that our focus is on protecting privacy during the communication of recom-
mendations between consumers and the online platform, rather than on the machine learning pro-
cess that identifies product preferences from personal data (see Figure 2). While privacy-preserving
machine learning has been widely studied, safeguarding privacy at the final recommendation stage,
an area that emphasizes the downstream operational perspective, is relatively new. We believe that
our framework can complement upstream privacy-preserving machine learning techniques, such as
federated learning, thereby enhancing overall privacy protection.
This paper seeks to explore these critical issues by analyzing a theoretical model involving three key
market participants: retailers, a representative consumer, and an online platform that facilitates the
flow of products from retailers to the consumer through personalized recommendations. The product
prices are set exogenously by retailers. The platform deploys an algorithm on the consumer’s device,
which has access to the consumer’s private data. This algorithm learns the consumer’s preference
ranking of products based on available data, typically in formats of binary comparisons and choices
in the retailing context (e.g., a customer choosing between brand 𝐴 and brand 𝐵 when both are
offered). Given the discrete nature of the data, the algorithm can estimate the ranking of alternatives
at best rather than the unobserved utility (see, e.g., Wauthier et al. 2013; Negahban et al. 2017).
Using this preference ranking, the algorithm generates personalized product recommendations aimed
at maximizing a weighted sum of retailers’ revenue and consumer surplus. Despite the benefits of
personalized recommendations, they pose significant privacy risks, as sensitive information may be
inferred from recommendation outcomes. To mitigate this concern, we draw on concepts from the
computer science literature ( Dwork et al. , 2014) and propose incorporating differential privacy (DP)
constraints into the recommendation policy. This approach could be implemented by external regula-
tors or by the platform itself to maintain consumer trust and protect its reputation. DP ensures that
recommendation policies applied to different consumers exhibit subtle variation, thereby preventing
attackers from inferring individual preferences based solely on the (leaked) recommended items.
It is worth mentioning that our analysis envisions a futuristic regulatory or self-regulatory frame-
work for privacy-preserving personalized product recommendations, rather than one currently in
place. Nevertheless, this framework aligns closely with ongoing industry developments and regulatory
trends, such as China’s “Internet Information Service Algorithmic Recommendation Management
Provisions”, which took effect on March 1, 2022. This regulation is the first globally to directly
regulate algorithmic product recommendations, with articles seven and eight requiring that recom-
mendation service providers design their algorithms in a socially responsible manner and conduct
regular audits to safeguard personal information. 6
The main methodological contribution of our paper is the characterization of the optimal person-
alized recommendation policy under differential privacy. In the differential privacy literature, the

F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems 5
input to the recommendation algorithm is usually continuous, and the common privacy-preserving
mechanism is to add Laplace-distributed noise to the input. However, in our model, the input is
the personalized preference ranking of products, which is not suitable for the Laplace mechanism
due to its discrete and combinatorial nature. Moreover, the space of (randomized) recommendation
policies is exponential in the number of products, presenting additional challenges. To address these
challenges, we identify an invariant property that the optimal privacy-preserving personalized recom-
mendation policy must satisfy. As a result, we show that a simple threshold policy is optimal under
differential privacy. The policy divides products into two classes based on a threshold derived from
the consumer’s preference ranking: one class is prioritized and recommended with a higher probabil-
ity than the other, while products within each class are recommended with equal probability. Our
policy is computationally efficient and easy to implement, providing a transparent and interpretable
recommendation scheme that subtly balances the trade-off between personalization and privacy.
Next, we investigate how the optimal recommendation policy adapts to changes in exogenous
parameters such as the privacy budget (i.e., how loose privacy constraints are), the weight given to
revenue in the platform’s objective, and the product price. To streamline our analysis, we use a fluid
approximation with a large number of products, which is relevant for many online platforms. We
find that the impact of the product price on the optimal recommendation threshold is non-monotonic :
as the price rises, the platform first expands and then shrinks the recommendation priority list.
The underlying reason is as follows. When the price rises, initially, retailer revenue accounts for
a larger portion of the platform’s objective. Hence, in order to increase the sale probability, the
platform incorporates more intermediate-valuation products into the priority list to suppress the
overall probability of recommending extremely ill-matched products. However, when the product
price is prohibitively high, only the most matched products can make the customer accept the
expensive deal. Consequently, in order to restore demand, the platform switches to shrink the priority
list to selectively recommend high-valuation products.
In addition, we also discuss the economic repercussions of implementing privacy-preserving person-
alized recommendations. Our analysis shows that when the price is exogenously specified, tightened
privacy constraints decrease consumer surplus by degrading the match values of recommended prod-
ucts. This suggests that pursuing privacy is not a free lunch. However, interestingly, we find that the
impact of privacy protection on consumer surplus can be non-monotonic when the retailer endoge-
nously optimizes the product price in response to changes in privacy requirements. The intuition is as
follows. With less privacy protection, the platform can recommend products in a more personalized
fashion, which benefits consumers. On the other hand, the retailer can also charge higher prices as a
result. The trade-off between recommendation accuracy and price inflation leads to this non-trivial
pattern, which suggests that a careful balance must be struck when considering the economic impact
of privacy preservation in recommender systems.

6 F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems
1.1. Related Literature
Privacy is a multidisciplinary concept that has been studied across various fields, including sociology
(Margulis, 2003), psychology ( Acquisti et al. , 2020), economics ( Posner, 1981; Acquisti et al. , 2016),
operations management ( Cohen, 2018; Lobel, 2021; Fainmesser et al. , 2023), marketing ( Goldfarb
et al. , 2020), and computer science ( Dwork et al. , 2014; Fioretto et al. , 2022).
Our study contributes to the active research area in operations management that focuses on the
design/impact of privacy-preserving personalized policies adopted by firms. For instance, several stud-
ies have investigated privacy-preserving personalized pricing. Chen, Simchi-Levi, and Wang (2022)
analyze a firm’s privacy-constrained pricing policy, where prices are adjusted dynamically subject
to the differential privacy criterion while attempting to learn the underlying demand model. They
assume a generalized linear model for the demand function and extend this framework to nonpara-
metric demand functions in Chen, Miao, and Wang (2023). In contrast, Lei, Miao, and Momot (2024)
consider an offline learning setting, where the firm has already collected data on historical consumers
and sets personalized prices for new customers while ensuring that new prices do not reveal too
much information about historical consumers. Other studies have focused on mechanism design with
privacy restrictions. For example, Fallah, Makhdoumi, Malekian, and Ozdaglar (2022) propose an
incentive mechanism to motivate data sharing and attempt to estimate a parameter with privacy
guarantees. We note that other notions of privacy requirements have also been studied, such as pre-
venting adversaries from gaining more information from queries ( Tsitsiklis et al. , 2021; Xu et al. ,
2021). The aforementioned studies primarily focus on continuous inputs (e.g., feature vectors) and
outputs (e.g., prices), and a typical privacy-preserving mechanism is to add Laplace-distributed noise
to inputs. In contrast, our model studies product recommendations based on consumers’ preference
rankings, which are inherently discrete and have a combinatorial nature. As a result, the optimal
algorithmic structure in our model, particularly the randomization approach, diverges significantly
from traditional methods. Our analysis indicates that a simple threshold policy is optimal in this con-
text. Furthermore, unlike these studies centered on regret analysis or estimation error, our approach
is more aligned with combinatorial optimization than with statistical analysis. We also acknowledge
the analytical challenges in deriving comparative statics of the optimal threshold in a finite products
setting, and we address this limitation through fluid approximation.
Our work builds upon the concept of differential privacy ( Dwork et al. , 2014), which is a widely
accepted standard for practitioners and regulators to impose privacy requirements. For example, it
has been adopted by the U.S. Census Bureau ( Abowd, 2018). This privacy notion has also been
applied to a wide range of existing business models and algorithms as an external constraint, including
network goods ( He and Mu , 2014), time-varying databases ( Zhang et al. , 2023), statistical learning
(Chaudhuri and Monteleoni , 2008), and neural networks ( Abadi et al. , 2016). Some studies have also

F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems 7
compared differential privacy with other privacy metrics, such as divergence privacy ( Makhdoumi and
Fawaz, 2013). The motivation of classical differential privacy literature often emphasizes scenarios
where an attacker pretends to be a regular consumer to infer other customers’ data. In contrast,
the 𝛼-DP we define, by privatizing the recommendation policy, is specifically designed to protect
a customer’s preference in cases where recommendation decisions applied to her/him are leaked.
Therefore, we extend the concept of differential privacy to a novel area of application, offering a
complementary perspective to the existing literature.
Our study is also related to the literature on consumer privacy protection in the digital era, which
has been studied in various fields, including operations management, marketing, and economics.
Researchers have developed various theoretical models to understand the economics of privacy. For
instance, Casadesus-Masanell and Hervas-Drane (2015) consider a vertical differentiation model and
illustrate that some firms offer free services in exchange for data (e.g., Google), while others charge
consumers for services and choose to protect privacy (e.g., Apple, Microsoft). Acemoglu, Makhdoumi,
Malekian, and Ozdaglar (2017) study the impact of individual privacy concerns on the formation of
social networks. Ke and Sudhir (2023); Xu, Wang, and Zhang (2025) analyze the welfare implications
of privacy laws, such as the EU’s General Data Protection Regulation (GDPR), in personal data-
driven markets and online retail supply chains, respectively. Hu, Momot, and Wang (2022) study a
service system where customers can disclose their personal information and they argue that giving
customers full control over their privacy might backfire. Fainmesser, Galeotti, and Momot (2023)
analyze how a firm’s revenue model shapes its data collection and protection strategy, and how
to eliminate social inefficiency via proper privacy regulation. Montes, Sand-Zantman, and Valletti
(2019); Valletti and Wu (2020); Laussel, Van Long, and Resende (2023); Li and Li (2023) investigate
analytical models in which consumers can erase/modify their online traces to conceal/manipulate
their sensitive data. Several empirical studies also investigate the real-world effects of privacy reg-
ulations. Goldfarb and Tucker (2011) show that an EU privacy law reduced the effectiveness of
online display advertising in Europe by roughly 65 percent. Johnson, Shriver, and Du (2020) find
that although customers express strong privacy concerns, only 0.23 percent of ads in the U.S. stem
from opted-out consumers. In other words, consumers’ weak revealed privacy-seeking actions are not
compatible with their strong stated privacy preferences, a phenomenon documented as the privacy
paradox ( Acquisti et al. , 2020). Our study contributes to the literature by analyzing the economic
costs and benefits associated with privacy protection mechanisms in personalized recommendations.
We confirm that pursuing privacy comes at a cost, as it leads to significant economic losses for mar-
ket participants due to the reduced recommendation accuracy. However, we also demonstrate that
the cost of not protecting privacy may be even higher, as the loss of privacy can harm consumers
monetarily by resulting in higher product prices.

8 F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems
Lastly, our study is related to the literature on choice models, product ranking, and recommenda-
tions. We assume that consumers have preference rankings of products, similar to the ranking-based
choice model ( Farias et al. , 2013). In our paper, the firm recommends a single personalized product
to individual customers based on their preference rankings. This is different from the classic product
ranking literature, which typically studies the firm’s decision to rank products for all customers in
a non-personalized way, assuming a position-aware choice model ( Gallego et al. , 2020; Gao et al. ,
2021; Chen et al. , 2021; Ferreira et al. , 2022; Derakhshan et al. , 2022). The exact optimal ranking
is often computationally intractable in the literature, while we are able to characterize the optimal
privacy-preserving personalized recommendation policy and provide a computational recipe.
1.2. Roadmap
The rest of our paper is organized as follows. Section 2 presents the conceptualization and formulation
of our model. In Section 3, we analyze the structure of the optimal recommendation policy with
differential privacy. We then study several extensions to enrich our analysis, including endogenous
pricing (Section 4), product heterogeneity (Section 5), and assortment recommendation (Section 6).
Finally, we conclude our paper in Section 7. All proofs are provided in the Online Supplement.
2. The Model
We analyze a marketplace consisting of three groups of participants: a cohort of retailers, a represen-
tative consumer, and an online platform, such as Meta or WeChat. The retailers offer 𝐾∈ N+ distinct
products, denoted by the set [𝐾] ≜{1,...,𝐾 }. The platform leverages its technological advantage to
facilitate the matching between products and the consumer through personalized recommendations.
The consumer demands at most one product, and her/his valuations for the 𝐾 products are repre-
sented by{𝑣𝑗}𝑗∈[𝐾], which are independently drawn from a distribution with a CDF 𝐹(·) and a PDF
𝑓(·). For simplicity, we assume that the distribution is supported on the unit interval [0, 1] and that
𝐹(·) is strictly increasing. The prices of the 𝐾 products are set at a uniform value of 𝑝∈ R+ exoge-
nously. This setup is motivated by two reasons: first, the 𝐾 products are symmetric from an ex-ante
perspective; and second, on many online platforms, third-party retailers, rather than the platform
itself, determine product prices. We will later relax these assumptions by incorporating endogenous
pricing (see Section 4) and heterogeneous products (see Section 5).
Consumer Data. As digital technologies become more prevalent and consumers utilize a wider
range of online services, their peripheral devices, such as mobile phones, smartwatches, and Amazon
Alexa, collect vast amounts of personal data. This data, which includes for instance, search and
purchase histories, location information, and voice recordings, is often referred to as the “new oil” of
the 21st century. Platforms can harness data analytics to extract information from this data, gaining

F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems 9
insights into consumers’ behaviors and preferences. In our study, we assume the online platform uses
a recommendation algorithm on the consumer’s edge device. The algorithm leverages the consumer’s
personal data to learn their preference ranking of the 𝐾 products. However, the data is not granular
enough to reveal the actual valuations {𝑣𝑗}𝑗∈[𝐾] of the consumer. This limitation is common among
online retail platforms, which typically collect data based on pairwise comparisons and discrete
choices, such as a customer’s choice between beer and wine when both are offered. Such data can, at
best, be used to infer the preference ranking rather than the unobserved utility (see, e.g., Wauthier
et al. 2013; Negahban et al. 2017). It is important to note that we do not explicitly model the learning
process (i.e., the process of inferring customer preference from data as shown in Figure 2) because
our focus is on the downstream operational decision (i.e., product recommendation), rather than the
upstream data science problem. In summary, prior to making a recommendation, the algorithm only
has access to ordinal information regarding consumer valuations, as opposed to cardinal information.
Formally, we define the consumer’s type as her/his preference ranking of the 𝐾 products. This
can be defined as a bijection 𝜋 :[𝐾]→[ 𝐾], where 𝑣𝜋(1)≥𝑣𝜋(2)≥···≥ 𝑣𝜋(𝐾). As such, there are 𝐾!
possible customer types, equal to the total number of permutations of the 𝐾 products. We use 𝜎(𝐾)
to denote the set of consumer types. Additionally, it is worth mentioning that, conditional on the
type 𝜋, the valuation of product 𝑗 is distributed as the 𝑖-th largest order statistic of 𝐾 i.i.d. random
samples from 𝐹(·), where 𝑖 = 𝜋−1(𝑗). We denote this conditional distribution as 𝐹𝜋,𝑗 , and a random
variable following 𝐹𝜋,𝑗 is denoted by 𝑉𝜋,𝑗 .
It is important to note that even though the algorithm has direct access to the customer type 𝜋
(see, e.g., Lei et al. 2024), the platform may not possess or remotely access the consumer’s data. We
envision that the entire process of data generation, storage, and preference learning occurs locally on
the user’s edge device. That is, our study is framed within the well-known federated learning frame-
work (see, e.g., Yang et al. 2019), an industry standard that not only benefits from low latency but
also ensures privacy by default. Major platforms like Google and Apple have already implemented
decentralized learning approaches like this to achieve on-device personalization while preserving pri-
vacy. The privacy-preservation mechanism we later examine protects each customer’s preference
ranking from being inferred at the recommendation stage, which remains vulnerable even when the
machine learning stage is well-safeguarded by the mentioned established protocols. Since customer
type encodes sensitive personal information, its exposure could lead to exploitation by malicious
actors. This risk makes our protection mechanism essential.
Product Recommendation. Based on the consumer’s type, the algorithm selects a single
product to recommend. From a public relations standpoint, recommending too many products can
irritate consumers. For instance, the frequency of product recommendations on WeChat Moments

10 F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems
is a significant concern. In response, WeChat has limited recommendations to one per eight-hour
period.7 Figure 1 also indicates that advertising a single product is a standard practice on social
media. In Section 6, we relax this assumption by allowing the recommendation of assortment. The
consumer decides to purchase the recommended product 𝑗 if and only if it provides a non-negative
payoff, i.e., 𝑣𝑗−𝑝≥ 0. In the case of a successful transaction, third-party retailers earn revenue 𝑝.
We assume that unrecommended products will not be purchased (see, e.g., Iyer et al. 2005; Ichihashi
2020) due to the consumer’s lack of awareness of the product or the high search costs.
Formally, the platform adopts a recommendation policy 𝑄 ≜{𝑄𝜋,𝑗}𝜋∈𝜎(𝐾);𝑗∈[𝐾], in which 𝑄𝜋,𝑗∈
[0, 1] denotes the probability that product 𝑗 is recommended to the type- 𝜋 consumer, and
∑
𝑗∈[𝐾]𝑄𝜋,𝑗 = 1 holds true for all type 𝜋. Note that the policy has 𝐾!·(𝐾− 1) parameters to optimize
because the constraint ∑ 𝑗∈[𝐾]𝑄𝜋,𝑗 = 1,∀𝜋∈ 𝜎(𝐾) eliminates one degree of freedom.
Privacy Preservation. As discussed in Section 1, personalized product recommendations pose
a significant risk to privacy. If these recommendations are exposed to external parties — such as
third-party retailers partnered with the platform, malicious browser plugins, or compromised WiFi
networks monitored by attackers — they can be easily exploited to reverse-engineer sensitive con-
sumer information. This is because recommendations serve as high-level, distilled summaries of per-
sonal data. For instance, attackers might infer a consumer’s family structure from children’s toy
recommendations or deduce religion/ethnicity from food/travel destination suggestions. This type of
information leakage can lead to unlawful activities such as fraud, blackmail, and harassment.
To address these concerns, we draw on the idea from the computer science literature ( Dwork et al. ,
2014) and impose 𝛼-differential privacy ( 𝛼-DP) constraints on the recommendation policy 𝑄.
Definition 1. The recommendation policy 𝑄 satisfies 𝛼-differential privacy ( 𝛼-DP) if it meets
following conditions:
𝑄𝜋,𝑗
𝑄ˆ𝜋,𝑗
≤ exp(𝛼), ∀𝜋,ˆ𝜋∈ 𝜎(𝐾); 𝑗∈[𝐾], (♣)
where 𝛼∈ R+ is the privacy budget.
Although inspired by differential privacy, the 𝛼-DP concept and its definition are distinct. These con-
straints are specifically designed to prevent attackers from inferring a consumer’s preference ranking
𝜋 through observed recommendation outcomes. The constraints may be enforced either by external
policymakers or voluntarily by the platform. In the latter case, consumer privacy concerns could
lead to reduced engagement with the platform’s services/products. Consequently, the platform has
strong incentives to protect customer data, not only to preserve short-term profitability but also to
maintain its long-term reputation, even in the absence of regulatory pressure.
The notion of 𝛼-DP essentially requires that the recommendation policies applied to different con-
sumers cannot vary significantly in the probabilistic sense, with lower values of 𝛼 corresponding to

F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems 11
stricter constraints and thus providing more privacy protection. This makes it difficult for attack-
ers to infer personal information based on the (leaked) recommendation decisions. For instance, in
the extreme case where 𝛼→ 0, the recommendation policy cannot be personalized; all customers,
regardless of types, would be offered product 𝑗 with the same probability.
Remark 1 (Downstream Protection). Our model addresses often-overlooked privacy risks
in downstream recommendation decisions, specifically the risk of exposing consumers’ preference
rankings. While techniques like federated learning and local differential privacy protect personal data
during machine learning, they primarily mitigate upstream risks. However, privacy vulnerabilities
persist downstream, specifically when recommendation decisions are communicated to consumers.
Unlike fragmented raw data, recommendations are high-level distillations of user preferences and
behaviors, making them more susceptible to breaches. To bridge this gap, we propose 𝛼-DP, which
targets the specific risks posed when recommendation decisions are exposed, either through systematic
breaches or opportunistic scenarios, such as third-party retailers sharing conversion data or malicious
actors intercepting public Wi-Fi. By shielding personalized recommendations from privacy breaches,
𝛼-DP complements upstream privacy-preserving techniques and enables full-stack protection.
Remark 2 (Departure from Classic Differential Privacy Applications). Note that
traditional differential privacy applications typically focus on protecting databases (see, e.g., Dwork
et al. 2014; Zhang et al. 2023). However, recent advances in the operations management community
have adapted differential privacy to broader applications, such as pricing (see, e.g., Chen et al. 2022;
Lei et al. 2024). The 𝛼-DP framework we define marks another departure from the classic uses of
differential privacy, aiming to protect high-level, interpretable outputs like product recommendations.
Remark 3 (Other Privacy Modeling Choices). Some other modeling choices can impose
privacy restrictions on the recommendation policy 𝑄, such as divergence privacy (e.g., Makhdoumi
and Fawaz 2013). However, these constraints involve logarithm operators, making the resulting opti-
mization problem non-linear. In contrast, differential privacy is not only more widely used but also
offers favorable analytical properties. Thus, we adopt differential privacy to motivate our constraints.
Platform’s Problem. As the organizer of a two-sided marketplace, the platform has a respon-
sibility to ensure the well-being of both retailers and consumers (see, e.g., Armstrong 2006). This
is because the platform typically earns a proportion of retailers’ sales as a direct cut, which is a
major source of revenue in this business model. Moreover, since the two-sided market exhibits a
cross-side externality, where retailers benefit when the platform can attract and retain customers, it
is important for the platform to also value consumer surplus to build a thriving business environment.
To be precise, we define Π𝜋,𝑗 ≜𝑝· P[𝑉𝜋,𝑗≥𝑝] and 𝑆𝜋,𝑗 ≜ E[(𝑉𝜋,𝑗−𝑝)+] as the expected retailer
revenue and consumer surplus, respectively, when recommending product 𝑗 to a customer of type

12 F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems
𝜋. Here, the operator (·)+ represents taking the positive part, i.e., max{·, 0}. The objective of the
platform is to maximize a convex combination of retailer revenue and customer surplus while adhering
to the imposed 𝛼-DP constraints (♣). Specifically, the platform aims to solve the following problem,
max
𝑄
∑
𝜋∈𝜎(𝐾)
∑
𝑗∈[𝐾]
𝑄𝜋,𝑗·
[
𝛾Π𝜋,𝑗+( 1− 𝛾)𝑆𝜋,𝑗
]
(▲)
subject to 𝑄𝜋,𝑗≥ 0, ∀𝜋∈ 𝜎(𝐾);𝑗∈[𝐾], ∑
𝑗∈[𝐾]
𝑄𝜋,𝑗 = 1, ∀𝜋∈ 𝜎(𝐾),
𝑄𝜋,𝑗
𝑄ˆ𝜋,𝑗
≤ exp(𝛼), ∀𝜋,ˆ𝜋∈ 𝜎(𝐾);𝑗.
Here, 𝛾∈[ 0, 1] represents the platform’s relative emphasis on retailers’ revenue, and we define 𝑂𝜋,𝑗 ≜
𝛾Π𝜋,𝑗+( 1− 𝛾)𝑆𝜋,𝑗 as the expected platform objective when recommending product 𝑗 to the type- 𝜋
consumer. Problem ( ▲) can be converted to linear programming and be solved efficiently, for instance,
by using the interior-point algorithm ( Karmarkar, 1984). In Section 3, our goal is to analyze the
structural properties of the optimal solution to problem ( ▲).
3. Optimal Policy
3.1. Structures
In this section, we will answer the main research question: how to develop a personalized product
recommendation policy that also preserves privacy? Specifically, we seek to identify the structural
properties of the solution to the constrained optimization problem ( ▲). However, addressing this
problem directly is a formidable challenge, given that there are 𝐾!·(𝐾− 1) decision variables and the
number of 𝛼-DP constraints is of order 𝒪(𝐾·(𝐾!)2). Therefore, we will first simplify problem ( ▲) by
leveraging the symmetric property of products. We introduce the first auxiliary result in Lemma 1.
Lemma 1. The expected retailer revenue, consumer surplus, and platform objective satisfy,
(1) For all 𝜋,ˆ𝜋∈ 𝜎(𝐾) and 𝑖∈[𝐾], we have Π𝜋,𝜋(𝑖) = Πˆ𝜋,ˆ𝜋(𝑖), 𝑆𝜋,𝜋(𝑖) =𝑆ˆ𝜋,ˆ𝜋(𝑖) and 𝑂𝜋,𝜋(𝑖) =𝑂ˆ𝜋,ˆ𝜋(𝑖).
(2) For all 𝜋∈ 𝜎(𝐾), Π𝜋,𝜋(𝑖), 𝑆𝜋,𝜋(𝑖) and 𝑂𝜋,𝜋(𝑖) decrease in 𝑖∈[𝐾].
The first part of Lemma 1 states that the ranking of the recommended product, rather than the
product itself, is sufficient for determining recommendation outcomes. This result is valid owing to
the symmetry of product candidates, which simplifies further analysis. The second part of the lemma
demonstrates that as we move down the consumer’s preference list, retailer revenue, consumer surplus,
and platform objective all decrease unambiguously. This finding is consistent with our intuition:
since the product price is fixed, recommending a less-preferred product lowers the likelihood of a
transaction and results in losses for all parties. With the aid of Lemma 1, we can establish the
following lemma, which significantly simplifies the original optimization problem.

F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems 13
Lemma 2. For any 𝛼-DP policy 𝐻, there exists another 𝛼-DP policy 𝑄 that achieves the same
expected objective as 𝐻. Moreover, 𝑄 possesses an invariant property, namely,
𝑄𝜋,𝜋(𝑖) =𝑄ˆ𝜋,ˆ𝜋(𝑖), ∀𝜋,ˆ𝜋∈ 𝜎(𝐾);𝑖∈[𝐾].
Lemma 2 suggests that, without loss of generality, we can focus on a specific category of recom-
mendation policies that possess an invariant property, where 𝑄𝜋,𝜋(𝑖) depends solely on the product
ranking 𝑖 and not on the consumer type 𝜋. In other words, we only need to optimize the probability
of recommending a customer’s 𝑖-th preferred product to her/himself. This result holds, again, due to
the symmetry of products. For the ease of exposition, we define 𝑄𝑖 ≜𝑄𝜋,𝜋(𝑖), Π𝑖 ≜ Π𝜋,𝜋(𝑖),𝑆𝑖 ≜𝑆𝜋,𝜋(𝑖),
and 𝑂𝑖 ≜𝑂𝜋,𝜋(𝑖). These definitions correspond to the probability, retailer revenue, consumer sur-
plus, and platform objective, respectively, for recommending a customer’s 𝑖-th preferred product.
Consequently, we can reformulate the original problem ( ▲) as follows,
max
𝑄
∑
𝑖∈[𝐾]
𝑄𝑖·𝑂𝑖 (▼)
subject to 𝑄𝑖≥ 0, ∀𝑖∈[𝐾], ∑
𝑖∈[𝐾]
𝑄𝑖 = 1,
𝑄𝑖
𝑄ˆ𝑖
≤ exp(𝛼), ∀𝑖,ˆ𝑖∈[𝐾].
In comparison with problem ( ▲), problem ( ▼) offers two significant advantages. Firstly, it reduces
the dimensionality of the platform’s policy space from 𝐾!·(𝐾− 1) to only (𝐾− 1). Secondly, it
reduces the number of 𝛼-DP constraints substantially. Instead of ensuring similar probabilities of
recommending the same product to different customer types, which requires 𝒪(𝐾·(𝐾!)2) constraints,
the problem is transformed to ensuring similar probabilities of recommending different products to a
single representative customer type, which needs only 𝒪(𝐾2) constraints. This simplification allows
us to characterize the structure of the optimal policy, as reported in Theorem 1.
Theorem 1 (Optimal Policy) . The optimal privacy-preserving personalized recommendation
policy under 𝛼-DP exhibits a threshold structure, given by,
𝑄𝑖(𝛼, 𝜅) =
{ exp(𝛼)
𝜅 exp(𝛼)+(𝐾−𝜅), 𝑖 ≤ 𝜅,
1
𝜅 exp(𝛼)+(𝐾−𝜅), 𝑖 > 𝜅, (⋆)
where 𝜅∈[𝐾] is a type-independent threshold on the consumer’s preference ranking.
In the absence of privacy concerns, the best strategy would be to recommend the product most
preferred by the customer, i.e., 𝜋(1), maximizing both the likelihood of purchase and the resulting
revenue/surplus. However, this approach reveals detailed customer preferences, posing a significant

14 F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems
privacy risk. To mitigate this risk, one extreme solution is to recommend products randomly, neglect-
ing types, ensuring that no information about customer preferences is revealed, e.g., 𝑄𝑖≡ 1/𝐾,∀𝑖∈
[𝐾]. While this protects privacy, it significantly reduces the likelihood that a customer will encounter
a preferred product, leading to diminished revenue/surplus. The optimal privacy-preserving personal-
ized recommendation scheme adopts a middle-ground solution and employs a coarse-grained threshold
policy (⋆), which is similar to the piece-wise policy in He and Mu (2014) and the interval mechanism
in Eilat et al. (2021). Instead of always recommending the top-ranked product, 𝛼-DP introduces
randomness to the recommendation outcomes. Specifically, the product space [𝐾] is divided into two
groups, and a product is randomly selected for recommendation. The first group comprises the top 𝜅
favorite products of the consumer, and the second group consists of the remaining (𝐾− 𝜅) products,
which are less preferred. Within each group, the recommendation probability for every product is
the same. However, the recommendation probability in the first group is systematically higher than
that in the second group, with the ratio exp(𝛼) > 1 dependent on the privacy budget. The threshold
structure strikes a balance between personalization and privacy protection. By grouping products
into two groups — “more favorable” and “less favorable” — the optimal policy enables personalized
recommendations while reducing granularity to limit the exposure of detailed preference rankings.
Policy ( ⋆) employs two key strategies to protect privacy. First, products in the “less favorable”
group are still recommended. This strategy prevents third parties from easily inferring the “more
favorable” products by analyzing a small number of recommendations. For example, if a customer
consistently ranks politically affiliated products highly, the policy introduces some irrelevant recom-
mendations rather than exclusively suggesting the most preferred option. This added randomness
obscures the consumer’s true preferences. However, to maintain revenue/surplus, the policy ensures
that less favorable products appear less frequently (recall that the ratio exp(𝛼) > 1).
Second, within each group, products are recommended with equal probability. This strategy pre-
vents observers from reconstructing an exact preference ranking, even if they intercept all recom-
mendations. Recall that our model accounts for 𝐾! distinct customer types. However, policy ( ⋆)
consolidates 𝐾! customer types into just 𝐶𝜅 𝐾 identity profiles, ensuring that each profile contains
𝜅!·(𝐾− 𝜅)! different customer types. As a result, any attempt to infer a consumer’s exact preference
ranking becomes highly uncertain, as multiple types share the same observable profile.
In summary, policy ( ⋆) is both interpretable and effective. By limiting the granularity of recom-
mendation decisions and merging multiple customer types into broader identity profiles, it conceals
individual preferences while preserving the benefits of personalized recommendations. This design
optimizes the trade-off between revenue/surplus optimization and privacy protection.
In practice, many companies have implemented product recommendation strategies similar to pol-
icy ( ⋆) to safeguard consumer privacy. For instance, Target, a prominent American department

F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems 15
store chain, once conducted detailed data analysis to predict customers’ pregnancy status and rec-
ommended maternity products like diapers and cribs to those identified as expectant mothers. While
this original approach effectively showed relevant items to the right audience, it also posed a privacy
risk: others could infer sensitive reproductive status based on the recommendations. A notable inci-
dent occurred when a father received product recommendations for baby clothes and cribs addressed
to his teenage daughter, leading him to accuse Target of encouraging her to get pregnant. Upon
investigation, he found that his daughter was indeed pregnant. This situation highlighted the pri-
vacy risks associated with highly personalized recommendations. In response to this public relations
crisis, Target modified its strategy by randomly including irrelevant products, like wine glasses or
lawnmowers, in its recommendations. 8 We also observe similar strategies in the content recommen-
dations. For instance, TikTok, a short-form video platform, has pledged that a certain percentage
of videos recommended by its secretive algorithm are intended to be “disruptive” and irrelevant to
users’ viewing histories. Consequently, it becomes more challenging to deduce one’s interests from
TikTok’s recommendation stream. 9
It is worth noting that, although our policy is designed to mitigate the risk of exposing personal
information during the (downstream) transmission of recommendations over networks, the optimal
policy suggests that it can also be applied during the (upstream) machine learning stage to conceal
customer preferences. As Theorem 1 shows, products are essentially categorized into “more favorable”
and “less favorable” groups. This categorization can be performed in the machine learning stage:
rather than establishing a full ranking of customer preferences, the platform can simply predict
whether a customer likes or dislikes a product. Based on this coarse-grained preference information,
the platform can make recommendations and address privacy concerns at the machine learning stage.
Before segueing into the next section, let us discuss the computational issue. Due to the threshold
structure, it is computationally efficient to determine the optimal policy; that is, the platform’s
objectives under policy ( ⋆) can be calculated for all threshold candidates 𝜅∈[𝐾], and then the one
that yields the highest objective value can be selected, denoted as 𝜅★. It is important to note that the
optimal threshold can be strictly greater than one. However, characterizing its analytical properties is
challenging because the valuation distribution 𝐹(·) lacks any particular structure and the underlying
optimization problem is discrete in nature. The following example illustrates this challenge.
Example 1. Consider the following parameters: 𝐾 = 5, exp(𝛼) = 10, 𝑝 = 1/2, and 𝛾 = 1/2. When
the valuation distribution is uniform, i.e., 𝐹(𝑥) =𝑥, we can check that 𝜅★ = 1. However, when 𝐹(𝑥) =
𝑥2, the optimal threshold becomes 𝜅★ = 2. This shows that the optimal threshold can vary depending
on the valuation distribution, highlighting the challenges in studying its analytical properties.
This example is non-trivial since raising 𝜅 above 1 results in the cannibalization of the most
matched product 𝜋(1), i.e., exp(𝛼) 𝜅 exp(𝛼)+(𝐾−𝜅) decreases in 𝜅. However, it is also important to note that

16 F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems
the aggregate probability of recommending products belonging to the less favored group (i.e., the last
𝐾− 𝜅 products), which is given by (𝐾−𝜅) 𝜅 exp(𝛼)+(𝐾−𝜅) , also decreases in 𝜅. Consequently, the platform may
be incentivized to raise 𝜅 to suppress the recommendation of extremely ill-matched products despite
the cannibalization of product 𝜋(1). We will delve further into the properties of 𝜅★ in Section 3.2.
3.2. Fluid Approximation: A Large Number of Products
Despite the appealing threshold structure of the optimal recommendation policy, further theoretical
analysis is not feasible due to the aforementioned difficulties. We hence employ the fluid approximation
of an infinite number of products, i.e., 𝐾→+∞ , to facilitate analytical derivation. This approximation
is relevant in practice since modern online platforms usually offer thousands, and sometimes millions,
of products. Studying fluid models is also a common simplification in the revenue management
literature (e.g., Gallego and Van Ryzin 1994).
To see why this simplifies the analysis, consider the cut-off 𝜅 in (⋆) satisfying 𝜅/𝐾→ constant as
𝐾 increases. The 𝜅-th largest valuation 𝑉𝜋,𝜋(𝜅) converges in probability to the (1− 𝜅/𝐾)-th quantile
of 𝐹(·), i.e., 𝑉𝜋,𝜋(𝜅)
P
→𝐹−1(1− 𝜅/𝐾) (see, e.g., Mosteller 1946). As a consequence, in this asymptotic
regime, there is an equivalence between the threshold on the preference ranking and a threshold
on the valuation. This observation allows us to conduct the following change of variable. Instead of
searching for the optimal ranking cut-off 𝜅★, now we switch to identify the optimal valuation cut-off
𝑧★ ≜𝐹−1(1− 𝜅★/𝐾); that is, products with valuations higher than 𝑧★ are recommended with larger
chance. We call the products pool with valuations higher than 𝑧★ as the priority list. Due to such
transformation, we can reformulate the platform’s optimization problem in a compact way so that
many handy tools, such as first-order conditions, can be utilized.
Specifically, let 𝑞(𝑥; 𝛼,𝑧) denote the probability density function of the valuation ˜𝑉 of the product
recommended by policy ( ⋆), where 𝑧 =𝐹−1(1− 𝜅/𝐾) is the valuation corresponding to ranking
cut-off. It is characterized in the following lemma.
Lemma 3. For all 𝛼 and 𝑧, 𝑞(𝑥; 𝛼,𝑧) is a piece-wise continuous function,
𝑞(𝑥; 𝛼,𝑧) =
{ exp(𝛼)𝑓(𝑥)
[1−𝐹(𝑧)] exp(𝛼)+𝐹(𝑧), 𝑥 ≥𝑧,
𝑓(𝑥)
[1−𝐹(𝑧)] exp(𝛼)+𝐹(𝑧), 𝑥 <𝑧.
As shown Lemma 3 (visualized in Figure 3), recommendation policy ( ⋆) leverages the consumer’s
personal data to suggest better-fitting products. This leads to a right-skewed distribution 𝑞(·), con-
trasting with the more balanced original distribution 𝑓(·). Despite this personalized approach, pol-
icy ( ⋆) is also privacy-preserving. Consequently, there remains a notable chance of recommending
products that may not be an ideal match, resulting in a left tail that is non-trivial for 𝑞(·).

F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems 17
0.3 0.6 0.9
0.5
1
1.5
2
2.5
𝑥
𝑞(𝑥)
𝑓(𝑥)
(a) 𝑎 = 1,𝑏 = 1
0.3 0.6 0.9
0.5
1
1.5
2
2.5
𝑥
𝑞(𝑥)
𝑓(𝑥)
(b) 𝑎 = 2,𝑏 = 2
0.3 0.6 0.9
0.5
1
1.5
2
2.5
3
𝑥
𝑞(𝑥)
𝑓(𝑥)
(c) 𝑎 = 1,𝑏 = 3
Figure 3 (Color online) PDF of the recommended product’s valuation. We set 𝛼 = 1.0, 𝜅/𝐾 = 0.1,
𝐹(𝑥) = Beta(𝑥;𝑎,𝑏).
By Lemma 3, we can express the retailer revenue and consumer surplus under policy ( ⋆) as
Π(𝑧) ≜𝑝· P˜𝑉∼𝑞[˜𝑉≥𝑝] =
{𝑝[exp(𝛼)(1−𝐹(𝑧))+𝐹(𝑧)−𝐹(𝑝)]
[1−𝐹(𝑧)] exp(𝛼)+𝐹(𝑧) , 𝑧 ≥𝑝,
𝑝 exp(𝛼)(1−𝐹(𝑝))
[1−𝐹(𝑧)] exp(𝛼)+𝐹(𝑧), 𝑧 <𝑝,
𝑆(𝑧) ≜ E˜𝑉∼𝑞[(˜𝑉−𝑝)+] =
 

exp(𝛼)
∫ 1
𝑧(𝑦−𝑝)𝑑𝐹(𝑦)+
∫ 𝑧
𝑝(𝑦−𝑝)𝑑𝐹(𝑦)
[1−𝐹(𝑧)] exp(𝛼)+𝐹(𝑧) , 𝑧 ≥𝑝,
exp(𝛼)
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦)
[1−𝐹(𝑧)] exp(𝛼)+𝐹(𝑧), 𝑧 <𝑝.
The platform’s design problem now involves choosing the optimal valuation cut-off 𝑧★ to maximize
a weighted summation of retailer revenue and consumer surplus, i.e.,
𝑧★∈ arg max
𝑧∈[0,1]
𝑂(𝑧),
where 𝑂(𝑧) ≜ 𝛾· Π(𝑧)+( 1− 𝛾)· 𝑆(𝑧). Lemma 4 guarantees the existence and uniqueness of 𝑧★.
Lemma 4. The function 𝑂(𝑧) is strictly quasi-concave in 𝑧 with a unique maximizer at 𝑧★≥𝑝.
With the aid of Lemma 4, we can now investigate the comparative statics of the optimal threshold
𝑧★ (equivalently, 𝜅★) concerning the exogenous parameters 𝛼, 𝛾, and 𝑝. Proposition 1 summarizes
our findings, which are illustrated in Figure 4.
Proposition 1. The comparative statics of 𝑧★ are given as below,
(1) Fix 𝛾,𝑝 and let ˆ𝛼 be the unique solution to 𝛾𝑝𝐹(𝑝) = exp(𝛼)(1− 𝛾)
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦), then,
(a) When 𝛼≤ˆ𝛼, we have 𝑧★ =𝑝.
(b) When 𝛼 >ˆ𝛼, we have 𝑧★ >𝑝 and 𝑧★ increases in 𝛼.
(2) Fix 𝛼,𝑝 and let ˆ𝛾 be the unique solution to 𝛾𝑝𝐹(𝑝) = exp(𝛼)(1− 𝛾)
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦), then,
(a) When 𝛾≤ˆ𝛾, we have 𝑧★ >𝑝 and 𝑧★ decreases in 𝛾.
(b) When 𝛾 >ˆ𝛾, we have 𝑧★ =𝑝.
(3) Fix 𝛼, 𝛾 and let ˆ𝑝 be the unique solution to 𝛾𝑝𝐹(𝑝) = exp(𝛼)(1− 𝛾)
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦), then,

18 F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems
0.2 0.4 0.6 0.8 1
0.2
0.4
0.6
0.8
1
𝑝
𝑧★
𝛾 = 1.0
𝛾 = 0.5
𝛾 = 0.0
(a) 𝐾 = 10
0.2 0.4 0.6 0.8 1
0.2
0.4
0.6
0.8
1
𝑝
𝑧★
𝛾 = 1.0
𝛾 = 0.5
𝛾 = 0.0
(b) 𝐾 = 100
Figure 4 (Color online) The optimal threshold 𝑧★ against other parameters. We set exp(𝛼) = 10 and 𝐹(𝑥) =𝑥.
(a) When 𝑝≤ˆ𝑝, we have 𝑧★ >𝑝 and
• If 𝛾 > 𝐹(𝑝) 2𝐹(𝑝)+𝑝𝑓(𝑝) , 𝑧★ decreases in 𝑝.
• If 𝛾 < 𝐹(𝑝) 2𝐹(𝑝)+𝑝𝑓(𝑝) , 𝑧★ increases in 𝑝.
(b) When 𝑝 >ˆ𝑝, 𝑧★ =𝑝 increases in 𝑝.
The first part of Proposition 1 shows that as the privacy budget 𝛼 increases, the recommendation
policy tends to shrink the size of the priority list; that is, 𝑧★ increases (or equivalently, 𝜅★ decreases).
In the extreme case where 𝛼 goes to infinity, the policy will recommend only the customer’s favorite
product, and the recommendation probabilities of all other products will drop to zero. This occurs
because a larger privacy budget allows the platform to recommend products that are better suited to
the customer’s preference. By shrinking the priority list, the platform can mitigate the cannibalization
effect, where the most relevant product loses sales to other less preferred products.
For the second part, Proposition 1 suggests that even under exactly the same privacy budget,
the platform will develop different recommendation strategies depending on whether it is retailer-
centric or customer-centric. Specifically, if the platform assigns more weight to the retailer revenue
Π, meaning that 𝛾 increases, it will expand the priority list. In other words, 𝑧★ will decrease (or
equivalently, 𝜅★ will increase). See Figure 4 for an illustration of this effect. To understand the logic
behind this result, we can start by recalling that retailer revenue is defined as Π = 𝑝· P[˜𝑉≥𝑝],
which depends on whether a transaction takes place at all. Once a transaction occurs, however, Π
does not depend on which specific product is purchased by the consumer. Therefore, the platform is
less concerned about the cannibalization of the favorite product and has the incentive to lower 𝑧★
(or raise 𝜅★) to include more intermediate-valuation products in the priority list. This suppresses

F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems 19
the overall probability of recommending extremely ill-matched products at the left-end tail of the
valuation distribution 𝐹(·), which can boost revenue. Conversely, when the platform values consumer
surplus 𝑆 more (i.e., 𝛾 gets smaller), it is optimal to narrow the priority list by raising 𝑧★ (or
lowering 𝜅★). This is because, unlike retailer revenue, the value of consumer surplus 𝑆 = E[(˜𝑉−
𝑝)+] does depend on which specific product is selected. Therefore, by cherry-picking the priority
list, the platform can prevent the most matched product from being cannibalized. To summarize,
revenue maximization requires restraining the recommendation of extremely low-valuation products
to boost aggregate demand, while surplus maximization requires restraining the recommendation
of intermediate-valuation products to prevent cannibalization. In mathematical terms, we can show
that arg max𝑧∈[0,1] Π(𝑧) < arg max𝑧∈[0,1]𝑆(𝑧), which is the key driver of this result.
The third part of Proposition 1 reveals that the impact of the product price on the optimal
design of the recommendation policy is more nuanced, as 𝑧★ can be non-monotonic in response to 𝑝.
Specifically,𝑧★ could first decrease and then increase as 𝑝 increases. The black solid curve in Figure 4b
demonstrates such a scenario. The underlying reason for this non-monotonicity is as follows. When
the product price 𝑝 rises, retailer revenue initially becomes a more significant part of the platform’s
objective. Therefore, the platform caters to retailers by lowering 𝑧★ (recall that arg max𝑧∈[0,1] Π(𝑧) <
arg max𝑧∈[0,1]𝑆(𝑧) holds). However, when the product price becomes prohibitively high, only the most
matched products can enable the consumer to accept the expensive deal. In this case, the platform
raises 𝑧★ to selectively recommend high-valuation products to restore demand.
Thus far, we have examined the structural properties of the optimal privacy-preserving personalized
recommendation policy and studied how exogenous parameters impact its design. Next, we will
investigate the welfare implications of privacy protection, which we summarize in Proposition 2.
Proposition 2. Letˆ𝛼 defined in the same way as Proposition 1, then we have the following: (1)
𝑂★ increases in 𝛼; (2) When 𝛾 = 1 or 𝛼 <ˆ𝛼, 𝑆★ is increasing in 𝛼.
For the first part, a platform with more relaxed privacy constraints (i.e., a larger 𝛼) has a less
restrictive design space, which certainly allows it to achieve a higher objective value. For the second
part, it is found that even in situations where the platform aims to maximize revenue (i.e., 𝛾 = 1),
the consumer can still experience economic benefits from weaker privacy protection. Furthermore,
when the privacy constraint is too stringent (i.e., 𝛼 <ˆ𝛼), the consumer may also be better off with
a less privacy-protective recommendation policy. The reason for this is that when privacy is not a
primary concern, the platform can use a more accurate personalized recommendation policy, leading
to the discovery of well-suited products that the consumer may have otherwise missed. Therefore,
pursuing privacy comes with an economic cost, and in some cases, consumers may benefit from a
recommendation policy that prioritizes accuracy over privacy.

20 F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems
This result is consistent with many real-world phenomena. For instance, Goldfarb and Tucker
(2011) empirically document that the EU privacy law “Privacy and Electronic Communications
Directive” reduced the effectiveness of online advertising by around 65% in Europe, imposing sig-
nificant costs on the European online advertising industry. Therefore, while there are many reasons
to preserve consumer privacy, policymakers and practitioners should conduct thorough benefit-cost
analyses before enacting any privacy-related regulations or protective protocols. From the consumers’
point of view, many studies have documented the so-called “privacy paradox” — a discrepancy
between consumers’ strong stated privacy concerns and their weak revealed privacy preferences (see,
e.g., Acquisti et al. 2020). For instance, only 0.23 percent of American ad impressions come from
privacy-conscious opted-out customers ( Johnson et al. , 2020). Our result provides an economic expla-
nation for this phenomenon: Consumers may derive significant economic gains from personalized
recommendations, which can outweigh the risks of privacy breaches.
However, as we will demonstrate in Section 4, privacy protection in recommendation policies is
not necessarily economically harmful to consumers. In fact, as we will show, consumer surplus may
decrease as 𝛼 increases if we incorporate endogenous pricing.
4. Endogenous Pricing
We will analyze the economic implications of incorporating 𝛼-DP protection in the recommendation
policy while taking into account the retailer’s endogenous pricing decision. To this end, we will study
a multi-product monopolistic retailer that can set a uniform price 𝑝∈ R+ for all products before
the platform determines its threshold policy. It is important to note that in this setup, the platform
acts as an intermediary marketing agency (such as Meta or WeChat) between the retailer and the
consumer, and is not involved in pricing. We have chosen to disallow the retailer to price discriminate
for two reasons. First, systematic price variation may lead to customer dissatisfaction and public
relations issues (see, e.g., Anderson and Simester 2010). Second, all products in this model are ex-ante
symmetric, i.e.,{𝑣𝑗}𝑗∈[𝐾] i.i.d.∼ 𝐹, and discriminatory pricing of “goods of like grade and quality” may
potentially violate the Federal Trade Commission’s anti-trust law, the “Robinson-Patman Act. ” 10
For analytical tractability, we consider the fluid approximation where 𝐾→+∞ (as described in
Section 3.2). We also assume a relative emphasis of 𝛾 = 1 on the retailer’s revenue, which is reasonable
given that the platform’s revenue is directly linked to Π. Additionally, we examine a specific functional
form of the valuation distribution, namely 𝐹(𝑥; 𝛽) ≜𝑥𝛽, where 𝛽 > 0 is the parameter that determines
the shape of the distribution. We will solve the equilibrium outcome using backward induction.
Given a price 𝑝, the platform optimizes the recommendation threshold to maximize its objective;
that is, 𝑧★(𝑝) = arg max𝑧∈[0,1]𝑂(𝑧). Since we assume 𝛾 = 1, then 𝑧★(𝑝) =𝑝 by Proposition 1(2b). In
other words, the platform recommends products more likely to result in transactions, while giving

F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems 21
5 10 15
0.4
0.6
0.8
1
𝛼
𝑝★
𝛽 = 2.0
𝛽 = 1.0
𝛽 = 0.1
(a) Product Price
5 10 15
5· 10−2
0.1
0.15
𝛼
𝑆★
𝛽 = 2.0
𝛽 = 1.0
𝛽 = 0.1
(b) Consumer Surplus
Figure 5 (Color online) The equilibrium price and consumer surplus under different privacy budgets.
lower priority to those with a reduced chance of success. Anticipating the platform’s recommendation
strategy, the retailer solves the following optimal pricing problem,
𝑝★ = arg max
𝑝∈[0,1]
𝑝· P[˜𝑉≥𝑝] = exp(𝛼)[1−𝐹(𝑝)]𝑝 exp(𝛼)[1−𝐹(𝑝)]+ 𝐹(𝑝).
Proposition 3 provides the equilibrium outcome, which is illustrated in Figure 5.
Proposition 3. Assuming𝐾→+∞ , 𝛾 = 1, and 𝐹(𝑥; 𝛽) =𝑥𝛽, where 𝛽 > 0, then we have
(1) The equilibrium recommendation threshold 𝑧★(𝛼) and price 𝑝★(𝛼) both increase in 𝛼.
(2) The equilibrium retailer revenue Π★(𝛼) increases in 𝛼.
(3) The equilibrium consumer surplus 𝑆★(𝛼) satisfies,
• When 𝛽 < 1, 𝑆★(𝛼) is quasi-concave with respect to 𝛼.
• When 𝛽≥ 1, 𝑆★(𝛼) is decreasing with respect to 𝛼.
The first part of Proposition 3 highlights the two distinct effects of privacy protection. As the pri-
vacy budget 𝛼 increases, on the one hand, the platform shortens its recommendation priority list to
provide more personalized and relevant recommendations, namely, 𝑧★(𝛼) increases (or equivalently,
𝜅★(𝛼) decreases). On the other hand, the retailer anticipates this improvement in recommendation
accuracy and sets a higher price to exploit it, i.e., 𝑝★(𝛼) increases (see Figure 5a). These two effects
work in the same direction for the retailer, leading to the monotonic pattern of Π★(𝛼), as demon-
strated in the second part of Proposition 3.
The third part of Proposition 3, however, demonstrates the two effects of privacy protection dis-
cussed earlier have opposite implications for the consumer. Specifically, as the privacy budget 𝛼

22 F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems
increases, the resulting more relevant product recommendations are beneficial for the consumer. Nev-
ertheless, the induced price inflation is clearly detrimental to the consumer. Therefore, the impact of
privacy protection on consumer surplus is ambiguous in the presence of the retailer’s endogenous pric-
ing decision, as it depends on the relative magnitude of these two mentioned effects (see, e.g., Bonatti
et al. 2023). For example, when 𝛽 = 0.1, the red dotted curve in Figure 5b exhibits a non-monotone
relationship with respect to 𝛼, which reflects the trade-off between the positive personalization effect
and the negative inflation effect. However, when 𝛽 takes on larger values such as 1 or 2, the black
and blue lines become decreasing in 𝛼, which is in stark contrast to Proposition 2 without pricing.
This is because as 𝛽 increases, the valuations of products become stochastically larger. Therefore,
the benefits of accurate recommendations to the consumer begin to wane, as the gap between the
first and other order statistics narrows. Consequently, the positive personalization effect dwindles,
and the negative inflation effect dominates, resulting in a downward pattern. It is noteworthy that,
all else being equal, larger 𝛽 (thereby more valuable products) can lead to a lower consumer surplus.
Again, this is due to the negative inflation effect.
Proposition 3 has significant practical implications for today’s digital economy. Despite claims by
some individuals that they no longer care about privacy and are willing to trade it for free online
services11, this proposition shows that such claims may be misguided. Consumers can be monetarily
exploited due to the loss of privacy, which induces price inflation (see, e.g., Eilat et al. 2021). Notably,
this conclusion holds even without price discrimination. Therefore, it is crucial to incorporate proper
privacy protection mechanisms into the design of personalized recommendation policies. This not
only ensures that consumers are not exploited but also respects their fundamental right to privacy.
5. Product Heterogeneity
In this section, we aim to demonstrate the robustness of our main result by incorporating product
heterogeneity into the base model. Specifically, we assume that customers’ valuations of the 𝐾 prod-
ucts are independently drawn from non-identical distributions, which are denoted by {𝐹𝑗}𝑗∈[𝐾]. The
price of each product, 𝑗∈[𝐾], is exogenously given by 𝑝𝑗.
Once again, the platform has access to the ranking 𝜋∈ 𝜎(𝐾) of the consumer’s valuations, where
𝑣𝜋(1)≥𝑣𝜋(2)≥···≥ 𝑣𝜋(𝐾). We denote 𝜌𝜋 ≜ P[𝜋] as the probability that the customer is of type 𝜋.
However, since we allow for heterogeneous distributions, {𝜌𝜋}𝜋∈𝜎(𝐾) does not necessarily follow a
uniform distribution over the type space, as was the case in our base model. The platform’s design
problem is formulated as follows,
max
𝑄
∑
𝜋∈𝜎(𝐾)
𝜌𝜋
∑
𝑗∈[𝐾]
𝑄𝜋,𝑗·𝑂𝜋,𝑗 (♦)
subject to 𝑄𝜋,𝑗≥ 0, ∀𝜋∈ 𝜎(𝐾);𝑗∈[𝐾],

F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems 23
∑
𝑗∈[𝐾]
𝑄𝜋,𝑗 = 1, ∀𝜋∈ 𝜎(𝐾),
𝑄𝜋,𝑗
𝑄ˆ𝜋,𝑗
≤ exp(𝛼), ∀𝜋,ˆ𝜋∈ 𝜎(𝐾);𝑗∈[𝐾].
In the following, we explore the structural properties of the optimal solution to problem ( ♦). We first
partition the product space [𝐾]. Specifically, we say products 𝑗1 and 𝑗2 belong to the same segment if
they share identical valuation distributions and are assigned the same prices, i.e., 𝐹𝑗1(·) =𝐹𝑗2(·) and
𝑝𝑗1 =𝑝𝑗2. This partition results in 𝐵 non-overlapping segments, with the total number of products in
each segment denoted by 𝐾𝑏 for 𝑏∈[𝐵]. It follows that ∑ 𝑏∈[𝐵]𝐾𝑏 =𝐾. To simplify the notation, we
defineℬ(𝑗) as the set of products that are in the same segment as product 𝑗∈[𝐾].
We now further partition the customer’s type space 𝜎(𝐾) to facilitate analysis. Let us define
customer types 𝜋1 and 𝜋2 as belonging to the same type segment if ℬ(𝜋1(𝑖)) =ℬ(𝜋2(𝑖)) holds for all
𝑖∈[𝐾]. In other words, the two customer types share identical valuation distributions and identical
prices for every position on their preference lists. We denote 𝒢(𝜋) as the set of customer types
that belong to the same segment as type 𝜋. We can establish the following facts: ( 𝑖) the number of
customer types in each segment is a constant value, namely ∏ 𝑏∈[𝐵]𝐾𝑏!; (𝑖𝑖 ) within each customer
segment, the probability of each type is identical; that is, 𝜌𝜋1 = 𝜌𝜋2 whenever𝒢(𝜋1) =𝒢(𝜋2).
With the help of these two definitions, we are now ready to establish some structural properties
of the optimal recommendation policy in the presence of product heterogeneity.
Lemma 5. For any given 𝛼-DP recommendation policy 𝐻, there exists another 𝛼-DP recom-
mendation policy 𝑄 that generates the same expected platform objective as the original policy 𝐻.
Additionally, if 𝒢(𝜋) =𝒢(ˆ𝜋), i.e., 𝜋 and ˆ𝜋 are in the same type segment, we have the following,
𝑄𝜋,𝜋(𝑖) =𝑄ˆ𝜋,ˆ𝜋(𝑖), ∀𝑖∈[𝐾].
Lemma 5 extends the results in Lemma 2 to heterogeneous products. It demonstrates that the
invariant property of the optimal recommendation policy remains valid for consumer types within
the same type segment. The following proposition provides further characterization of the optimal
policy in the presence of product heterogeneity.
Proposition 4. Under the optimal policy 𝑄, there exists{𝜃𝑗}𝑗∈[𝐾] and{𝑞𝜋,𝑗}𝜋∈𝜎(𝐾);𝑗∈[𝐾] such that
𝑄 can be decomposed as 𝑄𝜋,𝑗 = 𝜃𝑗·𝑞𝜋,𝑗 . Moreover, if we have 𝜃𝑗 > 0, then 𝑞𝜋,𝑗∈[ 1, exp(𝛼)] holds.
Furthermore, for each type 𝜋, there exists a type-dependent threshold 𝜅𝜋∈[𝐾] such that,
𝑞𝜋,𝑗 =
 

1, 𝑂𝜋,𝑗 <𝑂𝜋,𝜅𝜋,
∈[ 1, exp(𝛼)], 𝑂 𝜋,𝑗 =𝑂𝜋,𝜅𝜋,
exp(𝛼), 𝑂𝜋,𝑗 >𝑂𝜋,𝜅𝜋.

24 F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems
Proposition 4 generalizes the findings of Theorem 1 to heterogeneous products. Specifically, it
establishes that the optimal recommendation policy under product heterogeneity is a weighted thresh-
old policy. For each customer type 𝜋, the optimal policy includes a personalized factor 𝑞𝜋,𝑗 , which
reflects the trade-off between personalization and privacy. This factor captures the customer’s prod-
uct preferences in a coarse-grained manner through a threshold structure, where more favorable
products correspond to higher values of 𝑞𝜋,𝑗 . Moreover, the optimal policy applies a product-specific
weight 𝜃𝑗 to incorporate the impact of product heterogeneity in a non-personalized manner. Note
that the weight 𝜃𝑗 adjusts the recommended probability of product 𝑗 uniformly to customers of all
types. Unfortunately, it is analytically challenging to characterize the structural properties of 𝜃𝑗’s.
We thus use a numerical example to elaborate how and why 𝜃𝑗 may vary at optimality.
Example 2. Consider a setup with 𝐾 = 3 products that follow the same valuation distribution
𝐹1(𝑥) =𝐹2(𝑥) =𝐹3(𝑥) =𝑥. However, these products have heterogeneous prices 𝑝1 =𝑝2 <𝑝3. Product
𝑗 = 3 could be thought of as a limited version within the product series, maybe with a special
color. In this setup, there are 𝐾! = 6 different consumer types, 𝐶1 3 = 3 different type segments, and ∏
𝑏∈[𝐵]𝐾𝑏! = 2 types in each type segment. Moreover, the number of 𝛼-DP constraints to be satisfied
is 𝐾!·𝐾!·𝐾 = 108. Table 1 showcases𝑄𝜋,𝑗 , 𝑞𝜋,𝑗 , and 𝜃𝑗 under the optimal recommendation policy.
𝑄𝜋,𝑗 𝑞𝜋,𝑗
𝜋 𝑗 = 1 𝑗 = 2 𝑗 = 3 𝑗 = 1 𝑗 = 2 𝑗 = 3
1≻ 2≻ 3 0.366 0.366 0.269 2.718 2.718 1.0
2≻ 1≻ 3 0.366 0.366 0.269 2.718 2.718 1.0
1≻ 3≻ 2 0.366 0.134 0.500 2.718 1.0 1.859
2≻ 3≻ 1 0.134 0.366 0.500 1.0 2.718 1.859
3≻ 1≻ 2 0.134 0.134 0.731 1.0 1.0 2.718
3≻ 2≻ 1 0.134 0.134 0.731 1.0 1.0 2.718
𝜃𝑗
𝑗 = 1 𝑗 = 2 𝑗 = 3
0.134 0.134 0.269
Table 1 Optimal privacy-preserving personalized recommendation policy with heterogeneous products. We set
𝐾 = 3, 𝐹𝑗(𝑥) =𝑥(𝑗∈[𝐾]), 𝑝1 =𝑝2 = 0.1,𝑝 3 = 0.2, 𝛾 = 0.7, and exp(𝛼)≈ 2.718.
It is evident from Table 1 that the optimal policy 𝑄𝜋,𝑗 satisfies the symmetry property outlined
in Lemma 5 and can be decomposed as the product of 𝑞𝜋,𝑗 and 𝜃𝑗 as shown in Proposition 4.
Note that the values of 𝑞𝜋,𝑗 rank in the same order as the given preference profile 𝜋—confirming
its representation of customers’ private information. Moreover, we also find that 𝜃3 > 𝜃 1 = 𝜃2 in
this example because the platform places greater emphasis on retailer revenue (i.e., 𝛾 = 0.7) and
systematically prioritizes the higher-revenue product.
Figure 6 further exhibits the comparative statics on the product-specific weight 𝜃𝑗’s. First, we
observe that 𝜃1 equals 𝜃2 across all panels because products 1 and 2 belong to the same segment and
are treated identically, i.e., 𝐹1(·) =𝐹2(·) and 𝑝1 =𝑝2. Second, in panels 6a, 6b, and 6c, we observe

F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems 25
0.25 0.5 0.75 1
0.2
0.4
0.6
0.8
1
𝛾
𝜃
𝜃1(𝑝1 = 0.1)
𝜃2(𝑝2 = 0.1)
𝜃3(𝑝3 = 0.2)
(a) 𝛾 varies ( 𝛼 = 0.1)
0.25 0.5 0.75 1
0.2
0.4
0.6
0.8
1
𝛾
𝜃
𝜃1(𝑝1 = 0.1)
𝜃2(𝑝2 = 0.1)
𝜃3(𝑝3 = 0.2)
(b) 𝛾 varies ( 𝛼 = 0.5)
0.25 0.5 0.75 1
0.2
0.4
0.6
0.8
1
𝛾
𝜃
𝜃1(𝑝1 = 0.1)
𝜃2(𝑝2 = 0.1)
𝜃3(𝑝3 = 0.2)
(c) 𝛾 varies ( 𝛼 = 1.0)
0.6 1.2 1.8 2.4 3
0.1
0.2
0.3
0.4
0.5
𝛼
𝜃
𝜃1(𝑝1 = 0.1)
𝜃2(𝑝2 = 0.1)
𝜃3(𝑝3 = 0.2)
(d) 𝛼 varies ( 𝛾 = 0.2)
0.6 1.2 1.8 2.4 3
0.1
0.2
0.3
0.4
0.5
𝛼
𝜃
𝜃1(𝑝1 = 0.1)
𝜃2(𝑝2 = 0.1)
𝜃3(𝑝3 = 0.2)
(e) 𝛼 varies ( 𝛾 = 0.5)
0.6 1.2 1.8 2.4 3
0.2
0.4
0.6
0.8
1
𝛼
𝜃
𝜃1(𝑝1 = 0.1)
𝜃2(𝑝2 = 0.1)
𝜃3(𝑝3 = 0.2)
(f) 𝛼 varies ( 𝛾 = 0.8)
Figure 6 (Color online) Comparative statics of product-specific weight 𝜃 with heterogeneous products. We set
𝐾 = 3, 𝐹𝑗(𝑥) =𝑥(𝑗∈[𝐾]), and 𝑝1 =𝑝2 = 0.1,𝑝 3 = 0.2.
that 𝜃3 increases with 𝛾, while 𝜃1 = 𝜃2 decrease. This pattern arises because we set 𝑝3 >𝑝1 =𝑝2, and
as the platform becomes more focused on retailer revenue, it systematically prioritizes the higher-
priced product. We also observe a convergence between 𝜃1 = 𝜃2 and 𝜃3 as the privacy budget 𝛼
increases in panels 6d, 6e, and 6f. This occurs because the platform relies more on personal data for
recommendations as privacy concerns decrease. Consequently, the influence of the non-personalized
weight 𝜃𝑗’s becomes less significant.
6. Assortment Recommendation
In practice, the platform may recommend a subset of unranked products, rather than a single product,
to the consumer. For example, studies such as Honhon et al. (2012); Aouad et al. (2018); Sturt (2025)
examine assortment planning when consumers make choices according to the ranking-based model.
Building on Section 5, we consider heterogeneous products with independent valuation distribu-
tions{𝐹𝑗}𝑗∈[𝐾] and prices{𝑝𝑗}𝑗∈[𝐾]. The algorithm has access to the consumer’s type 𝜋∈ 𝜎(𝜋). Instead
of recommending one product only, the platform can now offer a personalized assortment of products
𝑎⊆[𝐾], where the set of all possible assortments is denoted as 𝐴, containing 2𝐾− 1 options. The

26 F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems
platform optimizes the recommendation policy 𝑄 ≜{𝑄𝜋,𝑎}𝜋∈𝜎(𝐾);𝑎∈𝐴 to maximize the weighted sum
of retailer revenue and consumer surplus, subject to 𝒪((𝐾!)2·( 2𝐾− 1)) 𝛼-DP constraints; that is,
max
𝑄
∑
𝜋∈𝜎(𝐾)
𝜌𝜋
∑
𝑎∈𝐴
𝑄𝜋,𝑎·[ 𝛾· Π𝜋,𝑎+( 1− 𝛾)· 𝑆𝜋,𝑎] (♯)
subject to 𝑄𝜋,𝑎≥ 0, ∀𝜋∈ 𝜎(𝐾);𝑎∈𝐴, ∑
𝑎∈𝐴
𝑄𝜋,𝑎 = 1, ∀𝜋∈ 𝜎(𝐾),
𝑄𝜋,𝑎
𝑄ˆ𝜋,𝑎
≤ exp(𝛼), ∀𝜋,ˆ𝜋∈ 𝜎(𝐾);𝑎∈𝐴,
where
Π𝜋,𝑎 ≜
∑
𝑗∈𝑎
𝑝𝑗· P
[
𝑉𝜋,𝑗−𝑝𝑗≥𝑉𝜋,𝑘−𝑝𝑘,∀𝑘∈𝑎, and𝑉𝜋,𝑗−𝑝𝑗≥ 0
]
and 𝑆𝜋,𝑎 ≜ E
[ (
max
𝑗∈𝑎
{𝑉𝜋,𝑗−𝑝𝑗}
)+]
are computed based on the consumer’s utility-maximizing random choice; that is, the consumer selects
from the products offered in the assortment or the no-purchase outside option, which provides a
deterministic utility of zero. As noted in Wang (2022), the assortment optimization problem becomes
challenging when the outside option’s utility is non-random in the underlying choice model. Therefore,
we will rely on numerical studies to gain insights into the problem ( ♯).
Example 3. We examine the case with 𝐾 = 4 products, each having i.i.d. uniform val-
uation distributions, i.e., 𝐹1(𝑥) = 𝐹2(𝑥) = 𝐹3(𝑥) = 𝐹4(𝑥) = 𝑥. The assortment optimization
problem becomes trivial if we consider homogeneous products, as recommending the full
set, 𝑎 =[𝐾], would always be optimal. To avoid this, we assume heterogeneous prices where
𝑝1 < 𝑝2 < 𝑝3 < 𝑝4. The platform can then recommend an assortment 𝑎⊆[ 𝐾] from the set 𝐴 ≜{
{1},{2},{3},{4},{1, 2},{1, 3},{1, 4},{2, 3},{2, 4},{3, 4},{1, 2, 3},{1, 2, 4},{1, 3, 4},{2, 3, 4},{1, 2, 3, 4}
}
,
providing 2𝐾− 1 = 15 possible options. The number of 𝛼-DP constraints to be satisfied is
(𝐾!)2·( 2𝐾− 1) = 8640. We numerically checked that the optimal assortment recommendation policy
shares a similar structure with the results in Lemma 5 and Proposition 4. Specifically, 𝑄 follows
a weighted threshold policy that can be decomposed into 𝑄𝜋,𝑎 =𝑞𝜋,𝑎· 𝜃𝑎, where 𝑞𝜋,𝑎 facilitates
personalized recommendations, and 𝜃𝑎 is the non-personalized assortment-specific weight.
Figure 7 shows the comparative statics of assortment-specific weight 𝜃𝑎’s. We observe that the
platform will recommend the full product set 𝑎 ={1, 2, 3, 4} with probability one when 𝛾 is small,
and only the highest-revenue product 𝑎 ={4} when 𝛾 is large. This occurs because, when 𝛾 is large
enough, the platform aims to avoid cannibalizing demand for product 𝑗 = 4, which generates the most
revenue, and thus prefers to recommend it as a singleton. Conversely, when 𝛾 is low, the platform
prioritizes consumer surplus, seeking to provide the consumer with as many choices as possible,
making the full product set 𝑎 ={1, 2, 3, 4} the optimal recommendation. For intermediate values of 𝛾,

F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems 27
0.25 0.5 0.75 1
0.25
0.5
0.75
1
𝛾
𝜃
𝜃{4}
𝜃{3,4}
𝜃{2,3,4}
𝜃{1,2,3,4}
(a) 𝛾 varies ( 𝛼 = 0.1)
0.25 0.5 0.75 1
0.25
0.5
0.75
1
𝛾
𝜃
𝜃{4}
𝜃{3,4}
𝜃{2,3,4}
𝜃{1,2,3,4}
(b) 𝛾 varies ( 𝛼 = 0.5)
0.25 0.5 0.75 1
0.25
0.5
0.75
1
𝛾
𝜃
𝜃{4}
𝜃{3,4}
𝜃{2,3,4}
𝜃{1,2,3,4}
(c) 𝛾 varies ( 𝛼 = 1.0)
Figure 7 (Color online) Comparative statics of assortment-specific weight 𝜃 with heterogeneous products. We
set 𝐾 = 4, 𝐹𝑗(𝑥) =𝑥(𝑗∈[𝐾]), and 𝑝1 = 0.05,𝑝 2 = 0.10,𝑝 3 = 0.15,𝑝 4 = 0.60.
a balance is struck between avoiding the cannibalization of product 𝑗 = 4 (hence, avoiding the full set
recommendation) and giving consumers more options (thus, not only product 4). As a result, partial
assortments containing product 𝑗 = 4 become viable, possibly with 𝜃{3,4}, 𝜃{2,3,4} > 0. Notably, in this
example, the 𝛼-DP constraints lead to a sparse assortment recommendation policy, with many 𝜃𝑎
values being zero. This occurs because the full set 𝑎 ={1, 2, 3, 4}, which is insusceptible to privacy
attacks, absorbs much of the recommendation weights.
7. Conclusion
In this paper, we address the privacy issue associated with personalized product recommendations.
We propose a privacy-preserving personalized product recommendation policy that adheres to dif-
ferential privacy constraints, effectively mitigating privacy risk while still providing relevant recom-
mendations. Our analysis shows that the optimal policy for privacy-preserving personalized product
recommendations is a threshold policy that randomly selects products. A subset of products have
higher recommendation probabilities than the remaining options, and the priority set is determined
by a cut-off on the consumer’s preference list. This policy strikes a subtle balance between person-
alization and privacy, which is transparent, interpretable, and easy to implement. We also explore
how exogenous parameters affect the optimal policy design by examining a fluid model. Of particular
interest, we find that the impact of the product price on the optimal threshold is non-monotonic.
Furthermore, we investigate the economic repercussions of having privacy preservation in recommen-
dations. Our analysis shows when product prices are exogenously determined, privacy protection
reduces consumer surplus due to the decreased match values of recommended products. However,
when retailers optimally set prices, the impact of privacy protection on surplus is more nuanced and
may be non-monotonic due to the trade-off between recommendation relevance and price inflation.

28 F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems
Our proposed privacy protection framework in recommendations aligns with current regulatory
trends and industry developments, offering valuable insights for practitioners looking to design
privacy-preserving personalized recommendation policies or policymakers aiming to enact privacy-
related regulations. It is worth noting that there is an ongoing discussion about incorporating more
ethical considerations into operational policies and prescriptive algorithms of firms (see, e.g., David
Hunt 2021). For example, to ensure fairness within these policies and prevent discrimination against
vulnerable minorities from being exacerbated by increasing computational power, we must guarantee
these policies are free from bias (see, e.g., Fu et al. 2022; Cohen et al. 2022). Moreover, we should
strive for greater transparency in black-box systems to alleviate people’s mistrust in opaque policies
and hold them accountable for their outputs (see, e.g., Wang et al. 2022). Additionally, it is essential
to curb the spread of misinformation facilitated by these advanced algorithms (see, e.g., Zhang et al.
2022). We hope our study will inspire further research on socially-responsible operational policies.
Acknowledgment
The authors thank Department Editor Francis de Vericourt, the Associate Editor, and two anonymous reviewers
for their feedback, which has significantly improved the paper. Xingyu Fu acknowledges financial support from the
University of New South Wales [Start-Up Grant, UNSW Business School Dean’s Research Fellowship]. Ningyuan Chen
is supported by the Institute for Management & Innovation (IMI) Research Grant. Pin Gao’s research is supported
by the National Natural Science Foundation of China [Grants 72522026, 72201234, 72192805], Collaborative Research
Funding Hong Kong [Grant C6032-21G], and the Guangdong Provincial Key Laboratory of Mathematical Foundations
for Artificial Intelligence [Grant 2023B1212010001].
Endnotes
1. “How retailers can keep up with consumers” from McKinsey: https://www.mckinsey.com/industries/retail/our-
insights/how-retailers-can-keep-up-with-consumers ; “Facebook’s global revenue as of 3rd quarter 2021, by
segment” from statista: https://www.statista.com/statistics/277963/facebooks-quarterly-global-revenue-
by-segment/.
2. The notification “This ad has multiple versions” means the ad is assembled by the dynamic creative algorithm to target
different customers. See “Facebook’s dynamic creative can generate up to 6,250 versions of an ad” from MarTech:
https://martech.org/facebooks-dynamic-creative-option-can-automatically-produce-6250-versions-ad/ .
3. In 2015, WeChat started to recommend products on the Moments, which is similar to the Meta Timeline. See
“Tencent Makes Advertising Push” from The Wall Street Journal: https://www.wsj.com/articles/tencent-makes-
advertising-push-1458235312 .
4. “Federated Learning: Collaborative Machine Learning without Centralized Training Data” from Google AI Blog:
https://ai.googleblog.com/2017/04/federated-learning-collaborative.html ; “Federated Evaluation and Tun-
ing for On-Device Personalization” from Apple Machine Learning Research: https://machinelearning.apple.com/
research/federated-personalization.

F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems 29
5. “Connecting to public Wi-Fi and hotspots” by Australian Signals Directorate: https://www.cyber.gov.au/protect-
yourself/staying-secure-online/connecting-to-public-wi-fi .
6. For an English summary of the new regulation, see, for instance, https://www.blankrome.com/publications/
chinas-regulation-internet-recommender-systems-what-us-companies-should-know . For the Chinese official
document, please visit http://www.cac.gov.cn/2022-01/04/c_1642894606364259.htm.
7. “WeChat has launched sponsored moments” from Red Ant Asia: https://asia.redant.com/wechat-has-launched-
sponsored-moments/; “Advertising on WeChat Moments” from WeChat Wiki: https://wechatwiki.com/wechat-
resources/wechat-moments-advertising-media-buying-cost-ad-format/ .
8. “How Companies Learn Your Secrets” from The New York Times: https://www.nytimes.com/2012/02/19/magazine/
shopping-habits.html.
9. “How TikTok’s Algorithm Figures You Out” from The Wall Street Journal: https://www.youtube.com/watch?v=
nfczi2cI6Cs.
10. “Price Discrimination: Robinson-Patman Violations” from the Federal Trade Commission: https://www.ftc.gov/
tips-advice/competition-guidance/guide-antitrust-laws/price-discrimination-robinson-patman .
11. For example, Mark Zuckerberg, the co-founder of Meta, has publicly downplayed the value of privacy by asserting
that “privacy is no longer a social norm” .
References
Abadi, M., A. Chu, I. Goodfellow, H. B. McMahan, I. Mironov, K. Talwar, and L. Zhang (2016). Deep
learning with differential privacy. In Proceedings of the 2016 ACM SIGSAC Conference on Computer
and Communications Security , pp. 308–318.
Abowd, J. M. (2018). The US Census Bureau adopts differential privacy. In Proceedings of the 24th ACM
SIGKDD International Conference on Knowledge Discovery & Data Mining , pp. 2867–2867.
Acemoglu, D., A. Makhdoumi, A. Malekian, and A. Ozdaglar (2017). Privacy-constrained network formation.
Games and Economic Behavior 105 , 255–275.
Acquisti, A., L. Brandimarte, and G. Loewenstein (2020). Secrets and likes: the drive for privacy and the
difficulty of achieving it in the digital age. Journal of Consumer Psychology 30 (4), 736–758.
Acquisti, A., C. Taylor, and L. Wagman (2016). The economics of privacy. Journal of Economic Litera-
ture 54(2), 442–92.
Anderson, E. T. and D. I. Simester (2010). Price stickiness and customer antagonism. Quarterly Journal of
Economics 125 (2), 729–765.
Aouad, A., V. Farias, R. Levi, and D. Segev (2018). The approximability of assortment optimization under
ranking preferences. Operations Research 66 (6), 1661–1669.
Armstrong, M. (2006). Competition in two-sided markets. RAND Journal of Economics 37 (3), 668–691.

30 F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems
Bonatti, A., Y. Huang, and J. M. Villas-Boas (2023). A theory of the effects of privacy. Working Paper.
Casadesus-Masanell, R. and A. Hervas-Drane (2015). Competing with privacy. Management Science 61 (1),
229–246.
Chaudhuri, K. and C. Monteleoni (2008). Privacy-preserving logistic regression. Advances in Neural Infor-
mation Processing Systems 21 .
Chen, N., A. Li, and S. Yang (2021). Revenue maximization and learning in products ranking. In Proceedings
of the 22nd ACM Conference on Economics and Computation , pp. 316–317.
Chen, X., S. Miao, and Y. Wang (2023). Differential privacy in personalized pricing with nonparametric
demand models. Operations Research 71(2), 581–602.
Chen, X., D. Simchi-Levi, and Y. Wang (2022). Privacy-preserving dynamic personalized pricing with
demand learning. Management Science 68 (7), 4878–4898.
Cohen, M. C. (2018). Big data and service operations. Production and Operations Management 27 (9),
1709–1723.
Cohen, M. C., A. N. Elmachtoub, and X. Lei (2022). Price discrimination with fairness constraints. Man-
agement Science 68 (12), 8536–8552.
David Hunt (2021). Can algorithms be ethical? https://pubsonline.informs.org/do/10.1287/orms.
2021.06.12/full/. [Online; Accessed 24-Feb-2025].
Derakhshan, M., N. Golrezaei, V. Manshadi, and V. Mirrokni (2022). Product ranking on online platforms.
Management Science 68 (6), 3975–4753.
Dwork, C., A. Roth, et al. (2014). The algorithmic foundations of differential privacy. Foundations and
Trends in Theoretical Computer Science 9 (3-4), 211–407.
Eilat, R., K. Eliaz, and X. Mu (2021). Bayesian privacy. Theoretical Economics 16 (4), 1557–1603.
Fainmesser, I. P., A. Galeotti, and R. Momot (2023). Digital privacy. Management Science 69 (6), 3157–3173.
Fallah, A., A. Makhdoumi, A. Malekian, and A. Ozdaglar (2022). Optimal and differentially private data
acquisition: Central and local mechanisms. In Proceedings of the 23rd ACM Conference on Economics
and Computation , pp. 1141–1141.
Farias, V. F., S. Jagabathula, and D. Shah (2013). A nonparametric approach to modeling choice with
limited data. Management Science 59 (2), 305–322.
Ferreira, K. J., S. Parthasarathy, and S. Sekar (2022). Learning to rank an assortment of products. Man-
agement Science 68 (3), 1828–1848.
Fioretto, F., C. Tran, P. Van Hentenryck, and K. Zhu (2022). Differential privacy and fairness in decisions
and learning tasks: A survey. arXiv: 2202.08187 .
Fu, R., M. Aseri, P. V. Singh, and K. Srinivasan (2022). “un”fair machine learning algorithms. Management
Science 68 (6), 4173–4195.

F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems 31
Gallego, G., A. Li, V.-A. Truong, and X. Wang (2020). Approximation algorithms for product framing and
pricing. Operations Research 68 (1), 134–160.
Gallego, G. and G. Van Ryzin (1994). Optimal dynamic pricing of inventories with stochastic demand over
finite horizons. Management Science 40 (8), 999–1020.
Gao, P., Y. Ma, N. Chen, G. Gallego, A. Li, P. Rusmevichientong, and H. Topaloglu (2021). Assortment
optimization and pricing under the multinomial logit model with impatient customers: Sequential
recommendation and selection. Operations Research 69 (5), 1509–1532.
Goldfarb, A., G. Jin, and K. Sudhir (2020). Introduction to the special issue on consumer protection.
Marketing Science 39 (1), 1–4.
Goldfarb, A. and C. E. Tucker (2011). Privacy regulation and online advertising. Management Science 57 (1),
57–71.
He, K. and X. Mu (2014). Differentially private and incentive compatible recommendation system for
the adoption of network goods. In Proceedings of the Fifteenth ACM Conference on Economics and
Computation, pp. 949–966.
Honhon, D., S. Jonnalagedda, and X. A. Pan (2012). Optimal algorithms for assortment selection under
ranking-based consumer choice models. Manufacturing & Service Operations Management 14 (2), 279–
289.
Hu, M., R. Momot, and J. Wang (2022). Privacy management in service systems. Manufacturing & Service
Operations Management 24 (5), 2761–2779.
Ichihashi, S. (2020). Online privacy and information disclosure by consumers. American Economic
Review 110 (2), 569–95.
Iyer, G., D. Soberman, and J. M. Villas-Boas (2005). The targeting of advertising. Marketing Science 24 (3),
461–476.
Johnson, G. A., S. K. Shriver, and S. Du (2020). Consumer privacy choice in online advertising: Who opts
out and at what cost to industry? Marketing Science 39 (1), 33–51.
Karmarkar, N. (1984). A new polynomial-time algorithm for linear programming. Combinatorica 4 (4),
373–395.
Ke, T. T. and K. Sudhir (2023). Privacy rights and data security: Gdpr and personal data markets. Man-
agement Science 69 (8), 4389–4412.
Laussel, D., N. Van Long, and J. Resende (2023). Profit effects of consumers’ identity management: A
dynamic model. Management Science 69 (6), 3602–3615.
Lei, Y., S. Miao, and R. Momot (2024). Privacy-preserving personalized revenue management. Management
Science 70 (7), 4875–4892.
Li, X. and K. J. Li (2023). Beating the algorithm: Consumer manipulation, personalized pricing, and big
data management. Manufacturing & Service Operations Management 25 (1), 36–49.

32 F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems
Liu, Z., D. J. Zhang, and F. Zhang (2021). Information sharing on retail platforms. Manufacturing & Service
Operations Management 23 (3), 606–619.
Lobel, I. (2021). Revenue management and the rise of the algorithmic economy. Management Science 67 (9),
5389–5398.
Makhdoumi, A. and N. Fawaz (2013). Privacy-utility tradeoff under statistical uncertainty. In 2013 51st
Annual Allerton Conference on Communication, Control, and Computing (Allerton) , pp. 1627–1634.
IEEE.
Margulis, S. T. (2003). Privacy as a social issue and behavioral concept. Journal of Social Issues 59 (2),
243–261.
Montes, R., W. Sand-Zantman, and T. Valletti (2019). The value of personal information in online markets
with endogenous privacy. Management Science 65 (3), 1342–1362.
Mosteller, F. (1946). On some useful inefficient statistics. Ann. Math. Statist. 17 (4), 377–408.
Negahban, S., S. Oh, and D. Shah (2017). Rank centrality: Ranking from pairwise comparisons. Operations
Research 65(1), 266–287.
Posner, R. A. (1981). The economics of privacy. American Economic Review 71 (2), 405–409.
Sturt, B. (2025). The value of robust assortment optimization under ranking-based choice models. Manage-
ment Science 71 (5), 4246–4265.
Tsitsiklis, J. N., K. Xu, and Z. Xu (2021). Private sequential learning. Operations Research 69(5), 1575–1590.
Valletti, T. and J. Wu (2020). Consumer profiling with data requirements: Structure and policy implications.
Production and Operations Management 29 (2), 309–329.
Wang, Q., Y. Huang, S. Jasin, and P. V. Singh (2022). Algorithmic transparency with strategic users.
Management Science 69 (4), 2297–2317.
Wang, R. (2022). What is the impact of nonrandomness on random choice models? Manufacturing & Service
Operations Management 24 (1), 485–503.
Wauthier, F., M. Jordan, and N. Jojic (2013). Efficient ranking from pairwise comparisons. In International
Conference on Machine Learning , pp. 109–117. PMLR.
Xu, F., X. Wang, and F. Zhang (2025). Consumer privacy in online retail supply chains. Management
Science, Forthcoming.
Xu, J., K. Xu, and D. Yang (2021). Learner-private convex optimization. In International Conference on
Machine Learning, pp. 11570–11580. PMLR.
Yang, Q., Y. Liu, Y. Cheng, Y. Kang, T. Chen, and H. Yu (2019). Federated learning. Synthesis Lectures
on Artificial Intelligence and Machine Learning 13 (3), 1–207.
Zhang, J., K. Moon, and S. K. Veeraraghavan (2022). Does fake news create echo chambers? SSRN 4144897 .
Zhang, M., E. Wei, R. Berry, and J. Huang (2023). Age-dependent differential privacy. IEEE Transactions
on Information Theory 70 (2), 1300–1319.

F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems 1
Online Supplement
Privacy-Preserving Personalized Recommender Systems
Appendix A: Proofs
A.1. Proof of Lemma 1
(1) We have Π𝜋,𝜋(𝑖) ≜ 𝑝· P[𝑉𝜋,𝜋(𝑖)≥ 𝑝], Πˆ𝜋,ˆ𝜋(𝑖) ≜ 𝑝· P[𝑉ˆ𝜋,ˆ𝜋(𝑖)≥ 𝑝] and 𝑆𝜋,𝜋(𝑖) ≜ E[(𝑉𝜋,𝜋(𝑖)−𝑝)+],𝑆ˆ𝜋,ˆ𝜋(𝑖) ≜
E[(𝑉ˆ𝜋,ˆ𝜋(𝑖)−𝑝)+]. Note that both random variables 𝑉𝜋,𝜋(𝑖) and𝑉ˆ𝜋,ˆ𝜋(𝑖) are subject to the 𝑖th largest order
statistics of 𝐹(·), which are independent of 𝜋 and ˆ𝜋, and thereby 𝑉𝜋,𝜋(𝑖) and 𝑉ˆ𝜋,ˆ𝜋(𝑖) share the same
probability distribution.
(2) Take𝑖,𝑘 ∈[𝐾], with 𝑖≤𝑘. The two events below satisfy the relation,
{𝜔∈ Ω|𝑉𝜋,𝜋(𝑖)(𝜔)≥ 𝑝}⊇{ 𝜔∈ Ω|𝑉𝜋,𝜋(𝑘)(𝜔)≥ 𝑝},
where Ω is the sample space. By the non-monotonicity of probability measure, we must have,
P[𝑉𝜋,𝜋(𝑖)≥𝑝]≥ P[𝑉𝜋,𝜋(𝑘)≥𝑝] ⇒ Π𝜋,𝜋(𝑖)≥ Π𝜋,𝜋(𝑘).
The above argument also shows the random variable 𝑉𝜋,𝜋(𝑖) has first-order stochastic dominance over the
random variable 𝑉𝜋,𝜋(𝑘). Note that an equivalent definition of first-order stochastic dominance is that
𝑋 has first-order stochastic dominance over 𝑌 if and only if E[𝜓(𝑋)]≥ E[𝜓(𝑌)] for all non-decreasing
function 𝜓 : R→ R. Let 𝜓(𝑥) ≜(𝑥−𝑝)+, which is non-decreasing, and then we must have,
E[𝜓(𝑉𝜋,𝜋(𝑖))]≥ E[𝜓(𝑉𝜋,𝜋(𝑘))] ⇒ 𝑆𝜋,𝜋(𝑖)≥𝑆𝜋,𝜋(𝑘).
We have completed the proof. ■
A.2. Proof of Lemma 2
Given an arbitrary 𝛼-DP recommendation policy 𝐻𝜋,𝑗 , we now intend to construct another recommendation
policy 𝑄𝜋,𝑗 satisfying the conditions enumerated in Lemma 2. Specifically, we let,
𝑄𝜋,𝑗 ≜
∑
˜𝜋∈𝜎(𝐾)𝐻˜𝜋,˜𝜋(𝜋−1(𝑗))
∑
˜𝜋∈𝜎(𝐾) 1 , 𝜋∈ 𝜎(𝐾),𝑗∈[𝐾]. (A.1)
Next, we aim to show the properties of the newly constructed policy 𝑄.
Property 1: ∑ 𝑗∈[𝐾]𝑄𝜋,𝑗 = 1,∀𝜋∈ 𝜎(𝐾).
proof:
∑
𝑗∈[𝐾]
𝑄𝜋,𝑗 =
∑
𝑗∈[𝐾]
∑
˜𝜋∈𝜎(𝐾)𝐻˜𝜋,˜𝜋(𝜋−1(𝑗))
∑
˜𝜋∈𝜎(𝐾) 1 =
∑
˜𝜋∈𝜎(𝐾)
∑
𝑗∈[𝐾]𝐻˜𝜋,˜𝜋(𝜋−1(𝑗))
∑
˜𝜋∈𝜎(𝐾) 1 .
Notice that 𝜋 and ˜𝜋 are both bijection from [𝐾] to[𝐾]. Thus, ∑ 𝑗∈[𝐾]𝐻˜𝜋,˜𝜋(𝜋−1(𝑗)) = ∑ 𝑖∈[𝐾]𝐻˜𝜋,˜𝜋(𝑖) = 1, which
suggests that 𝑄𝜋,· is indeed a probability distribution over the product space [𝐾]. □
Property 2:
𝑄𝜋,𝑗
𝑄ˆ𝜋,𝑗 ≤ exp(𝛼),∀𝜋,ˆ𝜋∈ 𝜎(𝐾);𝑗∈[𝐾].
proof: Denote 𝑖1 = 𝜋−1(𝑗) and 𝑖2 =ˆ𝜋−1(𝑗), then the ratio can be written as
𝑄𝜋,𝑗
𝑄ˆ𝜋,𝑗
=
∑
˜𝜋∈𝜎(𝐾)𝐻˜𝜋,˜𝜋(𝑖1) ∑
˜𝜋∈𝜎(𝐾)𝐻˜𝜋,˜𝜋(𝑖2)
=
∑
𝑘∈[𝐾]
∑
˜𝜋(𝑖1)=𝑘𝐻˜𝜋,𝑘 ∑
𝑘∈[𝐾]
∑
˜𝜋(𝑖2)=𝑘𝐻˜𝜋,𝑘
.

2 F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems
Note that for all 𝑘∈[𝐾], we have #{˜𝜋∈ 𝜎(𝐾)|˜𝜋(𝑖1) =𝑘} = #{˜𝜋∈ 𝜎(𝐾)|˜𝜋(𝑖2) =𝑘}, where the operator “ #”
represents the cardinality of a given set. Further notice that 𝐻 policy has already satisfied the 𝛼-DP con-
straint, i.e.,
𝐻𝜋1,𝑘
𝐻𝜋2,𝑘 ≤ exp(𝛼) for sure. Therefore, we can see the newly constructed policy 𝑄 also satisfies the
𝛼-DP constraint. □
Property 3: 𝑄𝜋,𝜋(𝑖) =𝑄ˆ𝜋,ˆ𝜋(𝑖),∀𝜋,ˆ𝜋∈ 𝜎(𝐾);𝑖∈[𝐾].
proof:
𝑄𝜋,𝜋(𝑖) =
∑
˜𝜋∈𝜎(𝐾)𝐻˜𝜋,˜𝜋(𝜋−1(𝜋(𝑖))) ∑
˜𝜋∈𝜎(𝐾) 1 =
∑
˜𝜋∈𝜎(𝐾)𝐻˜𝜋,˜𝜋(𝑖) ∑
˜𝜋∈𝜎(𝐾) 1 =
∑
˜𝜋∈𝜎(𝐾)𝐻˜𝜋,˜𝜋(ˆ𝜋−1(ˆ𝜋(𝑖))) ∑
˜𝜋∈𝜎(𝐾) 1 =𝑄ˆ𝜋,ˆ𝜋(𝑖),
which is independent of the consumer types 𝜋 and ˆ𝜋, but solely relies on the ranking 𝑖. Note that such
invariant property is the most useful feature of the newly constructed policy 𝑄, which greatly simplifies our
further analysis. □
Property 4: ∑ 𝜋∈𝜎(𝐾) ∑ 𝑗∈[𝐾]𝑄𝜋,𝑗·𝑂𝜋,𝑗 = ∑ 𝜋∈𝜎(𝐾) ∑ 𝑗∈[𝐾]𝐻𝜋,𝑗·𝑂𝜋,𝑗 .
proof:
∑
𝜋∈𝜎(𝐾)
∑
𝑗∈[𝐾]
𝑄𝜋,𝑗·𝑂𝜋,𝑗 =
∑
𝜋∈𝜎(𝐾)
∑
𝑖∈[𝐾]
𝑄𝜋,𝜋(𝑖)·𝑂𝜋,𝜋(𝑖) =
∑
𝜋∈𝜎(𝐾)
∑
𝑖∈[𝐾]
∑
˜𝜋∈𝜎(𝐾)𝐻˜𝜋,˜𝜋(𝑖)𝑂𝜋,𝜋(𝑖) ∑
˜𝜋∈𝜎(𝐾) 1
=
∑
𝜋∈𝜎(𝐾)
∑
˜𝜋∈𝜎(𝐾)
∑
𝑖∈[𝐾]𝐻˜𝜋,˜𝜋(𝑖)𝑂𝜋,𝜋(𝑖) ∑
˜𝜋∈𝜎(𝐾) 1 .
By Lemma 1, we have 𝑂𝜋,𝜋(𝑖) =𝑂˜𝜋,˜𝜋(𝑖) holds for all 𝜋,˜𝜋∈ 𝜎(𝐾). Thus, the above boils down to
∑
𝜋∈𝜎(𝐾)
[ ∑ ˜𝜋∈𝜎(𝐾) ∑ 𝑖∈[𝐾]𝐻˜𝜋,˜𝜋(𝑖)𝑂˜𝜋,˜𝜋(𝑖) ∑
˜𝜋∈𝜎(𝐾) 1
]
=
∑
˜𝜋∈𝜎(𝐾)
∑
𝑖∈[𝐾]
𝐻˜𝜋,˜𝜋(𝑖)𝑂˜𝜋,˜𝜋(𝑖) =
∑
𝜋∈𝜎(𝐾)
∑
𝑗∈[𝐾]
𝐻𝜋,𝑗𝑂𝜋,𝑗.
Therefore, we have shown that policy 𝑄 generates exactly the same objective value as policy 𝐻 for the
platform. □
To wrap up, given any 𝛼-DP recommendation policy 𝐻, we can construct another 𝛼-DP recommendation
policy 𝑄 based on ( A.1) so that 𝑄 generates the same objective value as 𝐻 and enjoys a nice invariant
property. We have completed the proof. ■
A.3. Proof of Lemma 3
For given 𝐾 and 𝑖, we use 𝑉(𝑖) to denote the 𝑖-th largest order statistic of 𝑉1, …, 𝑉𝐾. We also let 𝜅 =
⌊(1−𝐹(𝑧))𝐾⌋. By the law of total probability, the expression we are analyzing is
P
[
The valuation of a recommended product is less than 𝑥
]
=
𝐾∑
𝑖=1
𝑄𝑖(𝛼, 𝜅)· P[𝑉(𝑖)≤𝑥]
= 𝐾 𝜅 exp(𝛼)+( 𝐾− 𝜅)(exp(𝛼) 1 𝐾
𝜅∑
𝑖=1
P[𝑉(𝑖)≤𝑥]+ 1 𝐾
𝐾∑
𝑖=𝜅+1
P[𝑉(𝑖)≤𝑥]).
By the definition of 𝜅, it is clear that
lim
𝐾→∞
𝐾
𝜅 exp(𝛼)+( 𝐾− 𝜅) = 1 [1−𝐹(𝑧)] exp(𝛼)+ 𝐹(𝑧). (A.2)
So we will focus on analyzing the limit of the summation of probabilities.

F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems 3
When𝑉1, …, 𝑉𝐾 are realized, we show that
𝜅∑
𝑖=1
I[𝑉(𝑖) >𝑥] = max{𝜅,
𝐾∑
𝑖=1
I[𝑉𝑖 >𝑥]}
Indeed, if ∑𝐾 𝑖=1 I[𝑉𝑖 >𝑥] > 𝜅, then there are more than 𝜅 realized valuations greater than 𝑥 and the left-hand
side is exactly 𝜅. On the other hand, if ∑𝐾 𝑖=1 I[𝑉𝑖 >𝑥]≤ 𝜅, then both sides count the number of valuations
greater than 𝑥. As a result,
1
𝐾
𝜅∑
𝑖=1
I[𝑉(𝑖)≤𝑥] = 1− 1 𝐾 max{𝜅,
𝐾∑
𝑖=1
I[𝑉𝑖 >𝑥]}→ 1− max{1−𝐹(𝑧), 1−𝐹(𝑥)} = min{𝐹(𝑧),𝐹(𝑥)}
almost surely, due to the law of large numbers. Because the random variables are uniformly bounded, by
uniform integrability, it implies that
lim
𝐾→∞
1
𝐾
𝜅∑
𝑖=1
P[𝑉(𝑖)≤𝑥] = min{𝐹(𝑧),𝐹(𝑥)}. (A.3)
Similarly, we can show that
lim
𝐾→∞
1
𝐾
𝐾∑
𝑖=𝜅+1
P[𝑉(𝑖)≤𝑥] =𝐹(𝑥)− min{𝐹(𝑧),𝐹(𝑥)}. (A.4)
Combining ( A.2) to ( A.4) we have shown that
lim
𝐾→∞
𝐾∑
𝑖=1
𝑄𝑖(𝛼, 𝜅)· P[𝑉(𝑖)≤𝑥] = exp(𝛼) min{𝐹(𝑧),𝐹(𝑥)}+ 𝐹(𝑥)− min{𝐹(𝑧),𝐹(𝑥)} [1−𝐹(𝑧)] exp(𝛼)+ 𝐹(𝑧) .
Taking derivatives of both sides with respect to 𝑥 yields the desired result. ■
A.4. Proof of Theorem 1
Let{𝑄𝑖}𝑖∈[𝐾] be the optimal solution to problem ( ▼). We now show the structural properties of {𝑄𝑖}𝑖∈[𝐾].
Property 1: min{𝑄1,··· ,𝑄𝐾−1}≥ 𝑄𝐾 > 0.
proof: Otherwise, say there exists some ℓ∈{ 1,··· ,𝐾− 1} such that 𝑄𝐾 >𝑄ℓ . Then we can switch the values
of 𝑄𝐾 and 𝑄ℓ , which clearly would not affect the feasibility of the solution. While, such a modification
increases the platform’s objective value (note that 𝑂𝐾≤𝑂ℓ by Lemma 1), contradicting our assumption that
{𝑄𝑖}𝑖∈[𝐾] is optimal. Besides, if 𝑄𝐾 = 0, then the differential privacy constraint would be violated as there
exists some infinite probability ratio. Thus, 𝑄𝐾 > 0. □
Property 2: 𝑄1≥𝑄2≥···≥ 𝑄𝐾.
proof: Again, we can apply the switching argument similar to that in property 1 to establish the result. □
Property 3: 𝑄𝑖 =𝑄𝐾 or 𝑄𝑖 = exp(𝛼)· 𝑄𝐾,∀𝑖∈[𝐾].
proof: By property 1, we know 𝑄𝑖≥ 𝑄𝐾 for sure. Furthermore, due to the 𝛼-DP regulation, we have
𝑄𝑖≤ exp(𝛼)· 𝑄𝐾. Note that 𝑄𝐾 is strictly positive. Therefore, we can reformulate the platform’s problem as
follows
max
𝑥1,···,𝑥𝐾−1
𝑂𝐾+ ∑𝐾−1 𝑖=1 𝑥𝑖𝑂𝑖
1+ ∑𝐾−1 𝑖=1 𝑥𝑖 𝑠.𝑡. 𝑥 𝑖∈[ 1, exp(𝛼)].

4 F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems
Fixing arbitrary 𝑥−𝑖 =(𝑥1,··· ,𝑥𝑖−1,𝑥𝑖+1,··· ,𝑥𝐾−1), we take partial derivative of the objective with respect
to 𝑥𝑖, yielding
𝜕
𝜕𝑥𝑖
(𝑂𝐾+ ∑𝐾−1 𝑘=1 𝑥𝑘𝑂𝑘
1+ ∑𝐾−1 𝑘=1 𝑥𝑘
)
=(1+ ∑𝐾−1 𝑘=1 𝑥𝑘)𝑂𝑖−(𝑂𝐾+ ∑𝐾−1 𝑘=1 𝑥𝑘𝑂𝑘)
(1+ ∑𝐾−1 𝑘=1 𝑥𝑘)2
=(1+ ∑ 1≤𝑘≤𝐾−1 𝑎𝑛𝑑 𝑘≠𝑖𝑥𝑘)𝑂𝑖−𝑂𝐾− ∑ 1≤𝑘≤𝐾−1 𝑎𝑛𝑑 𝑘≠𝑖𝑥𝑘𝑂𝑘
(1+ ∑𝐾−1 𝑘=1 𝑥𝑘)2 ,
whose sign does not depend on 𝑥𝑖 per se. Therefore, the objective is either monotonically increasing or
monotonically decreasing in every single 𝑥𝑖, leading to a boundary solution. That is, at the optimality, we
must have 𝑥𝑖∈{ 1, exp(𝛼)}. □
To summarize, we have shown that the optimal privacy-preserving recommendation policy 𝑄𝑖 is decreasing
in the ranking index 𝑖. Besides, 𝑄𝑖 can only admit two possible values. These facts indicate that the optimal
recommendation method is a threshold policy, which completes the proof. ■
A.5. Proof of Lemma 4
When 𝑧 < 𝑝. We have consumer surplus 𝑆(𝑧) =
exp(𝛼)
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦)
[1−𝐹(𝑧)] exp(𝛼)+𝐹(𝑧) and retailer revenue Π(𝑧) =
𝑝 exp(𝛼)(1−𝐹(𝑝))
[1−𝐹(𝑧)] exp(𝛼)+𝐹(𝑧) , both of which are clearly increasing in 𝑧 (note that there are no 𝑧 in the numerators).
Therefore, 𝑂(𝑧) =(1− 𝛾)· 𝑆(𝑧)+ 𝛾· Π(𝑧) increases in 𝑧 for 𝑧 <𝑝.
When 𝑧≥𝑝. We have consumer surplus 𝑆(𝑧) =
exp(𝛼)
∫ 1
𝑧(𝑦−𝑝)𝑑𝐹(𝑦)+
∫ 𝑧
𝑝(𝑦−𝑝)𝑑𝐹(𝑦)
[1−𝐹(𝑧)] exp(𝛼)+𝐹(𝑧) and retailer revenue Π(𝑧) =
𝑝[exp(𝛼)(1−𝐹(𝑧))+𝐹(𝑧)−𝐹(𝑝)]
[1−𝐹(𝑧)] exp(𝛼)+𝐹(𝑧) . Differentiating 𝑂(𝑧) with respect to 𝑧 leads to
𝑂′(𝑧) = (exp(𝛼)− 1)𝑓(𝑧) [
(1−𝐹(𝑧)) exp(𝛼)+ 𝐹(𝑧)
] 2·𝐴(𝑧),
where the function 𝐴(𝑧) is defined as
𝐴(𝑧) ≜−𝛾𝑝𝐹(𝑝)+( 1− 𝛾)[(exp(𝛼)− 1)(𝑧−𝑝)𝐹(𝑧)+
∫ 𝑧
𝑝
(𝑦−𝑝)𝑑𝐹(𝑦)+ exp(𝛼)(𝑝−𝑧)+ exp(𝛼)
∫ 1
𝑧
(𝑦−𝑝)𝑑𝐹(𝑦)].
Thus, we have 𝑆𝑖𝑔𝑛[𝑂′(𝑧)] =𝑆𝑖𝑔𝑛[𝐴(𝑧)]. Moreover, we can check the following facts hold: ( 𝑖) 𝐴′(𝑧) =−[1−
𝛾]·[ exp(𝛼)(1−𝐹(𝑧))+𝐹(𝑧)] < 0; (𝑖𝑖 )𝐴(0) =(1− 𝛾) exp(𝛼)
∫ 1
0 𝑦𝑑𝐹(𝑦)≥ 0; (𝑖𝑖𝑖 )𝐴(1) =−𝛾≤ 0. Therefore, 𝑂(𝑧)
is strictly quasi-concave when 𝑧≥𝑝.
Combining the above two cases together, we know the platform’s objective function 𝑂(𝑧) is strictly quasi-
concave with respect to 𝑧 over𝑧∈[ 0, 1]. Since 𝑂(𝑧) is increasing in 𝑧 when 𝑧 <𝑝, we must have the optimal
valuation cut-off 𝑧★≥𝑝. ■
A.6. Proof of Proposition 1
(i) Fix 𝛾,𝑝 and let 𝛼 vary .Note that 𝜕 𝜕𝛼
[
−𝛾𝑝𝐹(𝑝)+( 1− 𝛾) exp(𝛼)
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦)
]
=(1− 𝛾) exp(𝛼)
∫ 1
𝑝(𝑦−
𝑝)𝑑𝐹(𝑦) > 0. In addition, when 𝛼→−∞ , we have −𝛾𝑝𝐹(𝑝)+( 1− 𝛾) exp(𝛼)
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦)→− 𝛾𝑝𝐹(𝑝) < 0;
when 𝛼→+∞ , we have −𝛾𝑝𝐹(𝑝)+( 1− 𝛾) exp(𝛼)
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦)→+∞ . Therefore, by the intermediate
value theorem (Rudin, 1976), there exists a unique solution, denoted as ˆ𝛼∈ R, to the equation 𝛾𝑝𝐹(𝑝) =
exp(𝛼)(1− 𝛾)
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦). When 𝛼≤ˆ𝛼, then we have lim𝑧↓𝑝𝑆𝑖𝑔𝑛[𝑂′(𝑧)] =𝑆𝑖𝑔𝑛[𝐴(𝑝)] =𝑆𝑖𝑔𝑛[−𝛾𝑝𝐹(𝑝)+
(1− 𝛾) exp(𝛼)
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦)]≤ 0, and therefore 𝑧★ =𝑝; When 𝛼 >ˆ𝛼, then lim𝑧↓𝑝𝑆𝑖𝑔𝑛[𝑂′(𝑧)] =𝑆𝑖𝑔𝑛[𝐴(𝑝)] =

F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems 5
𝑆𝑖𝑔𝑛[−𝛾𝑝𝐹(𝑝)+( 1− 𝛾) exp(𝛼)
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦)] > 0. Therefore, we have the optimal valuation cut-off 𝑧★ >𝑝,
which satisfies the first-order condition 𝐴(𝑧★; 𝛼) = 0. By the implicit function theorem (Rudin, 1976), we
have 𝑑𝑧 ★ 𝑑𝛼(𝛼) =− 𝜕𝐴/𝜕𝛼 𝜕𝐴/𝜕𝑧|𝑧=𝑧★(𝛼). Note that 𝜕𝐴/𝜕𝑧 =−[1− 𝛾]·[ exp(𝛼)(1−𝐹(𝑧))+ 𝐹(𝑧)] < 0 and 𝜕𝐴/𝜕 exp(𝛼) =
(1− 𝛾)
∫ 1
𝑧(1−𝐹(𝑦))𝑑𝑦 > 0. Thus, we have 𝑑𝑧 ★ 𝑑𝛼(𝛼) > 0.
(ii) Fix 𝛼,𝑝 and let 𝛾 vary .Note that 𝜕 𝜕𝛾
[
−𝛾𝑝𝐹(𝑝)+( 1− 𝛾) exp(𝛼)
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦)
]
=−𝑝𝐹(𝑝)− exp(𝛼)
∫ 1
𝑝(𝑦−
𝑝)𝑑𝐹(𝑦) < 0. In addition, when 𝛾→ 0,−𝛾𝑝𝐹(𝑝)+( 1− 𝛾) exp(𝛼)
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦)→ exp(𝛼)
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦) > 0;
when 𝛾→ 1,−𝛾𝑝𝐹(𝑝)+( 1− 𝛾) exp(𝛼)
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦)→− 𝑝𝐹(𝑝) < 0. Therefore, by the intermediate value
theorem, there exists a unique solution, denoted as ˆ𝛾∈( 0, 1), to the equation 𝛾𝑝𝐹(𝑝) = exp(𝛼)(1− 𝛾)
∫ 1
𝑝(𝑦−
𝑝)𝑑𝐹(𝑦). When 𝛾 > ˆ𝛾, then 𝑧★ =𝑝; When 𝛾≤ˆ𝛾, then 𝑧★ > 𝑝 and it satisfies the first-order condition
𝐴(𝑧★; 𝛾) = 0. By the implicit function theorem, we have 𝑑𝑧 ★ 𝑑𝛾(𝛾) =− 𝜕𝐴/𝜕𝛾 𝜕𝐴/𝜕𝑧|𝑧=𝑧★(𝛾). We can check 𝜕𝐴/𝜕𝛾 < 0.
Thus, 𝑑𝑧 ★ 𝑑𝛾(𝛾) < 0.
(iii) Fix 𝛼, 𝛾 and let 𝑝 vary .Note that −𝛾𝑝𝐹(𝑝)+( 1− 𝛾) exp(𝛼)
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦) strictly decreases in 𝑝.
This is because 𝐹(·) is the CDF of valuation distribution, which is assumed to be strictly increasing, and∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦) = E𝑋∼𝐹[max{𝑋−𝑝, 0}]. In addition, when 𝑝→ 0, we have −𝛾𝑝𝐹(𝑝)+( 1− 𝛾) exp(𝛼)
∫ 1
𝑝(𝑦−
𝑝)𝑑𝐹(𝑦)→( 1− 𝛾) exp(𝛼)
∫ 1
0 𝑦𝑑𝐹(𝑦) > 0; when 𝑝→ 1, we have −𝛾𝑝𝐹(𝑝)+( 1− 𝛾) exp(𝛼)
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦)→
−𝛾 < 0. Therefore, by the intermediate value theorem, there exists a unique ˆ𝑝∈( 0, 1) such that the equa-
tion 𝛾𝑝𝐹(𝑝) = exp(𝛼)(1− 𝛾)
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦) holds. When 𝑝 >ˆ𝑝, we have lim𝑧↓𝑝𝑆𝑖𝑔𝑛[𝑂′(𝑧)] =𝑆𝑖𝑔𝑛[𝐴(𝑝)] =
𝑆𝑖𝑔𝑛
[
−𝛾𝑝𝐹(𝑝)+( 1− 𝛾) exp(𝛼)
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦)
]
< 0, which leads to 𝑧★ = 𝑝; When 𝑝≤ˆ𝑝, then we have
lim𝑧↓𝑝𝑆𝑖𝑔𝑛[𝑂′(𝑧)] =𝑆𝑖𝑔𝑛[𝐴(𝑝)] =𝑆𝑖𝑔𝑛
[
−𝛾𝑝𝐹(𝑝)+( 1− 𝛾) exp(𝛼)
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦)
]
≥ 0. Therefore, 𝑧★ >𝑝 and
satisfies first-order condition 𝐴(𝑧★;𝑝) = 0. Taking implicit differentiation, we have 𝑑𝑧 ★ 𝑑𝑝(𝑝) =− 𝜕𝐴/𝜕𝑝 𝜕𝐴/𝜕𝑧|𝑧=𝑧★(𝑝).
Thus,𝑆𝑖𝑔𝑛[𝑑𝑧 ★ 𝑑𝑝(𝑝)] =𝑆𝑖𝑔𝑛[ 𝜕𝐴 𝜕𝑝|𝑧=𝑧★(𝑝)]. We can check 𝜕𝐴 𝜕𝑝 =𝐹(𝑝)− 2𝛾𝐹(𝑝)− 𝛾𝑝𝑓(𝑝), which completes the proof.
Lastly, as an example, say 𝛾 = 1/2; that is, the platform is maximizing the social welfare generated in the
marketplace. Then, when 𝑝≤ˆ𝑝, we have 𝜕𝐴 𝜕𝑝 =−𝛾𝑝𝑓(𝑝)≤ 0, namely, 𝑧★(𝑝) is decreasing in 𝑝; when 𝑝 >ˆ𝑝, we
have𝑧★(𝑝) =𝑝, which is increasing in 𝑝. Put simply, the optimal valuation cut-off 𝑧★ can be non-monotone
with respect to the product price 𝑝. ■
A.7. Proof of Proposition 2
We only prove the second part. If 𝛾 = 1, then we have,
lim
𝑝←𝑧
𝑆𝑖𝑔𝑛[𝑂′(𝑧)] =𝑆𝑖𝑔𝑛[𝐴(𝑝)] =𝑆𝑖𝑔𝑛 [ −𝑝𝐹(𝑝) ] < 0.
In addition, we already know that 𝑂(𝑧) increases in 𝑧 when 𝑧 <𝑝. Therefore, we obtain 𝑧★ =𝑝. If another
condition 𝛼 <ˆ𝛼 holds, then according to Proposition 1, we again obtain that 𝑧★ =𝑝.
If this is the case, we have the equilibrium consumer surplus given by,
𝑆★ = exp(𝛼)
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦)
exp(𝛼)[1−𝐹(𝑝)]+ 𝐹(𝑝) =
exp(𝛼)
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦)
exp(𝛼)
∫ 1
𝑝 1𝑑𝐹(𝑦)+
∫ 𝑝
0 1𝑑𝐹(𝑦)
,
Taking derivative, we have,
𝜕𝑆★
𝜕 exp(𝛼) =
∫ 𝑝
0 1𝑑𝐹(𝑦)·
∫ 1
𝑝(𝑦−𝑝)𝑑𝐹(𝑦)
(
exp(𝛼)
∫ 1
𝑝 1𝑑𝐹(𝑦)+
∫ 𝑝
0 1𝑑𝐹(𝑦)
) 2 > 0,
namely,𝑆★ is increasing in 𝛼, which completes the proof. ■

6 F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems
A.8. Proof of Proposition 3
We characterize the subgame-perfect equilibrium via backward induction; that is, we first derive how the
platform would design its personalized recommender system 𝑧★(𝑝) in response to the retailer’s price offer 𝑝,
and then solve for the retailer’s optimal pricing decision 𝑝★(𝛼).
Step 1: Platform’s Recommendation Decision. Say the retailer has set the product price at 𝑝∈[ 0, 1].
We intend to analyze the platform’s optimal recommendation policy 𝑧★(𝑝), which is determined after the
price announcement. According to the proof of Lemma 4, we have the platform’s objective 𝑂(𝑧) increases in
𝑧 for 𝑧≤𝑝; besides, when 𝛾 = 1, we have the following fact holds:
lim
𝑝←𝑧
𝑆𝑖𝑔𝑛[𝑂′(𝑧)] =𝑆𝑖𝑔𝑛[𝐴(𝑝)] =−𝑆𝑖𝑔𝑛[𝑝·𝐹(𝑝)] < 0.
Besides, we know that 𝑆𝑖𝑔𝑛[𝐴′(𝑧)] < 0 holds for 𝑧≥𝑝. Thus, 𝑂(𝑧) decreases in 𝑧 for𝑧≥𝑝. As a consequence,
the platform’s optimal response is 𝑧★(𝑝) =𝑝.
Step 2: Retailer’s Equilibrium Pricing. Anticipating the platform’s (responsive) recommendation policy
𝑧★(𝑝) =𝑝, the retailer faces the following optimization problem
𝑝★(𝛼)∈ arg max
𝑝∈[0,1]
𝑝· exp(𝛼)[1−𝐹(𝑝)]
exp(𝛼)[1−𝐹(𝑝)]+ 𝐹(𝑝),
where the valuation distribution satisfies 𝐹(𝑝) =𝑝𝛽 with 𝛽 > 0. Invoking the first-order condition, we can
derive the retailer’s (unique) equilibrium price given as follows
𝑝★(𝛼) = [ 1− 𝛽− 2 exp(𝛼)+ √ 1− 2𝛽+ 𝛽2+ 4𝛽 exp(𝛼) 2− 2 exp(𝛼) ] 1 𝛽 .
We can check that
𝑆𝑖𝑔𝑛
[𝑑𝑝 ★
𝑑𝛼(𝛼)
]
=𝑆𝑖𝑔𝑛
[
−1+ 𝛽+ 2 exp(𝛼)−
√
1− 2𝛽+ 𝛽2+ 4𝛽 exp(𝛼))
]
×
𝑆𝑖𝑔𝑛
[
1− 𝛽+ 2𝛽 exp(𝛼)−
√
1− 2𝛽+ 𝛽2+ 4𝛽 exp(𝛼)
]
.
It is easy to verify (by taking square) the above two factors are both non-negative and hence 𝑝★(𝛼) increases
in 𝛼. Therefore, the equilibrium recommendation threshold 𝑧★(𝛼) =𝑝★(𝛼) is increasing in 𝛼 as well. Moreover,
the equilibrium retailer revenue satisfies Π★(𝛼) = max𝑝∈[0,1] 𝑝·exp(𝛼)[1−𝐹(𝑝)] exp(𝛼)[1−𝐹(𝑝)]+𝐹(𝑝) . By the envelop theorem , we
have 𝑑Π★ 𝑑𝛼(𝛼) = 𝜕 𝜕𝛼 [ 𝑝·exp(𝛼)[1−𝐹(𝑝)] exp(𝛼)[1−𝐹(𝑝)]+𝐹(𝑝) ] |𝑝=𝑝★(𝛼) = exp(𝛼)𝑝1+𝛽(1−𝑝𝛽) [𝑝𝛽+exp(𝛼)(1−𝑝𝛽)]2|𝑝=𝑝★(𝛼), which is non-negative for sure. Thus,
we have the equilibrium retailer revenue Π★(𝛼) also increases in 𝛼.
Step 3: Equilibrium Consumer Surplus. Given product price 𝑝, the induced consumer surplus can be
computed as𝑆(𝑝|𝛼, 𝛽) = exp(𝛼)[𝛽−𝛽𝑝+𝑝(−1+𝑝𝛽)] [1+𝛽][𝑝𝛽−exp(𝛼)(−1+𝑝𝛽)] . Thus, the equilibrium consumer surplus is defined as 𝑆★(𝛼, 𝛽) ≜
𝑆(𝑝 =𝑝★(𝛼)| 𝛼, 𝛽). One can check that, when 𝛽∈( 0, 1), there exists a stationary point ˆ𝛼 > 0 such that
𝜕𝑆★
𝜕𝛼(𝛼, 𝛽) > 0 (resp., 𝜕𝑆★ 𝜕𝛼(𝛼, 𝛽) < 0) if and only if 𝛼 <ˆ𝛼 (resp., 𝛼 >ˆ𝛼); when 𝛽≥ 1, we can check that ˆ𝛼 < 0
holds, and therefore 𝜕𝑆★ 𝜕𝛼(𝛼, 𝛽) < 0 holds for 𝛼 > 0. We have completed the proof. ■

F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems 7
A.9. Proof of Lemma 5
Given any 𝛼-DP recommendation policy 𝐻, we now construct another policy 𝑄 such that
𝑄𝜋,𝑗 ≜
∑
˜𝜋∈𝒢(𝜋)𝐻˜𝜋,˜𝜋(𝜋−1(𝑗))
∑
˜𝜋∈𝒢(𝜋) 1 . (A.5)
Consider our base model in which all product valuations are independently and identically distributed, then
clearly𝒢(𝜋) = 𝜎(𝐾) holds. Therefore, construction ( A.5) nests construction ( A.1) as a special case. We intend
to show that the newly constructed recommendation policy 𝑄 satisfies all the requirements listed in Lemma 5.
Property 1: 𝑄𝜋,𝜋(·)≡𝑄ˆ𝜋,ˆ𝜋(·) holds when 𝒢(𝜋) =𝒢(ˆ𝜋).
proof: For 𝜋,ˆ𝜋 such that𝒢(𝜋) =𝒢(ˆ𝜋), we have
𝑄𝜋,𝜋(𝑖) =
∑
˜𝜋∈𝒢(𝜋)𝐻˜𝜋,˜𝜋(𝜋−1(𝜋(𝑖))) ∑
˜𝜋∈𝒢(𝜋) 1 =
∑
˜𝜋∈𝒢(𝜋)𝐻˜𝜋,˜𝜋(𝑖) ∑
˜𝜋∈𝒢(𝜋) 1 .
Note that the above quantity solely depends on ranking 𝑖 and type segment 𝒢(𝜋), and does not rely on
type 𝜋 per see. This implies that 𝑄𝜋,𝜋(𝑖) =𝑄ˆ𝜋,ˆ𝜋(𝑖) holds as long as 𝒢(𝜋) =𝒢(ˆ𝜋), which is the most important
property of policy 𝑄. □
Property 2: ∑ 𝑗∈[𝐾]𝑄𝜋,𝑗 = 1,∀𝜋∈ 𝜎(𝐾).
proof:
∑
𝑗∈[𝐾]
𝑄𝜋,𝑗 =
∑
𝑗∈[𝐾]
∑
˜𝜋∈𝒢(𝜋)𝐻˜𝜋,˜𝜋(𝜋−1(𝑗))
∑
˜𝜋∈𝒢(𝜋) 1 =
∑
˜𝜋∈𝒢(𝜋)
[∑
𝑗∈[𝐾]𝐻˜𝜋,˜𝜋(𝜋−1(𝑗))
]
∑
˜𝜋∈𝒢(𝜋) 1 .
Note that we have ∑ 𝑗∈[𝐾]𝐻˜𝜋,˜𝜋(𝜋−1(𝑗)) = 1 holds, and therefore we have established this property. □
Property 3:
𝑄𝜋,𝑗
𝑄ˆ𝜋,𝑗 ≤ exp(𝛼),∀𝜋 ≠ˆ𝜋∈ 𝜎(𝐾),𝑗∈[𝐾].
proof: Denote 𝑖1 = 𝜋−1(𝑗) and 𝑖2 =ˆ𝜋−1(𝑗). Since #𝒢(𝜋) = #𝒢(ˆ𝜋) = ∏ 𝑏∈[𝐵]𝐾𝑏! are the same constants, then
we have
𝑄𝜋,𝑗
𝑄ˆ𝜋,𝑗
=
∑
˜𝜋∈𝒢(𝜋)𝐻˜𝜋,˜𝜋(𝑖1) ∑
˜𝜋∈𝒢(ˆ𝜋)𝐻˜𝜋,˜𝜋(𝑖2)
.
Note that if ˜𝜋∈𝒢( 𝜋), then ˜𝜋(𝑖1) =˜𝜋(𝜋−1(𝑗))∈ℬ( 𝑗); similarly, when ˜𝜋∈𝒢(ˆ𝜋), we have ˜𝜋(𝑖2) =˜𝜋(ˆ𝜋−1(𝑗))∈
ℬ(𝑗). Therefore, the above expression can be expanded as
𝑄𝜋,𝑗
𝑄ˆ𝜋,𝑗
=
∑
𝑘∈ℬ(𝑗)
∑
˜𝜋∈𝒢(𝜋)∩˜𝜋(𝑖1)=𝑘𝐻˜𝜋,𝑘 ∑
𝑘∈ℬ(𝑗)
∑
˜𝜋∈𝒢(ˆ𝜋)∩˜𝜋(𝑖2)=𝑘𝐻˜𝜋,𝑘
.
For any given 𝑘∈ℬ( 𝑗), note that we can check that #{˜𝜋|˜𝜋∈𝒢( 𝜋)∩ ˜𝜋(𝑖1) =𝑘} = #{˜𝜋|˜𝜋∈𝒢(ˆ𝜋)∩ ˜𝜋(𝑖2) =
𝑘} =(𝐾ℬ(𝑗)− 1)!· ∏ 𝑏≠ℬ(𝑗)𝐾𝑏! holds, which are independent of 𝜋 andˆ𝜋, but merely depends on product 𝑗∈[𝐾].
Therefore, by the 𝛼-DP property of policy 𝐻 that
𝐻𝜋1,𝑘
𝐻𝜋2,𝑘 ≤ exp(𝛼),∀𝜋1, 𝜋2∈ 𝜎(𝐾),∀𝑘∈[𝐾], we could deduce
that
∑
˜𝜋∈𝒢(𝜋)∩˜𝜋(𝑖1)=𝑘𝐻˜𝜋,𝑘 ∑
˜𝜋∈𝒢(ˆ𝜋)∩˜𝜋(𝑖2)=𝑘𝐻˜𝜋,𝑘
≤ exp(𝛼), ∀𝑘∈ℬ( 𝑗).
As a consequence, we can obtain
∑
𝑘∈ℬ(𝑗)
∑
˜𝜋∈𝒢(𝜋)∪˜𝜋(𝑖1)=𝑘𝐻˜𝜋,𝑘 ∑
𝑘∈ℬ(𝑗)
∑
˜𝜋∈𝒢(ˆ𝜋)∪˜𝜋(𝑖2)=𝑘𝐻˜𝜋,𝑘
≤ exp(𝛼).
We are done. □

8 F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems
Property 4: ∑ 𝜋∈𝜎(𝐾) ∑ 𝑗∈[𝐾] 𝜌𝜋𝑄𝜋,𝑗𝑂𝜋,𝑗 = ∑ 𝜋∈𝜎(𝐾) ∑ 𝑗∈[𝐾] 𝜌𝜋𝐻𝜋,𝑗𝑂𝜋,𝑗 .
proof:
∑
𝜋∈𝜎(𝐾)
∑
𝑗∈[𝐾]
𝜌𝜋𝑄𝜋,𝑗𝑂𝜋,𝑗 =
∑
𝜋∈𝜎(𝐾)
∑
𝑖∈[𝐾]
𝜌𝜋𝑄𝜋,𝜋(𝑖)𝑂𝜋,𝜋(𝑖) =
∑
𝜋∈𝜎(𝐾)
∑
𝑖∈[𝐾]
∑
˜𝜋∈𝒢(𝜋) 𝜌𝜋𝐻˜𝜋,˜𝜋(𝑖)𝑂𝜋,𝜋(𝑖) ∑
˜𝜋∈𝒢(𝜋) 1 .
Note that the denominator ∑ ˜𝜋∈𝒢(𝜋) 1 = #𝒢(𝜋) = ∏ 𝑏∈[𝐵]𝐾𝑏! is a constant. Therefore, the above becomes
( ∑
𝜋∈𝜎(𝐾)
∑
˜𝜋∈𝒢(𝜋)
∑
𝑖∈[𝐾]
𝜌𝜋𝐻˜𝜋,˜𝜋(𝑖)𝑂𝜋,𝜋(𝑖)
)
/
( ∏
𝑏∈[𝐵]
𝐾𝑏!
)
.
Let 𝐺 denote the set of all distinct type segments, namely, it is defined as 𝐺 ≜{𝒢(𝜋)|𝜋∈ 𝜎(𝐾)}. Then, the
above further boils down to
(∑
𝑔∈𝐺
∑
𝜋∈𝑔
∑
˜𝜋∈𝑔
∑
𝑖∈[𝐾]
𝜌𝜋𝐻˜𝜋,˜𝜋(𝑖)𝑂𝜋,𝜋(𝑖)
)
/
( ∏
𝑏∈[𝐵]
𝐾𝑏!
)
.
Note that for all 𝜋∈𝑔, we have 𝜌𝜋 is independent of 𝜋 but solely relies on 𝑔. Moreover, we have 𝑂𝜋,𝜋(𝑖) solely
depends on 𝑔 and 𝑖, independent of 𝜋 per se. Therefore, the summation “ ∑ 𝜋∈𝑔” in the above expression
essentially times #𝑔 = #𝒢(𝜋) = ∏ 𝑏∈[𝐵]𝐾𝑏! in the numerator. This observation greatly simplifies the above
expression into
∑
𝑔∈𝐺
∑
˜𝜋∈𝑔
∑
𝑖∈[𝐾]
𝜌𝜋𝐻˜𝜋,˜𝜋(𝑖)𝑂𝜋,𝜋(𝑖).
Furthermore, we could replace 𝜌𝜋 by 𝜌˜𝜋 and replace 𝑂𝜋,𝜋(𝑖) by𝑂˜𝜋,˜𝜋(𝑖) since 𝜋,˜𝜋∈𝑔 both belong to the same
type segment. Then the above boils down to
∑
𝑔∈𝐺
∑
˜𝜋∈𝑔
∑
𝑖∈[𝐾]
𝜌˜𝜋𝐻˜𝜋,˜𝜋(𝑖)𝑂˜𝜋,˜𝜋(𝑖) =
∑
𝜋∈𝜎(𝐾)
∑
𝑗∈[𝐾]
𝜌𝜋𝐻𝜋,𝑗𝑂𝜋,𝑗.
We have finished the proof. □
Combining all the above four properties, we have proven this proposition: the invariant property of the
optimal recommendation policy persists for consumer types within the same type segment. ■
A.10. Proof of Proposition 4
To establish the proposition, we first show the following claim.
Claim: Policy 𝑄 subject to the 𝛼-DP constraint if and only if there exists some values {𝜃𝑗}𝑗∈[𝐾] and
{𝑞𝜋,𝑗}𝜋∈𝜎(𝐾);𝑗∈[𝐾] such that 𝑄 can be decomposed as 𝑄𝜋,𝑗 = 𝜃𝑗·𝑞𝜋,𝑗 . Furthermore, if we have 𝜃𝑗 > 0, then
𝑞𝜋,𝑗∈[ 1, exp(𝛼)] hold.
proof: “⇐”: This direction is obvious. “ ⇒”: Say 𝑄 subject to the 𝛼-DP constraint. For each 𝑗∈[𝐾], define
𝜃𝑗 ≜ min˜𝜋∈𝜎(𝐾)𝑄˜𝜋,𝑗 and 𝑞𝜋,𝑗 ≜𝑄𝜋,𝑗/𝜃𝑗 if 𝜃𝑗 > 0 holds. It is straightforward to see the properties hold. □
With the help of this claim, we can reformulate the platform’s optimization problem as follows,
max
𝜃,𝑞
∑
𝜋∈𝜎(𝐾)
∑
𝑗∈[𝐾]
𝜌𝜋𝑂𝜋,𝑗· 𝜃𝑗𝑞𝜋,𝑗
subject to 𝜃𝑗 > 0, ∀𝑗,
𝑞𝜋,𝑗∈[ 1, exp(𝛼)], ∀𝜋,𝑗, ∑
𝑗∈[𝐾]
𝜃𝑗𝑞𝜋,𝑗 = 1, ∀𝜋.

F u, Chen, Gao, and Li: Privacy-Preserving Personalized Recommender Systems 9
For each consumer type 𝜋, assume at the optimality there exists a threshold 𝜅𝜋∈[𝐾], such that 𝑞𝜋,𝜅𝜋 > 1.
Then we claim that 𝑞𝜋,𝑗 = exp(𝛼) for all 𝑂𝜋,𝑗 >𝑂𝜋,𝜅𝜋 . Suppose the claim does not hold, then there exists
some 𝑂𝜋,𝑗 >𝑂𝜋,𝜅𝜋 such that 𝑞𝜋,𝑗 < exp(𝛼). Then, we raise 𝑄𝜋,𝑗 slightly by 𝜖 > 0 (keeping 𝑞𝜋,𝑗 < exp(𝛼)) and
reduce 𝑄𝜋,𝜅𝜋 slightly by 𝜖 (keeping 𝑞𝜋,𝜅𝜋 > 1). This modification does not violate any imposed constraints.
Furthermore, notice that 𝑂𝜋,𝑗 >𝑂𝜋,𝜅𝜋 , which implies the objective is increased slightly. This contradicts the
optimality assumption. ■
References for Online Supplement
Rudin, W. (1976). Principles of Mathematical Analysis . McGraw-Hill New York.
