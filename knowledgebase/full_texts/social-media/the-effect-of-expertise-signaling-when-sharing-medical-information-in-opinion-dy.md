---
title: The Effect of Expertise Signaling when Sharing Medical Information in Opinion Dynamics
url: https://arxiv.org/abs/2610.16623
category: social-media
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Moyi Li
- Chuqiao Yan
- Jesus Jair Reyes Gutierrez
- Aleksandra Urman
- Stefania Ionescu
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.16623
pages: 12
chars: 34021
fetched_at: '2026-11-08T13:13:44+00:00'
kb_version: 1
---

# The Effect of Expertise Signaling when Sharing Medical Information in Opinion Dynamics

The Effect of Expertise Signaling when Sharing
Medical Information in Opinion Dynamics
Moyi Li⋆1 , Chuqiao Yan⋆2 Jesus Jair Reyes Gutierrez 3, Aleksandra Urman 2,
and Stefania Ionescu 3
1 TU Delft,
2 University of Zurich,
3 ETH Zurich
Abstract.Social media heavily influences health decisions, yet few opin-
ion dynamics models account for how information is delivered. This work
investigates how signaling source expertise shapes trust and long-term
opinion formation. Through an online experiment, we find that adding
a professional title to the sender’s display name significantly increases
a post’s perceived credibility. Incorporating these findings to create a
data-driven opinion dynamics model, we prove that (1) connecting users
through some paths to an expert guarantees consensus with experts’
opinion, while (2) higher rates of expertise signaling accelerate reaching
consensus. Simulations show that (3) convincing even 20% of users to sig-
nal their title reduces consensus time to nearly one-third in Erd˝ os–R´ enyi
networks and (4) higher title adoption brings average opinion much closer
to that of experts in scale-free and real-world networks. Altogether, our
work highlights expertise signaling as a viable intervention to promote
validated medical information online.
Keywords:Opinion dynamics, Social Media, Agent-based modeling
1 Introduction
Social media has become an important source for people seeking health-related
information. For example, social media played a key role in the dissemination
of treatment progress and health guidance during the COVID-19 pandemic [40,
32]. Beyond the pandemic, social media has also been used to seek information
about specific diseases and to engage in health-related discussions [33, 41]. In-
formation shared on social media shapes people’s knowledge and opinions, and
may affect their decisions [2]. When related to health, online information could
influence self-care, mental state, and lead people to take actions without con-
sulting professionals [35, 25]. Therefore, trusting and sharing wrong information
can have particularly serious consequences [34].
It is important to understand what affects people’s trust in health informa-
tion on social media. Prior studies focus on analyzing target audience groups
⋆ These authors contributed equally to this work.
arXiv:2610.16623v2  [cs.SI]  17 Oct 2026

2 M. Li & C. Yan et al.
and political relations [20, 9, 36]. Less research has examined the relationship
between the specific features of post senders and the credibility of their posts.
Previous research has demonstrated that people’s trust in information sources
online is associated with the perceived expertise of the sources [38]. For exam-
ple, [4] found that clinical therapists’ professional titles could influence their
perceived credibility. [26] also suggests that displaying ‘Dr.’ or ‘PhD’ on Reddit
increases feedback in expert communities. However, these works either do not
focus specifically on medical information or do not consider online information
dissemination. To address this, we investigate whether signaling expertise (‘Dr.’,
‘PhD’) can increase trust in medical information on social media.
While short-term effects can be investigated via online experiments, opin-
ion dynamics models are uniquely positioned to understand how these effects
compound over time. Examples include the DeGroot model [10], the Friedkin-
Johnsen (FJ) model [15], and the Flocking model [3]. While such models have
been extensively used in the Complex Networks community, recent work has
increasingly emphasized the need for data-driven models that better reflect real-
world behavior by incorporating empirical findings. Doing so improves the real-
ism and explanatory power of the model in opinion propagation, belief dynamics,
customer behavior, and fairness in digital systems [5, 8, 12, 29, 37]. Aligning with
this vision, we propose a data-driven agent-based model grounded in the De-
Groot and FJ models with weights calibrated based on data from the online
experiment. By varying the behavior of agents [17, 18, 31], we then test the ef-
fects of interventions such as encouraging more experts to signal their expertise.
Altogether, our work investigates how signaling expertise when creating health-
related content affects the credibility of this content and the long-term opinion
dynamics on social media platforms. To do so, we use a data-driven agent-based
modeling approach consisting of two steps. First, we conduct an exploratory on-
line experiment to study the impact of different creator features related to exper-
tise signaling on content credibility. The results show that including professional
titles, such as ‘Dr.’ or ‘MD’, in the display name makes receivers trust content
more. Second, we leverage the data from the online experiment to calibrate an
opinion dynamics model. We use both theoretical analysis and agent-based simu-
lations4 to understand the long-term implications of different expertise-signaling
attitudes on the opinion dynamics. The results suggest that platform interven-
tions encouraging experts to signal their expertise could more quickly promote
information agreed upon as true among experts.
2 Empirical Study: Online Experiment
Study Design.We conducted a between-subject exploratory online experiment
and considered four factors: sender’s username title (three levels: Non-title or
‘Dr.’ or ‘MD’), sender gender (two levels: male or female), profile information
that indicates relevant medical background (two levels: relevant or irrelevant),
4 Our code is publicly available on GitHub (https://github.com/LiMY00/Expert-
Title-in-Opinion-Dynamics)

The Effect of Expertise Signaling in Opinion Dynamics 3
(a) Factors examined in X posts.
Read a medical statement
Read one post from
 Perceived Credibility
How much does the
post affect the
credibility?
Read the same statement Perceived Credibility (b) Online experiment workflow.
Fig. 1: Overview of the factors examined in X posts and the experimental work-
flow. (a): Example X post showing four measured factors: the profile image at
the top of the post, the professional title directly below the profile name, the
profile description in the middle, and the source link below the post text. (b):
Workflow of the online experiment. Each participant was randomly assigned to
one experimental block and rated the perceived credibility of two posts.
and the presence of a source link in the message content (two levels: with or
without a link to a scientific source supporting the statement). To examine the
effects of these factors, we designed the experiment in three blocks. In Block
1, Gender (female vs. male) and Title (no title vs. ‘Dr.’ vs. ‘MD’) were varied,
resulting in six experimental conditions. In Block 2, Source link (included vs.
excluded) and Title (no title vs. ‘Dr.’ vs. ‘MD’) were varied, also resulting in
six conditions. In Block 3, only profile information (irrelevant vs. relevant) was
varied, resulting in two conditions. Participants were randomly assigned to one
condition within each block. Fig. 1 shows an example of the measured factors
and the experiment workflow.
Participants.We recruited 180 participants (90 female, 86 male, 4 preferred
not to say) throughProlific 5. The age ranges from ‘under 20’ to ‘over 60’, and
most participants were aged 20–30 (69%). These participants were located in 27
countries and completed the experiment in English. Each participant received
€0.75 upon completion and passing the attention check.
Data Analysis and Results.Since the independent variable,Title, has
three groups, we used a one-way ANOV A to compare the changes in perceived
credibility across the threeTitleconditions (no title vs. ‘Dr.’ vs. ‘MD’). The anal-
ysis revealed a significant effect ofTitle, (F(2,177) = 9.86,p < .001). Moreover,
we conducted Tukey’s HSD post hoc tests to determine which groups differed.
The results showed that both the ‘Dr.’ and ‘MD’ groups differed significantly
5 https://www.prolific.com

4 M. Li & C. Yan et al.
Table 1: ANOV A and Tukey HSD post-hoc results for the effect of the sender’s
signaled title in their display name on perceived credibility.
ANOV A:
Source df Sum Sq. Mean Sq.F p
Title 2 21.361 10.680 9.865< .001
Residual 177 191.639 1.083
T ukey HSD Post-Hoc Comparisons:
Comparison Mean Diff.p-value
‘Dr.’ vs. No title 0.748< .001
‘MD’ vs. No title 0.686.002
‘Dr.’ vs. ‘MD’ 0.062.946
from the no-title group (p=.0002 andp=.0016, respectively), whereas the two
professional-title groups did not differ significantly (p=.95) in the credibility
they induced. These results indicate that posts from users with a professional
title in their display name were perceived as more credible than those from users
without a title. Table 1 summarizes these results.
For the remaining variables, we used Welch’s two-sample t-tests to examine
their impact on the perceived credibility, namelyGender,Profile, andLink. The
results suggested no significant difference in the change of perceived credibility
caused by the sender’s gender, relevance of profile information, or link to scientific
support in the content (p gender = 0.42,p link = 0.34,p prof ile= 0.17).
3 Data-driven opinion dynamics model
The above data analysis indicates that including professional titles in users’
display names has a small yet significant impact on the credibility of their posts.
A natural question is how this effect compounds within a social network of
multiple users and affects opinion dynamics. To answer this, we extend classical
opinion dynamics models to account for expertise signaling. We use the data from
the online experiment to inform the trust parameters used in opinion updates.
PreliminariesWe denote a social network by a directed graphG= (V, E),
whereVis the set ofagents(social media users) andEis the set of edges
(following relationships). At every iteration (timestep), each agentiholds an
opinionx i(t)∈[0,1] capturing their level of trust in a given statement (with 1
corresponding to full trust). Opinions update via a DeGroot model [10]:
x(t+ 1) =W x(t),(1)
whereWdenotes the row-stochastic adjacency matrix of the networkG, with
wij denoting how much agentitrusts agentj’s opinion. Whenw ii = 1, agenti
always preserves their opinion, and we refer to it asstubborn.

The Effect of Expertise Signaling in Opinion Dynamics 5
Table 2: Overview of the different types of agents in our model. For each type,
we specify: if the agent isstubborn(i.e., keeps their initial opinion fixed), the
professionaltitlethey could include in their display name, and the range of values
for theirinitial opinion.
Agent type Stubborn Title Initial opinion
Common user False None [0,1]
Expert True ‘Dr.’/ None 1
User types.We extend the above model by distinguishing between common users
and experts (Table 2) that differ in stubbornness, title, and initial opinion. More
precisely,common usersare the general population on the social media platform
who update their opinions at each timestep.Expertshold a single opinion uni-
versally accepted as true among them and could either signal their expertise or
not. We track expertise signaling as our experiment showed it can affect trust 6.
Assumptions and parameters.While both our model and code (GitHub reposi-
tory mentioned above) for the simulation are general and could capture a variety
of settings, we make some assumptions to limit the scope of this work. The model
assumes experts unanimously agree on one opinion (without loss of generality,
the one with value 1) and there is only one type of expertise signaling. In terms
of information dynamics, the model assumes that the common user on social
media trust other actors than experts equally, and there is no marginal effect of
time (i.e., the impact of message from the same type of user is constant at every
time step). The model above is based on a few parameters, which we overview
in Table 3. For the simulations, we ground the parameter choices in our online
experiment data and prior work.
Table 3: Tabular description of model parameters (Left) and the values taken in
the simulations (Right). We use bold (red) for default parameter values: i.e., we
use this value when the parameter in question is not varied. For each combination
of parameters, we run 100 simulations with different random seeds.
Varied Parameters Values Taken
% of experts with title 0,20, . . . ,100
Network ER (edge pr. 0.01),SF(α= 2.5), PolBlog
Fixed Parameters Value
Total number of agents 1500 [1]
Number of experts 100
Opinion of experts 1
6 As there was no significant difference between ‘Dr.’ and ‘MD’ revealed from the
online experiment, we only capture one general form of expertise signaling (‘Dr.’).

6 M. Li & C. Yan et al.
–Initial opinionvalues are grounded in participants’ pre-experiment trust
in the medical statements. We first map the 7-point Likert scale to [0,1],
yieldingN(0.54,0.29). Then, we sample common users’ initial opinions from
this distribution, truncated to [0,1].
–Weight matrixvalues are derived from participants’ trust in posts from ac-
counts with different display names. For participanti, the experiment corre-
sponds to a single-step DeGroot update after seeing a post from an expert:
xi(1) =w ∗ iixi(0) +w ∗ ijxj(0), w ∗ ii +w ∗ ij = 1, x j(0) = 1 (2)
wherex i(0) andx i(1) denote pre- and post-experiment opinions of partici-
pantiand , andx j(0) denotes the sender’s opinion. Solving forw ∗ ij and av-
eraging by sender type givesw ∗ i,Dr = 0.183, w∗ i,CU = 0.003.For simulations,
we follow the approach of [42] and preserve row stochasticity by normalizing
the trust based on each agent’s connectivity.
–Networks.We use the Erd˝ os–R´ enyi (ER) and Barab´ asi–Albert models [24] to
create ER networks and scale-free (SF) networks [23, 14]. We also use a real-
world political blog network (PolBlog) [1], which is widely used in research
on information diffusion [28, 27, 39].
4 Expertise Signaling Impacts Opinion Dynamics
Evaluation metrics.To evaluate the social impact of signaling expertise on so-
cial media platforms, we adopt standard metrics and investigate (1) whether a
consensus(i.e., a state in which opinions no longer change and all agents hold
the same opinion) is reached, and, if so, (2) thetime needed to reach consensus
and (3) theconsensus value. These metrics are crucial as they capture whether
communities of users will eventually agree, what they would agree on, and how
long it takes for this agreement to arise. In the context of medical information,
consensus among scientists and public consensus around expert-backed evidence
is socially beneficial, as it promotes informed decision-making and reduces the
influence of misinformation [21, 22]. However, not all discrete-time linear systems
converge to a consensus [10, 6, 11] and many real-life platforms remain polarized
[30, 19]. Finally, we consider theaverage user opinionover time.
Increased connectivity to experts promotes convergence to the experts’ opinion.
As Theorem 1 demonstrates, ensuring a directed path between common users
and experts guarantees that all users reach consensus on the verified experts’
opinion. Consequently, the average user opinion also converges to this exact
value. In practice, this suggests that increasing connectivity to experts (either
by encouraging following relationships or by directly intervening on recommen-
dation systems to promote their message) drives the network toward a consensus
where all users adopt the verified opinion.
Theorem 1 (Existence of consensus).Consider a DeGroot systemx(t+1) =
W x(t)withnagents and a non-empty set of stubborn agents holding the same

The Effect of Expertise Signaling in Opinion Dynamics 7
opinion,c. If there exists a directed path from every non-stubborn agent to at
least one expert, the system converges to a global consensus where both individual
beliefs and the average user opinion equalc, i.e.,lim t→∞ x(t) =c·1 n =⇒
limt→∞ 1 n 1⊤ n x(t) =c.
Proof (Sketch).LetNbe the set of non-stubborn agents andSbe the non-
empty set of stubborn experts holding some opinionc. Drawing upon estab-
lished results in algebraic graph theory [7], we reorder the agents to partition the
row-stochastic matrixWinto block upper-triangular form:W=
WN NWN S
0I

.
Here,W N Ncaptures the trust of non-stubborn agents towards other non-stubborn
agents,W N Sdenotes the trust from non-stubborn agents towards experts, andI
reflects that experts maintain their beliefs. The path condition guarantees that
the matrixW N Nis sub-stochastic; thus, its spectral radius is bounded strictly
below 1, ensuring asymptotic convergence. Solving for the equilibrium point of
the non-stubborn agents as per Discrete-time Affine Systems ([7], p.35), resolves
toc·1 |N |. Because every individual agent’s opinion converges toc, the mean of
the agent’s opinions converges tocast→ ∞.■
An intervention encouraging more experts to signal their expertise speeds con-
vergence.Theorem 2 looks at the speed of convergence. It states that if experts
become more trusted (i.e., their corresponding weights increase), then consensus
is reached faster. In connection with the results from the online experiment, this
suggests that encouraging more experts to signal their expertise will speed the
time needed to reach consensus.
Theorem 2 (Impact of weights on the convergence speeds).Consider a
DeGroot system,x(t+ 1) =W x(t), satisfying the conditions of Theorem 1. Let
a second influence matrixW ′ be formed by increasing the trust of non-stubborn
agents in stubborn agents. Then, the convergence speed underW ′ is at least
as fast as underW. Furthermore, if at least one weight is strictly larger (i.e.,
W ′ > W), then the new system converges faster.
Proof (Sketch).Building on the block partitionW=
WN NWN S
0I

introduced
in Theorem 1, an increase in the trust weights of the block (W N S) requires a
corresponding decrease in the trust weights of the block (W N N) to maintain
the row-stochastic property ofW. According to the Monotonicity of Spectral
Radius, (Lemma 4.10 [7], p.56), this decrease implies that the new sub-matrix
W ′ N Nsatisfiesρ(W ′ N N)≤ρ(W N N), with a strict inequality if at least one weight
strictly decreases. Under modal decomposition, the evolution of the system’s
state can be expanded into its eigenmodes asx(t) = P λt i(v⊤ i x0)vi. Because the
system’s transient states decay proportionally to the eigenvalue powersλ t i, and
these non-consensus eigenvalues are bounded byρ(W N N) and smaller than 1,
a reduced spectral radius accelerates their decay to zero. Consequently, both
the individual agent states and the average user opinion converge to the expert
consensus at a faster rate.■

8 M. Li & C. Yan et al.
Convergence time and average opinion greatly improve as more experts signal
their expertise.While the analytical results specify the direction of change re-
sulting from the intervention, the magnitude of change remains unknown. There-
fore, we use simulations to find the intervention’s impact across settings. Fig. 2
(a) shows that on ER networks agents reach a consensus to a final opinion of
1. Moreover, the time for reaching consensus greatly reduces from the setting in
which no doctors signaling their expertise to the one when 20% do so (from 2023
to 763 steps). Further increasing this percentage produces diminishing gains in
convergence speed. In Fig. 2 (b), we plot only three conditions on the SF net-
work: 0%,50%,100% doctors have ‘Dr.’ displayed in usernames. Although the
average opinions increase when more doctors signal titles, the confidence inter-
vals overlap. By investigating the simulation runs, we believe this is caused by
the randomness in the position of experts within the network. More precisely,
the gains would be large if the ‘Dr.’ signaling expertise has a high degree and
negligible if they are a periphery node. We plot the same conditions for the Pol-
Blog network in Fig. 2 (c). Although the opinions do not converge to 1 as on
the ER network, there is less variance in average opinion across runs compared
to the SF network. As with the ER network, signaling expertise is especially
effective when the first doctors do so.
Policy implications.Overall, these results suggest that encouraging doctors
to signal expertise is an efficient intervention. Across scenarios, it can bring
the average opinion of users closer to that of experts. In networks with high
homogeneity and uniformly random connections, it can greatly reduce the time
people need to be fully convinced of the experts’ opinion. Such an intervention
is particularly effective when only a few experts already signal their expertise.
Accounting for malicious users and influencers.Having a modular code al-
lowed us to investigate additional scenarios and interventions. First, we assumed
we have malicious users, such as bots, promoting information opposite to the
experts [13]. In this case, we found it is more important to ensure these users
cannot pose as experts (e.g., by verifying accounts that include a title) than to
reduce their number through moderation. Second, we investigated the efficacy
of increasing the connectivity of experts. To this end, encouraging influencers
(i.e., high degree nodes) to re-post content from verified experts improves the
average opinion. Moreover, in accordance with the analytical results, we found
that a recommender system that boosts the visibility of even one verified expert
guarantees convergence and greatly improves the average opinion over time. We
include details of this additional work in the repository 7 and plan to further in-
vestigate these directions in future work. Meanwhile, these results demonstrate
the potential of our data-driven opinion dynamics model to support policymak-
ers and social media platforms in prioritizing interventions.
7 https://github.com/LiMY00/Expert-Title-in-Opinion-Dynamics

The Effect of Expertise Signaling in Opinion Dynamics 9
(a) ER network
 (b) SF network
 (c) PolBlog network
Fig. 2: Average opinion over time for different networks and shares of experts
signaling expertise. Lines show the average over 100 simulations. The shaded
areas represent the standard deviation in average opinion across simulations.
5 Conclusion
We investigate how signaling expertise (e.g., including professional titles) shapes
trust in medical information and influences long-term opinion dynamics on social
networks. Through an online experiment, we find that including professional ti-
tles (e.g., ‘Dr.’, ‘MD’) in the display name of the source slightly yet significantly
increases the perceived credibility of their posts. We use this data to extend
the DeGroot model with expertise signaling by grounding its parameters in the
experiment’s data. A theoretical analysis of the resulting discrete-time system
specifies sufficient conditions for consensus to emerge and demonstrates that en-
couraging expertise signaling increases the speed of reaching consensus. Through
simulations, we find that on both random (ER) and real-world (PolBlog) net-
works, even a small group of experts who include their title can greatly and
significantly improve the average opinion. While results on scale-free networks
are not significant, the trends persist.
With this being a first exploratory analysis, several limitations remain to
be tackled by future research. For example, future work can conduct a power
analysis and build a confirmatory experiment; such work can also verify if our
findings apply to more diverse samples of participants. Like any agent-based
model, our model makes several simplifying assumptions on user behavior (e.g.,
binary stubbornness, equal level of trust in non-expert sources, static trust net-
works). Additionally, we did not consider the time and cost of implementing
interventions (e.g., it can be time-consuming for experts to actively participate
on social media [16], limiting intervention integration).
Altogether, our work is a first step towards understanding how expertise
signaling and related interventions affect medical opinions. At a methodologi-
cal level, it combines online experiments, theoretical analysis, and agent-based
modeling, demonstrating the benefits of a holistic approach in linking short-term
effects to long-term impact. Having a dedicated online experiment allowed us to
vary one variable at a time, thus isolating its effect. This represents an alterna-
tive to data-driven modeling methods that calibrate parameters based on digital
trace data, which are more contextual and have many hard-to-disentangle ef-

10 M. Li & C. Yan et al.
fects. It also shows how isolating directions of change via dedicated experiments
supports a more insightful theoretical analysis, connected to real-life changes
and interventions. Thus, more generally, our work demonstrates the potential
of experiment-driven modeling for supporting realistic social simulations and an
initial comparison over potential interventions.
Acknowledgments
This work was supported as a part of NCCR Automation, a National Centre
of Competence in Research, funded by the Swiss National Science Foundation
(grant number 51NF40 225155).
References
1. Adamic, L.A., Glance, N.: The political blogosphere and the 2004 U.S. election:
divided they blog. In: Proceedings of the 3rd international workshop on Link
discovery, LinkKDD ’05, pp. 36–43. Association for Computing Machinery, New
York, NY, USA (2005). DOI 10.1145/1134271.1134277. URL https://dl.acm.org/
doi/10.1145/1134271.1134277
2. Ahmed, Y.A., Ahmad, M.N., Ahmad, N., Zakaria, N.H.: Social media for
knowledge-sharing: A systematic literature review. Telematics and Informatics37,
72–112 (2019). DOI 10.1016/j.tele.2018.01.015. URL https://www.sciencedirect.
com/science/article/pii/S0736585317306688
3. Asch, S.E.: Opinions and Social Pressure. Scientific American193(5), 31–35
(1955). URL https://www.jstor.org/stable/24943779. Publisher: Scientific Amer-
ican, a division of Nature America, Inc.
4. Bass, B.A.: Effects of Professional Title and Degree Upon the Perceived Cred-
ibility of A Sex Therapist. Journal of Sex Education and Therapy12(1), 47–
50 (1986). DOI 10.1080/01614576.1986.11074861. URL https://doi.org/10.1080/
01614576.1986.11074861
5. Bell, D., Mgbemena, C.: Data-driven agent-based exploration of customer behavior.
Simulation94(3), 195–212 (2018)
6. Berger, R.L.: A necessary and sufficient condition for reaching a consensus using
degroot’s method. Journal of the American Statistical Association76(374), 415–
418 (1981)
7. Bullo, F.: Lectures on Network Systems, 1.4 edn. Kindle Direct Publishing (2019).
With contributions by J. Cort´ es, F. D¨ orfler, and S. Mart ´ ınez
8. Dalege, J., Galesic, M., Olsson, H.: Networks of beliefs: An integrative theory of
individual-and social-level belief dynamics. Psychological Review (2024)
9. De Choudhury, M., Morris, M.R., White, R.W.: Seeking and sharing health infor-
mation online: comparing search engines and social media. In: Proceedings of the
SIGCHI Conference on Human Factors in Computing Systems, CHI ’14, pp. 1365–
1376. Association for Computing Machinery, New York, NY, USA (2014). DOI
10.1145/2556288.2557214. URL https://dl.acm.org/doi/10.1145/2556288.2557214
10. Degroot, M.H.: Reaching a Consensus. Journal of the American Statistical As-
sociation69(345), 118–121 (1974). DOI 10.1080/01621459.1974.10480137. URL
https://www.tandfonline.com/doi/abs/10.1080/01621459.1974.10480137

The Effect of Expertise Signaling in Opinion Dynamics 11
11. Dong, Y., Ding, Z., Mart ´ ınez, L., Herrera, F.: Managing consensus based on lead-
ership in opinion dynamics. Information Sciences397-398, 187–205 (2017). DOI
10.1016/j.ins.2017.02.052. URL https://www.sciencedirect.com/science/article/
pii/S0020025517305534
12. Du, Y., Ionescu, S., Sage, M., Joseph, K.: A data-driven simulation of the new york
state foster care system. In: Proceedings of the 2022 ACM Conference on Fairness,
Accountability, and Transparency, pp. 1028–1038 (2022)
13. Egele, M., Stringhini, G., Kruegel, C., Vigna, G.: Compa: Detecting compromised
accounts on social networks. In: NDSS, vol. 13, pp. 83–91 (2013)
14. Eikmeier, N., Gleich, D.F.: Revisiting power-law distributions in spectra of real
world networks. In: Proceedings of the 23rd ACM SIGKDD international confer-
ence on knowledge discovery and data mining, pp. 817–826 (2017)
15. Friedkin, N.E., Johnsen, E.C.: Social influence and opinions. Journal of mathe-
matical sociology15(3-4), 193–206 (1990)
16. Galetti, M., Costa-Pereira, R.: Scientists need social media influencers. Science
357(6354), 880–881 (2017)
17. Gilbert, N., Troitzsch, K.: Simulation for the social scientist. McGraw-Hill Educa-
tion (UK) (2005)
18. Hu, H.: Competing opinion diffusion on social networks. Royal Society Open Sci-
ence4(11), 171,160 (2017)
19. Jiang, J., Ren, X., Ferrara, E.: Social media polarization and echo chambers in the
context of covid-19: Case study. JMIRx med2(3), e29,570 (2021)
20. Li, Y., Wang, X., Lin, X., Hajli, M.: Seeking and sharing health information on
social media: A net valence model and cross-cultural comparison. Technological
Forecasting and Social Change126, 28–40 (2018). DOI 10.1016/j.techfore.2016.07.
021. URL https://www.sciencedirect.com/science/article/pii/S0040162516301780
21. van der Linden, S.L., Clarke, C.E., Maibach, E.W.: Highlighting consensus among
medical scientists increases public support for vaccines: evidence from a randomized
experiment. BMC public health15(1), 1207 (2015)
22. Maibach, E.W., Van Der Linden, S.L.: The importance of assessing and communi-
cating scientific consensus. Environmental Research Letters11(9), 091,003 (2016)
23. Mislove, A., Marcon, M., Gummadi, K.P., Druschel, P., Bhattacharjee, B.: Mea-
surement and analysis of online social networks. In: Proceedings of the 7th ACM
SIGCOMM conference on Internet measurement, pp. 29–42 (2007)
24. Newman, M.E., Strogatz, S.H., Watts, D.J.: Random graphs with arbitrary degree
distributions and their applications. Physical review E64(2), 026,118 (2001)
25. Oh, Y.S., Song, N.K.: Investigating relationships between health-related problems
and online health information seeking. CIN: Computers, Informatics, Nursing
35(1), 29–35 (2017)
26. Park, K., Kwak, H., Song, H., Cha, M.: “trust me, i have a ph. d.”: A propensity
score analysis on the halo effect of disclosing one’s offline social status in online
communities. In: Proceedings of the international AAAI conference on web and
social media, vol. 14, pp. 534–544 (2020)
27. Peralta, A.F., Kert´ esz, J., I˜ niguez, G.: Opinion dynamics in social networks: From
models to data. arXiv preprint arXiv:2201.01322 (2022)
28. Peralta, A.F., Neri, M., Kert´ esz, J., I˜ niguez, G.: Effect of algorithmic bias and
network structure on coexistence, consensus, and polarization of opinions. Physical
Review E104(4), 044,312 (2021)
29. Rieder, A., Chakraborty, S., Goyal, S., Berndt, D.J.: A critical realist approach to
agent-based modeling: Unlocking prediction in non-positivist paradigms. Journal
of Information Technology40(2), 122–139 (2025)

12 M. Li & C. Yan et al.
30. Schmidt, A.L., Zollo, F., Scala, A., Betsch, C., Quattrociocchi, W.: Polarization of
the vaccination debate on facebook. Vaccine36(25), 3606–3612 (2018)
31. Schweighofer, S., Garcia, D., Schweitzer, F.: An agent-based model of multi-
dimensional opinion dynamics and opinion alignment. Chaos: An Interdisciplinary
Journal of Nonlinear Science30(9) (2020)
32. Song, T., Yu, P., Yecies, B., Ke, J., Yu, H.: Social media crisis communication
and public engagement during covid-19 analyzing public health and news media
organizations’ tweeting strategies. Scientific Reports15(1), 18,082 (2025)
33. Taik, F.Z., Bensaid, R., Adnine, A., Mansouri, N.E., Aharrane, F.Z., Amar, A.,
Fourtassi, M., Abourazzak, F.E.: Use of social media as a source of health infor-
mation among patients with chronic low back pain. Musculoskeletal Care22(1),
e1846 (2024)
34. Tasnim, S., Hossain, M.M., Mazumder, H.: Impact of rumors and misinformation
on covid-19 in social media. Journal of preventive medicine and public health
53(3), 171 (2020)
35. Thapa, D.K., Visentin, D.C., Kornhaber, R., West, S., Cleary, M.: The influence
of online health information on health decisions: a systematic review. Patient
education and counseling104(4), 770–784 (2021)
36. Urman, A., Ionescu, S., Garcia, D., Hann´ ak, A.: The politicization of medical
preprints on twitter during the early stages of covid-19 pandemic. Journal of
Quantitative Description: Digital Media2(2022)
37. Wang, R., Lu, T., Zhang, P., Gu, N.: Data-driven agent-based model for public
opinion propagation simulation in cyberbullying. Big Data Mining and Analytics
8(4), 794–819 (2025)
38. Wathen, C.N., Burkell, J.: Believe it or not: Factors influencing credibility on the
Web. Journal of the American Society for Information Science and Technology
53(2), 134–144 (2002). DOI 10.1002/asi.10016. URL https://onlinelibrary.wiley.
com/doi/abs/10.1002/asi.10016
39. Zhang, Q., Wang, L., Wang, X., Chen, G.: Optimal selection of intervention timing
in opinion dynamics. IEEE Transactions on Automatic Control (2025)
40. Zhong, Y., Liu, W., Lee, T.Y., Zhao, H., Ji, J.: Risk perception, knowledge, in-
formation sources and emotional states among covid-19 patients in wuhan, china.
Nursing outlook69(1), 13–21 (2021)
41. Zhou, K., Constantinides, M., Quercia, D., ˇS´ cepanovi´ c, S.: How circadian rhythms
extracted from social media relate to physical activity and sleep. In: Proceedings of
the International AAAI Conference on Web and Social Media, vol. 17, pp. 948–959
(2023)
42. Zhou, Q., Wu, Z., Altalhi, A.H., Herrera, F.: A two-step communication opin-
ion dynamics model with self-persistence and influence index for social networks
based on the DeGroot model. Information Sciences519, 363–381 (2020). DOI
10.1016/j.ins.2020.01.052. URL https://www.sciencedirect.com/science/article/
pii/S0020025520300633
