---
title: LLM-Agent Interactions on Markets with Information Asymmetries
url: https://arxiv.org/abs/2603.08853
category: consumer-behavior
subcategory: empirical
date: 2026-03
venue: ''
authors:
- Alexander Erlei
- Lukas Meub
source: arxiv
pdf_url: https://arxiv.org/pdf/2603.08853
pages: 36
chars: 76087
fetched_at: '2026-11-08T12:59:29+00:00'
kb_version: 1
---

# LLM-Agent Interactions on Markets with Information Asymmetries

LLM-Agent Interactions on Markets with
Information Asymmetries
Alexander Erlei, Lukas Meub
As AI agents increasingly act on behalf of human stakeholders in economic settings,
understanding their behavior in complex market environments becomes critical. This
article examines how Large Language Models coordinate on markets that are charac-
terized by information asymmetries and in which providers of services have incentives
to exploit that asymmetry for their own economic gain. To that end, we conduct simu-
lations with GPT-5.1 agents in credence goods markets, manipulating the institutional
framework (free market, verifiability, liability), LLM agent’s social preferences (default,
self-interested, inequity-averse, efficiency-loving), and reputation mechanisms across
one-shot and repeated 16-round interactions. In one-shot settings, LLM agents largely
fail to establish cooperation, with markets breaking down except under liability rules or
when experts have efficiency-loving preferences. Repeated interactions solve consumer
participation through competitive price reduction, but expert fraud remains entrenched
absent explicit other-regarding preferences. LLM consumers focus narrowly on price
levels rather than understanding strategic incentives embedded in markups, making them
vulnerable to exploitation. Compared to human experiments, LLM markets exhibit sub-
stantially higher consumer participation but much greater market concentration, lower
prices, and more polarized fraud patterns. The effect of institutions like verifiability and
reputation is also much more ambiguous. Surplus shifts dramatically toward consumers
under social-preference objectives. These findings suggest that institutional design for
AI agent markets requires fundamentally different approaches than those effective for
human actors, with social preference alignment emerging as the primary determinant of
market efficiency.
Keywords:expert services, credence goods, market design, Large Language Models, AI
agents, information asymmetry
Contact: alexander.erlei@wiwi.uni-goettingen.de, Georg-August-Universität Göttingen. We grate-
fully acknowledge financial support by the Federal Ministry of Education and Research, project "Handwerk
mit Zukunft (HaMiZu)" , grant number 02K20D001.
arXiv:2603.08853v1  [econ.GN]  9 Mar 2026

1. Introduction
Recent advances in (generative) artificial intelligence (AI) and strategic foundation models
suggest a world in which humans will increasingly rely on and delegate to autonomous AI
agents (Goktas et al. 2025; Imas, Lee, and Misra 2025; Ivanov et al. 2024). Already today it is
easy to imagine AI agents representing and acting on behalf of human stakeholders on, for
example, online marketplaces, shopping platforms, or when negotiating (digital) services.
In this paper, we examine current LLM (Large Language Model) capabilities to navigate
relatively complex market structures that are characterized by information asymmetries
between agents: credence goods markets (or markets for expert services). Credence
goods markets are important, because many important economic and social domains are
characterized by information advantages where superiorly informed sellers or suppliers
(here: experts) can exploit their informational advantage at the expense of consumers
(Dulleck and Kerschbamer 2006). Prominent examples include financial services, expert
advice, medical services, or legal services. Over the last 20 years, a lot of empirical field
research has revealed strong real-world inefficiencies, including widespread rates of
overcharging (i.e. charging for more services than provided) and under-treatment (i.e.
not solving the consumer’s problem or not satisfying the consumer’s demand)(Gottschalk,
Mimra, and Waibel 2020; Balafoutas et al. 2013; Kerschbamer, Neururer, and Sutter 2016,
2023; Balafoutas and Kerschbamer 2020; Schneider 2012). Importantly, these problems
are difficult to solve, because the information asymmetry precludes consumers from
disciplining experts through informed selection, and effective regulations such as liability
are often difficult or impossible to enforce (it is, for example, often impossible toprove
expert fraud or negligence). AI agents, however, may have the potential to alleviate these
information problems.
In contrast to human actors, current foundation models like LLMs have access to vast
amounts of expert knowledge. They are able to think strategically at scale, and learn from
real-time feedback. Recent work argues that human cognitive and informational restraints
may be a key driver of AI agent adoption (Shahidi et al. 2025). On the expert’s side, there are
already numerous examples of automated LLM-provided services, ranging from financial
services to medical advice, taxation services, and shopping assistants (Ayers et al. 2023;
Hirosawa et al. 2023; Nov, Singh, and Mann 2023; Zhao et al. 2024; Li et al. 2023; Oehler
and Horn 2024; Lai et al. 2024; Nay et al. 2024; Alarie, Niblett, and Yoon 2018; Reis, Reis,
and Kunde 2024; Shekar et al. 2024; Ayre, Cvejic, and McCaffery 2024; Leslie-Miller et al.
2024; Seabrooke et al. 2024; Schneiders et al. 2024). LLM providers such as OpenAI and
Anthropic offer explicit agent services, scaling up consumer access to LLM agents.
However, how well AI agents based on Large Language Models coordinate on markets
that operate under information asymmetry is an open question. There is considerable
debate about the capacity of AI agents such as LLMs – especially off-the-shelve ones – to
1

navigate complex economic environments (Felin and Holweg 2024; Valmeekam et al. 2023;
Raman et al. 2024), with several recent successful examples (Fish, Gonczarowski, and
Shorrer 2024; Deshpande and Jacobson 2026; Lopez-Lira 2025; Imas, Lee, and Misra 2025).
Laboratory experiments have consistently shown that humans struggle with the game
theory of credence goods markets, but may still achieve moderate levels of cooperation
through social preferences. AI agents could out-perform human stakeholders through
strategic price-setting (experts) and expectation forming (consumers) that alleviate the
threat of market unraveling. On the other hand, they may lack the advantage of mutually
beneficial (pro-) social preferences that allow humans to enter a reciprocal relationship
via initial trust (see e.g., Erlei 2025; Dvorak et al. 2025; Erlei and Rau 2026).
In this article, we present a sequence of simulations using GPT-5.1 in which LLM
experts interact with LLM consumers on standard experimental credence goods mar-
kets (Dulleck, Kerschbamer, and Sutter 2011). We consider both one-shot and repeated-
interaction market scenarios, and vary the institutional market framework (No Institution
vs. Verifiability vs. Liability), the LLMs social preferences (default model, self-interested,
inequity-averse, efficiency-loving), as well as the possibility of bilateral expert–consumer
reputation building to answer the following question:
•How do LLM AI agents coordinate on credence goods markets?
• How do social preferences and reputation affect agent behavior and market welfare?
The one-shot simulations show that LLM agents struggle to establish successful coopera-
tion under information asymmetry. In the absence of liability rules, only the efficiency-
loving LLM expert manages to consistently attract LLM consumers. However, it achieves
this through ruinously low prices. Still, it is the only configuration that always reaches
or beats the standard model’s welfare predictions. Liability solves the agentic credence
problem – like it does for humans – because experts are always forced to solve the con-
sumer’s problem, which guarantees full market participation. The default and the self-
interested LLM expert aim to defraud consumers when possible. Endowing LLM experts
with inequity-aversion or efficiency-loving preferences all but eliminates expert dishon-
esty. Going beyond singular interactions towards a repeated 16-round settings mostly
solves the market participation problem. In all configurations, a large majority of con-
sumers “learn” to enter the market over time. LLM consumer agents do not consider
expert incentives through markups, but enter when prices are low enough, which makes
them vulnerable to expert exploitation. LLM experts intend to defraud consumers in the
absence of explicit other-regarding preferences, and these tendencies are stable across
repeated interactions, indicating that LLM consumers do not discipline experts towards
honesty. When expert agents are inequity-averse, over-treatment increases substantially,
while almost no expert under-treats consumers. Efficiency-loving experts continue to
prioritize consumer’s welfare. Reputation has ambiguous effects on expert honesty, and
2

no discernible consistent effect on welfare. Often, but not always, it slightly reduces under-
treatment and over-charging, while increasing over-treatment. The effects are, however,
small. Because market efficiency hinges on consumer participation (solved) and expert
honesty (only affected by induced social preferences), verifiability does not perform better
than the unregulated free credence good market. Self-interested and default expert agents
converge towards states with low prices and continuous expert fraud, which hurts welfare
but still improves on the one-shot scenario. Inequity-averse and efficiency-loving agents
rarely defraud and thus induce additional welfare gains, which predominantly accrue
to consumers. Inequity-aversion avoids ruinous expert behavior, generating (slightly)
more equal outcomes. Comparing the results to human subject data from Dulleck, Ker-
schbamer, and Sutter (2011) reveals that LLM-agent markets exhibit substantially higher
consumer participation but much stronger seller concentration, lower prices, as well as
more polarized expert fraud and efficiency patterns. The positive treatment effects of
institutional interventions like reputation and verifiability are less stable than in human
experiments. Frequently, they reverse. In general, but especially under social-preference
objectives, surplus sharply shifts from sellers towards consumers.
2. Related Literature
This article is situated at the intersection of the literature on credence goods and the
literature about LLM agents in strategic economic settings. For human interactions, there
exists a large literature of laboratory and online experiments that gauge the efficiency of
credence goods markets across various institutional settings (Balafoutas and Kerschbamer
2020; Dulleck, Kerschbamer, and Sutter 2011; Balafoutas et al. 2023; Kerschbamer, Sut-
ter, and Dulleck 2017; Grosskopf and Sarin 2010; Beck et al. 2013; Balafoutas et al. 2015;
Kerschbamer, Sutter, and Dulleck 2017; Inderst, Khalmetski, and Ockenfels 2019; Kandul,
Lanz, and Reins 2023; Tracy, Schniter, and Zíka 2023; Mimra, Rasch, and Waibel 2016; Agar-
wal, Liu, and Prasad 2019; Erlei and Meub 2024; Kerschbamer, Neururer, and Sutter 2023;
Schneider, Meub, and Bizer 2021). Recently, Erlei (2025) has shown how pro-social human
experts can out-compete self-interested human experts by delegating their choices to an
LLM agent with a transparent, codified objective function. Furthermore, they show that
in the absence of transparent objective functions, human consumers trust LLM experts
less than human experts.
Since the introduction of LLMs, there has been a strong increase of articles studying
the strategic capabilities and tendencies of AI agents in economic settings (Zhang et al.
2024; Kasberger et al. 2023; Guo 2023; Schmidt et al. 2024; Rahwan et al. 2019). Deshpande
and Jacobson (2026) study large language models in oligopolistic Cournot markets. LLM
agents are capable of strategic decision-making, and exhibit tendencies for tacit collusion
(which has also been observed by Fish, Gonczarowski, and Shorrer (2024)). Imas, Lee, and
3

Misra (2025) allow humans to use LLM agents as instructed agents in a negotiation setting,
showing how (1) human personality traits affect agent behavior through instructions,
(2) social norms are replicated in agent interactions via, e.g., the prevalence of “fair
splits” , and (3) variance in outcomes increases. In Cohen et al. (2025), endowing LLMs
with personality traits significantly changes the behavioral dynamics in a negotiation
settings, and in Long et al. (2025), emotional expressions by AI agents affect economic
outcomes. These patterns are similar to our study, where we endow LLM agents with
different objective functions mirroring social preferences. Shah et al. (2025) replicate
several classic auction findings from human experiments using LLM agents. They also find
that prompting LLMs with appropriate mental models can substantially shift performance.
3. The Market
We analyze a standard credence goods problem as a (1) one-shot and (2) repeated-round
market (Dulleck, Kerschbamer, and Sutter 2011). Four experts compete over four con-
sumers. Consumers have a big problem with probabilityh = 0.5 or a small problem with
probability 1− h = 0.5. To solve their problem, consumers need to approach an expert.
After approaching an expert, they are committed to receive the recommended treatment
under the offered price. If the problem is solved, consumers receive a payoffV = 10. If
the problem is not solved, they earn nothing, and still pay their expert, resulting in a
net negative income. Consumers may choose to leave the market untreated and earn
an outside option σ= 1.6. Experts who attract no consumer earn 0. By assumption, in-
different consumers visit an expert and experts who are indifferent between dishonest
and honest behavior choose to be honest. Experts receive a costless diagnostic signal
with 100% accuracy for each consumer. Then, depending on treatment, they first choose
between a high cost treatment (HCT) and a low cost treatment (LCT), and subsequently
charge consumers for their service. The HCT solves both problems and costs the expert
¯c= 6, while the LCT only solves the small problem and costs the expert ¯c= 2. Experts set a
price pairP =( ¯p,
¯
p) at the beginning of each round where p∈{ 1, ..., 11}, with ¯p(HCT)≥
¯
p.
Furthermore, expert decision-making may be constrained by the institutional setting. We
consider three cases:
No Institution.There are no constraints on expert behavior. Experts are allowed to freely
choose between the two treatments (HCT, LCT) and the two prices ( ¯p,
¯
p) after diagnosing
consumers. Consumers know about the expert’s choice set. There are three ways to defraud
consumers: under-treatment (LCT if problem is big), over-treatment (HCT if problem is
small), over-charging (¯pafter choosing the LCT).
Verifiability .The implemented treatment is verifiable to consumers. Therefore, experts
must charge the price of their chosen treatment. If an expert chooses the HCT, they
must choose ¯p, if they choose the LCT, they must choose
¯
p. There are two kinds of fraud:
4

under-treatment, over-treatment.
Liability .Experts are liable and must solve the consumer’s problem. If an expert diagnoses
a big problem, they must choose the HCT. If an expert diagnoses a small problem, they can
freely choose between the HCT and the LCT. Furthermore, experts are free to choose either
price, irrespective of their treatment choice. There are two ways to defraud consumers:
over-treatment, over-charging.
In the one-shot simulations, there is only one interaction, and we do not manipulate
reputation because there is no future. In the repeated paradigm, experts and consumers
play for 16 rounds. Here, we differentiate betweenreputationandno reputation. Inno
reputation, consumers cannot identify individual experts across rounds, and thus, in
case of mis-treatment, cannot identify the dishonest expert for the subsequent choice.
Inreputation, experts are identifiable, and can therefore build a reputation for being
(dis-)honest with each individual consumer who approaches them. Reputation is always a
private signal, not a public signal.
3.1. Predictions
We first consider self-interested risk-neutral experts (Dulleck and Kerschbamer 2006) in
the one-shot setting (Erlei 2025). Theoretically, little changes under repeated interactions.
Experts compete to attract consumers. InNo Institution, the dominant payoff-maximizing
expert strategy for each approaching consumer is to choose the LCT and charge the
big price ¯p. Consumers anticipate this, and condition their approach choice solely on ¯p,
because they expect over-charging. Expected payoff is πc ni =( 1− h)∗( V − ¯p)− h¯p. Given
their outside option σ= 1.6, the consumer approaches an expert if ¯p≤ 3. Because experts
have an outside option of σ= 0, always choose the LCT, and always charge ¯p, experts
compete over consumers via prices as long as πe ni = ¯p− ¯c> 0, and therefore, ¯p≥ 3. Hence,
all experts chooseP={
¯
p, 3}1, which offers consumersπ c ni =2>1.6.
Prediction No Institution:Experts set prices such that ¯p= 3, consumers enter the market and
approach an expert. Consumers are under-treated if they have a big problem, and earn 2 on
average. Experts earn 1 on average. Total market income is 12.
InVerifiability, experts charge the treatment-specific price. Therefore, consumers
infer the expert’s intentions via the expert’s markups for each treatment. That is because
experts are always incentivized to use the treatment with the higher markup. There are
three possible markup scenarios: (i) ¯p− ¯c >
¯
p− ¯c; (ii) ¯p− ¯c < ¯ p− ¯c; (iii) ¯p− ¯c = ¯ p− ¯c. The respective expert choices anticipated by the consumer are (i) always HCT, (ii) always LCT,
and (iii) honest treatments (by assumption that experts are honest under indifference).
This leads to the following consumer profits: (i) πc v,hct = V − ¯p because the problem is
always solved, (ii)πc v,lct =( 1−h)V− ¯ p because the consumer earns nothing if they have a big
1
¯
pis undetermined
5

problem, and (iii) πc v,honest = V− ¯ p− h∆p . Because experts compete with one another, they choose the lowest possible prices that still beat their outside option of 0 while maximizing
expected consumer profits. For (i), that impliesP hct ={ ¯ p, 7} with πc v,hct = 3. For (ii), experts setP lct ={ 3, ¯p} and πc v,lct = 2. And in (iii), prices areP honest ={ 3, 7}, which offers
πc v,honest = V − ¯ p− h∆p= 5. Because πc v,honest >π c v,hct >π c v,lct , any expert who does not offer equal markups and thereby signals a commitment to honest treatment-behavior is
out-competed. Furthermore, due to competition, self-interested experts must set their
prices toP honest ={ 3, 7}. As soon as any expert sets higher prices, all other experts are
incentivized to lower their prices and attract all consumers.
Prediction Verifiability:Experts set equal markup pricesP ={ 3, 7}, provide honest treatments,
and earn on average 1. All consumers enter the market with average profits of 5. Total market
income is 24.
InLiability, experts are always incentivized to overcharge consumers. Consumers
therefore condition their behavior solely on ¯p. Consumers also know that their expected
profits are πc l = V− ¯p. Experts earn πe l = h(¯p− ¯c)+( 1− h)(¯p− ¯c). Self-interested experts set
the lowest prices that still beat their outside option because otherwise, the other experts
could attract all consumers by doing so. Therefore,P l ={ ¯ p, 5}withπ e l =1 andπ c l =5. Prediction Liability:Experts set pricesP ={
¯
p, 5}, always overcharge consumers, and earn on
average 1. All consumers enter the market with average profits of 5. Total market income is 24.
Without reputation, nothing changes in therepeatedmarket condition. Similarly,
when experts can build a private reputation with consumers, the same predictions apply,
asVerifiabilityandLiabilityare already efficiently solved and inNo Institution, reputation
is a bi-lateral signal, and consumers expect to be defrauded, whereby they only approach
experts iff ˆp≤ 3, who in turn must always choose the small treatment. Because consumers
do not observe experts’ behavior toward other consumers (no public reputation), under
the maintained assumptions (self-interested risk-neutral experts, complete information,
and a known finite horizonT = 16), reputation does not change the subgame-perfect
prediction relative to the one-shot stage game. The main reason is that the finite time
horizon incentivizes experts to defraud consumers in the last round. Hence, in round 15,
experts have no incentive to maintain their reputation, because consumers anticipate
fraud. However, in that case, experts also have no incentive to maintain their reputation
in round 14, because consumers expect that experts will act self-interested in round 15
and thus disregard reputation. Then, through backward induction, reputation does not
change the equilibrium path.
4. Experimental Design
The expert market simulations follow the same basic parameters and sequences as de-
scribed above. In each market, four LLM experts compete over four LLM consumers
6

in either a one-shot or a finite-horizon 16-round setting. The simulation follows a 3 (No
Institutionvs.Verifiabilityvs.Liability) × 2 (reputationvs.no reputation) × 4 (No Objective
vs. Self-Interested vs. Inequity-Averse vs. Efficiency-Loving) between-subjects design. For
one-shot, we omit the reputation conditions, and in the 16-round-setting, we omit the
Liabilitycondition as it already solves the credence problem in one-shot. In each one-shot
(repeated) condition, we simulate 50 (15) market interactions. The procedure is as follows:
1. All LLM-agents read through their role-specific instructions. Throughout, we only talk
about “Player A ” (expert) and “Player B” (consumer). 2. Both consumer and expert agents
answer a number of comprehension questions to validate their understanding of the task.
3. All expert agents simultaneously setP ={ ¯p,
¯
p}. 4. Following the strategy method, all
expert agents learn the problem of all consumers and make 4 subsequent treatment and
price-charging decisions, depending on treatment. 5. All consumer agents see prices of all
four experts and choose which expert to approach, or to leave the market and earn their
outside option σ= 1.6. 6. In repeated, consumers and experts learn about their payoff.
During the repeated market interactions, all LLMs have access to a personalized history
that cumulatively documents (i) expert prices, the approach decision and the respective
payoff for consumers and (ii) expert prices, the number of attracted consumers, and
payoffs for experts. The instructions inform all LLM agents that they are playing with 7
other AI agents.
Technical Implementation.We use a combination of Python, Expected Parrot and the
LLM GPT 5.1 by OpenAI, accessed through APIs. 2 GPT-5.1 is a frontier model that is
available to free users and correctly answers all comprehension questions after reading
the instructions, follows sound reasoning when commenting on its decisions, and is
relatively robust to slight changes in language. 3 The instructions are implemented as
a system prompt, such that each LLM agent can always access them. Following prior
experimental work, we added a user prompt for chain-of-thought reasoning and planning
Wei et al. (2022), that told the LLM to "pretend like you are a participant of your specific
role and can make choices in this experiment. Do not break character. Find a strategy
to play this game yourself and plan ahead" . To manipulate the LLM’s (social) objective
function, the user prompt included the following objective prompt: "Remember that this
is a one-shot game, there are no future interactions or future visits [that this game has
16 rounds with the same composition of players]. You are [not] legally obligated to solve
the problem of any Player B who approaches you. [Your only objective is to maximize
your own payoff in this 1 round] Think about this objective when making your choices" . In
2All of our code, instructions, comprehension questions, prompts, LLM answers and LLM com-
ments can be accessed through the online appendix. https://osf.io/p8rjb/overview?view_only=
6e6574b221f74994b69bd474969349e9
3We use neutral wording, avoid morally loaded terms, and keep the instructions as constant as possible
across conditions.
7

Liability, the prompt stated "You are legally obligated to solve the problem of any Player B
who approaches you" . Beyond the self-interested objective prompt above, we also added
three others, depending on the desired social preference (Horton 2023):inequity-averse:
"You only care about fairness between yourself and Player B";efficiency-loving:"Your
only objective is to maximize the total payoff of yourself and Player B";no objective:here,
we gave the LLM no objective and left this part blank. Throughout, we sometimes used
additional instructions to ensure consistency and rule-adherence in, e.g., the format of the
LLM’s answers. Finally, the history prompt is a cumulative illustration of an LLM agent’s
prior choices and outcomes, which was appended to all questions, and further included
a few comprehension hints derived from the comprehension questions to support the
LLM in understanding the experiment’s income-relevant trade-offs. 4 Each agent only
has access to their own history, there is no public reputation institution. Following prior
literature, we set the model temperature to 1 (Kasberger et al. 2023; Bauer et al. 2023).
Treatments.The only difference between the four objective treatments are the respective
objective prompts formulated above. Regarding institutions, we augmented the instruc-
tions according to standard credence goods experiments, restricted the expert’s treatment
and price-charging choices when necessary, and changed the wording about liability as
described above. In conditions without reputation, all Player A ’s have non-enumerated
labels that are switched randomly between rounds. Furthermore, each Player A ’s position
in the question prompt is randomized. Hence, Player B can never identify any Player
A individually, When reputation is possible, Player A labels are enumerated (Player A1,
Player A2, . . . ) with the same label and position throughout the game.
4In Expected Parrot, LLM commands and prompts are being processed asynchronously. Thus, prior
answers only influence future answers if they are explicitly added as a user or question prompt.
8

5. Results
5.1. One-Shot
We conduct 50 independent simulations across the three market simulations and four
objective functions, resulting in 600 simulated one-shot markets. Figure 1 illustrates
average expected consumer payoff for all 12 conditions given expert prices.
FIGURE1. LLM Expert Price Setting and Expected Consumer Payoffs by Objective Function
and Market Institution.
InNo Institution, the standard model predicts low prices with ¯p=3 to internalize the
risk of expert fraud. Prices set by GPT-5.1 do not reflect that. Expected consumer income
is consistently negative irrespective of the LLM’s objective function. The average price
pairs are {5,7}/{5,8}/{4,8}/{2,6} forself-interested/no-objective/inequity-averse/efficiency-
lovingrespectively. IntroducingVerifiabilityremoves the expert’s ability to overcharge
consumers. Here, LLM price-setting works substantially better, but still does not con-
form to the theoretical prediction. Inself-interestedandefficiency-loving, expected
consumer payoffs lie above their outside option conditional on consumers expecting
expert honesty under monetary indifference. Only ininequity-aversedo prices induce
expectations of negative outcomes. Furthermore, the predicted strategy of signaling
honesty through equal markups is only played by the self-interested LLM. Otherwise,
LCT markups are consistently larger than HCT markups, indicating that LLMs do not
follow the theory’s incentive logic. The average price pairs are {5,9}/{4,7}/{6,8}/{2,3} forself-
9

FIGURE2. LLM expert treatment and price-charging behavior inNo Institution, conditional
on the LLM’s objective function prompt.
interested/no-objective/inequity-averse/efficiency-loving. Note that the inequity-averse
LLM sets prices that are consistent with an equal split of the economic gains between
experts and consumers provided that the expert is honest in their treatment behavior.
The efficiency-loving LLM sets prices that do not cover expert costs for the HCT, which,
given honest behavior, leads to negative expert income. Finally, underLiability, there
is no under-treatment, and expected consumer profits are always greater than the out-
side option. Prices are higher than predicted by a standard model under competition,
with the efficiency-loving LLM again offering the lowest prices: {8,8}/{8,8}/{6,8}/{2,6} for
self-interested/no-objective/inequity-averse/efficiency-loving.
5.1.1. Expert Honesty and Consumer Behavior
LLM experts set prices that are higher than theoretically optimal and frequently induce
negative expected consumer returns in absence of a liability rule. Figure ?? illustrates
the corresponding consumer approach rates, as well as intended expert treatment and
price-charging behavior forNo Institution. First, LLM consumers never approach LLM
experts, except inefficiency-loving, where market participation is almost 100%.
Hence, for most models, the market breaks down. LLM consumers are generally hesi-
tant to approach LLM experts in the presence of misaligned incentives through prices
10

FIGURE3. LLM expert treatment and price-charging behavior inVerifiability, conditional
on the LLM’s objective function prompt.
and markups. Yet, if prices are low enough as inefficiency-loving({2,6}), they ignore
misaligned incentives. Looking at expert honesty, both the default model inno objective
and theself-interestedLLM always intend to defraud consumers by implementing the
LCT and charging ¯p. Endowing them withinequity-averseorefficiency-lovingprefer-
ences mostly eliminates expert fraud, except for some residual over-treatment under
inequity-aversion. Consumer behavior inVerifiabilityelucidates that LLM consumers do
not follow the standard model’s markup logic. There is full participation inno objective
andefficiency-loving, and zero otherwise (Figure 3). That is despite expected consumer
payoff inno objectivebeing less than the outside option (because prices incentivize
experts to always choose the LCT), while being the highest inself-interestedgiven the
assumption of honesty under equal markups. Hence, price–approach combinations for
both conditions are not consistent with the standard model’s behavioral assumptions.
Expert dishonesty closely follows the patterns fromNo Institution. There is widespread
fraud by the default model and the self-interested LLM, which other-regarding prefer-
ences eliminate. Overall, like before,efficiency-lovingpreferences maximize consumer
participation while all but eliminating adverse expert behavior. However, because LLMs
approach experts with misaligned incentives, they are vulnerable to exploitation, as exem-
plified by the default model inno objective. Finally,Liabilitysolves the credence problem
11

FIGURE4. LLM expert treatment and price-charging behavior inLiability, conditional on
the LLM’s objective function prompt.
by eliminating under-treatment, leading to full LLM consumer participation across the
board (Figure 4). Experts without explicit other-regarding social preferences continue
to make dishonest choices by overcharging consumers when possible, which has only
distributive effects.
5.1.2. Welfare
The welfare implications follow straightforward from consumer approaches and expert
behavior as shown in Figure 5. Throughout, welfare is lowest when consumers do not
participate. Only inefficiency-lovingdo consumers always approach experts, who are
never dishonest, and therefore achieve average per-person-per-round welfare of around $6
which is optimal. However, due to the extremely low prices, experts consistently generate
negative returns, which is not sustainable on real economic markets. As expected, in
Liability, selfish preferences shift consumer gains towards experts, whereas income is
most equally distributed ininequity-averse. Overall, efficiency-loving preferences are
the only ones to reliably induce cooperation without liability institutions.
12

FIGURE5. Average consumer and expert payoffs in the one-shot games across institutions
and objective functions.
5.2. Results – Repeated Market Rounds
Next, we show results for 15 repeated-rounds market simulations per condition. We omit
Liability, because it already solves the credence problem for one-shot markets. LLMs play
16 rounds with the same group of agents, allowing for learning and adaption. First, we
look atNo Institutionwith self-interested LLM experts using the model gpt-5.1-2025-11-13.
Figure 6 shows average expert prices (left) and consumer approach shares (right)
across the 16 rounds. First, prices decrease strongly over the first rounds, hovering around
4 – 6 for ¯p and 1.5 – 3.8 for
¯
p. Prices tend to be smaller in theno reputationconditions, sug-
gesting some need to compensate consumer uncertainty through lower prices, although
differences for ¯p are small. In contrast to the one-shot environment, LLM consumers
learn to approach experts over time. While almost no consumer enters the market under
the initial prices, as competition sets in, almost all consumers participate from round 4
onward.
Yet, as shown in Figure 7, self-interested experts consistently opt for the small treat-
ment high price combination, leading to near universal intentions to under-treat con-
sumers (right panel). Concurrently, total average market income inno reputationlies
with roughly $15 per round clearly below the market optimum of $24. Interestingly, with
reputation, market income is significantly lower ($9 .75,t = 8.97 ,p< 0.001), which is
predominantly driven by a severe reduction in consumer gains. Whereas experts descrip-
tively benefit from building up a reputation ($100 vs. $84,t = 0.9 ,p= 0.366), consumers
13

FIGURE6.Left: Self-InterestedLLM Expert Price Setting Across 16 Rounds.Right:Con-
sumer Approach Share.
FIGURE7.Left:Total Group Income Across 16 Rounds.Right:IntendedSelf-Interested
Expert Under- and Over-Treatment.
experience strong losses on average ($55 vs. $160,t = 5.58, p< 0.001). In fact, total con-
sumer income lies substantially below the outside-option benchmark ($102). Thus, LLM
consumers do not exploit the potential to discipline identifiable experts, and instead
continuously approach experts despite economic losses once prices are low enough. Note
that while prices fall, they never reach the standard model’s benchmark ¯p= 3. Because
LLM experts profit from the repeated setup, overall market welfare is substantially higher
than in the one-shot case. LLMs learn to cooperate under information asymmetries, albeit
to the detriment of consumer welfare. Without reputation building, both consumers and
experts benefit compared to the one-shot scenario.
Figures 8 and 9 show very similar results for the default GPT-agent without an explicit
objective. Notably, prices fall in the beginning, which motivates LLM consumers to par-
ticipate in the market. Furthermore, experts exhibit a strong near-universal tendency
to exploit consumers through under-treatment and overcharging. In contrast to theself-
interestedcase, prices inno reputationare not necessarily lower. While there are very
small differences in
¯
p, prices for the HCT are higher inno reputation, which coincides
with a small drop in consumer participation towards the end of the 16 rounds (right panel
of Figure 8).
The second substantial difference pertains to overall market efficiency. As shown in
14

FIGURE8.Left: DefaultLLM Expert Price Setting Across 16 Rounds.Right:Consumer
Approach Share.
FIGURE9.Left:Total Group Income Across 16 Rounds.Right:IntendedDefaultExpert
Under- and Over-Treatment.
the left panel of Figure 9, total group income fluctuates at the beginning, and converges
towards a higher level inreputationthan inno reputation. Consequently, total income is
significantly higher inreputationacross all 16 rounds ($322 vs. $234,t = 11.25, p< 0.001),
which is entirely driven by consumer gains ($184 vs. $103,t = 7 .62,p< 0.001). The causal
relationship between market efficiency, income distribution and reputation flips. One
reason is that LLM experts are significantly less likely to under-treat and over-charge LLM
consumers when they are identifiable (Table 1). While levels of intended dishonesty and
fraud remain high, allowing consumer agents to identify each individual expert agent
in the following rounds does makes expert agents more honest. Overall, average market
welfare is much higher than in the one-shot setup, because experts learn to participate
in the market, and consumers either benefit from reputation mechanisms, or keep their
average income close to the outside option.
Figures 10 and 11 show the respective figure forinequity-averse. In contrast to the
one-shot environment, consumers enter the market from round 1 onward. That is despite
the familiar {6,8} price pair inreputation. This points towards a tendency for exploration.
LLM experts under inequity aversion exhibit low levels of under-treatment, ensuring
consistent consumer participation. In line with LLMs trying to reduce payoff differences
between experts and consumers, over-treatment rates are much higher than in any prior
15

TABLE1. Pooled panel regressions on expert behavior inNo Institution.
(1) Self-interested (2) Default (3) Inequity-averse (4) Efficiency-loving
Panel A: Under-treatment intent rate (big problems only)
No reputation (treat) 0.0039 0.0568*** -0.0133 0.0742***
(0.0022) (0.0085) (0.0088) (0.0124)
Round (roundc) 0.0003 0.0036*** 0.0001 0.0003
(0.0002) (0.0005) (0.0005) (0.0005)
No rep×Round -0.0003 -0.0050*** 0.0009 -0.0058***
(0.0002) (0.0007) (0.0007) (0.0012)
Observations 1776 1464 1720 1804
Experts 120 120 120 120
Panel B: Over-treatment intent rate (small problems only)
No reputation (treat) — — -0.2156*** -0.1126***
(0.0222) (0.0287)
Round (roundc) — — -0.0385*** 0.0079**
(0.0012) (0.0029)
No rep×Round — — 0.0281*** -0.0029
(0.0028) (0.0037)
Observations — — 1796 1660
Experts — — 120 120
Panel C: Overcharging intent rate (all decisions)
No reputation (treat) 0.0183*** 0.0211*** -0.0017 0.1170***
(0.0044) (0.0030) (0.0163) (0.0183)
Round (roundc) 0.0012*** 0.0012*** -0.0001 -0.0039***
(0.0003) (0.0002) (0.0007) (0.0009)
No rep×Round -0.0012*** -0.0017*** -0.0022* -0.0082***
(0.0003) (0.0002) (0.0009) (0.0014)
Observations 1920 1920 1920 1920
Experts 120 120 120 120
Notes.Pooled panel regressions of the form yit =α+β 1 treati +β 2 roundc +β 3 (treati × roundc)+ε it at the expert×round
level. Baseline condition isreputation;treat = 1 denotesno reputation. Standard errors in parentheses. Significance:
*p<0.05, **p<0.01, ***p<0.001.
setup, which makes sense as consumer-surplus for a successful LCT is higher than for a
successful HCT. Furthermore, over-treatment (but not under-treatment) is significantly
higher inreputation, once again pointing towards an ambiguous effect of reputation
mechanisms on AI agent behavior.
Finally, consumer participation inefficiency-lovingis always at 100% and prices
converge roughly towards {3,5} which is higher than predicted forNo Institutionbut also
less damaging for experts in case of honest treatment behavior. Like in the one-shot
setup, average expert income across 16 rounds is negative (-$60), while average consumer
16

FIGURE10.Left: Inequity-AverseLLM Expert Price Setting Across 16 Rounds.Right:
Consumer Approach Share.
FIGURE11.Left:Total Group Income Across 16 Rounds.Right:IntendedInequity-Averse
Expert Under- and Over-Treatment.
income eclipses all other social preference conditions ($405), with no significant difference
between reputation conditions. Reputation significantly decreases under-treatment and
overcharging, but increases over-treatment by efficiency-loving LLM experts (Table 1).
Looking at aggregate and role-specific incomes across the 16 rounds (Figure 14) high-
lights how other-regarding LLM expert preferences positively affect total and consumer-
specific welfare while hurting experts. In their absence (self-interestedandno objec-
tive), total income hovers between 150 and 320, depending on condition, with relatively
small expert–consumer differences that depend on the reputation regime. Generally, self-
interested LLM experts minimize welfare. On the other hand, market income ininequity-
averseandefficiency-lovingconsistently reaches 340–350, and heavily favors consumers.
Welfare gains compared to the one-shot setup predominantly accrue through increased ex-
pert incomes following higher consumer participation, while in efficiency-loving, effects
are mostly distributive due to on average higher expert prices
¯
p. Repeated interactions do
not meaningfully restrain expert dishonesty, because LLM consumers do not enforce it.
17

FIGURE12.Left: Efficiency-LovingLLM Expert Price Setting Across 16 Rounds.Right:
Consumer Approach Share.
FIGURE13.Left:Total Group Income Across 16 Rounds.Right:IntendedEfficiency-Loving
Expert Under- and Over-Treatment.
FIGURE14. Average total, consumer and expert payoffs across all 16 rounds.
18

5.2.1. Verifiability
Preventing LLM experts from overcharging consumers by introducing a verifiability insti-
tution does not fundamentally alter market dynamics under information asymmetry. All
figures are in the appendix. Pricing and consumer approach behavior forself-interested
LLM experts confirms that (1) our LLM consumer agents do not use the markup-logic to
infer incentives and thus expert strategies but instead (2) enforce (relatively) low prices to
alleviate the negative consequences of potential expert dishonesty. Consumers discipline
experts towards prices around
¯
p= 3 and ¯p< 6, such that consumers’ expected payoff
πcv = 2> 1.6 (see Figures A1 and A2). Here, expected (and realized) total group income per
round is below the standard model’s benchmark (12 < 24). Inreputation, consumers im-
mediately enter the market, otherwise, LLMs need a short learning period to sufficiently
decrease prices. There are little difference regarding expert honesty, but the regression
points to a marginal positive effect ofreputation(Table A1).
FIGURE15. Average total, consumer and expert payoffs across all 16 rounds inVerifiability.
Total income is higher inreputation($201 vs. $158,t = 7 .3,p< 0.001), which is mostly
driven by the initially higher market participation of consumers due to lower expert
prices. Comparing total market income inVerifiability(Figure 15) with total market in-
come inNo Institutionreveals a significantly higher aggregate income inNo Institution
forno reputation(t = 14.89 ,p< 0.001), which reverses inreputation(t = 4.57 ,p< 0.001).
Hence, verifiability does not automatically increase welfare in agent-based credence
markets. This is only further highlighted by looking at results for the defaultno objective
19

model. Here, aggregate income is higher forNo Institutionacross both reputation con-
ditions (t = 6.23, p< 0.001), driven primarily by substantial expert gains. Consequently,
market efficiency for theno objectiveagents inVerifiabilityis very low (9%). Otherwise,
results mirror the ones from above. LLM experts tend towards high levels of dishon-
esty, reputation slightly alleviates intention-to-under-treat, and income is significantly
higher inreputation($242 vs. $129 ,t = 10.97 ,p< 0.001). Regardinginequity-averseand
efficiency-loving, the results are very similar toNo Institution, without meaningful sys-
tematic changes. In these conditions, LLM expert agents tend towards honesty, although
inequity-aversepreferences motivate relatively high rates of over-treatment, especially
without any reputation mechanism. LLM experts do not make use of equal markup prices
to signal honest intentions, but compete via relatively low prices. Total market income
is higher inNo Institutionforinequity-averse(t = 4.18, p< 0.001), and slightly higher in
Verifiabilityforefficiency-loving(t = 2.15, p= 0.036). Overall,Verifiabilityprovides little
benefit for agent-based credence goods markets. Because the markup-logic of the stan-
dard model does not play a role, and the elimination of overcharging leads to on average
higher prices, while experts continue to make dishonest choices in the absence of explicit
other-regarding preferences, aggregate welfare fluctuates and often even decreases. In the
other-regarding conditions, experts tend to benefit from verifiability. Otherwise, expert
income is higher for the unregulated market. Notably, inVerifiability, expert income is
maximized under inequity-averse preferences, potentially inducing incentives for experts
to consider consumer outcomes. Overall, because repeated interactions induce almost
full consumer participation across the board, while social preferences mostly determine
expert honesty, verifiability has little influence on aggregate welfare.
5.3. Comparison with Human Experiments
We contextualize the simulated results with human experimental data from (Dulleck,
Kerschbamer, and Sutter 2011) who use the same setup. 5 A full table comparing all re-
sults is shown in the Appendix (Figure A2). Here, we concentrate on a few selected key
comparisons (Table 2). First, in Dulleck, Kerschbamer, and Sutter (2011), consumer par-
ticipation is fairly high while seller participation hovers around 50%-60%, suggesting
frequent trades with relatively low market concentration. In agent markets, participation
is generally higher – often near 1 –, but simultaneously much more concentrated. For
example, inNo Institutionwith agents that have no pre-defined objective function, ap-
proximately 3.1 consumers trade on average, while the average approached expert has
5The only difference is that in their experiments, experts also had a positive outside option σ= $1.6. This
may affect expert behavior. On the other hand, LLM expert agents in our simulations frequently disregard the
outside option 0 inefficiency-lovingas exemplified by negative expert returns, and LLM consumer agents
continue to approach experts if they average earnings lie below their outside option (e.g.,self-interested ×
reputationinNo Institution), suggesting a limited effect of outside options on LLM behavior.
20

TABLE2. Key outcome comparison: Human-Markets vs. AI-Agent-Markets
a. C/N (competition, no reputation, no verifiabil-
ity)
Trade
(C/S)
Avg. cons
per active
seller
Paid
price
Fraud
(UT/OC)
Profits
(S/C) Eff.
Humans 0.730/0.470 1.540 5.350 0.730/0.790 2.360/1.210 0.130
No obj. 0.772/0.256 3.030 4.656 0.998/0.615 2.041/1.610 0.466
Self-int. 0.666/0.211 3.187 3.948 1.000/0.994 1.309/2.499 0.502
Ineq.-averse 1.000/0.257 3.895 4.365 0.017/0.038 -0.010/5.552 0.891
Eff.-loving 1.000/0.292 3.475 3.427 0.064/0.071 -0.815/6.229 0.866
b. CR/N (competition, reputation, no verifiabil-
ity)
Trade
(C/S)
Avg. cons
per active
seller
Paid
price
Fraud
(UT/OC)
Profits
(S/C) Eff.
Humans 0.850/0.550 1.540 5.800 0.640/0.620 2.650/0.940 0.140
No obj. 0.875/0.282 3.100 4.627 0.867/1.000 2.174/2.870 0.783
Self-int. 0.777/0.298 2.697 4.106 1.000/0.954 1.571/0.867 0.190
Ineq.-averse 0.988/0.347 2.901 5.323 0.046/0.206 0.929/4.424 0.852
Eff.-loving 1.000/0.324 3.135 3.420 0.034/0.070 -1.064/6.424 0.849
c. C/V (competition, no reputation, verifiability)
Trade
(C/S)
Avg. cons
per active
seller
Paid
price
Fraud
(UT/OC)
Profits
(S/C) Eff.
Humans 0.880/0.540 1.630 5.190 0.530/— 1.960/2.180 0.340
No obj. 0.985/0.294 3.371 2.695 1.000/— 0.685/1.325 0.094
Self-int. 0.886/0.279 3.179 2.668 0.970/— 0.537/1.927 0.197
Ineq.-averse 0.942/0.235 4.000 5.800 0.002/— 0.852/4.039 0.748
Eff.-loving 1.000/0.265 3.789 4.265 0.033/— 0.306/5.558 0.950
d. CR/V (competition, reputation, verifiability)
Trade
(C/S)
Avg. cons
per active
seller
Paid
price
Fraud
(UT/OC)
Profits
(S/C) Eff.
Humans 0.930/0.580 1.600 5.580 0.360/— 1.900/2.590 0.460
No obj. 0.995/0.381 2.637 2.892 0.994/— 0.874/2.914 0.497
Self-int. 0.997/0.397 2.523 2.858 1.000/— 0.851/2.291 0.351
Ineq.-averse 0.998/0.315 3.200 5.779 0.023/— 1.150/4.101 0.830
Eff.-loving 0.943/0.327 2.897 4.244 0.125/— 0.367/4.944 0.843
Notes:Human data from Dulleck, Kerschbamer, and Sutter (2011). Trade (C/S) reports consumer-side trade
frequency and seller-side trade frequency (share of experts approached at least once per period). “ Avg.
consumers per active seller” is conditional on at least one consumer entering and captures market
concentration. Fraud reports undertreatment (UT) and overcharging (OC); OC is mechanically prevented by
verifiability. Profits (S/C) are per seller-period and per consumer-period. Eff. is normalized by the outside
optionσ=1.6. Note that in Dulleck, Kerschbamer, and Sutter (2011), both experts and consumers have the
respective outside options.
3.03 consumers, almost monopolizing the market. In every single LLM-agent condition,
a much higher share of trades goes to only one seller. This kind of Bertrand-like choice
behavior ties well into the second noticeable difference: expert prices in agentic credence
goods market are often much lower than in human markets. In Dulleck, Kerschbamer,
and Sutter (2011), transaction prices evolve around 5.2–5.80. For AI-markets, these prices
are only matched byinequity-averseLLM experts. Otherwise, competition drives prices
towards 2.7–4.7 . Note that inself-interestedandno objective, expert fraud remains high,
often approaching 1. Compared to human markets, expert fraud is much more polarized
by the objective function. While under-treatment and over-charging is substantial and
present in humans, it approaches either 1 or 0 for LLM-agents. Furthermore, whereas
reputation consistently reduces overcharging for humans, effects are context-dependent
for agentic interactions. These behavioral patterns lead to sharp shifts in the distribution
of surplus. In Dulleck, Kerschbamer, and Sutter (2011), sellers often out-earn consumers
on average. In our LLM interactions, consumers almost always secure substantially higher
surplus, a pattern that is broken in only two conditions (CR/N self-interested and C/N with
default agents). Finally, looking at welfare and institutions, verifiability consistently and
strongly improves market efficiency for human subjects, but not for AI agents. Overall,
LLM-interactions with experts who are endowed with other-regarding preferences ex-
hibit the highest efficiency levels by far. The effects forself-interestedandno objective
21

depend on the institutional context – efficiency sometimes collapses (e.g., C/V), but often
out-competes human markets (e.g., C/N), because (1) the human baseline can be quite
inefficient and (2) prices are much lower.
6. Conclusion
This article provides initial results about economic outcomes and behavioral trends in
agentic credence goods markets. We find that LLM agents do not follow the strategic behav-
ior dictated by the standard model. For one-shot settings, this causes market breakdown
in the absence of liability. In the repeated setting, LLM experts get away with widespread
consumer fraud because LLM consumers appear to condition their behavior mostly on
prices. In comparison to human data, market concentration increases, and the welfare
effects of institutions becomes much more ambiguous.
One-Shot.LLM Agents (here GPT-5.1) do not consider incentives through markups in their
pricing choices and therefore regularly offer negative expected value deals to consumers.
This leads to widespread market breakdown. However, even when prices follow theory
(e.g., equal markups in self-interested× verifiability), LLM consumers do not approach
LLM experts because they do not trust indifferent experts to not defraud them. AI-agents
behave dishonestly by default and when prompted to follow the objective of maximiz-
ing their own economic position. Inducing other-regarding preferences alleviates LLM
dishonesty, but does not improve price-setting. Notably, efficiency-loving LLM experts
consistently set prices that are so low that they always attract consumers but hurt the
expert’s income through negative returns. Apparently, the LLM prioritizes consumer
participation, which is indeed the most important factor for aggregate welfare. However,
because experts lose on average, this is not a stable strategy without some re-distributive
institution. Compared to recent behavior evidence from one-shot experiments with hu-
mans (Erlei 2025), LLM agents are generally substantially less successful than humans in
establishing cooperation on credence goods markets.
Repeated.Allowing LLM agents to interact for multiple rounds within a finite time horizon
solves the consumer participation problem because (1) LLM experts quickly learn to
lower their prices and (2) LLM consumers are quick to enter once prices reach a certain
threshold – despite adverse expert incentives hidden via different treatment-markups.
This makes LLM consumers vulnerable to dishonesty, which happens frequently, and is
not sufficiently punished. Hence, expert dishonesty becomes entrenched in the absence
of explicit other-regarding preferences. Experts’ treatment and price-charging behavior
is thoroughly dependent on their social preferences. Because consumers play no role
in disciplining experts, the patterns mostly mirror the ones from the one-shot setting,
with experts consistently opting for the high markup treatment (LCT) while overcharging
consumers (¯p). Private reputation institutions have small but positive effects on expert
22

fraud, while verifiability is, at best, neutral. In the absence of other-regarding preferences,
it hurts aggregate income. Neither expert agents nor consumer agents exploit the potential
of verifiability, which is consistent with them not acting strategically by signaling (or
inferring) intentions through markups. In comparison to the one-shot setting, market
efficiency is much higher. In particular, inequity-averse and efficiency-loving experts
cooperate with consumers to achieve almost full market efficiency. Yet, even with self-
interested experts, the market produces much higher levels of income that in one-shot,
which is driven by very high consumer participation. Compared to human benchmark
data, prices are lower, fraud is much more polarized, and efficiency is generally higher,
while the effect of institutions is less predictable and more context-dependent. Finally,
market concentration increases sharply with the introduction of AI agents, with singular
experts attracting the vast majority of consumers.
Implications.Our results highlight how information asymmetries that induce incentives
for fraud remain widespread in agent-based interactions. Even more so, they may become
entrenched parts of repeated interactions. Markets converge towards states with rampant
fraud that is compensated by somewhat low prices. In reality, this may be difficult to accept
for human stakeholders. However, it does lead to sustained expert-consumer interactions,
which – even when self-interested experts consistently intend to defraud consumers –
strongly outperforms one-shot settings and reaches efficiency rates of roughly 31% on
average. Notably, market efficiency climbs to 88% with efficiency-loving objective prompts
and 83% for inequity-averse prompts. This coincides with strong expert losses, leading to
negative aggregate income in efficiency-loving× No Institution, except for inequity-averse
experts under verifiable treatment outcomes. Therefore,Verifiabilityprovides an institu-
tional structure that rewards experts for considering consumer outcomes. This may be
one promising avenue when designing agentic credence goods markets. Similarly, private
reputation institutions like verified identities appear more consistently useful under veri-
fiability, whereas inNo Institution, the effects are very ambiguous, often harming overall
welfare. In conclusion, under complicated market structures that involve information
asymmetries and incentives for fraud, LLM behavioral structurally diverges from stan-
dard theory, leading to novel empirical patterns like entrenched fraud. Social preferences
can alleviate dishonesty, but often at the cost of expert welfare. Verifiability provides
some promise, as it is the only environment that offers experts incentives to deviate from
self-interest, and may positively affect the value of private reputation institutions that
reduce under-treatment and over-charging. However, in many conditions, verifiability
consistently worsens market outcomes, suggesting that it is far from a panacea. In gen-
eral, the impact of institutions like reputation and verifiability is very context-dependent
and difficult to predict. This stands in contrast to human subject experiments, in which
verifiability and reputation consistently produce either positive or null outcomes. Future
23

research may consider how these results change with the introduction of human oversight,
as both pricing and (dis-) honesty patterns are markedly different from human behavior
as observed in standard credence goods experiments.
24

References
Agarwal, Ritu, Che-Wei Liu, and Kislaya Prasad. 2019 . “Personal research, second opinions, and
the diagnostic effort of experts. ”Journal of Economic Behavior & Organization158: 44–61.
Alarie, Benjamin, Anthony Niblett, and Albert H Yoon. 2018. “How artificial intelligence will affect
the practice of law. ”University of Toronto Law Journal68 (supplement 1): 106–124.
Ayers, John W , Adam Poliak, Mark Dredze, Eric C Leas, Zechariah Zhu, Jessica B Kelley, Dennis J
Faix, Aaron M Goodman, Christopher A Longhurst, Michael Hogarth et al. 2023. “Comparing
physician and artificial intelligence chatbot responses to patient questions posted to a public
social media forum. ”JAMA internal medicine183 (6): 589–596.
Ayre, Julie, Erin Cvejic, and Kirsten J McCaffery. 2024. “Who is asking ChatGPT health questions?
Analysis of a nationally representative Australian community sample. ”medRxiv: 2024–10.
Balafoutas, Loukas, Adrian Beck, Rudolf Kerschbamer, and Matthias Sutter. 2013. “What drives
taxi drivers? A field experiment on fraud in a market for credence goods. ”Review of Economic
Studies80 (3): 876–891.
Balafoutas, Loukas, Adrian Beck, Rudolf Kerschbamer, and Matthias Sutter. 2015. “The hidden
costs of tax evasion.: Collaborative tax evasion in markets for expert services. ”Journal of Public
Economics129: 14–25.
Balafoutas, Loukas, Helena Fornwagner, Rudolf Kerschbamer, Matthias Sutter, and Maryna Tver-
dostup. 2023. “Serving consumers in an uncertain world: A credence goods experiment. ”MPI
Collective Goods Discussion Paper(2023/11).
Balafoutas, Loukas, and Rudolf Kerschbamer. 2020. “Credence goods in the literature: What the
past fifteen years have taught us about fraud, incentives, and the role of institutions. ”Journal
of Behavioral and Experimental Finance26: 100285.
Bauer, Kevin, Lena Liebich, Oliver Hinz, and Michael Kosfeld. 2023. “Decoding GPT’s Hidden
‘Rationality’of Cooperation. ”
Beck, Adrian, Rudolf Kerschbamer, Jianying Qiu, and Matthias Sutter. 2013. “Shaping beliefs in
experimental markets for expert services: Guilt aversion and the impact of promises and
money-burning options. ”Games and Economic Behavior81: 145–164.
Cohen, Myke C, Zhe Su, Hsien-Te Kao, Daniel Nguyen, Spencer Lynch, Maarten Sap, and Svitlana
Volkova. 2025. “Exploring Big Five Personality and AI Capability Effects in LLM-Simulated
Negotiation Dialogues. ”arXiv preprint arXiv:2506.15928.
Deshpande, Sanyukta, and Sheldon H Jacobson. 2026. “Strategic AI in Cournot Markets. ”arXiv
preprint arXiv:2601.17263.
Dulleck, Uwe, and Rudolf Kerschbamer. 2006. “On doctors, mechanics, and computer specialists:
The economics of credence goods. ”Journal of Economic literature44 (1): 5–42.
Dulleck, Uwe, Rudolf Kerschbamer, and Matthias Sutter. 2011. “The economics of credence goods:
An experiment on the role of liability, verifiability, reputation, and competition. ”American
Economic Review101 (2): 526–555.
Dvorak, Fabian, Regina Stumpf, Sebastian Fehrler, and Urs Fischbacher. 2025. “ Adverse reactions
to the use of large language models in social interactions. ”PNAS nexus4 (4): pgaf112.
Erlei, Alexander. 2025. “From Digital Distrust to Codified Honesty: Experimental Evidence on
Generative AI in Credence Goods Markets. ”arXiv preprint arXiv:2509 .06069.
Erlei, Alexander, and Lukas Meub. 2024. “Technological Shocks and Algorithmic Decision Aids in
25

Credence Goods Markets. ”arXiv preprint arXiv:2401.17929.
Erlei, Alexander, and Holger Andreas Rau. 2026. “Betrayal Aversion in Human-AI Interaction. ”
Available at SSRN 6078106.
Felin, Teppo, and Matthias Holweg. 2024. “Theory is all you need: AI, human cognition, and causal
reasoning. ”Strategy Science9 (4): 346–371.
Fish, Sara, Yannai A Gonczarowski, and Ran I Shorrer. 2024. “ Algorithmic Collusion by Large
Language Models. ”arXiv preprint arXiv:2404.00806.
Goktas, Denizalp, Amy Greenwald, Takayuki Osogami, Roma Patel, Kevin Leyton-Brown, Grant
Schoenebeck, Daphne Cornelisse, Constantinos Daskalakis, Ian Gemp, John Horton et al. 2025.
“Strategic Foundation Models. ”hal-04925309.
Gottschalk, Felix, Wanda Mimra, and Christian Waibel. 2020. “Health services as credence goods:
A field experiment. ”The Economic Journal130 (629): 1346–1383.
Grosskopf, Brit, and Rajiv Sarin. 2010. “Is reputation good or bad? An experiment. ”American
Economic Review100 (5): 2187–2204.
Guo, Fulin. 2023. “Gpt in game theory experiments. ”arXiv preprint arXiv:2305.05516.
Hirosawa, Takanobu, Ren Kawamura, Yukinori Harada, Kazuya Mizuta, Kazuki Tokumasu, Yuki
Kaji, Tomoharu Suzuki, and Taro Shimizu. 2023. “ChatGPT-generated differential diagnosis
lists for complex case–derived clinical vignettes: diagnostic accuracy evaluation. ”JMIR Medical
Informatics11: e48808.
Horton, John J. 2023. “Large language models as simulated economic agents: What can we learn
from homo silicus?” , National Bureau of Economic Research.
Imas, Alex, Kevin Lee, and Sanjog Misra. 2025. “ Agentic Interactions. ”Available at SSRN 5875162.
Inderst, Roman, Kiryl Khalmetski, and Axel Ockenfels. 2019 . “Sharing guilt: How better access to
information may backfire. ”Management Science65 (7): 3322–3336.
Ivanov, Dima, Paul Dütting, Inbal Talgam-Cohen, Tonghan Wang, and David C Parkes. 2024.
“Principal-agent reinforcement learning: Orchestrating ai agents with contracts. ”arXiv preprint
arXiv:2407 .18074.
Kandul, Serhiy, Bruno Lanz, and Evert Reins. 2023. “Reciprocity and gift exchange in markets for
credence goods. ”Games and Economic Behavior141: 52–69 .
Kasberger, Bernhard, Simon Martin, Hans-Theo Normann, and Tobias Werner. 2023. “ Algorithmic
cooperation. ”Available at SSRN 4389647.
Kerschbamer, Rudolf, Daniel Neururer, and Matthias Sutter. 2016. “Insurance coverage of cus-
tomers induces dishonesty of sellers in markets for credence goods. ”Proceedings of the National
Academy of Sciences113 (27): 7454–7458.
Kerschbamer, Rudolf, Daniel Neururer, and Matthias Sutter. 2023. “Credence goods markets, online
information and repair prices: A natural field experiment. ”Journal of Public Economics222:
104891.
Kerschbamer, Rudolf, Matthias Sutter, and Uwe Dulleck. 2017 . “How social preferences shape
incentives in (experimental) markets for credence goods. ”The Economic Journal127 (600):
393–416.
Lai, Jinqi, Wensheng Gan, Jiayang Wu, Zhenlian Qi, and S Yu Philip. 2024. “Large language models
in law: A survey. ”AI Open.
Leslie-Miller, Calissa J, Stacey L Simon, Kelsey Dean, Nadine Mokhallati, and Christopher C Cushing.
26

2024. “The critical need for expert oversight of ChatGPT: Prompt engineering for safeguarding
child healthcare information. ”Journal of pediatric psychology49 (11): 812–817 .
Li, Haitao, Qingyao Ai, Jia Chen, Qian Dong, Yueyue Wu, Yiqun Liu, Chong Chen, and Qi Tian. 2023.
“SAILER: structure-aware pre-trained language model for legal case retrieval. ” InProceedings
of the 46th International ACM SIGIR Conference on Research and Development in Information
Retrieval,: 1035–1044.
Long, Yunbo, Liming Xu, Lukas Beckenbauer, Yuhan Liu, and Alexandra Brintrup. 2025. “EvoEmo:
Towards Evolved Emotional Policies for Adversarial LLM Agents in Multi-Turn Price Negotia-
tion. ”arXiv preprint arXiv:2509 .04310.
Lopez-Lira, Alejandro. 2025. “Can Large Language Models Trade? Testing Financial Theories with
LLM Agents in Market Simulations. ”arXiv preprint arXiv:2504.10789.
Mimra, Wanda, Alexander Rasch, and Christian Waibel. 2016. “Second opinions in markets for
expert services: Experimental evidence. ”Journal of Economic Behavior & Organization131:
106–125.
Nay, John J, David Karamardian, Sarah B Lawsky, Wenting Tao, Meghana Bhat, Raghav Jain,
Aaron Travis Lee, Jonathan H Choi, and Jungo Kasai. 2024. “Large language models as tax
attorneys: a case study in legal capabilities emergence. ”Philosophical Transactions of the Royal
Society A382 (2270): 20230159 .
Nov, Oded, Nina Singh, and Devin Mann. 2023. “Putting ChatGPT’s medical advice to the (Turing)
test: survey study. ”JMIR Medical Education9: e46939 .
Oehler, Andreas, and Matthias Horn. 2024. “Does ChatGPT provide better advice than robo-
advisors?”Finance Research Letters60: 104898.
Rahwan, Iyad, Manuel Cebrian, Nick Obradovich, Josh Bongard, Jean-François Bonnefon, Cynthia
Breazeal, Jacob W Crandall, Nicholas A Christakis, Iain D Couzin, Matthew O Jackson et al.
2019 . “Machine behaviour. ”Nature568 (7753): 477–486.
Raman, Narun, Taylor Lundy, Samuel Amouyal, Yoav Levine, Kevin Leyton-Brown, and Moshe
Tennenholtz. 2024. “Steer: Assessing the economic rationality of large language models. ”arXiv
preprint arXiv:2402.09552.
Reis, Moritz, Florian Reis, and Wilfried Kunde. 2024. “Influence of believed AI involvement on the
perception of digital medical advice. ”Nature Medicine: 1–3.
Schmidt, Eva-Madeleine, Sara Bonati, Nils Köbis, and Ivan Soraperra. 2024. “GPT-3.5 altruistic
advice is sensitive to reciprocal concerns but not to strategic risk. ”Scientific Reports14 (1):
22274.
Schneider, Henry S. 2012. “ Agency problems and reputation in expert services: Evidence from
auto repair. ”The Journal of Industrial Economics60 (3): 406–433.
Schneider, Tim, Lukas Meub, and Kilian Bizer. 2021. “Consumer information in a market for expert
services: Experimental evidence. ”Journal of Behavioral and Experimental Economics94: 101754.
Schneiders, Eike, Tina Seabrooke, Joshua Krook, Richard Hyde, Natalie Leesakul, Jeremie Clos,
and Joel Fischer. 2024. “Objection Overruled! Lay People can Distinguish Large Language
Models from Lawyers, but still Favour Advice from an LLM. ”arXiv preprint arXiv:2409 .07871.
Seabrooke, Tina, Eike Schneiders, Liz Dowthwaite, Joshua Krook, Natalie Leesakul, Jeremie Clos,
Horia Maior, and Joel Fischer. 2024. “ A survey of lay people’s willingness to generate legal advice
using Large Language Models (LLMs). ” InProceedings of the Second International Symposium on
27

Trustworthy Autonomous Systems,: 1–5.
Shah, Anand, Kehang Zhu, Yanchen Jiang, Jeffrey G Wang, Arif K Dayi, John J Horton, and David C
Parkes. 2025. “Learning from Synthetic Labs: Language Models as Auction Participants. ”arXiv
preprint arXiv:2507 .09083.
Shahidi, Peyman, Gili Rusak, Benjamin S Manning, Andrey Fradkin, and John J Horton. 2025. “The
Coasean Singularity? Demand, Supply, and Market Design with AI Agents. ” , National Bureau of
Economic Research.
Shekar, Shruthi, Pat Pataranutaporn, Chethan Sarabu, Guillermo A Cecchi, and Pattie Maes. 2024.
“People over trust AI-generated medical responses and view them to be as valid as doctors,
despite low accuracy. ”arXiv preprint arXiv:2408.15266.
Tracy, Dustin, Eric Schniter, and Vojtěch Zíka. 2023. “Uncertainty and Reputation Effects in Cre-
dence Goods Markets. ”Available at SSRN 4513820.
Valmeekam, Karthik, Matthew Marquez, Alberto Olmo, Sarath Sreedharan, and Subbarao Kamb-
hampati. 2023. “Planbench: An extensible benchmark for evaluating large language models
on planning and reasoning about change. ”Advances in Neural Information Processing Systems36:
38975–38987 .
Wei, Jason, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny
Zhou et al. 2022. “Chain-of-thought prompting elicits reasoning in large language models. ”
Advances in neural information processing systems35: 24824–24837 .
Zhang, Ceyao, Kaijie Yang, Siyi Hu, Zihao Wang, Guanghe Li, Yihang Sun, Cheng Zhang, Zhaowei
Zhang, Anji Liu, Song-Chun Zhu et al. 2024. “ProAgent: building proactive cooperative agents
with large language models. ” InProceedings of the AAAI Conference on Artificial Intelligence, vol.
38: 17591–17599 .
Zhao, Huaqin, Zhengliang Liu, Zihao Wu, Yiwei Li, Tianze Yang, Peng Shu, Shaochen Xu, Haixing
Dai, Lin Zhao, Gengchen Mai et al. 2024. “Revolutionizing finance with llms: An overview of
applications and insights. ”arXiv preprint arXiv:2401.11641.
28

Appendix
FIGUREA1.Left: Self-InterestedLLM Expert Price Setting Across 16 Rounds.Right:Con-
sumer Approach Share. Verifiability.
FIGUREA2.Left:Total Group Income Across 16 Rounds.Right:IntendedSelf-Interested
Expert Under- and Over-Treatment. Verifiability.
29

FIGUREA3.Left: DefaultLLM Expert Price Setting Across 16 Rounds.Right:Consumer
Approach Share. Verifiability.
FIGUREA4.Left:Total Group Income Across 16 Rounds.Right:IntendedDefaultExpert
Under- and Over-Treatment. Verifiability.
FIGUREA5.Left: Inequity-averseLLM Expert Price Setting Across 16 Rounds.Right:
Consumer Approach Share. Verifiability.
FIGUREA6.Left:Total Group Income Across 16 Rounds.Right:IntendedInequity-averse
Expert Under- and Over-Treatment. Verifiability.
30

FIGUREA7.Left: Efficiency-lovingLLM Expert Price Setting Across 16 Rounds.Right:
Consumer Approach Share. Verifiability.
FIGUREA8.Left:Total Group Income Across 16 Rounds.Right:IntendedEfficiency-loving
Expert Under- and Over-Treatment. Verifiability.
31

TABLEA1. Pooled panel regressions on expert behavior inVerifiability.
(1) Self-interested (2) Default (3) Inequity-averse (4) Efficiency-loving
Panel A: Under-treatment intent rate (big problems only)
No reputation (treat) 0.0109*** 0.0413*** -0.1286*** 0.0765*
(0.0028) (0.0099) (0.0129) (0.0328)
Round (roundc) -0.0008* 0.0016 -0.0135*** -0.0066***
(0.0003) (0.0010) (0.0011) (0.0018)
No rep×Round -0.0021*** -0.0020 0.0120*** -0.0045
(0.0005) (0.0011) (0.0011) (0.0029)
Observations 1856 1736 1868 1804
Experts 120 120 120 120
Panel B: Over-treatment intent rate (small problems only)
No reputation (treat) -0.0000 -0.0088*** 0.2908*** -0.0479**
(0.0004) (0.0026) (0.0310) (0.0180)
Round (roundc) 0.0002 -0.0001 0.0273*** 0.0093***
(0.0001) (0.0002) (0.0029) (0.0020)
No rep×Round -0.0002 0.0002 -0.0375*** -0.0018
(0.0001) (0.0003) (0.0040) (0.0029)
Observations 1836 1768 1788 1736
Experts 120 120 120 120
Panel C: Overcharging intent rate (all decisions)
No reputation (treat) — — — —
Round (roundc) — — — —
No rep×Round — — — —
Observations — — — —
Experts — — — —
Notes.Pooled panel regressions of the form yit =α+β 1 treati +β 2 roundc +β 3 (treati × roundc)+ε it at the expert×round
level. Baseline condition isreputation;treat = 1 denotesno reputation. Standard errors in parentheses. Significance:
*p<0.05, **p<0.01, ***p<0.001.
32

Comparison with Dulleck et al. (2011)
TABLEA2. Comparison of simulated LLM-agent market results and human subject experi-
ment from Dulleck, Kerschbamer, and Sutter (2011) across treatments.
Treatment
C/N CR/N C/V CR/V
Panel A: Humans (Dulleck et al. 2011, Table 4)
Trade on consumer side 0.730 0.850 0.880 0.930
Avg # consumers (given seller has≥1) 1.540 1.540 1.630 1.600
Trade on seller side 0.470 0.550 0.540 0.580
Efficiency 0.130 0.140 0.340 0.460
Undertreatment (realized) 0.730 0.640 0.530 0.360
Overtreatment (realized) 0.080 0.100 0.130 0.190
Overcharging (realized) 0.790 0.620 — —
pl with trade 3.190 3.310 4.060 3.990
pl without trade 4.160 4.650 4.840 4.840
ph with trade 5.730 6.330 6.410 6.970
ph without trade 7 .550 7 .600 7 .720 7 .790
Actually paid price 5.350 5.800 5.190 5.580
Profits sellers (per seller-period) 2.360 2.650 1.960 1.900
Profits consumers (per consumer-period) 1.210 0.940 2.180 2.590
Mean total income per period (A+B) 14.280 14.360 16.560 17 .960
Panel B: Simulations (No Objective)
Trade on consumer side 0.772 0.875 0.985 0.995
Avg # consumers (given seller has≥1) 3.030 3.100 3.371 2.637
Trade on seller side 0.256 0.282 0.294 0.381
Efficiency 0.466 0.783 0.094 0.497
Undertreatment (realized) 0.998 0.867 1.000 0.994
Overtreatment (realized) 0.000 0.000 0.000 0.000
Overcharging (realized) 0.615 1.000 0.000 0.000
pl with trade 1.419 2.332 2.728 2.913
pl without trade 2.135 3.023 3.322 3.408
ph with trade 5.147 4.730 5.488 5.248
ph without trade 7 .529 6.260 6.699 6.322
Actually paid price 4.656 4.627 2.695 2.892
Profits sellers (per seller-period) 2.041 2.174 0.685 0.874
Profits consumers (per consumer-period) 1.610 2.870 1.325 2.914
Mean total income per period (A+B) 14.602 20.175 8.043 15.150
Continued on next page
33

Treatment
C/N CR/N C/V CR/V
Panel C: Simulations (Self-Interested)
Trade on consumer side 0.666 0.777 0.886 0.997
Avg # consumers (given seller has≥1) 3.187 2.697 3.179 2.523
Trade on seller side 0.211 0.298 0.279 0.397
Efficiency 0.502 0.190 0.197 0.351
Undertreatment (realized) 1.000 1.000 0.970 1.000
Overtreatment (realized) 0.000 0.000 0.000 0.002
Overcharging (realized 0.994 0.954 0.000 0.000
pl with trade 1.124 1.711 2.711 2.933
pl without trade 2.918 3.694 3.893 3.604
ph with trade 3.941 4.399 4.792 4.825
ph without trade 6.285 6.628 6.395 6.462
Actually paid price 3.948 4.106 2.668 2.858
Profits sellers (per seller-period) 1.309 1.571 0.537 0.851
Profits consumers (per consumer-period) 2.499 0.867 1.927 2.291
Mean total income per period (A+B) 15.232 9 .752 9 .860 12.570
Panel D: Simulations (Inequity-Averse)
Trade on consumer side 1.000 0.988 0.942 0.998
Avg # consumers (given seller has≥1) 3.895 2.901 4.000 3.200
Trade on seller side 0.257 0.347 0.235 0.315
Efficiency 0.891 0.852 0.748 0.830
Undertreatment (realized) 0.017 0.046 0.002 0.023
Overtreatment (realized) 0.259 0.248 0.392 0.307
Overcharging (realized 0.038 0.206 0.000 0.000
pl with trade 3.963 4.256 4.205 3.992
pl without trade 4.705 4.987 4.869 4.678
ph with trade 5.005 6.486 6.449 6.718
ph without trade 6.237 7 .270 7 .182 7 .319
Actually paid price 4.365 5.323 5.800 5.779
Profits sellers (per seller-period) -0.010 0.929 0.852 1.150
Profits consumers (per consumer-period) 5.552 4.424 4.039 4.101
Mean total income per period (A+B) 22.167 21.413 19 .565 21.005
Panel E: Simulations (Efficiency-Loving)
Trade on consumer side 1.000 1.000 1.000 0.943
Avg # consumers (given seller has≥1) 3.475 3.135 3.789 2.897
Trade on seller side 0.292 0.324 0.265 0.327
Efficiency (consumer outside option only; baseline=6.4, max=24.0) 0.866 0.849 0.950 0.843
Continued on next page
34

Treatment
C/N CR/N C/V CR/V
Undertreatment (realized) 0.064 0.034 0.033 0.125
Overtreatment (realized) 0.089 0.319 0.065 0.067
Overcharging (realized) 0.071 0.070 0.000 0.000
pl with trade 2.855 2.871 2.539 3.016
pl without trade 3.361 3.259 3.157 3.487
ph with trade 5.157 4.834 6.106 5.982
ph without trade 5.810 6.316 6.715 6.868
Actually paid price 3.427 3.420 4.265 4.244
Profits sellers (per seller-period) -0.815 -1.064 0.306 0.367
Profits consumers (per consumer-period) 6.229 6.424 5.558 4.944
Mean total income per period (A+B) 21.658 21.442 23.458 21.242
Notes:C/N = competition, no reputation, no verifiability; CR/N = competition, reputation, no verifiability;
C/V = competition, no reputation, verifiability; CR/V = competition, reputation, verifiability. Human values
are taken from Dulleck et al. (2011), Table 4, restricted to these four treatments. Simulation entries are cell
means (15 simulations per cell, 16 rounds each). Note that efficiency in Dulleck et al. (2011) is derived from a
setting in which both experts and consumers have outside options.
35
