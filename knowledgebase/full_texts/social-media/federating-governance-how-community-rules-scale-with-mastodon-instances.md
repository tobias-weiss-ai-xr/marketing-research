---
title: 'Federating Governance: How Community Rules Scale with Mastodon Instances'
url: https://arxiv.org/abs/2606.05069
category: social-media
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Rasika Muralidharan
- Yong-Yeol Ahn
- Bao Tran Truong
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.05069
pages: 28
chars: 101314
fetched_at: '2026-11-08T12:58:08+00:00'
kb_version: 1
---

# Federating Governance: How Community Rules Scale with Mastodon Instances

Federating Governance: How Community Rules Scale with Mastodon Instances∗
RASIKA MURALIDHARAN,Luddy School of Informatics, Computing, and Engineering, Indiana University, USA
YONG-YEOL AHN,University of Virginia, USA
BAO TRAN TRUONG,Center Synergy of Systems, TUD Dresden University of Technology, Germany
The rise of decentralized social media platforms like Mastodon and Bluesky highlights the challenge of scaling self-governance and
moderation. As communities grow, they face new issues that demand increasingly complex governance structures. However, as
moderation is mainly volunteer-driven, there is limited formal guidance on how community rules and moderation practices should
evolve with growth. This study investigates how moderation scale with Mastodon instances by analyzing community rules across
servers of varying sizes. We categorize these rules to identify key governance priorities and find that these priorities are remarkably
consistent across instance sizes: rules addressing problematic content, such as harassment, hate speech, and illegal content, dominate
regardless of scale. While smaller communities focus on narrower sets of topics, larger servers maintain a more balanced coverage of a
broad range of topics. Our analysis of rule formalization reveals that community size strongly predicts rule development. As instances
grow, their rules become more extensive and topically diverse, but also exhibit lower readability and linguistic diversity. In contrast,
external federation interactions have a limited role, mainly associated with a broader scope of rules without substantially affecting
their diversity or form. These findings highlight the relative influence of internal versus external factors, suggesting that local scaling
pressures outweigh network-level dynamics in decentralized social media governance. The scaling pattern observed on Mastodon
resemble those previously identified on centralized platforms such as Reddit, suggesting that community size imposes fundamental
constraints on self-governance that transcend platform architectures.
CCS Concepts:•Human-centered computing→Collaborative and social computing.
Additional Key Words and Phrases: online communities; community rules; Mastodon
ACM Reference Format:
Rasika Muralidharan, Yong-Yeol Ahn, and Bao Tran Truong. 2026. Federating Governance: How Community Rules Scale with Mastodon
Instances. InProceedings of ACM SIGCHI Conference on Computer-Supported Cooperative Work & Social Computing (CSCW ’26).ACM,
New York, NY, USA, 28 pages. https://doi.org/XXXXXXX.XXXXXXX
1 Introduction
Balancing platform safety with constructive participation is a longstanding and unresolved problem in social media
governance [21, 71, 72]. Major centralized platforms such as X [78], YouTube [23], and Meta [53] increasingly depend
on automated moderation systems built around globally defined policies that are enforced uniformly across diverse
user populations. These systems tend to focus on ostensibly universal content categories—such as unlawful content,
∗Our repository, including code and data, is available at https://github.com/Rasikamurali/MastodonModeration.
Authors’ Contact Information: Rasika Muralidharan, rasimura@iu.edu, Luddy School of Informatics, Computing, and Engineering, Indiana University,
Bloomington, Indiana, USA; Yong-Yeol Ahn, yyahn@virginia.edu, University of Virginia, Charlottesville, Virginia, USA; Bao Tran Truong, baotruon@iu.edu,
Center Synergy of Systems, TUD Dresden University of Technology, Dresden, Germany.
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not
made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components
of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on
servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.
©2026 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Manuscript submitted to ACM
Manuscript submitted to ACM 1
arXiv:2606.05069v2  [cs.SI]  4 Jun 2026

2 Muralidharan et al.
incivility, hate speech, and harassment—that are assumed to be universal across all users and communities. While this
approach enables moderation at scale, it privileges mainstream norms and may overlook diverse cultural norms, values,
and forms of expression used by minority and marginalized groups [8, 24, 34, 49].
In response to these limitations, decentralized social media platforms such as Mastodon and Bluesky have gained
prominence, renewing interest in community self-governance. These platforms distribute authority across independently
operated servers (i.e., “instances”), each self-governed by locally defined rules. Instances coexist within a network,
forming a polycentric governance model that allows both local autonomy and cross-community interactions. Instances
may choose to interoperate (i.e., “federating”), restrict, or sever connections with one another (i.e., “defederation”). As a
condition of federation, communities agree to a minimal set of basic norms, such as prohibitions of hate speech, a model
characterized by prior work as “covenantal federalism” [33]. While decentralized governance addresses some of the
shortcomings of centralized platforms—particularly their failure to account for contextual and diverse norms [10]—it
does not resolve scalability, which remains a central concern for moderation [22].
As a community grows, moderators are faced with not only increased volumes of content, but also more diverse
sets of users and problematic behaviors [29, 48]. At the same time, they need to coordinate within larger moderator
teams [3]. Even on comparatively well-resourced centralized platforms, moderators report burnout, inconsistency in
enforcement, and the need for additional automated support. Studies of moderators on Facebook Groups [ 41], and
Reddit moderators [9, 11, 27, 50] document these challenges. On Mastodon, these challenges are amplified as moderation
is almost entirely volunteer-driven. Moderation workloads thus grow without proportional increases in monetary or
organizational resources such as tools or standardized training. This creates a natural setting to test whether governance
scaling patterns observed in centralized platforms—which can invest in moderation infrastructure as they grow—also
emerge in systems where communities must adapt independently.
Federation further complicates moderation at scale. Beyond enforcing local norms, effective moderation in federated
networks requires balancing these norms with those introduced through federation [43]. Each instance must continually
articulate and renegotiate existing and emerging norms, as users routinely participate across multiple interconnected
communities and may adopt norms that conflict with those of their home instances [ 82]. As the network grows,
moderators increasingly face decisions about inter-instance relationships including federation, defederation, and
content filtering. Understanding how moderation functions under these conditions is essential both for sustaining
decentralized, volunteer-driven systems and for informing how self-governance could adapt in environments where
communities are highly interconnected.
Community rules are a key component of self-governance. Rules formalize norms and guide moderation decisions
such as curating content, developing new guidelines, and managing conflicts [73]. As a record of accepted social practices,
written rules align the understandings of members and moderators about expected behaviors [38]. Referencing rules can
further reinforce shared norms [7, 14]. Educating about the rules is an effective moderation strategy to deter problematic
users [6] on Twitch, and increase rule compliance as well as positive participation on Reddit [31]. At the same time, rules
do not fully capture how governance is enacted: in practice, enforcement may diverge from formal policy depending
on context and discretion [ 52]. Nevertheless, because rules are publicly visible, persistent, and comparable across
communities, they offer a valuable lens for examining self-governance at scale—particularly in decentralized systems
where other governance signals are often inaccessible or inconsistent.
Across platforms, larger, older, and more engaging communities tend to have more extensive rule sets and more
moderation activities [3, 19]. This pattern may reflect both selection effects—where communities with formalized rules
are more resilient to abuse—and adaptation effects, where growth introduces new challenges, such as information
Manuscript submitted to ACM

Federating Governance: How Community Rules Scale with Mastodon Instances 3
overload and decreased interaction quality [55] that necessitate more formal governance [80]. In this work, we draw on
Star and Ruhleder to conceptualize rules as governance artifacts that surface otherwise backgrounded coordination work
under conditions of infrastructural strain, such as changes in community size [75]. We examine how the characteristics
of community rules vary across Mastodon instances of different sizes to understand how self-governance adapts under
changing organizational conditions, while recognizing that rules represent only one facet of broader governance
processes.
Prior research has documented how rules formalize with community growth on centralized platforms like Reddit [19],
where platforms can invest in moderation infrastructure as communities scale. However, it remains unclear whether
these patterns hold in decentralized, volunteer-driven systems where each community must independently address
scaling challenges without centralized resources or coordination. This gap is significant: if scaling dynamics differ
in federated systems, it would suggest that governance tools developed for centralized platforms may not transfer
effectively; if they are similar, it would indicate fundamental constraints on self-governance that transcend platform
architecture.
We systematically analyze rule variation across instances to examine how moderation practices scale in decentralized
social media. We ask the following research questions:
Q1:How do moderation priorities on Mastodon vary with community scale?
Q2:How is community scale associated with rule formalization, such as scope and lexical features?
Q3:To what extent do rules reflect internal needs versus external federation interactions?
Our study builds on earlier work that categorized community rules on Mastodon [56], extending both the scope and
analytical depth. We introduce a large-scale, multi-lingual dataset with 28,910 rules across 6,660 instances of size one to
over two million. Unlike existing research that focuses only on popular, large, English-speaking Mastodon instances,
our dataset allows us to analyze rules across the entire active ecosystem, including small communities that are often
preferred by those seeking support, such as LGBT communities [82]. This rich dataset allows us to examine scaling
behaviors that would be otherwise obscured in other smaller or instance-limited samples, enabling a comprehensive
view growth dynamics and coordination on Mastodon.
Using this dataset, we make three contributions. First, we show that governance priorities are remarkably consistent
across instance sizes: rules addressing harassment, hate speech, and illegal content dominate regardless of scale,
suggesting normative convergence even within a decentralized ecosystem. Second, we demonstrate that scaling patterns
observed in centralized platforms—where larger communities develop more extensive but less readable rules—persist
in volunteer-driven, decentralized environments, even without monetary incentives or centralized support. This
finding suggests fundamental constraints on self-governance that transcend platform architecture. Third, we find that
rule formalization is primarily associated with internal community size rather than external federation interactions,
indicating that local scaling pressures outweigh network-level dynamics in shaping governance practices.
2 Related work
Ample work has established that decentralization empowers community self-governance, that moderation strategies
must adapt as communities scale, and that rules tend to formalize and proliferate as communities grow or encounter
new challenges. Yet, how these dynamics unfold in federated, volunteer-moderated platforms like Mastodon remains
under-explored. By analyzing Mastodon communities of varying sizes, our work connects these threads and fills a
Manuscript submitted to ACM

4 Muralidharan et al.
gap in understanding how rules evolve and formalize in decentralized contexts. In this section, we discuss previous
literature and set the stage for our inquiry into Mastodon’s moderation.
Decentralization and Community Self-governance.Elinor Ostrom demonstrated that communities can effectively self-
regulate common-pool resources without centralized control, guided by design principles such as clearly defined
boundaries, participatory rule-making, and nested governance [59, 60]. Drawing on Ostrom, early research on online
communities—such as Kollock and Smith’s work on “virtual commons”—showed how communities manage shared
spaces through collective norms and self-enforcement [ 37]. Herring further illustrated how early forums and chat
groups developed their own codes of conduct and mechanisms for upholding norms [26]. In the context of Wikipedia,
studies on decentralized governance also found that communities can create and enforce complex rule systems when
granted autonomy [17].
Decentralized social platforms such as Mastodon embody these self-governance ideals by design. Each instance em-
ploys local governance, with administrators tailoring rules to fit their community’s values, fostering diverse cultures and
social dynamics [4, 29, 42, 67, 82, 84]. This heterogeneity makes decentralized ecosystems a great setting for examining
“governable spaces”—infrastructures that empower community agency and participatory norm enforcement [46, 69].
Most governance research to date has focused on single-platform ecosystems like Reddit or Wikipedia or on policy
decisions made by centralized corporate platforms [ 15, 21, 64]. Scholars are now beginning to adapt governance
frameworks to decentralized settings. For instance, the concept of multi-level governance—spanning platform-level
protocols, community-level rules, and individual behavior—is increasingly applied to study the complex power dynamics
in federated systems [33].
Scaling of Moderation Strategies in Online Communities.Institutional theory suggests that as groups grow in size and
complexity, informal norms are increasingly codified into formal rules to reduce ambiguity and maintain stability [70].
From a social identity perspective, larger communities also heighten the need for clear boundaries and behavioral
expectations, making formalized rules an important mechanism for reinforcing shared identity [2]. Empirical work
by prominent scholars on online communities such as Preece and Seering has shown that the age of a community
can influence governance: over time shared norms are created, and social capital accumulates, which in turn shapes
formalization of rules [62, 71]. Mahony and Ferraro further highlight a direct link between community age and increasing
formality and stability of its rules [57]. This body of work suggests that community size and age is a critical explanatory
factor in understanding the formalization and development of community rules.
On many platforms, the burden of moderation falls to volunteers. Seering et al. highlight how Twitch and Reddit rely
on volunteers as the first line of governance, reflecting a “many communities, many local governors” model within a
broader system [72]. Klonick similarly describes volunteer moderators as part of the “new governors” of online speech,
wherein private platforms and their user moderators collectively create a multi-layered governance structure [36].
As communities expand, the challenge of moderation grows and moderators should increasingly rely on a combination
of social and technical strategies. Nakandala et al., showed that as Twitch channels grow in popularity, moderation
becomes more difficult to scale effectively: objectifying and gendered content is common in high-visibility channels
but rare in less popular ones, illustrating how the popularity (scale) of the channels can erode community norms and
moderation system that works for much smaller channels [54]. Lampe and Resnick’s analysis of Slashdot’s distributed
moderation system provided early evidence that community-based rating and meta-moderation can support large-scale
moderation [44]. Community rule formalization is another tool to enhance moderation transparency and communication,
Manuscript submitted to ACM

Federating Governance: How Community Rules Scale with Mastodon Instances 5
as echoed in moderation strategies across case studies of Twitch [6] and Reddit [31]. Indeed, many large online forums
have adopted templates for removal reasons or “user education” messages, institutionalizing this strategy [71].
Federated platforms like Mastodon rely even more on volunteer-driven models, where moderation is guided by local
norms, inter-instance agreements, and optional tools [29]. Unlike centralized platforms such as Facebook, X, and Reddit,
scaling moderation on Mastodon is not simply a matter of increasing automation or expanding moderation teams.
Instead, the community-led, volunteer-driven approach faces inherent cognitive and organizational constraints. As
communities grow, higher post-to-moderator ratios can diminish moderation effectiveness, impacting user satisfaction
and perceptions [81]. Social cognitive theory suggests that managing relationships, including those online, is limited
by cognitive capacity [12, 13]. Consequently, as communities scale, informal rules often evolve into more structured
governance to address increasing complexity [80]. Our work builds on the “community self-moderation” research put
forth by Seering et al. [71], examining how Mastodon’s decentralized nature constrains moderator management in the
absence of centralized oversight.
Evolution and Formalization of Community Rules.The evolution of community rules is shaped not only by growth in
size but by the ways communities interact with one another. As groups expand over time, mechanisms of reciprocity
and reputation weaken [ 28, 61], a pattern especially prevalent in online communities where anonymity is valued.
Thus, while informal, trust-based systems may suffice in small groups, larger communities depend on increasing
formalization, including designated roles, written rules, and structured moderation to sustain cohesion [20]. Smith’s
study of MicroMUSE, a 1990s educational MUD, documents how governance shifted from openness to formal gatekeeping
in response to disruptive growth [74]. Kraut and Resnick frame this transition in terms of community life cycles, noting
that documented policies and official roles become necessary as shared understanding wanes with scale [39]. Previous
research shows that interacting communities often observe what each do and adopt, borrow, adapt and/or discard rules
accordingly [51]. Taken together, prior research suggests that the size of a community and its degree of federation
might play a critical role in shaping Mastodon’s rules.
Herring and others show that governance evolves not only structurally but linguistically: informal norms enacted
through discourse eventually give way to codified rule language as communities grow [26]. Related work has explored
how rule types and linguistic structure must adapt for effectiveness at scale [5, 18, 19], and that larger communities
tend to adopt more standardized, systematic linguistic systems [63, 83]. However, the relationship between scaling of
moderation and participation is more nuanced. Stricter moderation can improve content quality but at the same time
introduce barriers to entry that might deter participation and inclusivity [39, 65, 66].
These insights highlight the role of well-crafted rules that are clear, readable, and context-sensitive as one solution
to bridge these challenges Our study contributes to this line of work by empirically analyzing how Mastodon instance
rules vary in topic coverage, length, formality, and readability as a function of community size and age, offering insight
into the evolution of rule structures in decentralized, volunteer-moderated platforms.
3 Data
Data for this study was collected in August 2024 using the instances.social API, which covers all Fediverse platforms.
Starting from 15,571 candidate instances, we retained only Mastodon instances that returned at least one rule via the
Mastodon API (see Appendix B for filtering details). Three outlier instances were removed upon manual inspection
(see Appendix B). We also excluded mastodon.social from our analysis as it is the only instance with over 10 million
users and, as the “default” instance, it may deviate from patterns observed in organic instances. For these instances,
Manuscript submitted to ACM

6 Muralidharan et al.
100 101 102 103 104 105 106
Instance Size
10 4
10 3
10 2
10 1
100
CCDF
100 101 102 103 104 105 106
Instance Size
100
101
102
103
104
105
Federating Number
100 101 102 103 104 105 106
Instance Size
100
101
102
103
104
105
106
Statuses
100 101 102 103 104 105 106
Instance Size
100
101
102
103
104
105
Logins
Fig. 1. Descriptive statistics of all Mastodon instances (a) Complementary cumulative distribution (CCDF) of instance size. Scatter
plots of various activity metrics against instance size: (b) the number of federations, (c) the number of weekly statuses, and (d) the
number of weekly logins. Orange dots represent the bootstrapped average and 95% confidence interval (CI) for log bins of 5.
the following metadata was collected: Instance ID, Instance Name, User Count, short Description, and status flags
indicating whether the instance is active (see Appendix B). As a result, our sample contains 6,660 instances across the
size spectrum with 28,910 rules.
Although moderation is local, federation exposes users to external content, increasing moderation demands. As
instances connect to more diverse communities, dissonant content becomes more likely, raising the burden of boundary
decisions such as defederation or bans [32, 82]. To capture the role of federation degree in shaping moderation complexity,
we used the Mastodon API to collect the following information: federation degree (number of federating connections)
and weekly activity data, including numbers of statuses, logins, and new accounts during the week of October 14–28,
2024.
Figure 1 visualizes the descriptive statistics for the instances in our dataset, showing a heavy-tailed distribution of
instance sizes. Activity levels, measured by the number of federations, the number of weekly statuses, and the number
of weekly logins increase exponentially.
Non-English rules account for a third of the dataset. We translated all non-English rules to English using Google
Translate and validated translation quality via back-translation and readability comparison (see Appendix B).
Manuscript submitted to ACM

Federating Governance: How Community Rules Scale with Mastodon Instances 7
4 Methods
4.1 Rule Categorization
We systematically analyze the topics of rules present across Mastodon instances to understand how communities
formalize community norms. Each rule may be assigned multiple rule topics. For a clearer comparative analysis, we
group the rule topics into four broader thematic categories—Action, Behavior, Content, and Distribution—based on
their functional focus.
For rule topic analysis of the rules, we randomly sample 1,100 unique rules and perform inductive coding. We find that
85% of these rules align with the rule types defined in the framework developed by [56], indicating substantial overlap
between our emergent codes and their taxonomy. However, we modify this taxonomy to best fit our needs. This includes
the removal of “Prescriptive” and “Restrictive” topic. In practice, these two topics were frequently conflated—many rules
framed as restrictions also implicitly prescribed behavior (e.g., “Do not post hate speech” vs. “Respect others”), making
it difficult to reliably distinguish between them. This ambiguity weakens their analytical utility and compromises
inter-coder reliability. By collapsing these topics, we retain a sharper conceptual boundary across rule topics and
reduce noise in our analysis of rule scope. We also eliminate certain topics that are too granular or ambiguous in
definition and are covered by other topics such as “Politics” and “Low-quality Content”. Using the annotated dataset
from Nicholson et al. [56], which contains 690 rules from top Mastodon instances labeled with one or more topics,
we develop a few-shot prompt to enable large language models (LLMs) to perform multi-label rule classification. We
select few-shot prompting for its reproducibility and effectiveness in multi-label tasks [ 76]. We test the prompt on
GPT-3.5-turbo and GPT-4o-mini, with GPT-4o-mini achieving the highest accuracy of 76%, measured by comparing
model-generated and manual annotations on a per-rule basis. Details about the prompts and the variants used for
testing are mentioned in Appendix E. We use this validated prompt to classify 28,910 rules in our full dataset.
To assess whether linguistic redundancy in rule phrasing could influence topic distributions, we conduct an additional
robustness test wherein we deduplicate highly similar rules within each instance using a text similarity threshold
using Jaccard Similarity. Repeating the topic analysis on this deduplicated dataset yields substantively similar results,
indicating that our findings are not driven by stylistic variation or differences in how instances segment their rules (see
Appendix D).
We adapt the Action, Behavior, Content, Distribution (ABCD) framework [58] to group the rule topics in Mastodon
instances (Table. 1). The framework, originally created for understanding platform policies for influence operations,
clearly identifies the five following categories: “Action”: operations through accounts, “Behavior”: tactics used on the
platform, “Content”: messages, narratives and subject matter, “Distribution”: reach of content and techniques including
but not limited to duplicate accounts for re-posting and “Effects”: actual consequences. We refine the framework to
suit our analysis. First, we eliminate the “Effects” category as this requires analysis of moderation actions which is
beyond the scope of the paper. Of the 19 rule topics we have, some mapping was straightforward. For instance, “Hate
Speech”, “Illegal Content” naturally belong in the Content category, while “Spam” and “Reposting/ Crossposting” belong
in Distribution. For rule topics whose categories are ambiguous, we use a bigram co-occurrence matrix to decide
how moderators might interpret the rules in practice. We use a simple tf-idf with bigrams and inspect the occurrence
map to observe which rules coincide. For example, “Copyright/ Piracy” could be a Content rule type but it occurs
with “Advertising and commercialization” which belongs in the Distribution category, thus “Copyright/ Piracy” is also
categorized under the Distribution section.
Manuscript submitted to ACM

8 Muralidharan et al.
4.2 Rule Diversity
To measure rule diversity, which we define as the amount of variety among the categories of rules within a given
instance, we use entropy. Entropy is a well-established measure of uncertainty or diversity in a distribution, making it
well-suited to quantify how evenly rules are distributed across different categories. A higher entropy value indicates a
more balanced and diverse rule set, while lower values suggest a concentration in fewer categories. Let𝑝𝑖 denote the
proportion of rules in category𝑖(where𝑖∈{𝐴,𝐵,𝐶,𝐷}for the four categories). The entropy𝐻is calculated as:
𝐻ABCD =−
𝑄∑︁
𝑖=A,B,C,D
𝑝𝑖 log2𝑝𝑖
We map each rule to one of four categories: Action, Behavior, Content, and Distribution. Since we use a base-2
logarithm and there are four categories, the entropy ranges from 0 (no diversity; all rules fall into one category) to 2
(maximum diversity; rules are evenly distributed across all four categories). The number and variety of rule categories
allude to the scope of rule formalization that instances of different sizes account for.
Table 1. Categories of Mastodon rules
Category Rule Topic Example % Instances
Action Automated toolsBots need instances admin approval2.24
Behavior
HarassmentDo not engage in harassment of any kind.11.58
DoxxingNo harassment, dogpiling or doxxing of other users5.54
Brigading/DogpilingNo harassment, dogpiling or doxxing of other users1.14
Impersonation No impersonation of individuals, public figures, or organizations
unless clearly marked as parody.
1.57
Trolling ABSOLUTELY NO TROLLING! This instance has ZERO TOLER-
ANCE for trolls!
1.44
Content
Hate Speech Hate speech is not tolerated. This includes but is not limited to
racism, sexism, homophobia, transphobia, classism, ableism, etc.
18.03
NSFW No explicit (NSFW) content without content warnings or sensitive
media markers. Must not appear in avatars or headers.
8.31
Content Warnings Use content warnings for text, images, video, and links appropri-
ately.
7.09
Illegal ContentAbide by the law. No illegal content whatsoever.9.99
Incitement of ViolenceNo incitement of violence or promotion of violent ideologies.5.95
Mis/Disinformation /Con-
spiracy
No spreading of mis/disinformation or conspiracy content.5.46
ImagesNo explicit sexual or violent images.5.25
Off-topic/Topic SpecificKeep posts relevant to the instance’s topic.1.72
Links & Outside ContentNo spammy or inappropriate external links.1.54
Distribution
SpamSpam is not authorized or welcome.6.24
Advertising & Commer-
cialization
Repeated or intrusive advertising is not accepted. Accounts may be
silenced or removed.
4.1
Copyright/Piracy You must obtain permission to quote, reproduce, or adapt any post. 2.11
Reposting/CrosspostingNo reposting or crossposting of copyrighted material.0.7
Manuscript submitted to ACM

Federating Governance: How Community Rules Scale with Mastodon Instances 9
4.3 Lexical Features
A lexical feature is a characteristic of the words or vocabulary in a text, such as word frequency, diversity, length, or
usage patterns, that reflects its linguistic and structural properties. Previous research suggests that lexical features
can provide valuable insights into the dynamics and governance of communities. In this study, lexical features were
analyzed to examine the linguistic characteristics of community rules and their evolution as community size increased.
We use number of users as a proxy for community size, as it is readily available across instances and consistent with
prior work on online community scaling [19]. This choice aligns with theories of governance scaling, which emphasize
coordination and rule-setting costs that grow with the size of the membership rather than solely with interaction
frequency. While content production and visible activity are driven by participating users, governance and moderation
must account for the entire membership, including inactive or “lurking” users, often in a proactive rather than purely
reactive manner [45]. Another meaningful proxy could be engagement volume which captures behavioral intensity but
does not fully represent the population over which governance applies.
However, to ensure robustness, we repeat the following analysis using number of statuses (engagement) as a proxy
for community size instead of user count (see Appendix C).
• Word Count. Prior studies [63] indicate that word count tends to increase with community size. As communities
grow, more words are used to express explicit expectations and describe a larger variety of challenges in hopes
to provide participants with all required information about the community.
• Rule Count. While rule count is a structural feature rather than a lexical feature, we include it in our analysis as
number of rules can indicate scope of the rules. Further, the presence of more rules can lead to a richer or more
complex lexicon. More rules can also indicate legal or technical vocabulary and rule count can be a proxy lexical
measure.
• Type-Token Ratio (TTR)This metric is used to quantify the diversity of vocabulary within a text [ 35]. It is
calculated by dividing the number of unique words (types) by the total number of words (tokens) in the text. A
higher TTR indicates greater lexical variety, while a lower TTR suggests more repetitive or limited word usage.
This metric is often employed to analyze language complexity or assess the lexical richness of written or spoken
material. For this study, we focus on instances where TTR scores were meaningful by excluding rules containing
fewer than seven words.
• Readability ScoreThe Flesch-Kincaid Reading Ease (FRE) score is a measure of assessing of a given text [ 16].
Here, we use the set of rules of an instance to analyze readability. We measure readability as it is a signal of
comprehension. We hypothesize, the larger the instance is, the more comprehendible a rule should be as the
rules serve as a guideline to a larger and more diverse set of people.
4.4 Regression
We investigate two independent variables that might affect rule formation, instance size and federation degree. The
dependent variables are lexical and topical features: word count, rule count, TTR and readability score. We regress
these outcomes on log-transformed instance size and federation degree, using model specifications appropriate to
each outcome type. Count outcomes, i.e., word count, rule count, topic count, are estimated with negative binomial
regression. or TTR, a ratio outcome with values between 0 and 1, we use beta regression with a logit link. Readability
(Flesch Reading Ease, FRE) is estimated via OLS with HC3 robust standard errors.
Manuscript submitted to ACM

10 Muralidharan et al.
Due to the nature of the data, the sample size for each of these model varies. In particular, after removing instances
with zero federation, we get a sample of N=4, 800(for word and rule count model). For topic count, we further exclude
instances where no rules could be categorized by the LLM, leaving N=3, 621. Japanese-script instances are omitted from
TTR and readability models due to incompatibility with space-tokenized lexical metrics.
A simple rule count may inflate differences across instances by treating semantically similar norms as multiple
distinct rules, e.g., a single norm might be split into separate rules such as “Respect others’ identities in full” and
“Respect others’ right to engage or disengage in conversation”, or versus combined into one rule such as “Respect others’
identities and their right to engage or disengage in conversation. ”). We also use topic count as an outcome to capture
the number of unique rule topics of an instance rather than the raw number of rule items retrieved from the API.
The age of an instance could be a potential confounder in the relationship between size, federation, and rule
characteristics. To assess this, we replicate all models on the subset with available creation dates (N=3, 356) and estimate
a sensitivity model controlling for age (see Appendix A).
5 Results
5.1 Topics
Through rule classification, described in Section 4.1, we found that “Hate Speech”, “Harassment” and “Illegal Content”
are a theme across the platform regardless of size, which is in line with previous research [56, 64, 68]. The number of rules
in an instance increases with size (Spearman’s coefficient of0.3, p< 0.05, Figure 2a). Our topic analysis (Fig. 3) reveals
that smaller communities focus disproportionately on a few rule types, while larger instances maintain a balanced
emphasis across many rule types. The results of our topic analysis trend remain consistent even after deduplication
of linguistically similar rules in an instance (see Appendix D). Community-topic focused analysis indicates that rule
distributions do not differ substantially across community topics (see Appendix F).
Our results of mapping rule types to the ABCD framework and measure of rule diversity (Fig. 2b) indicate that
though some instances regardless of size have no diversity, on average larger instances tend to have greater diversity.
This is supported by the Spearman’s co-efficient measured between size and rule diversity of0.21(p<0.005).
5.2 Lexical Features
The word count of the rules increases with instance size (Spearman’s coefficient 𝜌= 0.40, Fig. 4a). Rule count also
increases as instances get larger ( 𝜌= 0.33, Fig. 4b), reflecting the need for more granular governance in larger
communities. Somewhat counterintuively, larger communities tend to have lower rule readability (𝜌=−0.31, Fig. 4c).
Lexical diversity similarly decreases with instance size (𝜌=− 0.34, Fig. 4d), indicating greater vocabulary repetition in
larger instances’ rule texts. This likely reflects increasing standardization of rule language rather than simplification, as
readability simultaneously decreases with scale. All correlations reported are statistically significant,𝑝< 0.005. We
discuss potential explanations for these trends in Section 6.
Our analysis with engagement as a proxy of community size shows similar trends, where word and rule count
increase as size increases, and readability and lexical diversity decrease with size (see Appendix C). The correlations are
consistently weaker under the engagement proxy, suggesting that membership, including inactive and lurking users,
creates governance pressure beyond what behavioral activity alone predicts. This is consistent with a governance-burden
interpretation in which moderators must formally address the all membership, including potential bad actors who may
not yet have posted [45].
Manuscript submitted to ACM

Federating Governance: How Community Rules Scale with Mastodon Instances 11

a)
b)
Fig. 2. Distribution of topic count, measured by number of unique rule topics per instance (top) and topic diversity, measured by
entropy (bottom), across instance size bins.
5.3 Regression
Table 2 shows the regression results of instance size and federation degree. Across models, we find that instance size is
a consistent and statistically significant predictor for all rule formalization outcomes. Larger instances are associated
with higher word count, rule count, and topic count (𝛽≥ 0.2,𝑝< 0.001), as well as lower TTR (𝛽=− 0.47,𝑝< 0.001),
Manuscript submitted to ACM

12 Muralidharan et al.
Automated toolsHarassment
Doxxing/
Personal InfoImpersonation Dogpiling Trolling Hate SpeechIllegal Content NSFW Content W arnings Incitement of Violence
Mis/Disinfo
rmation/Conspiracy
Images
Off-topic/topic specific Links & Outside Content
Spam
Copyright/
Piracy
Advertising & Comme
rcialization
Reposting/C
rossposting
101 to 102
102 to 103
103 to 104
104 to 105
105 to 106
106 to 107
Instance Size Bin
0.01 0.11 0.04 0.01 0.01 0.01 0.24 0.12 0.06 0.05 0.04 0.04 0.03 0.02 0.02 0.05 0.02 0.03 0.00
0.02 0.12 0.05 0.01 0.01 0.02 0.23 0.11 0.09 0.07 0.05 0.05 0.05 0.03 0.02 0.06 0.02 0.04 0.01
0.03 0.13 0.05 0.02 0.01 0.01 0.23 0.11 0.10 0.09 0.05 0.04 0.05 0.04 0.02 0.08 0.03 0.05 0.01
0.03 0.12 0.05 0.02 0.01 0.02 0.21 0.11 0.10 0.09 0.06 0.06 0.06 0.03 0.04 0.07 0.03 0.07 0.01
0.03 0.12 0.06 0.02 0.01 0.02 0.21 0.11 0.10 0.10 0.06 0.07 0.05 0.01 0.02 0.10 0.02 0.09 0.01
0.01 0.10 0.06 0.02 0.02 0.01 0.15 0.12 0.11 0.12 0.09 0.08 0.11 0.01 0.04 0.06 0.07 0.04 0.02
0.05
0.10
0.15
0.20
Topic Prevalence
Action Behavior Content Distribution
Fig. 3. Heat map of topic prevalence per instance, across instance size bins. Topics are grouped into one of the four categories: Action,
Behavior, Content, and Distribution. Darker cells indicate higher prevalence of a given rule topic within an instance size bin.
and readability scores (𝛽=− 8.14,𝑝< 0.001), indicating longer and more topically diverse but lexically less varied and
less readable rule descriptions.
Table 2. Size and Federation Effects on Rule Formalization
Predictors Word Count † Rule Count† Topic Count† TTR‡ Readability§
Log User Count 0.42*** 0.29*** 0.20***−0.47***−8.14***
(0.02) (0.01) (0.01) (0.02) (0.56)
Log Fed Num 0.05 0.08*** 0.06*−0.11*** 2.35*
(0.03) (0.02) (0.03) (0.03) (1.07)
Intercept 3.41*** 0.82*** 1.04*** 2.74*** 65.10***
(0.11) (0.07) (0.10) (0.11) (4.07)
Observations 4,801 4,801 3,621 4,363 4,363
Pseudo-𝑅2 0.015 0.036 0.018 — 0.047
AIC 49,128 23,533 18,504−12,181 43,486
Note:Unstandardized coefficients shown. Standard errors in parentheses (HC3 robust for OLS).
***𝑝<0.001, **𝑝<0.01, *𝑝<0.05.
† Negative Binomial regression. Coefficients represent the log of expected counts.
‡ Beta regression.
§ OLS
Manuscript submitted to ACM

Federating Governance: How Community Rules Scale with Mastodon Instances 13

a)
b)
c)
d)
Fig. 4. Distribution of lexical features across instance sizes: (a) word count, (b) rule count, (c) readability of rule, measured by
Flesch-Kinaid score, and (d) rule lexical diversity, measured by Type-Token ratio. Grey dots represent the values of features, while red
dots and whiskers indicate the bootstrapped means and 95% CI, respectively.
For negative binomial regression estimating log(𝐸[𝑌])≈𝛽𝑋 , the coefficients represent log incidencerate ratios; we
interpret the results using the exponentiated coefficients, Incidence Rate Ratios, 𝐼𝑅𝑅=𝑒 𝛽. Each tenfold increase in
users is associated with 53% more words in rule text (IRR=1.53), 34% more rules (IRR=1.34), and 23% more unique rule
topics (IRR=1.23). For TTR, estimated via beta regression with a logit link, coefficients are on the log-odds scale and
not directly interpretable. We therefore compute average marginal effects (AME), defined as 1 𝑁 ˝ 𝑖𝛽·𝜇 𝑖(1−𝜇 𝑖), which
average the marginal effect𝜕𝜇𝑖/𝜕𝑥 over all observations. For log user count, this yields AME≈− 0.06, indicating that
a tenfold increase in users is associated with a 7% relative reduction at the sample mean (TTR≈ 0.83). For the OLS
model, coefficients are direct changes in FRE score on a 0–100 scale, where higher indicates more readable rules. Larger
instances also show meaningfully lower rule readability, i.e.,−8.1FRE points per tenfold increase in users; moving
from “standard” to “fairly difficult” on the Flesch-Kincaid scale.
Federation degree shows a smaller and less consistent effect, only significantly associated with rule count (𝛽= 0.08,
𝑝< 0.001) and TTR (𝛽=− 0.11,𝑝< 0.001). Each tenfold increase in federation connections is associated with 9% more
Manuscript submitted to ACM

14 Muralidharan et al.
rules (IRR=1.09,𝑝< 0.001). Federation’s effect on TTR (−0.01units at the mean) is statistically significant but negligibly
small in practice. This suggests that instances with more cross-instance exposure have modestly broader the scope of
governance, but no difference in linguistic characters.
The sensitivity analysis including community age as a predictor, yields substantively similar conclusions (Appendix A).
5.4 Robustness
Previous research indicates that communities centered on similar topics often develop similar norm sets [64]. At the
same time, Mastodon has also served as a major destination for users migrating from Twitter/X, particularly during
October 2022 [25, 30], which could also have influenced instance-level moderation rules. These dynamics raise the
possibility that both topical focus and migration dynamics may confound the observed patterns in rule formation.
We therefore examine each factor in turn. First, to assess the effect of topical focus, we manually categorize the short
descriptions of instances and compute the rule similarities across instance description topics (see Appendix F). We find
that more than 80% of the topics has high cosine similarity of above 0.92, indicating no significant difference between
the rule types of different topics (Fig.8).
Second, to evaluate the effect of the migration on instance rule sets, we used Wayback Machine1 to recover the rules
of instances at three time points: October 2022 (Twitter/X acquisition), January 2023 (shortly after the migration surge),
and January 2024 (one year later). Only a small set of 60 instances were recoverable and available for longitudinal
comparison. We categorize and compare the rule sets at different time points for these instances using Jaccard similarity
(see Appendix G). Instances are considered to have changed if the Jaccard similarity of their rule sets between two time
points is below 0.9. Yet with this relatively lax threshold, we find that only 19% of instances changed their rule sets
between 2022–2023, while only 10% changed between 2023–2024.
Overall, we find limited evidence that the Twitter takeover systematically reshaped written rule sets (see Appendix G).
However, our conclusions remain limited by the small number of recoverable instances: only 60 instances had recoverable
snapshots across all three time points, of which 11 showed rule changes between 2022 and 2023. The absence of detectable
change in this small and likely non-representative sample as null effects for the broader ecosystem should be interpreted
with caution. Nonetheless, these analyses suggest that neither topical focus nor migration dynamics explain the
variation in rule formalization documented in our main analysis, supporting the robustness of our findings of the
primary explanatory factors, community size and federation.
6 Discussion
This study examines self-governance on Mastodon, focusing on the relationship between community size and rule
complexity across a wide range of Mastodon instances.
First, we find that across instances of all sizes, rules consistently emphasize preventing harassment, hate speech
and illegal content. This aligns with previous research of the most popular Mastodon instances, showing that the
platform and its moderators prioritize creating safe spaces free from harassment, hate speech, and other common online
harms [56]. Notably, the relative emphasis on these topics remains invariant across community sizes, suggesting a
broadly shared normative commitment to harm reduction. Despite operating independently from one another, most
1web.archive.org
Manuscript submitted to ACM

Federating Governance: How Community Rules Scale with Mastodon Instances 15
Mastodon administrators appear to align with broad legal requirements and share normative priorities, such as anti-
harassment, with mainstream platforms [68]. This consistency points to a form of normative convergence within a
decentralized ecosystem.
Second, we observe that rule formalization is strongly associated with instances size. Larger communities tend to
adopt broader and more diverse rule sets, reflected in both topical scope (the number and the diversity of topics), and in
rule volume (word count and rule count). This pattern suggests an expansion of governance concerns as communities
grow, consistent with prior work on scaling in online communities [3, 19].
Linguistic analysis reveals a more complex picture: although rules in larger communities tend to have less lexical
diversity—indicating greater standardization— this does not translate into improved readability. One plausible interpre-
tation is that larger instances use more specialized or formal language to reduce ambiguity and to address a broader
range of behaviors. In contrast, smaller communities may rely on more informal language that is easier to read but less
precise.
Written rules, a core governance tool, become more formalized as communities grow, suggesting that scale remains a
key challenge for moderation. While decentralization distributes governance across instances, each instance continues
to face internal scaling pressures as its local community expands. Our regression results reinforce this: across a broad
sample of 4,801 instances, community size is the strongest and most consistent predictor of rule formalization, with
federation degree playing a secondary and outcome-specific role. This pattern holds in the age-controlled sensitivity
model (N = 3,356), confirming that the size effect is not an artifact of compositional differences between the two samples.
These findings suggest that, despite inter-instance connections, governance practices are primarily associated with
internal community needs and local interactions.
These results point to a broader insight: decentralization changeswheregovernance decisions are made, but not
the fundamental relationship between community size and governance complexity. The persistence of similar scaling
patterns across both centralized platforms (like Reddit) and decentralized, volunteer-driven systems (like Mastodon)
suggests that the challenges of governing larger communities may be difficult to escape through platform architecture
alone.
Design Implications for Moderation
Taken together, these findings highlight an important design trade-off between precision and accessibility in community
rules. More formal and detailed rules may support consistent enforcement and reduce ambiguity for moderators, but
reduced readability can create barriers for users, particularly newcomers, and undermine rule awareness or voluntary
compliance [39]. Rules that are difficult to understand can shift interpretive power toward moderators, increasing
discretionary enforcement and potentially affecting perceptions of fairness and legitimacy. In federated systems like
Mastodon, where governance is local and compliance often relies on shared norms rather than formal sanctions,
maintaining readable and inclusive rules is especially important as instances grow. Our results point to several concrete
design opportunities for federated platforms.
Size-calibrated rule revisions.Rule formalization scales monotonically with instance size across all measures:
scope, word count, topical diversity, and lexical complexity. Yet instance administrators do not currently receive any
infrastructure anticipating this trajectory. Federated platforms could offer tiered rule templates calibrated to community
size, providing a minimal high-readability template for new instances and detect when an instance crosses a size
threshold (e.g., 100 or 1,000 users) and prompt administrators with structured templates for expanding their rule set or
Manuscript submitted to ACM

16 Muralidharan et al.
recruiting additional moderators. This would reduce the cold-start burden on administrators and promote governance
continuity as communities expand [39, 71].
Readability tooling at the authoring stage.We find that larger instances produce rules with substantially lower
readability scores (𝜌=− 0.31), despite serving larger and more linguistically diverse user populations where accessibility
is most critical. To address this gap between complexity and accessibility, platforms could provide tools that show
real-time readability feedback, analogous to spelling checkers, could nudge administrators toward plain-language rule
formulation as complexity grows. The value of readable rules in supporting compliance and norm internalization is
well established [6, 31], and automated tooling could extend this benefit to contexts where administrators lack editorial
support.
Highlighting governance divergence across federated boundaries.The dominant rule categories—Hate Speech,
Harassment, Illegal Content—are consistent across all instance sizes, representing a shared normative floor. Federation
protocols currently offer limited visibility intoabove-floorgovernance differences, which our data show do vary
systematically with size and topical focus. Tools that surface these differences during federation negotiation—showing,
for instance, that a prospective federation partner handles NSFW content or misinformation differently—could help
administrators anticipate norm conflicts before they generate moderation load [33, 82].
Resource allocation.Community size, not federation degree, is the dominant predictor of rule formalization across
all outcomes. This finding suggests that platform support for governance would have greater payoffs when targeted at
growing instances than at inter-instance coordination. This support includes resources such as administrator training
and moderation tooling.
7 Limitations and Future Work
This study has several limitations. First, the analyses relies on a largely static snapshot of Mastodon. A longitudinal
analysis examining how rules evolve as instances grow could offer deeper insights. Second, while our regression
analyses identify strong associations between community size and rule formalization, they do not establish causality.
Future work combining longitudinal data, qualitative methods, or direct observations of moderation practices could
help unpack the mechanisms underlying these relationships. Finally, our topic annotation relies on an LLM using
a manually selected prompt. Although we carefully evaluated prompt performance, multi-label topic classification
remains challenging and may introduce noise.
Our analysis of rule sets from various timestamps indicates that despite Mastodon being a key location for Twitter
migration, the rule sets were not significantly affected. We find that many instances were created after the Twitter
takeover, likely reflecting Mastodon’s increased visibility and adoption. Future work could examine the impacts of the
Twitter/X migration to Mastodon more closely by combining longitudinal analyses of rule evolution with behavioral
data, such as moderation actions or user participation patterns, to better understand how large-scale migration events
influence moderation practices beyond formal rule articulation.
A second important direction for future research concerns the readability and accessibility of community rules.
Further work could investigate how different design choices in rule presentation—such as summaries, examples, or
layered disclosure—affect user understanding, perceptions of legitimacy, and moderation outcomes.
Finally, although some scholars advocate for network-level approaches to moderating federated systems [43], our
results indicate that rule formalization is most strongly associated with local community size rather than external
federation interactions. Prior qualitative research, including interviews with Mastodon administrators, highlights
tensions that arise when instances with differing norms interact [29, 82]. Future research should further explore how
Manuscript submitted to ACM

Federating Governance: How Community Rules Scale with Mastodon Instances 17
local autonomy and cross-instance coordination are negotiated over time, particularly as federated platforms continue
to scale and diversify. Understanding this balance is critical for advancing theories of decentralized governance and for
informing the design of tools that support coordination without undermining community self-governance.
References
[1] Ishaku Hassan Anaobi, Aravindh Raman, Ignacio Castro, Haris Bin Zia, Damilola Ibosiola, and Gareth Tyson. 2023. Will Admins Cope? Decentralized
Moderation in the Fediverse. InProceedings of the ACM Web Conference 2023. ACM, Austin TX USA, 3109–3120. doi:10.1145/3543507.3583487
[2] Blake E. Ashforth and Fred Mael. 1989. Social Identity Theory and the Organization.Academy of Management Review14, 1 (1989), 20–39.
doi:10.5465/amr.1989.4278999
[3] Shambhobi Bhattacharya, Jisung Yoon, and Hyejin Youn. 2024. Unveiling Scaling Laws in the Regulatory Functions of Reddit.
arXiv:2407.12063 [physics.soc-ph]
[4] Carlo Alberto Bono, Lucio La Cava, Luca Luceri, and Francesco Pierri. 2024. An Exploration of Decentralized Moderation on Mastodon. InACM
Web Science Conference. ACM, Stuttgart Germany, 53–58. doi:10.1145/3614419.3644016
[5] Bilge Bulat, Haotian Wang, Shun Fujimoto, and Seth Frey. 2024. The psychology of volunteer moderators: Tradeoffs between participation, belonging,
and norms in online community governance.New Media & Society0, 0 (2024), xx–yy. doi:10.1177/14614448241246512
[6] Jie Cai and Donghee Yvette Wohn. 2019. What are Effective Strategies of Handling Harassment on Twitch? Users’ Perspectives. InCompanion
Publication of the 2019 Conference on Computer Supported Cooperative Work and Social Computing(Austin, TX, USA)(CSCW ’19 Companion).
Association for Computing Machinery, New York, NY, USA, 166–170. doi:10.1145/3311957.3359478
[7] Jie Cai, Donghee Yvette Wohn, and Mashael Almoqbel. 2021. Moderation Visibility: Mapping the Strategies of Volunteer Moderators in Live
Streaming Micro Communities. InProceedings of the 2021 ACM International Conference on Interactive Media Experiences(Virtual Event, USA)(IMX
’21). Association for Computing Machinery, New York, NY, USA, 61–72. doi:10.1145/3452918.3458796
[8] Edoardo Celeste, Nicola Palladino, Dennis Redeker, and Kinfe Yilma. 2023.Platform Policies Versus Human Rights Standards. Springer International
Publishing, Cham, 93–129. doi:10.1007/978-3-031-32924-1_5
[9] Eshwar Chandrasekharan, Chaitrali Gandhi, Matthew Wortley Mustelier, and Eric Gilbert. 2019. Crossmod: A cross-community learning-based
system to assist reddit moderators.Proceedings of the ACM on human-computer interaction3, CSCW (2019), 1–30.
[10] Ángel Díaz and Laura Hecht-Felella. 2021.Double Standards in Social Media Content Moderation. Technical Report. Brennan Center for Justice at New
York University School of Law. https://www.brennancenter.org/our-work/research-reports/double-standards-social-media-content-moderation
Accessed: 24 Dec 2025.
[11] Bryan Dosono and Bryan Semaan. 2019. Moderation Practices as Emotional Labor in Sustaining Online Communities: The Case of AAPI Identity
Work on Reddit. InProceedings of the 2019 CHI Conference on Human Factors in Computing Systems (CHI ’19). Association for Computing Machinery,
New York, NY, USA, 1–13. doi:10.1145/3290605.3300372
[12] R. I. M. Dunbar. 2012. Social cognition on the Internet: testing constraints on social network size.Philosophical Transactions of the Royal Society B:
Biological Sciences367, 1599 (Aug. 2012), 2192–2201. doi:10.1098/rstb.2012.0121 Publisher: Royal Society.
[13] R. I. M. Dunbar. 2016. Do online social media cut through the constraints that limit the size of offline social networks?Royal Society Open Science3,
1 (Jan. 2016), 150292. doi:10.1098/rsos.150292 Publisher: Royal Society.
[14] Anna Fang, Wenjie Yang, and Haiyi Zhu. 2023. Shaping Online Dialogue: Examining How Community Rules Affect Discussion Structures on Reddit.
arXiv:2308.01257 [cs.SI] https://arxiv.org/abs/2308.01257
[15] Casey Fiesler, Jialun Jiang, Joshua McCann, Kyle Frye, and Jed Brubaker. 2018. Reddit Rules! Characterizing an Ecosystem of Governance.Proceedings
of the International AAAI Conference on Web and Social Media12, 1 (Jun. 2018), 72–81. doi:10.1609/icwsm.v12i1.15033
[16] Rudolf Franz Flesch. 1948. A new readability yardstick.The Journal of applied psychology32 3 (1948), 221–33. https://api.semanticscholar.org/
CorpusID:39344661
[17] Andrea Forte, Vanessa Larco, and Amy Bruckman. 2009. Decentralization in Wikipedia Governance.Journal of Management Information Systems26,
1 (2009), 49–72. https://www.jstor.org/stable/40398966
[18] Seth Frey and Robert W. Sumner. 2019. Emergence of integrated institutions in a large population of self-governing communities.PLOS ONE14, 7
(July 2019), e0216335. doi:10.1371/journal.pone.0216335
[19] Seth Frey, Qiankun Zhong, Beril Bulat, William D. Weisman, Caitlyn Liu, Stephen Fujimoto, Hannah Wang, and Charles M. Schweik. 2022. Governing
Online Goods: Maturity and Formalization in Minecraft, Reddit, and World of Warcraft Communities.Proceedings of the ACM on Human-Computer
Interaction6, CSCW2 (Nov. 2022), 1–23. doi:10.1145/3555191
[20] Edoardo Gallo and Chang Yan. 2015. The effects of reputational and social knowledge on cooperation.Proceedings of the National Academy of
Sciences112, 12 (2015), 3647–3652. arXiv:https://www.pnas.org/doi/pdf/10.1073/pnas.1415883112 doi:10.1073/pnas.1415883112
[21] Tarleton Gillespie. 2018.Custodians of the Internet: Platforms, Content Moderation, and the Hidden Decisions That Shape Social Media. Yale University
Press, New Haven, CT. doi:10.12987/9780300235029 Journal Abbreviation: Custodians of the Internet: Platforms, Content Moderation, and the
Hidden Decisions That Shape Social Media Pages: 288 Publication Title: Custodians of the Internet: Platforms, Content Moderation, and the Hidden
Decisions That Shape Social Media.
Manuscript submitted to ACM

18 Muralidharan et al.
[22] Tarleton Gillespie. 2020-07-01. Content moderation, AI, and the question of scale.Big Data & Society7, 2 (2020-07-01), 2053951720943234.
doi:10.1177/2053951720943234 Publisher: SAGE Publications Ltd.
[23] Google. 2025. YouTube Community Guidelines enforcement. https://transparencyreport.google.com/youtube-policy/removals
[24] Rachel Griffin. 2024. The heteronormative male gaze: Experiences of sexual content moderation among queer instagram users in berlin.International
journal of communications, network and system sciences18 (2024), 1266–1288.
[25] Jiahui He, Haris Bin Zia, Ignacio Castro, Aravindh Raman, Nishanth Sastry, and Gareth Tyson. 2023. Flocking to Mastodon: Tracking the Great
Twitter Migration. InProceedings of the 2023 ACM on Internet Measurement Conference(Montreal QC, Canada)(IMC ’23). Association for Computing
Machinery, New York, NY, USA, 111–123. doi:10.1145/3618257.3624819
[26] Susan C. Herring. 2004. Computer-Mediated Discourse Analysis: An Approach to Researching Online Behavior. InDesigning for Virtual Communities
in the Service of Learning, Sasha A. Barab, Rob Kling, and James H. Gray (Eds.). Cambridge University Press, New York, 338–376. Preprint.
[27] Benjamin Mako Hill. 2019. How Discord moderators build innovative solutions to problems of scale with the past as a guide. https://mako.cc/
copyrighteous/how-discord-moderators-build-innovative-solutions-to-problems-of-scale-with-the-past-as-a-guide
[28] Geoffrey M. Hodgson. 2025. Formal and informal institutions: some problems of meaning, impact, and interaction.Journal of Institutional Economics
21 (2025), e1. doi:10.1017/S1744137424000249
[29] Tao Huang. 2024. Decentralized social networks and the future of free speech online.Computer Law & Security Review55 (2024), 106059.
doi:10.1016/j.clsr.2024.106059
[30] Ujun Jeong, Paras Sheth, Anique Tahir, Faisal Alatawi, H. Russell Bernard, and Huan Liu. 2024. Exploring Platform Migration Patterns between
Twitter and Mastodon: A User Behavior Study. arXiv:2305.09196 [cs.SI] https://arxiv.org/abs/2305.09196
[31] Shagun Jhaver, Iris Birman, Eric Gilbert, and Amy Bruckman. 2019. Human-Machine Collaboration for Content Regulation: The Case of Reddit
Automoderator.ACM Trans. Comput.-Hum. Interact.26, 5, Article 31 (July 2019), 35 pages. doi:10.1145/3338243
[32] Shagun Jhaver, Christian Boylston, Diyi Yang, and Amy Bruckman. 2021. Evaluating the Effectiveness of Deplatforming as a Moderation Strategy
on Twitter.Proc. ACM Hum.-Comput. Interact.5, CSCW2, Article 381 (Oct. 2021), 30 pages. doi:10.1145/3479525
[33] Shagun Jhaver, Seth Frey, and Amy X. Zhang. 2023. Decentralizing Platform Power: A Design Space of Multi-Level Governance in Online Social
Platforms.Social Media + Society9, 4 (2023), 20563051231207857. arXiv:https://doi.org/10.1177/20563051231207857 doi:10.1177/20563051231207857
[34] Jialun ’Aaron’ Jiang, Skyler Middler, Jed R. Brubaker, and Casey Fiesler. 2020. Characterizing Community Guidelines on Social Media Platforms.
InCompanion Publication of the 2020 Conference on Computer Supported Cooperative Work and Social Computing(Virtual Event, USA)(CSCW ’20
Companion). Association for Computing Machinery, New York, NY, USA, 287–291. doi:10.1145/3406865.3418312
[35] Wendell Johnson. 1944. Studies in language behavior: A program of research.Psychological Monographs56, 2 (1944), 1–15.
[36] Kate Klonick. 2017. The new governors: The people, rules, and processes governing online speech.Harv. L. Rev.131 (2017), 1598.
[37] Peter Kollock and Marc A. Smith. 1996. Managing the virtual commons : Cooperation and conflict in computer communities.Pragmatics and beyond.
New series39 (1996), 109–128. https://api.semanticscholar.org/CorpusID:150982575
[38] Vinay Koshy, Tanvi Bajpai, Eshwar Chandrasekharan, Hari Sundaram, and Karrie Karahalios. 2023. Measuring User-Moderator Alignment on
r/ChangeMyView.Proc. ACM Hum.-Comput. Interact.7, CSCW2, Article 286 (Oct. 2023), 36 pages. doi:10.1145/3610077
[39] Robert E. Kraut, Paul Resnick, Sara Kiesler, Moira Burke, Yan Chen, Niki Kittur, Joseph Konstan, Yuqing Ren, and John Riedl. 2012.Building Successful
Online Communities: Evidence-Based Social Design. The MIT Press, Massachusetts. doi:10.7551/mitpress/8472.001.0001
[40] Klaus Krippendorff. 2004.Content Analysis: An Introduction to Its Methodology(2 ed.). Sage Publications, Thousand Oaks, CA. Especially Chapter
11, pp. 211–256.
[41] Tina Kuo, Alicia Hernani, and Jens Grossklags. 2023. The unsung heroes of facebook groups moderation: A case study of moderation practices and
tools.Proceedings of the ACM on Human-Computer Interaction7, CSCW1 (2023), 1–38.
[42] Lucio La Cava, Sergio Greco, and Andrea Tagarelli. 2021. Understanding the growth of the Fediverse through the lens of Mastodon.Applied Network
Science6, 1 (Dec. 2021), 64. doi:10.1007/s41109-021-00392-5 arXiv:2106.15473 [physics].
[43] S Lai, Yoel Roth, R DiResta, K Klonick, M Knodel, E Prodromou, and A Rodericks. 2025. New Paradigms in Trust and Safety: Navigating Defederation
on Decentralized Social Media Platforms. Carnegie Endownment for International Peace. https://carnegieendowment.org/research/2025/03/fediverse-
social-media-internet-defederation Accessed: 2025-05-13.
[44] Cliff Lampe and Paul Resnick. 2004. Slash(dot) and burn: distributed moderation in a large online conversation space. InProceedings of the SIGCHI
Conference on Human Factors in Computing Systems(Vienna, Austria)(CHI ’04). Association for Computing Machinery, New York, NY, USA, 543–550.
doi:10.1145/985692.985761
[45] Cliff Lampe, Rick Wash, Alcides Velasquez, and Elif Ozkaya. 2010. Motivations to participate in online communities. InProceedings of the
SIGCHI Conference on Human Factors in Computing Systems (CHI ’10). Association for Computing Machinery, New York, NY, USA, 1927–1936.
doi:10.1145/1753326.1753616
[46] Cliff Lampe, Paul Zube, Jusil Lee, Chul Hyun Park, and Erik Johnston. 2014. Crowdsourcing civility: A natural experiment examining the effects of
distributed moderation in online forums.Government Information Quarterly31, 2 (April 2014), 317–326. doi:10.1016/j.giq.2013.11.005
[47] Leon Leibmann, Galen Weld, Amy X. Zhang, and Tim Althoff. 2025. Reddit Rules and Rulers: Quantifying the Link Between Rules and Perceptions
of Governance Across Thousands of Communities.Proceedings of the International AAAI Conference on Web and Social Media19, 1 (Jun. 2025),
1098–1121. doi:10.1609/icwsm.v19i1.35863
Manuscript submitted to ACM

Federating Governance: How Community Rules Scale with Mastodon Instances 19
[48] Zhiyuan Lin, Niloufar Salehi, Bowen Yao, Yiqi Chen, and Michael Bernstein. 2017. Better When It Was Smaller? Community Content and Behavior
After Massive Growth.Proceedings of the International AAAI Conference on Web and Social Media11, 1 (May 2017), 132–141. doi:10.1609/icwsm.
v11i1.14884 Number: 1.
[49] Jessa Lingel and Adam Golub. 2015. In face on Facebook: Brooklyn’s drag community and sociotechnical practices of online communication.Journal
of Computer-Mediated Communication20, 5 (2015), 536–553.
[50] Travis Lloyd, Joseph Reagle, and Mor Naaman. 2025. ’There Has To Be a Lot That We’re Missing’: Moderating AI-Generated Content on Reddit.
Proc. ACM Hum.-Comput. Interact.9, 7 (Oct. 2025), CSCW264:1–CSCW264:24. doi:10.1145/3757445
[51] James G. March, Martin Schulz, and Xueguang Zhou. 2000.The Dynamics of Rules: Change in Written Organizational Codes(30 ed.). Stanford
University Press, Stanford, CA.
[52] J. Nathan Matias. 2019. The Civic Labor of Volunteer Moderators Online.Social Media + Society5, 2 (2019), 2056305119836778.
arXiv:https://doi.org/10.1177/2056305119836778 doi:10.1177/2056305119836778
[53] Meta. 2024. How enforcement technology works. https://transparency.meta.com/enforcement/detecting-violations/how-enforcement-technology-
works/
[54] Supun Nakandala, Giovanni Ciampaglia, Norman Su, and Yong-Yeol Ahn. 2017. Gendered Conversation in a Social Game-Streaming Platform.
Proceedings of the International AAAI Conference on Web and Social Media11, 1 (May 2017), 162–171. doi:10.1609/icwsm.v11i1.14885
[55] Azadeh Nematzadeh, Giovanni Luca Ciampaglia, Yong-Yeol Ahn, and Alessandro Flammini. 2019. Information overload in group communication:
from conversation to cacophony in the Twitch chat.Royal Society open science6, 10 (2019), 191412.
[56] Matthew N. Nicholson, Brian C Keegan, and Casey Fiesler. 2023. Mastodon Rules: Characterizing Formal Rules on Popular Mastodon Instances. In
Companion Publication of the 2023 Conference on Computer Supported Cooperative Work and Social Computing (CSCW ’23 Companion). Association
for Computing Machinery, New York, NY, USA, 86–90. doi:10.1145/3584931.3606970
[57] Siobhán O’Mahony and Fabrizio Ferraro. 2007. The Emergence of Governance in an Open Source Community.Academy of Management Journal50,
5 (2007), 1079–1106. doi:10.5465/amj.2007.27169153
[58] How Social Media Platforms’ Community Standards Address Influence Operations. 2021.Batemane, Jon abd Thompson, Natalie and Smith, Victoria.
Technical Report. Carnegie Endowment For International Peace.
[59] Elinor Ostrom. 1992. Governing the Commons: The Evolution of Institutions for Collective Action.Natural Resources Journal32, 2 (1992), 415–491.
https://digitalrepository.unm.edu/nrj/vol32/iss2/6
[60] Elinor Ostrom. 2000. Collective Action and the Evolution of Social Norms.Journal of Economic Perspectives14, 3 (2000), 137–158.
[61] Simon T. Powers, Carel P. van Schaik, and Laurent Lehmann. 2016. How institutions shaped the last major evolutionary transition to large-scale
human societies.Philosophical Transactions of the Royal Society B: Biological Sciences371, 1687 (2016), 20150098. doi:10.1098/rstb.2015.0098
[62] Jenny Preece and Diane Maloney-Krichmar. 2005. Online Communities: Design, Theory, and Practice.Journal of Computer-Mediated Communication
10, 4 (July 2005), JCMC10410. doi:10.1111/j.1083-6101.2005.tb00264.x
[63] Limor Raviv, Antje Meyer, and Shiri Lev-Ari. 2019. Larger communities create more systematic languages.Proceedings of the Royal Society B:
Biological Sciences286, 1907 (July 2019), 20191262. doi:10.1098/rspb.2019.1262
[64] Harita Reddy and Eshwar Chandrasekharan. 2023. Evolution of Rules in Reddit Communities. InComputer Supported Cooperative Work and Social
Computing. ACM, Minneapolis MN USA, 278–282. doi:10.1145/3584931.3606973
[65] Yuqing Ren, F. Maxwell Harper, Sara Drenner, Loren Terveen, Sara Kiesler, John Riedl, and Robert E. Kraut. 2012. Building Member Attachment in
Online Communities: Applying Theories of Group Identity and Interpersonal Bonds.MIS Quarterly36, 3 (2012), 841–864. http://www.jstor.org/
stable/41703483
[66] Yuqing Ren, Robert Kraut, and Sara Kiesler. 2007. Applying Common Identity and Bond Theory to Design of Online Communities.Organization
Studies28, 3 (2007), 377–408. arXiv:https://doi.org/10.1177/0170840607076007 doi:10.1177/0170840607076007
[67] Eduard Sabo, Mirela Riveni, and Dimka Karastoyanova. 2024. Decentralized Networks Growth Analysis: Instance Dynamics on Mastodon. In
Complex Networks & Their Applications XII, Hocine Cherifi, Luis M. Rocha, Chantal Cherifi, and Murat Donduran (Eds.). Springer Nature Switzerland,
Cham, 366–377. doi:10.1007/978-3-031-53503-1_30
[68] Brennan Schaffner, Arjun Nitin Bhagoji, Siyuan Cheng, Jacqueline Mei, Jay L Shen, Grace Wang, Marshini Chetty, Nick Feamster, Genevieve Lakier,
and Chenhao Tan. 2024. "Community Guidelines Make this the Best Party on the Internet": An In-Depth Study of Online Platforms’ Content
Moderation Policies. InProceedings of the 2024 CHI Conference on Human Factors in Computing Systems(Honolulu, HI, USA)(CHI ’24). Association
for Computing Machinery, New York, NY, USA, Article 486, 16 pages. doi:10.1145/3613904.3642333
[69] Nathan Schneider. 2022. Governable Spaces: A Feminist Agenda for Platform Policy. https://policyreview.info/articles/analysis/governable-spaces-
feminist-agenda-platform-policy. doi:10.14763/2022.1.1628 Internet Policy Review, 11(1).
[70] W. Richard Scott. 2013.Institutions and Organizations: Ideas, Interests, and Identities(4th ed.). SAGE Publications, Thousand Oaks, CA.
[71] Joseph Seering. 2020. Reconsidering Self-Moderation: the Role of Research in Supporting Community-Based Models for Online Content Moderation.
Proceedings of the ACM on Human-Computer Interaction4, CSCW2 (Oct. 2020), 1–28. doi:10.1145/3415178
[72] Joseph Seering, Tony Wang, Jina Yoon, and Geoff Kaufman. 2019. Moderator engagement and community development in the age of algorithms.
New Media & Society21, 7 (July 2019), 1417–1443. doi:10.1177/1461444818821316 Publisher: SAGE Publications.
[73] Joseph Seering, Tony Wang, Jina Yoon, and Geoff Kaufman. 2019. Moderator engagement and community development in the age of algorithms.
New media & society21, 7 (2019), 1417–1443.
Manuscript submitted to ACM

20 Muralidharan et al.
[74] Anna DuVal Smith. 2002. Problems of conflict management in virtual communities. InCommunities in cyberspace. Routledge, UK, 145–174.
[75] Susan Leigh Star and Karen Ruhleder. 1994. Steps towards an ecology of infrastructure: complex problems in design and access for large-scale
collaborative systems. InProceedings of the 1994 ACM Conference on Computer Supported Cooperative Work(Chapel Hill, North Carolina, USA)
(CSCW ’94). Association for Computing Machinery, New York, NY, USA, 253–264. doi:10.1145/192844.193021
[76] Thanakorn Thaminkaew, Piyawat Lertvittayakumjorn, and Peerapon Vateekul. 2024. Prompt-Based Label-Aware Framework for Few-Shot
Multi-Label Text Classification.IEEE Access12 (2024), 28310–28322. doi:10.1109/ACCESS.2024.3367994
[77] Emma Tosch, Luis Garcia, Cynthia Li, and Chris Martens. 2024. Privacy Policies on the Fediverse: A Case Study of Mastodon Instances.Proceedings
on Privacy Enhancing Technologies2024, 4 (Oct. 2024), 700–733. doi:10.56553/popets-2024-0138
[78] X Transparency. 2025. Global Transparency Report. https://transparency.x.com/en/reports/global-reports/2025-transparency-report
[79] Isaac Waller and Ashton Anderson. 2021. Quantifying social organization and political polarization in online platforms.Nature600, 7888 (Dec.
2021), 264–268. doi:10.1038/s41586-021-04167-x
[80] Emily Webber and Robin Dunbar. 2020. The fractal structure of communities of practice: Implications for business organization.PLOS ONE15, 4
(April 2020), e0232204. doi:10.1371/journal.pone.0232204 Publisher: Public Library of Science.
[81] Galen Weld, Leon Leibmann, Amy X. Zhang, and Tim Althoff. 2025. Perceptions of Moderators as a Large-Scale Measure of Online Community
Governance. arXiv:2401.16610 [cs.SI] https://arxiv.org/abs/2401.16610
[82] Zhilin Zhang, Jun Zhao, Ge Wang, Samantha-Kaye Johnston, George Chalhoub, Tala Ross, Diyi Liu, Claudine Tinsman, Rui Zhao, Max Van Kleek,
and Nigel Shadbolt. 2024. Trouble in Paradise? Understanding Mastodon Admin’s Motivations, Experiences, and Challenges Running Decentralised
Social Media.Proc. ACM Hum.-Comput. Interact.8, CSCW2, Article 520 (Nov. 2024), 24 pages. doi:10.1145/3687059
[83] Jian Zhu and David Jurgens. 2021. The structure of online social networks modulates the rate of lexical change. InProceedings of the 2021 Conference
of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Kristina Toutanova, Anna Rumshisky,
Luke Zettlemoyer, Dilek Hakkani-Tur, Iz Beltagy, Steven Bethard, Ryan Cotterell, Tanmoy Chakraborty, and Yichao Zhou (Eds.). Association for
Computational Linguistics, Online, 2201–2218. doi:10.18653/v1/2021.naacl-main.178
[84] Matteo Zignani, Sabrina Gaito, and Gian Paolo Rossi. 2018. Follow the “Mastodon”: Structure and Evolution of a Decentralized Online Social
Network.Proceedings of the International AAAI Conference on Web and Social Media12, 1 (June 2018), 541–550. doi:10.1609/icwsm.v12i1.14988
Number: 1.
A Regression: Age-Controlled Sensitivity Analysis
Table 3 replicates the primary regression (Table 2) on the subset of instances for which creation dates are recoverable
via the Mastodon API (N=3, 356for count models; N=3 , 059for TTR after Japanese exclusion). Community age is
included as an additional predictor. Coefficients for instance size and federation degree are directionally consistent
with the primary model. Age is negatively associated with rule count, word count, and topic count (𝛽=− 0.02to−0.04,
𝑝< 0.001), consistent with the interpretation that older communities maintain more concise rule sets, possibly reflecting
rule maturation over time. Age is positively associated with lexical diversity ( 𝛽= 0.05,𝑝< 0.001) and readability
(𝛽=0.87,𝑝<0.001), suggesting that governance language becomes more varied and accessible as communities age.
B Data Collection and Preprocessing
The instances.social API provides instance information across all Fediverse platforms. We retrieved a list of all possible
instances without any filters or parameters. This list is a reliable source for active instances in that it provides a by
default excludes instances that are “dead” instances, those that have been down for more than two weeks. Our collection
yielded us a total of 15,571 instances of all languages and topics.
To ensure our dataset contained only Mastodon instances, we queried each instance URI through the Mastodon
API to collect its rules. Of the 15,571 instances, 8,910 returned empty sets—either because they were not Mastodon
instances, had no rules, or stored rules in locations not accessible through the API endpoint. Another 953 instances
failed to retrieve rules due to unknown errors or server/client issues (e.g., 404, 5xx), which is a challenge also faced by
prior research that collects data in the Fediverse [1, 77].
For each instance, we collected the following metadata as defined by the instances.social API: Instance ID (unique ID
number provided), Instance Name (unique name of the instance), User Count (number of users currently registered
Manuscript submitted to ACM

Federating Governance: How Community Rules Scale with Mastodon Instances 21
Table 3. Full Models with Age Controls
Predictors Word Count † Rule Count† Topic Count† TTR‡ Readability§
Log User Count 0.29*** 0.20*** 0.20***−0.36***−7.83***
(0.02) (0.01) (0.01) (0.02) (0.56)
Log Fed Num 0.02 0.05* 0.08**−0.14*** 1.97
(0.03) (0.02) (0.02) (0.04) (1.12)
Age (years)−0.03***−0.02***−0.04*** 0.05*** 0.87***
(0.01) (0.01) (0.01) (0.01) (0.22)
Intercept 3.99*** 1.31*** 1.18*** 2.34*** 62.45***
(0.13) (0.08) (0.09) (0.15) (4.24)
Observations 3,356 3,356 3,356 3,059 4,357
𝑅2 / Pseudo-𝑅2 0.009 0.025 0.023 — 0.045
AIC 36,056 16,965 16,919−4,712 43,390
Note:Unstandardized coefficients shown. Standard errors in parentheses (HC3 robust for OLS).
***𝑝<0.001, **𝑝<0.01, *𝑝<0.05.
† Negative Binomial coefficients represent the log of expected counts.
‡ Beta regression model
§ OLS
with the instance), Description (provides information about what the instance converses about), Dead (tells us if the
instance is still up and running), Reg (if the instance is still allowing users to register). The last two fields are included
as filters to ensure that all Mastodon instances collected are active and contributing to a valuable selection of instances.
Prior to the rest of the analysis, we removed outlier instances upon manual inspection: libra.net, verna.social,
social.outsourcemath.com. The first two instances were legal communities with more than 150 rules, and the last had
500,000 federations but only one user, and was likely to be run by bots.
Prior to our analysis of the rules, we conducted standard preprocessing such as making all the rules lower case and
removing HTML entities, links and mentions. Upon manual inspection of a random set of rules with links, we found
that the links lead to information about privacy settings of the instance, or links unrelated to written norms of the
instance. Since our research questions are focused on the topic of the rule, the HTML entities and links are not relevant.
Translation Quality
As non-English rules account for a third of the rules in our dataset, we translated all non-English rules using Google
Translate. We assess translation quality through two checks. First, we conducted back-translation and on a random
sample of 120 rules covering a diverse range of languages and scripts. Each translated rule was re-translated back to
the original language using Google Translate, and assessed on multiple aspects using GPT-4o-mini. We queried three
questions from the model: 1) how much information loss is present? 2) how much contextual loss is present?, 3) Is there
a significant difference in tone? GPT-4o-mini provides answer on a 3-point qualitative scale (“High”, “Low”, “Moderate”).
In most cases, differences were related to tone. For example, the French phrase “être tenus responsables” (to be held
accountable) was softened in translation to “être responsables” (to be responsible), implying a subtle but not substantive
shift in assertiveness. Given the cultural and platform-specific nuances of tone, and the limited reliability of current
models in capturing it, we chose not to include tone as a formal part of our evaluation.
Manuscript submitted to ACM

22 Muralidharan et al.

Fig. 5. Distribution of lexical features across engagement levels. (a) Rule count. (b) Word count. (c) Readability of rule, measured by
Flesch-Kinaid score (d) Rule lexical diversity, measured by Type-Token ratio. Grey dots represent the values of features, while red dots
and whiskers indicate the bootstrapped means and 95% CI, respectively.
Second, we evaluated the readability of the translated rules by comparing Flesch-Kincaid Reading Ease (FRE) scores
between the original non-English rules and their English translations. FRE provides a standardized metric for assessing
textual complexity and helps us determine whether the translation alters the intended reading difficulty of the rule.
We expected a faithful translation to yield a small mean difference in FRE scores with low variance. We calculated the
absolute difference in FRE scores for each rule and normalized by the maximum FRE score (100), resulting in values on a
-1 to 1 scale. The normalized mean difference was 0 (SD=0.13), indicating that the translated texts maintain the structural
complexity of the original rules. However, FRE can only be extended to a select number of European languages, limiting
the generalization of the translation. To overcome this, we observed the lexical trends, namely word count and rule
count, in the original rule text and the translated text. We found that the trends were similar, and thus conclude that
the translation is robust for the purpose of this study.
C Engagement as Alternative Proxy of Community Size
We investigate the robustness of user count as a proxy for instance size by replicating the analysis in Section Lexical
Features, replacing user count with engagement level. Engagement level is measured as the number of statuses posted
per week within each instance. We collected these data over four weeks surrounding the data collection period and
Manuscript submitted to ACM

Federating Governance: How Community Rules Scale with Mastodon Instances 23
aggregated them accordingly. The relationships between community size and lexical features are similar when using
engagement level as a proxy. As engagement level increases, both word count (Fig. 5a, Spearman’s coefficient is
0.27(p < 0.005) and rule count increases (Fig. 5b, Spearman’s coefficient is0 .26(p < 0.005). As shown in Fig. 5c–d,
lexical diversity decreases in more active instances (Spearman’s𝜌=− 0.28), as does readability (𝜌=− 0.17), with both
correlations statistically significant (p<0.005). This is consistent with our results using instance size.
D The Impact of Rule Redundancy
In a given instance, multiple rules may articulate the same underlying norm using slightly different language. For
example, instances may treating semantically similar norms as multiple distinct rules (e.g., a single norm might be
split into separate rules such as “Respect others’ identities in full” and “Respect others’ right to engage or disengage in
conversation”, or versus combined into one rule such as “Respect others’ identities and their right to engage or disengage
in conversation. ”). Although the normative content is substantively similar, differences in linguistic granularity can
inflate the number of rules retrieved via the API. Such variation could inflate our topical analysis.
To ensure that our results are not driven by superficial differences in language use or rule segmentation, we perform
a deduplication procedure as a robustness check. Specifically, we first randomly sample pairs of rules from the entire
dataset to establish a baseline distribution of semantic similarity. This gave us a threshold of 0.25. We then compare
pairs of rules within each instance using Jaccard similarity and remove one rule from a pair if their similarity exceeds
the threshold, treating highly similar rules as redundant expressions of the same norm. This procedure reduces the
influence of stylistic or organizational differences in how instances articulate rules, while preserving substantively
distinct norms.
We rerun our topic analysis on this deduplicated dataset and find that with increase in size, the emphasis on various
topics become more equal. In comparison to smaller instances where an disproportional focus on few topics is present.
Additionally, instance size and topic count have a Spearmann correlation value of 0.324 (p«0.05). This indicates that
the overall trends do not change substantially. This suggests that our findings are not inflated by differences in linguistic
granularity or redundant rule formulations, and that the observed patterns reflect substantive normative content rather
than artifacts of rule phrasing or enumeration.
E LLM Classification Procedure
Our Rule Categorization, as described in Section 4.1, uses a few-shot prompt (n=12) to categorize the 28,000 rules into
categories adopted from [56]. Here, we present the prompt and additional experimental and variant details.
In 7 we show the prompt that was used for categorization. In our final prompt, we use twelve examples randomly
sampled across instances of varying sizes, rule types, and combinations of rule types. We incorporate a strict Q-A style
of prompt to ensure that our final output in consistent and thereby easy to parse and aggregate.
Prior to using this prompt for categorizing our entire rule dataset, we experimented with varying𝑛 for few-shot
prompting, addition of description of rule types, and model types. We experimented with different number of prompts:
eight, twelve and sixteen. We found that eight or sixteen did not give any substantial gains. Prior to experimenting with
few-shot prompting, we only provided rule types and definitions. However, we found that in this setup, LLM starts
creating it’s own categories and using varied naming conventions that made it hard to assimilate results. The addition
of rule description to the few-shot prompting did not improve its performance. Lastly, we tested across two models:
GPT-3.5-turbo and GPT-4o-mini, with temperature setting at the default 1.0. To ensure consistency, we ran the few shot
prompt 7 three times with GPT-3.5-turbo and GPT-4o-mini. GPT-4o-mini consistently outperformed GPT-3.5-turbo,
Manuscript submitted to ACM

24 Muralidharan et al.
Automated toolsHarassment
Doxxing/
Personal InfoImpersonation Dogpiling Trolling Hate SpeechIllegal Content NSFW Content W arnings Incitement of Violence
Mis/Disinfo
rmation/Conspiracy
Images
Off-topic/topic specific Links & Outside Content
Spam
Copyright/
Piracy
Advertising & Comme
rcialization
Reposting/C
rossposting
101 to 102
102 to 103
103 to 104
104 to 105
105 to 106
106 to 107
Instance Size Bin
0.01 0.13 0.05 0.01 0.01 0.02 0.28 0.13 0.07 0.06 0.05 0.05 0.04 0.02 0.02 0.06 0.03 0.03 0.00
0.02 0.15 0.06 0.01 0.01 0.02 0.27 0.13 0.10 0.08 0.06 0.06 0.06 0.03 0.03 0.07 0.02 0.04 0.01
0.03 0.15 0.06 0.02 0.01 0.02 0.26 0.12 0.11 0.10 0.06 0.05 0.06 0.04 0.02 0.09 0.03 0.06 0.01
0.04 0.14 0.06 0.03 0.01 0.02 0.25 0.13 0.13 0.10 0.07 0.07 0.07 0.03 0.04 0.09 0.03 0.08 0.01
0.04 0.14 0.07 0.03 0.02 0.02 0.24 0.13 0.12 0.10 0.08 0.08 0.05 0.01 0.02 0.11 0.02 0.10 0.01
0.01 0.12 0.06 0.04 0.02 0.01 0.21 0.16 0.16 0.15 0.11 0.09 0.14 0.01 0.05 0.07 0.07 0.04 0.02
0.05
0.10
0.15
0.20
0.25
Topic Prevalence
ActionAction Behavior Content Distribution
Fig. 6. Heat map of topic prevalence per instance, across instance size bins. Topics are deduplicated using a global Jaccard similarity
threshold. Topics are grouped into one of the four categories: Action, Behavior, Content, and Distribution.
though by just 1-2% points. Each run with GPT-4o-mini yielded an accuracy between 75-76%. Ultimately, we used the
best performing run and report that in the main paper 4.1.
F Robustness of Rule Topics as Community Topical Focus Measures
We investigate the focus of communities by using the topics inferred from rules. In this section, we examine an
alternative operationalization that uses community description. We used the ‘Short Description’ endpoint from the
Mastodon API to extract the topic of an instance. To categorize these topics, we adapted a set of topics derived from
an analysis of 5.1 billion Reddit comments between 2005 and 2018 [79]. The first author conducted inductive coding
to assess its suitability for our study, finding that the Reddit topic set provides good coverage for topics encountered
on Mastodon. Two authors independently annotated 100 randomly sampled instance descriptions in the first round
using this topic set. They then refined the taxonomy through discussion, producing a comprehensive list of topics and
definitions (see Appendix, Table F). A second round of annotation was conducted on another 100 instance descriptions
to calculate an inter-rater reliability score. Using Krippendorff’s alpha, which accounts for multiple labels [ 40], we
obtained a score of 0.79, indicating high agreement between annotators.
We then use GPT-4o to automatically annotate the full dataset of 6,660 instance short descriptions. The prompt
consisted of the taxonomy definitions (as described in Appendix, Table F), and a few randomly sampled examples.
To evaluate performance, we tested GPT-4o on the same 100-sample set coded by the authors, which yielded high
agreement with human annotations (𝛼= 0.71and 0.69). This result indicates that the prompt enabled GPT-4o to
generate high-quality annotations.
Manuscript submitted to ACM

Federating Governance: How Community Rules Scale with Mastodon Instances 25
Table 4. Taxonomy for the topics of Mastodon instances
ID Topic Description
1 General Instances that range in a wide variety of topics
2 Family & Friends Instances that explicitly mention that it is only for friends and family; or invite-only for people in the know
3 Personal Instances that explicitly mention that it is a personal instance
4 Gaming Instances that are about video games
5 Tech Instances about various tech topics such as coding, programming, open source etc.
6 Fediverse Instances are coming from other Fediverse platforms such as Pleroma or Pixelfed
7 Geographic Instances that are specifically for people of some countries or specific cities
9 Interests Instances that are for niche interests that may not fit into other cate- gories
8 Ideology Instances that specify focus on ideologies (such as equality, freedom, etc.)
10 Entertainment Instances that are about books, TV, shows, fandoms, music etc.
11 Sexual content Instances that are about sexual material including but not limited to photo-sharing and sexual role-play
13 LGBTQ Instances that explicitly state they are for people of the LGBTQ com- munity
14 News Instances that focus on conversations about news
16 Art & Culture Instances about the creation and sharing of art & culture
17 Self-improvement Instances for people to talk about ways to improve themselves and the world around them
18 Activism Instances for promoting activism related to more politically charged topics
19 Organization Instances for organizations such as companies, schools/universities, club chapter
20 Support Instances that focus on safety and inclusivity
22 Politics Instances to talk about politics and current affairs
23 Bots Instances specifically for bots
24 Religion Instance focused on conversation about faith
26 Pets Instances to talk about all sorts of pets such as dogs, cats etc.
27 N/A Instances that don’t specify purpose or target audience
28 Memes Instances about the sharing of memes and deep discussion about its cultural relevance
Manuscript submitted to ACM

26 Muralidharan et al.
We calculate the similarity between instance description topics based on their distributions of rule categories. Each
topic is represented as a 19-dimensional vector, where each dimension corresponds to the frequency of a rule category
within that topic. We normalize these vectors using TF-IDF to reduce the influence of commonly occurring categories.
This ensures that topics sharing widely prevalent categories are not falsely considered to be similar. Finally, we compute
the cosine similarity between the normalized vectors. A cosine similarity of 1 indicates that two topics have identical
distributions of rule categories, while 0 means they share no categories in common.
G Effects of Twitter/X Migration on Instance Rule Sets
Wayback Machine is an initiative to create an archive of the Internet. Previous research has used this archive to capture
historical data [47, 64]. We queried the CDX API2 to collect instance rule sets from October 2022, January 2023, and
January 2024. These timepoints correspond to the period before Twitter/X’s acquisition on October 27, 2022, and
approximately one month and one year after the acquisition, respectively.
We began by collecting data from a list of popular instances compiled by Nicholson et al. (2023). Only 10% of these
100 instances had snapshots available in the Wayback Machine prior to October 2022. Because most Personal instances
are single-use, we did not expect substantial changes or consistent archival by the Wayback Machine. Thus, to expand
coverage while maintaining relevance, we collected snapshots across multiple timestamps for all instances not tagged
as Personal (N=4,809, around 13%). Of these, only 130 instances had rule sets prior to Oct 2022 that could be recovered
from Wayback Machine, and only 60 instances contained rule sets across all three timestamps of interest—enabling
longitudinal comparison.
To analyze changes across periods 2022–2023 and 2023–2024, we measure differences in user count, rule count,
word count and rule topic categories. For user count, we record the number of users per instance at each timestamp
and calculated differences between January 2023 and October 2022, and between January 2024 and January 2023. We
average these differences across instances and report the mean and standard deviation (Table 5). Rule count is measured
similarly, based on the number of rules per instance. For word count, we calculate the total number of words in each
rule set, again reporting average differences and standard deviations across instances.
For changes in rule topic categories, we apply the prompt described in Section 4.1 to classify rules at each timestamp.
We then compare rule sets using Jaccard similarity, where 0 indicates no commonality, and 1 indicates exact match.
We use a lax threshold of 0.9 to distinguish stability from change: rule sets with similarity above 0.9 were considered
unchanged, while those below the threshold were treated as different. Yet, only 11 of 60 instances (19.05%) changed
between 2022–2023, and 5 of 60 (9.52%) changed between 2023–2024 under this criterion.
Transition User count change Rule count change Word count change Number of instances
Mean avg. Std Mean avg. Std Mean avg. Std
2022→2023 118.77 787.08 0.07 0.52 0.54 4.17 11
2023→2024 1843.09 5738.96 -0.03 0.26 -0.34 5.84 5
Table 5. Statistics of user count, rule count, word count, and rule type corresponding to different transition time points.
2github.com/internetarchive/wayback/tree/master/wayback-cdx-server
Manuscript submitted to ACM

Federating Governance: How Community Rules Scale with Mastodon Instances 27
Few-Shot Prompt for Rule Categorization
Rule types:Advertising & Commercialization, Copyright/Piracy, Doxxing/Personal Info, Harassment, Hate Speech, Images, Links
& Outside Content, NSFW, Off-topic/topic specific, Dogpiling, Reposting/Crossposting, Spam, Trolling, Incitement of Violence,
Mis/Disinformation/Conspiracy, Illegal Content, Content Warnings, Impersonation, Automated tools, Not Applicable
Q:Based on the given 𝑟𝑢𝑙𝑒𝑡𝑦𝑝𝑒𝑠 , select the appropriate categories for the rule: “No harassment, dogpiling or
doxing of other. ”
A:Doxxing/Personal Info, Harassment
Q:Based on the given𝑟𝑢𝑙𝑒𝑡𝑦𝑝𝑒𝑠, select the appropriate categories for the rule: “Be hot like Lily. ”
A:Not Applicable
Q:Based on the given 𝑟𝑢𝑙𝑒𝑡𝑦𝑝𝑒𝑠 , select the appropriate categories for the rule: “No trolling, microaggressions, or
harassment. See the Code of Conduct for the full list. ”
A:Harassment, Trolling
Q:Based on the given 𝑟𝑢𝑙𝑒𝑡𝑦𝑝𝑒𝑠 , select the appropriate categories for the rule: “No incitement of violence or
promotion of violent ideologies. ”
A:Incitement of Violence
Q:Based on the given 𝑟𝑢𝑙𝑒𝑡𝑦𝑝𝑒𝑠 , select the appropriate categories for the rule: “Conduct intended to stalk or
harass users, impede users from using the service, degrade the performance of the service, or incite others to
perform any of the aforementioned actions, is disallowed. ”
A:Copyright/Piracy, Harassment
Q:Based on the given 𝑟𝑢𝑙𝑒𝑡𝑦𝑝𝑒𝑠 , select the appropriate categories for the rule: “Respect the laws of Germany and
the Isle of Man, including those related to hate speech and defamation. ”
A:Hate Speech, Illegal Content
Q:Based on the given𝑟𝑢𝑙𝑒𝑡𝑦𝑝𝑒𝑠 , select the appropriate categories for the rule: “Account registrations are monitored
and accounts considered spam (including commercial advertising, political campaigning/propaganda, duplicate
accounts or impersonating legal entities) will be moderated or removed. ”
A:Advertising & Commercialization, Spam
Q:Based on the given 𝑟𝑢𝑙𝑒𝑡𝑦𝑝𝑒𝑠 , select the appropriate categories for the rule: “No racism, sexism, homophobia,
transphobia, xenophobia, or casteism. ”
A:Hate Speech
Q:Based on the given 𝑟𝑢𝑙𝑒𝑡𝑦𝑝𝑒𝑠 , select the appropriate categories for the rule: “Disallowed content: commercial
messages, all SPAM, and anything that could be considered NSFW (e.g. pornography). ”
A:NSFW, Spam
Q:Based on the given 𝑟𝑢𝑙𝑒𝑡𝑦𝑝𝑒𝑠 , select the appropriate categories for the rule: “No posting or reposting links to
otherwise illegal content. ”
A:Links & Outside Content, Reposting/Crossposting, Illegal Content
Q:Based on the given 𝑟𝑢𝑙𝑒𝑡𝑦𝑝𝑒𝑠 , select the appropriate categories for the rule: “Sexually explicit or violent media
must be marked as sensitive when posting. ”
A:Images
Q:Based on the given𝑟𝑢𝑙𝑒𝑡𝑦𝑝𝑒𝑠, select the appropriate categories for the rule: “Banana. ”
A:Not Applicable
Q:Based on the given rule types, select the appropriate categories for the rule:[rule text]
A:
Fig. 7. Few-shot prompt used for GPT-4o-mini rule categorization. The top section lists the 20 possible categories; the middle section
shows the 12 labeled examples; the bottom section shows the final task query with the target rule substituted in.
Manuscript submitted to ACM

28 Muralidharan et al.
0.6 0.7 0.8 0.9 1.0
Similarity
0.0
0.2
0.4
0.6
0.8
1.0CCDF
A
Activism
Art_Culture
Bots
CommunityEducation
EntertainmentFamily_Friends
FediverseGamingGeneral Geographic IdeologyInterestsLGBTQMemesNews Organization Personal Pets PoliticsReligion
Self-improvement
Sexual Content
Support
T ech
Activism
Art_Culture
Bots
Community
Education
Entertainment
Family_Friends
Fediverse
Gaming
General
Geographic
Ideology
Interests
LGBTQ
Memes
News
Organization
Personal
Pets
Politics
Religion
Self-improvement
Sexual Content
Support
T ech
B
0.60
0.65
0.70
0.75
0.80
0.85
0.90
0.95
1.00
Fig. 8. (a) CCDF and (b) heatmap of similarities between topics based on their rule categories
Manuscript submitted to ACM
