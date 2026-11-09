---
title: Remembering or monitoring? Contextual fit of simulated AI memory cues and consumer trust
url: https://doi.org/10.3389/fpsyg.2026.1934857
category: consumer-behavior
subcategory: empirical
date: 2026-09
venue: Frontiers in Psychology
authors:
- Runhua Huang
- Yanzhi Huang
- Huichao Guo
source: openalex-oa
pdf_url: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1934857/pdf
pages: 16
chars: 88616
fetched_at: '2026-11-08T18:49:24+00:00'
kb_version: 1
---

# Remembering or monitoring? Contextual fit of simulated AI memory cues and consumer trust

TYPE Original Research
PUBLISHED 10 September 2026
DOI 10.3389/fpsyg.2026.1934857
OPEN ACCESS
EDITED BY
Tze Wei Liew,
Multimedia University, Malaysia
REVIEWED BY
Xin Wang,
Chongqing University, China
Dario Sipos,
Institute of Technology and Digital
Marketing, Croatia
*CORRESPONDENCE
Huichao Guo
334998@whut.edu.cn
RECEIVED 11 July 2026
REVISED 25 August 2026
ACCEPTED 28 August 2026
PUBLISHED 10 September 2026
CITATION
Huang R, Huang Y and Guo H (2026)
Remembering or monitoring?
Contextual ﬁt of simulated AI memory
cues and consumer trust.
Front. Psychol. 17:1934857.
doi: 10.3389/fpsyg.2026.1934857
COPYRIGHT
© 2026 Huang, Huang and Guo. This is
an open-access article distributed under
the terms of theCreative Commons
Attribution License (CC BY).T h eu s e ,
distribution or reproduction in other
forums is permitted, provided the
original author(s) and the copyright
owner(s) are credited and that the
original publication in this journal is
cited, in accordance with accepted
academic practice. No use, distribution
or reproduction is permitted which does
not comply with these terms.
Remembering or monitoring?
Contextual ﬁt of simulated AI
memory cues and consumer trust
Runhua Huang1,2,Y a n z h iH u a n g1 and Huichao Guo1,3*
1Business Technology Innovation and Development Research Center (Hangzhou), Zhejiang Business
College, Hangzhou, Zhejiang, China,2School of Management and Economics, The Chinese University
of Hong Kong, Shenzhen, Guangdong, China,3School of Safety Science and Emergency Management,
Wuhan University of Technology, Wuhan, Hubei, China
AI assistants increasingly refer to information they ostensibly retain from
earlier sessions. A remembered preference can signal attentiveness, whereas a
reference to stress or late-night behavior can feel intrusive. Existing accounts
of personalization and privacy do not fully explain why these cues elicit
opposing reactions. We treat Memory Boundary Fit (MBF) as a preliminary
interaction-speciﬁc operationalization of whether remembered information
appears to fall within a consumer’s contextual boundary for the current
exchange.Acrosssixcontrolled,LLM-deliveredchatexperiments( N = 2,140),we
compared three complete simulated message packages that differed in whether
and how the assistant referenced remembered information: a relevant-memory
cue, an intrusive-memory cue, and no memory reference. The assistant’s
memory references were ﬁctitious claims rather than genuine retrieval of
previously disclosed information. The principal and most consistent ﬁnding
was that relevant-memory cue packages produced more favorable trust-related
outcomes than intrusive-memory cue packages; comparisons with no memory
varied across studies. Because the packages also differed in topical relevance,
sensitivity, perceived usefulness, information source, and implied surveillance,
the studies cannot isolate contextual ﬁt, or any other single cue attribute, as
the causal feature, and they do not establish MBF as a distinct psychological
mechanism. Study 2 yielded same-session indirect associations consistent with
theproposedMBFaccount.AcrossStudy2andasupplementalvalidationsample,
MBF explained additional variance in trust beyond that accounted for by the
adjacent appraisals measured alongside it. However, all of these measures were
self-reported in the same session. Study 3 found a larger intrusive-memory
penalty in the complete sleep-health scenario than in the apparel scenario, but
this is an exploratory scenario comparison rather than a test of information
sensitivity. In Study 4, the speciﬁc editable dashboard tested increased average
trust but did not selectively reduce the intrusive-memory penalty. Studies 5 and
6 extended the pattern to data-sharing and relational engagement, as well as
to loyalty and opt-in intentions, but not to transactional engagement, which
remained unaffected. These ﬁndings motivate contextual appropriateness as a
candidate design consideration to be tested in real persistent-memory systems.
KEYWORDS
AI memory, boundary regulation, consumer trust, contextual integrity, personalization,
privacy
Frontiersin Psychology 01 frontiersin.org

Huang et al. 10.3389/fpsyg.2026.1934857
1 Introduction
Consider two replies to a user’s request for headphone
recommendations. The ﬁrst says, “Since you told me you prefer a
snug ﬁt for running, here are three options.” The second says, “I
noticedyou’vebeenbrowsinglateatnightandseemstressedlately.
Maybe something calming would help?” Both replies use stored
information, but the ﬁrst is likely to feel helpful while the second
may feel intrusive. The diﬀerence lies in whether the remembered
information belongs in the exchange, rather than in how much the
systemremembersorhowaccurateitis.
AI assistants in shopping, travel, and health applications
can already retain a user’s budget, seating preference, recurring
complaint, or mood cue across sessions. This capability can reduce
repetition by allowing the system to reuse information the user
has already provided. It also makes the reappearance of stored
informationpartoftheuser’spersonalizedexperience.
Persistent memory makes stored data visible in the
conversation. With conventional personalization, users may
receive a tailored recommendation without seeing the data
that produced it. A memory-enabled assistant, by contrast, can
explicitly mention what it remembers, and the reference itself
becomes a social cue. The same fact may signal attentiveness in
one exchange and monitoring in another. This distinction aligns
with evidence that willingness to share or reuse information
depends heavily on the context in which it appears, not simply on
its sensitivity (Johnetal., 2011 ). It also aligns with a recent study
showing that data-driven personalization can elicit creepiness
when consumers interpret it as intrusive or opaque surveillance
(Petrovaetal.,2026 ).
Consumer research often frames this tension as the
personalization-privacy paradox: people value tailored experiences
yet often resist the data practices needed to deliver them
(AwadandKrishnan, 2006 ; Xuetal., 2011 ; Norbergetal., 2007 ).
Privacy calculus models disclosure as a tradeoﬀ between expected
beneﬁts and costs ( DinevandHart, 2006 ), while procedural-
fairness research shows that trust in an organization’s information
practices can oﬀset some perceived costs (CulnanandArmstrong,
1999). These frameworks capture general evaluations of
personalization and privacy, but visible AI memory raises a more
speciﬁc question. A consumer may welcome one remembered
detailandrejectanotherinthesameconversation.Inthatmoment,
the issue is not data collection in general but why the assistant
knows a particular fact and whether it should mention it here.
Privacychoicesvarywithframing,defaults,andimmediatecontext
(Acquistietal., 2015; Adjeridetal., 2019). People also disclose the
same information in one interactional frame and withhold it in
another, even from an anonymous counterpart (Johnetal., 2011 ).
Aﬁxeddispositiontowardprivacyconcerndoesnotreadilyexplain
eitherpattern.
The theory of contextual integrity locates privacy violations
in information ﬂows that breach contextual norms (Nissenbaum,
2010). On this account, a remembered detail is neither inherently
private nor public. Its appropriateness depends on the people
involved, the setting, and the purpose of the exchange. For AI-
mediated consumer interactions, however, the theory does not,
on its own, specify an interaction-level consumer measure. Such
a measure is compatible with economic accounts of privacy
tradeoﬀs (Acquistietal., 2016 ) and with marketing research on
data privacy and information control (MartinandMurphy, 2017).
Bothtraditionstreatprivacyjudgmentsasresponsivetoimmediate
circumstances.
Several adjacent traditions describe closely related reactions
and therefore constrain what a new measure can claim.
Communication privacy management treats disclosed information
as jointly owned and governed by negotiated rules, so that a
recipient who uses it outside those rules produces boundary
turbulence (Petronio, 2002, 2013). Expectancy-violation accounts
hold that a departure from what an interaction partner is expected
to do is appraised positively or negatively depending on how the
violation is interpreted (Burgoon, 1993). Research on advertising
intrusiveness locates the harm in interruption and forced exposure
(Edwardsetal., 2002 ), whereas work on creepiness emphasizes
practices that are lawful yet unsettling because social norms
have not yet settled around them (TeneandPolonetsky, 2014 ;
Petrovaetal., 2026). These accounts converge on the premise that
context governs the acceptability of an information ﬂow. MBF
is intended as a preliminary, compact interaction-level measure
of that judgment for the AI-memory setting rather than as an
established mechanism or a rival theory.SupplementarynoteS16
systematically compares MBF with each of these neighbors,
identifying for each construct the speciﬁc judgment it targets,
the condition under which it should diverge from MBF, and the
measurement that would adjudicate between them. Compared
with the appraisals measured alongside MBF in the present
data, MBF showed incremental validity in its association with
trust (SupplementarynoteS15 ). Because perceived usefulness,
intrusiveness, creepiness, information relevance, and perceived
norm violation were not measured, MBF’s empirical separation
from these appraisals remains an open question, and we return to
itintheConstructboundariessection.
We refer to this situated judgment as Memory Boundary
Fit (MBF). MBF is a preliminary, interaction-speciﬁc
operationalization of whether remembered information is
relevant, appropriate, and acceptable in the current exchange.
General privacy concern is a relatively stable disposition toward
data collection and use (Smithetal., 1996 ; Malhotraetal., 2004 ).
Bycontrast,MBFconcernsaparticularuseofrememberedcontent.
WeconceptuallydistinguishMBFfromtaskusefulness,whichasks
whetherthatcontenthelpstheimmediatedecision.Aremembered
detail may be useful yet seem out of place, or unobjectionable yet
add little to the interaction. This conceptual distinction was not
tested directly because perceived usefulness was not measured.
MBF therefore provides a candidate framework for assessing
whetherrememberedcontentbelongsinaparticularexchange.
MBF evaluates remembered content, whereas trust concerns
beliefs about a system’s competence, integrity, and benevolence
under uncertainty ( McKnightetal., 2002 ; Gefenetal., 2003 ;
Pavlou,2003).Anassistantmayaccuratelyanticipateauser’sneeds
and therefore appear competent. The same assistant may still lose
integrity-based trust by surfacing information the user did not
expect to see in the exchange. We therefore examine MBF as
a candidate appraisal that determines whether a memory cue is
perceivedasattentivenessorsurveillance.
Frontiersin Psychology 02 frontiersin.org

Huang et al. 10.3389/fpsyg.2026.1934857
Research on anthropomorphism and algorithmic skepticism
suggests competing reactions to memory. Humanlike cues can
make an automated agent seem warmer and more socially
engaging (Blutetal., 2021), and remembering a previous exchange
may reinforce that sense of continuity. Yet consumers often
resist AI in decisions they regard as subjective, personal, or
high stakes (Longonietal., 2019 ; Casteloetal., 2019 ), although
reactions vary by task and can include algorithm appreciation
(GliksonandWoolley,2020 ).Areferencetostoredinformationcan
therefore signal warmth and competence while reminding the user
thatthesystemcapturesdata.ThismakesvisiblethedualroleofAI
asasocialinterlocutorandatoolfordatacollection( Puntonietal.,
2021).
Studies of recommendation agents show that personalization
and familiarity can build trust by making an agent more
useful and understandable ( KomiakandBenbasat, 2006 , 2008;
WangandBenbasat, 2005 ). Conversational framing can also
substitute for trust during onboarding (HildebrandandBergner,
2021), even though users often struggle to determine how much
weight to give a recommendation (Yeomansetal., 2019 ). Such
familiarity has limits, as trust may decline when an agent
knows or uses more information than the exchange requires.
Human-computer interaction research also shows that users have
expectations about what an agent should remember and how
they should inspect, update, or correct its memory (Jonesetal.,
2025; Zhangetal., 2025 ). Long-term memory architectures for
large language model agents provide useful capabilities but also
introducerisks( MekioussaMalki,2026 ).Thisliteratureleavesopen
a consumer-behavior account linking memory design to trust,
purchasing, data sharing, and loyalty intentions. The proposed
MBF framework addresses this gap. AI memory also belongs to a
wider class of connected consumer objects that retain data across
uses(HoﬀmanandNovak,2018 ).Fortheseobjects,concernsabout
personalizationcaninvolveconsumerautonomyoveradatatrailas
wellasprivacynarrowlydeﬁned( Andréetal.,2018 ).
The six studies follow a three-stage cumulative design.
Studies 1 and 2 establish the memory-cue pattern, with Study
2 examining same-session indirect associations consistent with
the proposed MBF account. Study 3 compares two complete
scenarios, and Study 4 tests whether a speciﬁc editable dashboard
selectively attenuates the intrusive-memory penalty. Studies 5 and
6 extend the analysis to data-sharing and relational engagement,
privacy trust, and downstream intentions. Because participants
had no prior interaction history with the assistant and the
remembered details were ﬁctitious, the experiments test consumer
responses to simulated claims of memory rather than to genuine
retrieval of previously disclosed information; we return to this
boundarythroughout.
The research makes three deliberately bounded contributions.
First, it connects simulated memory-cue packages with consumer
trust and engagement, extending work focused mainly on
usability and privacy expectations (Jonesetal., 2025 ; Zhangetal.,
2025; MekioussaMalki, 2026). Second, it applies an interaction-
speciﬁc contextual account to the personalization-privacy tension
by asking whether remembered content appears to belong
in the current exchange ( AwadandKrishnan, 2006 ; Xuetal.,
2011). Third, it oﬀers MBF as a preliminary consumer-level
operationalization informed by contextual integrity (Nissenbaum,
2010). This measurement proposal is linked to commercially
relevant outcomes, not evidence that a distinct psychological
mechanismhasbeenestablished.
1.1 Hypotheses
The studies address successive parts of the MBF account in
threestages.Theyﬁrsttestthememory-cuepatternandanindirect-
associationaccount,thencomparecompletescenarioswithasingle
dashboard, and ﬁnally compare engagement and downstream
intention outcomes. Relevant memory should increase trust by
signaling competence and reducing eﬀort. Intrusive memory
should reduce trust because it may be interpreted as crossing
a contextual boundary. No memory provides no personalization
beneﬁt but also avoids that potential boundary violation, so we
expected it to fall between the other conditions. The relevant-vs.-
intrusivecontrastfollowsfromthesepredictionsandprovidestheir
clearestcombinedcomparison.
H1: Relevant AI memory increases trust and purchase
intention relative to no memory, whereas intrusive AI memory
decreasesboth.
H2: Memory type is indirectly associated with trust through
measuredMBF.BecauseMBFandtrustweremeasuredinthesame
session, this hypothesis concerns a statistical indirect association
ratherthancausalmediation.
Because consumers in high-sensitivity domains expect
narrower information ﬂows and stronger protection, we expected
theharmofintrusivememorytobeampliﬁedratherthanconstant
acrossproductcategories.
H3: The negative eﬀect of intrusive memory on trust is
strongerinhigh-sensitivityproductdomainsthaninlow-sensitivity
domains. Study 3 was motivated by this a priori expectation, but
because its two complete scenarios varied across several attributes
simultaneously, it oﬀers only an exploratory scenario comparison
anddoesnotdirectlytestH3.
If consumers can inspect, edit, or delete stored memories,
memory use may be reinterpreted as procedurally fair and
governableratherthanimposed.
H4: An editable memory dashboard increases MBF and
reduces the negative eﬀect of intrusive memory on trust. As with
H3,weretaintheoriginalaprioriwording.Study4operationalized
this expectation with a single inspect-edit-delete dashboard in one
presentation and at one timing, and it included no perceived-
control manipulation check, so its results are limited to that
implementationratherthantoeditablecontrolingeneral.
Data-sharing engagement exposes consumers to continued
information vulnerability and should therefore depend strongly
on trust in privacy practices. Perceived intrusiveness and privacy
concerns can erode attitudes toward continued information
use (Banoetal., 2022 ). Transactional engagement (e.g., purchase
intention) often depends more on product utility and may be less
sensitivetomemoryboundaryviolations.
H5: MBF has a stronger relationship with data-sharing
engagementthanwithtransactionalengagement.
Frontiersin Psychology 03 frontiersin.org

Huang et al. 10.3389/fpsyg.2026.1934857
We expected this immediate relational evaluation to be
associatedwithlonger-runrelationshipoutcomesviaprivacytrust.
H6: Memory type is associated with loyalty and opt-in
intentions via serial indirect associations involving MBF and
privacytrust.
2 Materials and methods
2.1 Participants and procedure
All six studies recruited students and local adult residents
through Zhejiang Business College course-participation channels
and on-campus community recruitment events. Students received
course credit, and local residents received small gifts. Including
both groups was intended to broaden the sample beyond students
alone. Eligible participants were at least 18 years old, ﬂuent in
Chinese, and able to complete the scenario task. All materials,
assistant messages, and questionnaire items were presented in
Simpliﬁed Chinese. Data were collected between March and
June 2026. At the beginning of each session, the experiment
programassignedparticipantsattheindividuallevelusingbalanced
randomized blocks; experimenters neither selected nor knew the
assignments. Participants gave electronic informed consent before
seeing the experimental material. Participants were told they were
testingaprototypeAIshoppingassistant;theinstructionsmadeno
claim about whether the assistant had access to previously stored
personal data, and suspicion about the memory references was not
assessed. The assistant’s memory references were simulated, and
participants had no prior interaction history with it. A debrieﬁng
screen therefore explained that the remembered details were
ﬁctitious and did not reﬂect stored personal data. The Institutional
Review Board of Zhejiang Business College approved the protocol
(ProtocolNo.ZJBCSCCT-2026-EXP007;March1,2026).
A total of 2,302 individuals were screened across the six
studies.Screeningappliedfourexclusioncriteria:failedattentionor
comprehension checks; data-entry errors (incomplete, malformed,
or duplicated submissions); insuﬃcient completion time (less than
one-third of the study median); and erroneous content (stimulus-
delivery compliance failures or oﬀ-task free-text input). These
criteria removed 162 responses (7.0%), leaving an analytic sample
of N = 2,140. Study-level samples weren = 264, n = 289,
n = 410, n = 516, n = 318, and n = 343 for Studies
1–6, respectively. SupplementaryTableS1 reports the screened,
excluded, and retained counts for each study, along with the
number of exclusions attributable to each of the four reasons.
Because raw screening logs are stored separately from the de-
identiﬁedanalysisﬁlesundertheIRBprotocol,wereportexclusions
by study and by reason rather than by condition. The retained
condition cells were nearly balanced in every study and show no
obvious gross depletion of any single condition, but condition-
speciﬁc exclusion rates cannot be tested from the retained ﬁles.
Retained cell sizes were 91/88/85 (no-memory/relevant/intrusive)
inStudy1,96/99/94inStudy2,67–70percellacrossthesixdesign
cells in Study 3, 84–88 per cell in Study 4, 108/106/104 in Study 5,
and116/115/112inStudy6.Becauseparticipationwasanonymous
and no directly identifying information was retained, we cannot
verifywhetheranyindividualtookpartinmorethanonestudy.The
pooled sample comprised 71.45% students and 28.55% local adult
residents.Participantshadameanageof26.18years( SD = 10.61);
58.3% identiﬁed as female, 40.1% as male, and 1.6% preferred not
to say. Campus-based sessions accounted for 71.2% of responses,
and online or network testing links accounted for 28.8%. Campus
andonlinesessionsfollowedidenticalproceduresandpresentedthe
same chat prototype and questionnaires; supplementary analyses
found no main eﬀect of testing channel and no Memory Type
× Channel interaction on any focal outcome (all p ≥ 0.18;
SupplementarynoteS13 ). Session identiﬁers were not retained in
the de-identiﬁed ﬁles, so intraclass correlations within recruitment
sessions cannot be computed. Because the experiment program
randomized conditions at the individual level within each session
ratherthanassigningconditionsby session,session-levelclustering
cannot confound the condition comparisons, although it could
in principle aﬀect standard errors.SupplementaryTableS2 reports
the composition and demographics of each study. We retain de-
identiﬁed analysis ﬁles, the stimulus protocol, the data dictionary,
analysis scripts, and exact statistics with the project materials. Raw
screeninglogsarestoredseparatelytoprotectparticipantprivacy.
Sample sizes were determined by the number of eligible
participants available within each study’s scheduled recruitment
windowratherthanbyprospectivepoweranalysis.Theexperiment
program assigned conditions in balanced blocks, and responses
excluded by the screening rules were replaced by continued
recruitment within the same window to keep the design cells
balanced. This procedure explains why the retained cells are near-
equal in Studies 1, 2, 5, and 6 and equal across the second factor
in the factorial designs of Studies 3 and 4. Recruitment was never
conditionedonoutcomedata:nointerimanalyseswereconducted,
and no study was stopped or extended based on observed eﬀects.
Achieved-sample power bounds for the original experimental test
familyarereportedinthe SupplementaryTableS10 .
In each study, participants chatted in real time with a mobile
prototype powered by Google’s gemini-3-flash-preview
large language model (Figure1). The prototype was accessed via
the oﬃcial Google API in Google AI Studio during the March–
June 2026 collection window. Because this was a preview build
that the provider could update without a public version change,
we cannot guarantee exact regeneration of the stimulus text.
The logged replies and the compliance checks described below
therefore document what participants actually received. The chat
delivered the experimental stimulus; outcome measures were
standard self-reports completed immediately afterward. Within
each scenario, and in Study 4 within each dashboard level, the
assigned memory cue was inserted programmatically into an
otherwise ﬁxed reply template via a conversation-preﬁx variable.
Thus, the memory-type conditions diﬀered only in the memory
sentence, while the core recommendation remained unchanged
within that scenario; the scenario factor in Study 3 and the
dashboard factor in Study 4 introduced the additional diﬀerences
described below. Decoding used a low temperature to limit
generativevariance(temperature = 0.1,top-p = 0.8,maximum600
tokens).Fixedpromptsandcondition-speciﬁcfew-shotconstraints
enforced this structure. Each session comprised the participant’s
Frontiersin Psychology 04 frontiersin.org

Huang et al. 10.3389/fpsyg.2026.1934857
FIGURE 1
Schematic of the memory manipulation and boundary-ﬁt logic.(A) Example replies in the no-memory, relevant-memory, and intrusive-memory
conditions for the same request. The remembered detail appears within the assistant’s message, while the core recommendation remains identical
across conditions.(B) The contextual-integrity boundary separating task-relevant memories from sensitive, cross-contextual content. Within each
scenario and dashboard level, the memory-type conditions used identical message formatting and visual styling, while memory-related wording
differed.
opening free-text request, the assistant’s focal reply carrying the
manipulation, and up to one free-text follow-up question. The
system instruction required follow-ups to be answered from the
ﬁxedoptionset,withnonewmemoryinformationintroduced.The
conversationendedafterthefollow-up,andparticipantsproceeded
directly to the questionnaire without the option to continue
chatting. Within each scenario and dashboard level, message
formatting and visual styling were identical across memory-type
conditions,andallreplieswerelogged.Anautomatedcheckveriﬁed
that the ﬁxed recommendation was appropriate for the assigned
scenario, memory condition, and permitted reply length for every
retained session. A second check conﬁrmed that no memory
reference appeared in the no-memory condition; every retained
session passed both checks. Measures followed a ﬁxed order in
every study: the MBF items (where measured) were administered
immediately after the chat and before the trust items; trust and
purchase intention preceded the broader platform judgments,
and downstream engagement and intention measures came last.
In every indirect-association model, the intermediate appraisal
was therefore measured before the outcomes but within the
same session. TheSupplementarymaterials contain the full system
prompt, few-shot constraints, decoding settings, and example
exchangesforeachcondition.
2.2 Design of the six studies
The no-memory condition presented a generic
recommendation without reference to prior interaction. The
relevant-memory condition referenced information that clearly
ﬁt the current task, such as budget, intended use, or comfort
preference. The intrusive-memory condition referenced sensitive
or cross-contextual information, such as late-night browsing
patterns, stress cues, or unrelated prior behavior. We refer to
the three complete assistant messages as cue packages; the no-
memory package is the same message with no memory reference.
These packages diﬀered jointly in topical relevance, information
sensitivity, potential perceived usefulness, information source,
and implied surveillance. Two of these attributes diﬀer from the
others. Topical relevance and information source are constitutive
of what we intended to manipulate: on the contextual account,
a remembered detail ﬁts an exchange partly because it bears on
Frontiersin Psychology 05 frontiersin.org

Huang et al. 10.3389/fpsyg.2026.1934857
TABLE 1 Overview ofstudy designs.
Study Objective Design Scenario domain Main outcomes Theoretical role
1 Testmemorytypeeﬀects Nomemory/Relevant/
Intrusive
Apparel(jacket) Trust,purchaseintention,
continueduse
Teststhebasicbeneﬁt-risk
pattern
2 Examineindirect
association
Memorytypewith
measuredMBFappraisal
Apparel(jacket) MBF,trust Estimatesasame-session
indirectassociation
3 Comparecomplete
scenarios(exploratory)
Memorytype ×scenario Apparelvs.sleephealth Trust Doesnotisolateinformation
sensitivity
4 Evaluate a speciﬁc
dashboard
Memorytype ×
inspect-edit-delete
dashboard
Apparel(jacket) Trust,MBF Testsonlythedashboard
implementationpresented
5 Compareengagement
types
Memorytype Apparel(jacket) Transactional,data-sharing,
relationalengagement
ComparesMBFassociations
acrossengagementoutcomes
6 Testdownstream
intentions
Memorytypewithserial
indirect-association
model
Apparel(jacket) Privacytrust,loyalty
intention,opt-inintention
Estimatessame-session
indirectassociationswith
downstreamintentions
the current task and partly because of how the assistant came to
know it. Sensitivity, potential usefulness, and implied surveillance,
by contrast, are attributes we did not intend to vary but could
not hold constant while producing a recognizably intrusive cue.
Neither group can be separated from the others in these data.
The experiments therefore estimate responses to the cue packages
as presented rather than isolating contextual ﬁt, or any other
single cue attribute, as the causal feature. In contextual-integrity
terms (Nissenbaum, 2010), the actors and exchange setting
were held constant across memory-type conditions within each
scenario and dashboard level; the manipulated memory cue
varied the information attributes (task-relevant vs. sensitive or
cross-contextual content) and the implied transmission principle
(reuse of information within its disclosure context vs. carryover
from another context). Study 3 separately changed the complete
scenario, and Study 4 separately varied the presence of one speciﬁc
set of controls for inspecting, editing, or deleting stored memories
(Table1).
Studies 1, 2, and 4–6 used an apparel scenario. Participants
requested a jacket recommendation, and the assistant returned
a ﬁxed set of three options. Study 3 crossed memory type
with scenario: apparel vs. sleep health. The sleep-health scenario
used a parallel recommendation structure and recommended
a sleep-monitoring ring, a smart white-noise machine, and
melatonin drops. We selected the domains a priori because we
expected them to diﬀer in information sensitivity, consistent
with evidence that health-related contexts are highly sensitive
(Longonietal., 2019 ). However, the scenarios also diﬀered in
product, recommendation content, cue wording, and other
attributes, so Study 3 is presented as an exploratory comparison
of two complete scenarios rather than as an isolated manipulation
ofsensitivity.
Studies 1 and 2 examined the basic memory-cue pattern, and
Study2alsoexaminedsame-sessionindirectassociationsinvolving
MBF. Study 3 then compared the pattern across two complete
scenarios, and Study 4 tested the speciﬁc inspect-edit-delete
dashboard. Studies 5 and 6 extended the analysis to additional
engagement outcomes, including privacy trust, loyalty intentions,
andopt-inintentions.
2.3 Measures
In the six experiments, each focal construct was computed
as the mean of three seven-point items. The outcome measures
were adapted from established scales in electronic-commerce
trust, personalization, and information-privacy research
(McKnightetal., 2002 ; KomiakandBenbasat, 2006 ; Pavlou,
2003;CulnanandArmstrong,1999 ;Malhotraetal.,2004 ),whereas
the three MBF items were newly written for this research, based
onthecontextual-integrityaccount.TrustwasmeasuredinStudies
1–4; Study 1 also measured purchase intention and continued
use. Study 5 measured transactional, data-sharing, and relational
engagement. Study 6 measured privacy trust, loyalty intention,
opt-inintention,andplatformtrust.MBFwasmeasuredinStudies
1, 2, and 4–6. Items were translated into Simpliﬁed Chinese
and checked by translation and back-translation (Brislin, 1970).
SupplementarynoteS14 documents the administration format,
response anchors, scoring rules, presentation order, the source
or theoretical basis for each measure, the administered wording
with veriﬁed back-translation, and item-level psychometric
evidence where retained data permit. MBF comprised three
seven-point items assessing whether the remembered information
was relevant, appropriate, and acceptable within the current
interaction. The experimental analysis ﬁles retain MBF as a
composite score. A supplemental validation sample (N = 234)
completed the three MBF items alongside the nine-item IUIPC
privacy-concern measure and three-item measures of relational
warmth, surveillance concern, and trust. In this sample, MBF
showed acceptable internal consistency (α = 0.76). Because a
three-indicatorone-factormodelisjust-identiﬁed,itsstandardized
loadings follow in closed form from the inter-item correlations
(0.62, 0.88, 0.66), computed from that common-factor solution
Frontiersin Psychology 06 frontiersin.org

Huang et al. 10.3389/fpsyg.2026.1934857
rather than from a principal-component solution; composite
reliability was CR = 0.77 and average variance extracted was AVE
= 0.53. A ﬁve-factor CFA ﬁt the data well (χ2 (179) = 197.85, CFI =
0.990, RMSEA = 0.021, SRMR = 0.045) and reproduced the same
loadings (0.58, 0.91, 0.66; AVE = 0.53, CR = 0.77). Discriminant-
validity checks separated MBF from adjacent constructs, but by
narrow margins: the maximum HTMT was 0.815, below the 0.85
criterion but close to it, and
√
AVE = 0.73 exceeded the largest
absolute composite correlation, |r|= 0.649 (with trust). The
loadings are uneven, and both margins are modest, so these values
supportMBFonlyasanacceptableinitialoperationalizationrather
than as a strongly established scale. Trust reliability ranged from
α = 0.86 to 0.88 across Studies 1–4. Reliability was acceptable for
purchase intention (α = 0.86), continued use (α = 0.85), and
transactional engagement (α = 0.86). Data-sharing and relational
engagement each hadα = 0.87. Privacy trust (α = 0.87), loyalty
intention (α = 0.83), opt-in intention (α = 0.86), and platform
trust( α = 0.85)showedsimilarreliability.
MBF diﬀers conceptually from usefulness, general privacy
concern, and control. Usefulness concerns whether remembered
information supports the current task. Privacy concern captures
broader worries about information collection and misuse, whereas
control concerns the ability to govern stored information. The
core recommendation remained constant across memory-
type conditions within each scenario, while the presence
and content of the memory cue varied. Study 2 measured
relational warmth and surveillance concern, and the supplemental
validation sample included IUIPC privacy concern, warmth,
surveillance concern, and trust. In each sample, MBF explained
approximately 20 percentage points of additional variance in
trust beyond the adjacent appraisals measured in that sample
(SupplementarynoteS15 ). Because MBF and trust were self-
reported in the same session, this increment reﬂects a concurrent
association and is inﬂated to an unknown degree by common-
method variance. The studies did not directly measure perceived
usefulness, creepiness, intrusiveness, information relevance, or
perceived norm violation. Therefore, distinctions between MBF
and these unmeasured appraisals remain conceptual rather than
empirically established; SupplementarynoteS16 outlines each
distinctionandthestudyneededtotestit.
2.4 Analytic strategy
We formulated all six hypotheses before data collection,
but we did not preregister the studies. We therefore describe
their designated tests, summarized inTable2, as conﬁrmatory in
intent; this label concerns the timing of the expectations, not
the strength of causal interpretation. Study 3 is an exception
in interpretation: although motivated by an a priori sensitivity
expectation, its bundled scenario manipulation does not isolate
sensitivity, so we treat its interaction only as an exploratory
comparison of the complete apparel and sleep-health scenarios.
Auxiliary outcomes, construct correlations not designated for
H5, competitive intermediate-appraisal comparisons, additional
indirect-association models, and auxiliary contrasts are treated as
exploratory. One-way and factorial ANOVAs tested experimental
eﬀects on the outcome measures, and we reported partial eta-
squared ( η2 p) throughout. Values near 0.01, 0.06, and 0.14
were interpreted as small, medium, and large, respectively.
We followed signiﬁcant omnibus eﬀects with Tukey HSD
comparisons. Assumption checks for every experimental test in
the cross-study multiplicity family (Levene’s test for variance
homogeneity; residual skewness, kurtosis, and Shapiro–Wilk
tests) are reported in SupplementarynoteS13 . Homogeneity
held in every case except Study 3, whose interaction and
expectation-aligned contrast were therefore re-estimated with
heteroscedasticity-robust (HC3) standard errors and remained
signiﬁcant. Separately from the heterogeneous hypothesis-speciﬁc
tests summarized inTable2, a Holm–Bonferroni adjustment was
applied to the original one-experimental-test-per-study family
listed in SupplementarynoteS13 . Every experimental eﬀect in
that family that was signiﬁcant without adjustment remained
signiﬁcant after adjustment (largest adjustedp = 0.017), and the
Study 4 interaction remained non-signiﬁcant. This is a robustness
check for the six-study experimental family, not a multiplicity
correction for every coeﬃcient or indirect association reported.
Pairwise comparisons within each ANOVA were Tukey-adjusted.
We report condition means with standard deviations and provide
Tukey-adjusted pairwise diﬀerences and 95% conﬁdence intervals
in SupplementaryTableS8 . Ordinary least squares regression was
used to estimate regression-based indirect-association models,
conventionally termed mediation and serial-mediation models.
We evaluated indirect associations using 95% percentile bootstrap
conﬁdence intervals from 5,000 resamples; intervals excluding
zero were treated as statistically reliable. Because memory type
is categorical, the primary models used two dummy variables,
with no memory as the reference category, yielding separate
relative indirect associations for relevant and intrusive memory
(HayesandPreacher, 2014). Ordinal-coded models (1 = intrusive,
2 = no memory, 3 = relevant) are reported only as supplementary
summaries(SupplementaryTablesS7,S9 ),becausetheno-memory
condition presents no remembered content to evaluate and we
do not interpret its MBF score as an intermediate level of ﬁt.
When an ordinal code is used, we report the dummy-coded and
relevant-vs.-intrusive re-estimations alongside it. For the same
reason, we additionally estimated the Study 2 and Study 6 models
on the relevant-vs.-intrusive subsample alone, in which every
participant rated an actual memory cue, and the intermediate
appraisal therefore has an unambiguous referent in each cell
(SupplementaryTableS9b ). Randomization supports the causal
interpretation of condition assignment but does not establish the
mediator-to-outcome paths or the ordering among same-session
self-reports. For the original expectations in H3 and H4, we also
reportthediﬀerence-in-diﬀerencescontrast(theintrusive-memory
penalty across the two scenarios or dashboard levels) alongside
the omnibus interaction ( SupplementarynoteS13 ). Achieved-
sample power analyses report the minimum detectable eﬀect with
80% power at α = 0.05 for each experimental test in the
six-study family (SupplementaryTableS10 ). For non-signiﬁcant
experimental results, we report Bayes factors comparing the null
and alternative models under two conventional default priors,
because the strength of evidence for a null is prior-dependent and
thetwodefaultsdivergesharplyinthesedesigns.TheﬁrstistheBIC
Frontiersin Psychology 07 frontiersin.org

Huang et al. 10.3389/fpsyg.2026.1934857
TABLE 2 Summary of focal results across the six studies.
Study N Focal effect Test statistic Outcome
1 264 Memorytype →trust F(2,261) = 5.96,p = 0.003, η2 p = 0.04 H1partiallysupported:
relevant-memorybeneﬁt;purchaseand
intrusive-memorypenaltynot
signiﬁcant
2 289 MBFindirect-associationmodel
(dummy-coded)
Relativeindirectassociations = 0.33,95%CI(0.18,
0.51)(relevant)and −0.42,95%CI( −0.60,−0.27)
(intrusive)
ConsistentwithH2asanassociation;no
causalmediationclaim
3 410 Memory×completescenario
comparison
F(2,404) = 4.82,p = 0.009, η2 p = 0.02;penaltycontrast
/Delta1 = 0.54,p = 0.031
H3notdirectlytested;exploratory
scenariocomparison
4 516 Memory×speciﬁcdashboard F(2,510) = 0.54,p = 0.584, η2 p = 0.002;penaltycontrast
/Delta1 = 0.16,p = 0.407
H4notsupportedforthisdashboard;no
generalcontrolclaim
5 318 MBFassociation:data-sharingvs.
transactionalengagement
Diﬀerenceindependent r = 0.35,95%CI(0.20,0.49);
diﬀerence-scoreF(2,315) = 5.78,p = 0.003
H5supportedfordata-sharingvs.
transactional,butnotvs.relational
engagement
6 343 Serialindirectassociationswith
loyaltyandopt-inintentions
(dummy-coded)
Relativeserialindirectassociations = 0.14,95%CI
(0.08,0.21)(relevant)and −0.15,95%CI( −0.23,
−0.09)(intrusive),bothoutcomes
ConsistentwithH6forsame-session
intentionoutcomes
Indirectassociationsarereportedwith95%percentilebootstrapconﬁdenceintervals(5,000resamples).Relativeindirectassociationsusenome moryasthereferencecategory.
approximation BF01 = exp[(BICalt − BICnull)/2] (Wagenmakers,
2007), computed from the ﬁtted OLS models of the corresponding
ANOVA (null model excluding, alternative model including the
focalterm).Thisapproximationcorrespondstoaunit-information
prior,thatis,a g-priorwith g = n;becausethatpriorisverydiﬀuse,
itimposesalargepenaltyonthealternativeandismarkedlybiased
toward the null at these sample sizes. The second is the Jeﬀreys–
Zellner–Siow (JZS) mixture-of-g-priors Bayes factor computed
from the same nestedF test (Liangetal., 2008 ), which places a
Cauchy prior on the standardized eﬀect and belongs to the same
family as the defaults implemented in common Bayesian ANOVA
software (Rouderetal., 2012 ). Because that family is indexed by
a prior scale, we veriﬁed that the conclusion does not depend on
the scale chosen (SupplementaryTableS12 ). We report the BIC
value ﬁrst for continuity with the wider literature, but we base
our interpretation on the more conservative JZS value, under
which none of the present nulls receives more than anecdotal-to-
moderate support (SupplementaryTableS12 ). We therefore treat
these results as consistent with no eﬀect of the size each design
could detect (SupplementaryTableS10 ), not as positive evidence
thattheeﬀectisabsent.AnalyseswereconductedinPython3using
pandas, SciPy, and statsmodels. Analysis scripts are available from
thecorrespondingauthoruponreasonablerequest.
2.5 Manipulation checks
SupplementaryTableS3 reports the manipulation checks.
Across all studies measuring MBF, scores were highest for relevant
memory and lowest for intrusive memory, with the no-memory
condition falling between them (allp < 0.001). This ordering
indicates that the complete cue packages shifted the measured
contextual-appropriateness appraisal in the intended direction.
Because no remembered content is present in the no-memory
condition, we interpret its MBF score as a neutral reference
point rather than as an intermediate level of ﬁt. Because MBF
served as both the manipulation check and the intermediate
variable in the indirect-association models, these checks are not
independentevidenceofapsychologicalmechanism.Wetherefore
give primary weight to the randomized relevant-vs.-intrusive cue-
packagecontrast.
3 Results
3.1 Study 1: memory type and trust
A one-way ANOVA showed that memory type aﬀected trust,
F(2,261) = 5.96, p = 0.003, η2 p = 0.04. Mean trust was 4.86 under
relevant memory (SD = 0.93), 4.47 under no memory (SD = 1.06),
and4.35underintrusivememory(SD=1.11; Figure2).TukeyHSD
comparisons showed that relevant memory exceeded no memory
[diﬀ= 0.40, 95% CI (0.03,0.76),p = 0.028] and intrusive memory
[diﬀ = 0.51, 95% CI (0.14,0.89),p = 0.003]. Intrusive and no
memory did not diﬀer [diﬀ= 0.12, 95% CI (−0.25,0.48), p =
0.736]. The results for continued use were similar,F(2,261) = 3.98,
p = 0.020, η2 p = 0.03. Relevant memory (M = 4.82, SD = 0.99)
exceeded no memory (M = 4.46, SD = 0.98;p = 0.040) and
intrusive memory (M = 4.45, SD = 0.96;p = 0.040), while the
lattertwoconditionsdidnotdiﬀer( p = 0.999).Purchaseintention
had the same ordering, but the omnibus eﬀect was not signiﬁcant,
F(2,261) = 1.76, p = 0.175, η2 p = 0.01. Bayes factors were sensitive
to the prior: the BIC approximation favored the no-eﬀect model
(BF01 = 45.2), but the JZS default did not distinguish the two
models (BF01 = 1.22). The observedη2 p = 0.01 also falls below the
smallesteﬀectthisstudycoulddetectwith80%power( η2 p = 0.036;
Frontiersin Psychology 08 frontiersin.org

Huang et al. 10.3389/fpsyg.2026.1934857
SupplementaryTableS10 ), so the result is uninformative rather
thanevidenceofabsence( Mrelevant = 4.73,SD=0.98; Mno = 4.59,
SD = 1.00;Mintrusive = 4.45, SD = 0.97). H1 was therefore partially
supported.Relevantmemoryincreasedtrustandcontinueduse,but
purchase intention and the intrusive-to-no-memory contrast were
notsigniﬁcant.
3.2 Study 2: memory type, MBF, and trust
Study 2 replicated the omnibus eﬀect of memory type on trust,
F(2,286) = 19.86,p < 0.001, η2 p = 0.12,althoughthepairwiseresults
diﬀered from Study 1. Trust was lower under intrusive memory
(M = 3.59, SD = 1.03) than under no memory [M = 4.17,
SD = 1.00; diﬀ= 0.59, 95% CI (0.24,0.93), p < 0.001]. Trust
was also lower under intrusive than relevant memory (M = 4.49,
SD = 1.00; diﬀ= 0.90, p < 0.001). The advantage of relevant
over no memory was not signiﬁcant (diﬀ= 0.31, p = 0.076). Both
studies produced the ordering relevant> no memory> intrusive.
ThereliablecontrastreﬂectedthebeneﬁtinStudy1andthepenalty
inStudy2.
Wenextestimatedadummy-codedindirect-associationmodel
involving MBF, with no memory as the reference category
(HayesandPreacher, 2014 ). Relevant memory increased MBF
(arel = 0.71,p < 0.001) and intrusive memory decreased it (aint =
−0.91,p < 0.001); MBF was associated with trust after adjustment
for condition (b = 0.47, p < 0.001). The relative indirect
association through MBF was 0.33 [95% bootstrap CI (0.18,0.51)]
for relevant vs. no memory and−0.42 [95% CI (−0.60,−0.27)]
for intrusive vs. no memory; the corresponding relative direct
associations were not signiﬁcant (p = 0.910 andp = 0.220). A
supplementary ordinal-coded summary model produced the same
pattern [indirect association = 0.38, 95% CI (0.28,0.49); direct
association p = 0.327; SupplementaryTableS9 ]. Because the no-
memoryconditionpresentsnorememberedcontenttoevaluate,we
also estimated the model on the relevant-vs.-intrusive subsample
alone (n = 193), in which every participant judged an actual
memory cue. Relevant memory raised MBF relative to intrusive
memory(a = 1.61,SE=0.15, p < 0.001),MBFwasassociatedwith
trust (b = 0.44, SE = 0.06,p < 0.001), and the indirect association
was 0.71 [95% bootstrap CI (0.49,0.96)]; the direct association was
not signiﬁcant (c′ = 0.19, p = 0.254; SupplementaryTableS9b ).
These results were consistent with H2 as a same-session statistical
association. They do not establish that MBF causally transmitted
theeﬀectofconditiontotrust.
The auxiliary measures allowed us to compare MBF with
relational warmth and surveillance concern. Relevant memory
produced the highest warmth (M = 4.97) and lowest surveillance
concern (M = 2.52); intrusive memory produced the reverse
pattern (Mwarmth = 3.62; Msurveillance = 4.34), F(2,286) = 52.87
and 95.17, respectively, bothp < 0.001. MBF correlated positively
with warmth (r = 0.42) and trust (r = 0.57), and negatively
with surveillance concern (r =− 0.55; SupplementaryTableS5 ).
In the supplemental validation sample, a ﬁve-factor CFA separated
MBF from IUIPC, warmth, surveillance concern, and trust (CFI =
0.990, RMSEA = 0.021, SRMR = 0.045). In a competitive indirect-
association model, MBF retained a speciﬁc indirect association
(0.38, 95% CI [0.27, 0.50]), whereas the intervals for warmth
and surveillance concern included zero; because a diﬀerence in
signiﬁcanceisnotasigniﬁcantdiﬀerence,wealsobootstrappedthe
contrasts directly, and MBF’s speciﬁc indirect association exceeded
that of warmth (diﬀerence= 0.39, 95% CI [0.24, 0.55]) and of
surveillance concern [diﬀerence = 0.40, 95% CI (0.23, 0.58)],
whichdidnotdiﬀerfromeachother( SupplementaryTableS7 ).The
same pattern holds when the competitive model is re-estimated
with dummy codes or on the relevant-vs.-intrusive subsample
(SupplementaryTableS7 ). This comparison is associational and
doesnotestablishMBFasthecausalmechanism.
3.3 Study 3: exploratory
apparel–sleep-health scenario comparison
Study 3 compared whether memory-type eﬀects diﬀered
between the complete apparel and sleep-health scenarios. The
Memory Type × Scenario interaction was signiﬁcant,F(2,404) =
4.82, p = 0.009, η2 p = 0.02. Under intrusive memory, trust was
lower in the sleep-health scenario (M = 3.48, SD = 1.34) than
in the apparel scenario (M = 4.15, SD = 1.13). Trust under
no memory and relevant memory changed little across scenarios
(Figure3). Relative to no memory, the intrusive-memory penalty
was 0.41 in the apparel scenario [95% CI (−0.0004,0.8202), p =
0.0503] and 0.95 in the sleep-health scenario [95% CI (0.53,1.38),
p < 0.001]. The diﬀerence-in-diﬀerences contrast between the
two complete scenarios was signiﬁcant [/Delta1 = 0.54, SE = 0.25,
t(404) = 2.17,p = 0.031, 95% CI (0.05,1.04)]. Because Levene’s test
indicated unequal cell variances, the interaction and contrast were
re-estimated with heteroscedasticity-robust (HC3) standard errors
and remained signiﬁcant (robust interactionF = 4.02, p = 0.018;
robust contrastz = 2.06,p = 0.039;SupplementarynoteS13 ). We
treatthisasanexploratoryscenariocomparison,notasadirecttest
of H3. Product context, information sensitivity, recommendation
content, cue wording, potential usefulness, and other scenario
characteristics changed together. The result therefore establishes
only that the complete sleep-health package carried a larger
intrusive-memory penalty than the complete apparel package;
it does not identify information sensitivity as the responsible
attribute. A valid test of H3 would hold cue content, source,
plausibility, and recommendation structure as closely matched as
possiblewhilevaryingsensitivityalone.
3.4 Study4:thespeciﬁceditabledashboard
Study 4 evaluated whether the inspect-edit-delete dashboard
testedherereducedtheintrusive-memorypenalty.A3 ×2ANOVA
found a main eﬀect of memory type on trust,F(2,510) = 36.91, p <
0.001, η2 p = 0.13. All three Tukey comparisons were signiﬁcant,
including the intrusive-to-no-memory penalty [diﬀ= 0.47, 95%
CI (0.24,0.70), p < 0.001]. The dashboard also had a main eﬀect
on trust, F(1,510) = 5.54, p = 0.019, η2 p = 0.011. Mean trust
was 4.49 when the dashboard was present (SD = 0.91) and 4.30
when it was absent (SD = 1.00). The Memory Type× Dashboard
interaction was not signiﬁcant, F(2,510) = 0.54, p = 0.584,
η2 p = 0.002. The diﬀerence-in-diﬀerences contrast comparing the
intrusive-memory penalty with and without this dashboard was
Frontiersin Psychology 09 frontiersin.org

Huang et al. 10.3389/fpsyg.2026.1934857
FIGURE 2
Study 1.(A) Trust and(B) purchase intention by memory type. Relevant memory increased trust relative to both other conditions; intrusive and no
memory did not differ signiﬁcantly. The omnibus effect on purchase intention was not signiﬁcant, so the pairwise comparison shown in(B) is
descriptive only. Brackets mark Tukey HSD pairwise comparisons (*p < 0.05, **p < 0.01; ns, not signiﬁcant). Error bars show±1 standard error of the
mean.
FIGURE 3
Study 3 exploratory scenario comparison. The complete
sleep-health scenario produced a larger intrusive-memory trust
penalty than the apparel scenario. Product context,
recommendation content, cue wording, and other attributes
changed together, so the interaction does not isolate information
sensitivity.** p < 0.01. Error bars show+/− 1 standard error of the
mean.
likewise not signiﬁcant [/Delta1 = 0.16, SE = 0.19,t(510) = 0.83, p =
0.407, 95% CI (−0.22,0.54)]. A BIC-approximation Bayes factor
favored the additive model over the interaction model (BF01 =
299.5), but this ﬁgure should not be read as decisive: under the
JZS default the same comparison yields only BF01 = 2.26, and
the observed η2 p = 0.002 is far below the smallest interaction
this design could detect (η2 p = 0.018; SupplementaryTableS10 ).
The intrusive-memory means were 4.03 with the dashboard and
3.89 without it (Figure4). The interaction for MBF was also
null (F(2,510) = 1.74, p = 0.177; BF01 = 89.4 by the BIC
approximation but 1.23 under the JZS default). Mean MBF was
4.14 with the dashboard and 4.30 without it, F(1,510) = 3.77,
p = 0.053. Here the two priors disagree in direction: the BIC
approximation favors no dashboard main eﬀect on MBF (BF01 =
3.45), whereas the JZS default slightly favors an eﬀect (BF01 =
0.65, i.e., BF10 = 1.54). We therefore treat this comparison as
undetermined. We note that the descriptive direction is opposite
to the H4 prediction: MBF was nominally lower, not higher, when
the dashboard was present. We do not interpret this diﬀerence,
which is not statistically reliable, but it gives no support to the
expectation that visible controls raise the perceived ﬁt of a speciﬁc
remembered detail. This dashboard raised trust on average but did
notselectivelyreducetheintrusive-memorypenaltyorproducethe
MBFimprovementspeciﬁedinH4.H4wasthereforenotsupported
for the implementation tested. Because we did not include a
perceived-control manipulation check, this result is limited to the
dashboardimplementation,presentation,andtimingtestedhere;it
leavesthegeneralformofH4untestedanddoesnotshowthatuser
controlisgenerallyineﬀective.
3.5 Study 5: engagement type
Memory type aﬀected data-sharing engagement, F(2,315) =
24.03, p < 0.001, η2 p = 0.13, and relational engagement,F(2,315) =
14.80, p < 0.001, η2 p = 0.09. It did not aﬀect transactional
engagement, F(2,315) = 1.95, p = 0.144, η2 p = 0.01. The
BIC-approximation Bayes factor favored the no-eﬀect model for
transactional engagement (BF01 = 44.9), although the JZS default
wasequivocal(BF 01 = 1.10),andallpairwisecomparisonshad p ≥
0.121. For data-sharing engagement, relevant memory exceeded
no memory (M = 4.86, SD = 0.91, vs. Mno = 4.20, SD =
1.08; diﬀ= 0.66, p < 0.001). Intrusive and no memory did not
diﬀer reliably (diﬀ= 0.27, p = 0.118). Thus, the data-sharing
result primarily reﬂected a relevant-memory beneﬁt rather than a
reliable intrusive-memory penalty. Relational engagement showed
both a relevant-memory beneﬁt (p = 0.010) and an intrusive-
memory penalty (p = 0.032). H5 concerns the relative strength
of MBF’s associations with the two engagement types. The focal
Frontiersin Psychology 10 frontiersin.org

Huang et al. 10.3389/fpsyg.2026.1934857
FIGURE 4
Study 4. Trust by memory type and availability of the speciﬁc
inspect-edit-delete dashboard tested. The dashboard increased
average trust (p = 0.019), but the Memory Type× Dashboard
interaction was not signiﬁcant. Thus, this dashboard did not
selectively reduce the intrusive-memory penalty; the result does not
establish that user control is generally ineffective. Error bars show
±1 standard error of the mean.
test therefore compared the two dependent correlations sharing
MBF: the MBF association with data-sharing engagement (r =
0.30, p < 0.001) exceeded the association with transactional
engagement (r =− 0.05, p = 0.423), diﬀerence in r =
0.35, 95% CI [0.20,0.49], where the conﬁdence interval for the
diﬀerence between the dependent correlations was obtained from
a 5,000-resample percentile bootstrap (SupplementaryTableS11 ).
As a complementary experimental contrast, we regressed each
participant’s data-sharing vs. transactional diﬀerence score on
memory type; this contrast was also signiﬁcant,F(2,315) = 5.78,
p = 0.003, η2 p = 0.04. MBF also correlated with relational
engagement(r = 0.20,p < 0.001),andthedata-sharingassociation
did not reliably exceed the relational association [diﬀerence in
r = 0.11, 95% CI (−0.03,0.24), same bootstrap procedure].
These results supported H5 for the focal data-sharing vs.
transactionalcontrast.
3.6 Study 6: privacy trust and downstream
intentions
Memory type aﬀected loyalty intention,F(2,340) = 9.77, p <
0.001, η2 p = 0.05, and opt-in intention,F(2,340) = 17.13, p <
0.001, η2 p = 0.09. For opt-in intention, both pairwise components
were signiﬁcant (relevant vs. no memory: diﬀ = 0.31, p =
0.038; no memory vs. intrusive: diﬀ= 0.43, p = 0.002). For
loyalty intention, the relevant- vs.-intrusive diﬀerence was clear
(diﬀ = 0.56, p < 0.001), but neither comparison with no memory
reached signiﬁcance (beneﬁtp = 0.055; penaltyp = 0.085). In
the primary dummy-coded serial indirect-association model (no
memory as reference), relevant memory increased MBF (arel =
0.77, p < 0.001) and intrusive memory decreased it (aint =
−0.85, p < 0.001); MBF was associated with privacy trust (d21 =
0.42, p < 0.001), and privacy trust was associated with both
loyalty intention (b2 = 0.43, p < 0.001) and opt-in intention
(b2 = 0.44, p < 0.001). The relative serial indirect associations
were 0.14 [95% CI (0.08,0.21)] for relevant vs. no memory and
−0.15 [95% CI (−0.23,−0.09)] for intrusive vs. no memory,
for both outcomes (SupplementaryTableS9 ). A supplementary
ordinal-coded summary model gave equivalent estimates [0.15 for
eachoutcome,95%bootstrapCIs(0.10,0.20)].Ontherelevant-vs.-
intrusive subsample (n = 227), the serial indirect association was
0.31 [95% CI (0.20,0.44)] for loyalty intention, where the direct
association was not signiﬁcant (c′ = 0.07, p = 0.591), and 0.34
[95%CI(0.23,0.47)]foropt-inintention,whereadirectassociation
remained (c′ = 0.39, p = 0.007; SupplementaryTableS9b ).
The pattern was consistent with H6 for same-session intention
outcomes.ItdoesnotestablishthecausalorderingofMBF,privacy
trust,ortheoutcomes,nordoesitestablishlongitudinalchangesin
realizedloyaltybehavior.
3.7 Synthesis across the six studies
The six studies build a cumulative rather than a repetitive case
across three stages of evidence. Studies 1 and 2 established the
memory-cue pattern, and Study 2 produced same-session indirect
associations consistent with the proposed MBF account. Study 3
showed that the penalty diﬀered across two complete scenario
packagesbutdidnotidentifysensitivityastheresponsibleattribute.
Study4showedthatthespeciﬁcdashboardtesteddidnotselectively
attenuatethepenalty.Studies5and6extendedtheanalysisbeyond
immediate trust to data-sharing engagement and downstream
intentions,withprivacytrustincludedasanintermediateappraisal
intheStudy6same-sessionmodel.
The principal and most consistent ﬁnding across studies is
thecontrastbetweenthecompleterelevant-memoryandintrusive-
memorycuepackages.ThiscontrastwasreliablefortrustinStudies
1–4,fordata-sharingandrelationalengagementinStudy5,andfor
loyaltyandopt-inintentionsinStudy6;itwasnotreliableforStudy
1 purchase intention or Study 5 transactional engagement, whose
omnibus tests were also null (Table3; SupplementaryTableS8 ).
Relevant memory was at least as favorable as no memory, which
was at least as favorable as intrusive memory, for every outcome,
but the reliable pairwise comparisons with no memory varied
across studies. A relevant-memory beneﬁt was reliable for Study
1 trust and continued use, both Study 3 scenarios, Study 4 trust,
Study 5 data-sharing and relational engagement, and Study 6 opt-
in intention. An intrusive-memory penalty was reliable for Study
2 trust, the Study 3 sleep-health scenario, Study 4 trust, Study 5
relational engagement, and Study 6 opt-in intention. Thus, both
components were reliable simultaneously only for the Study 3
sleep-healthscenario,Study4trust,Study5relationalengagement,
and Study 6 opt-in intention. The personalization beneﬁt and the
intrusion penalty should therefore not be regarded as uniformly
establishedrelativetonomemory.
Two qualiﬁcations limit what the principal contrast can carry.
First, given the descriptive ordering relevant > no memory >
intrusive, the relevant-vs.-intrusive comparison spans the two
extremes and, by construction, is the largest of the three pairwise
Frontiersin Psychology 11 frontiersin.org

Huang et al. 10.3389/fpsyg.2026.1934857
TABLE 3 Relevant-vs.-intrusive contrastsfor the principal outcomes.
Study Outcome Relevant minus intrusive Qualiﬁcation
1 Trust;continueduse 0.51,p = 0.003;0.36, p = 0.040 Purchaseintentionwasnotreliable(0.28, p = 0.148)
2 Trust 0.90,p < 0.001 Relevantvs.nomemorywasnotreliable( p = 0.076)
3 Trust:apparel;sleephealth 0.92,p < 0.001;1.68, p < 0.001 Completescenariosdiﬀeredonmultipleattributes
4 Trust(pooledacrossdashboard) 0.83,p < 0.001 Noselectiveattenuationbythetesteddashboard
5 Data-sharing;relationalengagement 0.94,p < 0.001;0.74, p < 0.001 Transactionalengagementwasnotreliable(0.28, p = 0.121)
6 Loyalty;opt-inintention 0.56,p < 0.001;0.75, p < 0.001 Loyaltycomparisonswithnomemorywerenotreliable
Positivediﬀerencesindicatehigherscoresundertherelevant-memorycuepackage.Pairwise pvaluesareTukey-adjusted.
diﬀerences; it is correspondingly the best powered, so part of its
greater consistency is a mechanical consequence of the ordering
rather than independent evidence. Second, because it combines
the two components, it is silent about their separate magnitudes: a
reliablerelevant-vs.-intrusivediﬀerenceiscompatiblewithabeneﬁt
alone,apenaltyalone,orboth.Wereportthedecompositionabove
andin SupplementaryTableS8 preciselysothatthiscontrastisnot
read as establishing either component on its own.Table2 reports
eachdesignatedhypothesistestandoutcome,and Table4 describes
therelationsamongconstructs.
4 Discussion
Acrossthesixstudies,completerelevant-memorycuepackages
were generally evaluated more favorably than intrusive-memory
cuepackages,withnomemorytypicallyfallingbetweenthem.This
pattern is consistent with, but does not establish, a contextual
account in which consumers evaluate remembered information
in relation to the current interaction. General preferences for
personalization, usefulness, less sensitive data use, or reduced
surveillance may also contribute, as the packages varied in topical
relevance, sensitivity, perceived usefulness, information source,
and implied surveillance. The relevant-memory beneﬁt and the
intrusive-memory penalty relative to no memory varied across
studies. The complete sleep-health scenario produced a larger
intrusive-memory penalty than the apparel scenario, but the
attribute responsible was not identiﬁed. Data-sharing engagement
was more responsive than transactional engagement, primarily
because relevant memory increased data-sharing engagement
(Zhuetal., 2025). The speciﬁc dashboard tested increased average
trust but did not selectively alter the eﬀect of memory type.
Throughout, the evidence concerns simulated claims of memory
delivered in a single session rather than genuine retrieval of
previouslydisclosedinformation.
4.1 Theoretical contributions
The ﬁndings make three related but preliminary theoretical
contributions. First, they connect simulated memory-cue packages
with consumer trust and engagement outcomes. This extends
agent-memory research that has concentrated on usability
and privacy expectations (Jonesetal., 2025 ; Zhangetal., 2025 ;
MekioussaMalki, 2026 ). Second, MBF oﬀers an interaction-
speciﬁc framing of the personalization-privacy paradox
(AwadandKrishnan, 2006 ; Xuetal., 2011 ; Norbergetal., 2007 ).
The relative weight of personalization beneﬁt and privacy risk may
depend on whether consumers regard a particular use of memory
as appropriate in the exchange. This interpretation accords with
evidence that privacy judgments change with context and framing
(Acquistietal., 2015; Adjeridetal., 2019). It also responds to calls
tostudytheparadoxinspeciﬁccontexts( Maoetal.,2026 ).
Third, MBF provides a preliminary measurable consumer
appraisal informed by contextual integrity (Nissenbaum, 2010).
It oﬀers one candidate account of why cross-context information
reuse may be associated with lower trust, even when the
recommendation is useful. Across Study 2 and the validation
sample, MBF explained roughly twenty percentage points of
additional variance in trust beyond the adjacent appraisals
measured alongside it. Because all of these measures were
self-reported in the same session, part of that increment
reﬂects common-method variance rather than construct-speciﬁc
information. This supports a limited measurement claim, not
a claim of identifying a psychological mechanism. The present
evidence does not separate MBF from perceived usefulness,
creepiness,intrusiveness,informationrelevance,ornormviolation,
none of which were measured. This boundary is especially
important because the cue packages also diﬀered in topical
relevance, sensitivity, potential perceived usefulness, information
source,andimpliedsurveillance.Theframeworkmayalsoconnect
memory design with consumer autonomy over personal data
(Andréetal., 2018 ) and connected objects that retain data during
ongoinguse( HoﬀmanandNovak,2018 ).
4.2 Design implications
The ﬁndings suggest that memory may aﬀect the user-facing
relationship and therefore should not be considered solely a
backend capability. They motivate testing whether systems beneﬁt
from distinguishing memories that serve the current task from
sensitive information carried over from another context, and from
informing users why a recommendation appeared. Conservative
defaults in health, ﬁnance, and identity-related settings remain a
design proposition that requires direct evaluation with genuine
persistentmemory.
Study 4 provides evidence only about the speciﬁc dashboard
implementation tested. It increased average trust but did not
Frontiersin Psychology 12 frontiersin.org

Huang et al. 10.3389/fpsyg.2026.1934857
TABLE 4 Constructinterpretationacross studies.
Construct Conceptual role Distinction from adjacent constructs Main studies
MemoryboundaryFit Fitbetweenremembered
contentandthecontextual
boundary
Preliminaryoperationalization,narrowerthangeneralprivacyconcernand
conceptuallydiﬀerentiatedfromtaskusefulness.Inthecompetitive
indirect-associationmodel,onlyMBFretainedareliableindirectassociation
whenMBF,warmth,andsurveillanceconcernwereenteredjointly,anddirect
bootstrapcontrastsconﬁrmthatitsspeciﬁcindirectassociationexceedseach
competitor’s(SupplementaryTableS7 ).Thevalidationsamplesupports
reliabilityandfactorialseparationfrommeasuredconstructs
(SupplementaryTableS5 ).MBFexplains /Delta1R2 ≈ 0.20ofadditionalvariancein
trustoverthemeasuredappraisals,thoughsame-sessionself-reportinﬂatesthis
increment(SupplementarynoteS15 ).Empiricalseparationfromusefulness,
creepiness,intrusiveness,relevance,andnormviolationremainsuntested
(SupplementarynoteS16 );nocausal-mechanismclaimismade
1,2,4–6;validation
sample
Privacytrust Conﬁdenceintheplatform’s
informationpractices
Targetsplatforminformationhandlingratherthantheﬁtofasingleremembered
item;includedasanintermediatevariableinthesame-sessionserial
indirect-associationmodel
6
Surveillanceconcern Concernthatmemoryreﬂects
monitoring
Anaﬀectivemonitoringappraisalratherthanacontextualﬁtjudgment;
correlatedwithMBF( r =− 0.55)butdidnotretainareliableindirectassociation
inthecompetitivemodel( SupplementaryTableS7 )
2
Memorycontrol Visiblecontrolstoinspect,
edit,ordeletememory
AspeciﬁcinterfaceaﬀordancetestedinStudy4,notevidenceaboutusercontrol
generally
4
Data-sharing
engagement
Willingnesstoauthorize
additionalinformationuse
Adownstreambehavioralintention,moresensitivetomemorytypethan
transactionalengagement(Study5within-personcontrast)
5
Loyaltyintention Intendedcontinuationofthe
relationshipwiththeinterface
Asame-sessionintentionincludeddownstreamofprivacytrustinan
associationalserialmodel
6
improve MBF or selectively reduce the intrusive-memory penalty.
An inspect-edit-delete dashboard may signal procedural control
without altering the judgment of a speciﬁc memory cue, but other
forms,strengths,ortimingofcontrolmayproducediﬀerentresults.
Moreover, without a perceived-control manipulation check, we
cannot determine whether participants experienced the interface
as providing meaningful control. The null interaction therefore
should not be interpreted as showing that editable control is
generally ineﬀective. At most, the ﬁndings motivate treating
memory selection and user control as complementary design
questions for future testing. Prior research similarly ﬁnds that
control and trust-building measures can reduce but not eliminate
negative reactions to data collection (Aguirreetal., 2015 ; Tucker,
2014).
4.3 Managerial and policy implications
Because the evidence derives from brief simulated interactions
in a single national context and relies predominantly on self-
reported intentions, the following implications are oﬀered as
tentative directions rather than prescriptions. For managers, the
results caution against assuming that greater memory visibility
will always improve personalization. The ﬁndings motivate testing
recency, relevance, user expectations, and memory governance in
real-world systems. Trust and data-sharing measures may reveal
costs that conversion rates alone miss. The larger penalty in the
complete sleep-health scenario suggests that uniform memory
policies may perform diﬀerently across categories, but the present
study cannot support category-speciﬁc prescriptions or attribute
thediﬀerencetosensitivity.Replicationwithmatchedmemorycues
isrequired.
Data protection rules that focus on collection and consent
may not capture every harmful use. Information can be lawfully
collected and later reused in ways that violate situational
expectations. Regulators and platform auditors could assess
contextual reuse alongside collection practices. Relevant criteria
include memory persistence, default retention, and cross-
application transfer. These policy directions are normatively
motivated extensions of the ﬁndings rather than empirically
tested prescriptions; the studies did not examine legal compliance,
consentbehavior,orreal-worlddataﬂows.
4.4 Construct boundaries
The supplemental validation sample distinguished MBF from
general privacy concern, surveillance concern, relational warmth,
and trust (SupplementaryTableS5 ). In Study 2, MBF retained a
reliable speciﬁcindirect association when warmth and surveillance
concern were entered into the same model, and bootstrap
contrasts placed it above each of them (SupplementaryTableS7 ).
These results concern measured covariance and do not identify
causalordering.
Frontiersin Psychology 13 frontiersin.org

Huang et al. 10.3389/fpsyg.2026.1934857
Two-sample tests also allow a direct incremental-validity
test against the adjacent appraisals measured concurrently
(SupplementarynoteS15 ). In Study 2, entering MBF after
relational warmth and surveillance concern increased the
variance explained by trust from R2 = 0.13 to R2 = 0.33
(/Delta1R2 = 0.199, F(1,285) = 84.30, p < 0.001). In the validation
sample, entering MBF after IUIPC privacy concern, warmth, and
surveillanceconcernincreased R2 from0.26to0.46( /Delta1R2 = 0.200,
F(1,229) = 84.33, p < 0.001). In Study 2, reverse-order checks
showed that warmth and surveillance concern each added only
/Delta1R2 < 0.001 after MBF (bothp = 0.854); the archived validation
analysis reports the corresponding reverse-order check only for
surveillance concern (/Delta1R2 = 0.001, p = 0.465). The primary
incremental results indicate that MBF contributed information
beyondthemeasuredappraisalsetineachsample,whileleavingits
distinctionfromtheunmeasuredalternativesunresolved.
These ﬁndings support MBF only as a preliminary, context-
speciﬁc operationalization of remembered-content evaluation.
They do not establish empirical separation from perceived
usefulness, creepiness, intrusiveness, information relevance, or
perceived norm violation because the studies did not measure
these alternatives directly. SupplementarynoteS16 presents a
systematic conceptual comparison of MBF with each of these
neighbors, specifying for each the judgment it targets, the point
at which it should diverge from MBF, and the measurement that
would adjudicate between them. A remembered detail may be
useful yet inappropriate, or unobjectionable yet of little value.
Related research has examined boundary crossing in personalized
advertising (Boermanetal., 2021 ) and creepiness in data-driven
personalization (TeneandPolonetsky, 2014 ; Petrovaetal., 2026 ).
Communication privacy management ( Petronio, 2002, 2013),
expectancy-violation theory (Burgoon, 1993), and research on
perceivedintrusiveness( Edwardsetal.,2002 )eachoﬀeracandidate
account of the same reaction. Discriminating MBF from these
accounts requires measuring them alongside MBF, which the
present studies did not do. The present manuscript therefore
does not claim that MBF is an established or distinctive
psychological mechanism; that question requires new data
with matched manipulations, independent checks, and separate
measurementoccasions.
4.5 Limitations and future research
Theindirect-associationmodelsusedmeasurescollectedwithin
the same session, so the intermediate-to-outcome paths remain
correlational and may reﬂect common-method variance, reverse
ordering,consistencybias,orconceptualoverlap,eventhoughMBF
was measured before the outcomes. MBF also served as both the
manipulation check and the intermediate variable, so the indirect
associations may partly reﬂect semantic correspondence between
thecuepackagesandtheMBFitems.Intheno-memorycondition,
participants evaluated MBF despite the absence of remembered
content; the primary models therefore used dummy coding, and
we do not interpret that condition’s MBF score as an intermediate
levelofﬁt.Thecompletecuepackagesdiﬀeredintopicalrelevance,
information sensitivity, perceived usefulness, information source,
and implied surveillance. Therefore, the design cannot isolate
contextual ﬁt, or any other single attribute, as the causal feature.
In Study 3, product context, recommendation content, and cue
wordingchangedtogether,preventingattributionoftheinteraction
toinformationsensitivity.Constructvalidationwasconductedina
supplementalsampleratherthanwithineachexperimentalsample.
In that sample, the three-item scale met conventional reliability
anddiscriminant-validitythresholdsonlybymodestmargins,with
unevenitemloadings.Itsseparationfromtrustistheweakest:after
attenuationcorrection,thetwoconstructsshareroughlytwo-thirds
oftheirreliablevariance,soMBFisbesttreatedasadistinguishable
but closely related antecedent of trust rather than a clearly
independent construct. The scale therefore requires reﬁnement
before it can carry heavier inferential weight. Future studies
should use orthogonal matched manipulations, independent
manipulation checks, separated measurement occasions, and
behavioral permission decisions. The present studies measured
willingness to share data and opt-in intentions rather than
actualchoices.
Generalizationislimitedbyrecruitmentatandaroundasingle
Chinese institution. Because participation was anonymous, we
also cannot rule out that some individuals took part in more
than one study. Privacy boundaries may vary across cultural
and regulatory settings. Across the original one-experimental-
test-per-study family, η2 p ranged from 0.002 to 0.13; the reliable
eﬀects ranged from 0.02 to 0.13 and were small to moderate. A
single exposure should not be interpreted as producing a large
behavioralchange.
The studies examined brief interactions with text-based
assistants and simulated memory cues. Participants had no
established relationship with the assistant, and the study did not
assess suspicion or cover-story credibility; some participants may
have viewed the memory references as fabricated or inaccurate.
Conclusions therefore pertain to responses to simulated memory
claims rather than to persistent memory of genuinely disclosed
information.Researchusinggenuinelyretainedinformationacross
repeated sessions is needed to examine memory accumulation,
decay,anduser-vs.system-initiatedretention.
5C o n c l u s i o n
Across six controlled single-session chat experiments using
simulated memory cues, the principal and most consistent ﬁnding
was that complete relevant-memory cue packages produced
more favorable trust-related outcomes than intrusive-memory
cue packages. Comparisons with no memory varied across
studies. The complete sleep-health scenario produced a larger
intrusive-memory penalty than the apparel scenario, although
multiple scenario characteristics changed together. Data-sharing
engagement was more responsive than transactional engagement,
primarily through a relevant-memory beneﬁt. The speciﬁc editable
dashboard tested raised average trust but did not selectively reduce
theintrusive-memorypenaltyorimproveMBF.
Together, the ﬁndings support contextual appropriateness as
a candidate design consideration alongside retrieval accuracy,
usefulness,andusercontrol.Theevidenceremainslimitedbyshort
interactions, simulated composite cues, and predominantly self-
reported outcomes. Whether the same pattern holds for genuine
Frontiersin Psychology 14 frontiersin.org

Huang et al. 10.3389/fpsyg.2026.1934857
persistent memory, repeated interactions, behavioral choices, or
otherformsofusercontrolremainstobeestablished.
Data availability statement
The datasets presented in this study can be found in
online repositories. The names of the repository/repositories and
accession number(s) can be found below: https://github.com/
RunhuaHuang/aimemory.
Ethics statement
The studies involving humans were approved by Institutional
Review Board of Zhejiang Business College. The studies were
conductedinaccordancewiththelocallegislationandinstitutional
requirements. The participants provided their written informed
consent to participate in this study. Written informed consent
was obtained from the individual(s) for the publication of any
potentiallyidentiﬁableimagesordataincludedinthisarticle.
Author contributions
RH: Conceptualization, Supervision, Writing – original draft,
Writing – review & editing, Formal analysis, Visualization.
YH: Data curation, Formal analysis, Methodology, Project
administration, Supervision, Writing – original draft, Writing
– review & editing, Conceptualization. HG: Data curation,
Methodology, Supervision, Writing – original draft, Writing –
review&editing,Investigation.
Funding
The author(s) declared that ﬁnancial support was not received
forthisworkand/oritspublication.
Conﬂict of interest
The author(s) declared that this work was conducted in the
absence of any commercial or ﬁnancial relationships that could be
construedasapotentialconﬂictofinterest.
Generative AI statement
The author(s) declared that Generative AI was used in the
creation of this manuscript. A large language model (gemini-3-
ﬂash) delivered the experimental stimuli under the constrained
prompting procedure described in the Materials and methods.
It was not used to generate, analyze, or interpret the research
data.GenerativeAItoolsusedduringmanuscriptpreparationwere
limited to language editing. The author(s) reviewed and take full
responsibilityforallcontent.
Any alternative text (alt text) provided alongside ﬁgures in
this article has been generated by Frontiers with the support of
artiﬁcial intelligence and reasonable eﬀorts have been made to
ensureaccuracy,includingreviewbytheauthorswhereverpossible.
Ifyouidentifyanyissues,pleasecontactus.
Publisher’s note
All claims expressed in this article are solely those of the
authors and do not necessarily represent those of their aﬃliated
organizations, or those of the publisher, the editors and the
reviewers. Any product that may be evaluated in this article, or
claim that may be made by its manufacturer, is not guaranteed or
endorsedbythepublisher.
Supplementary material
The Supplementary Material for this article can be found
online at: https://www.frontiersin.org/articles/10.3389/fpsyg.2026.
1934857/full#supplementary-material
References
Acquisti,A.,Brandimarte,L.,andLoewenstein,G.(2015).Privacyandhumanbehavior
intheageofinformation. Science347,509–514.doi:10.1126/science.aaa1465
Acquisti,A.,Taylor,C.,andWagman,L.(2016).Theeconomicsofprivacy. J.Econ.Lit .
54,442–492.doi:10.1257/jel.54.2.442
Adjerid,I.,Acquisti,A.,andLoewenstein,G.(2019).Choicearchitecture,framing,and
cascadedprivacychoices. Manage. Sci.65,2267–2290.doi:10.1287/mnsc.2018.3028
Aguirre, E., Mahr, D., Grewal, D., de Ruyter, K., and Wetzels, M. (2015).
Unraveling the personalization paradox: the eﬀect of information collection and
trust-building strategies on online advertisement eﬀectiveness.J. Retail. 91, 34–49.
doi:10.1016/j.jretai.2014.09.005
André, Q., Carmon, Z., Wertenbroch, K., Crum, A., Frank, D., Goldstein, W., et al.
(2018).Consumerchoiceandautonomyintheageofartiﬁcialintelligenceandbigdata.
Cust.NeedsSolut .5,28–37.doi:10.1007/s40547-017-0085-8
Awad, N. F., and Krishnan, M. S. (2006). The personalization privacy paradox:
an empirical evaluation of information transparency and the willingness to
be proﬁled online for personalization. MIS Q . 30, 13–28. doi: 10.2307/251
48715
Bano, S., Sarfraz, U., Salameh, A. A., and Jan, A. (2022). COVID-19 paradox:
the role of privacy concerns and ad intrusiveness on consumer’s attitude
toward app usage behavior. Front. Psychol. 13:836060. doi: 10.3389/fpsyg.2022.
836060
Blut, M., Wang, C., Wünderlich, N. V., and Brock, C. (2021). Understanding
anthropomorphism in service provision: a meta-analysis of physical robots,
chatbots, and other ai.J. Acad. Market. Sci. 49, 632–658. doi: 10.1007/s11747-020-
00762-y
Boerman, S. C., Kruikemeier, S., and Bol, N. (2021). When is personalized advertising
crossingpersonalboundaries?howtypeofinformation,datasharing,andpersonalized
Frontiersin Psychology 15 frontiersin.org

Huang et al. 10.3389/fpsyg.2026.1934857
pricing inﬂuence consumer perceptions of personalized advertising.Comput. Hum.
Behav.Rep.4:100144.doi:10.1016/j.chbr.2021.100144
Brislin,R.W.(1970).Back-translationforcross-culturalresearch. J.CrossCult.Psychol .
1,185–216.doi:10.1177/135910457000100301
Burgoon,J.K.(1993).Interpersonalexpectations,expectancyviolations,andemotional
communication.J.Lang.Soc.Psychol .12,30–48.doi:10.1177/0261927X93121003
Castelo, N., Bos, M. W., and Lehmann, D. R. (2019). Task-dependent algorithm
aversion.J.Market.Res .56,809–825.doi:10.1177/0022243719851788
Culnan, M. J., and Armstrong, P. K. (1999). Information privacy concerns, procedural
fairness, and impersonal trust: an empirical investigation.Organ. Sci. 10, 104–115.
doi:10.1287/orsc.10.1.104
Dinev, T., and Hart, P. (2006). An extended privacy calculus model for e-commerce
transactions.Inf.Syst.Res .17,61–80.doi:10.1287/isre.1060.0080
Edwards, S. M., Li, H., and Lee, J.-H. (2002). Forced exposure and psychological
reactance:antecedentsandconsequencesoftheperceivedintrusivenessofpop-upads.
J.Advert.31,83–95.doi:10.1080/00913367.2002.10673678
Gefen,D.,Karahanna,E.,andStraub,D.W.(2003).Trustandtaminonlineshopping:
anintegratedmodel. MISQ.27,51–90.doi:10.2307/30036519
Glikson,E.,andWoolley,A.W.(2020).Humantrustinartiﬁcialintelligence:reviewof
empiricalresearch. Acad.Manage.Ann .14,627–660.doi:10.5465/annals.2018.0057
Hayes, A. F., and Preacher, K. J. (2014). Statistical mediation analysis with a
multicategorical independent variable. Br. J. Math. Stat. Psychol . 67, 451–470.
doi:10.1111/bmsp.12028
Hildebrand, C., and Bergner, A. (2021). Conversational robo advisors as surrogates
of trust: onboarding experience, ﬁrm perception, and consumer ﬁnancial
decision making. J. Acad. Market. Sci . 49, 659–676. doi: 10.1007/s11747-020-
00753-z
Hoﬀman, D. L., and Novak, T. P. (2018). Consumer and object experience in the
internet of things: an assemblage theory approach.J. Consum. Res. 44, 1178–1204.
doi:10.1093/jcr/ucx105
John, L. K., Acquisti, A., and Loewenstein, G. (2011). Strangers on a plane: context-
dependent willingness to divulge sensitive information.J. Consum. Res. 37, 858–873.
doi:10.1086/656423
Jones, B., Stemmler, K., Su, E., Kim, Y.-H., and Kuzminykh, A. (2025). “Users’
expectationsandpracticeswithagentmemory,”in Proceedingsoftheextendedabstracts
of the CHI conference on human factors in computing systems(New York, NY: ACM),
1–8.doi:10.1145/3706599.3720158
Komiak, S. Y. X., and Benbasat, I. (2006). The eﬀects of personalization and
familiarity on trust and adoption of recommendation agents.MIS Q. 30, 941–960.
doi:10.2307/25148760
Komiak, S. Y. X., and Benbasat, I. (2008). A two-process view of trust and distrust
building in recommendation agents: a process-tracing study.J. Assoc. Inf. Syst.9 ,
727–747.doi:10.17705/1jais.00180
Liang, F., Paulo, R., Molina, G., Clyde, M. A., and Berger, J. O. (2008). Mixtures
of g priors for Bayesian variable selection. J. Am. Stat. Assoc . 103, 410–423.
doi:10.1198/016214507000001337
Longoni,C.,Bonezzi,A.,andMorewedge,C.K.(2019).Resistancetomedicalartiﬁcial
intelligence.J.Consum.Res .46,629–650.doi:10.1093/jcr/ucz013
Malhotra, N. K., Kim, S. S., and Agarwal, J. (2004). Internet users’ information privacy
concerns (IUIPC): The construct, the scale, and a causal model.Inf. Syst. Res. 15,
336–355.doi:10.1287/isre.1040.0032
Mao, K., Cui, R., and Wang, Z. (2026). Contextualizing the privacy paradox–a risk-
beneﬁt analysis of generation z’s adoption intentions toward AI-based virtual try-on.
Front.Psychol.17:1773754.doi:10.3389/fpsyg.2026.1773754
Martin,K.D.,andMurphy,P.E.(2017).Theroleofdataprivacyinmarketing. J.Acad.
Market. Sci.45,135–155.doi:10.1007/s11747-016-0495-4
McKnight, D. H., Choudhury, V., and Kacmar, C. (2002). Developing and validating
trust measures for e-commerce: an integrative typology.Inf. Syst. Res. 13, 334–359.
doi:10.1287/isre.13.3.334.81
MekioussaMalki,L.(2026).“Towardsusable,privacyrespectinglong-termmemoryfor
llm-based conversational agents,” inProceedings of the extended abstracts of the 2026
CHI conference on human factors in computing systems(New York, NY: ACM), 1–5.
doi:10.1145/3772363.3799198
Nissenbaum, H. (2010). Privacy in Context: Technology, Policy, and the Integrity
of Social Life . Stanford, CA: Stanford University Press. doi: 10.1515/9780804
772891
Norberg, P. A., Horne, D. R., and Horne, D. A. (2007). The privacy paradox: personal
information disclosure intentions versus behaviors. J. Consum. Aﬀ. 41, 100–126.
doi:10.1111/j.1745-6606.2006.00070.x
Pavlou, P. A. (2003). Consumer acceptance of electronic commerce: integrating trust
and risk with the technology acceptance model.Int. J. Electron. Commer. 7, 101–134.
doi:10.1080/10864415.2003.11044275
Petronio, S. (2002).Boundaries of Privacy: Dialectics of Disclosure.A l b a n y ,N Y :S t a t e
UniversityofNewYorkPress.doi:10.1353/book4588
Petronio,S.(2013).Briefstatusreportoncommunicationprivacymanagementtheory.
J.Fam.Commun .13,6–14.doi:10.1080/15267431.2013.743426
Petrova, A. Malär, L., Hoyer, W., and Krohmer, H. (2026). The phenomenon
of creepiness in a digital marketing world. Psychol. Market. 43, 834–851.
doi:10.1002/mar.70089
Puntoni, S., Reczek, R. W., Giesler, M., and Botti, S. (2021). Consumers
and artiﬁcial intelligence: an experiential perspective. J. Mark. 85, 131–151.
doi:10.1177/0022242920953847
Rouder, J. N., Morey, R. D., Speckman, P. L., and Province, J. M. (2012).
Default Bayes factors for ANOVA designs. J. Math. Psychol . 56, 356–374.
doi:10.1016/j.jmp.2012.08.001
Smith, H. J., Milberg, S. J., and Burke, S. J. (1996). Information privacy:
measuring individuals’ concerns about organizational practices.MIS Q. 20, 167–196.
doi:10.2307/249477
Tene, O., and Polonetsky, J. (2014). A theory of creepy: technology, privacy, and
shiftingsocialnorms. YaleJ.LawTechnol .16,59–102.doi:10.2139/ssrn.2326830
Tucker,C.E.(2014).Socialnetworks,personalizedadvertising,andprivacycontrols. J.
Mark. Res.51,546–562.doi:10.1509/jmr.10.0355
Wagenmakers, E.-J. (2007). A practical solution to the pervasive problems of p values.
Psychon.Bullet.Rev .14,779–804.doi:10.3758/BF03194105
Wang, W., and Benbasat, I. (2005). Trust in and adoption of online recommendation
agents.J.Assoc.Inf.Syst .6,72–101.doi:10.17705/1jais.00065
Xu, H., Luo, X. R., Carroll, J. M., and Rosson, M. B. (2011). The personalization
privacy paradox: an exploratory study of decision making process for location-aware
marketing.Decis.SupportSyst .51,42–52.doi:10.1016/j.dss.2010.11.017
Yeomans, M., Shah, A., Mullainathan, S., and Kleinberg, J. (2019). Making sense of
recommendations.J.Behav.Decis.Mak .32,403–414.doi:10.1002/bdm.2118
Zhang, S., Ma, R., Ma, Y., Li, S., Xu, Y., Yi, X., et al. (2025). “Understanding users’
privacy perceptions towards LLM’s RAG-based memory,” inProceedings of the 2025
workshop on human-centered AI privacy and security(New York, NY: ACM), 10–19.
doi:10.1145/3733816.3760750
Zhu, L., Zhang, C., Omar, B., Qi, F., and Ji, H. (2025). Privacy threats versus trust:
a behavioral decision approach to social media disclosure intention.Front. Psychol.
16:1609012.doi:10.3389/fpsyg.2025.1609012
Frontiersin Psychology 16 frontiersin.org
