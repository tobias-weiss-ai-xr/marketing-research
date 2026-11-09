---
title: 'Fifty Shades of Greenwashing: The Political Economy of Climate Change Advertising on Social Media'
url: https://arxiv.org/abs/2511.14930
category: consumer-behavior
subcategory: empirical
date: 2025-11
venue: ''
authors:
- Robert Kubinec
- Aseem Mahajan
source: arxiv
pdf_url: https://arxiv.org/pdf/2511.14930
pages: 49
chars: 96130
fetched_at: '2026-11-08T13:08:33+00:00'
kb_version: 1
---

# Fifty Shades of Greenwashing: The Political Economy of Climate Change Advertising on Social Media

Fifty Shades of Greenwashing: The Political
Economy of Climate Change Advertising on
Social Media
Robert Kubinec †,1 Aseem Mahajan †,2,*
November 18, 2025
In this paper, we provide a novel measure for greenwashing – i.e., climate-related
misinformation – that shows how polluting companies can use social media adver-
tising related to climate change to redirect criticism. To do so, we identify green-
washing content in 11 million social-political ads in Meta’s Ad Targeting Datset
with a measurement technique that combines large language models, human coders,
and advances in Bayesian item response theory. We show that what is called green-
washing has diverse actors and components, but we also identify a very pernicious
form, which we call political greenwashing, that appears to be promoted by fossil
fuel companies and related interest groups. Based on ad targeting data, we show
that much of this advertising happens via organizations with undisclosed links to
the fossil fuel industry. Furthermore, we show that greenwashing ad content is
being micro-targeted at left-leaning communities with fossil fuel assets, though we
also find comparatively little evidence of ad targeting aimed at influencing public
opinion at the national level. The supplementary information can be downloaded
from this link.1
† These authors contributed equally to this work.
1 University of South Carolina
2 KAPSARC School of Public Policy
* Correspondence: Aseem Mahajan <aseem.mahajan@kspp.edu.sa>
1We thank Jieun Byeon, Ryan Lohr, Ellis Padgett, and Aliza Danish for invaluable research assistance. We
thank New York University Abu Dhabi High Performance Computing Centre and the Texas A&M ACES
supercomputer for computing support. We thank attendees at the 2024 Language Models in Social Science
conference for helpful comments. We acknowledge support from the National Science Foundation ACCESS
program for computational resources.
1
arXiv:2511.14930v1  [stat.AP]  18 Nov 2025

Introduction
Growing awareness of climate change over the last thirty years has spurred political efforts
to replace fossil fuels with renewable energy through regulations, tax credits, and subsidies.2
It has also shaped individual preferences, giving rise to “green consumers,” who consider
the environmental impacts of companies or products in their purchasing decisions (Peattie
2010). Between growing pressure from policymakers and consumers, companies have increasing
incentives to persuade the broader public that their products help to alleviate the harms of
warming to avoid adverse regulatory decisions or consumer boycotts.
These trends raise concerns that firms may mislead the public about the environmental effects
of their practices or products, a practice commonly described asgreenwashing.3 In recent
years, political agencies across continents have taken aim at corporate greenwashing (Bryan
2023; Speed 2024; Ring and Speed 2023), levying millions of dollars in fines.4 Over 2023 and
2024, United Kingdom (UK) regulatory authorities banned asset managers from making mis-
leading claims about sustainability (Bryan 2023) and conducted “wide-ranging clampdowns”
on consumer-facing companies that make false environmental claims (Speed 2024; Ring and
Speed 2023). In the same period, the European Commission investigated twenty airlines for
making misleading greenwashing claims (European Commission 2024), and the Australian Se-
curities and Investment Commission (ASIC) took civil action against Vanguard Investments
for environmental, social, and governance (ESG) claims (ASIC 2024).
In the context of climate change, firms that greenwash may overstate the extent to which
their corporate social initiatives regulate greenhouse gas (GHG) emissions or counteract their
effects.5 Such behavior is in keeping with a large body of research on political lobbying, which
2Data from the Climate Policy Radar Database shows nearly a twenty-fold increase in climate laws and policies
between 1997 and 2018, from 72 to 1,500 (Nachmany and Setzer 2018).
3The definition ofgreenwashing presented here is a slight modification of one developed by Greenpeace, who
describe it as “the act of misleading consumers regarding the environmental practices of a company or the
environmental benefits of a product or service.”
4Deutsche Bank, for instance, paid the SEC $25 million for overstating the weight placed on environmental,
social, and governance (ESG) factors in funds.
5An analysis of ExxonMobil’s “Energy Solutions” advertisements by Plec and Pettenger (2012, 466) demon-
strates how the campaign constructs a greenwashed frame “by highlighting and amplifying science, technol-
2

demonstrates how private interests strategically appeal to the public to achieve political ends
(Kollman 1998; Baumgartner et al. 2009; Dür and Mateo 2016; Dür 2019; McKnight and
Hobbs 2013) and use voluntary environmental self-regulation to preempt public regulation
(Potoski and Prakash 2011, 2004; Malhotra, Monin, and Tomz 2019).6 Firms hold incentives
to make misleading claims7 — indeed, the fossil fuel industry has a long-history of doing so
(Oreskes and Conway 2011, 6; Supran and Oreskes 2017) — and these persuasion efforts can
have political consequences.
We propose a theory of greenwashing that distinguishes between greenwashing aimed at avoid-
ing adverse regulatory action versus advertising which is aimed at attracting climate-conscious
consumers. We argue that what we termpolitical greenwashing is more relevant to policy out-
comes concerning climate change. What we callconsumer greenwashing, on the other hand,
may meet some technical definitions of greenwashing defined in the literature but is theoret-
ically distinct from the greenwashing aimed at achieving corporate political aims. It is this
former kind of greenwashing that we believe to be of greater significance to policy efforts
to control climate change as its aim is to undermine costly efforts to move away from fossil
fuels.
To understand how political greenwashing occurs, we derive a novel measure of greeenwashing
from approximately 1 million Facebook and Instagram advertisements in Meta’s Ad Library
and Ad Targeting Dataset (collectively, “Meta Ad Data”). Due to the complexity of the
concept, we employ methodological triangulation, including human coding, large language
models, and regular expression matching, which we then feed into a robust Bayesian item
ogy, and the expertise of authorities” to “persuade consumers that oil companies will be the caretakers of
our environment.”
6The literature on self-regulation generally describes interactions between firms, who voluntarily choose to
disclose potentially incriminating information about themselves, and regulators, who choose whether self-
regulation is preferable to public regulation and, if so, how such a system should be designed. However,
firms’ incentives to self-disclosed remain the same even in a less organized environment. By self-disclosing
to the public, firms may preempt them from demanding more stringent regulation from policymakers.
7As Dür (2019) points out, David Truman, in an early book about the interaction between interest groups and
the public, writes that “almost invariably one of the first results of the formal organization of an interest
group is its embarking upon a program of propaganda, though rarely so labelled, designed to affect opinions
concerning the interests and claims of the new group” (Truman, David B 1951, 213).
3

response theory model (Kubinec 2025). From this system, we create nuanced ad-level political
greenwashing scores with uncertainty and robustness to non-ignorable missingness.
As we show with these measures, the firms that are most affected by political regulation
are also those most likely to engage in political greenwashing. Furthermore, political green-
washers appear to target audiences where a fossil fuel company’s assets are located. In these
environments, we show that advertisements with political greenwashing will target influential
demographic groups and areas where fossil fuel companies face possible adverse regulatory
decisions. At the same time, we show that this type of advertising does not appear to be
aimed at influencing national-level public opinion. Social media advertising seems most useful
to businesses as a micro-level political strategy that can protect important investments.
Theory
In this paper we are focusing on the role of economic actors with a vested interest in under-
mining climate change policies, specifically companies in the fossil fuel industry (Mildenberger
2020; Stokes 2020; Lucas 2021; Tienhaara 2018). For these companies, a transition away from
fossil fuels would reduce the value of their fixed assets in production; these cannot be easily con-
verted to renewable production, with some notable exceptions such as the growing geothermal
industry (Anderson and Rezaie 2019). Ownership of oil wells, natural gas pipelines, offshore
platforms and other assets is a rent that will lose value if governments force consumers to
transition to renewable energy. For these reasons, these companies have a significant financial
interest in opposing regulation that would reduce demand for fossil fuel companies up to the
value of these rents. We should expect based on standard political economy theory that these
firms should be willing to undertake costly actions to protect these investments, and indeed
there is a substantial empirical record of such actions (Mulvey et al. 2015).
At the same time, this view of the firm can be considered reductionist in that it ignores the
possibility that shareholders and managers could exercise a form of enlightened self-interest
in which they support an energy transition while they deplete their existing fossil fuel assets
4

(Nasiritousi 2017). The theory ofcorporate social responsibility proposes that companies can
indeed undertake relatively altruistic actions, especially when there are related benefits to the
firm through improving its image to consumers (Carroll, Primo, and Richter 2016). Fossil fuel
companies are actively involved in CSR (Megura and Gunderson 2022), and in principle they
could support climate change alleviation efforts out of an awareness of their responsibility for
the damage to the environment caused by their fossil fuel production. Fossil fuel involvement in
CSR could also be strategic to avoid blowback from consumers or policymakers who might see
any obstructionist political activity as behavior that should be punished (Bergman 2018).
For these reasons, there are competing incentives that make the strategic use of advertising
on social media by fossil fuel companies an open question. Will fossil fuel companies adopt a
relatively altrustic strategy that supports climate change policies out of a sense of corporate
socialresponsibility, orwilltheyseektopersuadevotersthatclimatechangeislessofaproblem
and governments should avoid adopting costly climate change policies? The individual nature
of social media, which permits individual fossil fuel companies to create their own accounts
and target audiences at the micro level (Macdonald, Gunderson, and Widner 2024), creates an
opening for this type of behavior to be observed with much more precision than was previously
possible. Furthermore, social media offers corporations the ability to advertise with plausible
deniability because they can run ads through accounts aﬀiliated with third parties that are
ostensibly independent entities.
This research question is of broader significance as well because fossil fuel companies are some
of the central actors in the growing climate crisis. Social media permits these companies the
chance to influence public opinion in a way that is unprecedented in human history, and we
as yet lack a clear understanding of how this type of political activity works and how effective
it might be. For these reasons, we theorize that this type of activity could depend as well on
the type of political institutions in a given country. Where public opinion is quite important,
which would generally happen in regimes that are more accountable and responsive (Slater
2008), then we might expect that companies will have a greater incentive to strategically shape
public opinion on climate change in an anti-regulation direction. In less democratic countries,
5

by contrast, fossil fuel companies might need to rely more on strong relationships with elites
as institutions are by definition not as responsive to the median voter (Kakenmaster 2024;
Francis and Kubinec 2025).
To study this research questions, we will need to also build a conceptual foundation for the
behavior we want to study: so-called greenwashing by corporations. If corporations are using
social media to influence public opinion in anti-regulatory direction, then they are likely en-
gaging in greenwashing by diverting attention from costly policies towards solutions that are
more amenable to continued fossil fuel production. In other words, it is unlikely that fossil fuel
companies will simply argue that global warming does not exist or that citizens should ignore
it; rather, they will employ more sophisticated outreach strategies that confuse and re-direct
climate concern. For these reasons, we focus on greenwashing as a viable advertising strategy
that could undermine climate action in a way that is diﬀicult to detect, permitting fossil fuel
companies to achieve their strategic objectives while minimizing blowback.
Becauseresearchongreenwashingspansdisciplinesandmeasuresdifferentbehaviors, paperson
the subject likewise use various data and definitions to assess public claims made by actors. In
a systematic review of the “greenwashing literature,” Lyon and Montgomery (2015) finds that
most quantitative empirical papers use companies’ annual reports (Wiseman 1982; Ingram
and Frazier 1980), corporate social responsibility (CSR) reports/disclosures to investors or
nonprofit organizations8 (Mahoney et al. 2013; Uyar, Karaman, and Kilic 2020; Tang and
Demeritt 2018) and their websites to assess claims about environmental performance. Similar
sources of data used in existing literature include corporate indices such as Bloomberg ESG
scores (Yu, Van Luu, and Chen 2020; Yu, Guo, and Luu 2018; Tamimi and Sebastianelli 2017)
and lists of corporate environmental scores published by news publications (Du et al. 2014).
Besides these studies, which examine greenwashing across various industries, others measure
greenwashing using ecolabels (Sirieix et al. 2013) or ISO 14001 certification, earned by meeting
standards in voluntary environmental audits (Potoski and Prakash 2005; Blackman 2012).
8One frequently source of data are company disclosures to the Carbon Disclosure Project nonprofit organization
that assists public and private actors disclose information about their environmental impact.
6

These studies use firms as their unit of analysis. Additionally, public statements or signals
of environmental compliance in these studies are directed to a narrow group of stakeholders,
such as investors or regulators.
Whilegreenwashingcanbedoneviaanymedium, theriseofsocialmediahasgivencorporations
and interest groups a novel platform which which to shape their image, as existing research
has shown. Using Twitter’s academic API, Blazkova et al. (2023) examine half a million
tweets containing the keywords ‘greenwash’, ‘greenwashing’, and ‘greenwashed,’ performing a
content analysis and identifying key stakeholders involved in these threads. Similarly, Amin,
Ali, and Mohamed (2024) analyze approximately 170,000 tweets issued from the accounts of
companies on the FTSE 350 Index, using a structural topic model to measure the adoption
and extent of corporate social responsibility (CSR) disclosure. Finally, Kwon et al. (2024)
analyzes Instagram posts between 2019 and 2021, focusing on posts issued by the 15 most
reputable companies in the world, as measured by GlobalRepTrak 100, a ranking of corporate
reputation issued by RepTrak, a reputation intelligence platform. Analyzing nearly 17,000
posts, it identifies 394 green advertising posts.
Although there is a substantial amount of research on greenwashing, there is little agreement
in the literature about how the concept is defined or measured. Given that the aim of this
paper is in understanding greenwashing by fossil fuel companies, we propose that greenwashing
should be differentiated betweenpoliticalgreenwashing andconsumer greenwashing. We argue
that these two types of greenwashing have different aims, and while they both may include
information about climate change and corporate behavior that is misleading in some sense,
they are unlikely to have similar effects in terms of shaping public opinion. Climate change
regulatory policy will affect fossil fuel producers much more heavily than most companies, and
for that reason, many companies would prefer to bolster their climate change bona fides out
of an effort to win over climate-conscious consumers rather than in an attempt to reduce fears
over climate change.
Separating these two types of greenwashing requires nuance and an awareness of the context
of the company behind the advertising. As we explain later, our measurement strategy uses
7

a diverse array of indicators to differentiate types of greenwashing. Ultimately, we want to
isolate that type of greenwashing that could benefit fossil fuel companies by diverting the
public’s concern over climate change. There are many other types of climate change-related
advertising, some of which can fit definitions of greenwashing as proposed in the literature, but
we argue that greenwashing that is primarily aimed at attracting climate-conscious consumers
using claims that may be more or less accurate is of less importance to the study of the
political economy of climate change. For these reasons, our main aim in this study is to see to
what extent fossil fuel producers and related actors are engaged in political greenwashing, and
more specifically, how they might be doing so via social media accounts, whether via oﬀicial
or unoﬀicial accounts.
Hypotheses
Once we have overcome the measurement challenge, our research design incorporates relatively
straightforward observational inference. Due to our theoretical priors that we specified above,
we think that higher levels of political greenwashing among fossil fuel producers and their
allies would be evidence that these companies are attempting to undermine costly policy
efforts to oppose climate change. While our research design is not causally identified, we still
have reason to believe that these associations are informative as we do not think there are
relevant confounders that could produce a spurious assocation. In other words, if we can find
associations between fossil fuel producers and greenwashing, we believe that this association is
most likely due to the companies’ investment in fossil fuels rather than some other unobserved
factor. This confidence derives from the research we cited earlier about the profit maximization
incentive of corporations and the real and present danger that costly climate change policies
pose to their bottom line.
For these reasons, we want to collect data on the different types of advertisers who are engaging
in any kind of climate change advertising. These other actors comprise the null hypothesis or
reference group by which we can evaluate the possible greenwashing of fossil fuel companies.
8

Furthermore, we will gain important descriptive information from having a more general sense
of the state of climate change advertising that will be of interest to policymakers and other
scholarly work on the topic.
We also want to collect information on the identity of a variety of types of interest groups with
potential links to fossil fuel companies. Part of the strategic nature of corporate advertising
is that it may come from relatively neutral-seeming trade associations or think tanks. If
corporations are funding these interest groups, then the climate change advertising that these
other organization undertake is essentially directed by the funders but with the deniability
of a separate organizational platform. For these reasons, we do not restrict ourselves only to
fossil fuel companies and their subsidiaries but also interest groups with which they share some
relationship.
With this combined dataset of the identity of advertising actors and the level of greenwashing,
we aim to test the following hypothesis:
H1: Fossil fuel companies and related interest groups are more likely than other
climate change advertisers to engage in political greenwashing.
In addition to this hypothesis, we want to further understand to what extent this type of
advertising is related to political institutions and to the nature of political competitions. We
hypothesize that if our theory is correct then we should be able to detect more greenwashing
in countries where popular legitimacy is more important; i.e., in democratic countries. We
further think that greenwashing should be more evident among groups that are important for
electoral reasons, especially older demographics that are more likely to vote.
In the United States, members of the Baby Boomer generation hold the largest share of
wealth (Board of Governors of the Federal Reserve System 2025), have the highest average
net worth (Board of Governors of the Federal Reserve System 2023) and vote at higher rates
than other generations (Pew Research Center 2023). Consequently, political and economic
actors may have greater incentives to influence their behavior and misrepresent their actions.
In contrast, individuals under 18 are least likely to make household purchasing decisions or
9

vote. Greenwashing could therefore be less prevalent in this cohort. Advertisers may also hold
a longer-time horizon with regard to younger generations, choosing to avoid greenwashing to
avoid damaging their brand.
To better understand the extent to which greenwashing is associated with political institutions
and demographics, we aim to test the following hypothesis:
H2: Greenwashing ads are more likely to occur in more democratic countries and
among older demographic groups.
An important feature of social media ads is micro-targeting, or the ability to only show ads
to very specific subsets of users based on geographic and other criteria (Kreiss 2017; Dobber,
Fathaigh, and Borgesius 2019). Based on the theory we have proposed, we have reason to
believe that corporations would also micro-target ads, specifically if there are existing assets
or investment opportunities in the given area. This micro-targeting approach contrasts with
H3, which examines prevalence of greenwashing across the social media landscape. As a result,
we want to test a third and final hypothesis:
H3: The presence of fossil fuel investments in a given geographic area is associated
with a greater prevalence of greenwashing content targeted to that area.
Data
To obtain real-world measures of political and consumer-oriented greenwashing, the data used
in this paper conducts a comprehensive analysis of the universe ofall Social Issues, Electoral,
and Political ads in English classified by Meta (Facebook’s parent company), which includes
all ads related to environmental issues.9 In addition to ads run by corporations, the dataset
includes statements by nongovernmental and international organizations, political actors, and
interest groups. As Lyon and Montgomery observe, existing greenwashing literature “shows
9See section Section for a description of Meta’s classification scheme.
10

that just like corporations, NGOs, and governments can engage in greenwashing; indeed, they
may often serve as partners in corporate greenwashing” (2015). The scope of actors included
in the dataset allows the paper to examine greenwashing conceived more broadly. The Meta
Ad Datasets have the added benefits of including specific data about the audience targeted by
advertisers. This allows the paper to present new information about which audiences compa-
nies intend to address and which audiences are exposed to greenwashing. Finally, advertisers
must pay money to run ads on Meta’s platforms, and audiences may therefore pay these ads
more attention than social media posts from other individuals.
As we explain further below, the Ad Library includes information about the delivery of adver-
tisements while the Ad Targeting dataset describes the audience that the advertiser seeks to
target.
Meta Ad Data
Facing criticisms about its advertising technology10, Facebook revised its terms of service in
2018 to limit the scope of advertising allowed on its platform, regulate advertisers, and increase
transparency (Bouchaud 2024). In 2019, Facebook, Inc. (rebranded as Meta in 2021) intro-
duced its Ad Library, a collection of information about ads focusing on SIEP advertisements
(Shukla 2019). Beginning in May 2022, Meta began publishing this information, along with
ad targeting information, for SIEP ads run on the platform starting from August 2020 (Meta
Platforms 2024). Ads classified as SIEP include (Meta Business Help Center 2025):
• Those made by a political actor or organization or advocates for an election outcome;
• Ads about any election, referendum, or ballot;
• Ads regulated in the advertiser’s country as political advertising; and
• Ads about any social issues in the place where the ad is being placed.
10Leading into and following the 2016 United States (US) presidential election, Facebook faced accusations
of purveying misinformation and contributing to political polarization Levin (2017). In the same year,
a ProPublica investigated revealed that Facebook’s advertising technology allowed marketers to exclude
specific ethnic groups by race (Angwin and Parris, Jr. 2016), leading to the US Department of Housing and
Urban Development to lodge a formal complaint against the company (Isaac and Hsu 2021).
11

Thefinalcategoryincludelocalsensitiveorheavilydebatedtopics, particularlythosethat“seek
to influence public opinion through discussion, or debate or advocacy for or against important
topics, like health and civil and social rights” (Meta Business Help Center 2025). For the entire
European Union and fourteen countries, Meta has developed a top-level country-specific list
of topics considered sensitive. The topic of environmental politics is included in all of the
lists. To identify and review SIEP ads, Meta relies on self-reporting by advertisers; automated
technology that reviews ad images, video, text, targeting information, and landing pages; and
manual reviews of ads. Ads are reviewed on a monthly basis and sometimes reclassified.
The Meta Ad Library and Ad Targeting Dataset comprise the Meta Ad Data used in this
paper (Meta Platforms 2024). The Ad Library includes information about the delivery of
advertisements. This includes text of the advertisement, the page associated with the adver-
tisement, the period over which the advertisement ran on Meta, and information about the
audience reached by the ad (e.g., demographic distribution, number of impressions, etc.). The
Ad Targeting Dataset, which maps to entries in the Ad Library, describes the audience that
an advertiser sought to target with a particular ad. It provides information about the tar-
geted audience’s location, age, gender, and language. Additionally, it describes whether and
how to target the ad to audience’s connections (Meta Platforms 2024). To ensure consistency
throughout the analysis, we focus on ads appearing in the Ad Library as of December 20,
2024.
Measurement
To capture political greenwashing, as opposed to more anodyne forms of grenwashing, we need
to employ diverse types of indicators with respect to climate change discourse, using both
quantitative and qualitative measurement strategies. By doing so, we can cast a broad net
to measure the complexities and nuances of political greenwashing in order to overcome the
ability of corporations and related interest groups to mask such advertising. We further want
to combine robust measures of greenwashing with covariates that relate to the identity of the
12

advertising entity so that we can understand what types of actors undertake greenwashing.
In particular, we want to understand how much greenwashing relates to political-economic
theories of corporations with strategic reasons to prefer less climate change regulation.
The measurement challenge we need to overcome is separating greenwashing from less strategic
forms of discourse around climate change. This task is no trivial matter as it is easy for an actor
to claim that it does not want climate change to occur, i.e., cheap talk. The difference between
discourse that diverts attention from costly solutions to climate change and a discourse that
has an aim of mitigating climate change can be one of considerable nuance. Furthermore, if
our theory is correct that fossil fuel producers are more likely to politically greenwash in order
to secure valuable political concessions, then these companies will have both the incentive and
resourcestomaketheiradvertisingeffortsrelativelysubtle. Forthesereasons, ourmeasurement
strategy triangulates across both qualitative and quantitative measurement techniques in order
to best identify the latent trait we want to capture.
Qualitative Coding of Political Greenwashing
Our qualitative approach to measuring greenwashing involves the use of regular expressions to
match specific keywords and employing human coders to identify social media accounts with
known linkages to the fossil fuel industry.
Table 1: Number of observations by keyword
Description Number of Observations
carbon capture 34,547
carbon remov* 1,194
climat* 124,838
coal 10,711
extinction 6,848
fossil fuel 11,974
13

Description Number of Observations
global warming 4,214
greenhouse 7,195
icecapand melt OR icecapand flood 24
recycle 22,825
sustainable 71,605
any keywords 235,032
Regular expression matching is used at two stages in our research design. First, we employ a
broad list of terms because we need to filter out from Meta’s massive Ad Library Dataset—
which has over 10 million ads—those ads that do not have any relationship to climate change
(or even the environment). At the same time, we need a list of terms that is broad enough
to capture all ads that have at least some positive probability of being greenwashing. Begin-
ning with basic words like “climate change”, we developed a broad list of 191 terms using
embeddings, i.e., we provide a prompt to large language models to provide synonyms of these
key words. Given that Meta’s database includes ads from all over the world, we translate
the keywords and regular expressions into 12 commonly-spoken languages–Arabic, Bengali,
Urdu/Hindi, Tagalo, Mandarain, Indonesian, Portuguese, French, Spanish, Swahili, Russian,
and German–so that we can obtain the universe of climate-related ads. The regular expressions
we employed are shown in SI section 3.
As a second filtering step, we removed ads that were primarily deployed for electoral purposes,
such as those referencing a specific candidate or campaign. A large share of the SIEP ads
are those run by U.S. electoral campaigns, and electoral campaigns are outside the scope of
our study as they have a different aim than influencing the pro- or anti-climate views of the
population. This step is especially important for identifying political greenwashing as we need
ads that are about climate change, have a politically-relevant theme, but are not appealing
for respondents to vote for a specific candidate.
14

The filtered list of ads included 1,176,612 ads from the larger dataset. With this smaller, yet
still quite large, list, we then coded ads for the presence of specific terms which we had a
prior reason to believe could be related to greenwashing, including a mention of technologies
known to be used as excuses for climate action by fossil fuel companies, including clean coal
and carbon capture. The particular way we operationalize these indicators using regular
expressions is shown in Table1. Each ad had a value of 1 if it matched the term and 0
otherwise, and these terms were also translated into other languages for non-English ads.
For our second form of qualitative measurement, we hired human coders to create a list of
fossil fuel companies and related interest groups, and then to comb through Meta’s list of
pages with related ads to see if there were matches. To identify advertisements by fossil fuel
companies, we supplement a list of the top investor- and state-owned companies ranked by
potential emissions from reserves (Heede 2013, 2014; Heede and Oreskes 2016) with a manually
compiled list of fossil fuel companies, interest groups, and aﬀiliates. The interest groups were
derived from policy reports by the climate change think tank InfluenceMap11 that identify
linkages between fossil fuel companies and other interest groups. In total, we identify 18 pages
associated with fossil fuel companies or aﬀiliates in the Meta Ad Data in English, which ran
2,155 ads. Of these, we identified 240 ads by fossil fuel actors that were also related to climate
change.
In addition to InfluenceMap, we used existing published lists to identify fossil fuel entities in
the social media data. Using production records from annual reports, public libraries, websites,
and US Security and Exchange Commission reports, and other sources, Heede (2014) calculates
historical fossil fuel production and carbon emissions for 90 entities producing more than eight
million tonnes of carbon per year. From this analysis, Heede and Oreskes (2016) focuses on
seventy companies and eight government-run entities producing 63% of fossil fuels between
1750 and 2010.12 It calculates potential emissions from the reserves of the seventy investor-
and state-owned companies, using self-reported reserves data. We conduct searches for pages
11See https://influencemap.org/ for more information.
12oreskes_footnote
15

associated with these companies or companies with similar names using regular expressions.
After eliminating pages with similar but unrelated names, this search produces sixty-nine pages
associated with twenty-one companies. Additionally, it produces seven page names associated
with five related interest groups or aﬀiliates. To add to this list, we (i) review the names of
all page names in the Meta Ad Data in English, identifying and investigating pages whose
names suggest that they might be associated with fossil fuel companies; and (ii) performing a
search for Meta pages associated with interest groups in an external list of groups developed
by InfluenceMap.
With this qualitative measurement, we are able to create further binary variables for our ads
dataset for whether a page is an oil company, a related interest group, think tank, or other
type of actor with some known link to the fossil-fuel industry. In total we were able to identify
233 pages in the Meta Ad Library that had such a known link.
Quantitative Measurement Evaluation
We also made use of quantitative techniques for measuing discourse given the large scale of
the data. However, it can be very diﬀicult to capture nuance from more simple text analysis
models like the “bag of words” approach; an ad could contain many references to carbon
capture, coal, and carbon removal yet still be aimed at increasing rather than reducing the
climate policy response. For these reasons, we introduce an ensemble of open-source large
language models (LLMs) as a way of providing much more nuanced coding of greenwashing.
An LLM is trained on a large corpus of diverse texts and represents these texts in a continuous
latent space known as “embeddings” (Rodriguez, Spirling, and Stewart 2023). Given an input
text, LLMs will select the highest-probability tokens conditional on the input, which can be
almost completely unstructured (Weber and Reichardt 2024).
To increase our measurement validity, we employ six open-source LLMs: Mistral:7b (Jiang et
al. 2023), Llama 3.2:3b (Touvron et al. 2023), Phi3 (Abdin et al. 2025), Gemma2 (Team
et al. 2024), Deepseek-r1 (Guo et al. 2025), and Qwen2.5:7b (Yang et al. 2025). We use
16

open-source models so that we can better ensure reproducibility by setting seeds and storing
model weights (Barrie, Palmer, and Spirling 2024). These models are small to medium LLMs
that can be operated with a single standard 16-GB GPU, which makes our method feasible
without access to very large GPUs or expensive computational resources.
The prompt we provide the LLMs is as follows:
Advertisement Text: [“ad text to classify”] : You are a human bot evaluating a
number of advertisements on webpages. You are given the text of the advertisement
and name of the website after _____.
Based on this information, your task is to answer the following question:
Greenwashing is the act of making false or misleading statements about the climate
impact of a product or practice. It can be a way for companies to maintain or
increase their greenhouse gas emissions. Is this ad engaged in greenwashing?
Your must choose exactly one of the following predefined answers: yes, no
You will only respond with the answer. Do not repeat these instructions or include
the word ‘Answer:’ before giving your answer. Do not give any explanations or
notes.
While the text of the prompt constrained the LLM to an extent, the LLM still sometimes
returned additional unstructured text in its response. As a result, we coded the response as
a 1 if we could identify a positive response in its answer, and 0 if a negative response, and
in cases where we could not identify an answer, we coded the response as missing (i.e., a
hallucination).
To directly evaluate the LLM, we randomly selected 1,000 ad texts and assigned them to be
coded as either having or not having greenwashing by three research assistants (RAs). Our
RAs had at least undergraduate or graduate degrees in the social sciences, and were given the
same prompt as the LLM for the purposes of fairness. To facilitate a comparison with LLMs
and their extensive training data, we allowed the RAs up to five minutes per coding to search
17

for background information about the ad. We report the results of this evaluation exercise
in SI Section 1. In short, the LLMs had a strong tendency to over-classify ads as containing
political greenwashing relative to RAs, and the Llama 3.2:3b model showing the strongest
overlap with human coding decisions. As such, while it is clear from the exercise that LLMs
can identify this type of speech, they are also relatively noisy when considered individually.
Besides LLMs, we also include a model known as DEBATE (Burnham 2025) that is a BERT
formulation (Bidirectional Encoder Representations from Transformers). This model has been
trained to identify stances in political texts. To employ the model, we have it determine
whether a specific hypothesis (i.e., declarative statement), namely whether the ad in question
opposes efforts to mitigate climate change, is supported for a given ad. While this is a concep-
tually simpler prompt than the one we give to LLMs, this type of information is quite useful
for estimating our greenwashing scores as we describe later. We code our ads with this model
with a 1 if they are pro-climate change action and 0 otherwise.
Combining Measures Into a Greenwashing Score
All of the methods of measurement we have mentioned previously have limitations. The
unstructured nature of LLMs, for example, can also produce random sequences of text or a
complete misreading of the prompt (Tonmoy et al. 2024). Qualitative measures are diﬀicult to
replicate for the entire dataset, and relatively simple measures like binary indicators for words
are unlikely to capture suﬀicient nuance. However, each of these measurement strategies has
its own strengths as well. For these reasons, we want to find a way to incorporate as much
of the information in each individual measure while also safeguarding against non-ignorable
measurement error.
To produce an aggregate greenwashing score at the ad level we turn to the ideal point model
parameterized via Bayesian item-response theory (Bafumi et al. 2005; Clinton, Jackman, and
Rivers 2004; Kubinec 2025). The advantage of using IRT to aggregate across diverse indicators
is to allow us to incorporate measurement error in a principled way. For example, by using
18

the LLM output as input to a measurement model, we can accept that LLMs will sometimes
fail or “hallucinate” and allow that uncertainty to propagate as measurement error (Burnham
2023; Green et al. 2025). A structured measurement model will also give valuable insights
into how these indicators are plausibly related to each other and to the latent concept we seek
to measure.
We do not further define IRT or Bayesian measurement models here as we note there is a
robust literature on the topic (Bafumi et al. 2005; Clinton, Jackman, and Rivers 2004; Park
2011; Hanson and Sigman 2021; Pemstein, Meserve, and Melton 2017). Our particular variant
of IRT is known in political science as the ideal point model given that it will provide latent
scores that can be interpreted as the ideal points of legislators (Clinton, Jackman, and Rivers
2004). However, as we are scaling ad texts rather than persons, we note that this variant
of IRT allows us to have bipolarity in the item indicators, that is, our possible indicators
for greenwashing can be either positively or negatively related to greenwashing. The model
estimates will provide us with both the sign and magnitude of this relationship via the item
discrimination parameters.
However, the flexibility of the ideal point model comes with a price as it requires informative
priors on at least some parameters to identify the rotation and scale of the latent variable
(Bafumi et al. 2005). Our IRT specification via Kubinec (2025) uses a re-scaled Beta distri-
bution for the item discrimination parameters as the primary means of identification of the
latent variable; this distribution forces all item discrimination parameters to lie within the
open interval of (-1,+1). To identify the sign of the latent variable, we further assign a strong
positive prior on our indicators for the phrase “natural gas” of Beta(1000, .001) and a strong
negative prior on the phrase “fossil fuel” of Beta(.001, 1000). We use these priors by examin-
ing the relative frequency of our indicators for ads that we manually classified as belonging
to fossil fuel companies—we found that “natural gas” appeared much more often in these ads
and “fossil fuel” appeared much less. As such, we believe that these priors will be helpful
to identify the latent trait of political greenwashing. In addition, the stochastic nature of
our measurement model does not require a mechanistic relationship between these informative
19

priors and the latent trait. So long as these relationships hold on average in the data (i.e., are
more right than wrong), then we can identify a unique rotation of our greenwashing scores
that is conditional on this prior information about the likely nature of greenwashing.
There is another important facet of the data that we need to incorporate–the ability of LLMs
to “hallucinate” or return responses that are outside the scope of the prompt or otherwise
irrelevant. To permit us to incorporate this type of non-ignorable missigness in the data along
with parallelism to handle the large data size, we employ the parameterization of Kubinec
(2025) that explicitly accounts for potential bias in missing data by fitting a separate first-
stage IRT model for whether the measurement is missing. By doing so, we obtain missingness
item discrimination parameters as described by Kubinec (2025) to allow us to adjust our scores
for LLMs potentially hallucinating more often when ads have very high or very low levels of
greenwashing. We employ default priors for other parameters as specified by Kubinec (2025).
We note that our empirical approach also breaks new ground in applying emerging tools –
specifically, LLMs – to diﬀicult measurement challenges. While LLMs have received enormous
attention in industry and academia in recent years (Manning, Zhu, and Horton 2024; Hack-
enburg and Margetts 2024; Dubova, Moskvichev, and Zollman 2024; Marshall et al. 2024),
it can be diﬀicult to incorporate them into robust research designs because LLM output is
not always reliable due to “hallucinations” (Tonmoy et al. 2024), or in more conventional
terms, non-classical measurement error. For these reasons, our research design discussed in
this section is aimed at taking advantage of the remarkable breadth of LLMs while adding
additional information from external sources to anchor estimates via IRT.
Results
Greenwashing Scores
We next turn to a discussion of the greenwashing scores that were derived from the measure-
ment model that we described earlier. Because these results derive from a principled Bayesian
20

item-response theory model, we have uncertainty in the scores at the ad level even with the
limited number of observations per ad. We show the full distribution of the mean of the poste-
rior draws (i.e., the point estimates) with 5% to 95% quantile uncertainty intervals in Figure1.
Positive values of the score indicate a higher probability of greenwashing while lower values
indicate a lower probability of greenwashing, though the exact value of the score is based on
an arbitrary scale centered around zero as is convention in IRT estimates.
Figure 1: Distribution of Posterior Uncertainty Intervals for Ad-level Greenwashing Scores
−10 −5 0 5 10
Greenwashing Score
Classified
FALSE
TRUE
Plot shows median posterior values and posterior 95% −
5% quantile intervals for an IRT ideal point model fit to
Facebook social and political ads. Higher values indicate
more likely to be engaged in greenwashing. Ads for which
uncertainty intervals do not overlap 0 are labeled as
classified. Plot was downsampled to 100,000 ads for
visualization purposes.
What is immediately evident from Figure1 is that there is substantial uncertainty in the
scores at the ad level. This uncertainty derives from the fact that we have 15 indicators per ad.
While this is a reasonable number for an index, we have only observation of these indicators
per ad. For this reason, while the spread of the mean scores is quite large, the model can only
21

classify approximately 21.8% of ads as being either related or unrelated to greenwashing with
high probability, with 3.1% of ads classified with political greenwashing and 18.7% without
greenwashing. While the number of positively-classified ads with high probability is relatively
small, we note that this number is reasonably close to the proportion of greenwashing we
estimated with human coders at 1.6% (95% CI, 0.9% - 2.5%) (see SI Section 1).
We validate the model in two different ways. First, we look at the ads that were classified
as having the highest probability of greenwashing, which we show in Table2. Ads in other
languages are translated into English, and for space limitations, we only show the first 250
characters of the ads (some of the ads only mention climate change related issues later in the
post). The German ads are calling for international cooperation for or against gas exporting
countries (i.e., Qatar and Russia), while the English ads are more focused on supporting oil
and gas industries in particular U.S. states. We note that the posterior uncertainty of these
scores is quite high, but even so, the vast majority of these ads would fit the core ideas of
greenwashing that we discussed previously, albeit with contextual features that are unique to
a given social and political context.
Second, we can examine the item discrimination parameters from the IRT model in Figure2.
A discrimination parameter is very useful for this measurement exercise because it shows which
indicators (items) “load”, or have the highest information, about the latent trait we are trying
to measure. It is important to note that the discrimination parameters have additive effects,
so even smaller discrimination values can matter for measuring the latent trait given that they
still contain some unique information. On the other hand, a discrimination parameter of zero
would indicate no information about the latent trait–the indicator has essentially dropped out
of the model.
Figure 2 shows the posterior mean value of the discrimination parameters for each indicator
with the 5% to 95% posterior quantile to capture uncertainty. Uncertainty for these scores
is quite small given that the number of items (15) is small relative to the number of ads,
resulting in a large amount of data per parameter. As discussed in the methods section,
we added informative prior information that the presence of the term “natural gas” should
22

Table 2: Top Ten Ad-level Greenwashing Scores
Ad Text Language 5% Low
Score
Posterior
Mean
95%
High
Score
++ The motto must be less Qatar, not more! ++ Human
rights violations, a strict ban on homosexuality, exploitation
of migrant workers, corruption in the World Cup award: For
Minister-President Stephan Weil (SPD), Qatar is nevertheless
a reliable
German 3.06 7.05 10.9
New Mexico is a leader in energy production through oil and
natural gas. We can’t allow the far Left to keep the state from
producing.
English 3.06 6.99 11.7
 Happy to announce $16.2M to build a 92km natural gas
pipeline from Peace River to La Crete with MLA Dan
Williams.  This strategic infrastructure project will provide
safe and secure supply for residents and increase the potential
to grow the reg
English 3.06 6.71 11.5
Oil and natural gas is keeping our economy strong! Stand up
to radical environmentalists to ensure we have a vibrant Texas
economy.
English 2.65 6.55 10.7
+++ Russia Day in Mecklenburg-Vorpommern: Good
international relations are a guarantee for prosperity in
Europe +++ Today, Russia Day took place for the fourth
time in Mecklenburg-Vorpommern. The chairman of the AfD
parliamentary group, @706006922
German 2.57 6.53 10.6
+++Farle calls for criminal sanctions in the
Bundestag+++Criminal elements: intent, deception, and
fraud proven+++Budget debate on November 28, 2023+++
While Scholz, in his government statement, declares business
as usual in his technocratic lang
German 2.11 6.33 10.6
Federal government must temporarily use even more coal to
survive the winter despite gas shortages. The fears of the
BVB/FREIE WÄHLER parliamentary group from the spring
have come true: The federal government has been failing to
conserve natural ga
German 1.97 6.27 10.5
In response to Gov. Kevin Stitt’s call to eliminate the state
income tax, Senate President Pro Tempore Greg Treat listed a
potential GPT increase on oil and natural gas as one way to
offset the decrease in state tax revenue. Even though
Oklahoma p
English 2.05 6.22 10.2
#Opinion #Fedumop #TransportationSector #Massification
#GNV |￿ The constant change of ministers in the Transport
portfolio delays the agreements that the unions reach with
this ministry. The president of the Federation of Multimodal
Transport of Pi
Spanish 2.38 6.07 10
Join a group of oil and natural gas lovin’ Texans! English 2.19 6.07 9.9
23

Figure 2: Posterior Distributions for Item Discrimination Parameters from Greenwashing IRT
Model
burnham
carbon capture
clean coal
climate
deepseek−r1
fossil fuel
global warming
greenhouse
llama3.2:3b
mistral
natural gas
phi3
qwen2.5:7b
recycle
related_oil
renewable
sustainable
−0.5 0.0 0.5 1.0
Posterior Median
Item Name
Results of Markov Chain Monte Carlo fit
with median posterior values and 5% to
95% posterior quantiles.
positively predict political greenwashing while the presence of the term “fossil fuel” should
negatively predict political greenwashing. We do indeed see these indicators on the assigned
sides, thoughtheyarenotthestrongestfactors. Rather, thestrongestindicatorforourpolitical
greenwashing score is our binary classification from the DEBATE BERT model about an ad
being pro- or anti-policy action towards climate change.
For the LLMs, we find in Figure2 that Llama3.2 is the second strongest positive predictor of
greenwashing (the natural gas indicator is technically the second-highest but it had a strongly
positive informative prior). The other LLMs have noticeably less discriminatory power for the
greenwashing score. Most of the other important indicators are terms, such as “greenhouse”
and “global warming” having a strong relationship with non-greenwashing ads. As such, in our
measurement model we have more indicators that are primarily helpful in determining which
ads do not contain greenwashing than we do in confirming greenwashing. This likely explains
why in Figure1 we have more ads strongly classified as non-greenwashing than greenwashing.
24

Figure 3: Posterior Distributions for Item Missingness Discrimination Parameters from Green-
washing IRT Model
deepseek−r1
llama3.2:3b
mistral
qwen2.5:7b
−0.10 −0.05 0.00
Posterior Median
Item Name
Results of Markov Chain Monte Carlo fit
with median posterior values and 5% to
95% posterior quantiles.
What we also want to note is that the words “sustainable” and “recycling” are negative predic-
tors of political greenwashing. This relationship provides evidence in support of our contention
that there are fundamentally two types of greenwashing; our model is primed to capturepolit-
ical greenwashing while words like “sustainable” and “recycling” tend to be associated either
with either consumer greenwashing or content that is authentically advocating for action to
prevent climate change. There could be content in this ads that is not strictly true from the
perspective of climate science, but at the same time the discourse is not aimed at obfuscating
the climate change movement.
In addition, in Figure3 we can see the missingness discrimination parameters for the LLM
models (the other indicators do not have them as they did not have any missing data). As men-
tioned earlier, these missingness parameters are estimated in a first-stage model to endogenize
missing data. These missingness parameters show what proportion of information about the
latent trait of political greenwashing is present in the missingness patterns introduced by LLM
25

hallucination. Interestingly, while LLama3.2 is the most informative model on observed data,
Mistral’s missing data is in fact fairly informative at predicting lower greenwashing scores.
In other words, given the prompt, Mistral tended to hallucinate more when presented with
a non-greenwashing ad. The 2-stage IRT model was than able to backwards infer that when
Mistral hallucinated, the ad should have a lower score. Through this method, we can safeguard
inferences from LLM model breakdown.
Exploratory Analysis of Ad Targeting
Before we test hypotheses, we want to describe the general patterns in this large and diverse
collection of data. While not strictly related to our hypotheses, this section points to important
features of the ad targeting data that are relevant to current concerns about the nature of
climate change advertising and its links to the fossil fuel industry.
Fossil Fuel Industry Networks
An issue of significant concern is that the relatively unregulated nature of social media ad-
vertising would permit fossil fuel industry groups to run ads that are not directly connected
with their oﬀicial accounts. Our universe of social media ads provides a unique window into
this type of behavior as we can look for similarities in patterns of ad text across plausibly
unrelated groups. To do so, we employed an embedding model to classify the Facebook Pages
in terms of their ad text cosine similarity (Sanh et al. 2020). We consider any two Pages to
be connected if they have at least five ads with a greenwashing score 1 SD above the average
and a cosine similarity score of at least +0.8 (the maximum is +1). In other words, the pages
must have been running at least five very similar ads that had a reasonably high probability
of greenwashing content.
To narrow down the list to those pages that might have links to the fossil fuel industry, we
filter the resulting connected pages to only those pages that were pre-identified via external
26

qualitative information as having a known identity as a fossil fuel actor (whether corpora-
tion or interest group). This step results in a final network of 31 pages that have plausible
greenwashing-related links to 352 other pages that we did not pre-identify as fossil fuel ac-
tors. This network of connected pages is shown in Figure4 in which the identified pages of
well-known interest groups and corporations are labeled. We further colored the nodes by the
average greenwashing scores for all ads for each page. As can be seen, there is a very large and
dense network around U.S. and U.K. fossil fuel actors, particularly the American Petroleum
Institute, Chevron, and BP. There is also a distinct cluster around Petrobras, the Brazilian
state oil producer.
It is important to note that these links do not necessarily mean that there is an actual rela-
tionship or that there is any undisclosed advertising funding. Indeed, a closer inspection of the
connected nodes shows that a considerable number of the pages report their connection to the
fossil fuel actor, such as distinct ExxonMobil subsidiaries like ExxonMobil México. However,
it is also clear that these associations are not always reported whether via the Facebook Page
name or via the funding entity data reported when a political ad is run on Facebook. For
example, the American Chemistry Council, which sometimes advocates on behalf of the fossil
fuel industry,13 has greenwashing ad content similarities with Enbridge Gas, the Gas Networks
of Ireland, the Propane Education and Research Council, the Petroleum Alliance of Oklahoma,
and the Hoover Institution. While adjudicating the exact nature of these links would require
extensive qualitative investigation, the analysis does reveal notably similar patterns of climate
change discourse across seemingly disparate organizations.
In Table3, we show the 10 pre-identified Facebook pages with the biggest positive difference
in greenwashing scores with the linked page. A high positive difference indicates that the
pre-identified page’s ads have much less greenwashing content on average than the linked page.
While this statistic does not provide proof of a subversive relationship, it does indicate that
these pages have notable similarities in ads while still maintaining on the whole very different
13See https://www.motherjones.com/politics/2025/01/fossil-fuel-industry-talking-points-obstruction-climate-
action-delay-denial/.
27

average profiles. As a result, they may be able to mask discursive similarities between different
pages that would very hard for users to discern. One notable example is the second-highest
difference, which is between BHP Billiton, an Australian mining company with oil and gas
assets, and NZ Energy Voices, a New Zealand NGO that “tells the story of natural gas and its
importance to New Zealand”14 and derives its funding from the Petroleum Exploration and
Production Association of New Zealand.15 While it is not clear if BHP Billiton currently has
active oil and gas operations in New Zealand, or simply promotes similar types of ads to NZ
Energy Voices, the obvious overlap in potential interests suggests that there may indeed be
networks (whether formal or informal) that coordinate advertising on climate change-related
issues.
It is important to note too that this exercise is necessarily conservative as we limited our net-
work data to those pages with pre-identified fossil fuel associations. One page that was in the
broader list (i.e., the list of all pages with greenwashing connections to other pages) but did
not have any previous association with the fossil fuel industry is the Empowerment Alliance,
which as of late 2025 had 24,000 followers on Facebook.16 The page describes its mission as
“fighting for millions of Americans who care about keeping energy affordable, reliable, and
clean.”17 While this group’s stated purpose might make it sound like a pro-climate change
mitigation platform, investigations by The Energy & Policy Institute have revealed a 501(c)4
“dark money” organization behind the page that is “aligned with the gas industry” and has a
president who is a former lobbyist for Chesapeake Energy. In our data, the average greenwash-
ing score for Empowerment is +4.55, but it has no disclosed links to fossil fuel institutions
that we were able to identify with pre-existing sources.18
14See https://x.com/nzenergyvoices
15See https://www.energyresources.org.nz/news/giving-a-voice-to-the-people-new-campaign-launched-on-oil-
and-gas-exploration-halt/
16See https://www.facebook.com/TheEmpowermentAlliance/.
17See https://www.facebook.com/TheEmpowermentAlliance/.
18See https://energyandpolicy.org/the-empowerment-alliance-2/ for more information.
28

Table 3: Linked Facebook Pages with Greatest Difference in Average Greenwashing Scores
FossilFuelAc-
tor
Linked Page Linked Page
Funder
Greenwashing
Difference
ExxonMobil
Atlantic Gulf
Pacific Com-
pany
NA 5.2
Chevron Your Energy
American
Gas Associa-
tion
4.8
BHP Billiton NZ Energy Voices NZ Energy Voices 4.7
ExxonMobil New Mexico Oil Gas New Mexico Oil and Gas Association 4.4
ExxonMobil
Grow
Louisiana
Coalition
Grow
Louisiana
Coalition
4.2
Chevron Power In Co- operation ConocoPhillips Company 4.2
ExxonMobil Além da Su- perfície
INSTITUTO
BRASILEIRO
DE
PETROLEO
E GAS
3.7
BP BOLD PAC CHC BOLD PAC 3.6
Business
Roundtable ExxonMobil
EXXON MO-
BIL CORPO-
RATION
3.5
BP
Texas Oil and
Gas Associa-
tion
Texas Oil and
Gas Associa-
tion
3.5
Table shows Facebook pages with pre-identified fossil fuel links and linked
pages where a link equals at least five very similar greenwashing ads. The
selected pages were those with the greatest difference in greenwashing scores
between the pre-identified page and the connected page, which could imply
unacknowledged advertising.
29

Figure 4: Networks of High Greenwashing Ad Similarity in Ad Library
American Clean Power Association
American Chemistry Council (ACC)
Consumer Energy Alliance
American Petroleum Institute
Business Roundtable American Legislative Exchange Council (ALEC)
BP
BG Group
Petrobras
Petrobras
Chevron
Chevron
BHP Billiton
Chevron
Petrobras
Glencore Xstrata
Rio Tinto
Chevron
Saudi Aramco
BHP Billiton
ExxonMobil
ExxonMobil
ExxonMobil
ExxonMobil
Petrobras
BP
Chevron
ExxonMobil
ExxonMobil
Pertamina
Greenwashing
Score
 −2.5 0.0 2.5
Plot shows Facebook pages that were matched to actors with fuel industry
connections denoted with labels with the name of the actor. Each link to other
nodes represents at least five very similar high greenwashing ads that were
run by other Facebook pages. The color of the page labels and nodes is for the
average greenwashing score of the page in question.
30

Inference About Greenwashing
Hypothesis 1: Fossil Fuel Companies and Greenwashing
Wenowturntoanevaluationofthehypothesesthatweproposedatthebeginningofthearticle.
We test our hypothesis 1 by examining distributions of ads to provide a nuanced understanding
of the patterns in the data rather than relying on a single summary measure like a𝑝-value. To
do so, we report the complete distribution of the posterior mean greenwashing scores for the
different types of entities that we coded (fossil fuel companies, their subsidiaries, think tanks,
trade associations, and related interest groups) as blue distributions in Figure5. In this plot,
we show each type of fossil fuel-related entity as a separate facet with the greenwashing scores
of the rest of climate ads as a reference distribution in gray.
Figure 5: Distribution of Posterior Mean Greenwashing Scores for Ads by Entity Type
Subsidiaries Think Tank Trade Association
All Other Oil Company Other Interest Group
−10 −5 0 5 −10 −5 0 5 −10 −5 0 5
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
Ad−level Greenwashing Score
Plot shows the distribution of political greenwashing scores for each ad
associated with a page of a fossil fuel actor of a given type in blue. The
reference distribution, a sample of greenwashing scores for 10,000 ads from the
complete dataset, is shown in grey.
On the whole, do these entities have higher greenwashing scores? The answer largely depends
on the entity type. One type of entity, oil company subsidiaries, do not appear to have very
31

much greenwashing content in their ads. In general, the score distributions are also very multi-
modal, suggesting that these advertising platforms design some ads with greenwashing content
but also that they put out ads that are much less easy to classify as greenwashing. The entity
types with the highest modes at positive greenwashing scores are the “think tank” category.
Given that we derived our list of interest groups from research on entities with links to fossil
fuel companies, we find this empirical relationship to be very interesting as it is suggestive that
fossil fuel companies may be using unconventional platforms to mask greenwashing advertising
on social media. Furthermore, it is important to note that there is considerable heterogeneity
within the category of oil companies as it includes both national state-owned oil companies
like Petrobras and private oil companies like Shell and BP.
The advantage of visually examining the distributions rather than relying on summary statis-
tics is that we can examine features that a comparison of means would obscure (i.e., multi-
modal distributions). It is clear from Figure5 that while there is reason to believe that there
is greenwashing occurring among these groups that we pre-identified as having an association
with the oil industry, the most pronounced modes are seen only in the think tank category. Fur-
thermore, this behavior does not manifest itself in oil company subsidiaries, probably because
the subsidaries are engaged in lower-level retail marketing rather than political action.
On the whole, we find moderate support for H1, with the primary caveat that the relationship
appears to vary significantly across the differen types fossil fuel-related groups.
Hypothesis 2: Country-level Analysis
In order to test hypotheses 2 and 3, we employ a metric that enables fair comparisons given
different sizes in advertising markets. To that end, we use in this section impression-weighted
greenwashing scores by different geographical areas and demographic groups. In other words,
for a given group, we multiply the ad greenwashing scores times the share of impressions that
each ad had for that target market. As such, the models we employ in this section show
32

how much greenwashing content a person might have seen on Facebook and Instagram as a
proportion of all climate change-related content in the country.
To evaluate hypothesis 2, we fit linear regression models of our impression-weighted greenwash-
ingscoresasanoutcomealongwithcovariatesproposedbytheliteratureasbeingimportantfor
explaining government policy towards climate change, including Varieties of Democracy scores
(V-DEM). We include in our models the V-DEM executive constraints index and polyarchy
index, average CO2 consumption per capita and oil and gas revenues per capita. Because this
analysis is exploratory, we fit a variety of models with and without other covariates as controls
and with and without interactions, which we report in Table4.
We first note that we have countries present in our data across the full range of the V-DEM
polyarchy score with a minimum value of 0.016 (Saudi Arabia) and a maximum value of 0.916
(Denmark). As such, we have reasonable global coverage with which to test this hypothesis,
even though we acknowledge that the number of ads in non-Western countries is considerably
less than Western countries.
The results in Table4 reveal that our hypothesis 2 relating to country-level regime type is
largelyfalsified. Weseelittleevidenceofanykindofsystematicassociationbetweendemocratic
values or rule of law and greenwashing scores. We account for fuel resources and carbon output
as possible confounding variables, but we do not see any difference in reported results when
we do so, nor do we see evidence of strong interaction effects. For these reasons, we believe
that institutional explanations—at least at the country level—do not appear to be suﬀicient
to explain this type of behavior.
The main caveat is that we do find a robust relationship betweenlower CO2 consumption and
a higher ratio of greenwashing content. This is a surprising finding as we might imagine that
countries with less CO2 output would also be less important targets for greenwashing-related
advertising. However, we note that our ad database captures both ads with and without
greenwashing, and there are a substantial number of actors in countries like the United States
that are attempting to influence climate change discourse in a very different direction than
33

Table 4: Regression Models of Average Country Greenwashing Scores
Model
Results (1) (2) (3) (4) (5) (6) (7) (8)
Variables
Inter-
cept
-0.31
(0.25)
-0.57
(0.17)
-0.75
(0.25)
-0.67
(0.16)
-0.48
(0.19)
-0.7
(0.15)
-0.27
(0.19)
-0.62
(0.16)
Exec.
Con-
straints
-0.35
(0.4)
-0.46
(0.25)
- - - - -0.43
(0.26)
-0.37
(0.23)
Pol-
yarchy
- - 0.54
(0.5)
-0.36
(0.28)
-0.1 (0.3) -0.28
(0.27)
- -
CO￿ pc -0.03
(0.02)
- -0.01
(0.02)
- -0.04
(0.01)
- -0.04
(0.01)
-
Oil pc - -37.29
(40.32)
- -28.3
(39.5)
- 1.8
(10.16)
- 1.71
(10.06)
Model Fit
R² 0.11 0.02 0.11 0.01 0.09 0.01 0.11 0.02
Adj.
R²
0.08 0 0.08 -0.01 0.07 0 0.09 0
DF 107 156 107 156 108 157 108 157
F-Stat 4.35 1.22 4.31 0.62 5.16 0.61 6.55 1.33
Table shows OLS regression coeﬀicients (standard errors in parentheses) of country-level covariates
on country-level average political greenwashing scores that have been weighted as a proportion
of the total impressions for all climate-related ads within the given country. Results that are
statistically significant at the𝑝<0.05 level are denoted with an *.
fossil fuel companies. As such, when measuring impression-weighted average greenwashing
scores by country, we find a higher ratio of such content in places that perhaps we would not
expect initially.
In SI section 2 we also report average levels of impression-weighted political greenwashing
separately for countries, major cities, U.S. states, and age groups. There is substantial het-
erogeneity across regions, and we also show that targeted ads occur at higher levels for older
demographics.
34

Hypothesis 3: Sub-national Covariates and Greenwashing in the United States
Similar to hypothesis 2, we fit linear models of impression-weighted greenwashing scores for ads
targeted toward individual US counties, examining associations with covariates that explain
local attitudes toward climate change. Among our covariates is an aggregated measure of
community exposure and sensitivity to the transition away from fossil fuels, developed by
Raimi, Carley, and Konisky (2022). The authors use a number of metrics (e.g., geological,
climate, socioeconomic, educational) to develop measures identifying the communities most
likely to be affected and harmed by the transition toward clean energy sources. Specifically,
we rely on an aggregate score combining communities’ sensitivity and exposure to the energy
transition across coal, oil, and natural gas. The scores, developed for census tracts, were
then aggregated to the county-level based on a population-weighted average. We believe
these transition risk scores provide a reasonable measurement of the distribution of costs
associated with a transition to renewable energy. In addition to these scores, we include county
partisanship, measuredusingtheproportionofvoteswonbyRepublicansinthe2024electionas
a share of total Democratic and Republican votes (2018); 2023 county gross domestic product
(GDP), obtained from the Bureau of Economic Analysis; and 2024 county population.19
Because this modeling is exploratory–we do not have a clean causal identification strategy such
as randomization of greenwashing scores–we do our best to avoid well-known pitfalls of applied
regression modeling such as post-treatment bias (Montgomery, Nyhan, and Torres 2018) and
induced collider bias (Hünermund and Louw 2020) that can come from the over-use of control
variables. For these reasons, we fit models both with and without adjustment variables both
singly and jointly so that we can test for obscure causal relationships between variables in
the model. While this does not in any way prove causal identification, it can help uncover
sensitivity of our results to a specific set of adjustment variables. Regardless, the results in
this section should be interpreted as exploratory associations, albeit at a much lower level of
19The Bureau of Economic Analysis’s most recently published county gross domestic product figures in 2023.
Population data was obtained from the US Census. Using 2020 presidential vote shares or 2023 population
does not meaningfully change our results.
35

Table 5: Regression Models of US County Greenwashing Scores: Main Effects
Dependent variable:
Greenwashing Score
(1) (2) (3) (4)
Transition 0.3∗∗∗
(0.1)
Republican 0.8∗∗∗
(0.2)
GDP -0.0
(0.0)
Population -0.0
(0.000)
Constant -0.3∗∗∗ -0.7∗∗∗ -0.3∗∗∗ -0.3∗∗∗
(0.04) (0.04) (0.04) (0.04)
Observations 2,253 2,247 2,230 2,247
R2 0.01 0.01 0.000 0.000
Adjusted R2 0.000 0.000 -0.000 -0.000
Residual Std. Error 1.7 (df = 2251) 1.7 (df = 2245) 1.7 (df = 2228) 1.7 (df = 2245)
F Statistic 12.8∗∗∗ (df = 1; 2251) 30.4 ∗∗∗ (df = 1; 2245) 0.003 (df = 1; 2228) 0.02 (df = 1; 2245)
Note: ∗p<0.1; ∗∗p<0.05; ∗∗∗p<0.01
granularity than our country-level results.
Tables Table5 and Table6 summarize our results, and Figure6 shows the distribution of a
random sample of 700 counties based on their transition risk and greenwashing score. Concern-
ing our hypothesis, there is a positive association between transition risk and greenwashing
scores across all specifications. Climate-related advertisements targeted toward consumers in
counties vulnerable to the energy transition are more likely to include greenwashing, even
controlling for the county’s population, partisan composition, and GDP. Though we cannot
exclude alternative explanations, two seem more striking than others. First, fossil fuel com-
panies face strong incentives to exert local political pressure in counties facing transition risk.
As owners of local land and mineral rights, companies are subject to municipal laws and reg-
ulations, particularly if they aim to expand or upgrade existing facilities. Homeowners may
organize to block the construction of facilities near their neighborhoods, and companies may
face litigation from local residents or workers affected by their operations. Second, since resi-
36

Table 6: Regression Models of US County Greenwashing Scores: Interaction Effects
Dependent variable:
Greenwashing Score
(1) (2) (3)
Transition 0.335∗∗∗ 0.674∗∗∗ 0.658∗∗∗
(0.070) (0.166) (0.169)
GDP -−0.000
(0.000)
Republican −3.819∗∗∗ −3.671∗∗∗ −3.969∗∗∗
(0.719) (0.721) (0.728)
Republican2 4.844∗∗∗ 4.920∗∗∗ 5.255∗∗∗
(0.719) (0.719) (0.729)
GDP2 0.000
(0.000)
Population −0.0000
(0.00000)
Population2 −0.000
(0.000)
Transition:Republican −0.683∗∗ −0.656∗∗
(0.304) (0.307)
Constant −5.078 −5.069
(0.160) (0.167) (0.168)
Observations 2,247 2,247 2,218
R2 0.041 0.043 0.044
Adjusted R2 0.040 0.042 0.043
Residual Std. Error 1.630 (df = 2243) 1.628 (df = 2242) 1.630 (df = 2209)
F Statistic 32.033∗∗∗ (df = 3; 2243) 25.333 ∗∗∗ (df = 4; 2242) 13.380 ∗∗∗ (df = 8; 2209)
Note: ∗p<0.1; ∗∗p<0.05; ∗∗∗p<0.01
37

dents in counties vulnerable to transition risk hold concentrated interests in fossil fuel activity,
companies may target them to “shore up’’ a base of voters to oppose climate legislation.
Figure 6: Association Between Transition Risk and Greenwashing Score
Figure 7 illustrates changes in the marginal effect of transition risk at different levels of par-
tisanship. An increase in transition risks is associated with sharper increases in greenwashing
scores in counties where smaller shares of voters supported Trump. Due to their economic
interests, voters in these counties may be more prone to oppose climate legislation than those
in other Democratic counties. Equivalently, compared to other voters in counties vulnerable
to transition risk, these voters may be more susceptible to Democratic messages supporting
climate legislation. From either perspective, there are strong incentives for emitting companies
to persuade these voters that their products and practices are less harmful than they appear.
38

Figure 7: Marginal Effect Plot between Transition Risk and 2024 Republican Vote Share
39

Conclusion
In this paper we are able to show using granular data how fossil fuel companies are targeting
people directly in areas in which they may fear adverse regulatory decisions. Contrary to
our initial expectations, we find these ads to be micro-targeted at places where oil companies
have fixed assets. We do not find much evidence for the idea that greenwashing may be more
prominent in more democratic countries, although we do find evidence that greenwashing is
more common among older demographic groups who tend to vote at higher rates. We believe
that our measurement approach can unlock further insights into political greenwashing as well
as provide a signal detection method for quickly and accurately classifying ads as potentially
containing greenwashing.
40

References
Abdin, Marah, JyotiAneja, HanyAwadalla, AhmedAwadallah, AmmarAhmadAwan, Nguyen
Bach, Amit Bahree, et al. 2025. “Phi-3 Technical Report: A Highly Capable Language
Model Locally on Your Phone.”https://doi.org/10.48550/arXiv.2404.14219.
Amin, Marian H, Heba Ali, and Ehab KA Mohamed. 2024. “Corporate Social Responsibility
Disclosure on Twitter: Signalling or Greenwashing? Evidence from the UK.”International
Journal of Finance & Economics 29 (2): 17451761.
Anderson, Austin, and Behnaz Rezaie. 2019. “Geothermal Technology: Trends and Potential
Role in a Sustainable Future.”Applied Energy 248 (August): 18–34. https://doi.org/10.1
016/j.apenergy.2019.04.102.
Angwin, Julia, and Terry Parris, Jr. 2016. “Facebook Lets Advertisers Exclude Users by Race.”
ProPublica, October. https://www.propublica.org/article/facebook-lets-advertisers-
exclude-users-by-race.
ASIC. 2024. “ASIC Wins First Greenwashing Civil Penalty Action Against Vanguard,” March.
https://asic.gov.au/about-asic/news-centre/find-a-media-release/2024-releases/24-
061mr-asic-wins-first-greenwashing-civil-penalty-action-against-vanguard/ .
Bafumi, Joseph, Andrew Gelman, David K Park, and Noah Kaplan. 2005. “Practical Issues
in Implementing and Understanding Bayesian Ideal Point Estimation.”Political Analysis
13 (2): 171187.
Barrie, Christopher, Alexis Palmer, and Arthur Spirling. 2024. “Replication for Lan-
guage Models Problems, Principles, and Best Practice for Political Science.” URL:
Https://Arthurspirling. Org/Documents/BarriePalmerSpirling TrustMeBro. Pdf .
http://arthurspirling.org/documents/BarriePalmerSpirling_TrustMeBro.pdf.
Baumgartner, Frank R, Jeffrey M Berry, Marie Hojnacki, Beth L Leech, and David C Kimball.
2009. Lobbying and Policy Change: Who Wins, Who Loses, and Why . University of
Chicago Press.
Bergman, Noam. 2018. “Impacts of the Fossil Fuel Divestment Movement: Effects on Finance,
Policy and Public Discourse.”Sustainability 10 (7): 2529.https://doi.org/10.3390/su1007
41

2529.
Blackman, Allen. 2012. “Does Eco-Certification Boost Regulatory Compliance in Developing
Countries? ISO 14001 in Mexico.”Journal of Regulatory Economics 42: 242263.
Blazkova, Tereza, Esben Rahbek Gjerdrum Pedersen, Kirsti Reitan Andersen, and Francesco
Rosati. 2023. “Greenwashing Debates on Twitter: Stakeholders and Critical Topics.”
Journal of Cleaner Production 427: 139260.
Board of Governors of the Federal Reserve System. 2023. “Changes in u.s. Family Finances-
from 2019 to 2022.”
———. 2025. “Distribution of Household Wealth in the u.s. Since 1989.”
Bouchaud, Paul. 2024. “On Meta’s Political Ad Policy Enforcement: An Analysis of Coordi-
nated Campaigns & Pro-Russian Propaganda.”
Bryan, Kenza. 2023. “UK Bans Vague ‘Sustainability’ Fund Labels in Greenwashing Crack-
down.” The Financial Times , November.
Burnham, Michael. 2023. “Semantic Scaling: Bayesian Ideal Point Estimates with Large
Language Models.” Archiv. https://doi.org/10.48550/arXiv.2405.02472.
———. 2025. “Stance Detection: A Practical Guide to Classifying Political Beliefs in Text.”
Political Science Research and Methods 13 (3): 611–28.https://doi.org/10.1017/psrm.202
4.35.
Carroll, Robert J., David M. Primo, and Brian K. Richter. 2016. “Using Item Response
Theory to Improve Measurement in Strategic Management Research: An Application to
Corporate Social Responsibility.” Strategic Management Journal 37 (1): 66–85. https:
//doi.org/10.1002/smj.2463.
Clinton, Joshua, Simon Jackman, and Douglas Rivers. 2004. “The Statistical Analysis of
Rollcall Data.” American Political Science Review 98 (2): 355–70.
Data, MIT Election, and Science Lab. 2018. “County Presidential Election Returns 2000-
2024.” Harvard Dataverse.https://doi.org/10.7910/DVN/VOQCHQ.
Dobber, Tom, Ronan Ó Fathaigh, and Frederik J. Zuiderveen Borgesius. 2019. “The Reg-
ulation of Online Political Micro-Targeting in Europe.” Internet Policy Review 8 (4).
https://doi.org/10.14763/2019.4.1440.
42

Du, Xingqiang, Wei Jian, Quan Zeng, and Yingjie Du. 2014. “Corporate Environmental
Responsibility in Polluting Industries: Does Religion Matter?”Journal of Business Ethics
124: 485507.
Dubova, Marina, Arseny Moskvichev, and Kevin Zollman. 2024. “Against Theory-Motivated
Experimentation in Science,” February.https://doi.org/10.31222/osf.io/ysv2u.
Dür, Andreas. 2019. “How Interest Groups Influence Public Opinion: Arguments Matter
More Than the Sources.”European Journal of Political Research 58 (2): 514535.
Dür, Andreas, and Gemma Mateo. 2016.Insiders Versus Outsiders: Interest Group Politics
in Multilevel Europe. Oxford University Press.
European Commission. 2024. “Commission and National Consumer Protection Authorities
Starts Action Against 20 Airlines for Misleading Greenwashing Practices,” April.https:
//ec.europa.eu/commission/presscorner/detail/en/ip_24_2322.
Francis, David C., and Robert Kubinec. 2025. “Beyond Political Connections: A Measurement
Model Approach to Estimating Firm-Level Political Influence in 41 Countries.”Political
Science Research and Methods. https://doi.org/doi.org/10.1017/psrm.2025.10046.
Green, Breanna, William Hobbs, Sofia Avila, Pedro L. Rodriguez, Arthur Spirling, and Bran-
don M. Stewart. 2025. “Measuring Distances in High Dimensional Spaces: Why Average
Group Vector Comparisons Exhibit Bias, And What to Do about It.”Political Analysis 33
(3): 266–73. https://doi.org/10.1017/pan.2024.22.
Guo, Daya, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu,
et al. 2025. “DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement
Learning.” https://doi.org/10.48550/arXiv.2501.12948.
Hackenburg, Kobi, and Helen Margetts. 2024. “Evaluatingthe PersuasiveInfluence of Political
Microtargeting with Large Language Models.” Proceedings of the National Academy of
Sciences 121 (24): e2403116121.https://doi.org/10.1073/pnas.2403116121.
Hanson, Jonathan K., and Rachel Sigman. 2021. “Leviathan’s Latent Dimensions: Measuring
State Capacity for Comparative Political Research.”The Journal of Politics 83 (4): 1495–
1510. https://doi.org/10.1086/715066.
Heede, Richard. 2013. “Carbon Majors: Accounting for Carbon and Methane Emissions
43

1854-2010 Methods & Results Report.” Snowmass, CO.
———. 2014. “Tracing Anthropogenic CO_2 and Methane Emissions to Fossil Fuel and
Cement Producers 1854–2010.” Climatic Change 122 (1): 229241. https://doi.org/http:
//dx.doi.org/10.1007/s10584-013-0986-y.
Heede, Richard, and Naomi Oreskes. 2016. “Potential Emissions of CO2 and Methane from
Proved Reserves of Fossil Fuels: An Alternative Analysis.”Global Environmental Change
36: 1220.
Hünermund, Paul, and Beyers Louw. 2020. “On the Nuisance of Control Variables in Regres-
sion Analysis.” Arxiv. https://doi.org/10.48550/arXiv.2005.10314.
Ingram, Robert W, and Katherine Beal Frazier. 1980. “Environmental Performance and
Corporate Disclosure.” Journal of Accounting Research, 614622.
Isaac, Mike, and Tiffany Hsu. 2021. “Meta Plans to Remove Thousands of Sensitive Ad-
Targeting Categories.”The New York Times , November.
Jiang, Albert Q., Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh
Chaplot, Diego de las Casas, Florian Bressand, et al. 2023. “Mistral 7B.”Archiv. https:
//doi.org/10.48550/arXiv.2310.06825.
Kakenmaster, William. 2024. “The Fossil-Fueled Roots of Climate Inaction in Authoritarian
Regimes.” Perspectives on Politics, August, 1–19.https://doi.org/10.1017/S15375927240
00793.
Kollman, Ken. 1998. Outside Lobbying: Public Opinion and Interest Group Strategies . Prince-
ton University Press.
Kreiss, Daniel. 2017. “Micro-Targeting, the Quantified Persuasion.”Internet Policy Review 6
(4). https://policyreview.info/articles/analysis/micro-targeting-quantified-persuasion.
Kubinec, Robert. 2025. “Generalized Ideal Point Models for Noisy Dynamic Measures in the
Social Sciences.” Open Science Foundation Preprints . https://doi.org/10.31219/osf.io/8j
2bt.
Kwon, Kyeongwon, Jaejin Lee, Cen Wang, and Vaibhav Shwetangbhai Diwanji. 2024. “From
Green Advertising to Greenwashing: Content Analysis of Global Corporations’ Green Ad-
vertising on Social Media.”International Journal of Advertising 43 (1): 97124.
44

Levin, Sam. 2017. “{M}ark {z}uckerberg: I Regret Ridiculing Fears over {f}acebook’s Effect
on Election.” The Guardian, September. https://www.theguardian.com/technology/201
7/sep/27/mark-zuckerberg-facebook-2016-election-fake-news .
Lucas, Adam. 2021. “Investigating Networks of Corporate Influence on Government Decision-
Making: The Case of Australia’s Climate Change and Energy Policies.”Energy Research
& Social Science 81 (November): 102271.https://doi.org/10.1016/j.erss.2021.102271.
Lyon, Thomas P, and A Wren Montgomery. 2015. “The Means and End of Greenwash.”
Organization & Environment 28 (2): 223249.
Macdonald, Maggie, Anna Gunderson, and Kirsten Widner. 2024. “Exploring Interest Group
Social Media Activity on Facebook and Twitter.” Journal of Quantitative Description:
Digital Media 4 (May).https://doi.org/10.51685/jqd.2024.014.
Mahoney, Lois S, Linda Thorne, Lianna Cecil, and William LaGore. 2013. “A Research
Note on Standalone Corporate Social Responsibility Reports: Signaling or Greenwashing?”
Critical Perspectives on Accounting 24 (4-5): 350359.
Malhotra, Neil, Benoît Monin, and Michael Tomz. 2019. “Does Private Regulation Preempt
Public Regulation?” American Political Science Review 113 (1): 1937.
Manning, Benjamin S, Kehang Zhu, and John J Horton. 2024. “Automated Social Science: A
Structural Causal Model-Based Approach.”Working Paper. https://benjaminmanning.io
/files/nature_draft_rs.pdf.
Marshall, MelanieBenson, StephenPinfield, PamelaAbbott, AndrewCox, JuanPabloAlperin,
Germana Barata, Natascha Chtena, et al. 2024. “The Impact of COVID-19 on the Debate
on Open Science: An Analysis of Expert Opinion,” January.https://doi.org/10.31235/osf
.io/xy874.
McKnight, David, and Mitchell Hobbs. 2013. “Public Contest Through the Popular Me-
dia: The Mining Industry’s Advertising War Against the Australian Labor Government.”
Australian Journal of Political Science 48 (3): 307319.
Megura, Matthew, and Ryan Gunderson. 2022. “Better Poison Is the Cure? Critically Ex-
amining Fossil Fuel Companies, Climate Change Framing, and Corporate Sustainability
Reports.” Energy Research & Social Science 85 (March): 102388. https://doi.org/10.101
45

6/j.erss.2021.102388.
Meta Business Help Center. 2025. “About Ads about Social Issues, Elections or Politics.”
https://www.facebook.com/business/help/167836590566506?id=288762101909005.
Meta Platforms, Inc. 2024. “Meta Ad Targeting Dataset.”https://doi.org/10.48680/meta.ad
targetingdataset.
Mildenberger, Matto. 2020. Carbon Captured: How Business and Labor Control Climate
Politics. MiT Press. https://books.google.com/books?hl=en&lr=&id=0LDMDwAAQB
AJ&oi=fnd&pg=PR5&dq=Carbon+Captured:+How+Business+and+Labor+Control+
Climate+Politics.&ots=DyAtwR070S&sig=0XYcZJ33K0XqBDmwA1PZPHER378.
Montgomery, Jacob M., Brendan Nyhan, and Michelle Torres. 2018. “How Conditioning on
Posttreatment Variables Can Ruin Your Experiment and What to Do about It.”American
Journal of Political Science 62 (3): 760–75.https://doi.org/10.1111/ajps.12357.
Mulvey, K., S. Shulman, Dave Anderson, N. Cole, Jayne Piepenburg, and Jean Sideris. 2015.
“The Climate Deception Dossiers: Internal Fossil Fuel Industry Memos Reveal Decades of
Corporate Disinformation.” In. https://www.semanticscholar.org/paper/The-climate-
deception-dossiers%3A-internal-fossil-of-Mulvey-Shulman/edfe683fb9afbb5588408701680f
292ac3df015e.
Nachmany, Michal, and Joana Setzer. 2018. “Global Trends in Climate Change Legislation
and Litigation: 2018 Snapshot.”Grantham Research Institute on Climate Change and the
Environment, May. https://www.lse.ac.uk/granthaminstitute/wp-content/uploads/2018
/04/Global-trends-in-climate-change-legislation-and-litigation-2018-snapshot-3.pdf .
Nasiritousi, Naghmeh. 2017. “Fossil Fuel Emitters and Climate Change: Unpacking the
Governance Activities of Large Oil and Gas Companies.”Environmental Politics 26 (4):
621–47. https://doi.org/10.1080/09644016.2017.1320832.
Oreskes, Naomi, and Erik M Conway. 2011.Merchants of Doubt: How a Handful of Scien-
tists Obscured the Truth on Issues from Tobacco Smoke to Global Warming . Bloomsbury
Publishing USA.
Park, Jong Hee. 2011. “Modeling Preference Changes via a Hidden Markov Item Response
Theory Model.” Handbook of Markov Chain Monte Carlo , 479491. https://www.research
46

gate.net/profile/Jong-Hee-Park-2/publication/237534789_Modeling_Preference_Chan
ges_via_a_Hidden_Markov_Item_Response_Theory_Model/links/56384e1808ae4bd
e50212f5f/Modeling-Preference-Changes-via-a-Hidden-Markov-Item-Response-Theory-
Model.pdf.
Peattie, Ken. 2010. “Green Consumption: Behavior and Norms.”Annual Review of Environ-
ment and Resources 35 (1): 195228.
Pemstein, Daniel, Stephen A. Meserve, and James Melton. 2017. “Democratic Compromise:
A Latent Variable Analysis of Ten Measures of Regime Type.”Political Analysis 18 (4):
426–49. https://doi.org/10.1093/pan/mpq020.
Pew Research Center. 2023. “Voter Turnout, 2018-2022.”
Plec, Emily, and Mary Pettenger. 2012. “Greenwashing Consumption: The Didactic Framing
of ExxonMobil’s Energy Solutions.”Environmental Communication: A Journal of Nature
and Culture 6 (4): 459476.
Potoski, Matthew, and Aseem Prakash. 2004. “The Regulation Dilemma: Cooperation and
Conflict in Environmental Governance.”Public Administration Review 64 (2): 152163.
———. 2005. “Green Clubs and Voluntary Governance: ISO 14001 and Firms’ Regulatory
Compliance.” American Journal of Political Science 49 (2): 235248.
———. 2011. “Voluntary Programs, Compliance and the Regulation Dilemma.”Handbook on
the Politics of Regulation , 8495.
Raimi, Daniel, Sanya Carley, and David Konisky. 2022. “Mapping County-Level Vulnerability
to the Energy Transition in US Fossil Fuel Communities.”Scientific Reports 12 (1): 15748.
Ring, Suzi, and Madeleine Speed. 2023. “{UK} Regulator Investigates {u}nilever over ‘Green’
Claims on Products.”The Financial Times , December.
Rodriguez, PedroL., ArthurSpirling, andBrandonM.Stewart. 2023. “EmbeddingRegression:
Models for Context-Specific Description and Inference.”American Political Science Review
117 (4): 1255–74.https://doi.org/10.1017/S0003055422001228.
Sanh, Victor, Lysandre Debut, Julien Chaumond, and Thomas Wolf. 2020. “DistilBERT, a
Distilled Version of BERT: Smaller, Faster, Cheaper and Lighter.”Archiv. https://doi.or
g/10.48550/arXiv.1910.01108.
47

Shukla, Satwik. 2019. “A Better Way to Learn about Ads on {f}acebook.” Meta, March.
https://about.fb.com/news/2019/03/a-better-way-to-learn-about-ads/ .
Sirieix, Lucie, Marion Delanchy, Hervé Remaud, Lydia Zepeda, and Patricia Gurviez. 2013.
“Consumers’ Perceptions of Individual and Combined Sustainable Food Labels: A UK Pilot
Investigation.” International Journal of Consumer Studies 37 (2): 143151.
Slater, Dan. 2008. “Can Leviathan Be Democratic? Competitive Elections, Robust Mass Pol-
itics and State Infrastructural Power.”Studies in Comparative International Development
43: 252–72.
Solon, Olivia. 2016. “2016: The Year Facebook Became the Bad Guy.” The Guardian ,
December. https://www.theguardian.com/technology/2016/dec/12/facebook-2016-
problems-fake-news-censorship.
Speed, Madeleine. 2024. “Asos, Boohoo and George Pledge Clarity on Green Credentials
After {CMA} Probe.”The Financial Times , March.
Stokes, Leah Cardamore. 2020. Short Circuiting Policy: Interest Groups and the Battle over
Clean Energy and Climate Policy in the American States . Oxford University Press, USA.
https://books.google.com/books?hl=en&lr=&id=uLTRDwAAQBAJ&oi=fnd&pg=PP
1&ots=UTnETelT4T&sig=50xEKeTKZTW9doBr5veQoCPmvvk.
Supran, Geoffrey, and Naomi Oreskes. 2017. “Assessing ExxonMobil’s Climate Change Com-
munications (1977–2014).” Environmental Research Letters 12 (8): 084019.
Tamimi, Nabil, and Rose Sebastianelli. 2017. “Transparency Among s&p 500 Companies: An
Analysis of ESG Disclosure Scores.”Management Decision 55 (8): 16601680.
Tang, Samuel, and David Demeritt. 2018. “Climate Change and Mandatory Carbon Report-
ing: Impacts on Business Process and Performance.”Business Strategy and the Environ-
ment 27 (4): 437455.
Team, Gemma, Morgane Riviere, Shreya Pathak, Pier Giuseppe Sessa, Cassidy Hardin, Surya
Bhupatiraju, Léonard Hussenot, et al. 2024. “Gemma 2: Improving Open Language
Models at a Practical Size.”https://doi.org/10.48550/arXiv.2408.00118.
Tienhaara, Kyla. 2018. “Regulatory Chill in a Warming World: The Threat to Climate
Policy Posed by Investor-State Dispute Settlement.”Transnational Environmental Law 7
48

(2): 229–50. https://doi.org/10.1017/S2047102517000309.
Tonmoy, S. M. Towhidul Islam, S. M. Mehedi Zaman, Vinija Jain, Anku Rani, Vipula Rawte,
Aman Chadha, and Amitava Das. 2024. “A Comprehensive Survey of Hallucination Miti-
gation Techniques in Large Language Models.”Archiv. https://doi.org/10.48550/arXiv.2
401.01313.
Touvron, Hugo, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Tim-
othée Lacroix, Baptiste Rozière, et al. 2023. “LLaMA: Open and Eﬀicient Foundation
Language Models.”https://doi.org/10.48550/arXiv.2302.13971.
Truman, David B. 1951.The Governmental Process: Political Interests and Public Opinion .
Knopf.
Uyar, Ali, Abdullah S Karaman, and Merve Kilic. 2020. “Is Corporate Social Responsibility
Reporting a Tool of Signaling or Greenwashing? Evidence from the Worldwide Logistics
Sector.” Journal of Cleaner Production 253: 119997.
Weber, Maximilian, and Merle Reichardt. 2024. “Evaluation Is All You Need. Prompting
Generative Large Language Models for Annotation Tasks in the Social Sciences. A Primer
Using Open Models.”https://doi.org/10.48550/arXiv.2401.00284.
Wiseman, Joanne. 1982. “An Evaluation of Environmental Disclosures Made in Corporate
Annual Reports.” Accounting, Organizations and Society 7 (1): 5363.
Yang, An, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li,
et al. 2025. “Qwen2.5 Technical Report.”https://doi.org/10.48550/arXiv.2412.15115.
Yu, Ellen Pei-Yi, Christine Qian Guo, and Bac Van Luu. 2018. “Environmental, Social and
Governance Transparency and Firm Value.”Business Strategy and the Environment 27 (7):
9871004.
Yu, Ellen Pei-Yi, Bac Van Luu, and Catherine Huirong Chen. 2020. “Greenwashing in En-
vironmental, Social and Governance Disclosures.”Research in International Business and
Finance 52: 101192.
49
