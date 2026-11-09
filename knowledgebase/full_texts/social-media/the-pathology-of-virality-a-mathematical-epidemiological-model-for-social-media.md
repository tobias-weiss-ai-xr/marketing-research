---
title: 'The Pathology of Virality: A Mathematical Epidemiological Model for Social Media Marketing'
url: https://doi.org/10.62476/amma112344
category: social-media
subcategory: framework
date: 2026-08
venue: Advanced mathematical models & applications.
authors: []
source: openalex-oa
pdf_url: https://api.jomardpublishing.com/api/main/articles/download?source=storage/journals/advanced-mathematical-models-applications/issues/pdf/2026/the-pathology-of-virality-a-mathematical-epidemiological-model-for-social-media-marketing.pdf
pages: 19
chars: 63183
fetched_at: '2026-11-08T19:31:21+00:00'
kb_version: 1
---

# The Pathology of Virality: A Mathematical Epidemiological Model for Social Media Marketing

Advanced Mathematical Models & Applications
Vol.11, No.2, 2026, pp.344-362
https://doi.org/10.62476/amma112344
THE PATHOLOGY OF VIRALITY: A MATHEMATICAL
EPIDEMIOLOGICAL MODEL FOR SOCIAL
MEDIA MARKETING
ID Tichaona Chikore
Department of Mathematics and Applied Mathematics, University of Johannesburg,
Johannesburg, South Africa
Abstract. The exponential growth of inﬂuencer-based social media marketing (SMM) has been paralleled by
increasing concerns about its long-term economic viability, speciﬁcally return on investment (ROI). While tradi-
tional metrics focus on short-term engagement, this study examines the systemic sustainability of SMM through
an epidemiological lens. We introduce a Swarm Inﬂuence Dynamics (SID) model that formalizes inﬂuencer be-
havior as adaptive particles in a content space, incorporating a digital behavioral pathogen called contentitis,
representing compulsive production driven by algorithmic feedback. Our methodology integrates swarm intelli-
gence with compartmental epidemiological modeling to capture the endogenous dynamics of attention economies.
Results reveal a critical phase transition: below a threshold Ψcrit, marketing thrives in a diverse, high-ROI regime;
above it, hyper-convergence on trends triggers violent saturation cycles that degrade returns into negative ter-
ritory. The model demonstrates that SMM’s worth follows a non-monotonic trajectory, with platform designs
that maximize engagement inadvertently pushing ecosystems toward pathological collapse. We conclude that
inﬂuencer marketing is only sustainable when platform architectures and marketing strategies actively maintain
diversity below the critical threshold, oﬀering design principles for algorithmic moderation and campaign timing
that avoid systemic degradation.
Keywords: Social Media Marketing, Digital Pathogens, Inﬂuencer Dynamics, Epidemiological Modeling, Atten-
tion Economy, Algorithmic Ampliﬁcation.
AMS Subject Classiﬁcation: 92D30, 91D30, 90B60, 37N25.
Corresponding author: Tichaona, Chikore, Department of Mathematics and Applied Mathematics, Univer-
sity of Johannesburg, P.O Box 524, Auckland Park, Johannesburg, South Africa, Tel.: +27115592790, e-mail:
tichaona.chikore@gmail.com
Received: 8 January 2026; Revised: 16 February 2026; Accepted: 3 March 2026; Published: 3 August 2026.
1 Introduction
The contemporary digital framework has transformed social media marketing from an experi-
mental channel into a dominant economic force, with global expenditures projected to exceed
$250 billion by 2027 (ResearchAndMarkets.com, 2025; Morris, 2025; Adams, 2025). However,
beneath this rapid growth lies a structural tension: as marketing investments scale, the long-
term dynamics of attention extraction may become increasingly fragile. Traditional marketing
frameworks often assess success through isolated engagement metrics such as reach, impressions,
and click-through rates, but they rarely incorporate the systemic eﬀects that emerge when large
numbers of inﬂuencers simultaneously optimize for algorithmic visibility. This raises the ques-
tion of whether the sustained pursuit of virality could destabilize the attention economy itself.
Moreover, the mathematical formalization of social media marketing dynamics remains largely
344

T. CHIKORE: EPIDEMIOLOGICAL MODEL FOR SOCIAL MEDIA MARKETING...
unexplored, with only a few studies rigorously modeling how content creation, attention alloca-
tion, and behavioral contagion interact to produce systemic outcomes. This scarcity of formal
frameworks underscores the need for a structured taxonomy of observable behaviors, digital
pathogens, and model abstractions that can anchor social media marketing within a coherent
theoretical foundation. Systematically linking real-world phenomena to mathematical represen-
tations not only clariﬁes existing models but also establishes a roadmap for future research,
enabling the integration of diverse data streams, cross-platform dynamics, and novel behavioral
mechanisms into a uniﬁed framework for understanding and predicting marketing outcomes.
The rapid expansion of global internet access and the proliferation of digital platforms have
fundamentally restructured the architecture of information dissemination, commercial market-
ing, and cultural production (Javaid et al., 2024). Content creation has evolved from a scarce
activity governed by institutional gatekeepers into a ubiquitous, high-velocity process driven by
individual users and professional inﬂuencers (Agrawal, 2016; Hughes et al., 2019). Within this
hyper-connected setting, social media marketing (SMM) has emerged as a dominant paradigm,
leveraging inﬂuencer-driven content to capture consumer attention and inﬂuence purchasing
behavior (Migkos et al., 2025; Libai et al., 2025). While existing scholarship has examined en-
gagement optimization and algorithmic ampliﬁcation, many models still emphasize short-term
performance metrics without accounting for long-term systemic consequences of content over-
production (Goel et al., 2024; Lorenz-Spreen et al., 2019).
Despite these advancements, the literature frequently treats the social media environment as
a static or exogenously deﬁned system (Bucher, 2018). Inﬂuencers are typically modeled as
rational actors optimizing engagement, while platforms are assumed to provide neutral recom-
mendation engines (Hudders et al., 2021; Mallipeddi et al., 2020). Emerging research challenges
this rational-actor assumption, emphasizing self-exploitation and performance pressure as per-
sistent inﬂuences on content production (Han, 2015). These pressures interact with algorithmic
reward structures to produce reinforcement-driven behaviors that may operate alongside or in-
dependently of deliberate rational choice (Kuss & Griﬃths, 2011; Centola, 2018). Even when
saturation or viewer fatigue is acknowledged, it is often modeled as a ﬁxed rate of diminish-
ing returns rather than as an emergent outcome of collective agent behavior (Vosoughi et al.,
2018). As a result, industry narratives often treat escalating content volume as beneﬁcial as
long as engagement metrics remain positive, while little attention is given to potential systemic
destabilization from synchronized optimization (Williams, 2018).
A key gap remains the absence of a formal dynamical framework capable of describing tran-
sitions from healthy competition to destabilizing production cycles. Existing concepts such as
attention economies (Kubler, 2023) and digital burnout (Hemalatha & Paul Kumar, 2025) have
not been integrated into a uniﬁed model that captures both micro-level behaviors and macro-
level outcomes. Speciﬁcally, there is limited analysis of SMM under conditions of extreme
synchronized trend convergence, when production velocity is prioritized over creative diﬀerenti-
ation, necessitating a theoretical link from microscopic behavioral distortions to systemic market
outcomes (Bak-Coleman et al., 2021). This paper introduces such a bridge, proposing that cer-
tain platform-mediated behaviors (compulsive content production, accelerated consumption of
short-form video, and habitual scrolling) can be modeled as behavioral contagions reinforced by
algorithmic feedback. These are treated as operational constructs grounded in observed engage-
ment and reinforcement patterns documented in neuroscience and behavioral psychology (Kuss
& Griﬃths, 2011; Centola, 2018; Lorenz-Spreen et al., 2019).
We present an epidemiological framework that recasts social media marketing as a dynamical
system governed by swarm intelligence and behavioral contagion. Inﬂuencers are represented as
agents embedded in a digital swarm, where a successful content ”mutation” propagates to other
agents. Historical patterns, such as the rapid acceleration of fashion trends from 2015–2022,
illustrate how algorithmic reinforcement can compress creative lifecycles and intensify competi-
tive pressures (Postdigitalist, 2025; Future Startup, 2023). Within this framework, the economic
345

ADVANCED MATHEMATICAL MODELS & APPLICATIONS, V.11, N.2, 2026
value of inﬂuencer marketing emerges as a collective property of the ecosystem rather than solely
as a function of individual content quality (Frontiers in Communication, 2025). As agents repli-
cate content to capture algorithmic rewards, the system may shift between distinct regimes.
Periods of niche diversity can give way, under intensiﬁed contagion and synchronization, to ho-
mogenized states in which trend convergence suppresses diﬀerentiation and accelerates attention
fatigue (Strong, 2025; Putri et al., 2024; Are, 2025). Central to this analysis is contentitis, de-
ﬁned as a behavioral state characterized by persistent content production reinforced through
social and algorithmic feedback (Konovalov & Bozhkova, 2022; Nyabadza & Chikore, 2025).
Modeling this phenomenon through Swarm Inﬂuence Dynamics reveals a non-monotonic trajec-
tory for marketing eﬀectiveness: beneﬁcial in diverse ecosystems, marginal during competitive
escalation, and potentially counterproductive under hyper-synchronized conditions.
Methodologically as illustrated in the framework in Figure 1, this work synthesizes swarm-
based optimization with epidemiological modeling. Inﬂuencers are adaptive agents navigating a
multi-dimensional content space, and pathological behaviors are aggregated through a mean-ﬁeld
reduction to a macroscopic system describing susceptible, infected, and attention populations.
This reduced system aligns with well-studied SIR-type epidemiological models with behavioral
feedback, providing analytical validation for the aggregation from agent-level dynamics. This
approach enables systematic analysis across healthy, marginal, and pathological regimes and
treats the economic value of social media marketing as an endogenous, state-dependent outcome.
The analysis provides a formal framework for identifying critical thresholds between sustainable
and destabilizing regimes, links individual behavioral reinforcement to ecosystem-level dynamics,
and oﬀers a predictive tool for assessing marketing viability based on systemic state rather
than isolated metrics. By framing social media marketing as an epidemiological process, the
paper contributes both analytical insights for platform stability and guidance for designing
more sustainable digital economies.
2 Methodology
We extend the Swarm Inﬂuence Dynamics framework by incorporating digital pathogens into
the inﬂuencer-level state space. We focus on contentitis, deﬁned as a compulsive drive toward
continuous content generation at the expense of cognitive well-being. Each inﬂuencer i is char-
acterized at time t by the state vector
(xi(t), vi(t), pi(t),ai(t),wi(t)),
where xi(t) denotes the inﬂuencer’s position in the interaction space, vi(t) their adaptation ve-
locity, pi(t) their inﬂuence or persuasion vector, ai(t) their activity or attention allocation level,
and wi(t) their cognitive well-being. We augment this state vector with a pathological marker
ci(t)∈ [0, 1], which quantiﬁes the severity of compulsive content production. The extended state
of inﬂuencer i is therefore
(xi(t), vi(t), pi(t),ai(t),wi(t),ci(t)).
The pathogen’s dynamics are governed by a dual process of social contagion and internal rein-
forcement. For each inﬂuencer i, the temporal evolution of the pathological content-production
level ci(t)∈ [0, 1], which quantiﬁes the severity of compulsive content generation at time t,
follows a diﬀerential equation incorporating exposure, susceptibility, and recovery:
dci
dt =βc
(
1−ci(t)
)∑
j∈Ni
Aijcj(t) +ηp|F (xi(t),t )−F (xi(t− 1),t )|− (γr +γb +γa)ci(t). (1)
The parameterNi denotes the social neighbourhood of inﬂuencer i, and Aij is the weighted
adjacency matrix encoding the strength of observational exposure from agent j to agent i.
346

T. CHIKORE: EPIDEMIOLOGICAL MODEL FOR SOCIAL MEDIA MARKETING...
Real Phenomena
Digital Pathogens
Swarm Model
Mean-Field
SIR Validation Analytical Validation
Economic
Predictions
Figure 1: Framework architecture: starting from observable social media behaviors (“Real Phe-
nomena”), we identify digital pathogens, develop a swarm-based model, reduce it to a mean-ﬁeld
system, and validate it analytically and with an SIR-type model to produce economic predictions.
The parameter βc > 0 represents the transmission rate of compulsive behaviour through social
observation. The factor 1−ci(t) measures the remaining cognitive regulation capacity of agenti,
while F (x,t ) denotes the engagement or ﬁtness framework evaluated at content position x and
time t. The reinforcement coeﬃcient ηp> 0 captures panic posting behaviour, whereby both
positive and negative engagement ﬂuctuations reinforce compulsive production through absolute
engagement shocks. Recovery from the pathological state is decomposed into three distinct
pathways: γr governing temporary recovery to a susceptible state, γb representing burnout and
prolonged disengagement, and γa accounting for permanent platform abandonment. In other
words, the rate of change of the inﬂuencer compulsive posting level ci(t) describes how quickly
their behaviour becomes more intense or begins to ease over time. This rate increases when the
inﬂuencer watches others who already post in a compulsive way, especially when those others
are highly visible or inﬂuential, and when sudden jumps in engagement create pressure to keep
posting more. At the same time, the rate decreases when diﬀerent recovery processes begin to
act, such as short breaks, deeper burnout that leads to longer disengagement, or a ﬁnal decision
to leave the platform completely, as formalized in Equation (1).
The rate of change of an inﬂuencer’s content strategy depends on both their personal prefer-
ences and the inﬂuence of global trends. Their velocity in content space, representing how fast
and in what direction they change topics, style, or format, is determined by a combination of
factors: memory of previous content decisions, attraction toward their own preferred style, pull
toward the most popular global trends, and resistance due to the eﬀort or diﬃculty of producing
certain content. Random ﬂuctuations account for unpredictable changes in attention, mood, or
external feedback. Pathological behavior modiﬁes these dynamics by increasing responsiveness
to trends and peer inﬂuence while reducing self-restraint, so compulsive inﬂuencers are more
likely to follow trends quickly and take creative shortcuts. This framework captures how indi-
347

ADVANCED MATHEMATICAL MODELS & APPLICATIONS, V.11, N.2, 2026
vidual goals, social pressures, and cognitive constraints interact to shape content evolution, as
formalized in Equation (2). The core velocity update equation of the Swarm Inﬂuence Dynamics
model is modiﬁed to reﬂect the cognitive and behavioural distortions induced by the pathological
state. The velocity vi(t) of inﬂuencer i in content space evolves according to:
vi(t + 1) =ω(t)vi(t) +c1r1(t)ψ(pi(t)− xi(t)) +c2w∗ i (t)r2(t)ξ(g(t)− xi(t))−λ∗∇C(xi(t)), (2)
where xi(t) denotes the content position of agent i (the current thematic or stylistic location
of the creator’s output, such as topic, tone, or format), pi(t) is its individual reference position
(the creator’s preferred or habitual content identity), andg(t) denotes the global trend attractor
(the dominant topic or style receiving maximal collective attention at time t). The coeﬃcients
r1(t),r 2(t)∼U(0, 1) are independent random variables (capturing unpredictable ﬂuctuations in
attention, mood, or external feedback), while c1,c 2> 0 scale individual and social acceleration,
respectively (setting how strongly creators respond to personal goals versus social pressure). The
functionsψ(·) andξ(·) are attraction kernels (mapping distance in content space to motivational
pull toward one’s own style or toward trends), andC(x) is a creative cost landscape (representing
the cognitive and eﬀort cost of producing content at position x, such as novelty or complexity),
with gradient ∇C (acting as resistance against costly creative moves). The baseline social
sensitivity wi(t) (normal responsiveness to trends and peer behavior) and creative inhibition
parameter λ (self-restraint arising from fatigue, quality concerns, or long-term planning) are
pathologically altered according to w∗ i (t) =wi(t)(1 +ξwci(t)) (ampliﬁed trend reactivity under
compulsion) and λ∗ = λ(1−ξλci(t)) (reduced self-control as compulsive behavior increases),
with ξw,ξλ> 0 (strengths of pathological ampliﬁcation and inhibition loss).
How strongly an inﬂuencer continues producing content in the same style or topic over time
is determined by the inertia term ω(t). It decreases both when their current content is far from
the dominant global trend and when compulsive behavior is high, meaning that pathological
inﬂuencers switch topics more rapidly and show less consistency. The formal expression of this
inertia is given in Equation (3) as:
ω(t) =ω0 exp
(
−γ‖g(t)− xi(t)‖2−γωci(t) ) , (3)
whereω0 is the baseline inertia (the tendency to continue producing similar content over time),
γ >0 controls sensitivity to trend deviation (how quickly creators abandon content that is far
from what is popular), and γω > 0 is the inertia decay coeﬃcient speciﬁc to pathological com-
pulsion (capturing accelerated switching and loss of consistency under compulsive production).
Each inﬂuencer has a limited attention capability in terms of their mental energy, focus, and
emotional capacity for creating content. This attention naturally recovers over time, but it is
reduced by managing audience engagement and feedback, and second, by the extra strain of
compulsively producing content quickly. In other words, the rate of change of an inﬂuencer’s
attention depends on how much rest they get, how much energy they spend interacting with
their audience, and how intensely they are posting due to compulsive behavior. The attention
budget ai(t)∈ [0, 1], representing the ﬁnite cognitive resources of inﬂuencer i (mental energy,
focus, and emotional capacity available for content creation), evolves according to:
dai
dt =ρ
(
1−ai(t)
)
−ζF (xi(t),t )−νci(t)‖vi(t)‖, (4)
where ρ >0 is the natural recovery rate (rest, downtime, and recovery of cognitive resources),
ζ >0 captures engagement-induced depletion (attention loss due to managing feedback, metrics,
and audience response), and ν >0 scales additional exhaustion arising from compulsive velocity
under contentitis (burnout caused by rapid, relentless content production driven by compulsion).
To model the audience-mediated “lurker” eﬀect (see also Sun et al. (2014)), where pathogen
transmission occurs indirectly through engagement metrics, the ﬁtness framework is coupled to
348

T. CHIKORE: EPIDEMIOLOGICAL MODEL FOR SOCIAL MEDIA MARKETING...
the total attention poolA(t) and the density of infected content. Within this framework, the ac-
cumulation of attention is critically driven by consumption-based pathogens, speciﬁcally reelisis
(the compulsive consumption of short-form video) and clickophilia (the motor-level compulsion
of scrolling and clicking), which sustain the velocity of the attention cycle (Nyabadza & Chikore,
2025). The dynamics of the audience attention pool are governed by:
dA
dt = Λ−δA(t)−
∫
X
ψ(x)ρ(x,t )dx−φ⊮A>AcritA(t), (5)
The term Λ > 0 is the inﬂux of new attention (new users or renewed focus), while δ > 0
represents the natural decay of attention over time due to cognitive fatigue or shifting interests.
The term ψ(x) quantiﬁes the rate at which attention is harvested by content at position x; in
this model, ψ is ampliﬁed by reelisis , which utilizes rapid novelty to bypass reﬂective ﬁlters
and maximize extraction. The integral term
∫
Xψ(x)ρ(x,t )dx represents the total amount of
audience attention being consumed by all content across the platform. The term φ⊮A>AcritA(t)
represents the “lurker-to-creator” eﬀect which, when the total attention pool A(t) exceeds a
critical threshold Acrit, the intermittent reinforcement and motor-habituation of clickophilia
trigger passive observers to transition into active content producers. This threshold-crossing
eﬀectively converts “lurkers” into new vectors for behavioral contagion, thereby expanding the
density of potentially compulsive agents within the university ecosystem.
The way content attracts engagement is inﬂuenced by the collective compulsive behavior
of inﬂuencers. Posts that were successful in the past make similar content more likely to be
produced, with the eﬀect stronger for content that is close in theme or style to what was
previously posted. This compulsion naturally fades over time, but the attention of the audience
and the concentration of similar compulsive posts can further amplify the popularity of certain
content, creating a feedback loop where repeated posting drives disproportionate engagement.
The engagement structure is perturbed by the collective pathology, with the modiﬁed ﬁtness
function given by:
F∗(x,t ) =F (x,t ) +κci(t)· exp
(
−‖x− xi(t− 1)‖2
2σ2c
)
· exp(−∆t/τc) +ϵA(t)ρc(x,t ). (6)
In Equation (6), κ >0 quantiﬁes ”content momentum,” meaning past successful posts in-
crease the attractiveness of similar content for the infected agent. The Gaussian kernel with
width σc ensures that content similar to the previous post receives a stronger boost, modeling
semantic proximity. The factor exp(−∆t/τc) introduces temporal decay with timescale τc, rep-
resenting how compulsion fades over time. The additional term ϵA(t)ρc(x,t ) couples ﬁtness to
the audience attention and density of infected content, capturing how compulsive posts capture
disproportionate attention. Hence, the term κci(t)·exp
(
−‖x−xi(t−1)‖2 2σ2c ) ·exp(−∆t/τc) represents
the momentum from an inﬂuencer’s previous posts since compulsive inﬂuencers are more likely
to repeat similar content, and this eﬀect is stronger for content that closely resembles their prior
posts, but it gradually fades as time passes.
At the population level, the total content distribution changes over time due to the movement
of regular and infected inﬂuencers through content space, random exploration or experimenta-
tion, and new participants being recruited from passive observers. The infected agents contribute
disproportionately by moving faster and following global trends more closely, which drives the
system toward highly uniform, trend-dominated content. The model tracks the density of in-
fected agents ρc(x,t ), and the dynamics of the overall content density ρ(x,t ) include a source
term that reﬂects altered behavior, as shown in Equation (7):
∂ρ
∂t =−∇· (Js(x,t )ρs + Jc(x,t )ρc) +D∇2ρ + Σ(A,ρc), (7)
where Js(x,t ) and Jc(x,t ) are the ﬂuxes of susceptible and infected agents, respectively, derived
349

ADVANCED MATHEMATICAL MODELS & APPLICATIONS, V.11, N.2, 2026
from their velocity ﬁelds in content space. The termD∇2ρ represents random diﬀusion in content
space, capturing the tendency of agents to explore or experiment with content independently of
social trends or compulsive alignment. The source term Σ(A,ρc) quantiﬁes recruitment from the
lurker pool into active content production, reﬂecting how passive observers become active con-
tributors under attention-driven contagion. Finally, infected agents move faster and align more
strongly with the global trend g(t), formalizing the hyper-convergence behavior characteristic
of pathological social swarms.
The trend intensity I(t) is augmented to include compulsive contributions:
dI(t) =βNρ (g(t),t )dt +β′ cNρc(g(t),t )A(t)dt−αI(t)2dt +σdWt. (8)
The ﬁrst term models standard ampliﬁcation from all creators, while β′ cNρc(g,t )A(t) captures
the stronger eﬀect of compulsive agents modulated by audience attention A(t). The quadratic
term αI(t)2 models saturation eﬀects, and σdWt adds stochastic ﬂuctuations. This structure
produces faster rise and collapse of trends when the infected fraction is high.
The basic reproduction number R0 for the digital pathogen is derived from a mean-ﬁeld lin-
earization:
R0 = βc⟨A⟩ +φ⟨A/Acrit⟩ (γr +γb +γa)−ηp⟨|∆F|⟩. (9)
The term⟨A⟩ is the mean audience attention, φ captures recruitment from lurkers, and ⟨|∆F|⟩
is the expected absolute engagement ﬂuctuation. The denominator represents net recovery (in-
cluding temporary recoveryγr, burnoutγb, and abandonmentγa) reduced by reinforcement from
engagement ﬂuctuationsηp. R0> 1 deﬁnes the epidemic threshold for pathological propagation.
Creator State
xi, vi,ai,wi
Engagement Feedback
F (xi,t )
Pathological Reinforcement
Compulsion ci(t)
Distorted Behaviour
↑w∗ i,↓λ∗,↓ω
Attention Budget
ai(t)
Burnout / Exit
γb,γa
Audience Attention
A(t)
Lurker Activation
A>A crit
↓ρ(x,t)
Figure 2: Behavioural ﬂow of the Swarm Inﬂuence Dynamics model with digital pathogens.
In Figure 2, we show that individual content decisions interact with engagement feedback,
pathological reinforcement, cognitive depletion, and audience-mediated recruitment, producing
feedback loops that can drive systemic collapse. The dashed arrow represents the negative
feedback from creator burnout to audience attention, completing the boom-bust cycle where
content overproduction leads to decreased content density and eventual attention recovery. Node
colors indicate systemic health impact: green for sustainable states, yellow for transitional states,
and red for pathological or collapse-prone states. The model exhibits a phase transition between
350

T. CHIKORE: EPIDEMIOLOGICAL MODEL FOR SOCIAL MEDIA MARKETING...
a healthy, diverse content regime and a pathological monoculture. The order parameter is the
steady-state diversity D = −
∫
Xρ(x) logρ(x)dx. Analysis shows D drops sharply when the
composite parameter Ψ = c2(β +ξc¯c)/(α(γr +γb +γa)) exceeds a critical value Ψ crit, where
¯c is the endemic infection level and ξc =∂(ϵA¯c)/∂¯c quantiﬁes the coupling between audience
attention and infected content density. In the pathological regime (Ψ > Ψcrit), the swarm
experiences repeated bursts of homogenization driven by compulsive creators, followed by abrupt
collapses reﬂecting digital burnout and recovery cycles.
2.1 Moderate analysis of content density dynamics
The partial diﬀerential equation governing the evolution of the total content density is given by
∂ρ
∂t =−∇· (Jsρs + Jcρc) +D∇2ρ + Σ(A,ρc), (10)
where ρ = ρs +ρc is the total content density, D represents random exploration or creative
diﬀusion, Js and Jc denote the ﬂuxes of susceptible and infected agents, and Σ( A,ρc) models
recruitment from the lurker pool into active production.
Integrating (10) over the content domain X with no-ﬂux or periodic boundary conditions
yields
d
dt
∫
X
ρ(x,t )dx =
∫
X
Σ(A,ρc)dx. (11)
This expression shows that the total content mass is inﬂuenced only by recruitment, while diﬀu-
sion and alignment redistribute content within the space. Positivity of ρ is preserved provided
Σ is bounded.
Consider a spatially uniform steady state ρ(x,t ) =ρ∗. Then ∇ρ∗ = 0 and (10) reduces to
0 = Σ(A,ρ∗ c), (12)
indicating that uniform content distribution exists only when recruitment balances exits. The
spatial proﬁle of ρ∗ is determined entirely by the mean-ﬁeld dynamics of A and ρc.
To assess the stability of the uniform state, we introduce a small perturbation
ρ(x,t ) =ρ∗ +εeλt cos(kx), 0<ε ≪ 1. (13)
Linearizing (10) gives the dispersion relation
λ =−Dk2 +χ(ρ∗ c)k2 + Σρ, (14)
where χ(ρ∗ c) captures alignment strength toward global trends and Σ ρ is the derivative of the
recruitment term with respect to ρ. The ﬁrst term represents stabilizing diﬀusion, while the
second and third terms promote aggregation around dominant trends.
The uniform content distribution is stable if
Dk2>χ (ρ∗ c)k2 + Σρ, (15)
so that perturbations decay over time, preserving diversity. Conversely, the system exhibits
trend condensation or monoculture formation when
χ(ρ∗ c)k2 + Σρ>Dk 2, (16)
indicating that strong alignment of infected creators and recruitment near popular trends over-
comes exploration, producing hyper-convergence toward a few dominant content positions. This
behavior corresponds to the pathological collapse regime observed in the mean-ﬁeld and eco-
nomic analysis.
Since the alignment strengthχ(ρ∗ c) grows with the fraction of infected agents andρc increases
when the basic reproduction numberR0> 1, the PDE demonstrates that exceeding the epidemic
threshold accelerates content homogenization. In other words, higher infection prevalence re-
duces the diﬀusion necessary to maintain content diversity, providing a mechanistic explanation
for the monoculture collapse predicted by the model.
351

ADVANCED MATHEMATICAL MODELS & APPLICATIONS, V.11, N.2, 2026
2.2 Economic analysis: The diminishing returns of marketing
The framework developed above provides a profound, albeit cynical, mathematical lens through
which to evaluate the economic utility of social media marketing. By framing SMM through
Swarm Inﬂuence Dynamics, we can assess its ”worth” as a function of the platform’s epidemio-
logical state, which dictates a precarious balance between reach and systemic collapse. To answer
”Is it worth it?” we must analyze the three distinct value regimes predicted by the model.
To begin, in the healthy swarm regime where Ψ < Ψcrit and infection levels are low (¯c≈ 0),
SMM demonstrates high economic utility. The diversity metricD is maximal, allowing brands to
establish distinct niches without being drowned out by homogenized content. The engagement
ﬁtness format F (x,t ) rewards authentic creativity, and the creative cost term λ∇C(xi(t)) in
Equation 2 maintains brand identity. In this phase, the expected return on investment for a
marketing campaign positioned at xB can be approximated as
ROIhealthy =
∫ t0+T
t0
[
φ(xB)−α
∫
X
K(‖xB− y‖)ρ(y,t )dy
]
ρ(xB,t )dt−CB, (17)
where the intrinsic appealφ(xB) dominates and saturation eﬀects are minimal due to low content
density around xB. The marketing cost CB is typically justiﬁed by sustainable engagement and
brand diﬀerentiation.
Second, as marketing eﬀorts scale, the system enters the pathological momentum regime.
Brands must increase their content momentum κ and production velocity ‖vi‖ to maintain
visibility, inadvertently increasing their infection levelci(t). Equation 1 shows that both positive
and negative engagement ﬂuctuations reinforce this compulsion. The economic utility becomes
marginal, as captured by the modiﬁed ROI:
ROImarginal =
∫ t0+T
t0
[F∗(xB,t )−νcB(t)‖vB(t)‖]ρ(xB,t )dt−CB−Cfatigue(cB), (18)
where the ﬁtness F∗ now depends on compulsive momentum terms (Equation 6), and an addi-
tional fatigue cost Cfatigue emerges from the attention depletion in Equation 4. Marketing gains
visibility at the expense of creative identity, as λ∗ =λ(1−ξλcB) decreases. The brand becomes
trapped in a ”Red Queen’s race” Voelpel et al. (2005), spending increasing resources to maintain
relevance.
Third, when the platform crosses the epidemic threshold R0 > 1, it enters the monoculture
collapse regime. The system experiences hyper-convergence where all agents chase the same
global trend g(t). The trend intensity I(t) from Equation 8 exhibits violent boom-bust cycles
due to quadratic saturation. The economic utility turns negative:
ROIcollapse =
∫ t0+T
t0
[
β′ cA(t)ρc(xB,t )−αI(t)2] ρ(xB,t )dt−CB−Cburnout(γb,γa). (19)
The saturation term αI(t)2 dominates, causing diminishing returns per marketing dollar. The
burnout and abandonment costsCburnout become signiﬁcant as creators exit the platform (γb,γa).
Marketing in this phase accelerates creative exhaustion and platform degradation.
The model therefore yields a clear, phase-dependent verdict on the worth of social media
marketing. For an individual marketer, SMM is economically rational only if they can operate
in the healthy regime (Ψ < Ψcrit) or exit trends before saturation collapse. For the platform
ecosystem, the reward structure that increases ηp and βc inevitably pushes the system toward
pathological monoculture, destroying the diversity that creates long-term value. This suggests
that sustainable digital marketing requires either platform designs that maintain Ψ < Ψcrit
through algorithmic moderation (reducing β′ c and ηp) or marketing strategies that explicitly
optimize for diversity preservation over virality. The framework thus provides not only a di-
agnostic tool for current platform health but also design principles for more sustainable digital
economies.
352

T. CHIKORE: EPIDEMIOLOGICAL MODEL FOR SOCIAL MEDIA MARKETING...
3 Analytical validation of the model: Thresholds and stability
The purpose of this section is to validate the theoretical framework introduced in Section 2.
Speciﬁcally, we derive the equilibria, critical thresholds, and stability properties of the system
to demonstrate that the mechanisms hypothesized in the methodology (including contentitis,
attention-mediated ampliﬁcation, and compulsive feedback) produce mathematically consistent
dynamics. These results conﬁrm that the model’s predictions, including the phase-dependent
economic outcomes, are internally coherent and analytically robust. An important aspect of
this validation is the demonstration that our complex agent-based swarm model (Eqs. 1–7)
reduces, under mean-ﬁeld assumptions, to a system that falls within the well-studied class of
compartmental epidemiological models. This reduction is not trivial, it requires that the mi-
croscopic rules governing inﬂuencer behavior (content positioning, velocity updates, compulsive
reinforcement, attention depletion) are suﬃciently coherent to aggregate into macroscopic dy-
namics that mirror established theory. The fact that such a reduction is possible constitutes
the primary validation of our framework: it shows that the agent-level assumptions produce
collective behavior consistent with a century of epidemiological modeling.
It is important to note that the present work focuses on analytical characterization of the re-
duced SIR-type mean-ﬁeld system rather than on numerical exploration of particular parameter
scenarios hence, accordingly, no numerical simulations are included in this work. First, the ana-
lytical derivations of critical thresholds (βc,crit and Ψcrit), Jacobian eigenvalues, and bifurcation
conditions establish structural consistency and dynamical admissibility of the model indepen-
dent of empirical calibration. These quantities are fully determined by the system parameters
and are suﬃcient to demonstrate the existence of transcritical bifurcation, regime transitions,
hysteresis conditions, and boom–bust dynamics within the SIR dynamical class at a theoret-
ical level. Second, the absence of empirically validated parameter estimates for the processes
governing contentitis, attention depletion, and panic reinforcement precludes meaningful quan-
titative calibration. Because the parameter space is high-dimensional and strongly nonlinear,
simulations based on arbitrary or synthetic parameter choices would primarily illustrate assumed
scenarios rather than provide independent validation of the underlying dynamical structure. For
this reason, the contribution of the present study lies in the analytical reduction and bifurcation
analysis, while empirical calibration and scenario-based simulation are deferred to future work.
3.1 Model deﬁnitions and mean-ﬁeld dynamics
Deﬁnition 1 (State variables). Let
S(t), I(t), A(t)∈ [0, 1]
denote the susceptible fraction, infected fraction, and normalized audience attention pool, respec-
tively, with the constraint S(t) +I(t)≤ 1.
Deﬁnition 2 (Reduced mean-ﬁeld system) . The macroscopic dynamics of attention-mediated
pathogen propagation are governed by the system
dS
dt = Λ−βcSIA−µS +γrI, (20)
dI
dt =βcSIA +ηpξcI(1−I)− (γr +γb +γa +µ)I, (21)
dA
dt =α(1−A)−δIA−ϵA2. (22)
Remark 1. System (20)–(22) preserves the essential nonlinear feedback between infection preva-
lence and attention depletion while remaining analytically tractable.
353

ADVANCED MATHEMATICAL MODELS & APPLICATIONS, V.11, N.2, 2026
Remark 2 (Relation to classical SIR epidemiology) . System (20)–(22) belongs to the well-
established class of compartmental epidemiological models. To see this explicitly, consider the
special case where attention is constant ( A(t)≡ 1) and panic reinforcement is absent ( ηp = 0).
Under these conditions, the system reduces to:
dS
dt = Λ−βcSI−µS +γrI, (23)
dI
dt =βcSI− (γr +γb +γa +µ)I. (24)
This is a standard SIR-type model with susceptible recruitment Λ, disease transmission βcSI ,
recovery γr, and disease-induced mortality γb +γa. The basic reproduction number for this
reduced system is the classical expression:
R0 = βc γr +γb +γa +µ. (25)
The threshold R0 = 1 governs the transition between disease extinction and endemic persis-
tence, a result ﬁrst established by Kermack and McKendrick Brauer (2005), and since conﬁrmed
across countless epidemiological contexts Hethcote (2000); Brauer et al. (2008). When attention
dynamics are restored (A(t) variable) and panic reinforcement is present (ηp> 0), the system be-
comes a member of the broader class of SIR models with behavioral feedback (see also Funk et al.
(2010)), where the eﬀective transmission rate becomes time-dependent such thatβeﬀ(t) =βcA(t).
The panic reinforcement term ηpξcI(1−I) introduces a nonlinear incidence component, but the
fundamental threshold structure is preserved, as demonstrated by our derivation of βc,crit in
Equation (27).
3.2 Equilibria and ampliﬁcation threshold
Deﬁnition 3 (Compulsion-Free Equilibrium). The Compulsion-Free Equilibrium (CFE) of sys-
tem (20)–(22) is given by
E0 := (S∗,I∗,A∗) = (1, 0,A∗),
whereA∗ satisﬁes
α(1−A∗)−ϵ(A∗)2 = 0.
Deﬁnition 4 (Pathological ampliﬁcation index). The pathological ampliﬁcation index associated
with the CFE is deﬁned as
P := βcA∗
(γr +γb +γa +µ)−ηpξc
. (26)
Remark 3. The denominator in (26) is reduced by panic reinforcementηpξc, reﬂecting endoge-
nous ampliﬁcation of compulsive persistence. Note that when A∗ = 1 and ηp = 0,P reduces to
the classical reproduction number R0 =βc/(γr +γb +γa +µ).
3.3 Existence of a critical threshold
Proposition 1 (Critical transmission rate) . The Compulsion-Free Equilibrium loses stability
when the transmission rate βc exceeds
βc,crit = (γr +γb +γa +µ)−ηpξc A∗ . (27)
Proof. Linearizing (21) around the Compulsion-Free Equilibrium E0 yields
dI
dt = [βcA∗− (γr +γb +γa +µ) +ηpξc]I +O(I 2).
The CFE loses stability when the linear coeﬃcient vanishes, yielding (27).
354

T. CHIKORE: EPIDEMIOLOGICAL MODEL FOR SOCIAL MEDIA MARKETING...
Corollary 1 (Connection to classical threshold). In the absence of panic reinforcement (ηp = 0)
and with constant attention ( A∗ = 1 ), the critical transmission rate reduces to the classical
threshold condition βc,crit =γr +γb +γa +µ, which is equivalent to R0 = 1.
3.4 Phase transition in the composite control parameter
Deﬁnition 5 (Composite acceleration parameter). The composite control parameter governing
swarm acceleration is
Ψ := c2(β +β′ cA) α(γr +γb +γa).
Theorem 1 (Critical threshold for pathological collapse) . The system undergoes a phase tran-
sition at
Ψcrit = c2(β +β′ cA∗) α(γr +γb +γa) ⏐⏐⏐⏐⏐ P=1 . (28)
Proof. At the transcritical bifurcation point P = 1, the critical transmission rate is given by
Proposition 1. Substituting βc =βc,crit into the deﬁnition of Ψ yields (28).
Corollary 2. Ψcrit is strictly increasing in the steady-state attention level A∗.
Proof. Diﬀerentiating (28) with respect to A∗ yields
dΨcrit
dA∗ = c2β′ c α(γr +γb +γa) > 0.
3.5 Local stability and bifurcation structure
Proposition 2 (Jacobian at the CFE) . The Jacobian matrix of system (20)–(22) evaluated at
the Compulsion-Free Equilibrium is
J(E0) =


−µ γ r−βcA∗ 0
0 βcA∗ +ηpξc− Γ 0
0 −δA∗ −(α + 2ϵA∗)

, (29)
where Γ =γr +γb +γa +µ.
Theorem 2 (Transcritical bifurcation). The Compulsion-Free Equilibrium undergoes a trans-
critical bifurcation atP = 1.
Proof. One eigenvalue of J(E0) is −µ < 0. Another is −(α + 2ϵA∗) < 0. The remaining
eigenvalue changes sign precisely when
βcA∗ +ηpξc− Γ = 0,
which is equivalent toP = 1. Standard bifurcation theory implies a transcritical bifurcation.
Remark 4. This transcritical bifurcation is the same qualitative behavior exhibited by classical
SIR models at the R0 = 1 threshold. The presence of attention dynamics A(t) and panic rein-
forcementηpξc shifts the critical value but does not alter the fundamental bifurcation structure
inherited from the SIR backbone.
355

ADVANCED MATHEMATICAL MODELS & APPLICATIONS, V.11, N.2, 2026
3.6 Hysteresis and oscillatory dynamics
Result 1 (Hysteresis via subcritical Hopf bifurcation). For suﬃciently large panic reinforcement
ηp, the endemic equilibrium undergoes a subcritical Hopf bifurcation, generating bistability and
hysteresis.
Remark 5. In this regime, reducing βc below βc,crit does not restore the DFE; the system
remains trapped in a pathological attractor. This phenomenon, while absent in the classical
SIR model, is known to arise in SIR extensions with nonlinear incidence or behavioral feedback
(Liu et al., 1987; Funk et al., 2010). Its presence in our reduced system indicates that the panic
reinforcement mechanism (derived from dopamine-driven engagement sensitivity) can produce
path dependence consistent with observed platform dynamics where recovery is diﬃcult once
compulsive behavior becomes endemic.
Result 2 (Boom–bust oscillations). Strong coupling between infection prevalence and attention
depletion (δ large) destabilizes the endemic equilibrium and produces stable limit cycles with
period
T∼ 2π Im(λ),
whereλ is the complex conjugate eigenvalue pair of the Jacobian.
Remark 6. Limit cycles in epidemiological models are associated with sustained oscillations
in disease prevalence. In our context, these correspond to the boom-bust cycles observed in
viral content dynamics: periods of intense trend-chasing and compulsive production followed by
collective burnout and attention recovery. The analytical condition for their existence ( δ large)
provides a testable prediction: platforms with strong attention depletion eﬀects should exhibit
cyclic behavior.
Remark 7. The analytical results establish that pathological digital homogenization is not driven
by instability in well-being variables alone, but by delayed behavioral feedback mediated through
attention depletion and panic reinforcement.
This analytical validation serves as a conceptual and mathematical demonstration of the
model’s behavior, establishing benchmarks and thresholds that can guide future empirical in-
vestigations once appropriate observational data become available. In this sense, the analysis
justiﬁes the model structure and predicted dynamics without reliance on synthetic simulations,
preserving the rigor and interpretability of the results. Essentially, the validation presented
here is not the claim that our SIR-type equations are novel, they are deliberately classical.
The innovation lies in deriving these equations from a complex agent-based swarm model of
inﬂuencer content dynamics (Eqs. 1–7). The fact that such a derivation is possible, that the
microscopic rules of content creation, trend-chasing, and compulsive reinforcement aggregate to
a macroscopic system that falls within the well-studied SIR class, is itself the validation. It
demonstrates that our agent-level assumptions produce collective behavior consistent with es-
tablished epidemiological theory. The analytical results in this section (thresholds, bifurcations,
stability conditions) are not presented as novel epidemiological discoveries; they are presented
as conﬁrmation that the reduced system inherits the qualitative properties of the SIR models
that have been rigorously analyzed in the literature for nearly a century.
4 Discussion
The necessity for this research arises from the critical analytical gap in traditional marketing
frameworks, which typically assess inﬂuencer-based social media marketing through isolated en-
gagement metrics such as reach and impressions, without accounting for the emergent, systemic
dynamics of collective behavior (Voelpel et al., 2005). In this section, we interpret the outcomes
356

T. CHIKORE: EPIDEMIOLOGICAL MODEL FOR SOCIAL MEDIA MARKETING...
of our theoretical model and demonstrate its predictive validity by connecting it to real-world
social media phenomena such as viral TikTok trends, Instagram Reels virality, and rapid meme
propagation.It is important to emphasize that we do not perform numerical simulations for bi-
furcations, limit cycles, or boom–bust content dynamics in the standard SIR-type dynamical
system. This choice is intentional and does not constitute a limitation, because the analytical
derivations of critical thresholds (βc,crit and Ψcrit), Jacobian eigenvalues, and bifurcation condi-
tions provide rigorous internal validation. Moreover, our ability to embed the SIA model as a
validation mechanism represents a key novelty of this work. These results are fully determined
by system parameters, enabling the prediction of phase transitions, hysteresis, and systemic
saturation without relying on speculative or hypothetical data. Consequently, the absence of
simulations does not compromise the model’s validity, and the analytical approach oﬀers clear,
interpretable insights that correspond directly to observed social media phenomena.
As marketing investments scale toward a projected $250 billion by 2027, the underlying
economics of attention extraction appear increasingly unsustainable due to the lack of a uniﬁed
dynamical model that can distinguish between healthy competitive marketing and pathological
degradation. Our model ﬁlls this gap by providing analytically derived thresholds and behavioral
predictions, which allow us to identify conditions under which marketing remains sustainable
versus when the system collapses. For example, brands running TikTok challenges may initially
see exponential engagement, but exceeding the derived critical threshold Ψ crit corresponds to
the point where follower attention saturates, trends collapse, and ROI diminishes, consistent
with the experience of overexposed campaigns like certain viral hashtag challenges (Connolly,
2025).
In this study, inﬂuencers are modeled as adaptive agents navigating a multidimensional
content space, driven by algorithmic rewards while susceptible to a behavioral pathogen termed
contentitis. Platforms act as feedback systems that reinforce compulsive production, while
viewers experience fatigue emerging from collective dynamics. The derivation of the critical
transmission rate βc,crit and the composite acceleration parameter Ψ crit in Section 3 provides
internal validation: these thresholds produce mathematically consistent phase transitions that
mirror observed phenomena such as burnout of daily vloggers or collapse of rapidly iterated
meme pages on Instagram Weng et al. (2013).
The analytical results reveal a critical phase transition governed by the composite control
parameter Ψ. Below the threshold Ψ crit, social media marketing operates in a sustainable,
high-diversity regime with high ROI. Once this threshold is crossed, the system enters a patho-
logical regime characterized by hyper-convergence on global trends, triggering violent saturation
cycles and negative economic utility. This conﬁrms that the theoretical framework is capable
of predicting emergent systemic behavior from agent-level dynamics, qualitatively reproducing
patterns seen in viral TikTok audio clips, Instagram memes, and YouTube vlogs (Vosoughi et
al., 2018).
For businesses, the model indicates that social media marketing is economically rational only
in the healthy regime. Continuing investment during hyper-convergent cycles forces brands into
a self-defeating race, spending increasing resources for marginal relevance. Inﬂuencers’ rapid
production velocity is directly linked to cognitive resource depletion, leading to burnout and
platform abandonment. Platform owners face systemic risks: reward structures that maximize
short-term engagement inadvertently push the ecosystem toward collapse. These implications
are direct consequences of mathematically derived thresholds and stability analysis, reﬂecting
real-world outcomes such as the collapse of overly aggressive viral campaigns or accounts over-
whelmed by algorithmic pressure to post continuously Sunil et al. (2022).
An important emergent property revealed by the analysis is hysteresis: when panic reinforce-
mentηp is suﬃciently high, reducing compulsive transmission does not restore the system to a
healthy state, as it remains trapped in a pathological attractor. This demonstrates the predictive
power of the model, showing bistability and path-dependence consistent with the derived sub-
357

ADVANCED MATHEMATICAL MODELS & APPLICATIONS, V.11, N.2, 2026
critical Hopf bifurcation results in Section 3. Real-world analogues include X (formerly Twitter)
accounts and Instagram pages where follower attention fails to recover even after creators scale
back posting (Qin et al., 2024).
Although this study focused on a reduced mean-ﬁeld system for analytical tractability, which
may oversimplify heterogeneous interactions in real-world networks, the rigorous derivation of
critical thresholds and phase transitions serves as a theoretical validation. By deriving these
results analytically, we provide a principled framework for understanding systemic behavior
without needing simulations, which could otherwise introduce arbitrary assumptions or specu-
lative inputs. Understanding Ψ crit can inform algorithmic design to avoid hyper-saturation and
guide brands in pacing content to maximize long-term engagement.
Table 1: Summary of analytical validation results and corresponding real-world phenomena
Analytical result Validation type Real-world analogue
βc,crit Critical transmission threshold Overexposed viral campaigns
Ψcrit Phase transition from sustainable to
pathological regime
Saturated TikTok/Instagram
trends
Subcritical Hopf bifurcation Hysteresis and bistability Attention fails to recover after over-
exposure
Limit cycle analysis Boom–bust content cycles Viral meme/audio cycles on social
media
Jacobian eigenvalue analysis Local stability of equilibria Platform-level content resilience
To summarize, the theoretical framework is validated by linking its analytical predictions to
practical outcomes: critical thresholds βc,crit and Ψ crit, hysteresis behavior, and ROI collapse
emerge directly from the model and align qualitatively with observed social media patterns.
Table 1 provides a concise mapping between analytical results, validation type, and real-world
analogue.
Despite the analytical rigor of the model, several limitations must be acknowledged. First,
the reduced mean-ﬁeld framework abstracts away heterogeneous interactions among individual
inﬂuencers, audiences, and platform algorithms, which may produce additional nonlinearities
in real networks. Second, the model parameters governing contentitis, attention depletion, and
panic reinforcement are currently theoretical, and no empirical calibration was possible due to
the lack of publicly available data; consequently, the quantitative predictions of critical thresh-
olds and phase transitions should be interpreted qualitatively rather than as precise forecasts.
Third, the analytical focus precludes exploration of stochastic variability and emergent phe-
nomena arising from network structure, temporal bursts, or platform-speciﬁc recommendation
systems. Future work should aim to incorporate multi-platform dynamics, empirically estimated
parameters, and stochastic simulations to explore how heterogeneous agent behavior, algorith-
mic curation, and generative AI interventions modulate the critical thresholds identiﬁed here.
Additionally, coupling the current framework with longitudinal social media data would allow
validation of predicted phase transitions, hysteresis eﬀects, and boom–bust cycles, providing
actionable guidance for sustainable marketing strategies and platform design.
In conclusion, the model demonstrates that emergent systemic behavior, such as hyper-
convergence, boom–bust cycles, and attention collapse, can be predicted from ﬁrst principles of
agent-level dynamics. These results justify the approach of not performing numerical simula-
tions for bifurcations and limit cycles: the analytical derivations themselves serve as validation,
oﬀering clear, interpretable thresholds and dynamics that are consistent with observed social
media phenomena, while avoiding speculative assumptions inherent in synthetic simulations.
Ethics approval and consent to participate
Not applicable for this study.
358

T. CHIKORE: EPIDEMIOLOGICAL MODEL FOR SOCIAL MEDIA MARKETING...
Conﬂict of interest
The author declares that there is no conﬂict of interest regarding the publication of this paper.
Consent for publication
Acknowledgements
The author acknowledges the resource support from the University of Johannesburg in the
production of the manuscript.
Availability of data and materials
No datasets were generated and analyzed during the current study.
References
Adams, P. (2025). Global ad spend to rise faster than expected amid digi-
tal boom: WARC. Marketing Dive . https://www.marketingdive.com/news/
global-ad-spend-rise-faster-than-expected-amid-digital-boom-warc/761119/
Agrawal, A.J. (2016). Why inﬂuencer marketing will explode in
2017. Forbes. https://www.forbes.com/sites/ajagrawal/2016/12/27/
why-influencer-marketing-will-explode-in-2017/
Brown, J. & Moln´ ar, M. (2025).Inﬂuencer marketing and mental health: Unpacking the mental
health struggles behind the glare of social media fame (Dissertation). J¨ onk¨ oping University.
https://urn.kb.se/resolve?urn=urn:nbn:se:hj:diva-68133
Bak-Coleman, J.B., Alfano, M., Barfuss, W., et al. (2021). Stewardship of global collective
behavior. Proceedings of the National Academy of Sciences , 118(27). https://www.pnas.
org/doi/10.1073/pnas.2025764118
Brauer, F. (2005). The Kermack–McKendrick epidemic model revisited. Mathematical Bio-
sciences, 198(2), 119–131. https://doi.org/10.1016/j.mbs.2005.07.006
Brauer, F., van den Driessche, P. & Wu, J. (Eds.). (2008). Mathematical epidemiology
(Lecture Notes in Mathematics). Springer Berlin, Heidelberg. https://doi.org/10.1007/
978-3-540-78911-6
Bucher, T. (2018). If. . . then: Algorithmic power and politics(Oxford Studies in Digital Politics).
Oxford University Press. https://doi.org/10.1093/oso/9780190493028.001.0001
Centola, D. (2018). How behavior spreads: The science of complex contagions . Princeton Uni-
versity Press. https://doi.org/10.23943/9781400890095
Strong, T. (2025). Review of Filterworld: How algorithms ﬂattened culture , by Kyle Chayka.
Journal of Constructivist Psychology, 38(2), 354–356. https://doi.org/10.1080/10720537.
2024.2352713
Connolly, E. (2025). How does social media content go viral across platforms? Modelling the
spread of Kamala is brat across X, TikTok, and Instagram.Journal of Information Technology
& Politics, 1–16. https://doi.org/10.1080/19331681.2025.2519052
359

ADVANCED MATHEMATICAL MODELS & APPLICATIONS, V.11, N.2, 2026
Dzreke, S., Dzreke, S. (2025). The inﬂuencer equity equation: Analyzing inﬂuencer marketing’s
eﬀect on brand equity via the perspectives of authenticity, credibility, and engagement. In-
ternational Journal for Multidisciplinary Research , 7(3), 1–23. https://doi.org/10.36948/
ijfmr.2025.v07i03.48683
Emereonye, V.C. (2025). Quantifying social media’s impact on business performance: A data-
driven approach to consumer engagement and ROI. World Journal of Advanced Research and
Reviews, 25(3), 1288–1306. https://doi.org/10.30574/wjarr.2025.25.3.0901
Fibre2Fashion. (2023). Shein shine story: Brand talk [Brand report]. https://fashiongear.
fibre2fashion.com/brand-story/shein-shine/brand-talk-shein.pdf
Frontiers in Communication. (2025). Algorithmic inﬂuence and media legitimacy: A system-
atic review. Frontiers in Communication , 10. https://www.frontiersin.org/journals/
communication/articles/10.3389/fcomm.2025.1667471/full
Funk, S., Salath´ e, M. & Jansen, V.A.A. (2010). Modelling the inﬂuence of human behaviour
on the spread of infectious diseases: A review. Journal of the Royal Society Interface , 7(50),
1247–1256. https://doi.org/10.1098/rsif.2010.0142
Future Startup. (2023). A brief history of SHEIN. https://futurestartup.com/2023/11/06/
a-brief-history-of-shein/
Goel, A., Masurkar, S. & Pathade, G.R. (2024). An overview of digital transformation and
environmental sustainability: Threats, opportunities, and solutions. Sustainability, 16, 11079.
https://doi.org/10.3390/su162411079
Han, B.-C. (2015). The burnout society . Stanford University Press.
Haouari, M., Mhiri, M. (2021). A particle swarm optimization approach for predicting the
number of COVID-19 deaths. Scientiﬁc Reports , 11, 16587. https://doi.org/10.1038/
s41598-021-96057-5
Hemalatha, P., Paul Kumar, K.S. (2025). Digital burnout and social media fatigue among Gen
Z: Psychological implications in a hyper-connected society. International Journal of Creative
Research Thoughts, 13(7), h689–h703. https://www.ijcrt.org/papers/IJCRT2507876.pdf
Hethcote, H.W. (2000). The mathematics of infectious diseases. SIAM Review, 42(4), 599-653.
https://doi.org/10.1137/S0036144500371907
Hudders, L., De Jans, S. & De Veirman, M. (2021). The commercialization of social media stars:
A literature review and conceptual framework on the strategic use of social media inﬂuencers.
International Journal of Advertising , 40(3), 327–375. https://doi.org/10.1080/02650487.
2020.1836925
Hughes, C., Swaminathan, V. & Brooks, G. (2019). Driving brand engagement through online
social inﬂuencers: An empirical investigation of sponsored blogging campaigns. Journal of
Marketing, 83(5), 78–96. https://doi.org/10.1177/0022242919854374
Javaid, M., Haleem, A., Singh, R.P. & Sinha, A.K. (2024). Digital economy to improve the cul-
ture of industry 4.0: A study on features, implementation and challenges. Green Technologies
and Sustainability, 2(2), 100083. https://doi.org/10.1016/j.grets.2024.100083
Kennedy, J., Eberhart, R. (1995). Particle swarm optimization. In Proceedings of ICNN’95 —
International Conference on Neural Networks (pp. 1942–1948). https://doi.org/10.1109/
ICNN.1995.488968
360

T. CHIKORE: EPIDEMIOLOGICAL MODEL FOR SOCIAL MEDIA MARKETING...
Konovalov, A.A., Bozhkova, E.D. (2022). The “digital pathogen” concept: Epidemiologi-
cal approach to problem of disorders associated with information technologies. Probl Sot-
sialnoi Gig Zdravookhranenniiai Istor Med , 30(4), 559–563. https://doi.org/10.32687/
0869-866X-2022-30-4-559-563
Kubler, K. (2023). Inﬂuencers and the attention economy: The meaning and management of
attention on Instagram. Journal of Marketing Management , 39(11–12), 965–981. https://
doi.org/10.1080/0267257X.2022.2157864
Kuss, D.J., Griﬃths, M.D. (2011). Online social networking and addiction—a review of the
psychological literature. International Journal of Environmental Research and Public Health ,
8(9), 3528–3552. https://doi.org/10.3390/ijerph8093528
Libai, B., Rosario, A.B., Beichert, M., et al. (2025). Inﬂuencer marketing unlocked: Under-
standing the value chains driving the creator economy. Journal of the Academy of Marketing
Science, 53, 4–28. https://doi.org/10.1007/s11747-024-01073-2
Lorenz-Spreen, P., Mønsted, B.M., H¨ ovel, P. & Lehmann, S. (2019). Accelerating dynam-
ics of collective attention. Nature Communications , 10, 1759. https://www.nature.com/
articles/s41467-019-09311-w
Mallipeddi, R., Kumar, S., Sriskandarajah, C. & Zhu, Y. (2020). A framework for analyzing
inﬂuencer marketing in social networks: Selection and scheduling of inﬂuencers. Management
Science. https://dx.doi.org/10.2139/ssrn.3255198
Migkos, S.P., Giannakopoulos, N.T. & Sakas, D.P. (2025). Impact of inﬂuencer marketing on
consumer behavior and online shopping preferences. Journal of Theoretical and Applied Elec-
tronic Commerce Research, 20(2), 111. https://doi.org/10.3390/jtaer20020111
Morris, S. (2025). 200+ social media marketing statistics every marketer should see (2025 data).
https://newmedia.com/blog/social-media-marketing-statistics
Nyabadza, F., Chikore, T. (2025). Towards the taxonomy of digital pathogens: An epidemio-
logical framework for modelling behavioural contagion and algorithmic compulsion [Preprint,
ResearchGate]. https://doi.org/10.13140/RG.2.2.15184.16640
Postdigitalist. (2025). Shein: Factory fashion and its consequences. https://www.
postdigitalist.xyz/blog/shein-factory
Putri, S.D.G., Purnomo, E.P. & Khairunissa, T. (2024). Echo chambers and algorithmic bias:
The homogenization of online culture in a smart society.SHS Web of Conferences, 202, 05001.
https://doi.org/10.1051/shsconf/202420205001
Qin, C., Li, Y., Wang, T., Zhao, J., Tong, L., Yang, J. & Liu, Y. (2024). Too much social
media? Unveiling the eﬀects of determinants in social media fatigue. Frontiers in Psychology,
15, 1277846. https://doi.org/10.3389/fpsyg.2024.1277846
Ren, X., Li, J. & Shi, Y. (2022). Can digital economic attention spillover to ﬁnancial markets?
Evidence from the time-varying Granger test. Journal of Digital Economy , 1(2), 102–116.
https://doi.org/10.1016/j.jdec.2022.11.002
ResearchAndMarkets.com. (2025). Social media advertising market report . https://www.
researchandmarkets.com/report/social-media-advertising
Stewart, A.J., Mosleh, M., Noble, D. & Rand, D.G. (2019). Information gerrymandering
and undemocratic decisions. Nature, 573, 117–121. https://www.nature.com/articles/
s41586-019-1507-6
361

ADVANCED MATHEMATICAL MODELS & APPLICATIONS, V.11, N.2, 2026
Sun, N., Rau, P.P.-L. & Ma, L. (2014). Understanding lurkers in online communities: A lit-
erature review. Computers in Human Behavior , 38, 110–117. https://doi.org/10.1016/j.
chb.2014.05.022
Sunil, S., Sharma, M.K., Amudhan, S., Anand, N. & John, N. (2022). Social media fatigue:
Causes and concerns. International Journal of Social Psychiatry , 68(3), 686–692. https://
doi.org/10.1177/00207640221074800
Voelpel, S., Leibold, M., Tekie, E. & von Krogh, G. (2005). Escaping the Red Queen eﬀect in
competitive strategy: Sense-testing business models. European Management Journal , 23(1),
37–49. https://doi.org/10.1016/j.emj.2004.12.008
Vosoughi, S., Roy, D. & Aral, S. (2018). The spread of true and false news online. Science, 359,
1146–1151. https://www.science.org/doi/10.1126/science.aap9559
Vyatkina, O.L. (2020). The impact of inﬂuencer marketing on the global economy. In S.I. Ash-
marina & V.V. Mantulenko (Eds.), Global challenges and prospects of the modern economic
development (European Proceedings of Social and Behavioural Sciences, Vol. 79, pp. 1307–
1311). European Publisher. https://doi.org/10.15405/epsbs.2020.03.187
Weng, L., Menczer, F. & Ahn, Y.Y. (2013). Virality prediction and community structure in
social networks. Scientiﬁc Reports, 3, 2522. https://doi.org/10.1038/srep02522
Williams, J. (2018). Stand out of our light: Freedom and resistance in the attention economy .
Cambridge University Press. https://doi.org/10.1017/9781108453004
362
