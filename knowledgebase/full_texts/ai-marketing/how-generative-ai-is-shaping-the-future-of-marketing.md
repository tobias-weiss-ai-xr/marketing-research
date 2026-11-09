---
title: How generative AI Is shaping the future of marketing
url: https://doi.org/10.1007/s11747-024-01064-3
category: ai-marketing
subcategory: empirical
date: 2024-12
venue: Journal of the Academy of Marketing Science
authors:
- Dhruv Grewal
- Cinthia B. Satornino
- Thomas H. Davenport
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s11747-024-01064-3.pdf
pages: 21
chars: 107638
fetched_at: '2026-11-08T13:39:55+00:00'
kb_version: 1
---

# How generative AI Is shaping the future of marketing

Vol:.(1234567890)
Journal of the Academy of Marketing Science (2025) 53:702–722
https://doi.org/10.1007/s11747-024-01064-3
ORIGINAL EMPIRICAL RESEARCH
How generative AI Is shaping the future of marketing
Dhruv Grewal1,2,3  · Cinthia B. Satornino4  · Thomas Davenport5,6  · Abhijit Guha7,8
Accepted: 11 October 2024 / Published online: 14 December 2024
© The Author(s) 2024
Abstract
Generative AI (Gen AI) is shaping the future of marketing. In the next decade, Gen AI will influence how marketers interact
and communicate with customers, help create and deliver marketing content (text, images, and video), and inform methods
for researching and developing new products and services. In both service and sales settings, Gen AI will affect customers
directly and significantly. Therefore, marketers, researchers, and public policy makers require a clear understanding of Gen
AI and its potential, as well as its limitations. To assist marketers in thinking through the adoption and implementation of
Gen AI, the current article presents a four-quadrant organizing framework that highlights trade-offs in both the nature of
Gen AI inputs and the extent of human augmentation needed to deliver Gen AI–generated outputs. This framework provides
guidance for the selection and implementation of Gen AI tools, as well as recommendations for further research.
Keywords Generative AI · Artificial intelligence · Human augmentation · Customization
Using deep-learning models (or algorithms), generative AI
(Gen AI) creates new and novel output (e.g., text, image,
video) from existing content. As such, Gen AI has sub-
stantially improved marketing outcomes across multiple
domains. For example, leading companies use Gen AI to
create suitable ad copy (Colburn, 2024): With Gen AI–cre-
ated ad copy, Vanguard was able to increase conversion
rates for its LinkedIn ads by 15%. Similarly, Emirates NBD
bank (based in the UAE) relied on Gen AI to create per -
sonalized credit card offers that increased leads by 177%.
Unilever also leveraged Gen AI in developing an applica-
tion that crafts initial responses to customer messages by
analyzing not only the issues that the customers raise, but
also the sentiment underlying their messages. According
to Unilever’s chief information officer, its use of Gen AI
has reduced the amount of time customer agents spend on
responses by approximately 90% (Olavsrud, 2023). Walmart
similarly used Gen AI to create a chatbot to execute market-
ing negotiations with vendors, most of which indicated that
they preferred working with the chatbot, which also deliv -
ered 3% cost savings (Hoek et al., 2022). As these use cases
illustrate, the impact of Gen AI is significant; it is estimated
to exceed $1.3 trillion by 2032 due to its potential to disrupt
and change multiple businesses (Bloomberg, 2023).
Herein, we aim to: (1) distinguish Generative AI (Gen
AI) from other forms of AI while highlighting its ben-
efits, (2) identify key considerations for practitioners when The authors appreciate the helpful feedback of the editor John Hulland and the three reviewers.
John Hulland served as editor for this article.
 * Dhruv Grewal
 dgrewal@babson.edu
 Cinthia B. Satornino
 Cinthia.Satornino@unh.edu
 Thomas Davenport
 tdavenport@babson.edu
 Abhijit Guha
 abhijit.guha@moore.sc.edu
1 Department of Marketing, Babson College, Babson Park,
MA 02457, USA
2 University of Bath, Bath, UK
3 Tecnológico de Monterrey, Monterrey, Mexico
4 Peter T. Paul College of Business and Economics, University
of New Hampshire, Durham, NH, USA
5 Babson Park, MA 02457, USA
6 UVA Darden School of Business, Charlottesville, VA , USA
7 College of Business, Florida Atlantic University, Boca Raton,
FL, USA
8 Present Address: Darla Moore School of Business, University
of South Carolina, Columbia, SC, USA

703Journal of the Academy of Marketing Science (2025) 53:702–722
implementing Gen AI, and (3) explain potential negative con-
sequences of strategic misalignment in the selection of Gen
AI tools. The key contribution is a four-quadrant framework
that helps select Gen AI tools based on input type and the
level of human modification needed. Using this framework,
we provide examples of Gen AI solutions, discuss trade-offs,
offer implementation suggestions, and propose areas for future
research.
The impact of Gen AI is rippling exponentially across
domains and industries, driving the fast-paced evolution of
perspectives and solutions. To capture this dynamic evolu-
tion and construct our framework, we gathered insights from
recent relevant industry reports, interviews with industry
experts, and a targeted review of pertinent literature. We
partnered with researchers who developed a recent Amazon
Web Service industry report (Davenport et al. 2023a), where
they surveyed more than 300 chief data officers (CDOs) with
respect to their Gen AI adoption. We learned that more than
three-quarters of these surveyed CDOs believed that Gen
AI would transform their business environments. Further,
over half also planned to invest more in Gen AI. We further
augment the insights from the survey data and qualitative
interviews by Davenport et al. (2023a) with additional inter-
views with senior executives across functions and industries.
Our discussions reveal that many firms already are having
conversations—both internally and with their customers and
technology providers—about the variety of ways that Gen AI
can help them serve their customers, compete in the market-
place, and improve their bottom lines. Yet the experimenta-
tion that the CDOs describe in the AWS survey mostly takes
place at the individual employee level (50%)—only about
20% of them involve the overall organization. Such findings
suggest a significant need for further scholarly guidance in
this nascent, critical area of evolution in marketing practice
and beyond. Our discussions also reveal some deep uncer -
tainty. First, respondents continue to wrestle with the ques-
tion of how to best to implement Gen AI. Their concerns
include the best way to experiment with Gen AI, trade-offs
between internal and external data, and the need for high
quality data (though this need appears to vary across indus-
tries). Second, the executives consistently express ongoing
concerns related to privacy and transparency, pertaining to
both data input in Gen AI and created in collaboration with
Gen AI. The popular press has echoed these concerns and
suggested the need for human augmentation, to ensure the
appropriateness of Gen AI output. In a recent opinion article
for Fast Company for example, Jeff Puritt, CEO of TELUS
International argues that the key questions include “how
decision-makers can help to ‘get GenAI right’ [and keep]
… humans in the loop …” (Puritt, 2023).
Considering its potential to catalyze novel, unprecedented
marketing capabilities (Harkness et al., 2023), Gen AI adop-
tion is likely to be especially prominent in marketing, media,
and consumer technology sectors—significantly more so than
in legal services, insurance, or data analytics, for example (JP
Morgan, 2024). As such, it seems fitting that members of the
marketing discipline take the lead on research into Gen AI.
Generative AI versus analytical AI
Distinguishing Gen AI from analytical AI
To define Gen AI, we compare it with analytical AI, which
represents a classic, widely available form of AI that has
been employed for decades. In terms of similarities, both
analytical AI (also referred to as predictive AI or discrimi-
native AI) and generative AI rely on statistical machine
learning, a technique for training models on past data and
using the models to make predictions. However, the two
forms of AI have different objectives, employ different
algorithm types, use different types of data, and generate
different types of output.
Analytical AI attempts to analyze past data to predict
future outcomes using structured (usually numerical) data.
Most analytical AI algorithms employ variants of predic-
tive models such as regression analysis, neural networks,
causal forests, etc., and are relatively interpretable and
explainable. For example, using prior data about customer
purchases, analytical AI might infer what product each
customer is likely to buy next or the price that the cus-
tomer is likely to pay for a specific item. Spotify lever -
ages analytical AI to suggest playlists that reflect some
activity (e.g., having dinner) or motivation (e.g., discov -
ery) expressed by users. Banks use analytical AI to clas-
sify customers into those more or less likely to default on
loans. In an influential series of papers, Huang and Rust
(2021) parse analytical AI into mechanical AI, thinking
AI, and feeling AI, contingent on the kind of insights it
generates, and outline the marketing tasks for which each
AI is most suited (Huang & Rust, 2021, Table  1).
In short, analytical AI is what firms leverage to improve
their large-scale operations, across various functions
(Siegel, 2024). Accordingly, AI-driven predictions power
millions of business decisions, including “whom to call,
mail, approve, test, diagnose, warn, investigate, incarcer -
ate, set up on a date or medicate” (Abdullahi, 2024). Such
widespread applications in domains spanning advertising,
marketing, customer service, sales, healthcare, peer-to-
peer marketplaces, and fraud detection (Abdullahi, 2024;
Satornino et al., 2023), together with illustrative use cases
and illustrations presented in prior research (Davenport
et al., 2020; Guha et al., 2021; Shankar, 2018), empha-
size the capacity for substantial value creation. Such prac-
tices also have facilitated reductions in prediction costs
(Agrawal et al., 2019).

704 Journal of the Academy of Marketing Science (2025) 53:702–722
Although Gen AI also uses some type of analytical AI
as its underlying foundation, its predictions are textual in
nature and it generates new content from past content, such
as predictions about future content that are based on data
inputs and existing content (using “attention” techniques,
Vaswani et al., 2017) or training on sequential content data.
The predicted content may be the next word in a sentence,
the next component of an image, the next note in a song, or
the next amino acid in a protein. These types of data are less
structured and numerical in nature (though they typically
get converted to numbers for use in Gen AI models). The
algorithms include attention-oriented techniques, as well
as very large and complex deep learning neural networks.
(Notably, it is difficult or impossible to explain why a par -
ticular Gen AI outcome has been produced in response to
a specific prompt.) In addition, Gen AI can operate across
various domains and generate different forms of output, such
as public relations content, social media posts, programming
code, and unique images (Davenport & Mittal, 2022).
Once a Gen AI model has been trained on and systematically
analyzed significant amounts of unstructured (typically, text or
image) data, it can summarize that input, as well as produce
novel insights based on the analysis (Davenport et al., 2023a, b).
For example, while reviewing competitors’ annual reports, Gen
AI can identify information disclosures that hint at significant
changes in competitors’ corporate strategies. Gen AI output
also pertains to mechanical, thinking, and feeling domains, such
that it can be used for (1) simple, repetitive tasks, as when Ama-
zon uses Gen AI to summarize reviews (Walk-Morris, 2023);
(2) complex tasks, such as acting like a “sparring partner” who
creates responses to solicitations during practice sales calls
(Grewal et al., 2024a); or (3) emotional, communicative tasks,
like creating a painting (Spair, 2024). As such, Gen AI has the
potential to influence every element of the marketing strategy
and every step of the strategic planning process.
The accuracy of both generative and analytical AI is largely
contingent on the quality and quantity of training data, though
the choice of algorithm also can have an impact. Well-trained
analytical AI models can effectively identify a suitable response
(e.g., next best offer) or classify objects (e.g., which loans are
most likely to go delinquent). Generative AI language models
trained on accurate data are more likely to produce accurate and
useful textual outputs. However, many models rely on data from
the internet, which feature a wide range of accuracy levels. Both
Gen AI and analytical AI models also are probabilistic rather
than deterministic. Thus, analytical AI models sometimes make
incorrect predictions about whether a person will repay a loan
or buy a product at a particular price. Similarly, Gen AI models
have a well-known tendency to “hallucinate,” or create inac-
curate output (Vana et al., 2024). As Huang and Rust (2024)
acknowledge, Gen AI is good at recognizing expressed emotions
but may be prone to hallucinating responses. This trait is una-
voidable, given the probabilistic nature of the models. Without
dramatically different Gen AI models, organizations that adopt
generative AI will continue to have to deal with the risk of inac-
curate or inappropriate content predictions.
Table 1 compares analytical AI and Gen AI, across various
marketing-relevant functions. There are clear points of simi-
larity, in that both analytical AI and Gen AI can have impacts
across the full marketing plan, from segmentation, targeting,
and positioning; to selecting the marketing mix; to conduct-
ing marketing research; to sales and customer service (e.g.,
customer care, Huang & Rust, 2024 ); to related functions
(e.g., coding, fraud detection). But we also note some critical
Table 1  Analytical AI versus Gen AI
Analytical AI Generative AI
S-T-P Predict -despite incomplete information- whether
customer might be in target segment
Predict long term customer value
Create first draft of marketing plan
Critique marketing plan
Create suitable positioning statements
4 Ps Predict optimal price
Predict best next-offer
Predict optimal ad space & ad space price
Predict customer mood during calls
Predict best personalized offer
Create advertisements
Create product descriptions
Summarize customer reviews; generate insight
Create social media posts
Marketing Research Predict how long persons take to complete surveys
Perform initial analysis of data
Create synthetic respondents for marketing research
New product ideation
Summarize qualitive interviews
Marketing-relevant functions Predict fraudulent transactions
Predict how likely products is to be returned
Create software code
Improve software code
Sales Predict which leads should be pursued Create sales scripts
Create counter to any sales proposal (“sparring partner”)
Customer service Predict complainer sentiment in real time Create first draft of customer complaint replies
Create post facto summaries/analyses customer com-
plaints to identify recurring problem areas

705Journal of the Academy of Marketing Science (2025) 53:702–722
points of difference. The main purpose of analytical AI is to
offer high-quality predictions, such as anticipating which offer
is most likely to spark a consumer’s interest (e.g., Stitchfix
uses analytical AI to predict which clothing subscribers will
enjoy; Davenport et al., 2020). In contrast, Gen AI creates
new content, such as multiple versions of advertisements for
a particular campaign (AIT News Desk, 2023).
There are two strategic decisions that firms must make when
considering Gen AI solutions: the input into Gen AI: the input
into Gen AI (e.g., on which data set should the Gen AI be
trained or prompted?) and the Gen AI output deployment (e.g.,
should the newly created Gen AI content get shared directly, or
should humans intervene prior to sharing?). First, the level of
input customization is an important consideration. Currently,
the most popular and widely used Gen AI solution, ChatGPT,
uses general large language models (LLM) that span a wide
variety of information as input. Conversely, Bloomberg GPT
uses a custom data set of content that is specific to the finance
sector (Davenport & Alavi, 2023). Between these two extremes
lie firms like Morgan Stanley, which uses an LLM customiza-
tion technique called “retrieval-augmented generation” (RAG)
to tune its LLM with a curated set of internal documents (Dav-
enport & Alavi, 2023). This approach involves augmenting a
general LLM with customized content to tune its LLM with
a curated set of internal documents (Gao et al., 2023). The
documents are typically transformed into numeric form (e.g.,
"embeddings") and stored in a vector database so that they can
be easily searched for relevance to a user prompt. One advan-
tage of this approach is that it allows the LLM to present cita-
tions to specific documents in its responses. The selection of
Gen AI input, along this continuum from general to custom
inputs, represents the first major decision for firms seeking to
implement Gen AI solutions.1
Second, it is also important to consider how much human
(or programmed) augmentation is necessary before deploying
Gen AI output. For example, some firms might deploy Chat-
GPT 4.0 for communications with their employees and affili-
ates and provide the resulting responses with little or no human
augmentation. Other firms instead might prefer Grammarly,
a Gen AI–based writing assistant, for such purposes. Unlike
ChatGPT, Grammarly offers some automated restrictions, such
as intervening to suppress responses to offensive prompts. The
BCG–Zeiss Gen AI solution (BCG, 2024) typically provides
responses to optometry practice managers only, which then can
be forwarded to patients (i.e., customers), after careful review.
The practice manager thus serves as a (human) intermediary
that augments the output by vetting it for accuracy—despite
claims that more than 90% of BCG–Zeiss Gen AI responses
are “patient-ready” (BCG, 2024). Like the customization of the
inputs, the level of human augmentation varies along a contin-
uum, from none to automatic restrictions (e.g., Grammarly), to
human augmentation (e.g. BCG-Zeiss), creating another critical
decision for the firm.
Firm perspectives on analytical and generative AI
Analytical AI has had, and is likely to continue to have, sub-
stantial impacts across enterprise functions (e.g., Davenport &
Mittal, 2023; Davenport et al., 2020; Mahurkar, 2023). Thus
far, it tends to be more accurate and reliable than newly devel-
oped Gen AI applications, as well as more robust to outliers
and noise. It is trained on a company’s own structured numeri-
cal data, so it offers more proprietary benefits to the company
that created it. Although both analytical AI and Gen AI are
somewhat opaque, the models for the former tend to be easier
to interpret (Mahurkar, 2023), such that it is relatively easier
to understand how analytical AI models make predictions—a
critical issue for firms that must justify the AI models they use
for customer segmentation, price setting, or classifying a trans-
action as fraudulent. Further, although Gen AI sparks excite-
ment due to its impressive potential, analytical AI has done
more (thus far) to enhance business performance and efficien-
cies (Siegel, 2024), such that analytical AI continues to be the
primary format being adopted in practice (Mahurkar, 2023).
Notwithstanding the advantages of analytical AI, the
appeal of Gen AI remains compelling for several reasons.
First, unlike analytical AI, (some) Gen AI solutions can
be implemented immediately, irrespective of a company’s
own data structure. Consider the case of a large Asian bank,
which previously had its call center agents manually record
the customer service issues. Now, the bank uses an internally-
developed Gen AI application to transcribe (and if needed,
summarize) the customer service call, and search the bank’s
knowledge base to retrieve information relevant to the cus-
tomer query. Based on data collected, call handling time has
been reduced by nearly 20%, so call center agents can spend
more time interfacing with customers (Lim, 2024).
Second, analytical AI often requires the input data to be for-
matted in a certain way, with some certain level of quality, such
that small and poorly resourced firms might lack the internal
data needed to implement analytical AI models. In contrast,
small and poorly resourced firms can readily take advantage of
Gen AI, such as by assigning ChatGPT to create drafts of social
media posts, check code, or create sales scripts (Guha et al.,
2023). Even if Gen AI can benefit from high-quality proprietary
data too (Davenport & Tiwari, 2024; Earley & Bernhoff, 2020),
in the absence of such data, Gen AI solutions like ChatGPT and
Grammarly still provide means for value creation.
Third, the capabilities of Gen AI continue to advance very
rapidly. As Fig. 1 shows, ChatGPT 4 achieved a significant
1 For this article, we largely refer to LLMs, which are Gen AI models
trained on large data sets with primarily text.
 data (e.g., Bard, ChatGPT), but we also acknowledge that Gen AI
encompasses multimodal data, such as large.
 vision models (LVMs), including Dino or Clip.

706 Journal of the Academy of Marketing Science (2025) 53:702–722
increase in capability compared with ChatGPT 3.5. It can
generate text output that looks like social media posts, along
with photos and images that might appear in advertising
campaigns (Rogers, 2024). The latter capacity is a substan-
tial advance, even though the latest version launched less
than four months after Chat GPT 3.5. Many other Gen AI
models exhibit similar levels of progress in a short time.
Consider an illustrative example to understand these
three relevant benefits (Grewal et al., 2024a). Suppose a
marketing agency is tasked with creating a digital market-
ing campaign for a major beverage producer, establishing a
tie-in with a major sporting event such as the Olympics or
FIFA World Cup. The marketer would expect to select the
appropriate sporting event, determine an appropriate and
coherent marketing message, create images for social media
posts, and create corresponding content that is appropriate
to post on various social media platforms. Performing these
tasks manually would take months of significant effort.
However, if the marketer chose to use Gen AI, this cam-
paign development could be completed in days or weeks.
Specifically, the marketer would first select the appropri-
ate AI tool (e.g., ChatGPT 4.0), then craft a prompt to
solicit sporting events that might fit with the beverage
producer’s brand. After identifying an event of interest,
the marketer can craft another ChatGPT 4.0 prompt that
is likely to create marketing messages that attract the tar -
get audience at the selected event, are consistent with
the brand positioning, and match the scope and platforms
the marketer intends to use for the marketing campaign.
The marketer also might prompt ChatGPT 4.0 to provide
a description of images that might correspond with the
selected messages. With this output, the marketer could
turn to an image generator (e.g., OpenAI’s DALL-E) and
provide it with the image description provided by Chat-
GPT 4.0, leading to the creation of an image that corre-
sponds with the selected marketing messages. Finally, the
marketer can prompt ChatGPT 4.0 to provide customized
messages for different social media platforms.
Following an internal review for accuracy and appropriate-
ness, the marketer can deliver all these items and ideas to the cli-
ent, for relatively minimal monetary and time costs. This exam-
ple illustrates the potential benefits to marketers, which reflect
rapid advances in Gen AI. To specify these benefits in greater
detail, we integrate our survey insights and interviews with sen-
ior managers with the results of a careful literature review.
Understanding generative AI
Insights from practice
In exploratory discussions with senior executives,2 we gath-
ered information about how their firms and their customers
use Gen AI, as well as which factors they consider when
Fig. 1  History of ChatGPT (adapted from Malik, 2023)
2 In addition to the interviews conducted as part of the CDO survey
(Davenport et al. 2023a, 2024), we interviewed 10 other senior execu-
tives, from a mix of small and large organizations that are exploring
and implementing gen AI applications.

707Journal of the Academy of Marketing Science (2025) 53:702–722
implementing Gen AI solutions. In Table  2, we present a
sample of perspectives from these interactions, focusing
on (1) the benefits of Gen AI, (2) how to implement Gen
AI, and (3) concerns about Gen AI. As might be expected,
these senior managers outlined the many benefits of Gen
AI, including revenue impacts, cost reductions, and ease of
deployment. They also noted the need to consider their stra-
tegic choices and concerns carefully. In these discussions,
we identified two key considerations: the choice between
using a general or custom input data set and the degree of
human augmentation to deploy.
Gen AI solution involving a general data set
As a typical Gen AI solution, ChatGPT can offer benefits
in multiple domains. This LLM (GPT-3.5 or GPT-4) is
based on a general data set, which means that it leverages
large quantities of publicly available data that provide a
broad scope of source material for creating novel output.
Therefore, ChatGPT could be used to create novel social
media content and generate unique services or sales scripts
(Sinha et al., 2023) based on a large body of unstructured
information.
In our discussions, the CEO of a technology start-up
highlighted the use of Gen AI by both the marketing and
technology departments. Specifically, the marketing depart-
ment leveraged ChatGPT to craft new social media content,
substantially improving productivity. These substantial time
savings effectively lowered the firm’s costs, while simultane-
ously providing novel content. The benefits are immediately
clear in the CEO’s description of their first attempts at using
ChatGPT, as are the limitations of the output:
“So then what we did was we said… let's try this Chat-
GPT thing…. we did …brainstorming….kind of put it
to ChatGPT and said… ‘Hey, write us a blog’. And it
wrote us a beautiful blog….this is better than what …
external people write….we …[need to] fix the things
that were wrong…”
Regarding the technology and new product development
departments, the CEO shared that they had achieved sub-
stantial savings from using ChatGPT. Due to the broad scope
of information from which the general data set underpinning
ChatGPT can draw, the use of this Gen AI tool substantially
augmented human programming efforts, leading to a reduc-
tion in employee headcount and increased productivity. Spe-
cifically, it reduced staffing needs, because the company only
required two software teams instead of three, which yielded
substantial, quantifiable cost savings:
“we had planned on having three distinct engineering
squads… through ChatGPT, we can get our roadmap
done with one less squad… that [is] huge”
These savings and benefits would be difficult and costly to
achieve if the Gen AI tool required a custom data set. How-
ever, the CEO also identified some trade-offs in the decision
to adopt the general LLM, including privacy concerns. This
informant admitted that the company was unsure if everything
uploaded onto ChatGPT would remain private or be used as
input in responding to others’ prompts. As a safeguard against
privacy breaches, the technology teams uploaded only a sub-
section of code onto ChatGPT, not the firm’s full code library.
Executives asserted that even if recent ChatGPT promise of
privacy, this concern is likely to persist.
Gen AI solution involving a custom data set
In cases where the consequences of inadvertently releasing
sensitive information using a general Gen AI tool such as
ChatGPT are high, custom input may be preferred. In contrast
to the broad scope of general inputs, Gen AI models involving
custom data sets contain information that is (1) firm-specific
(not generally available in the public sphere), (2) constantly
updated, and (3) generally reliable. Although more costly and
difficult to deploy, when the risks and trade-offs of general
data set–based solutions are too great, deploying a Gen AI
solution based on custom inputs may be more appropriate.
As an example of an appropriate use of custom inputs,
during our discussion with a retail technology vendor, they
disclosed that they were creating a Gen AI solution for a
specific retailer designed to provide patrons with the loca-
tion of any product in the store, as well as information about
specific stockkeeping units (SKU). In the case of a stockout,
it would offer information about replacement timetables and
potential substitutes. It also might suggest complementary
items and (down the road) offer price promotions, depending
on customer and other factors. All of these features required
store-specific information, so this Gen AI solution utilized
a custom data set. The vendor further clarified two types of
benefits obtained from using custom LLMs.
First, because the output from the Gen AI solution was
store-specific, it helped mitigate demands on retail work -
ers during peak times. This retailer earned substantial sales
through shopping agents, such as those working for Instac-
art. These Instacart shoppers—under significant time pres-
sure to assemble and deliver products to offsite customers—
often would demand considerable time and assistance from
the store employees during peak shopping times (when retail
store employees should be focused on in-store customers):
“it's incredibly oppressive…. [Instacart shoppers
would] have a list of 20 things, and they would just go
up to a store employee [and ask] where are the canned
onions? Where's this? Where is that?... [we are now]
seeing some efficiencies in offloading those [questions]
to an app…”

708 Journal of the Academy of Marketing Science (2025) 53:702–722
Table 2  Senior executives’ perspectives on developing and implementing Gen AI applications
Profile Benefits of Gen AI Concerns about Gen AI Implementing Gen AI
EVP–Technology and Data, global marketing
services  company1
Prior experience as partner in a major consult-
ing firm
Gen AI enables rapid image creation for new
marketing campaigns
Using LLMs (and LVMs) in ways that do not
infringe on intellectual property
Head of Sales, Edtech startup, with operations
in North America and  Europe2
Using Gen AI substantially improves produc-
tivity, in both education and business
Many are unwilling to use Gen AI, if materi-
als uploaded might (potentially) shared with
others, and/or if content co-created with Gen
AI might (potentially) be shared with others
Including privacy as part of the Gen AI offering
is valued by (many) customers
Chief Data Science Officer, large U.S.  retailer1 Using Gen AI to create product labels Use of Gen AI for product labeling gener-
ates hallucinations; editing them reduces
productivity
Chief Data and Analytics Officer, large Cana-
dian  bank1
Early Gen AI application for customer ser-
vice; won award for best AI in practice
Key concerns about privacy, bias, and intel-
lectual property rights infringement, “mostly
related to privacy and related to bias. And
now that there's so much, especially in the
generative space, we're looking at patent law
and copyrights and ownership.”
Gen AI trained on customers’ questions and
answers
Chief Data Officer, large U.S. telecom  firm1 Gen AI used for a wide variety of purposes
across the company, including coding, data
analysis, and image finding
“Boot camp” training to implement Gen AI
across the organization
Chief Technology Officer, leading provider
of research and ratings to asset management
firms  worldwide1
Gen AI created a financial Q&A system using
the firm’s in-house content
Gen AI capability was created quickly, with a
relatively small budget
CEO of a technology start-up2 Using Gen AI reduced costs (time, headcount)
for marketing (e.g., ad copy) and software
development
Materials uploaded into Gen AI might be
subsequentially shared with others
Advisor, Major retail  chain2 Using Gen AI can increase revenue and
streamline operations by freeing up
resources
Benefits from both a general (e.g., general-
ized information like recipes) and custom,
regularly updated (e.g., where certain items
are located in the store) data sets
Former CMO, large private  university1 Uses Gen AI to create ad copy and email
copy, with both text and images
Beyond hallucinations, intellectual property
rights infringement is a key risk
Gen AI output is reviewed by university
employees; the cost of inappropriate or incor-
rect copy reaching external stakeholders is
very high, “So everything that we do is more
of a co pilot orientation, right? We don't just
let it run.”
Director of Marketing Communications, large
U.S. think  tank2
Gen AI can create initial drafts of emails and
website content (both text and images),
such that it is “good for initial drafts, saves
time….”
Gen AI makes errors and also might use
copyrighted content. Correcting for it is very
concerning and important

709Journal of the Academy of Marketing Science (2025) 53:702–722
Table 2  (continued)
Profile Benefits of Gen AI Concerns about Gen AI Implementing Gen AI
Chief Analytics Officer, global CPG
 company1/a
Uses Gen AI to collect consumer insights;
mass personalization at scale (for ads); new
product testing; and understanding consumer
sentiment: “We are using generative AI for
synthesizing consumer and shopper insights
and other marketing use cases. We’re talking
with our marketing agencies about mass
personalization at scale of ads or offers. And
the other area is innovation. So new product
development, perhaps some automated
consumer insights, and then automated con-
sumer testing with digital twins. We want
to use it to understand consumer sentiment
and what they’re asking for. So those are the
enterprise ‘big bets’….”
Chief Analytics Officer, global media
 company1/a
Exploring Gen AI and associated use cases:
“We’re all very interested in generative AI.
Clients and employees are experimenting
within the guardrails that have been placed
on them. And I expect that it will gather
steam slowly and there’ll eventually be some
kind of tipping point. We’ll suddenly real-
ize, wow, this thing has had a tremendous
impact.”
Find ways to experiment with Gen AI, yet
retain guardrails
Chief Data Officer, global financial services
 company1/a
Creating clear, additional guidelines for Gen
AI usage, for which purpose it engaged law-
yers, data professionals, and human resource
professionals
Questions about extent of use of proprietary
data
Managing Director with responsibility for AI,
global  bank1/a
Not all Gen AI is “transparent” (both input
data and algorithms)
Important to know which data the Gen AI uses;
high quality (accurate, up-to-date) data are
critical
1 Large firm. 2Small firm. aInterviews conducted for the CDO survey

710 Journal of the Academy of Marketing Science (2025) 53:702–722
By providing customized output (derived from informa-
tion that is not publicly available) via the Gen AI solution
to the Instacart shoppers, the retailer aimed to reduce the
demands on retail store employees’ time, with the hope it
would translate into labor reductions and cost savings. These
benefits could not be realized without the use of store-spe-
cific (e.g., product locations, prices) information that is both
fresh (e.g., promotions) and reliable (e.g., stockouts).
Second, the Gen AI solution promised increased revenues.
The retail store conducted a pilot field test and compared
sales before versus after implementing the Gen AI solution.
The test identified a substantial sales lift when the retailer
implemented the Gen AI, specifically in “hard-to-shop” cat-
egories. Although field tests like these are subject to limita-
tions, this initial, positive result was encouraging, and again,
would not be possible without the use of in-store data that
were updated regularly and reliable. This much more tech-
nically complex implementation, compared with using a
general, publicly available data set, demands training and
prompting the Gen AI model with firm-specific information,
as well as integration with existing technology architectures
and systems, including inventory management and pricing
optimization systems. Many companies may find such efforts
difficult or impossible to implement without considerable
external assistance from vendors or consultants.
Human augmentation
Beyond the choice of general or custom input data sets,
the preceding examples (i.e., technology start-up firm and
retail technology vendor) illuminate another consideration:
the extent of the need for human augmentation. Under -
standing how humans (human intelligence) and AI should
collaborate is a critical topic, as highlighted by both Huang
and Rust (2021) and Davenport et al. (2020). For our pur -
poses, human augmentation refers to modifications of Gen
AI output by a human actor, serving as a go-between the
Gen AI solution and the end user. 3 For example, a senior
manager in the digital marketing/SEO division of a national
law firm explained that when developing social media con -
tent, ChatGPT can provide output to the firm’s marketing
department, which reviews that content for appropriateness
and impact and edits it as needed, before disseminating the
output. In this case, the Gen AI (ChatGPT) solution is aug-
mented by the human efforts  of the marketing personnel.
In contrast, the vendor of the aforementioned retail Gen AI
solution explicitly built its offering to replace human effort
and communicate directly with retail customers, without
any human augmentation; the Gen AI output is delivered
directly to end users (i.e., Instacart shoppers).
Due to the need for accuracy, many organizations require
some human augmentation between the Gen AI solution and
the final user. For example, a vice president at a Fortune 500
company described to us how the firm’s sales teams employ
a Gen AI solution to generate first drafts of sales proposals.
Before sending the proposals to clients, however, the sales
teams review drafts and customize the content to the specific
client’s needs, leveraging their nuanced understanding of
each client’s needs and objectives. The benefit of employing
a Gen AI solution in this manner, according to this inform-
ant, is the efficiency of editing a baseline proposal, rather
than starting from a blank page. It reduces both the financial
cost and the time needed to produce a sales proposal. How-
ever, a key part of this process is a human review, which
reduces the chance of unsuitable content and subsequent
loss of sales, though it is slower than direct delivery of the
content to users would be.
Another senior manager underscored the importance
of human augmentation. This manager worked for a tech
company that sells a Gen AI solution for proofreading and
copyediting services, as well as an array of value-added ser-
vices (e.g., document retrieval, brainstorming, structured learn-
ing solutions, writing in certain ways or using a certain tone
to cater to specific audiences). As its key benefits, this Gen AI
solution can improve writing quality and increase efficiency
by reducing the time needed for writing, document retrieval,
and brainstorming. It also promises strong privacy protec-
tion; any materials it helps create and all materials uploaded
to the Gen AI remain wholly the property of the customer and
will not be used or saved by the Gen AI solution provider. In
addition, the Gen AI solution screens prompts and queries for
“offensive content,” to be reviewed later by an employee. This
human augmentation, even if delayed, has strong appeal for
educational institutions. Such screening might also help limit
legal liabilities, were an individual user to employ the solution
nefariously, such as to plan and execute an illegal act.
The key point emerging from this discussion is that firms
implementing Gen AI solutions need to be concerned about
the extent of human augmentation between Gen AI and the
end customer. They should explicitly and carefully consider
if the Gen AI output should go directly to an outside-the-
firm customer or if there should be some form of (prior)
human augmentation (e.g., employee overviews the Gen AI
output) before that output gets disseminated to customers.
Insights from academia
Turning our attention to extant academic literature, we gather
insights from scholars immersed in the theoretical and empir-
ical exploration of Gen AI, who have considered its likely
impacts on practice and scholarship. Despite the relative
3 Augmentation is not limited to Gen AI; Davenport et  al. (2020)
cite Stitch Fix, which augments data produced by analytical AI with
human employees’ efforts.

711Journal of the Academy of Marketing Science (2025) 53:702–722
dearth of research on Gen AI in marketing literature, we can
draw from related scholarly domains to extract insights that
may be of use in the marketing domain. Prior literature reso-
nates with the experiences of the practitioners we interviewed
regarding the benefits of Gen AI, such as speed (i.e., increased
efficiency), the ability to contribute to marketing tasks like
marketing research (e.g., by creating synthetic data), and
enhanced ideation (e.g., new products). Table 3 provides an
overview of extant literature, with a summary of key insights.
Although the benefits related to efficiency are well sup-
ported by extant literature, the results regarding effectiveness
are mixed. Many employees can be more effective using Gen
AI, but the use of Gen AI also carries risks. For example,
Gen AI can hallucinate (provide inaccurate or fabricated
information; Cacicio & Riggs, 2023), which reduces its
effectiveness. As such, some scholars recommend human
augmentation, due to its capacity to increase both the job
satisfaction of content producers and the effectiveness of
Gen AI outputs (e.g., Zhang & Gosline, 2023). However,
reviews require human time and attention, so such effort
reduces the productivity benefits of Gen AI solutions.
Beyond Gen AI’s propensity to hallucinate, scholars have
highlighted other explicit concerns. First, the algorithms
are opaque and difficult to explain, which can be a serious
issue in cases where Gen AI produces unexpected or
inappropriate output (Williams, 2024), for which the
marketer may be held accountable. Second, its output can
be biased (Piers, 2024), an issue that largely depends on the
input training data in the model. For example, Grewal et al.,
(2024b) report instances of ChatGPT exhibiting a progressive
bias. Third, privacy-related concerns are prevalent, though
they are less common with customized versions of these
models within companies. Fourth, we note concerns about
ethics, including Gen AI using data that might have copyright
protection (some of these considerations are being adjudicated
in the courts, at the time of writing). Fifth, our review
underscores the importance of regulatory, human, and process
human augmentation to mitigate various risks.
Perhaps the most important insight we gleaned from this
literature review is that there is currently little marketing-
specific, empirically supported guidance for practitioners.
We might carefully draw inferences from a broad multidisci-
plinary lens, but we also note a glaring lack of research into
Gen AI as it pertains to the specific application concerns of
marketers. Such a gap might not be surprising, consider -
ing how relatively new Gen AI technology is to the field at
large. Yet marketing practitioners already are grappling with
the nuances and trade-offs of deploying Gen AI solutions,
emphasizing the dire need for rigorous scholarship. As is
true of any novel, fast-developing field, we expect a plethora
of papers to enter the review process soon, but the impact
of Gen AI on the practice of marketing makes it critically
important to focus scholarly attention in this space.
Developing a Gen AI organizing framework
To that end, we present an organizing framework, extrapolated
from our review of both scholarly content and interviews with
senior managers, designed to provide guidance for implement-
ing Gen AI solutions, as well as illuminating inherent trade-
offs. Specifically, we present important considerations for firms
that plan to implement Gen AI solutions, organized around
two key issues: the type of Gen AI input and the handling of
Gen AI output. We follow the framework with a discussion of
promising avenues for continued scholarly exploration.
Gen AI inputs
Different Gen AI solutions involve custom versus more gen-
eral inputs (e.g., LLMs, LVMs). A custom Gen AI solution
requires company-specific information, which may be sup-
plemented with general information. For example, retail-
ers might need to link the Gen AI to their own customer
data. Marr (2024) details Walmart’s adoption of a Gen AI
solution that is connected to internal Walmart information,
and thereby, it can help customers order, as well as assist
staffers with information to answer queries. In the discus-
sions with the retail vendor, we also learned that its retailer
customer implemented a Gen AI solution that could link to
both in-store data and company inventory data. Other situ-
ations favoring custom inputs include customer service and
support use cases, those involving access to a company’s
internal knowledge, and those involving detailed content
about a company’s specific products or services.
Custom inputs can be provided in various ways
(Davenport and Alavi (2023). The most common and least
technically challenging is to employ retrieval-augmented
generation (RAG), an approach that does not alter the
training or variable weights of existing public or open-
source generative models but instead revises the prompt-
based instructions for specific models. If organizations
seeking such customization have large volumes of content,
they also need to apply vector databases or content similarity
algorithms to feed the customized content selectively into
the model. Customization using a company’s own content
requires that the content is well-curated and of high quality,
currency, uniqueness, and so forth (Davenport & Tiwari, 2024).
However, in other cases, a general input might be prefer-
able, as our discussions with the representative of a technol-
ogy startup indicated. This firm possessed relatively little
internal data. However, one of its goals was to post general
content social media posts, for which general input may well
be effective. ChatGPT, a general LLM using a general data
set built from public sources, has proven especially success-
ful in creating social media posts (Cook, 2023). Broadly,
if the firm’s goals include creating social media posts, ini-
tial drafts of sales scripts, and advertising drafts, a Gen AI

712 Journal of the Academy of Marketing Science (2025) 53:702–722
solution based on a general that can access both more infor-
mation and diverse information is preferable. Ultimately, the
choice of input is within the firm’s control, and should be
made strategically based on the specific tasks it wants the
Gen AI solution to address.
Beyond these influential considerations, several other
points are noteworthy. Using a custom Gen AI model may
help allay concerns about potential bias, because the firm has
more control over the input information. To the extent bias
is driven by the data in the Gen AI model, uses of a custom
model might mitigate such bias, because it can be created
Table 3  Overview of extant Gen AI literature
Author (Year) Insights for Marketing Practice
Benefits
  Brand, Israeli, and Ngwe
(2023)
LLMs (ChatGPT 3.5) provide survey responses consistent with expectations from economic theory, highlight-
ing potential uses for understanding consumer preferences
  Capraro et al. (2024) Gen AI–enabled sentiment analysis is accurate, relative to economic outcomes. Sentiment analysis is currently
implemented by marketing practitioners to help respond to customers messages
  Carlson et al. (2023) Gen AI can be used to develop insightful and engaging syntheses of product reviews, with the potential to
benefit retailers and consumers
  Ghaffarzadegan et al. (2023) Uses of Gen AI to build useful diffusion models that include realistic human reasoning and decision-making.
Does not consider issues of bias in training sets or diffusion models. This benefit is important to social media
marketers and other marketing practitioners that depend on viral content or word-of-mouth dynamics
  Goli and Singh (2024) LLMs can help marketing researchers understand preference heterogeneity. However, the preferences gener-
ated need to be carefully explored, because they can be misleading
  Hirn et al. (2022) Gen AI can facilitate pattern identification in complex, multidimensional data, effectively and efficiently,
which can be useful for firms that are analyzing complex and multidimensional customer profiles that
include, for example, buying patterns
  Hubert et al. (2024) Benefits of Gen AI in tasks that require divergent thinking, for which Gen AI outperforms humans and contin-
ues to improve, scoring in the top 1% of responses, which is valuable for marketers working on new product
development or marketing research
  Jackson et al. (2024) Benefits include enhanced "efficiency, accuracy, resilience, and overall effectiveness," which are important
considerations for supply chain practitioners
  Jo et al. (2024) Gen AI can preserve local identity through visualization in early design communications phases, manifested as
financial and temporal efficiency, which has implications for new product development
  Li et al. (2024) The generation of synthetic data can be used for market research, to save costs and time
  Yoshioka (2024) Using synthetic data to develop a more accurate valuation for previously undervalued intangible assets show-
cases the benefits of Gen AI in financial analysis, a significant concern for marketing research practitioners
too
Concerns/Risks
  Herbosch (2024) Chatbots provide incorrect information, with legal implications, which are relevant to firms that use chatbots to
help with sales or service processes
  Levantino (2023) Explores the role of civil society in regulating Gen AI and threats to fundamental rights and society, with
implications for marketing and public policy
  Markowitz (2024) Gen AI’s limitations for text analysis, including important implications for marketers who use sentiment analy-
sis tools, for example
  Monteith et al. (2024) Issues of misinformation and ethics of using Gen AI in content generation, which pertain to marketers
involved in content creation and deployment
  Samuelson (2023) Issues with intellectual property rights and the impacts of regulation, along with the possible risk of legal
exposure for firms that deploy general LLMs
Implementation of Gen AI
  Andrieux et al. (2024) Trade-offs in implementing Gen AI, including when to mitigate harm via human augmentation
  Brüns and Meißner (2024) Human augmentation in content creation is needed to mitigate negative attitudinal and behavioral reactions in
followers
  Kang, Kim, and Kim (2024) Documents the creation of a custom LLM with human augmentation at the input phase
  Langevin et al. (2023) Proposes empirical design that can test both custom and general LLMs
  Rossi et al. (2024) Benefits of collaboration (human augmentation) with Gen AI, use of synthetic data, and corresponding ethical
considerations, with use case and examples of general LLMs
  Sleiman (2023) Explicates the importance of selecting the right LLM and attention to regulatory concerns

713Journal of the Academy of Marketing Science (2025) 53:702–722
explicitly to limit bias. To the extent that ethical or legal
concerns surround the data the model uses (e.g., appropriate
copyright permission to use the information, such as rights
to the input images or videos), adopting a custom model that
has been created suitably and carefully, using only internal
or free-to-use data, might reduce ethical concerns.
P1 The a) higher the need for a wide range of information
and/or b) the lower the need for firm-specific information
to generate the desired output, the more appropriate the
use of Gen AI tools that use generalized input.
P2 The a) lower the risk from errors from inaccurate
information, and/or b) lower the risk from privacy
concerns, the more appropriate the use of Gen AI tools
that use generalized input.
P3 The higher the a) need for proprietary or firm-specific
information, b) risk of error from inaccurate information,
and/or c) privacy concerns, the more appropriate the use
of Gen AI tools that use customized input.
Level of human augmentation for Gen AI outputs
Some Gen AI solutions require limited or no human aug-
mentation, such as Amazon’s use of Gen AI to summarize
customer reviews (Walk-Morris, 2023) or providing infor -
mation about the location of a certain SKU in a retail store
(Table 2). Because Gen AI tends to perform better in terms
of speed than accuracy (Eastwood, 2023), a lack of human
augmentation is most appropriate when the cost of any error
is relatively low, allowing the firm to leverage the benefits
of Gen AI, like speed and cost savings. But if the costs of a
potential mistake are high (Eastwood, 2023), firms need to
impose relatively more human augmentation. For example,
the risks associated with an inartful or offensive social media
post are fairly substantial. Therefore, an employee likely
needs to review the generated content before it is posted on
social media.
We propose that two factors should inform decisions
about the amount of human augmentation: (1) the task type,
which dictates the inherent risk involved, and (2) strate-
gic firm considerations of the value proposition. Regard-
ing the latter, a firm may opt for human augmentation even
if risk is somewhat low. For example, both ChatGPT and
Grammarly can respond to prompts related to ideation, but
whereas ChatGPT requires no human augmentation (i.e.,
the output goes directly to the customer), Grammarly builds
in human augmentation, suppressing responses to prompts
that it deems “offensive,” which then get reviewed by Gram-
marly, thus building “safety” (e.g., suppression of offensive
prompts) into its value proposition, which is greatly valued
by some customer segments (e.g., educational institutions).
Independent of the risk, greater human augmentation
can provide additional benefits. Although Gen AI increases
efficiency, the effectiveness of its output remains in ques-
tion (Zhou & Lee, 2024). A recent test, comparing ads cre-
ated by Gen AI with ads created by a human creative team,
reflects this dichotomy (Erdem & Sidlova, 2023). The Gen
AI ads prompted three times higher click-through rates, but
the human-created ads generated 9.5 times as many leads
(AIT News Desk, 2023). Baker (2024) adds to this discus-
sion, arguing that effectiveness represents the next frontier
for Gen AI. For firms that implement Gen AI solutions for
marketing tasks, stronger human augmentation efforts might
enhance effectiveness, especially if the Gen AI output alone
does not appear very effective.
Some companies may decide to leave the level of human
augmentation—review and editing in particular—up to
human end-users. But such an approach may be problematic,
considering evidence that employees who have the agency
to decide whether to review and edit Gen AI–generated con-
tent do not always make wise decisions. For example, in an
experiment involving writing with Gen AI, Noy and Zhang
(2023) find that among participants who had access to Gen
AI to help with their writing, 68% submitted the model’s
initial output without editing it. Yet these researchers also
find no correlation between the extent of human editing
and the quality-related grade the participants received from
evaluators.
P4 A) The lower the risks associated with Gen AI output
containing errors and/or b) the weaker the linkage
between the firm’s value proposition and mitigating
output errors, the more appropriate the use of Gen AI
tools with lower human augmentation.
P5 A) The higher the risks associated with Gen AI output
containing errors and/or b) the stronger the linkage
between the firm’s value proposition and mitigating
output errors, the more appropriate the use of Gen AI
tools with higher human augmentation.
Proposed implementation framework
Combining our findings from discussions in the field and
the review of the extant literature, we extrapolate several
key points. First, Gen AI solutions can be classified accord-
ing to two dimensions: the nature of the input (general vs.
custom) and the level of human augmentation (low vs. high).
Second, there are trade-offs inherent to making strategic
choices across these dimensions. To capture these insights
succinctly, we propose a Gen AI implementation framework
for firms (Fig. 2). The first dimension, on the horizontal axis,
reflects the level of customization of the input for Gen AI
solutions, ranging from relatively low (i.e., general LLMs) to

714 Journal of the Academy of Marketing Science (2025) 53:702–722
relatively high customization (i.e., custom LLMs). The sec-
ond (vertical) axis relates to the extent of human augmenta-
tion before delivering the Gen AI output to the user, ranging
from relatively low (i.e., nearly autonomous) to relatively
high human augmentation.
The axes delineate four distinct quadrants, which are
illustrated in Fig.  2. Quadrant 1 (Q1, fastest, less control,
more risk) with general input and low human augmenta-
tion (e.g., summarizing customer reviews); Quadrant 2
(Q2, slower, more control, some risk), with general input
and high human augmentation (e.g., Gen AI creates social
media posts that are reviewed by a human employee); Quad-
rant 3 (Q3, faster, less control, some risk) utilizing custom
input and lower human augmentation (e.g., Gen AI solution
providing information about SKU locations); and Quadrant
4 (Q4, slowest, most control, least risk), offering custom
input and high human augmentation (e.g., Bloomberg GPT
creating an initial draft of a Securities and Exchange Com-
mission (SEC) filing that is reviewed prior to submission).
Importantly, although our discussions imply dichoto-
mous anchors, we recognize that most Gen AI solutions
are positioned along these continua (Davenport & Alavi,
2023). For LLM input types, the two extremes are repre-
sented by ChatGPT (general) and Bloomberg GPT (cus-
tom), but multiple hybrid LLMs appear between them,
such as Morgan Stanley’s Gen AI solution—a general
LLM that gets trained by RAG-based prompt-tuning, to
improve the accuracy and relevance of the information it
uses. Similarly, the two human augmentation extremes
are represented by using ChatGPT for editing and using
ChatGPT to create social media posts. In the former case,
no human augmentation takes place; the material goes
into ChatGPT and comes back edited. In contrast, there is
much human augmentation in the latter case, such that a
human employee carefully reviews the draft social media
post prior to posting. Somewhere in between is Grammarly,
which will flag an offensive ideation prompt, pending sub-
sequent resolution by a human employee. Even if Gram-
marly responds to most ideation prompts with output pro-
vided directly to the customer, in some cases, the prompts
may be suppressed and require human augmentation.
Trade‑offs and selection heuristics for practitioners
The framework (Fig.  2) illustrates trade-offs in each
quadrant.
Quadrant 1  With Q1 tools, the Gen AI relies on general
inputs for training and requires little human augmentation.
Therefore, such applications are fast and relatively inex-
pensive, but they are less likely to be perfectly appropriate
or accurate. These solutions raise privacy and regulatory
risks, associated with the use of general inputs. Therefore,
Q1 tools are ideally suited for tasks with limited risk of dam-
age or liability due to incorrect or inappropriate action and
little need for firm-specific data. If a firm uses ChatGPT to
summarize recent customer reviews for an internal employee
audience, any inaccuracies are unlikely to lead to substantial
brand damage, so low human augmentation seems appro-
priate. In addition, ChatGPT possesses capabilities to sum-
marize reviews fairly well, so its effectiveness should be
reasonably high and sufficient.
Fig. 2  Proposed generative AI selection framework

715Journal of the Academy of Marketing Science (2025) 53:702–722
Quadrant 2 Like Q1, Q2 tools utilize generalized input, but
unlike Q1, Q2 the output is coupled with more human aug-
mentation prior to delivery. Output is delivered more slowly
due to the inherent delay of adding human augmentation, but
risk of inaccuracies and errors is mitigated. However, privacy
concerns remain. Q2 tools are also more costly than Q1 tools
due to the expense of human augmentation, but they remain
less costly than solutions requiring a custom input (Q3 and
Q4) and more likely than Q1 to be appropriate and accurate.
Managers should select solutions in this quadrant when the risk
related to an incorrect action is relatively higher, and the need
for firm-specific information is lower. For example, consider-
ing the potential for substantial brand damage stemming from
an inartful or incorrect social media post, high human aug-
mentation is essential for generating social media content, but
firm-specific data are not necessarily required to draft a sam-
ple social media post. Although human augmentation might
increase the costs (time and money) or reduce response speed
for Q2 tools, firms might choose to incur these costs, to ensure
accuracy and appropriateness (i.e., greater effectiveness).
Quadrant 3 Q3 tools utilize customized input and low human
augmentation. Output is delivered quickly, and privacy con-
cerns are mitigated. However, risk of inaccuracy in the output
remains. For Q3 tools, the specialized nature of the demand
motivates the need for custom inputs. The solutions in this
quadrant are best suited for tasks featuring a low risk related
to incorrect actions but a strong need for firm-specific infor-
mation. For example, a retail store might implement a Gen
AI solution to provide SKU locations to its customer, which
demands a custom, continuously updated data set depicting
those locations. The risk of providing incorrect information is
somewhat low though; customers might express a little frus-
tration if they receive incorrect information, but it is unlikely
to create significant brand damage. Therefore, no human aug-
mentation is required, and by using a Q3 Gen AI solution, the
retail store can gain speed and efficiency.
Quadrant 4 Finally, Q4 tools utilize customized input and high
human augmentation. Output is delivered slowly, but privacy
concerns and risks of inaccuracy in the output are mitigated.
Q4 tools offer significant but expensive protection against risk.
They offer reduced privacy and regulatory risks, due to their
use of custom input, along with enhanced accuracy, due to
their reliance on human augmentation. These solutions are
best suited for tasks for which the risks related to incorrect
action and inaccuracies are very substantial, and the need for
firm-specific information is significant. For example, a firm
might use Bloomberg GPT to generate its SEC filing docu-
ments. The specialized nature of the required information sug-
gests the need for a custom LLM, and Bloomberg GPT was
trained “from scratch” on a large volume of financially ori-
ented content. Other benefits include the (relatively) accurate
information and (relatively) reduced levels of bias or objec-
tionable outputs. Noting the potential for substantial financial
damage stemming from an incorrect SEC filing, high human
augmentation is essential; such human augmentation can
increase the effectiveness of the SEC filing too (e.g., in the
Management Discussion and Analysis section). The temporal
and monetary costs required might be high, but firms choose to
incur them to avoid the significant risks associated with inac-
curate, biased, or hallucinated output for this task.
Such trade-offs imply that firms must make suitable,
careful design choices when they create or deploy Gen AI
solutions. Human augmentation of Gen AI output is costly
in both time and money but can improve the accuracy and
effectiveness of the output. Depending on the intended goal
for implementing Gen AI, it might be useful to incur the
(sometimes substantial) cost of creating custom inputs (ver-
sus general inputs). In other cases, there are clear benefits of
using general inputs, but doing so might increase the need
for costly human augmentation to improve the accuracy and
appropriateness of the final deliverable.
Limitations of Gen AI
As Gen AI continues to evolve and proliferate, it has sig-
nificant potential for positive impact. But it also raises con-
cerns that merit examination. For example, Gen AI solutions
grapple with potential infringement of intellectual property
rights (IPR). This concern is likely more relevant to Gen AI
solutions using general LLMs, which draw from a wide body
of content. When creating new output in response to user
prompts, Gen AI potentially creates output that may infringe
on IPR (Susarla, 2024; also see Table 2), which represents a
serious concern, especially in creative contexts. As Susarla
(2024) cautions, both individual and corporate users of Gen
AI arguably can be held liable for such infringements. Refer-
ring specifically to DALL-E 3 and Midjourney, Marcus and
Southen (2024) recognize their capacity to copy protected
materials, as well as their failure to offer clear information
about the sources from which they might have copied mate-
rials. If users adopt the output without question, they could
inadvertently infringe on the original creator’s IPR. Thus,
the possibility of IPR infringement creates legal risks for
both the Gen AI and the Gen AI user, above and beyond the
business risk to the content creator. It is difficult to know just
how serious these legal risks are; they are likely to remain
the subject of legal action for many years.
Another concern applies to all types of Gen AI solutions,
namely, the creation of misinformation . Gen AI can be
exploited to create convincing “fake content” such as deep-
fake videos, forged documents, or realistic-looking images.
This capability raises concerns about inappropriate content,
identity theft, and fraud; malicious actors could use such
content for deceptive purposes, especially during elections,

716 Journal of the Academy of Marketing Science (2025) 53:702–722
as demonstrated in recent years (Wirtshafter, 2024). At a
broad level, this ethical concern should intensify consid-
erations of how to decide which uses Gen AI should and
should not support. Note that this issue rises over and above
concerns linked to hallucinations, meaning Gen AI produce
factually incorrect content.
When it comes to privacy concerns, a key concern is that
any output created using Gen AI, or any materials input into
the Gen AI as prompts, might be “appropriated” by the Gen
AI, for use elsewhere. This specific point was raised in our
discussions with senior managers, and it could be especially
serious (and damaging) if the data include sensitive cor -
porate or personally identifiable information. Many large
companies have established agreements with LLM provid-
ers to prevent such content leakage, but executives remain
concerned about this threat.
Turning to issues of bias, Gen AI algorithms might accentu-
ate biases inherent in the data (Nicolletti & Bass, 2023). This
concern is particularly relevant to Gen AI solutions using gen-
eral LLMs, which typically include non-curated content from
the internet. Such considerations imply a vicious cycle: As
digital content increasingly gets generated by AI, the foun-
dational biases spread, perpetuating and reinforcing harmful
stereotypes (Nicolletti & Bass, 2023). The expanding reliance
on and reach of Gen AI, in various marketing applications and
daily life, grants this concern even greater significance.
Finally, there are concerns related to opacity (Yu &
Guo, 2023). It is difficult or even impossible to explain the
algorithms underlying Gen AI, which can be an issue in cer-
tain industries, particularly those that are substantially regu-
lated. Furthermore, it may prove difficult to address other
critical issues (e.g., privacy, IPR, bias) if the mechanisms
that allow for such ethical transgressions are unclear, inex-
plicable, or inaccessible. In turn, firms could be vulnerable
to liability, without a means to correct the underlying issues.
Research opportunities
Gen AI and its applications remain in their infancy, suggest-
ing a plethora of opportunities for continued research. As we
indicated previously, the marketing discipline should take
the lead in research into Gen AI (JP Morgan, 2024), and we
outline three distinct categories of research topics for such
exploration, as summarized in Table 4, related to (1) Gen AI
input, (2) Gen AI output and deployment, and (3) regulatory
and societal issues.
Research topics related to Gen AI input
Researchers should define precise parameters for deter -
mining the need for custom inputs, such as Bloomberg
GPT’s Gen AI solution (Davenport & Alavi, 2023), versus
easier-to-create RAG models using prompt-tuning. Popular
wisdom holds that custom inputs offer performance ben -
efits; the Bloomberg GPT model outperforms existing open
models of a similar size on financial tasks by large margins,
while still performing on par or better on general natural
language processing benchmarks (Bloomberg, 2023). Yet
Li et al. (2023) suggest that ChatGPT 4.0 (a general LLM)
can hold its own against, if not achieve better performance
than, BloombergGPT. Therefore, we do not yet understand
the boundary conditions that determine whether investing
in a custom LLM will reap the returns needed to justify
the expense or what type of customization is most effec-
tive in specific circumstances. Such boundary conditions are
complex and ever-changing, so they also need to be tested
formally, and then retested, to establish the actual benefits of
using a custom LLM. Considering the potential for multiple
objective goals (e.g., accuracy, speed, cost), the boundary
conditions that affect the choice between a custom versus
general input (whether for LLMs or multimodal and LVMs)
may have differential impacts.
Researchers also might explore lower-cost alternatives
for creating custom inputs. Davenport and Alavi (2023) sug-
gest fine-tuning the training of an existing LLM with specific
domain content; Google implemented this approach when
building a medicine-focused LLM. Alternatively, as we noted
previously, prompt-tuning modifies a general LLM using a set
of suitable contents, as demonstrated by Morgan Stanley (Dav-
enport & Alavi, 2023). The cost of creating and updating a cus-
tom LLM is non-trivial, and the effort itself is difficult (Shah,
2023), so finding lower-cost, viable alternatives is pertinent,
especially considering the benefits of using custom inputs.
Some Gen AIs establish value propositions associated
with assuaging privacy concerns. For example, Grammarly’s
Gen AI solution promises that it will not absorb any content
created by its users or data made available in users’ prompts
into its LLM. Several providers make similar promises about
the general LLMs they offer; other Gen AI solutions do not
make any such promises. Some firms employ open-source
models (e.g., Llama) in private clouds to address privacy
concerns. Researchers should examine how Gen AI users
balance increased privacy and IPR protection versus, for
example, reduced costs to implement and deploy a Gen AI
solution. We need scholarly attempts to probe the boundary
conditions of when the benefits of privacy and IRP protec-
tions result in adequate returns on the investments needed
to institute such protections.
Research topics related to Gen AI output
A key issue relates to bias: Gen AI can amplify the biases
present in an LLM. Scholars should explore when and how
to measure, manage, and mitigate bias in outputs. Beyond
managing the LLM, two possible approaches entail altering

717Journal of the Academy of Marketing Science (2025) 53:702–722
the algorithm or applying human augmentation, or some
combination of both. Specifically, firms could manage bias
by including costly human augmentation processes, such as
careful reviews prior to the delivery of any output, when it
seems necessary. But humans also suffer from bias. Scholars
thus might attempt to quantify the interaction between human
mediator bias and LLM bias, while also exploring other, per-
haps less costly, more efficient, and/or more effective ways
to mitigate biased output. Another route to addressing bias
involves improving the underlying Gen AI algorithm. Like
the humans who design them, algorithms are not neutral.
According to recent, international research involving 14
LLMs, “OpenAI’s ChatGPT and GPT-4 were the most left-
wing libertarian, while Meta’s Llama was the most right-
wing authoritarian” (Heikkila, 2023). Such bias creates
risks, especially as Gen AI becomes increasingly involved
in various marketing (and other) tasks. Nor can all the bias
be attributed to raw data, because it also reflects the weights
of and adjustments to the underlying model. Research can
explore bias at each level and examine alternative options for
measuring, managing, and mitigating bias. This discussion
presumes that Gen AI solution providers are seeking to avoid
bias; it may be that some providers have less concern about
bias or even embrace certain types of bias.
Relatedly, scholars should probe the boundaries of ethi-
cal uses to determine if there are some tasks for which Gen
AI should not be used. Such questions are particularly
challenging for practitioners because these refer to both
firm-level priorities and policy-level preferences. Schol-
ars might provide empirical evidence related to how con -
text- and task-specific boundary conditions vary (e.g.,
Wirtschafter,  2024), and the resulting insights could help
guide developments of, for example, counter-AI tools that
can detect Gen AI attempts in certain domains (e.g., detect-
ing deep fake images). If scholars explore these boundary
conditions, they also could establish policy recommenda-
tions for how to craft effective legislation, such as requiring
watermarks on Gen AI images, or other regulations specific
to Gen AI providers. Some technology moguls (e.g., Elon
Musk) and leading AI researchers (e.g., Yoshua Bengio,
Stuart Russell) already have called for a pause in Gen AI
development (Narayan et al., 2023).
A related area for scholarly exploration pertains to risk
(e.g., Haidar, 2023; Vartak, 2023). One of the senior execu-
tives we interviewed, employed by a Fortune 500 company,
indicated both excitement and significant trepidation about
the deployment of various Gen AI solutions. They noted
concern about the opportunity costs of not deploying Gen AI
solutions, along with an equal measure of concern about risk
exposure in deploying these tools (e.g., malicious use). Risk
researchers could help assuage these concerns by outlining
ways for practitioners to measure, mitigate, and report the
risks they assume when deploying a Gen AI solution. Such
efforts will represent a complex and difficult endeavor, but it
Table 4  Research avenues
Topic Important Questions for Research
#1: Gen AI input:
Understanding the inputs (e.g., text,
images, video) into the LLM and
alternative ways to build LLMs (or
LVMs)
• Given some desired Gen AI output, which LLM is optimal: custom LLM, general LLM, or an inte-
grated version? What are some factors that inform such choices? How do these questions extend to
multimodal models or LVMs?
• What are some methods for improving a general LLM, such as prompt-tuning (improving inputs)? Can
a custom LLM be useful outside the specific use case for which it was built?
• What are the costs and return on investments for ensuring better privacy and reduced IPR infringement
in newly developed Gen AI solutions? What factors affect the decision to offer increased privacy and/or
reduced IPR infringement?
#2: Gen AI output and deployment:
Understanding the outputs of the pro-
posed Gen AI solution and the level
of human augmentation needed
• Which biases are associated with different Gen AI solutions (according to their inputs), and how can
they be managed or mitigated?
• To mitigate biases, is it optimal to manage the LLM input, manage the algorithm, or manage the output
through human augmentation?
• Considering ethical and public policy quandaries, which applications should avoid the use of Gen AI?
How can firms and individuals be dissuaded from pursuing such applications (e.g., election-related
deep fakes) or creating unethical Gen AI outputs?
• What options are available to increase transparency and returns on investments in Gen AI solutions?
How should firms think of balancing risk versus returns in their Gen AI investments?
• What insights might be derived from classifying Gen AI, similar to the classification of analytical AI,
into mechanical, thinking, and feeling types? Is another classification more appropriate for Gen AI?
#3: Regulatory and societal issues • Can newly proposed and implemented rules and regulations enhance (or detract from) Gen AI innova-
tion, solutions, and returns?
• How should we measure the trade-offs evoked by rules and regulations involving privacy, IPR, and
other societal concerns, across various Gen AI inputs, outputs, and overall social impacts?
• Will certain Gen AI solutions advance or hinder human social skills? How will such influences change
society?

718 Journal of the Academy of Marketing Science (2025) 53:702–722
remains critically necessary to find a way forward for practi-
tioners and address broader issues, including but not limited
to marketplace freedom and personal space.
In relation to opacity (Yu & Guo,  2023), an interesting
discussion surrounds the benefits of developing less opaque
Gen AI algorithms. This line of research might start with the
themes proposed by Rai (2020), who argues that the benefits
of explainable AI stem from either the domain (i.e., govern-
ment requires the use of explainable algorithms) or customer
desire (i.e., customers are more willing to pay more for or
adopt explainable Gen AI solutions). Researchers might
use these themes to understand when the use of a relatively
opaque Gen AI may lead to complications. Other researchers
might examine ways to create less opaque Gen AI versions.
Most of these concerns involve risks related to Gen AI,
but we also call on scholars to investigate ways to turbo-
charge the returns. For example, might Gen AI create text,
images, video, and audio output that not only systemati-
cally rivals human-created content but also is highly rel -
evant to marketing applications? Although JP Morgan
(2024) acknowledges the benefits of current research into
LLMs and algorithms, it also predicts that Gen AI will move
towards “edge AI”—that is, decentralized computation loads
that expand the benefits to end-users. Carlson et al. (2023)
already have started to explore how deep learning and neu-
ral network–based Gen AI can develop online reviews that
could be useful to consumers and managers alike. Accord-
ingly, we call for research that recommends future moves,
given the potential returns from Gen AI.
Research should also examine the conditions that allow for
the productive deployment of Gen AI models (e.g., Satornino
et al., 2024), to support the generation of economic returns,
rather than just “proof of concept” experiments. Survey
research (Davenport and Tiwari, 2023) suggests that a low
percentage of companies (e.g., 6%) have deployments actu-
ally in place. Most companies are experimenting at individual
or departmental levels, but it is production deployments that
are likely to induce changes in employee skills, business pro-
cesses, strategies, and business models. Researchers could
identify some important, non-technological human augmen-
tations needed to deploy Gen AI projects that support the pur-
suit of productivity benefits and economic value (Brynjolfsson
et al., 2021).
Finally, prior work has classified analytical AI into
mechanical AI, thinking AI and feeling AI (Huang and Rust
2021a, b), which could offer a useful framework for think -
ing about different types of AI and how to deploy them.
As we noted, Gen AI output reflects all three domains and
can be used to conduct mechanical, thinking, and feeling
tasks (Spair, 2024; Walk-Morris, 2023). The question that
remains though is whether this specific classification is use-
ful for Gen AI. With regard to analytical AI, Huang and Rust
(2021) argue that mechanical AI is probably the easiest to
execute, whereas feeling AI is the hardest and thus is likely
be the last domain implemented in practice. Such predictions
also might extend to Gen AI, but it is critical to consider if
and how this classification should be adapted to reflect the
unique aspects of Gen AI. Analytical AI has been deployed
in the field for longer, and our understanding of its advances
and the related technologies have improved over time; we
have less clear insights into the relevant mechanisms for
ensuring the advancement of Gen AI.
Research addressing regulatory, societal, and social
issues associated with Gen AI
Continued research might address three other notable
issues. First, we need a better understanding of the impact
of regulation. A variety of laws related to AI have passed,
and some even make specific references to Gen AI. The in-
process EU AI Act (AIA) not only attempts to define Gen
AI but also contains specific provisions for it (Barani & Van
Dyck, 2023), such as efforts to curtail IPR infringement and
restrict manipulative, deepfake content. Lee, Lucchini, and
Lee (2024) predict that both the General Data Protection
Regulation (GDPR), in effect since 2018, and the AIA,
which entered into force in August 2024, will transform the
Gen AI market. Accordingly, we call for research into the
likely impacts of current and proposed regulations on Gen
AI advancement, proliferation, and innovation.
Second, investigations of the longer-term societal impact
of Gen AI will be helpful. Considering its exponential
growth, Gen AI is likely to continue to advance in the com-
ing years. In so doing, it could threaten various job func-
tions, including white-collar tasks (e.g., marketing research-
ers, analysts, content creators). Its ability to generate content
also might mean that Gen AI applications could serve effec-
tively as virtual companions. In this sense, the cost-related
benefits of highly advanced Gen AI seem obvious, but its
implications for capability and social issues  are less so. If
Gen AI performs various tasks, then human capabilities
linked to such tasks atrophy, with substantial repercussions.
Scholars in human behavior and marketplace dynamics
domains might explore the implications of Gen AI–driven
losses and acquisitions of capabilities, to help prepare prac-
titioners, policy makers, and marketplace participants for
positive progress.
Third, turning to related social issues, if Gen AI–pow -
ered applications can serve as effective substitutes for human
interaction or virtual companions, the seeming deterioration
of social skills and community cohesion in today’s socie-
ties may continue to worsen (Grewal et al., 2024). Scholars
should explore the potential for negative repercussions of
increasing social distance within organizations, communi-
ties, and regions, as implied by the increased use of Gen
AI to address social needs. We also need ideas for how to

719Journal of the Academy of Marketing Science (2025) 53:702–722
assess and mitigate such deterioration of social structures.
More powerful, believable, and capable proxies, driven by
Gen AI, could have notable implications for social atrophy,
and we need research into potential human augmentations to
prevent the complete breakdown of communities.
Conclusion
Generative AI has radically transformed the business land-
scape, with particularly strong impacts on marketing. As
such, marketing scholars must take the lead to make sense of
this rapidly evolving space and provide guidance to manag-
ers eager to capitalize on the spectacular benefits of Gen AI,
particularly in elevating the efficiency and effectiveness of
their marketing function. Such guidance must encompass not
only ideas for how to deploy Gen AI in ways that suitably
enhance value but also suggestions for how to navigate the
risks and complexities associated with Gen AI solutions. By
building on prior work and interviews with senior manag-
ers and Gen AI users, we determine that, when choosing to
deploy Gen AI, key concerns relate to Gen AI inputs (gen-
eral versus custom inputs) and Gen AI outputs (extent of
human augmentation, prior to deployment to the end user).
Contingent on the Gen AI task, its value proposition, the
risks associated with any Gen AI error or miscommunica-
tion, and the costs, firms must make careful, suitable choices
and trade-offs of their Gen AI input and output. To this end,
we propose a framework (Fig. 2) to provides relevant, much
needed guidance.
We also outline various limitations and concerns associ-
ated with Gen AI. Like analytical AI (Davenport et al., 2020),
Gen AI raises concerns related to data privacy, embedded
algorithmic bias, ethics (including whether certain Gen AI
applications should even be considered), and opacity (“black
box” nature of the algorithm). Other concerns are unique to
Gen AI though. First, it is vulnerable to “hallucinations,” in
the sense it provides erroneous output, on a scale very differ-
ent from that possible with analytical AI. Second, Gen AI is
especially amenable to the creation of disinformation, which
has substantial public policy implications. Third, Gen AI out-
put, especially creative forms (text, images), can infringe on
IPR, with consequent risks for Gen AI creators and users.
The Gen AI research agenda that we propose covers
three broad areas (1) Gen AI input, (2) Gen AI output, and
(3) concerns associated with Gen AI. The topics contained
within this research agenda warrant consideration by aca-
demic researchers, firms that create Gen AI applications,
Gen AI users, and policy experts. Gen AI already has
exerted notable impacts on marketing; it will continue to
have substantially more impact in the days and years ahead,
and there is much still to learn. We hope that this agenda
motivates, and structures continued research into Gen AI.
Open Access This article is licensed under a Creative Commons Attri-
bution 4.0 International License, which permits use, sharing, adapta-
tion, distribution and reproduction in any medium or format, as long
as you give appropriate credit to the original author(s) and the source,
provide a link to the Creative Commons licence, and indicate if changes
were made. The images or other third party material in this article are
included in the article’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in
the article’s Creative Commons licence and your intended use is not
permitted by statutory regulation or exceeds the permitted use, you will
need to obtain permission directly from the copyright holder. To view a
copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
References
Abdullahi, A. (2024). Generative AI vs. predictive AI: What’s
the difference? Eweek.com. Retrieved April 5, 2024, from
https:// www. eweek. com/ artif icial- intel ligen ce/ gener ative- ai-
vs- predi ctive- ai/#: ~: text= Gener ative% 20AI% 20sof tware%
20cre ates% 20ima ges,sugge st% 20out comes% 20and% 20fut
ure% 20tre nds
Agrawal, A., Gans, J. S., & Goldfarb, A. (2019). Exploring the impact
of artificial intelligence: Prediction versus judgment. Information
Economics and Policy, 47, 1–6.
AIT News Desk (2023). Borzo presents online ad study AI vs. human
a marketing battleground. Who optimizes more? Retrieved April
5, 2024, from https:// aitho rity. com/ machi ne- learn ing/ borzo- prese
nts- online- ad- study- ai- vs- human-a- marke ting- battl egrou nd- who-
optim izes- more/
Andrieux, P., Johnson, R. D., Sarabadani, J., & Van Slyke, C. (2024).
Ethical considerations of generative AI-enabled human resource
management. Organizational Dynamics, 53(1), 101032.
Baker, J. (2024). Predictions 2024: effectiveness will be the next fron-
tier in the AI battle. The drum. Retrieved April 5, 2024, from
https:// www. thedr um. com/ news/ 2024/ 01/ 31/ predi ctions- 2024-
effec tiven ess- will- be- the- next- front ier- the- ai- battle
Barani, M. & Van Dyck, P. (2023). Generative AI and the EU
AI act – A closer look. Retrieved April 5, 2024, from https://
www. allen overy. com/ en- gb/ global/ blogs/ tech- talk/ gener
ative- ai- and- the- eu- ai- act-a- closer- look
BCG (2024). Using Gen AI to expand understanding of health care
solutions. Retrieved April 5, 2024, from https:// www. bcg. com/
capab iliti es/ artifi  cial- intel ligen ce/ gener ative- ai/ expand- under
stand ing- of- health- care- solut ions
Bloomberg (2023). Generative AI to become a $1.3 Trillion market
by 2032, Research finds. Bloomberg. Retrieved April 5, 2024,
from https:// www. bloom berg. com/ compa ny/ press/ gener ative- ai-
to- become- a-1- 3- trill ion- market- by- 2032- resea rch- finds/
Brand, J., Israeli, A., & Ngwe, D. (2023). Using LLMs for Market
Research. HBS Working Paper, 23–062. Retrieved October 22,
2024. from https:// www. hbs. edu/ ris/ Publi cation% 20Fil es/ 23- 062_
ed720 ebc- ec4d- 4bc3- a6ba- bad8c fbd9d 51. pdf
Brüns, J. D., & Meißner, M. (2024). Do you create your content your-
self? Using generative artificial intelligence for social media con-
tent creation diminishes perceived brand authenticity. Journal of
Retailing and Consumer Services, 79, 103790.
Brynjolfsson, E., Rock, D., & Syverson, C. (2021). The productiv -
ity J-curve: How intangibles complement general purpose tech-
nologies. American Economic Journal: Macroeconomics, 13(1),
333–372.
Cacicio, S., & Riggs, R. (2023). Bridging Resource Gaps in Adult
Education: The Role of Generative AI. Adult Literacy Education,
5(3), 80–86.

720 Journal of the Academy of Marketing Science (2025) 53:702–722
Capraro, V., Di Paolo, R., Perc, M., & Pizziol, V. (2024). Language-
based game theory in the age of artificial intelligence. Journal of
the Royal Society Interface, 21(212), 20230720.
Carlson, K., Kopalle, P. K., Riddell, A., Rockmore, D., & Vana, P.
(2023). Complementing Human Effort in Online Reviews: A Deep
Learning Approach to Automatic Content Generation. Interna-
tional Journal of Research in Marketing, 40(1), 54–74.
Colburn, L. (2024), AI in Marketing: Benefits, Use Cases, and Exam-
ples. Persado, July 6, 2024. Retrieved July 19, 2024, from https://
www. persa do. com/ artic les/ ai- marke ting/
Cook, J. (2023). 5 ChatGPT prompts to supercharge your social media
game. Forbes, October 23. Retrieved April 5, 2024, from https://
www. forbes. com/ sites/ jodie cook/ 2023/ 10/ 23/5- chatg pt- promp
ts- to- super charge- your- social- media- conte nt- game/? sh= 3a29e
b5e75 f3
Davenport, T., Guha, A., Grewal, D., & Bressgott, T. (2020). How
artificial intelligence will change the future of marketing. Journal
of the Academy of Marketing Science, 48(1), 24–42.
Davenport, T. & Alavi, M. (2023). How to train generative AI using
your company’s data. Harvard Business Review. Retrieved April
5, 2024, from https:// hbr. org/ 2023/ 07/ how- to- train- gener ative- ai-
using- your- compa nys- data
Davenport, T. & Mittal, N. (2022). How generative AI is changing
creative work. Harvard Business Review. Retrieved April 5, 2024,
from https:// hbr. org/ 2022/ 11/ how- gener ative- ai- is- chang ing- creat
ive- work
Davenport, T. and Mittal, N. (2023) All in on AI: How smart compa-
nies win big with artificial intelligence. Boston: Harvard Business
Review Press
Davenport, T. & Tiwari, P. (2024). Is your company’s data ready for
generative AI? Harvard Business Review. Retrieved April 5, 2024,
from https:// hbr. org/ 2024/ 03/ is- your- compa nys- data- ready- for-
gener ative- ai
Davenport, T., Bean, R., & Wang, R. (2023a). CDO Agenda 2024: Nav-
igating data and generative AI Frontiers. Amazon Web Service.
Davenport, T., Parra-Moyano, J, Schmedders, K., & Schulte, S. (2023b)
Use gen AI to uncover new insights into your competitors. Har -
vard Business Review. Retrieved April 5, 2024 from https:// hbr.
org/ 2023/ 11/ use- genai- to- uncov er- new- insig hts- into- your- compe
titors
Earley, S. & Bernhoff, J. (2020). Is your data infrastructure ready for
AI? Harvard Business Review. Retrieved April 5, 2024, from
https:// hbr. org/ 2020/ 04/ is- your- data- infra struc ture- ready- for- ai
Eastwood, B. (2023). It’s time for everyone in your company to under-
stand generative AI. Retrieved April 5, 2024, from https:// mitsl
oan. mit. edu/ ideas- made- to- matter/ its- time- every one- your- compa
ny- to- under stand- gener ative- ai
Erdem, E. & Sidlova, V. (2023). The future of generative AI in
advertising: Efficiency without effectiveness? Retrieved April
5, 2024, from https:// www. kantar. com/ inspi ration/ analy tics/
the- future- of- gener ative- ai- in- adver tising- effic iency- witho
ut- effec tiven ess
Gao, Y., Xiong, Y., Jia, K., Pan, J., Bi, Y., Dai, Y., Sun, J., Wang, M.,
& Wang, H. (2023). Retrieval-augmented generation for large
language models: a survey. arXiv: 2312. 10997
Ghaffarzadegan, N., Majumdar, A., Williams, R., & Hosseinichimeh,
N. (2023). Generative agent-based modeling: Unveiling social sys-
tem dynamics through coupling mechanistic models with genera-
tive artificial intelligence. arXiv preprint arXiv: 2309. 11456
Goli, A., & Singh, A. (2024). Can Large Language Models Capture
Human Preferences? Marketing Science, 43(4), 697–708.
Grewal, D., Guha, A., Satornino, C. B., & Becker, M. (2024a). The
future of marketing and marketing education. Journal of Market-
ing Education. Forthcoming.
Grewal, D., Guha, A., & Becker, M. (2024b). The AI is changing
the world: for better or for worse? Journal Macromarketing.
Forthcoming.
Guha, A., Grewal, D., & Atlas, S. (2023). Generative AI and marketing
education: What the future holds. Journal of Marketing Educa -
tion, 46(1), 6–17.
Guha, A., Grewal, D., Kopalle, P. K., Haenlein, M., Schneider, M. J.,
Jung, H., ... & Hawkins, G. (2021). How artificial intelligence will
affect the future of retailing. Journal of Retailing, 97(1), 28–41.
Haidar, B. (2023) Quantifying the risks of generative AI. Retrieved
April 5, 2024 from https:// guide house. com/ insig hts/ advan ced-
solut ions/ 2023/ quant ifying- the- risks- of- gener ative- ai
Harkness, L., Robinson, K., Stein, E., & Wu, W. (2023). How genera-
tive AI can boost consumer marketing. McKinsey & Company.
Retrieved April 5, 2024 from https:// www. mckin sey. com/ capab
iliti es/ growth- marke ting- and- sales/ our- insig hts/ how- gener ative-
ai- can- boost- consu mer- marke ting#/
Heikkila, M. (2023). AI language models are rife with different politi-
cal biases. MIT Technology Review. Retrieved April 5, 2024,
from https:// www. techn ology review. com/ 2023/ 08/ 07/ 10773 24/
ai- langu age- models- are- rife- with- polit ical- biases/
Herbosch, M. (2024). Fraud by generative AI chatbots: On the thin
line between deception and negligence. Computer Law & Security
Review, 52(April), 105941.
Hirn, J., García, J. E., Montesinos-Navarro, A., Sánchez-Martín, R.,
Sanz, V., & Verdú, M. (2022). A deep Generative Artificial Intel-
ligence system to predict species coexistence patterns. Methods
in Ecology and Evolution, 13(5), 1052–1061.
Hoek, R. V., DeWitt, M, Lacity, M., & Johnson, T. (2022). How
Walmart Automated Supplier Negotiations. Harvard Business
Review, https:// hbr. org/ 2022/ 11/ how- walma rt- autom ated- suppl
ier- negot iatio ns
Huang, M. H., & Rust, R. T. (2024). The caring machine: Feeling AI
for customer care. Journal of Marketing, 88(5), 1–23.
Huang, M. H., & Rust, R. T. (2021). A strategic framework for artificial
intelligence in marketing. Journal of the Academy of Marketing
Science, 49(2), 30–50.
Hubert, K. F., Awa, K. N., & Zabelina, D. L. (2024). The current state
of artificial intelligence generative language models is more crea-
tive than humans on divergent thinking tasks. Scientific Reports,
14(1), 3440.
Jackson, I., Ivanov, D., Dolgui, A., & Namdar, J. (2024). Generative
artificial intelligence in supply chain and operations management:
a capability-based framework for analysis and implementation.
International Journal of Production Research, 1–26.
Jo, H., Lee, J. K., Lee, Y. C., & Choo, S. (2024). Generative artificial
intelligence and building design: Early photorealistic render visu-
alization of façades using local identity-trained models. Journal of
Computational Design and Engineering, 11(2), 85–105.
Kang, M., Kim, J., & Kim, S. (2024). Unsupervised generation of fash-
ion editorials using deep generative model. Fashion and Textiles,
11(1), 4.
Langevin, M., Grebner, C., Güssregen, S., Sauer, S., Li, Y., Matter, H.,
& Bianciotto, M. (2023). Impact of applicability domains to gen-
erative artificial intelligence. ACS Omega, 8(25), 23148–23167.
Lee, P., Luccini, L. & Lee, M. (2024). Walking the tightrope: As
generative AI meets EU regulation, pragmatism is likely.
Retrieved April 5, 2024, from https:// www2. deloi tte. com/ xe/
en/ insig hts/ indus try/ techn ology/ techn ology- media- and- telec

721Journal of the Academy of Marketing Science (2025) 53:702–722
om- predi ctions/ 2024/ tmt- predi ctions- eu- gener ative- ai- regul
ation. html
Levantino, F. P. (2023). Generative and AI-powered oracles: “What
will they say about you?” Computer Law & Security Review, 51,
105898.
Li, P., Castelo, N., Katona, Z., & Sarvary, M. (2024). Frontiers: Deter-
mining the Validity of Large Language Models for Automated
Perceptual Analysis. Marketing Science, 43(2), 254–266.
Li, X., Chan, S., Zhu, X., Pei, Y., Ma, Z., Liu, X., & Shah, S. (2023).
Are ChatGPT and GPT-4 general-purpose solvers for financial
text analytics? A study on several typical tasks. In Proceedings of
the 2023 Conference on Empirical Methods in Natural Language
Processing: Industry Track, 408–422. Singapore: Association for
Computational Linguistics.
Lim, R. (2024). DBS launches generative AI virtual assistant for cus-
tomer service workforce, The Business Times, July 18. Retrieved
August 07. 2024, from https:// www. busin essti mes. com. sg/ compa
nies- marke ts/ dbs- launc hes- gener ative- ai- virtu al- assis tant- custo
mer- servi ce- workf orce
Mahurkar, A. (2023). Why discriminative AI will continue to dominate
enterprise AI adoption in a world flooded with discussions on gen-
erative AI. Fast Company. Retrieved April 5, 2024 from https://
www. fastc ompany. com/ 90927 119/ why- discr imina tive- ai- will-
conti nue- to- domin ate- enter prise- ai- adopt ion- in-a- world- flood
ed- with- discu ssions- on- gener ative- ai
Malik, E. (2023). Artificial intelligence (AI) and ChatGPT: history
and timelines. Retrieved April 5, 2024, from https:// www. offic
etime line. com/ blog/ artifi  cial- intel ligen ce- ai- and- chatg pt- histo
ry- and- timel ines
Marcus, G. & Southen, R. (2024). Generative AI has a visual plagia-
rism problem. Retrieved April 5, 2024, from https:// spect rum. ieee.
org/ midjo urney- copyr ight
Markowitz, D. M. (2024). Can generative AI infer thinking style from
language? Evaluating the utility of AI as a psychological text
analysis tool. Behavior Research Methods, 1–12.
Marr, B. (2024). The amazing ways in which Walmart is using gen-
erative AI. Forbes, February 15. Retrieved April 5, 2024, from
https:// www. forbes. com/ sites/ berna rdmarr/ 2024/ 02/ 15/ the- amazi
ng- ways- walma rt- is- using- gener ative- ai/? sh= 2abe0 f9aa2 f9
Monteith, S., Glenn, T., Geddes, J. R., Whybrow, P. C., Achtyes, E., &
Bauer, M. (2024). Artificial intelligence and increasing misinfor-
mation. The British Journal of Psychiatry, 224(2), 33–35.
Morgan JP (2024). Is generative AI a game changer? Retrieved April 5,
2024, from https:// www. jpmor gan. com/ insig hts/ global- resea rch/
artifi  cial- intel ligen ce/ gener ative- ai
Narayan, J., Hu, K., Coulter, M., & Mukherjee, S. (2023) Elon Musk
and others urge AI pause citing “risks to society”. Reuters.
Retrieved April 5, 2024, from https:// www. reute rs. com/ techn
ology/ musk- exper ts- urge- pause- train ing- ai- syste ms- that- can-
outpe rform- gpt-4- 2023- 03- 29/
Nicoletti, L. & Bass, D. (2023). Humans are biased: Generative AI is
even worse. Retrieved April 5, 2024, from https:// www. bloom
berg. com/ graph ics/ 2023- gener ative- ai- bias/? embed ded- check
out= true
Noy, S., & Zhang, W. (2023). Experimental evidence on the produc-
tivity effects of generative artificial intelligence. Science,  381,
187–192. https:// doi. org/ 10. 1126/ scien ce. adh25 86
Olavsrud, T. (2023). Unilever leverages GPT API to deliver business
value. CIO, March 10, 2023, Retrieved July 19, 2024, from https://
www. cio. com/ artic le/ 464190/ unile ver- lever ages- chatg pt- to- deliv
er- busin ess- value. html
Piers, C. (2024). Even ChatGPT Says ChatGPT Is Racially Biased.
Scientific American, https:// www. scien tific ameri can. com/ artic le/
even- chatg pt- says- chatg pt- is- racia lly- biased/
Puritt, J (2023). Generative AI’s success depends on “humanity in the
loop”. Fast Company, June 20, 2023, Retrieved July 19, 2024
from https:// www. fastc ompany. com/ 90909 976/ gener ative- ais-
succe ss- depen ds- on- human ity- in- the- loop
Rai, A. (2020). Explainable AI: From black box to glass box. Journal
of the Academy of Marketing Science, 48, 137–141.
Rogers, C. (2024, May 17). Coca-Cola: The future is “AI meets human
ingenuity.” Marketing Week. https:// www. marke tingw eek. com/
coca- cola- artifi  cial- intel ligen ce/
Rossi, S., Rossi, M., Mukkamala, R. R., Thatcher, J. B., & Dwivedi, Y.
K. (2024). Augmenting research methods with foundation models
and generative AI. International Journal of Information Manage-
ment, 102749.
Samuelson, P. (2023). Generative AI meets copyright. Science,
381(6654), 158–161.
Satornino, C. B., Grewal, D., Guha, A., Schweiger, E. B., & Good-
stein, R. C. (2023). The perks and perils of artificial intelligence
use in lateral exchange markets. Journal of Business Research,
158(March), 113580.
Satornino, C. B., Du, S., & Grewal, D. (2024). Using artificial intel-
ligence to advance sustainable development in industrial markets:
A complex adaptive systems perspective. Industrial Marketing
Management, 116, 145–157.
Shah, S. (2023). Prompt tuning: A powerful technique for adapting
LLMs to new tasks. Retrieved April 5, 2024, from https:// medium.
com/@ shahs hreya nsh20/ prompt- tuning- a- power ful- techn ique- for-
adapt ing- llms- to- new- tasks- 6d6fd 9b835 57#: ~: text= Prompt%
20tun ing% 20is% 20a% 20tec hniqu e,small% 20num ber% 20of%
20pro mpt% 20par amete rs
Shankar, V. (2018). How Artificial Intelligence (AI) is Reshaping
Retailing. Journal of Retailing, 94(4), vi–xi.
Siegel, E. (2024). 3 ways predictive AI delivers more value than gen-
erative AI. Forbes, March 4. Retrieved April 5, 2024, from https://
www. forbes. com/ sites/ erics iegel/ 2024/ 03/ 04/3- ways- predi ctive-
ai- deliv ers- more- value- than- gener ative- ai/ amp/
Sinha, P., Shastri, A., & Lorimer, S. (2023). How generative AI will
change sales. Harvard Business Review. March 31, https:// hbr. org/
2023/ 03/ how- gener ative- ai- will- change- sales
Sleiman, J. P. (2023). Generative artificial intelligence and large lan-
guage models for digital banking: First outlook and perspectives.
Journal of Digital Banking, 8(2), 102–117.
Spair, R. (2024). The future of creativity: How generative AI is revo-
lutionizing art and design. Medium. Retrieved August 3, 2025,
from https:// medium. com/@ ricks pair/ the- future- of- creat ivity-
how- gener ative- ai- is- revol ution izing- art- and- design- art- gener
ative ai- 166ed b1d02 67#: ~: text= One% 20exa mple% 20is% 20the%
20fie ld,and% 20exp erime nt% 20with% 20diff  erent% 20app roach es
Susarla, A. (2024). Generative AI’s “Snoopy problem” makes avoid -
ing copyright infringement a challenge. Fast Company. Retrieved
April 5, 2024, from https:// www. fastc ompany. com/ 91068 738/
gener ative- ai- snoopy- probl em- copyr ight- infri ngeme nt
Vana, Prasad, Praveen K. Kopalle, Pradeep N. Pachigolla, and Keith
Carlson (2024), “Generating “Accurate” Online Reviews: Aug-
menting a Transformer-Based Approach with Structured Predic-
tions,” Unpublished working paper, Tuck School of Business,
Dartmouth College.
Vartak, M. (2023). Six risks of generative AI. Retrieved April 16, 2024,
from https:// www. forbes. com/ sites/ forbe stech counc il/ 2023/ 06/ 29/
six- risks- of- gener ative- ai/? sh= 5b0c6 b5232 06

722 Journal of the Academy of Marketing Science (2025) 53:702–722
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez,
A.N., Kaiser, Ł. & Polosukhin, I. (2017). Attention is all you need.
Advances in Neural Information Processing Systems. In 31st Con-
ference on Neural Information Processing Systems (NIPS 2017).
Walk-Morris, T. (2023). Amazon deploys generative AI to summarize
reviews. RetailDive. Retrieved August 3, 2024, from https:// www.
retai ldive. com/ news/ amazon- gener ative- ai- revie ws/ 69085 2/#: ~:
text= Amazon% 20is% 20usi ng% 20gen erati ve% 20art ifici al,detai
ling% 20inf ormat ion% 20abo ut% 20the% 20item
Williams, S. C. P. (2024). Personalizing ChatGPT can make it more
offensive, researchers find. Princeton . Retrieved April 5, 2024,
from https:// engin eering. princ eton. edu/ news/ 2024/ 01/ 30/ perso
naliz ing- chatg pt- can- make- it- more- offen sive- resea rchers- find#:
~: text= Resea rch% 20by% 20Pri nceton% 20Uni versi ty% 20com puter
,cause% 20som eone% 20to% 20lea ve% 20a
Wirtshafter, V. (2024). The impact of generative AI in a global election
year. Brookings, April 05. Retrieved April 05, 2024 from https://
www. brook ings. edu/ artic les/ the- impact-  of- gener ative- ai- in-a-
global- elect ion- year/
Yoshioka, T. (2024). Valuation of Intangible Fixed Assets Using Gen-
erative Artificial Intelligence and Machine Learning. Journal of
Management Science, 13, 27–36.
Yu, H., & Guo, Y. (2023, June). Generative artificial intelligence
empowers educational reform: Current status, issues, and pros-
pects. In Frontiers in Education (Vol. 8), https:// doi. org/ 10. 3389/
feduc. 2023. 11831 62
Zhang, Yunhao and Gosline, Renee, (2023. Human Favoritism, Not
AI Aversion: People’s Perceptions (and Bias) Toward Generative
AI, Human Experts, and Human-GAI Collaboration in Persuasive
Content Generation (May 20, 2023). Available at SSRN:  https://
ssrn. com/ abstr act= 44539 58
Zhou, E., & Lee, D. (2024). Generative artificial intelligence, human
creativity, and art. PNAS Nexus, 3(3), pgae052. https:// doi. org/ 10.
1093/ pnasn exus/ pgae0 52
Publisher's Note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional affiliations.
