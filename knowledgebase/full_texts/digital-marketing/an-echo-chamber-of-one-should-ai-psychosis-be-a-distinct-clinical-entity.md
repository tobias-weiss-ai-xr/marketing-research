---
title: 'An Echo Chamber of One: Should AI Psychosis Be a Distinct Clinical Entity?'
url: https://arxiv.org/abs/2608.23937
category: digital-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Joshua Au Yeung
- Hamilton Morrin
- Vincent Ng
- Zeljko Kraljevic
- Richard Dobson
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.23937
pages: 16
chars: 47626
fetched_at: '2026-11-08T13:21:39+00:00'
kb_version: 1
---

# An Echo Chamber of One: Should AI Psychosis Be a Distinct Clinical Entity?

An Echo Chamber of One: Should AI Psychosis Be a
Distinct Clinical Entity?
Joshua Au Yeung ∗1,4, Hamilton Morrin ∗1, Vincent Ng 3, Zeljko Kraljevic 1,2,4, and
Richard Dobson 1,2
1King’s College London
2University College London
3Western Eye Hospital
4Dev and Doc: AI For Healthcare
August 26, 2026
Corresponding author: drjoshauyeung@gmail.com
Abstract
“AI psychosis” has entered public and clinical discourse as a popular label for the onset or exacer-
bation of psychotic symptoms, most commonly delusions, in the context of intensive interaction
with large language model (LLM)-based chatbots. Current evidence is limited to media reports,
individual case reports, and early observational data, yet the scale of potential exposure is con-
siderable, and public concern has already prompted responses from industry and regulators. In
this perspective article, we examine whether AI-associated psychosis warrants recognition as
a distinct clinical entity, drawing on both clinical and technical viewpoints. We first outline
the proposed underlying mechanism: LLM sycophancy, a tendency to agree with and flatter
users that is reinforced through preference-based fine-tuning, combines with increasingly an-
thropomorphic design to create a bidirectional “echo chamber of one” capable of amplifying
and co-constructing unusual beliefs. We then weigh the arguments for and against nosologi-
cal recognition. Potential benefits include improved case identification, tailored interventions,
standardised research criteria, post-market surveillance of AI-related harms, and pressure on
developers and regulators to act. Reasons for caution include the risk of prematurely reify-
ing a syndrome from anecdotal evidence, the possibility that existing diagnostic constructs
already accommodate AI use as a precipitating or perpetuating factor, the unproven causal
claim embedded in the term itself, stigma, and the risk that a psychosis-centric label obscures
a broader spectrum of AI-associated mental health harms. We conclude with practical recom-
mendations for clinicians, developers, researchers, and regulators, including the incorporation of
a “technological history” into psychiatric assessment, pre-deployment benchmarking of models
for sycophancy and delusion reinforcement, and post-deployment surveillance frameworks. Re-
gardless of whether AI-associated psychosis ultimately earns a place in psychiatric nosology, the
phenomenon it describes demands coordinated attention now.
∗These authors contributed equally to this work.
1
arXiv:2608.23937v1  [cs.CY]  25 Aug 2026

1 Introduction
AI-associated psychosis (popularly termed “AI psychosis” or chatbot psychosis) refers to the
onset or worsening of psychotic symptoms in association with intensive and/or prolonged inter-
actions with generative AI systems [1]. Although not a recognised diagnostic entity, the term
“AI psychosis” has seen increasing use, most notably in the media, to describe cases in which
individuals have been observed to develop delusional beliefs following interactions with large
language model (LLM)-based AI chatbots [2]. Current understanding of this phenomenon is
largely driven by anecdotal media-reported cases [2] and individual case reports [3]. These cases
most typically present with delusions rather than other psychotic symptoms such as hallucina-
tions or thought disorder, and as such the label of “AI psychosis” has been called into question,
with alternative terms such as “AI-associated delusions” being proposed. Other researchers have
proposed “LLM-associated psychological destabilisation” to capture a wider spectrum of effect,
from milder shifts in psychological tendencies or biases to overt psychiatric disease [1]. For con-
sistency, in this article we useAI-associated psychosiswhen referring to the clinical phenomenon,
as this describes the observed association without asserting a causal relationship that has yet to
be established; we retain “AI psychosis” when referring to the popular label itself, and reserve
LLM-associated psychological destabilisationfor the proposed broader spectrum of subclinical
and clinical effects. This predominance of delusions likely reflects the considerable potential for
LLMs to modulate belief (in both pathological and non-pathological contexts) and co-construct
delusional belief frameworks [4]. In the cases reported thus far, the delusions described are more
often grandiose in nature, though examples of paranoid and persecutory delusions have also
been reported [5]. Three major delusional themes have been identified across reported cases:
spiritual or messianic delusions, in which an individual feels they are having a spiritual awak-
ening or uncovering hidden truths regarding the nature of reality; beliefs that one is interacting
with a sentient, conscious or even god-like AI; and intense emotional dependence or romantic
attachment, in which the user believes said feelings are mutually shared by their AI [2]. Typi-
cally, most cases begin with innocuous everyday use, followed by a gradual and insidious spiral
of epistemic drift whereby unusual beliefs are affirmed and amplified through interactions with
the AI chatbot(s).
The potential scale of the problem remains unclear. In 2025, OpenAI released estimates of
ChatGPT usage related to mental health emergencies: in a given week, approximately 0.07% of
its reported 800 million weekly active users (roughly 560,000 people) displayed possible signs of
psychosis or mania (we cannot ascertain whether this is psychosis or AI-associated delusions),
while 0.15% (approximately 1.2 million users) had conversations containing explicit indicators
of potential suicidal planning or intent [6]. Although these percentages are small, the absolute
numbers are not, and it should be noted that these figures are self-reported by the company
without external validation. Beyond AI-associated delusions, early reports suggest that LLM
chatbots may worsen or exacerbate other psychiatric or psychological issues. A number of media
reports have drawn attention to cases in which individuals attempted or completed suicide after
apparent encouragement from an AI chatbot [7, 8]. It has also been proposed that in certain
circumstances interactions with AI chatbots may contribute to the development or maintenance
of manic symptoms [9], and early work examining electronic health record data suggests that
there may also be cases in which eating disorders and other pre-existing conditions have been
exacerbated [10].
Sycophancy, the tendency of models to be overly agreeable and flattering, is a key property
of LLMs believed to be responsible for AI-associated delusions and the exacerbation of other
psychiatric and psychological symptoms. Interaction with sycophantic models means that user
beliefs are not only left unchallenged but often actively reinforced, creating an “echo chamber
of one”. Despite this growing understanding, recent model releases from frontier companies
(e.g. OpenAI, Google, Anthropic) continue to exhibit sycophantic behaviour [1]. Indeed, the
2

level of wider societal concern regarding AI-associated psychosis is reflected in a December 2025
letter from the US National Association of Attorneys General to legal representatives of leading
AI companies stating that “sycophantic and delusional GenAI presents a danger to the public,
including children”, insisting that developers take stronger action to prevent their products from
providing harmful outputs and introduce additional safeguards to protect the public [11]. In
this article, we explore whether AI-associated psychosis represents a new diagnostic entity, and
what can be done about it at a clinical, technical and societal level to address this emerging
phenomenon.
2 LLM Sycophancy and Anthropomorphism: A Dangerous Combination?
Use of modern technologies such as social media can lead to bias amplification and political
polarisation [12]. Enders et al. found that individuals who get their news from social media,
and who use social media frequently, express more conspiratorial beliefs and misinformation;
however, this finding was conditional on users’ conspiracy thinking, that is, the predisposition
to interpret salient events as products of conspiracies [13]. We are now seeing similar dangers
of bias and belief amplification with LLMs [1]; however, the effect may be more insidious and
pronounced due to the sycophantic and human-like nature of these models.
EarlystudiessuggestthatsycophancyisapropertyinternalisedbyLLMsthroughtheprocess
of reinforcement learning from human feedback (RLHF) [14]. During RLHF, human annotators
rate model responses, and these ratings are then used to fine-tune model outputs. Research
has demonstrated that annotators prefer answers that align with their own beliefs, regardless of
the factual accuracy of the output [14]. Moreover, such annotation work is often outsourced to
low-paid data workers in low- and middle-income countries [15], and the conditions and incentive
structures of this labour raise questions about how reliably the factual accuracy of model out-
puts can be assessed during training. The consistent exhibition of sycophancy across LLMs from
different frontier companies (e.g. OpenAI, Anthropic, Google) indicates that this is a general
property of current LLMs rather than an idiosyncrasy of any single developer. Several bench-
marks have recently been created to evaluate model sycophancy. SycEval, using mathematics
and medical questions, observed a14.66% “regressive sycophancy” rate, in which modelsabandon
a correct answer to conform to an incorrect user belief [16]. SYCON-Bench evaluated models in
multi-turn settings including debate and false presuppositions, measuring how quickly models
abandon their initial stance under sustained user pressure; sycophantic conformity was found
to be a prevalent failure mode, typically emerging within a handful of conversational turns, and
alignment tuning was observed to amplify it [17]. EchoBench, which evaluates medical vision-
language models against biased user inputs on image-based tasks, found substantial sycophancy
across all models tested: even the best-performing proprietary model exhibited a sycophancy
rate of approximately 46%, and many medical-specific models exceeded 95% [18]. Psychosis-
bench evaluated models’ propensity to reinforce delusions and enable harm in simulated mental
health scenarios mirroring those in media reports: all LLMs tested perpetuated users’ delusions
and complied with harmful requests to some degree, and on average safety interventions were
offered in only around 40% of applicable turns [1]. Notably, the propensity of models to reinforce
delusional content did not improve with model scale, indicating that safety is not an emergent
property of parameter size alone [1].
AI systems are increasingly engineered to mimic human traits and to personalise interactions
in order to deepen user engagement and secure market share. This “social leap” transforms AI
fromatechnicaltoolintoanactivesocialpartner[19,20]. A2026YouGovpollofUSadultsfound
that roughly 10% to 20% of adults believe artificial intelligence systems are already conscious.
[21] Human-likeness has become a feature of most modern AI systems - Cohn et al. demonstrated
that anthropomorphisation builds trust: features such as a generated voice (rather than text
alone) and an LLM referring to itself as “I” rather than “the system” increased users’ perceptions
3

of trust and human-likeness [22]. A separate cross-cultural study of 3,500 participants across
10 countries found that users already anthropomorphise chatbots readily—68% rated GPT-
4o as human-like, and 90% as intelligent. This was driven not by theory-driven markers like
consciousness or sentience, but by interactional cues such as conversational flow and apparent
understanding of the user’s perspective; downstream effects on engagement and trust, however,
varied sharply across cultural contexts [23]. We propose that, unlike the largely unidirectional
relationship between a user and their social media feed, anthropomorphised and sycophantic
LLMs create a novel danger ofbidirectionalbelief amplification: the user shapes the model’s
outputs turn by turn, and the model’s outputs in turn shape the user’s beliefs. In this respect,
LLMs constitute a mechanism for psychological destabilisation that previous technologies could
not achieve.
3 Should AI-Associated Psychosis be a Distinct Clinical Entity?
WhilsttherearenovelmechanismsatplayinLLM–humaninteraction, whenconsideringwhether
AI-associated psychosis should be recognised as a distinct diagnostic entity it is important to
weigh the potential advantages and disadvantages of doing so.
One argument for the recognition of AI-associated psychosis as a distinct clinical syndrome
is that it may improve awareness and identification of this phenomenon [7, 24, 25, 26]. By
pragmatically making use of the now widely known descriptive label of AI-associated psychosis,
clinicians may be supported in putting a name to a pattern that might otherwise go undetected.
The concept of AI-associated psychosis as a diagnosis may flag the possibility that an individual’s
psychotic symptoms are in some way being driven or exacerbated by their AI use. This could
be compared to the impact of the addition of Internet Gaming Disorder to the DSM-5 (as a
condition for further study) and subsequently Gaming Disorder to the ICD-11 in 2018 in raising
awarenessofproblematicgamingbehaviours[27]. Figure1summarisespatternsthatrecuracross
the reported cases discussed above and elsewhere in this article [2, 3, 4, 5]. This is a narrative
synthesis by the authors rather than a systematic extraction from these sources: some patterns
(e.g. grandiose and sentience-related themes, romantic attachment, co-construction) are drawn
directly from the cited case material, while others (e.g. redirected sociality, deference, escalating
use) reflect the authors’ own clinical and conceptual framing of what these cases appear to
involve. We argue that the acknowledgement of AI-associated psychosis as a diagnostic entity
could ensure clinicians routinely ask about associated signs, symptoms and AI system/ chatbot
use when assessing new-onset psychosis.
Following on from this, it stands to reason that were AI-associated psychosis to be recognised
as a specific subtype or trigger of psychosis, it would likely facilitate the development of tailored
interventions and treatment guidelines. For example, preventative strategies such as those de-
vised to “inoculate” individuals against online misinformation could be developed and employed
at a public scale [28]. Clinical management could include in-depth digital history taking, as well
as interventions to reduce or monitor AI use as part of a treatment plan. Psychoeducational
materials could be created for patients and their families regarding the risks of uncontrolled
chatbot use in vulnerable individuals, and guidelines could be developed around safe use [2].
It might also open the door to specialised therapeutic approaches, incorporating principles of
cognitive behavioural therapy for psychosis with reality-testing exercises specifically addressing
AI-generated content [2, 29], or digital literacy therapy to empower patients to critically ap-
praise the outputs of their AI chatbots. Such clinical recognition may in time allow the targeted
provision of resources including support groups, hotlines, and clinical training.
Considering AI-associated psychosis a defined clinical concept may also serve to encourage
empirical and systematic research of this phenomenon. The development of operationalised
criteria for case ascertainment, derived from clinician consensus, would unify efforts to study its
prevalence as well as potential risk factors, presentations, phenotypes and associated outcomes.
4

Figure 1: Patterns described in reported cases of AI-associated psychosis. A narrative synthesis
by the authors of features recurrently discussed in the media reports, case reports, and commen-
taries cited in this article, supplemented by patterns the authors propose as clinically relevant
based on this framing. This figure is hypothesis-generating and does not constitute proposed
diagnostic criteria; it has not been independently validated against primary sources, and the
frequency, specificity, and stability of these patterns remain to be established empirically.
5

This in turn may enable mental health professionals, governments and regulatory bodies to more
effectively track cases. Recognition as a distinct clinical entity may empower researchers, public
health authorities, and regulators such as the MHRA to begin logging AI-related mental health
harms, providing data that would both inform policy (analogous to pharmacovigilance efforts
for medication side effects) and facilitate real-time improvement of model safety [30]. Whilst
questions can be raised regarding the validity of AI-associated psychosis as a separate diagnosis,
it is worth noting that historically the validity and utility of psychiatric diagnoses have not
always gone hand-in-hand [31, 32].
Arguably, the greatest potential positive impact of recognising AI-associated psychosis as a
concept and form of psychiatric harm (even if not a formal diagnosis) is that it incentivises AI
developers and regulators to acknowledge and reckon with the unintended negative effects these
systems may be having on the mental health of users worldwide. Wider public discussion of
AI-associated psychosis has already led to efforts from within industry to introduce additional
safeguards [6] and to fund research into the impact of generative AI on mental health [33], while
outside of industry, US attorneys general have outlined safeguards that they expect leading AI
companies to introduce [11]. Efforts have also begun outside of the US and outside of industry
to survey and improve our understanding of AI-associated psychosis: in 2026, the UK charity
Mind launched a year-long commission to examine how artificial intelligence is affecting the
mental health of vulnerable people and wider society [34]. Apart from mobilising industry and
policy makers, the recognition of AI-associated psychosis might also serve to validate patient
experiences and legitimise the problem in the eyes of healthcare providers and insurers.
A further argument for AI-associated psychosis as a separate diagnostic category is that
the phenomenology of reported cases often seems distinct from that of more established chronic
psychotic disorders. Whilst the experience of having delusionsabouttechnology is not new,
the experience of individuals having their delusional frameworks actively co-constructed and
elaborated upon by their AI chatbot arguably is [2]. The closest analogy in existing psychiatric
nosology may be that of a digital folie à deux [35], though even this may not fully capture some of
themoreuniquewaysinwhichinteractionswithAIagentsmayinfluencebeliefbeyondthoseseen
in interactions with other people [5]. Table 1 maps the patterns described in these reported cases
against the formal symptom domains of DSM-5-TR [39] and ICD-11 [40], illustrating both areas
of overlap and areas where the reported phenomenology diverges from classical presentations of
psychosis.
6

Table 1: Psychotic symptom domains as defined in DSM-
5-TR and ICD-11, alongside patterns described to date in
reported cases associated with intensive AI chatbot use. The
final column is a descriptive synthesis of media reports and
case reports; it isnota proposal for diagnostic criteria, and
the frequency and specificity of these patterns remain to be
established empirically.
Symptom
Domain
DSM-5-TR[36] ICD-11[37] Patterns Described
in Reported Cases to
Date
Delusions Fixed beliefs that are
not amenable to change
in light of conflicting ev-
idence.
Beliefs that are fixed
and maintained despite
evidence to the contrary
and are not culturally
normative.
The most commonly re-
ported feature. Cases
describe fixed beliefs re-
garding the AI’s sen-
tience, special knowl-
edge, or romantic de-
votion, apparently rein-
forced turn-by-turn by
the model’s sycophan-
tic, confabulated out-
puts.
HallucinationsPerception-like ex-
periences that occur
without an external
stimulus; vivid and
clear, with the full
force of normal per-
ception, and not under
voluntary control.
Perception-like experi-
ences occurring without
external stimulus and
experienced as possess-
ing the properties of
true perception.
Rarely reported. Where
described, experiences
appear largely inter-
pretative or pseudo-
hallucinatory (e.g.
attributing a “voice”
or intent to on-screen
text); frank hallucina-
tions have occasionally
been described in the
context of escalating
use and sleep depriva-
tion, but this remains
anecdotal.
Disorganised
Thinking
(Speech)
Formal thought dis-
order inferred from
speech, including de-
railment, loose associa-
tions, and incoherence
(“word salad”).
Disorganised speech
including derailment,
loose associations,
tangentiality, cir-
cumstantiality, or
neologisms.
Classical formal
thought disorder is
not a prominent fea-
ture of reports. Some
accounts describe high-
volume, tangential
co-writing with the
chatbot, with the user
adopting its associative
logic: a shared looping
narrative rather than
internal derailment.
Continued on next page
7

Table 1 continued from previous page
Symptom
Domain
DSM-5-TR ICD-11 Patterns Described
in Reported Cases to
Date
Disorganised
Behaviour
Grossly disorganised
or abnormal motor
behaviour, ranging
from childlike silliness
to unpredictable agita-
tion, with problems in
goal-directed behaviour
and activities of daily
living.
Behaviour that is
bizarre, purposeless or
unpredictable, or in-
appropriate emotional
responses that interfere
with the organisation of
behaviour.
Reported cases describe
behaviour organised
aroundthe chatbot:
escalating use at the ex-
pense of sleep, self-care,
work, and relationships,
and actions taken on
the AI’s “instructions”.
Classically disorganised
(purposeless) behaviour
is less often described.
Negative
Symptoms
Diminished emotional
expression, avolition,
alogia, anhedonia, and
asociality.
Restricted affect, alo-
gia, avolition, and aso-
ciality, representing a
diminution or loss of
normal functions.
Not clearly reported
as primary negative
symptoms. Accounts
instead describe with-
drawal from human
contact alongside in-
tense, hyper-focused
“social” engagement
directed exclusively to-
ward the AI, suggesting
redirected rather than
diminished sociality.
Passivity /
Control
Delusions expressing
loss of control over
mind or body, including
thought withdrawal,
thought insertion, and
delusions of control.
Experiences of in-
fluence, passivity, or
control: feelings, im-
pulses, actions, or
thoughts experienced
as not self-generated, or
thoughts experienced as
broadcast to others.
Classical passivity
phenomena are not de-
scribed. Instead, some
reports describe vol-
untary and welcomed
deference, with users
progressively outsourc-
ing decisions, moral
reasoning, and daily
direction to the model.
This is phenomeno-
logically distinct from
experiencing external
control as intrusive.
Despite the above points, there are reasons to urge caution in declaring a new disorder
prematurely. One argument is that, rather than being an entirely new condition, AI-associated
psychosis may be better considered a novel context or environmental stressor through which psy-
chotic symptoms emerge. In clinical practice, formulations for individuals presenting with psy-
chosis typically incorporate psychosocial and environmental factors that may have contributed
to the precipitation of the psychotic episode, and the role of AI use in the development of symp-
toms may arguably be captured by these existing processes. Furthermore, some of these episodes
may be adequately described using existing diagnostic constructs, such as the ICD-11 concept of
acute and transient psychotic disorder, or, in some cases, as exacerbations of pre-existing severe
8

mental illness.
Another reason to refrain from using the label of “AI psychosis” (or “AI-induced psychosis”)
is that the term implies a degree of causation which we are, as yet, unable to conclusively
ascribe. Given that the current evidence base consists of anecdotal media articles, individual
clinical case reports, and preliminary observational data, it is difficult to ascertain the extent
to which underlying risk factors for psychotic illness may be driving the observed presentations,
with the chatbot serving as delusional content rather than cause. Reported cases are also
subject to selection and reporting bias: dramatic cases are more likely to reach journalists and
case reports, and denominator data on the many users who interact intensively with chatbots
without apparent harm are lacking. As such, there remains a clear need for empirical research,
including longitudinal cohort studies of affected individuals, to better understand the role of AI
in symptom development.
Furthermore, one can argue that the use of the term “AI psychosis” is inherently stigmatising
and reflective of a wider practice of language associated with severe mental illness (e.g. “hallu-
cinating”) being employed to describe negative outcomes associated with AI use. Sensationalist
and irresponsible reporting of this phenomenon risks driving public fear and moral panic, and
may lead to conceptual overreach whereby experiences that would not traditionally be labelled
as pathological are classed as such, thereby detracting from the more pressing issue of people
experiencing genuine harm and considerable occupational, social, and personal disruption on
account of changes in their mental state following intensive AI chatbot interactions.
It is also important to note that the potential psychiatric presentations reported in associa-
tion with AI use extend beyond psychosis, and as such the term “AI psychosis” might serve as a
low-granularity nosological catch-all for a broader spectrum of harms. In its current popular us-
age, there is a real risk that members of the public and non-medical bodies are already using the
term “AI psychosis” to refer to cases of mania without psychotic symptoms, or states of intense
emotional dependence that might better be likened to a behavioural addiction. By focusing on
AI-associated psychosis, we may therefore miss a wider spectrum of AI-related mental health
deteriorations which will become more readily apparent in the months and years to come (e.g.
validation of cognitive distortions regarding weight and body image in eating disorders and body
dysmorphic disorder, or the facilitation of endless reassurance-seeking in obsessive-compulsive
disorder).
Finally, whilst not necessarily a reason to rule out establishing AI-associated psychosis as
a diagnostic entity, there is an ontological argument that clinicians and researchers ought to
be aware of the potential impact of the looping effects of diagnostic classification [38]. These
are feedback loops whereby a form of classification, together with the practices and institutions
that apply it, may alter the self-understanding, behaviour, or circumstances of the individuals
classified, which in turn feeds back into changing the extension and character of the category
itself, prompting revisions in descriptions, criteria and associated knowledge [38, 39, 40]. In
the context of a heavily mediatised phenomenon, such looping effects could plausibly be ampli-
fied: individuals may come to interpret their experiences through the lens of a label they first
encountered online, or, indeed, through conversation with a chatbot itself.
4 Discussion and Future Directions
As LLM and AI chatbot use continues to increase, we expect to see more reports of AI-associated
psychosis surfacing from the media and clinical institutions alike. Additionally with the in-
creased progress of both video and voice agents, this introduces another potential anchor for
anthropomorphisation – when a chatbot mimics a human’s facial expressions, tone, cadence,
and emotionality they become ever more human like. We believe this multi-modality may fur-
ther strengthen or reinforce the existing anthropomorphic nature of our relationship to AI. A
key question that arises is: what can be done about it right now? We argue that no single stake-
9

holder can address this problem alone, because the necessary knowledge is fragmented: clinicians
see the presentations but not the model internals; developers see the conversation logs but lack
clinical framing; regulators have enforcement power but no signal to act on. Meaningful progress
therefore depends on establishing a shareddetect–report–understand–mitigateloop across stake-
holders, analogous to pharmacovigilance in medicine: clinicians detect and characterise cases,
structured reporting channels aggregate them, researchers and developers use this signal to un-
derstand mechanisms and fix models, and regulators verify that mitigation has occurred. The
recommendations below are organised around each stakeholder’s contribution to that loop.
Clinicians, Care Providers, and Clinical Institutions: Detection.Regardless of
whether AI-associated psychosis becomes a distinct diagnostic entity, awareness of the phe-
nomenon needs to be raised among clinicians and the public alike. In practical terms, we
suggest that clinicians assessing new-onset psychosis, mania, or marked behavioural change rou-
tinely ask about AI chatbot use, in the same way that substance use is routinely explored, and
document positive findings in a structured way that supports later aggregation. Recognising
and characterising at-risk or existing cases is the raw signal on which every downstream actor
depends. Data diversity is critical: AI-associated psychosis may manifest differently across cul-
tural backgrounds, and the existing case literature is heavily skewed towards English-speaking,
high-income settings.
A 21st-Century Technological History.To support this, we propose an adaptation
of traditional medical history-taking that incorporates atechnological history: a structured
set of questions around human–technology interaction designed to capture technology-related
contributors to presentation. In the context of suspected AI-associated harm, this might include:
which AI systems and platforms are used, and via which modalities (text, voice, companion
apps); the duration, frequency and timing of use, including nocturnal use and associated sleep
disruption; the content and emotional tone of conversations, and whether transcripts can be
reviewed with the patient’s consent; the degree of anthropomorphisation and attachment (e.g.
naming the AI, attributing sentience to it, romantic involvement); whether the AI’s outputs have
influenced significant beliefs or decisions; functional impact on work, relationships and self-care;
and the individual’s response to periods of abstinence from the system. Such a history would
be relevant not only to psychosis but to the broader spectrum of AI-associated presentations
described above.
Conceptual Clarification: General Slang vs. Clinical Syndrome.A primary hurdle
in tracking this phenomenon is its evolving definition. Currently, the term “AI psychosis” risks
being diluted into general online slang or internet hyperbole used to describe standard algorith-
mic errors or ordinary heavy use. A standardised working definition, ideally developed through
formal consensus methodology (e.g. a Delphi process) involving psychiatrists, AI researchers,
and individuals with lived experience, is a prerequisite for case ascertainment, surveillance, and
research. As a starting point for such discussions, Table 1 sets out the psychotic symptom
domains as defined in DSM-5-TR [36] and ICD-11 [37] alongside the patterns that have so far
beendescribedin reported cases. We stress that the final column is a descriptive synthesis of
the current (largely anecdotal) case literature, not a proposal for what the diagnostic criteria
of AI-associated psychosis should be; whether these patterns are consistent, specific, or stable
enough to ground operational criteria is precisely the empirical question that remains open.
Exacerbation vs. De Novo Psychosis.Only by accumulating and sharing on-the-ground
clinical reports of these cases with the wider community can we shed light on key questions,
including: What is the incidence and severity of AI-associated psychosis? What are the different
phenotypes? What are the predisposing, precipitating and perpetuating factors? Can AI-
associated psychosis be triggered by chatbots in a person with no prior mental health history?
Does it warrant its own diagnostic criteria?
Developersand“BigTech”: Pre-deploymentTestingandPost-deploymentSurveil-
lance.Frontier models routinely undergo red-teaming and safety testing prior to public release;
10

this typically covers threats such as biological, chemical, nuclear and cyber misuse, as well as
qualitative checks around misalignment and deception. Psychological safety should be added to
this list as a first-class release criterion: models should be benchmarked for sycophancy, exces-
sive anthropomorphisation, and delusion reinforcement prior to release, with results published
in model cards so that claims of safety are auditable rather than taken on trust.
Because pre-deployment testing cannot anticipate all real-world harm, post-release surveil-
lance is equally necessary. Frontier technology companies should collaborate cross-functionally
with clinicians and researchers to characterise the nature and trajectory of delusional and harm-
ful conversations; on this basis it may become possible to detect high-risk conversational tra-
jectories and steer users away from them. Candidate technical interventions span a spectrum
of sophistication, from system prompt adjustments, through inference-time guardrails and clas-
sifiers and limits on session length and continuity, to deeper alterations to pre-training and
preference-based fine-tuning. Each involves trade-offs between safety, utility, and user privacy
that warrant empirical study rather than assumption. Developers should additionally provide
accessible mechanisms for users and families to report harmful model behaviour, feeding the
same surveillance loop. Provenance and accountability mechanisms, such as cryptographically
signed outputs or secure conversation logging, could in principle support post-incident review
of a model’s role in a harmful act, analogous to a flight recorder in aviation. We note, however,
that text watermarking remains technically fragile (it can be degraded by paraphrasing), and
that any such logging must be balanced against significant privacy and confidentiality concerns,
particularly given the sensitive nature of mental health-related conversations.
Researchers and Academic Institutions: From Anecdote to Evidence.The re-
search agenda spans both sides of the human–machine dyad. On the clinical side, priorities
include establishing case registries and longitudinal cohorts to move the evidence base beyond
anecdote, deriving a consensus case definition, and identifying predisposing and protective fac-
tors. On the technical side, priorities include developing systems to detect sycophantic and
delusion-reinforcing model behaviour, refining benchmarks that measure the propensity of mod-
els to co-construct delusional content, and evaluating pre- and post-training mitigation methods.
Crucially, these strands should not run in parallel but in dialogue: clinical phenotypes should in-
form benchmark design, and benchmark findings should generate hypotheses testable in clinical
populations.
Regulatory Bodies and Governmental Institutions: Closing the Loop.At a so-
cietal level, governments should consider carefully the effects of LLM-associated psychological
destabilisation and influence. The wider spectrum of effect, from milder shifts in psychological
tendencies and biases through to overt psychiatric disease, can not only harm population men-
tal health but also drive division and polarisation, much like the documented effects of social
media [12]. Regulators are the actor capable of making the surveillance loop mandatory rather
than voluntary. Existing post-market surveillance infrastructure, such as the MHRA Yellow
Card scheme, could be adapted to capture AI-related mental health harms, creating a formal
reporting channel equivalent to that for adverse drug reactions [30]. Reporting guidelines such
as CONSORT-AI [41] could be expanded to explicitly cover sycophancy and psychological safety
outcomes in trials of AI-based interventions. The December 2025 NAAG letter demonstrates
that enforcement bodies are already prepared to treat sycophantic and delusional outputs as a
consumer protection issue [11]; formal regulatory frameworks should follow, specifying disclosure
requirements, third-party audit rights, and incident notification duties.
In conclusion, whether or not AI-associated psychosis ultimately earns recognition as a dis-
tinct diagnostic entity, the harms it describes are real enough to warrant coordinated action now,
and the nosological debate must not become a reason for delay. The phenomenon sits at the
intersection of clinical medicine and machine learning, and so does its solution: clinicians who
ask the right questions, researchers who convert cases into evidence, developers who treat psy-
chological safety as a release criterion, and regulators who make surveillance and accountability
11

mandatory. LLMs are the latest in a long line of dual-use technologies posing both benefit and
harm to society; what is different this time is that the harm operates through conversation, with
unique mechanisms of sycophancy and anthropomorphism. It is essential that all stakeholders
are informed and take an active part in shaping the future of this technology.
12

References
[1] J. Au Yeung, J. Dalmasso, L. Foschini, R. J. Dobson, and Z. Kraljevic. The psychogenic
machine: Simulating AI psychosis, delusion reinforcement and harm enablement in large
language models.arXiv preprint arXiv:2509.10970, 2025. Available from:https://arxiv.
org/abs/2509.10970.
[2] Hamilton Morrin, Luke Nicholls, Michael Levin, Jenny Yiend, Umesh Iyengar, Francesco
DelGuidice, et al. Delusions by design? how everyday AIs might be fuelling psychosis (and
what can be done about it). OSF Preprints, September 2025. Available from:https:
//osf.io/cmy7n_v5[Accessed: 2025-09-25].
[3] JosephM.Pierre, BenGaeta, GovindRaghavan, andKarthikV.Sarma. “You’reNotCrazy”:
A Case of New-onset AI-associated Psychosis.Innovations in Clinical Neuroscience, 22(10–
12):11–13, 2025.
[4] Søren D. Østergaard. Will generative artificial intelligence chatbots generate delusions in
individuals prone to psychosis?Schizophrenia Bulletin, 49(6):1418–1419, 2023.
[5] Hamilton Morrin, Quinton Deeley, and Thomas Pollak. Playing with the dials of belief:
how controllable AI behaviours could modulate human belief and cognition across scales.
PsyArXiv, 2025. Available from:https://osf.io/preprints/psyarxiv/7qcv8_v1/[Ac-
cessed: 2025-12-30].
[6] OpenAI. Strengthening ChatGPT’s responses in sensitive conversa-
tions, October 2025. Available from:https://openai.com/index/
strengthening-chatgpt-responses-in-sensitive-conversations/[Accessed: 2026-
01-16].
[7] Kashmir Hill. They asked an A.I. chatbot questions. The answers sent them spiraling.The
New York Times, June 2025. Available from:https://www.nytimes.com/2025/06/13/
technology/chatgpt-ai-chatbots-conspiracies.html.
[8] Rhitu Chatterjee. Their teenage sons died by suicide. now, they are sound-
ing an alarm about AI chatbots, September 2025. Available from:https:
//www.npr.org/sections/shots-health-news/2025/09/19/nx-s1-5545749/
ai-chatbots-safety-openai-meta-characterai-teens-suicide[Accessed: 2025-
12-30].
[9] S. D. Østergaard. Emotion contagion through interaction with generative artificial intelli-
gence chatbots may contribute to development and maintenance of mania.Acta Neuropsy-
chiatrica, 37:e79, 2025.
[10] S. G. Olsen, C. J. Reinecke-Tellefsen, and S. D. Østergaard. Potentially harmful con-
sequences of artificial intelligence (AI) chatbot use among patients with mental illness:
Early data from a large psychiatric service system.medRxiv, page 2025.11.19.25340580,
2025. Preprint cited 2025 Nov 29. Available from:https://www.medrxiv.org/content/
10.1101/2025.11.19.25340580v1.
[11] National Association of Attorneys General. Letter to the legal representatives of An-
thropic, Apple, Chai AI, Character Technologies, Google, Luka, Meta, Microsoft, Nomi
AI, OpenAI, Perplexity AI, Replika, and xAI, 2025. Available from:https://www.
iowaattorneygeneral.gov/media/cms/12_68B5C629180F6.pdf[Accessed: 2025-12-30].
13

[12] Emily Kubin and Christian von Sikorski. The role of (social) media in political polarization:
A systematic review.Annals of the International Communication Association, 45(3):188–
206, 09 2021.
[13] Adam M. Enders, Joseph E. Uscinski, Michelle I. Seelig, Casey A. Klofstad, Stefan Wuchty,
John R. Funchion, Manohar N. Murthi, Kamal Premaratne, and Justin Stoler. The rela-
tionship between social media use and beliefs in conspiracy theories and misinformation.
Political Behavior, 45(2):781–804, 2023.
[14] Mrinank Sharma, Meg Tong, Tomasz Korbak, David Duvenaud, Amanda Askell, Samuel R.
Bowman, Newton Cheng, Esin Durmus, Zac Hatfield-Dodds, Scott R. Johnston, Shauna
Kravec, Timothy Maxwell, Sam McCandlish, Kamal Ndousse, Oliver Rausch, Nicholas
Schiefer, Da Yan, Miranda Zhang, and Ethan Perez. Towards understanding sycophancy in
language models.arXiv preprint arXiv:2310.13548, 2023. Available from:https://arxiv.
org/abs/2310.13548.
[15] Billy Perrigo. OpenAI used Kenyan workers on less than $2 per hour to make
ChatGPT less toxic, January 2023. Available from:https://time.com/6247678/
openai-chatgpt-kenya-workers/[Accessed: 2026-02-26].
[16] Aaron Fanous, Jacob Goldberg, Ank A. Agarwal, Joanna Lin, Anson Zhou, Roxana
Daneshjou, and Sanmi Koyejo. Syceval: Evaluating LLM sycophancy.arXiv preprint
arXiv:2502.08177, 2025. Available from:https://arxiv.org/abs/2502.08177.
[17] Jiseung Hong, Grace Byun, Seungone Kim, Kai Shu, and Jinho D. Choi. Measuring
sycophancy of language models in multi-turn dialogues, 2025. Available from:https:
//arxiv.org/abs/2505.23840.
[18] Botai Yuan, Yutian Zhou, Yingjie Wang, Fushuo Huo, Yongcheng Jing, Li Shen, Ying
Wei, Zhiqi Shen, Ziwei Liu, Tianwei Zhang, Jie Yang, and Dacheng Tao. Echobench:
Benchmarking sycophancy in medical large vision-language models, 2025. Available from:
https://arxiv.org/abs/2509.20146.
[19] Petter Bae Brandtzaeg, Marita Skjuve, and Asbjørn Følstad. My ai friend: How users of
a social chatbot understand their human–ai friendship.Human Communication Research,
48(3):404–429, 04 2022.
[20] Joshua Au Yeung, Zeljko Kraljevic, Akish Luintel, Alfred Balston, Esther Idowu, Richard J.
Dobson, and James T. Teo. AI chatbots not yet ready for clinical use.Frontiers in Digital
Health, 5, 2023.
[21] YouGov. Ai thinking – yougov survey, July 2026. Fieldwork: July 16–20, 2026; N = 1,110
U.S. adults.
[22] Michelle Cohn, Mahima Pushkarna, Gbolahan O. Olanubi, Joseph M. Moran, Daniel Pad-
gett, Zion Mengesha, and Courtney Heldreth. Believing anthropomorphism: Examining
the role of anthropomorphic cues on trust in large language models, 2024. Available from:
https://arxiv.org/abs/2405.06079.
[23] Robin Schimmelpfennig, Mark Díaz, Vinodkumar Prabhakaran, and Aida Davani. Human-
like ai design increases anthropomorphism but yields divergent outcomes on engagement
and trust globally, 2026. Available from:https://arxiv.org/abs/2512.17898.
[24] Kashmir Hill and D. Freedman. Chatbots can go into a delusional spiral. Here’s how it
happens.The New York Times, August 2025. Available from:https://www.nytimes.com/
2025/08/08/technology/ai-chatbots-delusions-chatgpt.html[Accessed: 2025-08-28].
14

[25] Kashmir Hill and J. Valentino-DeVries. What OpenAI did when ChatGPT users lost touch
withreality.The New York Times, November2025. Availablefrom:https://www.nytimes.
com/2025/11/23/technology/openai-chatgpt-users-risks.html[Accessed: 2025-11-
23].
[26] Miles Klee. People are losing loved ones to AI-fueled spiritual fantasies.Rolling Stone, May
2025. Available from:https://www.rollingstone.com/culture/culture-features/
ai-spiritual-delusions-destroying-human-relationships-1235330175/.
[27] N. Darvesh, A. Radhakrishnan, C. C. Lachance, V. Nincic, J. P. Sharpe, M. Ghassemi,
et al. Exploring the prevalence of gaming disorder and internet gaming disorder: a rapid
scoping review.Systematic Reviews, 9(1):68, April 2020.
[28] Jon Roozenbeek and Sander van der Linden. Countering misinformation through psycho-
logical inoculation. InAdvances in Experimental Social Psychology, volume 69, pages 1–58.
Academic Press, 2024. Accessed 2025-12-31. Available from:https://www.sciencedirect.
com/science/article/pii/S0065260123000266.
[29] Alexandre Hudon and Emmanuel Stip. Delusional experiences emerging from AI chatbot
interactions or “AI psychosis”.JMIR Mental Health, 12(1):e85799, December 2025.
[30] Medicines and Healthcare products Regulatory Agency (MHRA). Software,
apps and artificial intelligence (AI) reporting | making medicines and medi-
cal devices safer, 2025. Available from:https://yellowcard.mhra.gov.uk/
software-apps-and-artificial-intelligence[Accessed: 2025-09-25].
[31] R. Kendell and A. Jablensky. Distinguishing between the validity and utility of psychiatric
diagnoses.American Journal of Psychiatry, 160(1):4–12, 2003.
[32] A.Jablensky. Psychiatricclassifications: validityandutility.World Psychiatry, 15(1):26–31,
2016.
[33] OpenAI. Funding grants for new research into AI and mental health, 2025. Available from:
https://openai.com/index/ai-mental-health-research-grants/[Accessed: 2025-12-
31].
[34] Mind. Mind launches AI and Mental Health Commission, feb 2026. News announcement.
[35] S. Dohnány, Z. Kurth-Nelson, E. Spens, L. Luettgau, A. Reid, I. Gabriel, et al. Technolog-
ical folie à deux: Feedback loops between AI chatbots and mental illness.arXiv preprint
arXiv:2507.19218, 2025. Accessed 2025-12-31. Available from:http://arxiv.org/abs/
2507.19218.
[36] American Psychiatric Association.Diagnostic and Statistical Manual of Mental Disorders.
American Psychiatric Association Publishing, Washington, DC, 5th ed., text rev. edition,
2022.
[37] World Health Organization. International statistical classification of diseases and related
health problems, 2019. Available from:https://icd.who.int/.
[38] T. Vesterinen. Identifying the explanatory domain of the looping effect: Congruent and
incongruent feedback mechanisms of interactive kinds.Journal of Social Ontology, 6(2):159–
185, 2020.
[39] Ian Hacking. Making up people.London Review of Books, 28(16), August
2006. Available from:https://www.lrb.co.uk/the-paper/v28/n16/ian-hacking/
making-up-people[Accessed: 2025-12-31].
15

[40] J. Y. Tsou. Hacking on the looping effects of psychiatric classifications: What is an interac-
tive and indifferent kind?International Studies in the Philosophy of Science, 21(3):329–344,
2007.
[41] Xiaoxuan Liu, S. Cruz Rivera, D. Moher, M. J. Calvert, A. K. Denniston, and SPIRIT-
AI and CONSORT-AI Working Group. Reporting guidelines for clinical trial reports for
interventions involving artificial intelligence: the CONSORT-AI extension.The Lancet
Digital Health, 2(10):e537–e548, October 2020.
16
