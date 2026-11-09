---
title: 'Social media battle for attention: opinion dynamics on competing networks'
url: https://arxiv.org/abs/2310.18309
category: social-media
subcategory: empirical
date: 2023-10
venue: ''
authors:
- Andrea Somazzi
- Giuseppe Maria Ferro
- Diego Garlaschelli
- Simon Asher Levin
source: arxiv
pdf_url: https://arxiv.org/pdf/2310.18309
pages: 13
chars: 54979
fetched_at: '2026-11-08T13:03:02+00:00'
kb_version: 1
---

# Social media battle for attention: opinion dynamics on competing networks

arXiv:2310.18309v1  [physics.soc-ph]  27 Oct 2023
Social media battle for attention:
opinion dynamics on competing networks
Andrea Somazzi ∗1,2, Giuseppe M. Ferro †3, Diego Garlaschelli 1,4,5, and Simon A. Levin 3
1IMT School for Advanced Studies, Piazza S. Francesco 19, 551 00 Lucca, Italy
2Scuola Normale Superiore, Piazza dei Cavalieri 7, 56126 Pis a, Italy
3Department of Ecology and Evolutionary Biology, Princeton University, Princeton, NJ 08544
4Lorentz Institute for Theoretical Physics, Niels Bohrweg 2 , 2333 CA Leiden, The Netherlands
5INdAM-GNAMPA Istituto Nazionale di Alta Matematica, Italy
Author contribution
A.S. and G.M.F. conceived the idea and design, developed the mathematical framework, performed all simulations,
analyze and interpret the results and wrote the manuscript.
D.G and S.A.L. provided critical discussions, guidance, an d supervision throughout the research process.
Abstract
In the age of information abundance, attention is a coveted r esource. Social media platforms
vigorously compete for users’ engagement, inﬂuencing the e volution of their opinions on a variety
of topics. With recommendation algorithms often accused of creating “ﬁlter bubbles”, where
like-minded individuals interact predominantly with one a nother, it’s crucial to understand the
consequences of this unregulated attention market. To addr ess this, we present a model of opinion
dynamics on a multiplex network. Each layer of the network re presents a distinct social media
platform, each with its unique characteristics. Users, as n odes in this network, share their opinions
across platforms and decide how much time to allocate in each platform depending on its perceived
quality. Our model reveals two key ﬁndings. i) When examinin g two platforms — one with a
neutral recommendation algorithm and another with a homoph ily-based algorithm — we uncover
that even if users spend the majority of their time on the neut ral platform, opinion polarization
can persist. ii) By allowing users to dynamically allocate t heir social energy across platforms in
accordance to their homophilic preferences, a further segr egation of individuals emerges. While
network fragmentation is usually associated with “echo cha mbers”, the emergent multi-platform
segregation leads to an increase in users’ satisfaction wit hout the undesired increase in polarization.
These results underscore the signiﬁcance of acknowledging how individuals gather information from
a multitude of sources. Furthermore, they emphasize that po licy interventions on a single social
media platform may yield limited impact.
1 Signiﬁcance statement
Understanding how people consume information on social med ia is key to unveil its inﬂuence on political opinions
and shaping eﬀective platform regulation policies. A Faceb ook study suggests that their recommendation algorithm,
suggesting like-minded content, has a limited impact on pol itical attitudes, as such beliefs remain unchanged even whe n
individuals are exposed to more diverse content. Our opinio n dynamics model challenges this study, demonstrating that
the interplay between diverse and homophilic content recom mendations across various platforms can sustain opinion
polarization, highlighting the importance of multi-media information gathering. Our model also reproduces the obser ved
relationship between opinions’ stance and social media pre ferences. These insights underscore the intricate relatio nship
between recommendation algorithms, news consumption, and opinion dynamics in the digital age, with the potential to
inform and guide policy decision-making within the ever-ch anging landscape of information dissemination.
2 Introduction
In our contemporary landscape, online social networks have evolved into pivotal platforms for the acquisition of polit ical
news [ 1, 2]. These modern communication platforms have several advan tages for democracy: they simplify access to in-
formation, boost citizen participation, enable individua ls to express their views, counteract misinformation, and e nhance
∗andrea.somazzi@imtlucca.it
†giuseppe.ferro@princeton.edu
1

transparency and responsibility in political actions. Ide ally, individuals can tap into social media to encounter a ra nge
of ideological perspectives and consequently make more inf ormed choices [ 3–5]. An extensive literature, empirical [ 6–11]
and theoretical [ 12–15], pertains to how social media inﬂuence opinion dynamics, f ostering (or not) the appearance of
“echo-chambers” where individuals are mainly connected wi th like-minded peers. Echo chambers are often believed to
stem from the recommendation systems utilized by social med ia platforms, which tend to link individuals with similar
views. This phenomenon contributes to the rise of opinion po larization [ 8]. Furthermore, these automated algorithms
interact with the cognitive limitations of individuals, wh o tend to gravitate towards information that aligns with the ir
existing beliefs and actively avoid contradictory informa tion [16]. It is thus crucial to distinguish between the inﬂuence of
algorithms and inherent human tendencies when examining th e genesis of echo chambers. A recent empirical study [ 11]
has shown how increasing the amount of cross-cutting conten t on Facebook does not signiﬁcantly alter political opinion s,
thereby suggesting that social media recommendation algor ithms may not contribute to opinion polarization. They note
however that political information on Facebook is mainly in cidental (6 .7% of the total news consumption), and thus
people might get political information from other sources. More in general, the above cited studies focus on the eﬀect of
only one social media platform, while contemporary news con sumption is characterized by its reliance on a multitude of
sources [ 17]. People exhibit diﬀerent news repertoires depending on a v ariety of needs [ 18–20]. Several scholars [ 21–23]
stress that an adequate study of political opinions must con sider the interplay between news repertoires and political
communication processes.
Here, we answer to the following question: what are the impli cations of social media platforms competing for
users’ attention on opinion dynamics? To address this, we de velop a model of opinion dynamics which integrates three
main ingredients. i) People can connect on diﬀerent platfor ms, each platform represented by a layer in a multiplex
network. These networks diﬀer in their recommendation algo rithms (a single parameter representing its homophily)
and in their political focus. ii) Users’ opinions evolve acc ording to a well-known non-linear model [ 15], on the basis of
interactions taking place on the multiplex. Opinions depen d on the social interaction strength , issue controversy and the
heterogeneous activity proﬁle on social media. iii) Users a llocate their time among the diﬀerent social media platform s,
depending on their personal preferences and limited inform ation processing.
Our model provides two pivotal insights. Firstly, when cons idering two platforms — one governed by a neutral
recommendation algorithm and the other by a homophily-cent ric algorithm — we ﬁnd that even with a user majority on
the neutral platform, opinion polarization can endure. Sec ondly, as users dynamically allocate their social engageme nt
across platforms based on their (strong or weak) homophilic inclinations, agents manifest a pronounced separation acr oss
platforms. While most associate network fragmentation wit h “echo chambers”, this emergent multi-platform segregati on
boosts user satisfaction without increasing polarization . These ﬁndings highlight the importance of recognizing the
multifaceted avenues through which individuals assimilat e information.
3 Results
As detailed in Sec. 5, we consider a system composed by Γ social platforms populat ed by N agents (see Fig. 1)
having continuous opinions xi(t) ∈ (−∞, +∞), i = {1, ...N }. The opinions evolve according to ˙ xi = −xi +∑Γ
γ=1
(K (γ)∑N j=1 A(γ) ij (t) tanh (cxj )), a generalization of a well-known model [ 24]. In absence of social interactions,
i.e. the second addend on the r.h.s. equals zero, all opinion s relax to x∗ = 0. This assumption allows us to study the
network inﬂuence on opinions, isolating it from the other po ssible causes of polarization such as identity politics [ 25],
cognitive biases [ 13, 26] and economic inequality [ 27]. The tanh( cx) term reﬂects the fact that the opinion change for
each interaction is limited. The parameter c represents how controversial a topic is. For c high enough, all opinions
equally contribute to the dynamics since | tanh(cx)| saturates to 1, meaning that people are maximally susceptib le to
be socially inﬂuenced. On the other hand, if c is very small, only users with extreme opinions are eﬀective ly able to
inﬂuence others. The platform-dependent parameter K (γ) represents the social interaction strength. The larger K (γ),
the larger opinions change as a consequence of given interac tions. Its platform-dependence captures the idea that, for a
given topic, users may consider a platform more “appropriat e” than another. For instance, since the exposure to politic al
content on Facebook is often incidental [ 11], while users tend to consume more political news on Twitter [28, 29], it is
reasonable to assume that, in the realm of politics, Faceboo k social interaction strength K (F B) is lower than Twitter
K (T W ). This results in users giving less credit to the political ne ws they are exposed on Facebook.
The opinion dynamics model evolves on a multiplex directed n etwork, where each layer represents a single social
platform, as pictured in Fig 1. At every time step (see Sec. 5 and SI for further details), user i can be active (news
producer), passive (news consumer) or both with probability ai, pi and aipi respectively. Conditional on being active
(resp. passive), user i chooses a platform γ with probability ρ(γ) i . Note that he might be active on platform γ and passive
on platform γ′, each with probability ρ(γ) i and ρ(γ′) i , respectively. Active users on a platform/layer contact pa ssive users
on the same platform/layer. The probability that a γ-active user i contacts a γ-passive user j on platform γ at time t
is q(γ) ij (t) ∝ | xi(t) − xj(t)|−β(γ) , leading to A(γ) ji (t) = 1. The exponent β(γ) represents the degree of homophily of the
recommendation engine of platform γ.
The model with a single platform (Γ = 1) has been studied in [ 24]. Figure 2 shows the main qualitatively diﬀerent
dynamics that the model exhibits, as a function of the diﬀere nt parameters, obtained initializing the opinions uniform ly
in [ −1, +1]. Speciﬁcally, when K (1) = K is small, social interaction is negligible and opinions rel ax to 0 (Fig. 2(a)). If
instead social coupling is relevant ( K = 3), but no homophilic recommendation engine is present ( β = 0), a one-side
radicalization appears where all the opinions have the same sign (Fig. 2(b)). When both K and β are big enough, opinions
split into two opposite sides. The intuition is that with β ⁄= 0 agents tend to connect only with like-minded peers, an
interaction which further polarizes users’ stance. This eﬀ ect makes it even more likely to connect with like-minded
individuals; this vicious cycle fosters polarization (a mo re exhaustive phase diagram for the single-platform model i s
reported in [ 24]). Note that this phase manifests only if opinions are initi alized with diﬀerent signs. Otherwise, there is
no range of parameters which leads to polarization.
As anticipated in Sec. 2, we ask whether polarization can persist when users spend a t iny fraction of their time on
2

Figure 1: Opinion dynamics on a multiplex network. Dashed lines indic ate that the same nodes (users) are
shared among the layers. In this example, every active user ( blue dots) contacts m = 2 passive users (yellow
dots). A passive user can reciprocate a link with probabilit y r (see Sec. 5). A user can be both active and
passive on the same platform (green dots), or not engaging at all in social media activity (white dots).
0 2 4 6 8 10
t
−1.00
−0.75
−0.50
−0.25
0.00
0.25
0.50
0.75
1.00
x
i
( t )
Neutral Consensus ( β = 0, K = 0.3, c = 3)
(a)
0 2 4 6 8 10
t
0
2
4
6
8
10
12
14
x
i
( t )
Radicalization ( β = 0, K = 3, c = 3)
(b)
0 2 4 6 8 10
t
−7.5
−5.0
−2.5
0.0
2.5
5.0
7.5
x
i
( t )
Polarization ( β = 2, K = 3, c = 3)
(c)
Figure 2: (a) Neutral consensus, all opinions converge to zero ( K = 0.3, β = 0). (b) (One-sided) radicalization
(K = 3, β = 0). (c) Opinion polarization, in which opinions split into two opposite sides ( K = 3, β = 2). Topic
controversiality and reciprocity were set to c = 3 and r = 0.5.
politically-oriented social media with an homophilic reco mmendation engine, while engaging the rest of their time on
a politically neutral platform. To explore this scenario, w e consider Γ = 2 platforms and stationary and homogeneous
allocation probabilities, i.e. ρ(γ) i (t) = ρ(γ) for all i and for γ = {1, 2}. Clearly, ρ(1) + ρ(2) = 1. Both the assumptions of
stationarity and homogeneity will be later relaxed. Platfo rm 1 has a set of parameters such that, if users were only there ,
opinions would converge to neutral consensus ( β(1) = 0 and K (1) small). On the other hand, platform 2 is assumed
to adopt an homophilic recommendation engine, which transl ates in β(2) ⁄= 0. The social interaction strength K (2)
is left as a varying parameter, meaning that platform 2 could have exhibited both neutral consensus or polarization
if it were the only platform, depending on its value. W e are th en interested in exploring the opinion dynamics for
diﬀerent values of ρ(1) and K (2). The former represents how long users engage on platform 1 (t he “politically neutral”
platform); the latter captures how “polarizing” platform 2 is. W e deﬁne the rescaled vector of opinions at equilibrium as
x = {
x(eq) 1
K(1)ρ(1)+K(2)ρ(2) , . . . ,
x(eq) N
K(1)ρ(1)+K(2)ρ(2) } in order to compute a set of three metrics which allow us to dis tinguish
diﬀerent opinion phases. In particular, such metrics are th e standard deviation of the opinions σ(x), the absolute value
of the average opinion |µ(x)| and the absolute value of the average opinions’ sign |⟨sign(x)⟩|. In Figure 3 we show the
results of our analysis for β(1) = K (1) = 0 and β(2) = 3. W e can observe three main phases. i) Neutral Consensus
(σ(x) ≈ 0, µ(x) ≈ 0), observable when platform 2 is not polarizing enough (i.e . K (2) not high enough) w.r.t. the time
spent on the neutral platform 1 1. ii) Radicalization ( |µ(x)| >> 0, ⟨sign(x)⟩ = 1) is evident by the fact that all opinions
share the same sign. Such phase is driven by an initial relaxa tion towards xi(t) ≈ 0 ∀i due to the neutral platform.
Then, when close to 0, opinions start to share the same sign an d are progressively ampliﬁed by the polarizing (now,
rather, radicalizing) platform. iii) Polarization ( σ(x) >> 0, ⟨sign(x)⟩ < 1) emerges if platform 2 can sustain diverging
opinions, i.e. if K (2) is big enough to oﬀ-set the time users spend on the neutral pla tform ρ(1). The take home message
is that polarization can persist even when users spend most o f their time on a politically neutral platform ( ρ(1) > 0.5),
thus suggesting the importance of considering that users ga ther information from diﬀerent sources. In Fig. S1 of the SI,
we show a similar phase diagram for a diﬀerent value β(2). The qualitative picture remains the same.
The above results are obtained by assuming that users’ taste for social media platforms may depend on factors which
1The neutral consensus phase can have both |⟨sign(x)⟩| ≈ 0 and |⟨sign(x)⟩| ≈ 1, as the opinions never really reach
exactly 0.
3

0.00 0.44 0.89 1.33 1.78 2.22 2.67 3.12 3.38 3.62 3.88
K
(2)
0.50
0.60
0.70
0.80
0.90
ρ
(1)
σ ( x )
0.0
0.2
0.4
0.6
0.8
1.0
(a)
0.00 0.44 0.89 1.33 1.78 2.22 2.67 3.12 3.38 3.62 3.88
K
(2)
0.50
0.60
0.70
0.80
0.90
ρ
(1)
| μ ( x )|
0.0
0.1
0.2
0.3
0.4
(b)
0.00 0.44 0.89 1.33 1.78 2.22 2.67 3.12 3.38 3.62 3.88
K
(2)
0.50
0.60
0.70
0.80
0.90
ρ
(1)
|⟨si⟨n( x )⟩|
0.2
0.4
0.6
0.8
1.0
(c)
0.00 0.44 0.89 1.33 1.78 2.22 2.67 3.12 3.38 3.62 3.88
K
(2)
0.50
0.60
0.70
0.80
0.90
ρ
(1)
Phase Diagram
NC
R
P
(d)
Figure 3: Allocation diagram. In all the four panels, on the horizonta l axis the social interaction strength of
the polarizing platform, and on the vertical axis the time sp ent on the neutral platform. (a) Standard deviation
of the opinions; (b) Absolute value of average opinion; (c) A bsolute value of average opinions’ sign; (d) Phase
diagram. Panel (d) is obtained through “ﬁltering” panels (a )-(b)-(c) according to the conditions detailed in
the main text. In short: i) NC corresponds to σ(x) ≈ 0 and µ(x) ≈ 0). ii) R corresponds to |µ(x)| >> 0 and
⟨sign(x)⟩ = 1. iii) P corresponds to σ(x) >> 0 and ⟨sign(x)⟩ < 1.
are not captured in the model (e.g. better user interface), t herefore we had an homogeneous and stationary allocation
probability ρ = {ρ(1), ρ(2)}. Hereafter, we suppose that users dynamically choose their Social Media Repertoire (SMR),
depending on the perceived political quality of platforms. Based on the psychological theory of optimal distinctivene ss
[30], we imagine that each user looks for a trade-oﬀ between assi milation (homophily) and diﬀerentiation (debate). As
detailed in Sec. 5.3, we capture such desired balance into the (user-dependent) parameter φi, which represents the desired
4

fraction of “far” opinions (i.e. contributing to diﬀerenti ation) user i wants to be exposed to. In particular, inspired by
bounded conﬁdence theory [ 31], user i considers “far” opinions those x such that |xi − x| > r . The others are considered
“close” opinions, contributing to assimilation. Thus, whi le in bounded conﬁdence theory users do not engage with peers
having far opinions, we relax this hypothesis by introducin g φi, which can be seen as user i’s desired probability to contact
a distant peer. The idea is to capture the observed desire of d ebate. Indeed, as reported in [ 32], despite the general
tendency for social media networks to form homogeneous comm unities, networks formed through reply-to messages reveal
a users’ stance heterophily, with individuals using replie s more often to express divergent opinions. W e deﬁne the util ity
(i.e. satisfaction) of each user as Ui(t) = −(fi(t) − φi)2, where fi(t) is the fraction of distinctiveness experienced by user
i, which is compared to the desired one. Clearly, fi(t) depends on the SMR of user i (i.e. ρi(t) = {ρ(γ) i (t)}Γ γ=1 ), since
user’s exposure to distinctiveness and assimilation depen ds on the connections formed on each platform, which in turn
depend on his allocation probability. W e assume therefore t hat user i dynamically updates ρi(t) in order to maximize
his Ui(t) (see Sec. 5.3 and SI for additional details).
In the context of platforms’ battle for users’ attention, so cial media are interested in maximizing users’ satisfactio n
(which translates in higher activity, thus revenue). W e wil l now show how a market populated by two platforms achieves
higher average satisfaction without the undesired drawbac k of increasing polarization. This is surprising, as one wou ld
expect that the additional degree of freedom increases soci al fragmentation, thus increasing polarization.
Suppose that each platform can vary its characteristics by t uning its β(γ) 2. First, we consider a single platform
(i.e. Γ = 1) and consider K = c = 3, r = 2 and φi = 0 .2 ∀i. In this setting, the highest single-platform average
utility ⟨U ⟩1 is reached in β∗ = 3, i.e. ⟨U ⟩Γ=1(β∗) = ⟨U ⟩1. On the other hand, a market populated by Γ = 2
platforms can result in an higher satisfaction. Figure 4 summarizes our results by showing the variation of average
utility and standard deviation in passing from Γ = 1 to Γ = 2 for diﬀerent values of β(1) and β(2). In particular,
we deﬁne ∆ ⟨U ⟩(β(1), β(2)) = ⟨U ⟩Γ=2(β(1), β(2)) − ⟨ U ⟩1 and ∆ σ(x; β(1), β(2)) = σΓ=2(x; β(1), β(2)) − σ1(x), where
σ1(x) = σΓ=1(x; β∗). Even if in the ﬁgure we reported, for the sake of completene ss, the values corresponding to
β(1) = 0 or β(2) = 0, in the following discussion we are going to neglect those points. The reason is that they correspond
to a radicalized regime, which is highly undesired in a democ racy, which lies on dialogue and debate. Thus, restricting
the attention to( β(1), β(2)) ∈ [1, 5]2, the average utility increases for many couples of values wi th respect to the best
possible single-platform average utility. The reason is th at users can dynamically change their SMR, thus allocating t heir
time among platforms to satisfy their desired diﬀerentiati on φ. Moreover, focusing our attention on the point ( β(1) = 2,
β(2) = 1) (or, by symmetry, ( β(1) = 1, β(2) = 2)), which is arguably very close to the two-platform optim um, we can
see that the corresponding variation of polarization is alm ost zero, i.e. ∆ σ(x; 2, 1) ≈ 0. As we show in Fig. S2, the
explanation for higher satisfaction without increasing po larization is the emerging quasi-segregation between mode rate
and extreme opinions. The moderate individuals, in absence of the extreme ones who populate another platform, get
radicalized less, eﬀectively reducing polarization. This is in qualitative agreement with ﬁndings on media habits and
opinion stance, where individuals at both the left and right ends of the spectrum tend to be clustered around a single
media source 3 [33]. So, by focusing only on users’ satisfaction, the competit ion of platforms brings notable beneﬁts.
Finally, the points for which satisfaction decreases with r espect to Γ = 1 are those where both β(1) and β(2) are large
enough. In this regime, users connect only to very close peer s, and can not ﬁnd an alternative, cross-cutting platform.
Thus, they cannot satisfy their desire for diﬀerentiation e ncapsulated in φ = 0 .2. In SI Fig. S3 we show an alternative
situation, where φ = 0.1. In that case, users’ desire for diﬀerentiation is too low a nd maximizing the utility leads to an
increased polarization.
4 Discussion
Online social networks have become crucial for political ne ws consumption [ 1, 2]. Existing studies [ 6–15] explore the
impact of recommendation algorithms on opinion dynamics, w ith some ﬁndings on Facebook’s limited inﬂuence [ 6, 11].
However, news consumption spans various platforms [ 17], and individual preferences [ 18] play a role. It is thus crucial to
consider the interplay between news repertoires and politi cal communication processes to understand political opini ons
fully.
Here we show that when examining two platforms — one with a low political focus and a neutral recommendation
algorithm, and another more politically oriented with a hom ophily-based algorithm — even if users spend the majority
of their time on the neutral platform, opinion polarization can persist. This result casts some doubts on the generality of
conclusions drawn from the recent study on the impact of Face book recommendation algorithm on political opinions [ 11],
which shows that people’s political attitudes did not signi ﬁcantly change when they were exposed to more diverse conten t.
Indeed, the consumption of political news on Facebook is inc idental (low political focus), and the polarization might
originate from (little) time spent on other news sources.
When we allow users to dynamically optimize their satisfact ion by adjusting their SMR, the further segregation of
individuals brought by multiple platforms leads to an incre ase of global satisfaction without, unexpectedly, an incre ase
of polarization, with respect to the single platform case. I n fact, more active (i.e. more extreme) users separate from
users with “low” activity (i.e. more moderate), thus the lat ter are no longer inﬂuenced by the former, resulting in a
reduced (or, at least, not increased) polarization.
While our multiplatform opinion dynamics model oﬀers a comp rehensive framework for understanding interactions
across diverse platforms, it is imperative to acknowledge t he inherent constraints and nuances that underpin its desig n.
The following considerations delve into these aspects, she dding light on both the model’s robustness and areas that
warrant further reﬁnement. In the ﬁrst place, while our mode l describes social media platforms, there exist traditiona l
media not captured by it, which inﬂuence users’ opinions. Br oadcasting platforms such as TVs and radios are an
example, contributing to opinion formation in a way which is structurally and temporally diﬀerent from social media.
2W e assume that K (γ) = K for all γ, implying that they all have the same political focus.
3Note however that there are some important diﬀerences betwe en liberals and conservatives that the model cannot
capture
5

0.00 1.00 2.00 3.00 4.00 5.00
β
(2)
0.00
1.00
2.00
3.00
4.00
5.00
β
(1)
ΔΔ U ⟨
|Δ U ⟨
1
|
⟩0.2
0.0
0.2
0.4
(a)
0.00 1.00 2.00 3.00 4.00 5.00
β
(2)
0.00
1.00
2.00
3.00
4.00
5.00
β
(1)
Δ σ ( x )
σ
1
( x )
−0.3
−0.2
−0.1
0.0
0.1
0.2
(b)
Figure 4: Relative increment passing from Γ = 1 to Γ = 2 platforms of (a) s atisfaction and (b) opinions’
standard deviation. Neglecting the ﬁrst row and the last col umn ( β(1) = 0 or β(2) = 0), which correspond to
a radicalized regime, for “moderate” values of homophilic a lgorithm (e.g. β(1) = 1 and β(2) = 2), an increased
satisfaction ( ≈ 40%) is clear. Moreover, in such points, the standard deviat ion relative increse in negligible
(≈ 0%). For very high values of homophilic recommendations (e. g. β(1) = 5 and β(2) = 5), the satisfaction
drops signiﬁcantly while the standard deviation increases , making this the worst possible scenario.
With reference to our model, they would act as hub nodes in the network of interactions, each diﬀusing a certain opinion
to other nodes. However such nodes, unlike “normal” ones, do not change (or, rather, change very slowly) their opinions
over time. Thus, eﬀectively, traditional platforms can be s een as idiosyncratic relaxation terms in Eqn. 1, as opposed to
having all opinions relax to zero xi(∞) = x∗ = 0 when K (γ) = 0 for all γ. The interplay between these two sources of
information is left for future studies.
Regarding how users are aﬀected by peers, while we assume tha t they converge (i.e. their opinions approach each
other when interacting), other models [ 14, 34–36] consider also the presence of “polarizing” nodes, whose op inions move
away if exposed to those of opposite sign. Since this charact erization does not qualitatively change our results, we neg lect
it. In fact, as we have shown, both polarization and consensu s emerge without the introduction of this additional featur e.
Our last assumption is the conservation of activity over tim e, i.e. ai(t) = ai ∀i, t. In modeling users’ satisfaction
across platforms, it would be reasonable to require that use rs’ activity (which corresponds to users’ engagement on soc ial
platforms) could decrease if they are not able to reach a cert ain degree of satisfaction (i.e. a certain value of their uti lity).
However, modeling such behavior would require a clear deﬁni tion of what a decreasing activity really mean — do users
move their attention to traditional media? Do they allocate their SMR on a not-considered social platform? Or do they
literally stop consuming news? — W e believe that it is reason able to assume the considered system (which, we note,
can be made arbitrary large by increasing N and/or Γ) as an isolated social system, in which social energy (i.e. users’
activity) is conserved 4. In fact, it is possible to think that our model is valid in a sp an of time T in which activities
4Although note that daily time spent on social media by intern et users worldwide has been steadily increasing from
6

remain constant, meaning that they change on a time scale muc h greater than T .
Finally, we want to stress how β(γ) encapsulates the role of the recommendation engine of platf orm γ. Typically,
recommendation systems aim to infer users’ needs, tastes an d preferences, on the basis of their behavior on the platform ,
in order to suggest them the “best” product [ 38]. In terms of social media platforms, recommendation syste ms try
to connect people who are “similar” according to some metric . Obviously, diﬀerent platforms collect diﬀerent kind of
users’ data, deploy diﬀerent recommendation algorithms an d have diﬀerent purposes. Such dissimilarities translate i nto
a non-homogeneous degree of recommendations’ homophily. W e imagine that the distances between users, evaluated
by the recommendation algorithms by considering the huge am ount of data social media collect, can be projected into
1-dimensional distances between political opinions, furt her distorted by the degree of homophily β(γ). Such assumption
is based on the well-known phenomenon of issue alignment [ 24, 39, 40], i.e. individuals are much more likely to have a
certain combination of opinions than others. On this note, a n interesting extension of the model would be to consider
a multi-topic opinion dynamics on a multiplex network; the i dea would be that on a given layer/platform it might be
more likely to talk about a topic than another.
5 Model
W e consider a system of N agents, where each agent i has a one-dimensional continuous opinion variable xi(t) ∈
(−∞, +∞). The sign of xi describes the agent’s stance (e.g. being pro or against abor tion). The absolute value of xi
quantiﬁes the strength of this opinion: the larger |xi|, the more extreme the stance of agent i. Moreover, we also consider
that agents can interact on Γ diﬀerent platforms. Each agent allocates his “time” in these Γ platforms. In the following
sections we detail how opinions and interaction networks ev olve and how each agent divides his attention among the
platforms (see SI for a detailed outline of the model simulat ion).
5.1 Opinions update
The opinion dynamics is driven by the interactions among age nts, captured by a system of N coupled ordinary diﬀerential
equations,
˙xi = −xi +
Γ∑
γ=1
(
K (γ)
N∑
j=1
A(γ) ij (t) tanh (cxj ) ) . i ∈ {1, ..N } (1)
K (γ) > 0 represents the social interaction strength among agents o n platform γ. The tanh ( cx), with c > 0, embodies
the fact that an agent i inﬂuences others in the direction of his own opinion, but suc h inﬂuence is “bounded”. The term
A(γ) ij (t) is the entry of the N × N temporal Adjacency matrix A(γ)(t) corresponding to platform γ.
5.2 Network update
At every time step, user i can actively engage with the social media on platform γ with probability aiρ(γ) i , and/or
passively engage on platform γ′ with probability piρ(γ′) i 5. Active users contact users that are passive on the same
platform, meaning that the opinions of the former aﬀect the o pinions of the latter. For example, if j is active on
γ and contacts i, who is passive on γ, then A(γ) ij = 1. The term ai (resp. pi) is called activity (resp. passivity).
Moreover, ρ(γ) i represents the probability that user i, conditional on being active/passive, chooses platform γ. Of course,∑Γ
γ=1 ρ(γ) i = 1. W e assume that ai ∈ [ǫ, 1] for all i, and that the activities are distributed according to a powe r law
F (a) ∼ a−η. Moreover, we assume for simplicity that pi = 1 ∀i.
The temporal adjacency matrices A(γ) ij (t) are assumed to evolve according to an activity-driven (AD) temporal
network [ 41]. At each time step, each γ-active user contacts m γ -passive users. It is further assumed that these links
are reciprocated with probability r. The probability q(γ) ij that agent i contacts agent j on platform γ is given by the
following expression:
q(γ) ij = |xi − xj|−β(γ) ∑
k∈P (γ) |xi − xk|−β(γ) (2)
where P (γ) is the set of γ-passive users and β(γ) ≥ 0 captures the degree of homophily of γ’s recommendation algorithm.
5.3 SMR update
While for a part of our results we considered ρ(γ) i = ρ(γ) homogeneous and constant in time, we also developed a
model for which it changes on the basis of the observations of each user. In particular, we suppose that users allocate
their “social energy” among platforms depending on their pe rceived quality. Grounded on the well-known psychological
theory of optimal distinctiveness [ 30], individuals desire a balance of between assimilation (ho mophily) and diﬀerentiation
(debate)(see [ 42] for an example of discrete opinion dynamics with optimal di stinctiveness preferences). Borrowing from
bounded conﬁdence theory [ 43], an agent with opinion x considers those with opinion in [ x − r, x + r] contributing to
assimilation, while the others to diﬀerentiation. Formall y, if α(γ) i (t) (resp. δ(γ) i (t)) is the number of in-degree connections
2012 to 2023 [ 37].
5Note that we can have γ = γ′.
7

contributing to assimilation (resp. diﬀerentiation) on γ at time t for user i6, we deﬁne his utility as:
Ui(tn) = −(fi(tn) − φi)2
= −
( ∑
γ
∑n
m=n−L+1 δ(γ) i (tm) ∑
γ
∑n
m=n−L+1 δ(γ) i (tm) +∑ γ ∑n m=n−L+1 α(γ) i (tm) − φi
)2
.
(3)
Here fi(t) is the experienced distinctiveness, while φi the desired one. The parameter L encapsulates the time window
over which users perceive the distinctiveness (which, in ti me units, is τ = Ldt), thus representing their “memory”. For
example, consider Γ = 2, L = 1 and φ = 0.5. If user i is connected to user j on platform 1 with |xj − xi| < r , and to user
k on platform 2 with |xk − xi| > r at time tn, then it follows that δ(1) i (tn) = α(2) i (tn) = 0 and δ(2) i (tn) = α(1) i (tn) = 1.
Thus, fi(tn) = φi = 0.5 and Ui(tn) = 0 is maximized.
It remains to specify how users maximize their utility. They can only control the fraction of time spent on each
platform γ, proportional to ρ(γ) i (tn). W e assume that users update their platform allocation eve ry L steps, i.e. their
preferences stay constant during the time interval over whi ch assimilation and diﬀerentiation are experienced 7. For this
reason, each user can estimate the quality of platforms given her current preferences. Such estimates are in turn used
to update the platform allocation, on the basis of an anticip ated utility. It is reasonable to assume that each user acts
as if the assimilation and diﬀerentiation experienced on ea ch platform are proportional to the time spent on it. For this
reason, it is possible to write:
n∑
m=n−L+1
δ(γ) i (tm) = Lω(γ) δi (tn)ρ(γ) i (tn),
n∑
m=n−L+1
α(γ) i (tm) = Lω(γ) αi (tn)ρ(γ) i (tn).
(4)
Here, ω(γ) δi (tn) and ω(γ) αi (tn) are the diﬀerentiation and the assimilation slopes estima ted by the user i. Formally, deﬁning
ρ = (ρ(1), . . . , ρ(Γ)), each user aims to maximize:
ˆUi(ρ, tn) = −
(
ωδi (tn) · ρ
ωδi (tn) · ρ + ωαi (tn) · ρ − φi
)2
, (5)
where ωδi (tn) = ( ω(1) δi (tn), . . . , ω(Γ) δi (tn)) is the vector of diﬀerentiation slopes estimated using us er’s previous interactions
(an analogous deﬁnition holds for the assimilation slopes ωαi (tn)). ˆUi(ρ, tn) is the utility estimated by user i at time
tn. He assumes that it represents his future satisfaction (i.e . for t > t n) depending on how he reallocates his ρi(tn+1).
His assumption lies on hypothesizing that the slopes ωαi and ωδi are roughly constant in time (which, instead, can vary
due to the reallocation of all the other agents). User i updates then according to:
ρi(tn+1) =
{
ρi(tn) if n/L /∈ N
arg maxρ ˆUi(ρ, tn) otherwise . (6)
Clearly, the utility of user i depends not only on his ρi, but also on how the other users have allocated their time on
social media. Let us stress that in our model, users can only d ecide whether to be on a particular platform, but the
connections are decided entirely by the recommendation alg orithm. A justiﬁcation for this comes from the work of [ 44],
which shows that on Facebook the number of new links per day in creased abruptly after the introduction of a “who
to follow” recommendation algorithm. In other words, the in dividual agency in choosing connections is negligible with
respect to the volume of content suggested by the platform it self.
5.4 Combined dynamics
W e focus on a regime in which the three processes described ab ove have diﬀerent time scales. As already mentioned,
we consider the network dynamics being much faster than the o pinion dynamics. This is especially true in online
social media context. In particular, for each network updat e we integrate Eq ( 1) for dt = 0 .001. Moreover, the SMR
dynamics lies between the two, representing the fact that th e choice of the allocation among platforms is faster than the
opinion dynamics, but requires a signiﬁcant number of obser vations and interactions. Speciﬁcally, each user updates h is
preferences ρi(tn) every L = 100 time steps. In short, every L = 100 network updates each user modiﬁes her allocation
preferences, and every 1000 network updates the opinions ev olve of a unit time.
6 Conclusions
Our study examines the impact of social media competition fo r users’ engagement on opinion dynamics. First, we show
that opinion polarization can persist as long as users spend a fraction of their time on a homophilic platform, highlight ing
the importance of multi-sources news diets. Second, we show that individual users’ preferences interact in a non-trivi al
way with the recommendation algorithms in the presence of mu ltiple platforms. The model indeed predicts the observed
relationship between news outlet preference and political ideology. Interestingly, a multi-platform setup may be use d
to curb polarization while keeping user engagement intact. To this end, it is paramount to experimentally investigate
6αγ i (t) + δγ i (t) is always equal to the total in-degree of node i. 7In other words, users gather experience before changing the ir mind about a given social media.
8

users preferences for diversity (estimates for φ), either via surveys or controlled experiments. This avenu e may help
to shed light on healthy synergies between diﬀerent social m edia platforms. From the revenue point of view, synergies
are already well-known in this environment (think about use rs spending time on Whatsapp, Instagram and Facebook
without ever going out from the Meta universe). Future resea rch and eﬀorts should thus gather cross-platform data,
via survey [ 29, 45] or by experiments, in order to fully comprehend the subtle m echanism of opinion formation in online
environments.
Acknowledgments
The work of D.G. has been supported by the European Union – Hor izon 2020 Program under the scheme “INFRAIA-01-
2018-2019 – Integrating Activities for Advanced Communiti es”, Grant Agreement n. 871042, “SoBigData++: European
Integrated Infrastructure for Social Mining and Big Data An alytics” http://www.sobigdata.eu, by the NextGenera-
tionEU – National Recovery and Resilience Plan (Piano Nazio nale di Ripresa e Resilienza, PNRR) – Project: “So-
BigData.it – Strengthening the Italian RI for Social Mining and Big Data Analytics” – Prot. IR0000013 – Avviso n.
3264 del 28/12/2021. A.S. and D.G. acknowledge support from the Dutch Econophysics Foundation (Stichting Econo-
physics, Leiden, the Netherlands). G.M.F. acknowledges su pport from Swiss National Science Foundation (grant number
P500PS-211064).
W e thank Fernando Santos, Yphtach Lelkes and Keena Lipsitz f or enriching comments.
References
[1] Robert M Bond, Christopher J Fariss, Jason J Jones, Adam D I Kramer, Cameron Marlow, Jaime E Settle,
and James H Fowler. A 61-million-person experiment in socia l inﬂuence and political mobilization. Nature,
489(7415):295–298, 2012.
[2] Elisa Shearer and Elizabeth Grieco. Americans are wary o f the role social media sites play in delivering the news.
Pew Research Center , 2, 2019.
[3] Pablo Barber´ a, John T Jost, Jonathan Nagler, Joshua A Tu cker, and Richard Bonneau. Tweeting from left to right:
Is online political communication more than an echo chamber ? Psychological science, 26(10):1531–1542, 2015.
[4] Cass R Sunstein. Is social media good or bad for democracy . SUR-Int’l J. on Hum Rts. , 15:83, 2018.
[5] Andrew Guess, Brendan Nyhan, Benjamin Lyons, and Jason R eiﬂer. Avoiding the echo chamber about echo
chambers. Knight Foundation, 2(1):1–25, 2018.
[6] Eytan Bakshy, Solomon Messing, and Lada A Adamic. Exposu re to ideologically diverse news and opinion on
facebook. Science, 348(6239):1130–1132, 2015.
[7] Michela Del Vicario, Alessandro Bessi, Fabiana Zollo, F abio Petroni, Antonio Scala, Guido Caldarelli, H Eugene
Stanley, and W alter Quattrociocchi. The spreading of misin formation online. Proceedings of the national academy
of Sciences , 113(3):554–559, 2016.
[8] Kiran Garimella, Gianmarco De Francisci Morales, Arist ides Gionis, and Michael Mathioudakis. Political discours e
on social media: Echo chambers, gatekeepers, and the price o f bipartisanship. In Proceedings of the 2018 world
wide web conference , pages 913–922, 2018.
[9] Ferenc Husz´ ar, Soﬁa Ira Ktena, Conor O’Brien, Luca Bell i, Andrew Schlaikjer, and Moritz Hardt. Algorithmic
ampliﬁcation of politics on twitter. Proceedings of the National Academy of Sciences , 119(1):e2025334119, 2022.
[10] Ro’ee Levy. Social media, news consumption, and polari zation: Evidence from a ﬁeld experiment. American
economic review, 111(3):831–870, 2021.
[11] Brendan Nyhan, Jaime Settle, Emily Thorson, Magdalena W ojcieszak, Pablo Barber´ a, Annie Y Chen, Hunt Allcott,
Taylor Brown, Adriana Crespo-Tenorio, Drew Dimmery, et al. Like-minded sources on facebook are prevalent but
not polarizing. Nature, pages 1–8, 2023.
[12] Petter Holme and Mark EJ Newman. Nonequilibrium phase t ransition in the coevolution of networks and opinions.
Physical Review E , 74(5):056108, 2006.
[13] Xin W ang, Antonio D Sirianni, Shaoting Tang, Zhiming Zh eng, and Feng Fu. Public discourse and social network
echo chambers driven by socio-cognitive biases. Physical Review X , 10(4):041042, 2020.
[14] Fernando P Santos, Yphtach Lelkes, and Simon A Levin. Li nk recommendation algorithms and dynamics of
polarization in online social networks. Proceedings of the National Academy of Sciences , 118(50):e2102141118,
2021.
[15] Fabian Baumann, Philipp Lorenz-Spreen, Igor M Sokolov , and Michele Starnini. Modeling echo chambers and
polarization dynamics in social networks. Physical Review Letters , 124(4):048301, 2020.
[16] William Hart, Dolores Albarrac ´ ın, Alice H Eagly, Inge Brechan, Matthew J Lindberg, and Lisa Merrill. Feeling val-
idated versus being correct: a meta-analysis of selective e xposure to information. Psychological bulletin, 135(4):555,
2009.
[17] Uwe Hasebrink and Jutta Popp. Media repertoires as a res ult of selective media use. a conceptual approach to the
analysis of patterns of exposure. Communications, 31(3):369––387, 2006.
[18] Dolf Zillmann. Mood management in the context of select ive exposure theory. Annals of the International Com-
munication Association, 23(1):103–123, 2000.
9

[19] Alan M Rubin. The uses-and-gratiﬁcations perspective of media eﬀects. In Media eﬀects, pages 535–558. Routledge,
2002.
[20] Edson C Tandoc Jr, Chen Lou, and Velyn Lee Hui Min. Platfo rm-swinging in a poly-social-media context: How and
why users navigate multiple social media platforms. Journal of Computer-Mediated Communication , 24(1):21–35,
2019.
[21] R Lance Holbert and William L Benoit. A theory of politic al campaign media connectedness. Communication
Monographs, 76(3):303–332, 2009.
[22] Elaine Yuan. News consumption across multiple media pl atforms: A repertoire approach. Information, communi-
cation & society , 14(7):998–1016, 2011.
[23] Uwe Hasebrink and Hanna Domeyer. Media repertoires as p atterns of behaviour and as meaningful practices: A
multimethod approach to media use in converging media envir onments. Participations, 9(2):757–779, 2012.
[24] Fabian Baumann, Philipp Lorenz-Spreen, Igor M. Sokolo v, and Michele Starnini. Emergence of polarized ideologica l
opinions in multidimensional topic spaces. Physical Review X , 11, 1 2021.
[25] Alexander J Stewart, Joshua B Plotkin, and Nolan McCart y. Inequality, identity, and partisanship: How redistribu -
tion can stem the tide of mass polarization. Proceedings of the National Academy of Sciences , 118(50):e2102140118,
2021.
[26] Eva Jonas, Stefan Schulz-Hardt, Dieter Frey, and Norma n Thelen. Conﬁrmation bias in sequential information
search after preliminary decisions: an expansion of disson ance theoretical research on selective exposure to infor-
mation. Journal of personality and social psychology , 80(4):557, 2001.
[27] John V Duca and Jason L Saving. Income inequality and pol itical polarization: Time series evidence over nine
decades. Review of Income and Wealth , 62(3):445–466, 2016.
[28] Sam Bestvater, Sono Shah, Gonzalo River, and Aaron Smit h. Politics on twitter: One-third of tweets from us adults
are political. Pew Research Center , 2022.
[29] J Liedke and KE Matsa. Social media and news fact sheet. Pew Research Center’s Journalism Project , 2022.
[30] Marilynn B Brewer. The social self: On being the same and diﬀerent at the same time. Personality and social
psychology bulletin , 17(5):475–482, 1991.
[31] Rainer Hegselmann and Ulrich Krause. Opinion dynamics and bounded conﬁdence models, analysis, and simulation.
Journal of Artiﬁcal Societies and Social Simulation (JASSS ) vol , 5(3), 2002.
[32] Mirko Lai, Marcella Tambuscio, Viviana Patti, Giancar lo Ruﬀo, and Paolo Rosso. Stance polarity in political de-
bates: A diachronic perspective of network homophily and co nversations on twitter. Data & Knowledge Engineering ,
124:101738, 2019.
[33] Markus Prior. Media and political polarization. Annual Review of Political Science , 16:101–127, 2013.
[34] Christopher A Bail, Lisa P Argyle, Taylor W Brown, John P Bumpus, Haohan Chen, MB Fallin Hunzaker, Jaemin
Lee, Marcus Mann, Friedolin Merhout, and Alexander Volfovs ky. Exposure to opposing views on social media can
increase political polarization. Proceedings of the National Academy of Sciences , 115(37):9216–9221, 2018.
[35] Yotam Shmargad and Samara Klar. How partisan online env ironments shape communication with political out-
groups. International Journal of Communication , 13:27, 2019.
[36] Elizabeth Levy Paluck. Is it better not to talk? group po larization, extended contact, and perspective taking in
eastern democratic republic of congo. Personality and Social Psychology Bulletin , 36(9):1170–1185, 2010.
[37] W e Are Social, DataReportal, and Hootsuite. (january 2 6, 2023). Daily time spent on social networking by internet
users worldwide from 2012 to 2023 (in minutes) [Graph]. In St atista. Retrieved October , 23, 2023.
[38] Robin Burke. Hybrid recommender systems: Survey and ex periments. User modeling and user-adapted interaction ,
12:331–370, 2002.
[39] Delia Baldassarri and Andrew Gelman. Partisans withou t constraint: Political polarization and trends in america n
public opinion. American Journal of Sociology , 114(2):408–446, 2008.
[40] Daniel DellaPosta, Yongren Shi, and Michael Macy. Why d o liberals drink lattes? American Journal of Sociology ,
120(5):1473–1511, 2015.
[41] Nicola Perra, Bruno Gon¸ calves, Romualdo Pastor-Sato rras, and Alessandro Vespignani. Activity driven modeling
of time varying networks. Scientiﬁc reports, 2(1):469, 2012.
[42] Olivia Jessica Chu. Heterogeneity in Human Populations, from Structure to Pers onality—A Modeling and Data
Approach. Princeton University, 2021.
[43] Ulrich Krause et al. A discrete nonlinear and non-auton omous model of consensus formation. Communications in
diﬀerence equations, 2000:227–236, 2000.
[44] Bimal Viswanath, Alan Mislove, Meeyoung Cha, and Krish na P Gummadi. On the evolution of user interaction in
facebook. In Proceedings of the 2nd ACM workshop on Online social network s, pages 37–42, 2009.
[45] Trevor Diehl, Matthew Barnidge, and Homero Gil de Zunig a. Multi-platform news use and political participation
across age groups: Toward a valid metric of platform diversi ty and its eﬀects. Journalism & Mass Communication
Quarterly, 96(2):428–451, 2019.
10

Supplementary information
A Pseudo code
In each time step of the numerical algorithm the opinions, th e temporal matrix and the SMR are update according to
the following steps:
1. Each user i is only active with probability ai(1 − pi), only passive with probability (1 − ai)pi, active and passive
with probability aipi and inert with probability (1 − ai)(1 − pi).
2. If active (resp. passive), user i chooses the platform γ (resp γ′) on which he actively (resp. passively) engages
with probability ρ(γ) i (t) (resp. ρ(γ′) i (t)) Note that it could be γ = γ′.
3. If active on platform γ, agent i inﬂuences m distinct agents j ∈ P (γ) — where P (γ) is the set of users passively
engaged on platform γ — chosen according to Eqn. ( 2). This inﬂuence is expressed by updating the temporal
adjacency matrix A(γ) ji (tn) = 1.
4. With probability r the directed link is reciprocated, so that agent i receives inﬂuence from j, i.e. A(γ) ij (tn) = 1.
5. Opinions xi are updated by numerically integrating Eq. ( 1) using the total adjacency matrix elements Aij (tn) =∑Γ
γ=1 A(γ) ij (tn).
6. Each user i collects the experienced assimilation and diﬀerentiation on each platform at the time step tn as:
α(γ) i (tn) = ∑
j s.t. |xi−xj |<r
A(γ) ij (tn)
δ(γ) i (tn) = ∑
j s.t. |xi−xj |>r
A(γ) ij (tn).
7. If mod ( tn, L) ⁄= 0, then the SMR remains constant for all users ρi(tn+1) = ρi(tn) ∀i. If mod ( tn, L) = 0,
each user updates his SMR according to the following steps:
(a) estimate diﬀerentiation and assimilation slopes ωδi (tn) and ωαi (tn) according to Eqn. ( 4)
(b) updates SMR according to ρi(tn+1) = arg max ρ ˆUi(ρ, tn), where ˆUi(ρ, tn) is deﬁned in Eq. ( 5). To perform
the utility maximization, we use a gradient descent algorit hm on the Γ-dimensional simplex, consisting of
nGD iterations of learning rate ∆ GD. In particular, the following equation is iterated nGD times:
ρi(k + 1) = PΓ
(
ρi(k) − ∆GD∇ ˆUi(ρi(k), tn) ) ,
where PΓ is the projection on the Γ-dimensional simplex, k runs from k = 0 to k = nGD − 1, ρi(0) = ρi(tn)
and ρi(nGD) = ρi(tn+1).
8. After each time step the temporal networks A(γ) ij (tn) are deleted.
Of course, when we considered a homogeneous and stationary ( HS) SMR, steps 6. and 7. are ignored, i.e. ρi(tn) = ρi(t0)
∀i, t. As done in [ 15], we integrate Eq. ( 1) using an explicit fourth-order Runge-Kutta method with a t ime step of dt = 0.01
in the case of HS SMR, and dt = 0 .001 in the case of evolving SMR. In the latter, we also conside r L = 100. This
leads to a timescale separation between the network dynamic s, the SMR update and the opinion evolution mentioned
in Sec. 5.4.
W e independently sampled activities {ai}N i=1 from the power law F (a) = (1 − η)a−η /(1 − ǫ1−η), with parameters
η = 2 .1 and ǫ = 0 .01 [ 15]. W e also set pi = 1 ∀i. Moreover, we consider the following parameters’ values: N = 800,
r = 0.5 and c = 3.
Throughout all of our simulations, we start with initial opi nions {xi(0)}N i=1 uniformly distributed in [ −1, 1]. In the
case of dynamical SMR, we let the opinions evolve for nboot = 2000 steps before allowing users to reallocate themselves
(i.e. we ignore point 7. for the nboot steps before t0). The reason is that we want to provide as input to our SMR
update model an opinions’ spectrum which is at (metastable, in the case of polarization) equilibrium . W e initialize
ρi(tn) = 1 /Γ ∀n ∈ {− nboot + 1, . . . ,0}. Then, at t0, we “turn on” the SMR allocation described in point 7. of the
pseudo-code.
B Robustness of the phase diagram
Here we show the phase-diagram reported in the main text with β(2) = 2, i.e. assuming the polarizing platform provides
more cross-cutting content. By comparing Fig. 3 and Fig. S1, we can see that the green region shrinks as β(2) decreases,
in accordance with the meta-stability analysis of polariza tion reported in [ 15].
C Multi-platform segregation
To understand the beneﬁts of the multi-platform reported in the main text, we deﬁne the following quantities.
f > γ (t) =
∑N
i=1 ρ(γ) i (t)H(ai − θ) ∑N
i=1 H(ai − θ)
f < γ (t) =
∑N
i=1 ρ(γ) i (t)H(θ − ai) ∑N
i=1 H(θ − ai)
,
(S1)
11

0.00 0.89 1.78 2.67 3.56
K
(2)
0.50
0.72
0.95
ρ
(1)
Phase Diagram
NC
R
P
Figure S1: Phase diagram in the case β(1) = 0 , β(2) = 2. The other parameters are as in the corresponding
Fig. 3 reported in the main text.
where H is the Heaviside function. In words, f > γ (t) (resp. f < γ (t)) is the “eﬀective” share of users on platform γ whose
activity is above (resp. below) a threshold θ. The idea is to understand whether these two classes of users exhibit
qualitatively diﬀerent behavior, notwithstanding their a -priori equal preferences (i.e. φi = φ and ri = r for all users).
Let us consider the 2 platform case reported in the main text, where β(1) = 2 , β(2) = 1. In Fig. S2, we plot f > 1 (t)
and f < 1 (t) for θ = 0 .1, which roughly divide the activity proﬁle in 90 % below the t hreshold and 10% above. Highly
active users deterministically prefer the more homophilic platform ( f > 1 ≈ 1), while less active users tend to explore both,
though they prevalently occupy the platform with more cross -cutting content ( f < 1 ≈ 0.3)
This is consistent with what we observe in reality, i.e. peop le with extreme opinions tend to have a more restricted
outlet of like-minded sources, which further polarizes the ir view. On the other hand, more moderate users typically
exhibit a more diverse news diet.
0 1 2 3 4 5 6 7 8
t
0.3
0.4
0.5
0.6
0.7
0.8
0.9
f
>
1
( t )
f
<
1
( t )
Figure S2: Eﬀective share of users on platform 1 in the case where β(1) = 2 , β(2) = 1. θ = 0 .1, so that
approximately 90% of individuals have ai < θ .
D Robustness with respect to desired distinctiveness
Here, we want to show how satisfaction and opinions standard deviation change with respect to the single-platform case
for φ = 0.1. The main physical diﬀerence with respect to the case prese nted in the main text (where φ = 0.2) is that here
users have an “halved” desire for diﬀerentiation, meaning t hat their maximal satisfaction requires a much high number
of interactions contributing to assimilation, with respec t to those contributing to diﬀerentiation. Figure S3 shows indeed
how users’ utility is maximized in those regimes for which th ey are more exposed to like-minded peers, i.e. for high value s
of β(1) and β(2). However, in this case, maximizing users’ satisfaction lea ds to an increase in polarization, meaning that
if users desire high conﬁrmation opinions tend to extremize .
12

0.00 1.00 2.00 3.00 4.00 5.00
β
(2)
0.00
1.00
2.00
3.00
4.00
5.00
β
(1)
ΔΔ U ⟨
|Δ U ⟨
1
|
⟩1.5
⟩1.0
⟩0.5
0.0
(a)
0.00 1.00 2.00 3.00 4.00 5.00
β
(2)
0.00
1.00
2.00
3.00
4.00
5.00
β
(1)
Δ σ ( x )
σ
1
( x )
−0.4
−0.3
−0.2
−0.1
0.0
0.1
0.2
(b)
Figure S3: Relative increment of (a) satisfaction and (b) opinions’ st andard deviation, when passing from
Γ = 1 to Γ = 2 platforms, for φ = 0 .1. In this regime, high values of both β(1) and β(2) lead to an increased
users’ satisfaction but also in an increased polarization ( i.e. standard deviation).
13
