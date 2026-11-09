---
title: 'Tracking Conversations: Measuring Content and Identity Exposure on AI Chatbots'
url: https://arxiv.org/abs/2604.27438
category: digital-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Muhammad Jazlan
- Ethan Wang
- Yash Vekaria
- Zubair Shafiq
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.27438
pages: 10
chars: 50876
fetched_at: '2026-11-08T12:59:31+00:00'
kb_version: 1
---

# Tracking Conversations: Measuring Content and Identity Exposure on AI Chatbots

Tracking Conversations: Measuring Content and
Identity Exposure on AI Chatbots
Muhammad Jazlan
University of California, Davis
mjazlan@ucdavis.edu
Ethan Wang
University of California, Davis
ebwang@ucdavis.edu
Yash Vekaria
University of California, Davis
yvekaria@ucdavis.edu
Zubair Shafiq
University of California, Davis
zubair@ucdavis.edu
Abstract
AI chatbots are becoming a primary interface for seeking
information. As their popularity grows, chatbot providers
are starting to deploy advertising and analytics. Despite this,
tracking on AI chatbots has not been systematically studied.
We present a systematic measurement of web tracking on
20 popular AI chatbots. Under controlled settings using a
sensitive prompt, we capture and compare network traffic
in normal chats and, where supported, private chats. We
search for exposure of two categories of information:con-
tent, including prompts, prompt-derived titles, chat URLs,
and chat identifiers; andidentity, including names, emails,
account identifiers, first-party cookies, and explicit IP/User-
Agent fields in payloads. We find that 17 of 20 chatbots share
information with at least one third party. Three chatbots
share plaintext conversation text, including both prompt and
response snippets, with Microsoft Clarity through session
replay. Fifteen chatbots share conversation URLs or chat
identifiers with third-party advertising, analytics, or social
endpoints. Several chatbots expose user identity through
support widgets, analytics, advertising, and session replay
tags; in some cases, hashed emails are shared.
1 Introduction
AI chatbots have rapidly become a primary interface for seek-
ing information, advice, and assistance. Modern AI chatbots
support open-ended conversations, answer complex queries,
generate content, and adapt responses to individual users
across a wide range of tasks and domains [11, 77]. As users
increasingly turn to AI chatbots for tasks previously handled
by search engines or other services [60], the web interfaces of
these systems have become an important surface for privacy
and safety measurements.
AI chatbot providers have growing incentives to collect
and share information from these interfaces. Advertising is
a key driver: with their growing popularity, AI chatbots are
emerging as an attractive channel for advertisers to reach
high-intent audiences [24]. Chatbot services such as Ope-
nAI’s ChatGPT and Microsoft’s Copilot have recently intro-
duced advertising [37, 48]. Advertising creates incentives to
track user activity for ad targeting (i.e., show relevant ads to
a user) and conversion tracking (i.e., what a user does after
seeing an ad) [74]. Chatbot providers also deploy analytics,
session replay, and experimentation tools to understand and
optimize usage patterns [16, 66].
Tracking on AI chatbots is more consequential than track-
ing on many typical websites for two reasons. First, the
content can be unusually sensitive. Users disclose health
concerns, relationships, finances, and mental state to chat-
bots [31, 56, 67, 76]. A traditional news site reveals what a
user is reading; a chatbot, like a search engine, can reveal
what a user is actively seeking, but often with more conver-
sational detail and personal context. Second, authentication
is common. Many chatbots allow limited use without sign-in,
but reserve functionality such as chat history and file uploads
for logged-in users. This shifts tracking from browser-level
identifiers, such as cookies, fingerprints, and IP addresses,
toward account-level identifiers, such as email addresses and
names, that are directly linked to a person.
Despite these risks, tracking on AI chatbot websites has
not been systematically studied. Prior work has measured
adjacent AI surfaces such as GPT plugins and browser-based
AI assistants [12, 68, 71], but not first-party chatbot websites,
where the provider controls the interface, users are often
authenticated, and conversational state is rendered directly
into page metadata, URLs, and DOM content. This creates
a distinct measurement problem: traditional web tracking
mechanisms now operate on pages whose state may include
prompts, responses, chat identifiers, prompt-derived titles,
and account identity. It remains unclear which third parties
are embedded within these platforms, what information is
shared with them, and whether privacy controls such as
privatechats limit third-party exposure.
To address this gap, we perform a systematic measurement
of web tracking on 20 popular AI chatbots. Under controlled
1
arXiv:2604.27438v2  [cs.CR]  13 May 2026

Jazlan et al.
settings, we capture and compare the network traffic ob-
served using “pregnancy test near me”—a sensitive prompt
that combines health information with an implicit location
request. We analyze exposure under two categories of in-
formation:content, including prompts, prompt-derived ti-
tles, chat URLs, and chat identifiers; andidentity, including
names, emails, first-party cookies, and explicit IP/User-Agent
fields in payloads. For chatbots that support private mode,
we repeat the same experiment in private chats to evaluate
whether these modes reduce third-party tracking.
Our results show that tracking on AI chatbots is wide-
spread and can expose both content and identity informa-
tion. Seventeen of 20 chatbots share information with at least
one third party during a single normal chat session. Three
chatbots share plaintext conversation text, including both
the user’s prompt and assistant-response snippets, with Mi-
crosoft Clarity through session replay. Fifteen chatbots share
conversation URLs or chat identifiers with third-party ad-
vertising, analytics, or social endpoints. Several chatbots ex-
pose account identity, including email addresses and names,
through embedded support widgets, analytics, session replay,
and advertising tags; in some cases, hashed emails are shared.
We also find that private modes substantially reduce third-
party tracking. We conclude by discussing privacy policies
and privacy-enhancing design/configuration choices that
reduce exposure in AI chatbots.
2 Background and Related Works
2.1 Overview of AI Chatbots
AI chatbots deliver personalized conversations by learning
from each user’s history, progressively building an under-
standing of their preferences, habits, and context [ 29, 68].
When a user submits a query, their prompt is combined with
the provider-set system instructions and the current chat
history to form the context window, and then sent as an
input to a backend LLM hosted on the provider’s servers.
Chatbot-as-a-service platforms (e.g., OpenRouter [51]) ex-
pose multiple third-party LLMs through a single interface,
forwarding queries either directly to the model provider or
via the platform’s own infrastructure.
The context window also includes two types of chatbot-
managed memory [ 47]:reference memories, inferred from
past chats via the provider’s proprietary memory architec-
ture, andsaved memories, which the user has explicitly asked
the chatbot to retain. Together, they let the model tailor
responses to the individual.
Privacy features in AI chatbots. AI chatbots offer privacy
controls in three categories.Memory controlslet users toggle
reference and saved memories, and view or selectively delete
saved ones [47].Model improvement controlslet users opt out
of having their conversations used to train or fine-tune the
provider’s LLMs [45].Privateortemporary chats—analogous
to a browser’s incognito mode—isolate the session from prior
memories and disable retention of the new ones [ 25, 46],
typically bundling the other two controls and preserving
conversational utility while keeping the session private.
2.2 Studies on Privacy in AI Chatbots
Prior work has examined chatbot security and privacy prac-
tices [39, 59] and the resulting harms to users [28], including
LLMs’ ability to infer sensitive attributes from innocuous
text [21, 64], and adversarial configurations that elicit disclo-
sures or exfiltrate user data [30, 75].
Recent work has explored tracking in adjacent AI surfaces.
Wu et al. [71] and Carrillo et al. [ 12] audit OpenAI’s GPT
plugin ecosystem, finding third-party Actions that collect
data prohibited by OpenAI, enable cross-GPT tracking, and
disclose data practices inconsistently—only 5.8% of Actions
disclose collection in their privacy policy, and over 37% of
GPTs show broken traceability between transmissions and
disclosures. Most relevant to our work, Vekaria et al. [ 68]
audit generative AI browser extensions and find them shar-
ing webpage content, prompts, and identifiers with third-
party trackers. These works examine peripheral AI surfaces—
plugins and browser extensions—rather than the first-party
chatbots where users share information most directly. We
fill this gap by analyzing the network traffic of the 20 most
popular AI chatbots.
3 Methodology
3.1 Data Collection on AI Chatbots
Chatbot selection. We study web-based AI chatbots: that
is, chatbot services that users access directly through the
provider’s website. Our scope excludes mobile applications,
browser extensions/plugins, and chatbot functionality em-
bedded inside websites. Our goal in this study is to study
the tracking behavior of the chatbot provider’s own web
interface during a user-initiated conversation. We select 20
popular AI chatbot services: ChatGPT* [49], Gemini* [27],
Claude* [10], Grok* [73], DeepSeek [18], Character.AI [13],
Perplexity* [53], Microsoft Copilot [38], PolyBuzz [55], Kimi
[43], Qwen Chat* [8], Manus [33], Genspark [23], Meta AI
[34], Duck.ai [20], SeaArt [62], OpenRouter [51], Poe [58],
Mistral* [41], and ChatOn [6] (Services marked with * sup-
port private/temporary chats). We use Similarweb rankings
and traffic estimates as an external signal of popularity [63].
Account setup. For each chatbot, we created a fresh user ac-
count using either email-based registration or Google single
sign-on (SSO), depending on the options supported by the
chatbot service. When the service requested profile informa-
tion, we provided consistent name and account identity.
2

Tracking Conversations
Table 1: Summary of identity and content exposure on chatbots. For identity exposures, green=first-party, red=third-
party, and orange=both; channel markers: U=url, B=body, H=header, and C=cookie. Content cells reflect third-party
exposure only. For IP and User Agent, we only report exposure from the Body of the request.
ChatGPT
Gemini
Claude
Grok
DeepSeek
Character AI
Perplexity
Copilot
PolyBuzz
Kimi
Qwen
Manus
Genspark
Meta AI
Duck.ai
SeaArt
OpenRouter
Poe
Mistral
ChatOn
Identity
Email HC ✘ B B ✘ B UBH ✘ ✘ ✘ ✘ ✘ ✘ ✘ ✘ B B ✘ B C
Name HC ✘ B B ✘ B B ✘ ✘ ✘ ✘ UHC ✘ ✘ ✘ BHC B ✘ B HC
IP and User Agent ✘ ✘ ✘ ✘ ✘ B ✘ ✘ ✘ ✘ ✘ ✘ ✘ ✘ ✘ ✘ ✘ ✘ ✘ ✘
Content
User Prompt ✘ ✘ ✘ ✘ ✘ ✘ ✘ ✘ ✘ UH ✘ ✘ UH ✘ ✘ ✘ ✘ ✘ ✘ ✘
Prompt Keywords ✘ ✘ B ✘ ✘ ✘ ✘ ✘ ✘ UH ✘ B UHB ✘ ✘ ✘ ✘ ✘ ✘ ✘
Chat URL ✘ ✘ ✘ ✘ ✘ U ✘ U U UB UH UB UHB ✘ ✘ UHB ✘ U ✘ B
Chat Identifier U B B U B U ✘ U UB UB UH UB UHB ✘ ✘ UHB ✘ U ✘ B
Prompt. For each chatbot, we conducted a chat session using
the fixed prompt:“pregnancy test near me. ”This prompt com-
bines a health-related query with an implicit location request,
allowing us to understand how chatbots handle potentially
sensitive information. Note that our goal is not to evaluate
the quality or correctness of the chatbot’s response. Instead,
the single-prompt conversation provides a controlled inter-
action in which any observed disclosures can be tied to the
same user input across different chatbot services.
Normal and private modes. We evaluate the defaultnor-
malmode for all 20 chatbots. For chatbots that offer apri-
vatemode, we conduct an additional session using the same
prompt. Private chats are presented as incognito-styled con-
versations that claim to provide heightened privacy pro-
tections (e.g., no retention). This comparison allows us to
measure the extent of tracking inprivatevs.normalchats.
Capturing network traffic. All testing was conducted in
Chrome browser, which does not offer tracking protection at
the time of writing as is offered in other browsers such as Sa-
fari’s Intelligent Tracking Prevention (ITP) [70] or Firefox’s
Enhanced Tracking Protection (ETP) [65]. Chrome provides
a baseline for tracking that is caused by chatbot website de-
sign and third-party integration. For each session, we began
from a fresh browser state for the corresponding account
and recorded the traffic generated while loading the chat-
bot interface, submitting the prompt, and waiting for the
chatbot to complete its response. For each session, we cap-
tured network traffic containing HTTP request and response
metadata, including URLs, headers, and payloads. Addition-
ally, we also extract first-party cookies. Fornormalsessions,
recording begins at page navigation and continues until the
chatbot completes its response. Forprivatesessions, record-
ing begins when theprivatesession is initiated, so that traffic
from initial normal-mode activity is excluded.
3.2 Analyzing Chatbot Traffic
We analyze each captured session in four stages: preprocess-
ing traffic, defining search targets, matching targets against
the traffic, and attributing matches to the receiving parties.
Preprocessing. The information transmitted by chatbot
websites and embedded third-parties is often encoded or
compressed before transmission. We therefore preprocess
captured URLs, headers, cookies, and payloads before search-
ing them. We decompress gzip- and zlib-compressed pay-
loads when present and decode common transport encodings
including base64 and URL encoding. Decoded payloads are
converted to strings so they can be searched alongside re-
quest URLs, query parameters, headers, and cookie values.
Search targets. We search the preprocessed traffic for two
broad categories of information:contentandidentity.Con-
tentcaptures what the user is asking or which conversation
the user is engaged in. It includes the user’s exact prompt,
readable assistant-response text when present in captured
payloads, keywords drawn from the prompt (e.g.,pregnancy,
test,pregnancy test), generated chat titles derived from the
prompt, chat identifiers, and unique URLs to individual chats.
Identitycaptures who the user is or how the user can be rec-
ognized across requests. It includes the test account’s first
name, last name, display name, email address, internal user
identifiers when observable, and any first-party cookies sent
to third parties. We also search for IP and User-Agent values
when they appear as explicit fields in request payloads.
Matching procedure. For each search target, we look for
exact string matches as well as common hashing, encoding
schemes, and compression formats as used in [69]. Specifi-
cally, we generate case-variants (lowercase, uppercase), en-
coded forms (hex/base16, base32, base64, base64url, URL-
encoded, URL-plus-encoded), compressed forms (gzip and de-
flate, both base64-encoded), checksums (Adler-32, CRC-32),
3

Jazlan et al.
and cryptographic hashes (MD5, SHA-1, SHA-224/256/384/
512, SHA3-224/256/384/512, and RIPEMD-160 where avail-
able) of both the original value and each case-variant.
Party attribution. Each request in a session is classified
as first-party, if its eTLD+1 matches that of the chatbot’s
landing page, and third-party, otherwise. Third parties are
further categorized by functionality into analytics, advertis-
ing, and other. When a domain is clearly part of the chatbot
provider (e.g., openai.com on chatgpt.com), we categorize it
as platform-party rather than as a third-party.
4 Results
In this section, we present the results of our measurement
study. We first characterize the third-party and platform-
party flows observed during our measurements. We then
analyze exposure of the two categories of information:con-
tentandidentity. Finally, we comparenormalandprivate
chats to evaluate whether private modes reduce tracking.
4.1 Third-Party vs. Platform-Party Flows
We categorize domains present on a chatbot into three cate-
gories: afirst partyshares the chatbot’s eTLD+1, aplatform
partyhas a different eTLD+1 but the same owner, and athird
partyhas a different eTLD+1 and a different owner.
Across the 20 chatbots we test, we observe 47 unique
third-party owners and 178 distinct (chatbot, third-party do-
main) pairs during ournormalchat sessions, after excluding
each chatbot’s platform-party domains. Three chatbots con-
tact no third parties: Gemini (gemini.google.com), Meta AI
(meta.ai), and Duck.ai (duck.ai). Instead, these services con-
tact first- or platform-party domains. Gemini contacts several
Google-owned domains, including Google Analytics (google-
analytics.com), Google Tag Manager (googletagmanager.com),
and Google static content (gstatic.com). Meta AI loads con-
tent from Facebook’s CDN (fbcdn.net), while Duck.ai sends
requests to duckduckgo.com. Figure 1 visualizes these data
flows for advertising and analytics parties. See Appendix D
for data flows to all parties in normal and temporary chats.
Third parties by category. We classify each third party
into one of three functional categories: advertising, analytics,
and other. Analytics and advertising appear on 17 and 12 of
the 20 chatbots, respectively. Advertising appears on fewer
chatbots than analytics, but the chatbots that load advertising
services often contact many advertising domains in a single
session. As a result, advertising accounts for the largest share
of observed (chatbot, third-party domain) pairs: 73 of 178. For
example, SeaArt contacts 13 distinct advertisers in a single
session: A8, Amazon, Google, Meta, Microsoft, Outbrain,
Pinterest, Quora, Reddit, TikTok, Twitter/X, Yahoo Japan,
and Yandex. Genspark contacts a comparable number.
Note that the same owner can appear under multiple cate-
gories because organizations operate different domains and
endpoints for different purposes. Google is the clearest ex-
ample: doubleclick.net and googlesyndication.com are cate-
gorized as advertising; googletagmanager.com and google-
analytics.com as analytics; gstatic.com, googleusercontent.
com, googleapis.com, and run.app as other. Microsoft is sim-
ilar: clarity.ms is categorized as analytics, while bing.com
and azure.com are categorized as other.
First-party and platform-party flows. Some services route
analytics or session-replay traffic through first- or platform-
party domains. For example, Google Analytics appears on
Gemini, but we classify it as platform-party because the con-
tacted domain is owned by Google. Microsoft Copilot sends
Microsoft Clarity traffic through the first-party endpoint
https://copilot.microsoft.com/cl/eus2-g/collect. Similarly, on
ChatGPT, we observe requests to chatgpt.com/ces/ whose
payloads include Datadog- and Statsig-related fields. We
classify these requests as first-party because they are sent
to chatgpt.com, but they remain relevant to our analysis
because they show that analytics-related payloads can be
routed through first-party or platform-party domains rather
than through third-party domains.
4.2 Content Exposure
We now examine exposure ofcontentinformation to different
parties, observed through three mechanisms: session replay,
embedded widgets, and page meta-data collected by tags and
widgets loaded on the chatbot page.
Session replay. Four chatbots embed Microsoft Clarity [3], a
session replay service. Because the rendered DOM on a chat-
bot page contains the conversation itself, session replay can
capture both the user’s prompt and the assistant’s response.
Three of the four (Genspark, SeaArt, and Chaton) transmit
conversation text in plaintext to Clarity. We observed Clar-
ity receiving the exact prompt string (“pregnancy test near
me”) on all three chatbots, along with readable portions
of the assistant’s reply: on Genspark, response consisted
“Here are a few pregnancy test options near you”; on SeaArt,
extended roleplay response text spanned multiple sentences;
and on Chaton, response text was “Most pharmacies like
CVS, Walgreens, or Rite Aid offer carry home pregnancy
tests. ” Thus, Clarity receives a readable reconstruction of
the conversation (i.e., prompt, response, and surrounding UI
text) sufficient to infer what the user asked, what they were
told, and what action did the user take.
Copilot Chat also embeds Clarity, but routes it through the
first-party endpoint https://copilot.microsoft.com/cl/eus2-
g/collect. We do not observe plaintext conversation text
in these payloads. Instead, the payloads include message-
specific identifiers and the order in which messages appeared
in the DOM. We therefore treat Copilot separately from the
third-party plaintext session-replay exposures above.
4

Tracking Conversations
ChatOn
Mistral
Poe
OpenRouter
SeaArt
Genspark
Manus
Qwen Chat
Kimi
PolyBuzz
Microsoft Copilot
Perplexity
Character.AI
DeepSeek
Grok
Claude
Gemini
ChatGPT
yandex.ru
rumt-sg.com
prodregistryv2.org
sprig.com
sentry.io
instajob.ai
plausible.io
clarity.ms
intercom.io
googletagmanager.com*
google-analytics.com*
google-analytics.com
google.com (Analytics)
googletagmanager.com
eppo.cloud
browser-intake-datadoghq.com
browser-intake-us5-datadoghq.com
dashfi.dev
cloudflareinsights.com
volces.com
amplitude.com
aliyuncs.com*
yandex.com
yimg.jp
yahoo.co.jp
twitter.com
t.co
ads-twitter.com
tiktokw.us
tiktok.com
tver.sale
tver.jp
smartnews-ads.com
singular.net
reddit.com
quora.com
pinterest.com
outbrain.com
pstatic.net
naver.net
naver.com
docomo.ne.jp
bing.com*
bing.com
facebook.net
facebook.com
adtrafficquality.google
googleadservices.com
google.com (Advertising)
googlesyndication.com
doubleclick.net
d2c.ne.jp
d2-apps.net
paa-reporting-advertising.amazon
amazon-adsystem.com
taobao.com*
alibaba.com*a8.net3P Categories
Advertising
Analytics
Figure 1: Sankey of data flows from chatbots to adver-
tising and analytics third-parties in normal chats.
Widgets. Genspark transmits the full prompt to Google
Maps [1] by embedding it within a query to the URL: www.
google.com/maps/embed/v1/search?q=pregnancy+test+near+
me. The raw prompt is URL-encoded and passed to Google
in parameter q of the map load. This exposes the user’s ex-
act prompt to Google as part of loading the embedded map.
The map is loaded as a third-party iframe, which can attach
Google cookies depending on the user’s browser state—for
instance, whether the user is logged into a Google account—
potentially linking the prompt to the user’s Google identity.
Title. Kimi, Claude, Manus, Gemini, and Genspark place the
user’s prompt or an extracted keyword (e.g., “pregnancy”)
into the page title, from where it is collected by tags and
widgets loaded on the page. Kimi’s title reaches Google’s
DoubleClick via the standard dt parameter and is forwarded
to Google Ads via a tiba parameter. Claude and Manus
both embed Intercom’s customer-support messenger [ 2];
Intercom’s web widget posts page metadata (including the
title) to api-iam.intercom.io/messenger/web/metrics. Gemini
sends the page title to its platform-party Google Analytics
in the standard payload.
URL. Chatbots typically assign a per-conversation URL that
appears in the browser’s address bar (e.g., claude.ai/chat/
<chat-id>). Fifteen of the 20 chatbots we test transmit the
URL to at least one third-party through standard analytics
or advertising tags, reaching 29 distinct destinations in total.
Meta Pixel’s dl parameter, Google Analytics’s collect end-
point, Bing’s UET tag, and DoubleClick’s conversion tags all
collect the current page URL by default, so any chatbot that
embeds these tags automatically transmits the chat identi-
fier to the corresponding destination. SeaArt and Genspark
exhibit the broadest exposure: SeaArt transmits chat identi-
fiers to 12 destinations, including Facebook, Google, TikTok,
Yandex, Outbrain, and Quora, and Genspark to 7, including
Facebook, Google, Bing, TikTok, and Microsoft Clarity. The
remaining chatbots transmit to between 1 and 4 destinations.
Unlike prompt keywords, the chat identifier does not it-
self reveal conversation text, but it identifies a specific con-
versation. On chatbots where the chat URL is shareable or
otherwise resolvable, exposing the URL can expose a pointer
to the conversation; even where the URL requires authenti-
cation, the identifier still lets the receiving party associate
information with the same chat.
4.3 Identity Exposure
Next, we examine exposure ofidentityinformation to other
parties, observed through four mechanisms: widgets, analyt-
ics, advertising, and session replay.
Widgets. Embedded widgets transmit identity information
as part of their own functional payloads. On Claude and
Mistral, the Intercom widget fires a ping request when the
chat page loads, carrying the user’s email, name, internal
user ID, and user hash (Listing 1). The ping fires without any
interaction with the support widget. Intercom also transmits
first-party cookies (intercom-device-id-* and intercom-
session-*) to intercom.io. Genspark transmits the__stripe
_midand__stripe_sidfirst-party cookies to stripe.com.
Analytics. Analytics and error-monitoring tags receive iden-
tity data attached to event payloads. On Character.ai, the
Sentry tag transmits session envelopes to sentry.io. The did
field carries the user’s email, the user_agent field carries
the User-Agent string directly, and the ip_address field is
set to the sentinel "{{auto}}", which instructs Sentry to
record the client IP from the connection (Listing 2). This
differs from automatic network-layer IP exposure because
the tag explicitly configures IP collection as part its payload.
5

Jazlan et al.
Also on Character.ai, the Statsig tag transmits experimenta-
tion and feature-flag events to prodregistryv2.org/v1/rgstr.
Each event payload carries the user’s email, internal user
ID, IP address, and User-Agent in the user object alongside
the experiment or feature-flag exposure being logged (List-
ing 3). Claude transmits the ajs_user_id cookie and the
lastActiveOrg cookie, which identifies the active organi-
zation, to Datadog.
Advertising. Advertising tags mainly receive two types of
identity information: hashed emails that function as per-
sistent cross-site identifiers [4], and first-party cookies (in
addition to third-party cookies) that function as advertis-
ing and analytics identifiers. Perplexity transmits hashed
email to Singular, and SeaArt transmits a hashed email in the
eb_email field to the TikTok pixel at analytics.tiktok.com.
Because the same email produces the same hash across sites,
these values can support cross-site recognition [4]: Singular
and TikTok can link the user’s activity on these chatbot sites
to activity on any other site that reports the same hashed
email. Meta’s _fbp cookie is the most widespread advertising
identifier we observe, transmitted on Character.ai, Chaton,
Genspark, Manus, PolyBuzz, and SeaArt to facebook.com/tr
or facebook.com/privacy_sandbox. Microsoft’s UET cook-
ies (_uetsid, _uetvid) are sent to bat.bing.com on Chaton,
Copilot, Genspark, and SeaArt. SeaArt additionally transmits
TikTok’s _ttp and Pinterest’s _pin_unauth first-party cook-
ies to tiktok.com and pinterest.com, respectively. Perplexity
transmits thepplx.visitor-idcookie to Singular.
Session replay. On Chaton, Genspark, and SeaArt, the user’s
email and name are captured by Microsoft Clarity as part
of the rendered DOM and transmitted to *.clarity.ms/collect.
Because these values are displayed in the chatbot UI (e.g.,
greeting messages, in-conversation mentions), they are auto-
included in the session-replay snapshot as a side effect. Un-
like the widget, analytics, and advertising examples above,
this identity information is not placed into a labeled field. It
appears as readable text on the page that the replay tooling
captures alongside the rest of the DOM.
4.4 Private Chats
Tracking is substantially reduced in private chats. Among
chatbots with aprivatemode, distinct (chatbot, third-party
domain) pairs drops to 13 (shown in Figure 2), and the num-
ber of unique third-party owners drops to 3: Datadog, Map-
box, and Google. Only ChatGPT, Claude, Grok, Perplexity
and Qwen send requests to third parties. Most importantly,
we observe noidentityorcontentexposure to any third party
in any private chat session.
5 Conclusion & Discussion
We present the first systematic measurement of tracking on
AI chatbots, analyzing the network traffic of the 20 most
popular services. We find that 17 of 20 chatbots embed third
parties, several expose user identity to analytics and adver-
tising vendors, and a subset transmit full conversation text
in plaintext via session-replay tools. Conversation identifiers
reach a broad set of third-party destinations. In the rest of
this section, we discuss mitigations that chatbot providers
can adopt, and compare the observed third-party exposure
with what the chatbot privacy policies disclose to users.
5.1 Mitigations
Most of the exposures in our analysis result from design or
configuration choices made by the chatbot provider. In this
section, we discuss mitigations that can reduce these expo-
sures short of completely removing analytics, advertising, or
embedded widgets.
Page URL and title. Placing a user’s prompt, chat title, or
chat identifier in the page URL or title exposes them to being
tracked via embedded analytics, advertising, and support
widgets that collect page metadata by default. Providers can
avoid prompt-derived text in document.title and redact
chat identifiers from URLs reported to third-party tags.
Widget integrations. Embedded widgets should not re-
ceive the user’s raw prompt unless they directly need it. On
Genspark, the Google Maps widget exposes the user’s full
prompt because the prompt is embedded in the Maps iframe
URL as the q parameter. A more privacy-preserving design
would resolve the location query server-side and pass only
the minimum information needed to render the map, such
as coordinates or a sanitized place query.
Third-party tag configurations. Several third-party tools
provide configurations that can reduce identity and content
exposure. Session-replay tools should not be deployed on
authenticated conversation pages, where the rendered DOM
contains both identity information and conversation text;
if deployed, content masking should be employed to redact
prompts, responses, and account fields. For analytics and
error monitoring, providers should avoid directly attaching
identifying account fields when other identifiers suffice. For
example, the Sentry configuration on Character.AI records
the client IP and transmits the user’s email—neither is nec-
essary for typical error monitoring.
5.2 Privacy Disclosures
We compare the observed third party data exposure with the
disclosures in each chatbot’s privacy policy. We aim to assess
whether the policies give users a concrete description of the
third parties that receive data during chatbot use. All 20 pri-
vacy policies [7, 9, 14, 15, 17, 19, 22, 26, 32, 35, 36, 40, 42, 44,
50, 52, 54, 57, 61, 72] disclose that user data may be collected
and used for a subset of the following purposes: analytics,
6

Tracking Conversations
advertising, service operation, personalization, safety, debug-
ging, or support. However, the policies vary substantially in
how specifically they identify the parties involved. Eight poli-
cies describe categories of recipients or purposes of sharing
but do not name the third parties we observe in network traf-
fic. The gap is concerning when a privacy policy names some
recipients but omits others. Chaton, SeaArt, and Genspark
each name specific third parties in their policies but omit
Microsoft Clarity, despite Clarity receiving plaintext conver-
sation text in our measurements. In contrast, Claude and
OpenRouter list a broad set of third parties present on their
websites and describe the types of data shared with them.
DuckAI is a clear outlier; they do not track the user, going
as far as stripping user IPs before forwarding requests to AI
providers, hosted on named services. The additional privacy
disclosures shown when a user opens a private (or tempo-
rary chat) focus primarily on chat retention, model training,
and personalization—not tracking [5]. We found that private
modes reduce third-party exposure in our measurements
even though the disclosures do not explicitly characterize
them as tracking controls.
References
[1] n.d.. Google Maps — google.com. https://www.google.com/maps.
[Accessed 27-04-2026].
[2] n.d.. Intercom | AI Customer Service Platform — intercom.com. https:
//www.intercom.com/drlp/ai-customer-service. [Accessed 27-04-
2026].
[3] n.d.. Microsoft Clarity - Free Heatmaps & Session Recordings — clar-
ity.microsoft.com. https://clarity.microsoft.com. [Accessed 27-04-
2026].
[4] n.d.. No, hashing still doesn’t make your data anonymous —
ftc.gov. https://www.ftc.gov/policy/advocacy-research/tech-at-ftc/
2024/07/no-hashing-still-doesnt-make-your-data-anonymous. [Ac-
cessed 26-04-2026].
[5] n.d.. Temporary Chat FAQ | OpenAI Help Center — help.openai.com.
https://help.openai.com/en/articles/8914046-temporary-chat-faq. [Ac-
cessed 28-04-2026].
[6] AIBY. n.d.. ChatOn. https://chaton.ai. Accessed: 2026-04-27.
[7] Alibaba Cloud. 2026. Qwen Chat Privacy Policy. https:
//web.archive.org/web/20260424164454/https://chat.qwen.ai/legal-
agreement/privacy-policy. Archived snapshot 2026-04-24 of
https://chat.qwen.ai/legal-agreement/privacy-policy.
[8] Alibaba Cloud. n.d.. Qwen Chat. https://chat.qwen.ai. Accessed:
2026-04-27.
[9] Anthropic. 2026. Updates to Our Acceptable Use Policy
(Now Usage Policy), Consumer Terms of Service and Privacy
Policy. https://web.archive.org/web/20260427050410/https:
//privacy.claude.com/en/articles/9301722-updates-to-our-
acceptable-use-policy-now-usage-policy-consumer-terms-of-
service-and-privacy-policy. Archived snapshot 2026-04-27 of
https://privacy.claude.com/en/articles/9301722-updates-to-our-
acceptable-use-policy-now-usage-policy-consumer-terms-of-
service-and-privacy-policy.
[10] Anthropic. n.d.. Claude. https://claude.ai. Accessed: 2026-04-27.
[11] Guendalina Caldarini, Sardar Jaf, and Kenneth McGarry. 2022. A
literature survey of recent advances in chatbots.Information13, 1
(2022), 41.
[12] Juan-Carlos Carrillo, Jose Luis Martin-Navarro, Rongjun Ma, and Jose
Such. 2026. Personal Data Flows and Privacy Policy Traceability in
Third-party LLM Apps in the GPT Ecosystem.Proceedings on Privacy
Enhancing Technologies(2026).
[13] Character Technologies. n.d.. Character.AI. https://character.ai. Ac-
cessed: 2026-04-27.
[14] Character.AI. 2026. Privacy Policy. https://web.archive.org/web/
20260427024931/https://policies.character.ai/privacy. Archived snap-
shot 2026-04-27 of https://policies.character.ai/privacy.
[15] ChatOn. 2026. Privacy Policy. https://web.archive.org/web/
20260409165952/https://chaton.ai/legal/privacy/en/. Archived snap-
shot 2026-04-09 of https://chaton.ai/legal/privacy/en/.
[16] The Conversation. 2026. You probably wouldn’t notice if an AI chatbot
slipped ads into its responses. https://theconversation.com/you-
probably-wouldnt-notice-if-an-ai-chatbot-slipped-ads-into-its-
responses-276010 Accessed: April 2026.
[17] DeepSeek. 2026. DeepSeek Privacy Policy. https://web.archive.
org/web/20260425172815/https://cdn.deepseek.com/policies/en-
US/deepseek-privacy-policy.html. Archived snapshot 2026-04-25
of https://cdn.deepseek.com/policies/en-US/deepseek-privacy-
policy.html.
[18] DeepSeek. n.d.. DeepSeek. https://chat.deepseek.com. Accessed:
2026-04-27.
[19] DuckDuckGo. 2026. Duck.ai Privacy and Terms. https:
//web.archive.org/web/20260424003226/https://duckduckgo.
com/duckai/privacy-terms. Archived snapshot 2026-04-24 of
https://duckduckgo.com/duckai/privacy-terms.
[20] DuckDuckGo. n.d.. Duck.ai. https://duck.ai. Accessed: 2026-04-27.
[21] Jinyan Fan, Tianjun Sun, Jiayi Liu, Teng Zhao, Bo Zhang, Zheng Chen,
Melissa Glorioso, and Elissa Hack. 2023. How well can an AI chatbot
infer personality? Examining psychometric properties of machine-
inferred personality scores.Journal of Applied Psychology108, 8 (2023),
1277.
[22] Genspark. 2026. Privacy Policy. https://web.archive.org/web/
20260405154843/https://www.genspark.ai/privacy. Archived snapshot
2026-04-05 of https://www.genspark.ai/privacy.
[23] Genspark. n.d.. Genspark. https://genspark.ai. Accessed: 2026-04-27.
[24] Joanna Gerber. 2025. Programmatic Ads Are Coming To AI Chat-
bots. https://www.adexchanger.com/publishers/programmatic-ads-
are-coming-to-ai-chatbots/
[25] Google. 2025. Gemini adds Temporary Chats and new personaliza-
tion features. https://blog.google/products/gemini/temporary-chats-
privacy-controls/ Accessed: April 2026.
[26] Google. 2026. Gemini Apps Privacy Hub. https://web.archive.org/
web/20260427020833/https://support.google.com/gemini/answer/
13594961?hl%3Den&sa=D&source=docs&ust=1777260507640669&
usg=AOvVaw2mU7m5ctEia5pjcwwMRTgf. Archived snapshot
2026-04-27 of https://support.google.com/gemini/answer/13594961.
[27] Google. n.d.. Gemini. https://gemini.google.com. Accessed: 2026-04-
27.
[28] Ece Gumusel, Kyrie Zhixuan Zhou, and Madelyn Rose Sanfilippo.
2024. User privacy harms and risks in conversational ai: A proposed
framework.arXiv preprint arXiv:2402.09716(2024).
[29] Bowen Jiang, Zhuoqun Hao, Young Min Cho, Bryan Li, Yuan Yuan,
Sihao Chen, Lyle Ungar, Camillo Jose Taylor, and Dan Roth. [n. d.].
Know Me, Respond to Me: Benchmarking LLMs for Dynamic User
Profiling and Personalized Responses at Scale. InSecond Conference
on Language Modeling.
[30] Yigitcan Kaya, Anton Landerer, Stijn Pletinckx, Michelle Zimmermann,
Christopher Kruegel, and Giovanni Vigna. 2025. When AI Meets the
Web: Prompt Injection Risks in Third-Party AI Chatbot Plugins.arXiv
7

Jazlan et al.
preprint arXiv:2511.05797(2025).
[31] Lisa Mekioussa Malki, Akhil Polamarasetty, Majid Hatamian, Mark
Warner, and Enrico Costanza. 2025. Hoovered up as a data point:
Exploring Privacy Behaviours, Awareness, and Concerns Among UK
Users of LLM-based Conversational Agents.Proceedings on Privacy
Enhancing Technologies(2025).
[32] Manus. 2026. Privacy Policy. https://web.archive.org/web/
20260425063340/https://manus.im/privacy. Archived snapshot 2026-
04-25 of https://manus.im/privacy.
[33] Manus. n.d.. Manus. https://manus.im. Accessed: 2026-04-27.
[34] Meta. n.d.. Meta AI. https://meta.ai. Accessed: 2026-04-27.
[35] Meta Platforms. 2026. Meta Privacy Policy. https://web.archive.org/
web/20260426031933/https://www.facebook.com/privacy/policy/.
Archived snapshot 2026-04-26 of https://www.facebook.com/privacy/
policy/.
[36] Microsoft. 2026. Microsoft Privacy Statement. https://web.
archive.org/web/20260426204347/https://www.microsoft.com/en-
us/privacy/privacystatement. Archived snapshot 2026-04-26 of
https://www.microsoft.com/en-us/privacy/privacystatement.
[37] Microsoft. n.d.. About Ads in Copilot. https://help.ads.microsoft.com/
#apex/ads/en/60343/0. [Accessed 27-04-2026].
[38] Microsoft. n.d.. Microsoft Copilot. https://copilot.microsoft.com. Ac-
cessed: 2026-04-27.
[39] Niloofar Mireshghallah and Tianshi Li. 2025. Position: Privacy Is Not
Just Memorization!arXiv preprint arXiv:2510.01645(2025).
[40] Mistral AI. 2026. Privacy Policy. https://web.archive.org/web/
20260406094100/https://legal.mistral.ai/terms/privacy-policy.
Archived snapshot 2026-04-06 of https://legal.mistral.ai/terms/privacy-
policy.
[41] Mistral AI. n.d.. Mistral. https://mistral.ai. Accessed: 2026-04-27.
[42] Moonshot AI. 2026. Kimi User Privacy Policy. https:
//web.archive.org/web/20260330170734/https://platform.kimi.
ai/docs/agreement/userprivacy. Archived snapshot 2026-03-30 of
https://platform.kimi.ai/docs/agreement/userprivacy.
[43] Moonshot AI. n.d.. Kimi. https://kimi.com. Accessed: 2026-04-27.
[44] OpenAI. 2026. ChatGPT Privacy Policy (Rest of World).
https://web.archive.org/web/20260426234619/https://openai.com/
policies/row-privacy-policy/. Archived snapshot 2026-04-26 of
https://openai.com/policies/row-privacy-policy/.
[45] OpenAI. 2026. Data Controls FAQ. https://help.openai.com/en/
articles/7730893-data-controls-faq Accessed: April 2026.
[46] OpenAI. 2026. How your data is used to improve model perfor-
mance. https://openai.com/policies/how-your-data-is-used-to-
improve-model-performance/ Accessed: April 2026.
[47] OpenAI. 2026. Memory FAQ. https://help.openai.com/en/articles/
8590148-memory-faq Accessed: April 2026.
[48] OpenAI. n.d.. Ads in ChatGPT | OpenAI Help Center —
help.openai.com. https://help.openai.com/en/articles/20001047-ads-
in-chatgpt. [Accessed 28-04-2026].
[49] OpenAI. n.d.. ChatGPT. https://chatgpt.com. Accessed: 2026-04-27.
[50] OpenRouter. 2026. Privacy Policy. https://web.archive.org/web/
20260418174831/https://openrouter.ai/privacy. Archived snapshot
2026-04-18 of https://openrouter.ai/privacy.
[51] OpenRouter. n.d.. OpenRouter. https://openrouter.ai. Accessed:
2026-04-27.
[52] Perplexity AI. 2026. Privacy Policy. https://web.archive.org/web/
20260425043522/https://www.perplexity.ai/hub/legal/privacy-policy.
Archived snapshot 2026-04-25 of https://www.perplexity.ai/hub/legal/
privacy-policy.
[53] Perplexity AI. n.d.. Perplexity. https://perplexity.ai. Accessed: 2026-
04-27.
[54] PolyBuzz. 2026. Privacy Policy. https://web.archive.org/web/
20260409194027/https://www.polybuzz.ai/privacy-policy. Archived
snapshot 2026-04-09 of https://www.polybuzz.ai/privacy-policy.
[55] PolyBuzz. n.d.. PolyBuzz. https://polybuzz.ai. Accessed: 2026-04-27.
[56] Synthia Qia Wang, Sai Teja Peddinti, Nina Taft, and Nick Feamster.
2026. Beyond PII: How Users Attempt to Estimate and Mitigate Implicit
LLM Inference. InProceedings of the 2026 CHI Conference on Human
Factors in Computing Systems. 1–17.
[57] Quora. 2026. Poe Privacy Policy. https://web.archive.org/web/
20260427025713/https://poe.com/pages/privacy. Archived snapshot
2026-04-27 of https://poe.com/pages/privacy.
[58] Quora. n.d.. Poe. https://poe.com. Accessed: 2026-04-27.
[59] Abdelrahman Ragab, Mohammad Mannan, and Amr Youssef. 2024.
“Trust Me Over My Privacy Policy”: Privacy Discrepancies in Romantic
AI Chatbot Apps. In2024 IEEE European Symposium on Security and
Privacy Workshops (EuroS&PW). IEEE, 484–495.
[60] Chris Rowlands. 2025. Goodbye Google? People are increas-
ingly switching to the likes of ChatGPT, according to major
survey. https://www.techradar.com/tech/people-are-increasingly-
swapping-google-for-the-likes-of-chatgpt-according-to-a-major-
survey-heres-why
[61] SeaArt. 2026. Privacy Policy. https://web.archive.org/web/
20260425184324/https://node1.cdn2.seaart.ai/mirror/static/
upload/policy.html. Archived snapshot 2026-04-25 of
https://node1.cdn2.seaart.ai/mirror/static/upload/policy.html.
[62] SeaArt. n.d.. SeaArt. https://seaart.ai. Accessed: 2026-04-27.
[63] Similarweb. 2026. Top AI Chatbots and Tools Websites Rank-
ing. https://web.archive.org/web/20260424195050/https://www.
similarweb.com/top-websites/ai-chatbots-and-tools/.
[64] Robin Staab, Mark Vero, Mislav Balunović, and Martin Vechev. 2023.
Beyond memorization: Violating privacy via inference with large
language models.arXiv preprint arXiv:2310.07298(2023).
[65] Mozilla Support. 2026. Enhanced Tracking Protection in Firefox for
desktop. https://support.mozilla.org/en-US/kb/enhanced-tracking-
protection-firefox-desktop.
[66] Surfshark. 2025. AI Chatbots Ranked by Data They Collect. https:
//surfshark.com/research/chart/ai-chatbots-privacy Accessed: April
2026.
[67] Jan Tolsdorf, Alan F Luo, Monica Kodwani, Junho Eum, Mahmood
Sharif, Michelle L Mazurek, and Adam J Aviv. 2025. Safety Perceptions
of Generative {AI} Conversational Agents: Uncovering Perceptual
Differences in Trust, Risk, and Fairness. InTwenty-First Symposium
on Usable Privacy and Security (SOUPS 2025). 93–112.
[68] Yash Vekaria, Aurelio Loris Canino, Jonathan Levitsky, Alex Ciechon-
ski, Patricia Callejo, Anna Maria Mandalari, and Zubair Shafiq. 2025.
Big Help or Big Brother? Auditing Tracking, Profiling, and Personal-
ization in Generative {AI} Assistants. In34th USENIX Security Sym-
posium (USENIX Security 25). 8115–8134.
[69] Yash Vekaria, Nurullah Demir, Konrad Kollnig, and Zubair Shafiq.
2026. Understanding Data Collection, Brokerage, and Spam in the
Lead Marketing Ecosystem.arXiv preprint arXiv:2604.06759(2026).
[70] WebKit. [n.d.]. Tracking Prevention in WebKit. https://webkit.org/
tracking-prevention/.
[71] Yuhao Wu, Evin Jaff, Ke Yang, Ning Zhang, and Umar Iqbal. 2025. An
in-depth investigation of data collection in llm app ecosystems. In
Proceedings of the 2025 ACM Internet Measurement Conference. 150–
170.
[72] xAI. 2026. Privacy Policy. https://web.archive.org/web/
20260426055921/https://x.ai/legal/privacy-policy. Archived snapshot
2026-04-26 of https://x.ai/legal/privacy-policy.
[73] xAI. n.d.. Grok. https://grok.com. Accessed: 2026-04-27.
8

Tracking Conversations
[74] Maxwell Zeff. 2025. Meta plans to sell targeted ads based on data in
your AI chats. https://techcrunch.com/2025/10/01/meta-plans-to-
sell-targeted-ads-based-on-data-in-your-ai-chats/
[75] Xiao Zhan, Juan Carlos Carrillo, William Seymour, and Jose Such.
2025. Malicious {LLM-Based} Conversational {AI} Makes Users
Reveal Personal Information. In34th USENIX Security Symposium
(USENIX Security 25). 61–80.
[76] Zhiping Zhang, Michelle Jia, Hao-Ping Lee, Bingsheng Yao, Sauvik
Das, Ada Lerner, Dakuo Wang, and Tianshi Li. 2024. “It’s a Fair Game”,
or Is It? Examining How Users Navigate Disclosure Risks and Benefits
When Using LLM-Based Conversational Agents. InProceedings of the
2024 CHI Conference on Human Factors in Computing Systems. 1–26.
[77] Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang,
Yupeng Hou, Yingqian Min, Beichen Zhang, Junjie Zhang, Zican
Dong, et al. 2023. A survey of large language models.arXiv preprint
arXiv:2303.182231, 2 (2023), 1–124.
A Ethical Considerations
This work studies the privacy practices of AI chatbot web-
sites and does not rely on data collected from users. We
instead use test name, email, and account created specifically
for the experimentation and is not tied to any real individ-
ual’s identity. We performed a small-scale measurement by
signing up on 20 chatbot services, resulting in negligible
resource utilization burden on chatbot providers: we sent
a single prompt on 13 chatbots, and two prompts on the
7 chatbots that support a private or temporary chat mode.
Overall, this work does not raise any ethical concerns.
B Categorization of Third Parties
We classify each third-party domain into one of three cate-
gories:advertising,analytics, orother. We first identify the
eTLD+1’s owner from public ownership records, then ex-
amine the owner’s primary function. A domain is classified
asadvertisingif its owner runs an advertising platform or
serves ads on other platforms; asanalyticsif not, but instead
the owner provides analytics services; and else asother. Some
owners operate distinct services across paths or subdomains
of the same eTLD+1; in such cases we classify each path sep-
arately. For example, google.com/ccm isadvertising, while
google.com/maps isother.
C Request Payloads
Listing 1: Mistral messenger/web/ping payload to Inter-
com (URL-decoded, PII redacted).
user_data ={
" email ": "[ REDACTED ]" ,
" user_id ": " d34f1d9a -..." ,
" user_hash ": "5 df3adcd5f0d ..." ,
" name ": "[ REDACTED ]" ,
" company ": {
" company_id ": "3661535 f -..." ,
" name ": "[ REDACTED ]'s Org "
}
}
Listing 2: Character.ai Sentry session envelope trans-
mitted to sentry.io (PII redacted). The did field carries
the user’s email, and ip_address: "{{auto}}" instructs
Sentry to record the client IP from the connection.
{
" sid ":"2017 ad2c ..." ,
" status ":" exited " ,
" errors ":0 ,
" did ":"[ REDACTED ]" ,
" attrs ":{
" release ":" e86f7f ..." ,
9

Jazlan et al.
ChatOn
Mistral
Poe
OpenRouter
SeaArt
Duck.ai
Meta AI
Genspark
Manus
Qwen Chat
Kimi
PolyBuzz
Microsoft Copilot
Perplexity
Character.AI
DeepSeek
Grok
Claude
Gemini
ChatGPT
jsdelivr.net
unpkg.com
a3mspt.com
qq.com
stripe.network
stripe.com
seaart.me*
seaart.dev*
saconsole.com*
redditstatic.com
poecdn.net*
polyspeak.ai*
pinimg.com
payermax.com
profitwell.com
paddle.com
openai.com*
onetrust.com
cookielaw.org
auth0.com
moonshot.cn*
azure.com
virtualearth.net*
bingapis.com*
azure.com*
bing.net
fbcdn.net*
mapbox.com
intercomcdn.com
gstatic.com*
googleusercontent.com*
googleapis.com*
googleusercontent.com
run.app
gstatic.com
googleapis.com
google.com (Other)
duckduckgo.com*
cloudflareaccess.com
cloudflare.com
clerk.com
characterai.io*
cdn-go.cn
volccdn.com
manuscdn.com*
butterfly-effect.dev*
cdn-apple.com
anthropic.com*
cloudfront.net
amazonaws.com
alicdn.com*
akamaized.net
airwallex.com
aiby.mobi*
yandex.ru
rumt-sg.com
prodregistryv2.org
sprig.com
sentry.io
instajob.ai
plausible.io
clarity.ms
intercom.io
googletagmanager.com*
google-analytics.com*
google-analytics.com
google.com (Analytics)
googletagmanager.com
eppo.cloud
browser-intake-datadoghq.com
browser-intake-us5-datadoghq.com
dashfi.dev
cloudflareinsights.com
volces.com
amplitude.com
aliyuncs.com*
yandex.com
yimg.jp
yahoo.co.jp
twitter.com
t.co
ads-twitter.com
tiktokw.us
tiktok.com
tver.sale
tver.jp
smartnews-ads.com
singular.net
reddit.com
quora.com
pinterest.com
outbrain.com
pstatic.net
naver.net
naver.com
docomo.ne.jp
bing.com*
bing.com
facebook.net
facebook.com
adtrafficquality.google
googleadservices.com
google.com (Advertising)
googlesyndication.com
doubleclick.net
d2c.ne.jp
d2-apps.net
paa-reporting-advertising.amazon
amazon-adsystem.com
taobao.com*
alibaba.com*
a8.net
Categories
Advertising
Analytics
Other
Figure 3: Sankey diagram of data flow from chatbots to
all parties in normal chats. An asterisk indicates first-
or platform-party, while no asterisk means third-party.
" environment ":" production " ,
" ip_address ":"{{ auto }}" ,
" user_agent ":"[ REDACTED ]"
}
}
Listing 3: Character.ai Statsig event payload trans-
mitted to prodregistryv2.org/v1/rgstr (PII redacted).
Each event carries the user’s identity alongside the
experiment or feature-flag exposure being logged.
" user ":{
" userAgent ":"[ REDACTED ]" ,
" ip ":"[ REDACTED ]" ,
" custom ":{
" userAgeInYears ":24 ,
" ageCategory ":" AGE _CATEGOR Y_O18 " ,
} ,
" userID ":"[ REDACTED ]" ,
" email ":"[ REDACTED ]"
}
D Additional Traffic Flows
Qwen Chat
Perplexity
Grok
Claude
Gemini
ChatGPT
mapbox.com
google.com
gstatic.com*
gstatic.com
googleusercontent.com
googleapis.com
anthropic.com*
alicdn.com*
google-analytics.com*
google-analytics.com
browser-intake-datadoghq.com
browser-intake-us5-datadoghq.com
googlesyndication.com
taobao.com*
alibaba.com*
Categories
Advertising
Analytics
Other
Figure 2: Sankey diagram of data flow from chatbots
to all parties in temporary chats. An asterisk indicates
first- or platform-party, while no asterisk means third-
party.
10
