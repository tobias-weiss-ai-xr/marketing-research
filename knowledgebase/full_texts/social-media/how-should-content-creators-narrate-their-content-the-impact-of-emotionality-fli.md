---
title: How Should Content Creators Narrate Their Content? The Impact of Emotionality Flips on Audience
  Engagement
url: https://doi.org/10.2139/ssrn.6135287
category: social-media
subcategory: case-study
date: 2026-01
venue: SSRN Electronic Journal
authors:
- Hesam Ghasemi
- Vivek Astvansh
- Amir Sepehri
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s11747-026-01147-3.pdf
pages: 21
chars: 109765
fetched_at: '2026-11-08T17:04:23+00:00'
kb_version: 1
---

# How Should Content Creators Narrate Their Content? The Impact of Emotionality Flips on Audience Engagement

ORIGINAL EMPIRICAL RESEARCH
Journal of the Academy of Marketing Science (2026) 54:1080–1100
https://doi.org/10.1007/s11747-026-01147-3
Introduction
The creator1economy refers to “a space where individuals,
known as creators, generate income through producing and
sharing original content, products, or services on digital
platforms” (Peres et al., 2024, p.1). It includes influencers,
podcasters, video creators, bloggers, and live streamers. The
creator economy is valued at $192  billion in 2025 (Kumar
2025) and projected to reach nearly half a trillion U.S. dol -
lars by 2027 (Goldman Sachs 2023), with a cumulative
average growth rate of 23% (Kumar 2025). The economy
boasts 207 million creators globally (Kumar 2025), result-
ing in 1.5  million digital creator jobs in the United States
alone in 2024 (Fischer 2025). These statistics highlight the
need for research on the creator economy.
1  A creator is an individual or an organization who produces content,
often with the aim of generating revenue through audience engage -
ment with the content (Kozinets et al., 2023).
2  Influencers are individuals who turn their online followers into a
target audience for marketing messages in exchange for compensa -
tion from firms (Mardon et al., 2023). Influencer marketing involves
a firm selecting and incentivizing influencers to engage their follow -
ers on social media, leveraging the unique resources these influencers
 Michael Haenlein served as guest editor for this article.
  Vivek Astvansh
vivek.astvansh@mcgill.ca
Hesam Ghasemi
mohammadhesam.hajighasemi@essec.edu
Amir Sepehri
sepehri@essec.edu
1 Department of Marketing, ESSEC Business School, 3 Av.
Bernard Hirsch, Cergy 95000, France
2 Marketing Area, Desautels Faculty of Management, McGill
University, 1001 Rue Sherbrooke O, Montreal,
QC H3A 1G5, Canada
3 Academic Director, Bensadoun School of Retail
Management, McGill University, 1001 Rue Sherbrooke O,
Montreal, QC H3A 1G5, Canada
4 Department of Informatics, Luddy School of Informatics,
Computing, and Engineering, Indiana University,
Bloomington, IN 47408, USA
5 Environmental Resilience Institute, Indiana University,
Bloomington, IN 47405, USA
Abstract
The creator economy marks a pivotal shift in influencer marketing. Content creators create long content to engage their
audience on social media platforms and generate revenue through engagement. We hypothesize that audience engagement
with content is a function of emotionality flips: the number of times emotionality flips direction (from a positive slope to
a negative slope and vice versa) from one content unit (e.g., sentence) to another. Five studies—including 33,598 podcast
episodes, 3,381 TED Talks, two lab experiments, and one synthetic validation—support this hypothesis. Furthermore,
arousal is the underlying mechanism; that is, emotionality flips raise the audience’s arousal, which in turn boosts audience
engagement. Lastly, emotionality flips’ positive effect is stronger for (1) content that is easier (vs. harder) to process, and
(2) audiences with high (vs. low) need-for-affect. This research advances understanding of emotionality dynamics in the
creator economy and offers insights for creators, platforms, and consumers.
Keywords Influencers · Natural language processing  · Automated text analysis  · Narrative transportation  · Digital
opinion leaders
Received: 4 January 2025 / Accepted: 25 January 2026 / Published online: 15 April 2026
© The Author(s) 2026
How should content creators narrate their content? The impact of
emotionality flips on audience engagement
Hesam Ghasemi1  · Vivek Astvansh3,4,5,2  · Amir Sepehri1
1 3
On the surface, the creator economy term broadens influ-
encer marketing 2 in two ways. First, the prefix “creator”

Journal of the Academy of Marketing Science (2026) 54:1080–1100
emotionality flips increase audience engagement with nar -
rative content. We reason that longer content is more likely
to regress to the mean in emotionality, as more emotional
sentences will be canceled out by less emotional ones, ren -
dering the “average” emotionality less insightful.
Regression analyses of 33,598 YouTube podcast episodes
published between 2019 and 2024 (Study 1) and 3,381 TED
Talks published between 2006 and 2020 (Study 2) support
the hypothesized association. Two lab experiments (Stud -
ies 3 and 4) provide causal evidence, and one synthetic
study (Study 5) validates the robustness of the findings. The
key insight is that what drives audience engagement with
long-form narratives is not simply the emotional valence or
intensity, but rather the number of shifts—or flips—in emo-
tionality valence throughout the content. Moreover, Studies
1 and 2 demonstrate a moderating effect of narrative flu -
ency, Study 3 clarifies that arousal is an underlying psycho-
logical mechanism, and Study 4 establishes the moderating
role of consumers’ Need for Affect (NFA).
Our research makes three contributions. First, it advances
work on audience engagement in the creator economy
(Rizzo et al., 2023a; Rizzo et al., 2023b; Goldenberg et al.,
2023; Gu et al., 2024; Lanz et al., 2024; Leung et al., 2022a,
b; Mosley et al., 2024; see Web Appendix A, Table A1 for
a summary of representative research) by showing that
beyond emotional valence and intensity, changes in emo -
tionality over the course of a narrative meaningfully shape
engagement in long-form content. Second, it contributes to
narrativity research (Hamby & Escalas, 2024; Herzenstein
et al., 2011; van Laer et al., 2014; Laer et al., 2019; see Web
Appendix A, Table A2 for a summary of representative
research) by positioning emotionality flips as a discourse-
level feature (i.e., how a content is expressed; Chatman,
1978; Culler, 1981) that introduces emotional dynamics
into messages and facilitates narrative persuasion (Argo et
al., 2008; Escalas, 2007). Third, it offers practical implica -
tions: creators can use emotionality flips to enhance engage-
ment, platforms may integrate them into recommendation
systems, and consumers can leverage emotional variability
to enrich affective experiences.
Narrativity in content
Content creators can persuade the audience through narra-
tive transportation—“the degree to which (1) a consumer
empathizes with the story’s characters and (2) the plot stim-
ulates consumers’ imagination, causing them to temporar -
ily experience a suspension of reality during the story” (van
Laer et al., 2014, pp. 799–800; see also Escalas, 2007; Green
& Brock, 2000; Hamby & Brinberg, 2016). By immersing
1 3
1081
replaces the word “influencer” and thus overcomes the
negative connotation of influencing/persuading others
(Campbell & Kirmani, 2000). Second, the suffix “econ -
omy” reminds stakeholders of the economic significance of
the created content rather than limiting their view of it as
just another marketing activity. Interestingly, this broaden -
ing of the term is also a marketing exercise, and influencer
marketing has become a key catalyst in growing the creator
economy (Kozinets et al., 2023).
On a deeper level, the creator economy characterizes a
pivotal shift in influencer marketing. It provides anyone
with internet access an unprecedented opportunity to turn
their creativity into an entrepreneurial career. This growth
reflects a significant change in content production, distri -
bution, and monetization, moving away from traditional
media platforms such as television, where media organiza -
tions mainly generate content. By the end of 2023, there
were over 1  million content creators on TikTok (Duarte
2023a), more than 23 million on Instagram (Howarth 2024),
and over 60  million on YouTube (Duarte 2023b). Unlike
their traditional media counterparts, social media platforms
enable creators to bypass gatekeepers, such as publish -
ers and broadcasters, engage directly with their audience,
and assume greater control over their content (Gardner &
Lehnert, 2016). The expanding market size of the creator
economy has attracted more content creators, driving them
to enhance content quality and narrativity to boost audi -
ence engagement (Jiang et al., 2024). What type of content
should creators produce to receive high audience engage -
ment? The success of the creator economy may hinge on the
answer to this question.
Prior research has shown that content emotionality is
a central determinant of audience engagement with tradi -
tional media (Tellis et al., 2019) and social media (Berger,
2014). Therefore, we use emotionality as our starting point.
Next, although previous research has shown that emotion -
ality drives engagement (e.g., Berger et al., 2023; Berger
& Milkman, 2012; Lee, 2021; Milkman & Berger, 2014),
academics and practitioners have paid less attention to how
and why audience engagement is a function of emotionality
flips,3 the number of times emotionality flips direction (from
a positive slope to a negative slope or vice versa) from one
unit of content (e.g., a sentence) to another (see Berger et al.,
2021 for how sentiment volatility can lead to virality). This
lack of attention motivates our research and is our point of
departure. We extend prior research by hypothesizing that
provide to promote the firm’s offerings, with the ultimate goal of
enhancing the firm’s performance (Leung et al., 2022b).
3  Emotionality pivots and emotionality reversals are practical alter -
native terms to describe similar directional changes in the emotional-
ity of a content.

Journal of the Academy of Marketing Science (2026) 54:1080–1100
themselves in a story world (Green & Brock, 2000), audi-
ences tend to process the content less critically (Adaval &
Wyer Jr., 1998; Escalas, 2007) and sense a real-life experi -
ence (Green & Brock, 2000).
The level of narrativity influences the degree to which
audiences experience narrative transportation and become
immersed in the story world (Nell, 1988). Narrativity con-
sists of two key components: (1) what is conveyed and (2)
how it is conveyed (Chatman, 1978). Differences in these
narrative elements can significantly impact transportation
into the narrative and the resulting persuasion (van Laer et
al., 2019). Narrative transportation leaves the audience with
the perception that the content creator’s story is based on
direct experience, which typically makes novel information
easier to understand and seemingly more intuitively truthful
(Marsh & Fazio, 2006). As a result, the audience tends to
engage with the story less critically and is ultimately per -
suaded by it.
However, not all content in the creator economy is
overtly narrative in form, yet “definitions of narratives
and stories are highly fluid. The most traditional assump -
tion is that a narrative consists of a series of connected
events with a clear beginning, middle, and end. Gener -
ally, a narrative is considered a superordinate construct
composed of a series of stories or events, which may be
imaginary or factual. Whereas novels and short-form fic -
tion are narratives, the factual accounts of scientific dis -
coveries are likely less story-like but are still narratives
nonetheless” (Boyd et al., 2020, p. 3). This perspective
suggests that even fact-based content (e.g., New York
Times articles, TED Talks, or U.S. Supreme Court opin -
ions) can exhibit varying degrees of narrativity, albeit
with different forms of staging, plot progression, and
cognitive tension.
Relatedly, van Laer et al. ( 2019) emphasized that nar -
rativity should be understood as a continuum rather than
a binary distinction between story and non-story. Prior
research has also distinguished between story-based and
argument-based messages, while acknowledging that
real-world content often blends both forms. Notably,
Green and Brock ( 2000) found that whether the message
was framed as fiction or fact induced neither narrative
transportation nor belief change, highlighting that how a
message is conveyed (i.e., narrative discourse) and pro -
cessed matters more than whether it is explicitly fictional.
For example, Krause-Galoni and Rucker ( 2024) showed
that embedding factual arguments in a narrative structure
can increase elaboration and persuasion without dimin -
ishing transportation. Similarly, prior research has shown
that narrativity can be present in factual content such as
online reviews (van Laer et al., 2019), advertisements
(Escalas, 2004a), and documentaries (Green, 2008).
Emotionality in content
Prior research has advised content creators to craft emo -
tional content to increase audience engagement (Berger et
al., 2021, 2023; Lee, 2021; Lin et al., 2021; Tellis et al.,
2019). For example, broadcasters should smile more dur -
ing their live broadcasts to enhance engagement (Lin et al.,
2021). Audiences engage not only by liking, commenting,
and sharing the content, but also by discussing it in sub -
sequent conversations (Berger & Milkman, 2012). Further,
audiences produce emotional content via narrative reviews
of their consumption experiences (Berger, 2014; Melumad
et al., 2019; Yin et al., 2017).
Literature on content emotionality can be organized
along two themes. The first theme relates to determinants
of the level of emotionality (low vs. high; e.g., Melumad
et al., 2019; Mosley et al., 2024), and the impacts of this
level on audience engagement (e.g., Lin et al., 2021) and
downstream marketing outcomes (e.g., Lee, 2021; van Laer
et al., 2019). For example, people generate shorter content
when using their phones (vs. computers) and therefore use
less emotional language (Melumad et al., 2019). Content
broadcasters who express happiness emotions induce hap -
piness among the audience. Thus, broadcasters can increase
audience engagement with more smiles (Lin et al., 2021).
The second theme focuses on the type of emotionality
that boosts engagement (e.g., Berger et al., 2023; Berger &
Milkman, 2012). For example, high-arousal emotions (e.g.,
awe) make content more viral due to physiological arousal
(Berger & Milkman, 2012). Anxious, exciting, and hopeful
language captures attention, whereas sad language discour-
ages it, with uncertainty and arousal playing the mediating
role (Berger et al., 2023).
The preceding discussion suggests that academics have
paid less attention to whether changes in emotionality,
rather than its valence and extremity, can affect engage -
ment. Emotionality changes are paramount to creators’ abil-
ity to engage their audience with narrative content, which
forms the creator economy’s foundation. Thus, this lack of
academic attention is consequential in advising creators of
what content to create to engage the audience. Our research
addresses this lack of attention.
Emotionality flips
We extend prior research by reasoning that audience
engagement with long narrative content (e.g., podcasts and
TED talks) is driven more by emotionality flips, the number
of times emotionality flips direction (from a positive slope
to a negative slope or vice versa) from one unit of content
(e.g., a sentence) to another. These flips may reflect dra -
matic plot twists or significant character developments. The
1 3
1082

Journal of the Academy of Marketing Science (2026) 54:1080–1100
(Kleres, 2011). Theoretically, sentences encapsulate com -
plete ideas and their corresponding emotionality, facilitat -
ing a more precise measurement of changes in emotionality
valence (Bestgen, 1994). This “completeness” is crucial for
identifying temporal changes in emotions that drive audi -
ence engagement in long narratives. Second, sentences are
typically neither too small (like a phrase), risking the loss
of context and meaning, nor too large (like a paragraph),
and may thus reveal the nuances of emotionality changes
(Gee & Grosjean, 1984). Therefore, a sentence is an ideal
unit for analyzing the complexity and development of
emotional arcs in narratives, offering a more accurate and
detailed understanding of how emotionality impacts audi -
ence engagement. Third, the natural boundaries of sen -
tences align well with how the brain processes and responds
to language, making them an adequate chunk size for study-
ing neural and psychological responses to narrative content
(Ptaszynski et al., 2013).
Consider the following example of a six-sentence seg -
ment of a podcast. The example highlights the narrativity
imperative in content.
“What happens if you leave school? You’re so excited,
school’s over. You’re walking home, just chatting with
all your friends, and all of a sudden, a complete psy -
chopath approaches you and pulls a gun on you. How
would you react? What would you do in that moment,
wondering what events are about to unfold from this
psychopath on the loose? That is the case that I am
excited to discuss today.”
Following previous research (Lacka et al., 2022; Pancer et
al., 2019), we measure each sentence’s emotionality score
using the Valence Aware Dictionary and Sentiment Rea -
soner’s (V ADER’s) compound variable because V ADER
measures the valence of words (i.e., positive, negative, and
neutral), as well as their intensity (e.g., “okay” is rated 0.9,
“good” 1.9, and “great” 3.1; Hutto & Gilbert, 2014). Our
code produces an array of six scores, one for each sentence:
[− 0.05, 0.40, 0.18, 0.0, − 0.31, 0.34]. Figure 1 shows each
sentence’s location in the narrative on the X-axis and the
sentence-specific emotionality on the Y-axis.
We are interested in counting the number of times emo -
tionality changes direction. The first sentence has a slightly
negative emotionality score of − 0.05. In contrast, the sec -
ond sentence has a positive score of 0.40. Theoretically, as
the audience moves from the first to the second sentence,
they experience a positive shift in their emotional state.
However, because the audience has heard only two sen -
tences thus far, they have experienced no change (because
“change” requires at least three points). The third sentence’s
score of 0.18 is less positive than the second sentence. In
extended length and complexity of long narratives allow
characters and plots to unfold gradually (Feiereisen et al.,
2021), creating multiple points of emotional engagement.
Additionally, the average emotionality of a long narrative
tends to regress toward the mean (Morin & Acerbi, 2017)
because highly emotional sentences are balanced out by less
emotional ones, making the average less insightful. These
emotionality flips generate dynamic shifts in the audience’s
emotions, creating memorable and impactful moments that
sustain interest throughout the story. These emotional highs
and lows prevent monotony, offering moments of relief and
reflection that enhance overall enjoyment.
Indeed, neuroscience research has indicated that sen -
sitivity to stimulus gradients, such as changes in the car -
diac cycle, affects the detection of emotional nuances and
emotional intensity. Importantly, this sensitivity operates
independently of stimulus intensity, underscoring the criti -
cal role of bodily states and their variations (Garfinkel et
al., 2014). Furthermore, experimental research has shown
that changes in stimulus intensity affect cortical activity, the
brain’s process for handling information, making decisions,
and controlling actions. When experiment participants rated
stimuli with varying intensity, the variations in intensity—
and not the average intensity—influenced perception and
neural activity (Torta et al., 2020). Moreover, other studies
have shown that changing the stimuli results in better brain
responses to sensory input, indicating that variations in the
stimulus intensity are a more effective measure than the
average intensity. For instance, brains distinguish changes
in sounds independently of their volume levels, demonstrat-
ing that variation in change is a superior metric (Whiteford
& Oxenham, 2023). Another study highlighted that the
brain’s sensitivity to changes in sensory differences, rather
than absolute intensity, is a widespread feature of neural
processing (Somervail et al., 2021).
Previous research has suggested that sentiment volatility
enhances audience engagement with content (i.e., virality;
Berger et al., 2021), indicating that sentiment volatility (i.e.,
the standard deviation of sentiment differences between
adjacent chunks of content) can increase virality. Consistent
with the notion that sentiment volatility makes experiences
more stimulating, thereby increasing virality, we reason that
not only the magnitude of emotion and its extremity (i.e.,
two components of volatility) but also the changes in the
direction of emotionality impact audience engagement.
Our measure of emotionality flips
Three reasons drive us to measure emotionality at the sen-
tence—as opposed to phrase or paragraph—level (Sepehri
et al., 2021; van Laer et al., 2019). First, sentences represent
natural, coherent units of thought and emotion within a text
1 3
1083

Journal of the Academy of Marketing Science (2026) 54:1080–1100
of emotionality flips (20 ÷ 100), whereas Episode B has 0.15
intensity (30 ÷ 200). Therefore, we follow previous research
that used proportions instead of counts of their textual vari-
ables (Packard et al., 2023; van Laer et al., 2019).
The preceding example illustrates two points that high -
light the novelty of emotionality flips, relative to emotional-
ity valence and intensity (Melumad et al., 2019; van Laer et
al., 2019). First, the valence shifts three times, but emotion-
ality changes direction twice. Therefore, our measure differs
from merely counting the number of times the emotionality
valence flips. We believe that measuring changes in the emo-
tionality slope is a better metric than valence flips because
the emotionality of content can remain positive (negative)
even when the previous sentence had a positive (negative)
score. Yet, the audience senses a downward (upward) slope,
despite the valence being the same. For instance, after the
sentence “After getting to know him better,” with an emo -
tionality score of 0.44, one might say, “I liked him,” with an
emotionality score of 0.42, or “I loved him,” with an emo -
tionality score of 0.59. Depending on the content creator’s
choice of words, the slope could shift, but in both cases, the
valence remains positive. Second, the emotionality inten -
sity does not impact our measure, as even subtle changes in
the emotionality slope direction can create an emotionality
flip. This flip can be considered the highest (lowest) point of
emotionality that an audience feels over the last sentence(s),
after which they experience a downward (upward) trend.
More concretely, the intensity of change between the fifth
and sixth sentences is greater than between the third and
second. However, these two sentences contribute to only a
local extreme.
Mathematically, the changes in emotionality direction
create a local optimum ( y′ n ̸= y′ n+1 ̸= 0).5 A content with
n sentences will produce n − 1 slopes and n − 2 positions
for the local optimum (see Fig. 2). In this way, each time
there is an emotionality local optimum, we count it as a sud-
den emotional change. Last, we divide the number of local
optima by the number of sentences to account for the fre -
quency and distribution of optima, thereby more accurately
measuring how dynamic and stimulating the content is.
Arousal and surprise as psychological mechanisms
Building on dual-process theories of information processing
(e.g., Pham, 1998; Schwarz, 2000), we distinguish between
affective and cognitive mechanisms through which emotion-
ality flips enhance audience engagement. We conceptualize
arousal as an affective experience that reflects the visceral
intensity of emotion (Mandler, 1982), operating quickly and
5  If there is no change in emotionality between two sentences, the
derivative of the slope will be zero, which does not account for a local
optimum in the emotionality graph.
other words, emotionality has changed direction. The graph
was upward sloping from the first sentence to the second.
The second sentence has diminished the audience’s emo -
tional experience. This change in the direction of the emo -
tionality creates a “local peak” in the graph. Our count of
the number of times emotionality changes direction is now
one.
The emotionality score of the fourth sentence, which
is lower than the emotionality score of the third sentence
(0.0 < 0.18), indicates a consistent direction in the emotion -
ality between these two sentences and, thus, no local opti -
mum in the emotionality graph. The fifth sentence expresses
the negative emotionality of − 0.31. In contrast, the sixth
sentence conveys a positive emotionality of 0.34, creating a
“local trough.” That is, the second—and the last—change in
emotionality occurs when the audience moves from the fifth
sentence to the sixth. Thus, our final count of the number of
times emotionality flips direction is two.
Next, we reason that what engages the audience is not the
mere count of the times emotionality flips direction, but the
intensity of this count throughout the narrative (Van Boven
et al., 2010). Therefore, we divide the number of local
optima by the number of sentences; that is, 2 ÷ 6 = 0.33. The
reason for using intensity is that an episode with many sen-
tences might naturally have more emotionality flips simply
because of its length.4 Consider two episodes: Episode A has
100 sentences and 20 emotionality flips, whereas Episode B
has 200 sentences and 30 emotionality flips. Episode B has
a greater number of changes in emotionality direction than
Episode A (30 vs. 20). However, Episode A has 0.2 intensity
4  Duration and length (number of sentences or words) are different
variables that could be associated with engagement but might also
influence the number of emotionality flips. Therefore, it is important
to control for both the number of sentences and the duration when
measuring emotionality flips, even when the independent variable is
the intensity of emotionality flips.
Fig. 1 An example of emotionality flips

1 3
1084

Journal of the Academy of Marketing Science (2026) 54:1080–1100
For example, the audience may be surprised when listening
to the Titanic story and suddenly witness the disaster unfold
as the ship hits an iceberg while passengers are engaged
in regular activities. Another example is the Red Wed -
ding scene in the Game of Thrones series, where disaster
strikes unexpectedly during a wedding, making it one of the
most shocking scenes in the entertainment industry (Hough
2019). These unexpected emotional turns disrupt listeners’
predictions, triggering cognitive appraisal processes (Tei -
gen & Keren, 2003) and increasing engagement by drawing
renewed attention and interest.
In summary, emotionality flips increase engagement
through (1) fast, automatic affective responses (arousal)
and (2) slower emotionally triggered cognitive appraisals
(surprise), preventing habituation and keeping the audience
mentally invested in the content (Fig. 3).
Fluency as a moderator
Individuals process narratives as if constructing and visual-
izing a story (Nielsen & Escalas, 2010), naturally impos -
ing temporal structure and causal links on events (Escalas,
2004b). Therefore, we hypothesize that the narrative’s flu -
ency—the ease with which the audience processes content
(Schuster et al., 2016)—moderates emotionality flips’ effect
on audience engagement.
We reason that emotionality flips unfold at the sentence
level, making sentence-based fluency directly relevant to
the audience’s processing of emotional shifts. Prior research
has demonstrated that processing fluency induces arousal
through the pleasure of effortless comprehension (Forster
et al., 2016). Critically, building on dual-process theo -
ries (Pham, 1998; Schwarz, 2000), highly fluent narrative
reduces the cognitive resources needed for understanding
(Alter & Oppenheimer, 2009), thereby freeing up mental
automatically to heighten engagement (Berger, 2011; Pham,
1998). In contrast, surprise represents both an emotional
and cognitive response (Teigen & Keren, 2003; Valenzuela
et al., 2010)—an emotion triggered by expectancy viola -
tions that simultaneously initiates cognitive appraisal and
mental updating (Fisk, 2002).
Arousal is a condition in which one is physiologi -
cally alert, conscious, and attentive (Heilman, 1997). This
increase in alertness captures one’s subjective feelings,
thereby enhancing engagement (Schachter & Singer, 1962).
Additionally, arousal enhances attention, encourages con -
tent consumption, and increases the virality of content
(Berger et al., 2023; Berger & Milkman, 2012). For exam-
ple, readers who encounter more arousal cues in a review
are likely to infer that the reviewer experienced higher
arousal while writing it, leading them to form related opin -
ions about the reviewer and the review (Yin et al., 2017).
Applied to narrative content, emotionality flips may serve
as affective signals of arousal, indicating that the content
creator experienced an emotional high or low, thereby trans-
mitting emotional intensity to the audience and amplifying
their engagement.
Surprise, in turn, is an emotion (Ekman et al., 1972) that
arises from unexpected events, engaging cognitive pro -
cesses of comparison and updating (Teigen & Keren, 2003;
Valenzuela et al., 2010). It reflects a hybrid mechanism—an
emotional trigger with cognitive consequences—that cap -
tures how audiences process unexpected emotional turns.
This surprise can enhance content creators’ effectiveness by
leveraging the content’s novelty (Kim et al., 2024). Listen-
ers anticipate (1) an increase in the positivity of the emo -
tionality as the content progresses with a positive emotional
trajectory or (2) a decrease in emotion when the content’s
emotion is on a downward trajectory. However, when the
trajectory unexpectedly shifts, listeners experience surprise.
Fig. 2 Example of changes in
the direction of emotionality
slopes. Note. Both examples
change the emotionality valence
twice and have the same peaks

1 3
1085

Journal of the Academy of Marketing Science (2026) 54:1080–1100
determines whether emotionality flips enhance or dampen
audience engagement with the content (Fig. 3).
H1 Emotionality flips increase audience engagement with
long narratives.
H2 Audience arousal and surprise mediate emotionality
flips’ effect on audience engagement. In other words,
emotionality flips increase audience arousal and surprise,
each of which in turn increases audience engagement.
H3 Narrative fluency strengthens emotionality flips’ posi -
tive effect on audience engagement. In other words,
emotionality flips’ positive effect on audience engage -
ment is stronger when fluency is high (vs. low).
H4 Need for affect moderates emotionality flips’ positive
effect on audience engagement, such that the effect dis-
appears for people with a low (vs. high) need-for-affect.
Study 1: Podcasts on youtube
Study 1 uses podcasts as the content of interest. A podcast
is a digital medium that features spoken content on various
topics, often serialized in formats such as interviews, discus-
sions, or storytelling (Cox et al., 2023). A podcast is distinc-
tive in its blend of narrativity and community engagement
(Cox et al., 2023). In 2019, 274.8 million people listened
to podcasts. By 2024, the number had grown to 504.9 mil-
lion, an increase of more than 80%, and the market size
reached US$30 billion. Furthermore, it is projected to exceed
$130 billion by 2030 (Backlinko Team 2024). These statistics
suggest the economic significance of research on podcasts.
Data and method
We obtained data from YouTube on April 29, 2024. Specifi-
cally, we selected the 50 most popular English text-based
capacity for affective (i.e., visceral) responses to emotional-
ity flips (van Laer et al., 2014).
In contrast, less fluent narrative taxes the audience’s cog-
nitive resources, reducing their ability to process and react
to emotional shifts. Put differently, when content is fluent,
reduced processing load enhances the affective resonance
of emotionality changes while also increasing general audi-
ence liking (Fig. 3).
Need for affect as a moderator
Individuals differ in their motivation to approach or avoid
emotionally charged experiences, a trait captured by Need
for Affect (NFA; Maio & Esses, 2001). High-NFA individu-
als are motivated to seek out, experience, and make sense
of emotions, whereas low-NFA individuals tend to avoid
emotional situations, preferring affect-neutral experiences.
These motivational orientations shape how people process
affective information and respond to emotionally laden nar-
ratives (Appel et al., 2012).
Evidence from behavioral and neurocognitive research
underscores that NFA determines the depth and style of affec-
tive processing. In naturalistic reading paradigms, high-NFA
individuals exhibit slower reading of emotion-laden cues,
reflecting deeper engagement and elaboration on affective cues,
whereas low-NFA individuals process such cues more rapidly
(Lei et al., 2023). Similarly, high-NFA individuals show greater
behavioral responsiveness to affective variable messages than
their low-NFA counterparts (Haddock & Maio, 2019).
Extending these findings to narrative dynamics, we rea -
son that emotionality flips serve as affectively rich signals
that evoke arousal and surprise. Such affective variability
is inherently engaging for high-NFA individuals because
it aligns with their motivation to approach, experience,
and interpret emotions. By contrast, low-NFA individuals
are less inclined to seek out affective stimulation and may
disengage when confronted with emotional shifts, perceiv -
ing them as overwhelming. Thus, NFA’s motivational role
Fig. 3 Conceptual framework
1 3
1086

Journal of the Academy of Marketing Science (2026) 54:1080–1100
the two-dimensional space. We connect the points to form a
zigzag line representing the episode’s emotional trajectory.
Fourth, we calculate the slope between each pair of points.
Fifth, we compute the number of times the slope changes
from upward to downward (i.e., from positive to negative)
or vice versa. Sixth, we divide the number of times emo -
tionality flips (i.e., changes direction) by the number of
sentences.
Moderator variable of fluency We measure a narrative’s
fluency by the Flesch Reading Ease metric (Flesch, 1948), a
widely adopted measure of processing fluency (Markowitz,
2023; Packard et al., 2023; Pancer et al., 2019). The Flesch
Reading Ease score is calculated based on (1) the average
sentence length and (2) the average number of syllables per
word, with higher scores indicating more fluent (i.e., easier-
to-process) text (Markowitz, 2023; Schuster et al., 2016; see
Web Appendix D for the formula).
Control variables  We list our control variables in four
groups: (1) 25 episode-specific control variables related to
the episode’s topics, (2) five” other” episode-specific covari-
ates, (3) one podcast-specific control variable, and (4) four
levels of fixed effects (channel, year, month, and weekdays).
Table 1 lists the variables (see Web Appendix B; Table B4
for descriptive statistics and Table B5 for Pearson bivariate
correlation coefficients).
Regression specification
To estimate the effect of emotionality flips on audience
engagement, we include episode-level covariates and fixed
effects for channels, years, months, and weekdays. Because
emotionality flips is non-normally distributed and may be
endogenous to audience engagement, we include a Gauss -
ian copula term in the specification (Park & Gupta, 2012;
details of Normality tests are provided in Web Appendix B,
Table B3, and Fig. B2). Therefore, we specify the follow -
ing equation to measure a podcast episode e’s emotional -
ity flips’ effect on audience engagement with the episode
e, which was published on YouTube channel c on day d of
month m in calendar year y.
Log (Audience engagement )= β 0 + β 1 × (Emotionality f lips )e
+β 2 × (F luency )e + β 3 × (N umber of sentences )e + β 4
× (Average emotionality )e + β 5 × (N umber of days since posted )e
+ β 6 × (Duration)e + β 7 × (N umber of subscribers)+β 8−32
× (T opic weights )e + β 33 × (Copula term f or the emotionality f lips) e
+ Channelc + Dayd + M onth m + Y ear y + ϵe
 (1)
The episodes within the same podcast are nested within the
channels and thus not independent of each other. Therefore, we
estimate standard errors clustered at the channel level. Lastly,
our DV is a log-transformed count. Consequently, we use the
ordinary least squares (OLS) estimator to estimate Eq. 1.
podcasts as of April 29, 2024 (see Web Appendix B; Table
B1 lists names of the 50 podcast channels in our sample,
along with the number of episodes in each channel). We col-
lected the transcripts of each podcast’s episodes published
from January 1, 2019, to April 29, 2024. 6,7 This procedure
yielded transcripts for 33,598 episodes. We measure the
independent variable, the moderator, and the dependent
variable at the episode level. Thus, the podcast episode
serves as our unit of analysis.
Dependent variable (DV) of audience engagement  Fol -
lowing previous research (Rizzo et al. 2023a), we measure
audience engagement by the sum of the episode’s (1) num -
ber of views, (2) the number of likes, and (3) the number of
comments as of April 29, 2024. The sum is highly skewed
and has high kurtosis (details in Web Appendix B, Table
B2). Therefore, following prior research (Chen & Berger,
2013), we natural log-transform (i.e., log transform with
base e, where e is 2.718) the values of the sum (see Web
Appendix B; Fig. B1 presents the histogram of the values of
audience engagement before and after the log transforma -
tion). Web Appendix C’s Table C1 reports robustness across
the three individual counts (i.e., log of the number of views,
likes, and comments) as DVs.
Explanatory variable of e motionality flips  We measure
an episode’s emotionality flips by a ratio variable. The
numerator is the number of times sentence-level emotional-
ity changes direction in the episode. The denominator is the
episode’s number of sentences.
We calculate the values in six steps. First, we split each
episode into sentences (Packard et al., 2023). Second, prior
marketing research has reasoned that “V ADER outperforms
other commonly used benchmark methodologies such as
Linguistic Inquiry and Word Count, Affective Norms for
English Words, and the machine learning algorithm sup -
port vector machine” (Lacka et al., 2022, p. 69). Therefore,
we measure each sentence’s emotionality using the Valence
Aware Dictionary and Sentiment Reasoner’s (V ADER’s)
compound variable (Hutto & Gilbert, 2014). V ADER clas-
sifies words by valence (i.e., positive, negative, and neutral)
and weights the valence by intensity (Pancer et al., 2019).8
Third, we draw a graph, plotting sentence number (e.g., 1, 2,
and so on) on the X-axis and the sentences’ compound val-
ues on the Y-axis. Thus, each sentence occupies a point in
6  We omitted podcasts that do not include text (e.g., music podcasts).
7  Podcasts have experienced a rise in popularity since 2019 (Cramer-
Flood, 2021).
8  For example, the compound score for “love” is 0.63, whereas the
compound score for “hate” is − 0.57. Similarly, the compound score
for “excellent” is 0.57, but the compound score for “terrible” is − 0.47.
1 3
1087

Journal of the Academy of Marketing Science (2026) 54:1080–1100
positive and statistically significant, providing support for H3
(Table 2, Column II: bEmotionality flips × Fluency → Audience engagement
= 0.0001, p < 0.01). This finding supports our theorization
that fluency facilitates emotionality shifts’ affective process-
ing by reducing cognitive load and enhancing the audience’s
capacity to engage with emotionally dynamic content.
Robustness checks
We conducted an extensive set of robustness analyses to
ensure that the relationship between emotionality flips and
audience engagement is not an artifact of model speci -
fication, measurement choices, or alternative linguistic
constructs. Across nine robustness checks—including
(1) random-effects specification with channel treated as a
Results
Main specification Table 2’s Column I reports the estimates.
We find a positive association between the emotionality flips
in a podcast episode and audience engagement with the epi-
sode (Table 2, Column I: bEmotionality flips → Audience engagement =
0.945, p < 0.001, Exp(b) = 2.57). The interpretation is that
a 1% increase in emotionality flips in a podcast episode is
associated with a 157% increase in engagement with the epi-
sode. This result supports H1. The estimated coefficient of the
copula term is insignificant, suggesting that Emotionality flips
is likely exogenous in our specification (Papies et al., 2017).
Moderation by fluency  The estimated coefficient of the
interaction term between emotionality flips and fluency is
Variable Measure Reason for inclusion, if regressor Reference
research
DV
Audience
Engagemente
The sum of three counts: (1)
the episode’s number of views,
the number of likes, and the
number of comments as of
April 29, 2024.
Rizzo et al.
(2023a)
Moderator
Fluencye The ease with which words
and sentences are processed
(determined by their length
and syntactic complexity).
Moderator  Markow-
itz (2023);
Schuster et al.
(2016)
Controls
Average
emotionalitye
The value of the V ADER com-
pound score, averaged over all
sentences of the episode.
Overall emotionality of the content
can be associated with engagement.
 Berger et al.
(2023); Berger
and Milkman
(2012)
Duratione Episode’s number of seconds. Previous research has suggested that
content duration can be associated
with engagement.
 Markowitz
and Shulman
(2021)
Number of
subscriberse
Controlling for the number of
subscribers to the channel.
The more subscribers the podcast
channel has, the more the audience
engages with the episodes.
25 Topic weightse 25 episode-specific con-
trol variables related to the
episode’s topics (see Web
Appendix E for details).
Audience engagement with content
is a function of the topics it covers.
 Berger et
al. (2021);
Packard et al.
(2023)
Channels FEs Channel ID It helps us control for time-invari-
ant, channel-specific determinants
(e.g., topics, podcaster) of audience
engagement with an episode.
 Perse (1998)
Years FEs 2019 to 2024 Audience engagement may vary by
year (e.g., during the COVID-19
pandemic).
 Li et al.
(2021)
Months FEs 12 months of the year Audience engagement may vary by
the month (e.g., weather)
 Stroud and
Muddiman
(2019)
Weekdays FEs 7 days of the week Audiences may engage less on their
workdays than on their off-work
days.
 Devereux et
al. (2020)
Table 1 Study 1: Variables
Subscript e refers to episode

1 3
1088

Journal of the Academy of Marketing Science (2026) 54:1080–1100
their followers’ opinions and behaviors. This influence is
directly tied to the level of engagement their content can
generate. Therefore, our Study 2 samples influencers’ con -
tent (in place of podcasts), testing whether influencers can
boost audience engagement by flipping emotionality in their
content and whether fluency can moderate this effect.
We source data from TED.com, a platform dedicated to
the dissemination of “ideas worth spreading.” Prior research
has examined the relation between a TED talk’s content and
its number of views (Markowitz & Shulman, 2021). View-
ers are more likely to share an engaging talk with their
online network (e.g., on Facebook or LinkedIn). Such shar-
ing, in turn, increases the talk’s number of views (Seiler et
al., 2017).
Data and method
We use a publicly available dataset of 3,381 TED talks. 10
Thus, a talk is our unit of observation and analysis. The
measurements for the independent variable, moderator, and
dependent variables in Study 2 are identical to those in Study
1, with the slight difference that we measure engagement by
the sum of (1) the number of views and (2) the number of
comments. The sum is highly skewed and has high kurtosis.
Therefore, we natural log-transform the values of audience
engagement (our DV) and estimate the regression using the
OLS estimator (see Web Appendix B; Table B2 for details,
and Fig. B3 presents the histograms of audience engage -
ment before and after log-transformation). Web Appendix
C’s Table C2, reports robustness using (1) the log of the
number of views and (2) the log of the number of comments
as DVs.
We retain all covariates from Study 1 except (1) the num-
ber of subscribers and (2) channel-fixed effects, which do
not apply to TED talks. We include two new control vari -
ables. First, we control for the number of available subtitles
for the talk because the more subtitles available, the more
accessible the talk is to audiences with varying language
preferences. Second, we included fixed effects for speakers’
gender. Furthermore, using the same topic modeling method
as in Study 1, the 20-topic model yielded the lowest per -
plexity score (see Web Appendix B, Table B6 for descrip -
tive statistics and Table B7 for correlation coefficients).
Our specification likely omits variables that correlate
with emotionality flips and audience engagement. We
account for Emotionality flips ’ potential endogeneity by
using the Gaussian Copula method (Park & Gupta, 2012;
details of the normality tests are provided in Web Appendix
B, Table B3). Each of the four tests rejects the null hypoth -
esis of Emotionality flips’ normality and thus supports our
10   h t t p s :   /  / g i t h u   b . c  o  m /  T  h e  - G  u p  t a /  T E D - S c r a p e r.
random effect, (2) an alternative rule-based sentiment tool
(TextBlob), (3) a deep-learning–based sentiment regressor
(DistilBERT), (4) ChatGPT-based emotionality scoring, (5)
alternative units of emotionality measurement (two-sen -
tence chunks),9 (6) alternative dependent-variable scaling,
(7) controls for sentiment volatility (Berger et al., 2021),
(8) controls for the magnitude of emotionality changes,
and (9) controls for semantic progression (Toubia et al.,
2021)—the positive association between emotionality flips
and audience engagement remained statistically significant
and directionally consistent (Web Appendix F; Table F1).
The effect sizes obtained from these alternative approaches
closely track those from our main specification, demonstrat-
ing that the observed effect is robust to multiple modeling
assumptions, alternative sentiment engines, and theoreti -
cally relevant covariates.
Study 2: TED talks
Influencers are regarded as opinion leaders due to their
extensive reach and ability to shape public perceptions by
disseminating content across social media platforms (Leung
et al., 2022b; Mardon et al., 2023). They aim to influence
9  See Web Appendix F, Table F1 (columns X–XII) for results using
three-, four-, and five-sentence chunk sizes. The results remained the
same, demonstrating that the effect of emotionality flips on engage -
ment is robust to alternative chunking specifications.
Table 2 Study 1: regression estimates
DV = log (Audience engagement)
(I) Main specification (II) Moderation
Emotionality flips 0.945*** (0.341) 1.028*** (0.339)
Fluency −0.00004*** (0.0000) −0.0002*
(0.0001)
Emotionality flips ×
Fluency
0.0001**
(0.0001)
Number of sentences 0.0004** (0.00003) 0.0004**
(0.0001)
Average emotionality −0.661*** (0.133) −0.659*** (0.132)
Days elapsed 0.002*(0.001) 0.002* (0.001)
Duration 0.0001*** (0.0000) 0.0001***
(0.0002)
Number of subscribers −0.0000 (0.0000) −0.0000 (0.0000)
Copula term for IV −0.003 (0.010) −0.010 (0.010)
25 LDA Topic weights ✓ ✓
Channel FEs ✓ ✓
Year FEs ✓ ✓
Month FEs ✓ ✓
Day FEs ✓ ✓
Constant 7.861*** (1.828) 7.826*** (1.828)
Observations 33,584 33,584
Log likelihood −52,677.720 −52,674.090
AIC 105,563.400 105,558.200
*p < 0.05; **p < 0.01; ***p < 0.001
1 3
1089

Journal of the Academy of Marketing Science (2026) 54:1080–1100
experience and respond to shifts in emotional tone more
fully.
Robustness checks
We reported nine robustness checks for Study 1: (1) random-
effects regression, (2) an alternative method (i.e., TextBlob)
of measuring emotionality, (3) using a deep learning-based
method to measure emotionality, (4) using ChatGPT-gen -
erated emotionality scores, (5) an alternative unit of mea -
surement of emotionality (i.e., two-sentence instead of
one-sentence chunks), (6) an alternative measure of the DV ,
(7) controlling for Berger et al.‘s (2021) sentiment volatility,
(8) controlling for the magnitude of emotionality flips, and
(9) controlling for Toubia et al.‘s ( 2021) semantic progres-
sion variables.
Unlike podcast episodes, which are nested within chan -
nels, TED Talks are not embedded within higher-order
structures such as channels. Therefore, a random-effects
regression is not particularly appropriate in this context.
However, the remaining nine robustness checks are appli -
cable. Results from these tests continue to support our main
findings. Table F2 in Web Appendix F reports estimates
consistent with those presented in Table 3, Column I of the
main specification.13
Study 3: Replicating the effect in a controlled
experiment
Study 3 tests the effect in a controlled lab setting, leverag -
ing random assignment to examine the causal interpretation
of our hypothesized coefficients in H1. Moreover, it helps
test the underlying mechanisms by examining both affective
and cognitive pathways through which emotionality flips
may influence engagement (our H2). To rule out curiosity as
a hybrid motivational state arising from perceived knowl -
edge gaps (Berlyne, 1966), we measured curiosity alongside
arousal and surprise to ensure that any observed effects of
emotionality flips on engagement were not better explained
by a heightened sense of curiosity.
Participants, design, and procedure
Our pre-registered experiment (see  h t t p  s : /  / a s p  r e  d i c  t e d .  o r g
/ t z  z 7 - 5 h z 3 . p d f) recruited 801 participants (M Age = 42.13,
48.4% female) from Prolific and randomly assigned them to
one of two between-subjects conditions: low emotionality-
flips vs. high emotionality-flips.
13  We also tested the measure using three-, four-, and five-sentence
chunk sizes. The results remained consistent across all specifications,
confirming the robustness of our findings. See Web Appendix F, Table
F2 for detailed results.
inclusion of the Gaussian copula term to control for Emo-
tionality flips’ potential endogeneity (see Web Appendix B;
Fig. B4).
Results
Regression estimates report that a Ted talk’s number
of emotionality flips is positively associated with audi -
ence engagement with the Talk (Table 3, Column I:
bEmotionality flips → Audience engagement  = 0.828, p <  0.001,
Exp(b) = 2.29).11 The interpretation is that a 1% increase
in the emotionality flips in a TED talk is associated with
a 129% increase in engagement. 12 This result supports H1.
The estimated coefficient of the copula term is insignificant,
suggesting that Emotionality flips is likely exogenous in our
specification (Papies et al., 2017).
Moderation by fluency  We next test whether the Talk’s
fluency strengthens emotionality flips’ positive effect on
audience engagement. The results, reported in Table 3, indi-
cate a significantly positive coefficient of the interaction
between emotionality flips and fluency (Table 3, Column II:
bEmotionality flips × Fluency → Audience engagement  = 0.006, p < 0.05),
providing support for H3. This finding aligns with our theo-
retical argument that narrative fluency facilitates affective
processing of emotional variation, enabling audiences to
11  Results hold when the DV is the individual components of (1) the
number of views, and (2) the number of comments, (see Web Appen -
dix C; Table C2).
12  ( Exp (b) − 1) × 100 = ( Exp (0.828) − 1) × 100 = 129% .
Table 3 Study 2: Regression estimates
DV = log (Audience engagement)
(I)
Main specification
(II)
Moderation
Emotionality flips 0.828*** (0.172) 0.504* (0.266)
Fluency 0.0002 (0.0003) −0.0003 (0.0004)
Emotionality flips × Fluency 0.006* (0.003)
Number of sentences 0.003*** (0.0004) 0.0003*** (0.001)
Average emotionality 0.030* (0.017) 0.032* (0.017)
Days elapsed 0.003** (0.001) 0.003** (0.001)
Duration 0.0004*** (0.0001) 0.005*** (0.0001)
Number of subscribers 0.063*** (0.002) 0.063*** (0.002)
Copula term for IV −0.005 (0.017) −0.008 (0.017)
20 LDA Topic weights ✓ ✓
Gender FEs ✓ ✓
Year FEs ✓ ✓
Month FEs ✓ ✓
Day FEs ✓ ✓
Constant −6.439 (6.807) −6.174 (6.809)
Observations 3,381 3,381
Log likelihood −3,172.399 −3,170.842
AIC 6,468.799 6,467.684
*p < 0.05; **p < 0.01; ***p < 0.001
1 3
1090

Journal of the Academy of Marketing Science (2026) 54:1080–1100
low emotionality-flips condition (M Low = 4.52, SD = 1.70;
F(1, 799) = 18.31, p < 0.001, partial η² = 022).
Surprise Participants in the high emotionality-flips con -
dition (M High = 3.98, SD = 1.08) reported feeling a higher
level of surprise while watching the podcast episode than
those in the low emotionality-flips condition (M Low = 3.83,
SD = 1.16; F(1, 799) = 3.68, p = 0.050, partial η² = 0.005).
Curiosity Participants in the high emotionality-flips condi -
tion (MHigh = 4.61, SD = 2.02) and the low emotionality-flips
condition reported similar levels of curiosity (MLow = 4.59,
SD = 2.02; F < 1, p = 0.882, partial η² = 0.000). Therefore,
this variable cannot be a mediator.
Mediation Next, we examine whether arousal and surprise
mediate emotionality flips’ effect on participants’ engage -
ment with the podcast. First, we conduct separate media -
tion analyses using PROCESS Model 4 (Hayes, 2022; 5,000
bootstrapped samples), testing each mediator individually.
Results reveal that arousal (indirect effect = 0.21, 95% CI =
[0.10, 0.29]) and surprise (indirect effect = 0.03, 95% CI =
[0.01, 0.05]) significantly mediate the effect of emotionality
flips on podcast liking. This result supports H2.
We assess the relative contribution of each mechanism
variable by including them simultaneously in a parallel
mediation model using PROCESS Model 4 (Hayes, 2022;
5,000 bootstrapped samples). The indirect effect via arousal
remains significant (indirect effect = 0.20, 95% CI = [0.11,
0.29]), whereas the indirect effect via surprise is no longer
significant (indirect effect = 0.00, 95% CI = [− 0.00, 0.01]).
These findings suggest that while surprise may help explain
the effects of emotionality flips, arousal is the primary
mechanism underlying these effects. This result brings clari-
fication to H2.
Discussion
Study 3 replicates emotionality flips’ causal impact on audi-
ence engagement in a carefully controlled lab experiment
and identifies arousal as the key explanatory mechanism.
While both arousal and surprise mediate the effect when
tested separately, only arousal remains significant when the
two variables are modeled simultaneously, accounting for
the majority of the variance in liking. These results provide
strong causal support for H1 and H2, demonstrating that
arousal is the primary driver of emotionality flips’ effect on
audience engagement. Lastly, this mechanism aligns with
our findings regarding the moderating role of fluency (H3):
disfluent content allocates more resources to the cognitive
We rely on previous experimental research on long-
form content (e.g., TED Talks; Sepehri et al., 2025) to
create stimuli for manipulating emotionality flips. Spe -
cifically, we utilized Study 1’s emotionality flips scores
and randomly selected two podcast episodes, one from the
top 10% (emotionality flips’ score = 0.66) and the other
from the bottom 10% (emotionality flips’ score = 0.36)
of the distribution. We drew these stimuli-episodes from
the same podcast channel to control for potential con -
founds related to topic, host style, and episode length,
thereby ensuring that only the emotionality flips’ level
varies across the two experimental conditions (see Web
Appendix G for stimuli). We assigned each participant
randomly to a condition. The participant listened to a
podcast episode and subsequently completed the survey.
While Studies 1 and 2 measured audience engagement
by the sum of the number of views, likes, and comments
received by each podcast/talk, Study 3 measures engage -
ment by interest and liking (i.e., “How interesting did you
find this podcast episode? How much did you like this pod-
cast episode?” α = 0.97; Sepehri et al., 2025).
We also measured several psychological mechanisms
hypothesized to mediate emotionality flips’ effect on
audience engagement. Specifically, we measure Arousal
using three bipolar scales that assess the degree of
energy, activation, and excitement elicited by the epi -
sode (α = 0.85; Berger, 2011). We measure Surprise  by
three items asking the extent to which participants felt
able to predict upcoming events, how unexpected they
found the storyline, and how difficult it was to anticipate
what would happen next (α = 0.81). Lastly, we measure
Curiosity  by asking participants to report their desire
to continue listening to the series, learn more about the
narrator, and gain further information about the main
character (α = 0.89; see Web Appendix G for items). We
concluded the study by collecting participants’ basic
demographic information.
Results
Audience engagement Results reveal that emotionality flips
increase participants’ engagement with the episode. Specifi-
cally, participants in the high emotionality-flips condition
(MHigh = 5.24, SD = 1.78) engaged with the podcast episode
more compared to participants in the low emotionality-flips
condition (M Low = 4.90, SD = 1.80; F(1, 799) = 7.34, p =
0.007, partial η² = 0.01).
Arousal Participants in the high emotionality-flips con -
dition (M High = 5.01, SD = 1.50) reported feeling higher
arousal while watching the podcast episode than those in the
1 3
1091

Journal of the Academy of Marketing Science (2026) 54:1080–1100
were identical in length, pacing, and voice but differed in
the emotionality flips (Fig. 4).
After listening to one of the two podcast versions, partici-
pants evaluated the episode using the same measures used
in Study 3 (α = 0.97). Participants also completed the NFA
scale (Appel et al., 2012), consisting of ten items (e.g., “I
feel that I need to experience strong emotions regularly”;
“I would prefer not to experience either the lows or highs
of emotion” [reverse-coded]; full scale in Web Appendix H,
α = 0.70). The study concluded with collecting basic demo -
graphic information.
Results
Audience engagement Participants in the high-flip condi -
tion (MHigh = 4.91, SD = 1.51) reported greater engagement
than those in the low-flip condition (MLow = 4.14, SD = 2.04;
F(1,196) = 9.22, p = 0.003, partial η² = 0.045).
Moderation To test the moderating role of NFA, we con -
ducted a moderation analysis (PROCESS Model 1, 5000
bootstrapped samples; Hayes, 2022). We find a significant
interaction between emotionality flips and NFA (b = 0.59,
SE = 0.24, t = 2.49, p = 0.014), indicating that the effect of
emotionality flips disappears for people with low NFA.
Floodlight analyses (Spiller et al., 2013) indicate that this
effect holds only among participants with an NFA of 4.63 or
higher (63.64% of the sample; Fig. 5).
Discussion
Study 4 replicates the main effect of emotionality flips
on audience engagement and provides evidence that this
relationship is moderated by Need for Affect . Specifi -
cally, individuals high in NFA were significantly more
system and diverts resources away from the affective route,
which served as the main pathway through which emotion -
ality flips increased engagement.
Study 4: Moderating role of need for affect
Study 4 pursues three main goals. First, it seeks to replicate
the main effect of emotionality flips on audience engage -
ment using podcast stimuli we created for this study (H1).
Second, because these podcasts were generated using the
same text-to-speech system and identical voices, the flu -
ency, tone, and idiosyncratic vocal style of the podcaster
were held constant, thereby ruling out these potential con -
founds in Study 3. Third, the study aimed to test the mod -
erating role of NFA to examine whether the positive impact
of emotionality flips on audience engagement depends on
listeners’ motivation to approach and experience emotions
(H4).
Participants, design, and procedure
Our pre-registered experiment (see  h t t p  s : /  / a s p  r e  d i c  t e d .  o r g  / s
g  7 f t 4 . p d f) recruited 200 participants (M Age = 45.42, 55.1%
female) from Prolific and randomly assigned them to one of
two between-subjects conditions: low emotionality flips vs.
high emotionality flips.
To ensure that potential confounds such as vocal flu -
ency, tone, or idiosyncratic voice characteristics were
held constant, we created both podcast episodes ourselves
using text-to-speech synthesis. This approach enabled us
to manipulate only the degree of emotionality flips, while
maintaining identical pacing, prosody, and vocal quality
across conditions. Both podcasts narrated the same storyline
but were systematically modified to differ in their emotional
variability (excerpts in Web Appendix H). The two versions
Fig. 4 Emotionality flips across
both conditions (Left: low
emotionality flips; Right: high
emotionality flips)

1 3
1092

Journal of the Academy of Marketing Science (2026) 54:1080–1100
developing two podcast transcripts that describe the
Apollo 11 Moon landing. The two versions were identi -
cal in length, topic, and informational content but dif -
fered systematically in emotionality flips: the low-flip
version contained 20 emotional shifts across 65 sen -
tences (flip score = 0.31), whereas the high-flip version
included 43 emotional shifts across 62 sentences (flip
score = 0.69; see Web Appendix I for full transcripts and
Fig. I1 for the sentence-level flip distributions).
We then used the ChatGPT API (model gpt-4o) to sim -
ulate 5,000 independent participants (2,500 per condi -
tion). Each synthetic participant was randomly assigned
two or three human-like characteristics from a pool of 50
traits (e.g., curiosity, analytical thinking, emotional sen -
sitivity, attentional control; full list in Web Appendix I,
Table I1). These traits were embedded directly into the
system prompt, instructing the model to respond as if
it were a person possessing those characteristics (Yuan
et al., 2024). After reading one version of the podcast
transcript, each synthetic participant answered a single
engagement question: “How engaging did you find this
podcast episode?” (1 = Not at all engaging, 7 = Extremely
engaging).
For each condition, the model generated 2,500 unique
engagement ratings with randomized temperature settings
(0.8–1.2) to induce natural variability across simulated
respondents. Each response, along with the assigned char -
acteristic codes, was recorded automatically via the API and
stored in a structured dataset.
engaged by podcasts featuring high emotionality flips,
whereas the effect disappeared among individuals low
in NFA. This pattern supports H4. Additionally, by hold -
ing constant the fluency, tone, and idiosyncratic vocal
style of the podcaster through text-to-speech synthesis,
Study 4 rules out these potential confounds and dem -
onstrates that the observed effects are driven by emo -
tional dynamics rather than differences in delivery style
or expressiveness.
Study 5: Validation with synthetic audiences
With the rapid rise of generative AI, researchers increas -
ingly use Large Language Models (LLMs) to simulate
human judgments and generate synthetic behavioral
data (Huang & Rust, 2025). These models can approxi -
mate consumer evaluations with high reliability, offer -
ing a scalable, replicable complement to traditional
data collection (Toubia et al., 2025). Building on this
methodological advancement, Study 5 uses synthetic
participants to examine whether podcasts with high
emotionality flips are perceived as more engaging than
those with low emotionality flips.
Design and procedure
Study 5 employed a between-subjects design: low emo -
tionality flips vs. high emotionality flips. We test the
robustness of our findings using long-form stimuli by
Fig. 5 The conditional effect of emotionality flips on DV at different levels of Need for Affect. The grey area indicates the Johnson-Neyman region
of significance

1 3
1093

Journal of the Academy of Marketing Science (2026) 54:1080–1100
content creators are incentivized to produce long-form nar -
ratives that sustain audience interest. We contribute to this
literature by introducing a novel construct that is especially
relevant to long narratives: emotionality flips. Unlike valence,
intensity, or emotional type, emotionality flips capture the
dynamic flow of emotion over time, making them uniquely
suited to understanding engagement in long-form content.
By focusing on this temporal emotional structure, our work
offers new, content-specific insights into how creators can
craft more engaging narratives.
Second, our research contributes to the literature on nar -
rativity by focusing on the discourse dimension (i.e., how
narrativity is conveyed; Chatman, 1978; Culler, 1981)—
specifically, the role of emotionality flips in narrative deliv-
ery. Emotionality flips serve as narrative discourse tools
that introduce emotional dynamics into messages, allowing
podcasters and speakers to embed a sense of narrativity and
benefit from its persuasive effects (i.e., narrative persuasion;
Argo et al., 2008; Escalas, 2007).
Third, we extend dual-process models (e.g., Pham, 1998;
Schwarz, 2000) of engagement by uncovering the underly -
ing psychological mechanisms through which emotional -
ity flips operate. Study 3 reveals that arousal mediates the
effect of emotionality flips on podcast liking, whereas sur -
prise plays a weaker and less consistent role. This suggests
that emotionality flips engage audiences primarily through
fast, visceral emotional activation. This contributes to the
theories of affective engagement (Berger, 2011; Mandler,
1982) by showing that dynamic emotional variation, when
processed fluently, can trigger heightened arousal that sus -
tains attention and liking.
Implications for practice
We offer insights for content creators, influencers, opinion
leaders, and anyone seeking to shape audience opinions and
enhance engagement. Additionally, we cater to platforms
that curate and recommend content, as well as to consumers
who aim to select content that best fits their interests and
goals.
Recommendations for content creators  Prior research has
advised content creators to engage their audience by (1)
defining a clear niche (Garcia 2021), (2) using specific
types of words (e.g., semantic; Rizzo al., 2023a; Rizzo et
al., 2023b), (3) delivering specific types of emotions (Lin
et al., 2021), (4) referencing their close social ties (Chung
et al., 2023), and (5) paying attention to the match between
supported brands and followers (Leung et al., 2022a). Prac-
titioners also offer recommendations, such as exhibiting
creativity (Adobe Express 2024), creating longer videos on
Results
Audience engagement Results showed that synthetic par -
ticipants exposed to the high-flip podcast rated it as signifi -
cantly more engaging (M High = 4.96, SD = 1.13) than those
exposed to the low-flip version (M Low = 4.87, SD = 1.15;
F(1, 4,998) = 7.58, p = 0.006). The effect remained signifi -
cant after controlling for all 50 personality-like traits (F(1,
2,449) = 32.05, p < 0.001).
Discussion
Study 5 validated the effect of emotionality flips using syn-
thetic audiences simulated via ChatGPT. This approach
demonstrates that the observed patterns generalize beyond
traditional, limited samples and can be reproduced in large-
scale, fully controlled, long-form narrative contexts.
General discussion
Our research develops the concept of emotionality flips. It
tests its impact on audience engagement using two large-
scale observational datasets, two controlled lab experiments,
and a synthetic validation using LLMs. The five studies
demonstrate that emotionality flips are associated with, and
causally lead to, higher audience engagement, providing
support for H1. Study 3 also indicates that arousal drives
this effect, thus supporting and clarifying H2. Furthermore,
our observational studies consistently reveal that narrative
fluency moderates emotionality flips’ effect, such that emo-
tionality flips are more impactful when the content is easier
to process, providing support for H3. Lastly, Study 4 intro -
duces a boundary condition based on individual differences,
showing that the effect of emotionality flips depends on the
audience’s NFA (H4), thereby extending the framework to
account for individual variability in audience responses.
Contributions to theory
First, previous research has documented various determinants
of audience engagement with content. These determinants
include (1) overall emotionality (Lee, 2021), (2) specific
types of emotionality (Mosley et al., 2024), (3) non-emotional
cues such as selfies with a brand (Hartmann et al., 2021), and
(4) the audience’s level of closeness with the person post -
ing the content (Dubois et al., 2016). However, these studies
largely overlook the role of content length and narratives—a
key consideration in the creator economy, where longer nar-
ratives often translate into greater monetization opportuni -
ties. Because revenue is closely tied to engagement duration,
1 3
1094

Journal of the Academy of Marketing Science (2026) 54:1080–1100
Therefore, including emotionality flips may increase
users’ adoption of the recommended content, thereby
boosting their trust in the recommendations.
2. Platforms should develop AI-powered diagnostic tools
for creators. Content creators may lack knowledge of
emotionality flips in their content. Platforms can pro -
vide a tool that scores a content’s emotionality flips
score and identifies emotionally flat or overly volatile
segments in text, audio, or video content. The content
creator may revise the segments and publish the con -
tent that they believe has the emotionality flips they are
comfortable with. Subsequently, the platform should
provide evidence of the association between content’s
emotionality flips and audience engagement. The evi -
dence will give feedback to the content creator and help
them adjust the emotionality flips in their future content.
Recommendations for consumers  Emotionality flips also
carry practical implications for audiences who seek engag -
ing, meaningful, and emotionally balanced experiences.
Understanding how emotional variation shapes engagement
can help audiences make more intentional choices about the
content they consume. Accordingly, we recommend that
consumers:
1. Select emotionality flip content for high engagement.
The audience should choose creators or genres with
high emotionality flips because they provide emotional
arousal.
2. Seek emotionality flip content if high on need-for-affect
(NF A). The audience should favor emotionality flip con-
tent, particularly if they experience high NFA.
Emotionality flips beyond the creator economy  Beyond
influencer content, emotionality flips may serve as a ver -
satile mechanism across broader consumer communication
domains. In advertising, sequencing emotional highs and
lows can sustain arousal and enhance persuasion (Berger
& Milkman, 2012). In online reviews, moderate emotional
variation may enhance perceived effort and helpfulness
(Yin et al., 2017), while excessive emotional variation may
reduce trust. Similarly, on platforms like Yelp, where sec -
ondary metrics such as “love this” and “oh no” are tracked,
emotionality flips may help reviewers shape reader percep -
tions and boost content visibility. Lastly, since high-arousal
emotions are linked to greater WOM diffusion, emotionality
flips may increase the likelihood of sharing, expanding the
reach of emotionally dynamic narratives (Consiglio et al.,
2018).
However, emotionality flips may not be universally effec -
tive. Poorly calibrated arousal fluctuations may overburden
YouTube (Peterson 2024), and maintaining a strong connec-
tion with the audience (Spotify 2024).
However, academic and practitioner discussions have
mostly overlooked the emotionality dynamics that unfold
within a narrative. Our research fills this “gap” by demon -
strating that emotionality flips—deliberate shifts between
emotional highs and lows—increase audience engagement.
Accordingly, we put forth the following recommendations:
1. Creators should create emotional variation.  They
should design content with emotional highs and lows
and thus increase engagement.
2. Creators should increase audience arousal.  Audience
arousal is the primary underlying psychological mecha-
nism. Therefore, creators can heighten arousal not only
by flipping emotionality but also through nonverbal ele-
ments such as pauses, music transitions, vocal inflec -
tions, or visual pacing.
3. Creators should create content that is easy to process
for the audience. Maintain narrative fluency by keeping
transitions coherent and natural so that emotional shifts
enhance, rather than disrupt, the audience experience.
4. Creators should acknowledge individual differences
in need-for-affect (NF A). Emotionality flips are most
effective for audiences with high NFA. Therefore, emo-
tionality flips are beneficial for content targeted at high-
NFA audiences, but not for content targeted at low-NFA
audiences.
Recommendations for platforms Our findings hold impor -
tant implications for platform-level strategy and algorithmic
design. Recommendation systems employed by platforms
such as YouTube, Spotify, and TikTok often prioritize con-
tent that elicits high arousal or surprise (Berger et al., 2023;
Teixeira et al., 2012). Emotionality flips can serve as a strong
signal to such curation algorithms, increasing the likelihood
that emotionally dynamic content surfaces on platform
users’ feeds. Algorithms may also tailor recommendations
based on users’ prior engagement with emotionally fluctuat-
ing narratives, meaning creators who strategically incorpo -
rate emotionality flips may benefit from greater algorithmic
amplification. Accordingly, we put forth two recommenda -
tions for platforms:
1. Platforms should incorporate the emotionality flips
feature into recommendation algorithms . Including
emotionality flips as a predictive feature in audience
engagement models can increase platform users’ accep-
tance of the recommended content and thus boost the
model’s true positives. Additionally, content consumers
often watch content to experience a sense of arousal.
1 3
1095

Journal of the Academy of Marketing Science (2026) 54:1080–1100
Fifth, prior research differentiates between mega- and
micro-influencers (Rizzo et al. 2023b). Our data draws from
highly popular YouTube podcasts and TED Talks, which
may bias effects toward well-established creators. Future
studies should examine whether emotionality flips operate
similarly for micro-influencers or creators at earlier stages
of audience growth.
Sixth, YouTube podcasts and TED Talks include visual
cues. Although our hypotheses focus on textual emotion -
ality (Berger et al., 2021; Markowitz & Shulman, 2021),
emotional fluctuations can also be conveyed through tone,
facial expression, pacing, and editing. Future research
should examine emotionality flips in purely audio-based
formats (e.g., Spotify podcasts), other narrative forms (e.g.,
vlogs), and multimodal or short-form content (e.g., TikTok,
Instagram Reels). Understanding how emotional dynamics
manifest beyond text is increasingly important as platforms
evolve.
Supplementary Information The online version contains supplementary
material available at  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 0 7  / s 1  1 7 4 7 - 0 2 6 - 0 1 1 4 7 - 3.
Acknowledgements Not applicable.
Funding This research was supported by funding received from CER-
ESSEC.
Data availability Available from the first author.
Declarations
Ethical approval This research was approved by the ESSEC Business
School Research Ethics Committee (Ref: 2024-47).
Competing interest The authors declare that they have no competing
interests.
Open Access   This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format,
as long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate
if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless
indicated otherwise in a credit line to the material. If material is not
included in the article’s Creative Commons licence and your intended
use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright
holder. To view a copy of this licence, visit  h t t p  : / /  c r e a  t i  v e c  o m m o  n s .  o
r g  / l i c e n s e s / b y / 4 . 0 /.
References
Adaval, R., & Wyer, R. S., Jr. (1998). The role of narratives in con -
sumer information processing. Journal of Consumer Psychology,
7(3), 207–245.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  2 0 7  / s 1  5 3 2 7 6 6 3 j c p 0 7 0 3 _ 0 1
audiences, reduce trust in micro-influencers (Rizzo et al.,
2023b), or provoke discomfort with novel innovations
(Noseworthy et al., 2014). Thus, emotionality flips’ effec -
tiveness may hinge on an optimal match between arousal
dynamics, audience goals, and contextual factors.
Limitations and future research
Our research has several limitations that offer opportunities for
future inquiry. Although we examined processing fluency and
NFA as moderators, other factors—such as content type, plat-
form features, audience characteristics, and cultural context—
may also shape how emotionality flips influence engagement.
Emotionality flips may operate differently across genres (e.g.,
educational vs. entertainment), platforms (e.g., YouTube vs.
Spotify), or creator styles, and these structural differences may
interact with emotional dynamics in meaningful ways.
First, as shown in Study 4, audience characteristics are
particularly important. Arousal responses depend on expec-
tations shaped by familiarity with creators, prior engagement,
and individual preferences (Teixeira et al., 2012). Loyal fol-
lowers may interpret emotional shifts as intentional, whereas
audiences expecting consistency may find them jarring. Indi-
vidual differences in arousal sensitivity (Blascovich, 1990)
further suggest that some users seek emotionally dynamic
content while others avoid it. Future research should exam-
ine how such audience-level factors condition responses to
emotional structure in narrative content.
Second, cultural values may influence whether emotional
variation is interpreted positively or negatively. For instance,
Western audiences often view emotional dynamism as
engaging, whereas East Asian audiences tend to prefer emo-
tional restraint (Valenzuela et al., 2010). Investigating cross-
cultural differences in emotionality flip processing could
yield meaningful insights for global content strategies.
Third, past work shows that older adults rely more on
emotionally congruent cues (Noh & Isaacowitz, 2013) and
interpret ambiguity more positively (Shuster et al., 2017).
Gender differences may also matter (Kovacheva et al., 2022).
Our observational datasets lack demographic information,
limiting our ability to test these moderators directly. Study 3
provided an initial test and found no significant moderation
by age or gender, though exploratory floodlight analyses
suggested effects may emerge among older viewers. Future
research should explore demographic heterogeneity using
datasets with richer individual-level information.
Fourth, emotionality flips may not always be beneficial.
If content repeatedly generates emotional shifts, it may
exhaust audiences. Future work should examine whether
varying the frequency or intensity of flips affects fatigue,
enjoyment, and satisfaction, and identify optimal emotional
dynamics for sustained engagement.
1 3
1096

Journal of the Academy of Marketing Science (2026) 54:1080–1100
close social ties. Journal of Consumer Research, 50(4), 683–703.
h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 9 3  / j c  r / u c a d 0 1 9
Consiglio, I., De Angelis, M., & Costabile, M. (2018). The effect of
social density on word of mouth. Journal of Consumer Research.
h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 9 3  / j c  r / u c y 0 0 9
Cox, M., Harrison, H. L., Partelow, S., Curtis, S., Elser, S. R., Ham -
mond Wagner, C., et al. (2023). How academic podcasting can
change academia and its relationship with society: A conversation
and guide. Frontiers in Communication.  h t t p  s : /  / d o i  . o  r g /  1 0 . 3  3 8 9  /
f c  o m m . 2 0 2 3 . 1 0 9 0 1 1 2
Cramer-Flood, E. (2021). Global Podcast Listener Forecast 2021–
2025.  h t t p  s : /  / w w w  . e  m a r  k e t e  r . c  o m /  c o n  t e n  t / g l  o b  a l -  p o d c  a s t  - l i  s t e  n e
r  - f o r  e c  a s t - 2 0 2 1 - 2 0 2 5
Culler, J. D. (1981). The Pursuit of Signs: Semiotics, Literature,
Deconstruction (Ithaca.). NY: Cornell University Press.
Devereux, E., Grimmer, L., & Grimmer, M. (2020). Consumer engage-
ment on social media: Evidence from small retailers. Journal of
Consumer Behaviour, 19(2), 151–159.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 0 2  / c
b  . 1 8 0 0
Duarte, F. (2023a). TikTok Content Creator Statistics (2024).
Duarte, F. (2023b). YouTube Content Creator Statistics (2024).  h t t p  s : /
/ e x p  l o  d i n  g t o p  i c s  . c o  m / b  l o g  / y o u  t u  b e - c r e a t o r - s t a t s
Dubois, D., Bonezzi, A., & De Angelis, M. (2016). Sharing with
friends versus strangers: How interpersonal closeness influences
word-of-mouth valence. Journal of Marketing Research,  53(5),
712–727.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  5 0 9  / j m  r . 1 3 . 0 3 1 2
Ekman, P., Friesen, W. V ., & Ellsworth, P. (1972). Emotion in the
human face: Guidelines for research and an integration of find -
ings. Emotion in the human face: Guidelines for research and an
integration of findings., xii, 191–xii, 191.
Escalas, J. E. (2004a). Imagine yourself in the product: Mental simula-
tion, narrative transportation, and persuasion. Journal of Advertising,
33(2), 37–48.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 8 0  / 0 0  9 1 3  3 6 7  . 2 0 0  4 a  . 1 0 6 3 9 1 6 3
Escalas, J. E. (2004b). Narrative processing: Building consumer con -
nections to brands. Journal of Consumer Psychology,  14(1–2),
168–180.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  2 0 7  / s 1  5 3 2  7 6 6  3 j c p  1 4  0 1 & 2 _ 1 9
Escalas, J. E. (2007). Self-referencing and persuasion: Narrative trans-
portation versus analytical elaboration. Journal of Consumer
Research, 33(4), 421–429.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 8 6  / 5 1  0 2 1 6
Feiereisen, S., Rasolofoarison, D., Russell, C. A., & Schau, H. J.
(2021). One brand, many trajectories: Narrative navigation in
transmedia. Journal of Consumer Research, 48(4), 651–681.  h t t p
s : /  / d o i  . o  r g /  1 0 . 1  0 9 3  / j c  r / u c a a 0 4 6
Fischer, S. (2025). Axios Media Trends.  h t t p  s : /  / w w w  . a  x i o  s . c o  m / n  e w
s  l e t  t e r  s / a x  i o  s - m  e d i a  - t r  e n d  s - d  a 7 b  e 5 0 0  - 2  4 5 8  - 1 1 f  0 - b  8 9 e  - d 1 e 9 e 0 7
6 5 a 0 0
Fisk, J. E. (2002). Judgments under uncertainty: Representativeness
or potential surprise? British Journal of Psychology, 93(4), 431–
449.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  3 4 8  / 0 0  0 7 1 2 6 0 2 7 6 1 3 8 1 3 3 0
Flesch, R. (1948). A new readability yardstick. Journal of Applied Psy-
chology, 32(3), 221–233.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 3 7  / h 0  0 5 7 5 3 2
Forster, M., Leder, H., & Ansorge, U. (2016). Exploring the subjective
feeling of fluency. Experimental Psychology, 63(1), 45–58.  h t t p  s :
/  / d o i  . o  r g /  1 0 . 1  0 2 7  / 1 6  1 8 - 3 1 6 9 / a 0 0 0 3 1 1
Garcia, C. (2021). How to engage your audience.  h t t p  s : /  / c r e  a t  o r s  . g o o  g
l e  / e n  - u s  / c o  n t e n  t -  c r e  a t i o  n - g  u i d  e s /  a u d  i e n c  e -  e n g  a g e m  e n t  / e v  e r y  t h i  n
g - y  o u  - n e  e d - t  o - k  n o w  - a b o u t - a u d i e n c e - e n g a g e m e n t /
Gardner, J., & Lehnert, K. (2016). What’s new about new media? How
multi-channel networks work with content creators. Business
Horizons, 59(3), 293–302.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 1 6  / j .  b u s h o r . 2 0 1 6
. 0 1 . 0 0 9
Garfinkel, S. N., Minati, L., Gray, M. A., Seth, A. K., Dolan, R. J., &
Critchley, H. D. (2014). Fear from the heart: Sensitivity to fear
stimuli depends on individual heartbeats. The Journal of Neuro-
science, 34(19), 6573.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  5 2 3  / J N  E U R  O S C  I . 3 5  0
7  - 1 3 . 2 0 1 4
Adobe Express (2024). 9 tested tips to boost your Instagram engage -
ment in 2025.  h t t p  s : /  / w w w  . a  d o b  e . c o  m / e  x p r  e s s  / l e  a r n /  b l  o g /  i n s t  a g r
a m -  e n g a g e m e n t
Alter, A. L., & Oppenheimer, D. M. (2009). Uniting the tribes of flu -
ency to form a metacognitive nation. Personality and Social Psy-
chology Review, 13(3), 219–235.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 7 7  / 1 0  8 8 8 6
8 3 0 9 3 4 1 5 6 4
Appel, M., Gnambs, T., & Maio, G. R. (2012). A short measure of the
need for affect. Journal of Personality Assessment , 94(4), 418–
426.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 8 0  / 0 0  2 2 3 8 9 1 . 2 0 1 2 . 6 6 6 9 2 1
Argo, J. J., Zhu, R., & Dahl, D. W. (2008). Fact or fiction: An inves -
tigation of empathy differences in response to emotional melo -
dramatic entertainment. Journal of Consumer Research,  34(5),
614–623.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 8 6  / 5 2  1 9 0 7
Backlinko Team (2024). 13 Podcast Statistics You Need To Know.  h t t
p  s : /  / b a c  k l  i n k  o . c o  m / p  o d c  a s t  - s t  a t s #  p o  d c a s t - g r o w t h
Berger, J. (2011). Arousal increases social transmission of information.
Psychological Science, 22(7), 891–893.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 7 7  / 0
9  5 6 7 9 7 6 1 1 4 1 3 2 9 4
Berger, J. (2014). Word of mouth and interpersonal communication: A
review and directions for future research. Journal of Consumer
Psychology, 24(4), 586–607.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 1 6  / j .  j c p s . 2 0 1 4
. 0 5 . 0 0 2
Berger, J., Kim, Y . D., & Meyer, R. (2021). What makes content
engaging? How emotional dynamics shape success. Journal of
Consumer Research, 48(2), 235–250.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 9 3  / j c  r
/ u c a b 0 1 0
Berger, J., & Milkman, K. L. (2012). What makes online content viral?
Journal of Marketing Research , 49(2), 192–205.  h t t p  s : /  / d o i  . o  r g /
1 0 . 1  5 0 9  / j m  r . 1 0 . 0 3 5 3
Berger, J., Moe, W. W., & Schweidel, D. A. (2023). What holds atten-
tion? Linguistic drivers of engagement. Journal of Marketing,
87(5), 793–809.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 7 7  / 0 0  2 2 2 4 2 9 2 3 1 1 5 2 8 8 0
Berlyne, D. E. (1966). Curiosity and exploration. Science, 153(3731),
25–33.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 2 6  / s c  i e n c e . 1 5 3 . 3 7 3 1 . 2 5
Bestgen, Y . (1994). Can emotional valence in stories be determined
from words? Cognition and Emotion, 8(1), 21–36.  h t t p  s : /  / d o i  . o  r g
/  1 0 . 1  0 8 0  / 0 2  6 9 9 9 3 9 4 0 8 4 0 8 9 2 6
Blascovich, J. (1990). Individual differences in physiological arousal
and perception of arousal: Missing links in Jamesian notions of
arousal-based behaviors. Personality and Social Psychology Bul-
letin, 16(4), 665–675.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 7 7  / 0 1  4 6 1 6 7 2 9 0 1 6 4 0 0 7
Boyd, R. L., Blackburn, K. G., & Pennebaker, J. W. (2020). The narra-
tive arc: Revealing core narrative structures through text analysis.
Science Advances, 6(32), Article eaba2196.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1
2 6  / s c  i a d v . a b a 2 1 9 6
Campbell, M. C., & Kirmani, A. (2000). Consumers’ use of persuasion
knowledge: The effects of accessibility and cognitive capacity on
perceptions of an influence agent. Journal of Consumer Research,
27(1), 69–83.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 8 6  / 3 1  4 3 0 9
Cascio Rizzo, G. L., Berger, J., De Angelis, M., & Pozharliev, R.
(2023a). How sensory language shapes influencer’s impact. Jour-
nal of Consumer Research, 50(4), 810–825.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0
9 3  / j c  r / u c a d 0 1 7
Cascio Rizzo, G. L., Ordenes, V ., Pozharliev, F., De Angelis, R., M.,
& Costabile, M. (2023b). How High-Arousal Language shapes
Micro- versus Macro-Influencers’ impact. Journal of Marketing,
00222429231207636.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 7 7  / 0 0  2 2 2 4 2 9 2 3 1 2 0 7 6
3 6
Chatman, S. (1978). Story and discourse: Narrative structure in fiction
and film. NY: Cornell University Press.
Chen, Z., & Berger, J. (2013). When, why, and how controversy causes
conversation. Journal of Consumer Research, 40(3), 580–593.  h t
t p  s : /  / d o i  . o  r g /  1 0 . 1  0 8 6  / 6 7  1 4 6 5
Chung, J., Ding, Y ., & Kalra, A. (2023). I really know you: How influ-
encers can increase audience engagement by referencing their
1 3
1097

Journal of the Academy of Marketing Science (2026) 54:1080–1100
influencers. International Journal of Advertising (3).  h t t p  s : /  / d o i  .
o  r g /  1 0 . 1  0 8 0  / 0 2  6 5 0  4 8 7  . 2 0 2  4 .  2 3 8 6 9 1 6
KLERES, J. (2011). Emotions and narrative analysis: A methodologi-
cal approach. Journal for the Theory of Social Behaviour , 41(2),
182–202.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 1 1  / j .  1 4 6  8 - 5  9 1 4 .  2 0  1 0 . 0 0 4 5 1 . x
Kovacheva, A., Nikolova, H., & Lamberton, C. (2022). Will he buy a
surprise? Gender differences in the purchase of surprise offerings.
Journal of Retailing, 98(4), 667–684.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 1 6  / j .  j r
e t a i . 2 0 2 2 . 0 4 . 0 0 2
Kozinets, R. V ., Gretzel, U., & Gambetti, R. (2023). Influencers and
Creators: Business, Culture and Practice. Sage Publications.
Krause-Galoni, R., & Rucker, D. D. (2024). Fact versus fiction: Blend-
ing storytelling with product attributes in advertisements. Journal
of the Association for Consumer Research, 9(1), 58–70.  h t t p  s : /  / d
o i  . o  r g /  1 0 . 1  0 8 6  / 7 2  7 8 3 5
Kumar, N. (2025). 32 + Creator Economy Statistics of 2025 (Market
Size Data).  h t t p  s : /  / w w w  . d  e m a  n d s a  g e .  c o m  / c r  e a t  o r - e  c o  n o m y - s t a t i
s t i c s /
Lacka, E., Boyd, D. E., Ibikunle, G., & Kannan, P. K. (2022). Measur-
ing the real-time stock market impact of firm-generated content.
Journal of Marketing,  86(5), 58–78.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 7 7  / 0 0  2
2 2 4 2 9 2 1 1 0 4 2 8 4 8
Lanz, A., Goldenberg, J., Shapira, D., & Stahl, F. (2024). Buying
future endorsements from prospective influencers on user-gener -
ated content platforms. Journal of Marketing Research, , Article
00222437231207323.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 7 7  / 0 0  2 2 2 4 3 7 2 3 1 2 0 7 3
2 3
Lee, J. K. (2021). Emotional expressions and brand status. Journal of
Marketing Research, 58(6), 1178–1196.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 7 7  / 0
0  2 2 2 4 3 7 2 1 1 0 3 7 3 4 0
Lei, A., Willems, R. M., & Eekhof, L. S. (2023). Emotions, fast and
slow: Processing of emotion words is affected by individual dif -
ferences in need for affect and narrative absorption. Cognition
and Emotion, 37(5), 997–1005.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 8 0  / 0 2  6 9 9  9 3
1  . 2 0 2  3 .  2 2 1 6 4 4 5
Leung, F. F., Gu, F. F., Li, Y ., Zhang, J. Z., & Palmatier, R. W. (2022a).
Influencer marketing effectiveness. Journal of Marketing, 86(6),
93–115.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 7 7  / 0 0  2 2 2 4 2 9 2 2 1 1 0 2 8 8 9
Leung, F. F., Gu, F. F., & Palmatier, R. W. (2022b). Online influencer
marketing. Journal of the Academy of Marketing Science,  50(2),
226–251.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 0 7  / s 1  1 7 4 7 - 0 2 1 - 0 0 8 2 9 - 4
Li, C., Xie, M., & Wang, M. (2021). Understanding user engagement
in online communities during COVID-19 pandemic . Evidence
from Sentiment and Semantic Analysis on YouTube.
Lin, Y ., Yao, D., & Chen, X. (2021). Happiness begets money: Emo-
tion and engagement in live streaming. Journal of Marketing
Research, 58(3), 417–438.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 7 7  / 0 0  2 2 2 4 3 7 2 1 1
0 0 2 4 7 7
Maio, G. R., & Esses, V . M. (2001). The need for affect: Individual dif-
ferences in the motivation to approach or avoid emotions. Journal
of Personality, 69(4), 583–615.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 1 1  / 1 4  6 7 - 6 4 9
4 . 6 9 4 1 5 6
Mandler, G. (1982). The Structure of Value: Accounting for Taste. In
M. S. Clark & S. T. Fiske (Eds.), Affect and Cognition: The Sev-
enteenth Annual Carnegie Symposium on Cognition  (pp. 3–36).
Erlbaum.
Mardon, R., Cocker, H., & Daunt, K. (2023). How social media influ-
encers impact consumer collectives: An embeddedness perspec -
tive. Journal of Consumer Research, 50(3), 617–644.  h t t p  s : /  / d o i  .
o  r g /  1 0 . 1  0 9 3  / j c  r / u c a d 0 0 3
Markowitz, D. M. (2023). Instrumental goal activation increases
online petition support across languages. Journal of Personality
and Social Psychology, 124(6), 1133–1145.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0
3 7  / p s  p a 0 0 0 0 3 3 3
Markowitz, D. M., & Shulman, H. C. (2021). The predictive util -
ity of word familiarity for online engagements and funding.
Gee, J. P., & Grosjean, F. (1984). Empirical evidence for narrative
structure. Cognitive Science, 8(1), 59–85.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 1
6  / S 0  3 6 4 - 0 2 1 3 ( 8 4 ) 8 0 0 2 5 - 7
Goldenberg, J., Lanz, A., Shapira, D., & Stahl, F. (2023). Target -
ing nearby influencers: The acceleration of natural triadic clo -
sure by leveraging interconnectors. Journal of Marketing ,
00222429231223420.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 7 7  / 0 0  2 2 2 4 2 9 2 3 1 2 2 3
4 2 0
Goldman Sachs (2023). The creator economy could approach half-a-
trillion dollars by 2027.  h t t p  s : /  / w w w  . g  o l d  m a n s  a c h  s . c  o m /  i n t  e l l i  g e
n c e  / p a g  e s /  t h e  - c r  e a t  o r - e  c o  n o m  y - c o  u l d  - a p  p r o  a c h  - h a l  f -  a - t  r i l l  i o n  - d
o  l l a r s - b y - 2 0 2 7 . h t m l
Green, M., & Brock, T. (2000). The role of transportation in the per -
suasiveness of public narrative. Journal of Personality and Social
Psychology, 79, 701–721.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 3 7  / 0 0  2 2 - 3 5 1 4 . 7 9
. 5 . 7 0 1
Green, M. C. (2008). Transportation theory. The international encyclo-
pedia of communication.
Gu, X., Zhang, X., & Kannan, P. K. (2024). Influencer mix strategies in
livestream commerce: Impact on product sales. Journal of Mar-
keting, 88(4), 64–83.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 7 7  / 0 0  2 2 2 4 2 9 2 3 1 2 1 3 5 8
1
Haddock, G., & Maio, G. R. (2019). Inter-individual differences in
attitude content: Cognition, affect, and attitudes. Advances in
Experimental Social Psychology , 59, 53–102.  h t t p  s : /  / d o i  . o  r g /  1 0
. 1  0 1 6  / b s  . a e s p . 2 0 1 8 . 1 0 . 0 0 2
Hamby, A., & Brinberg, D. (2016). Happily ever after: How ending
valence influences narrative persuasion in cautionary stories.
Journal of Advertising,  45(4), 498–508.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 8 0  /
0 0  9 1 3  3 6 7  . 2 0 1  6 .  1 2 6 2 3 0 2
Hamby, A., & Escalas, J. E. (2024). Connecting the plot points: How
consumers use and respond to narratives. Journal of the Associa-
tion for Consumer Research,  9(1), 1–8.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 8 6  /
7 2  7 8 2 9
Hartmann, J., Heitmann, M., Schamp, C., & Netzer, O. (2021). The
power of brand selfies. Journal of Marketing Research , 58(6),
1159–1177.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 7 7  / 0 0  2 2 2 4 3 7 2 1 1 0 3 7 2 5 8
Hayes, A. F. (2022). Introduction to Mediation, Moderation, and Con-
ditional Process Analysis: A Regression-Based Approach  (third
edition.). The Guilford Press.
Heilman, K. M. (1997). The neurobiology of emotional experience.
The Journal of Neuropsychiatry and Clinical Neurosciences,
9(3), 439–448.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 7 6  / j n  p . 9 . 3 . 4 3 9
Herzenstein, M., Sonenshein, S., & Dholakia, U. M. (2011). Tell me a
good story and I may lend you money: The role of narratives in
peer-to-peer lending decisions. Journal of Marketing Research,
48(SPL), S138–S149.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  5 0 9  / j m  k r . 4 8 . S P L . S 1 3 8
Hough, Q. (2019). Why The Red Wedding Is Still Game of Thrones’
Most Shocking Moment.  h t t p  s : /  / s c r  e e  n r a  n t . c  o m /  r e d  - w e  d d i  n g - g  a
m  e - t  h r o n  e s -  s h o  c k i n g - m o m e n t /
Howarth, J. (2024). 30 + Incredible Creator Economy Statistics (2024).
h t t p  s : /  / e x p  l o  d i n  g t o p  i c s  . c o  m / b  l o g  / c r e  a t  o r - e c o n o m y - s t a t s
Huang, M.-H., & Rust, R. T. (2025). The GenAI future of consumer
research. Journal of Consumer Research, 52(1), 4–17.  h t t p  s : /  / d o i
. o  r g /  1 0 . 1  0 9 3  / j c  r / u c a f 0 1 3
Hutto, C., & Gilbert, E. (2014). Vader: A parsimonious rule-based
model for sentiment analysis of social media text. In Proceedings
of the international AAAI conference on web and social media
(V ol. 8, pp. 216–225).
Jiang, H., Messinger, P. R., Liu, Y ., Lu, Z., Yang, S., & Li, G. (2024).
Divergent versus relevant ads: How creative ads affect purchase
intention for new products. Journal of Marketing Research,
61(2), 271–289.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 7 7  / 0 0  2 2 2 4 3 7 2 3 1 1 8 7 6 3 0
Kim, E., Shoenberger, H., Kim, D., Thorson, E., & Zihang, E. (2024).
Novelty vs. trust in virtual influencers: Exploring the effective -
ness of human-like virtual influencers and anime-like virtual
1 3
1098

Journal of the Academy of Marketing Science (2026) 54:1080–1100
Schuster, S., Hawelka, S., Hutzler, F., Kronbichler, M., & Richlan, F.
(2016). Words in context: The effects of Length, Frequency, and
predictability on brain responses during natural reading. Cerebral
Cortex, 26(10), 3889–3904.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 9 3  / c e  r c o r / b h w 1
8 4
Schwarz, N. (2000). Emotion, cognition, and decision making. Cogni-
tion and Emotion , 14(4), 433–440.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 8 0  / 0 2  6 9
9 9 3 0 0 4 0 2 7 4 5
Seiler, S., Yao, S., & Wang, W. (2017). Does online word of mouth
increase demand? (And how?) Evidence from a natural experi -
ment. Marketing Science, 36(6), 838–861.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  2 8
7  / m k  s c . 2 0 1 7 . 1 0 4 5
Sepehri, A., Duclos, R., & Haghighi, N. (2025). Ideas worth spread -
ing? When, how, and for whom information load hurts online
talks’ popularity. Journal of Personality and Social Psychology ,
128(2), 281–299.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 3 7  / p s  p a 0 0 0 0 4 3 0
Sepehri, A., Markowitz, D. M., & Duclos, R. (2021). The location of
maximum emotion in deceptive and truthful texts. Social Psycho-
logical and Personality Science, 12(6), 996–1004.  h t t p  s : /  / d o i  . o  r g
/  1 0 . 1  1 7 7  / 1 9  4 8 5 5 0 6 2 0 9 4 9 7 3 0
Shuster, M. M., Mikels, J. A., & Camras, L. A. (2017). Adult age
differences in the interpretation of surprised facial expressions.
Emotion, 17(2), 191–195.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 3 7  / e m  o 0 0 0 0 2 3 4
Somervail, R., Zhang, F., Novembre, G., Bufacchi, R. J., Guo, Y .,
Crepaldi, M., et al. (2021). Waves of change: Brain sensitivity to
differential, not absolute, stimulus intensity is conserved across
humans and rats. Cerebral Cortex, 31(2), 949–960.  h t t p  s : /  / d o i  . o  r
g /  1 0 . 1  0 9 3  / c e  r c o r / b h a a 2 6 7
Spiller, S. A., Fitzsimons, G. J., Lynch, J. G., & Mcclelland, G. H.
(2013). Spotlights, floodlights, and the magic number zero: Sim -
ple effects tests in moderated regression. Journal of Marketing
Research, 50(2), 277–288.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  5 0 9  / j m  r . 1 2 . 0 4 2 0
Spotify (2024). How to grow your podcast audience.  h t t p  s : /  / c r e  a t  o r s  . s
p o  t i f  y . c  o m /  r e s  o u r c  e s  / g r o w / g r o w - a u d i e n c e
Stroud, N. J., & Muddiman, A. (2019). Social media engagement with
strategy- and issue-framed political news. Journal of Communi -
cation, 69(5), 443–466.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 9 3  / j o  c / j q z 0 2 9
Teigen, K. H., & Keren, G. (2003). Surprises: Low probabilities or
high contrasts? Cognition, 87(2), 55–71.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 1 6
/ s 0  0 1 0 - 0 2 7 7 ( 0 2 ) 0 0 2 0 1 - 9
Teixeira, T., Wedel, M., & Pieters, R. (2012). Emotion-induced
engagement in internet video advertisements. Journal of Market-
ing Research, 49(2), 144–159.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  5 0 9  / j m  r . 1 0 . 0 2
0 7
Tellis, G. J., MacInnis, D. J., Tirunillai, S., & Zhang, Y . (2019). What
drives virality (sharing) of online digital content? The critical role
of information, emotion, and brand prominence. Journal of Mar-
keting, 83(4), 1–20.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 7 7  / 0 0  2 2 2 4 2 9 1 9 8 4 1 0 3 4
Torta, D., Ninghetto, M., Ricci, R., & Legrain, V . (2020). Rating the
intensity of a laser stimulus, but not attending to changes in its
location or intensity modulates the laser-evoked cortical activity.
Frontiers in Human Neuroscience.  h t t p  s : /  / d o i  . o  r g /  1 0 . 3  3 8 9  / f n  h u m
. 2 0 2 0 . 0 0 1 2 0
Toubia, O., Berger, J., & Eliashberg, J. (2021). How quantifying
the shape of stories predicts their success. Proceedings of the
National Academy of Sciences, 118(26), Article e2011695118.  h t t
p  s : /  / d o i  . o  r g /  1 0 . 1  0 7 3  / p n  a s . 2 0 1 1 6 9 5 1 1 8
Toubia, O., Gui, G. Z., Peng, T., Merlau, D. J., Li, A., & Chen, H.
(2025). Database report: Twin-2K-500: A data set for building
digital twins of over 2,000 people based on their answers to over
500 questions. Marketing Science.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  2 8 7  / m k  s c .
2 0 2 5 . 0 2 6 2
Valenzuela, A., Mellers, B., & Strebel, J. (2010). Pleasurable surprises:
A cross-cultural study of consumer responses to unexpected
incentives. Journal of Consumer Research, 36, 792–805.  h t t p  s : /  /
d o i  . o  r g /  1 0 . 1  0 8 6  / 6 0  5 5 9 2
Proceedings of the National Academy of Sciences, 118(18), Arti-
cle e2026045118.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 7 3  / p n  a s . 2 0 2 6 0 4 5 1 1 8
Marsh, E., & Fazio, L. (2006). Learning errors from fiction: Difficul -
ties in reducing reliance on fictional stories. Memory & Cogni -
tion, 34, 1140–1149.  h t t p  s : /  / d o i  . o  r g /  1 0 . 3  7 5 8  / B F  0 3 1 9 3 2 6 0
Melumad, S., Inman, J. J., & Pham, M. T. (2019). Selectively emo -
tional: How smartphone use changes user-generated content.
Journal of Marketing Research, 56(2), 259–275.  h t t p  s : /  / d o i  . o  r g /  1
0 . 1  1 7 7  / 0 0  2 2 2 4 3 7 1 8 8 1 5 4 2 9
Milkman, K. L., & Berger, J. (2014). The science of sharing and the
sharing of science. Proceedings of the National Academy of Sci -
ences, 111(supplement_4), 13642–13649.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 7 3
/ p n  a s . 1 3 1 7 5 1 1 1 1 1
Morin, O., & Acerbi, A. (2017). Birth of the cool: A two-centuries
decline in emotional expression in Anglophone fiction. Cognition
and Emotion, 31(8), 1663–1675.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 8 0  / 0 2  6 9 9  9
3 1  . 2 0 1  6 .  1 2 6 0 5 2 8
Mosley, B., Schweidel, D. A., & Zhang, K. (2024). When connec -
tion turns to anger: How consumer–brand relationship and crisis
type moderate language on social media. Journal of Consumer
Research, 50(5), 907–922.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 9 3  / j c  r / u c a d 0 2 7
Nell, V . (1988). Lost in a Book. Yale University Press.  h t t p  s : /  / d o i  . o  r g /
1 0 . 2  3 0 7  / j .  c t t 1 w w 3 v k 3
Nielsen, J. H., & Escalas, J. E. (2010). Easier is not always better: The
moderating role of processing type on preference fluency. Journal
of Consumer Psychology, 20(3), 295–305.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 1
6  / j .  j c p s . 2 0 1 0 . 0 6 . 0 1 6
Noh, S. R., & Isaacowitz, D. M. (2013). Emotional faces in context:
Age differences in recognition accuracy and scanning patterns.
Emotion, 13(2), 238–249.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 3 7  / a 0  0 3 0 2 3 4
Noseworthy, T. J., Di Muro, F., & Murray, K. B. (2014). The role of
arousal in congruity-based product evaluation. Journal of Con -
sumer Research, 41(4), 1108–1126.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 8 6  / 6 7  8
3 0 1
Packard, G., Berger, J., & Boghrati, R. (2023). How verb tense shapes
persuasion. Journal of Consumer Research, 50(3), 645–660.  h t t p
s : /  / d o i  . o  r g /  1 0 . 1  0 9 3  / j c  r / u c a d 0 0 6
Pancer, E., Chandler, V ., Poole, M., & Noseworthy, T. J. (2019). How
readability shapes social media engagement. Journal of Con -
sumer Psychology, 29(2), 262–270.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 0 2  / j c  p y
. 1 0 7 3
Papies, D., Ebbes, P., & van Heerde, H. (2017). Addressing Endogene-
ity in Marketing Models (pp. 581–627).  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 0 7  / 9
7  8 - 3 - 3 1 9 - 5 3 4 6 9 - 5 _ 1 8
Park, S., & Gupta, S. (2012). Handling endogenous regressors by joint
estimation using copulas. Marketing Science, 31(4), 567–586.
Peres, R., Schreier, M., Schweidel, D. A., & Sorescu, A. (2024).
The creator economy: An introduction and a call for scholarly
research. International Journal of Research in Marketing, 41(3),
403–410.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 1 6  / j .  i j r  e s m  a r . 2  0 2  4 . 0 7 . 0 0 5
Perse, E. (1998). Implications of cognitive and affective involvement
for channel changing. Journal of Communication, 48(3), 49–68.
h t t p  s : /  / d o i  . o  r g /  1 0 . 1  1 1 1  / j .  1 4 6  0 - 2  4 6 6 .  1 9  9 8 . t b 0 2 7 5 9 . x
Peterson, T. (2024). Why longer videos are becoming more common -
place on YouTube.  h t t p  s : /  / d i g  i d  a y .  c o m /  f u t  u r e  - o f  - t v  / w h y  - l  o n g  e r - v
i d e  o s -  a r e  - b e  c o m i  n g  - m o  r e - c  o m m  o n p  l a c e - o n - y o u t u b e /
Pham, M. T. (1998). Representativeness, relevance, and the use of feel-
ings in decision making. Journal of Consumer Research,  25(2),
144–159.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 8 6  / 2 0  9 5 3 2
Ptaszynski, M., Dokoshi, H., Oyama, S., Rzepka, R., Kurihara, M.,
Araki, K., & Momouchi, Y . (2013). Affect analysis in context of
characters in narratives. Expert Systems with Applications, 40(1),
168–176.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 1 6  / j .  e s w a . 2 0 1 2 . 0 7 . 0 2 5
Schachter, S., & Singer, J. (1962). Cognitive, social, and physiologi -
cal determinants of emotional state. Psychological Review, 69(5),
379–399.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  0 3 7  / h 0  0 4 6 2 3 4
1 3
1099

Journal of the Academy of Marketing Science (2026) 54:1080–1100
Whiteford, K. L., & Oxenham, A. J. (2023). Sensitivity to frequency
modulation is limited centrally. The Journal of Neuroscience,
43(20), 3687.  h t t p  s : /  / d o i  . o  r g /  1 0 . 1  5 2 3  / J N  E U R  O S C  I . 0 9  9 5  - 2 2 . 2 0
2 3
Yin, D., Bond, S. D., & Zhang, H. (2017). Keep your cool or let it
out: Nonlinear effects of expressed arousal on perceptions of con-
sumer reviews. Journal of Marketing Research, 54(3), 447–463.
h t t p  s : /  / d o i  . o  r g /  1 0 . 1  5 0 9  / j m  r . 1 3 . 0 3 7 9
Yuan, H., Che, Z., Li, S., Zhang, Y ., Hu, X., & Luo, S. (2024). The high
dimensional psychological profile and cultural bias of ChatGPT.
arXiv, abs/2405.03387,
Publisher’s note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional affiliations.
Van Boven, L., Kane, J., Mcgraw, A. P., & Dale, J. (2010). Feeling
close: Emotional intensity reduces perceived psychological dis -
tance. SSRN Electronic Journal .  h t t p  s : /  / d o i  . o  r g /  1 0 . 2  1 3 9  / s s  r n . 1 5
3 1 6 6 1
van Laer, T., de Ruyter, K., Visconti, L. M., & Wetzels, M. (2014). The
extended transportation-imagery model: A meta-analysis of the
antecedents and consequences of consumers’ narrative transpor -
tation. Journal of Consumer Research, 40(5), 797–817.  h t t p  s : /  / d
o i  . o  r g /  1 0 . 1  0 8 6  / 6 7  3 3 8 3
van Laer, T., Edson Escalas, J., Ludwig, S., & van den Hende, E. A.
(2019). What happens in Vegas stays on TripAdvisor? A theory
and technique to understand narrativity in consumer reviews.
Journal of Consumer Research,  46(2), 267–285.  h t t p  s : /  / d o i  . o  r g /
1 0 . 1  0 9 3  / j c  r / u c y 0 6 7
1 3
1100
