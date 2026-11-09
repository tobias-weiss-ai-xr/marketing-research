---
title: 'The language of leaving: Decoding defection via B2B customer language features'
url: https://doi.org/10.1007/s11747-026-01192-y
category: cx-retail
subcategory: empirical
date: 2026-08
venue: Journal of the Academy of Marketing Science
authors:
- Peter Nguyen
- Scott B. Friend
- Christopher P. Blocker
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s11747-026-01192-y.pdf
pages: 24
chars: 122805
fetched_at: '2026-11-08T18:47:13+00:00'
kb_version: 1
---

# The language of leaving: Decoding defection via B2B customer language features

ORIGINAL EMPIRICAL RESEARCH
Journal of the Academy of Marketing Science
https://doi.org/10.1007/s11747-026-01192-y
Lopo Rego served as Area Editor for this article.
All authors contributed equally to the study.
 Scott B. Friend
sfriend1@udayton.edu
Peter Nguyen
nguyen49@miamioh.edu
Christopher P. Blocker
chris.blocker@colostate.edu
1 Department of Marketing, Miami University, Farmer School
of Business, 800 E. High Street, Oxford, OH 45056, USA
2 Department of Management and Marketing, University of
Dayton, School of Business Administration, 300 College
Park, Dayton, OH 45469, USA
3 Department of Marketing, Colorado State University, College
of Business, 501 W. Laurel Street, Fort Collins, CO
80523, USA
Abstract
Customer language data (e.g., online reviews, call transcripts) is widely available. Yet, research in B2B contexts is still in
its early stages of analyzing a full range of customer language features to derive insight. Using an empirics-first approach,
this research sequentially identifies robust and parsimonious language features in B2B customer data that are diagnostic
of customer experiences and predictive of forthcoming purchasing decisions. The authors examine five categories of how
business customers speak: sentiment, temporality, certainty, concreteness, and personal pronouns. Results reveal that
sentiment and temporality consistently reflect customer experience and provide incremental predictive value of customer
defections within request-for-proposal (RFP) decisions. The authors demonstrate this pattern across customers’ written
(Study 1), spoken (Study 2), and pre-RFP (Study 3) language. These studies leverage empirical regularities to advance
early-stage theorizing around psychological distance and language-based models of customer defection. Illustrating the
managerial relevance of customer language features, findings show that in a customer’s collective communication prior to
an RFP decision, a 1% increase in past focus raises the odds of a multimillion-dollar RFP defection by 8.4%. The research
also equips practitioners to compute sentiment and temporality in customer language via large-language-model prompts
and statistical code, facilitating resource allocation and prioritization of customer accounts.
Keywords Customer relationship management · Customer retention and defection · Customer language data · Sentiment
analysis · Temporal language · Empirics-first
Received: 31 January 2025 / Accepted: 28 July 2026
© The Author(s) 2026
The language of leaving: Decoding defection via B2B customer
language features
Peter Nguyen1  · Scott B. Friend2  · Christopher P . Blocker3
Firms continually aim to predict and prevent customer
defection (Gupta et al., 2004; Habel et al., 2024). To this
end, predictive modeling of customer churn has advanced
considerably in recent decades, including hidden Markov
models of customer relationship dynamics (Netzer et al.,
2008; Zhang et al., 2016) and customer base analysis (Bach-
mann et al., 2021; Gupta et al., 2004; McCarthy & Fader,
2018). These methods lean on structured data such as cus -
tomer usage rates, purchase history, and satisfaction surveys
to forecast defection (Ascarza & Hardie, 2013; Lemmens
& Croux, 2006). However, researchers are concerned that
structured data impose limitations for measurement (Gupta
& Zeithaml, 2006) and ecological validity (Van Heerde et
al., 2021). Likewise, executive leaders worry that forecast -
ing and deal scoring suffer as relationship deterioration
rarely shows up first in structured systems (Marrs, 2026). To
understand customers, analysts are turning to unstructured
data (e.g., conversation intelligence), while scholars call for
new metrics and models via AI to extract real-world insights
(Marketing Science Institute, 2024).

1 3
Journal of the Academy of Marketing Science
Unstructured data represent as much as 90% of data
stored by firms (Harbert, 2021), providing ample opportuni-
ties to uncover new insights (Balducci & Marinova, 2018).
Beyond its availability, research reveals how unstructured
data generates novel insights across diverse marketing con-
texts. Notable examples include detecting electronic word-
of-mouth conversations (Vermeer et al., 2019); identifying
textual cues that reveal which sales tactics shape buyer
attention and contract outcomes (Singh et al., 2020); con-
ceptualizing unstructured data analysis to enhance predic -
tive accuracy and optimization of sales (Glackin & Adivar,
2023); and identifying textual cues in online conversations
for business-to-consumer (B2C) sales lead qualification
(Good et al., 2025). Despite these advances, firms still strug-
gle to translate customer language into actionable insights
about relationship health. Practitioners highlight the grow -
ing adoption of conversation intelligence systems that ana -
lyze customer conversations to assess relationship health,
forecast deal outcomes, and support managerial decision-
making (Drenik, 2026; Fisher, 2025; Marrs, 2026). Collec-
tively, managers and sales strategists need robust pathways
for identifying linguistic signals that reliably assess rela -
tionship health before customers defect.
A preponderance of customer language scholarship
focuses on what customers say (i.e., content topics) (Berger
et al., 2020), such as analyzing customer reviews to under -
stand gaps in customer needs. Topic modeling of what cus-
tomers say can highlight key themes in customer language,
yet content themes often stop short of providing predictions
that span customer segments (e.g., Büschken & Allenby,
2016; Timoshenko & Hauser, 2019). That is, while content
topics can effectively extract account-based insights from a
customer’s post-decision language (e.g., a customer reflect-
ing on a service experience with a seller), such analyses may
be less effective in predicting forthcoming decisions when
analyzing a customer’s pre-decision language. One factor
contributing to this limitation is the vast heterogeneity in the
content topics that customers discuss, which can vary signif-
icantly across customer segments, spending levels, product
categories, and relationship durations. This variability con -
strains the predictive utility of any single topic (e.g., a focus
on service quality by a given customer for a given supplier)
when applied to independent outcomes (e.g., predicting the
decision of another customer for another supplier based on
a service quality focus).
As an alternative, analyzing patterns of how customers
speak may produce more generalizable insights. By how,
we refer to deeply embedded patterns of customer language
that are rooted in all speech. Because these linguistic pat -
terns occur across communication contexts, they may reveal
underlying psychological states and relationship repre -
sentations in ways that are less dependent on the specific
issues customers discuss. Conversation intelligence sys -
tems similarly suggest that diagnostically meaningful sig -
nals are embedded within customer conversations, enabling
organizations to shift the operating model from hindsight
to insight; as Marrs ( 2026) notes, “when deal health is
assessed based on actual buyer conversations, not rep sen -
timent, forecast accuracy improves dramatically.” Scholars
have likewise examined the marketing relevance of sev -
eral how customer language features, including sentiment
(Ludwig et al., 2013), temporality (Packard et al., 2023),
concreteness (Packard & Berger, 2021), certainty (Rocklage
et al., 2023), and personal pronouns (Packard et al., 2018).
To date, however, much of the research on how customers
speak has been studied at the individual consumer level;
while less is known about the role of language features in
more formal, extended B2B interactions.
To advance scholarship in B2B customer language, our
research focuses on how business customers speak. Given
the growing availability of B2B customer language data and
the need for agile, managerially-relevant defection predic -
tion (Marketing Science Institute, 2024; Harbert, 2021),
we ask: Can specific features of how business customers
speak parsimoniously reflect B2B relationship health and
provide a robust signal for predicting forthcoming defec -
tion (vs. renewal) decisions? To address this aim, we lever-
age advances in language-based analysis and closely follow
strategies for empirics-first (EF) research in marketing.
Although B2B communication has been widely studied, an
EF research sequence (see Golder et al., 2023) is warranted
due to ongoing gaps in leveraging natural language for pre-
dictive insight (see Web Appendix A for an overview of EF
stages, strategies, and fitness in the current study).
Study 1 starts broadly with a dataset of 6,061 online
reviews from organizational customers. The study advances
the nascent nature of B2B customer language research by
identifying prominent how customer language features that
are associated with customer experience ratings. To extend
emergent insights from written reviews to spoken language,
Study 2 consists of 1,586 pages of interview transcripts with
organizational buyers from 230 request-for-proposal (RFP)
post-decision cases (average annual value and duration:
$5.3 M over 4.4 years). The study examines the relation -
ship between customer experience (positive vs. negative)
and how customer language features, as well as relationship
incumbency as a boundary condition for the experience-lan-
guage phenomena. Finally, to move beyond associative con-
texts, Study 3 tests the predictive efficacy of how customers
speak about incumbent suppliers prior to their RFP decision.
This study consists of 995 transcript pages from organiza -
tional buyers across 137 RFP pre-decision cases (average
annual contract value and duration: $5.9 M over 4.5 years).
While our research examines several how language features

1 3
Journal of the Academy of Marketing Science
across all studies, our EF findings demonstrate the diag -
nostic value of sentiment (emotional tone in language) and
temporality (time periods referenced in speech). We therein
produce three key theoretical contributions.
First, we contribute to theorizing about customer defec -
tion (e.g., Ascarza & Hardie, 2013; Lemmens & Croux,
2006) by advancing the role of customer language features
as a lens for detecting the conditions under which customers
are more or less likely to leave a relationship. We identify
novel insights regarding the role of sentiment and temporal-
ity to yield diagnostic and predictive insights into customer
experiences and defection decisions. Second, this research
advances the integration of psychological distance within
emotional regulation theories (Gross, 1998) and construal
level theory (CLT; Trope & Liberman, 2010) by contextual-
izing and refining psychological distancing predictions in
naturalistic B2B customer language. While sentiment and
temporality emerge as robust indicators of customer rela -
tionship experiences, other language markers do not. These
findings refine CLT with domain-specific insights and
inform marketing applications, such as forward-oriented
interventions to enhance customer retention. Third, we con-
tribute to literature bases specific to our emergent language
features. For example, we show that sentiment remains
diagnostically informative in B2B customer language
when measured using contextual language models (i.e.,
transformer-based model vs. lexicon-based approach) that
capture affective meaning embedded within professional
communication. We also advance understanding of the
state-like features of temporal language (Rush & Grouzet,
2012; Tang et al., 2020), extending prior work that empha -
sizes how temporal language influences others in interac -
tions (see Packard et al., 2023) by showing how it reflects
customers’ internal mindsets.
Beyond research and theory, we offer clear and com -
pelling pathways for managerial relevance. Chief revenue
officers and other leaders aiming to use unstructured data,
such as buyer conversations, for resource allocation (e.g.,
prioritizing customer accounts) and resource intensity (e.g.,
customer-facing strategies) decisions (cf., Marrs, 2026) can
directly leverage our findings and methodology. Empiri -
cally, we demonstrate how customer sentiment and tempo -
rality can predict the likelihood that customers will defect
from (vs. renew) upcoming RFP bids. For example, based
on the collection of a customer’s communication prior to
the RFP decision, and holding all else equal, a 1% increase
in the customer’s focus on past experiences increases the
odds that a multimillion-dollar RFP leads to defection (vs.
renewal) by 8.4%. Analysis demonstrates how our findings
provide incremental value beyond that of expert consultants
who help forecast defection. To further support practical
applications, we provide prompts for large language models
(e.g., ChatGPT) and statistical code to help firms conduct
and scale the computation of sentiment and temporality in
their customer language data.
Stage 1: Identify opportunity
Given the nascent stage of theory development for our
research question, as well as the emergent nature of lan -
guage-based investigations in marketing (e.g., Packard &
Berger, 2021, 2017), we leverage an EF approach with mul-
tiple sources of real-world data to create insights for theory
development. That is, rather than formalizing hypotheses
based upon a weak theory-driven lattice, we apply EF cri -
teria to advance our research questions. Following estab -
lished stages and strategies (see Golder et al., 2023; Nanni
& Ordanini, 2025), we carefully align our studies to justify
and apply this research sequence (see Web Appendix A).
Within the EF framework, Stage 1 identifies opportuni -
ties by exploring real-world inspiration, novelty, and rel -
evance, while evaluating the suitability of an EF approach.
Our research framework (see Fig. 1) depicts the conceptual
relationship between customer’s net positive or negative
evaluation with a supplier and their subsequent decision to
stay (renew) or leave (defect) when the contract expires.
Within this framework, we assess whether these relation -
ship experiences are reflected in how they communicate
(sentiment, temporality, concreteness, certainty, and per -
sonal pronouns) and whether these linguistic patterns serve
as reliable signals of renewal versus defection decisions. We
provide a foundation for our empirical approach by review-
ing relevant scholarship and theory.
Customer language
Marketing puts a premium on the “voice of the customer”
to understand and predict buyer behavior. For example,
firms use unstructured data from customers’ spoken lan -
guage to identify insights regarding sales forecasting,
real-time customer interactions, and strategic decisions
(Glackin & Adivar, 2023). Since spoken language arises
naturally, this type of data is high in ecological value
(Van Heerde et al., 2021) and external validity (Berger et
al., 2020). Customer language also addresses limitations
of explicit feedback in sales research (Friend & Johnson,
2015), enabling scholars to examine when and why lan -
guage matters (Berger et al., 2020; Packard et al., 2023).
That is, customer language may reveal perspectives that
elude more isolated, directed measures; offering insight
into customers’ needs and goals (Timoshenko & Hauser,
2019). For example, research shows that language reveals

1 3
Journal of the Academy of Marketing Science
customers’ consideration sets (Netzer et al., 2012) and
helps predict eventual loan defaults (Netzer et al., 2019).
Despite significant advances in language research in
marketing (see Web Appendix B), we find three impor -
tant gaps that revolve around the analytical focus, the
exchange context, and the decision context for predic -
tion. First, research on customer and marketer language
has primarily examined how language influences oth -
ers (e.g., persuading customers; Packard et al., 2023),
with far less attention to how language reveals the inner
thoughts, attitudes, and intentions of the speaker  (Jackson
et al., 2022). By shifting this focus, scholars can lever -
age linguistic analysis to help firms assess churn risk and
proactively trigger recovery strategies. Second, much
of the extant research in marketing on language centers
on B2C exchange contexts and consumers (e.g., Pack -
ard & Berger, 2024), while less is known about whether,
and to what extent, language features help understand
and predict phenomena in the extended interactions of
B2B relationships . This context is particularly valuable
given the increasing availability of B2B customer lan -
guage data and the high value account sizes in B2B rela -
tionships. Third, while language research in marketing
largely focuses on customers’ post-decision language
(e.g., customer reflections of consumption experiences)
for diagnostic insights (e.g., Büschken & Allenby, 2016),
less attention has been paid to customers’ pre-decision
language  (e.g., customer communications prior to out -
comes). Pre-decision language is a data source that can
be valuable in helping firms forecast customers’ behav -
iors and decisions.
Theory-language signposts for customer defection
To gain directional guidance in our emergent theorizing, we
overlay our review of theory and language features against
the research context. Specifically, we surface conceptual
lenses that may explain buyers’ exit-oriented mindsets
within B2B relationships and their decisions to renew or
defect. We assess that some perspectives, such as the degree
of formality or syntactical structure in buyer communica -
tion, carry limited informational value. Industry conven -
tions or the technical nature of a solution being discussed
may shape buyer communication but offer little diagnostic
insight into the health of the supplier relationship.
In contrast, the concept of psychological distance pro -
vides theoretical guidance for understanding how buyers
experience and evaluate supplier relationships. Psycho -
logical distance, as featured in CLT (Trope & Liberman,
2010) and emotional regulation (Gross, 1998), refers to the
cognitive and affective processes through which individu -
als separate themselves from a person or relationship that
feels less relevant or aligned with their goals. Distancing
plays a central role in how individuals process and discuss
unfavorable experiences and relationships (Maglio 2020b).
Although psychological distancing is not always explicitly
articulated, language can provide reliable signals of one’s
distancing from stimuli (Nook et al., 2017).
While both emotional regulation and CLT are grounded
in psychological distancing, they provide complementary
guidance regarding how distancing may manifest in cus -
tomer language. Emotional regulation theory emphasizes
how individuals manage negative affect by changing how
they interpret and communicate about aversive experiences
(Gross, 1998). Consequently, emotional distancing is most
Fig. 1 Research framework

1 3
Journal of the Academy of Marketing Science
likely to be reflected through changes in sentiment, as cus-
tomers increasingly communicate about supplier relation -
ships using more negative affective language. In contrast,
CLT focuses on how increasing psychological distance
changes individuals’ mental representations of relation -
ships (Trope & Liberman, 2010). Such shifts may mani -
fest through multiple linguistic dimensions associated with
psychological distance, including temporal framing and
the level of abstraction used to describe experiences. For
example, drawing on evidence that temporal language can
signal psychological distance (Nook et al., 2017; Packard
et al., 2023), greater emphasis on past-oriented language
may reflect increasing relationship disengagement, as com-
munication shifts from ongoing experience to retrospective
evaluation.
Some perspectives, such as CLT, assume that distancing
occurring along one dimension is correlated with distanc -
ing in other dimensions. However, extant research shows
that this interdependence is not always uniform, particularly
in domains where situational factors shape how individuals
communicate about and interpret experiences (Brügger et al.
2016; Maglio 2020a; Stephan et al. 2010). Viewed through
a psychological-distancing lens, deteriorating buyer-sup -
plier relationships would therefore be expected to mani -
fest through linguistic patterns reflecting both affective and
cognitive distancing. Yet, while theory provides directional
guidance and suggests several plausible manifestations, it
provides limited specification regarding which linguistic
expressions should consistently emerge as the strongest
diagnostic indicators in naturalistic B2B communication.
How customers speak
Guided by the psychological-distancing perspective, the
next question becomes how such distancing may manifest
in customer language. Whereas what language reflects the
thematic content of discourse, how language reflects broader
patterns that are common across communication contexts.
The latter is particularly useful when topical themes (in
what language) are too numerous and heterogenous to yield
sufficient statistical power for prediction. Accordingly, how
language features have the potential to reveal underlying
psychological states and relationship representations in
ways that are less dependent on the specific products, ser -
vices, or issues being discussed.
Prior language research has identified several prominent
how language features that have been linked to customer
perceptions and behavior, including sentiment, temporal -
ity, concreteness, certainty, and personal pronouns. Table 1
provides an overview of these language features, including
their meaning and applications for understanding customer
judgments and marketplace behavior. However, customer
language scholarship—particularly in B2B predictive con -
texts—remains in an early stage of theoretical development.
While psychological distancing serves as the conceptual
lens motivating our search for informative language features,
our broader review of marketing, management, linguistics,
and psychology (Web Appendix B) identified numerous
plausible language features and theoretical perspectives that
could explain customer language. These perspectives often
yield competing or overlapping interpretations regarding
which linguistic manifestations should emerge and why.
Accordingly, rather than deriving formal hypotheses from
an equivocal theoretical foundation, we adopt an empirics-
first approach (Golder et al., 2023; Web Appendix A) that
begins with the prominent how language features identified
in prior research and allows robust empirical regularities to
guide subsequent theorizing.
Stage 2: Explore terrain
In Stage 2, we explore the EF terrain by acquiring data,
listening to the data, and assessing closure. Across three
studies, we examine the relationship between how custom-
ers speak and customer evaluation measures, including
customer experience ratings and defection (vs. renewal)
decisions. Each study provides distinct insights regarding
language features, with the progression of each study nar -
rowing our empirical scope, mitigating alternative explana-
tions, and enhancing generalizability. An overview of each
study is provided in Table 2 and a data dictionary of the
variables utilized across the studies is presented in Web
Appendix C.
Data for Study 1 consist of 6,061 online reviews from
organizational customers on G2.com, an online review plat-
form for business software and services. The aim of this
study is to examine the extent to which prominent how cus-
tomer language features vary as a function of B2B customer
experience ratings. The online review context provides a set
of customer language datapoints large enough to provide a
level of statistical power that can detect relevant customer
language features. Further, the structured nature of review
data allows for the control of potential buyer/seller con -
founds. To extend from written to spoken language, Study
2 consists of 1,586 pages of interview transcripts with cus -
tomers from 230 RFP post-decision cases. Post-decision
language is studied, as such data enables exploration of rela-
tionship incumbency as a boundary condition for customer
experience and language phenomenon. To extend beyond
the post-hoc associations, Study 3 tests the predictive effi -
cacy of how customers speak about incumbent suppliers
prior to the RFP decisions. This study consists of 995 tran -
script pages from customers across 137 RFP pre-decision

1 3
Journal of the Academy of Marketing Science
cases. Controlling for what customers say (content topics)
and contract features (contract duration, contract price, RFP
competitiveness), this study compares whether—and to
what extent—incumbent customers’ how language predicts
defection outcomes.
Study 1: Identifying relevant how customer
language features
The purpose of Study 1 was to test whether how custom-
ers speak is reflective of customer experience ratings. Based
on our review of language research and theories that exam-
ine psychological distance in relationships, we considered
prominent language features: sentiment, temporality, con -
creteness, certainty, and personal pronouns. Our objective
was to identify language features that correlate with cus -
tomer experience ratings. Although various relationships
may exist between language features and customer experi -
ence, we focused on strong linear relationships due to their
diagnostic value and clarity. This focus aligns with our EF
approach, as linear relationships provide a foundation for
understanding how language features relate to customer out-
comes, especially when customer experience is measured
binarily (positive vs. negative, as in Study 2). Further, in lin-
ear relationships, specific values of a language feature indi-
cate either positive or negative experiences, enhancing their
predictive utility. By contrast, non-linear relationships, such
as U-shaped, are less diagnostic, as similar feature values
may correspond to both positive and negative experiences.
Method
Data
The study consists of data collected from G2.com, an online
review platform for business software (e.g., Salesforce) and
professional services (e.g., Deloitte Consulting). We col -
lected two sets of data: (a) reviews about the same service
provider from multiple different reviewers (by-service-
provider data) and (b) reviews by the same reviewers about
multiple different products (by-reviewer data). The purpose
Table 1 Prominent how language features for diagnosing and predicting customer decisions
How language
feature
Meaning and application for under-
standing customers
Research insights and linguistic theories: linkages between language features and
customer perceptions
Sentiment • Reflects emotional tone
• Reveals affective information about
customer (dis)satisfaction, trust, and
commitment within relationships
• Sentiment valence associated with relationship satisfaction (Ngobo et al.,
2012)—also shapes outcomes, cf., servqual (Ahmad & Guzmán, 2021) and pur-
chase intentions (Hsu et al., 2017).
• Valenced words can mask granular language effects explained using politeness
theory (Brown & Levinson, 1987) or speech act theory (Villarroel Ordenes et al.,
2017) to clarify perceptions.
• Sentiment may lack interpretive value without language style match (Ludwig et
al., 2013).
Temporality • Reflects emphasis on time period for
one’s experiences and relationships
• Reveals customers’ relative mental
attention for past (e.g., regret), present
(e.g., relevant now), or future (e.g.,
goal-seeking) experience
• Past-focused concerns are frequently construed with more negative valence than
present or future concerns—negative past focus may reflect broken psychological
contracts (Peltokorpi et al., 2023; Shipp et al., 2022).
• Temporality draws on temporal focus theory and time perspective theory to
explain how attention to time periods is associated with negative perceptions
(past), immediacy (present), or goals (future) (Packard et al., 2023; Shipp &
Aeon, 2019; Tang et al., 2020).
Concreteness • Reflects use of detailed and sensory
versus abstract and general language
• Reveals customer comprehension,
memory, engagement, and mental
distance with market experiences
• Concreteness signals psychological proximity and heightened cognitive
engagement, making it a window into how mentally “close” or relevant a person
perceives a relationship or experience (Short et al., 2018).
• Concrete language reveals what customers attend to and understand—with con-
crete feedback linked to higher satisfaction based on processing fluency (Packard
& Berger, 2021).
Certainty • Reflects confidence or assurance
• Reveals customers’ confidence in
exchange partners, marketplace com-
munication, and outcomes
• Certainty language reflects a person’s belief strength and confidence in claims
or future outcomes—with its absence indicating doubt, hedging, or ambiguity
(Rocklage et al., 2023).
• Subtle expressions of certainty can reveal buyers’ implicit stance or intent, align-
ing with speech act theory or cognitive appraisal theory (Packard et al., 2023).
Pronouns • Reflects pronoun usage, e.g., “I”,
“we”, and “you”
• Reveals customers’ perceptions of
exchange partners; first-person plural
(we) signaling collaborative and first-
person singular (I) individualistic
• Pronoun usage reflects individuals’ emotional attachment—with greater use of
“we” or “you” signaling perceived closeness and agency in the exchange (Chung
& Pennebaker, 2011).
• In line with communication accommodation theory, first-person singular (I)
versus first-person plural (we) pronouns distinguish self-focus from other-focus,
revealing whether people frame relationships as expressive or instrumental (Pack-
ard et al., 2014, 2018).

1 3
Journal of the Academy of Marketing Science
of collecting both datasets was to control for the same prod-
uct and the same reviewer in our analyses, safeguarding that
key findings about how customers speak are a function of
customer experience levels and not confounded by prod -
uct (selection bias) or buyer (individual trait differences)
characteristics.
To ensure an adequate degree of elaboration and infor -
mation diagnosticity in the reviews (Mudambi & Schuff,
2010), we collected only reviews with at least 50 words. For
the by-service-provider data, we collected 5,482 reviews
across 70 different software/service offerings. For the by-
reviewer data, we collected 579 reviews generated by 70
different customers. Additional details on the data collection
are presented in Web Appendix D.
Variables and analysis
Our goal was to examine how the different customer lan -
guage features varied as a function of customer experience
ratings. Customer experience (CustomerExperience) was
captured by the reviewer’s assigned star rating, a value
ranging from 0 (Terrible) to 5 (Excellent) in 0.5 increments.
Given our EF approach, we considered several language
features. To enable cross comparison of the language fea -
tures, we standardized each language feature by provider
and by reviewer for our two datasets, respectively. Given
the numeric nature of customer language outcome vari -
ables, analyses were conducted using ordinary least square
Table 2 Overview of Studies 1–3
Study 1:
Identifying relevant customer language
features from B2B online reviews
Study 2:
Extending insights from written
reviews to customer spoken language
Study 3:
From association to prediction of defec-
tion via B2B customer language
Data Format Written language
(6,061 online B2B reviews)
Spoken language
(1,586 Transcript Pages
230 RFP Cases)
Spoken language
(995 Transcript Pages
137 RFP Cases)
Language
Data Structure
Post-hoc (associative);
customer written language
occurs after having used product
Post-hoc (associative);
customer spoken language
occurs after interaction with sales team
and RFP decision
A-priori (predictive);
customer spoken language occurs before
RFP decision
Incremental
Benefits of
Research
Context
Context enables collection of large sample
size to ensure sufficient power to detect
relevant language features.
Collection of online reviews by the same
customer and about the same supplier
enables control for buyer/seller confounds.
Context enables the extension of cus-
tomer insights from written to spoken
language.
Post-hoc nature of language data
enables the testing of incumbency sta-
tus (i.e., new vs. existing relationship)
as a key boundary condition.
Context enables testing the predictive
efficacy of language features established
in previous two studies.
Context contains data about human
expert assessments, enabling the com-
parison of the effect size of language
features to human experts.
Study Focus How Customers Communicate ~ B2B
Customer Experience
Relationship Incumbency as a Bound-
ary Condition
How Customers Communicate →
RFP Decision
Are there features of how customers speak
that are reflective of customer experience
ratings?
Empirically assess the relevance of the
prominent customer language features:
sentiment, temporality, concreteness,
certainty, and personal pronouns.
Do the relevant features of how
customers speak extend from written
reviews to spoken language?
How does relationship incumbency
influence the diagnostic value of how
customers speak?
Do the relevant features of how custom-
ers speak predict customer defection (vs.
renewal) decisions?
What are the relative predictive values
of these language features and how
do they compare with human expert
assessments?
Sentiment ✓ ✓ ✓Temporality ✓ ✓ ✓Certainty × ×  ×
Concreteness × ×  ×
Pronouns × ✓  × Within-Sub-
jects Robust-
ness Analysis
By-reviewer data; language standardized
by same reviewer across different product
experiences
Language specificity moderator (sup-
plier-specific vs. general responses)
Within-subjects language measures (con-
trols for customer’s baseline speech)
Incremen-
tal Study
Findings and
Summary of
Results by
Language
Feature
Across prominent language features,
sentiment and temporality are the leading
factors associated with customer experi-
ence ratings.
Negative customer ratings are associated
with greater negative emotional language
and greater past temporal language.
The diagnostic value of sentiment and
temporality remain prominent in B2B
customer spoken language.
The patterns on customer how lan-
guage is salient for incumbent (vs.
prospective) relationships.
Temporality and sentiment are predictive
of defection decisions, with their predic-
tive efficacy operating separately; effects
comparable to human experts.
A 1% decrease in sentiment (1% increase
in past focus) increases the odds an RFP
leads to a defection by 1.6% (8.4%).
✓: statistically significant relationship; ×: no statistical relationship

1 3
Journal of the Academy of Marketing Science
regression, while controlling for number of words and
words per sentence (see Table WAD.1).
Sentiment Sentiment analysis was conducted using the
DistilBERT model, a transformer-based architecture fine-
tuned for sentiment analysis (Devlin et al., 2019). The anal-
ysis was implemented in R using the reticulate package to
interface with Python’s ‘transformers’ and ‘torch’ libraries.
The review texts were tokenized with DistilBERT, applying
truncation and padding to a maximum length of 512 tokens.
The model generated logits, which were converted to prob-
abilities using a softmax function. Sentiment scores were
computed by scaling the positive probabilities by product
offering (by-service-provider data) and by reviewer (by-
reviewer data). The statistical code to conduct the analysis
in R is provided in Web Appendix E.
While research reports relatively high accuracy for Dis -
tilBERT-based sentiment analysis (85–94%; Minaee et al.,
2021; Ng et al., 2023), we sought to ensure robustness in
our construct measurement. We therefore computed senti -
ment using two widely adopted lexicon-based approaches:
AFINN lexicon (Nielsen, 2011) and Linguistic Inquiry and
Word Count (LIWC) (Boyd et al., 2022). Additional details
are provided in Web Appendix D.
Temporality Temporality in language is operationalized
in two related but distinct ways. One approach focuses on
grammatical verb tense, distinguishing between past and
present tense verbs (e.g., “we are evaluating the platform”
vs. “we evaluated the platform”) (Packard et al., 2023). A
second approach captures broader temporal references using
lexicons that include both verbs and non-verbs referring to
time (e.g., “already,” “currently,” “presently,” “previously”)
(Pennebaker & Stone, 2003). The verb-based approach
isolates grammatical tense shifts in actions described by
the speaker, whereas the lexicon-based approach captures
a wider range of temporal framing cues embedded in lan -
guage. To ensure patterns are not dependent on a specific
operationalization, we employ both measures.
The verb-tense operationalization was conducted
using part-of-speech (POS) tagging (udpipe package in
R; Wijffels, 2023) to categorize words into grammatical
classes (e.g., noun, verb, adjective). The udpipe package is
well suited for this context because its POS tagging model
not only detects verbs but also identifies whether verbs
are used in past or present tense. For example, verbs such
as “used” and “implemented” are classified as past tense,
whereas verbs such as “use” and “implement” are classified
as present tense. The model was selected due to its ease of
implementation and high POS tagging accuracy of approxi-
mately 95% (Wijffels, 2023).
As noted by Packard et al. ( 2023), English does not
contain a grammatical future tense comparable to past and
present tense. Accordingly, our primary focus is on past
and present temporal language. The POS-based tempo -
rality score was calculated as the number of verbs in past
tense divided by the total number of past and present verbs
in a review. Although POS tagging can require additional
processing time depending on the size of the dataset, the
method is open-source and scalable. We provide the R code
used for this analysis in Web Appendix E.
We also operationalize temporality using the tempo -
ral lexicons from LIWC (Boyd et al., 2022). Unlike the
POS-based approach, LIWC captures both verbs and
non-verbs that reference time. For example, past-oriented
non-verb terms may include terms such as “previously” or
“yesterday,” whereas present-oriented non-verb language
may include terms such as “now” or “today.” LIWC also
includes a lexicon of future-related terms (e.g., “will,”
“next,” “soon,” “tomorrow”). Consistent with prior research
(Packard et al., 2023), we observe that the vast majority of
temporal references in customer language occur in the past
or present (97.2%), with relatively few references to the
future (2.8%).
Across our datasets, the POS-based and LIWC-based
measures of past temporal language are highly correlated
(r = .79, p < .001). The use of the two operationalizations
ensures observed patterns reflect temporal framing in cus -
tomer language rather than artifacts of a measurement
approach. For parsimony, we report the POS-based tem -
porality measure in the main analyses and provide results
using the LIWC-based measure as robustness checks (see
Web Appendix D).
Concreteness Concreteness in language was assessed using
the concreteness ratings provided by Brysbaert et al. (2014).
The lexicon contains 39,954 words, with each word con -
taining a concreteness score between 1 and 5. Examples
of high concreteness words include “armchair,” “bird,”
“comb,” and “flower.” Examples of low concreteness words
are “spirituality,” “belief,” “ambivalent,” and “idealistic.”
Scores were computed using the summation of word-con -
creteness values divided by the total number of words in
the response.
Certainty Certainty scores were computed using the LIWC
certainty word dictionary (Boyd et al., 2022), including
words such as “absolutely,” “always,” “confident,” and
“perfect.” Certainty scores were computed by taking the
total number of words in a given response contained in the

1 3
Journal of the Academy of Marketing Science
certainty lexicon and then divided by the total number of
words in the response.
Personal pronoun use Personal pronouns were captured
via plural (vs. singular) first-person use. First-person pro -
noun use was computed using the LIWC first-person sin -
gular pronoun and LIWC first-person plural pronoun word
dictionaries (Boyd et al., 2022). The first-person singular
pronoun dictionary includes terms such as “I,” “I’d,” “me,”
and “myself.” The first-person plural pronoun diction -
ary contains terms such as “we,” “us,” “let’s,” and “ours.”
First-person voice scores were computed by taking the total
number of first-person plural terms (“we”) divided by the
total number of first-person pronoun terms (“I” + “we”) in
a given review.
Results
Sentiment
We first examine how customer language sentiment var -
ied as a function of customer experience ratings. We find
a strong positive relationship between the two variables
(DistilBERT: b = 0.157, SE = 0.009, p < .001; Cohen’s
f2 = 0.06; see Fig. 1). The finding is also pronounced across
the lexicon-based measurements of language sentiment
(AFINN: b = 0.096, SE = 0.009, p < .001; LIWC: b = 0.053,
SE = 0.009, p < .001) and is robust in the by-service-pro -
vider and by-reviewer datasets ( b = 0.122, SE = 0.018, p <
.001; Cohen’s f2 = 0.08; see Fig. WAD.1). The by-provider
and by-reviewer results help rule out seller (selection bias)
and buyer (individual trait differences) characteristics as
confounds of the experience-language relationship. An
overview of the regression results for all the customer lan -
guage features from the two datasets are provided in Tables
WAD.2 and WAD.3.
Temporality
Next, we examine the role of temporality in language—
examining the salience of terms in the past and present
focus lexicons of LIWC, separately, as a function of cus -
tomer experience ratings. While we observe no statistical
relationship between customer experience ratings and pres-
ent temporal language (by-service-provider data: p = .59,
by-reviewer data: p = .08), negative customer experiences
are associated with greater past temporal language (by-
service-provider data: b = -0.050, SE = 0.009, p < .001; by-
reviewer data: b = -0.056, SE = 0.019, p = .003).
Using present temporal language as a baseline, we cre -
ate a composite measure of past temporality (PastTemporal-
ity), operationalized as the number of past temporal terms
divided by all temporal terms (i.e., LIWC past / [LIWC past
+ LIWC present]). Consistent with the past component of
temporal language, we find that this composite measure
is negatively associated with customer experience ratings
(by-service-provider data: b = -0.050, SE = 0.009, p < .001,
Cohen’s f2 = 0.004; by-reviewer data: b = -0.059, SE = 0.019,
p = .002, Cohen’s f2 = 0.02).
To ensure results are agnostic to our measurement
approach, we rerun the analysis based on the verb tense
approach (Packard et al., 2023), where we compute the pro-
portion of past tense verbs relative to all verbs used in the
review.1 Rerunning our analysis with the purely verb-based
operationalization of past temporality, we find the same pat-
tern holds (by-service-provider data: b = -0.061, SE = 0.009,
p < .001, Cohen’s f2 = 0.007; by-reviewer data: b = -0.072,
SE = 0.019, p < .001, Cohen’s f2 = 0.03). That is, negative
customer experiences are associated with a greater propor -
tion of verbs used in their past tense forms (see Fig. 2B).
Certainty
Using the certainty lexicon provided by LIWC, we exam -
ine how language certainty in customer reviews varies as
a function of customer experience ratings. While we find
that customer experience ratings are positively associated
with language certainty in the by-service-provider data
(b = 0.034, SE = 0.009, p < .001, Cohen’s f2 = 0.003), this
pattern is only marginally significant in the by-reviewer data
(b = 0.036, SE = 0.019, p = .056, Cohen’s f2 = 0.007), with an
overall small effect size across the by-service-provider and
by-reviewer data.
Concreteness
We examine how the concreteness in customer language
varies as a function of customer experience. We find a weak
negative linear relationship between the two variables in the
by-service-provider data ( b = -0.023, SE = 0.009, p = .01,
Cohen’s f2 = 0.0008) and no statistical significance in the
by-reviewer data (b = 0.020, SE = 0.019, p = .29, Cohens’
f2 = 0.002), with an overall small effect size across the by-
service-provider and by-reviewer data.
1  As expected, this past temporality measure based on solely verb
tense has a high correlation ( r=.90) with the LIWC-based measure (a
mixture of verbs and non-verbs).

1 3
Journal of the Academy of Marketing Science
Fig. 2 Exploring how B2B customers speak as a function of customer
experience valence. Note: A–E explore variance in customer lan -
guage features as a function of customer star ratings in G2 software
and service reviews (study 1). These figures are presented with the by-
service-provider data (see Web Appendix D for the by-reviewer data
results). All y-axis variables are standardized by product. Across the
by-service-provider and by-reviewer data, sentiment and temporality
are consistently significant across customer experience ratings. F–J
explore variance in B2B customer language features as a function of
customer experience valence (Study 2)

1 3
Journal of the Academy of Marketing Science
Personal pronouns
We examine how the use of personal pronouns, specifi -
cally plural (“we”) versus singular (“I”) first-person pro -
nouns, vary by customer experience ratings. While we find
no statistical relationship in the by-service-provider data
(b = 0.015, SE = 0.009, p = .10, Cohen’s f2 = 0.0007), we
find a weak negative relationship in the by-reviewer data
(b = -0.037, SE = 0.019, p = .048, Cohen’s f2 = 0.007), with
a small effect size across the by-service-provider and by-
reviewer data.
Key patterns across product types
A central goal of our research is to examine the diagnostic
role of language in B2B contexts, particularly those charac-
terized by organizational relationships. G2 contains reviews
from organizational customers of both business software
products (e.g., Adobe Experience Manager, HubSpot,
Hootsuite) and professional services firms (e.g., Accenture,
Deloitte Consulting, IBM Consulting). In our by-service-
provider data, 20.6% of reviews pertained to professional
services and 79.4% to software products.
To examine whether the observed relationships between
customer experience and language features generalize, we
estimate the focal models separately for software products
and professional services. Across both types, we observe
consistent patterns: more negative customer experiences are
associated with more negative sentiment (software products
only: b = 0.168, SE = 0.01, p < .001; professional services
only: b = 0.120, SE = 0.020, p < .001) and a greater empha -
sis on past temporal language (software products only: b =
-0.054, SE = 0.01, p < .001; professional services only: b =
-0.094, SE = 0.020, p < .001).
Key takeaways
Across the language features examined, sentiment and tem-
porality emerge as the most diagnostically robust indicators
of customer experience. More negative experiences are con-
sistently associated with more negative language sentiment
and a greater emphasis on past temporal language. These
patterns hold when controlling both provider and reviewer,
mitigating concerns related to (seller) selection bias and
(buyer) trait differences as alternative explanations.
These patterns also generalize across organizational
software and professional services contexts, where interac -
tions are more relational and embedded within buyer–seller
exchanges. This result thus demonstrates that the diagnostic
value of sentiment and temporality extends beyond transac-
tional product evaluations to relational contexts. Such gen -
eralizability establishes sentiment and temporality as stable
linguistic signals that can be carried forward into contexts
where buyer–seller relationships, and their embedded deci -
sions, are more consequential.
To further assess robustness, we test and replicate our B2B
insights with a supplemental B2C study (see Web Appendix
F). Using Yelp.com restaurant reviews ( N = 182,097), we
continue to find in this supplemental study that both senti -
ment and temporality are the leading language factors asso-
ciated with customer experience. Building on these insights,
we examine how these linguistic signals manifest in spoken
contexts where buyers communicate about suppliers and
make consequential relationship decisions.
Study 2: Extending insights to customer
spoken language
The purpose of Study 2 is to investigate the features of how
customers speak established in Study 1’s written online
reviews and extend the insights to the spoken language of
organizational buyers. In addition, Study 2 examines the
contextual boundaries under which language features pro -
vide diagnostic signals of customer experience in B2B rela-
tionship contexts.
A key feature of B2B purchasing decisions is that buyers
evaluate incumbent suppliers and prospective alternatives
during the decision process. Yet, language directed toward
these suppliers occurs at different relationship stages. Dis -
cussions about incumbents are typically grounded in prior
experiences, whereas discussions about prospective suppli -
ers focus on proposals, with little or no prior experience.
This structural difference raises the possibility that observed
differences in sentiment or temporal framing may reflect
relationship stage rather than customer experience levels or
decision signals. To account for this distinction, we explic -
itly model relationship incumbency and examine whether
the diagnostic relationship between customer experience
and language patterns holds within, and across, these rela -
tionship contexts.
Method
Data
The data for Study 2 consisted of 1,586 single-spaced pages
of the verbatim text of 230 in-depth interviews with orga -
nizational buyers. The interviews were conducted after the
buying firm made the decision to either accept or reject an
RFP bid from the supplier. The post-hoc nature of the cus -
tomer language data provides clear evidence for temporal
precedence, where customer language is distinctly col -
lected after a positive or negative experience milestone.

1 3
Journal of the Academy of Marketing Science
Additionally, the post-hoc nature of the language data
contains thorough details about relationship incumbency,
enabling us to examine how customers speak about incum -
bent (past/current) versus prospective (future) suppliers.
As we note, these relationship contexts differ structurally:
discussions of incumbent suppliers are grounded in accu -
mulated experience, whereas discussions of prospective
suppliers arise from interactions during the RFP process
(e.g., meetings and presentations) and are thus more for -
ward-looking and evaluative in nature.
All cases were independent from one another, spanning
seven different supplier firms across a variety of industries:
food service, financial services, office supplies, transporta -
tion, shipping and logistics, food and beverage, and waste
management. Across all cases, the annual valuation of the
related contract proposals ranged from $100K to $260 M,
with a median of $2.0 M (mean = $5.3 M; SD = $18.1 M).
The duration of the contract proposals ranged from 1 year
to 10 years, with a median contract duration of 4 years
(mean = 4.4 years; SD = 2.5 years).
Interviews were collected for each supplier firm by a
research consultancy firm tasked to provide case-by-case
vendor audits, specifically to help suppliers understand why
customers opted to accept or reject their RFP bids. All inter-
views were conducted in English, recorded and transcribed
verbatim to text. Each interview was guided by a structured
protocol that asked respondents to reflect deeply on their
experiences and to provide their unfiltered, honest perspec -
tives. While several of the open-ended questions are more
naturally grounded in prior experience, analogous questions
for prospective suppliers are formed based on observed
interactions during the RFP process.
Variables
Our objective was to examine the extent to which relevant
how customer language features established in Study 1 vary
as a function of B2B customer experience. Customer experi-
ence is operationalized as a binary variable of either positive
(1: the customer chose to accept the RFP bid) or negative (0:
the customer chose to reject the RFP bid). The prominent
language features (sentiment, temporality, certainty, con -
creteness, and personal pronouns) were operationalized the
same as in Study 1 (Boyd et al., 2022; Devlin et al., 2019;
Wijffels, 2023).
In addition to examining whether how customers speak
reflects B2B customer experience, we account for contex -
tual features of the buying process that may systematically
shape language patterns. In particular, buyers discuss both
incumbent suppliers, with whom they have prior interaction
history, and prospective suppliers, whose evaluation is likely
to be proposal-specific and forward-looking. Because these
relationship stages naturally generate different types of lan-
guage (e.g., retrospective versus prospective framing), we
include relationship incumbency (RelationshipIncumbency:
1 = incumbent, 0 = prospective) as a contextual feature of the
decision environment. We further treat relationship stage as
a boundary condition that influences the depth and diagnos-
tic value of language.
We also examine whether the diagnostic strength of lan -
guage signals vary depending on whether respondents are
discussing the focal supplier directly or generally speaking
about the buying process. We thus include supplier-specific
questions (SupplierSpecificLanguage: 1 = supplier-specific,
0 = general) as a contextual moderator of the relationship
between customer experience and language features. This
distinction allows us to differentiate between experience-
based evaluations (more prevalent in incumbent contexts)
and interaction-based evaluations (more prevalent in pro -
spective contexts), thereby reducing potential confounding
due to differences in experiential grounding. Descriptive
statistics on these variables, validation of the supplier-spe -
cific language measure, and data preprocessing steps are in
Web Appendix G.
Analysis
Due to the nested nature of the data (question-responses
nested by contracts, contracts nested by suppliers), we used
a mixed-effect model. Specifically, we treated the identifica-
tion of contracts and the collection of contracts by suppliers
as random effects.2 Our linear mixed-effects models regress
the dependent variable—the focal language feature—on our
main independent variable (CustomerExperience), contex -
tual moderating variables (SupplierSpecificLanguage, Rela-
tionshipIncumbent), and control variables (AnnualPrice,
ContractDuration).
Results
Overview of the language features
We examined whether and how each of the prominent how
customer language features are reflective of B2B customer
experiences. Consistent with Study 1 and the supplemen -
tary study, we find that sentiment (b = 0.129, SE = 0.038, p
< .001, Cohen’s f2 = 0.05; see Model 1 of Table WAG.2 in
Web Appendix G) and temporality (b = -0.065, SE = 0.017,
p < .001, Cohen’s f2 = 0.07; see Model 3 of Table WAG.2)
2 A base model with only the random effects of question-responses by
case IDs and case IDs by suppliers indicate a total intraclass correla -
tion of 0.138 (0.110 for the former and 0.038 for the latter). Results
are robust even without capturing the random effects of case ID and
suppliers.

1 3
Journal of the Academy of Marketing Science
continue to be diagnostic of customer experiences. Cer -
tainty (p = .52) and concreteness ( p = .42) again show no
significant association with customer experience. Although
first-person voice reaches statistical significance in this
study (b = 0.067, SE = 0.030, p = .028, Cohen’s f² = 0.03),
this pattern did not replicate consistently across studies.
Accordingly, we focus the remaining analyses on sentiment
and temporality, the two language features that demonstrate
robust diagnostic value across datasets. Figure 2 F–J illus -
trates how each language feature varies by customer experi-
ence levels.
Language sentiment
Building on the established effect of customer experience
on language sentiment, we assessed whether extreme values
influence our findings. After excluding the top and bottom
5% of sentiment scores, the positive association between
customer experience and language sentiment remained sig -
nificant ( b = 0.099, SE = 0.038, p = .010), confirming that
extreme values do not drive the observed experience-lan -
guage relationship.
We next examined whether the diagnostic value of sen -
timent varies across relationship contexts. The interaction
between customer experience and relationship incumbency
was not statistically significant (p = .26; see Model 2 of Table
WAG.2), suggesting no strong evidence that the experience–
sentiment relationship differs across incumbency conditions
at the aggregate level. However, conditional analyses reveal
that the association between customer experience and senti-
ment is significant when customers discuss incumbent sup -
pliers (b = 0.159, SE = 0.047, p = .001, Cohen’s f² = 0.10),
but not when they discuss prospective suppliers ( b = 0.080,
SE = 0.058, p = .17, Cohen’s f² = 0.02).
We further investigated whether the nature of the
response (whether customers are speaking directly about
the focal supplier) shapes the diagnostic strength of senti -
ment. We find a significant positive interaction between cus-
tomer experience and supplier-specific responses (b = 0.163,
SE = 0.064, p = .012; see Model 2, Table WAG.2). That is,
the relationship between customer experience and sentiment
is significant for supplier-specific responses ( b = 0.178,
SE = 0.041, p < .001), but not for general discussions of the
buying process ( p = .83). Sentiment thus serves as a more
diagnostic indicator of customer experience when custom -
ers’ language is directly anchored to the focal supplier.
Consistent with this pattern, the effect size increases from
Cohen’s f² = 0.05 in the full sample to f² = 0.09 in supplier-
specific contexts.
Past temporality
We next analyzed the role of past temporal language, build-
ing on the established negative association between cus -
tomer experience and past-focused language. To assess
the influence of extreme values, we reran the analysis after
excluding the top and bottom 5% of past temporal language
scores. The negative relationship remained significant ( b =
-0.035, SE = 0.012, p = .006), confirming that extreme val -
ues do not drive this relationship.
We then tested whether the diagnostic value of past tem-
porality varies across relationship contexts. A significant
negative interaction between customer experience and rela-
tionship incumbency emerged ( b = -0.086, SE = 0.032, p
= .007), indicating that the association between customer
experience and past temporal language differs depending
on whether discussing incumbent or prospective suppliers.
That is, the relationship is significant for incumbent suppli-
ers (b = -0.094, SE = 0.032, p < .001), but not for prospective
suppliers (p = .46).
We further examined whether the specificity of the
response moderates this relationship. We find a significant
negative interaction between customer experience and
supplier-specific responses ( b = -0.082, SE = 0.027, p =
.002; see Model 4, Table WAG.2). The association between
customer experience and past temporal language is signifi -
cant when customers speak directly about the supplier ( b =
-0.092, SE = 0.016, p < .001), but not when they discuss the
buying process more generally (p = .54).
Combining these moderators, the strongest negative
relationship between customer experience and past tem -
poral language emerged in supplier-specific discussions of
incumbent suppliers (b = -0.108, SE = 0.019, p < .001), with
a large effect size (Cohen’s f² = 0.33). These findings reveal
that past temporality is a context-sensitive indicator of cus -
tomer experience, most informative when buyers reference
historical interactions with the focal supplier.
Key takeaways
This study examined how customer language features in
B2B communications vary depending on the nature of the
customer experience (positive vs. negative). Controlling
for differences in contract features and the random effects
of different suppliers, results show that negative customer
experiences are associated with greater language negativ -
ity (sentiment) and increased use of past temporal language.
Consistent with Study 1 and the supplementary analysis,
sentiment and temporality emerge as the most reliable lan -
guage features. Yet, the diagnostic strength of these lan -
guage features depends on the context in which customers
communicate.

1 3
Journal of the Academy of Marketing Science
For sentiment, the relationship with customer experience
is robust but context-sensitive. Although the interaction
with relationship incumbency is not statistically significant,
sentiment more reliably reflects customer experience when
buyers discuss incumbent suppliers and when responses
directly focus on the focal supplier. Thus, sentiment is most
informative when language is grounded in supplier evalua -
tions versus general discussions of the buying process.
In contrast, the diagnostic value of past temporal lan -
guage is sharply bounded by context. The association
between customer experience and past-focused language
emerges when buyers have prior relationship history (i.e.,
incumbent suppliers) and when their responses are anchored
to the focal supplier. Thus, temporal language is particularly
informative when customers can draw on past experiences,
consistent with prior work conceptualizing temporal lan -
guage as a situational, state-like property of communication
(Rush & Grouzet, 2012; Tang et al., 2020).
Collectively, the evidence thus far establishes that senti -
ment and temporality in buyer language are robust indica -
tors of customer experience, while also showing that their
diagnostic strength depends on contextual features of the
communication setting. Via Study 1 controls, results rule
out buyer and seller characteristics as potential confounds
to the experience-language relationship. Study 2 provides
clear evidence for temporal precedence, where customer
language is distinctly collected after a positive or negative
experience milestone, while also evidencing the importance
of relationship history and response focus in fostering the
experience-language association. Although the associa -
tion of customer experience with how customers speak is
strong, an important question remains: can customers’ how
language about incumbent suppliers, captured before major
relationship decisions, help predict major B2B relationship
outcomes?
Study 3: Assessing the incremental
predictive value of language features
The purpose of Study 3 is to examine whether and to what
extent the language features identified in Studies 1 and 2
provide incremental predictive value for customer defection
(vs. renewal) when applied to customers’ pre-decision lan -
guage. Rather than testing causal effects, this study evaluates
whether patterns in how customers speak prior to contract
renewal contain forward-looking signals that are diagnostic
of subsequent purchase decisions.
Method
Data
The data consisted of 995 single-spaced transcript pages
of 137 in-depth interviews of organizational buyers across
three supplier firms and industries: food service, transporta-
tion, and shipping and logistics. All cases are independent
from those in Study 2. Interviews were conducted through
the same consultancy firm in the months prior to contract
expiration to assess account health. The authors were not
involved in determining which customer accounts were
assessed. All pre-decision interviews made available by the
consultancy were included in the analysis. For all cases, a
follow up was conducted after contract expiration to deter -
mine if the customer stayed with the incumbent supplier or
defected: 29 (21.2%) defection outcomes and 108 (78.8%)
renewal outcomes. Interviews were recorded and tran -
scribed to verbatim text. The annual valuation of the con -
tract proposals ranged from $210K to $80 M, with a median
of $3.2 M (mean = $5.9 M; SD = $9.5 M). The duration of
the contract proposals ranged from 1 year to 10 years, with
a median contract duration of 5 years (mean = 4.5 years;
SD = 1.5 years).
Variables
In Study 3, we examine customer language that precedes the
RFP decision (pre-decision language). We treat features in
buyer language as the predictors and the decision outcome
(CustomerDefection) as the dependent variable. The main
predictor variables were sentiment (Sentiment) and past
temporal language (PastTemporality), each operationalized
the same way as in the previous two studies (Boyd et al.,
2022; Devlin et al., 2019; Wijffels, 2023).
Building on extant models of customer language features
(Packard et al., 2023), several types of control variables
were included in the analysis, including buyer response ten-
dencies (ResponseLength, SentenceLength, FleschScore),
contract features (AnnualPrice, ContractDuration), RFP
competitiveness (CompetitionElaboration), other linguistic
features (Concreteness, Certainty, FirstPerson), content top-
ics (via topic modeling; Blei & Lafferty, 2006), and predic-
tions from human experts (consultants with over 20 years
of experience collecting and analyzing these account health
assessments). Details on control variables, topic modeling
methodology, and predictions from human experts are pro -
vided in Web Appendix H.

1 3
Journal of the Academy of Marketing Science
Analysis
To assess the predictive role of customer language fea -
tures while addressing concerns of model complexity and
incremental validity, we implemented a multi-step ana -
lytical approach. First, we estimated mixed-effects logistic
regression models predicting defection (1) versus renewal
(0), with supplier treated as a random effect. We compared
a sequence of nested models to evaluate the stability and
incremental contribution of the focal language features.
That is, we estimated (a) a parsimonious model including
sentiment and past temporality, (b) models that incremen -
tally incorporated response characteristics, additional lin -
guistic controls, contract features, and topic variables, and
(c) a full model including all predictors. This sequential
approach allows us to assess whether effects persist across
increasingly stringent specifications.
Second, to evaluate predictive performance while
accounting for the small number of defection cases, we con-
ducted repeated stratified k-fold cross-validation. Stratifica-
tion preserved the base rate of defection outcomes within
each fold, and repetition reduced dependence on any single
fold assignment. Because precision–recall metrics are par -
ticularly informative for imbalanced classification prob -
lems, we report mean performance and variability across
repetitions for precision, recall, F1 (the harmonic mean of
precision and recall), and the area under the precision–recall
curve (PR-AUC).
Third, to evaluate managerial usefulness, we conducted
a threshold-based risk analysis. To avoid selecting a risk
threshold on the same data used for evaluation, we selected
the classification threshold within each training fold and
evaluated the selected threshold on the corresponding held-
out fold.
Fourth, to assess the relative importance of predictors
under potential multicollinearity, we estimated a ridge
regression model with cross-validated regularization param-
eters. Ridge regression retains all predictors while shrinking
coefficients, allowing us to evaluate the relative contribu -
tion of correlated linguistic features within a unified predic-
tive framework.
Finally, to benchmark the predictive value of customer
language against human judgment, we conducted a hierar -
chical comparison with expert assessments. We estimated
(a) a baseline model including only expert predictions, and
(b) an augmented model including both expert assessments
and the focal language features. Likelihood ratio tests were
used to assess whether language features provide incremen-
tal explanatory power beyond expert judgment. In addition,
we examined coefficient stability and attenuation to evalu -
ate the degree of overlap between expert assessments and
linguistic predictors.
Across our analyses, all language measures are derived
from interviews conducted prior to the contract renewal
decision, establishing temporal precedence between predic-
tors and outcome and enabling a forward-looking assess -
ment of customer behavior. However, because the data
are observational, this temporal structure does not fully
eliminate endogeneity concerns, including omitted vari -
ables, latent decision states that may jointly shape language
and outcomes, or selection into communication patterns.
Accordingly, our analyses are predictive rather than causal
in nature, and results are interpreted as diagnostic associa -
tions. We complement the main analyses with additional
diagnostic tests to probe alternative explanations within this
framework.
Results
Baseline predictive effects of language features
We begin by examining the predictive effects of senti -
ment and temporality. Consistent with prior studies, both
language features significantly predict defection outcomes
when estimated independently (sentiment: b = -1.620,
SE = 0.521, p = .002, Model 1, Table 3; past temporality:
b = 9.253, SE = 3.601, p = .01, Model 2, Table 3) and jointly
(Model 3, Table 3). These findings indicate that language
features in pre-decision communication contain meaning -
ful signals related to subsequent customer decisions. Nota -
bly, the predictive value of sentiment depends on how it is
operationalized. In supplementary analyses, the contextual
transformer-based sentiment measure outperformed the lex-
icon-based approach, suggesting that evaluative meaning
in formal B2B communication is more effectively recov -
ered through context-sensitive language models (see Web
Appendix H).
Another supplementary analysis revealed no evidence
of an interaction between sentiment and past temporality
(p = .30), indicating that their predictive effects are addi -
tive and capture non-overlapping variance in defection risk.
This pattern suggests that sentiment and temporality reflect
distinct aspects of customer evaluation—affective tone and
temporal framing—that independently contribute to pre -
dicting defection. Consistent with emerging perspectives
that conceptualize psychological distance as multidimen -
sional rather than unitary (Maglio 2020a, b; Stephan et al.
2010), these findings are broadly aligned with the view that
different linguistic features may capture separable facets of
how customers mentally represent their relationship with a
supplier. A discussion of this result and its theoretical impli-
cations are provided in Web Appendix H.

1 3
Journal of the Academy of Marketing Science
Parsimonious versus full model comparison
We next compare models of increasing complexity to assess
whether the predictive signal identified in the focal language
features persists when additional controls are introduced.
We begin by examining coefficient stability across specifi -
cations. In the parsimonious model (Model 3, Table 3), both
sentiment and past temporality significantly predict defec -
tion (sentiment: b = -1.554, SE = 0.514, p = .002; past tem -
porality: b = 8.064, SE = 3.576, p = .024). Importantly, these
effects remain substantively similar in magnitude and signif-
icance as additional response, linguistic, contract, and topic
controls are introduced (full model: sentiment: b = -1.520,
SE = 0.641, p = .018; past temporality: b = 9.455, SE = 4.637,
p = .041; see Model 7, Table 3). This stability indicates that
the relationship between language features and defection
is not explained by the measured controls included in the
model and is robust across alternative model specifications.
Based on the parsimonious model (Model 3, Table 3),
holding past temporal language constant, a 1%-point
decrease in the probability that a customer’s language is
classified as positive (i.e., a 0.01 decrease in the sentiment
score) is associated with an approximately 1.6% increase in
the odds of defection (b = -1.554, p = .002). Holding senti-
ment constant, a 1%-point increase in the proportion of past-
focused language is associated with an approximately 8.4%
increase in the odds of defection (b = 8.064, p = .024). With
the compounding effect of each point changed, a 44.5%-
point decrease in sentiment probability (0.446 units) or an
8.6%-point increase in past-focused language (0.086 units)
roughly doubles the odds of defection. These estimates
indicate that even modest shifts in customer language, par -
ticularly toward more negative sentiment and greater ret -
rospective framing, correspond to meaningful increases in
defection risk.
Cross-validation for predictive performance
We next evaluate whether increased model complexity
improves predictive performance. To rigorously assess out-
of-sample predictive stability and address potential data
volatility, we subjected both specifications to a repeated
stratified 5-fold cross-validation procedure across 100 inde-
pendent repetitions to reduce dependence on any single
Table 3 Study 3 pre-decision regression results
Customer defection (1 =defect vs. 0 = renew existing buyer-seller relationship)
Senti-
ment
only
Tempo-
rality
only
Sentiment + temporality + Response
controls
+ Linguistic
features
+ Contract
controls
+ Topic
controls
(1) (2) (3) (4) (5) (6) (7)
Sentiment1 -1.620**
(0.521)
[2.04]
-1.554** (0.514) [1.96] -1.474**
(0.526) [1.89]
-1.468**
(0.529) [1.89]
-1.503**
(0.537) [1.92]
-1.520*
(0.641) [2.00]
PastTemporality 9.253*
(3.601)
[1.83]
8.064* (3.576) [1.69] 9.540* (3.751)
[1.87]
10.118**
(3.918) [1.95]
11.579**
(4.291) [2.16]
9.455* (4.637)
[1.91]
ResponseLength -0.630 (0.375) -0.676
(0.384)
-0.673 (0.415) -0.561 (0.507)
SentenceLength 0.406 (1.283) 0.482 (1.318) 0.181 (1.348) 0.871 (1.682)
FleschScore -0.000 (0.000) -0.000
(0.000)
-0.000 (0.001) -0.001 (0.001)
Concreteness -0.159
(0.244)
-0.188 (0.247) -0.122 (0.287)
Certainty -0.043
(0.237)
-0.063 (0.237) -0.070 (0.262)
FirstPerson 0.016 (0.265) -0.010 (0.271) -0.222 (0.307)
ln(AnnualPrice) 0.164 (0.255) -0.196 (0.314)
ContractDuration 0.023 (0.169) 0.323 (0.277)
ln(CompetitionElaboration) -0.207 (0.284) -0.592 (0.486)
Topics No No No No No No Yes
Intercept -0.403
(0.432)
-2.997***
(0.857)
-2.139** (0.807) 0.569 (4.084) 0.560 (4.185) -0.170 (5.801) 5.568 (6.941)
Observations 137 137 137 137 137 137 137
*p < .05; **p < .01; ***p < .001. Values in the table represent regression coefficients. Values in round parentheses are standard errors. Values in
square parentheses are standardized odds ratios. 1All the standardized odds ratios for Sentiment have been inverted to allow for cross compari -
son with PastTemporality. Description of control predictors can be found in Web Appendix H. See Web Appendix H for details on the topic
modeling methodology. None of the ten topic controls were statistically significant

1 3
Journal of the Academy of Marketing Science
train-test partition, totaling 500 discrete evaluations. Rather
than relying on single in-sample estimates or isolated splits,
we report the aggregated out-of-sample performance met -
rics across all 500 folds as means and 95% confidence inter-
vals (CI).
The repeated cross-validation results demonstrate stable
predictive performance and favor the parsimonious speci -
fication over the full model. Specifically, the parsimonious
model achieves a mean out-of-sample PR-AUC of 0.263
(95% CI = [0.255, 0.272]) and a mean out-of-sample F1
score of 0.297 (95% CI = [0.293, 0.302]). Under the base -
line classification threshold, it yields a mean out-of-sample
precision of 0.714 (95% CI = [0.677, 0.752]) and a mean
out-of-sample recall of 0.0163 (95% CI = [0.0116, 0.0209]).
In contrast, the full model yields lower overall predictive
performance across repetitions, with a mean out-of-sample
PR-AUC of 0.228 (95% CI = [0.221, 0.234]), an F1 score
of 0.283 (95% CI = [0.281, 0.285]), precision of 0.319
(95% CI = [0.280, 0.358]), and recall of 0.0130 (95% CI
= [0.0090, 0.0170]). Consistent with these out-of-sample
results, in-sample model fit comparisons based on AIC
also favor the parsimonious specification (AIC parsimonious
= 134.67 vs. AIC full = 141.57; delta AIC = -6.90), indicat -
ing that the additional parameters do not provide sufficient
explanatory value to justify their complexity.
Notably, out-of-sample recall for defection cases remains
low across specifications at this baseline stage (mean recall
< 0.02). This reflects the highly conservative and sparse
distribution of actual defection events relative to retained
accounts in our pre-RFP sample ( n = 29 defections out of
137 cases), indicating that at a standard 0.50 probability
threshold, the classifier primarily identifies a small subset
of high-certainty at-risk accounts. As we demonstrate in
the subsequent threshold-based risk analysis, model perfor-
mance is highly sensitive to this threshold choice, and alter-
native thresholds substantially improve the balance between
recall and precision for practical managerial deployment.
Threshold-based risk analysis
Given the class imbalance (21% defection rate), we con -
ducted a threshold-based risk analysis to move beyond the
default 0.50 classification cutoff. This analysis evaluates the
necessary trade-off between detection rates (recall) and false
alarm accuracy (precision). To prevent optimistic bias, we
implemented a nested threshold tuning procedure. Specifi -
cally, for each cross-validation partition, the classification
threshold was optimized strictly within the training folds
based on the peak F1 score and then applied completely out-
of-sample to the held-out test cases.
Across our 500 evaluations, the data-driven nested
selection procedure settled on a mean optimal probability
threshold of 0.216 (SD = 0.040). Evaluated strictly out-of-
sample on held-out cases, the model under this dynamically
tuned threshold achieves a mean F1 score of 0.405 (95% CI
= [0.394, 0.415]), a mean recall of 0.590 (95% CI = [0.571,
0.608]), and a mean precision of 0.320 (95% CI = [0.311,
0.329]). This represents a meaningful improvement in out-
of-sample deployment utility over the default specification,
enabling managers to identify 59.0% of all forthcoming
account defections while maintaining an alarm accuracy rate
that stands substantially above the 21% baseline defection
rate. These findings suggest that while the linguistic signals
in pre-RFP data are subtle, they yield a useful early-warn -
ing decision-support tool when classification thresholds are
properly calibrated to the underlying risk distribution of the
B2B context.
Assessment of language feature importance
To assess the relative contribution of the focal language fea-
tures while accounting for shared variance among predic -
tors, we estimated a ridge regression model (α = 0), which
retains all predictors while shrinking coefficients, making
it well suited for evaluating the relative importance of theo-
retically related features that may exhibit collinearity. The
results (see Table WAH.3 in Web Appendix H) reveal a clear
hierarchy in feature importance. Sentiment emerges as the
dominant predictor (Importance = 100.00), indicating that
affective tone provides the strongest signal of subsequent
defection. Past-tense temporal language also contributes
meaningfully to the model (Importance = 30.88), suggesting
that temporal framing captures a distinct and complemen -
tary dimension of customer experience beyond sentiment
alone.
Importantly, the ridge regression and logistic models cap-
ture different aspects of the relationship. Logistic regression
reflects per-unit changes in log-odds, while ridge regression
emphasizes regularized predictive contribution across cor -
related features. Both highlight sentiment and temporal -
ity as primary predictors, but with differing prominence:
ridge regression underscores sentiment’s overall influence,
whereas logistic regression shows a greater per-unit effect
for past-focused language. This difference partly reflects
scaling differences—temporality varies over a narrower
range than sentiment—leading to stronger unit-level effects
but a smaller contribution to overall predictive variance.
It is worth noting that the additional linguistic controls
exhibit minimal contributions. First-person pronoun usage
(Importance = 3.35) and certainty (Importance = 1.02) pro-
vide only marginal incremental value, while concreteness
does not contribute to predictive performance (Impor -
tance = 0). This pattern indicates that the predictive signal is

1 3
Journal of the Academy of Marketing Science
not broadly distributed across linguistic features but instead
concentrated in a small set of contextually linked constructs.
Comparison with expert assessments
To benchmark the predictive value of customer language
against human judgment, we compared model performance
with and without expert assessments. Specifically, we esti -
mated a baseline model including only expert predictions
and a full model incorporating both expert assessments and
the focal language features (sentiment and temporality). A
likelihood ratio test indicates that the inclusion of language
features significantly improves model fit (Δχ²(2) = 7.07,
p = .029), demonstrating that customer language contains
incremental predictive information not fully captured by the
judgement of human experts.
Examining the full model further reveals differences in the
relative contribution of predictors. While sentiment remains
a significant predictor of defection ( b = -0.59, SE = 0.25, p
= .018), the effect of expert assessment becomes non-sig -
nificant (b = 0.45, SE = 0.52, p = .388), suggesting the pre -
dictive signal captured by expert evaluations overlaps with
information embedded in customers’ linguistic expressions.
To better understand this overlap, we examine correlations
among predictors. Expert assessments are moderately cor -
related with sentiment ( r = − .37), but only weakly associ -
ated with past temporal language ( r = .18). This suggests
that while experts successfully incorporate affective cues,
temporal framing represents a systematic signal that appears
partly orthogonal, which may provide complementary diag-
nostic value.
Addressing endogeneity and alternative explanations
Although Study 3 is predictive rather than causal, a central
concern in observational analyses of customer language is
the potential for endogeneity, including omitted variables,
reverse causality, and selection into communication pat -
terns. We conduct several analyses to probe these concerns.
First, we leveraged the temporal structure of the data, as all
language measures are derived from interviews conducted
prior to the observed decision outcome. While the possibil-
ity remains that language captures latent decision states, this
ordering reduces concerns that language reflects realized
outcomes.
Second, we conducted placebo (falsification) tests to
ensure our language variables were not merely proxies for
case-level noise. Sentiment and past temporality failed to
jointly predict unrelated case attributes such as contract
length (F(2,134) = 2.17, p = .118) or the specific report year
(F(2,68) = 1.15, p = .322). The lack of association with these
exogenous variables supports the claim that our identified
linguistic signal is specific to the buyer-supplier relation -
ship health.
Third, to rule out buyer-specific traits as a confound, we
utilized a within-subject differencing approach. Drawing
from Study 2, we calculated the delta between language used
when discussing the supplier versus general business topics
within the same interview. That is, the within-subjects mea-
sure represents an incremental linguistic emphasis toward
the focal supplier beyond the buyer’s general discourse tone
when talking about procurement. We recognize that the gen-
eral procurement baseline may not be uncontaminated, as
current experiences with the focal supplier could influence
even broader procurement commentary. Accordingly, we
view the within-subject deltas primarily as a tool for internal
validation (i.e., helping to rule out stable confounds) rather
than as the sole basis for practical inference. These within-
subject measures for sentiment (b = -0.825, SE = 0.404, p =
.041) and past temporality ( b = 6.896, SE = 2.913, p = .018;
see Table WAH.2 in Web Appendix H) remained robust,
confirming that the signal is driven by the relationship itself
rather than the respondent’s baseline personality or contem-
poraneous mood.
Collectively, these analyses reduce the likelihood that the
observed relationships are due to spurious correlations or
individual-level response biases. Of further note, the objec-
tive of this research is not to establish a formal causal mech-
anism, such as whether specific language causes defection,
but rather to identify forward-looking, diagnostic signals
that are embedded within natural customer discourse. The
consistent predictive power of sentiment and temporal -
ity across increasingly stringent analytical specifications
underscores their utility as high-fidelity indicators of sub -
sequent purchase decisions in complex B2B environments.
Key takeaways
Study 3 demonstrates that sentiment and past temporality,
as identified in Studies 1 and 2, provide robust, incremental
predictive value for customer defection from pre-decision
interview transcripts. These language features remain stable
across increasingly complex specifications. Repeated strati-
fied cross-validation further indicates that the predictive
signal remains stable across repeated out-of-sample evalua-
tions and consistently favors the parsimonious two-feature
model over more complex specifications. Complementary
ridge regression analyses likewise identify sentiment and
past temporality as the dominant linguistic predictors of
customer defection. Critically, the language model extends
beyond expert predictions, with sentiment subsuming much
of experts’ signal while temporality offers unique value.
From a managerial perspective, customer language pro -
vides a practical basis for early identification of at-risk

1 3
Journal of the Academy of Marketing Science
accounts. When classification thresholds are selected within
the training data and evaluated on held-out cases, the model
identifies approximately 59% of future defections while
maintaining a precision rate substantially above the base -
line defection rate. Together, these findings suggest that
customer language can complement expert judgment by
providing forward-looking indicators of relationship risk
prior to contract renewal. Consistent with the predictive
framing of this research, the value of customer language
lies in early detection rather than causal attribution. Even
if the observed linguistic patterns partly reflect emerging
decision states, they nonetheless provide timely diagnostic
signals that can support earlier and more informed manage-
rial intervention.
Stage 3: Advance understanding
Across three studies, we find that two features of customer
language, sentiment and past temporal focus, consistently
reflect B2B relationship experience and provide incremental
predictive value. These patterns emerge across customers’
written reviews (Study 1), spoken post-decision interviews
(Study 2), and spoken pre-decision communications (Study
3).
These relationships are particularly strong when cus -
tomers speak about incumbent suppliers. Collectively, the
findings demonstrate that how customers speak provides a
parsimonious and observable signal of underlying relation -
ship evaluations, extending beyond content-based analyses
of what customers say (Berger et al., 2020). In doing so, this
research establishes language features as both diagnostic
indicators of relationship health and predictive markers of
customer defection.
Theoretical implications
Customer defection as a language-signaled risk
Scholars note that unstructured data can enhance theorizing
of buyer-seller dynamics and offer opportunities for strate -
gic insight (Balducci & Marinova, 2018). However, extant
customer language scholarship emphasizes what custom -
ers say, rather than linguistic features of how they speak, to
explain market phenomena (e.g., Good et al., 2025; Packard
& Berger, 2017; Packard et al., 2018). Our EF approach (see
Golder et al., 2023 and Web Appendix A), tests features for
how customers speak as proxies for revealing experiential
information that customers attend to and filter over time in
their decisions.
Our results indicate that sentiment and temporality con -
tribute to defection modeling by identifying customers’
implicit dispositions and relationship intentions (Ascarza
& Hardie, 2013; Habel et al., 2024; Lemmens & Croux,
2006). These language features also enhance the predictive
modeling of churn through relationship dynamics (Netzer et
al., 2008; Zhang et al., 2016) and support broader customer
base analysis (Bachmann et al., 2021; Gupta et al., 2004;
McCarthy & Fader, 2018). Moreover, our findings suggest
that the theoretical value of customer language depends not
only on the linguistic constructs being examined, but also
on the correspondence between the communication envi -
ronment and the approach used to operationalize them. In
formal B2B interactions, customers often communicate
affective evaluations indirectly through nuanced, relation -
ship-preserving language (Andrade & Ho, 2009; Johnson
& Saboe, 2011), rather than overt emotional language.
Consequently, contextual language models are better suited
to recovering these evaluative signals than surface-level
lexical approaches. These findings thus provide theoretical
steppingstones for understanding how sentiment and past
temporal language reveal relationship evaluations and can
be leveraged to diagnose buyer-seller relationship health.
Psychological distancing as an interpretive lens
The observed patterns are consistent with psychological
distancing, wherein individuals regulate their relationship
to aversive experiences by creating cognitive separation
(Gross 1998; Maglio 2020b). Psychological distancing
is a core mechanism within emotion regulation, enabling
individuals to manage negative affect by altering how they
construe an experience. Prior research shows that such dis -
tancing is often reflected in language, as individuals shift
how they describe negative stimuli to reduce their psycho -
logical proximity to them (Nook et al., 2017). In the present
context, negative sentiment in customer language reflects
emotional distancing from the supplier, while increased
past temporal focus reflects temporal distancing from the
relationship (Trope & Liberman, 2010). These patterns are
pronounced in supplier-specific and incumbent contexts,
where customers have accumulated direct experience with
the supplier and can anchor their distancing in evaluations
of relational episodes. Together, these findings suggest that
customer language provides signals consistent with buyers
cognitively and affectively disengaging.
Distancing, however, does not emerge uniformly across
all dimensions of language. While sentiment and tempo -
rality shift systematically with negative experiences, other
features (e.g., concreteness) remain relatively stable. While
this null pattern should be interpreted as an open question
rather than a definitive conclusion, one plausible explana -
tion is that professional communication norms in B2B con-
texts constrain how distancing is expressed. That is, buyers

1 3
Journal of the Academy of Marketing Science
may still be expected to provide concrete, evidence-based
justifications for their evaluations even when disengaging
from the relationship. Accordingly, we position the stability
of concreteness as an avenue for future research, particu -
larly to better understand when and why certain dimensions
of psychological distance manifest in language while others
do not. Thus, the findings position psychological distancing
not as a uniformly expressed construct, but as one that is
selectively manifested through specific linguistic channels
in B2B contexts. This pattern provides suggestive evidence
that may refine broader assumptions of CLT, which often
posits interdependence across dimensions of psychological
distance (Trope & Liberman, 2010), and aligns with emerg-
ing work suggesting that such coupling may weaken in
complex, context-dependent settings (Brügger et al. 2016;
Maglio 2020a, b; Stephan et al. 2010).
Temporal language as a state-like indicator of relationship
dynamics
Prior research has conceptualized temporal orientation as
a relatively stable individual trait, reflecting enduring cog -
nitive dispositions or time perspectives that persist across
contexts (Shipp et al., 2009; Zimbardo & Boyd, 1999).
More current work, however, suggests that temporal focus
can shift in response to situational conditions and emotional
experiences (Rush & Grouzet, 2012; Shipp & Aeon, 2019).
Our findings extend this evolving state-like view by dem -
onstrating that past-focused language varies systematically
with customer experience and is not merely a stable charac-
teristic of the speaker. Across studies, past temporal focus
intensifies in negative experiences and is most pronounced
when customers discuss incumbent suppliers. This pattern
indicates that temporal language is responsive to relation -
ship conditions and reveals how customers cognitively
organize their experiences over time.
Importantly, past-focused language captures a shift in
how customers construe the relationship, from ongoing to
retrospective. As dissatisfaction builds, we theorize that
customers increasingly anchor communication in prior
interactions (e.g., “what went wrong”), signaling a reori -
entation away from future collaboration toward evalua -
tion of past performance. This framing is consistent with
research showing that negative affect heightens the salience
and recall of prior experiences (Nook et al., 2017; Shipp &
Aeon, 2019) and suggests that temporal language serves as
a behavioral trace of cumulative dissatisfaction. In this way,
temporal language extends beyond its predominant role in
shaping interpersonal influence (Packard et al., 2023) to
function as a diagnostic signal of disengagement. By cap -
turing the transition from present-oriented coordination
to past-oriented reflection, it provides a window into the
early-stage defection cadence, revealing when customers
begin to cognitively and motivationally disengage.
Managerial implications
Executive leaders prioritize customer retention, and market-
ing research continually tries to assess loyalty and prevent
churn (Habel et al., 2024). Our results have practical value
for organizations assessing the health of their customer
relationships and allocating resources to prevent churn. For
example, based on our B2B multimillion dollar RFP context,
we find that assuming all else equal, for every 1% increase
in a customer’s emphasis on the past, the odds of an RFP
resulting in defection increase by 8.4%. At scale, our model
can be applied to sources of unstructured text data that cap-
ture the customer voice to determine micro-level forecasts
(e.g., incumbent defection likelihood) or macro-level trend-
lines (e.g., incumbent account prioritization). Thus, data
scientists on sales enablement teams can explore sentiment
and temporal language in their customer datasets and assess
their relationships with key performance indicators.
As summarized by Marrs (2026), “For CROs, conversa-
tion intelligence is no longer optional. It’s the connective
tissue between selling reality and executive decision mak -
ing. The organizations that treat conversations as a strategic
revenue asset will see fewer surprises, stronger execution
and more predictable growth.” Yet, while vendors in the
sales tech stack offer platforms to capture and analyze con -
versational intelligence (e.g., Gong, Clari-Salesloft), our
findings suggest that such data dashboards are incomplete.
Typical output on these platforms includes sales call met -
rics (e.g., talk-to-listen ratio, number of speakers switches,
keyword analysis), but do not yet fully leverage the insight
available from how elements of customer language. Our
study provides a roadmap for managers to use their own
unstructured text data to derive powerful, predictive insights
that can optimally guide their resource allocations.
Fortunately for practice, sentiment and temporal language
are foundational aspects of everyday language (Tang et al.,
2020; Villarroel Ordenes et al., 2017) and captured suc -
cinctly within customer discourse (Park et al., 2017). Given
their salience across communication forms, managers can
take stock of sentiment and temporal language when their
teams are engaged in customer conversations (e.g., quar -
terly business reviews) and utilize technology platforms to
transcribe these conversations (e.g., Zoom). Since unstruc -
tured text data is high in ecological value (Van Heerde et
al., 2021) and external validity (Berger et al., 2020), manag-
ers can confidently pair such data with existing approaches
(e.g., customer surveys). To guide such communications,
we offer supplier-focused questions that could be integrated:
What are your most critical strategic needs that the supplier

1 3
Journal of the Academy of Marketing Science
has been able to address and solve? In what ways has the
supplier exceeded or fallen below your expectations? What
services and support are the supplier not providing that, if
offered, would put them over the top?
With the use of such questions and control of in-house
unstructured data, we conclude with a three-step tactical
roadmap for managers to analyze, segment, and act on the
“language of leaving.” Following data capture, step one for
managers is to analyze the unstructured data. To do so, we
provide large-language-model prompts, along with corre -
sponding statistical code, for sales leaders to compute senti-
ment or past temporality in applications such as ChatGPT
(see Web Appendix I for prompts and Tables WAI.1 and
WAI.2 for ChatGPT results). As documented, these mea -
sures effectively capture sentiment and temporal cues to
extract linguistic risk signals, yielding convergent patterns
of association with customer outcomes.
Following data analysis, step two for managers is to
systematically segment customer accounts based on their
predicted defection likelihood. To do so, firms should trans-
late linguistic signals into illustrative account-level triage
mechanisms, such as the Composite Defection Risk Index
(CDRI). Based on our pre-decision data, sentiment and tem-
poral focus serve as complementary early-warning signals
of relationship health within the CDRI. Examples of spe -
cific values of sentiment and past temporality for triage are
presented in Table WAJ.1 (see Web Appendix J for details
on the construction and calibration of the CDRI). However,
since these values are tied to our B2B RFP context (Study
3), they should be treated as a starting point rather than
universal cutoffs (additional discussion regarding the inter -
pretation and calibration of these thresholds across organi -
zational context is provided in Web Appendix J).
Step three is to act based on the emergent risk index and
implement differentiated account management strategies.
For accounts assessed as low in defection risk, managers
are advised to build upon stable engagement to expand
account value through cross- and up-selling initiatives,
and leverage these relationships as sources of referral capi -
tal. For accounts showing signs of disengagement but that
have not yet reached a critical defection threshold (i.e.,
medium defection risk), managers should proactively nur -
ture the account and engage in account health checks. In
addition, managers should conduct what (topical) analysis
on unstructured data to identify account-level areas of fric -
tion to inform interventions. For accounts characterized by
a high likelihood of defection, managers must evaluate the
merits of investing additional resources versus strategically
disengaging. For example, high-risk accounts with strong
revenue potential and strategic relevance may warrant tar -
geted retention efforts, including intensified senior-level
contact, joint problem-solving workshops, and structured
conversations aimed at surfacing legacy points of friction
in the relationship. While the optimal intervention will vary
by context, managers should then use these evaluations
to monitor the trajectory of at-risk accounts and to deter -
mine whether retention investments are generating positive
momentum or whether relationships remain static—thereby
signaling that reallocation of resources may be warranted.
Limitations and future research directions
Despite the advantages offered via unstructured data and
computational text analysis, as well as the generalizabil -
ity demonstrated by our results, the predictive aspects of
our findings are curbed by our research contexts. As with
most observational research, potential endogeneity con -
cerns exist, including omitted variables, reverse causal -
ity, and self-selection into communication patterns. While
we take steps to mitigate these concerns (e.g., temporal
ordering, within-subject comparisons, placebo tests), these
approaches do not fully eliminate time-varying confound -
ers. Our findings should thus be interpreted as predictive
associations rather than causal effects. In addition, although
Study 3 includes all pre-decision interviews made available
by the consultancy firm, we cannot rule out selection bias
because the criteria used to select accounts for assessment
are unknown. If the sampled accounts differ systemati -
cally from the broader customer base (e.g., more strategi -
cally important relationships), the predictive performance
observed here may not fully generalize to other B2B set -
tings. Scholars may therefore identify opportunities to blend
data and contexts in future work to enhance generalizabil -
ity—such as by extending insights from high-value B2B
RFPs to transactional settings, increasing the sample size
of pre-decision cases to mitigate model overfitting, testing
non-linear relationships between language features and cus-
tomer experience via advanced machine learning techniques
(e.g., gradient boosting, random forests), examining com -
munication styles across cultures rather than solely within
Western settings, and investigating whether the observed
communication patterns consistently forecast leading per -
formance indicators and lagging relationship outcomes.
Beyond the context of ongoing B2B contractual rela -
tionships, another drawback of our studies is that they
exclusively capture buyer responses. Such responses are
aggregated to the level of the buying team decision, rather
than accounting for role heterogeneity amongst buying cen-
ter stakeholders. Future research might address such role-
specific conditions (e.g., variance in linguistic expressions)
to add nuance to our understanding of buying team predic -
tions. Further, while capturing the customer’s perspective is
an advantageous direct link to the decision-making source
(Hansen & Riggle, 2009), other perspectives may also add

1 3
Journal of the Academy of Marketing Science
power to the model. Future research can thus add general -
izability by examining the role of sentiment and temporal
language in dyadic forms of buyer-seller communications
as well as customer language expressions at different units
of analysis (e.g., individual, team, organization; Tang et al.,
2020). Within the sales organization, additional perspec -
tives might incorporate the ecosystem of cross-functional
supplier stakeholders that are increasingly involved in com-
plex, enterprise-level relationships (e.g., customer feedback
managed by customer success teams; Vermeer et al., 2019).
Within the customer organization, hierarchical perspectives
of senior-level and frontline personnel can also enhance
the accuracy and effectiveness of predictive sales analytics
tools (Habel et al., 2024).
Finally, our study does not capture a longitudinal perspec-
tive of the relationship. While we sought to capture critical
incidence data from two pivotal points of relationship man-
agement (pre-decision, post-decision), these independent
snapshots do not track customer language before, during,
and after the decision. Given that temporal focus develops
over time and solidifies into stable group tendencies (Tang
et al., 2020), future researchers could extend our findings
via a longitudinal empirical package to produce stronger
evidence of sentiment and past temporal focus predicting
defection. Since machine learning analysis often examines
emergent, correlational relationships (Ma & Sun, 2020),
a longitudinal design could pinpoint causal mechanisms.
While our model provides predictive potency at a point in
time proximal to the decision, scholars should assess how
far back into the relationship indicators remain diagnostic.
Conclusion
As marketing and sales analysts seek to leverage unstruc -
tured data for strategic insights, research offers many
insights to deploy what elements of customer language. To
build on this momentum, our study advances pathways to
mine how elements of language that offer novel insights,
robust prediction, and analytical consistency. Across three
studies, our results advance understanding and practice
for using sentiment and temporal aspects of customer lan -
guage to provide incremental predictive value into customer
defection and theorize psychological distance in customer–
supplier relationships.
Supplementary Information  The online version contains
supplementary material available at  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 0 7 / s 1 1 7 4 7 - 0
2 6 - 0 1 1 9 2 - y     .
Acknowledgements The authors thank the review team for their devel-
opmental feedback throughout the review process. We also acknowl -
edge Dr. Jeff Johnson, Dr. Nandini Nim, Dr. Zhiyong Yang, and Dr.
Jonathan Zhang for their constructive advice on earlier versions of the
manuscript. Finally, we are grateful for financial support from research
grants provided by the Farmer School of Business at Miami Univer -
sity, the Sales Education Foundation, the University Sales Center Alli-
ance, and the AMA Relationship Marketing Special Interest Group.
Funding Partial financial support was received from the Sales Edu -
cation Foundation Research Grant, University Sales Center Alliance
Research Grant, and the American Marketing Association Relation -
ship-Marketing Special Interest Group. The authors have no compet -
ing or financial interests to declare that are relevant to the content of
this article.
Data availability The data and R code for Study 1 are available on
the Open Science Framework ( https://osf.io/9pwku/). To protect the
identity of firms and individual reviewers, the shared dataset excludes
identifying information, while retaining the variables used in the anal-
yses. The data underlying Studies 2 and 3 cannot be shared because
they were obtained under non-disclosure agreements with the associ -
ated market research consultancy firm. The web appendix provides the
statistical code and large language model prompts used to compute the
focal language measures, enabling researchers to apply the methodol -
ogy to their own customer language data.
Declarations
Ethical approval Not required. This study used archival data, includ -
ing de-identified internal records and publicly available secondary
sources, and did not involve direct interaction with human participants
or the use of identifiable private information.
Competing interests The authors declare that they have no competing
interests.
Open Access   This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format,
as long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate
if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless
indicated otherwise in a credit line to the material. If material is not
included in the article’s Creative Commons licence and your intended
use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright
holder. To view a copy of this licence, visit  h t t  p : / /  c r e  a t i  v e c o m m o n s . o
r g / l i c e n s e s / b y / 4 . 0 /     .
References
Ahmad, F., & Guzmán, F. (2021). Negative online reviews, brand
equity and emotional contagion. European Journal of Marketing,
55, 2825–2870.
Andrade, E. B., & Ho, T. H. (2009). Gaming emotions in social inter -
actions. Journal of Consumer Research, 36, 539–552.
Ascarza, E., & Hardie, B. G. (2013). A joint model of usage and churn
in contractual settings. Marketing Science, 32, 570–590.
Bachmann, P., Meierer, M., & Näf, J. (2021). The role of time-varying
contextual factors in latent attrition models for customer base
analysis. Marketing Science, 40, 783–809.
Balducci, B., & Marinova, D. (2018). Unstructured data in marketing.
Journal of the Academy of Marketing Science, 46, 557–590.

1 3
Journal of the Academy of Marketing Science
Berger, J., Humphreys, A., Ludwig, S., Moe, W. W., Netzer, O., & Sch-
weidel, D. A. (2020). Uniting the tribes: Using text for marketing
insight. Journal of Marketing, 84, 1–25.
Blei, D., & Lafferty, J. (2006). Correlated topic models. Advances in
Neural Information Processing Systems, 18, 147–154.
Boyd, R. L., Ashokkumar, A., Seraj, S., & Pennebaker, J. W. (2022).
The Development and Psychometric Properties of LIWC-22. Uni-
versity of Texas at Austin.
Brown, P., & Levinson, S. C. (1987). Politeness: Some Universals in
Language Usage. Cambridge University.
Brügger, A., Morton, T. A., & Dessai, S. (2016). Proximising climate
change reconsidered: A construal level theory perspective. Jour-
nal of Environmental Psychology, 46, 125–142.
Brysbaert, M., Warriner, A. B., & Kuperman, V . (2014). Concreteness
ratings for 40 thousand generally known english word lemmas.
Behavior Research Methods, 46, 904–911.
Büschken, J., & Allenby, G. M. (2016). Sentence-based text analysis
for customer reviews. Marketing Science, 35, 953–975.
Chung, C., & Pennebaker, J. (2011). In K. Fiedler (Ed.), The psycho-
logical functions of function words. Social Communication  (pp.
343–359). Psychology.
Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2019). BERT:
Pre-training of deep bidirectional transformers for language
understanding, in proceedings of the 2019 conference of the
North American Chapter of the association for computational lin-
guistics: Human language technologies.
Drenik, G. (2026). Three strategies to amplify conversation intelli -
gence, Forbes. Available at:  h t t  p s : /  / w w  w . f  o r b  e s .  c o m /  s i  t e s  / g a r  y d
r  e n i  k / 2 0 2 6 / 0 5 / 2 6 / t h r e e - s t r a t e g i e s - t o - a m p l i f y - c o n v e r s a t i o n - i n t e l l
i g e n c e
Fisher, T. (2025). How to integrate conversation intelligence into mar-
keting and sales, Forbes. Available at:  h t t  p s : /  / w w  w . f  o r b  e s .  c o m /  c
o  u n c  i l s /  f o r  b e s  t e c  h c o  u n c i  l /  2 0 2 5 / 0 3 / 1 4 / h o w - t o - i n t e g r a t e - c o n v e r s a
t i o n - i n t e l l i g e n c e - i n t o - m a r k e t i n g - a n d - s a l e s
Friend, S. B., & Johnson, J. S. (2015). Implicit measures in sales
research. Journal of Personal Selling & Sales Management , 35,
72–84.
Glackin, C. E., & Adivar, M. (2023). Using the power of machine
learning in sales research: Process and potential. Journal of Per-
sonal Selling & Sales Management, 43, 178–194.
Golder, P. N., Dekimpe, M. G., An, J. T., van Heerde, H. J., Kim, D.
S., & Alba, J. W. (2023). Learning from Data: An Empirics-First
Approach to Relevant Knowledge Generation. Journal of Mar -
keting, 87, 319–336.
Good, V ., Bhattacharya, A., Hochstein, B. W., & V oorhees, C. M.
(2025). Determining the quality of B2C sales leads from online
chats. International Journal of Research in Marketing , 43(2),
383–403.
Gross, J. J. (1998). The emerging field of emotion regulation: An inte-
grative review. Review of General Psychology, 2, 271–299.
Gupta, S., & Zeithaml, V . (2006). Customer metrics and their impact
on financial performance. Marketing Science, 25, 718–739.
Gupta, S., Lehmann, D. R., & Stuart, J. A. (2004). Valuing customers.
Journal of Marketing Research, 41, 7–18.
Habel, J., Alavi, S., & Heinitz, N. (2024). Effective implementation
of predictive sales analytics. Journal of Marketing Research, 61,
718–741.
Hansen, J. D., & Riggle, R. J. (2009). Ethical salesperson behavior in
sales relationships. Journal of Personal Selling & Sales Manage-
ment, 29, 151–166.
Harbert, T. (2021). Tapping the power of unstructured data, MIT Sloan.
Available at:  h t t  p s : /  / m i  t s l  o a n  . m i  t . e d  u /  i d e a s - m a d e - t o - m a t t e r / t a p p i
n g - p o w e r - u n s t r u c t u r e d - d a t a
Hsu, C. L., Yu, L. C., & Chang, K. C. (2017). Exploring the effects of
online customer reviews, regulatory focus, and product type on
purchase intention: Perceived justice as a moderator. Computers
in Human Behavior, 69, 335–346.
Jackson, J. C., Watts, J., List, J. M., Puryear, C., Drabble, R., &
Lindquist, K. A. (2022). From text to thought: How analyzing
language can advance psychological science. Perspectives on
Psychological Science, 17, 805–826.
Johnson, R. E., & Saboe, K. N. (2011). Measuring implicit traits in
organizational research: Development of an indirect measure of
employee implicit self-concept. Organizational Research Meth-
ods, 14, 530–547.
Lemmens, A., & Croux, C. (2006). Bagging and boosting classifica -
tion trees to predict churn. Journal of Marketing Research , 43,
276–286.
Ludwig, S., De Ruyter, K., Friedman, M., Brüggen, E. C., Wetzels, M.,
& Pfann, G. (2013). More than words: The influence of affective
content and linguistic style matches in online reviews on conver-
sion rates. Journal of Marketing, 77, 87–103.
Ma, L., & Sun, B. (2020). Machine learning and AI in marketing–con-
necting computing power to human insights. International Jour-
nal of Research in Marketing, 37, 481–504.
Maglio, S. J. (2020a). An agenda for psychological distance apart from
construal level. Social and Personality Psychology Compass, 14,
1–12.
Maglio, S. J. (2020b). Psychological distance in consumer psychol -
ogy: Consequences and antecedents. Consumer Psychology
Review, 3, 108–125.
Marketing Science Institute (2024). MSI research priorities 2024.
Available at:  h t t  p s : /  / w w  w . m  s i . o r g / w p - c o n t e n t / u p l o a d s / 2 0 2 4 / 0 4 /
2 0 2 4 - R P . p d f
Marrs, S. (2026). Chief revenue officers’ path to AI is through conver-
sations, Forbes. Available at:  h t t    p  s : /  / w  w w  . f  o  r b e  s . c o  m /  c o u  n c i   l s  /   f
o  r  b  e s b   u s i n   e s   s  d  e  v e l  o p m e n t c o u n c i l / 2 0 2 6 / 0 2 / 2 3 / c h i e f - r e v e n u e - o ffi
c e r s - p a t h - t o - a i - i s - t h r o u g h - c o n v e r s a t i o n s /
McCarthy, D. M., & Fader, P. S. (2018). Customer-based corporate
valuation for publicly traded noncontractual firms. Journal of
Marketing Research, 55, 617–635.
Minaee, S., Kalchbrenner, N., Cambria, E., Nikzad, N., Chenaghlu,
M., & Gao, J. (2021). Deep learning–based text classification: A
comprehensive review. ACM Computing Surveys, 54, 1–40.
Mudambi, S. M., & Schuff, D. (2010). Research note: What makes a
helpful online review? A study of customer reviews on Amazon.
com. MIS Quarterly, 34(1), 185–200.
Nanni, A., & Ordanini, A. (2025). Unintended consequences of in-store
technology for frontline employees: An empirics-first approach.
Journal of the Academy of Marketing Science, 53, 129–149.
Netzer, O., Lattin, J. M., & Srinivasan, V . (2008). A hidden markov
model of customer relationship dynamics. Marketing Science, 27,
185–204.
Netzer, O., Feldman, R., Goldenberg, J., & Fresko, M. (2012). Mine
your own business: Market-structure surveillance through text
mining. Marketing Science, 31, 521–543.
Netzer, O., Lemaire, A., & Herzenstein, M. (2019). When words sweat:
Identifying signals for loan default in the text of loan applica -
tions. Journal of Marketing Research, 56, 960–980.
Ng, S. Y ., Lim, K. M., Lee, C. P., & Lim, J. Y . (2023). Sentiment analy-
sis using DistilBERT, in 2023 IEEE 11th conference on systems,
process & control (ICSPC): IEEE.
Ngobo, P. V ., Casta, J. F., & Ramond, O. (2012). Is customer satisfac-
tion a relevant metric for financial analysts? Journal of the Acad-
emy of Marketing Science, 40, 480–508.
Nielsen, F. Å. (2011). A new anew: Evaluation of a word list for sen -
timent analysis in microblogs, arXiv preprint arXiv:1103.2903.
Nook, E. C., Schleider, J. L., & Somerville, L. H. (2017). A linguis -
tic signature of psychological distancing in emotion regulation.
Journal of Experimental Psychology: General, 146, 337–346.

1 3
Journal of the Academy of Marketing Science
Packard, G., & Berger, J. (2017). How language shapes word of
mouth’s impact. Journal of Marketing Research, 54, 572–588.
Packard, G., & Berger, J. (2021). How concrete language shapes cus -
tomer satisfaction. Journal of Consumer Research, 47, 787–806.
Packard, G., & Berger, J. (2024). The emergence and evolution of
consumer language research. Journal of Consumer Research, 51,
42–51.
Packard, G., Moore, S. G., & McFerran, B. (2018). (I'm) happy to help
(you): the impact of personal pronoun use in customer–firm inter-
actions. Journal of Marketing Research, 55(4), 541–555.
Packard, G., Berger, J., & Boghrati, R. (2023). How verb tense shapes
persuasion. Journal of Consumer Research, 50, 645–660.
Park, G., Schwartz, H. A., Sap, M., Kern, M. L., Weingarten, E., Eich-
staedt, J. C., Berger, J., Stillwell, D. J., Kosinski, M., & Ungar,
L. H. (2017). Living in the past, present, and future: Measuring
temporal orientation with language. Journal of Personality , 85,
270–280.
Peltokorpi, V ., Allen, D. G., & Shipp, A. J. (2023). Time to leave?
The interaction of temporal focus and turnover intentions in
explaining voluntary turnover behaviour. Applied Psychology ,
72, 297–316.
Pennebaker, J. W., & Stone, L. D. (2003). Words of wisdom: Language
use over the life span. Journal of Personality and Social Psychol-
ogy, 85, 291–301.
Rocklage, M. D., He, S., Rucker, D. D., & Nordgren, L. F. (2023).
Beyond sentiment: The value and measurement of consumer cer-
tainty in language. Journal of Marketing Research, 60, 870–888.
Rush, J., & Grouzet, F. M. (2012). It is about time: Daily relation -
ships between temporal perspective and well-being. The Journal
of Positive Psychology, 7, 427–442.
Shipp, A. J., & Aeon, B. (2019). Temporal focus: Thinking about the
past, present, and future. Current Opinion in Psychology , 26,
37–43.
Shipp, A. J., Edwards, J. R., & Lambert, L. S. (2009). Conceptualiza -
tion and measurement of temporal focus: The subjective experi -
ence of the past, present, and future. Organizational Behavior and
Human Decision Processes, 110, 1–22.
Shipp, A. J., Gabriel, A. S., & Lambert, L. S. (2022). Profiles in time:
Understanding the nature and outcomes of profiles of temporal
focus. Journal of Applied Psychology, 107, 1640–1654.
Short, J. C., McKenny, A. F., & Reid, S. W. (2018). More than words?
Computer-aided text analysis in organizational behavior and
psychology research. Annual Review of Organizational Psychol-
ogy and Organizational Behavior, 5, 415–435.
Singh, S. K., Marinova, D., & Singh, J. (2020). Business-to-business
e-negotiations and influence tactics. Journal of Marketing , 84,
47–68.
Stephan, E., Liberman, N., & Trope, Y . (2010). Politeness and psycho-
logical distance: A construal level perspective. Journal of Person-
ality and Social Psychology, 98, 268–280.
Tang, S., Richter, A. W., & Nadkarni, S. (2020). Subjective time in
organizations: conceptual clarification, integration, and implica -
tions for future research. Journal of Organizational Behavior, 41,
210–234.
Timoshenko, A., & Hauser, J. R. (2019). Identifying customer needs
from user-generated content. Marketing Science, 38, 1–20.
Trope, Y ., & Liberman, N. (2010). Construal-level theory of psycho -
logical distance. Psychological Review, 117, 440–463.
Van Heerde, H. J., Moorman, C., Moreau, C. P., & Palmatier, R. W.
(2021). Reality check: Infusing ecological value into academic
marketing research. Journal of Marketing, 85, 1–13.
Vermeer, S. A., Araujo, T., Bernritter, S. F., & van Noort, G. (2019).
Seeing the wood for the trees: How machine learning can help
firms in identifying relevant electronic word-of-mouth in social
media. International Journal of Research in Marketing , 36,
492–508.
Villarroel Ordenes, F., Ludwig, S., De Ruyter, K., Grewal, D., & Wet-
zels, M. (2017). Unveiling what is written in the stars: Analyzing
explicit, implicit, and discourse patterns of sentiment in social
media. Journal of Consumer Research, 43, 875–894.
Wijffels, J. (2023). _Udpipe: tokenization, parts of speech tagging,
lemmatization and dependency parsing with the ‘Udpipe’ ‘NLP’
toolkit_. R Package Version 0.8.11.
Zhang, J. Z., Watson, G. F., Palmatier, R. W., & Dant, R. P. (2016).
Dynamic relationship marketing. Journal of Marketing , 80,
53–75.
Zimbardo, P. G., & Boyd, J. N. (1999). Putting time in perspective: A
valid, reliable individual-differences metric. Journal of Personal-
ity and Social Psychology, 77, 1271–1288.
Publisher’s Note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional affiliations.
