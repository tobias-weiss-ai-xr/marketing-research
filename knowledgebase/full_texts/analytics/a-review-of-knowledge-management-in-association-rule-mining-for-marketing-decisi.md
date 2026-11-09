---
title: A Review of Knowledge Management in Association Rule Mining for Marketing Decision
url: https://doi.org/10.37649/ajes-25-024
category: analytics
subcategory: review
date: 2026-05
venue: Anbar journal for engineering sciences/Mağallaẗ al-anbār li-l-ʻulūm al-handasiyyaẗ
authors:
- Omar  Bilal Alani
- Mortadha  Mohammed Hamad
source: openalex-oa
pdf_url: https://ajes.uoanbar.edu.iq/ajes/article/download/656/640
pages: 13
chars: 51464
fetched_at: '2026-11-08T17:38:41+00:00'
kb_version: 1
---

# A Review of Knowledge Management in Association Rule Mining for Marketing Decision

Anbar Journal of Engineering Science ( AJES )                                                                                   Vol. 17 , No. 1 (2026) , pp. 1 ~ 13
P-ISSN: 1997-9428; E-ISSN: 2706-7440                                                                                        DOI: https://doi.org/10.37649/AJES-25-024

University  of Anbar
Anbar Journal of Engineering Science
journal homepage:  https://ajes.uoanbar.edu.iq/

* Corresponding author: Omar Bilal Al-Ani;  omar221415@gmail.com   ;  +964-7734585804
A Review of Knowledge Management in Extracting Association Rules
for Marketing Decision-Making
Omar Bilal Al-Aniᵃ, Murtadha M. Hamadᵇ
ᵃComputer Science Department, College of Computer Science and Information Technology, University of Anbar, Ramadi, Iraq
Email: omar221415@gmail.com   ; ORCID: https://orcid.org/0009-0008-8458-3851
ᵇComputer Science Department, College of Computer Science and Information Technology, University of Anbar, Ramadi, Iraq
Email: dr.mortadha61@uoanbar.edu.iq  ; ORCID: https://orcid.org/0000-0001-9919-3217

PAPER INFO

ABSTRACT
Paper h is tory :
Received:   17/07/2025
Revised:     23/02/2026
Accepted:   11/03/2026
Recently, intensive applications of data -driven methods
emerged in marketing decision-making and customer behavior
analysis. Although conventional approaches produced
Association Rules (ARs) from transaction trends, these rules
were frequently overlooked s ince they were extracted
statically and isolated from lifecycle management systems.
Therefore, this study integrated the association rule extraction
technique with a knowledge management framework to
enhance rule quality and ensure long -term utility. The
proposed approach segmented customers based on purchasing
behavior using recency, frequency, and monetary (RFM)
parameters. Following the extraction of these behavioral
features, the K -Means algorithm clustered customers into
distinct segments, including hi gh-volume, new, and moderate
purchasers. To enhance decision -making accuracy and
eliminate irrelevant patterns concealed within transactions,
machine learning models, specifically XGBoost and Isolation
Forest, were deployed to filter out redundant rules. T his
integration of knowledge management enabled continuous
system learning and optimization. Ultimately, the outcomes
demonstrated a substantial positive impact on marketing
decision support, delivering higher-quality, actionable insights
for strategic planning.

K eyw or ds :
Data-Driven Marketing,
Knowledge Management,
Association Rule Mining,
Pattern Discovery,
Marketing Decision Support.

Copyright: ©202 6 by the authors. Submitted for
possible open access publication under the terms
and conditions of the Creative Commons Attribution
(CC BY-4.0) license.
https://creativecommons.org/licenses/by/4.0/

1. Introduction
In today’s data -driven business environment,
organizations increasingly rely on data analysis
techniques to understand customer behavior and
support marketing decision -making. Customer
behavior analysis plays an essential role in
identifying recurring purc hasing patterns and
relationships among products, which can be
utilized in marketing strategies, pricing
optimization, and personalized recommendation
systems. Association Rule Mining (ARM) is one of
the most widely used techniques for discovering
hidden relationships in transactional databases.
Several algorithms have been developed for ARM,
including Apriori, FP -Growth, and Eclat. Among
these, FP -Growth has gained significant attention
due to its efficiency in extracting frequent itemsets
without generating candidate sets. Unlike Apriori,
which repeatedly scans the database to generate
candidate itemsets, FP -Growth constructs a

2                                                                                             Omar Bilal Al-Ani / Anbar Journal of Engineering Science, 17, 1, (2026) 1 ~ 13

A Review of Knowledge Management in Extracting Association Rules for Marketing Decision-Making                                        (Omar Bilal Al-Ani)
compact FP -tree structure that reduces
computational complexity and improves mining
performance [1]  , [2]  . These techniques have been
successfully applied in various marketing
applications. For example, Yanti et al. (2024)
utilized FP -Growth on retail transaction data to
generate purchasing rules that improved
promotional planning and product placement
strategies [3]  . Similarly, Kajornkasirat et al. (2025)
applied ARM techniques to customer datasets and
derived association rules that enhanced customer
experience and increased sales performance [4] .
Despite the effectiveness of ARM techniques, the
extracted rules are often large, complex, and
difficult to interpret directly for practical decision -
making. Most existing studies focus mainly on rule
extraction as a standalone analytical process while
neglecting the role of Knowledge Management
(KM) in organizing, maintaining, and utilizing the
generated knowledge. In many cases, association
rules become outdated or less valuable when they
are not systematically managed, updated, and
integrated into organi zational knowledge
processes [5] .
Knowledge Management provides mechanisms for
capturing, organizing, sharing, and maintaining
knowledge generated from analytical systems.
Integrating KM with ARM can significantly improve
the practical value of extracted association rules by
transforming r aw analytical outputs into
structured and reusable organizational knowledge.
Several recent studies highlight the importance of
this integration. For instance, Yanti et al. (2024)
demonstrated how ARM -based customer
relationship insights can support market ing
strategies, while Kajornkasirat et al. (2025) showed
that customer segmentation rules managed
through knowledge -oriented processes contribute
to business growth and customer satisfaction [4] .
However, there is still a lack of comprehensive
review studies that systematically examine the
integration of Knowledge Management and
Association Rule Mining within marketing decision
support systems. Therefore, this paper aims to
review and analyze the current state of research on
KM–ARM integration in marketing applications.
The study seeks to identify existing research
trends, challenges, and opportunities, as well as to
clarify how KM practices can enhance the
effectiveness and sustainability of ARM -based
marketing decisions.

2.  Theoretical Background
As marketing becomes more and more data-driven
and intelligent, it is more important than ever to
comprehend the theoretical frameworks that guide
marketing decisions.  People don't just make
decisions based on gut feelings or past experiences
anymore. They a lso use advanced analytics to find
patterns in massive data and turn them into useful
information.  So, it is becoming more and more
important to combine knowledge management
approaches with association rule mining
techniques. This is because this combinat ion gives
firms a knowledge base that helps them make
better and longer-lasting marketing decisions
2.1 Knowledge Management (KM)
In 2023, Idris and a group of individuals presented
a specific definition of knowledge management,
stating, "Knowledge management is the ability to
manage information, which includes obtaining
knowledge from multiple sources, both external
and internal, an d then transforming it into new
strategies and innovative ideas, then applying and
storing them." In other words, they obtain data
sources, whether external or internal, and then
transform this data into knowledge, applying it, and
then storing it. Knowled ge management enables
organizations to collect, organize, and efficiently
store knowledge assets. [6] . It is the primary way
in which companies and organizations produce
knowledge. They acquire, organize, store,
disseminate, and use it effectively to support
strategies, enhance decision -making, and improve
organizational performance. Knowledge
management i s concerned with making the tacit
knowledge of individuals explicit, so that it can be
shared and used throughout the organization to
stimulate innovation, prevent the repetition of
previous mistakes, and increase responsiveness to
market changes [7] . Knowledge management
consists of three main components: people,
processes, and technology. People are the creators
and users of knowledge [45]. Processes are the
activities that capture, store, update, and apply
knowledge in decision -making [46]. Techno logy
provides the tools and platforms that enable us to
store, share, and access knowledge [47] . Together,
these three transform knowledge into a sustainable
asset for the organization.

Omar Bilal Al-Ani / Anbar Journal of Engineering Science, 17,1, (2026) 1 ~ 13                                                                                              3

AJES   P-ISSN: 1997-9428  ; E-ISSN: 2706-7440                                                                                                  https://ajes.uoanbar.edu.iq/

Figure 1. Components of Knowledge Management [8] .
The above triangular diagram illustrates the three
fundamental components of knowledge
management: people, process, and technology. The
model proposes that successful knowledge
management is attained by the balance of these
components: people generate and share
knowledge, processes structure it, and technologies
provide access to it. This equilibrium is the key to
sustainable and successful knowledge flow in
organizations [8] .

The types of knowledge that are essential to
knowledge management include tacit, procedural,
and explicit knowledge. These types are
particularly important in marketing decisions, and
each plays a significant and distinct role in
capturing, organizing, and  applying information.
The following is an overview of these three basic
types of knowledge.

A – Explicate Knowledge
Knowledge that can be effectively documented and
stored (e.g., policies, manuals, and documents), and
easy to share and transfer. It is also known as
discerptible knowledge and is widely used in
content management systems and enterprise
portals [9].
B - Implicit / Procedural Knowledge
Also known as "practical knowledge" or "know -
how." It is not documented knowledge but can be
acquired and applied through training or
observation. It is often used as the basis of
employee training and the development of skills
based on their acquired experience [10].
C – Tacit Knowledge
Deeper and more complicated than tacit
knowledge; personal knowledge that is based on
experience and context, and cannot be easily
formulated or directly transferred. Said by Nasab to
account for over 90% of knowledge in
organizations and usually transferred through
practice and informal coordination [11].
2.2 Knowledge Management Processes
The figure illustrates the basic processes of
knowledge management within an integrated cycle.
It begins with knowledge creation and acquisition,
then moves through the stages of capture, sharing,
storage, and application, concluding with the
evaluation st age to ensure continuous
improvement. This representation reflects the
circular nature of knowledge flow within
organizations to support learning, innovation, and
decision-making [12] .

Figure 2. The Knowledge Management Process Cycle [12] .
A-Knowledge creation and acquisition
It involves training as many people as possible who
already possess the same profession through
practical training, so that the knowledge stored in
one person is transformed into distributed
expertise for those who have been trained [12] .
B-Knowledge sharing
is the learning process that occurs through people
collaborating with and helping each other to
develop themselves and acquire new knowledge
[12].

4                                                                                             Omar Bilal Al-Ani / Anbar Journal of Engineering Science, 17, 1, (2026) 1 ~ 13

A Review of Knowledge Management in Extracting Association Rules for Marketing Decision-Making                                        (Omar Bilal Al-Ani)
C – Knowledge Capture
means converting tacit knowledge in individuals'
minds into explicit knowledge that can be written
down or documented [12].
D – Knowledge Store
refers to knowledge repositories such as databases,
documents, or reports that store knowledge for
future use [12].
E – Knowledge Application
Using the knowledge created and captured in
various educational or practical situations [12].
F – Knowledge Evaluation
The process of examining and evaluating existing
knowledge to ensure it is accurate and relevant to
the topic or need [12].
2.3 Association Rule Mining (ARM)
Association Rule Mining (ARM) is a pattern
discovery technique used in large databases to
extract correlations between items within a set of
transactions. It aims to identify rules of the type "if
X happens, then Y is likely to happen," which helps
analyze consumer behavior or uncover hidden
correlations in data. It is a cornerstone of shopping
cart analysis and data-driven marketing [13] .
2.3.1 Common Algorithm using in ARM
These three algorithms are important algorithms in
association rules, as they differ in their form and
structure for analyzing customer behavior, which
makes choosing one of them an important matter
for extracting useful rules and applying them.
Among the most important of these three
algorithms are Apriori, FP -Growth, and ECLAT, as
each of them relies on different search and
processing mechanisms.
A – Aproiri
This algorithm is based on the idea that if a set of
elements is rare, then all individual branches are
also rare. The algorithm starts by searching and
finding duplicate individual elements, then
gradually builds with a larger set of elements,
where it scans the data elements repeatedly, which
makes it slow on large data. Therefore, it is suitable
for medium and small data due to its
simplicity.[14].
B – FP-Growth
FP-Growth outperforms Apriori by avoiding
candidate generation. It builds a compact structure
called an FP-Tree to store data efficiently. Frequent
patterns are then extracted using a divide -and-
conquer strategy.As a result, it is much faster and
more memo ry-efficient, especially with large
atasets [14] .
C – Eclat
Eclat takes a different approach by storing a list of
transactions for each item (TID list). It calculates
support using set intersections instead of scanning
the dataset repeatedly. It applies depth-first search
and works well with dense datasets. However , it
may become slow or memory -heavy with very
large or sparse data [14] .
2.4 KM and ARM Integration
Knowledge management (KM) involves processes
for creating, sharing, and using an organization’s
knowledge assets to achieve strategic goals [16].
Data mining – including association rule mining
(ARM) – discovers patterns and correlations
hidden in large data repositories, effectively
turning raw data into actionable knowledge. For
example, Shettigar et al. note that data mining
“enabling organizat ions to discover hidden
knowledge and relationships in their data” is
crucial for supporting effective KM and decision -
making [17] . In practice, many organizations “lack
the ability to learn from historical data” and thus
miss opportunities to reuse existing knowledge
[16]. Integrating ARM with KM addresses this gap
by capturing discovered patterns (association
rules) as explicit knowledge in KM systems,
ensuring that insights (e.g. co -purchase rules or
usage patterns) are recorded, managed, and
applied rather than lost. In this way, ARM becomes
a component of the knowledge discovery process:
data mining is “a process leading to the analysis and
use of large datasets to extract valuable insights
and the resulting knowledge” [18], and KM
provides the framework to store and exploit these
insights in decision support.

Omar Bilal Al-Ani / Anbar Journal of Engineering Science, 17,1, (2026) 1 ~ 13                                                                                              5

AJES   P-ISSN: 1997-9428  ; E-ISSN: 2706-7440                                                                                                  https://ajes.uoanbar.edu.iq/
Table 1. Comparative Analysis of Apriori, FP-Growth, and Eclat
Algorithms [15]
Aspect Apriori FP-
Growth
Eclat
Data
Representation
horizontal
layou
Also uses
horizontal
layout but
transforms
into a
compressed
tree (FP -
Tree).
Employs
vertical
format using
transaction
ID (TID) lists
for each item.
Candidate
Handling
Generates
all
possible
candidate
itemsets
level by
level.
Avoids
candidate
generation
through
tree-based
pattern
extraction.
No candidate
generation;
relies on
intersection
of TID lists.
Database Scans Requires
multiple
full
database
scans—
one per
iteration
level.
Only two
full scans:
one to
count, one
to build the
FP-tree.
Requires
fewer scans;
works with
in-memory
TID list
intersections.
Execution
Efficiency
Slower on
large or
dense
datasets
due to
candidate
explosion.
Highly
efficient
and
scalable,
especially
with dense
or large
datasets.
Performs
well on dense
data; less
efficient on
sparse or
huge
datasets.
Memory
Consumption
Can be
high due to
candidate
generation
and
support
counting.
Optimized
memory use
via FP -tree
structure.
Memory
usage
depends on
size of TID
lists and
dataset
density.
Application Best used
for closed
item
sets.
Used in
cases of
large data
Best used for
free item
sets

2.5 Applications of Association Rule Mining
(ARM) in Marketing
ARM is used in fraud detection, retail studies, and
recommendation systems. It is a data mining
method for extracting rules from big data and is
also important for decision support systems due to
its ability to identify important rules [19] .

Figure  3. Application of ARM in Marketing [19]
The above diagram shows the main and important
applications of Association Rule Mining (ARM) in
marketing. ARM is widely used to analyze customer
purchasing behavior (market basket analysis),
detect suspicious patterns (fraud detection),
improve customer r ecommendations
(recommender systems), and segment customers
based on their purchasing habits (customer
segmentation). These applications help companies
make informed, data -driven marketing decisions.
The application in Marketing is :

1 - Market Basket Analysis
It is widely used to know what items customers buy
most frequently. For example, if a customer buys
milk, he often buys bread with it. This method helps
us to know several things, including understanding
how to arrange products inside the store. We can
also know how to display cross -selling offers. For
example, we make an offer that says buy a
calculator and get a certain mouse at half price. We
also control inventory management so that a
product that is related to other products does not
run out. [20] .

2 – Recommendations System
Retailers leverage association rules (ARM) to build
a profile for each customer based on their past
purchase characteristics and preferences. If a
customer purchases the first product, the system
suggests a second product based on their previous
preferences. These recommendations enhance

6                                                                                             Omar Bilal Al-Ani / Anbar Journal of Engineering Science, 17, 1, (2026) 1 ~ 13

A Review of Knowledge Management in Extracting Association Rules for Marketing Decision-Making                                        (Omar Bilal Al-Ani)
customer satisfaction and contribute to increased
sales [21].

3 – Detection of fraud
ARM is also used to detect fraud and identify
abnormal patterns, enabling organizations to
monitor any abnormal or anomalous cases and
issue a warning by examining transaction data
[22] .
4 – Customer Segments
The ARM system also segments customers based on
the nature of their purchases, enabling businesses
to manage their plans accordingly. For example,
customers with high incomes are offered discounts
or better offers [23] .

3. Literature Review
In recent years, there has been increased interest in
integrating knowledge management and
association rules extraction in the field of
marketing. Many studies have addressed how
relying on data and the knowledge management
process can improve the effectiveness of marketing
decision-making [24].
In 2023, Zhao  [31] developed a decision support
system (DSS) based on knowledge extracted from
data mining techniques. This system helped
improve sales forecasting accuracy, but it did not
directly utilize association rule extraction
algorithms and did not address structure d
customer knowledge, which justifies a gap in rule -
based knowledge.
Saura (2021) [32]. conducted a broad survey on
machine learning and data science applications in
digital marketing, identifying ARM as a core
technique for market basket analysis and consumer
behavior understanding. However, his review
emphasized technical tools and lacked i ntegration
with KM frameworks or knowledge reuse
strategies.
In 2025, Gupta  [33]. used the fuzzy rules model.
The model's objective was to understand customer
preferences and also improve system accuracy.
This study did not focus on knowledge storage from
a knowledge management perspective and focused
only on algorithmic and technical aspects.
In 2023, Saeed and others [34]. presented a
conceptual model for the knowledge management
lifecycle in financial institutions. Despite the
comprehensiveness of their proposed framework,
it has not been tested in marketing fields. In 2025,
Hunyadi .[35] compared the Aproiri and FP-Growth
algorithms using real data from e -commerce
websites. Their study found that FP -Growth was
more efficient at extracting rules. While their
Although previous research has provided valuable
insights and valuable ideas, it hasn't organized and
stored these rules as usable knowledge for the long
term. These studies have shown that knowledge
management is a crucial component of marketing,
but some  focus on integrating knowledge
management with the extraction of correlational
rules and the proper reuse of that extracted
knowledge. Currently, there is a lack of integration
between knowledge management and correlational
rule extraction, leading to gaps in this area.

3.1 Literature Analysis
Previous studies conducted between 2020 and
2025 reveal a growing interest in integrating
knowledge management and association rule
mining to improve marketing decision -making.
While association rule mining techniques have
been used for a long time, their synergy with
knowledge management systems remains limited
and often superficial.
Association Rule Mining (ARM) algorithms are
frequently used in studies to uncover patterns that
can be practically exploited, such as purchasing
behavior or product bundling strategies. For
example, Gupta et al. (2025) used the Fuzzy ARM
algorithm to impr ove recommendation systems in
e-commerce platforms, while Hunyadi et al. (2025)
demonstrated the effectiveness of the FP -Growth
algorithm in analyzing large transaction databases.
These studies emphasize the pivotal role of ARM in
extracting marketing knowledge.
The integration and reuse of knowledge
management remains incomplete. While Saura and
Chauli (2023) described systems that generate
valuable insights, they did not link these In 2023,
Saeed proposed a knowledge management
framework that also incorporates correlation rule
extraction. While tested in the financial sector, its
effectiveness in marketing has not been proven.
Many previous studies extract data only once and
use static data, limiting the extraction of strategic
insights. None of these studies included
mechanisms for updating, maintaining, storing, or
reusing the discovered rules.
In general, recent studies show promising potential
for integrating correlation rule extraction (ARM)
with knowledge management (KM). However, this
integration has been limited. Therefore, rules

Omar Bilal Al-Ani / Anbar Journal of Engineering Science, 17,1, (2026) 1 ~ 13                                                                                              7

AJES   P-ISSN: 1997-9428  ; E-ISSN: 2706-7440                                                                                                  https://ajes.uoanbar.edu.iq/
should not only be extracted but also organized,
stored, updated, and reused. This will ensure the
sustainability of this knowledge and its ability to
adapt to rapid market changes.

4. Result and Discussion
 This section provides an overview of the findings
from other research regarding the combination of
knowledge management and the extraction of
correlation rules. Recent literature shows that the
extraction of correlation rules has become an
utmost necessary  task, especially regarding the
understanding of customers’ behavior and
purchasing patterns. The findings from other
studies, such as those by Gupta (2025) and Hunyadi
(2025), have shown that correlation rules
extraction algorithms and fuzzy rules have a  great
role to play in the success of e-commerce. However,
the findings from Said (2023) have shown that
though the application of the frameworks, such as
the framework by Said (2023), may seem limited to
other sectors rather than the marketing sector, the
findings from other studies, such as Saura (2021)
and Schole (2023), have shown the importance of
deriving insights from the data. Nonetheless, the
findings have not shown the importance of the use
or transfer of the data within the boundaries of
knowledge management. This failed amalgamation
of the two concepts regarding the use of the
findings from the research will limit the importance
of the findings from the research. The data analyzed
from the research provides findings only once
without going into c ycles such as storage or
repeated use. This will provide an indication that
though the extraction from the databases provides
great powers of analysis. Therefore, the results
collectively suggest that future marketing decision
support systems should move beyond rule
extraction and focus on managing ARM outputs as
evolving knowledge assets, enabling sustainable,
adaptive, and knowledge -driven marketing
strategies.

5. Gaps Identified
Despite the growing interest in integrating
association rule mining (ARM) with knowledge
management (KM) in the fields of marketing and
business intelligence, studies still reveal clear
shortcomings. Shaw et al. (2025) point out that
most research treats k nowledge management and
data analytics as two separate fields, emphasizing
the weak integration between knowledge
management practices and big data analytics
initiatives [25]. In other words, the extracted
association rules are rarely linked to a coherent
knowledge management framework as the
knowledge acquired is often isolated from
organizational knowledge repositories.
In general, association rule mining is typically
applied once to a historical dataset, resulting in a
static set of rules. This approach results in these
rules quickly becoming outdated as new data
arrives (early studies noted that mining is
performed "onc e and only once" on a static
database). Few studies address the flow of rules or
their real -time updating, and thus the extracted
knowledge cannot adapt to changes in the market
or ever-changing customer behavior  [5] .
On the other hand, many of the results of ARM are
not organized or linked within formal knowledge
management (KM) frameworks. For example,
Selamat et al. (2020) demonstrated that
organizations do not effectively leverage tacit
knowledge (the accumulated ex pertise of
individuals) and often rely on traditional IT
systems for KM. This means that most ARM
applications focus on explicit and visible data, such
as customer profiles, while neglecting the deeper
expertise within the organization. Consequently,
the d iscovered rules remain isolated from the
broader knowledge assets within the organization,
limiting their usefulness in supporting decision -
making [26].
There are also conceptual models without
application. One recurring gap is that many
proposals for integrating knowledge management
and association rule mining remain at the
conceptual level, lacking empirical validation. This
essentially calls for "an innovative assessment plan
for knowledge management and knowledge
governance" to ensure the usability of the
generated knowledge, as stated by Selmat et al.
[26]. In other words, although many frameworks
and structures have been proposed, only a few have
been applied or tested in real-world settings. Shaw
et al. (2025) point out that knowledge management
and business models are often presented without
case studies  or prototypes, meaning that the
practical synergy between knowledge management
processes and ARM algorithms remains unproven
[25]. In summary, recent studies consistently point
out that KM –ARM integrations are hampered by
static, one -off rule extraction; insufficient
structuring of knowledge (especially tacit
knowledge); lack of real -time updates; and the
prevalence of unvalidated co nceptual models.

8                                                                                             Omar Bilal Al-Ani / Anbar Journal of Engineering Science, 17, 1, (2026) 1 ~ 13

A Review of Knowledge Management in Extracting Association Rules for Marketing Decision-Making                                        (Omar Bilal Al-Ani)
Addressing these gaps – for example by developing
adaptive, knowledge-driven ARM systems with live
feedback loops – is a clear direction for future
research.

6. Future Research Opportunities
Based on the gaps in current research we have
examined, this study proposes a conceptual
framework that integrates knowledge management
and association rule extraction into the context of
marketing decision -making. This framework aims
to address the major limitatio ns of previous
studies, particularly the lack of knowledge
structuring, the extraction of consistent rules, and
the limited integration of organizational knowledge
repositories.

Figure 4. A Proposed Framework for Integrating Knowledge
Management with Association Rule Mining Using RFM and
Machine Learning Techniques
The proposed framework (Figure 4) starts from the
preprocessed dataset, which involves removing
duplicates and entails many other details. Next
comes the second phase, which involves calculating
RFM features: recency, frequency, and monetary
value. Then, the features undergo clustering based
on K -Means to segregate customers and further
involves the application of ARM to identify patterns
based on the behavior of the customers. However,
to aid better accuracy in predictions, the proposed
framework involves the use of XGBoost as an
additive predictive model. Based on all details that
emerge from all phases, the structured, interpreted,
and organized knowledge acquisition and handling
is facilitated by the Streamlit knowledge
management module. Finally, all ou tput results are
included in the NoSQL database (MongoDB), and all
outputs can be accessed in the future and remain
prospective. But another phase has been
introduced, and that involves feedback. The
proposed framework involves an incorporated
feedback mechanism that aims to re-enter updated
details about knowledge and insights derived from
the ARM and XGBoost module to the Streamlit KM
module.

7. Equations
This section presents the mathematical formulas
used in the proposed framework. The model
integrates the Recency, Frequency, and Monetary
Value (RFM) scoring system to describe customer
behavior, followed by K -MEANS clustering
techniques and the extraction  of association rules
from them. Equations are presented to determine
how to calculate RFM scores, along with other
analytical steps that support customer
segmentation and rule extraction. These formulas
form the basis for building marketing knowledge
and guiding decision-making processes.
First, we calculate the recency, frequency, and
monetary value of each customer.
Support is a way to find out how often an item or
group of objects shows up in a data set. In other
words, support is the number of transactions that
have a certain set of items divided by the total
number of transactions. The rule is more important
and can be used in more situations if it has greater
backing [27].

Support(X⇒Y)
𝑵𝒖𝒎𝒃𝒆𝒓 𝒐𝒇 𝒕𝒓𝒂𝒏𝒔𝒂𝒄𝒕𝒊𝒐𝒏𝒔 𝒄𝒐𝒏𝒕𝒂𝒊𝒏𝒊𝒏𝒈 𝒃𝒐𝒕𝒉 𝑿 𝒂𝒏𝒅 𝒀
𝑻𝒐𝒕𝒂𝒍 𝒏𝒖𝒎𝒃𝒆𝒓 𝒐𝒇 𝒕𝒓𝒂𝒏𝒔𝒆𝒄𝒕𝒊𝒐𝒏𝒔               (1)
Then we calculate confidence, which is the
probability that product Y will be purchased by
customers who previously purchased product X,
and it expresses the strength and value of the
association rule [27].

Confidence(X⇒Y) =
𝝈(𝑿∪𝒀)
𝝈(𝑿)                                       (2)
σ here is Represents the number of occurrences or
Support Count of a particular element in
association rules.
Then (Lift) measures the strength of the
relationship between X and Y compared to the
random probability. If it is greater than 1, it
indicates a positive relationship, and if it is less than
1, it indicates a negative relationship.

Omar Bilal Al-Ani / Anbar Journal of Engineering Science, 17,1, (2026) 1 ~ 13                                                                                              9

AJES   P-ISSN: 1997-9428  ; E-ISSN: 2706-7440                                                                                                  https://ajes.uoanbar.edu.iq/
Lift(X⇒Y) =
𝑪𝒐𝒏𝒇𝒊𝒅𝒆𝒏𝒄𝒆(𝑿⇒𝒀)
𝑺𝒖𝒑𝒑𝒐𝒓𝒕 ( 𝒀 )                                         (3)
These equations are used to calculate recency,
frequency, and monetary value, then apply the k -
means algorithm, extract the association rules, and
store them in a special database.

8. Illustrative Case Study of the
Proposed Framework
To illustrate the practical applicability of the
proposed Knowledge Management –Association
Rule Mining (KM –ARM) framework, an illustrative
case study based on a retail marketing scenario is
presented. In this scenario, customer transactional
data are first  preprocessed to compute Recency,
Frequency, and Monetary (RFM) metrics, which are
then used to segment customers into homogeneous
groups using K -Means clustering. This
segmentation step ensures that customer
behavioral differences are captured before the rule
mining process.
Subsequently, the FP -Growth algorithm is applied
within each customer cluster to extract cluster -
specific association rules that reflect purchasing
patterns more accurately than global rule
extraction. The discovered rules are then stored
within a structur ed knowledge base, enabling
knowledge organization, reuse, and continuous
refinement over time. Marketing decision makers
can utilize this stored knowledge to support actions
such as product bundling, personalized
promotions, and customer retention strategies.

9.  Enhancing the Proposed Framework
with Intelligent Models
Integrating machine learning into the following
application enhances the marketing decision -
making process. For example, the XGBOOST
classifier can be used to determine which group a
new user belongs to upon entering the system,
based on their behavior. It can be trained by taking
user behavior as its input and then classifying these
users into which group they belong. For example, if
a person makes frequent purchases, they will be
classified as a frequent purchaser and will be
shown special offers. In addi tion, an algorithm like
Isolate Forest can be used to isolate outliers. For
example, if a customer buys sugar and then buys
tea, this is not considered an outlier because the
criteria, such as trust, support, and boost, are equal
in magnitude and are also strong. However, if they
buy tea and then, by chance, buy clothes, the
correlation between these criteria is not strong,
and this is considered an outlier because the
criteria are not equal. This particular purchase is
random over  a whole year, for example , unlike
purchases like tea and sugar within the same year.

10.  Research Contributions
This research is dedicated to realizing a long -term
process where rules mined from data are converted
into reusable knowledge. The major contributions
can be listed below:
1. A method incorporating the extraction of
correlation rules with the management of
knowledge for more intelligent decision -making in
marketing, ensuring rules are relevant for more
than the point of their creation.
2. Segmentation of the customers is done through
an analysis of the monetary value for every
customer, frequency of purchase, and recency,
thereafter clustering the profiles using K -Means
before the rules are generated from the framework.
3. For every identified cluster, the FP -GROWTH
algorithm is utilized to find the rules specific to that
particular cluster, unlike finding all the rules
simultaneously. This prevents fragmentation and
undistinguishable rules, and the phenomenon of
“rule explosion,” which has existed in the previous
studies.
4. The use of a special database is specifically
geared toward the capacity to store these extracted
rules, as opposed to extracting rules for a single use.
5 _ Develop a control panel using Python, similar to
Streamlet, to support marketing decisions.

11.  Conclusion
This study emphasizes the need for the integration
of knowledge management and the extraction of
correlation rules for informed marketing decisions.
This comes with the realisation that this attempt
will be more successful compared to the earlier
extraction that took place for a limited period of
time without the integration of the information
within the knowledge lifecycle. The findings from
the study will be summarized below.
1. According to the studies analyzed in this
research, it has been evident that most studies
undertook the extraction of correlation rules for
short-term durations without taking into
consideration the integration of knowledge
management.

10                                                                                            Omar Bilal Al-Ani / Anbar Journal of Engineering Science, 17, 1, (2026) 1 ~ 13

A Review of Knowledge Management in Extracting Association Rules for Marketing Decision-Making                                        (Omar Bilal Al-Ani)
2. The proposed method integrates correlation rule
extraction by using FP growth, the k -means
clustering algorithm, and customer behavior study.
The method also retains, reuses, and adjusts these
rules in order to present a complete model for
making long-term marketing strategies.
3. The integration of knowledge management with
correlation rules extraction, storage, and efficient
management helps to make accurate marketing
decisions.
4. Association rules management in a knowledge
base improves recommendation quality and
facilitates creating better strategies for marketing.
5. Future studies should emphasize the creation of
dynamic systems that can continuously update and
verify knowledge bases to keep up with the
developing consumer behavior and market trends.

12. Summary of Techniques and
Findings in Related Work
In some previous studies where correlation rules
were extracted, Liao et al. (2015) used the Aproiri
algorithm with user clustering to extract
knowledge from social network data and online
purchases. They showed that user behavior
improves marketing decisi ons, although the reuse
of knowledge was limited to analytical
interpretation only [28] . Zekic-Soshak and Haas
(2015) used the FP-Growth model within an online
marketing system and showed that extracting sets
of recurring elements can support marketing
strategy formulation when combined with the
underlying knowledge management layer, but
without dynamic f eedback or rule evolution [29].
Esteratt and Lalich (2017) applied Apriori ARM to
sales transaction data to support decision -making
in the automotive retail sector, where the extracted
rules were treated as fixed organizational
knowledge rather than as part of the ongoing
knowledge management lifecycle [30].

Table 2. Summary of Reviewed Studies Integrating KM and ARM in Marketing
Gap Identified Key Finding Dataset Method Used Year Author(s)
Relies on historical structured
data; does not integrate
association-rule analysis or
unstructured customer
knowledge.
Data-driven marketing system combining
data mining with neural networks (BP)
achieving 85% accuracy in sales
forecasting .
Simulated
sales data
(Chinese
company)
Data‐mining
DSS (BP
neural net)
2023
Zhao, X.
& Li, C .
[31]]
Focus is on methods, not on
managing organizational
“knowledge”; does not propose
combining ARM with a KM
framework for marketing .
A review of the use of data science in
marketing identified ARM as an essential
tool for market basket analysis and
marketing analytics methods .
Literature
(digital
marketing
cases)
Data-science
in Digital
Marketing
(Survey of
ML/ARM
techniques)
2021
Saura, J.
R
 [32] .
Tested on static datasets; lacks
dynamic/real-time integration.
Did not evaluate integration
with a knowledge base or
experts’ input .
Proposed a fuzzy ARM framework for
live-stream e -commerce. Fuzzy logic
refines association patterns, improving
recommendation relevance and consumer
engagement. Extracted knowledge (e.g.
consumer preferences) is more nuanced
with fuzzy rules .
E-
commerce
live-
streaming
data
(public
dataset)
Fuzzy
Association-
Rule Mining
2025
Gupta, N.
et al
[33] .
Focused on finance domain;
the framework is conceptual
and has not been validated on
marketing data. KM processes
are generic (e.g. codification)
but specific marketing
applications are not addressed.
Outlined a KM–data-science lifecycle for
FinTech firms. In the “discovery” phase,
association-rule mining is used to uncover
interdependencies among features.
Demonstrated how ARM can reveal
hidden patterns in transactional data for
customer insights .
Financial
services
(FinTech)
data
KM + Data
Analysis
Framework
(incl. ARM)
2023 Saeed, T. et al.[34]
Study focuses on algorithm
efficiency, not on capturing or
using domain knowledge. Does
not address how discovered
rules are managed as
“marketing knowledge” or
integrated into decision
processes.
Empirical comparison: FP -Growth
outperforms Apriori for large -scale
shopping data. This yields faster and more
memory-efficient rule mining in
marketing contexts. Provides practical
guidelines (tooling in RapidMiner) for
selecting ARM techniques in e-commerce .
Real e -
commerce
transaction
logs
Comparative
ARM
(Apriori vs.
FP-Growth)
2025
Hunyadi,
I. D. et
al.[35]

Omar Bilal Al-Ani / Anbar Journal of Engineering Science, 17,1, (2026) 1 ~ 13                                                                                              11

AJES   P-ISSN: 1997-9428  ; E-ISSN: 2706-7440                                                                                                  https://ajes.uoanbar.edu.iq/
Nomenclature
     Column A      Column B
X ,Y Two related items appear together in a single purchase.
σ here is Represents the number of occurrences or Support Count of a particular element in association rules.
ARM Association rules mining
KM Knowledge management
FP-Growth Frequent Pattern Growth
Apriori A Priori Algorithm
Eclat Equivalence Class Transformation
RFM Recency, Frequency, Monetary
ML Machine Learning
AI Artificial inelegant

Funding
None
Acknowledgements
The author would like to thank his supervisor and
the Department of Computer Science, University of
Anbar, for their guidance and support.
Conflicts of Interest
The authors declare no conflict
Appendix
 Appendixes appear after acknowledgments.
References

[1] R. Yanti, P. N. Maradjabessy, Q. Qurtubi, and I.
P. Rachmadewi, “Determining the retail sales
strategies using association rule mining,”
International Journal of Advances in Applied
Sciences, vol. 13, no. 3, p. 530, Sep. 2024, doi:
10.11591/ijaas.v13.i3.pp530-538.
[2] I. D. Hunyadi, N. Constantinescu, and O. -A.
Țicleanu, “Efficient Discovery of Association
Rules in E -Commerce: Comparing Candidate
Generation and Pattern Growth Techniques,”
Applied Sciences, vol. 15, no. 10, p. 5498, May
2025, doi: 10.3390/app15105498.
[3] R. Yanti, P. N. Maradjabessy, Q. Qurtubi, and I.
P. Rachmadewi, “Determining the retail sales
strategies using association rule mining,”
International Journal of Advances in Applied
Sciences, vol. 13, no. 3, p. 530, Sep. 2024, doi:
10.11591/ijaas.v13.i3.pp530-538.
[4] S. Kajornkasirat, P. Gunglin, K. Puangsuwan,
and N. Kaewsuwan, “Customer segmentation
using association rule mining on retail
transaction data,” IAES International Journal
of Artificial Intelligence (IJ-AI), vol. 14, no. 3, p.
1919, Jun. 2025, doi:
10.1109/ACCESS.2025.3573807.
[5] A. Veloso, B. Wagner, and M. Carvalho,
“Knowledge Management in Association Rule
Mining,” Dec. 2001.
[6] H. Idrees, J. Xu, S. A. Haider, and S. Tehseen, “A
systematic review of knowledge management
and new product development projects:
Trends, issues, and challenges,” Journal of
Innovation & Knowledge , vol. 8, p. 100350,
Mar. 2023, doi: 10.1016/j.jik.2023.100350.
[7] M. Alavi and D. E. Leidner, “Review:
Knowledge Management and Knowledge
Management Systems: Conceptual
Foundations and Research Issues,” MIS
Quarterly, vol. 25, no. 1, p. 107, Mar. 2001, doi:
10.2307/3250961.
[8] B. Gunjal, “Knowledge Management: Why Do
We Need it for Corporates,” Malaysian Journal
of Library & Information Science , vol. 10, Dec.
2005, doi: 10.2139/ssrn.3375572.

12                                                                                            Omar Bilal Al-Ani / Anbar Journal of Engineering Science, 17, 1, (2026) 1 ~ 13

A Review of Knowledge Management in Extracting Association Rules for Marketing Decision-Making                                        (Omar Bilal Al-Ani)
[9] F. Nickols, “The knowledge in knowledge
management,” The Knowledge Management
Yearbook 2000-2001, pp. 12–21, Jan. 2000.
[10] E. A. Smith, “The role of tacit and explicit
knowledge in the workplace.” [Online].
Available: http://www.emerald -
library.com/ft
[11] J. Oranga, “Tacit Knowledge Transfer and
Sharing: Characteristics and Benefits of Tacit
& Explicit Knowledge,” Journal of Accounting
Research, Utility Finance and Digital Assets ,
vol. 2, pp. 736 –740, Oct. 2023, doi:
10.54443/jaruda.v2i2.103.
[12] K. Hołowińska, “E -learning as an Extending
Tool of Knowledge Management,” 2021, pp.
59–66. doi: 10.1007/978-3-030-85001-2_5.
[13] Data Mining . Elsevier, 2012. doi:
10.1016/C2009-0-61819-5.
[14] A. Sharma and A. Ganpati, “Association Rule
Mining Algorithms: A Comparative Review,”
Jan. 2022.
[15] A. Sharma and A. Ganpati, “ASSOCIATION
RULE MINING ALGORITHMS: A
COMPARATIVE REVIEW,” International
Research Journal of Engineering and
Technology, 2021, [Online]. Available:
www.irjet.net
[16] R. Pawlak, P. Wyrozębski, I. Pietras, and J.
Parys, “The Use of Machine Learning in
Enhancing Data and Information
Management Processes in the Context of
Knowledge Management,” e-mentor, vol. 108,
no. 1, pp. 52 –62, Mar. 2025, doi:
10.15219/em108.1694.
[17] R. Shettigar, D. Bhise, B. Bandgar, and S.
Madhavedi, “Data Mining Application In
Effective Knowledge Management: An
Empirical Study,” International Journal of
Food and Nutritional Sciences , vol. 11, pp.
2285–2296, Dec. 2022.
[18] R. Pawlak, P. Wyrozębski, I. Pietras, and J.
Parys, “The Use of Machine Learning in
Enhancing Data and Information
Management Processes in the Context of
Knowledge Management,” e-mentor, vol. 108,
no. 1, pp. 52 –62, Mar. 2025, doi:
10.15219/em108.1694.
[19] Data Mining . Elsevier, 2012. doi:
10.1016/C2009-0-61819-5.
[20] A. B. Rao, J. S. Kiran, and P. G, “Application of
market–basket analysis on healthcare,”
International Journal of System Assurance
Engineering and Management , vol. 14, no. S4,
pp. 924 –929, Dec. 2023, doi:
10.1007/s13198-021-01298-2.
[21] H. Ko, S. Lee, Y. Park, and A. Choi, “A Survey of
Recommendation Systems: Recommendation
Models, Techniques, and Application Fields,”
Electronics (Basel) , vol. 11, no. 1, p. 141, Jan.
2022, doi: 10.3390/electronics11010141.
[22] M. Seera, C. P. Lim, A. Kumar, L. Dhamotharan,
and K. H. Tan, “An intelligent payment card
fraud detection system,” Ann Oper Res , vol.
334, no. 1 –3, pp. 445 –467, Mar. 2024, doi:
10.1007/s10479-021-04149-2.
[23] K. Tabianan, S. Velu, and V. Ravi, “K -Means
Clustering Approach for Intelligent Customer
Segmentation Using Customer Purchase
Behavior Data,” Sustainability, vol. 14, no. 12,
p. 7243, Jun. 2022, doi: 10.3390/su14127243.
[24] W. A. Wahab and S. A. Rahman, “A Brief
Review on the Knowledge Management and
Data Mining for Marketing Decision,”
International Journal of Academic Research in
Business and Social Sciences , vol. 8, no. 9, Oct.
2018, doi: 10.6007/IJARBSS/v8-i9/4588.
[25] S. V. Tsiu, M. Ngobeni, L. Mathabela, and B.
Thango, “Applications and Competitive
Advantages of Data Mining and Business
Intelligence in SMEs Performance: A
Systematic Review,” Businesses, vol. 5, no. 2, p.
22, May 2025, doi:
10.3390/businesses5020022.
[26] S. A. Mohd Selamat, S. Prakoonwit, and W.
Khan, “A review of data mining in knowledge
management: applications/findings for
transportation of small and medium
enterprises,” SN Appl Sci , vol. 2, no. 5, p. 818,
May 2020, doi: 10.1007/s42452-020-2589-3.
[27] R. Agrawal, T. Imieliński, and A. Swami,
“Mining association rules between sets of
items in large databases,” ACM SIGMOD
Record, vol. 22, no. 2, pp. 207 –216, Jun. 1993,
doi: 10.1145/170036.170072.

Omar Bilal Al-Ani / Anbar Journal of Engineering Science, 17,1, (2026) 1 ~ 13                                                                                              13

AJES   P-ISSN: 1997-9428  ; E-ISSN: 2706-7440                                                                                                  https://ajes.uoanbar.edu.iq/
[28] S.-H. Liao, P. -Y. Hsiao, C. -W. Li, and Y. -F. Lin,
“Mining Marketing Knowledge to Explore
Social Network Sites and Online Purchase
Behaviors,” Applied Artificial Intelligence , vol.
29, no. 7, pp. 697 –732, Aug. 2015, doi:
10.1080/08839514.2015.1051892.
[29] M. Zekić -Sušac and A. Has, “Data Mining as
Support to Knowledge Management in
Marketing,” Business Systems Research
Journal, vol. 6, no. 2, pp. 18–30, Sep. 2015, doi:
10.1515/bsrj-2015-0008.
[30] V. Istrat and N. Lalić, “Creating a Decision -
Making Model Using Association Rules,”
Applied Artificial Intelligence , vol. 31, no. 5 –6,
pp. 538 –553, Jul. 2017, doi:
10.1080/08839514.2017.1378301.
[31] R. Hou, X. Ye, H. B. O. Zaki, and N. A. B. Omar,
“Marketing Decision Support System Based
on Data Mining Technology,” Applied Sciences,
vol. 13, no. 7, p. 4315, Mar. 2023, doi:
10.3390/app13074315.
[32] J. R. Saura, “Using Data Sciences in Digital
Marketing: Framework, methods, and
performance metrics,” Journal of Innovation &
Knowledge, vol. 6, no. 2, pp. 92 –102, Apr.
2021, doi: 10.1016/j.jik.2020.08.001.
[33] H. Liao, “E -commerce Live -Streaming
Platform and Decision Support System Based
on Fuzzy Association Rule Mining,”
International Journal of Computational
Intelligence Systems, vol. 18, no. 1, p. 41, Feb.
2025, doi: 10.1007/s44196-025-00744-4.
[34] G. Pisoni, B. Molnár, and Á. Tarcsi, “Knowledge
Management and Data Analysis Techniques
for Data-Driven Financial Companies,” Journal
of the Knowledge Economy , vol. 15, no. 3, pp.
13374–13393, Nov. 2023, doi:
10.1007/s13132-023-01607-z.
[35] I. D. Hunyadi, N. Constantinescu, and O. -A.
Țicleanu, “Efficient Discovery of Association
Rules in E -Commerce: Comparing Candidate
Generation and Pattern Growth Techniques,”
Applied Sciences, vol. 15, no. 10, p. 5498, May
2025, doi: 10.3390/app15105498.
