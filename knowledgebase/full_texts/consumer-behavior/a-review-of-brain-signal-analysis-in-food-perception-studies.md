---
title: A review of brain signal analysis in food perception studies
url: https://doi.org/10.11591/ijai.v15.i4.pp3967-3980
category: consumer-behavior
subcategory: review
date: 2026-08
venue: IAES International Journal of Artificial Intelligence
authors:
- Harish Velingkar
- Roopa R. Kulkarni
- Prashant P. Patavardhan
source: openalex-oa
pdf_url: https://ijai.iaescore.com/index.php/IJAI/article/download/29594/15361
pages: 14
chars: 59387
fetched_at: '2026-11-08T18:23:31+00:00'
kb_version: 1
---

# A review of brain signal analysis in food perception studies

IAES International Journal of Artificial Intelligence (IJ-AI)
Vol. 15, No. 4, August 2026, pp. 3967~3980
ISSN: 2252-8938, DOI: 10.11591/ijai.v15.i4.pp3967-3980      3967

Journal homepage: http://ijai.iaescore.com
A review of brain signal analysis in food perception studies

Harish S. Sinai Velingkar1, Roopa R. Kulkarni2, Prashant Patavardhan3, Abdul Haq Nalband4
1Department of Electronics and Communication, Agnel Institute of Technology and Design, Visvesvaraya Technological University,
Belagavi, India
2Department of Electronics and Communication Engineering, Dayananda Sagar Academy of Technology and Management,
Belagavi, India
3Department of Electronics and Communication Engineering, RV Institute of Technology and Management, Bengaluru, India
4Department of Computer Science and Engineering (AI and ML), School of Engineering, Dayananda Sagar University, Bengaluru, India

Article Info  ABSTRACT
Article history:
Received Jul 4, 2025
Revised Jul 15, 2026
Accepted Jul 21, 2026

 Food perception is more than just taste. It is a multisensory experience
shaped by smell, texture , and even how the food looks. The human brain
works to make sense of all these signals, influencing everything from
cravings to food choices. This review looks at more than 40 studies that used
electroencephalography (EEG) and other brainwave analysis tools to
understand how to process food related stimuli. In order to identify patterns
associated with attention, mood , and appetite, these studies looked at brain
responses using techniques including event related potentials  (ERPs) and
spectral analysis. Current research shows that human desire for food, level
of focus on it , and the feelings it evokes are all correlated with certain brain
signals. However, majority of the studies investigated individual senses in
isolation and focused on basic taste attributes such as sweet, salty , or bitter.
The complexity of eating in real life, where several senses interact, is missed
by this. Furthermore, a lot of research is lab based, short term , and does not
represent real world situations.  Future research must adopt practical,
multimodal methods in order to fully understand how humans perceive food.
Such studies could help improve food design, predict consumer behavior,
and even support interventions for eating disorders.
Keywords:
Brain computer interface
Cognitive neuroscience
Consumer behavior
Electroencephalography
Event related potentials
Multisensory perception
Neurophysiological
This is an open access article under the CC BY-SA license.

Corresponding Author:
Harish S. Sinai Velingkar
Department of Electronics and Communication, Agnel Institute of Technology and Design
Visvesvaraya Technological University
Belagavi, India
Email: harishvelingkar@gmail.com

1. INTRODUCTION
Food is not just a source of energy; it  is also a rich mental and sensory experience that the brain
makes sense of by combining different signals. The human brain reacts to food through complicated neural
dynamics because billions of neurons talk to each other through electrical activity.  Electroencephalography
(EEG) is a widely used non -invasive technique for recording brain s electrical activity associated with
perception, attention , and emotion s. Different mental states are linked to different frequency bands. For
example, beta waves (13 –30 Hz) are most common during focused cognitive activity, especially in the front
of the brain; alpha waves (8–13 Hz) are most common during relaxed alertness, often in the back of the brain;
theta waves (4 –8 Hz) are most common during drowsiness or light sleep; and delta waves (0.5 –4 Hz) are
most common during deep sleep [1], [2].
The physiological foundation for understanding how the brain reacts to everyday experiences like
eating is provided by these neural rhythms.  Sight, smell, taste, texture , and even human expectations of the

                ISSN: 2252-8938
Int J Artif Intell, Vol. 15, No. 4, August 2026: 3967-3980
3968
food about to taste  are all a part of the multimodal process of eating. Different kinds of sensory information
stimulate different brain regions. For example, taste activates the insular cortex, texture activates the
somatosensory areas and reward and value stimulates the orbitofrontal cortex (OFC). Together, these regions
influence the perception and emotional reaction to food [3]. Instead of processing these attributes
independently, the distributed neural networks combine them to produce a single eating experience [4]. The
effect of sensory cues on emotional and cognitive responses related to food perception, consumer preference ,
and appetite regulation have been extensively studied using EEG and brain imaging techniques [5], [6].
Another commonly used tool in cognitive research is functional magnetic resonance imaging
(fMRI). Using fMRI studies, we may gain a deeper understanding of how the brain interprets sensory and
branding cues. Due to its relatively slower timing resolution (seconds), high power consumption , and a
constrained motion limited scanner environment, the fMRI technique is less suitable for natural eating or real
world sensory tasks, even though it offers high spatial detail (millimeter  level), which is great for identifying
specific areas [7].
EEG on the other hand is more reliable for researching rapid sensory reactions, taste memory and
attention shifts since it records brain activity at millisecond speeds, uses relatively low power and can be used
in a seated, movement  tolerant arrangement s. Studies combining EEG  and fMRI show that the brain
connectome patterns are repeatable from 1.5  T to 7  T scanners [8] and that EEG's strength resides in
recording rapid neural changes [9] despite the fact that EEG is more sensitive to motion and muscle artefacts.
Also majority of the research that is available focuses on basic lab stimuli and fundamental taste categories
like sweet or bitter, despite the growing interest in brain research related to food. As demonstrated by
Warnakulasooriya et al. [10] who used EEG and modern artificial intelligence (AI) techniques to assess the
sensory qualities of food, recent approaches have also combined brainwave analysis with other computational
tools for food evaluation.
However, real world meals are far more intricate. It is influenced by the situations in which human
beings the food, the surroundings, the individual's personality and integrate numerous other sensory elements
simultaneously [11]. This leads to major gaps in our understanding of how the brain processes complex, real
world food experiences.
Studying these gaps is crucial for improving cognitive neuroscience as well as for managing
disordered eating, developing nutrition plans, and designing healthier food  alternatives. In order to examine
how the brain interprets taste, smell, touch , and visual cues independently , and also in conjunction with a
broader multisensory experience, this review combines findings from more than 40 peer -reviewed studies.
The review is divided into three main sections: how various senses interact with one another , how
multisensory integration functions and the new research gaps that need to be filled with a focus on the need
for real world and ecologically valid investigations.

2. MATERIALS AND METHODS
The background for the EEG based investigations examined in this article is provided by Figure 1,
which summarizes the key EEG frequency bands and the cognitive and behavioral states that are frequently
associated with them. A typical EEG data collection protocol used in food perception research is shown in
Figure 2, which includes electrode placement, sensory stimulation, signal acquisition , and subsequent signal
analysis. In compliance with the preferred reporting items for systematic reviews and meta analyses (PRISMA)
guidelines [12], a systematic literature review was conducted to identify studies related to neurophysiological
processing of food related multisensory stimuli using EEG and other related methodologies.

2.1.  Search strategy and data sources
A systematic search was conducted across the various platforms such as PubMed, Web of Science,
and Scopus databases. Recent studies in multimodal neuroscience and EEG  based food perception published
between 2015 and 2025 were included in the search . The following terms and Boolean combinations were
used: “EEG”, “food perception”,  “taste”, “texture”, “smell”, “visual cues ”, “multisensory integration ”,
“event-related potentials”, and “consumer behavior”. This study used synonyms and variations to ensure that
all relevant literature was covered.

2.2.  Study selection and screening
290 records were found in the initial search: 150 from Scopus, 55 from Web of Science , and
85 from PubMed. After eliminating any duplicates, 210 unique articles remained. To eliminate research
unrelated to food perception, multisensory processing , or neurophysiological data , this study further filtered
the titles and abstracts. As a result , 60 irrelevant records were further eliminated. The whole text of the
remaining 150 articles was screened.

Int J Artif Intell  ISSN: 2252-8938 

A review of brain signal analysis in food perception studies (Harish S. Sinai Velingkar)
3969
2.3.  Inclusion and exclusion criteria
Studies that explored food related sensory stimuli like taste, texture, smell, visual cues , or their
combinations, used EEG or other comparable neurophysiological techniques, were published as peer-reviewed
journal publications, and included any human subjects were included in the review. Studies that focused only on
animal models, did not include food related stimuli, lacked neurophysiological measurements , or were purely
review articles, editorials, or conference abstracts with incomplete data were excluded from this study.

Figure 1. Correlation between EEG waveforms and emotional states

Figure 2. EEG data acquisition protocol for food perception studies

2.4.  Eligibility and final selection
40 studies that satisfied all  the eligibility requirements after full  text evaluation were added to the
final qualitative synthesis. Figure 3 shows the PRISMA flow diagram and illustrates the selection process.
The clarity of the experimental design, participant information, EEG acquisition techniques , and result
reporting were all examined to qualitatively examine the methodological quality of the included research.
Because the experimental procedures, outcome measurements, and analysis techniques varied across
the different studies. Therefore, a quantitative meta -analysis was not feasible. Instead, a thematic qualitative
synthesis was used to identify consistent neurophysiological patterns associated with multisensory perception
of food.

                ISSN: 2252-8938
Int J Artif Intell, Vol. 15, No. 4, August 2026: 3967-3980
3970

Figure 3. PRISMA flow diagram of the study screening and selection process

3. SENSORY PROCESSING OF TASTE AND TEXTURE OF FOOD IN THE HUMAN BRAIN
The gustatory cortex of the brain receives taste information from the tongue via nerves. The
amygdala and hippocampus add emotional and memory-based layers to our taste sensations, while the OFC
connects taste and reward  thus modifying preferences based on hunger [3]. Taste perception has been
demonstrated to affect advanced social and emotional processes , as Schaefer et al. [13] reported enhanced
prosocial behavior following a sweet taste exposure highlighting the extensive cognitive implications of
gustatory processing. It has also been demonstrated that oral stimulus related to taste influences the cognitive
states. Even when no meal is consumed, Hosang  et al. [14] demonstrated that washing the mouth with carbs
alters how attention is processed . Our food choices  also greatly influenced by its texture  in Figure 4.
Figure 4. Illustrates how Neuron 25 in the OFC responds strongly to slippery food textures, with a high
inverse correlation to friction (r = -0.91) (Figure 4(a)) . Its response to viscosity is weaker (r = 0. 06)
(Figure 4(b)), suggesting that lubricity plays a more critical role in texture-related brain activity [16].
The somatosensory cortex , which deals with touch, is how our brain interprets sensations like
crunchiness or creaminess  of food. Not only can these textures improve the experience , but they also affect
human perception of flavor and food choices. Low  frequency oscillations are essential for gustatory
processing according to recent the EEG research [15], with delta-band activity showing how the human brain
encodes information linked to taste.  For instance, because of their high sensory feedback, crunchy meals
frequently cause stronger attention and brain responses. Rolls  [16] discovered that the friction of the food
altered the activity of a particular neuron in the OFC thus demonstrating the brain ’s fine tuning of food
texture and reward.
Foods with complex or layered textures increase satisfaction  levels by activating more brain regions
for longer periods of time [17], [18] . Textur e related food perception , which primarily stimulates
somatosensory cortices but is modified by visual, auditory , and taste  related inputs through integrative
regions such the insula, supports multisensory and affective elements of eating [19]. Studies also reveal that
taste and texture are processed by the brain together rather than as two distinct sensations. The insula, OFC,
anterior cingulate cortex (ACC) , and the amygdala are among the areas where multimodal integration
takes place.
These regions are crucial for memory, emotion, and decision  making. Studies have also shown that
multisensory food cues generate integrated neural responses  thus helping the brain combine sensory
information such as taste and texture into a single perception of food [20]. Overlapping activation of the OFC
and the anterior insula during flavor perception has also been reported  suggesting their involvement in
integrating taste, smell , and texture [21], [22] . Also, Kim and Kim  [23] highlighted the insula's role in
combining gustatory and somatosensory signals.

Int J Artif Intell  ISSN: 2252-8938 

A review of brain signal analysis in food perception studies (Harish S. Sinai Velingkar)
3971
The amygdala, which adds emotional meaning to sensory experiences, influences texture
preferences especially for rich, indulgent foods . These results suggest that our brain make s eating a smooth
experience by combining different sensory signals into one tasty perception.  Food preferences also depend on
taste, texture, familiarity, and the past experiences.
High-fat and layered foods activate reward centers more intensely and stay interesting for longer,
making them harder to resist  [21]. Familiarity and emotional associations also enhance pleasure from
eating [3], explaining cravings for processed, texture -rich foods like chips and fries  [24], [25]. Children who
are overweight or obese have also been found to exhibit different EEG activity patterns in response to food
related stimuli than their peers who are of normal weight, suggesting that their cortical processing during
food perception is altered [26].

(a)

(b)

Figure 4. OFC Neuron 25 responses to (a) friction and (b) viscosity

Researchers have learned a lot about how the brain processes simple tastes and textures in
Table 1, but we still don't know much about how complex taste and textures like junk food for e.g. chips
affect the brain in the real world. Such foods are of strong flavor, layered textures and have a lot of visual
appeal but researchers haven’t often looked into how they affect brain activity and the long-term eating
habits caused by them. Studies show that even minor changes in texture can trigger different reactions in
the brain. Need more real life, long -term studies with tools such as EEG and fMRI to really understand the
consumer psychology.

                ISSN: 2252-8938
Int J Artif Intell, Vol. 15, No. 4, August 2026: 3967-3980
3972
Table 1. Comparative summary of literature on changes in brain waves for different tastes and flavors
Study Key focus Main findings Brain
response/techniques
Results and implications
Zhou et al.
[3]
Spicy craving and
reward
Spicy cravers show stronger brain
response to chili food images
fMRI reward/visual
regions
Visual spicy cues activate
reward circuits, similar to
addiction
Schaefer
et al. [13]
Sweet taste and
social behavior
Sweet taste increases prosocial
responses
EEG/ERP affective
markers
Taste influences emotion and
social behavior, beyond sensory
reward
Hosang
et al. [14]
Attention
modulation during
carbohydrate mouth
rinsing
Carbohydrate mouth rinsing alters
attention and cognitive
engagement
Behavioral attention
measures + EEG/ERP
markers
Suggests that taste/nutrient cues
can modulate attentional
processing even without
ingestion
Wallroth
et al. [15]
Taste information in
EEG
Delta band carries taste-related
signals
EEG spectral (delta
activity)
Low-frequency EEG supports
taste encoding
Rolls [16] Texture and taste
perception
Firing rate strongly linked to
friction (r = -0.91); weaker for
viscosity
OFC activity Texture impacts flavor
pleasantness; useful for appetite
and obesity research
Andersen
et al. [17]
Similar taste
classification
EEG can differentiate
perceptually close tastes
EEG + independent
component analysis
(ICA) preprocessing
Supports subtle taste
discrimination when cleaned
well
Peng et al.
[18]
Color–texture
congruence
Congruent color-texture cues
increase gamma/theta activity and
improve evaluation
EEG oscillations +
behavior
Packaging texture can shape
perceived reward and choice
Luo and
Han [19]
Multisensory flavor
integration
Flavor shaped by senses +
personal factors
Theoretical model Flavor is psychological,
influenced by environment and
past experiences
Stuldreher
et al. [20]
Taste-visual
conditioning
Taste pairings enhanced visual
neural responses; increased
delta/theta
EEG (N2-P3 waves,
delta/theta bands)
Taste-visual learning induces
long-term sensory brain
changes
Han et al.
[21]
Sweetness
sensitivity and fat
food
Sweet-sensitive individuals:
stronger insula activity, prefer
high-carb foods
EEG, insular cortex Sweet sensitivity shapes eating
behavior and food preferences
Kosling
et al. [22]
Obesity and neural
food reactivity
Obese children: increased frontal
beta, decreased parietal alpha
with high-calorie cues
EEG (frontal/parietal
activity)
Distinct neural markers for
overeating tendencies
Kusunoki
et al. [24]
Eating and emotion EEG bands shift with emotion
during eating
EEG frequency
domain
Emotional context changes
feeding signatures
Songsamoe
et al. [25]
Consumer emotion
to food
EEG tracks physiological and
emotional reactions to food
EEG spectral + ERP
(review context)
EEG useful for consumer
neuroscience outside labs
Baines
et al. [26]
Reward timing and
body mass index
(BMI)
Overweight groups show altered
reward response to pleasant taste
cues
EEG + ERP reward
components
BMI affects neural reward
phases and attention to pleasant
food
Kim and
Kim [23]
Makgeolli taste
analysis
Brainwaves linked to bitterness;
unsterilized samples preferred
Brainwave analysis Brain-based systems help
evaluate and scale beverage
preferences

4. SENSORY AND NEURAL PROCESSING OF VISUAL FOOD CUES IN THE HUMAN BRAIN
Images of food trigger a broad brain network that links memories, feelings , and desires. Using EEG
methods like multifractal detrended fluctuation analysis (MFDFA) and multifractal detrended cross -
correlation analysis (MFDXA), Roy et al. [27] discovered that blue  colored food images triggered the most
complex brain activity. These changes were reflected in distinct patterns of brain activity indicating enhanced
communication between brain regions and a prolonged processing of sensory information. In addition to taste
and texture, visual cues such as packaging and labeling also play an important role in shaping neural
responses to food. Spence et al.  [4] demonstrated that color contrast can influence perceived taste and
increase the perceived appeal of food . David et al. [28] found that while some health warnings reduced the
attractiveness of food products, others increased their appeal, emphasizing the complex role of visual cues in
shaping the food preferences. Food choices depend on more than just sensory characteristics such as taste and
texture. Economic incentives, cultural influences  also contribute in the  decision-making process.
Banerjee et al.  [1] showed that rebates made healthier food options more appealing and activated reward
related brain regions, making these choices easier for participants . In another study, Lim et al. [29] examined
traditional Korean dinners  in Figure 5 and discovered that people's enjoyment of the foods increased with
their complexity and familiarity. Stronger reward reactions and reduced mental effort were shown in brain
scans indicating that our brain switches from comparing the options to just savoring the moment when eating
feels familiar and pleasant  in Figure 6.  Figure 5. illustrates how participants liking scores improved as
Korean dishes became more complex (M1 –M4) thus indicating a greater preference for visual and flavor

Int J Artif Intell  ISSN: 2252-8938 

A review of brain signal analysis in food perception studies (Harish S. Sinai Velingkar)
3973
richness throughout 80 randomized trials [29] . Figure 6 shows stronger brain responses to the visuals of
complex meal 4 across key ERP time windows indicating increased sensory engagement with food cues [29] .

Figure 5. Experimental food stimuli with increasing meal complexity

Figure 6. ERP responses to food stimuli

According to Zhou et al. [3], those who enjoyed spicy food exhibited higher levels of brain activity
connected to food cravings and react faster to the visuals of spicy food, indicating that their brain  is more
sensitive to the spice level . The brain responds rapidly to visual food cues, even before any conscious
evaluation of food takes place. Vermeir  and Roose [30] reviewed how visual design elements such as color,
shape and the layout influence s the food choices through psychological and behavioral mechanisms  while
also identifying important gaps and future research directions in this field . In a nother different study,
Vartanian et al. [31] demonstrated that visually appealing foods can trigger brain activity patterns resembling
those observed in addictive behaviors, particularly when an individual is hungry and has a greater body
weight. Schubert et al. [32] showed that the brain responds to the healthiness of food even before consciously
evaluating its taste. The study reported that healt h related information was identified from the food images
with approximately 77% accuracy, while taste  related information was recognized with about 71% accuracy
during the evaluation process. These findings suggest that health  related neural processing precedes the

                ISSN: 2252-8938
Int J Artif Intell, Vol. 15, No. 4, August 2026: 3967-3980
3974
conscious assessment of flavor  while making food choices. It also  shows how deeply food images can
influence our brain’s emotional and decision-making systems.
A brief overview of how the visual food cues affect human brain activity specifically in areas linked
to emotion, reward , and decision  making is provided in Table 2. Our brain frequently react s to food even
before we realize it. The amygdala and insula can indicate repulsion to food , whereas areas like the OFC
assess how appetizing the food appears. According to some research , similar to addiction, regions of the
brain linked to cravings are activated in reaction to specific images . However, most of this research has been
conducted in controlled laboratory environments or within  a specific cultural setting. Future studies need to
look into how different  real life food images in real life scenarios affect brain responses over long periods
of time.

Table 2. Summary of studies on neural responses to visual food stimuli
Study Key focus Main findings Brain response/techniques Results and implications
Roy et al. [27] Color and
brain activity
Blue color triggered
highest neural complexity
EEG, MFDFA/MFDXA,
frontal, occipital, and
parietal
Color significantly shapes the
brain dynamics
Spence et al.
[4]
Visual
aesthetics of
food
Color
contrast/background
affects perceived
deliciousness
EEG and reward regions Visuals can influence healthier
food choices
David et al.
[28]
Food labeling
and emotion
Health warnings reduced
appeal but red labels
backfired
EEG, ERPs, and emotional
modulation
Label design affects food
appeal and policy impact
Banerjee et al.
[1]
Fiscal
incentives and
food choice
Rebates boosted healthier
choices and reduced
mental effort
EEG, fMRI, and reward
regions
Fiscal tools encourage better
food decisions
Lim et al. [29] Meal
complexity and
liking
Complex meals increased
liking and reward activity
EEG, Insula, OFC, and
dorsolateral prefrontal
cortex (dlPFC)
Complexity enhances reward
and preference circuits
Zhou et al. [3] Craving spicy
foods
Cravers showed faster,
stronger neural response
fMRI, Insula, ACC, and
Putamen
Craving linked to addiction-like
brain activity
Vermeir and
Roose [30]
Visual design
cues and food
choice
Visual elements (color,
layout, and imagery)
influence food decisions
via attention, affect,
cognition, and motivation
Narrative review of
behavioral and
psychological studies
Visual design shapes
perceptions and attitudes,
affecting food choice behaviour
and highlighting gaps for future
research
Vartanian et al.
[31]
Weight and
hunger effects
on neural food
cue processing
Food visuals activate
reward and visual areas
fMRI meta-analysis Shows shared reward/visual
processing, with some
differences by BMI and hunger
Schubert et al.
[32]
Taste vs. health
in decisions
Health cues processed
earlier than taste
EEG, OFC, cingulate, and
insula
Challenges assumption that
taste dominates food choice

5. SENSORY AND NEURAL PROCESSING OF MULTISENSORY STIMULI IN THE HUMAN
BRAIN
Our brain’s response to food isn’t just about taste or looks but it’s shaped by a mix of smell, texture,
packaging, and even mood or tiredness, in turn deciding what we choose or crave. Yang et al. [33] found that
taste doesn’t just help us recognize food , it also stirs emotional brain responses, influencing how much we
enjoy it and the choices we make  in Figure 7. Figure 7. Illustrates how visual presentation , specifically the
color of drinks  (Figure 7(a)) and shape of glassware  (Figure 7(b)), significantly influenced brain responses
and increased positive ratings due to color -flavor congruency [33]. In the experiment conducted, p articipants
preferred drinks when the color matched the expected flavor, and drinks served in wine or cocktail glasses
were rated tastier showing how glass shape and color influences our taste perception.
In another study, Yagyu et al. [34] found that flavored chewing gum altered the global complexity
of multichannel EEG activity in a manner that unflavored gum did not . This shows how the combination of
taste and s mell increases brain activity. The brain's function in integrating the sensory inputs is highlighted
also by Maeda and Yoshimur a [35] who reported an increased theta  band activity during mismatched
olfactory taste stimulation. Event related potentials (ERPs) have been widely used to study brain responses
associated with reward and food  related cognitive processing. These measures provide useful insights into
how known food cues become linked with attention and motivational responses [36]. ERPs are particularly
useful for stimulus onset analysis because they capture rapid and time locked brain responses occurring when
a sensory stimulus like taste or texture is presented. On the other hand,  spectral analysis provides insights

Int J Artif Intell  ISSN: 2252-8938 

A review of brain signal analysis in food perception studies (Harish S. Sinai Velingkar)
3975
into neural activity over much longer periods of time and can help examine processes related to perception of
texture, cravings and taste memory through changes in frequency band activity [37].
Byrne et al.  [38] observed an increased gamma activity when visual food cues matched the
perceived taste. In contrast  for mismatched cues, such as viewing broccoli while tasting sugar evoked the
N400 responses which are generally associated with conflicting sensory information.  These studies suggest
that taste is rarely experienced on its own  while the brain continuously combines what we see and what we
taste. This interaction between taste and visual cues can influence a person’s food perception. Domracheva
and Kulikova [39] also supported this idea by identifying distinct EEG patterns which are associated with
perceived similarities between food products during a taste visual integration task.

(a)

(b)

Figure 7. Visual presentation of (a) effect of drink color and (b) glass shape on likability ratings

According to Christoffersen et al.  [40], the  human brain react s not just to taste but also to the
appearance of food and past experiences with it. The human brain uses that visual memory to influence  and
decide how it would respond to a particular food in the future if have frequently perceived it as either
pleasant or unpleasant. In a similar study, Wolz et al. [41] found that individuals with binge eating tendencies
showed stronger brain responses to the sight and smell of chocolate , which were also associated with
increased craving and attention. Such findings show how the human brain recalls previous visual and sensory
experiences to influence responses to food. Internal factors such as hunger and hormonal state s also influence
how the brain responds to food, beyond the effects of visual, olfactory , and taste cues. Janet et al. [42] found
that hunger was associated with  an increased activity in the brain regions such as the ventromedial prefrontal
cortex and striatum when the participants were exposed to food cues.  Similarly, Lowe et al. [43] also found
that using brain stimulation to disrupt the left dorsolateral prefrontal cortex led to alterations in  the EEG
(stronger N2 and P3), which also suggested a decrease in the cognitive control as well as an increase in the
consumption of high calorie items.
Flavor is not just determined by taste alone rather it develops through the combined influence of
multiple other senses. Studies have shown that these sensory systems do not operate independently as even
visual and auditory cues can influence the eating experience. Jing et al. [44] found that pleasant background
sounds while consuming sweets increased both  neural activity and perceived enjoyment.  Similarly,
Rodriguez et al. [45] and Jusienė et al. [46] reported that people tend to consume more food while watching
television than while eating without such distractions. Such findings  suggest that audiovisual distractions
may influence attention during eating and contribute to an increased consumption  of food. The feel of the
packaging and financial incentives  like discounts can also significantly influence food perception and brain
responses. Smooth textures are generally linked with healthier foods , while discounts can alter neural reward
processing in low  income groups [47]. Lastly, the s leep quality can also influence taste preferences. Deeper
sleep reduced sweet cravings without altering smell sensitivity [48].
Table 3 summarizes how the brain processes multisensory food cues like taste, smell, texture , and
visuals. EEG and fMRI studies reveal that regions like the orbitofrontal and prefrontal cortex integrate these
signals, which are influenced by our emotions, hunger, memory, and sleep. These results show that taste is a
very personal and brain based experience, but most studies so far have only looked at small, similar groups of
people in short lab experiments  [49], [50] . To truly understand how human senses shape what eat, future
research needs to include more diverse participants, real life eating situations and long-term observations.

                ISSN: 2252-8938
Int J Artif Intell, Vol. 15, No. 4, August 2026: 3967-3980
3976
This gap has begun to receive greater attention in the recent years. Recent studies have increased the
scope of EEG  based food perception research by providing broader reviews of consumer neuroscience [51]
demonstrating that the neurocognitive processing of texture and other sensory attributes span across a wide
range of foods including the processed products [52]. They have also shown that real  world eating
environments produce neurophysiological and behavioral responses that are different from those observed in
a controlled laboratory setting [53] while summarizing recent advances in EEG signal processing and
analytical techniques for studying gustatory perception [54]. These findings support the need for more
ecologically valid and multisensory research approaches  thus reinforcing the direction of the present review.
The summary of all the studies and references included in the qualitative analysis is shown in Table 4.

Table 3. Comparison of studies on neural dynamics of multisensory integration and brain responses to
combined sensory stimuli
Study Key focus Main findings Brain response/techniques Results and implications
Yang et al. [33] Brain activity in taste
preference
Brain distinguishes taste
qualities and pleasantness
EEG, frequency bands,
temporal dynamics
Taste linked to specific
brain patterns; further
study needed on timing
Yagyu et al. [34] Flavor of chewing
gum and EEG
complexity
Flavored gum alters global
EEG complexity vs.
unflavored gum
Multichannel EEG, global
complexity measures
Flavor cues from gum alter
global brain-signal
complexity
Maeda and
Yoshimura [35]
Olfactory–taste
mismatch effects
Theta activity rises during
mismatched smell–taste
EEG spectral (theta band) Shows mismatch drives
higher cognitive load in
sensory hubs
Forester et al.
[36]
ERP methods for
reward processing
ERP markers are sensitive
to food-related reward and
attention
EEG-based ERP components
(P2, P3/LPP)
Supports ERPs as effective
tools for studying food-
related reward and cue
processing
Campos et al.
[37]
Principal ERP
extraction (pERP-
RED)
Reduces ERPs to core
waveforms across
tasks/subjects
ERP reduction + cross-
electrode estimation
Supports scalable ERP
analysis across subjects
and electrodes.
Byrne et al. [38] EEG measures in
neuromarketing
Identifies common EEG
markers linked to attention,
emotion, and rewardpower;
mismatch evoked N400
EEG spectral analysis, ERP
components
Highlights EEG as a useful
tool for assessing
consumer and food-related
neural responses
Domracheva
and Kulikova
[39]
Taste–visual
congruence/mismatch
Congruence boosts
induced gamma; mismatch
evokes N400-like
EEG + ERP (gamma, N400-
like deflection)
Confirms early neural
signatures of sensory
congruence vs confusion.
Christoffersen
et al. [40]
Visuo-gustatory
conditioning
Conditioned visuals
enhanced cortical
responses, right dominance
visual evoked potential
(VEP), N2-P3 amplitude
Visual-taste pairings
modulate sensory brain
responses
Wolz et al. [41] Olfactory and visual
food cues in cravings
Binge-eaters showed
stronger craving, increased
N2 and LPP
EEG, N2, LPP amplitudes Craving linked to
heightened brain reactivity
in disorder group
Janet et al. [42] Appetite regulation
via food stimuli
Hunger modulated brain
activation in food valuation
regions
fMRI, dorsomedial prefrontal
cortex (dmPFC),
ventromedial PFC (vmPFC),
and striatum
Specific areas control
hunger and decision-
making
Lowe et al. [43] dlPFC’s role in
controlling cravings
Disrupted dlPFC led to
increased high-calorie
intake
Repetitive transcranial
magnetic stimulation
(rTMS), EEG, N2, P3b, P3a
dlPFC involved in
inhibiting food
consumption
Jing et al. [44] Effect of music
context on food
preference
Different music types
modulate neural responses
to food stimuli
ERP analysis (N2, P2
components)
Shows that auditory
context influences food
preference through neural
processing mechanisms
Rodriguez et al.
[45]
Impact of screen use
during eating on
snack consumption
Watching TV while eating
increases snack
consumption; smartphone
use does not
Behavioral intake measures
(no neural measures)
Indicates that sustained
audiovisual distraction
(TV) may disrupt eating
control, while brief
smartphone use does not
Jusienė et al.
[46]
Screen distraction
during meals
TV use links to less
regulated eating
Behavioral survey and
screen-eating context
Screen distraction
associates with weaker
eating self-control.
Peng et al. [47] Packaging texture
and health perception
Smooth texture linked to
healthier choices, stronger
P300 response
ERP, brief implicit
association test (BIAT),
P300, and late negative
component (LNC)
Subtle tactile cues
influence food
expectations
Szczygiel et al.
[48]
Sleep and sweet
preference
More sleep linked to
reduced preference for
sweetness
EEG Sleep patterns subtly shape
taste preferences

Int J Artif Intell  ISSN: 2252-8938 

A review of brain signal analysis in food perception studies (Harish S. Sinai Velingkar)
3977
Table 4. Summary of studies and references included in the qualitative analysis
Taste and flavour Visual stimuli Multisensory stimuli
Study Reference Table/figure Study Reference Table/figure Study Reference Table/figure
1 Zhou et al.
[3]
1 1 Roy et al.
[27]
2 1 Yang et al. [33] 3/7
2 Schaefer
et al. [13]
1 2 Spence
et al. [4]
2 2 Yagyu [34] 3
3 Hosang
et al. [14]
1 3 David
et al. [28]
2 3 Maeda and
Yoshimura [35]
3
4 Wallroth
et al. [15]
1 4 Banerjee
et al. [1]
2 4 Forester et al. [36] 3
5 Rolls [16] 1/4 5 Lim et al.
[29]
2/5-6 5 Campos et al. [37] 3
6 Andersen
et al. [17]
1 6 Zhou et al.
[3]
2 6 Byrne et al. [38] 3
7 Peng et al.
[18]
1 7 Vermeir
and Roose
[30]
2 7 Domracheva and
Kulikova [39]
3
8 Luo and
Han [19]
1 8 Vartanian
et al. [31]
2 8 Christoffersen et al.
[40]
3
9 Stuldreher
et al. [20]
1 9 Schubert
et al. [32]
2 9 Wolz et al. [41] 3
10 Han et al.
[21]
1    10 Janet et al. [42] 3
11 Kosling
et al. [22]
1    11 Lowe et al. [43] 3
12 Kusunoki
et al. [24]
1    12 Jing et al. [44] 3
13 Songsamoe
et al. [25]
1    13 Rodriguez et al.
[45]
3
14 Baines et al.
[26]
1    14 Jusienė et al. [46] 3
15 Kim and
Kim [23]
1    15 Peng et al. [47] 3
      16 Szczygiel et al. [48] 3

6. CONCLUSION
This review shows that the brain integrates smell, vision, touch , and memory of food into a single
experience, making the food perception more than just  the taste. These sensory inputs are combined by the
OFC, insula, and prefrontal cortex, which are  the crucial brain regions that influence our desire or avoidance
of particular meals. In addition, these processes are influenced by external factors like food presentation and
packaging as well as internal factors like hunger and mood.  From a practical perspective, understanding how
the brain responds to food can help designers and manufacturers develop  the food products, packaging and
marketing cues that better align with  the consumers expectation and preference. This knowledge also has
important applications in public health, where a better understanding of sensory cues may support dietary
interventions, encourage healthier food choices  and help to address unhealthy eating behaviors.  A major
limitation of the existing research is that it relies  on simplified food stimuli, highly controlled laboratory
settings and narrowly defined participant groups. Although these conditions are useful for understanding
specific responses, they may not fully represent how people actually experience food in everyday life,
particularly in the case of processed foods and culturally diverse diets. This limits the real-world applications
of many findings and highlights the need for studies which need to be conducted in a more natural eating
environment. Portable EEG devices and wearable sensors are making it easier to study food  related responses
in everyday settings rather than only in controlled laboratories. Combining brain data with AI and machine
learning techniques may also help to improve the prediction of food preferences and eating behaviors.
Further progress in this field will depend on collaboration across neuroscience, psychology, nutrition  and
marketing to develop a larger understanding of how people perceive and choose food.  Finally, ethical
considerations should remain as an important part of consumer neuroscience and neuromarketing as the fields
continue to develop. These technologies should be used to inform and support consumers with transparency
rather than manipulate their choices  thus making responsible use of neural data. The future of this field will
depend not only on advances in the methods and technology but also on the ethical and responsible manner in
which the research is conducted.

FUNDING INFORMATION
This research received no external funding.

                ISSN: 2252-8938
Int J Artif Intell, Vol. 15, No. 4, August 2026: 3967-3980
3978
AUTHOR CONTRIBUTIONS STATEMENT
This journal uses the Contributor Roles Taxonomy (CRediT) to recognize individual author
contributions, reduce authorship disputes, and facilitate collaboration.

Name of Author C M So Va Fo I R D O E Vi Su P Fu
Harish S.Sinai
Velingkar
✓ ✓   ✓ ✓ ✓ ✓ ✓
Roopa R. Kulkarni ✓ ✓  ✓    ✓  ✓ ✓ ✓ ✓
Prashant Patavardhan ✓  ✓ ✓      ✓ ✓ ✓ ✓
Abdul Haq Nalband ✓   ✓      ✓  ✓

C :  Conceptualization
M :  Methodology
So :  Software
Va :  Validation
Fo :  Formal analysis
I :  Investigation
R :  Resources
D : Data Curation
O : Writing - Original Draft
E : Writing - Review & Editing
Vi :  Visualization
Su :  Supervision
P :  Project administration
Fu :  Funding acquisition

CONFLICT OF INTEREST STATEMENT
The author declares no conflict of interest.

DATA AVAILABILITY
This study is a literature review and does not include any original data. All sources of information
used in the review are publicly available and cited within the manuscript. No new datasets were generated or
analyzed during this study.

REFERENCES
[1] T. Banerjee, V. Chattaraman, H. Zou, and G. Deshpande, “A neurobehavioral study on the efficacy of price interventions in
promoting healthy food choices among low socioeconomic families,” Scientific Reports , vol. 10, no. 1, Sep. 2020,
doi: 10.1038/s41598-020-71082-y.
[2] M. Priyadarshani, P. Kumar, K. S. Babulal, D. S. Rajput, and H. Patel, “Human brain waves study using EEG and deep learning
for emotion recognition,” IEEE Access, vol. 12, pp. 101842–101850, 2024, doi: 10.1109/ACCESS.2024.3427822.
[3] Y. Zhou, X. Gao, D. M. Small, and H. Chen, “Extreme spicy food cravers displayed increased brain activity in response to
pictures of foods containing chili peppers: an fMRI study,” Appetite, vol. 142, 2019, doi: 10.1016/j.appet.2019.104379.
[4] C. Spence, K. Motoki, and O. Petit, “Factors influencing the visual deliciousness/eye -appeal of food,” Food Quality and
Preference, vol. 102, 2022, doi: 10.1016/j.foodqual.2022.104672.
[5] M. Klug and K. Gramann, “Identifying key factors for improving ICA-based decomposition of EEG data in mobile and stationary
experiments,” European Journal of Neuroscience, vol. 54, no. 12, pp. 8406–8420, 2021, doi: 10.1111/ejn.14992.
[6] N. Panigrahi and S. P. Mohanty, “Protocol and process of EEG data acquisition,” Brain Computer Interface , pp. 81 –95, 2022,
doi: 10.1201/9781003241386-5.
[7] I. C. Tang et al. , “Using functional magnetic resonance imaging (fMRI) to analyze brain region activity when viewing
landscapes,” Landscape and Urban Planning, vol. 162, pp. 137–144, 2017, doi: 10.1016/j.landurbplan.2017.02.007.
[8] R. F. Ahmad, A. S. Malik, N. Kamel, and F. Reza, “EEG -fMRI combination for better understanding of brain functions: pros and
cons,” in IEEE 2015 International Conference on Signal and Image Processing Applications, ICSIPA 2015 - Proceedings, 2016,
pp. 278–281, doi: 10.1109/ICSIPA.2015.7412204.
[9] J. Wirsich et al., “The relationship between EEG and fMRI connectomes is reproducible across simultaneous EEG -fMRI studies
from 1.5T to 7T,” NeuroImage, vol. 231, 2021, doi: 10.1016/j.neuroimage.2021.117864.
[10] K. Warnakulasooriya, J. Bandara, and B. H. Sudantha, “Sensory evaluation of foods using modern AI techniques and brain wave
analysis,” in Proceedings of International Conference on Image Processing and Robotics, ICIPRoB 2020 , 2020 ,
doi: 10.1109/ICIP48927.2020.9367340.
[11] M. Heidari, Y. K . Jokar, S. Madani, S. Shahi, M. S. Shahi, and M. Goli, “Influence of food type on human psychological –
behavioral responses and crime reductio,” Nutrients, vol. 15, no. 17, 2023, doi: 10.3390/nu15173715.
[12] M. J. Page et al., “The PRISMA 2020 statement: an updated guideline for reporting systematic reviews,” Systematic Reviews,
vol. 10, no. 1, 2021, doi: 10.1186/s13643-021-01626-4.
[13] M. Schaefer, A. Kühnel, F. Schweitzer, F. Rumpel, and M. Gärtner, “Experiencing sweet taste is associated with an increase in
prosocial behavior,” Scientific Reports, vol. 13, no. 1, 2023, doi: 10.1038/s41598-023-28553-9.
[14] T. J. Hosang, S. Laborde, A. Löw, M. Sprengel, N. Baum, and T. Jacobsen, “How attention changes in response to carbohydrate
mouth rinsing,” Nutrients, vol. 15, no. 13, 2023, doi: 10.3390/nu15133053.
[15] R. Wallroth, R. Höchenberger, and K. Ohla, “Delta activity encodes taste information in the human brain ,” NeuroImage, Apr. 13,
2018, doi: 10.1101/300194.
[16] E. T. Rolls, “The texture and taste of food in the brain,” Journal of Texture Studies , vol. 51, no. 1, pp. 23 –44, 2020,
doi: 10.1111/jtxs.12488.
[17] C. A. Andersen et al., “EEG discrimination of perceptually similar tastes,” Journal of Neuroscience Research , vol. 97, no. 3,
pp. 241–252, 2019, doi: 10.1002/jnr.24281.
[18] Y. Peng, Y. Sun, and X. Wan, “Influence of the crossmodal congruency between color and flavor on product evaluations:
evidence from behavioral and oscillatory brain responses,” Food Quality and Preference , vol. 97, 2022,
doi: 10.1016/j.foodqual.2021.104480.

Int J Artif Intell  ISSN: 2252-8938 

A review of brain signal analysis in food perception studies (Harish S. Sinai Velingkar)
3979
[19] L. Luo and P. Han, “Assessing food -evoked emotions using functional magnetic resonance imaging: a systematic review,” Food
Quality and Preference, vol. 108, 2023, doi: 10.1016/j.foodqual.2023.104877.
[20] I. V. Stuldreher, D. Kaneko, H. Hiraguchi, J. B. F. V. Erp, and A. M. Brouwer, “EEG measures of attention toward food -related
stimuli vary with food neophobia,” Food Quality and Preference, vol. 106, 2023, doi: 10.1016/j.foodqual.2022.104805.
[21] P. Han, M. Mohebbi, H. S. Seo, and T. Hummel, “Sensitivity to sweetness correlates to elevated reward brain responses to swee t
and high-fat food odors in young healthy volunteers,” NeuroImage, vol. 208, 2020, doi: 10.1016/j.neuroimage.2019.116413.
[22] C. Kösling, L. Schäfer, C. Hübner, C. Sebert, A. Hilbert, and R. Schmidt, “Food -induced brain activity in children with
overweight or obesity versus normal weight: an electroencephalographic pilot study,” Brain Sciences , vol. 12, no. 12, 2022,
doi: 10.3390/brainsci12121653.
[23] Y. S. Kim and Y. S. Kim, “Biometrics analysis and evaluation on Korean Makgeolli using brainwaves and taste biological sensor
system,” BioMed Research International, 2015, doi: 10.1155/2015/918631.
[24] S. Kusunoki et al., “Relationships between feeding behaviors and emotions: an electroencephalogram (EEG) frequency analysis
study,” The journal of physiological sciences , vol. 73, no. 1, 2023, doi: 10.1186/s12576-022-00858-w.
[25] S. Songsamoe, R. Saengwong -ngam, P. Koomhin, and N. Matan, “Understanding consumer physiological and emotional
responses to food products using electroencephalography (EEG),” Trends in Food Science and Technology, vol. 93, pp. 167–173,
2019, doi: 10.1016/j.tifs.2019.09.018.
[26] S. Baines, I. S. Hensels, and D. Talmi, “An EEG study on the effect of being overweight on anticipatory and consummatory
reward in response to pleasant taste stimuli,” Physiology and Behavior, vol. 252, 2022, doi: 10.1016/j.physbeh.2022.113819.
[27] S. Roy et al., “Brain response to color stimuli: an EEG study with nonlinear approach,” Cognitive Neurodynamics, vol. 15, no. 6,
pp. 1023–1053, 2021, doi: 10.1007/s11571-021-09692-z.
[28] I. A. David et al., “Use of event -related potentials to measure the impact of front -of-package labels on food -evoked emotion,”
Food Quality and Preference, vol. 111, 2023, doi: 10.1016/j.foodqual.2023.104995.
[29] M. Lim, S. Park, Y. Lee, and H. S. Kwak, “Brain responses and connectivity to visual meal compositions: an EEG investigation
into food liking,” Food Quality and Preference, vol. 112, 2023, doi: 10.1016/j.foodqual.2023.105029.
[30] I. Vermeir and G. Roose, “Visual design cues impacting food choice: a review and future research agenda,” Foods, vol. 9, no. 10,
2020, doi: 10.3390/foods9101495.
[31] M. Vartanian et al. , “Neural responses to visual food cues according to weight and hunger state: a systematic review and
meta-analysis,” Neuroscience and Biobehavioral Reviews, vol. 177, 2025, doi: 10.1016/j.neubiorev.2025.106301.
[32] E. Schubert, D. Rosenblatt, D. Eliby, Y. Kashima, H. Hogendoorn, and S. Bode, “Decoding explicit and implicit representations
of health and taste attributes of foods in the human brain,” Neuropsychologia, vol. 162, 2021,
doi: 10.1016/j.neuropsychologia.2021.108045.
[33] T. Yang et al. , “Insights into brain perceptions of the different taste qualities and hedonic valence of food via scalp
electroencephalogram,” Food Research International, vol. 173, 2023, doi: 10.1016/j.foodres.2023.113311.
[34] T. Yagyu et al. , “Chewing -gum flavor affects measures of global complexity of multichannel EEG,” Neuropsychobiology,
vol. 35, no. 1, pp. 46–50, 1997, doi: 10.1159/000119329.
[35] S. Maeda and H. Yoshimura, “Enhancement of electroencephalogram activity in the theta-band range during unmatched olfactory-
taste stimulation,” Journal of Physiological Sciences, vol. 69, no. 4, pp. 613–621, 2019, doi: 10.1007/s12576-019-00674-9.
[36] G. Forester, L. M. Schaefer, D. R. Dodd, and J. S. Johnson, “The potential application of event -related potentials to enhance
research on reward processes in eating disorders,” International Journal of Eating Disorders , vol. 55, no. 11, pp. 1484 –1495,
2022, doi: 10.1002/eat.23821.
[37] E. Campos et al., “Principle ERP reduction and analysis: estimating and using principle ERP waveforms underlying ERPs across
tasks, subjects, and electrodes,” NeuroImage, vol. 212, 2020, doi: 10.1016/j.neuroimage.2020.116630.
[38] A. Byrne, E. Bonfiglio, C. Rigby, and N. Edelstyn, “A systematic review of the prediction of consumer preference using EEG measures
and machine-learning in neuromarketing research,” Brain Informatics, vol. 9, no. 1, 2022, doi: 10.1186/s40708-022-00175-3.
[39] M. Domracheva and S. Kulikova, “EEG correlates of perceived food product similarity in a cross -modal taste-visual task,” Food
Quality and Preference, vol. 85, 2020, doi: 10.1016/j.foodqual.2020.103980.
[40] G. R. J. Christoffersen et al., “Long-term visuo-gustatory appetitive and aversive conditioning potentiate human visual evoked
potentials,” Frontiers in Human Neuroscience, vol. 11, 2017, doi: 10.3389/fnhum.2017.00467.
[41] I. Wolz et al., “Subjective craving and event -related brain response to olfactory and visual chocolate cues in binge -eating and
healthy individuals,” Scientific Reports, vol. 7, 2017, doi: 10.1038/srep41736.
[42] R. Janet et al. , “Cognitive and hormonal regulation of appetite for food presented in the olfactory and visual modalities,”
NeuroImage, vol. 230, 2021, doi: 10.1016/j.neuroimage.2021.117811.
[43] C. J. Lowe, W. R. Staines, F. Mannochio, and P. A. Hall, “The neurocognitive mechanisms underlying food cravings and snack
food consumption. A combined continuous theta burst stimulation (cTBS) and EEG study,” NeuroImage, vol. 177, pp. 45 –58,
2018, doi: 10.1016/j.neuroimage.2018.05.013.
[44] Y. Jing, Z. Xu, Y. Pang, X. Liu, J. Zhao, and Y. Liu, “The neural correlates of food preference among music kinds,” Foods,
vol. 13, no. 7, 2024, doi: 10.3390/foods13071127.
[45] A. C. I. Rodriguez, M. S. Kirschner, and L. S. Nunes, “To stream or not to stream? watching TV while eating promotes increased
calorie consumption, but using a smartphone does not,” Physiology and Behavior, vol. 294, 2025, doi: 10.1016/j.physbeh.2025.114878.
[46] R. Jusienė et al., “Screen use during meals among young children: exploration of associated variables,” Medicina, vol. 55, no. 10,
2019, doi: 10.3390/medicina55100688.
[47] M. Peng, F. Liang, L. Yu, and H. Huang, “Smooth or rough? the impact of food packaging design on product healthiness
perception,” Food Quality and Preference, vol. 111, Oct. 2023, doi: 10.1016/j.foodqual.2023.104970.
[48] E. J. Szczygiel, S. Cho, and R. M. Tucker, “Characterization of the relationships between sleep duration, quality, architecture, and
chemosensory function in nonobese females,” Chemical Senses, vol. 43, no. 4, pp. 223–228, 2018, doi: 10.1093/chemse/bjy012.
[49] A. Krugliak and A. Clarke, “Towards real -world neuroscience using mobile EEG and augmented reality,” Scientific Reports ,
vol. 12, no. 1, 2022, doi: 10.1038/s41598-022-06296-3.
[50] A. L. -Zhu, M. P. H. Lau, and G. McLoughlin, “Mobile EEG in research on neurodevelopmental disorders: opportunities and
challenges,” Developmental Cognitive Neuroscience, vol. 36, 2019, doi: 10.1016/j.dcn.2019.100635.
[51] A. Panteli, E. Kalaitzi, and C. A. Fidas, “A review on the use of EEG for the investigation of the factors that affect consum er’s
behavior,” Physiology and Behavior, vol. 278, 2024, doi: 10.1016/j.physbeh.2024.114509.
[52] M. M. Ciobanu, E. I. Flocea, and P. C. Boișteanu, “The impact of artificial and natural additives in meat products on
neurocognitive food perception: a narrative review,” Foods, vol. 13, no. 23, 2024, doi: 10.3390/foods13233908.
[53] K. Colla, R. Keast, M. Mohebbi, C. G. Russell, and D. G. Liem, “Testing the validity of immersive eating environments against
laboratory and real life settings,” Food Quality and Preference, vol. 103, 2023, doi: 10.1016/j.foodqual.2022.104717.

                ISSN: 2252-8938
Int J Artif Intell, Vol. 15, No. 4, August 2026: 3967-3980
3980
[54] L. Yang, C. Zhang, W. Wu, J. Xie, and Z. Ding, “Advancements and applications of EEG in gustatory perception,” Brain
Sciences, vol. 15, no. 12, 2025, doi: 10.3390/brainsci15121317.

BIOGRAPHIES OF AUTHORS

Harish S. Sinai Velingkar     holds a master’s degree (M.Tech.) in Communication
Systems from R.V. College of Engineering, Bengaluru, affiliated with Visvesvaraya
Technological University, Belagavi, Karnataka, India, completed in 2014. He received his
bachelor’s degree in Electronics and Telecommunications from Padre Conceicao College of
Engineering, Verna, affiliated with Goa University, Goa, India, in 2012. He is currently
serving as an assistant professor in the Department of Electronics and Communication
Engineering at Agnel Institute of Technology and Design (AITD), Visvesveraya
Technological University , Goa. He has over 12 years of teaching experience. His areas of
interest include biomedical engineering, cognitive neuroscience, brain computer interface
(BCI), embedded systems, image processing, computer networks, cryptography , and network
security. He is currently pursuing his Ph.D. Dayananda Sagar Academy of Technology and
Management (DSATM), Bengaluru, India affiliated with Visvesvaraya Technological
University, Belagavi, Karnataka, India in cognitive neuroscience with a focus on sensory
processing and neural correlates of perception. He can be contacted at email:
harishvelingkar@gmail.com.

Dr. Roopa R. Kulkarni      received her Ph.D. in Low Power VLSI from
Visvesvaraya Technological University, Belagavi, in 2019. She completed her M.Tech . in
VLSI Design and Embedded Systems from the same university in 2005. She is currently
working as an associate professor in the Department of Electronics and Communication
Engineering at Dayananda Sagar Academy of Technology and Management (DSATM),
Bengaluru, India. With over 26 years of teaching experience, her areas of interest include low
power VLSI design and verification, internet of things  (IoT), artificial intelligence, and
embedded system design. She is a senior member of IEEE and a life member of ISTE. She has
contributed to various research publications in reputed journals and conferences and is actively
involved in academic mentoring. She can be contacted at email: roopakulkarni-
ece@dsatm.edu.in or roopa.patavardhan@gmail.com.

Dr. Prashant Patavardhan     received his B.E. in Electronics and Communication
Engineering from Karnataka University in 1995. He earned his M.Tech . in Digital Electronics
and Communication Systems from Visvesvaraya Technological University (VTU), Belagavi,
in 2001, graduating as the University Topper. He was awarded the Ph.D. degree by VTU,
Belagavi in 2011. With over 28 years of academic experience, He has served in various
teaching, research and academic leadership roles. He has held the position of professor and
head at reputed institutions, including in Department of Electronics and Communication
Engineering, RV Institute of Technology and Management (RVITM), Bengaluru, Dayananda
Sagar University, Bengaluru and KLS Gogte  Institute of Technology (KLS GIT), Belagavi.
Throughout his career, he has made significant contributions to academic administration,
curriculum development, outcome -based education, research supervision and institutional
quality enhancement. His research interests include biometrics, signal, image and video
processing, artificial neural networks, fuzzy logic, pattern recognition, embedded systems and
intelligent computing. He has published more than 27 research articles in international
journals and has presented his research at several national and international conferences. He
can be contacted at email: prashantgemini73@gmail.com.

Dr. Abdul Haq Nalband     received his B.E. degree from Visvesvaraya
Technological University, Belagavi, in 2010, and his M.Tech. Degree in Communication
Systems from Visvesvaraya Technological University, India, in 2014. He is currently working
as associate professor in Department of Computer Science and Engineering  (AI and ML),
Dayananda Sagar University, Ramanagara, Bengaluru, Karnataka, India. He did Ph.D. in 5G
Technologies in 2022. He recently completed the visiting postdoctoral fellowship in Cyber
Security from City, University of London, U nited Kingdom. He has published more than
20 research articles in indexed journals and conference. He has published 3 patents, out of
which one international patent is granted for his innovation. He is a Member of the IEEE,
USA, a life member of the Indian Society for Technical Education (ISTE, India), and associate
member of IETE, India. He has funded projects to his credit in the areas of wireless and
mobile communication, currently he is working on a project ‘Protocols for reconfigurable
communication system on ultra -massive MIMO architecture’, funded by ISRO. His student
projects explore the areas of 5G and beyond, blockchain, web 3.0, artificial intelligence , and
IoT security. He can be contacted at email: abjag.n@gmail.com.
