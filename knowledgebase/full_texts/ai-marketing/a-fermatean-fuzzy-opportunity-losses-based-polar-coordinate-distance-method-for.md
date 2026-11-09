---
title: A Fermatean Fuzzy Opportunity Losses-Based Polar Coordinate Distance Method for Artificial Intelligence-Enhanced
  Custom-Made Print Advertisements
url: https://doi.org/10.1007/s12559-026-10642-2
category: ai-marketing
subcategory: framework
date: 2026-08
venue: Cognitive Computation
authors:
- Elif Akagün Ergin
- Galip Cihan Yalçın
- Karahan Kara
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s12559-026-10642-2.pdf
pages: 29
chars: 123553
fetched_at: '2026-11-08T19:59:01+00:00'
kb_version: 1
---

# A Fermatean Fuzzy Opportunity Losses-Based Polar Coordinate Distance Method for Artificial Intelligence-Enhanced Custom-Made Print Advertisements

RESEARCH
Cognitive Computation          (2026) 18:101
https://doi.org/10.1007/s12559-026-10642-2
Extended author information available on the last page of the article
Abstract
The increasing adoption of artificial intelligence (AI) across industries has also extended to the field of advertising, where
AI is being utilized in various aspects of advertisement design. AI bots employing text-to-image techniques have emerged
as an effective approach for generating customized print advertisements. Drawing on the principles of Social Cognitive
Theory, this study conceptualizes AI as a cognitive decision-support tool that enhances marketers’ learning, creative judg -
ment, and advertising decision-making through iterative feedback and systematic evaluation. This study aims to develop
a decision support system (DSS) for designing AI-enhanced custom-made print ads and selecting the best advertisement
from among the generated alternatives. A methodological approach comprising four phases is employed, focusing on the
production of advertisement alternatives and their ranking using a multi-attribute group decision-making approach. As
DSS, the Fermatean fuzzy (FF)-Entropy-opportunity losses (OPLO)-based polar coordinate distance (POCOD) hybrid
method is proposed and developed in this research. Decision-maker weights are determined using FF sets. Criteria weights
are calculated based on expert opinions through the FF-Entropy method. The aggregation of expert decision matrices is
conducted using the FF-weighted partitioned dual Maclaurin symmetric mean (FFWPDMSM) aggregation operator. The
AI-enhanced custom-made print ads are ranked using the FF-OPLO-POCOD method. The applicability of the proposed
hybrid method is demonstrated in a case study involving the design of advertisements for a dairy product aimed at a
hedonic customer base. The results identify Ads-4 as the most effective AI-generated advertisement among the twelve
alternatives. Sensitivity and comparative analyses confirm the robustness and consistency of the proposed framework, with
the top-ranked alternative remaining unchanged in all but one sensitivity scenario, thereby demonstrating the stability and
reliability of the decision-making process. The study concludes by presenting theoretical and practical implications for
AI-assisted advertising and marketing decision-making.
Keywords Custom-made print ads · Artificial intelligence · Fermatean fuzzy sets · Opportunity losses-based polar
coordinate distance
Received: 20 November 2024 / Accepted: 22 July 2026
© The Author(s) 2026
A Fermatean Fuzzy Opportunity Losses-Based Polar Coordinate
Distance Method for Artificial Intelligence-Enhanced Custom-Made
Print Advertisements
Elif Akagün1  · Galip Cihan Yalçın2  · Karahan Kara3,2,4  · Pınar Aytekin5  · Tuğçe Çelik6  · Vladimir Simic7,8,9 ·
Dragan Pamucar10
advertisements. Traditional advertising focuses on broad
audiences, often delivering standardized messages [ 2]. To
design advertisements more tailored to a company’s tar -
get audience, the concept of custom-made print ads has
emerged [3]. Custom-made print ads are designed to deliver
a specific message aimed at a particular target audience for
a given product or brand [ 4]. Creativity plays a key role
in these ads, aiming to capture the attention of the target
Introduction
Companies utilize advertising to increase sales, build brand
awareness, create brand image, and systematically influ -
ence consumer behavior [ 1]. Advertising, particularly in
promotional activities, plays a crucial role. In the adver -
tising industry, agencies and media organizations support
companies in designing and selecting the most appropriate

1 3
  101  Page 2 of 29
Cognitive Computation (2026) 18:101
audience and stimulate a desire to purchase, prompting
them to act. In terms of characteristics, custom-made print
ads are more niche compared to traditional advertising [ 5].
As a result, the process of designing custom-made print
ads may involve higher costs. However, because they tar -
get more specific audiences, the overall distribution of the
advertisement may also incur lower costs. Furthermore, the
personalized nature of custom-made print ads contributes
to creating advertisements that align more closely with the
strategies of the brand and product [ 6]. Technically, these
ads (given their clearer objectives) can more easily achieve
high-quality and desired messaging outcomes.
In the process of designing custom-made print ads,
advertising agencies, and consultants provide more special-
ized services to support companies. Compared to traditional
advertisement design, companies typically face higher costs
when developing digital and custom-made print ads [ 7].
This is particularly challenging for smaller businesses and
individual sellers, who may find it difficult to bear the higher
costs of developing advertisements specifically tailored to
their target audience. Moreover, limited expertise in design-
ing custom-made print advertisements can negatively affect
small-scale companies’ ability to gain a competitive advan-
tage. AI (Artificial Intelligence)-supported advertising offers
an effective solution by reducing design costs, automating
content generation, and enabling the rapid development of
personalized advertisements without requiring extensive
marketing expertise. From the perspective of Social Cog -
nitive Theory, AI-based tools also facilitate observational
learning by enabling small business owners to identify suc-
cessful advertising patterns and apply these insights to their
own campaigns [ 8]. In addition, AI-generated feedback
helps improve marketing knowledge, strengthens self-effi -
cacy in advertising decisions, and supports the refinement
of promotional strategies through repeated learning. As a
result, AI-supported advertising enables small businesses to
enhance advertising effectiveness, respond more quickly to
changing customer preferences, and compete more success-
fully with larger firms despite their limited resources.
The rapid development of technology and the increasing
use of AI have begun to significantly impact the advertising
industry [9, 10]. AI applications, particularly those involv -
ing text-to-image and image-to-image approaches for visual
design, are becoming increasingly important [ 11, 12]. The
use of AI in the advertising industry offers opportunities for
cost-effective solutions [ 13, 14]. AI applications can serve
as a viable alternative in the process of designing custom-
made print ads [ 15]. The main motivation of this research
stems from the increasing use of generative AI in adver -
tisement design and the lack of systematic approaches for
selecting the most effective advertisement from the numer -
ous alternatives generated by AI. Although AI technologies
can rapidly produce personalized custom-made print adver-
tisements, organizations still require structured decision sup-
port to identify the alternative that best satisfies advertising
objectives and target customer expectations. Accordingly,
this study presents an AI-enhanced approach that combines
generative AI with a multi-attribute group decision-making
framework to support both the creation and evaluation of
advertisement alternatives. Within this context, the design
and selection of AI-enhanced custom-made print adver -
tisements are formulated as a decision-making problem,
enabling a transparent, reliable, and evidence-based adver -
tisement selection process.
In literature, decision-making problems are often
approached using multi-criteria decision-making (MCDM)
methods [16], allowing decision-makers to select the best
alternative and rank the options [ 17]. This study adopts a
multi-attribute group decision-making (MAGDM) approach
for the design and selection of AI-enhanced custom-made
print ads. The research proposes using AI bots [ 18] for
designing custom-made print ads, and the Fermatean fuzzy
(FF)-Entropy-opportunity losses (OPLO)-based polar coor-
dinate distance (POCOD) hybrid method is developed
and recommended as a decision support system (DSS) for
selecting the best advertisement from the designed alter -
natives. FF sets are adopted because they provide greater
flexibility than traditional fuzzy sets in representing experts’
uncertainty and hesitation, thereby enabling more reliable
modeling of subjective evaluations in complex advertising
selection problems. In addition, the OPLO-POCOD method
is selected as the alternative ranking approach because it
simultaneously considers opportunity losses between alter -
natives and ideal reference points in a polar coordinate
space. This dual evaluation mechanism provides a more
comprehensive assessment than distance-based methods
relying on a single measurement perspective. In this hybrid
method, FF sets are used to determine the contribution lev -
els of decision-makers in the decision-making process. The
FF-Entropy method, extended with FF sets, is utilized to
calculate the weights of the selection criteria for custom-
made print ads. Furthermore, the FF-weighted partitioned
dual Maclaurin symmetric mean (FFWPDMSM) aggrega -
tion operator [ 19] is employed to aggregate expert evalu -
ations. The FFWPDMSM operator is selected because it
effectively captures the interrelationships among criteria
while accommodating the uncertainty and hesitation inher -
ent in experts’ linguistic assessments under the FF environ-
ment. To select the best alternative from the AI-generated
custom-made print ads, the FF-OPLO-POCOD method
[20], extended with FF sets, is applied. This hybrid method
enables more precise calculations of the importance levels
of both experts and criteria, leading to more robust results in
the ranking of alternatives.

1 3
Page 3 of 29   101
Cognitive Computation (2026) 18:101
Research Gap
Existing studies have primarily focused on the capabil -
ity of AI to generate creative advertising content, improve
personalization, and automate design processes. However,
comparatively limited attention has been paid to the sys -
tematic evaluation and selection of AI-generated advertise -
ment alternatives. In practice, organizations often generate
multiple advertisement designs using AI tools, yet selecting
the most effective alternative remains a complex decision-
making problem involving multiple evaluation criteria,
uncertainty in expert judgments, and differing stakeholder
perspectives. Consequently, there is a need for a structured
decision support framework that can objectively evaluate
AI-generated advertisements and identify the most appro -
priate alternative.
Furthermore, the existing literature has rarely integrated
Social Cognitive Theory with AI-assisted advertisement
evaluation and advanced multi-attribute group decision-
making approaches. Previous studies generally emphasize
AI as a content generation technology, while overlooking
its role as a cognitive decision-support tool that facilitates
learning, expert judgment, and adaptive decision-making.
In addition, no previous study has combined FF sets, the FF-
Entropy weighting method and the OPLO-POCOD ranking
method within a unified framework for evaluating AI-gen -
erated custom-made print advertisements. Addressing these
gaps, the present study proposes a novel FF-Entropy-OPLO-
POCOD hybrid decision support system that integrates gen-
erative AI with Social Cognitive Theory and MAGDM to
provide a systematic, reliable, and uncertainty-aware frame-
work for advertisement design and selection.
Research Aims and Contributions
The primary aim of this study is to develop a DSS for AI-
enhanced advertisement design by integrating AI technolo -
gies with a MAGDM framework. Specifically, the study
focuses on the generation of custom-made print adver -
tisements using AI bots through a text-to-image approach
and the selection of the most appropriate advertisement
from the generated alternatives using the proposed FF-
Entropy-OPLO-POCOD hybrid method. By combining
AI-assisted creative content generation with advanced deci-
sion-making techniques, the proposed framework supports
organizations in producing personalized advertisements
while enabling systematic, transparent, and reliable adver -
tisement selection.
To achieve this objective, the study develops a compre -
hensive hybrid methodology in which FF sets are employed
to represent experts’ uncertain linguistic assessments and
determine their contribution levels, while the FF-Entropy
method is used to calculate objective criterion weights.
Expert evaluations are aggregated using the FFWPDMSM
operator, which was selected because it can capture the
interrelationships and interactions among criteria while
simultaneously accommodating the uncertainty inherent in
experts’ linguistic evaluations. Unlike conventional aggre -
gation operators that typically assume criterion indepen -
dence, the FFWPDMSM operator preserves dependency
structures within criterion groups, resulting in a more real -
istic representation of complex decision-making problems.
Subsequently, the FF-OPLO-POCOD method is applied to
rank the AI-generated advertisement alternatives. The pro -
posed framework is validated through a real-world case
study involving dairy products in Türkiye, and its robust -
ness and reliability are examined through sensitivity and
comparative analyses.
This research makes several noteworthy contributions
to advertising, marketing, and decision science literature.
First, it introduces the FF-Entropy-OPLO-POCOD hybrid
method as a novel DSS for AI-enhanced advertisement
design and selection. Second, it demonstrates the practi -
cal feasibility of employing AI boots to generate custom -
ized print advertisements using a text-to-image approach,
thereby illustrating how generative AI can support creative
advertising processes. Third, the study represents the first
integration of the OPLO-POCOD method with FF sets,
extending the applicability of this ranking approach to
uncertain group decision-making environments. Fourth, the
proposed framework combines advanced fuzzy modeling,
objective weighting, expert aggregation, and alternative
ranking into a unified MAGDM methodology, providing a
comprehensive decision-making framework for advertise -
ment evaluation. Finally, the empirical case study confirms
the applicability of the proposed method in practice and
shows that it produces robust and consistent results, high -
lighting its potential to assist organizations in designing and
selecting AI-supported advertisements more effectively. The
developed framework may also be adapted to other adver -
tisement design and marketing decision problems, provid -
ing a foundation for future research on AI-assisted decision
support systems.
Research Novelty and Methodological Advantages
The novelty of this study lies in the integration of generative
AI with an advanced MCDM framework to support both the
generation and systematic selection of AI-enhanced custom-
made print advertisements. Unlike existing studies, the pro-
posed framework unifies these two processes within a DSS.
From a methodological perspective, this research presents
the first integration of the OPLO-POCOD method with FF
sets, enabling the ranking method to operate effectively in

1 3
  101  Page 4 of 29
Cognitive Computation (2026) 18:101
uncertain group decision-making environments. In addi -
tion, the proposed FF-Entropy-OPLO-POCOD hybrid
method combines FF sets, FF-Entropy, the FFWPDMSM
aggregation operator, and the FF-OPLO-POCOD ranking
approach into a comprehensive framework that simultane -
ously addresses uncertainty. The proposed approach also
offers a more comprehensive representation of uncertainty,
considers interrelationships among criteria during expert
aggregation, and evaluates alternatives by jointly incorpo -
rating opportunity losses and distances from ideal reference
points. These methodological advantages provide a robust
decision support framework for selecting AI-generated cus-
tom-made print ads and demonstrate its potential applicabil-
ity to a wide range of AI-assisted marketing and advertising
decision problems.
Organization of the Study
This paper consists of six sections. In Sect. "Literature
review", information is provided about custom-made print
ads and their design using AI enhancements. Section "Meth-
odological Framework" presents the research methodology,
which is divided into four phases, each explained in detail.
Section " Case Study: Development and Selection of AI-
Enhanced Custom-Made Print Ads Targeting Hedonistic
Consumers for a Dairy Product " focuses on the case study
application, where information about the case study is pro -
vided and the methodology of the case study implementa -
tion is described. Additionally, each phase of the research
methodology is applied step by step, and the sensitivity and
comparative tests are presented at the end of this section.
In Section "Results and Implications", the research findings
and their implications are discussed. Section " Conclusion"
serves as the conclusion, where a general assessment is
made, along with the limitations of the study and recom -
mendations for future research.
Literature Review
Generating Custom-Made Print Ads Using Artificial
Intelligence
The emergence of Web 3.0 has profoundly altered how
individuals seek and consume information tailored to their
specific preferences. Recognizing the significance of per -
sonalization, businesses have aimed to deliver more sophis-
ticated and precise information services to meet individual
needs [21]. Marketers are increasingly adopting digital tech-
nologies to reach consumers more effectively and deliver
more personalized advertising experiences [ 22, 23]. This
shift creates new opportunities to develop more innovative
and personalized advertising strategies, particularly in digi-
tal environments [24].
AI has become an integral part of everyday life and is
now widely used across many industries. In marketing, AI
supports product development, enables personalized adver-
tising, improves customer targeting, and helps identify
consumer behavior patterns. As a result, it has become an
important tool for delivering more personalized and effec -
tive marketing strategies [ 25]. The rapid growth of social
media and digital platforms has transformed how consum -
ers interact with brands, making personalized communi -
cation increasingly important. Since 2020, advances in AI
have further strengthened this trend by enabling the analy -
sis of large volumes of consumer data and supporting the
design, management, and optimization of advertising cam -
paigns. By identifying patterns in online behavior, social
media activity, and purchasing habits, AI helps marketers
better understand consumer preferences and deliver more
targeted and personalized advertisements.
By combining AI with personalized marketing strategies,
businesses can better understand customer preferences and
develop targeted offers that provide more relevant and indi-
vidualized experiences [26]. By analyzing large volumes of
customer data, AI helps companies understand consumer
preferences and provide personalized experiences at scale,
enhancing the overall customer journey [ 25]. AI also can
identify consumer behavior patterns and help marketers
deliver advertisements to the right audience at the right
time. By continuously analyzing user data, AI improves the
relevance and effectiveness of advertising campaigns, lead-
ing to higher customer engagement, improved conversion
rates, and better marketing performance [25].
Companies develop various advertising strategies to
strengthen their marketing policies [ 27]. These strate -
gies may focus on the product itself, the target audience,
or specific themes. When companies present their targeted
advertising strategies as specially designed ads, these are
referred to as custom-made print ads. This strategy involves
creating advertisements tailored specifically to individual
customers [28]. Custom-made print ads allow for the prepa-
ration of advertisements suited to the target audience, fos -
tering focused messaging. Additionally, they contribute to
strengthening brand identity by creating a lasting image and
original designs. Given their tailored nature, custom-made
print ads also play a direct role in creating a visual impact
that significantly enhances purchasing attitude [29].
The process of designing custom-made print ads differs
from traditional advertising approaches. While traditional
ad design prioritizes product promotion, custom-made
print ad design adopts a multidimensional approach. This
involves analyzing the target audience to determine their
demographic characteristics, interests, and needs [ 30].

1 3
Page 5 of 29   101
Cognitive Computation (2026) 18:101
Furthermore, to encourage call-to-action behavior among
consumers, the message must be accurately defined and
designed with a clear purpose [ 31]. Moreover, visual ele -
ments such as visual design [ 32], color contrast [ 33], the
placement of images, and text in the advertisement are
critical factors that enhance ad effectiveness [ 34]. From a
technical standpoint, the quality of the print, resolution lev-
els, and the use of specialized printing techniques are also
important.
Designing custom-made print ads requires a professional
approach. Advertising agencies are ideal professionals for
creating custom-made print ads. In computer-assisted cus -
tom-made print ad design, graphic designers play a key role.
Freelance graphic designers provide individual services to
companies, aiding in the creation of custom-made print ads,
while graphic design agencies offer professional services.
Within companies, marketing departments and teams also
contribute to the creation of custom-made print ads.
The advancement of information technology and the
growing capability of AI in generating visual materials have
opened new avenues for using AI as an ideal tool in the
design of custom-made print ads [ 35]. AI bots, particularly
those that offer text-to-image and image-to-image design
capabilities [ 11], present an alternative, cost-effective
method for companies seeking to create ads with little to no
expense. Specifically, the text-to-image approach facilitates
the design of alternative ads for well-defined custom-made
print ad campaigns, streamlining companies’ marketing
and advertising processes [ 36]. This research examines
the AI-enhanced custom-made print ad design process and
proposes the use of AI to create cost-effective ads. Addi -
tionally, it suggests that the problem of selecting the best
custom-made print ad from AI-generated alternatives can be
addressed using an MCDM approach, which supports the
decision-making process.
Developing a decision model and defining criteria within
that model is crucial for solving the custom-made print ads
selection problem. The identification of appropriate criteria
and the inclusion of expert opinions significantly improve
the selection process. Thus, the methodological approach
and DSS proposed in this study offer an alternative solution
for the design and selection of custom-made print ads.
Recent Advances in Fuzzy-Based Decision Support
Systems
DSS development increasingly relies on advanced fuzzy
environments to model uncertainty and ambiguity in com -
plex decision-making problems. Among these environ -
ments, FF sets have attracted considerable attention because
of their superior ability to represent experts’ uncertainty and
hesitation compared with conventional fuzzy extensions.
Owing to this flexibility, FF sets have been widely inte -
grated with MCDM methods to improve the reliability of
decision support algorithms.
Recent studies demonstrate the growing applicability
of FF sets across a wide range of decision-making con -
texts. For example, Seikh and Chatterjee [ 37] proposed an
FF-based hybrid framework integrating SWARA (Step -
wise Weight Assessment Ratio Analysis), the Best–Worst
Method (BWM), and VIKOR (VIšeKriterijumska Optimi -
zacija I Kompromisno Rešenje) for sustainable electronic
waste management. In the renewable energy domain, Seikh
and Chatterjee [38] employed interval-valued FF sets within
a MAGDM framework by integrating SWARA and ARAS
(Additive Ratio Assessment) to evaluate renewable energy
alternatives. Similarly, Seikh and Mukherjee [ 39] com -
bined FF sets with the CRADIS (Compromise Ranking of
Alternatives from Distance to Ideal Solution) method to
support online shopping decisions. More recently, Chat -
terjee and Seikh [ 40] developed a hybrid FF-RANCOM
(Ranking Comparison)-AROMAN (Alternative Ranking
Order Method Accounting for Two-Step Normalization)
framework for evaluating wastewater reuse alternatives in
industrial treatment systems. Likewise, Yalçın et al. [ 41]
integrated FF sets with the SIWEC (Simple Weight Calcu -
lation) and ARLON (Alternative Ranking using Two-Step
Logarithmic Normalization) methods to assess transporta -
tion performance, while Yalçın et al. [ 42] combined FF-
RANCOM with the Symmetry Point of Criterion (SPC)
method to evaluate sustainability performance. These stud -
ies collectively demonstrate that FF sets provide an effec -
tive environment for handling uncertainty in complex group
decision-making problems.
In parallel with the development of advanced fuzzy envi-
ronments, aggregation operators have become an essen -
tial component of contemporary decision support systems
because they enable the integration of multiple experts’
opinions while preserving the characteristics of uncertain
information. Recent research has highlighted the effective -
ness of aggregation operators in diverse application areas.
For instance, Abosuliman et al. [ 43] integrated aggrega -
tion operators with neural networks for nanosensor selec -
tion under fuzzy environments. Zhang et al. [ 44] employed
linguistic aggregation operators to support robotic motion
simulation, whereas Nawaz et al. [ 45] demonstrated the
usefulness of aggregation operators in improving surgi -
cal decision-making processes. These studies indicate that
appropriate aggregation mechanisms play a crucial role in
enhancing the reliability and robustness of group decision-
making models.
Beyond FF environments, numerous fuzzy extensions
have also been developed to improve decision-making
under uncertainty. These include spherical fuzzy sets [ 46],

1 3
  101  Page 6 of 29
Cognitive Computation (2026) 18:101
Pythagorean fuzzy sets [ 47], single-valued neutrosophic
sets [48], intuitionistic fuzzy sets [49], bipolar neutrosophic
sets [50], picture fuzzy sets [51, 52], q-rung orthopair fuzzy
sets [ 53], and fractional fuzzy sets [ 54]. The increasing
diversity of these fuzzy environments reflects the continu -
ous effort to develop more flexible and accurate decision
support methodologies capable of handling uncertainty in
real-world applications.
Although previous studies have demonstrated the effec -
tiveness of FF sets and aggregation operators in various
MCDM problems, their application to AI-enhanced adver -
tisement design and selection remains largely unexplored.
Existing research has primarily focused on traditional engi-
neering, sustainability, logistics, healthcare, and energy
applications, with limited attention given to advertising
decision-making supported by generative AI. Furthermore,
no previous study has integrated FF sets, the FF-Entropy
weighting method, the FFWPDMSM aggregation operator,
and the OPLO-POCOD ranking method within a unified
MAGDM framework for evaluating AI-generated custom-
made print advertisements. The present study addresses this
gap by developing a comprehensive hybrid decision support
system that combines uncertainty modeling, objective cri -
terion weighting, expert opinion aggregation, and alterna -
tive ranking to support reliable and transparent AI-assisted
advertisement selection.
Methodological Framework
The methodological framework developed in this study for
designing AI-enhanced custom-made print advertisements
and selecting the most appropriate advertisement is illus -
trated in Fig. 1. The framework consists of four sequential
phases, each addressing a specific stage of the decision-
making process.
Phase 1 focuses on AI-assisted advertisement generation.
At this stage, the product characteristics, marketing objec -
tives, and target customer profile are identified. Based on
these inputs, a detailed prompt is developed and submit -
ted to AI bots using a text-to-image approach to generate
multiple custom-made print advertisement alternatives. The
outcome of this phase is a set of AI-generated advertise -
ments that constitute the decision alternatives.
Phase 2 establishes the decision-making framework for
advertisement evaluation. The generated advertisements are
defined as the alternatives, the evaluation criteria are identi-
fied through an extensive literature review and expert con -
sultation, and the expert panel responsible for the assessment
process is determined. This phase provides the foundation
for the subsequent multi-attribute group decision-making
analysis.
Phase 3 involves the development and implementation
of the proposed FF-Entropy-OPLO-POCOD hybrid deci -
sion support system. First, FF sets are employed to repre -
sent experts’ linguistic assessments and determine their
contribution levels. The FF-Entropy method is then applied
to calculate the objective weights of the evaluation crite -
ria, while the FFWPDMSM operator aggregates individual
expert judgments into a collective decision matrix. Finally,
the FF-OPLO-POCOD method is used to evaluate and rank
the AI-generated advertisement alternatives.
Phase 4 is dedicated to validating the proposed method -
ology. Sensitivity analyses are conducted under different
scenarios to examine the stability of the ranking results,
while comparative analyses with established MCDM meth-
ods are performed to evaluate the consistency and reliability
of the proposed hybrid framework. These analyses verify
the robustness of the developed decision support system and
demonstrate its practical applicability in AI-assisted adver -
tisement selection.
Phase 1: Creating AI-Enhanced Custom-Made Print
Ads
Recent advancements in AI and machine learning have
enabled the development of sophisticated generative AI
techniques and systems capable of producing text, code,
images, and other media in response to user inputs [ 55].
The primary goal of visualization is to present information
in a clear, meaningful, and actionable way. Achieving this
requires collaboration among domain experts, designers,
Fig. 1 Methodological framework

1 3
Page 7 of 29   101
Cognitive Computation (2026) 18:101
and developers to create visual solutions that effectively
meet user needs, support decision-making, and fit the
intended context.
AI technologies have rapidly emerged as one of the most
disruptive and transformative innovations of our time. AI
refers to a suite of algorithms capable of producing con -
tent such as text, images, etc. within existing datasets [ 56].
This technology replicates creative processes traditionally
undertaken by humans, shifting AI’s role from an enabler
to a highly efficient co-creator. Tools like ChatGPT, Gem -
ini, DALL-E, Midjourney, and AlphaCode have driven
exponential growth in user adoption. However, generative
AI’s potential to transform knowledge work is even more
profound. AI is rapidly being embedded into software plat -
forms, influencing how companies across industries develop
products, deliver services, and create value [57].
Generative AI models excel in processing text, produc -
ing human-like responses, and generating realistic images.
The use of AI in creating and assembling visualizations has
a well-established history. Many recommendation systems
have been developed to assist creators in selecting visu -
als, either through rule-based approaches (typically task-
oriented) or machine learning techniques [ 55]. AI is also
increasingly permeating professional domains, streamlining
and automating tasks [58].
Text-to-image AI systems have become invaluable in
design, enabling the creation of original visual content
based on natural language descriptions [ 59]. These sys -
tems also provide layout recommendations that improve the
consistency between text prompts and generated images.
As a result, they simplify the design process and help pro -
duce more coherent and visually appealing advertisements
[60]. Furthermore, text-to-image AI enables designers to
generate personalized visual content directly from natural
language prompts. This capability supports creativity, accel-
erates the design process, and helps produce advertisements
that closely reflect the intended concepts and target audi -
ence [61]. The integration of AI systems into design prac -
tices creates new opportunities for innovation and creative
expression. Text-to-image platforms are increasingly used
in advertising to generate visual content and promotional
designs. As these technologies continue to advance, their
role in developing custom-made print advertisements is
expected to expand, transforming the future of advertising
design [62].
Companies can produce custom-made print ads, one of
the parameters shaping their advertising policies, using AI-
enhanced methods, differing from the traditional production
process. In this study, keywords were generated to define the
target customer portfolio for a dairy brand that a company
intends to launch. The prompt to be given to the AI for the
design of custom-made print ads was prepared descriptively
based on these keywords. The prepared prompt was input
into the selected AI interfaces, and the production process
was repeated multiple times. Different results were obtained
with each iteration. This method demonstrates that custom-
made print ads for various products can also be produced
using an AI-based approach.
Phase 2: Developing a Decision Model for AI-
Enhanced Custom-Made Print Ads
At this phase, the decision model structure is established for
the AI-enhanced custom-made print ads selection process.
Three key elements are identified in the decision model:
experts, criteria, and AI-enhanced ads. Experts are selected
from those with expertise and experience in marketing and
advertising, with a particular emphasis on their ability to
evaluate ads based on the defined selection criteria. Dur -
ing the criteria determination process, factors that directly
influence ad selection are identified, and their impact on the
selection process is explained and defined. To define the ad
alternatives, the text prompts to be input into AI bots are first
determined. These text inputs are converted into images,
resulting in various ad designs. This process is carried out
using different AI bots. Subsequently, alternative ads, along
with expert opinions, are incorporated into the decision
model. Once the decision model is created, data is collected
for the implementation of the FF-Entropy-OPLO-POCOD
hybrid method, and the application steps are initiated.
Phase 3: Developing a Hybrid Model for AI-
Enhanced Custom-Made Print Ads
At this phase, the FF-Entropy-OPLO-POCOD hybrid
method is developed and presented to address the AI-
enhanced custom-made print ads selection problem. First,
the preliminaries for FF set operations are explained. Then,
the steps of the FF-Entropy-OPLO-POCOD hybrid method
are outlined sequentially.
Fermatean Fuzzy Sets
Definition 1. An FF sets ~J defined over a non-empty set K can
be expressed as follows: ~J =
{
⟨k,δ ~J (k) ,β ~J (k) |k ∈ K⟩
}
,
where δ~J (k): K → [0,1] ,β ~J (k): K → [0,1] , andγ~J (k)=
3
√
1 −
{
δ~J (k)
)3
−
{
β~J (k)
)3
. These represent the
concepts of MD, NMD, and indeterminacy, respec -
tively [ 63]. These are explained with the limitation
that0 ≤
{
δ~J (k)
)3
+
{
β~J (k)
)3
≤ 1. Herein, it holds true

1 3
  101  Page 8 of 29
Cognitive Computation (2026) 18:101
for all elements k in the set K. In this paper, it is called FF
numbers for elements of the FF sets.
Definition 2. An empirical application illustrating the
use of FF sets based on the proposed procedures [ 64]:
Let ~J =
{
δ~J (k) ,β ~J (k)
)
, ~J1 =
{
δ~J1 (k) ,β ~J1 (k)
)
, and
~J2 =
{
δ~J2 (k) ,β ~J2 (k)
)
 are three FF numbers. The opera -
tions are as follows:
(i)
~J1 ⊕ ~J2
=





3
√{
δ~J1 (k)
)3
+
{
δ~J2 (k)
)3
−
{
δ~J1 (k)
)3{
δ~J2 (k)
)3 ,β ~J1 (k) β~J2 (k)

)( |k ∈ K
)
(
 ,

(ii)
~J1 ⊗ ~J2
=




δ~J1 (k) δ~J2 (k) , 3
/√ad]cal√p/√ad]calv~√√~x/√ad]calv~√√~x/√ad]calv~√√~x√ { β~J1 (k) )3 + { β~J2 (k) )3
−
{
β~J1 (k)
)3{
β~J2 (k)
)3
(
)( |k ∈ K


 ,

(iii)
ψ~J =



 3
√
1 −
{
1 −
{
δ~J (k)
)3)ψ
,
{
β~J (k)
)ψ

) |k ∈ K
(
)
( forψ> 0,

(iv)
~Jψ =




{
δ~J (k)
)ψ
,
3
√
1 −
{
1 −
{
β~J (k)
)3)ψ

) |k ∈ K
(
)
( forψ> 0.

s
{
~J
)
 and a
{
~J
)
 for ~Ji(i = 1,2), the following ordering
relationship can be established [63]:
(i) If s
{
~J1
)
 > s
{
~J2
)
, then ~J1 > ~J2,
(ii) If s
{
~J1
)
 = s
{
~J2
)
, a
{
~J1
)
 > a
{
~J2
)
, then ~J1>~J2,
(iii) If s
{
~J1
)
 = s
{
~J2
)
, a
{
~J1
)
 = a
{
~J2
)
, then ~J1=~J2.
Definition 5. Let ~Jt =
{
δ~Jt (k) ,β ~Jt (k)
)
 represent a family
of FF numbers, the FFWPDMSM is defined by Eq. (3) [19]:
FFWPD MSM (l)
{
~J1, ~J2,..., ~JT
)
= 1 c

⊕c t=1

 ⊗ 1≤k1 ≤···≤kl≤ot (⊕l t=1(ϖkt Jkt ))
1
(Clot )
l



 =

 3
/√ad]cal√p/√ad]calv~√√~x/√ad]calv~√√~x/√ad]calv~√√~x√1 −  )c t=1 ( 1 − ) 1≤k1≤···≤kl ≤ot ) 1 − )l t=1 ) 1 − { δ~Jt (k) )3(ϖkt ( 1 (Clot ) ) 1 l   1 c   ,



 )c t=1

 3
√
1 − ) 1≤k1≤···≤kl ≤ot
)
1 −
{)l
t=1
{
β~Jt (k)
)ϖkt )3( 1 (Clot )   1 l   1 c   .
 (3)
Herein, l = 1,2,...,o t; t =1 , 2,...,c , c represents the
number of partitions, ot represents the number of ele -
ments in a group, Cl ot  represents the binomial coefficient as
Cl ot = ot! l!(ot−l)! , kl represents all the l-tuple combination of
ot, and ϖkt  represents the weight of kt (t = 1,2, 3 ...,l ).
Definition 2 is expected to satisfy the following criteria:
(i) ~J1 ⊕ ~J2 = ~J2 ⊕ ~J1,
(ii) ~J1 ⊗ ~J2 = ~J2 ⊗ ~J1,
(iii) ψ
{
~J1 ⊕ ~J2
)
= ψ~J1 ⊕ ψ~J2forψ> 0,
(iv)
{
~J1 ⊗ ~J2
)ψ
= ~Jψ 1 ⊗ ~Jψ 2 forψ > 0,
(v) ψ1~J ⊕ ψ2~J =( ψ1 + ψ2) ~Jforψ1,ψ 2 > 0,
(vi) ~Jψ1 ⊗ ~Jψ2 = ~J(ψ1+ψ2)forψ1,ψ 2 > 0.
Definition 3. Let ~J =
{
δ~J (k) ,β ~J (k)
)
 be an FF set over the
universe K, with the score function (Eq. (1)) and the accu -
racy function (Eq. (2)) [63], [65]:
s
{
~J
)
= 1 2 { 1+ { δ~J (k) )3 − { β~J (k) )3) ; s { ~J ) ∈ [0,1] ,  (1)
a
{
~J
)
=
{
δ~J (k)
)3
+
{
β~J (k)
)3
; a
{
~J
)
∈ [0,1] . (2)
Definition 4. Let ~J1 =
{
δ~J1 (k) ,β ~J1 (k)
)
 and
~J2 =
{
δ~J2 (k) ,β ~J2 (k)
)
 be two FF sets in the universe K.
Considering the score and accuracy functions denoted as

1 3
Page 9 of 29   101
Cognitive Computation (2026) 18:101
Novel FF-Entropy-OPLO-POCOD Hybrid Method Based on
the FFWPDMSM Aggregation Operator
The FF-Entropy-OPLO-POCOD hybrid method has been
created to assist in the selection of custom-made print ads.
Let (Bi)= {B1, B2,..., BI }, where (i = 1,2,..., I) ,
represent the alternatives,
(
Cj
)
= {C1, C2,..., CJ },
where
(
j = 1,2,..., J
)
, represent the criteria,
(Dk)= {D1, D2,..., DK}, where (k = 1,2,..., K) ,
indicate the experts participating in the decision-making
process. The notations employed in the FF-Entropy-OPLO-
POCOD hybrid method are presented in the Appendix (also
shown abbreviations). The proposed hybrid method con -
sists of three stages: expert weighting using FF sets, crite -
rion weighting through FF-Entropy, and alternative ranking
using FF-OPLO-POCOD. The overall procedure is pre -
sented in Fig. 2.
The steps of the FF-Entropy-OPLO-POCOD hybrid
method are outlined as follows:
Stage 1: Determining the weights for each expert utiliz -
ing FF sets.
Step 1–1: In the first step of Stage 1, information regard-
ing the experts’ qualifications and experience is collected
to determine their expertise levels. Based on the expertise
assessment scale presented in Table 1, the experts’ expertise
levels are expressed using FF numbers. During this process,
expert assessments are represented through predefined lin -
guistic terms.
Step 1–2: To determine the experts’ weight vector, the FF
numbers are transformed into crisp values. For this purpose,
the score function
{
s
{
~Dk
))
 is applied to convert (Eq. (4))
the FF numbers into quantitative values suitable for subse -
quent calculations:
s
{
~Dk
)
= 1 2 { 1+ { δ ~Dk (k) )3 − { β ~Dk (k) )3) ; { k = 1K ) . (4)
Steps 1–3: To obtain the experts’ weight vector, the crisp val-
ues are standardized (Eq. (5)) within the interval ([0,1]). In this
step, a linear normalization approach is employed to calculate
the normalized weights (ϖ =[ ϖk]K), which are subsequently
used in the following stages of the proposed methodology:
ϖk =
s
{
~Dk
)
∑K
k=1 s
{
~Dk
) ; { k = 1K ) . (5)
Stage 2: Determining the weights for each criterion using
FF-Entropy.
Step 2–1: In the first step of Stage 2, individual evalu -
ation matrices are constructed based on the assessments
obtained during face-to-face interviews with the experts
(Dk). The experts evaluate each advertisement alterna -
tive (Bi) with respect to the predefined selection crite -
ria
(
Cj
)
, and their judgments are systematically recorded.
The scale presented in Table 2 is used throughout this
assessment process
{
~E(Dk) = [ ~E(Dk) ij ] IxJ )  where
~E(Dk) ij =
{
δ~E(Dk) ij (k) ,β ~E(Dk) ij (k)
)
{
i =1 ,..., I; j =1 ,..., J ; k =1 ,..., K
):
Step 2–2:  The individual evaluation matrices are
aggregated using the FFWPDMSM aggregation operator
(Eq. (6)), taking the experts’ weight vector into account. As
a result, an aggregated decision matrix
{
~E =
[
~Eij
]
IxJ
)

expressed in FF numbers is obtained, which serves as
the initial decision matrix for the subsequent FF-Entropy
weighting process:
FFWPD MSM (l)
{
~E1, ~E2,..., ~EK
)
= 1 c

⊕c t=1

 ⊗ 1≤k1≤···≤kl ≤ot
{
⊕l k=1
{
ϖk ~Ek
)) 1 clot
l



 =

 3
/√ad]cal√p)))(1 −  )c t=1 ( 1 − ) 1≤k1≤···≤kl ≤ot { 1 − )l k=1 { 1 − { δ~Ek (k) )3)ϖk ) 1 clot ) 1 l   1 c   ,



 )c t=1

 3
⏐
1 − ) 1≤k1≤···≤kl ≤ot
{
1 −
{)l
t=1
{
β~Ek (k)
)ϖk )3) 1 clot


1
l


1
c

 ,
 (6)
herein, l = 1,2,...,o t; t =1 , 2,...,c , while c represents
the number of partitions, ot represents the number of ele -
ments in a group, Cl ot  represents the binomial coefficient as
Cl ot = ot! l!(ot−l)! , kl represents all the l-tuple combination of
ot, ϖk represents the weight of k =( 1,2, 3 ...,l ).
Step 2–3:  In this step, the aggregated FF numbers are
transformed (Eq. (7)) into crisp values using the score func-
tion
{
s
{
~Eij
))
. This transformation converts the decision
matrix from the Fermatean fuzzy environment into a crisp
form
(
E =
[
Eij
]
IxJ
)
, enabling the subsequent objective
weighting calculations:
Eij = s
{
~Eij
)
= 1 2 { 1+ { δ~Eij (k) )3 − { β~Eij (k) )3) ; { j = 1J ; i = 1I ) . (7)
Step 2–4:  In this step, the crisp decision matrix is nor -
malized (Eq. (8)) to transform all values into the interval
([0,1]), thereby ensuring comparability among the evalua -
tion criteria prior to the entropy-based weighting process (
F =
[
Fij
]
IxJ
)
:
Fij = Eij∑I
i=1 Eij
;
(
j = 1J ; i = 1I
)
. (8)

1 3
  101  Page 10 of 29
Cognitive Computation (2026) 18:101
Fig. 2 FF-Entropy-OPLO-POCOD hybrid method

1 3
Page 11 of 29   101
Cognitive Computation (2026) 18:101
Step 2–5: In this step, the entropy values
of the evaluation criteria are calculated (Eq. (9)) to measure
the amount of information and uncertainty associated with
each criterion. Herein, α =( ln (I))−1:
 (9)
Step 2–6:  The degree of differentiation for each criterion (
H =
[
Hj
]
J
)
 is calculated (Eq. (10)) based on the entropy
values, reflecting the discriminating power and informa -
tional contribution of each criterion to the decision-making
process:
 (10)
Step 2–7: The normalized criterion weights
(
w =
[
wj
]
J
)

are determined (Eq. (11)) based on the calculated degrees of
differentiation:
wj = Hj∑J
j=1 Hj
;
(
j = 1J ; i = 1I
)
. (11)
Stage 3: Establishing the rankings of alternatives through
the application of the FF-OPLO-POCOD method:
Step 3–1:  In the first step of Stage 3, the best (ideal)
values for each criterion
(
L =
[
Lj
]
J
)
 are identified
(Eq. (12)). These values serve as the reference points for the
subsequent calculations in the FF-OPLO-POCOD ranking
procedure:
Lj =
{ maxi ( Eij ) f or j ∈C +
mini
(
Eij
)
f or j ∈C − ;
(
j = 1J ; i = 1I
)
. (12)
Step 3–2: The loss values
(
M =
[
Mij
]
IxJ
)
 for each alter-
native are determined (Eq. (13)) by measuring the deviation
of their performance from the corresponding best (ideal)
values for each criterion:
Mij =
⏐⏐Eij −L j ⏐⏐ ; { j = 1J ; i = 1I ) . (13)
Step 3–3:  The ordered pair values
(
N =
[
Nij
]
IxJ
)
 are
constructed (Eq. (14)) by combining the best (ideal) values
and the corresponding loss values for each criterion:
Nij =
(
Eij, Mij
)
;
(
j = 1J ; i = 1I
)
. (14)
Step 3–4: The best ordered pair values
(
O =
[
Oj
]
J
)
 are
identified (Eq. (15)) to establish the ideal reference points
for each criterion:
Oj =



((
maxi
(
Eij
))
,
(
mini
(
Mij
)))
f or j ∈C +
((
mini
(
Eij
))
,
(
mini
(
Mij
)))
f or j ∈C − ;
(
j = 1J ; i = 1I
)
. (15)
Step 3–5:  The distance values
(
P =
[
Pij
]
IxJ
)
 between
each alternative and the corresponding best ordered pair
values are calculated (Eq. (16)) to measure the relative per-
formance of the alternatives:
Pij =



√(
Eij −
(
maxi
(
Eij
)))2
+
(
Mij −
(
mini
(
Mij
)))2
f or j ∈C +
√(
Eij −
(
mini
(
Eij
)))2
+
(
Mij − mini
(
Mij
))2
f or j ∈C −
;
(
j = 1J ; i = 1I
)
. (16)
Step 3–6:  The distance values
(
Q =
[
Qij
]
IxJ
)
 are
weighted (Eq. (17)) using the criterion weight vector:
Qij = wjPij;
(
j = 1J ; i = 1I
)
. (17)
Step 3–7:  The weighted distance values are aggregated
(Eq. (18)) to obtain the total distance value (R =[ Ri]I ) for
each advertisement alternative:
Ri =
J∑
j=1
Qij;
(
j = 1J ; i = 1I
)
. (18)
Step 3–8: The degree of opportunity loss values (S =[ Si]I )
are calculated (Eq. (19)) for each advertisement alternative
to quantify the overall performance loss relative to the ideal
solution:
Table 1 Expert assessments scale [66]
Expertise (level of proficiency) FF sets
“Very-poor (VP)” (0.21, 0.70)
“Poor (P)” (0.36, 0.41)
“Medium (M)” (0.42, 0.52)
“Good (G)” (0.73, 0.10)
“Very-good (VG)” (0.82, 0.50)
Table 2 Alternative assessments scale [66]
Linguistic variables FF sets
“Exceptionally low (ExL)” (0.30, 0.50)
“Extremely low (EL)” (0.35, 0.43)
“Very low (VL)” (0.36, 0.56)
“Low (L)” (0.40, 0.73)
“Below average (BA)” (0.42, 0.30)
“Average (A)” (0.47, 0.21)
“Above average (AA)” (0.50, 0.62)
“High (H)” (0.55, 0.38)
“Very high (VH)” (0.60, 0.18)
“Extremely high (EH)” (0.72, 0.50)
“Exceptionally high (ExH)” (0.83, 0.42)

1 3
  101  Page 12 of 29
Cognitive Computation (2026) 18:101
Si = Ri ∑I
i=1 Ri
;
(
j = 1J ; i = 1I
)
. (19)
Step 3–9: The percentage of opportunity achievement val -
ues (T =[ Ti]I ) are calculated (Eq. (20)) for all advertise -
ment alternatives. Based on these values, the alternatives
are ranked, and the advertisement with the highest percent -
age of opportunity achievement is identified as the optimal
AI-enhanced custom-made print advertisement:
Ti =1 −S i;
(
j = 1J ; i = 1I
)
. (20)
The algorithmic steps of the FF-Entropy-OPLO-POCOD
hybrid model are outlined in Table S.1 in Supplementary
Materials.
Phase 4: Robustness and Consistency Tests
Sensitivity analyses are scenario-based, where the method
is reapplied according to the prepared scenarios, and the
results are compared with the original outcomes to evaluate
the reliability of the findings. To further evaluate the con -
sistency of the FF-Entropy-OPLO-POCOD hybrid model,
different methods are employed for comparativeness. The
differences and similarities in the rankings of alternatives
are observed to form conclusions regarding the model’s
reliability.
Case Study: Development and Selection
of AI-Enhanced Custom-Made Print Ads
Targeting Hedonistic Consumers for a Dairy
Product
In this paper, the problem of designing AI-enhanced cus -
tom-made print ads for a dairy product in Türkiye and
selecting the best advertisement is addressed. The dairy
company aims to create advertisements to market its dairy
products and wishes to identify the most effective ad. The
target audience of the dairy company consists of hedonic
consumers, who are more likely to make purchase deci -
sions based on enjoyment rather than only on functional
product features. Therefore, the ads prompts were prepared
to reflect these preferences by emphasizing emotional
appeal, attractive visuals, and enjoyable consumption expe-
riences. To capture the attention of this customer segment
and increase sales, the company seeks to prepare advertise-
ments at minimal cost while determining the best adver -
tisement. This case study is created, and the four phases
of the methodology presented in this paper are applied and
explained sequentially.
Application Phase 1: Creating AI-Enhanced Custom-
Made Print Ads for a Dairy Product
In the creation of AI-enhanced custom-made print ads, text-
to-image technology was utilized through various AI plat -
forms. The selected AI tools include Microsoft Copilot AI,
Leonardo AI, Stable Diffusion AI, and ImagineArt AI, all of
which support high-quality text-to-image generation. These
platforms were selected because of their widespread use,
accessibility, ease of use, and ability to generate diverse and
customizable visual content suitable for advertising appli -
cations. Compared with many other AI image-generation
tools, they offer a practical balance between image quality,
prompt responsiveness, and creative flexibility. Visual out -
puts were generated by submitting identical prompts to each
platform. Although the same prompts were used, each AI
tool produced distinct advertisement designs, providing a
diverse set of alternatives for the subsequent multi-attribute
group decision-making process. This characteristic suggests
that these AI-enhanced tools not only offer the potential to
generate a wide range of design options but also possess
creative capabilities that can enhance the personalization of
advertisements.
Prior to generating the advertisements, the prompt was
systematically developed to ensure consistency across all AI
platforms. The prompt preparation process involved defining
the product category, identifying the target customer profile,
and specifying the desired advertising message and visual
characteristics. These elements were integrated into a single
standardized prompt to ensure that all AI tools generated
advertisements under identical input conditions, thereby
enabling a fair and consistent comparison of the resulting
alternatives. In the case study of this research, the identified
characteristics were employed to describe the custom-made
print ads intended for AI-enhanced production, resulting in
the preparation of the following prompt: “A custom-made
print ads for a milk product that is aimed at customers
who are pleasure-oriented, shop with their emotions and
are satisfied with it, enjoy consumption and shopping, are
interested, curious, care about emotional experiences, tend
towards products or brands that can provide entertainment,
pleasure, enjoyment, fantasy, and dream creation, reward
themselves with the products they buy, and tend to consume
for conspicuous purposes.”.
The qualities of the distinct visual outputs generated
autonomously differ based on the skills and capabilities
of the employed AI interfaces. When visually successful
results were achieved, further alternatives were developed.
Although identical text prompts were used, different AI
tools produced results characterized by diverse styles. This
variation extended beyond mere stylistic differences; it was

1 3
Page 13 of 29   101
Cognitive Computation (2026) 18:101
also evident in the skill and expertise exhibited in the design
of the visual products.
Application Phase 2: Developing a Decision Model
for AI-Enhanced Custom-Made Print Ads for a Dairy
Product
Identification of Experts
To apply the proposed FF-Entropy-OPLO-POCOD hybrid
method for selecting AI-enhanced custom-made print adver-
tisements, the components of the decision model must first
be clearly defined. Among these components, the expert
panel plays a pivotal role, as the quality and reliability of the
decision-making process largely depends on expert knowl -
edge and experience. Therefore, the expert group was inten-
tionally composed of both academics and practitioners with
substantial expertise in marketing, advertising, and brand
management to ensure a balanced evaluation from theoreti-
cal and practical perspectives.
For this application, nine experts participated in the
evaluation process. The first two experts are professors
specializing in marketing, each with more than twenty
years of academic and research experience. The remaining
seven experts hold managerial positions in the marketing
and advertising industry. Specifically, the third expert is an
advertising and public relations manager with 13 years of
experience, the fourth is a brand and marketing communica-
tion manager with seven years of experience, the fifth is a
marketing coordinator with 10 years of experience, the sixth
is an executive creative director with 20 years of experi -
ence, the seventh is a marketing manager with nine years
of experience, the eighth is an advertising director with five
years of experience, and the ninth is a marketing specialist
with five years of experience. The profiles of all experts are
summarized in Table 3.
The expert evaluation process was conducted individu -
ally to avoid potential bias arising from group influence
or dominant opinions. Each expert was provided with the
AI-generated advertisement alternatives, the evaluation
criteria, and detailed assessment instructions. The experts
independently assessed each advertisement using the pre -
defined linguistic evaluation scale based on FF sets. After
the individual evaluations were completed, the collected
assessments were converted into FF numbers and subse -
quently aggregated using the FFWPDMSM operator to con-
struct the collective decision matrix for the proposed hybrid
decision support system. This procedure ensured consis -
tency, preserved the independence of expert judgments, and
enabled the integration of diverse professional perspectives
into the final decision-making process.
Criteria Set
Twelve criteria have been identified for determining the best
advertisement among the AI-enhanced Custom-Made Print
Ads alternatives. These criteria serve as reference points
for experts when evaluating advertisements. The criteria
included in the decision model are as follows:
 ● Level of visual appeal (C1) − The visual element is one
of several components, such as the logo, body copy, and
headline, that together form an advertisement [ 67]. To
capture consumer attention, a print advertisement must
possess features that make it visually appealing. Among
these attributes, visual appeal plays a critical role [ 68].
The visual appeal of an advertisement significantly in -
fluences its ability to attract and engage the target audi -
ence. If an advertisement fails to capture attention, po -
tential customers may be lost. Therefore, it is essential
that the ad immediately captures consumer attention and
raises awareness of the products being promoted [ 69].
Within the scope of this research, “level of visual ap -
peal” has been identified as a key criterion for evaluat -
ing “AI-enhanced custom-made print advertisements”.
 ● Level of generating interest  (C2) − When designing a
poster, marketers must carefully consider the informa -
tion to include to effectively convey the product’s ben -
efits after capturing the consumer’s attention. Consum -
ers are typically willing to invest time in reading the
advertising message in detail or examining the poster.
If marketers can demonstrate that the product addresses
a particular problem and clearly explain its features and
benefits, they can successfully generate interest among
the target audience [ 70], [ 71]. Accordingly, the “level
of generating interest” has been selected as one of the
evaluation criteria in this research.
Table 3 The group of experts
Experts Significance level Professions
D1 V ery Good (VG) Professor specializing in
marketing and advertising
D2 V ery Good (VG) Professor specializing in
marketing communications
D3 Good (G) Advertising and public rela-
tions manager
D4 Medium (M) Brand & marketing commu-
nication—senior specialist
D5 Good (G) Marketing coordinator
D6 V ery Good (VG) Executive creative director
D7 Good (G) Marketing manager
D8 Medium (M) Advertising director
D9 Medium (M) Marketing specialist

1 3
  101  Page 14 of 29
Cognitive Computation (2026) 18:101
 ● Level of purchase desire generation  (C3) − One of the
primary objectives of advertising is to encourage con -
sumers to purchase a product by communicating its val-
ue in a compelling and persuasive manner. Effective ad-
vertisements should capture consumers’ attention, create
emotional engagement, and strengthen their intention to
buy [70, 72]. When an advertisement successfully ad -
dresses consumers’ needs and expectations, it increases
their motivation to choose the advertised product [ 71].
For this reason, the level of purchase desire generation
was identified as one of the key evaluation criteria in
this study.
 ● Level of call to action (C4) − An effective advertisement
should encourage consumers to act by increasing their
willingness to purchase the advertised product or ser -
vice. Even when an immediate purchase does not occur,
a persuasive advertisement can positively influence con-
sumers’ decision-making process and strengthen their
future purchase intentions [ 73]. Ads that create emo -
tional engagement are particularly effective in motivat -
ing consumer action [31]. Therefore, the level of call to
action was included as one of the key evaluation criteria
in this study.
 ● Degree of product-visual compatibility (C5) − This cri-
terion reflects the level of successful alignment between
the visual elements used in the advertisement and the
product itself. In product-visual compatibility, the ad -
equacy of the advertisement’s visuals is crucial to ensure
that the message conveyed to the target audience is com-
municated effectively [ 74]. Therefore, product-visual
compatibility plays a critical role in the evaluation pro -
cess of advertisements. In this context, this criterion is
included in the decision-making model.
 ● Level of target audience compatibility  (C6) − The pro-
cess of creating custom-made print ads involves ensur -
ing that the designed advertisements convey a specific
message tailored to a particular target demographic [75].
Thus, the demographic, social, and cultural alignment
of the advertisement with the target audience is of para-
mount importance. Therefore, this criterion is included
in the decision-making model during the evaluation pro-
cess of the advertisements.
 ● Level of purpose reflectiveness (C7) − This criterion in-
dicates the extent to which the advertisement reflects its
intended purpose. In the context of custom-made print
ads, each advertisement is designed with a specific ob -
jective in mind [2]. Therefore, it is essential for the ad -
vertisement to align with this purpose throughout its de-
sign. Consequently, the level of purpose reflectiveness
is regarded as a critical evaluation criterion. The criteria
included in the decision model are assessed by experts,
considering the relationship between the advertisement
and its intended purpose.
 ● Level of clarity/comprehensibility of image and mes -
sage (C8) − Considering the multitude of elements
across various modalities, the process of poster creation
can pose significant challenges, encompassing funda -
mental aspects and requirements. One such require -
ment is the generation of concise and structured taglines
based on product information, which is essential for the
efficient transmission of messages to consumers [76].
 ● Level of creativity  (C9) − To create an effective and
visually appealing poster, all design elements should
work together in a consistent and harmonious manner.
Achieving this balance often requires considerable time,
creativity, and expertise in design, particularly when de-
veloping advertisements for different products and for -
mats [76].
 ● Level of typography suitability (C10) − Visual commu-
nication design, predominantly rooted in typography,
constitutes a significant public art form [77]. Within this
framework, “AI-enhanced custom-made print advertise-
ments” is also regarded as a product of art and visual
communication design, and in this context, “level of
typography suitability” has been selected as one of the
evaluation criteria.
 ● Level of color incompatibility  (C11) − The ability of
humans to discern images strongly indicates that color
compatibility is a factor for realistic image composition.
By effectively managing color compatibility, it is pos -
sible to enhance the realism of an image composite [78].
In this context, “level of color incompatibility” has been
established as a cost-based criterion.
 ● Level of ethical concerns  (C12) − Ethics emerges as a
fundamental value within any society [ 79]. Businesses
operating within a society are expected to align their
practices with the ethical values and norms of that social
environment. Thus, ethical conduct has evolved into a
central strategic focus for many organizations in articu -
lating and advancing their brand values [80, 81]. Indeed,
ethical principles significantly shape a firm’s services, as
well as its relationships with society [82]. This criterion
is also identified as a cost type in this model.
Identification of AI-Enhanced Custom-Made Print Ads for
Dairy Products
Custom-made print ads were designed using various AI sys-
tems, including Microsoft Copilot AI, Leonardo AI, Stable
Diffusion AI, and ImagineArt AI, for a company specializ -
ing in dairy production. The details regarding these AI sys -
tems are as follows:

1 3
Page 15 of 29   101
Cognitive Computation (2026) 18:101
 ● Microsoft Copilot AI  is an AI-powered image genera -
tion tool developed by Microsoft that utilizes DALL·E
3 technology to create images from text prompts. By
interpreting users’ textual descriptions, it generates mul-
tiple visual alternatives that closely match the intended
concepts. Its ability to produce high-quality and detailed
images, particularly when provided with well-structured
prompts, makes it a suitable tool for creating AI-en -
hanced advertisement designs. The first seven alterna -
tive custom-made print ads (from B1 to B7) presented in
Fig. 3 were designed using Microsoft Copilot AI.
 ● Leonardo AI is a generative AI platform designed for
creating high-quality visual content from text prompts.
It enables users to produce detailed images suitable for
creative applications such as graphic design, digital art,
and advertising. Its capability to generate visually rich
and customizable outputs makes it well suited for de -
veloping AI-enhanced advertisement alternatives. The
8th alternative custom-made print ads (B8) presented in
Fig. 3 were designed using Leonardo AI.
 ● Stable Diffusion AI is an open-source generative AI mod-
el that creates high-quality images from text prompts. It
is widely recognized for its flexibility, customization ca-
pabilities, and ability to generate diverse visual outputs
from the same prompt. These features make it an effec -
tive tool for producing alternative advertisement designs
with varying creative styles. The 9th and 10th alterna -
tive custom-made print ads ( B9 and B10) presented in
Fig. 3 were designed using Stable Diffusion AI.
 ● Like other AI-powered tools in the realm of text-to-im -
age generation, ImagineArt AI leverages machine learn-
ing techniques to transform user inputs into creative and
realistic visual outputs. It caters primarily to artists, de -
signers, and content creators seeking to streamline their
creative process or explore new artistic possibilities us -
ing AI technology. The 11th and 12th alternative cus -
tom-made print ads (B11, B12) presented in Fig. 3 were
designed using ImagineArt AI.
Application Phase 3: Application of the FF-Entropy-
OPLO-POCOD Hybrid Method
In this case study, the development and selection of AI-
enhanced custom-made print advertisements for a dairy
product are examined. The primary objective is to dem -
onstrate the practical implementation of the proposed FF-
Entropy-OPLO-POCOD hybrid method for identifying the
most effective advertisement among AI-generated custom-
made print advertisement alternatives. As described in the
previous section, the decision-making model consists of
nine experts, twelve evaluation criteria, and twelve adver -
tisement alternatives. Based on the data collected through
Table 4 The matrix of expert weights
Experts D1 D2 D3 D4 D5 D6 D7 D8 D9
ϖk 0.1269 0.1269 0.1234 0.0830 0.1234 0.1269 0.1234 0.0830 0.0830
Ads-1( ) Ads-2( ) Ads-3( )A ds-4 ( ) Ads-5( )
Ads-6( ) Ads-7( ) Ads-8( )A ds-9 ( ) Ads-10 ( )
Ads-11 ( ) Ads-12 ( )
Fig. 3 AI-enhanced custom-made
print ads

1 3
  101  Page 16 of 29
Cognitive Computation (2026) 18:101
face-to-face interviews with the experts, the stages of the
proposed FF-Entropy-OPLO-POCOD hybrid method were
implemented sequentially as follows.
Stage 1 (Application): Determining the weights for each
expert utilizing FF sets: Stage 1 consists of three sequential
steps designed to determine the experts’ weights and their
contribution levels to the decision-making process. In Step
1–1, the experts qualified to evaluate the custom-made print
advertisements were assessed (Table S.2) using the exper -
tise assessment scale presented in Table 1. In Step 1–2 ,
the corresponding FF numbers were transformed (Eq. (4))
into crisp values
{
s
{
~Dk
))
 to facilitate quantitative analy -
sis (Table S.2). Finally, in Step 1–3, the crisp values were
normalized (Eq. (5)) to calculate the experts’ weight vector
(ϖ =[ ϖk]K) (Table 4), which was subsequently used in the
following stages of the proposed hybrid decision-making
framework.
Stage 2 (Application): Determining the weights for each
criterion using FF-Entropy: Stage 2 aims to determine the rel-
ative importance of the evaluation criteria in the selection of
AI-enhanced custom-made print advertisements. To accom-
plish this objective, seven sequential steps were performed.
In Step 2–1, each AI-enhanced custom-made print advertise-
ment was evaluated (Table S.3) by the experts (using linguis-
tics scale Table 2) with respect to the predefined criteria, and
the individual evaluation matrices
{
~E(Dk) = [ ~E(Dk) ij ] IxJ )
were constructed (Table S.4). In Step 2–2, these individual
matrices were aggregated using the experts’ weight vec -
tor obtained in Stage 1. The FFWPDMSM aggregation
operator (Eq. (6)) was employed (l = 1,2,...,o t = 3) ;
(l = 2 );( k =1 , 2,...,c = 3) ; (k =1= {D1, D2, D6});
(k =2= {D3, D5, D7}); (k =3= {D4, D8, D9}) to inte -
grate the weighted expert assessments into a single collec -
tive FF decision matrix
{
~E =
[
~Eij
]
IxJ
)
 (Table S.5) while
preserving the interrelationships among the criteria. In Step
2–3, the aggregated FF numbers were converted (Eq. (7))
into crisp values
(
E =
[
Eij
]
IxJ
)
 (Table S.6). In Step 2–4,
the crisp decision matrix was normalized (Eq. (8)) to trans-
form all values into the interval [0,1]
(
F =
[
Fij
]
IxJ
)

(Table S.7). In Step 2–5, the entropy values
required for the FF-Entropy weighting procedure were cal -
culated (Eq. ( 9)) (Table S.8). Subsequently, in Step 2–6 ,
the differentiation values
(
H =
[
Hj
]
J
)
 of the criteria
were determined (Eq. ( 10)) (Table S.8) to measure their
discriminative power. Finally, in Step 2–7, the differentia -
tion values were standardized (Eq. (11)) to obtain the final
Table 5 The matrix of criteria weights
Criteria C1 C2 C3 C4 C5 C6 C7 C8 C9 C10 C11 C12
wj 0.1151 0.0324 0.1031 0.0748 0.0991 0.0263 0.0885 0.0702 0.0670 0.0445 0.1095 0.1694
Rank 2nd 11th 4th 7th 5th 12th 6th 8th 9th 10th 3rd 1st

1 3
Page 17 of 29   101
Cognitive Computation (2026) 18:101
criterion weight vector
(
w =
[
wj
]
J
)
 within the interval
[0,1] (Table 5), representing the relative influence of each
criterion on the selection of AI-enhanced custom-made print
advertisements. These weights were then used as inputs to
the subsequent FF-OPLO-POCOD ranking procedure.
Stage 3 (Application):  Establishing the rankings of
alternatives through the application of the FF-OPLO-
POCOD method : Stage 3  focuses on ranking the twelve
AI-enhanced custom-made print advertisement alternatives
by considering the criterion weights obtained in Stage 2.
This stage consists of nine sequential steps. In Step 3–1 ,
the best values
(
L =
[
Lj
]
J
)
 required for implementing
the FF-OPLO-POCOD method were identified (Eq. (12))
(Table S.9). In Step 3–2 , the corresponding opportunity
loss values
(
M =
[
Mij
]
IxJ
)
 were calculated (Eq. (13))
(Table S.10). In Step 3–3 , these values were transformed
into (Eq. (13)) ordered pairs
(
N =
[
Nij
]
IxJ
)
 to estab -
lish the basis for the POCOD analysis (Table S.11). In Step
3–4, the best ordered pair values
(
O =
[
Oj
]
J
)
 were deter-
mined (Eq. (15)) (Table S.12), and in Step 3–5, the distances (
P =
[
Pij
]
IxJ
)
 between each advertisement alternative
and the corresponding best ordered pair were computed
(Eq. (16)) (Table S.13). In Step 3–6, these distances were
weighed (Eq. (17))
(
Q =
[
Qij
]
IxJ
)
 using the criterion
weight vector obtained from the FF-Entropy method (Table
S.14). Subsequently, in Step 3–7 , the total weighted dis -
tances (R =[ Ri]I ) for each advertisement alternative were
calculated (Eq. (18)) (Table S.15). In Step 3–8, the degree of
opportunity loss values (S =[ Si]I ) was determined for all
alternatives (Eq. (19)) (Table S.15). Finally, in Step 3–9, the
percentage of opportunity achievement values (T =[ Ti]I )
was computed (Eq. (20)) and used to rank the AI-enhanced
custom-made print advertisement alternatives (Table 6).
Based on the obtained ranking results, the overall perfor -
mance order of the twelve advertisement alternatives was
established, with Ads-4 achieving the highest performance
and being identified as the most effective AI-enhanced cus-
tom-made print advertisement.
Application Phase 4: Sensitivity and Comparative
Tests for Custom-Made Print Ads Selection
Sensitivity Analysis
The selection results of AI-enhanced custom-made print ads
were obtained using the FF-Entropy-OPLO-POCOD hybrid
method. To test the robustness of the results, three different
sensitivity analysis scenarios (SAS) were developed.
Table 6 The matrix of custom-made print ads ranks
Ads B1 B2 B3 B4 B5 B6 B7 B8 B9 B10 B11 B12
Ti 0.8915 0.9187 0.9272 0.9600 0.9337 0.9564 0.9302 0.9216 0.9477 0.9184 0.8710 0.8237
Rank 10th 8th 6th 1st 4th 2nd 5th 7th 3rd 9th 11th 12th

1 3
  101  Page 18 of 29
Cognitive Computation (2026) 18:101
In SAS-1, each evaluation criterion for the ads pro -
duced by AI, which was part of the decision model, was
removed one by one, and the algorithm was rerun. In SAS-
2, the lowest-ranked ad identified in the initial study was
removed from the decision model to identify the best ad,
and the algorithm was rerun. This process was repeated until
only the two best ads remained, after which the top ad was
identified. In SAS-3, the conditions for the parameter l with
potential values of l =1 , l =2 , and l =3 , were examined
individually. The results of SAS-1 are presented in Table 7
for the rankings.
Figure 4 shows the final advertisement scores. The analy-
sis shows that the removal of the “degree of product–visual
compatibility (C5)” criterion changes the best-performing
alternative from Ads-4 to Ads-6. This change can be attributed
to the fact that Ads-4 and Ads-6 exhibit very similar overall
performance scores under the original decision model. The
C5 criterion provides a greater comparative advantage for
Ads-4 than for Ads-6, allowing Ads-4 to achieve the highest
overall ranking when all evaluation criteria are considered.
Once this criterion is excluded, the performance difference
between the two alternatives becomes negligible, enabling
Ads-6 to move to the first position. Since Ads-6 is originally
ranked second and its overall performance is very close to
that of Ads-4, this ranking change is expected and reflects
the sensitivity of the results to the discriminative influence
of the degree of product–visual compatibilit criterion. In all
other sensitivity analysis scenarios, the removal of individ -
ual criteria does not alter the top-ranked alternative, indicat-
ing that the proposed decision framework produces stable
and robust ranking results.
The results of SAS-2 are shown in Table 8. In this sce -
nario, where the lowest-ranked ad was sequentially removed,
Ads-4 emerged as the top-ranked ad across all applications.
The results of SAS-3 are displayed in Fig. 5. Minor varia-
tions were observed in this scenario, particularly for param-
eter values c =3 , and l =3 , where Ads-9 was identified as
the best ad. In all other conditions, Ads-4 was determined to
be the best ad.
Comparative Analysis
To test the consistency of the application, results obtained
from the FF-Entropy-OPLO-POCOD hybrid method, anal -
yses were conducted by comparing it with various MCDM
methods found in the literature. In this context, decision
problems related to the ads designed using AI were solved
using AROMAN [83], ARTASI [84], MABAC [85], MAR-
COS [86], SAW, and WASPAS [87] methods. The results
are presented in Table 9.
Figure 6 displays the final values of the ads standard -
ized through max–min normalization. According to the
Table 7 The ads rank according to SAS-1
SAS-1 Ranking Best ads
The research ranking B4 > B6 > B9 > B5 > B7 > B3 > B8 > B2 > B10 > B1 > B11 > B12 Ads-4
Scenario-1a B4 > B6 > B9 > B5 > B7 > B3 > B8 > B2 > B10 > B1 > B11 > B12 Ads-4
Scenario-1b B4 > B6 > B9 > B7 > B5 > B3 > B8 > B10 > B2 > B1 > B11 > B12 Ads-4
Scenario-1c B4 > B6 > B9 > B5 > B7 > B3 > B8 > B2 > B10 > B1 > B11 > B12 Ads-4
Scenario-1d B4 > B6 > B5 > B9 > B3 > B7 > B2 > B8 > B10 > B1 > B11 > B12 Ads-4
Scenario-1e B6 > B4 > B9 > B5 > B7 > B8 > B3 > B10 > B2 > B1 > B11 > B12 Ads-6
Scenario-1f B4 > B6 > B9 > B5 > B3 > B7 > B10 > B2 > B8 > B1 > B11 > B12 Ads-4
Scenario-1 g B4 > B6 > B9 > B5 > B7 > B3 > B2 > B8 > B10 > B1 > B11 > B12 Ads-4
Scenario-1 h B4 > B6 > B9 > B3 > B5 > B7 > B8 > B2 > B10 > B1 > B11 > B12 Ads-4
Scenario-1i B4 > B6 > B9 > B5 > B7 > B3 > B8 > B10 > B2 > B1 > B11 > B12 Ads-4
Scenario-1j B4 > B6 > B9 > B5 > B3 > B7 > B2 > B8 > B10 > B1 > B11 > B12 Ads-4
Scenario-1 k B4 > B6 > B9 > B5 > B7 > B3 > B2 > B8 > B10 > B1 > B11 > B12 Ads-4
Scenario-1 l B4 > B6 > B9 > B7 > B5 > B10 > B3 > B2 > B8 > B1 > B11 > B12 Ads-4

1 3
Page 19 of 29   101
Cognitive Computation (2026) 18:101
results obtained, Ads-4 was identified as the best-designed
ad across all methods. Furthermore, the rankings obtained
from the FF-Entropy-OPLO-POCOD hybrid method align
perfectly with those from the SAW and WASPAS methods.
Minor ranking variations were observed when compared
to the other methods. According to the ranking results
obtained from the comparative analysis, the correlation
analysis indicates that the proposed FF-Entropy-OPLO-
POCOD method exhibits perfect (100%) rank correlation
(Pearson) with the SAW and WASPAS methods. Further -
more, the proposed method demonstrates correlation coef -
ficients exceeding 98% with all other comparison methods,
indicating a high level of consistency and robustness in the
ranking results. Ultimately, it can be concluded that the FF-
Entropy-OPLO-POCOD hybrid method serves as a suit -
able DSS for the ad selection process. This hybrid method
is recommended for use in ad selection due to its consis -
tency and robustness.
Compared with these alternative methods, the proposed
FF-Entropy-OPLO-POCOD framework provides the fol -
lowing methodological advantages:
 ● Compared with AROMAN, the method evaluates alter -
natives by jointly considering opportunity losses and
distances from ideal reference points.
 ● Compared with ARTASI, the method considers not only
the distance from the ideal solution but also the oppor -
tunity losses associated with non-selected alternatives
through its polar coordinate framework.
 ● Compared with MABAC, the method minimizes oppor-
tunity losses based on distances to polar reference points
rather than distances to the border approximation area.
 ● Compared with MARCOS, the method ranks alterna -
tives based on the degree of opportunity loss rather
than solely on their distances from ideal and anti-ideal
solutions.
 ● Compared with SAW, the method is based on distance
and opportunity-loss calculations rather than simple
normalized weighted summation.
 ● Compared with WASPAS, the method evaluates alterna-
tives based on their distances to the best ordered pair
values, rather than using weighted additive and multi -
plicative aggregation.
Overall, while the method offers a more comprehensive and
robust decision-making framework by simultaneously pro -
viding opportunity-loss-based alternative evaluation.
Results and Implications
Results
In this paper, the FF-Entropy-OPLO-POCOD Hybrid
Method was proposed as DSS for the selection of AI-
enhanced custom-made print ads. The method was applied
through a case study. As a result of the application, custom-
made print ads were successfully designed using AI support.
0.8
0.85
0.9
0.95
1
Removed
1st
criterion
Removed
2nd
criterion
Removed
3rd
criterion
Removed
4th
criterion
Removed
5th
criterion
Removed
6th
criterion
Removed
7th
criterion
Removed
8th
criterion
Removed
9th
criterion
Removed
10th
criterion
Removed
11th
criterion
Removed
12th
criterion
AI-enhanced Custom-Made Print Ads  final value
Ads-1 Ads-2 Ads-3 Ads-4 Ads-5 Ads-6 Ads-7 Ads-8 Ads-9 Ads-10 Ads-11 Ads-12
Fig. 4 The ads ranking results according to SAS-1

1 3
  101  Page 20 of 29
Cognitive Computation (2026) 18:101
Subsequently, the best ads were selected from the alterna -
tives using the FF-Entropy-OPLO-POCOD Hybrid Method.
The study’s findings yielded insights into the weightings of
decision-makers, the weights oh criteria, and the ranking of
the ads. Three main outputs were derived from the proposed
algorithm, as follows:
 ● At the conclusion of the first stage, the weights of the experts
were calculated using FF sets, with the ranking as follows:
“ D1 = D2 = D6 > D3 = D5 = D7 > D4 = D8 = D9
”. According to this ranking, the first, second, and sixth
experts played the main roles for decision process.
 ● In the second stage, using the FF-Entropy and FFWPD-
MSM aggregation operators, the criterion weights were
ranked as follows: “level of ethical concerns” (C12) >
“level of visual appeal” (C1) > “level of color incom -
patibility” (C11) > “level of purchase desire generation”
(C3) > “degree of product-visual compatibility” (C5) >
“level of purpose reflectiveness” (C7) > “level of call
to action” (C4) > “level of clarity/comprehensibility of
image and message” (C8) > “level of creativity” (C9) >
“level of typography suitability” (C10) > “level of gener-
ating interest” (C2) > “level of target audience compat -
ibility” (C6). In this case, the most important criterion
was identified as the “level of ethical concerns”. This
indicates that ethical considerations were paramount in
the design of AI-enhanced custom-made print ads. The
second most important criterion was the “level of visual
appeal”, demonstrating that the visual attractiveness of
the ads played a predominant role. “Level of color in -
compatibility” ranked third, revealing that both ethical
Table 8 The ads rank according to SAS-2
SAS-1 Ranking Best ads
The research ranking B4 > B6 > B9 > B5 > B7 > B3 > B8 > B2 > B10 > B1 > B11 > B12 Ads-4
Removed 12th ads B4 > B6 > B9 > B7 > B5 > B3 > B8 > B10 > B1 > B1 > B11 Ads-4
Removed 11th ads B4 > B6 > B9 > B7 > B3 > B5 > B8 > B10 > B2 > B1 Ads-4
Removed 1 st ads B4 > B6 > B9 > B5 > B7 > B3 > B8 > B10 > B2 Ads-4
Removed 2nd ads B4 > B6 > B9 > B5 > B3 > B7 > B8 > B10 Ads-4
Removed 10th ads B4 > B6 > B5 > B9 > B7 > B3 > B8 Ads-4
Removed 8th ads B4 > B6 > B9 > B7 > B5 > B3 Ads-4
Removed 3rd ads B4 > B6 > B9 > B7 > B5 Ads-4
Removed 5th ads B4 > B6 > B9 > B7 Ads-4
Removed 7th ads B4 > B6 > B9 Ads-4
Removed 9th ads B4 > B6 Ads-4
0
2
4
6
8
10
12
Ads-1
Ads-2
Ads-3
Ads-4
Ads-5
Ads-6
Ads-7
Ads-8
Ads-9
Ads-10
Ads-11
Ads-12
c=3 and l=1 c=3 and l=2 c=3 and l=3
Fig. 5 The ads rank according to SAS-3

1 3
Page 21 of 29   101
Cognitive Computation (2026) 18:101
concerns and color incompatibility, as cost-related crite-
ria, played a crucial role in the decision process.
 ● By the end of the third stage, the ranking of the
AI-enhanced custom-made print ads was as fol -
lows: “ B4 > B6 > B9 >B5 > B7 > B3 > B8 >
B2 > B10 > B1 > B11 > B12”. According to this rank-
ing, the fourth ad was deemed the most successful.
Thus, the FF-Entropy-OPLO-POCOD hybrid method
was successfully applied, accounting for varying expert
opinions and differing ad selection criteria, and the re -
sults were obtained.
The results of the SAS tests yielded the following
conclusions:
 ● When the “degree of product-visual compatibility” (C5)
was removed from the model, the alternative changed to
Ads-6. Given that this criterion evaluates the relation -
ship between the product and its visual representation, it
can be inferred that AI-designed ads may exhibit short -
comings in the product-visual relationship, leading to
variations in ad selection.
 ● In the application of the FF-Entropy-OPLO-POCOD
hybrid method, when the lowest-ranked ad was re -
moved and the algorithm rerun, the best one remained
consistent. This consistency supports the robustness of
the model, confirming that Ads-4 is the best ad under all
conditions.
Changes to the l parameter revealed that under the condition
l =3 , the results varied. In this case study, l =2  provided
the best results, indicating that this parameter setting is
most suitable.Comparison analyses were conducted to test
the consistency of the method. The ranking results of the
ads were obtained using the AROMAN, ARTASI, MABAC,
MARCOS, SAW, and WASPAS methods for comparison
analyses. The comparison results are:
 ● When comparing the results of the FF-Entropy-OPLO-
POCOD hybrid method with those of the AROMAN
and MABAC methods, Ads-8 (B8) and Ads-10 (B10)
advanced by one rank each, while Ads-3 (B3) and Ads-2
(B2) dropped by one rank each.
 ● When comparing the FF-Entropy-OPLO-POCOD hy -
brid method with those of the ARTASI and MARCOS
methods, Ads-10 (B10) advanced by one rank, while
Ads-2 (B2) dropped by one rank.
 ● When comparing the FF-Entropy-OPLO-POCOD hy -
brid method with those of the SAW and WASPAS meth-
ods, the rankings were observed to be identical.
Table 9 The ads rank according to comparative analysis
Methods Ranking Best ads
FF-Entropy-OPLO-POCOD B4 > B6 > B9 > B5 > B7 > B3 > B8 > B2 > B10 > B1 > B11 > B12 Ads-4
AROMAN B4 > B6 > B9 > B5 > B7 > B8 > B3 > B10 > B2 > B1 > B11 > B12 Ads-4
ARTASI B4 > B6 > B9 > B5 > B7 > B3 > B8 > B10 > B2 > B1 > B11 > B12 Ads-4
MABAC B4 > B6 > B9 > B5 > B7 > B8 > B3 > B10 > B2 > B1 > B11 > B12 Ads-4
MARCOS B4 > B6 > B9 > B5 > B7 > B3 > B8 > B10 > B2 > B1 > B11 > B12 Ads-4
SAW B4 > B6 > B9 > B5 > B7 > B3 > B8 > B2 > B10 > B1 > B11 > B12 Ads-4
W ASPAS B4 > B6 > B9 > B5 > B7 > B3 > B8 > B2 > B10 > B1 > B11 > B12 Ads-4

1 3
  101  Page 22 of 29
Cognitive Computation (2026) 18:101
 ● Across all methods, Ads-4 (B4) was identified as the
best alternative ad, while Ads-12 (B12) was identified as
the worst alternative ad.
Theoretical and Practical Implications
This study provides several theoretical and practical impli -
cations for advertising, marketing, and decision support
systems by integrating generative AI with a multi-attri -
bute group decision-making framework. The proposed
FF-Entropy-OPLO-POCOD hybrid method demonstrates
that AI can contribute not only to the efficient generation
of customized print advertisements but also to systematic,
transparent, and reliable advertisement selection under
uncertainty.
From a theoretical perspective, this research extends
the application of Social Cognitive Theory to AI-enhanced
advertising. Rather than viewing AI solely as an automa -
tion technology, the findings suggest that AI functions as
a cognitive decision-support mechanism that facilitates
observational learning, continuous feedback, and adaptive
decision-making. By generating multiple advertisement
alternatives and providing structured evaluations of these
alternatives, the proposed framework enables market -
ers to learn from AI-generated outputs, compare different
design strategies, and refine their creative judgments. This
iterative interaction between human expertise and AI assis-
tance strengthens marketers’ self-efficacy in advertising
decision-making and supports the continuous improvement
of creative marketing practices.
The study also contributes to the decision science litera -
ture by introducing the FF-Entropy-OPLO-POCOD hybrid
method as a comprehensive MAGDM framework capable
of handling uncertainty in expert judgments. The integra -
tion of FF sets, the FFWPDMSM aggregation operator, the
FF-Entropy weighting method, and the FF-OPLO-POCOD
ranking approach provide a structured methodology that
simultaneously considers expert uncertainty, criterion
importance, and alternative performance. The robustness
analyses further demonstrate the stability and reliability of
the proposed decision support system.
From a practical perspective, the proposed framework
offers valuable guidance for companies, advertising agen -
cies, and marketing professionals seeking to incorporate AI
into their creative processes. AI-assisted advertisement gen-
eration enables organizations to produce multiple custom -
ized advertisement alternatives rapidly, while the proposed
decision support system facilitates the identification of the
most effective design using objective and systematic evalu-
ation procedures. This capability is particularly valuable
for small and medium-sized enterprises, which often face
financial and human resource constraints in developing pro-
fessional advertising campaigns. By reducing design costs,
supporting evidence-based decision-making, and improv -
ing the quality of advertisement selection, the proposed
framework helps organizations compete more effectively in
increasingly dynamic markets.
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
FF-Entropy-
OPLO-POCOD
AROMAN ARTASI MABACM ARCOS SAW WASPAS
AI-enhanced Custom-Made Print Ads  final value
Ads-1 Ads-2 Ads-3 Ads-4 Ads-5 Ads-6 Ads-7 Ads-8 Ads-9 Ads-10 Ads-11 Ads-12
Fig. 6 The ads rank values according to comparative analysis

1 3
Page 23 of 29   101
Cognitive Computation (2026) 18:101
The findings also suggest broader implications beyond
the advertising sector. Since the proposed methodol -
ogy combines AI-assisted content generation with struc -
tured group decision-making, it can be adapted to various
domains requiring the evaluation of multiple design alter -
natives under uncertainty, such as product design, packag -
ing development, branding, service innovation, and digital
content creation. Future research may further extend this
framework by incorporating different generative AI models,
additional fuzzy environments, or alternative MCDM tech -
niques to examine its applicability across diverse decision-
making contexts.
Overall, this study contributes to the growing body of
research on AI-supported marketing by demonstrating that
the combination of generative AI and structured decision-
making frameworks can improve not only operational effi -
ciency but also the cognitive quality of marketing decisions.
The proposed approach establishes a foundation for devel -
oping intelligent decision support systems that enhance
creativity, learning, and strategic decision-making in AI-
assisted advertising.
Conclusion
This study developed and validated an AI-enhanced DSS
for the design and selection of custom-made print ads by
integrating generative AI with a MAGDM framework. The
results demonstrate that generative AI can successfully pro-
duce multiple personalized advertisement alternatives from
a single standardized prompt, offering organizations an effi-
cient and scalable approach to creative advertising. At the
same time, the study shows that selecting the most effec -
tive advertisement should not rely solely on AI-generated
outputs. Instead, expert evaluations remain essential for
assessing the quality, relevance, and persuasive potential of
alternative designs. By integrating the FF-Entropy-OPLO-
POCOD hybrid method into the evaluation process, the
proposed framework enables organizations to systemati -
cally identify the advertisement that best satisfies multiple
advertising criteria.
From a theoretical perspective, the findings extend the
application of Social Cognitive Theory to AI-assisted adver-
tising by demonstrating that effective advertisement design
emerges through the interaction of technological capabili -
ties and human cognitive judgment rather than through AI
alone. While generative AI facilitates observational learning
by producing diverse creative alternatives based on learned
patterns, expert evaluation introduces reflective judgment,
experience, and contextual understanding into the final deci-
sion. This complementary process supports more informed
and transparent advertising decisions, illustrating how
human cognition and AI can jointly enhance creative perfor-
mance. From a practical perspective, the proposed frame -
work provides advertisers and marketing practitioners with
a structured methodology for generating, evaluating, and
selecting AI-generated custom-made print advertisements
while reducing subjectivity in the decision-making pro -
cess. The flexibility of the proposed framework also makes
it applicable to different products, customer segments,
and advertising formats, providing a valuable foundation
for future research on AI-assisted marketing, personalized
advertising, and intelligent decision support systems.
Research Limitations
This study has several limitations that should be considered
when interpreting the findings. First, the empirical applica -
tion was limited to AI-generated print advertisements for
dairy products in Türkiye, which may restrict the generaliz-
ability of the proposed framework to other industries, prod-
ucts, and cultural contexts. Second, the evaluation process
relied on expert judgments, making the results dependent
on the experience and perspectives of the selected experts.
Third, the quality and diversity of the generated advertise -
ments were influenced by the capabilities of the selected
generative AI platforms and the standardized prompts used
in the study. Moreover, although the proposed decision-
making framework provides a systematic evaluation of
advertisement alternatives, it does not incorporate actual
consumer responses or behavioral outcomes.
Future Suggestions
Future research may extend the proposed framework by
examining its applicability across different industries,
products, and cultural settings to enhance its generalizabil -
ity. In addition, integrating consumer-based experiments
would provide a more comprehensive assessment of the
effectiveness of AI-generated advertisement. Further stud -
ies may also investigate the use of emerging generative AI
models and alternative MCDM techniques and fuzzy sets
to improve advertisement generation and selection perfor -
mance. Future studies could investigate the effectiveness of
the proposed framework across different cultural contexts,
while examining how the interaction between AI-generated
content and human judgment shapes advertising quality and
decision-making outcomes. Finally, implementing the pro -
posed FF-Entropy-OPLO-POCOD algorithm in computa -
tional environments such as MATLAB, Python, or similar
platforms would enable the evaluation of its computational
efficiency and runtime performance, providing additional
evidence of its applicability to large-scale and real-time
decision-making problems.

1 3
  101  Page 24 of 29
Cognitive Computation (2026) 18:101
Appendix: Notation and Abbreviations
Notations
Indices and sets:
i = 1,2,..., I index of alternatives (custom-made print ads),
j = 1,2,..., J index of criteria,
k = 1,2,..., K index of experts,
t =1 , 2,...,c index of partitions,
l = 1,2,...,o t index of element in the partitions,
B = {B1, B2,..., Bi,..., BI } set of alternatives (custom-made print ads),
C = {C1, C2,..., Cj,..., CJ } set of criteria,
C− ⊆C set of the cost criteria,
C+ ⊆C set of the benefit criteria,
D = {D1, D2,..., Dk,..., DK} set of experts
Parameters:
C≥ 2 number of criteria,
B≥ 2 number of alternatives,
D≥ 2 number of experts,
Cl ot -tuple combination of ot,
Variables:
s
{ ~Dk ) (k ∈D ) score function value of the expert Dk,
δ~Dk (k ∈D ) the degrees of membership value (FF set) of the assessment by the expert Dk for expertise level,
β~Dk (k ∈D ) the degrees of non-membership value (FF set) of the assessment by the expert Dk for expertise level
ϖk(k ∈D ) significant level of the expert Dk,
~E(Dk) ij (k ∈D , i ∈I , j ∈J ) FFN assessment of the alternative Bi under the criterion Cj provided by the expert Dk,
δ~E(Dk) ij (k ∈D , i ∈I , j ∈J ) the degrees of membership value of the FFN assessment of the alternative Bi under the criterion Cj provided by the expert Dk,
β~E(Dk) ij (k ∈D , i ∈I , j ∈J ) the degrees of non-membership value of the FFN assessment of the alternative Bi under the criterion Cj provided by the expert Dk,
~Eij {i ∈I , j ∈J ) FFN aggregated assessment of the alternative Bi under the criterion Dk using FFWPD- MSM aggregation operator,
s
{~Eij ){ i ∈I , j ∈J ) score function value of the alternative Bi under the criterion Dk,
Eij
(i ∈I , j ∈J ) numerical aggregated value of the alternative Bi under the criterion Dk,
Fij
(i ∈I , j ∈J ) the normalization value of the alternative Bi under the criterion Cj,
the entropy value of the criterion Cj,
Hj
(j ∈J ) the degrees differentiation value of the criterion Cj,
wj
(j ∈J ) final weighting of the criterion Cj,
Lj
(j ∈J ) the best value for each action of the criterion Cj,
Mij
(i ∈I , j ∈J ) the opportunity loss value of the alternative Bi under the criterion Cj,
Nij
(i ∈I , j ∈J ) the ordered pair values of the alternative Bi under the criterion Cj,
Oj
(j ∈J ) the best ordered pair values for each action of the criterion Cj,
Pij
(i ∈I , j ∈J ) the distance of pair values of the alternative Bi under the criterion Cj,
Qij
(i ∈I , j ∈J ) the weighted distance of pair values of the alternative Bi under the criterion Cj,

1 3
Page 25 of 29   101
Cognitive Computation (2026) 18:101
Indices and sets:
i = 1,2,..., I index of alternatives (custom-made print ads),
Ri (i ∈I ) the total distance values for each action of the alternative Bi,
Si (i ∈I ) the degree opportunity loss values for each action of the alternative Bi,
Ti (i ∈I ) the final ranking value of the alternative Bi for FF-Entropy-OPLO-POCOD hybrid
method
Abbreviations
Abbreviation Stands for
AI : Artificial Intelligence
ARAS : Additive Ratio Assessment
ARLON : Alternative Ranking using Two-Step Loga-
rithmic Normalization
AROMAN : Alternative Ranking Order Method Account-
ing for Two-Step Normalization
ARTASI : Alternative Ranking Technique Based On
Adaptive Standardized İntervals
BWM : Best–Worst Method
CRADIS : Compromise Ranking of Alternatives from
Distance to Ideal Solution
DSS : Decision Support System
FFs : Fermatean Fuzzy Sets
FFWPDMSM : FF-Weighted Partitioned Dual Maclaurin
Symmetric Mean
MABAC : Multi-Attributive Border Approximation
Area Comparison
MAGDM : Multi-Attribute Group Decision-Making
MARCOS : Measurement Of Alternatives And Ranking
According To Compromise Solution
MCDM : Multi-Criteria Decision-Making
OPLO : Opportunity Losses
POCOD : Polar Coordinate Distance
RANCOM : Ranking Comparison
SAW : Simple Additive Weighting
SIWEC : Simple Weight Calculation
SPC : Symmetry Point of Criterion
SWARA : Step-wise Weight Assessment Ratio Analysis
VIKOR : VIšeKriterijumska Optimizacija I Kompro-
misno Rešenje
WASPAS : Weighted Aggregated Sum Product
Assessment
Supplementary Information The online version contains supplementary
material available at  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 0 7 / s 1 2 5 5 9 - 0 2 6 - 1 0 6 4 2 - 2     .
Acknowledgements This study was supported by Korea University.
Authors Contributions Elif Akagün Ergin: Conceptualization, Investi-
gation, Validation, Formal analysis, Data Curation, Writing—Original
Draft, Review & Editing. Galip Cihan Yalçın: Methodology, Valida -
tion, Formal analysis, Visualization, Data Curation, Writing—Original
Draft, Review & Editing. Karahan Kara: Methodology, Validation,
Formal analysis, Visualization, Data Curation, Writing—Original
Draft, Review & Editing. Pınar Aytekin: Investigation, Validation, For-
mal analysis, Writing—Original Draft, Review & Editing. Tuğçe Çe -
lik: Investigation, Formal analysis, Writing—Original Draft, Review
& Editing. Vladimir Simic: Project Administration, Formal analysis,
Visualization, Validation, Writing—Original Draft, Review & Editing.
Dragan Pamucar: Writing—Original Draft, Review & Editing.
Funding Not available.
Data Availability Available on a reasonable request.
Declarations
Ethical Approval This article does not contain any studies with human
participants or animals performed by any of the authors.
Consent to Participate All authors read and approved the final manu -
script.
Consent to Publish All authors consent when it is published.
Conflict of interest The authors declare that they have no conflict of
interest.
Open Access  This article is licensed under a Creative Com -
mons Attribution-NonCommercial-NoDerivatives 4.0 International
License, which permits any non-commercial use, sharing, distribu -
tion and reproduction in any medium or format, as long as you give
appropriate credit to the original author(s) and the source, provide a
link to the Creative Commons licence, and indicate if you modified
the licensed material. You do not have permission under this licence
to share adapted material derived from this article or parts of it. The
images or other third party material in this article are included in the
article’s Creative Commons licence, unless indicated otherwise in a
credit line to the material. If material is not included in the article’s
Creative Commons licence and your intended use is not permitted
by statutory regulation or exceeds the permitted use, you will need
to obtain permission directly from the copyright holder. To view
a copy of this licence, visit http:// creativ ecommon s.org /licenses/
by-nc-nd/4.0/.
References
1. Bergkvist L, Taylor CR. Reviving and improving brand awareness
as a construct in advertising research. J Advert. 2022;51(3):294–
307. https:/ /doi.or g/10.10 80/00 913367.2022.2039886.
2. Kerr G, Richards J. Redefining advertising in research and prac -
tice. Int J Advert. 2021;40(2):175–98.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 8 0 / 0 2
6 5 0 4 8 7 . 2 0 2 0 . 1 7 6 9 4 0 7     .
3. De Keyzer F, Dens N, De Pelsmacker P. How and when personal-
ized advertising leads to brand attitude, click, and WOM inten -
tion. J Advert. 2022;51(1):39–56.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 8 0 / 0 0 9 1 3 3
6 7 . 2 0 2 1 . 1 8 8 8 3 3 9     .

1 3
  101  Page 26 of 29
Cognitive Computation (2026) 18:101
4. Segijn CM, Van Ooijen I. Differences in consumer knowledge
and perceptions of personalized advertising: Comparing online
behavioural advertising and synced advertising. J Mark Commun.
2022;28(2):207–26.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 8 0 / 1 3 5 2 7 2 6 6 . 2 0 2 0 . 1 8 5
7 2 9 7     .
5. Lehnert K, Goupil S, Brand P. Content and the customer: inbound
ad strategies gain traction. J Bus Strateg. 2021;42(1):3–12. https:/
/doi.or g/10.11 08/JB S-12-2019-0243.
6. Hess NJ, Kelley CM, Scott ML, Mende M, Schumann JH. Get -
ting personal in public!? How consumers respond to public per -
sonalized advertising in retail stores. J Retail. 2020;96(3):344–61.
https:/ /doi.or g/10.10 16/j. jretai.2019.11.005.
7. Kumar V , Gupta S. Conceptualizing the evolution and future of
advertising. J Advert. 2016;45(3):302–17.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 8 0
/ 0 0 9 1 3 3 6 7 . 2 0 1 6 . 1 1 9 9 3 3 5     .
8. Noerman T, Riyadi Yuliaji ES, Natasha CAM. The impacts
of social influence and hedonic motivation on experience and
continuance intention of using AI in SMEs’ HRM. Cogent Bus
Manag. 2025; 12(1):2542422.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 8 0 / 2 3 3 1 1 9 7 5
. 2 0 2 5 . 2 5 4 2 4 2 2     .
9. Mondal S, Goswami SS. Rise of intelligent machines: influence
of artificial intelligence on mechanical engineering innovation.
Spec Eng Man Sci. 2024;2(1):46–55.  h t t  p s : /  / d o  i . o  r g / 1 0 . 3 1 1 8 1 / s e
m s 1 1 2 0 2 4 4 h     .
10. Vakratsas D, Wang X. Artificial intelligence in advertising cre -
ativity. J Advert. 2020;50(1):39–51.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 8 0 / 0 0 9 1
3 3 6 7 . 2 0 2 0 . 1 8 4 3 0 9 0     .
11. Horvath AS, Pouliou P. AI for conceptual architecture: reflections
on designing with text-to-text, text-to-image, and image-to-image
generators. Front Archit Res. 2024;13(3):593–612.  h t t  p s : /  / d o  i . o  r g
/ 1 0 . 1 0 1 6 / j . f o a r . 2 0 2 4 . 0 2 . 0 0 6     .
12. Önden A, Alnour M, Simic V , Pamucar D. The evolution of senti-
ment analysis across various scientific disciplines: a comprehen -
sive review based on the bibliometric technique. Decis Mak Adv.
2024;2(1):222–37. https:/ /doi.or g/10.31 181/d ma21202441.
13. Li Y . “Will artificial intelligence platforms replace designers in
the future?” Analyzing the impact of artificial intelligence plat -
forms on the engineering design industry through color percep -
tion. Eng Appl Artif Intell. 2024;138:109369.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1
0 1 6 / j . e n g a p p a i . 2 0 2 4 . 1 0 9 3 6 9     .
14. Nair K, Gupta R. Application of AI technology in modern digi -
tal marketing environment. World J Entrep Manag Sustain Dev.
2021;17(3):318–28.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 1 0 8 / W J E M S D - 0 8 - 2 0 2 0
- 0 0 9 9     .
15. Huang MH, Rust RT. A strategic framework for artificial intel -
ligence in marketing. J Acad Mark Sci. 2021;49:30–50.  h t t  p s : /  / d o
i . o  r g / 1 0 . 1 0 0 7 / s 1 1 7 4 7 - 0 2 0 - 0 0 7 4 9 - 9     .
16. Sahoo SK, Goswami SS. Green supplier selection using MCDM:
a comprehensive review of recent studies. Spectr Eng Manag Sci.
2024;2(1):1–16. https:/ /doi.or g/10.31 181/s ems1120241a.
17. El-Araby A, Sabry I, El-Assal A. Ranking performance of MAR-
COS method for location selection problem in the presence of
conflicting criteria. Decis Mak Adv. 2024;2(1):148–62.  h t t  p s : /  / d o
i . o  r g / 1 0 . 3 1 1 8 1 / d m a 2 1 2 0 2 4 3 5     .
18. Alqahtani H, Kumar G. Advances in artificial intelligence for
detecting algorithmically generated domains: current trends and
future prospects. Eng Appl Artif Intell. 2024;138(B):109410.
https:/ /doi.or g/10.10 16/j. engappai.2024.109410.
19. Roy S. A multi attribute decision making framework based on
partitioned dual Maclaurin symmetric mean operators under
Fermatean fuzzy environment. Phys Scr. 2024;99(10):105286.
https:/ /doi.or g/10.10 88/14 02-4896/ad7bf8.
20. Sheikh R, Senfi S. A novel opportunity losses‐based polar coor -
dinate distance (OPLO‐POCOD) approach to multiple criteria
decision‐making. J Math. 2024.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 1 5 5 / 2 0 2 4 / 8 8
4 5 8 8 6     .
21. Liu X, Burns AC, Hou Y . An investigation of brand-related user-
generated content on twitter. J Advert. 2017;46(2):236–47. https:/
/doi.or g/10.10 80/00 913367.2017.1297273.
22. Becker IF, Linzmajer M, von Wangenheim F. Cross-industrial
user channel preferences on the path to online purchase: homo -
geneous, heterogeneous, or mixed? J Advert. 2017;46(2):248–68.
https:/ /doi.or g/10.10 80/00 913367.2017.1300076.
23. Schultz D. The future of advertising or whatever we’re going to
call it. J Advert. 2016;45(3):276–85.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 8 0 / 0 0 9
1 3 3 6 7 . 2 0 1 6 . 1 1 8 5 0 6 1     .
24. Deng S, Tan CW, Wang W, Pan Y . Smart generation system of
personalized advertising copy and its application to advertising
practice and research. J Advert. 2019;48(4):356–65.  h t t  p s : /  / d o  i . o  r
g / 1 0 . 1 0 8 0 / 0 0 9 1 3 3 6 7 . 2 0 1 9 . 1 6 5 2 1 2 1     .
25. Murár P. Bridging personalised marketing with artificial intelli -
gence: An analysis of evolution and future trends. In: Prostináková
Hossová M, Martovič M, Solík M, , editors. Media & marketing
identity: AI the future of today; 2023. P. 348–355.  h t t  p s : /  / d o  i . o  r g /
1 0 . 3 4 1 3 5 / m m i d e n t i t y - 2 0 2 3 - 3 5     .
26. Kumar V , Rajan B, Venkatesan R, Lecinski J. Understanding the
role of artificial intelligence in personalized engagement market-
ing. Calif Manag Rev. 2019;61(4):135–55.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 1 7
7 / 0 0 0 8 1 2 5 6 1 9 8 5 9 3 1 7     .
27. Key TM, Czaplewski AJ. Upstream social marketing strategy:
an integrated marketing communications approach. Bus Horiz.
2017;60(3):325–33.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 1 6 / j . b u s h o r . 2 0 1 7 . 0 1 . 0
0 6     .
28. De Keyzer F, Dens N, De Pelsmacker P. Is this for me? How
consumers respond to personalized advertising on social network
sites. J Interact Advert. 2015;15(2):124–34.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0
8 0 / 1 5 2 5 2 0 1 9 . 2 0 1 5 . 1 0 8 2 4 5 0     .
29. Pfiffelmann J, Dens N, Soulez S. Personalized advertisements
with integration of names and photographs: an eye-tracking
experiment. J Bus Res. 2020;111:196–207.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0
1 6 / j . j b u s r e s . 2 0 1 9 . 0 8 . 0 1 7     .
30. Chandra S, Verma S, Lim WM, Kumar S, Donthu N. Personaliza-
tion in personalized marketing: trends and ways forward. Psychol
Mark. 2022;39(8):1529–62. https:/ /doi.or g/10.10 02/ma r.21670.
31. Poels K, Dewitte S. The role of emotions in advertising: a call to
action. J Advert. 2019;48(1):81–90.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 8 0 / 0 0 9 1
3 3 6 7 . 2 0 1 9 . 1 5 7 9 6 8 8     .
32. Shaouf A, Lü K, Li X. The effect of web advertising visual design
on online purchase intention: an examination across gender.
Comput Hum Behav. 2016;60:622–34.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 1 6 / j
. c h b . 2 0 1 6 . 0 2 . 0 9 0     .
33. White AR, Martinez LM, Martinez LF, Rando B. Color in web
banner advertising: the influence of analogous and complemen -
tary colors on attitude and purchase intention. Electron Commer
Res Appl. 2021;50:101100.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 1 6 / j . c h b . 2 0 2 0 . 1 0
6 6 5 7     .
34. Pieters R, Wedel M. Attention capture and transfer in advertising:
brand, pictorial, and text-size effects. J Mark. 2004;68(2):36–50.
https:/ /doi.or g/10.15 09/jm kg.68.2.36.27794.
35. Haleem A, Javaid M, Qadri MA, Singh RP, Suman R. Artificial
intelligence (AI) applications for marketing: A literature-based
study. Int J Intell Netw. 2022;3:119–32.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 1 6 /
j . i j i n . 2 0 2 2 . 0 8 . 0 0 5     .
36. Kara K, Ergin EA, Yalçın GC, Çelik T, Deveci M, Kadry S. Sustain-
able brand logo selection using an AI-Supported PF-WENSLO-
ARLON hybrid method. Expert Syst Appl. 2024;125382.  h t t  p s : /  /
d o  i . o  r g / 1 0 . 1 0 1 6 / j . e s w a . 2 0 2 4 . 1 2 5 3 8 2     .
37. Seikh MR, Chatterjee P. Identifying sustainable strategies for
electronic waste management utilizing confidence-based group
decision-making method in interval valued Fermatean fuzzy
environment. Eng Appl Artif Intell. 2024;135:108701.  h t t  p s : /  / d o  i
. o  r g / 1 0 . 1 0 1 6 / j . e n g a p p a i . 2 0 2 4 . 1 0 8 7 0 1     .

1 3
Page 27 of 29   101
Cognitive Computation (2026) 18:101
38. Seikh MR, Chatterjee P. Determination of best renewable energy
sources in India using SWARA-ARAS in confidence level based
interval-valued Fermatean fuzzy environment. Appl Soft Comput.
2024;155:111495. https:/ /doi.or g/10.10 16/j. asoc.2024.111495.
39. Seikh MR, Mukherjee A. Fermatean fuzzy CRADIS approach
based on triangular divergence for selecting online shopping plat-
form. Trans Fuzzy Sets Syst. 2024; 6(2):108.  h t t  p s : /  / d o  i . o  r g / 1 0 . 7
1 6 0 2 / t f s s . 2 0 2 4 . 1 1 2 7 2 2 4     .
40. Chatterjee P, Seikh MR. Analysing sustainable industrial waste -
water treatment technologies using circular fermatean fuzzy
multi-attribute group decision making with decision experts’ con-
fidence levels. Eng Appl Artif Intell. 2025;162:112549.  h t t  p s : /  / d o
i . o  r g / 1 0 . 1 0 1 6 / j . e n g a p p a i . 2 0 2 5 . 1 1 2 5 4 9     .
41. Yalçın GC, Kara K, Özekenci EK, Simic V , Pamucar D. Green
maritime transport performance analysis of G-7 countries using
an interval-valued Fermatean fuzzy ARLON-based decision
model. Appl Soft Comput. 2025; 113677.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 1
6 / j . a s o c . 2 0 2 5 . 1 1 3 6 7 7     .
42. Yalçın GC, Kara K, Özekenci EK, Simic V , Pamucar D. Promot-
ing biodiversity-based trade: a fuzzy multi-criteria decision ana -
lytics for performance measurement of sustainable development
in megadiverse countries. J Clean Prod. 2026;547:147831. https:/
/doi.or g/10.10 16/j. jclepro.2026.147831.
43. Abosuliman SS, Abdullah S, Ullah I. Using a fuzzy credibility
neural network to select nanomaterials for nanosensors. Eng Appl
Artif Intell. 2024;136:108958.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 1 6 / j . e n g a p p a i
. 2 0 2 4 . 1 0 8 9 5 8     .
44. Zhang Y , Abdullah S, Ullah I, Ghani F. A new approach to neural
network via double hierarchy linguistic information: application
in robot selection. Eng Appl Artif Intell. 2024;129:107581. https:/
/doi.or g/10.10 16/j. engappai.2023.107581.
45. Nawaz M, Abdullah S, Ullah I. An integrated fuzzy neural net -
work model for surgical approach selection using double hierar -
chy linguistic information. Comput Biol Med. 2025;186:109606.
https:/ /doi.or g/10.10 16/j. compbiomed.2024.109606.
46. Irvanizam I, Nasution MK, Tulus T, Nababan EB. A hybrid deci-
sion support framework using MEREC-RAFSI with spherical
fuzzy numbers for selecting banking financial aid recipients.
IEEE Access. 2025;13:33101–23.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 1 0 9 / A C C E
S S . 2 0 2 5 . 3 5 3 9 2 0 0     .
47. Ullah I, Abdullah S, Nawaz M. A novel framework for selection
of renewable energy source based on three-way decision making
model under Pythagorean fuzzy credibility numbers. Eng Appl
Artif Intell. 2025;154:110941.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 1 6 / j . e n g a p p a
i . 2 0 2 5 . 1 1 0 9 4 1     .
48. Irvanizam I, Zahara N, Marzuki M. Single-valued neutrosophic
ARAS based on multi-criteria group decision-making for a
school selection. In: Multi-criteria decision making models and
techniques: neutrosophic approaches. IGI Global Scientific Pub -
lishing; 2025. p. 307–32.  h t t  p s : /  / d o  i . o  r g / 1 0 . 4 0 1 8 / 9 7 9 - 8 - 3 6 9 3 - 2 0 8
5 - 3 . c h 0 1 0     .
49. Garg H. Multi-attribute group decision-making process based on
possibility degree and operators for intuitionistic multiplicative
set. Complex Intell Syst. 2021;7(2):1099–121.  h t t  p s : /  / d o  i . o  r g / 1 0 .
1 0 0 7 / s 4 0 7 4 7 - 0 2 0 - 0 0 2 5 6 - y     .
50. Irvanizam I, Helzami D. Bipolar neutrosophic ARAS method
based on multiple attribute group decision-making to evaluate the
service quality of sharia bank branch offices. In: Neutrosophic
paradigms: advancements in decision making and statistical
analysis: neutrosophic principles for handling uncertainty. Cham:
Springer Nature Switzerland; 2025. p. 319–48.  h t t  p s : /  / d o  i . o  r g / 1 0 .
1 0 0 7 / 9 7 8 - 3 - 0 3 1 - 7 8 5 0 5 - 4 _ 1 7     .
51. Chammam W, Ganie AH, Saeed MM, Sief AM, Khalaf MM.
A new similarity measure for picture fuzzy sets and its various
applications. Cogn Comput. 2025;17(2):91.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0
0 7 / s 1 2 5 5 9 - 0 2 5 - 1 0 4 4 9 - 7     .
52. Hussain A, Ullah K, Senapati T, Esztergár-Kiss D, Moslem S. A
multi-attribute group decision-making method for optimal selec -
tion of digital voting tools to ameliorate public participation in
urban transport. Results Eng. 2025;25:103867.  h t t  p s : /  / d o  i . o  r g / 1 0 .
1 0 1 6 / j . r i n e n g . 2 0 2 4 . 1 0 3 8 6 7     .
53. Naz S, Fatima A, But SA, Pamucar D, Zamora-Musa R, Acosta-
Coll M. Effective multi-attribute group decision-making approach
to study astronomy in the probabilistic linguistic q-rung orthopair
fuzzy VIKOR framework. Heliyon. 2024.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 1 6
/ j . h e l i y o n . 2 0 2 4 . e 3 3 0 0 4     .
54. Kara K, Yalçın GC, Özekenci EK, Bilek G, Simic V , Tunçsiper Ç,
et al. Promoting transition towards sustainable air transport sys -
tems: a hybrid decision support system for effective national-level
performance evaluation. J Air Transp Manag. 2026;133:102964.
https:/ /doi.or g/10.10 16/j. jairtraman.2025.102964.
55. Basole RC, Major T. Generative AI for visualization: opportuni -
ties and challenges. IEEE Comput Graph Appl. 2024;44(2):55–
64. https:/ /doi.or g/10.11 09/MC G.2024.3362168.
56. Muller M, Chilton LB, Kantosalo A, Martin CP, Walsh G.
GenAICHI: generative AI and HCI. In: CHI conference on
human factors in computing systems extended abstracts; 2022. p.
1–7. https:/ /doi.or g/10.11 45/34 91101.3503719.
57. Daugherty P, Wilson HJ. Radically human: how new technology
is transforming business and shaping our future. Harvard Busi -
ness Press; 2022.
58. Thomson TJ, Thomas RJ, Matich P. Generative Visual AI in
News Organizations: Challenges, Opportunities, Perceptions, and
Policies. Digit Journal. 2024; 1–22.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 8 0 / 2 1 6 7
0 8 1 1 . 2 0 2 4 . 2 3 3 1 7 6 9     .
59. Dehouche N, Dehouche K. What’s in a text-to-image prompt?
The potential of stable diffusion in visual arts education. Heliyon.
2023; 9(6). https:/ /doi.or g/10.17 632/s x9sfpm5hj.1.
60. Liang J, Pei W, Lu F. Layout-bridging text-to-image synthesis.
IEEE Trans Circuits Syst Video Technol. 2023;33(12):7438–51.
https:/ /doi.or g/10.11 09/TC SVT.2023.3274228.
61. Jaruga-Rozdolska A. Artificial intelligence as part of future prac-
tices in the architect’s work: MidJourney generative tool as part
of a process of creating an architectural form. Architectus. 2022;3
(71):95–104. https:/ /doi.or g/10.37 190/a rc220310.
62. Rong A, Hansopaheluwakan-Edward N, Li D. Analyzing the
color availability of AI-generated posters based on K-means clus-
tering: 74% orange, 38% cyan, 32% yellow, and 28% blue-cyan.
Color Res Appl. 2024;49(2):234–57.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 0 2 / c o l .
2 2 9 1 2     .
63. Senapati T, Yager RR. Fermatean fuzzy sets. J Ambient Intell
Humaniz Comput. 2020;11:663–74.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 0 7 / s 1 2 6
5 2 - 0 1 9 - 0 1 3 7 7 - 0     .
64. Hadi A, Khan W, Khan A. A novel approach to MADM problems
using Fermatean fuzzy Hamacher aggregation operators. Int J Intell
Syst. 2021;36(7):3464–99.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 0 2 / i n t . 2 2 4 2 3     .
65. Sahoo L. A new score function based Fermatean fuzzy transporta-
tion problem. Results Control Optim. 2021;4:100040.  h t t  p s : /  / d o  i .
o  r g / 1 0 . 1 0 1 6 / j . r i c o . 2 0 2 1 . 1 0 0 0 4 0     .
66. Shahzadi G, Luqman A, Ali Al-Shamiri MM. The extended
MOORA method based on Fermatean fuzzy information. Math
Probl Eng. 2022;2022(1):7595872.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 1 5 5 / 2 0 2 2
/ 7 5 9 5 8 7 2     .
67. Cummins RG, Gong ZH, Reichert T. The impact of visual sexual
appeals on attention allocation within advertisements: an eye-
tracking study. Int J Advert. 2021;40(5):708–32.  h t t  p s : /  / d o  i . o  r g /
1 0 . 1 0 8 0 / 0 2 6 5 0 4 8 7 . 2 0 2 0 . 1 7 7 2 6 5 6     .
68. Gupta H, Singh S, Sinha P. Multimedia tool as a predictor for
social media advertising-a YouTube way. Multim Tools Appl.
2017;76:18557–68. https:/ /doi.or g/10.10 07/s1 1042-016-4249-6.
69. Hassan S, Nadzim SZA, Shiratuddin N. Strategic use of social
media for small business based on the AIDA model. Procedia Soc

1 3
  101  Page 28 of 29
Cognitive Computation (2026) 18:101
Behav Sci. 2015;172:262–9.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 1 6 / j . s b s p r o . 2 0 1
5 . 0 1 . 3 6 3     .
70. Su KW, Huang PH, Chen PH, Li YT. The impact of formats and
interactive modes on the effectiveness of mobile advertisements.
J Ambient Intell Humaniz Comput. 2016;7(6):817–27.  h t t  p s : /  / d o  i
. o  r g / 1 0 . 1 0 0 7 / s 1 2 6 5 2 - 0 1 6 - 0 3 4 3 - x     .
71. Pashootanizadeh M, Khalilian S. Application of the AIDA model:
Measuring the effectiveness of television programs in encouraging
teenagers to use public libraries. Inf Learn Sci. 2018;119(11):635–
51. https:/ /doi.or g/10.11 08/IL S-04-2018-0028.
72. Lee YI, Trim PR. Enhancing marketing provision through
increased online safety that imbues consumer confidence: cou -
pling AI and ML with the AIDA model. Big Data Cogn Comput.
2022;6(3):78. https:/ /doi.or g/10.33 90/bd cc6030078.
73. Sharifi M, Pool JK, Jalilvand MR, Tabaeeian RA, Jooybari MG.
Forecasting of advertising effectiveness for renewable energy
technologies: a neural network analysis. Technol Forecast Soc
Change. 2019;143:154–61.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 1 6 / j . t e c h f o r e . 2 0
1 9 . 0 4 . 0 0 9     .
74. Myers SD, Deitz GD, Huhmann BA, Jha S, Tatara JH. An eye-
tracking study of attention to brand-identifying content and recall
of taboo advertising. J Bus Res. 2020;111:176–86.  h t t  p s : /  / d o  i . o  r g
/ 1 0 . 1 0 1 6 / j . j b u s r e s . 2 0 1 9 . 0 8 . 0 0 9     .
75. Nasir V A, Keserel AC, Surgit OE, Nalbant M. Segmenting con-
sumers based on social media advertising perceptions: How does
purchase intention differ across segments? Telematics Inform.
2021;64:101687. https:/ /doi.or g/10.10 16/j. tele.2021.101687.
76. Lin J, Zhou M, Ma Y , Gao Y , Fei C, Chen Y et al. Autoposter: A
highly automatic and content-aware design system for advertising
poster generation. In:Proceedings of the 31st ACM International
Conference on Multimedia; 2023. p. 1250–1260.  h t t  p s : /  / d o  i . o  r g / 1
0 . 1 1 4 5 / 3 5 8 1 7 8 3 . 3 6 1 1 9 3 0     .
77. Chen W, Yang J, Wang Y . The influence of Chinese typography
on information dissemination in graphic design: based on eye-
tracking data. Sci Rep. 2024;14(1):13947.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 3
8 / s 4 1 5 9 8 - 0 2 4 - 6 4 9 6 4 - y     .
78. Wong BY , Shih KT, Liang CK, Chen HH. Single image realism
assessment and recoloring by color compatibility. IEEE Trans
Multimedia. 2012;14(3):760–9.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 1 0 9 / T M M . 2 0
1 2 . 2 1 8 8 9 9 7     .
79. Ulrich P. Integrative economic ethics: foundations of a civilized
market economy. Cambridge University Press; 2008.
80. Husted BW, Allen DB. Is it ethical to use ethics as strategy? J Bus
Ethics. 2000;27:21–31.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 2 3 / A : 1 0 0 6 4 2 2 7 0 4 5 4 8     .
81. Morsing M. Corporate social responsibility as strategic auto-
communication: on the role of external stakeholders for member
identification. Bus Ethics A Eur Rev. 2006;15:171–82.  h t t  p s : /  / d o  i
. o  r g / 1 0 . 1 1 1 1 / j . 1 4 6 7 - 8 6 0 8 . 2 0 0 6 . 0 0 4 4 0 . x     .
82. Mpinganjira M, Maduku DK. Ethics of mobile behavioral adver-
tising: antecedents and outcomes of perceived ethical value of
advertised brands. J Bus Res. 2019;95:464–78.  h t t  p s : /  / d o  i . o  r g / 1 0
. 1 0 1 6 / j . j b u s r e s . 2 0 1 8 . 0 7 . 0 3 7     .
83. Bošković S, Švadlenka L, Jovčić S, Dobrodolac M, Simić V ,
Bačanin N. An alternative ranking order method accounting for
two-step normalization (AROMAN)–a case study of the electric
vehicle selection problem. IEEE Access. 2023;11:39496–507.
https:/ /doi.or g/10.11 09/AC CESS.2023.3265818.
84. Pamucar D, Simic V , Görçün ÖF, Küçükönder H. Selection of
the best Big Data platform using COBRAC-ARTASI method -
ology with adaptive standardized intervals. Expert Syst Appl.
2024;239:122312. https:/ /doi.or g/10.10 16/j. eswa.2023.122312.
85. Pamucar D, Ćirović G. The selection of transport and handling
resources in logistics centers using Multi-Attributive Border
Approximation area Comparison (MABAC). Expert Syst Appl.
2015;42(6):3016–28.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 1 6 / j . e s w a . 2 0 1 4 . 1 1 . 0 5 7     .
86. Stević Ž, Pamučar D, Puška A, Chatterjee P. Sustainable supplier
selection in healthcare industries using a new MCDM method:
measurement of alternatives and ranking according to COmpro -
mise solution (MARCOS). Comput Ind Eng. 2020;140:106231.
https:/ /doi.or g/10.10 16/j. cie.2019.106231.
87. Chakraborty S, Zavadskas EK. Applications of WASPAS method
in manufacturing decision making. Informatica (Vilnius).
2014;25(1):1–20. https:   //d oi. or g/10. 153 88/Infor mati ca.2014.01.
Publisher's Note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional affiliations.

1 3
Page 29 of 29   101
Cognitive Computation (2026) 18:101
Authors and Affiliations
Elif Akagün1  · Galip Cihan Yalçın2  · Karahan Kara3,2,4  · Pınar Aytekin5  · Tuğçe Çelik6  · Vladimir Simic7,8,9 ·
Dragan Pamucar10
 Vladimir Simic
vsima@sf.bg.ac.rs
Elif Akagün
elif.akagun@ostimteknik.edu.tr
Galip Cihan Yalçın
galipcihan.yalcin@ostimteknik.edu.tr
Karahan Kara
karahan.kara@ikcu.edu.tr
Pınar Aytekin
pinar.aytekin@idu.edu.tr
Tuğçe Çelik
tugce.celik@ostimteknik.edu.tr
Dragan Pamucar
dragan.pamucar@gmail.com
1 Department of Marketing, OSTIM Technical University,
06374 Ankara, Türkiye
2 Department of Business, Faculty of Economics and
Administrative Sciences, OSTIM Technical University,
06374 Ankara, Türkiye
3 Department of Data Science and Analytics, Faculty of
Economics and Administrative Sciences, İzmir Katip Çelebi
University, 35620 İzmir, Türkiye
4 Department of Engineering, Saveetha School of Engineering,
Saveetha Institute of Medical and Technical Sciences,
SIMATS, Chennai, India
5 Department of Business, Faculty of Economics and
Administrative Sciences, İzmir Democracy University,
35140 İzmir, Türkiye
6 Department of Interior Architecture and Environmental
Design, Faculty of Architecture and Design, OSTIM
Technical University, 06374 Ankara, Türkiye
7 Faculty of Transport and Traffic Engineering, University of
Belgrade, V ojvode Stepe 305, 11010 Belgrade, Serbia
8 College of Engineering, Department of Industrial
Engineering and Management, Yuan Ze University,
Taoyuan City 320315, Taiwan
9 Department of Computer Science and Engineering, College
of Informatics, Korea University, 145 Anam-Ro, Seongbuk-
Gu, Seoul 02841, Republic of Korea
10 Transport and Logistics Competence Centre, Vilnius
Gediminas Technical University, Vilnius, Lithuania
