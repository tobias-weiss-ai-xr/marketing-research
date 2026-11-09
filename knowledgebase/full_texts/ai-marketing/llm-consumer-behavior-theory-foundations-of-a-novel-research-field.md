---
title: 'LLM Consumer Behavior Theory: Foundations of a Novel Research Field'
url: https://arxiv.org/abs/2606.18005
category: ai-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Manon Reusens
- Sofie Goethals
- David Martens
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.18005
pages: 7
chars: 29469
fetched_at: '2026-11-08T13:00:58+00:00'
kb_version: 1
---

# LLM Consumer Behavior Theory: Foundations of a Novel Research Field

LLM Consumer Behavior Theory: Foundations of a Novel Research Field
Manon Reusens1*, Sofie Goethals1*, David Martens1
1Department of Engineering Management, University of Antwerp
{manon.reusens, sofie.goethals, david.martens}@uantwerpen.be
Abstract
Large language models (LLMs) are increas-
ingly deployed as autonomous agents that make
consumption decisions on behalf of users. This
shift raises fundamental questions for consumer
theory, which has traditionally modeled hu-
mans as the primary decision-makers. In this
paper, we introduceLLM Consumer Behav-
ior Theory, a new field of study concerned
with analyzing consumer behavior in agentic
markets. Drawing on classical and behavioral
economics alongside recent advances in Nat-
ural Language Processing, we formalize how
human preferences are reflected and acted upon
by LLM-based agents, and how agent-level
decisions aggregate into market demand. We
unify previously fragmented literature on LLM
decision-making, human behavior simulation,
and preference elicitation under a common eco-
nomic lens, highlighting where assumptions,
such as rationality and heterogeneity, may fail
in agentic markets. Rather than providing em-
pirical validation, this paper outlines the scope
of LLM consumer behavior and identifies open
research questions related to alignment, prefer-
ence representation, and market dynamics.
1 Introduction
AI systems have undergone a shift from passive
conversational tools toagenticAI systems that in-
creasingly make decisions on our behalf (Gaarlandt
et al., 2025; Purdy, 2024; Goli and Singh, 2024).
These emerging AI agents can proactively plan,
evaluate alternatives, and execute complex tasks
across domains (Acharya et al., 2025; Whiting,
2024). From an economic point of view, these
systems are a new type of actors increasingly mak-
ing purchasing decisions on our behalf (Cherep
et al., 2025a). This is also highlighted by the an-
ticipated growth of agentic commerce: McKinsey
Research, for example, estimates that by 2030 agen-
tic commerce could orchestrate $ 3 to $ 5 trillion
*Equal contribution
globally (Schumacher et al., 2025). Accordingly,
classical economic frameworks that solely model
individuals as decision-makers must evolve to ac-
count for agentic systems acting on behalf of users.
This paper introducesLLM Consumer Behav-
ior Theory, a new research field concerned with
consumption decisions made by LLM-based agents
acting on behalf of human users. By integrating
insights from classical consumer behavior theory,
behavioral economics, and Natural Language Pro-
cessing (NLP), we unify previously fragmented lit-
erature under a common economic framework, es-
tablishing a coherent foundation for studying agen-
tic consumer behavior. Rather than exhaustively
characterizing all implications of this emerging do-
main, we outline the scope and core conceptual
structure of LLM consumer behavior, clarify how
existing empirical findings fit within it, and identify
central open questions that arise when consumer
decision-making is delegated to algorithmic agents.
The paper is organized around three core com-
ponents of LLM Consumer Behavior Theory, sum-
marized in Figure 1. First, we ground(LLM) con-
sumer preferencesin classical utility theory and
behavioral economics, analyzing how choices arise
from preferences, constraints, and cognitive biases.
Second, we studythe user–agent alignment, for-
malizing how consumer preferences are reflected
in LLM-based agents through an agent–principal
perspective. Third, we turn toconsumer markets,
aggregating agent-level decisions to characterize
agentic demand and exploring how heterogeneity
and market dynamics might be affected in compar-
ison to human consumer markets, and how align-
ment and diversification can mitigate these effects.
2 Consumer preferences and utility
This section reviews the principal theories used to
modelindividualconsumers, and discusses related
work on how these frameworks have been applied
1
arXiv:2606.18005v1  [cs.AI]  16 Jun 2026

User Profile
Consumption levels (x)
Budget Constraints (a)
U(x)=Vi + ϵ i
with: px<=aCognitive
Biases
U(x)=Vi + ϵ i
with: px<=a
Cognitive Biases
Cognitive
Biases
User Profile
Consumption levels (x)
Budget Constraints (a)
Real Users Reflection Agent Instantiation
Agent Profile
Inherent choice
patterns
Lack of full rationality
Agentic Market
Aggregate
Agentic Demand
personalization
User-Agent Alignment
2
Figure 1: Field of LLM Consumer Behavior Theory. Consumers are modeled via preference structures. These
preferences are imperfectly reflected and instantiated in LLM agents. Each agent acts on behalf of a user, producing
agent-level choices that aggregate into market demand
in autonomous decision-making settings.
2.1 Model of Individual Choice
In classical economic theory, consumers are as-
sumed to choose the option that maximizes utility,
represented by U(x), where x is a set of consump-
tion levels, subject to a budget constraint px≤a
where p,where p is a set of prices and a is the in-
come of the consumer (McFadden, 2001). This
framework is commonly referred to as the rational
choice model (Ooghe et al., 2023). In practice, how-
ever, decision-making may also be influenced by
random factors, such as noise or bias. Therefore,
random utility theory was introduced to analyze
choices that maximize utility, while allowing for
random elements (McFadden, 2001). Utility is then
decomposed into a systematic part V and an error
term or unobservable partϵ(Masiero et al., 2015):
U(x) =V+ϵ(1)
Different models can approximate this utility func-
tion, such as the multinomial logit model or the
mixed logit model (Masiero et al., 2015; McFad-
den, 2001; Reusens et al., 2026)
Research in NLP has begun to study LLM choice
preferences in market-like settings. Cedro et al.
(2025) study a series of real-world dilemmas, such
as whether to accept a discount in exchange for
longer waiting times, and map the resulting prefer-
ences of several LLMs. They find that smaller and
older models exhibit less consistent preferences,
whereas larger and more recent models display
sharper and more stable patterns. Related studies
consider other forms of LLM decision-making, in-
cluding preferences over time (Goli and Singh,
2024), risk (Jia et al., 2024), or walking dis-
tance (Fulman et al., 2025). From an economic
perspective, Reusens et al. (2026) use a discrete
choice method to estimate Willingness to Pay for
hotel room features.1.
2.2 Behavioral Economics
Classical economic theory treats the systematic
component of human decision-making as rational.
Yet even within this component, people are influ-
enced by behavioral biases and do not behave fully
rationally. Deviations include loss aversion, anchor-
ing, overconfidence, and framing effects (Tversky
and Kahneman, 1979; Kahneman, 2011).
LLM RationalityJiang (2025) characterizes a
rational agent using four main axioms: informa-
tion grounding, logical consistency, invariance
from irrelevant context, and orderability of pref-
erences. Evidence suggests that LLMs do not
fully satisfy these criteria, due in part to incon-
sistent outputs, a bounded knowledge space, and
their lack of direct real-world grounding and feed-
back mechanisms (Jiang et al., 2025). At the
same time, some evidence of economic rational-
ity is found, although these are highly sensitive
1The maximum willingness to pay signals that the con-
sumer is indifferent between buying or not buying the prod-
uct (Ooghe et al., 2023)
2

to prompt variations (Chen et al., 2023). A grow-
ing body of work thus investigates how rationality
can be improved through, for example multimodal
systems, integrated tool use, or additional align-
ment (Jiang, 2025; Liu et al., 2025a). However,
these approaches do not yet succeed in making
LLMs fully rational (Jiang, 2025; Liu et al., 2025a).
LLM cognitive biasesBeyond violations of ra-
tionality, research examines whether LLMs exhibit
systematic behavioral deviations similar to those
observed in humans (Liu et al., 2025a; Jones and
Steinhardt, 2022; Jia et al., 2024). These mod-
els apply higher discount rates than humans in in-
tertemporal tasks while simultaneously producing
more internally consistent choices in gambling-like
settings (Goli and Singh, 2024; Liu et al., 2025b).
Jones and Steinhardt (2022) show that prompt de-
signs inspired by human cognitive biases can reli-
ably induce systematic errors. Additionally, both
risk and loss aversion are present within LLMs,
though the degree is model-dependent (Jia et al.,
2024) and LLMs are more susceptible to nudges
than humans (Cherep et al., 2025b). In general,
LLMs exhibit a range of behaviors between these
human biases and more economically rational deci-
sions (Chen et al., 2023; Raman et al., 2024; Ross
et al., 2024; Bini et al., 2025; Lou and Sun, 2026).
3 User-Agent Alignment
In agentic markets, LLMs make decisions on be-
half of users, requiring alignment with user prefer-
ences. Assuming one agent per user, this setting
maps onto the classical principal-agent problem,
where decision authority is delegated under imper-
fect information and potentially divergent objec-
tives (Grossman and Hart, 1983). Users delegate
decisions to LLMs expecting that these systems
act in their best interest. Yet LLMs are shaped by
the design choices of their developers, which can
lead to misalignment between model behavior and
the behavior that a user might seek, as shown by
Fan et al. (2024) and Reusens et al. (2025). Ad-
ditionally, LLMs do not directly observe true user
preferences, but rely on proxy representations in-
ferred from prompts, context history, past behavior,
and available demographic information (Figure 1).
Persona-based alignmentResearch studies the
use of LLMs to simulate human behavior (Wang
et al., 2025b; Yoon et al., 2024; Kim et al., 2026;
Horton et al., 2023). A popular approach for im-
proving human alignment ispersonaassignment:
instructing an LLM to “act as" a user with spe-
cific characteristics or preferences (Wang et al.,
2025b). Personas can also be based on behavioral
rather than demographic attributes (Goethals et al.,
2025). While persona assignment can improve
alignment in simple tasks (Liu et al., 2025a), it also
has important limitations: models may not follow
assigned personas consistently (Horton et al., 2023;
Reusens et al., 2025), especially when asked to fol-
low uncommon preferences (Fan et al., 2024), and
may behave stereotypically (Wang et al., 2025a;
Reusens et al., 2025). Lastly, careful persona de-
sign is required as it could lead to extreme model
behavior (Reusens et al., 2026).
Alignment through few-shot learning and fine-
tuningA complementary line of work studies
whether LLM-based agents can learn individual
preferences from limited interaction data. Several
papers use in-context-learning from past choices
i.e. (Kim et al., 2026; Singh et al., 2025; Reusens
et al., 2026). Other papers finetune a user-specific
personalized model i.e. (Thonet et al., 2025). How-
ever, full fine-tuning per user can be costly and
hard to scale. Therefore, more efficient methods
are also proposed, such as LoRe, that models in-
dividual preferences as weighted combinations of
base reward functions (Bose et al., 2025).
4 Consumer Markets
If everyone uses an agent as their proxy, a fully
agentic consumer market would emerge, as shown
in Figure 1. In microeconomics, consumer’s Will-
ingness to Pay values constitute the demand gov-
erned by theLaw of Demand: as the quantity sold
increases, the price must fall to attract additional
buyers (Marshall et al., 1961). In agentic markets,
aggregating individual agentic willingness to pay
values across this population thus yields the agentic
market demand curve.
4.1 The Heterogeneous User Demand
Individual human choices are driven by utility,
which depends on factors such as preferences and
income (Marshall et al., 1961) but also on unob-
served dimensions such as tastes and perceptions
of the world (McFadden, 2001). As a result, tradi-
tional consumer markets are characterized by sub-
stantial heterogeneity in preferences reflecting dif-
ferences in income, taste, and lived experiences.
This heterogeneity is a central feature of economic
3

models, as variation across individuals shapes both
market outcomes and welfare implications (McFad-
den, 1972; Berry et al., 1993).
4.2 The Homogenous Agentic Demand
Heterogeneity may be reduced in agentic markets,
since LLMs tend to reproduce average patterns
from their training data rather than diverse hu-
man preferences (Bender et al., 2021; Matz et al.,
2025). This effect may be reinforced by the con-
centrated LLM ecosystem, in which state-of-the-
art models rely on largely overlapping corpora,
similar architectures, and related alignment pro-
cedures (Bommasani et al., 2021; Intel Market
Research, 2024). Although homogenization has
been documented in other downstream applica-
tions (Weidinger et al., 2021; Shumailov et al.,
2024; Goethals and Rhue, 2025), its implications
for consumer markets and aggregate demand re-
main underexplored. Early evidence suggests that
agentic demand may be more homogeneous than
human demand: LLMs show more uniform out-
of-the-box choice patterns (Chen et al., 2023), AI
agents can concentrate demand on a few “modal”
products (Allouah et al., 2025), and LLM behav-
ior appears less heterogeneous than human behav-
ior (del Rio-Chanona et al., 2025). These prefer-
ences may also be unstable, with model updates
substantially shifting market shares (Allouah et al.,
2025).
4.3 Diversifying the Agentic Demand
Agentic heterogeneity can still arise from both
model-side and user-side factors. On the model
side, architectural differences across foundation
models can lead to different decisions or price
boundaries (Reusens et al., 2026; Cedro et al.,
2025), and higher temperature settings can also
induce response diversity (Chen et al., 2023). On
the user side, aligning agents to specific user pro-
files can further diversify behavior, as discussed
in Section 3. For example, LLMs can behave like
heterogeneous households when assigned different
profiles, occupations, and income levels, generat-
ing consumption patterns consistent with macroe-
conomic regularities (Li et al., 2024).
5 Discussion
A central implication of LLM Consumer Behavior
Theory is that consumer analysis can no longer
focus solely on human users. When decisions
are delegated to LLM-based agents, market out-
comes reflect a broader pipeline involving pref-
erence reflection, initial agentic preferences, and
user–agent alignment (Figure 1). Understanding
behavior along this continuum is therefore critical
for analyzing emerging consumer markets, moti-
vating several directions for future research.
LLM choice patternsA first key direction con-
cerns LLM choice patterns. What factors influence
the choices these models make? How robust and
consistent are these choices across models, settings
and prompts? To what extent can they be influ-
enced or steered, either through prompting strate-
gies or through modifications to the model itself?
Personalized agentsA second direction con-
cerns aligning agents with unique user preferences.
Which data sources and alignment mechanisms
best capture true user preferences? How do reflec-
tion errors or biases propagate from agent decisions
to market-level distortions? Can shared agents ef-
fectively serve heterogeneous users without dis-
advantaging minority groups, or does meaningful
alignment require individualized models?
Hybrid MarketsRather than an abrupt shift,
consumer markets are likely to evolve gradually
from human-driven to increasingly agentic systems,
creating hybrid market structures. Open questions
include the pace of this transition, the dynamics of
hybrid markets, and whether shared model weights
could induce preference homogenization without
collusion. What risks arise when large populations
of agents update simultaneously, and how will hu-
man consumers adapt to the growing concentration
of agentic decision-making? How are prices and
equilibria affected in hybrid markets?
6 Conclusion
This paper introducesLLM Consumer Behav-
ior Theory, which studies consumption decisions
made by LLM-based agents acting on behalf of hu-
man users. As consumer decision-making becomes
increasingly agentic, market behavior can no longer
be understood solely through human preferences.
By grounding this in classical and behavioral con-
sumer theory and linking it to recent advances in
NLP, we clarify how empirical findings on LLM be-
havior map to established economic concepts and
why agentic consumption raises new challenges
of alignment and heterogeneity. We delineate the
4

scope of this emerging field and identify founda-
tional questions for future research.
Limitations
As noted, the primary aim of this paper is to intro-
duce LLM Consumer Behavior Theory as a novel
field of study, rather than to provide empirical vali-
dation, which we leave to future work. Our analy-
sis is further limited to the demand side of agentic
markets; extending these ideas to agentic supply,
and to settings in which both supply and demand
are partially agentic, raises additional questions for
future research. Finally, we do not attempt an ex-
haustive review of all related literature. Instead, we
synthesize insights across economics and NLP to
offer a structured perspective on agentic consumer
behavior.
Ethical Considerations
Analyzing agentic consumer markets also raises
several ethical considerations. A central issue con-
cernsaccountabilitywhen LLMs make decisions
on behalf of users. Who is to blame for a poor de-
cision? Currently, there is no global consensus for
this question (Schumacher et al., 2025). Individuals
should provide informed consent and understand
to what extent they remain responsible for agentic
choices. This concern extends beyond fully au-
tonomous settings to cases where users explicitly
approve recommendations, as approving a sugges-
tion generated by an LLM involves more cognitive
engagement and deliberation than making the deci-
sion independently. Additional ethical risks arise
when agents are misaligned with user preferences
and exhibit stereotypical or biased behavior. Fi-
nally, the complexity of LLMs limits transparency
into their underlying decision-making processes.
Addressing these challenges represents an impor-
tant direction for future research.
Acknowledgments
We would like to thank the Antwerp Center on
Responsible AI (ACRAI) for their support.
References
Deepak Bhaskar Acharya, Karthigeyan Kuppan, and
B Divya. 2025. Agentic ai: autonomous intelligence
for complex goals - a comprehensive survey.IEEE
Access.
Amine Allouah, Omar Besbes, Josué Figueroa, Yash
Kanoria, and Akshit Kumar. 2025. What is your ai
agent buying? evaluation, implications, and emerg-
ing questions for agentic e-commerce.Evaluation,
Implications, and Emerging Questions for Agentic
E-Commerce (August 04, 2025).
Emily M Bender, Timnit Gebru, Angelina McMillan-
Major, and Shmargaret Shmitchell. 2021. On the
dangers of stochastic parrots: Can language models
be too big? InProceedings of the 2021 ACM confer-
ence on fairness, accountability, and transparency,
pages 610–623.
Steven T Berry, James A Levinsohn, and Ariel Pakes.
1993. Automobile prices in market equilibrium: Part
i and ii.
Pietro Bini, Lin William Cong, Xing Huang, and
Lawrence J Jin. 2025. Behavioral economics of
ai: Llm biases and corrections.Available at SSRN
5213130.
Rishi Bommasani, Drew A Hudson, Ehsan Adeli, Russ
Altman, Simran Arora, Sydney von Arx, Michael S
Bernstein, Jeannette Bohg, Antoine Bosselut, Emma
Brunskill, and 1 others. 2021. On the opportuni-
ties and risks of foundation models.arXiv preprint
arXiv:2108.07258.
Avinandan Bose, Zhihan Xiong, Yuejie Chi, Si-
mon Shaolei Du, Lin Xiao, and Maryam Fazel. 2025.
Lore: Personalizing LLMs via low-rank reward mod-
eling. InSecond Conference on Language Modeling.
Mateusz Cedro, Timour Ichmoukhamedov, Sofie
Goethals, Yifan He, James Hinns, and David Martens.
2025. Cash or comfort? how llms value your incon-
venience.arXiv preprint arXiv:2506.17367.
Yiting Chen, Tracy Xiao Liu, You Shan, and 1 oth-
ers. 2023. The emergence of economic rationality
of GPT.Proceedings of the National Academy of
Sciences, 120(51).
Manuel Cherep, Chengtian Ma, Abigail Xu, Maya
Shaked, Patricia Maes, and Nikhil Singh. 2025a. A
framework for studying ai agent behavior: Evidence
from consumer choice experiments. InNeurIPS 2025
Workshop on Bridging Language, Agent, and World
Models for Reasoning and Planning.
Manuel Cherep, Pattie Maes, and Nikhil Singh. 2025b.
Llm agents are hypersensitive to nudges.arXiv
preprint arXiv:2505.11584.
R Maria del Rio-Chanona, Marco Pangallo, and Cars
Hommes. 2025. Can generative ai agents behave like
humans? evidence from laboratory market experi-
ments.arXiv preprint arXiv:2505.07457.
Caoyun Fan, Jindou Chen, Yaohui Jin, and Hao He.
2024. Can large language models serve as ratio-
nal players in game theory? a systematic analysis.
Proceedings of the AAAI Conference on Artificial
Intelligence, 38(16):17960–17967.
5

Nir Fulman, Abdulkadir Memduho˘glu, and Alexander
Zipf. 2025. Utilizing large language models to simu-
late parking search.Transportation Research Part A:
Policy and Practice, 199:104542.
Jur Gaarlandt, Wesley Korver, Nathan Furr, and 1 oth-
ers. 2025. Ai agents are changing how people shop.
here’s what that means for brands.Harvard Business
Review.
Sofie Goethals, Johannes Luther, and Sandra Matz.
2025. Words reveal wants: How well can simple
llm-based ai agents replicate people’s choices based
on their social media posts. InAdjunct Proceed-
ings of the 33rd ACM Conference on User Modeling,
Adaptation and Personalization, pages 126–131.
Sofie Goethals and Lauren Rhue. 2025. One world, one
opinion? the superstar effect in llm responses. In
Proceedings of the 3rd Workshop on Cross-Cultural
Considerations in NLP (C3NLP 2025), pages 89–
107.
Ali Goli and Amandeep Singh. 2024. Frontiers: can
large language models capture human preferences?
Marketing Science, 43(4):709–722.
Sanford J. Grossman and Oliver D. Hart. 1983. An anal-
ysis of the principal-agent problem.Econometrica,
51(1):7–45.
John J Horton, Apostolos Filippas, and Benjamin S
Manning. 2023. Large language models as simulated
economic agents: What can we learn from homo sili-
cus? Technical report, National Bureau of Economic
Research.
Intel Market Research. 2024. Large language model
(LLM) market report 2024–2030, by model architec-
ture, geo, tech. Accessed: April 17, 2026.
Jingru Jia, Zehua Yuan, Junhao Pan, Paul E McNamara,
and Deming Chen. 2024. Decision-making behav-
ior evaluation framework for llms under uncertain
context.Advances in neural information processing
systems, 37:113360–113382.
Bowen Jiang, Yangxinyu Xie, Xiaomeng Wang, Yuan
Yuan, Zhuoqun Hao, Xinyi Bai, Weijie J Su,
Camillo Jose Taylor, and Tanwi Mallick. 2025. To-
wards rationality in language and multimodal agents:
A survey. InProceedings of the 2025 Conference
of the Nations of the Americas Chapter of the Asso-
ciation for Computational Linguistics: Human Lan-
guage Technologies (Volume 1: Long Papers), pages
3656–3675, Albuquerque, New Mexico. Association
for Computational Linguistics.
Jingjing Jiang. 2025. Towards human-like dialogue
systems: Integrating multimodal emotion recognition
and non-verbal cue generation. InProceedings of the
21st Workshop of Young Researchers’ Roundtable
on Spoken Dialogue Systems, pages 15–17, Avignon,
France. Association for Computational Linguistics.
Erik Jones and Jacob Steinhardt. 2022. Capturing fail-
ures of large language models via human cognitive
biases.Advances in Neural Information Processing
Systems, 35:11785–11799.
Daniel Kahneman. 2011.Thinking, Fast and Slow. Far-
rar, Straus and Giroux.
Jeongbin Kim, Matthew Kovach, Kyu-Min Lee, Eu-
ncheol Shin, and Hector Tzavellas. 2026. Can an
llm learn preferences from choice data?Preprint,
arXiv:2401.07345.
Nian Li, Chen Gao, Mingyu Li, Yong Li, and Qing-
min Liao. 2024. EconAgent: Large language model-
empowered agents for simulating macroeconomic ac-
tivities. InProceedings of the 62nd Annual Meeting
of the Association for Computational Linguistics (Vol-
ume 1: Long Papers), pages 15523–15536, Bangkok,
Thailand. Association for Computational Linguistics.
Jiaxin Liu, Yixuan Tang, Yi Yang, and Kar Yan Tam.
2025a. Evaluating and aligning human economic
risk preferences in LLMs. InProceedings of the
2025 Conference on Empirical Methods in Natural
Language Processing, pages 18174–18188, Suzhou,
China. Association for Computational Linguistics.
Ryan Liu, Jiayi Geng, Joshua Peterson, and 1 others.
2025b. Large language models assume people are
more rational than we really are. InThe Thirteenth
International Conference on Learning Representa-
tions.
Jiaxu Lou and Yifan Sun. 2026. Anchoring bias in large
language models: An experimental study.Journal of
Computational Social Science, 9(1):11.
Alfred Marshall, Claude William Guillebaud, and 1
others. 1961.Principles of economics, volume 1.
Springer.
Lorenzo Masiero, Cindy Yoonjoung Heo, and Bing Pan.
2015. Determining guests’ willingness to pay for
hotel room attributes with a discrete choice model.
International Journal of Hospitality Management,
49:117–124.
Sandra C Matz, C Blaine Horton, and Sofie Goethals.
2025. The basic b*** effect: The use of llm-based
agents reduces the distinctiveness and diversity of
people’s choices.arXiv preprint arXiv:2509.02910.
Daniel McFadden. 1972. Conditional logit analysis of
qualitative choice behavior.
Daniel McFadden. 2001. Economic choices.American
economic review, 91(3):351–378.
Erwin Ooghe, Tom Verbeke, Karolien De Bruyne, Si-
mon De Jaeger, Hans Degryse, Johan Eyckmans,
Marjan Maes, Nicky Rogge, Patrick Van Cayseele,
Stijn Vanormelingen, Dieter Verhaest, and Andreé’
Watteyne. 2023.Economie: Een inleiding, negende
uitgave edition. Acco, Leuven.
6

Mark Purdy. 2024. What is agentic ai, and how will it
change work?Harvard Business Review.
Narun Raman, Taylor Lundy, Samuel Amouyal, and
1 others. 2024. Steer: assessing the economic ra-
tionality of large language models.Preprint at
https://arxiv.org/pdf/2402.09552.
Manon Reusens, Bart Baesens, and David Jurgens. 2025.
Are economists always more introverted? analyz-
ing consistency in persona-assigned LLMs. InFind-
ings of the Association for Computational Linguistics:
EMNLP 2025, pages 11268–11287, Suzhou, China.
Association for Computational Linguistics.
Manon Reusens, Sofie Goethals, Toon Calders, and
David Martens. 2026. Would a large language model
pay extra for a view? inferring willingness to pay
from subjective choices.Expert Systems with Appli-
cations, page 133279.
Jillian Ross, Yoon Kim, and Andrew Lo. 2024. Llm
economicus? mapping the behavioral biases of llms
via utility theory. InFirst Conference on Language
Modeling.
Katharina Schumacher, Roger Roberts, and Katharina
Giebel. 2025. The agentic commerce opportunity:
How ai agents are ushering in a new era for con-
sumers and merchants. Report.
Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas
Papernot, Ross Anderson, and Yarin Gal. 2024. Ai
models collapse when trained on recursively gener-
ated data.Nature, 631(8022):755–759.
Anikait Singh, Sheryl Hsu, Kyle Hsu, Eric Mitchell, Ste-
fano Ermon, Tatsunori Hashimoto, Archit Sharma,
and Chelsea Finn. 2025. Fspo: Few-shot prefer-
ence optimization of synthetic preference data in llms
elicits effective personalization to real users.arXiv
preprint arXiv:2502.19312.
Thibaut Thonet, Germán Kruszewski, Jos Rozen, Pierre
Erbacher, and Marc Dymetman. 2025. FaST:
Feature-aware sampling and tuning for personalized
preference alignment with limited data. InProceed-
ings of the 2025 Conference on Empirical Methods
in Natural Language Processing, pages 9341–9370,
Suzhou, China. Association for Computational Lin-
guistics.
Amos Tversky and Daniel Kahneman. 1979. Prospect
theory: An analysis of decision under risk.Econo-
metrica, 47(2):263–292.
Angelina Wang, Jamie Morgenstern, and John P Dick-
erson. 2025a. Large language models that replace
human participants can harmfully misportray and
flatten identity groups.Nature Machine Intelligence,
7(3):400–411.
Kuang Wang, Xianfei Li, Shenghao Yang, Li Zhou,
Feng Jiang, and Haizhou Li. 2025b. Know you first
and be you better: Modeling human-like user sim-
ulators via implicit profiles. InProceedings of the
63rd Annual Meeting of the Association for Compu-
tational Linguistics (Volume 1: Long Papers), pages
21082–21107, Vienna, Austria. Association for Com-
putational Linguistics.
Laura Weidinger, John Mellor, Maribeth Rauh, Conor
Griffin, Jonathan Uesato, Po-Sen Huang, Myra
Cheng, Mia Glaese, Borja Balle, Atoosa Kasirzadeh,
and 1 others. 2021. Ethical and social risks
of harm from language models.arXiv preprint
arXiv:2112.04359.
Kate Whiting. 2024. The rise of ‘ai agents’: what they
are and how to manage the risks.World Economic
Forum.
Se-eun Yoon, Zhankui He, Jessica Echterhoff, and Ju-
lian McAuley. 2024. Evaluating large language mod-
els as generative user simulators for conversational
recommendation. InProceedings of the 2024 Con-
ference of the North American Chapter of the Asso-
ciation for Computational Linguistics: Human Lan-
guage Technologies (Volume 1: Long Papers), pages
1490–1504, Mexico City, Mexico. Association for
Computational Linguistics.
7
