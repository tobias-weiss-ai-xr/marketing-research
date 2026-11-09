---
title: 'From Words to Worlds: Transforming One-line Prompt into Immersive Multi-modal Digital Stories
  with Communicative LLM Agent'
url: https://arxiv.org/abs/2406.10478
category: ai-marketing
subcategory: empirical
date: 2024-06
venue: ''
authors:
- Samuel S. Sohn
- Danrui Li
- Sen Zhang
- Che-Jui Chang
- Mubbasir Kapadia
source: arxiv
pdf_url: https://arxiv.org/pdf/2406.10478
pages: 42
chars: 85956
fetched_at: '2026-11-08T13:18:37+00:00'
kb_version: 1
---

# From Words to Worlds: Transforming One-line Prompt into Immersive Multi-modal Digital Stories with Communicative LLM Agent

From Words to Worlds: Transforming One-line Prompt into
Immersive Multi-modal Digital Stories with Communicative
LLM Agent
Samuel S. Sohn 1,*, Danrui Li 1,*, Sen Zhang 1,*, Che-Jui Chang 1, and Mubbasir
Kapadia1
1Rutgers University, 08854, New Jersey, USA
*Equal contribution
Consistency
Consistency across
modalities
Scene InteractivityAgent-wise Intervention Flexibility
“A boy that has
an adventure in
the woods ”
One-line text input
StoryAgent
Framework Long-duration multi-modal digital
storytelling
Scene-aware
camera focus
Scene-aware
character gestures
Character consistency across scenes
Change screenplay styles
Change character/world settings
Change plots
Scene-aware
dialogues
I've heard the rumors
about the woods, but
I can't help but want
to explore it.
I've heard of the
woods, so haunted
and deep, I must
explore, while the
world's asleep.
Make it
rhythmic
Switch to city world
setting
City world setting
with four peopleBase story
They finally decipher
the messages that
lead them to a
specific tree…
After days of
decoding, they
finally decipher the
messages which tell
the tale of a hero…
Minor plot
change
Figure 1: StoryAgent is a digital storytelling generation framework that integrates communicative
Large Language Model agents with state-of-the-art generative models and tools. Taking one-line
text instruction as input, it produces digital storytelling content with scene interactivity, long-
duration consistency, and intervention flexibility.
Abstract
Digital storytelling, essential in entertainment, education, and marketing, faces challenges
in production scalability and flexibility. The StoryAgent framework, introduced in this paper,
utilizes Large Language Models and generative tools to automate and refine digital storytelling.
Employing a top-down story drafting and bottom-up asset generation approach, StoryAgent
tackles key issues such as manual intervention, interactive scene orchestration, and narrative
consistency. This framework enables efficient production of interactive and consistent narra-
tives across multiple modalities, democratizing content creation and enhancing engagement.
Our results demonstrate the framework’s capability to produce coherent digital stories without
reference videos, marking a significant advancement in automated digital storytelling.
Key W ords:Pedestrian Model, Visual Attention, Retail Environment, Transportation
hubs
1
arXiv:2406.10478v2  [cs.CL]  21 Jun 2024

2 Samuel S. Sohn, Danrui Li, Sen Zhang et al.
1 Introduction
Digital storytelling has emerged as a powerful medium across various domains, including enter-
tainment, education, and marketing [1, 2, 3] due to its ability to combine multimedia elements
such as text, images, audio, and video to create immersive and interactive digital narratives. Its
versatile applications, ranging from interactive narratives in video games to immersive experiences
in virtual reality, make it an indispensable tool for conveying information and eliciting emotions
in today’s digital age. Traditionally the production processes of digital storytelling narratives are
often time-consuming and resource-intensive, limiting the speed and volume of content output.
Hence, there arises a critical need to streamline and automate the production pipeline to meet
the growing demands for engaging and dynamic storytelling content. Recent advancements in text-
based generative models[4, 5, 6, 7, 8, 9, 10], which enable synthesizing assets in text, image, sound,
and motion, have facilitated a hands-free digital storytelling production. It can democratize the
creation process and potentially enable anyone who lacks the artistic skills to produce complex
digital narratives easily. Several previous works [11, 12, 13, 14] tried to consolidate an automation
procedure for part of the production pipeline for different use cases such as immersive interactive
storytelling, storyboard making, staging, and script writing and functioning as authoring tools.
With the help of multimodal generative models, we could ease the procedure of producing assets for
digital storytelling. However, significant challenges persist in leveraging those multimodal generative
models.
One notable challenge is the need for flexible intervention ( Challenge 1 ), as human creators
often require the ability to modify initial generation results according to their preferences. Text-
based generative models[7, 9] are proficient at creating high-quality short clips but offer limited
fine-grained control over outcomes, such as modifying characters while maintaining the same sto-
ryline. Conversely, procedural methods [12, 15] enable fine-grained control but typically require a
specialized interaction interface with the framework, which often lacks a universal and convenient
approach for human intervention. Moreover, orchestrating the interactions between characters, ob-
jects, and scenes remains a difficult task ( Challenge 2), yet indispensable to improving the visual
fidelity and elevating the digital storytelling experience [16]. Finally, consistency is needed for au-
dience engagement. For instance, character appearances and voice tones should remain consistent
with the narrative context throughout the story. In addition, consistency should also include the
synchronization of the textual plots and downstream modalities, including audio, speech, and visuals
[17, 18, 19, 20, 21, 22]. Despite advancements in diffusion-based animation generation [23, 24, 25],
existing methods struggle to ensure long-term consistency or require additional inputs like reference
videos or skeletons ( Challenge 3).
We propose a novel StoryAgent framework, which integrates communicative Large Language
Model agents [26, 27] with generative models and tools. Our framework operates by initially drafting
the story by a top-down approach, using communicative LLM agents to decompose text instructions
into a hierarchical textual representation of the digital storytelling content, where the leaf nodes are
descriptions of a single modality for a snippet of the timeline. Subsequently, it employs generative
models and tools in a bottom-up fashion to create and assemble the corresponding assets from text
descriptions.
The framework addresses the three aforementioned challenges. First, its textual representa-
tion and generation pipeline facilitate fine-grained control and intervention for human developers
through simple natural language instructions (Challenge 1). Leveraging the reasoning capabilities
of Large Language Models, the framework can comprehend instructions to identify and modify the

From Words to Worlds 3
World Character Audio Others
Plot Semantic Visual Appearance Animation Music Speech SFX Cinematography
[28] ✓
[29] ✓
[30] ✓ △
[13] ✓
[31] △ △ ✓+ △
[32] ✓ △ △ △
[8] ✓ ✓ + △ ✓
Ours ✓ ✓ ✓ ✓ + △ △ ✓ ✓ ✓ + △ ✓
Table 1: Digital storytelling components covered in prior works and ours. ✓= generative models.
△ = retrieval methods.
corresponding leaf nodes in the hierarchy, while keeping other components unchanged. This process
allows for targeted adjustments without disrupting the rest of the content. Moreover, by combining
the bottom-up idea in the procedural generation pipeline with the top-down hierarchical textual
representation, our framework handles the issue of consistency and scene interactivity ( Challenge
2). For instance, a character’s appearance across time frames is linked to the same costume asset
ID within the textual representation. During video rendering, this asset is consistently reused,
ensuring visual uniformity across all scenes. Similarly, semantic and spatial information from the
generated images is captured and integrated into the textual hierarchy, paving the way to the scene
interactivity for downstream components. Inherently, with the design of our framework, it can
generate videos that require no reference videos as inputs, and the temporal limitation does not
exist(Challenge 3).
Additionally, by leveraging text as the intermediate product to decouple story drafting and asset
generation, our framework facilitates a plug-and-play structure. It not only allows for unprecedented
coverage of modalities (see Tab. 1), but also easy integration of the latest generative models,
which ensures that our framework performance can continuously benefit from ongoing research
developments.
2 Background
2.1 Digital storytelling as authoring tools
Digital storytelling has traditionally focused on providing authoring tools for human developers,
typically adopting a procedural generation approach rather than end-to-end solutions like [9]. This
methodology incorporates a wide range of storytelling components. Following the definition of [17],
the components can be categorized into plots (textual contents such as story arc and events) and
space (world settings, characters, scene props, etc.).
Previous storytelling authoring tools like [11, 12, 13, 14] are made for a specific stage in the film
production pipeline, to involve human invention and refinement, they require domain knowledge for
users. Our StoryAgent framework provides agent-wise human intervention both on the high and
low levels for amateurs and professionals.

4 Samuel S. Sohn, Danrui Li, Sen Zhang et al.
2.2 Enable scene interactivity
Recent studies have advanced the dynamics of character interactions within 3D environments, sig-
nificantly aided by the explicit spatial representations of 3D objects [31, 16, 33, 34, 18, 35, 36, 37].
In contrast, for 2D art styles, despite diffusion-based models delivering superior visual quality,
the lack of inherent spatial scene information within 2D images poses challenges for implementing
interactivity.
Nevertheless, existing research in image understanding offers many tools for deducing spatial
data from images, including techniques like segmentation [38] and depth estimation [39]. These
methodologies can underpin a procedural pipeline designed to facilitate interactivity in 2D contexts.
This paper represents an initial effort to enable such scene interactivity for 2D art styles.
2.3 Consistency in digital storytelling
Prior works have explored various approaches to ensure coherence and consistency within the plot
generation, such as event-driven [15], persona-driven [40, 41], state-space planning[42], and top-
down decomposition [43]. However, for the consistent joint generation between plot and space
components, previous studies have been limited, generally focusing on one or two areas such as
crowd motion [44], cinematography [13], world settings [30, 45] etc. (see Tab. 1). While some
approaches have aimed to address the alignment of all visual components simultaneously, typically
using latent diffusion text-to-image models [46, 47, 48], their effectiveness is still constrained by the
time length, rendering them unsuitable for long-term digital storytelling scenarios. In this work, we
aim to achieve a wide range of consistency between various components from a procedural approach.
2.4 Generative digital storytelling with LLM agents
Prior works have explored LLM-assisted generation frameworks covering several components such
as text[28, 29], audio[8], and visual[32], where LLMs have shown their capabilities in assisting
single-modal asset generation in the following aspects:
Firstly, they can extract information from natural language descriptions and convert it into
formatted parameters [49, 32]. Leveraging their world knowledge, LLMs can also break down com-
plicated concepts into several simpler components [8], which lowers the difficulties for downstream
generative models. In addition, the organization of components can be stored and updated in ex-
plicit formats [50]. Finally, with reasoning capabilities [51, 52], LLMs can plan for the generation
tasks with predefined toolsets and real-time feedback. But prompt-based narrative scene genera-
tion tools like [32] are limited in the ability to generate multiple coherent and compelling narrative
scenes in sequence.
LLM agent systems are widely used in complex generation tasks such as game world narratives
[53] and computer programs [54]. In these cases, the consistencies are achieved by predefined
hierarchical memories and reflection procedures. In this paper, we apply an LLM agent system to
ensure consistency in both temporal and modal dimensions.
3 Method
The entire pipeline (see Fig. 2) begins with a text instruction, then develops an intricate storyline
by an LLM-agent-based story cluster (see 3.1) with scene understanding capabilities (see 3.2).

From Words to Worlds 5
Long-duration
digital story
Compose
Agent
Scene Understanding Team
“A story about Jack
and magic  beans”
One line text input
“A boy that has an
adventure in the
woods ”
Speech Team
Character Team
Environmental Sound Team
Story
Cluster
Settings Team
… …
Character Team
…
Setting
Affordance Team
… …
Screen play
Team
…
Story arc Team
…
Story beat Team
…
Story scene Team
…
Timmy (excited): I want to
explore the forest!
Sound of folk chatting and the
splash of the fountain
Table (depth: 5, region: [350,…]),
Window (depth: 7, region...)…
Timmy is a boy with blue eyes…
The house is decorated with
blue candles…
Character
Speech
Sound
Scene
…
…
… …
…
…
…
SFX
composer Search API
SFX
decomposer
Query and
rank
SFX
generator
Speech
Reference Speech API
Profile
extractor
Voice
generator
Scene
captioning
Scene
segmenter
Scene
generator
Depth
estimator
Character
composer
Body part
generator
Character
parameterizer
LLM agent
Generative models
or tools
… Intermediate product in text
Intermediate product
in image
Intermediate product
in audio
Figure 2: The framework of StoryAgent. Beginning with a text instruction, the framework builds the
story with task decomposition, specifying all asset files for each modality in the textual description.
Then generative models and tools are organized to create and compose tangible assets of the story.
The story cluster deconstructs the digital storytelling task into multiple subtasks, each targeting
a specific modality. For each modality, the story cluster specifies all output asset files of the story
through the textual descriptions. Based on these descriptions, generative models and tools are
organized into asset generation teams (see 3.3) to create tangible assets of the story. Finally,
approaches for potential interventions are introduced in 3.4.
3.1 Story cluster
The story cluster drafts the storyline through a network of LLM agent teams. Inspired by the
pipeline workflow in the film industry, the agent teams handle story arcs, characters, settings, story
beats, setting affordances, story scenes, and the screenplay respectively.
The network begins with a story arc team, which composes a blueprint of the narrative in
text, instructing the entire production at the highest level. Then, the blueprint is distributed to
numerous downstream teams to handle different narrative components such as character settings,
settings, scenes, screenplays, and so on. The intermediate products that are circulated between
teams are always in text. Although the cluster is built upon AutoGen[27], the circulation follows a
predefined procedure (see Fig. 1) to ensure generation stability.
Based on upstream content, each team’s generated outcome is incrementally optimized through
single-stage or multi-stage dialogues (see Fig.3). All multi-stage configurations are manually de-
signed to further decompose the generation process, as some agent teams require complex reflections
that the current LLM backbone cannot handle. In each stage, the dialogue takes place between two
LLM agents. Inspired by the role-playing method in [26], each agent is initialized with a system
prompt, where dialogue history and upstream content are attached to an agent-specific template.
Among the two, one “expert agent” is responsible for creating component specifications based

6 Samuel S. Sohn, Danrui Li, Sen Zhang et al.
Expert Agent 1
JSON JSONJSON
Expert Agent 2
Critic Agent 1 Critic Agent 2
Stage 1 Stage 2
Figure 3: Structure of a two-stage LLM agent team. It takes upstream JSON as inputs and uses
two expert-critic LLM agent pairs to process. Finally, another JSON string will be generated for
downstream teams.
on predefined requirements and upstream inputs. The other “critic agent”, evaluates and scores
them against predefined criteria. The roles of the agents, their constraints, and the output formats
are shared between the expert and the critic within individual team stages but differ across different
agent teams and stages. For comprehensive prompts for all agents, please refer to the appendix.
Starting from the expert agent, the two respond to each others’ outputs in a round-robin way,
where the circulation ends when the critic is satisfied with the expert’s outcome.
Utilizing GPT-4 as the LLM agent backbone, this expert-critic design facilitates a robust capac-
ity for self-correction, which ensures consistency between the upstream commands and downstream
outcomes. To illustrate, consider the following example where the critic agent helps the expert
agent refine a character profile:
Admin
(provide a story arc in JSON format)
Expert in Character
{”name”: ”Village elders”... }
Critic in Character
...The character name ”Village elders” is plural and should be singular...The ex-
pert should break down ”Village elders” into individual characters with singular
names. For example, they could create characters for a few prominent elders
and villagers.
Expert in Character
{”name”: ”Elder John”... },{”name”: ”Elder Mary”... }...
Critic in Character
(pass the check)

From Words to Worlds 7
3.2 Image-based scene understanding and interaction
Simply putting the characters in the foreground and the story setting images in the background
could result in unreasonable arrangements like a character standing on the water or up in the
air. To enhance the fidelity of each scene and give audiences a better immersion in the story, the
pipeline conducts several measures: first fusing image semantic segmentation and depth estimation
explicitly and implicitly as the visuospatial information and then letting setting affordance agents
to enable foreground characters to interact with background images, which would otherwise be
disjoint. The visuospatial information could also benefit cinematography by providing the object’s
estimated position and distance to the camera.
3.2.1 Scene understanding
The scene understanding process is structured in three key stages, designed to equip setting agents
with comprehensive knowledge of the narrative environment, enabling them to provide relevant
affordances for dynamic story interaction.
Initially, story setting agents construct a hierarchical graph of all narrative settings. Each node
within this graph represents a distinct setting and includes essential details like the setting’s name,
visual prompts, and its relationship with other settings (parent and children). From these visual
prompts, background images are generated using [5], forming the visual foundation of the story’s
environments.
The generated images undergo semantic segmentation to identify and categorize objects within
each setting. This segmentation ([38]), paired with depth estimation ([55]), provides a three-
dimensional understanding of each scene. Objects are encapsulated within bounding boxes, which
highlight their spatial position and median depth, aiding in the precise placement within the nar-
rative space. This crucial spatial data informs how characters and cameras will interact with these
objects, ensuring accurate and realistic scene compositions(see 3.2.2).
In the final stage, setting affordance agents utilize the detailed object and spatial data (see ap-
pendix 6.1.5) to create a rich layer of interaction possibilities through affordances. These affordances
are meticulously documented with object relations, narrative relevance, and evidence of the object’s
existence in the image. This structural information is then passed to story scene agents, who use
it to script interactions and narrative events, ensuring that characters can interact naturally with
their environment.
3.2.2 Character and camera interaction
Our pipeline processes and utilizes object location information to enhance storytelling through
precise cinematography. Once this data is captured, screenplay agents integrate it to orchestrate
scene dynamics effectively. This involves using the object centers as focal points in animation and
cinematography—characters interact with key objects via targeted movements, and cameras adjust
focus and framing based on the object’s position and estimated distance. This approach allows for
the strategic selection of shot types (close, medium, or wide) to best capture the narrative moment.
3.3 Asset generation teams
Each agent generation team represents a hybrid of LLM agents and generative models. Gener-
ally, the LLM agents here serve as the bridge between the upstream textual descriptions and the

8 Samuel S. Sohn, Danrui Li, Sen Zhang et al.
Figure 4: Semantic scene understanding example
downstream generative models and tools. Specifically, LLM agents aim to convert specifications ar-
ticulated in natural language into model parameters and reflect on feedback from generative models
and tools.
In our study, we employ the rigging framework, CC2D[56], to construct and animate human
avatars. To generate image assets for different parts of the character, such as pants and clothing, we
input appearance descriptions into a text-to-image generative model [5]. These assets are produced
using a supplemental prompt—such as “detailed, cartoon, 8k”—to enhance the initial description.
Since diffusion-based generative models are hard to generate meaningful 2D textures directly, the
generative procedure goes through a composite and decompose process. First We composite the 2D
texture of the tunic and pants into a meaningful shape of the asset (see Fig. 5), then generate assets
using its assembled mask. After the generation is done, we decompose the whole assets back with
their texture mask and then integrate them within the CC2D framework (see Fig. 6). Textures are
loaded during runtime (see Fig. 7).
For background image creation, we utilize the same generative model to ensure style consistency.
We use [57] to lift the token limitation and generate backgrounds by visual prompts provided by
the setting configuration agents. Furthermore, these images undergo further processing in a scene
understanding cluster (see 3.2) to enable interactivity. This additional step allows for dynamic
interaction within the generated environments (detailed in 3.2).
In speech generation, a character description simplified by LLMs is firstly fed to AudioGen[10]
to create a voice fingerprint, containing the voice feature of that character. Then it is smoothed by
XTTS [58], producing a reference speech audio. Next, the reference audio, speech in text, and the
emotion state in text are fed to ElevenLabs API [59] to create the final speech audio.
Inspired from [8], the sound description is firstly decomposed to components by LLMs, where
different decomposition methods are tailored for sound effect types (looping or one-time). Then,
for each component, an LLM agent is applied to search corresponding assets on FreeSound [60],

From Words to Worlds 9
Figure 5: Character pants asset examples
Figure 6: Character parts mask. Left is the original texture format and right is the assembled
mask for better generation quality
where the assets are evaluated by feeding their descriptions to the agent. The search is repeatedly
triggered with keywords that are optimized by the agent using previous search results. If there are
no suitable assets, AudioGen[10] is called to create one. All music clips are created by MusicGen
[10], a text-to-music generative model.
Consistency is optimized by communication between LLM agents and other generative models
and tools. For instance, in sound retrieval, after the initial description is broken down into simpler
components, each component’s description is transformed into a query string, which is iteratively
refined based on the results of previous searches. This method underscores the dynamic use of
LLMs to enhance the consistency between the text description and the retrieved assets.
Admin
The sound of townsfolk chatting, children playing, and the gentle splash of the
fountain water.

10 Samuel S. Sohn, Danrui Li, Sen Zhang et al.
Figure 7: Pants asset in the runtime
Decomposition Agent
{ ”name”: ”townsfolk chatting”, ”desc”: ”the sound of townsfolk chatting in
a town square”, ”volume”: -25 }, { ”name”: ”children playing”, ”desc”: ”the
sound of children playing in a town square”, ”volume”: -20 }, { ”name”: ”foun-
tain water”, ”desc”: ”the gentle splash of fountain water in a town square”,
”volume”: -30 }
Decomposition Agent
@Query Agent the gentle splash of fountain water in a town square
Query Agent
@Search API water +fountain +splash +gentle -ocean -river
Search API
(a list of sound with descriptions)
Query Agent
water +fountain +gentle +town -ocean -river -greenway
Search API
(a list of sound with descriptions)
Query Agent
fountain +gentle +town
Search API
(a list of sound with descriptions)

From Words to Worlds 11
Query Agent
(The index of the best sound asset)
3.4 Intervention
While our framework facilitates a hands-free generation process, it also offers flexible intervention
approaches for human creators. The framework allows for the following intervention approach:
• Full regeneration from the beginning: by feeding prior generation results and extra instructions
to the framework inputs, the framework updates all contents with maximum consistency
ensured. We apply this approach in Section 4.3. Please refer to the instruction prompt in the
appendix.
• Intermediate the process: by fixing upstream results and altering agent system prompt, the
framework updates all downstream contents with finer control over selected modalities.
• Replacement: by replacing generated results with human-crafted ones, human creators get
their maximum control over the outcome. However, replacing downstream assets may cause
inconsistency issues since the framework cannot reflect on them.
(a) A curious boy
named Tim and
his adventurous
friend, Sam, decide
to explore the
woods near their
homes, despite the
rumors of it being
haunted.
(b) As they ven-
ture deeper into
the woods, they
find cryptic mes-
sages carved into
the trees. They
decide to decipher
these, believing
they might lead to
a treasure.
(c) They finally
decipher the mes-
sages that lead
them to a specific
tree. They find an
old, weathered box
buried at the base
of the tree.
(d) They open the
box to find a map
of their town from
decades ago, with a
path marked lead-
ing back to their
homes.
(e) They follow the
path on the map
and realize that
the treasure was
the journey and
the memories they
made. They return
to Sam’s home
with friendship
strengthened.
Figure 8: Screenshots of a story generation, with one frame selected from each stage of a five-stage
storytelling arc.
4 Storytelling Experience
In this section, we present the qualitative results of our pipeline, highlighting three benefits of our
text-based pipeline. We first demonstrate how the reasoning capabilities of StoryAgent facilitate
consistency between plots and downstream components. Then we illustrate how the coordination

12 Samuel S. Sohn, Danrui Li, Sen Zhang et al.
of various agents and generative tools ensures scene interactivity in 2D art styles. Finally, we show
its capability to adapt human intervention during the generation process, thus providing story
alternatives for human creators. Here is the story arc for our baseline story:
In the story, Tim and his friend Sam explore the woods near their homes, discovering cryptic
messages on trees that they believe might lead to treasure. Following the clues, they uncover an
old box containing an antique map of their town. The map guides them back home, revealing that
the real treasure was the adventure and the bond they strengthened along the way.
4.1 Story consistency
Our framework keeps a hierarchical organization of all asset files, which enables asset re-usages.
Consequently, this structure ensures appearance consistency across all visual elements, both within
neighboring frames and across different scenes (see Fig.9).
Figure 9: Character consistency across scenes. Based on the textual descriptions of the generative
narrative, the character assets are reused across scenes, ensuring visual consistency.
Additionally, our framework ensures consistency across modalities, as visual and audio elements
together create an emotive storytelling experience. In this manuscript, the generated auditory
descriptions of scenes are paired with corresponding visualizations in Fig.10, illustrating how our
framework maintains alignment between visual and audio styles.
4.2 Scene interactivity
StoryAgent can integrate detailed scene information into digital storytelling, creating scene inter-
activity. We focus on two common practices in digital storytelling for children, effectively engaging
young audiences by emphasizing narrative elements.
Firstly, the interactions take place at the semantic level. When the story unfolds, characters
will refer to the scene objects in their dialogue, maintaining the story’s coherence at the same time.
In Fig.11, the characters are talking about their childhood memories, while raising a fence in the
background as a reference.
The interactivity is also enhanced by the synchronous interplay between the dialogue, character
gestures, and cinematography. As characters discuss an object within the scene, not only does
the camera shift focus to and zoom in on the object for detailed visualization, but the characters
also direct their gazes and gestures toward it. This coordination makes digital storytelling more
accessible and engaging for children, as detailed in Fig. 12.

From Words to Worlds 13
[Visual] A small room with a single bed, a wooden desk,
a bookshelf filled with books, a window overlooking the
yard, and a blue rug.
[Audio] Background sounds of a quiet suburban
neighborhood, with distant sounds of children playing
and birds chirping.
[Visual] A dense forest with towering trees, a carpet of
fallen leaves, a narrow trail, bird nests in branches,
and a quiet stream.
[Audio] Background sounds of rustling leaves, chirping
birds, and distant animal sounds create an atmosphere
of being deep in the woods.
Figure 10: Consistency across modalities. Our framework ensure the coherence between visual and
audio elements by aligning their text descriptions.

14 Samuel S. Sohn, Danrui Li, Sen Zhang et al.
Figure 11: Character dialogue with scene understanding. (left) ”Look at our house Sam. It is not
the treasure we expected, but it’s a symbol of our adventure today” (right) ”You are right Tim.
And remember the times we used to sit on that fence, dreaming about finding treasure?”
4.3 Agent-wise human intervention
Our framework’s coarse-to-fine approach to generating digital narratives lends itself to flexible hu-
man intervention because all agents that are affected by the intervention are strictly downstream.
Below, we demonstrate this flexibility by altering a base story generation outcome at various loca-
tions within the pipeline, each corresponding to a different modality in the storytelling process.
First, our framework demonstrates its capability to adapt writing styles while preserving the
story’s outline. Here we directly instruct a downstream agent team to compose the dialogue in the
screenplay as rhyming couplets. This allowed us to re-use the upstream content of the base story
for an easier comparison.
Base Story Script:
NARRATOR: In a quiet neighborhood, we meet Tim, a curious boy with a thirst for adventure.
TIM: I’ve heard the rumors about the woods, but I can’t help but want to explore it.
NARRATOR: Despite the rumors, Tim’s curiosity is not deterred.
TIM: No matter how far I go, I know this house will always be my safe haven.
Screenplay-Intervened Story Script:
NARRATOR: In a cozy home, lived a boy named Tim, his spirit was adventurous, his curiosity
never dim.
TIM: I’ve heard of the woods, so haunted and deep, I must explore, while the world’s asleep.
NARRATOR: With a heart full of courage, and a mind full of wonder, into the woods, Tim
decided to wander.
TIM: No matter how far, into the woods I delve, this house will always be my safe haven, my safe
shelf.

From Words to Worlds 15
Figure 12: Camera shoot and character gesture with scene understanding. (left) The camera shifts
to focus on the trees while simultaneously, the character points at them as he discusses them. (right)
The camera zooms in on the character’s face while the narrator describes his eyes.
Next, we demonstrate more complex interventions with larger-scale impacts on the narrative
generation process (i.e., downstream agents). This was achieved by using the story arc of the
base story as input in the framework with an additional instruction to preserve some elements of
the story while changing others. Unlike the screenplay intervention, where character appearances
were directly copied, this intervention fully regenerated the characters, resulting in different-colored
clothing.
Figure 9 shows two such interventions: one where the characters and plot are fixed, but the
setting is changed ( S-intervention), and another where the plot is fixed, but the characters and
setting are changed ( CS-intervention). Between both interventions, we observe that the cryptic
carvings in the forest of the base story is reflected in the cryptic graffiti in the S-intervention and
the cryptic etchings in the CS-intervention (Event 1). Each image corresponding to Event 1 also
shows that the story is making use of affordances to have characters look and point at the cryptic
imagery. In Events 2 and 3, we see that each story’s plot leads the characters on a circuitous
adventure back to where they started and they share the same moral of appreciating the adventure.
In the CS-intervention, the dialogue that was originally distributed between two characters has
been distributed among four characters, meaning that the characters have not only been added but
are being fully utilized. Unedited videos of the original story and the three interventions can be
found in the Supplementary Materials.
5 Discussions
In this paper, we introduce the ”StoryAgent” framework, which utilizes text as a central medium
to organize existing generative models to produce long-duration digital storytelling. While the
state-of-the-art prior works excel in the quality of short animation clips, our work is designed to

16 Samuel S. Sohn, Danrui Li, Sen Zhang et al.
address two principal hurdles in storytelling: long-duration alignment between modalities and scene
interactivity.
In addition, we argue such a framework offers more flexibility in real-world digital storytelling
production: First, the rapid emergence of new generative models and tools for various modalities
necessitates their swift applications into a larger pipeline at minimal cost. Our model-independent
framework facilitates a plug-and-play approach, allowing the latest research advancements to be
easily incorporated. This ensures that the performance of our framework continuously benefits from
ongoing research developments. Second, by replacing generative assets with human-crafted ones,
our framework addresses the specific limitations faced by indie developers in certain modalities. For
example, graphic artists can use our pipeline to integrate music into their digital stories, whereas
musicians can employ it to generate visual representations of their audio works. Finally, the text-
based nature of our framework permits human artists to readily adjust intermediate products,
thereby enhancing the controllability of the production process.
However, we identify several limitations in our study as follows: Firstly, while our approach has
achieved broad coverage of story components, the narrative presentation—encompassing duration,
order, and style of storytelling (collectively referred to as ’discourse’ in [17])—is only minimally
explored. Secondly, we acknowledge that the current generation results are constrained by the per-
formance and capabilities of state-of-the-art singular-modality models. This limitation affects the
alignment between the plots and the downstream components, potentially impacting the overall
coherence and immersion of the generated results. Lastly, our experimentation with scene inter-
activity is limited to a small number of scenarios. Future research should explore more complex
interaction modes, such as enabling characters to pick up items or alter the status of objects within
the environment, to enhance the interactive experience in 2D art styles.
References
[1] Adele De Jager, Andrea Fogarty, Anna Tewson, Caroline Lenette, and Katherine M Boydell.
Digital storytelling in research: A systematic review. The Qualitative Report, 22(10):2548–2582,
2017.
[2] Joe Lambert. Digital storytelling: Capturing lives, creating community . Routledge, 2013.
[3] Jing Wu and Der-Thanq Victor Chen. A systematic review of educational digital story-
telling. Computers & Education , 147:103786, 2020. ISSN 0360-1315. doi: https://doi.org/
10.1016/j.compedu.2019.103786. URL https://www.sciencedirect.com/science/article/
pii/S0360131519303367.
[4] James Betker, Gabriel Goh, Li Jing, Tim Brooks, Jianfeng Wang, Linjie Li, Long Ouyang,
Juntang Zhuang, Joyce Lee, Yufei Guo, Wesam Manassra, Prafulla Dhariwal, Casey Chu,
Yunxin Jiao, and Aditya Ramesh. Improving image generation with better captions, 2023.
URL https://cdn.openai.com/papers/dall-e-3.pdf .
[5] Daiqing Li, Aleks Kamko, Ehsan Akhgari, Ali Sabet, Linmiao Xu, and Suhail Doshi. Play-
ground v2.5: Three insights towards enhancing aesthetic quality in text-to-image generation,
2024.

From Words to Worlds 17
[6] Patrick Esser, Sumith Kulal, Andreas Blattmann, Rahim Entezari, Jonas M¨ uller, Harry Saini,
Yam Levi, Dominik Lorenz, Axel Sauer, Frederic Boesel, Dustin Podell, Tim Dockhorn, Zion
English, Kyle Lacey, Alex Goodwin, Yannik Marek, and Robin Rombach. Scaling rectified flow
transformers for high-resolution image synthesis, 2024.
[7] Jonathan Ho, William Chan, Chitwan Saharia, Jay Whang, Ruiqi Gao, Alexey Gritsenko,
Diederik P. Kingma, Ben Poole, Mohammad Norouzi, David J. Fleet, and Tim Salimans.
Imagen video: High definition video generation with diffusion models, 2022.
[8] Xubo Liu, Zhongkai Zhu, Haohe Liu, Yi Yuan, Meng Cui, Qiushi Huang, Jinhua Liang, Yin
Cao, Qiuqiang Kong, Mark D. Plumbley, and Wenwu Wang. Wavjourney: Compositional
audio creation with large language models, 2023.
[9] Tim Brooks, Bill Peebles, Connor Holmes, Will DePue, Yufei Guo, Li Jing, David Schnurr,
Joe Taylor, Troy Luhman, Eric Luhman, Clarence Ng, Ricky Wang, and Aditya Ramesh.
Video generation models as world simulators. 2024. URL https://openai.com/research/
video-generation-models-as-world-simulators .
[10] Felix Kreuk, Gabriel Synnaeve, Adam Polyak, Uriel Singer, Alexandre D´ efossez, Jade Copet,
Devi Parikh, Yaniv Taigman, and Yossi Adi. Audiogen: Textually guided audio generation,
2023.
[11] Marc Cavazza, Jean-Luc Lugrin, David Pizzi, and Fred Charles. Madame bovary on the
holodeck: immersive interactive storytelling. In Proceedings of the 15th ACM International
Conference on Multimedia , MM ’07, page 651–660, New York, NY, USA, 2007. Association
for Computing Machinery. ISBN 9781595937025. doi: 10.1145/1291233.1291387. URL https:
//doi.org/10.1145/1291233.1291387.
[12] Mubbasir Kapadia, Seth Frey, Alexander Shoulson, Robert W. Sumner, and Markus Gross.
Canvas: computer-assisted narrative animation synthesis. In Proceedings of the ACM SIG-
GRAPH/Eurographics Symposium on Computer Animation , SCA ’16, page 199–209, Goslar,
DEU, 2016. Eurographics Association. ISBN 9783905674613.
[13] Amaury Louarn, Marc Christie, and Fabrice Lamarche. Automated staging for virtual cine-
matography. In Proceedings of the 11th ACM SIGGRAPH Conference on Motion, Interaction
and Games, MIG ’18, New York, NY, USA, 2018. Association for Computing Machinery. ISBN
9781450360159. doi: 10.1145/3274247.3274500. URL https://doi.org/10.1145/3274247.
3274500.
[14] Marcel Marti, Jodok Vieli, Wojciech Wito´ n, Rushit Sanghrajka, Daniel Inversini, Diana
Wotruba, Isabel Simo, Sasha Schriber, Mubbasir Kapadia, and Markus Gross. Cardinal: Com-
puter assisted authoring of movie scripts. In Proceedings of the 23rd International Conference
on Intelligent User Interfaces , IUI ’18, page 509–519, New York, NY, USA, 2018. Associa-
tion for Computing Machinery. ISBN 9781450349451. doi: 10.1145/3172944.3172972. URL
https://doi.org/10.1145/3172944.3172972.
[15] Mubbasir Kapadia, Alexander Shoulson, Cyril Steimer, Samuel Oberholzer, Robert W. Sum-
ner, and Markus Gross. An event-centric approach to authoring stories in crowds. In Pro-
ceedings of the 9th International Conference on Motion in Games , MIG ’16, page 15–24, New

18 Samuel S. Sohn, Danrui Li, Sen Zhang et al.
York, NY, USA, 2016. Association for Computing Machinery. ISBN 9781450345927. doi:
10.1145/2994258.2994265. URL https://doi.org/10.1145/2994258.2994265.
[16] Hongwei Yi, Justus Thies, Michael J. Black, Xue Bin Peng, and Davis Rempe. Generating
human interaction motions in scenes with text control, 2024.
[17] Ben Kybartas and Rafael Bidarra. A survey on story generation techniques for authoring
computational narratives. IEEE Transactions on Computational Intelligence and AI in Games ,
9(3):239–253, 2017. doi: 10.1109/TCIAIG.2016.2546063.
[18] Che-Jui Chang, Samuel S Sohn, Sen Zhang, Rajath Jayashankar, Muhammad Usman, and
Mubbasir Kapadia. The importance of multimodal emotion conditioning and affect consistency
for embodied conversational agents. In Proceedings of the 28th International Conference on
Intelligent User Interfaces , pages 790–801, 2023.
[19] Che-Jui Chang, Long Zhao, Sen Zhang, and Mubbasir Kapadia. Disentangling audio content
and emotion with adaptive instance normalization for expressive facial animation synthesis.
Computer Animation and Virtual Worlds , 33(3-4):e2076, 2022.
[20] Che-Jui Chang, Sen Zhang, and Mubbasir Kapadia. The ivi lab entry to the genea chal-
lenge 2022–a tacotron2 based method for co-speech gesture generation with locality-constraint
attention mechanism. In Proceedings of the 2022 International Conference on Multimodal In-
teraction, pages 784–789, 2022.
[21] Inˆ es Salselas and Rui Penha. The role of sound in inducing storytelling in immersive en-
vironments. In Proceedings of the 14th International Audio Mostly Conference: A Jour-
ney in Sound , AM ’19, page 191–198, New York, NY, USA, 2019. Association for Com-
puting Machinery. ISBN 9781450372978. doi: 10.1145/3356590.3356619. URL https:
//doi.org/10.1145/3356590.3356619.
[22] James J. Cummings and Jeremy N. Bailenson. How immersive is enough? a meta-analysis of the
effect of immersive technology on user presence. Media Psychology, 19(2):272–309, 2016. doi:
10.1080/15213269.2015.1015740. URL https://doi.org/10.1080/15213269.2015.1015740.
[23] Mengyang Feng, Jinlin Liu, Kai Yu, Yuan Yao, Zheng Hui, Xiefan Guo, Xianhui Lin, Haolan
Xue, Chen Shi, Xiaowen Li, Aojie Li, Xiaoyang Kang, Biwen Lei, Miaomiao Cui, Peiran Ren,
and Xuansong Xie. Dreamoving: A human video generation framework based on diffusion
models, 2023.
[24] Yuwei Guo, Ceyuan Yang, Anyi Rao, Zhengyang Liang, Yaohui Wang, Yu Qiao, Maneesh
Agrawala, Dahua Lin, and Bo Dai. Animatediff: Animate your personalized text-to-image
diffusion models without specific tuning, 2023.
[25] Jun Hao Liew, Hanshu Yan, Jianfeng Zhang, Zhongcong Xu, and Jiashi Feng. Magicedit:
High-fidelity and temporally coherent video editing, 2023.
[26] Guohao Li, Hasan Abed Al Kader Hammoud, Hani Itani, Dmitrii Khizbullin, and Bernard
Ghanem. Camel: Communicative agents for ”mind” exploration of large language model
society. In Thirty-seventh Conference on Neural Information Processing Systems , 2023.

From Words to Worlds 19
[27] Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun
Zhang, Shaokun Zhang, Jiale Liu, Ahmed Hassan Awadallah, Ryen W White, Doug Burger,
and Chi Wang. Autogen: Enabling next-gen llm applications via multi-agent conversation,
2023.
[28] Prithviraj Ammanabrolu, Ethan Tien, Wesley Cheung, Zhaochen Luo, William Ma, Lara J.
Martin, and Mark O. Riedl. Story realization: Expanding plot events into sentences. Proceed-
ings of the AAAI Conference on Artificial Intelligence , 34(05):7375–7382, April 2020. ISSN
2159-5399. doi: 10.1609/aaai.v34i05.6232. URL http://dx.doi.org/10.1609/aaai.v34i05.
6232.
[29] J. Timothy Balint and Rafael Bidarra. Procedural generation of narrative worlds. IEEE
Transactions on Games, 15(2):262–272, 2023. ISSN 2475-1502. doi: 10.1109/TG.2022.3216582.
Green Open Access added to TU Delft Institutional Repository ‘You share, we take care!’ –
Taverne project https://www.openaccess.nl/en/you-share-we-take-care Otherwise as indicated
in the copyright section: the publisher is the copyright holder of this work and the author uses
the Dutch legislation to make this work public.
[30] Ken Hartsook, Alexander Zook, Sauvik Das, and Mark O. Riedl. Toward supporting sto-
ries with procedurally generated game worlds. In 2011 IEEE Conference on Computational
Intelligence and Games (CIG’11) , pages 297–304, 2011. doi: 10.1109/CIG.2011.6032020.
[31] Jia-Qi Zhang, Xiang Xu, Zhi-Meng Shen, Ze-Huan Huang, Yang Zhao, Yan-Pei Cao, Pengfei
Wan, and Miao Wang. Write-an-animation: High-level text-based animation editing with
character-scene interaction. Computer Graphics Forum, 40(7):217–228, 2021. doi: https://doi.
org/10.1111/cgf.14415.
[32] Vikram Kumaran, Jonathan Rowe, Bradford Mott, and James Lester. Scenecraft: Automating
interactive narrative scene generation in digital games with large language models. Proceedings
of the AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment , 19
(1):86–96, Oct. 2023. doi: 10.1609/aiide.v19i1.27504. URL https://ojs.aaai.org/index.
php/AIIDE/article/view/27504.
[33] Che-Jui Chang, Danrui Li, Deep Patel, Parth Goel, Honglu Zhou, Seonghyeon Moon, Samuel S
Sohn, Sejong Yoon, Vladimir Pavlovic, and Mubbasir Kapadia. Learning from synthetic human
group activities. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 21922–21932, 2024.
[34] Che-Jui Chang, Danrui Li, Seonghyeon Moon, and Mubbasir Kapadia. On the equivalency,
substitutability, and flexibility of synthetic data. arXiv preprint arXiv:2403.16244 , 2024.
[35] Pei Xu, Kaixiang Xie, Sheldon Andrews, Paul G. Kry, Michael Neff, Morgan Mcguire, Ioannis
Karamouzas, and Victor Zordan. Adaptnet: Policy adaptation for physics-based character
control. ACM Trans. Graph., 42(6), dec 2023. ISSN 0730-0301. doi: 10.1145/3618375. URL
https://doi.org/10.1145/3618375.
[36] Sebastian Starke, He Zhang, Taku Komura, and Jun Saito. Neural state machine for character-
scene interactions. ACM Trans. Graph. , 38(6), nov 2019. ISSN 0730-0301. doi: 10.1145/
3355089.3356505. URL https://doi.org/10.1145/3355089.3356505.

20 Samuel S. Sohn, Danrui Li, Sen Zhang et al.
[37] Mohamed Hassan, Yunrong Guo, Tingwu Wang, Michael Black, Sanja Fidler, and Xue Bin
Peng. Synthesizing physical character-scene interactions. In ACM SIGGRAPH 2023 Con-
ference Proceedings, SIGGRAPH ’23, New York, NY, USA, 2023. Association for Com-
puting Machinery. ISBN 9798400701597. doi: 10.1145/3588432.3591525. URL https:
//doi.org/10.1145/3588432.3591525.
[38] Enze Xie, Wenhai Wang, Zhiding Yu, Anima Anandkumar, Jose M Alvarez, and Ping Luo.
Segformer: Simple and efficient design for semantic segmentation with transformers. In Neural
Information Processing Systems (NeurIPS) , 2021.
[39] Shariq Farooq Bhat, Reiner Birkl, Diana Wofk, Peter Wonka, and Matthias M¨ uller. Zoedepth:
Zero-shot transfer by combining relative and metric depth. arXiv preprint arXiv:2302.12288 ,
2023.
[40] Zhexin Zhang, Jiaxin Wen, Jian Guan, and Minlie Huang. Persona-guided planning for con-
trolling the protagonist’s persona in story generation, 2022.
[41] Feifei Xu, Xinpeng Wang, Yunpu Ma, Volker Tresp, Yuyi Wang, Shanlin Zhou, and Haizhou
Du. Controllable multi-character psychology-oriented story generation. In Proceedings of the
29th ACM International Conference on Information & Knowledge Management , CIKM ’20,
page 1675–1684, New York, NY, USA, 2020. Association for Computing Machinery. ISBN
9781450368599. doi: 10.1145/3340531.3411937. URL https://doi.org/10.1145/3340531.
3411937.
[42] Chris Miller, Mayank Dighe, Chris Martens, and Arnav Jhala. Stories of the town: balancing
character autonomy and coherent narrative in procedurally generated worlds. In Proceedings
of the 14th International Conference on the Foundations of Digital Games , FDG ’19, New
York, NY, USA, 2019. Association for Computing Machinery. ISBN 9781450372176. doi:
10.1145/3337722.3341850. URL https://doi.org/10.1145/3337722.3341850.
[43] Juntae Kim, Yoonseok Heo, Hogeon Yu, and Jongho Nang. A multi-modal story generation
framework with ai-driven storyline guidance. Electronics, 12(6), 2023. ISSN 2079-9292. doi:
10.3390/electronics12061289. URL https://www.mdpi.com/2079-9292/12/6/1289.
[44] Chien-Yuan Chen, Sai-Keung Wong, and Wen-Yun Liu. Generation of small groups with rich
behaviors from natural language interface. Computer Animation and Virtual Worlds , 31(4-5):
e1960, 2020. doi: https://doi.org/10.1002/cav.1960. URL https://onlinelibrary.wiley.
com/doi/abs/10.1002/cav.1960.
[45] Timothy Merino, Roman Negri, Dipika Rajesh, M Charity, and Julian Togelius. The five-dollar
model: generating game maps and sprites from sentence embeddings. In Proceedings of the
Nineteenth AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment ,
AIIDE ’23. AAAI Press, 2023. ISBN 1-57735-883-X. doi: 10.1609/aiide.v19i1.27506. URL
https://doi.org/10.1609/aiide.v19i1.27506.
[46] Adyasha Maharana, Darryl Hannan, and Mohit Bansal. Storydall-e: Adapting pretrained
text-to-image transformers for story continuation. In Computer Vision – ECCV 2022: 17th
European Conference, Tel Aviv, Israel, October 23–27, 2022, Proceedings, Part XXXVII , page
70–87, Berlin, Heidelberg, 2022. Springer-Verlag. ISBN 978-3-031-19835-9. doi: 10.1007/
978-3-031-19836-6 5.

From Words to Worlds 21
[47] Xiaoqian Shen and Mohamed Elhoseiny. Storygpt-v: Large language models as consistent story
visualizers, 2023.
[48] Chang Liu, Haoning Wu, Yujie Zhong, Xiaoyun Zhang, Yanfeng Wang, and Weidi Xie. Intel-
ligent grimm – open-ended visual storytelling via latent diffusion models, 2024.
[49] Zhongfei Qing, Zhongang Cai, Zhitao Yang, and Lei Yang. Story-to-motion: Synthesizing infi-
nite and controllable character animation from long text. In SIGGRAPH Asia 2023 Technical
Communications, SA ’23, New York, NY, USA, 2023. Association for Computing Machin-
ery. ISBN 9798400703140. doi: 10.1145/3610543.3626176. URL https://doi.org/10.1145/
3610543.3626176.
[50] Fernanda De La Torre, Cathy Mengying Fang, Han Huang, Andrzej Banburski-Fahey, Ju-
dith Amores Fernandez, and Jaron Lanier. Llmr: Real-time prompting of interactive worlds
using large language models, 2024.
[51] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan
Cao. React: Synergizing reasoning and acting in language models, 2023.
[52] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi,
Quoc Le, and Denny Zhou. Chain-of-thought prompting elicits reasoning in large language
models, 2023.
[53] Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, and
Michael S. Bernstein. Generative agents: Interactive simulacra of human behavior, 2023.
[54] Chen Qian, Xin Cong, Wei Liu, Cheng Yang, Weize Chen, Yusheng Su, Yufan Dang, Jiahao
Li, Juyuan Xu, Dahai Li, Zhiyuan Liu, and Maosong Sun. Communicative agents for software
development, 2023.
[55] Shariq Farooq Bhat, Reiner Birkl, Diana Wofk, Peter Wonka, and Matthias M¨ uller. Zoedepth:
Zero-shot transfer by combining relative and metric depth, 2023. URL https://arxiv.org/
abs/2302.12288.
[56] CC2D Essential Bundle | 2D Characters | Unity Asset Store. URL https://assetstore.
unity.com/packages/2d/characters/cc2d-essential-bundle-187410 .
[57] Damian Stewart. Compel: A prompting enhancement library for transformers-type text em-
bedding systems. URL https://github.com/damian0815/compel.
[58] CoquiAI. coqui-ai/TTS: a deep learning toolkit for Text-to-Speech, battle-tested in research
and production. URL https://github.com/coqui-ai/TTS?tab=readme-ov-file .
[59] elevenlabs/elevenlabs-python, April 2024. URL https://github.com/elevenlabs/
elevenlabs-python. original-date: 2023-03-26T11:59:52Z.
[60] Freesound. URL https://freesound.org/.

22 Samuel S. Sohn, Danrui Li, Sen Zhang et al.
Base Story Settings Intervened Character and Settings Intervened
Event 1: Deci-
pher the code
These carvings..they
might be a code...
Look at that graffiti,
Sam. It’s so cryptic!
Guys, look at these mes-
sages. They are like a
puzzle...
Event 2: Nav-
igate back to
origin
Tim and Sam...begin
their journey back
through the woods
Tim and Sam...navigate
through the bustling
cityscape
They continue their jour-
ney...
Event 3: Trea-
sure is the ad-
venture
Indeed, the real treasure
was the journey...
And the adventure, Sam.
The adventure is a trea-
sure, too.
...And the treasure was
the memories we made.
Figure 13: Story outcomes (screenshots and speech) with agent-wise intervention. The original
base story is shown in the first column, while a variant on world settings is shown in the second.
The last column is the variant where both world settings and character settings are intervened.
The results show a strong complaint to the original plot, as all outcomes show the same key events
(shown in rows). However, the diversity of the intervention modality is ensured at the same time.

From Words to Worlds 23
6 Appendix
6.1 Prompts in story cluster
For their system prompts, all LLM agents within the story cluster utilize one of two templates
provided below. Each template is tailored to a specific agent by filling in details for the agent role,
constraint, and output format. Initially, we present the templates in full and subsequently, we focus
exclusively on the aforementioned three components, which are illustrated as placeholders within
each template.
Expert Agent
{upstream_contents}
Expert {agent_name}.
Role:
{agent_role}
Constraints:
{agent_constraints}
ONLY OUTPUT A JSON FILE.
The expert must include an explanation of how each constraint is followed.
Format:
{agent_output}
Critic Agent
{upstream_contents}
Critic {agent_name}.
Check that the expert is performing its role and adhering to the following
constraints.
Role:
{agent_role}
Constraints:
{agent_constraints}
For every single constraint, output a constraint score between 0.0 and 1.0 (
inclusive) that judges the quality of Expert’s output and explain your reasoning.
Do not omit any constraints. Be very strict.
Also ensure that the expert’s output adheres perfectly to the following format
and adds nothing else:
{agent_output}

24 Samuel S. Sohn, Danrui Li, Sen Zhang et al.
Output a format score between 0.0 and 1.0 (inclusive) for whether the output is
strictly in JSON format. 1.0 means that the format is perfect. Be very strict.
DO NOT FORGET the leading and trailing "‘‘‘json" and "‘‘‘".
DO NOT CREATE unterminated strings.
If the expert has not completed all of its turns, its turn constraint score must
be 0.0.
If and only if the constraint and format scores are all equal to 1.0 (meaning
there are no suggestions), you must print TERMINATE.
Otherwise, explain to the Expert exactly why the score is less than 1.0, make
suggestions on how they can improve their score and DO NOT PRINT TERMINATE IN ANY
WAY.
DO NOT SAY "we cannot print TERMINATE".
DO NOT ASK QUESTIONS.
6.1.1 Story arc team
Agent role
In your first turn, use the story input to output a general story arc that
describes the exposition, rising action, climax, falling action, and resolution.
In your second turn, expand upon anything vague. E.g., if challenges/puzzles/
mysteries are mentioned, explain what they are specifically.
Agent constraint
1. Each character must be a singular human.
2. There must be no non-human characters.
3. Characters cannot interact with non-human characters in the story.
4. There must be multiple main characters that talk to each other throughout the
story.
5. Keep the story simple.
6. Do not be vague (e.g., "they solve a puzzle", "they encounter a mystery"), be
specific!
7. It must be possible to animate the story with characters only speaking and
walking. They cannot climb, jump, or hold anything.
8. Make sure that with each change, the motifs in the story stay consistent.
Agent output
The output should be a markdown code snippet formatted in the following schema,
including the leading and trailing "‘‘‘json" and "‘‘‘":
‘‘‘json
{
"story_arc": dict // Story arc

From Words to Worlds 25
{
"exposition": str
"rising_action": str
"climax": str
"falling_action": str
"resolution": str
}
"constraints": list[str] // Explanation for each constraint
}
‘‘‘
6.1.2 Characters team
Agent role
For each character, describe their name, gender, age, personality, beliefs,
motivations, development, and physical description.
The physical description must describe the fabric, color, texture, and
accessories of the tunic, pants, and boots that the character is wearing.
In your first turn, for each part of the story arc (exposition, rising action,
climax, falling action, and resolution) create a list of every single human
mentioned directly or indirectly with empty attributes.
In your second turn, collate these lists and populate every character’s
attributes with broad details that are consistent with the story arc.
In your third turn, make attributes much more detailed.
Agent constraint
1. Every human mentioned in the story arc must be in the character list.
2. There must be more than 1 character listed.
3. Every character must be human.
4. Every character name must be singular, e.g., an entry cannot be named "
villagers" or "siblings" because these are plural.
5. There must be a Narrator with empty attributes in its physical description.
6. Each character’s attributes must be non-empty, unambiguous, and detailed.
Agent output
The output should be a markdown code snippet formatted in the following schema,
including the leading and trailing "‘‘‘json" and "‘‘‘":
‘‘‘json
{
"story_characters": list[dict] // List of story characters
{

26 Samuel S. Sohn, Danrui Li, Sen Zhang et al.
"name": str // Character name
"gender": str // Character gender: "Male" or "Female"
"age": int // Character age
"personality": str // Character’s personality
"beliefs": str // Character’s beliefs
"motivations": str // Character’s motivations
"development": str // How the character develops throughout the story
"physical_description": dict[str] // Character’s physical description
{
"tunic": str // Description of tunic
"pants": str // Description of pants
"boots": str // Description of boots
}
}
"constraints": list[str] // Explanation for each constraint
}
‘‘‘
6.1.3 Settings team
Stage 1 Agent role
Create a hierarchical graph of settings directly or indirectly mentioned in the
story arc, where each node is a setting consists of its name, its parent setting,
a list of its children settings, and story-related information.
The parent of the current setting must be a larger area that the current setting
must be fully contained within.
A child of the current setting must be a smaller area that is fully contained
within the current setting.
All children within a setting should be navigable between each other without
leaving the setting.
The first setting should be named World and all other settings are contained
within this setting.
The World setting’s parent must be an empty string.
In your first turn, create the setting hierarchy and omit "is_outside" attributes
.
In your second turn, for each setting that has an interior enter (e.g., a house),
create appropriate children settings for the inside that are relevant to the
story arc.
In your third turn, fill in the "is_outside" attribute for each setting.
Agent constraint
1. Every single setting mentioned directly or indirectly in the story arc (both
large and small) must be included.

From Words to Worlds 27
2. For every setting that has an interior (e.g., a house), there must be at least
one child setting so that characters can enter.
3. The difference in scale between a parent setting and child setting must be
gradual. Create intermediate settings is this is not the case.
4. If a setting is a building (e.g., a house, mansion, shed, etc.), its
is_outside attribute must be true, but its children settings (rooms) must have
is_outside = false.
5. All setting names must be unique.
6. Make sure the expert completes 3 turns.
Agent output
The output should be a markdown code snippet formatted in the following schema,
including the leading and trailing "‘‘‘json" and "‘‘‘":
‘‘‘json
{
"story_settings": list[dict] // List of settings
{
"name": str // Name of the setting
"is_outside": bool // Indicates whether the setting is inside or outside.
"parent": str // Name of parent setting or empty string if none
"children": list[str] // List of children settings
}
"constraints": list[str] // Explanation for each constraint
}
‘‘‘
Stage 2 Agent role
For each setting, add a visual prompt that summarizes its physical state. Include
the visible square footage of walkable area and the visual style that all
settings should have (e.g., time period).
Agent constraint
1. The visual prompt should not include any information about the characters.
2. The visual prompt must describe at least 5 interesting objects (big or small)
in the setting.
3. The visual prompt should be written in prose and be concise and literal and
not figurative.
4. The visual prompt must be UNDER 60 words long. Do not waste any words!
5. If a setting has is_outdoors = true, the square footage should also consider
the surrounding area. If the setting has is_outdoors = false, the square footage
should be limited to the room.
6. If a setting has is_outdoors = true, ONLY DESCRIBE THE OUTSIDE of the setting.
If the setting has is_outdoors = false, ONLY DESCRIBE THE INSIDE.

28 Samuel S. Sohn, Danrui Li, Sen Zhang et al.
7. The square_footage of each setting must be at least 100. Otherwise, add
details about the parent setting into the visual prompt and update square_footage
accordingly.
8. DO NOT OMIT ANY SETTINGS.
Agent output
The output should be a markdown code snippet formatted in the following schema,
including the leading and trailing "‘‘‘json" and "‘‘‘":
‘‘‘json
{
"story_settings": list[dict] // List of settings
{
"name": str // Name of the setting
"is_outside": bool // Indicates whether the setting is inside or outside.
"parent": str // Name of parent setting or empty string if none
"children": list[str] // List of children settings
"visual_prompt": str // Description of physical state for stable diffusion
prompt
"square_footage": int // Visible square footage of setting
}
"visual_style": str // Visual style of all settings
"constraints": list[str] // Explanation for each constraint
}
‘‘‘
6.1.4 Storybeat team
Agent role
Each story beat has a description, a list of characters involved, a list of
settings involved, time of day, and how characters and the audience should feel.
In your first turn, output a detailed list of story beats.
In your second turn, split story beats that have multiple settings into multiple
story beats with single settings.
Agent constraint
1. There must be at least 1 story beat for each part of the story arc (exposition
, rising action, climax, falling action, resolution).
2. Do not introduce new settings or characters that are not in story_characters
and story_settings.
3. Each story beat’s characters list must include Narrator.
4. The passage of time during a story beat should be reasonably small to minimize
the amount of jumps in time.
Agent output

From Words to Worlds 29
The output should be a markdown code snippet formatted in the following schema,
including the leading and trailing "‘‘‘json" and "‘‘‘":
‘‘‘json
{
"story_beats": list[dict] // Story beats
{
"description": str // Description of what happens in the story beat
"settings": list[str] // List of setting used in the story beat
"characters": list[str] // List of characters present in the story beat
"time_passage": str // How much time passes during the story beat
"character_feelings": str // Describe how characters feel during the story
beat
"audience_feelings": str // Describe how the audience should feel during the
story beat
}
"constraints": list[str] // Explanation for each constraint
}
‘‘‘
6.1.5 Setting affordance team
Stage 1 Agent role
setting_objects contains a list of objects detected in that image, their bounding
boxes, and their depths. KEEP IN MIND that bounding boxes can be mislabeled or
false positives and 1 object can be detected as multiple bounding boxes.
In your first turn, add each entry in setting_objects to object_list and use the
bboxes (detected bounding boxes) and bbox_depths (average depths of the bounding
boxes) to describe the configuration of the objects in high detail. Output empty
strings for spatial_relations and evidence.
In your second turn, add the spatial_relations describing how the configurations
are related BETWEEN different types of objects in high detail. Output empty
strings for evidence.
Agent constraint
1. The spatial_relations for each object should be as specific as possible!
2. Make sure the expert completes 2 turns.
Agent output
The output should be a markdown code snippet formatted in the following schema,
including the leading and trailing "‘‘‘json" and "‘‘‘":
‘‘‘json
{
"setting_affordances": list[dict] // List of affordances per setting

30 Samuel S. Sohn, Danrui Li, Sen Zhang et al.
{
"name": str // Name of the setting
"object_list": list[dict] // List of affordances
{
"object_name": str // Object name
"configuration": str // Description of how the bounding boxes of the
object are arranged in space
"spatial_relations": str // Description of how the object is configured
with respect to other objects.
}
}
"constraints": list[str] // Explanation for each constraint
}
‘‘‘
Stage 2 Agent role
setting_prompt is the prompt used to generate an image.
setting_objects contains a list of objects detected in that image, their bounding
boxes, and their depths. KEEP IN MIND that some bounding boxes are false
positives and 1 object can be detected as multiple bounding boxes.
setting_caption describes what is visible in the image.
setting_beats lists what characters will do in the setting.
In your first turn, add the evidence that the objects appear in the image using
the setting_prompt and the setting_caption and rate that evidence from 0 to 1.
Leave the affordances list completely empty.
Even if an object is not explicitly mentioned in the prompt or caption, if
it is highly related to the context, its evidence should be high.
An evidence rating below 0.5 means that the object was falsely detected.
Keep in mind that the object detection system can misinterpret the image,
the captioning system can misinterpret the image, and the image generation
can misinterpret the prompt.
You can also use the bounding boxes as evidence, e.g., if compared to the
bounding box of another object, the current object is too small/large (
depth must also be accounted for).
In your second turn, use the story beats to populate the affordances with things
that characters can say that are relevant to the beat.
The dialogue MUST NOT say that an object looks a certain way.
Score the rating of the affordance (from 0 to 1) based on how much it
aligns with character_feelings and audience_feelings.
0 means that the dialogue is not critical to the story.
1 means that the dialogue is critical to the story.
Agent constraint
1. Dialogue in the affordances must not describe the appearance of the objects.

From Words to Worlds 31
2. The affordances list must not be empty for any object.
3. Do not omit any objects.
4. Do not output configuration or spatial_relations.
5. The affordances list must be as long as the setting_beats list.
6. Make sure the expert completes 2 turns.
Agent output
The output should be a markdown code snippet formatted in the following schema,
including the leading and trailing "‘‘‘json" and "‘‘‘":
‘‘‘json
{
"setting_affordances": dict // List of affordances per setting
{
"name": str // Name of the setting
"object_list": list[dict] // List of affordances
{
"object_name": str // Object name
"configuration": str // Description of how the bounding boxes of the object
are arranged in space
"spatial_relations": str // Description of how the object is configured with
respect to other objects.
"evidence": str // Evidence supporting the object’s presence in the image
"evidence_rating": float // Value between 0 and 1 judging the amount of
evidence
"affordances": dict // List of things that characters can say about the object
in each relevant story beat.
{
"dialogue": str // Character dialogue
"reason": str // Reasoning based on story beat
"rating": float // Value between 0 and 1 judging importance to story beat
}
}
}
"constraints": list[str] // Explanation for each constraint
}
‘‘‘
6.1.6 Story scene team
Agent role
A scene is a set of instructions for a 2D animator.
The characters parameter is a list of all characters that are present during the
scene, meaning that they have dialogue or are visible.
The setting parameter is depicted as a static background image that characters
walk in front of.

32 Samuel S. Sohn, Danrui Li, Sen Zhang et al.
Characters are only allowed to talk, so they cannot perform any other
actions.
The objects parameter lists objects that are part of the image that characters
can speak about.
If there are no affordances, the object list MUST BE EMPTY.
All objects must be from the setting_affordances.
The dialogue parameter describes what all characters talk about in high detail.
It should not include direct quotes.
The sound_effects and music_effects parameters must be consistent with the
character_feelings, audience_feelings, and setting.
Your role is to decide precisely how the story beat should be visually and
auditorily portrayed through a series of scenes.
Agent constraint
1. Do not makes scenes that are redundant with the previous or next story beats.
2. Since characters can only talk, if the story beat requires a character to do
anything else, you must convey this by having the narrator dictate it.
3. Every scene must have a sound and music effects.
4. If a scene has dialogue from characters or the Narrator, the dialogue
description must describe what they say in full detail and nothing else.
5. The scene cannot include details that cannot be animated by characters.
Characters cannot be said to make certain facial expressions.
6. Do not create more scenes than necessary.
7. There must be no new characters that are not in the character list.
8. The setting of the scene must be the lowest suitable child setting. E.g., if
two people are talking in the house, the setting should not be house, but a child
setting of the house, because house is the outside. If the people are talking
directly outside the house, then the setting should be house.
9. Each character must have dialogue.
10. The dialogue must include at least 1 object in the setting and must blend it
seamlessly into the conversation.
11. If there are no affordances, the objects list must be empty.
12. All objects must be from the setting_affordances
Agent output
The output should be a markdown code snippet formatted in the following schema,
including the leading and trailing "‘‘‘json" and "‘‘‘":
‘‘‘json
{
"scene_count_explanation": str // Explanation of the number of scenes
"story_scenes": list[dict] // Story scenes
{
"characters": list[str] // List of present characters
"setting": str // Setting name
"objects": list[str] // List of objects that characters interact with

From Words to Worlds 33
"dialogue": str // Description of character dialogue
"sound_effects": str // A description of background sound effects
"music_effects": str // A description of background music
}
"constraints": list[str] // Explanation for each constraint
}
‘‘‘
6.1.7 Screenplay team
Agent role
For the given story scene, output a sequence of actions similar to a screenplay.
At the start of a scene, all involved characters enter at the start from the left
and exit at the end to the right.
Each action can either be CAMERA, SPEAK.
The CAMERA action is used to control the camera. It must include the following
parameters: target, size.
The target determines where the camera focuses: either "setting" or the
name of a character.
The size determines how zoomed in the camera should be: "close", "medium",
"wide".
If the target is "setting", the size must be "wide".
The SPEAK action should be used for all dialogue and must include the following
parameters: speaker, line, listener, emotion, adverb, object.
The speaker must be in the list of characters (including the Narrator).
The line is the spoken dialogue.
The listener must another character that the speaker is directly talking
to or an empty string if the speaker is monologuing.
The emotion must be either Happy, Sad, Angry, Afraid, Disgusted, Surprised
, or Neutral.
The adverb must describe how the line is spoken by the character.
The object is empty by default unless the character is speaking about an
object in setting_affordances.
Create at least 5 SPEAK actions. DO NOT BE REDUNDANT. Characters should not
repeat each other.
A character’s dialogue should reflect their traits and character_feelings. E.g.,
a child should not speak like an adult.
Agent constraint
1. No actions outside of CAMERA or SPEAK can be used.
2. Make sure that characters are consistent with the story beat’s
character_feelings.

34 Samuel S. Sohn, Danrui Li, Sen Zhang et al.
3. Make sure that the audience would feel audience_feelings by the end of the
action list.
4. You must incorporate at least one object from setting_affordances if it is not
empty.
5. There must be at least 5 SPEAK actions.
Agent output
The output should be a markdown code snippet formatted in the following schema,
including the leading and trailing "‘‘‘json" and "‘‘‘":
‘‘‘json
{
"action_list": list[dict] // Story beats
{
"action_type": str // Either CAMERA, SPEAK
"params": dict // The parameters of the action_type
}
}
‘‘‘
6.2 Prompts in asset generation cluster
6.2.1 Image
Character parameterizer: agent role
Using the CC2D Guide below, output a dictionary for the body, skin details,
values for each body slider, hair, facial hair, eyebrows,
and a list of RGB values for each part in the Colors list based on the character’
s description.
All slider values are between 0 and 1 and default to 0.5 for a normal-sized adult
.
If a slider has 1 value, it should still be returned as part of a list.
Lower values produce smaller body parts.
Provide an explanation for the choices.
Colors must only have RGB list of floats (between 0.0 and 1.0) as values and
strings as keys. DO NOT ADD ANY NEW KEYS.
BLACK MUST NOT BE PITCH BLACK (0.0, 0.0, 0.0).
{
"CC2D Guide": {
"Body": {
"Base 00 Female": "base female character",
"Base 00 Male": "base male character"

From Words to Worlds 35
},
"BodySliders": {
"Body": "2 values for width/length of torso",
"Ear": "1 value for ear size",
"Foot": "1 value for foot size",
"Hand": "1 value for hand size",
"Head": "1 value for head size, but not ear size",
"LowerArm": "2 values for width/length of lower arm",
"LowerLeg": "2 values for width/length of lower leg",
"Neck": "2 values for width/length of neck",
"UpperArm": "2 values for width/length of upper arm",
"UpperLeg": "2 values for width/length of upper leg"
},
"Colors": [
"BodySkin",
"SkinDetails",
"Hair",
"FacialHair",
"Eyebrow",
"Eyes",
"Mouth",
"Armor",
"Pants",
"Boots"
],
"Eyebrow": {
"00": "default",
"01": "thinner",
"02": "more arched",
"03": "more straight",
"04": "thicker and furrowed",
"05": "bushy",
"09": "eyebrow slit",
"NULL": "none"
},
"FacialHair": {
"09": "bushy sideburns",
"10": "mutton chops",
"11": "walrus mustache",
"12": "large beard with walrus mustache",
"NULL": "none"
},
"Hair": {
"00": "buzz cut",
"01": "buzz cut",
"02": "short, messy hair",

36 Samuel S. Sohn, Danrui Li, Sen Zhang et al.
"03": "short, smooth hair with side part",
"04": "straight bob cut",
"05": "wavy bob cut",
"06": "volumous, slicked-back hair with fade on sides",
"07": "short mohawk",
"08": "short, messy mohawk",
"09": "flat, slicked-back hair with fade on sides",
"10": "flat, slicked-back hair with fade on sides with man bun",
"11": "medium length messy waves with middle part",
"12": "messy hair covering forehead",
"13": "chest-length hair with side part",
"14": "ponytail with long bangs",
"15": "shoulder-length hair with side part covering eye",
"16": "chest-length hair with middle part",
"17": "messy chest-length hair pulled back",
"18": "long ponytail with puffy front",
"19": "bob cut with side part",
"20": "bob cut with bangs",
"21": "long comb-over with fade",
"22": "medium faux hawk with fade",
"23": "small afro",
"24": "small afro with fade",
"25": "big afro",
"NULL": "bald"
},
"SkinDetails": {
"Dirt 00": "small specks of dirt on skin",
"Dirt 01": "large patches of dirt on skin",
"NULL": "no blemishes on skin",
"Scars 00": "large scar across face",
"Scars 01": "large scars across body and face",
"Tattoo 00": "geometric tattoos on arms, chest, and neck",
"Tattoo 01": "black-out tattoos on hands and feet",
"Tattoo 02": "tattoos on arms",
"Tattoo 03 Female": "tattoo on sternum",
"Tattoo 03 Male": "tattoo on sternum",
"Tattoo 04": "curving and dotted tattoos on arms, upper chest, and
upper thighs",
"Tattoo 05": "small symbol tattoos on arms, upper chest, upper thighs,
and face",
"Tattoo 06": "thick stripe tattoos on arms, upper chest, and face",
"Tattoo 07": "bold tattoos fully covering arms, legs, neck, and upper
chest"
}
}
}

From Words to Worlds 37
Character parameterizer: agent output
The output should be a markdown code snippet formatted in the following schema,
including the leading and trailing "‘‘‘json" and "‘‘‘":
‘‘‘json
{
"cc2d": list[dict] // Story beats
{
"character_options": dict // Dictionary of chosen options
for body parts, body sliders, and RGB values
"explanation": str // Explanation for choices
}
}
‘‘‘
image generation for tunic:
tunic with description: {description}, fit the mask, 3/4 perspective, cartoon, 8k
image generation for pants
pants with this description: {description}, fit the mask, 3/4 perspective front
view, cartoon, 8k
6.2.2 Sound
Background sound (looping) description decomposition
You are a sound director that decomposes the an audio description into a
composition of several small self-looping audio scripts.
You should read the input JSON and respond with a list in JSON format:
Example input:
‘‘‘
{
"desc": "The crackling of the fire and the Village Elder’s voice, weaving
tales of the forest and its spirits.",
"people": [{"name": Lily, "desc": a little girl}, {"name": John, "desc": a
blacksmith}, {"name": Village Elder, "desc": an old man}]
}
‘‘‘
Example output:
‘‘‘json
{
"audio_scripts": [
{’type’: ’background’, ’name’: ’fire’, ’desc’: ’The crackling of the fire
in a village’, ’duration’: 10, ’volume’: -35, ’min_pause’: 0, ’max_pause’:
0},

38 Samuel S. Sohn, Danrui Li, Sen Zhang et al.
{’type’: ’foreground’, ’name’: ’village elder’, ’desc’: ’An old man is
speaking in a village’, ’duration’: 5, ’volume’: -20, ’min_pause’: 10, ’
max_pause’: 30},
]
}
‘‘‘
The meaning of each field in audio scripts is as follows:
- type: either ’background’ or ’foreground’. ’background’ means the sound is
looping seamlessly in the background. ’foreground’ means the sound is looping
with randomized pause. There should be at least one ’background’ sound.
- name: the name of the sound
- desc: the description of the sound. Rewrite the description to replace people’s
names with its descriptions. For example, replace "John" with "a blacksmith".
And describe the sound environment at the end. For example, "in a village".
- duration: the duration of the sound in seconds. Background sounds usually have
a duration of 10 seconds. Foreground sounds usually have a duration of 1 ~ 5
seconds.
- volume: the volume of the sound in dB. The volume of background sound is
usually around -35 ~ -40 dB. The volume of foreground sound is usually around -20
~ -30 dB.
- min_pause: for foreground sounds, there should be a pause between each loop.
This is the minimum pause in seconds. if the sound only plays once (e.g. the
intro music), set this to -1.
- max_pause: this is the maximum pause in seconds. It should be less than 40. if
the sound only plays once, set this to -1.
Note:
- Don’t use ambiguous words like "forest ambience". Instead, you should break it
into specific components like "leaves rustling" and "birds chirping".
- Remove sounds related to narratoring or a single person’s speech voice.
Sound effects (one-time) description decomposition
You are a sound director that modify an audio description using a given
instruction, then decomposes the new description into a composition of several
small audio scripts.
You should read the input JSON and respond with a list in JSON format:
Example input:
‘‘‘
{
"description": "The sound of pebbles crunching under Sammy’s feet as he walks
along the river bank.",
"people": [{"name": Sammy, "desc": a little boy}, {"name": John, "desc": a
blacksmith}, {"name": Village Elder, "desc": an old man}]
}

From Words to Worlds 39
‘‘‘
Example output:
‘‘‘json
{
"duration": 3,
"audio_scripts": [
{’name’: ’pebbles’, ’desc’: ’pebbles crunching at a river bank’, ’volume’:
-20},
]
}
‘‘‘
Example input 2:
‘‘‘
{
"description": "The hoot of an owl echoes through the woods, followed by the
rustling of leaves.",
"people": [{"name": Sammy, "desc": a little boy}, {"name": John, "desc": a
blacksmith}, {"name": Village Elder, "desc": an old man}]
}
‘‘‘
Example output 2:
‘‘‘json
{
"duration": 5,
"audio_scripts": [
{’name’: ’owl’, ’desc’: ’the hoot of an owl at a river bank’, ’volume’:
-20},
{’name’: ’leaves rustling’, ’desc’: ’the rustling of leaves at a river
bank’, ’volume’: -30},
]
}
‘‘‘
The meaning of each field is as follows:
- duration: the duration of all the sound in seconds, usually around 1 ~ 10.
- name: the name of the sound.
- desc: the description of the sound. Simplify the description by removing text
that are unrelated to the sound feature. Rewrite the description to replace
people’s names with its descriptions. For example, replace "John" with "a
blacksmith". And describe the sound environment at the end. For example, "in a
village".
- volume: the volume of the sound in dB. The volume of sound effects is usually
around -40 ~ -20 dB.

40 Samuel S. Sohn, Danrui Li, Sen Zhang et al.
Note:
- Don’t use ambiguous words like "forest ambience". Instead, you should break it
into specific components like "leaves rustling" and "birds chirping".
- Remove sounds related to narratoring or a single person’s speech voice.
Sound query and rank (first run)
Given a text description about a sound effect, please generate a query string
that can be used in a search engine. You should only respond in query string.
# Query format
Queries can be composed of positive tags and negative tags such as:
‘‘‘
dog bark +city -cat
‘‘‘
and
‘‘‘
water +river -sea
‘‘‘
where positive tags are preceded with "+" and negative ones with "-"
# Your task
{description}
Sound query and rank (subsequent run)
You are an assistant for sound effect searching. Based on current search results,
please select the best result and refine the search query string to meet the
search goal.
# Query format
Queries can be composed of positive tags and negative tags such as:
‘‘‘
dog bark +city -cat
‘‘‘
where positive tags are preceded with "+" and negative ones with "-"
# Note
If no results are found, that means the current query is too strict.
You should shorten the query down to one or two tags.
# Response format
You should only respond in JSON like this:

From Words to Worlds 41
‘‘‘json
{
"best_index": "the index of the best result",
"query": "refined query",
}
‘‘‘
# Search goal
{goal}
# Search history
{history}
# Current query
{query}
# Current results
{results}
Sound selection
Given a text description about a sound effect, please choose a sound file from
the following list. You should only respond in index number. If none of the files
is good enough, respond in -1.
{system_prompt_end}
# Sound description
{description}
# Searched sound files
{results}
6.2.3 Speech
Character simplification
Please simplify the character description using one or two simple adjectives
followed by a noun.
You should read the input json and respond with a json that has the same format.
Example input:
‘‘‘json
[
{’name’: ’Tom’, ’age’: 6, ’gender’: ’male’},
{’name’: ’Carol’, ’age’: 45, ’gender’: ’female’},
{’name’: ’Max’, ’desc’: ’Wearing a black t-shirt and jeans, Max is a young
male with short, brown hair and blue eyes’},
]

42 Samuel S. Sohn, Danrui Li, Sen Zhang et al.
‘‘‘
Example output:
‘‘‘json
[
{’name’: ’Tom’, ’desc’: ’A young boy’},
{’name’: ’Carol’, ’desc’: ’A middle aged woman’},
{’name’: ’Max’, ’desc’: ’A young male’},
]
‘‘‘
Prompts for voice fingerprint (using AudioGen)
{character_desc} is speaking clearly and slowly.
Prompts for speech reference (using XTTS)
There are a lot of things that I could talk about. But it will probably sound
similar to this.
Prompts for text-to-speech API.
"{line}" {character} said {emotion_adverb}.
