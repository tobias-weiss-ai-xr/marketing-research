---
title: 'MindFuse: Towards GenAI Explainability in Marketing Strategy Co-Creation'
url: https://arxiv.org/abs/2512.04112
category: digital-marketing
subcategory: measurement
date: 2025-10
venue: ''
authors:
- Aleksandr Farseev
- Marlo Ongpin
- Qi Yang
source: arxiv
pdf_url: https://arxiv.org/pdf/2512.04112
pages: 10
chars: 53233
fetched_at: '2026-11-08T12:57:04+00:00'
kb_version: 1
---

# MindFuse: Towards GenAI Explainability in Marketing Strategy Co-Creation

MindFuse: Towards GenAI Explainability
in Marketing Strategy Co-Creation
Aleksandr Farseev
farseev@itmo.ru
ITMO University
SoMin.ai Research
Singapore, Singapore
Marlo Ongpin
marlo@somin.ai
SoMin.ai Research
Singapore, Singapore
Qi Yang
yang@somin.ai
SoMin.ai Research
Singapore, Singapore
Ilia Gossoudarev
goss@itmo.ru
Faculty of Software Engineering and
Computer Systems, ITMO University
Saint Petersburg, Russia
Yu-Yi Chu-Farseeva
joy@somin.ai
SoMin.ai Research
Singapore, Singapore
Sergey Nikolenko
sergey@logic.pdmi.ras.ru
ISP RAS Research Center for Trusted
Artificial Intelligence
Moscow, Russia
Abstract
The future of digital marketing lies in the convergence of human cre-
ativity and generative AI, where insight, strategy, and storytelling
are co-authored by intelligent systems [18]. We present MindFuse,
a brave new explainable generative AI framework designed to act
as a strategic partner in the marketing process. Unlike conventional
LLM applications that stop at content generation, MindFuse fuses
CTR-based content AI-guided co-creation with large language mod-
els to extract, interpret, and iterate on communication narratives
grounded in real advertising data. MindFuse operates across the
full marketing lifecycle: from distilling content pillars and customer
personas from competitor campaigns to recommending in-flight
optimizations based on live performance telemetry. It uses attention-
based explainability to diagnose ad effectiveness and guide content
iteration, while aligning messaging with strategic goals through
dynamic narrative construction and storytelling. We introduce a
new paradigm in GenAI for marketing, where LLMs not only gen-
erate content but reason through it, adapt campaigns in real time,
and learn from audience engagement patterns. Our results, vali-
dated in agency deployments, demonstrate up to 12 × efficiency
gains, setting the stage for future integration with empirical audi-
ence data (e.g., GWI, Nielsen) and full-funnel attribution modeling.
MindFuse redefines AI not just as a tool, but as a collaborative agent
in the creative and strategic fabric of modern marketing. In the
end of the paper, we also provide a forward-looking forecast on
how platforms like MindFuse and Google DeepMind’s ACAI are
likely to shape the future of marketing agencies. These systems
will not only reset client expectations toward greater transparency,
speed, and personalization, but will also redefine the skillsets de-
manded from the new generation of marketers. As hybrid agencies
emerge—blending creative storytelling with data science and AI
engineering—the competitive landscape will increasingly hinge on
talent. In this new environment, professionals will be expected to
This work is licensed under a Creative Commons Attribution-NonCommercial 4.0
International License.
MM ’25, Dublin, Ireland
©2025 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2035-2/2025/10
https://doi.org/10.1145/3746027.3758167
pair human imagination with technical fluency, while agencies will
need to reinvent themselves as AI facilitators and curators of brand
authenticity amidst the ongoing talent war led by platforms such
as Meta.
ACM Reference Format:
Aleksandr Farseev, Marlo Ongpin, Qi Yang, Ilia Gossoudarev, Yu-Yi Chu-
Farseeva, and Sergey Nikolenko. 2025. MindFuse: Towards GenAI Explain-
ability in Marketing Strategy Co-Creation. InProceedings of the 33rd ACM
International Conference on Multimedia (MM ’25), October 27–31, 2025, Dublin,
Ireland.ACM, New York, NY, USA, 10 pages. https://doi.org/10.1145/3746027.
3758167
1 Introduction
The online marketing ecosystem is undergoing a transformation
driven by an exponential increase in the volume and complexity
of multimedia content. From advertising libraries and social media
to consumer behavior data, marketers today navigate a turbulent
digital environment that demands not only speed and precision but
also strategic depth and creativity. The primary challenge lies in
synthesizing insights at scale without sacrificing interpretability
[27, 71, 74, 75] or intent, which has been considered to be a major
bottleneck of traditional machine learning in the marketing [14, 25,
30, 31, 37] and, more specifically, AI-driven user profiling [5, 6, 8,
13, 20–24, 26, 28, 29, 50, 61, 62, 68–70, 73, 76] domains.
Recent breakthroughs in LLMs have offered promising pathways
for tackling these challenges. These models have demonstrated
success across a range of domains, from low-resource translation
and program synthesis to engineering and control systems [10–12,
41]. Their architecture continues to evolve, with newer Transformer
variants such as Longformer [2], Linformer [67], and Mamba-style
state-space models [33, 57] drastically extending context lengths
and reducing inference complexity [45, 66]. These advances enable
the direct analysis of large-scale text and multimedia datasets—a
crucial requirement in marketing.
Furthermore, LLMs now possess multimodal capabilities [53, 64],
allowing them to jointly process image, video, and audio alongside
text. These systems can also be integrated with generative diffusion
models [35, 60] to generate campaign-ready media, making them
increasingly relevant for advertising content production [36, 44].
arXiv:2512.04112v1  [cs.MM]  1 Dec 2025

MM ’25, October 27–31, 2025, Dublin, Ireland Aleksandr Farseev, Marlo Ongpin, Qi Yang, Ilia Gossoudarev, Yu-Yi Chu-Farseeva, and Sergey Nikolenko
Despite these capabilities, a fundamental gap remains in apply-
ing LLMs to strategic marketing workflows. While they excel at
generating content, LLMs perform inconsistently incontent under-
standing—a critical task in identifying high-impact ads and strate-
gising future campaigns [ 7, 77]. This shortcoming is especially
problematic given that industry-grade content assessment models
used by platforms such as Meta [34], Google [46], and Alibaba [55]
are proprietary and inaccessible to most marketers, and although
there was a growing body of research in ad understanding [ 63],
before the advent of multimodal LLMs it had been insufficiently
powerful to actually be practical.
To address this, we propose MindFuse, a Generative AI frame-
work that reimagines the role of intelligent systems in market-
ing—not merely as tools for automation, but as co-strategists. Mind-
Fuse integrates a CTR-based prediction model with generative LLMs
to power a novel workflow for campaign ideation, audience seg-
mentation, and team briefing. Crucially, it shifts from static analysis
to dynamic persona mining and narrative generation, effectively
constructing high-quality content briefs aligned with market needs.
This system builds on recent advances in explainable and action-
able AI [52, 54, 75], using clustering techniques and LLM to extract
communication personas and thematic challenges from large-scale
ad corpora. These are synthesized into narrative briefs—compact,
strategy-ready stories that marketers can use for content calendars,
creative direction, or campaign pitches.
MindFuse is a novel brave idea, which is grounded in prior
work on recommender systems and user modeling, which tradition-
ally relied on topic models [42], convolutional networks [63], and
handcrafted user profiles [5]. Our approach moves beyond these
paradigms, offering LLM-powered, explainable pipelines that allow
human strategists to collaborate with AI on equal footing. By au-
tomating the transformation of ad performance data into creative
strategy, MindFuse envisions a new generation of AI systems that
supplant human intuition in marketing.
2 Content pillar identification
Digital marketers routinely face the challenge of processing vast
and constantly updating volumes of creative assets—ranging from
advertisements and campaign messages to competitor materials
and user interactions. In such a high-frequency, “always-on” en-
vironment, manual analysis of each asset or campaign becomes
infeasible, creating a pressing need for scalable, automated inter-
pretation tools.
To address this, we introduce a semantic layer within the Mind-
Fuse framework that leverages LLMs to extract structured insights
from marketing content. These insights—referred to ascontent pil-
lars—form the foundation for downstream strategic analysis and
narrative generation. They represent interpretable attributes such
as customer needs, product value propositions, emotional appeals,
and stylistic tone.
Our pipeline, begins by processing ad corpora through an LLM
fine-tuned with domain-specific prompts. The model identifies
structured semantic units in each creative asset (e.g., what need
it targets, which product is featured), and stores these in tabular
form. These content pillars are then aggregated and analyzed to
reveal latent patterns in a brand’s communication strategy—such
Figure 1: Sample ad analysis via LLM-powered content pillar
extraction.
as the dominant audience segments, key messaging themes, and
emotional appeals.
To demonstrate this process in action, we conducted an em-
pirical analysis of advertising content from four major Singapore-
based transportation companies. As shown in Figure 1, we collected
batches of ads from the Facebook Ad Library, then parsed them
through LLM prompts designed to simulate a strategic planner’s
line of questioning—e.g., “What is the underlying human need tar-
geted here?”, “What is the dominant product category?”, or “Which
archetype is invoked in this message?”
The resulting outputs were standardized and highly interpretable,
enabling downstream automation and large-scale comparison across
campaigns. Unlike traditional manual content audits, which are
time-intensive and limited in scope, our approach enables rapid,
scalable analysis across thousands of assets—laying the groundwork
for deeper persona and theme discovery, as described in Section 3.
3 Mining Communication Themes
3.1 From Description to Strategic Inference
Extracting surface-level descriptors such as customer needs and
product categories—what we refer to as content pillars—is only the
first step toward intelligent marketing systems. To truly augment
strategy design, AI must engage in higher-order reasoning: discern-
ing why certain messages resonate, who they target, and how they
can be recombined to create new, context-aware narratives.
Yet most marketers operate without formal data science training,
and current tools rarely support strategic ideation beyond dash-
boards and KPIs. This creates a gap between accessible insights and
actionable planning. MindFuse bridges this gap through a unified
pipeline that integrates content scoring and LLM-driven clustering
to surface latent strategic elements—namely, customer personas and

MindFuse: Towards GenAI Explainability
in Marketing Strategy Co-Creation MM ’25, October 27–31, 2025, Dublin, Ireland
thematic challenges—from large ad corpora. These form the foun-
dational elements of generative marketing storytelling, explored
further in Section 4.
3.2 Uncovering Personas from The Data
Customer personas are traditionally crafted through manual syn-
thesis of demographics, survey data, and creative intuition. In Mind-
Fuse, we replace this manual bottleneck with a semi-automated
process that uses unsupervised clustering and generative summa-
rization. Using X-Means clustering [56] on ADA embeddings [48]
derived from the “Audience” content pillar, we identify meaning-
ful groupings that reflect distinct psychological and behavioral
marketing profiles.
To ground the analysis in a competitive context, we collected
1,120 business-focused ads from Gojek and Grab, Singapore’s two
leading ride-hailing platforms, covering 2023–2024. These ads—part
of a larger corpus of 5,967 content items—were pre-filtered to focus
on B2B communication. Fig. 2 presents the three personas that
emerged: (1)Efficiency Enthusiasts(206 items): traditional-minded
decision-makers focused on operational cost savings, (2)Financial
Empowerment Champions(144 items): advocates of equitable and
flexible employee benefits, and (3)Efficiency Innovators(707 items):
technology-forward adopters seeking scalable digital solutions.
The resulting clusters are not just static categories. Through
LLM-guided summarization and image generation, each persona
becomes a narrative archetype that can be woven into campaign
strategy. This synthesis transforms latent engagement patterns into
design-ready story templates—machine-mined but human-usable.
3.3 Mining Thematic Challenges
A persona alone is not enough to drive effective storytelling. Just
as protagonists are defined by the challenges they face, marketing
narratives require a complementary communication theme—often
rooted in the implicit tension the campaign seeks to resolve.
To identify such themes, we applied a second round of X-Means
clustering to the “Insights” content pillar, again using ADA embed-
dings [48]. These clusters reflect recurring pain points, value propo-
sitions, or aspirations across campaigns. The LLM was prompted
to label and describe each theme based on the dominant content
features within the cluster.
As shown in Fig. 3, the system surfaced three distinct challenge
themes: (1)Inefficient Corporate Expense and Transportation Man-
agement(672 items), (2)Improving Business Operations and Em-
ployee Satisfaction(94 items), and (3)Streamlining Work Trans-
port Processes(336 items). These themes serve as strategic lenses
through which brands frame their messaging. When paired with
personas, they form complete narrative skeletons—fitting the ar-
chetypal “hero + conflict” structure—ready for story generation.
Unlike static segmentations used in traditional marketing, these
LLM-assisted groupings are fluid, data-driven, and continuously
refreshable as campaign data evolves.
In summary, this dual-layer personas and themes mining demon-
strates how MindFuse turns raw engagement data into generative
storytelling assets. It moves beyond explainability toward a future
where AI co-authors the narratives that define brand identity.
Figure 2: MindFuse-generated customer personas based on
semantic clustering of B2B ad content.
4 Real-World Application
MindFuse advances beyond analysis by generating strategic nar-
ratives that marketers can directly apply. Building on previously
extracted personas and challenges, the system synthesizes these
into personalized campaign stories using LLM prompts (Fig. 4).
This generative pipeline simulates real-world strategy design work-
flows—replacing manual brainstorming with data-driven creativity.
Based on detected campaign gaps, MindFuse can suggest target-
ing underused personas (e.g., “Efficiency Enthusiasts”) with over-
looked challenges (e.g., “Streamlining Work Transport”). The LLM
then generates a narrative—such as one about a fictional business
owner, “Samuel Tan”—highlighting how the brand addresses both
practical and emotional needs. These stories serve as high-quality
content briefs, on par with those crafted by human strategists,
yet produced in seconds. With a simple prompt, the story is dis-
tilled into a campaign insight, which, when paired with actual
offerings like GoJek’s Corporate Car Hailing and framed by the

MM ’25, October 27–31, 2025, Dublin, Ireland Aleksandr Farseev, Marlo Ongpin, Qi Yang, Ilia Gossoudarev, Yu-Yi Chu-Farseeva, and Sergey Nikolenko
Figure 3: Representative communication challenges ex-
tracted from insight-driven clustering.
selected challenge, forms the foundation of a compelling campaign
idea—typically a task requiring days of agency work.
To evaluate the applicability of this approach in the real-world
settings, we deployed MindFuse across four organizations—two cre-
ative agencies, one branding firm, and one consumer brand—evaluating
time savings in core strategic tasks. As shown in Table 1, market-
ing teams reported 2×–5×reductions in task durations for content
strategy, campaign planning, and audience research.
The observed efficiency gains—from 2.5×to 12×—demonstrate
that LLM-generated campaign briefs are not only practical but
transformative. MindFuse empowers marketers to move seamlessly
from insight to execution, converting audience signals and ad per-
formance data into actionable strategic narratives. This marks a
significant shift toward co-creative AI in brand storytelling, redefin-
ing how marketing strategies are conceived and delivered.
5 Content Scoring and Explainable Content
Optimization
Once strategic direction is set, teams invest heavily in generating
ad visuals, copy, and campaign assets. However, empirical studies
reveal a sobering fact: only around 20% of ad creatives succeed
in delivering strong campaign performance [15]. The rest? They
consume budgets with little return.
This inefficiency is not just a production problem—it’s a strategic
blind spot.
Figure 4: LLM-generated campaign brief: combining persona
+ challenge into a strategic narrative.
To confront this challenge, we propose a novel integration of
predictive modeling and explainability into the creative pipeline.
Within the MindFuse framework, we introduce a Content Scoring
Module, informed by Yang et al. [72], that evaluates advertising as-
sets before they go live. Built upon the SODA architecture for CTR
prediction and recommendation, this module goes further by offer-
ing interpretable attention-based heatmaps—enabling marketers to
understand why certain creatives are likely to perform better than
others.
This represents a shift from post hoc measurement to pre-launch
optimization, towards data-driven creativity where insight and
imagination converge to reduce waste and unlock impact at scale.
5.1 Predictive Scoring with Explainable Visual
Guidance
Our system generates heatmaps from attention layers within the
scoring model, highlighting regions most influential in driving
predicted user engagement. In this study, we examined whether
marketers can leverage these visual cues to optimize creative assets
and improve campaign performance.

MindFuse: Towards GenAI Explainability
in Marketing Strategy Co-Creation MM ’25, October 27–31, 2025, Dublin, Ireland
Figure 5: Heatmaps visualizing high-attention regions in ad creatives.
Table 1: Time savings from LLM-based narrative generation.
Task Before (hrs) After (hrs)
NEO360 (Performance Agency [49])
Social Media Proposals 3.0 0.75
Competitor Monitoring 3.0 0.25
Audience Research 5.0 0.5
Ad Brainstorming 2.5 0.25
Blak Labs (Creative Agency) [4]
Campaign Planning 5.0 2.0
Content Planning 10.0 3.0
Brand Analysis 10.0 1.0
Bit by Bit (Branding Agency) [3]
Content Strategy 5.0 1.0
Mothercare (Consumer Brand) [47]
Competitor Analysis 5.0 2.0
Ad Compilation 5.0 1.0
Customer Segmentation 5.0 2.0
We deployed original and modified versions of ad creatives on the
Metaadvertising platform to test the impact of removing heatmap-
highlighted elements. Each creative underwent the following:
• ads are created using MindFuse-generated stories as de-
scribed in the previous sections;
• heatmaps are visualizations of the attention layers of the
CTR prediction model [72] to highlight high-impact regions;
Table 2: Performance degradation after object removal.
Layout LPV CTR-LPV CTR F1 Score
Layout 1 0.769 0.769 0.692 0.750
Layout 2 0.751 0.751 0.250 0.500
Layout 3 0.570 0.857 0.857 0.860
Overall0.708 0.792 0.667 0.740
• critical elements were removed iteratively to create variants;
• all creatives were deployed under identical Meta campaign
settings (Objective: Landing Page View Optimization; Bud-
get, Targeting, Placements, etc. were equal for all experi-
ments for an “apple-to-apple” comparison);
• we recorded performance across 65,107 impressions, 2,243
clicks, and 1,162 LPVs.
5.2 Experimental Findings
Results in Table 2 confirm the utility of attention maps in identifying
high-impact visual features:
• Removing theprimary visual elementreduced CTR by
58%, showing its key role in user attention.
• Eliminating theCTA buttonresulted in a 22% drop in CTR,
reflecting its engagement-driving power.
• Replacing thetransparent backgroundled to a 64% CTR
drop—the most severe impact—indicating its importance for
contrast and visual clarity.

MM ’25, October 27–31, 2025, Dublin, Ireland Aleksandr Farseev, Marlo Ongpin, Qi Yang, Ilia Gossoudarev, Yu-Yi Chu-Farseeva, and Sergey Nikolenko
Figure 6: Performance comparison across modified creatives.
5.3 Implications for Creative Strategy
These results demonstrate that MindFuse’s explainable content
scoring approach, enhanced with explainability through heatmaps,
not only forecasts performance but also provides practical guidance
to optimize visual storytelling. Marketers can thus make data-driven
design choices that preserve or enhance campaign impact.
This approach shifts content scoring from black-box predic-
tion to an actionable co-creative process, enabling better-informed
decision-making and more effective content iteration at scale.
6 GenAI as a Performance Marketer
With high-performing creatives now selected through explainable
and iterative predictive modeling, the next frontier lies in scaling
campaigns under real-world constraints—namely, fixed creative
pipelines, high media spend, and rigid approval cycles. In such en-
vironments, the traditional assumption that quality creatives alone
drive results quickly breaks down. Even top-performing assets can
stagnate if not aligned with evolving audience dynamics or strate-
gic shifts. We propose a paradigm where large language models
function as autonomous performance strategists, augmenting cam-
paign optimization in-flight. Rather than relying solely on manual
intervention, these agents ingest live campaign telemetry, interpret
micro-level content performance signals, and translate them into
macro-level decisions on budget allocation, targeting refinement,
and pacing strategies. This approach reframes LLMs from content
generators to adaptive, real-time interpreters of marketing perfor-
mance—closing the feedback loop between creative impact and
strategic execution in high-stakes campaign environments.
6.1 Data and Performance Metrics
Our system interprets campaign health across the following key
metrics: (i)Reach: Unique individuals exposed to the campaign.
(ii)Frequency: Average ad exposures per user—critical to monitor
fatigue. (iii)Results: Conversions, leads, or purchases. (iv)Cost per
Result (CPR): Conversion efficiency. (v)Spend: Budget deployed.
(vi)CPM: Cost per 1,000 impressions—market competitiveness
proxy. (vii)CTR: Ad engagement rate. (viii)CR: Click-to-View: % of
users who land on the destination page. (ix)CR: Click-to-Result: %
of users completing the campaign goal.
We monitored a three-month Meta campaign (Oct 2023–Jan
2024), collecting metrics at three levels: (i) weekly—to smooth anom-
alies, (ii) daily—for day-to-day variance, and (iii) by creative—to
evaluate asset-level impact. To make the data LLM-readable, we
resized the visuals to 512×512 and encoded them and transformed
metrics into percentage changes to emphasize trends.
6.2 Prompt Design for Campaign Performance
Analysis
LLM-driven optimization relied on a custom prompt structure:
Knowledge + Role + Task + Guiding Questions + Dat Input.
Knowledge:Metric definitions (Reach, CPR, CTR, etc.) were
embedded in the prompt for consistent interpretation.
Role:The LLM was cast as a senior performance marketing lead,
expected to deliver decisive, insight-driven guidance—avoiding
hedging language.
Task:The core task was CPR minimization. The LLM reviewed
trends in CPR and Spend alongside CTR, CPM, and CR to identify
strategic shifts.
Guiding Questions:The LLM answered:
(1) How did CPR and Spend evolve?
(2) What were the corresponding changes in CTR, CPM, and
CR?
(3) Were these changes causally connected?
(4) Which secondary metrics influenced CPR the most?
(5) What creative-level insights explain these shifts?
(6) What actions should be taken?
Data Input (Tabular + Visual):Prompts included tabulated
performance data and ad creatives to enable both analytical and
visual evaluation—critical for multimodal LLMs like GPT-4.
6.3 Emergent Strategic Thinking in GenAI
Campaign Analysis
In the absence of ground-truth supervision or domain-specific fine-
tuning, the LLM, prompted only with structured campaign out-
puts, exhibits signs of emergent strategic reasoning. Operating as a
zero-shot performance analyst, the model autonomously navigates
from signal detection to tactical recommendations—mirroring the
thought process of a seasoned media strategist. The unfolding steps

MindFuse: Towards GenAI Explainability
in Marketing Strategy Co-Creation MM ’25, October 27–31, 2025, Dublin, Ireland
Figure 7: Meta campaign data: (a) weekly trendline; (b) sample creative.
below illustrate the model’s capacity for interpretive abstraction
and causal synthesis in the context of campaign analytics:
Step 1: Salient Metric Disruption.The model independently
identified volatility across key performance indicators—most no-
tably, Cost Per Result (CPR) and Spend—without explicit cues, flag-
ging instability in campaign dynamics.
Step 2: Interpreting Efficiency and Pacing Variance.It quan-
tified extreme disparities in CPR (ranging from $27.68 to $208.28)
and total Spend ($175.18 to $4664.91), diagnosing inefficiencies in
budget deployment and inconsistent cost-effectiveness.
Step 3: Auxiliary Signal Correlation.Beyond primary metrics,
the LLM tracked secondary signals such as CTR (peaking at 3.59%)
and a declining Conversion Rate—interpreting them as symptoms
of audience fatigue. Concurrent CPM spikes (up to $14.06) were
read as evidence of heightened auction competition.
Step 4: Proto-Causal Inference.Despite lacking causal train-
ing, the model connected declining CR and rising CPM as joint
contributors to CPR escalation—demonstrating an emergent ability
to reason through multi-variable interdependencies.
Step 5: Narrative Synthesis.The LLM generated a tempo-
ral hypothesis of campaign behavior: initial targeting success, fol-
lowed by mid-phase market saturation and late-stage creative fa-
tigue. This phased interpretation was neither prompted nor pre-
encoded—suggesting latent theorization capabilities.
Step 6: Cross-Modal Creative Evaluation.Through textual
analysis, the model affirmed audience-product alignment (e.g., Keto
interest), but identified visual creative gaps—specifically a lack of
compelling calls-to-action. It proposed A/B testing on visual assets,
a task typically reserved for experienced human planners.
Step 7: Actionable Tactical Blueprint.Final recommenda-
tions spanned CTR/CR monitoring, creative iteration loops, CPM-
sensitive bidding strategies, funnel-stage retargeting, and time-
based budget optimization—each reflecting principles of advanced
media planning.
These outputs demonstrate a key shift: LLMs are not merely
automating reporting—they are simulating the interpretive, diag-
nostic, and strategic reasoning of human marketing analysts. Im-
portantly, this reasoning was grounded in multimodal data and
framed in the language of marketing practice, not engineering. The
limitations are notable—some creative suggestions were generic,
highlighting the need for tighter grounding in brand context. Yet
for junior marketers or lean teams, such co-pilots represent a leap
in decision support, converting raw metrics into actionable strategy
at unprecedented speed.
In effect, GenAI enables a transition from retrospective analytics
to real-time campaign sensemaking. This is not just automation —
it is the first step toward cognitive collaboration between AI and a
performance marketer.
7 Conclusion and Future Work
In this work, we introduced MindFuse, an explainable and genera-
tive AI agent framework designed to co-author marketing strategy
with human teams. By fusing CTR-based content performance mod-
eling with LLM-driven synthesis and reasoning, MindFuse bridges
the persistent divide between unstructured advertising data and
strategic actionability.
Crucially, MindFuse is not limited to insight generation. Through
iterative content refinement guided by model feedback—and real-
time campaign optimization suggestions informed by emergent
performance signals—the system actively participates in the cre-
ative and tactical decision cycle. From predicting which creative
assets will perform, to proposing rewrites, budget reallocations, or
retargeting strategies, MindFuse demonstrates agent-like behavior
in dynamically evolving campaign contexts.
Our deployments across agencies and global brands show that
MindFuse does more than automate dashboards—it enables mar-
keters to transition from manual execution to narrative intelli-
gence. Tasks like persona mapping, content planning, and creative

MM ’25, October 27–31, 2025, Dublin, Ireland Aleksandr Farseev, Marlo Ongpin, Qi Yang, Ilia Gossoudarev, Yu-Yi Chu-Farseeva, and Sergey Nikolenko
ideation—once requiring hours of human labor—are now acceler-
ated up to 12×, while retaining transparency through embedded
explainability mechanisms.
Future Work.Looking ahead, two core directions shape the
evolution of MindFuse:
(1) Grounding Narrative Insights in Real Audience Data.
We plan to integrate statistically robust audience intelligence
from databases such as Nielsen) [ 51] and Global Web In-
dex (GWI) [32], aligning LLM-inferred personas and con-
tent narratives with empirically observed psychographics
and behavioral signals. This will ensure that strategic rec-
ommendations are not only semantically coherent but also
representative of actual audiences on the ground.
(2) Attributing Paid Media Performance to Content Pillars.
Another frontier involves correlating performance metrics
across the paid media funnel—such as CPM, CTR, CR, and
ROAS—with distinct content pillars (e.g., emotional appeal,
product value, urgency). This will enable marketers to trace
which narrative elements are truly driving business out-
comes, establishing a framework for explainable attribution
that connects story structure with media efficiency.
More than a tool, MindFuse represents a new paradigm of co-
creative AI — where strategic reasoning, storytelling, and optimiza-
tion converge in a single loop. As a decision partner, not just an
analyst, it marks a step toward the future of marketing—where
human creativity is not replaced, but augmented, iterated, and
grounded through intelligent collaboration with AI [39].
8 AI Futures in Advertising: Replacement,
Empowerment, or Insight?
Recent industry discussions, led by Meta CEO Mark Zuckerberg,
envision a radical future where advertisers provide only goals and
budgets, while AI systems autonomously manage the entire adver-
tising pipeline - creative, targeting, optimization, and measurement.
Zuckerberg described this as a “redefinition of the category of ad-
vertising, ” promising speed, scalability, and simplicity. However,
critics warn of risks to transparency and trust, as such systems
could displace agencies and in-house teams, leaving brands with
little oversight of the “black box” outcomes [19].
Alternative approaches highlight different philosophies of AI
in marketing. Google’s ACAI project, developed with DeepMind
and Oxford researchers, positions AI as a co-creator: advertisers
upload assets, insights, and inspiration, which are synthesized into
structured “super-prompts” guiding campaign generation. This
model enhances user agency and transparency, positioning AI as a
creative partner rather than a replacement [40]. Similarly, Meta’s
AI Sandbox explores collaborative generative tools that assist with
copy, visuals, and resizing, while preserving human input. Empirical
evidence suggests such co-created campaigns achieve significantly
higher returns on ad spend, underscoring the value of AI-human
collaboration [9].
A third path, represented by platforms such as SOMIN, Nielsen,
and GWI, prioritizes insight and explainability over automation.
Instead of generating ads, these systems analyze high-performing
campaigns to surface patterns in audience targeting, creative direc-
tion, and content optimization [27, 32, 51]. This paradigm augments,
rather than supplants, human creativity, embedding AI as an inter-
pretive layer that grounds strategic decisions in data.
Together, these models illuminate three diverging philosophies:
(i)replacement, where AI supplants creative and strategic func-
tions (Meta); (ii)empowerment, where AI scaffolds human creativity
(Google); and (iii)insight, where AI explains and enhances strategic
thinking (SOMIN [16] and peers).
For agencies, the implications are profound [17]. Routine tasks
such as asset resizing and A/B testing are increasingly automated,
but the enduring value of agencies lies in orchestrating these AI
systems, ensuring brand alignment, cultural nuance, and authen-
ticity. Far from being rendered obsolete, agencies must evolve into
facilitators and curators of AI-driven creativity, blending human
storytelling with machine efficiency. In this sense, AI is not elimi-
nating the role of agencies, but transforming them into higher-order
strategists in the advertising ecosystem.
The accelerating adoption of AI across advertising is driving a
profound shift in the skills required of agency professionals. While
routine tasks such as asset resizing, reporting, and basic copywriting
are increasingly automated, demand is growing for hybrid skillsets
that combine human creativity with technical fluency. Industry
leaders emphasize that traditional storytelling remains indispens-
able, but must now be paired with AI literacy, data interpretation,
and prompt engineering [58, 65]. Many agencies are investing heav-
ily in upskilling programs - for example, WPP reported over 150,000
AI training sessions for staff in 2025 - to ensure creative, media, and
strategy teams can collaborate effectively with generative systems
[58]. As a result, roles such as “creative technologists, ” AI trainers,
and ethics officers are emerging, reshaping agency talent profiles.
These shifts have fueled the growth of hybrid agencies that inte-
grate creative storytelling, data science, and engineering capabili-
ties within a single structure. Hybrid firms such as Accenture Song,
which invested billions in AI talent and platforms, demonstrate
how combining consulting-scale technical expertise with creative
execution can disrupt traditional agency models. Analysts describe
these players as “talent magnets, ” attracting professionals eager to
work across disciplines and leverage proprietary AI-driven solu-
tions [1, 38]. For clients, this model offers end-to-end capabilities -
from developing brand-trained language models to orchestrating
cross-channel campaigns - that were previously fragmented across
multiple agencies. Consequently, agencies that fail to evolve risk
losing both clients and top talent to more agile, hybrid competitors.
Overlaying these transformations is an intensifying global com-
petition for AI-savvy creative talent. Meta, in particular, has esca-
lated the talent war by offering unprecedented compensation pack-
ages, sometimes exceeding $100 million for senior AI researchers,
along with access to cutting-edge computing infrastructure [43, 59].
Meta’s push to automate creative production threatens tradi-
tional agency roles, forcing agencies to stand out through culture,
talent growth, and creative freedom. Since they cannot match big
tech’s resources, their future lies in becoming AI facilitators and
curators of authenticity, keeping human creativity central in an
increasingly automated, platform-driven ecosystem.

MindFuse: Towards GenAI Explainability
in Marketing Strategy Co-Creation MM ’25, October 27–31, 2025, Dublin, Ireland
Acknowledgements
This work was supported by a grant provided by the Ministry of Eco-
nomic Development of the Russian Federation in accordance with
the subsidy agreement (agreement identifier 000000C313925P4G0002)
and the agreement with the Ivannikov Institute for System Pro-
gramming of the Russian Academy of Sciences dated June 20, 2025,
No. 139-15-2025-011.
References
[1] Accenture. 2025. Accenture Song: Tech-Powered Creativity at Scale. https:
//www.accenture.com/. Accessed: 2025-06-01.
[2] Iz Beltagy, Matthew E. Peters, and Arman Cohan. 2020. Longformer: The Long-
Document Transformer. arXiv:2004.05150 [cs.CL]
[3] Bit by Bit. 2025. Bit by Bit - Digital Strategy, Data, and Design Agency. https:
//www.bitbybit.tech Accessed: 2025-05-31.
[4] Blak Labs. 2025. Blak Labs - Independent Creative Agency. https://www.blaklabs.
com Accessed: 2025-05-31.
[5] Kseniya Buraya, Aleksandr Farseev, and Andrey Filchenkov. 2018. Multi-view
personality profiling based on longitudinal data. InInternational Conference of the
Cross-Language Evaluation Forum for European Languages. Springer International
Publishing Cham, 15–27.
[6] Kseniya Buraya, Aleksandr Farseev, Andrey Filchenkov, and Tat-Seng Chua. 2017.
Towards user personality profiling from multiple social networks. InProceedings
of the AAAI Conference on Artificial Intelligence, Vol. 31.
[7] Yuyan Chen, Qiang Fu, Yichen Yuan, Zhihao Wen, Ge Fan, Dayiheng Liu, Dong-
mei Zhang, Zhixu Li, and Yanghua Xiao. 2023. Hallucination detection: Robustly
discerning reliable answers in large language models. InProceedings of the 32nd
ACM International Conference on Information and Knowledge Management. 245–
255.
[8] Alok Kumar Chowdhury, Aleksandr Farseev, Prithwi Raj Chakraborty, and Dian
Tjondronegoro. 2017. Automatic Classification of Physical Exercises from Wear-
able Sensors using Small Dataset from Non-Laboratory Settings. InIEEE Life
Sciences Conference 2017.
[9] Fast Company. 2025. How AI Co-Creation is Transforming Advertising Campaign
ROI. https://www.fastcompany.com/. Accessed: 2025-05-31.
[10] Maxim Enis and Mark Hopkins. 2024. From LLM to NMT: Advancing Low-
Resource Machine Translation with Claude. arXiv:2404.13813 [cs.CL]
[11] Albert Q. Jiang et al. 2023. Mistral 7B. arXiv:2310.06825 [cs.CL]
[12] Mark Chen et al. 2021. Evaluating Large Language Models Trained on Code.
arXiv:2107.03374 [cs.LG]
[13] Aleksandr Farseev. 2017.360 user profile learning from multiple social networks for
wellness and urban mobility applications. Ph. D. Dissertation. National University
of Singapore (Singapore).
[14] Aleksandr Farseev. 2023. Under the hood of social media advertising: how
do we use AI responsibly for advertising targeting and creative evaluation. In
Proceedings of the Sixteenth ACM International Conference on Web Search and
Data Mining. 1281–1282.
[15] A Farseev. 2024. Redemptive Marketing: The Path To Resolving Transparency
And Performance Dilemmas In Digital Advertising.Forbes.com(2024).
[16] Aleksandr Farseev. 2025. SOMIN: An Explainable AI and LLM Platform for
Real-Time, Data-Driven Digital Marketing Strategy. InProceedings of the 33rd
ACM International Conference on Multimedia (MM ’25)(Dublin, Ireland)(MM ’25).
Association for Computing Machinery, New York, NY, USA.
[17] Aleksandr Farseev. 2025. Will AI Make Agencies Obsolete? Rethinking the
Future of Advertising. InProceedings of the 33rd ACM International Conference
on Multimedia (MM ’25)(Dublin, Ireland)(MM ’25). Association for Computing
Machinery, New York, NY, USA.
[18] Aleksandr Farseev. 2025. Will AI Make Agencies Obsolete? The
Future of Advertising.Forbes Technology Council(22 May 2025).
https://www.forbes.com/councils/forbestechcouncil/2025/05/22/will-ai-
make-agencies-obsolete-the-future-of-advertising/ Accessed: 2025-05-31.
[19] Aleksandr Farseev. 2025. Will AI Make Agencies Obsolete? The Future of Adver-
tising. https://www.forbes.com/councils/forbestechcouncil/2025/05/22/will-ai-
make-agencies-obsolete-the-future-of-advertising/. Forbes Technology Council,
accessed: 2025-05-31.
[20] Aleksandr Farseev, Yu-Yi Chu-Farseeva, Yang Qi, and Daron Benjamin Loo. 2020.
Understanding Economic and Health Factors Impacting the Spread of COVID-19
Disease.https://www.medrxiv.org/content/10.1101/2020.04.10.20058222v1(2020).
[21] Aleksandr Farseev and Tat-Seng Chua. 2017. Tweet can be fit: Integrating data
from wearable sensors and multiple social networks for wellness profile learning.
ACM Transactions on Information Systems (TOIS)35, 4 (2017), 1–34.
[22] Aleksandr Farseev and Tat-Seng Chua. 2017. Tweetfit: Fusing multiple social
media and sensor data for wellness profile learning. InProceedings of the AAAI
Conference on Artificial Intelligence, Vol. 31.
[23] Aleksandr Farseev, Nikolay Gukov, Ilia Gossoudarev, and Uriy Zarichnyak. 2014.
Cross-Platform online venue and user community recommendation based upon
social networks data mining. 28–38 pages.
[24] Aleksandr Farseev, Denis Kotkov, Alexander Semenov, Jari Veijalainen, and
Tat-Seng Chua. 2015. Cross-social network collaborative recommendation. In
Proceedings of the ACM Web Science Conference. 1–2.
[25] Aleksandr Farseev, Kirill Lepikhin, Hendrik Schwartz, Eu Khoon Ang, and Kenny
Powar. 2018. SoMin.ai: Social Multimedia Influencer Discovery Marketplace. In
Proceedings of the 26th ACM international conference on Multimedia. 1234–1236.
[26] Aleksandr Farseev, Liqiang Nie, Mohammad Akbari, and Tat-Seng Chua. 2015.
Harvesting multiple sources for user profile learning: a big data study. InPro-
ceedings of the 5th ACM on International Conference on Multimedia Retrieval.
235–242.
[27] Aleks Farseev, Sergey Nikolenko, Qi Yang, Kirill Lepikhin, Da-Min You, Yu-Yi
Chu-Farseeva, Ilia Gossoudarev, and Marlo Ongpin. 2025. SOEX: Explainable
AI for Competitor Communications Analytics. InCompanion Proceedings of the
ACM on Web Conference 2025(Sydney NSW, Australia)(WWW ’25). Association
for Computing Machinery.
[28] Aleksandr Farseev, Ivan Samborskii, and Tat-Seng Chua. 2016. bBridge: A Big
Data Platform for Social Multimedia Analytics. In23rd ACM Multimedia Confer-
ence. ACM.
[29] Aleksandr Farseev, Ivan Samborskii, Andrey Filchenkov, and Tat-Seng Chua. 2017.
Cross-domain recommendation via clustering on multi-layer graphs. InProceed-
ings of the 40th international ACM SIGIR conference on research and development
in information retrieval. 195–204.
[30] Aleksandr Farseev, Qi Yang, Andrey Filchenkov, Kirill Lepikhin, Yu-Yi Chu-
Farseeva, and Daron-Benjamin Loo. 2021. Somin. ai: Personality-driven content
generation platform. InProceedings of the 14th ACM international conference on
Web search and data mining. 890–893.
[31] Aleksandr Farseev, Qi Yang, Marlo Ongpin, Ilia Gossoudarev, Yu-Yi Chu-Farseeva,
and Sergey Nikolenko. 2024. Somonitor: Combining explainable ai & large
language models for marketing analytics.arXiv preprint arXiv:2407.13117(2024).
[32] GlobalWebIndex. 2025. GlobalWebIndex - Audience Insight Platform. https:
//www.gwi.com. Accessed: 2025-05-31.
[33] Albert Gu and Tri Dao. 2024. Mamba: Linear-Time Sequence Modeling with
Selective State Spaces. InFirst Conference on Language Modeling. https:
//openreview.net/forum?id=tEYskw1VY2
[34] X. He, J. Pan, O. Jin, T. Xu, B. Liu, T. Xu, Y. Shi, A. Atallah, R. Herbrich, S.
Bowers, and J. Q. Candela. 2014. Practical Lessons from Predicting Clicks on
Ads at Facebook. InProc. 8th International Workshop on Data Mining for Online
Advertising (ADKDD’14). ACM, 1–9.
[35] Jonathan Ho, Ajay Jain, and Pieter Abbeel. 2020. Denoising Diffusion Probabilistic
Models. InAdvances in Neural Information Processing Systems, H. Larochelle,
M. Ranzato, R. Hadsell, M.F. Balcan, and H. Lin (Eds.), Vol. 33. Curran Associates,
Inc., 6840–6851.
[36] Wenyi Hong, Ming Ding, Wendi Zheng, Xinghan Liu, and Jie Tang. 2022.
CogVideo: Large-scale Pretraining for Text-to-Video Generation via Transform-
ers. arXiv:2205.15868 [cs.CV]
[37] Alfred Huang, Qi Yang, Sergey Nikolenko, Marlo Ongpin, Ilia Gossoudarev, Ngoc
Yen Duong, Kirill Lepikhin, Sergey Vishnyakov, Yuyi Chu-Farseeva, and Alek-
sandr Farseev. 2023. SoCraft: Advertiser-Level Predictive Scoring for Creative
Performance on Meta. InProceedings of the Sixteenth ACM International Confer-
ence on Web Search and Data Mining. 1132–1135.
[38] Marketing Agency Insider. 2023. 5 Ways Hybrid Marketing Agencies Will Trans-
form the Industry. https://marketingagencyinsider.com/. Accessed: 2025-05-31.
[39] Nimisha Karnatak, Adrien Baranes, Rob Marchant, Tríona Butler, and Kristen
Olson. 2025. ACAI for SBOs: AI Co-creation for Advertising and Inspiration for
Small Business Owners.arXiv preprint arXiv:2503.06729(2025). https://arxiv.
org/abs/2503.06729
[40] Nimisha Karnatak, Adrien Baranes, Rob Marchant, Tríona Butler, and Kristen
Olson. 2025. ACAI for SBOs: AI Co-creation for Advertising and Inspiration for
Small Business Owners.arXiv preprint arXiv:2503.06729(2025). https://arxiv.
org/abs/2503.06729
[41] Darioush Kevian, Usman Syed, Xingang Guo, Aaron Havens, Geir Dullerud, Peter
Seiler, Lianhui Qin, and Bin Hu. 2024. Capabilities of Large Language Models in
Control Engineering: A Benchmark Study on GPT-4, Claude 3 Opus, and Gemini
1.0 Ultra. arXiv:2404.03647 [math.OC]
[42] Sergei Koltcov, Olessia Koltsova, and Sergey Nikolenko. 2014. Latent Dirichlet
Allocation: Stability and Applications to Studies of User-Generated Content. In
Proceedings of the 2014 ACM Conference on Web Science(Bloomington, Indiana,
USA)(WebSci ’14). ACM, New York, NY, USA, 161–165. doi:10.1145/2615569.
2615680
[43] Steven Levy. 2025. Here’s What Mark Zuckerberg Is Offering Top AI Talent.
https://www.wired.com/story/meta-ai-talent-war/. WIRED, July 1, 2025.
[44] Yixin Liu, Kai Zhang, Yuan Li, Zhiling Yan, Chujie Gao, Ruoxi Chen, Zhengqing
Yuan, Yue Huang, Hanchi Sun, Jianfeng Gao, Lifang He, and Lichao Sun. 2024.
Sora: A Review on Background, Technology, Limitations, and Opportunities of
Large Vision Models. arXiv:2402.17177 [cs.CV]

MM ’25, October 27–31, 2025, Dublin, Ireland Aleksandr Farseev, Marlo Ongpin, Qi Yang, Ilia Gossoudarev, Yu-Yi Chu-Farseeva, and Sergey Nikolenko
[45] Xuezhe Ma, Chunting Zhou, Xiang Kong, Junxian He, Liangke Gui, Graham
Neubig, Jonathan May, and Luke Zettlemoyer. 2023. Mega: Moving Average
Equipped Gated Attention. arXiv:2209.10655 [cs.LG]
[46] H. B. McMahan, G. Holt, D. Sculley, M. Young, D. Ebner, J. Grady, L. Nie, T. Phillips,
E. Davydov, D. Golovin, S. Chikkerur, D. Liu, M. Wattenberg, A. M. Hrafnkelsson,
T. Boulos, and J. Kubica. 2013. Ad Click Prediction: A View from the Trenches.
InProc. 19th ACM SIGKDD (KDD ’13). ACM, 1222–1230.
[47] Mothercare Singapore. 2025. Mothercare Singapore - Baby and Maternity Store.
https://www.mothercare.com.sg Accessed: 2025-05-31.
[48] Arvind Neelakantan, Tao Xu, Raul Puri, Alec Radford, Jesse Michael Han, Jerry
Tworek, Qiming Yuan, Nikolas Tezak, Jong Wook Kim, Chris Hallacy, et al .
2022. Text and code embeddings by contrastive pre-training.arXiv preprint
arXiv:2201.10005(2022).
[49] NEO360. 2025. NEO360 - Full-Funnel Digital Marketing Agency. https://neo360.
digital Accessed: 2025-05-31.
[50] Liqiang Nie, Luming Zhang, Meng Wang, Richang Hong, Aleksandr Farseev,
and Tat-Seng Chua. 2017. Learning user attributes via mobile social multimedia
analytics.ACM Transactions on Intelligent Systems and Technology (TIST)8, 3
(2017), 1–19.
[51] Nielsen. 2025. Nielsen - Audience Measurement and Media Analytics. https:
//www.nielsen.com. Accessed: 2025-05-31.
[52] OpenAI. 2023. GPT-4 Technical Report. arXiv:2303.08774 [cs.CL]
[53] OpenAI. 2024. Hello GPT-4o. https://openai.com/index/hello-gpt-4o/.
[54] Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela
Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schul-
man, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Pe-
ter Welinder, Paul Christiano, Jan Leike, and Ryan Lowe. 2022. Training language
models to follow instructions with human feedback. arXiv:2203.02155 [cs.CL]
[55] Wentao Ouyang, Xiuwu Zhang, Shukui Ren, Chao Qi, Zhaojie Liu, and Yanlong
Du. 2019. Representation Learning-Assisted Click-Through Rate Prediction. In
Proc. 28th IJCAI. 4561–4567. doi:10.24963/ijcai.2019/634
[56] Dan Pelleg, Andrew W Moore, et al. 2000. X-means: Extending k-means with
efficient estimation of the number of clusters.. InIcml, Vol. 1. Stanford, CA,
727–734.
[57] Haohao Qu, Liangbo Ning, Rui An, Wenqi Fan, Tyler Derr, Hui Liu, Xin Xu, and
Qing Li. 2024. A Survey of Mamba. arXiv:2408.01129 [cs.LG] https://arxiv.org/
abs/2408.01129
[58] Mark Read. 2025. ‘Even With AI, You Still Need Traditional Storytelling Skills’ –
WPP’s Mark Read. https://www.creativesalon.com/. Accessed: 2025-06-09.
[59] Reuters. 2025. Zuckerberg’s Meta Superintelligence Labs Poaches Top AI Tal-
ent. https://www.reuters.com/technology/meta-ai-superintelligence-labs-2025-
07-17/. Accessed: 2025-07-17.
[60] Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn
Ommer. 2022. High-Resolution Image Synthesis With Latent Diffusion Models. In
Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition
(CVPR). 10684–10695.
[61] Ivan Samborskii, Aleksandr Farseev, Andrey Filchenkov, and Tat-Seng Chua.
2019. A whole new ball game: Harvesting game data for player profiling. In
Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 33. 10025–10026.
[62] Ivan Samborskii, Andrey Filchenkov, Georgiy Korneev, and Alex Farseev. 2018.
Person, organization, or personage: Towards user account type prediction in
microblogs. InInternational Conference on Electronic Governance and Open Society:
Challenges in Eurasia. Springer International Publishing Cham, 111–122.
[63] Andrey Savchenko, Anton Alekseev, Sejeong Kwon, Elena Tutubalina, Evgeny
Myasnikov, and Sergey Nikolenko. 2020. Ad Lingua: Text Classification Im-
proves Symbolism Prediction in Image Advertisements. InProceedings of the
28th International Conference on Computational Linguistics. International Com-
mittee on Computational Linguistics, Barcelona, Spain (Online), 1886–1892.
doi:10.18653/v1/2020.coling-main.171
[64] Yunlong Tang, Jing Bi, Siting Xu, Luchuan Song, Susan Liang, Teng Wang,
Daoan Zhang, Jie An, Jingyang Lin, Rongyi Zhu, Ali Vosoughi, Chao Huang,
Zeliang Zhang, Feng Zheng, Jianguo Zhang, Ping Luo, Jiebo Luo, and Chen-
liang Xu. 2024. Video Understanding with Large Language Models: A Survey.
arXiv:2312.17432 [cs.CV]
[65] Justin Thomas-Copeland. 2025. Cannes 2025: What Does AI Mean for the Future
of Agency Work? https://www.aaaa.org/. American Association of Advertising
Agencies, accessed: 2025-06-16.
[66] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones,
Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. 2017. Attention Is All
You Need.CoRRabs/1706.03762 (2017). http://arxiv.org/abs/1706.03762
[67] Sinong Wang, Belinda Z. Li, Madian Khabsa, Han Fang, and Hao Ma. 2020.
Linformer: Self-Attention with Linear Complexity. arXiv:2006.04768 [cs.LG]
[68] Qi Yang, Aleksandr Farseev, and Andrey Filchenkov. 2020. I Know Where You Are
Coming From: On the Impact of Social Media Sources on AI Model Performance.
arXiv preprint arXiv:2002.01726(2020).
[69] Qi Yang, Aleksandr Farseev, and Andrey Filchenkov. 2021. Two-faced humans
on twitter and facebook: Harvesting Social Multimedia for Human Personality
Profiling. InProceedings of the 2021 ACM Workshop on Intelligent Cross-Data
Analysis and Retrieval. 39–47.
[70] Qi Yang, Aleksandr Farseev, Sergey Nikolenko, and Andrey Filchenkov. 2022. Do
we behave differently on Twitter and Facebook: Multi-view social network user
personality profiling for content recommendation.Frontiers in big Data5 (2022),
931206.
[71] Qi Yang, Aleksandr Farseev, Marlo Ongpin, Alfred Huang, Yu-Yi Chu-Farseeva,
Da-Min You, Kirill Lepikhin, and Sergey Nikolenko. 2025. Fusing Predictive and
Large Language Models for Actionable Recommendations In Creative Marketing.
ACM Transactions on Information Systems(2025).
[72] Qi Yang, Aleksandr Farseev, Marlo Ongpin, Alfred Huang, Yu-Yi Chu-Farseeva,
Da-Min You, Kirill Lepikhin, and Sergey Nikolenko. 2025. Fusing Predictive and
Large Language Models for Actionable Recommendations In Creative Marketing.
ACM Transactions on Information Systems(2025).
[73] Qi Yang, Sergey Nikolenko, Alfred Huang, and Aleksandr Farseev. 2022.
Personality-driven social multimedia content recommendation. InProceedings of
the 30th ACM International Conference on Multimedia. 7290–7299.
[74] Qi Yang, Sergey Nikolenko, Marlo Ongpin, Ilia Gossoudarev, Yu-Yi Chu-Farseeva,
and Aleksandr Farseev. 2024. SOMONITOR: Explainable marketing data process-
ing and analysis with large language models.arXiv e-prints(2024), arXiv–2407.
[75] Qi Yang, Marlo Ongpin, Sergey Nikolenko, Alfred Huang, and Aleksandr Farseev.
2023. Against opacity: Explainable ai and large language models for effective
digital advertising. InProceedings of the 31st ACM International Conference on
Multimedia. 9299–9305.
[76] Qi Yang, Christos Tzelepis, Sergey Nikolenko, Ioannis Patras, and Aleksandr
Farseev. 2023. " Just To See You Smile": SMILEY, a Voice-Guided GUY GAN. In
Proceedings of the Sixteenth ACM International Conference on Web Search and
Data Mining. 1196–1199.
[77] Yue Zhang, Yafu Li, Leyang Cui, Deng Cai, Lemao Liu, Tingchen Fu, Xinting
Huang, Enbo Zhao, Yu Zhang, Yulong Chen, et al . 2023. Siren’s song in the
AI ocean: a survey on hallucination in large language models.arXiv preprint
arXiv:2309.01219(2023).
