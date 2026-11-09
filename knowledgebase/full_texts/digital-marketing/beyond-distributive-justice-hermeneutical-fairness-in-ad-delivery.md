---
title: 'Beyond Distributive Justice: Hermeneutical Fairness in Ad Delivery'
url: https://arxiv.org/abs/2605.03419
category: digital-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Camilla Quaresmini
- Valentina Breschi
- Jessica Leoni
- Viola Schiaffonati
- Mara Tanelli
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.03419
pages: 24
chars: 105317
fetched_at: '2026-11-08T12:59:54+00:00'
kb_version: 1
---

# Beyond Distributive Justice: Hermeneutical Fairness in Ad Delivery

BEYONDDISTRIBUTIVEJUSTICE: HERMENEUTICALFAIRNESS
INADDELIVERY
Camilla Quaresmini
Politecnico di Milano
Milan, Italy
camilla.quaresmini@polimi.it
Valentina Breschi
Eindhoven University of Technology
Eindhoven, The Netherlands
v.breschi@tue.nl
Jessica Leoni
Politecnico di Milano
Milan, Italy
jessica.leoni@polimi.it
Viola Schiaffonati
Politecnico di Milano
Milan, Italy
viola.schiaffonati@polimi.it
Mara Tanelli
Politecnico di Milano
Milan, Italy
mara.tanelli@polimi.it
Giulia De Pasquale
Eindhoven University of Technology
Eindhoven, The Netherlands
g.de.pasquale@tue.nl
ABSTRACT
Fairness in online advertising is often formalized as a distributive justice problem, aiming to ensure
that impressions, opportunities, or outcomes are allocated comparably across protected groups.
However, even when fairness is ensured according to classical statistical notions, online advertising
can still produce systematic harms arising from the ads’ content and the way recipients interpret
and uptake them. To capture this dimension, we draw on Miranda Fricker’s notion ofhermeneutical
injustice. Building on this philosophical account, we model online ad delivery as a mechanism
that distributes interpretative resources and can fail in two ways. First, relevant concepts can
be withheld through systematic under-exposure, leading tohermeneutical deprivation. Second,
recipients may experiencehermeneutical distortionswhen they are saturated with low uptake or
skewed framings. According to these findings, after grounding these mechanisms in exploratory
correlational patterns from theAIDS Advertising Evaluationsurveys (1986-1987), we introduce a
group-level hermeneutical fairness constraint and a hermeneutically-aware utility cost in the design
of an optimal ad distribution strategy to account for interpretative uptake. We then integrate them
into a benchmark, versatile, utility-driven ad allocation framework that already enforces distributive
justice, yielding a distributively fair, hermeneutically aware ad allocation framework that prevents the
concentration of deprivation and distortion within any protected group. Using controlled simulations,
we explore the trade-offs between economic utility, classical distributive fairness constraints (statistical
parity and equality of opportunity), and hermeneutical cost and constraints. The results show that
a purely utility-based viewpoint drives systematic under-delivery to the disadvantaged group of
recipients. Meanwhile, when the hermeneutical stakes of withholding ads are high, distributive
constraints can reduce hermeneutical cost at modest utility loss. Conversely, placing a large weight
on hermeneutical cost in the absence of distributive constraints can yield ad delivery policies that
are highly concentrated on the disadvantaged recipient group. Together, these findings motivate
expanding fairness analyses of online advertising beyond classical distributive notions to account for
epistemic conditions of interpretation and uptake.
KeywordsTargeted Advertising, Epistemic Harms, Hermeneutical Injustice, Algorithmic Fairness, Distributive Justice
1 Introduction
Algorithmic personalization shapes how people access knowledge and are exposed to online advertising [Bozdag(2013),
Cotter and Reisdorf(2020), Sweeney(2013)]. Indeed, search engines, recommender systems, and ad platforms tailor
results and sponsored content to inferred preferences [Noble(2018), Pariser(2011), Kant(2020)], thereby influencing not
only what people consume but also what they are able to know [Cotter and Reisdorf(2020), Harris(2022), Shin(2025)].
arXiv:2605.03419v1  [cs.CY]  5 May 2026

Quaresmini et al.
Since pattern-based personalization is central to modern informational infrastructures, questions about fairness
in access to—and the quality of—information in ad delivery are increasingly pressing [ Deldjoo et al.(2022),
Chien and Danks(2023), Goodman(2014)].
Empirical work already documents discriminatory patterns across ad domains, including job postings
[Imana et al.(2021), Stauffer(2018)], insurance [Fabris et al.(2021)], healthcare [Schenker et al.(2014)], political cam-
paigns [Bär et al.(2024)], and societal discourse [ Ali et al.(2021)]. This evidence has motivated a view on fairness
that largely emphasizes distributive concerns, thus prompting its operationalization through quantitative criteria on
how benefits, opportunities, or resources (concretely impressions, bids, or outcomes) are allocated across protected
groups [ Baumann et al.(2024), Datta et al.(2018), Watts(2021), Speicher et al.(2018), Lambrecht and Tucker(2019),
Navon et al.(2023), Chowdhary et al.(2024)]. While this exposure-focused framing is natural in a setting where deliv-
ery is explicitly conditioned on user features, limiting or constraining targeting options does not fully mitigate dis-
criminatory effects [Baumann et al.(2024), Ali et al.(2019), Imana et al.(2021), Sapiezynski et al.(2024)]. In particular,
[Soares et al.(2019), Muñoz et al.(2024), Phillips et al.(2023), Celis et al.(2019a), Bozdag and Van Den Hoven(2015),
Ribeiro et al.(2018), Cagle(2023), Guo et al.(2022), Tang et al.(2022), Ross Arguedas et al.(2022)] show that feature-
based targeting and personalization can generate informational asymmetries and contribute to opinion clustering, as
users are steered into increasingly segmented information environments. However, even when distributional fair-
ness holds, advertising can still disadvantage groups due to its conceptual content and the interpretative frames
it embeds. Indeed, since algorithmic systems mediate the diffusion and validation of knowledge, they shape
classificatory boundaries that structure how the world is interpreted [ Alvarado(2023), Symons and Alvarado(2022),
Mollema(2025), Hyzen et al.(2025)]. This aspect is significant as it proves that currently employed approaches to
ensuring fair advertising across domains, from healthcare to employment, remain susceptible to conceptual availability
and distortion, which, in turn, can influence how individuals interpret their circumstances and perceived opportuni-
ties [Gaucher et al.(2011), Mintzes(2002), Applequist and Ball(2018), Ventola(2011), Vakratsas and Ambler(1999)].
These considerations emphasize the importance to explicitly account for anepistemicperspective - understood
broadly as the conditions, limits, and opportunities for knowing - along with distributive accounts in online
ads to capture the full social stakes of algorithmic systems, as argued by a growing body of work (see, e.g.,
[Hoffmann(2019), Selbst et al.(2019), Shelby et al.(2023), Wegner et al.(2024), Grgi´c-Hlaˇca et al.(2018)]).
To theoretically ground our intuition, we draw on Miranda Fricker’s framework which distinguishes testimonial from
hermeneutical injustice [Fricker(2007)].1 These are two forms of epistemic injustice: the former concerns credibility
deficits driven by prejudice, while the latter concerns gaps in shared interpretative resources that make experiences
difficult to understand In this work we focus on interpretative resources and treat hermeneutical injustice - wrongful
gaps in shared interpretative resources that make some experiences unintelligible - as a specific form of the broader
category of epistemic injustice. More precisely, we treat epistemic harm as the broader category of wrongs done to
subjects in their capacity as knowers. Such harm takes a specifically hermeneutical form when ad delivery shapes
access to the interpretative resources needed to render socially significant experiences intelligible. Accordingly, we
read targeted advertising not only as a problem of ad allocation, but also as a problem of distributing a specific type of
epistemic resources, in particular interpretative resources. Therefore, in this work, we identify two mechanisms through
which targeted ads can generateepistemic harms:systematic under-exposureandsystematic over-exposure. 2 These can
in turn give rise tohermeneutical harms: the former tohermeneutical deprivations, as relevant concepts are withheld
from particular audiences, and the latter tohermeneutical distortionsthrough repeated exposure to simplified or skewed
framings. We show that these mechanisms are consistent with exploratory patterns found in our analysis of theAIDS
Advertising Evaluationsurveys 3 (1986-1987). We wish to stress that, although our exploratory empirical illustration
relies on a healthcare advertising dataset, the framework we develop is not specific to healthcare. We use the AIDS
case as a concrete baseline for motivating and operationalizing a more general account of hermeneutical fairness in ad
delivery. This empirical analysis motivates our development of a novel quantitative operationalization of hermeneutical
fairness4 in terms of costs and constraints that, combined with utility-driven losses and more classical distributive
justice constraints (i.e., enforcing statistical parity and equality of opportunity), can be used to design distributionally
and hermeneutically fair ad delivery policies. We do so by extending the fair utility-maximizing allocation strategy
proposed in [Baumann et al.(2024)] with our proposed hermeneutical cost and constraints, exploring the trade-offs
between economic utility, distributive fairness, and hermeneutical fairness via numerical simulations. In the following,
we usehermeneutically-awareandhermeneutically fairto mark two distinct notions. Hermeneutically-aware denotes
1This work analyzes how identity power shapes what is intelligible and socially recognized.
2Here,epistemic harmsare wrongs done to subjects in their capacityas knowers.
3https://discovery.nationalarchives.gov.uk/details/r/C11521962
4We usejusticein its philosophical sense to denote the relevant normative wrongs in epistemic relations. Our contribution,
however, is framed in terms offairnessas an evaluative property of the distributive process governing an allocation. On our usage,
fairness concerns whether the allocation rule yields just outcomes, wherejusticeis assessed at the level of the resulting distributions
rather than as a complete account of the underlying wrong.
2

Beyond Distributive Justice: Hermeneutical Fairness in Ad Delivery
designs that explicitly model and respond to hermeneutical considerations, whereas hermeneutically fair denotes the
stronger condition of satisfying a formal hermeneutical fairness criterion.
The paper is structured as follows. The overall framework of our work is developed in Section 2, situating our
contribution within the literature on fairness in advertising and motivating why a purely distributive, exposure-based
view is incomplete for capturing epistemic harms. Section 3 presents exploratory empirical evidence consistent
with epistemic harms in theAIDS Advertising Evaluationsurveys. In Section 4, we introduce our formalization of
hermeneutical harms and fairness, that we use in Section 5 to present a utility-maximizing allocation strategy under
hermeneutical and classical distributive constraints. Section 6 presents a set of numerical results aimed at underpinning
how group-structured asymmetries interact with standard fairness constraints. Section 7 discusses these findings,
clarifies the scope of our work and poses awareness on its limitations. Finally, Section 8 concludes with implications
for auditing and platform design and highlights future research directions.
2 From Distributive to Hermeneutical Fairness
Most works on fairness in advertising revolve around distributive concerns. Hence, they tend to primarily fo-
cus on how ad delivery, exposure, or outcomes are allocated across protected groups, treating fairness solely
as a property of group-level exposure or outcome distributions. This choice is indeed supported by sev-
eral empirical studies (see, e.g., [ Datta et al.(2018), Sweeney(2013), Lambrecht and Tucker(2019), Ali et al.(2019),
Imana et al.(2024)]), which show that targeting and auction dynamics can cause systematic disparities in ac-
cess to opportunities, including (but not limited to) employment, housing, credit, and education. Corre-
spondingly, audit studies generally compare the delivery of specific ad types across user groups or profiles
[Imana et al.(2021), Speicher et al.(2018), Kingsley et al.(2020), Asplund et al.(2020)]. Meanwhile, mitigation strate-
gies typically impose group-conditioned constraints on reach/impressions [Speicher et al.(2018), Baumann et al.(2024),
Schoeffer et al.(2023), Singh and Joachims(2018), Timmaraju et al.(2023), Li et al.(2025), Molina et al.(2023)], mod-
ify auction or pacing mechanisms [ Celis et al.(2019b), Dalenberg(2018), Lee et al.(2013), Yuan et al.(2013),
Yuan et al.(2025)], or target parity in downstream outcomes [Watts(2021), Ali et al.(2023), Peysakhovich et al.(2023)].
However, not all harms in advertising boil down to who sees an ad. Indeed, even with equalized exposure, advertising
content can encode normative frames that shape in different ways the identities and options that appear legitimate to dif-
ferent groups of recipients [Eisend(2010), Antoniou and Akrivos(2020), Sierra et al.(2012), Rößner and Eisend(2023),
Davis(2018), Rona(2023)]. For instance, Sony’s Dutch billboard for the white PlayStation Portable - which paired the
tagline "White is coming” with racialized imagery - was criticized as racist and withdrawn from the market5. Likewise,
the V olkswagen e-Golf advert banned by the UK Advertising Standards Authority6 relied on gendered role juxtaposition
that reinforced stereotypes about who belongs in technical domains.
These cases highlight that a core harm in advertising lies in the creative’s normative framing rather than in un-
equal delivery, and that exposure parity can coexist with systematic differences in the informational quality of what
audiences receive. This fact motivates an epistemic perspective that conceptualizesad delivery not only as the
allocation of attention, but also as the allocation of interpretative resources- the shared concepts and meaning-
making tools whose gaps and distortions are central to hermeneutical injustice. This perspective is complemen-
tary to recent work on representational harms in algorithmic systems, which examines how models and outputs
can depict, classify, or rank groups in harmful ways, for example through stereotyping or underrepresentation
[Katzman et al.(2023), Wang et al.(2025), Kong(2026), Lalor et al.(2024)]. While representational harm frameworks
focus on harmful portrayals or classifications, our focus is on how ad delivery systems may differentially distribute the
interpretative resources needed to make experiences intelligible. In this sense, representational harms can arise even
when the relevant concepts are already available, whereas the hermeneutical injustice lens highlights cases in which a
system helps sustain or reproduce interpretative gaps.
2.1 An Epistemic Perspective on Online Advertising
Digital platforms intensify segmentation beyond pre-digital media choice and geography by enabling fine-grained profil-
ing and rapid content optimization [Wind(1978), Williamson(1978), Oswald and Oswald(2012), Coeckelbergh(2022),
Coeckelbergh(2025)]. However, in online advertising, feature-driven targeting and personalization do not only lead to
reallocation of attention, but also reallocation of interpretative resources embedded in ad content [McCracken(1986),
Pollay(2014)]. As a consequence, they can produce opinion clustering and epistemic polarization, saturating some
5See, e.g., https://www.campaignlive.co.uk/article/sony-withdraws-potentially-racist-dutch-billboards/
569738
6https://www.theguardian.com/media/2019/aug/14/first-ads-banned-for-contravening-gender-stereotyping-rules
3

Quaresmini et al.
audiences with narrow frames while excluding others [ Ribeiro et al.(2018), Phillips et al.(2023), Cinus et al.(2022),
Hartmann et al.(2025)]. In addition, personalization can isolate similarly situated individuals, weakening the condi-
tions for collective recognition of structural harms [ Milano and Prunkl(2025)]. Meanwhile, platform optimization
- which inherently tends to privilege majority behavior and engagement-friendly content - can amplify dominant
narratives and suppress contested voices [ Stewart et al.(2022), Coeckelbergh(2022)], shaping which interpretations
become socially salient and authoritative. As a consequence, even if relevant categories and framings may circu-
late, targeting and delivery can make them selectively visible - or systematically skewed - for particular audiences
[Lambrecht and Tucker(2019), Imana et al.(2025), Andreou et al.(2018), Skurka and Keating(2024)]. These pervasive
harms in ad delivery can be seen as forms ofhermeneutical injustice, because they systematically shape who has
access to the concepts and framings needed to interpret experiences, thereby reproducing group-structured gaps in
interpretative resources. They yield amisdistribution 7 [Coady(2017)] of concepts and, hence, epistemic resources
across specific respondent groups.
Despite these recognized harms, hermeneutical injustice remain comparatively under-operationalized in algorithmic
fairness [Coliva(2025), Hopster(2024), Milano and Prunkl(2025), Pozzi(2023), Stewart et al.(2022)]. Dominant ap-
proaches instead emphasize distributive criteria such as parity in exposure or outcomes, highlighting the need not only
to include these forms of injustice into debates on fairness in online ad delivery, but also to explicitly account for them
within targeting and delivery operations themselves.
3 Hermeneutical Harms: Formalization and Experimental Evidence
The theoretical framework for ad delivery outlined in Section 2 highlights a limitation of the fair ad-distribution
literature, which largely focuses on exposure and outcomes but does not explicitly account for epistemic wrongs in
ad delivery. In particular, targeted advertising can wrong subjects in their capacity as knowers by shaping what they
can learn, recognize, and make sense of through patterned delivery and framing. The core idea from Fricker is that
hermeneutical injustice arises when people lack adequate shared interpretative resources (such as concepts, labels, or
frames) for making sense of significant aspects of their experience [Fricker(2007)]. The harm is not merely unequal
access to information, but a disadvantage in making one’s own experience intelligible because the social circulation of
interpretative resources is incomplete or distorted. To make this explicit, we distinguish two forms of epistemic harm:
•Epistemic exclusion: Concepts are withheld from particular audiences through systematic under-exposure.
•Epistemic bombing: Systematic over-exposure to narrow or sensational framings saturates attention.
We then interpret these epistemic harms through the lens ofhermeneutical injustice. Our proposed framework frames
hermeneutical injustice as a collective interpretative gap [Dotson(2011), Dotson(2012), Medina(2013)], that is, a gap
between shared interpretative resources and what is needed to make own experiences intelligible. Building on this , we
treat ad delivery as a mechanism that allocates interpretative resources. Here, repeated or skewed exposure may affect
how recipients process and evaluate informational content over time [Hassan and Barber(2021), Li and Yang(2025)],
yielding two hermeneutical manifestations of the above harms:
• Hermeneutical deprivation: Relevant informational content fails to reach particular audiences, undermining
their ability to interpret an experience. This can be exemplified by Alzheimer’s prevention campaigns, whose
ads often target an older audience [Perez-Heydrich et al.(2024), Heger et al.(2020)]. However, based on this
allocation and content choice, younger users - including those potentially affected by early-onset Alzheimer’s -
may receive limited exposure and fail to connect symptoms to available care pathways [Loi et al.(2022)].
• Hermeneutical distortion: Repeated delivery of narrow or sensational framings can saturate or sim-
plify concepts, misleading interpretation. This phenomenon is visible in short-form mental health
advertising. For example, ADHD-oriented ads often present broad, engagement-optimized symptom
checklists [Karasavva et al.(2025)], repeated exposure to which can encourage overgeneralization or self-
misclassification [de Vries et al.(2025), Schiros et al.(2025)].
We distinguish delivery-level mechanisms from their interpretative effects. Therefore, in our framework,epistemic
exclusionrefers to identity-structured under-exposure to interpretative resources in ad delivery, whereasepistemic
bombingrefers to repeated or saturating exposure to narrow or sensational framings.Hermeneutical deprivation
andhermeneutical distortionrefer to the corresponding harms that may arise when these patterns affect recipients’
capacity for sense-making. We also distinguishepistemic exclusionfrominformational injustice[ Bagwala(2024)].
7Going beyond the conceptualization in [Fricker(2007), Fricker(2017)], which frames hermeneutical injustice as arising from
structural deficits in collective interpretative responses.
4

Beyond Distributive Justice: Hermeneutical Fairness in Ad Delivery
Not Exposed Exposed0.0
0.2
0.4
0.6
0.8
1.0P (Exposure | Sexuality)
0.15
0.40
0.85
0.60
Homosexual Heterosexual
(a) Exposure distributionsP(Exposure|Sexuality).
 (b) Behavior-change distributions P(Behavior change|
Exposure).
Figure 1:Asymmetric reach and non-monotonic behavior change in HIV prevention advertising.(a) Asymmetric
reach in HIV prevention advertising. Heterosexual respondents report a lower probability of high exposure and a higher
probability of low exposure than homosexual respondents. (b) Distribution of self-reported behavioral change after
the campaign, stratified by exposure group (Not exposed vs Exposed; exposure categories defined in Appendix A).
Values report conditional proportions P(Behavior change|Exposure). In our data, higher exposure is not associated with
a monotonic increase in substantial behavioral change: exposed respondents more often report moderate or no change
than substantial change.
Informational injustice concerns cases in which an informational asymmetry is used to disadvantage less-informed
agents. Epistemic exclusion, by contrast, concerns the resulting exclusion from participation in knowledge practices. It
becomes hermeneutically relevant when the withheld content matters for sense-making.
3.1 Evidence of Hermeneutical Harms from Data: Analysis of AIDS Advertising
We conduct an exploratory analysis of theAIDS Advertising Evaluationsurveys (1986-1987) 8 to demonstrate the harms
that the epistemic mechanisms introduced above may produce, and to ground the subsequent formalization of our
proposed approach. We consider a non-algorithmic advertising dataset as our baseline before extending the analysis
to algorithmic settings in simulation (Section 6). To this end, we retain only surveys with consistent coverage of the
variables used in our analysis, as detailed in Appendix A. We use the offline survey data as a methodological baseline to
show that the proposed hermeneutical mechanisms can arise outside platform-mediated online delivery. This means
that we do not intend to treat this dataset as a direct proxy for online advertising, but rather as an empirical baseline for
studying the epistemic mechanisms of interest. Although platform-mediated delivery builds on familiar advertising
logics [Goldfarb(2014)], online systems differ in important ways, including scale, optimization dynamics, targeting
granularity, repeated exposure, and attention capture. These differences may affect the magnitude and form of the harms
we study. In the absence of a comparable online advertising dataset containing the measures required for our analysis,
we use this dataset as an illustrative offline baseline to isolate the epistemic mechanisms.
Analyzing the available data, we observe two descriptive patterns that motivate our modeling of interpretative resource
failures.9 First, as shown in Figure 1a, exposure to ads is asymmetric. The results for heterosexuals report a
systematically lower reach than for homosexuals, suggesting a clear targeting strategy in the advertising campaign and
highlighting a potential unequal access to prevention-relevant concepts. Second, as shown in Figure 1b, self-reported
behavioral change does not increase monotonically with exposure. When responses are stratified by exposure group,
higher exposure is not associated with a larger share of substantial behavioral change. Instead, exposed respondents
more often report moderate or no change than substantial change. We interpret this pattern as correlational evidence
consistent with saturation-like dynamics, rather than as evidence of a monotonic increase in uptake with exposure.
From the analyzed dataset, we also observe descriptive patterns consistent with the possibility ofepistemic bombing
and relatedhermeneutical distortion, while remaining agnostic about the underlying causal mechanism. As shown
8To the best of our knowledge, nobody has used theAIDS Advertising Evaluationsurveys for analyses of this kind.
9We do not treat the variables below as direct measurements of harm, but as illustrative indicators of harm-relevant patterns. In
our reading, systematic under-exposure to relevant interpretative resources is consistent with deprivation, whereas exposure patterns
that coincide with weak uptake or with responses suggestive of sensationalized or framing-sensitive reception are consistent with
the possibility of distortion. A less harmful pattern would instead involve more even access to relevant exposure and stronger, less
uneven uptake under exposure.
5

Quaresmini et al.
Yes No
Worried about AIDS
I agree strongly
I tend to agree
I tend to disagree
I disagree stronglySensationalism
230 280
107 179
133 185
136 66
Sensationalism vs WorriedAboutAIDS
75
100
125
150
175
200
225
250
275
Count
(a) Sensationalism perceptions and worry about AIDS.
 (b) SensationalismP(Sensationalism|Exposure).
0 20 40 60 80 100
Percentage
High Awareness
No Awareness
No Answer
27.1%
72.2%
0.7%
Heterosexual Respondents
0 20 40 60 80 100
Percentage
36.3%
63.3%
0.4%
Homosexual Respondents
How at risk are People who need blood transfusions from catching AIDS?
0 20 40 60 80 100
Percentage
High Awareness
No Awareness
No Answer
24.0%
74.5%
1.5%
Heterosexual Respondents
0 20 40 60 80 100
Percentage
27.9%
70.7%
1.4%
Homosexual Respondents
How at risk are haemophiliacs from catching AIDS?
(c) Framing-sensitive awareness of transfusion-related HIV risk.
Figure 2:Exploratory correlational evidence for deprivation and distortion mechanisms.(a) Perceived sensational-
ism vs. worry about AIDS (joint distribution). Count-annotated heatmap of the joint distribution between responses to
the sensationalism item and self-reported worry about AIDS (Yes/No). The sensationalism item is: “How much do you
personally agree with this statement?: The newspapers have been too sensational in their reporting of AIDS” (V154).
Rows report responses (excluding Don’t know): I disagree strongly, I tend to disagree, I tend to agree, I agree strongly.
(b) Sensationalism responses by exposure group. Conditional response distribution P(Sensationalism|Exposure) shown
across categories (I disagree strongly, I tend to disagree, I tend to agree, I agree strongly) for Not exposed vs Exposed
respondents. (c) Transfusion-risk awareness variables exhibit framing sensitivity and lower self-reported awareness
among heterosexual respondents.
in Figure 2a, stronger agreement with the statement that media coverage was “too sensational” is associated with
lower self-reported worry about AIDS. In Figure 2b, the distribution of responses to the sensationalism item differs
across exposure groups, with exposed respondents being relatively more likely to fall in the agreement categories than
non-exposed respondents. Taken together, these patterns are consistent with the possibility that repeated or affectively
skewed messaging may coincide with reduced perceived risk or weaker uptake of prevention messages. At the same
time, these data are correlational and admit alternative explanations, including the possibility that respondents who were
already less worried about AIDS were also more likely to perceive public discourse and advertising about AIDS as
sensationalized. We wish to remark that our aim is not to establish a causal mechanism, but to show that delivery-uptake
mismatches of the kind motivating hermeneutical concerns are visible in empirical data.
The results of our analysis further indicate that interpretative resources are sensitive to framing, not only to exposure.
Indeed, as shown in Figure 2c for transfusion-related HIV risks, the subgroup-specific formulation (“people who
need blood transfusions” versus “hemophiliacs”) yields response distributions that are comparable across groups of
respondents. Both heterosexual and homosexual respondents are indeed more likely to report “no awareness” and less
likely to report “high awareness”, a pattern consistent withepistemic exclusioninduced not by exposure alone but by
content framing. In turn, this indicates a potential group-freehermeneutical deprivation, that is, reduced uptake of a
prevention-relevant concept that can impede recognition and articulation of a risk. Appendix A reports confidence
intervals and basic association tests for the main descriptive patterns discussed.
Taken together, these associations provide exploratory evidence consistent with the two ways in which advertising can
fail as a carrier of collective interpretative resources introduced at the beginning of this section. Consequently, we draw
on these empirically observed patterns as qualitative guidance to develop our formulation of hermeneutical injustice in
ad delivery, which we then implement in the simulation study in Section 6. Therefore, we treat these empirical patterns
6

Beyond Distributive Justice: Hermeneutical Fairness in Ad Delivery
as qualitative, harm-relevant indicators that motivate the formalization developed in the remainder of the paper, rather
than as definitive measurements of hermeneutical harm.
4 Modeling Hermeneutical Fairness in Ad Delivery
So far, we have argued that fairness in advertising has both distributive and hermeneutical dimensions, but the latter has
not yet been formalized in the literature. In this section, we thus make this formalization step, building on the empirical
evidence from Section 3 and the utility-based framework from [Baumann et al.(2024)]. To this end, we focus on the
(simplified) case in which the online ad platform makes a binary display decision dx ∈ {0,1}for each user x on a focal
ad. We further assume that the potential recipients of the ad form a finite set of users G, that can be partitioned into
two protected groups Ga and Gb according to one or more features that influence the utility gained by the platform if
they are targeted and their ability to understand or benefit from the ads content. If the platform decides not to expose
the user x to the ad (dx = 0), user x can then be subject tohermeneutical deprivation. This circumstance exacerbates
selective underexposurewhen individuals from a specific group are systematically excluded from receiving the ad. Such
a selective advertising campaign can, at the same time, lead toepistemic bombingamong the targeted user groups (as
evidenced in Section 3), due tosystematic overexposure.
These issues can nonetheless be mitigated on the platform by designing ad delivery policies constrained toparity of
exposure, defined next.
Definition 4.1(Parity of exposure).Let Na and Nb be the sizes of the two protected groups Ga and Gb. We say the ad
allocation decision{d x}x∈G guarantees parity of exposure if the following holds
1
Na
X
x∈Ga
dx = 1 Nb X x∈Gb dx,(1)
namely, if the average of ad receivers is equal for both groups.
Note that this definition is nothing but the sample approximation for statistical parity of exposure (see the definition in
[Corbett-Davies et al.(2017)]). Hence, hermeneutical underexposure and overexposure can be alleviated by enforcing
classical distributive fairness constraints in ad-delivery policy design, thereby reinforcing our vision of hermeneutical
fairness as an (interpretative) resource allocation problem. At the same time, underexposure and overexposure are not
the only issues when looking at ad delivery from an epistemic perspective. Indeed, even if users receive an ad, they
might still not make sense of it. Therefore, to achieve hermeneutical fairness, an ad platform must not only guarantee
that both groups are reached by the advertisement but also ensure that different user groups can equally make sense of
the ad content, according to the criteria formalized next.
Definition 4.2(Equality of hermeneutical opportunity).Let Ga and Gb be two protected groups. Then, the ad allocation
decision{d x}x∈G guarantees equality of hermeneutical opportunity if the following holds
P
x∈Ga dxρx P
x∈Ga ρx
=
P
x∈Gb dxρx P
x∈Gb ρx
,(2)
withρ x ∈[0,1]being the probability that userxunderstands the focal ad 10.
Note that, similarly to the definition employed in [Baumann et al.(2024)], each side of (2) corresponds to the share of
users belonging to a specific user group seeing the focal ad among all those that would be able to make sense of it.
Remark 1.Based on our definition, equality of hermeneutical opportunity depends not only on the ad platform’s
delivery strategy, but also on the ad content. Hence, guaranteeing equality of hermeneutical opportunity implies
redesigning ad campaigns that ultimately count as a cost for the platform.
We can thus formally characterize a hermeneutically fair ad delivery strategy as follows:
Definition 4.3(Hermeneutically fair ad delivery).Consider two protected groups Ga and Gb. We say that the ad
allocation decision {dx}x∈G ishermeneutically fairif it guarantees parity of exposure as in (1) and equality of
hermeneutical opportunity according to(2).
As already mentioned, allocating resources, both distributive and interpretative, has a cost. This motivates the adoption
of a cost-sensitive perspective on hermeneutical fairness, which we will use in Section 5 to inform the design of our
hermeneutically-aware ad delivery strategy. Similarly to [Baumann et al.(2024)], we can thus define a hermeneutic cost
10Withρ x ≈1indicating that userxhas successfully made sense of the ad’s content.
7

Quaresmini et al.
that depends on whether user x receives the ad and uptake (i.e., makes sense of) the ad’s content. Let ρx ∈[0,1] be the
probability that user x makes sense of the focal ad, where θ >0 denotes the reward for successful uptake, ω >0 the
penalty for failed uptake, and ξ >0 the exclusion penalty for withholding the ad and its interpretative resources. We
then define thehermeneutical injustice costassociated to userxas
HI(dx) = [−θρx +ω(1−ρ x)]dx +ξ(1−d x).(3)
Hence, if the user does not receive the advertisement (dx = 0), the cost reduces to the fixed exclusion penalty ξ. If
instead the user receives the ad (dx = 1), hermeneutical injustice decreases with ρx at rate θ and increases with failed
uptake, weighted byω.
Intuitively, according to (3), the ad can either increase utility, framed as U(d x)−HI(d x), (when uptake succeeds) or
decrease it (when uptake fails). When the ad is withheld, by contrast, the user has no opportunity to benefit from its
interpretative content, which we represent as a fixed exclusion costξ.
Remark 2.Similarly to the assumptions made in [ Baumann et al.(2024)], we suppose that the probabilities ρx (or
an estimate thereof) are available to the ad platform for all x∈G . In practice, ρx is a latent variable that would
likely not be directly observable. In modern advertising systems, it would more plausibly be inferred from richer
platform-side signals, such as historical interaction patterns, repeated engagement, post-click behavior, and learned
user/content representations. The controlled protocol outlined in Section 7 provides one possible strategy for validating
or calibrating whether such platform-side proxies meaningfully track interpretative uptake.
Remark 3.In empirical applications, the epistemic parameters θ, ω, and ξ could be estimated by measuring exper-
imentally induced variation in exposure and framing, leading to controlled changes in recognition, articulation, or
downstream actions attributable to withholding versus showing the ad. To do so, one would require data from controlled
ad delivery experiments, whose collection and analysis we leave for future work.
5 Optimal Ad Delivery Strategy Under Hermeneutical Lens
Relying on the previous definition of hermeneutical fairness and cost, we now extend the fairness-constrained utility
maximization problem introduced in [Baumann et al.(2024)] to explicitly account for epistemic harms.
To this end, let the platform’s economic utility for a userxbe
u(dx) =αpxdx +β(1−d x),
where px ∈[0,1] is the platform’s estimate of the probability that user x takes the advertiser’s desired action (e.g.,
clicks), α is the utility/revenue gained conditional on that action (e.g., the advertiser’s bid), and β is the utility when the
high-stakes ad is not shown (e.g., the expected utility of the best alternative ad or showing no ad). Accordingly, let us
define the expected utility over the overall set of usersGas
U(d) =
X
x∈G
u(dx),
whered={d x}x∈G.
To account for the economic impact of epistemic harms exemplified by(3), we assume that a rational decision maker
seeks ford={d x}x∈G that maximizes the hermeneutically-aware utility
UH(d) := U(d)−γHI(d),(4)
with
HI(d) =
X
x∈G
{[−θρx +ω(1−ρ x)]dx +ξ(1−d x)},
hence seeking for a trade-off between economic and epistemic expected utilities governed by the decision maker via the
tunable trade-off parameterγ≥0.
Following [Baumann et al.(2024)], we further assume that any acceptable allocation d must satisfy baseline distributive
and, eventually, hermeneutical fairness constraints. From a distributive fairness perspective, we focus on the classical
group fairness criteria of statistical parity and equality of opportunity [Corbett-Davies et al.(2017)]. The first choice
ultimately allows us to already contrast under- and over-exposure11. Throughout the second, we impose
P
x∈Ga dxpx P
x∈Ga px
=
P
x∈Gb dxpx P
x∈Gb px
,(5)
11See the connection between statistical parity and parity of exposure highlighted in Section 4.
8

Beyond Distributive Justice: Hermeneutical Fairness in Ad Delivery
Parameters
Scenarioα β a βb θa θb ωa ωb ξ
A0.2 0.03var.0.05 0.1 0.01 0.01 0.2
B0.2 0.03 0.05 0.05var.0.01 0.01 0.2
C0.2 0.03 0.05 0.05 0.1 0.01var.0.2
D0.2 0.03 0.05 0.05 0.1 0.01 0.01var.
Table 1: Numerical simulations: explored scenariosvsfixed and varying (var.) utility and epistemic parameters.
where px ∈[0,1] is the probability of user x clicking on the focal ad. In addition, we enforce (2) as a hermeneu-
tical constraint, hence promoting user groups to equally make sense of the focal ad when received, leading to the
hermeneutically-aware ad optimization problemas
max
d
UH(d)
s.t. (1),(2),(5).
(6)
Accordingly, we can define the optimal allocation ruled ⋆(γ)as
d⋆(γ) = arg max
d
UH(d)
s.t. (1),(2),(5),
(7)
and the hermeneutically fair allocation rule as follows.
Definition 5.1(Hermeneutically Fair Allocation Rule).The hermeneutically fair allocation rule is the mapping that
returnsd ⋆(γ)in(7)whenγ >0.
Therefore, in the absence of hermeneutically aware components in (6), a platform may allocate low-uptake impressions
unevenly across groups. This is not the case in our formulation, where hermeneutical constraints and loss terms
regulate the distribution of hermeneutical mechanisms, namely content deprivation and distortion, rather than merely
the distribution of impressions.
Unconstrained closed-form solutionSince the objective is additive over x, in the absence of any distributive and/or
hermeneutical constraints, the maximization of UH(d) in (4) admits an explicit point-wise optimal solution. The
associated optimizer is determined by showing the focal ad (dx = 1) if and only if
[u(dx)−γHI(d x)]dx ≥[u(d x)−γHI(d x)](1−d x),(8)
i.e., if the hermeneutically-aware utility is maximized if userxreceives the utility. Equivalently, (8) corresponds to
αpx +γθρ x −γω(1−ρ x)≥β−γ ξ,
leading to the threshold that can be operationalized by the platform, namely
px ≥ β−γξ+γω(1−ρ x)−γθρ x α .
This last rule highlights the resulting decision logic at the individual level in the absence of constraints. For fixed γ,
the platform should prefer showing the focal ad to users with a higher uptake probability ρx. Given the combinatorial
complexity of the active constraints given the parameters, no analogous closed-form characterization is provided for the
constrained cases. Once fairness constraints are imposed, we solve the resulting optimization problem numerically for
each parameter configuration in Section 6.
6 Trade-offs Between Utility, Distributive Constraints and Hermeneutical Costs: A
Simulation Study
Through numerical simulations, we now analyze how variations in the trade-off weighting γ, as well as the utility and
epistemic parameters in (4) change the allocation policy and, hence, the resulting trade-offs between utility, classical
fairness constraints, and hermeneutical harms. In doing so, we always assume α= 0.2, hence implying that the gain
for receiving the focal ad is the same regardless of which user group they belong to. Meanwhile, we study the trade-off
by dividing users into two groups, a and b, fixing θa = 0.05and βa = 0.03, while letting the remaining user-specific
utility and epistemic parameters vary as reported in Table 1.
9

Quaresmini et al.
0.0 0.3 0.6 0.9
βb [-]
98.5
99.0
99.5
100.0
Utility in [%] of unconstrained utility
Scenario A
0.0 0.3 0.6 0.9
θb [-]
99.6
99.8
100.0
Scenario B
0.0 0.3 0.6 0.9
ωb [-]
99.6
99.8
100.0
Scenario C
0.0 0.3 0.6 0.9
ξ [-]
99.6
99.8
100.0
Scenario D
0.0 0.3 0.6 0.9
βb [-]
−0.05
0.00
0.05
0.10
Diﬀerence in parity of exposure [-]
0.0 0.3 0.6 0.9
θb [-]
0.00
0.01
0.02
0.03
0.04
0.0 0.3 0.6 0.9
ωb [-]
0.00
0.01
0.02
0.03
0.04
0.0 0.3 0.6 0.9
ξ [-]
0.00
0.01
0.02
0.03
0.04
Constraint
Unconstrained
Parity of Exposure
Equality of Opportunity
Equality of Hermeneutical Opportunity
Figure 3:Simulation results for Scenarios A–D (Table 1)imposing different fairness constraints. Top row: achieved
utility (in % of the unconstrained solution). Bottom row: parity of exposure difference. Solid lines show the median
outcomes across the 100 replications, while the shaded bands show their range according to the 0.25-0.75 quartiles.
Across simulations, we compare five allocation rules:unconstrained, where the platform only aims at maximizing
the hermeneutical-aware utility UH(d); underparity of exposure, i.e., when hermeneutical-aware utility is maximized
subject to (1); underequality of opportunity, i.e., when hermeneutical-aware utility is maximized subject to (5); with
equality of hermeneutical opportunity, so that hermeneutical-aware utility is maximized under (2). In all scenarios, γ in
(4) is set to 0.01. In each simulation run, we sample group-specific uptake probabilities ρx from Beta distributions.
Concretely, we use ρa ∼Beta(4,6) and ρb ∼Beta(7,3) . This yields mean uptake probabilities of 0.4 and 0.7,
respectively, thus modeling group b as having higher expected uptake than group a. We also consider three additional
uptake configurations: an a-advantaged setting, with ρa ∼Beta(8,2) and ρb ∼Beta(3,7) ; a balanced high-uptake
setting, with ρa =ρ b ∼Beta(7,3) ; and a balanced lower-uptake setting, with ρa =ρ b ∼Beta(4,6) . The main text
reports results for the b-advantaged case only. The corresponding results for the other uptake configurations are reported
in Appendix B.1. We further model p via a power-law distribution with fixed coefficients ka = 0.05and kb = 0.05. For
each scenario and each value of the varying parameters, we run 100 replications, resampling ρx and p in each of them.
Given this setting, the simulated scenarios are the following:
• A. Competitive spillover:( βb varies, βa is fixed). This scenario models economic asymmetries in the
opportunity cost of showing the focal ad. By varying the utility of the alternative ad for group b (βb) while
keeping βa fixed, we simulate a market where one group is more expensive to target. This allows us to examine
how the platform’s allocation reacts to purely economic pressure.
• B. Competitive uptake:( θb varies, θa is fixed). In this case, we investigate how the model handles asymmetric
benefits of understanding. By varying the reward for successful uptake θb, we represent cases where the
interpretative resource provided by the ad is more vital for one group than the other. The setup explores the
tension between maximizing group-specific hermeneutical benefits and satisfying equality of opportunity
constraints.
• C. Competitive hermeneutical loss:( ωb varies, ωa is fixed). This scenario isolates the risks associated with
hermeneutical distortion. By varying the penalty ωb for failed uptake in group b, we simulate high-stakes
environments where epistemic bombing is particularly harmful to a specific subgroup. We use this to test how
the platform balances the risk of epistemic harms against the requirement for parity of exposure.
• D. Hermeneutical spillover:(the exclusion cost ξ varies). This parameter represents the cost of being
systematically blind to the interpretative resources contained in the ad. This setup allows us to observe how
the platform’s preference for broad reach evolves as the cost of withholding information increases.
7 Discussion
We discuss the results shown in Figure 3 and the limitations of our work.
10

Beyond Distributive Justice: Hermeneutical Fairness in Ad Delivery
7.1 The Price of Hermeneutical Fairness
As shown in Figure 3, imposing any of the considered fairness constraints reduces the platform’s hermeneutically-aware
utility, U H(d), compared to the purely economic cost (baseline), U(d). In particular, equality of opportunity induces
the largest utility loss across all scenarios, while parity of exposure and equality of hermeneutical opportunity remain
closer to the unconstrained utility. The magnitude of the price of hermeneutical fairness is modest. Indeed, even in the
scenario with the largest drop in utility (A at low βb), enforcing equality of opportunity reduces utility by at most a
couple of percentage points. Meanwhile, the other two constraints lead overall to slightly smaller losses. Focusing
on Scenario A, all constrained solutions move closer to the unconstrained optimum as βb increases. Meanwhile, in
Scenarios B-D, utility under all constraints decreases slightly as the respective parameter increases, but the losses
remain below a few percentage points, and the relative ordering of the constraints remains stable.
7.2 Economic Pressure and Hermeneutical Deprivation
The lower panels of Figure 3 highlight the distributional effects across the explored scenarios. Focusing on the
unconstrained policy, the difference in parity of exposure is consistently positive (see the gray-circled curve in the
bottom row of all panels), exceeding 10% in some scenarios (most notably Scenario A). This result implies that, by
using the unconstrained delivery policy, the platform systematically under-delivers ads to the disadvantaged group.
By contrast, imposing either of the three classical fairness constraints reduces these disparities to values close to zero
(see the three curves in the bottom row corresponding to constrained scenarios in Figure 3), thereby preventing the
disadvantaged group from being structurally sidelined in ad delivery. From the platform’s perspective, however, such
corrections are not costless. Even though the efficiency losses we observe are numerically modest (on the order of
0.1–2% relative to the unconstrained utility), they arise because the (hermeneutically-aware) platform is no longer free
to choose an economic utility-maximizing policy. This claim is supported by the results in shown in the top row of
Figure 3, where curves corresponding to constrained scenarios consistently lie below the unconstrained benchmark. This
fact creates economic pressure to ignore hermeneutical stakes. Importantly, the unconstrained policy still optimizes the
hermeneutically-aware utility objective but does not impose a distributive constraint. In the bottom row of Figure 3, the
unconstrained solution exhibits a positive parity of exposure difference that becomes large under economic asymmetries
(Scenario A, as βb increases) and remains positive under group-b specific penalties for failed uptake (Scenario C, as
ωb varies). Our simulations thus illustrate a form of hermeneutical deprivation that is endogenous to the ad-delivery
objective: without explicit distributive constraints, the optimizer may still withhold interpretatively valuable ads from
the group for which delivery becomes comparatively less attractive under the modeled asymmetries. In particular, when
we model group-b specific penalties for failed uptake via ωb, the unconstrained policy maintains a positive exposure gap
in Scenario C (bottom-row gray curve in Figure 3), indicating that the group facing higher modeled harm from failed
uptake is also the group from which exposure is withheld.
7.3 Hermeneutical Fairness Beyond Parity of Exposure
Taken together, our results refine existing understandings of fairness-utility trade-offs in online ad delivery by shifting
attention from exposure alone to its hermeneutical consequences. Our simulations suggest that once hermeneutical
considerations are made explicit in the objective, the additional price of enforcing group-level fairness remains limited.
Indeed, across Scenarios A-D, the constrained policies achieve roughly 98-100% of the unconstrained utility, with the
largest observed gap being about 2% in Scenario A. At the same time, the same constraints substantially reduce the
concentration of exposure disparities: the unconstrained solution exhibits a consistently positive parity of exposure
difference across scenarios (gray curve in the bottom row plots of Figure 3), reaching above 0.1 in Scenario A,
whereas the constrained variants remain near 0 throughout. Within this setting, the classical fairness constraints we
considered (i.e., statistical parity and equality of opportunity) thus play a dual role. On the one hand, they secure a
more even distribution of impressions, as shown by the fact that the difference in parity of opportunity in all constrained
cases is close to 0 (see the plots in the bottom panel of Figure 3). At the same time, they help mitigate the systematic
withholding of interpretative resources by preventing the large exposure gaps that arise under the unconstrained objective
when asymmetries make delivery to one group less attractive (e.g., as shown in the unconstrained case in Figure 3
for Scenario A as βb increases). Meanwhile, our framework also highlights a crucial limitation of exposure-based
fairness criteria. By construction, these constraints only regulate who sees a given ad, not how that ad interacts with
existing hermeneutical asymmetries. Accordingly, policies that equalize exposure can still differ in their hermeneutical
implications. This result is confirmed by comparing the red and blue-starred lines in Figure 3, which highlight that
imposing parity of exposure and equality of hermeneutical opportunity yield different utility levels, even though both
produce similarly small parity-of-exposure differences. In principle, a policy can satisfy parity of exposure while still
producing hermeneutical deprivation (for instance, by withholding key concepts from all groups) or hermeneutical
distortion (for instance, by disproportionately saturating one group with low-uptake or skewed framings). This suggests
11

Quaresmini et al.
that future fairness audits of ad-delivery systems should incorporate measures of interpretative opportunity and risk,
rather than treating exposure parity as a sufficient proxy for fairness.
7.4 Limitations
The main limitation of our framework concerns empirical validation. Our exploratory analysis relies on an offline
advertising dataset that serves as a baseline rather than as a direct proxy for online ad delivery. This allows us to
illustrate the epistemic mechanisms of interest, but it does not capture central features of online advertising such as
large-scale optimization, fine-grained targeting, repeated delivery over time, and persistent competition for attention.
These features may affect both the magnitude and the form of the hermeneutical harms we identify. The empirical
results should therefore be read as illustrative. A second limitation concerns parameter identification. In our model,
the epistemic parameters are specified a priori rather than identified from data. In particular, the historical survey data
used in our exploratory analysis do not contain a direct measure of uptake probability ρx. The available variables
capture exposure, beliefs, awareness, perceived knowledge, confusion, and some downstream behavioral proxies. These
features do not allow to isolate uptake itself from its downstream consequences.
A concrete path toward empirical validation is a controlled ad-delivery study designed to estimate individual-level
uptake probability ρx. Participants would be assigned to attribute-myopic delivery conditions that vary exposure
intensity and framing, and would then complete a post-exposure uptake evaluation combining content understanding,
scenario-based application, and a teach-back or paraphrase task [ Baseman et al.(2013), Talevski et al.(2020)]. The
resulting responses could be aggregated into an individual uptake score yielding an estimate ˆρx. Appendix C reports the
corresponding flowchart and provides additional details. More broadly, an auditing workflow would require estimating
and validating ˆρx, calibrating epistemic parameters, evaluating group-level exposure and hermeneutical opportunity
constraints where protected-group information is available, and stress-testing robustness to proxy misspecification
and estimation error. A further failure mode concerns over-personalized interpretability. Optimizing for predicted
uptake may improve average comprehension while reducing plural interpretability or worsening outcomes for specific
subgroups.
7.5 Ethical Considerations
We are aware that our framework might raise ethical concerns. At the same time, the level of analysis we develop in this
paper remains primarily conceptual, rather than directly deployable in real-world ad systems. In the empirical analysis,
the protected-group variable is a coarse proxy based on reported recent partner history, not a measure of sexual identity.
Any grouping induced from these variables may misclassify respondents, collapse distinct experiences, and reproduce
stigmatizing categories. These risks are further amplified by substantial missingness and uneven survey coverage.
The framework should likewise not be read as licensing intrusive profiling in real-world ad systems. While access
to protected attributes and per-user uptake estimates is analytically useful for formalization and auditing, inferring
such quantities in practice may create privacy risks, stigmatizing segmentation, and manipulative optimization. In
particular, optimizing on predicted uptake may privilege commercially effective but overly narrow interpretative
framings. For this reason, any empirical implementation of the framework would require strict data minimization, strong
governance constraints on sensitive attributes, validation of uptake proxies, and auditing for failure modes including
misclassification, proxy misspecification, over-personalized interpretability, and reduced plural interpretability.
8 Conclusions and Future Work
Fairness in advertising is often cast as a purely distributive problem: ensuring that impressions or outcomes are
comparable across protected groups. While this perspective has yielded important insights, our analysis indicates that
it leaves out a crucial epistemic dimension. Building on Fricker’s notion of hermeneutical injustice, we treat ads as
carriers of interpretive resources and formalize two hermeneutical harms. On the one hand, we introduce hermeneutical
deprivation through systematic under-exposure. On the other hand, we define hermeneutical distortion as a systematic
over-exposure. We illustrate these mechanisms using exploratory correlational evidence from theAIDS Advertising
Evaluationsurveys, where framing-sensitive awareness gaps and patterns involving perceived sensationalism are
consistent with deprivation and distortion. We then incorporate these harms into an allocation framework by defining
a new, hermeneutically aware utility and a group-level constraint on hermeneutical opportunity, thereby extending
standard utility-driven and parity-based formulations. Controlled simulations trace how hermeneutical harms interact
with classical fairness constraints, indicating that classical fairness requirements come with a modest but non-zero
loss in hermeneutically-aware utility. Meanwhile, equality of opportunity is consistently the constraint that affects
cost the most. At the same time, classical fairness constraints substantially reduce concentrated under-delivery to
12

Beyond Distributive Justice: Hermeneutical Fairness in Ad Delivery
disadvantaged groups. This explicitly highlights that economic utility, distributive guarantees, and hermeneutical harms
are not automatically aligned in ad delivery.
More broadly, this paper advances a broader aim of informing formal allocation models with philosophically grounded
epistemic concepts. The framework shows how hermeneutical injustice can be embedded into optimization objectives
and constraints, reframing fairness in ad delivery as a hermeneutical question. Indeed, it is not only who sees which ads
that matters, but also what interpretative resources those ads provide and how different groups are positioned to make
sense of them. Incorporating hermeneutical harms into ad allocation provides a principled approach to detecting and
mitigating exclusionary dynamics that may persist under exposure parity alone.
Future work includes: i) estimating our model parameters and validating uptake-related constructs and our framework
within controlled laboratory experiments and, where possible, using online ad-delivery data; ii) validating our notion of
hermeneutical fairness in other domains, such as job advertising, finance, and politics; iii) extend our framework to
multiple protected groups, multiple ads, and to account for dynamic feedback.
References
[Ali et al.(2023)] Muhammad Ali, Angelica Goetzen, Alan Mislove, Elissa M Redmiles, and Piotr Sapiezynski. 2023.
Problematic advertising and its disparate exposure on Facebook. In32nd USENIX Security Symposium (USENIX
Security 23). 5665–5682.
[Ali et al.(2019)] Muhammad Ali, Piotr Sapiezynski, Miranda Bogen, Aleksandra Korolova, Alan Mislove, and Aaron
Rieke. 2019. Discrimination through optimization: How Facebook’s Ad delivery can lead to biased outcomes.
Proceedings of the ACM on human-computer interaction3, CSCW (2019), 1–30.
[Ali et al.(2021)] Muhammad Ali, Piotr Sapiezynski, Aleksandra Korolova, Alan Mislove, and Aaron Rieke. 2021. Ad
delivery algorithms: The hidden arbiters of political messaging. InProceedings of the 14th ACM International
Conference on Web Search and Data Mining. 13–21.
[Alvarado(2023)] Ramón Alvarado. 2023. AI as an epistemic technology.Science and Engineering Ethics29, 5
(2023), 32.
[Andreou et al.(2018)] Athanasios Andreou, Giridhari Venkatadri, Oana Goga, Krishna P Gummadi, Patrick Loiseau,
and Alan Mislove. 2018. Investigating ad transparency mechanisms in social media: A case study of Facebook’s
explanations. InNDSS 2018-Network and distributed system security symposium. 1–15.
[Antoniou and Akrivos(2020)] Alexandros Antoniou and Dimitris Akrivos. 2020. Gender portrayals in advertising:
stereotypes, inclusive marketing and regulation.Journal of Media Law12, 1 (2020), 78–115.
[Applequist and Ball(2018)] Janelle Applequist and Jennifer Gerard Ball. 2018. An updated analysis of direct-to-
consumer television advertisements for prescription drugs.The Annals of Family Medicine16, 3 (2018),
211–216.
[Asplund et al.(2020)] Joshua Asplund, Motahhare Eslami, Hari Sundaram, Christian Sandvig, and Karrie Karahalios.
2020. Auditing race and gender discrimination in online housing markets. InProceedings of the international
AAAI conference on web and social media, V ol. 14. 24–35.
[Bagwala(2024)] Abbas Bagwala. 2024. On informational injustice and epistemic exclusions.Synthese203, 6 (2024),
194.
[Bär et al.(2024)] Dominik Bär, Francesco Pierri, Gianmarco De Francisci Morales, and Stefan Feuerriegel. 2024.
Systematic discrepancies in the delivery of political ads on Facebook and Instagram.PNAS nexus3, 7 (2024),
pgae247.
[Baseman et al.(2013)] Janet G Baseman, Debra Revere, Ian Painter, Mariko Toyoji, Hanne Thiede, and Jeffrey Duchin.
2013. Public health communications and alert fatigue.BMC health services research13, 1 (2013), 295.
[Baumann et al.(2024)] Joachim Baumann, Piotr Sapiezynski, Christoph Heitz, and Aniko Hannak. 2024. Fairness in
online ad delivery. InProceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency.
1418–1432.
[Bozdag(2013)] Engin Bozdag. 2013. Bias in algorithmic filtering and personalization.Ethics and information
technology15, 3 (2013), 209–227.
[Bozdag and Van Den Hoven(2015)] Engin Bozdag and Jeroen Van Den Hoven. 2015. Breaking the filter bubble:
democracy and design.Ethics and information technology17, 4 (2015), 249–265.
[Cagle(2023)] Veronica Cagle. 2023. Using Machine Learning to Measure Political Polarization on Social Media.
(2023).
13

Quaresmini et al.
[Celis et al.(2019b)] Elisa Celis, Anay Mehrotra, and Nisheeth Vishnoi. 2019b. Toward controlling discrimination in
online ad auctions. InInternational Conference on Machine Learning. PMLR, 4456–4465.
[Celis et al.(2019a)] L Elisa Celis, Sayash Kapoor, Farnood Salehi, and Nisheeth Vishnoi. 2019a. Controlling polariza-
tion in personalization: An algorithmic framework. InProceedings of the conference on fairness, accountability,
and transparency. 160–169.
[Chien and Danks(2023)] Jennifer Chien and David Danks. 2023. Fairness vs. personalization: Towards equity in
epistemic utility.arXiv preprint arXiv:2309.11503(2023).
[Chowdhary et al.(2024)] Shubham Chowdhary, Giulia De Pasquale, Nicolas Lanzetti, Ana-Andreea Stoica, and
Florian Dörfler. 2024. Fairness in social influence maximization via optimal transport.Advances in Neural
Information Processing Systems37 (2024), 10380–10413.
[Cinus et al.(2022)] Federico Cinus, Marco Minici, Corrado Monti, and Francesco Bonchi. 2022. The effect of people
recommenders on echo chambers and polarization. InProceedings of the International AAAI Conference on Web
and Social Media, V ol. 16. 90–101.
[Coady(2017)] David Coady. 2017. Epistemic injustice as distributive injustice. InThe Routledge handbook of
epistemic injustice. Routledge, 61–68.
[Coeckelbergh(2022)] Mark Coeckelbergh. 2022.The political philosophy of AI: an introduction. John Wiley & Sons.
[Coeckelbergh(2025)] Mark Coeckelbergh. 2025. AI and Epistemic Agency: How AI Influences Belief Revision and
Its Normative Implications.Social Epistemology(2025), 1–13.
[Coliva(2025)] Annalisa Coliva. 2025. Hysteria, Hermeneutical Injustice and Conceptual Engineering.Social Episte-
mology39, 2 (2025), 121–133.
[Corbett-Davies et al.(2017)] Sam Corbett-Davies, Emma Pierson, Avi Feller, Sharad Goel, and Aziz Huq. 2017.
Algorithmic decision making and the cost of fairness. InProceedings of the 23rd acm sigkdd international
conference on knowledge discovery and data mining. 797–806.
[Cotter and Reisdorf(2020)] Kelley Cotter and Bianca C Reisdorf. 2020. Algorithmic knowledge gaps: A new horizon
of (digital) inequality.International Journal of Communication14 (2020), 21.
[Dalenberg(2018)] David Jacobus Dalenberg. 2018. Preventing discrimination in the automated targeting of job
advertisements.Computer law & security review34, 3 (2018), 615–627.
[Datta et al.(2018)] Amit Datta, Anupam Datta, Jael Makagon, Deirdre K Mulligan, and Michael Carl Tschantz. 2018.
Discrimination in online advertising: A multidisciplinary inquiry. InConference on Fairness, Accountability and
Transparency. PMLR, 20–34.
[Davis(2018)] Judy Foster Davis. 2018. Selling whiteness?–A critical review of the literature on marketing and racism.
Journal of Marketing Management34, 1-2 (2018), 134–177.
[de Vries et al.(2025)] Wietske de Vries, Laura Batstra, and Arjen van Assen. 2025. Exploring Concept Creep: Youth’s
portrayal of ADHD on TikTok.SSM-Mental Health(2025), 100489.
[Deldjoo et al.(2022)] Yashar Deldjoo, Dietmar Jannach, Alejandro Bellogin, Alessandro Difonzo, and Dario Zan-
zonelli. 2022. Fairness in recommender systems: research landscape and future directions.arXiv preprint
arXiv:2205.11127(2022).
[Dotson(2011)] Kristie Dotson. 2011. Tracking epistemic violence, tracking practices of silencing.Hypatia26, 2
(2011), 236–257.
[Dotson(2012)] Kristie Dotson. 2012. A cautionary tale: On limiting epistemic oppression.Frontiers: A Journal of
Women Studies33, 1 (2012), 24–47.
[Eisend(2010)] Martin Eisend. 2010. A meta-analysis of gender roles in advertising.Journal of the academy of
marketing science38, 4 (2010), 418–440.
[Fabris et al.(2021)] Alessandro Fabris, Alan Mishler, Stefano Gottardi, Mattia Carletti, Matteo Daicampi, Gian Anto-
nio Susto, and Gianmaria Silvello. 2021. Algorithmic audit of italian car insurance: Evidence of unfairness in
access and pricing. InProceedings of the 2021 AAAI/ACM Conference on AI, Ethics, and Society. 458–468.
[Fricker(2007)] Miranda Fricker. 2007.Epistemic Injustice: Power and the Ethics of Knowing. Oxford University
Press, Oxford.
[Fricker(2017)] Miranda Fricker. 2017. Evolving concepts of epistemic injustice. InThe Routledge handbook of
epistemic injustice. Routledge, 53–60.
14

Beyond Distributive Justice: Hermeneutical Fairness in Ad Delivery
[Gaucher et al.(2011)] Danielle Gaucher, Justin Friesen, and Aaron C Kay. 2011. Evidence that gendered wording in
job advertisements exists and sustains gender inequality.Journal of personality and social psychology101, 1
(2011), 109.
[Giannou et al.(2016)] Foteini K Giannou, Chrissa G Tsiara, Georgios K Nikolopoulos, Michael Talias, Vasiliki
Benetou, Maria Kantzanou, Stefanos Bonovas, and Angelos Hatzakis. 2016. Condom effectiveness in reducing
heterosexual HIV transmission: a systematic review and meta-analysis of studies on HIV serodiscordant couples.
Expert review of pharmacoeconomics & outcomes research16, 4 (2016), 489–499.
[Goldfarb(2014)] Avi Goldfarb. 2014. What is different about online advertising?Review of Industrial Organization
44, 2 (2014), 115–129.
[Goodman(2014)] Ellen Goodman. 2014. Informational justice as the new media pluralism.Media Policy Blog(2014).
[Grgi´c-Hlaˇca et al.(2018)] Nina Grgi´c-Hlaˇca, Muhammad Bilal Zafar, Krishna P Gummadi, and Adrian Weller. 2018.
Beyond distributive fairness in algorithmic decision making: Feature selection for procedurally fair learning. In
Proceedings of the AAAI conference on artificial intelligence, V ol. 32.
[Guo et al.(2022)] Yi Guo, Zhaocheng Liu, Jianchao Tan, Chao Liao, Sen Yang, Lei Yuan, Dongying Kong, Zhi Chen,
and Ji Liu. 2022. LPFS: Learnable Polarizing Feature Selection for Click-Through Rate Prediction.arXiv
preprint arXiv:2206.00267(2022).
[Harris(2022)] Keith Raymond Harris. 2022. Real fakes: The epistemology of online misinformation.Philosophy &
Technology35, 3 (2022), 83.
[Hartmann et al.(2025)] David Hartmann, Sonja Mei Wang, Lena Pohlmann, and Bettina Berendt. 2025. A systematic
review of echo chamber research: comparative analysis of conceptualizations, operationalizations, and varying
outcomes.Journal of Computational Social Science8, 2 (2025), 52.
[Hassan and Barber(2021)] Aumyo Hassan and Sarah J Barber. 2021. The effects of repetition frequency on the
illusory truth effect.Cognitive research: principles and implications6, 1 (2021), 38.
[Heger et al.(2020)] Irene Heger, Sebastian Köhler, Martin van Boxtel, Marjolein de Vugt, KlaasJan Hajema, Frans
Verhey, and Kay Deckers. 2020. Raising awareness for dementia risk reduction through a public health campaign:
a pre-post study.BMJ open10, 11 (2020), e041211.
[Hoffmann(2019)] Anna Lauren Hoffmann. 2019. Where fairness fails: data, algorithms, and the limits of antidiscrimi-
nation discourse.Information, Communication & Society22, 7 (2019), 900–915.
[Hopster(2024)] JKG Hopster. 2024. Socially disruptive technologies and epistemic injustice.Ethics and Information
Technology26, 1 (2024), 14.
[Hyzen et al.(2025)] Aaron Hyzen, Hilde Van den Bulck, Manuel Puppis, Michelle Kulig, and Steve Paulussen. 2025.
Epistemic welfare and algorithmic recommender systems: overcoming the epistemic crisis in the digitalized
public sphere.Communication Theory(2025), qtaf018.
[Imana et al.(2021)] Basileal Imana, Aleksandra Korolova, and John Heidemann. 2021. Auditing for discrimination in
algorithms delivering job ads. InProceedings of the web conference 2021. 3767–3778.
[Imana et al.(2024)] Basileal Imana, Aleksandra Korolova, and John Heidemann. 2024. Auditing for racial discrimina-
tion in the delivery of education ads. InProceedings of the 2024 ACM Conference on Fairness, Accountability,
and Transparency. 2348–2361.
[Imana et al.(2025)] Basileal Imana, Aleksandra Korolova, and John Heidemann. 2025. Auditing for Bias in Ad
Delivery Using Inferred Demographic Attributes. InProceedings of the 2025 ACM Conference on Fairness,
Accountability, and Transparency. 2640–2656.
[Kant(2020)] Tanya Kant. 2020.Making it personal: Algorithmic personalization, identity, and everyday life. Oxford
University Press.
[Karasavva et al.(2025)] Vasileia Karasavva, Caroline Miller, Nicole Groves, Andrés Montiel, Will Canu, and Amori
Mikami. 2025. A double-edged hashtag: Evaluation of# ADHD-related TikTok content and its associations with
perceptions of ADHD.PloS one20, 3 (2025), e0319335.
[Katzman et al.(2023)] Jared Katzman, Angelina Wang, Morgan Scheuerman, Su Lin Blodgett, Kristen Laird, Hanna
Wallach, and Solon Barocas. 2023. Taxonomizing and measuring representational harms: A look at image
tagging. InProceedings of the AAAI Conference on artificial intelligence, V ol. 37. 14277–14285.
[Kingsley et al.(2020)] Sara Kingsley, Clara Wang, Alex Mikhalenko, Proteeti Sinha, and Chinmay Kulkarni. 2020. Au-
diting digital platforms for discrimination in economic opportunity advertising.arXiv preprint arXiv:2008.09656
(2020).
15

Quaresmini et al.
[Kong(2026)] Youjin Kong. 2026. What is the point of equality in machine learning fairness? Beyond equality of
opportunity.ACM Journal on Responsible Computing3, 1 (2026), 1–25.
[Lalor et al.(2024)] John P Lalor, Ahmed Abbasi, Kezia Oketch, Yi Yang, and Nicole Forsgren. 2024. Should fairness
be a metric or a model? A model-based framework for assessing bias in machine learning pipelines.ACM
Transactions on Information Systems42, 4 (2024), 1–41.
[Lambrecht and Tucker(2019)] Anja Lambrecht and Catherine Tucker. 2019. Algorithmic bias? An empirical study of
apparent gender-based discrimination in the display of STEM career ads.Management science65, 7 (2019),
2966–2981.
[Lee et al.(2013)] Kuang-Chih Lee, Ali Jalali, and Ali Dasdan. 2013. Real time bid optimization with smooth budget
delivery in online advertising. InProceedings of the seventh international workshop on data mining for online
advertising. 1–9.
[Li and Yang(2025)] Jinhui Li and Xiaodong Yang. 2025. Does exposure necessarily lead to misbelief? A meta-analysis
of susceptibility to health misinformation.Public Understanding of Science34, 2 (2025), 222–242.
[Li et al.(2025)] Xiaolong Li, Ying Rong, Renyu Zhang, and Huan Zheng. 2025. Online advertisement allocation
under customer choices and algorithmic fairness.Management Science71, 1 (2025), 825–843.
[Loi et al.(2022)] Samantha M Loi, Anita MY Goh, Ramon Mocellin, Charles B Malpas, Shaun Parker, Dhamidhu
Eratne, Sarah Farrand, Wendy Kelso, Andrew Evans, Mark Walterfang, et al . 2022. Time to diagnosis in
younger-onset dementia and the impact of a specialist diagnostic service.International Psychogeriatrics34, 4
(2022), 367–375.
[McCracken(1986)] Grant McCracken. 1986. Culture and consumption: A theoretical account of the structure and
movement of the cultural meaning of consumer goods.Journal of consumer research13, 1 (1986), 71–84.
[Medina(2013)] José Medina. 2013.The epistemology of resistance: Gender and racial oppression, epistemic injustice,
and the social imagination. Oxford University Press.
[Milano and Prunkl(2025)] Silvia Milano and Carina Prunkl. 2025. Algorithmic profiling as a source of hermeneutical
injustice.Philosophical Studies182, 1 (2025), 185–203.
[Mintzes(2002)] Barbara Mintzes. 2002. Direct to consumer advertising is medicalising normal human experienceFor.
Bmj324, 7342 (2002), 908–911.
[Molina et al.(2023)] Mathieu Molina, Nicolas Gast, Patrick Loiseau, and Vianney Perchet. 2023. Trading-off price
for data quality to achieve fair online allocation.Advances in Neural Information Processing Systems36 (2023),
40096–40139.
[Mollema(2025)] Warmhold Jan Thomas Mollema. 2025. A taxonomy of epistemic injustice in the context of AI and
the case for generative hermeneutical erasure.AI and Ethics5, 5 (2025), 5535–5555.
[Muñoz et al.(2024)] Pau Muñoz, Alejandro Bellogín, Raúl Barba-Rojas, and Fernando Díez. 2024. Quantifying
polarization in online political discourse.EPJ Data Science13, 1 (2024), 39.
[Navon et al.(2023)] Inbal Livni Navon, Charlotte Peale, Omer Reingold, and Judy Hanwen Shen. 2023. Bidding
Strategies for Proportional Representation in Advertisement Campaigns.arXiv preprint arXiv:2305.13542
(2023).
[Noble(2018)] Safiya Umoja Noble. 2018. Algorithms of oppression: How search engines reinforce racism. In
Algorithms of oppression. New York university press.
[Oswald and Oswald(2012)] Laura R Oswald and Laura Oswald. 2012.Marketing semiotics: Signs, strategies, and
brand value. Oxford University Press.
[Pariser(2011)] Eli Pariser. 2011.The filter bubble: What the Internet is hiding from you. penguin UK.
[Perez-Heydrich et al.(2024)] Carlos Perez-Heydrich, Courtney Walker, Macie Pile, and Yuri Agrawal. 2024.
Comparison of digital recruitment strategies for Alzheimer’s disease patients.Digital Health10 (2024),
20552076241229164.
[Peysakhovich et al.(2023)] Alexander Peysakhovich, Christian Kroer, and Nicolas Usunier. 2023. Implementing
fairness constraints in markets using taxes and subsidies. InProceedings of the 2023 ACM Conference on
Fairness, Accountability, and Transparency. 916–930.
[Phillips et al.(2023)] Samantha C Phillips, Joshua Uyheng, and Kathleen M Carley. 2023. A high-dimensional
approach to measuring online polarization.Journal of Computational Social Science6, 2 (2023), 1147–1178.
[Pollay(2014)] Richard W Pollay. 2014. The distorted mirror: Reflections on the unintended consequences of
advertising. InReadings in Advertising, Society, and Consumer Culture. Routledge, 291–318.
16

Beyond Distributive Justice: Hermeneutical Fairness in Ad Delivery
[Pozzi(2023)] Giorgia Pozzi. 2023. Automated opioid risk scores: a case for machine learning-induced epistemic
injustice in healthcare.Ethics and Information Technology25, 1 (2023), 3.
[Ribeiro et al.(2018)] Filipe Ribeiro, Lucas Henrique, Fabricio Benevenuto, Abhijnan Chakraborty, Juhi Kulshrestha,
Mahmoudreza Babaei, and Krishna Gummadi. 2018. Media bias monitor: Quantifying biases of social media
news outlets at large-scale. InProceedings of the International AAAI Conference on Web and Social Media,
V ol. 12.
[Rona(2023)] Emmett Rona. 2023. Representation of race and ethnicity in mainstream advertising: A critical analysis
of racial stereotypes in global advertising campaigns.Journal of Linguistics and Communication Studies2, 4
(2023), 44–50.
[Ross Arguedas et al.(2022)] Amy Ross Arguedas, Craig Robertson, Richard Fletcher, and Rasmus Nielsen. 2022.
Echo chambers, filter bubbles, and polarisation: A literature review. (2022).
[Rößner and Eisend(2023)] Anna Rößner and Martin Eisend. 2023. Ethnic minorities in advertising.Journal of
Advertising52, 5 (2023), 774–784.
[Sapiezynski et al.(2024)] Piotr Sapiezynski, Levi Kaplan, Alan Mislove, and Aleksandra Korolova. 2024. On the
Use of Proxies in Political Ad Targeting.Proceedings of the ACM on Human-Computer Interaction8, CSCW2
(2024), 1–31.
[Schenker et al.(2014)] Yael Schenker, Robert M Arnold, and Alex John London. 2014. The ethics of advertising for
health care services.The American Journal of Bioethics14, 3 (2014), 34–43.
[Schiros et al.(2025)] Ashley Schiros, Nick Bowman, and Kevin Antshel. 2025. Misinformation mayhem: the effects
of TikTok content on ADHD knowledge, stigma, and treatment-seeking intentions.European Child & Adolescent
Psychiatry(2025), 1–13.
[Schoeffer et al.(2023)] Jakob Schoeffer, Alexander Ritchie, Keziah Naggita, Faidra Monachou, Jessica Finocchiaro,
and Marc Juarez. 2023. Online platforms and the fair exposure problem under homophily. InProceedings of the
AAAI conference on artificial intelligence, V ol. 37. 11899–11908.
[Selbst et al.(2019)] Andrew D Selbst, Danah Boyd, Sorelle A Friedler, Suresh Venkatasubramanian, and Janet
Vertesi. 2019. Fairness and abstraction in sociotechnical systems. InProceedings of the conference on fairness,
accountability, and transparency. 59–68.
[Shelby et al.(2023)] Renee Shelby, Shalaleh Rismani, Kathryn Henne, AJung Moon, Negar Rostamzadeh, Paul
Nicholas, N’Mah Yilla-Akbari, Jess Gallegos, Andrew Smart, Emilio Garcia, et al . 2023. Sociotechnical
harms of algorithmic systems: Scoping a taxonomy for harm reduction. InProceedings of the 2023 AAAI/ACM
Conference on AI, Ethics, and Society. 723–741.
[Shelton et al.(2004)] James D Shelton, Daniel T Halperin, Vinand Nantulya, Malcolm Potts, Helene D Gayle, and
King K Holmes. 2004. Partner reduction is crucial for balanced “ABC” approach to HIV prevention.Bmj328,
7444 (2004), 891–893.
[Shin(2025)] Donghee Shin. 2025. Automating epistemology: how AI reconfigures truth, authority, and verification.
AI & SOCIETY(2025), 1–7.
[Sierra et al.(2012)] Jeremy J Sierra, Michael R Hyman, and Robert S Heiser. 2012. Ethnic identity in advertising: A
review and meta-analysis.Journal of Promotion Management18, 4 (2012), 489–513.
[Singh and Joachims(2018)] Ashudeep Singh and Thorsten Joachims. 2018. Fairness of exposure in rankings. In
Proceedings of the 24th ACM SIGKDD international conference on knowledge discovery & data mining.
2219–2228.
[Skurka and Keating(2024)] Chris Skurka and David M Keating. 2024. How repeated exposure to persuasive messaging
shapes message responses over time: a longitudinal experiment.Human Communication Research50, 4 (2024),
518–529.
[Soares et al.(2019)] Felipe Bonow Soares, Raquel Recuero, and Gabriela Zago. 2019. Asymmetric polarization on
Twitter and the 2018 Brazilian presidential elections. InProceedings of the 10th international conference on
social media and society. 67–76.
[Speicher et al.(2018)] Till Speicher, Muhammad Ali, Giridhari Venkatadri, Filipe Nunes Ribeiro, George Arvanitakis,
Fabrício Benevenuto, Krishna P Gummadi, Patrick Loiseau, and Alan Mislove. 2018. Potential for discrimination
in online targeted advertising. InConference on fairness, accountability and transparency. PMLR, 5–19.
[Stauffer(2018)] Brian Stauffer. 2018. Only men need apply” gender discrimination in job advertisements in China.
New York: Human Rights Watch(2018).
17

Quaresmini et al.
[Stewart et al.(2022)] Heather Stewart, Emily Cichocki, and Carolyn McLeod. 2022. A perfect storm for epistemic
injustice: Algorithmic targeting and sorting on social media.Feminist Philosophy Quarterly8, 3/4 (2022).
[Sweeney(2013)] Latanya Sweeney. 2013. Discrimination in online ad delivery.Commun. ACM56, 5 (2013), 44–54.
[Symons and Alvarado(2022)] John Symons and Ramón Alvarado. 2022. Epistemic injustice and data science tech-
nologies.Synthese200, 2 (2022), 87.
[Talevski et al.(2020)] Jason Talevski, Anna Wong Shee, Bodil Rasmussen, Georgie Kemp, and Alison Beauchamp.
2020. Teach-back: A systematic review of implementation and impacts.PloS one15, 4 (2020), e0231350.
[Tang et al.(2022)] Tanzhe Tang, Amineh Ghorbani, Flaminio Squazzoni, and Caspar G Chorus. 2022. Together alone:
a group-based polarization measurement.Quality & Quantity56, 5 (2022), 3587–3619.
[Timmaraju et al.(2023)] Aditya Srinivas Timmaraju, Mehdi Mashayekhi, Mingliang Chen, Qi Zeng, Quintin Fettes,
Wesley Cheung, Yihan Xiao, Manojkumar Rangasamy Kannadasan, Pushkar Tripathi, Sean Gahagan, et al. 2023.
Towards fairness in personalized ads using impression variance aware reinforcement learning. InProceedings of
the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. 4937–4947.
[Vakratsas and Ambler(1999)] Demetrios Vakratsas and Tim Ambler. 1999. How advertising works: what do we really
know?Journal of marketing63, 1 (1999), 26–43.
[Ventola(2011)] C Lee Ventola. 2011. Direct-to-consumer pharmaceutical advertising: therapeutic or toxic?Pharmacy
and Therapeutics36, 10 (2011), 669.
[Wang et al.(2025)] Angelina Wang, Xuechunzi Bai, Solon Barocas, and Su Lin Blodgett. 2025. Measuring Machine
Learning Harms from Stereotypes Requires Understanding Who Is Harmed by Which Errors in What Ways. In
Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency. 746–762.
[Watts(2021)] Alison Watts. 2021. Fairness and efficiency in online advertising mechanisms.Games12, 2 (2021), 36.
[Wegner et al.(2024)] Laila Wegner, Marie Christin Decker, and Carmen Leicht-Scholten. 2024.Beyond Distributions:
A Systematic Review on Relational Algorithmic Justice.
[Weller et al.(1996)] Susan C Weller, Karen Davis-Beaty, and Cochrane HIV/AIDS Group. 1996. Condom effectiveness
in reducing heterosexual HIV transmission.Cochrane database of systematic reviews2012, 3 (1996).
[Williamson(1978)] Judith Williamson. 1978.Decoding advertisements. V ol. 4. Marion Boyars London.
[Wind(1978)] Yoram Wind. 1978. Issues and advances in segmentation research.Journal of marketing research15, 3
(1978), 317–337.
[Yuan et al.(2025)] Di Yuan, Manmohan Aseri, and Tridas Mukhopadhyay. 2025. Is Fair Advertising Good for
Platforms?Marketing Science(2025).
[Yuan et al.(2013)] Shuai Yuan, Jun Wang, and Xiaoxue Zhao. 2013. Real-time bidding for online advertising:
measurement and analysis. InProceedings of the seventh international workshop on data mining for online
advertising. 1–8.
A AIDS Advertising Evaluation (1986-1987): Dataset Details and Pre-processing
We use theAIDS Advertising Evaluationsurveys collected in 1986-1987. The public release includes multiple survey
versions (questionnaire variants) fielded across several waves. We construct a pooled respondent-level dataset from
versions 1, 2, 3, 4, 6, 7, 8, and 16. We instead exclude versions 5 and 12-15 because they omit key variables required
for our constructs, including sexual behavior history questions needed to construct the protected-group proxy and
behavioral outcome index. In the following, we explain how we have pre-processed data and used them for our analysis.
Protected-group proxy constructionThe dataset does not contain a direct measure of sexual orientation. We
therefore define a coarse partner-history grouping from reported partners in the last 12 months:
• Same-sex partner history(“homosexual” proxy): SameSexPartners>0 (regardless of
OppositeSexPartners).
•Opposite-sex only(“heterosexual” proxy):SameSexPartners= 0andOppositeSexPartners>0.
• Unknown: otherwise (i.e., SameSexPartners= 0 and OppositeSexPartners= 0 , or missing partner
counts).
18

Beyond Distributive Justice: Hermeneutical Fairness in Ad Delivery
Survey version Opposite-sex only Any same-sex Total coded
version 1 654 40 694
version 2 5 151 156
version 3 660 40 700
version 4 9 289 298
version 6 216 10 226
version 7 553 38 591
version 8 0 284 284
version 16 0 250 250
Total 2097 1102 3199
Table 2: Counts by survey version for the partner-history proxy, restricted to respondents for whom the proxy is defined.
Respondents reporting both partner types are assigned to the any same-sex group. This avoids forcing bisexual
respondents into the opposite-sex-only group, but it collapses bisexuality into a broader non-heterosexual category. The
proxy captures reported recent behavior (12 month window), not identity, and may misclassify respondents whose
relevant behavior occurs outside the window or is not disclosed. We therefore interpret subgroup comparisons as
descriptive and potentially conservative with respect to the any same-sex group.
Table 2 reports counts in the proxy-defined sample. The dataset contains n= 3,199 coded respondents, comprising
2,097 classified as opposite-sex only and 1,102 classified as any same-sex. As indicated in Table 2, the sample is
unbalanced overall and exhibits pronounced imbalance across survey versions.
Advertising exposure measureWe operationalize self-reported advertising exposure using reception variables of the
form: “Where did you see or hear this information?” We treat each channel indicator as binary (Yes/No) where available
(e.g., magazines, newspapers, radio, TV , pamphlets/leaflets, posters, newspaper articles, radio/TV programmes, talking
with friends, telephone line).
We define respondent-level exposure as:
•Exposedif the respondent answers “Yes” to at least one observed reception variable.
•Not exposedif the respondent answers “No” to all observed reception variables.
Exposure is coded missing if all reception variables are missing, to avoid treating nonresponse as non-exposure.
Behavioral-outcome proxy constructionWe construct a three-level behavioral-outcome proxy from two self-report
binary variables:
cut_down_sexual_partnersandused_sheaths(condoms). We code:
No Change (No/No), Moderate Change (Yes/No or No/Yes), Change (Yes/Yes).
This coding treats the two reported behaviors as complementary forms of risk reduction: fewer partners reduce
exposure opportunities, while condom use reduces per-act transmission risk [Shelton et al.(2004), Giannou et al.(2016),
Weller et al.(1996)]. We only define the composite index when both components are observed and standard (Yes/No)
responses; otherwise the index is missing.
Missingness in behavioral variables and implicationsThe behavioral variables exhibit substantial nonresponse in
the dataset used for the behavioral-outcome analysis. Table 3 reports missingness rates by partner-history group in this
analysis sample.
To assess whether missingness is associated with the partner-history grouping, we test independence between a
missingness indicator and partner-history group using Pearson χ2 tests on the corresponding contingency tables (Table
4). In both cases, independence is rejected, indicating that missingness is systematically associated with the grouping.
Accordingly, all statistics involving these behavioral variables are computed on the subset of non-missing responses
and should be interpreted as descriptive patterns for that responding subset rather than as population-representative
estimates.
Statistical checks for the exploratory patternsFor Figure 1a, we report 95% Wilson confidence intervals for the
conditional proportions P(Exposure|Sexuality) , along with a Pearson χ2 test of independence for the associated 2×2
19

Quaresmini et al.
Variable Partner-history group Total Observed Missing Missing rate (%)
used_sheathsOpposite-sex only 2088 63 2025 96.98
Any same-sex 529 46 483 91.30
Unknown 169 0 169 100.00
cut_down_sexual_partnersOpposite-sex only 2088 63 2025 96.98
Any same-sex 529 233 296 55.95
Unknown 169 0 169 100.00
Table 3: Missingness rates for the behavioral variables by partner-history group in the analysis sample used for the
behavioral-outcome proxy.
Variableχ 2 dofp-value
used_sheaths43.527 23.5×10 −10
cut_down_sexual_partners769.586 27.7×10 −168
Table 4: Results of Pearsonχ2 tests of independence between missingness in the behavioral variables and partner-history
group in the analysis sample, with degrees of freedom (dof) andp-value.
contingency table and Cramér’s V as a measure of association strength. Table 5 reports the estimated proportions.
The association is statistically clear (χ2(1) = 148.37,p <0.001, Cramér’sV= 0.215), indicating different exposure
distributions across the two partner-history groups. Consistent with the framing of this section, we interpret this result
as evidence of an asymmetric descriptive exposure pattern in the sample rather than as a definitive measure of harm.
For Figure 1b, we report 95% Wilson confidence intervals for the conditional proportions P(Behavior change|
Exposure), together with a Pearson χ2 test of independence for the corresponding 2×3 contingency table and Cramér’s
V . Table 6 reports the estimated proportions. Confidence intervals are wider for the exposed group because of its
smaller sample size. The global test does not indicate a statistically clear difference in the distribution of behavioral
change across exposure groups (χ2(2) = 1.12, p= 0.572, Cramér’s V= 0.084 ). We therefore treat this pattern as
descriptive and exploratory rather than as evidence of a strong difference between exposure groups.
For Figure 2a, we report a Pearson χ2 test of independence for the corresponding 4×2 contingency table, together with
Cramér’s V . Table 7 gives the underlying counts. The association between sensationalism responses and self-reported
worry about AIDS is statistically clear ( χ2(3) = 47.87, p <0.001 , Cramér’s V= 0.191 ). As elsewhere in this
appendix, we interpret this result as correlational support for the descriptive pattern shown in the heatmap, not as
evidence of a causal effect. For Figure 2b, we report 95% Wilson confidence intervals for the conditional proportions
P(Sensationalism|Exposure) , together with a Pearsonχ2 test of independence for the corresponding2×4 contingency
table and Cramér’s V . Table 8 reports the estimated proportions. Confidence intervals are wider for the not-exposed
group because of its smaller sample size. The global test does not indicate a statistically clear difference in the
distribution of sensationalism responses across exposure groups (χ2(3) = 0.91, p= 0.824, Cramér’s V= 0.032 ). We
therefore treat this pattern as descriptive and exploratory rather than as evidence of a strong between-group difference.
For Figure 2c, we report Pearson χ2 tests of independence for the relevant contingency tables, together with Cramér’sV .
Under the formulation referring topeople who need blood transfusions, the distribution of awareness responses differs
across the two partner-history groups (χ2(2) = 29.88, p <0.001, Cramér’s V= 0.097 ). Under thehaemophiliacs
formulation, the association is weaker and only borderline significant (χ2(2) = 5.99, p= 0.050, Cramér’s V= 0.043 ).
We also test whether response distributions differ across the two formulations within each partner-history group.
The wording effect is statistically clear both among opposite-sex-only respondents ( χ2(2) = 10.45, p= 0.005 ,
Cramér’s V= 0.050 ) and among respondents with any same-sex partner history (χ2(2) = 22.94, p <0.001, Cramér’s
V= 0.102 ). As elsewhere in this section, we interpret these findings as correlational support for framing-sensitive
awareness patterns rather than as definitive measures of harm.
B Additional Simulation Diagnostics
We here report a set of results that complement the main analysis. First, we fix γ= 0 and we vary βb, thus considering
the same setting as in [ Baumann et al.(2024)], to show the consistency of our results with what we regard as the
baseline for our framework. Second, we vary γ (i.e., the hermeneutical-cost weight) while keeping all other parameters
20

Beyond Distributive Justice: Hermeneutical Fairness in Ad Delivery
Group Exposure Count N Proportion 95% CI
Any same-sex Not Exposed 883 1102 0.801 [0.777, 0.824]
Any same-sex Exposed 219 1102 0.199 [0.176, 0.223]
Opposite-sex only Not Exposed 1975 2097 0.942 [0.931, 0.951]
Opposite-sex only Exposed 122 2097 0.058 [0.049, 0.069]
Table 5: Estimated conditional proportions for Figure 1a with 95% Wilson confidence intervals.
Exposure Behavior change Count N Proportion 95% CI
Not Exposed No Change 50 125 0.400 [0.318, 0.488]
Not Exposed Moderate Change 43 125 0.344 [0.266, 0.431]
Not Exposed Change 32 125 0.256 [0.188, 0.339]
Exposed No Change 12 34 0.353 [0.215, 0.521]
Exposed Moderate Change 15 34 0.441 [0.289, 0.605]
Exposed Change 7 34 0.206 [0.103, 0.368]
Table 6: Estimated conditional proportions for Figure 1b with 95% Wilson confidence intervals.
fixed. This second scenario allows us to examine how increasing the weight on the hermeneutical-cost term affects the
achieved utility and exposure disparities.
When looking at Figure 4, we achieve results that are comparable with the one shown in [ Baumann et al.(2024)].
In particular, the constrained policies exhibit the largest utility loss (relative to the unconstrained benchmark) for
intermediate values of βb (around βb ≈0.2 -0.3), with smaller losses toward both ends of the explored range. Moreover,
Figure 4b shows that, while the unconstrained policy yields a large positive parity of exposure difference quickly rising,
the three fairness constraints variants keep the parity of exposure difference small and nearly flat acrossβ b.
Meanwhile, Figure 5 shows the results achieved when varying γ. As expected, Figure 5a shows that achieved utility
under all three fairness constraint variants declines overall as γ increases, with the gap between constrained and
unconstrained setting widening at higher γ. In terms of exposure disparities, Figure 5b indicates that the unconstrained
policy produces a growing parity of exposure difference as γ increases, whereas the constrained policies keep the
parity gap low with only minor variation across the full range of γ. Taken together, these patterns indicate that placing
greater weight on the hermeneutical-cost term is associated with a larger utility penalty for satisfying distributive and
hermeneutical constraints, and increased exposure inequality when no distributive constraint is imposed. This effect is
attenuated once distributive and hermeneutical constraints are imposed.
B.1 Additional Uptake Configurations
To assess how sensitive the qualitative patterns are to the distribution of uptake probabilities across groups, we
additionally report results for the three alternative uptake configurations introduced in Section 6. In the main text, results
are shown for the b-advantaged case (with ρa ∼Beta(4,6) and ρb ∼Beta(7,3) ). Here, we complement that analysis
with three additional configurations: (i) an a-advantaged case with ρa ∼Beta(8,2) and ρb ∼Beta(3,7) (Figure 6);
(ii) a neutral high-uptake configuration with ρa =ρ b ∼Beta(7,3) (Figure 7); (iii) a neutral lower-uptake configuration
withρ a =ρ b ∼Beta(4,6)(Figure 8). All other simulation settings are unchanged.
Across these configurations, the main qualitative patterns remain stable. In particular, constrained solutions continue to
achieve utility levels close to the unconstrained benchmark, while keeping exposure disparities substantially smaller
than in the unconstrained case. Changing the uptake distributions does affect the magnitude of the unconstrained
exposure gap, but does not alter the broader comparative pattern across constraints. Overall, these additional scenarios
suggest that the main simulation conclusions are not driven by a single parameterization of the Beta distributions,
although the size of the resulting disparities remains sensitive to the modeled uptake configuration.
C Protocol sketch for estimating uptake probability
A concrete path toward empirical validation of our framework is a controlled ad-delivery study designed to estimate
individual-level uptake probabilityρ x, a pipeline of which is sketched in Figure 9.
At a high level, each participant first enters the experiment and is assigned to an attribute-myopic delivery condition.
This places the participant into one of three exposure conditions: no exposure, low exposure with neutral or skewed
framing, or repeated exposure with neutral or skewed framing. After exposure, the participant completes a post-
21

Quaresmini et al.
Sensationalism Yes No
I disagree strongly 136 66
I tend to disagree 133 185
I tend to agree 107 179
I agree strongly 230 280
Table 7: Contingency table for Figure 2a, relating sensationalism responses to self-reported worry about AIDS.
Exposure Sensationalism Count N Proportion 95% CI
Not exposed I disagree strongly 9 49 0.184 [0.100, 0.314]
Not exposed I tend to disagree 13 49 0.265 [0.162, 0.403]
Not exposed I tend to agree 7 49 0.143 [0.071, 0.267]
Not exposed I agree strongly 20 49 0.408 [0.282, 0.548]
Exposed I disagree strongly 144 860 0.167 [0.144, 0.194]
Exposed I tend to disagree 191 860 0.222 [0.196, 0.251]
Exposed I tend to agree 157 860 0.183 [0.158, 0.210]
Exposed I agree strongly 368 860 0.428 [0.395, 0.461]
Table 8: Estimated conditional proportions for Figure 2b with 95% Wilson confidence intervals.
exposure uptake evaluation. This evaluation is intended to measure understanding and combines three components:
content understanding, scenario-based content application, and a teach-back or paraphrase task [Baseman et al.(2013),
Talevski et al.(2020)]. For instance, the instrument may ask participants to explain the main message of the ad, apply it
to a hypothetical case, and restate it in their own words. The resulting responses are then aggregated and normalized
into an individual uptake score, which yields an estimateˆρx for that participant.
At minimum, estimating uptake ρx requires linked data on participant features, assigned ad condition, ad variant or
framing, exposure count, and post-exposure uptake responses. Estimating platform-side utility parameters further
requires standard internal delivery variables such as bid value and predicted click probability. Enforcing or auditing the
group-level fairness constraints additionally requires access to protected-group labels or fairness-relevant proxies. This
highlights an implementation boundary. The individual-level hermeneutical cost can in principle be modeled without
direct access to protected attributes, whereas the group-level fairness constraints cannot be imposed or evaluated without
some group information. In practice, platforms may infer uptake-related signals from behavioral traces or learned
user representations, but such proxies may encode behavioral bias, unequal access, or platform-specific engagement
artifacts. As a result, optimizing on poorly validated proxies could amplify interpretative distortions while appearing
well calibrated under the model. When protected attributes are unavailable or highly regulated, the framework may
still support individual-level robustness checks and sensitivity analysis, but not the full enforcement of the fairness
constraints introduced in Section 4.
Remark on parameter calibration.The model parameters play different operational roles. The economic parameters
α and β are platform-side utility quantities and can in principle be obtained from delivery logs or advertiser bids. By
contrast, the epistemic parameters θ, ω, and ξ should be interpreted as decision weights encoding the costs of successful
uptake, failed uptake, and exclusion. For this reason, the empirical goal is not necessarily to identify them pointwise,
but to calibrate or bound them. Once ρx has been estimated, variation across the three exposure conditions can be used
to inform these remaining parameters. Comparisons between no exposure and exposure conditions can help bound
exclusion-related costs, while comparisons between lower-uptake and repeated-exposure conditions can inform the
calibration of penalties associated with failed or distorted uptake. These comparisons are therefore best understood as
inputs to calibration and sensitivity analysis, rather than as a strategy for point identification.
22

Beyond Distributive Justice: Hermeneutical Fairness in Ad Delivery
0.0 0.2 0.4 0.6 0.8 1.0
βb [-]
98.00
98.25
98.50
98.75
99.00
99.25
99.50
99.75
100.00
Utility in % of unconstrained utility
 Metric
Unconstrained
Parity of exposure
Equality of opportunity
Equality of hermeneutical opportunity
(a) Utility (% of unconstrained).
0.0 0.2 0.4 0.6 0.8 1.0
βb [-]
−0.100
−0.075
−0.050
−0.025
0.000
0.025
0.050
0.075
0.100
Diﬀerence in parity of exposure [-]
 Scenario
Unconstrained
Parity of exposure
Equality of epistemic opportunity
Equality of hermeneutical opportunity (b) Parity of exposure difference.
Figure 4:Baseline results.Achieved utility (as % of the unconstrained solution) and parity of exposure difference for
γ= 0and varyingβ b.
0.00 0.02 0.04 0.06 0.08 0.10 0.12
γ [-]
99.2
99.4
99.6
99.8
100.0
Utility in % of unconstrained utility
Metric
Unconstrained
Parity of exposure
Equality of opportunity
Equality of hermeneutical opportunity
(a) Utility (% of unconstrained).
0.00 0.02 0.04 0.06 0.08 0.10 0.12
γ [-]
−0.02
0.00
0.02
0.04
0.06
0.08
0.10
Diﬀerence in parity of exposure [-]
Scenario
Unconstrained
Parity of exposure
Equality of opportunity
Equality of hermeneutical opportunity (b) Parity of exposure difference.
Figure 5:Additional simulation results with varying hermeneutical-cost weight γ.Achieved utility (as % of the
unconstrained solution) and parity of exposure difference.
0.0 0.3 0.6 0.9
βb [-]
98.5
99.0
99.5
100.0
Utility in [%] of unconstrained utility
Scenario A
0.0 0.3 0.6 0.9
θb [-]
99.6
99.8
100.0
Scenario B
0.0 0.3 0.6 0.9
ωb [-]
99.6
99.8
100.0
Scenario C
0.0 0.3 0.6 0.9
ξ [-]
99.6
99.8
100.0
Scenario D
0.0 0.3 0.6 0.9
βb [-]
−0.05
0.00
0.05
0.10
Diﬀerence in parity of exposure [-]
0.0 0.3 0.6 0.9
θb [-]
0.00
0.01
0.02
0.03
0.04
0.0 0.3 0.6 0.9
ωb [-]
0.00
0.01
0.02
0.03
0.04
0.0 0.3 0.6 0.9
ξ [-]
0.00
0.01
0.02
0.03
0.04
Constraint
Unconstrained
Parity of Exposure
Equality of Opportunity
Equality of Hermeneutical Opportunity
Figure 6:Simulation results for Scenarios A–D (Table 1) under an a-advantaged uptake configuration.Uptake
probabilities are sampled as ρa ∼Beta(8,2) and ρb ∼Beta(3,7) . Top row: achieved utility (in % of the unconstrained
solution). Bottom row: parity of exposure difference. Solid lines show the median outcomes across the 100 replications,
while the shaded bands show their range according to the 0.25-0.75 quartiles.
23

Quaresmini et al.
0.0 0.3 0.6 0.9
βb [-]
98.5
99.0
99.5
100.0
Utility in [%] of unconstrained utility
Scenario A
0.0 0.3 0.6 0.9
θb [-]
99.6
99.8
100.0
Scenario B
0.0 0.3 0.6 0.9
ωb [-]
99.6
99.8
100.0
Scenario C
0.0 0.3 0.6 0.9
ξ [-]
99.6
99.8
100.0
Scenario D
0.0 0.3 0.6 0.9
βb [-]
−0.05
0.00
0.05
0.10
Diﬀerence in parity of exposure [-]
0.0 0.3 0.6 0.9
θb [-]
0.00
0.01
0.02
0.03
0.04
0.0 0.3 0.6 0.9
ωb [-]
0.00
0.01
0.02
0.03
0.04
0.0 0.3 0.6 0.9
ξ [-]
0.00
0.01
0.02
0.03
0.04
Constraint
Unconstrained
Parity of Exposure
Equality of Opportunity
Equality of Hermeneutical Opportunity
Figure 7:Simulation results for Scenarios A–D (Table 1) under a neutral high-uptake configuration.Uptake
probabilities are sampled identically across groups, with ρa =ρ b ∼Beta(7,3) . Top row: achieved utility (in % of the
unconstrained solution). Bottom row: parity of exposure difference. Solid lines show the median outcomes across the
100 replications, while the shaded bands show their range according to the 0.25-0.75 quartiles.
0.0 0.3 0.6 0.9
βb [-]
98.5
99.0
99.5
100.0
Utility in [%] of unconstrained utility
Scenario A
0.0 0.3 0.6 0.9
θb [-]
99.6
99.8
100.0
Scenario B
0.0 0.3 0.6 0.9
ωb [-]
99.6
99.8
100.0
Scenario C
0.0 0.3 0.6 0.9
ξ [-]
99.6
99.8
100.0
Scenario D
0.0 0.3 0.6 0.9
βb [-]
−0.05
0.00
0.05
0.10
Diﬀerence in parity of exposure [-]
0.0 0.3 0.6 0.9
θb [-]
0.00
0.01
0.02
0.03
0.04
0.0 0.3 0.6 0.9
ωb [-]
0.00
0.01
0.02
0.03
0.04
0.0 0.3 0.6 0.9
ξ [-]
0.00
0.01
0.02
0.03
0.04
Constraint
Unconstrained
Parity of Exposure
Equality of Opportunity
Equality of Hermeneutical Opportunity
Figure 8:Simulation results for Scenarios A–D (Table 1) under a neutral lower-uptake configuration.Uptake
probabilities are sampled identically across groups, with ρa =ρ b ∼Beta(4,6) . Top row: achieved utility (in % of the
unconstrained solution). Bottom row: parity of exposure difference. Solid lines show the median outcomes across the
100 replications, while the shaded bands show their range according to the 0.25-0.75 quartiles.
start attribute-myopic assignment
no exposure
low exposure
neutral/skewed
repeated exposure
neutral/skewed
uptake
evaluation
understanding
scenario
application
teach-back
aggregate &
normalize
estimate
ˆρx
Figure 9: Individual-level pipeline for estimating uptake probabilityρ x.
24
