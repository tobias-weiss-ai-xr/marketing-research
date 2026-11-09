---
title: The New Age of Collusion? An Empirical Study into Airbnb's Pricing Dynamics and Market Behavior
url: https://arxiv.org/abs/2312.05633
category: consumer-behavior
subcategory: empirical
date: 2023-12
venue: ''
authors:
- Richeng Piao
source: arxiv
pdf_url: https://arxiv.org/pdf/2312.05633
pages: 12
chars: 35399
fetched_at: '2026-11-08T13:08:29+00:00'
kb_version: 1
---

# The New Age of Collusion? An Empirical Study into Airbnb's Pricing Dynamics and Market Behavior

arXiv:2312.05633v1  [econ.GN]  9 Dec 2023
The New Age of Collusion? An Empirical Study into Airbnb’s
Pricing Dynamics and Market Behavior
[Dr. Richeng Piao]
December 12, 2023
Abstract
This study investigates the implications of algorithmic pr icing in digital marketplaces, fo-
cusing on Airbnb’s pricing dynamics. With the advent of Airb nb’s new pricing tool, this
research explores how digital tools inﬂuence hosts’ pricin g strategies, potentially leading to
market dynamics that straddle the line between eﬃciency and collusion. Utilizing a Regres-
sion Discontinuity Design (RDD) and Propensity Score Match ing (PSM), the study examines
the causal eﬀects of the pricing tool on pricing behavior amo ng hosts with diﬀerent opera-
tional strategies. The ﬁndings aim to provide insights into the evolving landscape of digital
economies, examining the balance between competitive mark et practices and the risk of tacit
collusion facilitated by algorithmic pricing. This study c ontributes to the discourse on digital
market regulation, oﬀering a nuanced understanding of the i mplications of AI-driven tools in
market dynamics and antitrust analysis.
1 Introduction
1.1 Background
In the evolving landscape of the digital economy, the emergence of sophisticated digital tools has
revolutionized the way businesses operate and compete. A centra l development in this transfor-
mation is the advent of algorithmic pricing, which has the potential to alter market dynamics
profoundly. Historically, pricing strategies have been the domain of human decision-making, often
based on a mix of cost-plus logic, market sensing, and competitive an alysis. However, with the
rise of big data and advanced computational techniques, pricing alg orithms are increasingly taking
center stage.
The automation of pricing and other complex listing maintenance task s through digital tools
oﬀers signiﬁcant advantages in terms of eﬃciency and responsiven ess to market changes. Yet, this
evolution also brings forth new challenges and risks. One such risk is t he potential for algorithmic
collusion, where pricing algorithms could learn to implicitly coordinate wit h each other, leading to
price settings that may not align with competitive market outcomes.
The concept of algorithmic collusion is not merely theoretical but gro unded in economic princi-
ples. The Folk Theorem of game theory, for instance, suggests th e possibility of multiple equilibria
in inﬁnitely repeated games, including both competitive and collusive ou tcomes. In digital market-
places, where algorithms can quickly adjust prices in response to ma rket signals, a seemingly minor
event, such as a change in a single seller’s marginal cost(unilateral), could trigger a chain reaction.
1

This reaction could potentially escalate market prices, possibly even approaching monopoly pricing
levels under certain conditions.
Moreover, the self-learning capability of these algorithms, fueled b y vast troves of data and
machine learning techniques, could lead them to discover and sustain collusive equilibria without
explicit human direction or communication. This possibility marks a depa rture from traditional
collusion models, which typically require explicit agreements or commun ication between ﬁrms. In a
digital setting, algorithms might independently converge on similar pr icing strategies that maximize
proﬁts collectively, rather than competing aggressively as traditio nal market models would predict.
The potential for such outcomes is not just an academic concern b ut is increasingly gaining
attention in policy and regulatory circles. As algorithms become more sophisticated and perva-
sive, understanding their impact on market dynamics, competition, and consumer welfare becomes
paramount. This is especially pertinent in platforms like Airbnb, where pricing tools can provide
hosts with detailed market insights, potentially inﬂuencing their pricin g and listing strategies in
ways that have yet to be fully understood.
Our research seeks to empirically investigate these dynamics within t he context of Airbnb’s
marketplace. By analyzing the impact of Airbnb’s new pricing tool on h osts’ pricing and listing
strategies, we aim to shed light on the broader implications of digital t ools on market competition
and potential pathways towards algorithmic collusion. This investiga tion is not only critical for
understanding the current state of digital marketplaces but also for anticipating future developments
as these technologies continue to evolve.
1.2 Research Problem
This research delves into the evolving interplay between technology , market dynamics, and antitrust
concerns, speciﬁcally within the context of digital platforms like Airb nb. The introduction of
Airbnb’s new pricing tool, applicable to a broader category of digital m arketplaces and sellers,
serves as an ideal natural experiment for this study.
A primary focus of this research is the antitrust and anti-competit ive aspects associated with AI
algorithm pricing, not only in Airbnb’s context but in digital marketplac es at large. The current use
of similar pricing tools by humans already poses questions about comp etitive outcomes. However,
the move towards fully automated systems, where algorithmic pricin g might be automatically set,
intensiﬁes these concerns. This automation signiﬁcantly reduces t he cost and eﬀort required for
hosts (or general sellers in digital marketplaces) to manage their lis tings, potentially leading to a
strategic shift from long-term, stable pricing strategies to short -term, dynamic ones.
In traditional settings, some sellers might opt for lower prices and lo nger-term stability due to
the high costs associated with frequent price adjustments and list ing management. However, the
ease and eﬃciency oﬀered by automated tools could encourage a mo re frequent adjustment of prices
in response to real-time market data. This ease of pricing adjustme nt could lead to a strategic shift
among sellers toward more dynamic pricing strategies.
The implications of this shift are profound in terms of market compet ition. Markets might
move from competitive outcomes to collusive ones as sellers increasin gly rely on algorithmic tools
for pricing. These tools, designed to optimize revenues, might inadv ertently facilitate a form of tacit
collusion across the platform. The concern is that algorithmic pricing , especially in an inﬁnite game
setting as interpreted in the context of Folk Theorems, could sust ain cooperation (or collusion) more
easily than in ﬁnite settings. According to these theorems, in inﬁnite ly repeated games, multiple
equilibria—including collusive equilibria—are possible, and the automation of pricing decisions
2

could make such outcomes more likely.
This potential for algorithmic pricing tools to facilitate collusion withou t explicit coordination
between sellers represents a signiﬁcant challenge to traditional an titrust frameworks. It necessitates
a nuanced understanding of how these technologies operate and t heir broader implications for
market structure and consumer welfare.
This study aims to explore these dynamics in depth, using Airbnb’s pric ing tool as a case study.
By empirically examining the tool’s impact on pricing and listing strategies , with a particular focus
on minimum stay requirements, this research seeks to oﬀer insights into the ongoing debate on
competition in digital marketplaces and the role of algorithmic pricing in market outcomes.
2 Literature Review
The rapid digitization of the economy and the advent of algorithmic pr icing mechanisms have
brought about signiﬁcant changes in market dynamics. This literatu re review synthesizes insights
from existing literature with a focus on how these developments impa ct market transparency, com-
petition, and the potential for collusive behavior.
2.1 Digitalization and Enhanced Market Transparency
The digital transformation of the economy has greatly increased t he transparency of market prices.
Retail chains are increasingly posting their prices online, and brick-a nd-mortar stores are adopting
electronic shelf labels, leading to a more dynamic pricing environment. This trend is exempliﬁed
by practices like Tesco’s price matching strategy from 2013 to 2018 , which automatically adjusted
prices at the till to match competitors (The Guardian). These deve lopments, while enhancing
market eﬃciency and consumer information, also create an environ ment conducive to collusion,
as ﬁrms can more easily monitor and respond to competitors’ pricing strategies (Rotemberg and
Saloner, 1986; Green and Porter, 1984).
2.2 Algorithmic Pricing and Market Dynamics
The shift to algorithmic pricing, where prices are set through autom ated tools using data analytics
and machine learning, has profound implications for market dynamics . These tools can potentially
lead to more eﬃcient market responses but also raise concerns abo ut facilitating tacit collusion.
Algorithmic pricing can enable ﬁrms to rapidly adjust to competitors’ prices and market conditions,
potentially leading to anti-competitive outcomes (Salcedo, 2015; Ca lvano et al., 2020; Klein, 2021;
Hansen et al., 2021).
2.3 Empirical Evidence on Algorithmic Collusion
Empirical studies have begun to explore the real-world implications of algorithmic pricing and
collusion. For instance, the publication of ﬁrm-speciﬁc transaction prices in the Danish ready-
mixed concrete market led to decreased price competition (Albaek e t al., 1997). Additionally,
research indicates that gasoline prices in Germany increased signiﬁc antly when local duopolies
adopted algorithmic pricing strategies (Assad et al., 2020). These e xamples highlight the potential
for algorithmic pricing to reduce market competition, even in the abs ence of explicit collusion among
ﬁrms.
3

2.4 Impact of Digital Tools on Market Competition
Digital tools extend beyond pricing algorithms to encompass various aspects of listing and sales
management in marketplaces. The automation of these tasks could lead to strategic shifts from
long-term, stable pricing to short-term, dynamic pricing strategie s. This shift, facilitated by the
reduced cost of managing listings, could encourage more frequent price adjustments, potentially
disrupting traditional market equilibria and leading to collusive outcom es (Varian, H. R., 1980, “A
model of sales,” American Economic Review).
2.5 Algorithmic Pricing and Market Competition
• A growing body of literature examines the impact of algorithmic pricing on market dynam-
ics, with a particular focus on how these tools can inﬂuence competit ive behaviors among
participants.
• One pivotal study in this domain is ”Algorithmic Pricing Facilitates Tacit C ollusion Evi-
dence,” which provides empirical evidence on how algorithmic pricing ca n lead to less aggres-
sive competition, and in some cases, facilitate tacit collusion among ma rket participants.
• This paper’s ﬁndings are particularly pertinent to the current stud y as they oﬀer insights into
how digital tools like Airbnb’s pricing tool might inﬂuence host pricing st rategies, potentially
leading to more uniform and stable prices across listings, which could b e indicative of tacit
collusion.
2.6 Digital Tools in Marketplaces
• The role of digital tools in shaping market competition is an emerging ar ea of interest. These
tools can increase market eﬃciency and transparency but also rais e concerns about potential
anti-competitive behaviors.
• The insights from ”Algorithmic Pricing Facilitates Tacit Collusion Evidenc e Full” are in-
strumental in understanding the dual nature of these tools, high lighting the need for careful
examination of their impact in various market contexts, including plat forms like Airbnb.
2.7 Antitrust Concerns in the Digital Era
The rise of algorithmic pricing poses new challenges for antitrust and competition policy. Traditional
antitrust frameworks, based on human decision-making, may need to be adapted to account for the
potential of algorithms to facilitate tacit collusion without explicit coo rdination. This necessitates a
nuanced understanding of how these technologies operate and th eir broader implications for market
structure and consumer welfare (Cr´ emer, J., de Montjoye, Y. A., Schweitzer, H., 2019, “Competition
Policy for the Digital Era,” Report for the European Commission).
3 Research Questions
This study aims to explore the nuanced implications of Airbnb’s pricing t ool and its impact on
market dynamics, focusing particularly on the frequency of marke t interaction, changes in listing
characteristics, and potential anti-competitive behaviors:
4

1. Correlation Between Market Interaction F requency and Pric ing Strategies:
• How do Airbnb hosts’ minimum stay requirements, as an indicator of m arket interac-
tion frequency, correlate with their pricing strategies, particular ly in response to market
dynamics? This question seeks to understand the broader relation ship between the fre-
quency of hosts’ interactions with the market and their approach es to pricing, especially
in the context of evolving market conditions.
2. Behavioral Impact of Airbnb’s New Pricing T ool:
• How does the introduction of Airbnb’s dynamic pricing tool inﬂuence t he overall pricing
behavior of hosts across various minimum stay requirements? This q uestion explores the
general impact of the tool on hosts’ pricing strategies, assessin g whether its implemen-
tation encourages more competitive pricing or trends towards tac it collusion, without
explicitly focusing on hosts’ operational strategies or market inte raction frequency.
3. Utilization of Airbnb’s Pricing T ool and Its Impact on Hosts ’ Pricing Decisions:
• Considering the availability of data on price changes and the limitations faced by fully
booked hosts, how does the introduction of Airbnb’s pricing tool inﬂ uence the pricing
decisions of hosts who are able to adjust their prices? This question aims to apply
a Regression Discontinuity Design (RDD) approach to assess the ca usal impact of the
pricing tool on hosts’ pricing behaviors. Special attention will be giv en to comparing
hosts who changed their prices with those who couldn’t due to full bo okings, providing
insight into the tool’s impact under diﬀerent operational constraint s.
4. New Pricing T ool and Host Size Dynamics in Airbnb:
• How does Airbnb’s new pricing tool aﬀect the pricing strategies of sm all (fewer/smaller
listings) versus large (more/larger listings) hosts, especially regar ding their capacity to
adjust prices in the context of varying booking statuses (fully boo ked vs. available)?
• Diﬀerential Price Adjustment Strategies : This study will analyze how small and
large hosts diﬀerentially adjust their prices in response to the pricin g tool, focusing on
their relative booking occupancy levels. It will explore whether smalle r hosts, due to
potentially lower booking volumes, are more agile in adapting their pricin g strategies
compared to larger hosts who may possess less ﬂexibility but greate r market inﬂuence.
• Inﬂuence of Booking Status on Pricing : Assess the impact of booking status (fully
booked vs. available) on hosts’ ability to utilize the pricing tool eﬀect ively. This analysis
will highlight how the ability to adjust prices varies between small and la rge hosts,
providing insights into the operational dynamics inﬂuenced by host s ize.
• Economic Implications of Size and Flexibility : The research will delve into the
economic implications of host size on pricing ﬂexibility and market respo nsiveness. It
aims to understand how diﬀerent-sized market participants levera ge technological tools
in response to policy changes, aligning with Industrial Organization p rinciples.
• Methodological Approach : Employ Regression Discontinuity Design to discern the
causal impact of the pricing tool on small and large hosts. The stud y will compare hosts
with the ability to adjust prices (due to availability) against those who cannot (being fully
5

booked) across both host categories. This approach provides a c omprehensive analysis of
the policy’s impact across diﬀerent segments within Airbnb’s market s tructure, factoring
in both size and operational constraints.
5. New Pricing T ool Impact on New vs. Established Hosts in Airbn b:
• How does the introduction of Airbnb’s dynamic pricing tool diﬀerentia lly impact the
pricing strategies and market behaviors of new versus established hosts, particularly in
terms of reputation dynamics and competitive equilibrium in the platfo rm’s marketplace?
• Diﬀerential Impact on Host Segments : This part of the study will investigate the
varied responses of new hosts (less experienced, potentially less r eputed) and established
hosts (with a solid presence and customer base) to the dynamic pric ing tool.
• Adaptation to Pricing Algorithms : Assess the adaptation mechanisms in pricing
strategies among new and established hosts in response to the too l. The focus will be on
whether the tool facilitates faster adaptation and competitive st rategies for newer hosts
and how it complements the market experience of established hosts .
• Reputation and Game Theory Dynamics : Explore the strategic role of reputation,
framed within game theory, post-implementation of the pricing tool. This analysis will
consider how reputation inﬂuences the pricing decisions of hosts an d whether the tool
mitigates or ampliﬁes existing reputation disparities between new and established hosts.
• Market Equilibrium and Competitive Dynamics : Analyze the implications of
these diﬀerential impacts for competitive equilibrium on Airbnb. This w ill involve ex-
amining whether the tool fosters a more vibrant and competitive ma rketplace or creates
market imbalances that favor one host segment.
• Methodological Approach : Utilize Regression Discontinuity Design to determine the
causal eﬀect of the pricing tool’s introduction on new and establishe d hosts. The study
will compare pre- and post-implementation pricing strategies and ma rket performance
indicators, while controlling for other inﬂuencing factors.
6. Changes in Listing Characteristics Post-Policy Implement ation:
• How have Airbnb hosts adjusted their listing characteristics, like min imum stay require-
ments, in reaction to the introduction of the new pricing tool? This inq uiry seeks to
understand if changes in operational strategies are a direct resp onse to the tool’s capa-
bilities and market insights.
• Are these strategic adjustments indicative of a shift towards mor e competitive pricing
behaviors, or do they potentially signal a decrease in market divers ity and individuality
among listings?
• Is there a trend towards uniformity in listing features and pricing st rategies among
hosts after the introduction of the tool, hinting at a potential red uction in competitive
diﬀerentiation in the Airbnb market?
7. Assessing Anti-Competitive Behavior and Market Dynamics:
• What are the emerging patterns of pricing behavior among diﬀerent host segments after
the policy implementation, and do these suggest any anti-competitiv e practices such as
tacit collusion?
6

• Does the integration of the pricing tool lead to behaviors like price-ﬁ xing, or do the ob-
served pricing strategies align with competitive market norms, desp ite increased pricing
coordination?
• In what ways has the enhanced transparency and facilitation of pr ice adjustments by the
tool inﬂuenced the competitive dynamics within the Airbnb marketpla ce?
8. Implications for Antitrust Analysis and Market Regulation :
• Given the analyzed pricing behaviors and market responses, what im plications can be
drawn for antitrust analysis in digital marketplaces like Airbnb, espe cially in the context
of algorithmic pricing tools?
• How do the ﬁndings contribute to the discourse on the role of pricing transparency in
fostering competitive integrity versus enabling potential collusion?
• What regulatory considerations or policy recommendations could be derived from the
study, particularly concerning the diverse pricing strategies adop ted by Airbnb hosts in
response to the new pricing tool?
4 Methodology
This study employs a nuanced approach utilizing Regression Discontin uity Design (RDD) and
Propensity Score Matching (PSM) to rigorously analyze the impact o f Airbnb’s newly implemented
pricing tool on host pricing strategies and broader market dynamic s.
4.1 Data Collection and Description
4.1.1 Nature of the Data
• Data collection began quarterly starting from December 5th, 2022 , encompassing 35 cities
across the United States. A global dataset is also available for broa der insights.
• Each data scraping cycle captured the continuous daily price decisio ns for each listing, span-
ning from the date of collection up to 356 days thereafter. This app roach provides a detailed
view into the evolution of dynamic pricing behaviors among hosts.
4.1.2 Content of the Data
• The dataset includes variables such as listing prices, availability, minimu m stay requirements,
host characteristics, and other listing attributes.
• The data cover a period of 3 months before and 9 months after the introduction of Airbnb’s
pricing tool, enabling an assessment of its impact.
• Additional metadata includes reviews, booking rates, and seasona l demand indicators.
• The inclusion of information on listings that were fully booked serves t o enrich the study’s
control group, especially in the RDD analysis.
• Key policy changes from Airbnb that are relevant to the study includ e:
7

– Redesigned Pricing Tools: The integration of various pricing tools within the calendar
interface streamlines the price-setting experience for hosts. Th is enhancement in pricing
transparency could signiﬁcantly inﬂuence hosts’ pricing strategie s. In line with the folk
theorem, which suggests the possibility of multiple equilibria in repeate d games, this
change may lead to a diverse range of equilibrium outcomes in the Airbn b market.
Depending on the hosts’ interactions and strategic choices, thes e outcomes could range
from highly competitive pricing strategies to more cooperative, collu sive approaches.
The ease of adjusting prices, combined with greater market inform ation, provides hosts
with the ﬂexibility to navigate between these equilibria based on their p references and
market conditions.
– Compare Similar Listings: This feature enables hosts to benchmark their pricing against
the average of similar listings in close proximity. While this could lead to mo re compet-
itive pricing by providing hosts with clearer market rate insights, it ma y also instigate
dynamic pricing behaviors akin to the Edgeworth cycle. For instance , a random increase
in one host’s marginal costs might lead others to adjust their prices accordingly. This
could potentially trigger a sequence of price adjustments among ho sts, as each responds
to changes in others’ pricing strategies, ﬂuctuating between com petitive and cooperative
pricing over time.
– Swipe-to-Select and Yearly View in Calendar: The introduction of these features, espe-
cially the yearly view in the calendar, has the potential to signiﬁcantly inﬂuence hosts’
long-term pricing strategies. By oﬀering a more extensive overview of pricing trends
and availability across an extended time frame, these tools could enh ance hosts’ abil-
ity to engage in strategic pricing. From an Industrial Organization p erspective, this
improved visibility and planning capability might lead to heightened price c ompetition
among hosts, as they are better equipped to anticipate market ﬂu ctuations and adjust
their prices more eﬀectively over the long term. On the other hand, it could also facil-
itate a form of tacit collusion where hosts, observing and aligning with broader pricing
trends, might inadvertently stabilize prices at a higher level, reducin g the intensity of
price competition in the market.
4.1.3 Usefulness of the Data
• The detailed nature of the dataset facilitates a granular examinatio n of how pricing strategies
adapt in response to market ﬂuctuations and policy implementations .
• The longitudinal aspect of the quarterly data collection allows for an assessment of persistent
trends and shifts in pricing strategies over time.
• The diversity of geographic locations covered in the dataset ensur es that the ﬁndings are
applicable across a variety of market environments, enhancing the study’s generalizability.
• The inclusion of fully booked listings provides a unique opportunity to e stablish a control
group, enhancing the robustness of the causal inferences draw n from the RDD methodology.
4.2 Regression Discontinuity Design (RDD)
• The RDD approach is utilized to establish a causal relationship betwee n the introduction of
Airbnb’s pricing tool and changes in hosts’ pricing strategies. This m ethodology hinges on the
8

identiﬁcation of a ’cut-oﬀ’ point related to the policy implementation d ate, which is critical
for distinguishing between the treatment and control groups.
• The ’cut-oﬀ’ point for this study is identiﬁed around the early acces s release of the pricing tool
on March 5th, with its broader public availability on May 25th. Listings a ctive and making
price adjustments around these dates are considered the treat ment group, while those not
available for booking due to being fully booked are designated as the c ontrol group.
• To enhance the precision of the analysis, Propensity Score Matchin g (PSM) will be applied to
pair listings in the treatment group with similar listings in the control gr oup. This matching
will be based on characteristics such as listing features, host infor mation, and historical pricing
patterns. PSM allows for a more accurate comparison by ensuring t hat the listings in both
groups are similar in all aspects except for the exposure to the new pricing tool.
• The focus of the RDD analysis will be on assessing both the immediate a nd longer-term
impacts of the pricing tool within the Airbnb market. By comparing th e pricing strategies of
the treatment and control groups over time, the study aims to iso late the eﬀect of the policy
from other external factors.
• This rigorous methodological approach aims to provide clear insights into the causal eﬀects
of Airbnb’s pricing tool on host pricing behavior, oﬀering valuable per spectives on market
dynamics and policy implications.
4.3 Propensity Score Matching (PSM)
4.3.1 Estimating Propensity Scores
• Logistic regression will be employed to estimate the likelihood of each lis ting being available
or fully booked at the time of the introduction of Airbnb’s new pricing t ool.
• The regression model incorporates variables such as location, listin g type, host reputation,
historical pricing patterns, and proximity to the policy implementatio n date to accurately
estimate propensity scores.
4.3.2 Matching Listings and Balancing Groups
• Using the calculated propensity scores, listings from the treatmen t group (those that adjusted
prices post-policy implementation) will be matched with those in the co ntrol group (listings
fully booked and unable to adjust prices).
• Balancing checks, including standardized mean diﬀerences and varia nce ratios, will be con-
ducted to ensure that the treatment and control groups are st atistically similar in observable
characteristics, thereby reducing selection bias.
4.3.3 Addressing Unmatched Listings
• Listings that cannot be adequately matched will either be excluded t o maintain the integrity
of the analysis or subject to separate examination to identify uniqu e attributes or outliers.
• Alternative methods, such as nearest-neighbor matching or calipe r matching, may be em-
ployed to reﬁne the matching process and address any discrepanc ies in the initial matching.
9

4.3.4 Sensitivity Analysis
• Sensitivity analyses will be conducted to evaluate the impact of vary ing matching parameters
and criteria on the study’s ﬁndings.
• These analyses will help in assessing the stability of the results and th e potential inﬂuence of
unobserved confounding variables on the causal inference.
5 Expected Outcomes and Implications
This study aims to provide a comprehensive understanding of the imp acts of Airbnb’s new pricing
tool on market competition:
• Algorithmic Pricing and Market Dynamics : This research will explore how Airbnb’s
pricing tool inﬂuences hosts’ pricing strategies. The focus is on as sessing whether the tool leads
to more coordinated pricing behaviors, potentially reducing price va riability across listings and
contributing to a more uniform market structure.
• Evidence of T acit Collusion : The study will analyze if the usage of Airbnb’s pricing tool
mirrors patterns of tacit collusion observed in other markets with a lgorithmic pricing, as
indicated in referenced papers. Speciﬁcally, it will investigate wheth er the tool fosters less
competitive behavior among hosts, leading to more stable but poten tially higher prices.
• Comparative Analysis : A detailed comparison will be conducted between hosts who adopt
the pricing tool and those who do not. This analysis will shed light on th e diﬀerential impacts
of algorithmic pricing tools on hosts’ pricing decisions and market dyn amics, oﬀering insights
into the extent of competitive versus coordinated behavior.
• Policy Implications: Findings from this study will be critical for informing competition pol-
icy in digital marketplaces. The results will delineate the balance betw een the eﬃciency gains
oﬀered by algorithmic pricing tools and their potential to foster ant i-competitive practices.
This will contribute to the broader discourse on regulating and monit oring digital market
platforms to ensure fair and competitive practices.
The outcomes of this research are expected to enhance the unde rstanding of the role of digital
tools, particularly algorithmic pricing mechanisms, in shaping competit ive dynamics in online mar-
ketplaces. It will provide valuable insights into the balance between m arket eﬃciency and the risk
of collusion, with signiﬁcant implications for market regulation and ant itrust policy.
6 Potential Limitations and Future Research Directions
6.1 Current Study Limitations
This study, while utilizing rigorous methodologies and a comprehensive dataset, acknowledges sev-
eral inherent limitations:
10

• Data Limitations : The quarterly scraped data provides a detailed snapshot of mark et
dynamics, but it may not capture extremely rapid changes or intra- quarter events that sig-
niﬁcantly inﬂuence pricing strategies. This could limit the ability to dete ct more subtle or
immediate responses to market shifts.
• Scope of the Study : The primary focus is on assessing the immediate impacts of Airbnb’s
pricing tool on host pricing behaviors. This approach may overlook lo nger-term market ad-
justments, changes in consumer behavior, and broader economic implications that unfold over
extended periods.
• Methodological Constraints : The RDD and PSM methods are robust statistical ap-
proaches; however, they have inherent limitations in fully isolating th e causal impact of the
pricing tool, particularly regarding potential unobserved confoun ding factors. This could
aﬀect the precision of the causal inferences drawn from the analy sis.
6.2 Directions for Future Research
Given these limitations, future research could explore several ave nues to build upon the ﬁndings of
this study:
• Incorporating High-F requency Data: Future studies could utilize higher-frequency data,
such as daily or weekly scrapings, to capture more granular market dynamics and immediate
responses to policy changes or market events.
• Long-T erm Impact Analysis: Further research could extend the time horizon to examine
the long-term eﬀects of algorithmic pricing tools on market structu res, host behaviors, and
consumer experiences.
• Expanding Methodological Approaches : Employing additional econometric techniques,
such as structural modeling or time-series analysis, could provide d eeper insights and help
address some of the limitations associated with RDD and PSM.
• Broader Market Studies : Expanding the scope to include diﬀerent platforms or geographic
markets could oﬀer comparative insights and enhance understand ing of how digital tools
impact market dynamics across various contexts.
These future research directions can signiﬁcantly contribute to t he evolving discourse on digi-
tal marketplaces, algorithmic pricing, and the balance between mar ket eﬃciency and competitive
integrity.
6.3 Next Research Paper: Demand Estimation and Market Dynam ics
Using the BLP Model
Building upon the ﬁndings of this study, future research could signiﬁ cantly beneﬁt from employing
the Berry, Levinsohn, and Pakes (BLP) demand estimation model in the context of Airbnb’s market.
This approach would enable a more nuanced analysis of both demand a nd supply dynamics:
11

• Demand and Supply Curve Estimation : Utilize the BLP model to estimate demand
and supply curves in Airbnb’s market. This involves analyzing listing cha racteristics, booking
prices, and quantities while accounting for the heterogeneity in con sumer preferences and host
strategies. The model can provide detailed insights into how diﬀeren t factors, such as price,
location, and listing features, inﬂuence consumer choices and host pricing decisions.
• Counterfactual Market Scenarios : Conduct counterfactual simulations to understand
the impact of policy changes on market dynamics. For instance, simu late scenarios where
all listings are mandated to oﬀer instant booking or have a minimum sta y requirement of
one day. Analyze how these policy shifts would aﬀect prices, quantit ies, and overall market
equilibrium. Such simulations can reveal the potential consequence s of diﬀerent regulatory or
platform policy changes.
• Comprehensive Market Analysis : Expand the scope to include a comprehensive analysis
of market competitiveness and eﬃciency. Investigate how change s in listing policies, like
adjustments in minimum stay requirements or the introduction of ne w booking features,
impact the overall market structure and competitiveness.
• Exploring Market Segmentation : Examine market segmentation by categorizing listings
based on various attributes such as price range, location, and typ e. Analyze how diﬀerent
segments respond to market changes and policy interventions, pr oviding a more granular
understanding of the market.
• Policy Implications and Market Design : Utilize the insights gained from these analyses
to oﬀer recommendations for platform policies and market design. T he ﬁndings could inform
strategies to enhance market eﬃciency, foster healthy competit ion, and improve consumer
and host welfare.
• Extended Time Horizon Analysis : Consider extending the time horizon for data collection
and analysis to capture long-term market trends and responses t o policy changes, enriching
the understanding of the market’s evolution over time.
This future research direction, encompassing demand estimation, counterfactual simulations,
and comprehensive market analysis using the BLP model, will compleme nt and extend the current
study’s ﬁndings. It aims to provide a holistic understanding of the co mplex dynamics in digital
marketplaces like Airbnb and oﬀer valuable insights for platform desig n and regulatory considera-
tions.
12
