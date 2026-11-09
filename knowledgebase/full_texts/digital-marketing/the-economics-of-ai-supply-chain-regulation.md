---
title: The Economics of AI Supply Chain Regulation
url: https://arxiv.org/abs/2603.12630
category: digital-marketing
subcategory: empirical
date: 2026-03
venue: ''
authors:
- Sihan Qian
- Amit Mehra
- Dengpan Liu
source: arxiv
pdf_url: https://arxiv.org/pdf/2603.12630
pages: 41
chars: 125204
fetched_at: '2026-11-08T13:21:59+00:00'
kb_version: 1
---

# The Economics of AI Supply Chain Regulation

The Economics of AI Supply Chain Regulation*
Sihan Qian† Amit Mehra‡ Dengpan Liu§
December 17, 2025
Abstract
The rise of foundation models has driven the emergence of AI supply chains, where upstream
foundation model providers offer fine-tuning and inference services to downstream firms developing
domain-specific applications. Downstream firms pay providers to use their computing infrastructure
to fine-tune models with proprietary data, creating a co-creation dynamic that enhances model
quality. Amid concerns that foundation model providers and downstream firms may capture excessive
consumer surplus, along with increasing regulatory measures, this study employs a game-theoretic
model involving a provider and two competing downstream firms to analyze how policy interventions
affect consumer surplus in the AI supply chain. Our analysis shows that policies promoting price
competition in downstream markets (i.e.,pro–price–competitive policies) boost consumer surplus
only when compute or data preprocessing costs are high, while compute subsidies are effective only
when these costs are low, suggesting these policies complement each other. In contrast, policies
promoting quality competition in downstream markets (i.e.,pro–quality–competitive policies) always
improve consumer surplus. We also find that under pro–price–competitive policies or compute
subsidies, both the provider and downstream firms can achieve higher profits along with greater
consumer surplus, creating a win–win–win outcome. However, pro–quality–competitive policies
increase the provider’s profits while reducing those of downstream firms. Finally, as compute costs
decline, pro–price–competitive policies may lose their effectiveness, whereas compute subsidies may
shift from ineffective to effective. These findings offer insights for policymakers seeking to foster AI
supply chains that are economically efficient and socially beneficial.
Keywords:Artificial Intelligence; Foundation Model; Fine-tuning; Regulation; AI Supply Chain
∗ An earlier version of this paper, titled “The Economics of Fine-Tuning for Large-Scale AI Models,” was presented at WISE 2023,
where it won the Best Student Paper Award.
† School of Economics and Management, Tsinghua University. Email: qsh22@mails.tsinghua.edu.cn.
‡ Naveen Jindal School of Management, The University of Texas at Dallas. Email: amit.mehra@utdallas.edu.
§ School of Economics and Management, Tsinghua University. Email: liudp@sem.tsinghua.edu.cn.
1
arXiv:2603.12630v1  [econ.TH]  13 Mar 2026

1. Introduction
The rapid advancement of artificial intelligence (AI) is transforming economic sectors on an unprecedented
scale (Sun et al. 2025). The global AI market, valued at $638.23 billion in 2024, is projected to grow at a
compound annual growth rate (CAGR) of 19.2% to reach $3,680.47 billion by 2034 (Precedence Research
2025). However, this profound growth introduces significant risks to consumer welfare, including deceptive
claims about AI tools that lead consumers to make suboptimal purchasing decisions (FTC 2025b). This dual
nature of AI, as both a powerful productivity tool and a potential source of risk, highlights the urgent need
for effective regulatory oversight. However, applying traditional regulatory frameworks to AI is problematic
because the technology operates within a complex, multi-layered market structure, often conceptualized as
anAI supply chain(Cen et al. 2024a). This structure is characterized by a distinct upstream-downstream
dynamic: a small number of upstream providers develop large-scale AI models, also known asfoundation
models, which are then adapted and deployed by a broad downstream market of firms for specific applications.
The inherent interdependence of this structure renders existing regulatory frameworks inadequate, inevitably
leading to substantial oversight gaps (Cen et al. 2024b). Therefore, safeguarding consumers and ensuring
market efficiency necessitate a holistic regulatory approach tailored to address the unique interdependencies
of the AI supply chain.
1.1. Foundation Models
To develop a holistic regulatory approach to the AI supply chain, it is essential to first gain a comprehensive
understanding of its most fundamental component: the upstream segment, where developers create founda-
tion models. These models, built with billions of parameters and trained on massive datasets, exhibit remark-
able capabilities in tasks such as logical reasoning and natural language processing (Vohra 2024). Often
hailed as a cornerstone of the next industrial revolution (Menear 2024), foundation models have driven major
technology companies, including Microsoft, Amazon, and Google, to make substantial investments to secure
dominance in the upstream market, with Google alone reportedly committing over $100 billion (Bhati 2024).
Despite their impressive general-purpose performance, foundation models often fall short in specialized
domains such as healthcare and law. These limitations stem primarily from the restricted access to domain-
specific data, which is often highly confidential(Chen et al. 2026). Yet, organizations in these sectors, which
have access to such data, generally lack the resources to develop foundation models independently due to the
prohibitively high costs involved. These costs include not only massive computational resources, but also
specialized technical expertise. For example, training a model at the scale of GPT-4 is estimated to cost over
$100 million, making in-house development infeasible for most organizations (Wikipedia 2023).
1.2. Fine-tuning
To tackle these challenges, a co-creation process has emerged within a comprehensive AI ecosystem, bring-
ing together upstream foundation model providers and downstream firms. As shown in Figure 1, adapting a
2

Figure 1 Creation of a fine-tuned model
Preprocessed
Domain-specific Data
by Downstream Firms
Pretrain
Foundation Model
Fine-tuned Model
Fine-tune
General-purpose Data
by Foundation Model Provider
model for downstream applications typically requires two key training stages. The first stage is pretraining,
which involves building a foundation model using general-purpose data (Stryker 2025). Pretraining is
primarily conducted by leading technology companies such as Google and OpenAI (Singh 2024).
The second stage, known as fine-tuning, is typically performed by downstream firms and consists of two
critical steps. The first step is preprocessing domain-specific data to remove noise, errors, and inconsis-
tencies1 (Huizenga 2025). Once the data is cleaned, it is used to retrain the foundation model, yielding a
fine-tuned version tailored to specific downstream applications. Unlike the resource-intensive pretraining
phase, fine-tuning requires significantly less computational power, making it a feasible option for most firms
(Competition and Markets Authority 2023). This reduced computational cost enables smaller companies to
take advantage of the models developed by large technology companies and adapt them to their special-
ized needs (AI Now Institute 2023). Fine-tuning is widely regarded as essential for embedding complex
domain-specific behavioral patterns in AI models (OpenAI 2023). Supporting this, a 2024 report by Pricewa-
terhouseCoopers (PwC) finds that organizations using fine-tuned models experienced a 37% increase in the
accuracy of AI-generated content (ITSoli 2025). The same report predicts that by 2030, 90% of companies
will have deployed at least one fine-tuned large language model.
To protect the proprietary nature of the foundation model’s parameters, model providers do not share the
models directly with downstream firms. Instead, firms are required to upload clean, domain-specific data,
which is obtained by preprocessing their datasets, a process that incurs what are known asdata preprocessing
costs, to the provider’s infrastructure for fine-tuning. Given that fine-tuning requires significant computational
resources, providers also facecompute costs. In exchange, they charge afine-tuning fee, typically based on the
volume of preprocessed data firms use on the provider’s infrastructure. Once the model has been fine-tuned,
it is hosted on the provider’s infrastructure, and firms are charged aninference fee, usually based on the
1 For example, the fine-tuning for CoCounsel was based on a curated dataset of approximately 30,000 legal
questions, refined over six months by a multidisciplinary team of lawyers, domain experts, and AI engineers
(Kardach 2024).
3

Figure 2 Example of an AI supply Chain
Fine-tune
Harvey’s
domain data
Thomson’s
domain data
Fine-tuned Model
of Harvey
Fine-tuned Model
of Thomson
Foundation Model
Legal AI assistant
of Harvey
Legal AI assistant
of Thomson
Sale to end users
volume of usage data (both input and output), to access the model for downstream applications (OpenAI
2024b). In this way, foundation model providers generate two primary revenue streams: one from fine-tuning
fees and the other from inference fees.
1.3. The AI Supply Chain
The central role of fine-tuning in AI development has led to the emergence of the AI Supply Chain (Cen et al.
2024a), where foundation model providers offer general-purpose models that downstream firms fine-tune
for specialized applications and subsequently market to end users. A real-world example of this AI supply
chain is illustrated in Figure 2. For instance, law firms such as Harvey and Thomson Reuters are the leading
players in developing AI-powered legal assistants (Fisher 2024). Both firms fine-tune OpenAI foundation
models using their proprietary legal data (OpenAI 2024a, Reuters 2024). Using these fine-tuned models,
they have created and commercialized advanced AI legal assistants that help attorneys with tasks such as
drafting legal documents and managing complex litigation (OpenAI 2024a).
This novel form of supply chain has several distinctive characteristics. First, the foundation models are fine-
tuned through a co-creation process involving both the foundation model provider and the downstream firm.
This approach to product development contrasts sharply with traditional supply chains, where manufacturers
typically handle all aspects of product design and development. Even in collaborative supply chains, such
as those that involve vendor–client partnerships for enterprise systems such as ERP (Demirezen et al.
2020, Gupta et al. 2023), the co-creation process typically occurs independently between vendors and
clients. In contrast, the fine-tuning of foundation models entails a mutually dependent form of co-creation:
upstream providers supply not only the base foundation models but also the computational infrastructure
necessary for fine-tuning, while downstream firms contribute domain-specific data and expertise to adapt
these models for specialized applications. Second, the provision of computational resources for fine-tuning
creates a revenue stream for foundation model providers during the co-creation process, which represents a
unique form of revenue generation compared to traditional settings, where manufacturers generate revenue
4

only through wholesale prices. Third, the fine-tuned models are customized versions of foundation models
deployed through a Software-as-a-Service (SaaS) framework. Traditionally, software customization occurs
in on-premise settings, where clients adapt the software locally; in such cases, SaaS-style pricing models
are typically not applied. Hence, the integration of extensive customization with a SaaS deployment model
constitutes a distinctive feature of our context.
1.4. Motivation and Research Questions
The rapid diffusion of AI-enabled products has introduced substantial risks to consumer welfare, particularly
by shifting power from consumers to firms. As Nobel laureate Daron Acemoglu cautions, the use of AI tech-
nologies and data increases companies’ power over consumers, with important distributional implications
that enable AI-intensive companies to capture a larger share of consumer surplus (Acemoglu 2021).
These concerns are compounded by the fact that AI-enabled products introduce fundamentally new types
of services for consumers (e.g., AI-based legal assistants), yet assessing their quality remains inherently
difficult (Ngo 2025). For example, consumers cannot easily anticipate the extent of hallucinations, which
can significantly undermine the reliability of the output. Legal experts caution that AI systems remain
susceptible to errors, biases, and malfunctions, requiring professionals to be aware of their limitations
(Eldridge 2025). More concerningly, some companies have exploited the hype around AI, exaggerating the
capabilities of their products and further complicating consumers’ ability to assess quality. For example,
DoNotPay marketed itself as the “world’s first robot lawyer,” falsely claiming that it could replace human
legal expertise, only to fall short of those promises (FTC 2025b). This lack of quality transparency enables
downstream firms to soften competition, potentially leading to subpar offerings and a decline in consumer
welfare. In a similar vein, challenges also arise in pricing: Opaque and highly differentiated pricing schemes
hinder straightforward comparisons. As Dreyer (2025) notes, reduced comparability undermines competitive
pressure and tends to drive prices higher.
Given these issues, a natural regulatory response to AI supply chains is to implement pro-competitive
policies that strengthen price or quality competition in downstream markets (Austrian Federal Competition
Authority 2024). Such approaches have already been successfully applied in the broader digital economy.
For instance, to promote price competition, the U.S. Federal Trade Commission (FTC) required Ticketmaster
to display the full ticket price upfront during the purchase process, thereby improving price transparency
(Boggs 2025). Similarly, in a quality competition context, the FTC alleged that Fashion Nova, a U.S.-based
online fast-fashion retailer, misled consumers by suppressing negative reviews, underscoring the importance
of truthful product quality disclosure (FTC 2025c). Crucially, some of these established regulatory tools have
already been adapted to AI-enabled product markets. For example, the FTC has begun to require companies
to refrain from making misleading claims about the capabilities of consumer-facing AI products (Hrdy et al.
2025, Leblanc et al. 2025). Ultimately, these measures contribute to a broader competition policy framework
by limiting misleading practices that distort consumer choice and weaken competitive pressures (FTC 2025).
5

Another regulatory strategy targets upstream foundation model providers in the AI supply chain, aiming
to enhance consumer surplus by subsidizing the fine-tuning process and incentivizing the development of
higher-quality products and services in downstream markets. A notable example is the annual commitment
by the Beijing Municipal Government of 100 million RMB in computing power subsidies to firms
engaged in large-scale AI model services (Wu 2024). Similar programs have been introduced by municipal
governments in Shenzhen, Shanghai, Chengdu, and several other Chinese cities. By offsetting a significant
portion of the compute costs for fine-tuning, these subsidies help lower barriers to producing higher-quality
AI-enabled offerings.
However, the implications of such regulatory measures in the AI supply chain are not straightforward
and may differ from those seen in traditional supply chain models, due to the unique co-creation dynamics
inherent in this intricate ecosystem. In conventional supply chains, pro-competitive policies that lower retail
prices typically increase consumer surplus without diminishing the manufacturer’s incentive to maintain
product quality. In contrast, in the AI supply chain context, a reduction in downstream prices can erode
downstream firms’ marginal returns, diminishing their incentives to invest in fine-tuning and ultimately
lowering overall product quality. This interdependence between pricing, incentives, and quality gives rise to
a welfare trade-off absent in conventional market structures.
This trade-off highlights the need to evaluate not only whether regulatory interventions enhance consumer
welfare but also the mechanisms through which they operate and the conditions under which they may inad-
vertently discourage quality investment. Understanding these mechanisms is essential because the welfare
implications of a policy depend on how it shapes firms’ incentives: Measures that appear pro-competitive
can, under certain conditions, diminish firms’ incentives to invest in quality, ultimately undermining overall
welfare. Recent debates on AI regulation reveal growing gaps in adapting existing regulatory frameworks to
complex AI supply chains, underscoring the importance of understanding how different policy instruments
perform in such environments (Cen et al. 2024b). These considerations motivate our central research ques-
tions:How do regulatory approaches that promote competition in downstream markets or provide compute
subsidies impact consumer surplus within the AI supply chain, and which policy instrument proves most
effective under varying conditions?Addressing these questions is crucial to ensure that regulatory efforts
ultimately promote, rather than compromise, welfare in AI-enabled markets.
The success of any regulatory policy ultimately depends on its acceptance by industry participants.
Therefore, it is crucial to understand how pro-competitive policies and compute subsidies impact the
profitability of both foundation model providers and downstream firms. Policies that increase consumer
surplus while simultaneously improving the profitability of providers and downstream firms are more likely
to be adopted, as they create a “win–win–win” outcome in which all stakeholders benefit. Conventional
wisdom suggests that increased competition erodes downstream firms’ market power, thereby reducing their
profitability (Matsushima 2006). However, Tyagi (1999) provides an alternative view, showing that increased
6

downstream rivalry can induce price adjustments by upstream providers, thereby easing competitive pressures
among downstream firms and mitigating the need for aggressive pricing. This suggests that the relationship
between downstream competition and firm profitability is theoretically ambiguous. In AI supply chains,
where downstream firms co-create value through fine-tuning, the dynamics are likely even more complex.
Furthermore, strategic interactions between upstream providers and downstream firms make the effects of
compute subsidies on their profitability uncertain, as changes in incentives from one party can influence
the other party’s strategic responses. To address these uncertainties, we pose our second research question:
How do pro-competitive policies and compute subsidies influence the profitability of both foundation model
providers and downstream firms within the AI supply chain?
While evaluating the immediate effects of regulatory policies is important, it is equally crucial to recognize
how these policies must evolve over time to respond to the shifting dynamics of AI markets. This also
represents a key practical challenge for policymakers due to the rapid and continuous evolution of AI
technologies (Competition Bureau Canada 2025). A key driver of these changes is the steady decline in
compute costs, largely driven by advancements in graphics processing units (GPUs), which play a crucial
role in fine-tuning AI models (NVIDIA 2024, Diehl 2025). Lower compute costs enable providers to reduce
fine-tuning prices, benefiting downstream firms. However, prior research suggests that falling IT costs can
intensify competition over product quality, potentially eroding downstream profitability (Demirhan et al.
2005). Consequently, the overall impact of declining compute costs on downstream profitability remains
uncertain. In AI supply chains, where downstream firms co-create value through fine-tuning, these dynamics
may further influence incentives to invest in quality and, ultimately, consumer surplus. This raises important
policy considerations: Regulatory interventions that are effective under current compute cost structures may
need to be adjusted as costs decline in order to maintain their intended effects on consumer surplus and firm
incentives. To examine the implications of declining compute costs, we pose our third research question:
How do declining compute costs impact consumer surplus and the profitability of both foundation model
providers and downstream firms within the AI supply chain, and how should regulatory policies evolve to
ensure welfare-enhancing outcomes?
1.5. Key Findings
To address these research questions, we develop a game-theoretic model in which a foundation model
provider offers both fine-tuning and inference services to two competing downstream firms. These firms,
in turn, leverage these services to develop and sell AI-powered products to consumers. Our analysis yields
several key insights. First, we show that neither policies promoting price competition in downstream AI
markets nor compute subsidies always effectively enhance consumer welfare. Nevertheless, these two policy
strategies are complementary, and their effectiveness depends on the underlying cost conditions, which relate
to both the foundation model provider’s compute costs and downstream firms’ data preprocessing costs,
7

reflecting the co-creation nature of the AI supply chain. Specifically, policies that promote price competition
in downstream AI markets are effective only when compute or data preprocessing costs are relatively high,
whereas compute subsidies are effective only when these costs are relatively low. In contrast, policies that
promote quality competition in downstream AI markets always enhance consumer welfare, making it a
robust and broadly effective regulatory approach.
Second, contrary to conventional wisdom, we find that policies that promote price competition among
downstream firms can increase their profits while reducing the foundation model provider’s profits. More-
over, both policies promoting price competition and compute subsidies can, in some cases, generate a
“win–win–win” outcome in which all stakeholders benefit. In contrast, policies promoting quality competi-
tion consistently reduce downstream firms’ profits while increasing the provider’s profits, offering no such
“win–win–win” potential.
Third, as GPU technology advances and compute costs decline over time, both the consumer surplus and
provider profits increase, but downstream firms’ profits may decrease. Furthermore, declining compute costs
alter the effectiveness of policy interventions. Policies promoting price competition may shift from effective
to ineffective, while compute subsidies may transition from ineffective to effective. In contrast, policies that
promote quality competition remain consistently effective.
The remainder of this paper is organized as follows. Section 2 reviews the relevant literature and situates
our work within existing research. Section 3 presents the modeling framework underlying our analysis,
while Section 4 develops formal models to examine the optimal decision-making processes of both the
foundation model provider and the downstream firms. Section 5 evaluates the effectiveness of various
regulatory interventions in AI markets, and Section 6 examines the impact of pro-competitive policies and
compute subsidies on the profitability of key stakeholders. Section 7 explores how declining compute costs
influence stakeholder profitability, consumer surplus, and the effectiveness of these regulatory policies.
Finally, Section 8 concludes with a discussion of theoretical contributions and managerial implications.
2. Literature Review
Our study relates primarily to three streams of literature: (i) AI Regulation, (ii) Software as a Service
(SaaS), and (iii) Implications of Declining Information Technology (IT) Costs. Below, we briefly review the
relevant literature and highlight our contributions to each stream, with Figure 3 summarizing these works
and illustrating the positioning of our study.
2.1. AI Regulation
Our paper contributes to the recently emerging literature on the regulation of AI. Prior work has analyzed
the risks posed by AI, highlighting the urgent need for regulatory oversight. For example, Acemoglu
(2021) highlights the broad social and economic harms associated with AI, while Cajueiro and Celestino
(2025) offer a comprehensive review of the challenges involved in the governance of rapidly evolving AI
8

technologies. Empirically, Assad et al. (2024) demonstrate that algorithmic pricing can facilitate collusion
and weaken competition, underscoring regulators’ concerns about the widespread adoption of AI-powered
pricing tools. Another stream of literature proposes or examines specific regulatory approaches. Mahari and
Pentland (2024) introduce a Regulation-by-Design paradigm, which integrates regulatory objectives directly
into AI system architectures. Other studies investigate the unintended effects of particular interventions
(Vijairaghavan et al. 2025). For example, Mohammadi et al. (2024) find that policies designed to improve AI
explainability can unintentionally worsen outcomes for both consumers and firms, while Wang et al. (2023)
show that policies requiring full transparency of AI algorithms can inadvertently harm end users.
Unlike these studies, we examine two regulatory approaches that have not yet been analyzed in the AI
context, namely pro-competitive policies and compute subsidies. More importantly, we incorporate the
multi-layer structure of the AI market, specifically the AI supply chain, a factor that can significantly influence
policy effectiveness (Cen et al. 2024b) but has been largely neglected in the literature. By modeling the
strategic interactions between upstream foundation model providers and downstream firms, our study offers
a systematic framework for evaluating the implications of regulatory policies in the AI supply chain.
2.2. SaaS
Because fine-tuning and inference services can be viewed as forms of SaaS for AI (Design Gurus 2025),
our study is closely related to the literature on SaaS (Yang et al. 2021, Sun et al. 2023, Jiang et al. 2019).
Competition among IT resource vendors has been extensively studied in this context. For example, Kim
et al. (2009) examine quality competition between SaaS vendors and show that risk-sharing contracts can
incentivize vendors to improve product quality. Ma and Kauffman (2014) investigate both price and quality
competition, finding that high client switching costs can ultimately drive a vendor out of the market.
Similarly, Guo and Ma (2018) and Zhang et al. (2020) analyze the competitive dynamics between perpetual
software vendors and SaaS providers, highlighting how factors such as quality improvement rates and
network effects shape SaaS competitiveness. While this body of work provides valuable insights into vendor-
side competition, it largely overlooks the competitive dynamics among downstream firms that use SaaS
products. In particular, little attention has been paid to how competition among downstream users shapes
SaaS vendors’ pricing strategies. Our study addresses this gap by examining the interplay between vendor
pricing (specifically, by foundation model providers) and downstream market competition. In doing so, we
contribute novel insights into how the structure of downstream markets can influence upstream pricing
decisions, with implications for both market participants and policymakers.
Prior research has primarily focused on customizable software services (Ma and Seidmann 2015, Zhang
et al. 2020), with a particular emphasis on modifiable off-the-shelf (MOTS) products. These solutions are
typically installed on-premises and offered at fixed prices, rather than through usage-based or on-demand
billing, which is a distinctive characteristic of SaaS. In contrast, traditional SaaS models offer limited
9

Figure 3 Relevant Literature and the Positioning of Our Study
The Economics of
Regulation for the
AI Supply Chain
SaaS
Competition among
SaaS vendors
(Kim et al. 2009, Guo and Ma
2018)
Relevant literature Our study
Impact of SaaS users'
competition on consumer welfare
and stakeholder profits
considering a customizable SaaS
(Propositions 1, 3)
Implications of Declining IT
Costs
AI Regulation
Declining IT Costs
in horizontal markets
(Demirhan et al. 2005, 2007)
Examining the effects of
declining IT costs in the vertical
market structure of the AI
supply chain
(Proposition 4)
Limited customization of SaaS
(Ma and Seidmann 2015, Zhang
et al. 2020)
Explainability of AI systems
(Mohammadi et al. 2024) Effectiveness of two AI-market regulatory approaches that differ
from those examined in prior
work, within the distinctive
context of the AI supply chain
(Propositions 1, 2)Algorithm Transparency
(Wang et al. 2023)
customization because multiple customers share a single software instance, thereby restricting access to
source code modifications (Sun et al. 2008, Muller et al. 2009, Ma and Kauffman 2014, Guo 2009, Ma and
Seidmann 2015, Zhang et al. 2020). While SaaS platforms often include configuration options, these are
generally insufficient to accommodate advanced or domain-specific customization needs (Schneier 2015,
Zhang et al. 2020, Karanika 2013). The emergence of large-scale AI models introduces a fundamental shift in
the nature of service customization. Through fine-tuning, firms can retrain foundation models on proprietary
data, enabling parameter adjustments without requiring access to or modification of the underlying source
code. This capability fosters a new form of co-creation, wherein service quality reflects both the capabilities
of the vendor’s foundation model and the unique data contributed by downstream firms. This interdependence
gives rise to strategic dynamics that diverge significantly from those observed in traditional SaaS settings.
Despite these shifts, the strategic implications of customizable SaaS remain underexplored in the existing
literature. Our study addresses this gap by examining the evolving interactions between SaaS vendors (i.e.,
foundation model providers in our context) and downstream firms within this emerging paradigm.
2.3. Implications of Declining IT Costs
Given the continued decline in the costs of AI computing, our paper also contributes to the broader literature
on declining IT costs. Prior research in this area has primarily focused on the implications of declining IT
costs for firm profitability in competitive, consumer-oriented markets. For example, Demirhan et al. (2005,
2007) examine strategic IT investments and show that whether firms can benefit from declining IT costs
depends on factors such as price sensitivity and user switching costs. Similarly, Bohlmann et al. (2002)
analyze the sequential entry of firms into downstream markets and empirically show that the negative effect
of declining IT costs on the profit of the pioneer is more pronounced in product categories where quality is
a key differentiator.
10

In contrast to prior work, our study examines the effects of declining IT costs within a vertical market
structure, specifically the AI supply chain that includes upstream providers, downstream firms, and end
consumers. While earlier research has primarily focused on horizontal market settings, where interactions
occur only between downstream firms and consumers, our model captures the strategic implications of
vertical interactions throughout the supply chain. Moreover, while prior studies typically attribute IT costs
to downstream firms, our analysis highlights the strategic impact of declining compute costs incurred by
upstream providers.
3. Modeling Framework
We analyze a market scenario involving a foundation model provider (hereafter referred to as theprovider)
and two competing downstream firms (denoted byfirm𝑖, where𝑖∈{1,2}). To ground the analysis in a real-
world example, consider law firms such as Harvey and Thomson Reuters, which are prominent competitors
in the provision of AI-powered legal assistants (Fisher 2024). Both firms have fine-tuned OpenAI’s GPT
model to develop legal assistants. This fine-tuning process enables legal assistants to deliver highly relevant
and accurate results, thereby enhancing service quality and contributing significantly to firm profitability
(OpenAI 2024a). Such scenarios, where competing firms rely on the same foundation model provider, are
increasingly common in practice (Shaver 2025).
Next, we define the profit functions for each stakeholder and outline the game’s sequence.
3.1. Foundation model provider
To help firms leverage the foundation model, the provider offers two key services: fine-tuning and inference.
Both services are essential for firms to deliver AI-powered products, such as AI-driven legal assistants, to
end users, including individuals and enterprises.
In the fine-tuning process, firms supply domain-specific data to the provider, who utilizes its computing
infrastructure to adapt the foundation model, thereby enhancing its domain-specific performance. According
to OpenAI (2023), the performance of a fine-tuned model improves with the volume of data provided. To
quantify this relationship, we define adata unitas the amount of data required to enhance the quality of model
by one unit (e.g., 1,000 tokens 2). Additionally, we definedata volumeas the volume of data used for fine-
tuning, denoted by𝑉𝑖. Hence, if firm𝑖provides𝑉 𝑖 data units for fine-tuning, the corresponding improvement
in model quality is𝑉 𝑖. Therefore, the quality of the fine-tuned model can be represented as𝑞 𝑖=𝛼+𝑉 𝑖,
where𝛼denotes the base quality of the foundation model. Since fine-tuning is performed on the provider’s
computing infrastructure, it incurs rising computational costs as the volume of training data increases. These
costs are modeled using the quadratic expression𝑐 𝐹𝑉 2 𝑖 , where𝑐 𝐹 is the cost coefficient associated with
2 Tokens refer to words, character sets, or combinations of words and punctuation input or generated by large
language models (LLMs).
11

fine-tuning. The convex cost structure arises because the fine-tuning of large-scale AI models depends on
distributed computing architectures (Yanbc 2024, Insights 2024). As the volume of data increases, additional
GPU nodes are required, thereby increasing communication overhead between GPUs. This, in turn, creates
computational bottlenecks that reduce GPU efficiency and cause costs to grow non-linearly (Narayanan et al.
2021, Zhao et al. 2021). To provide fine-tuning services, the provider sets a per-unit price of𝑝𝐹 for the data
used in this process. For example, OpenAI charges $6 per million tokens to fine-tune its Davinci model,
which is part of the GPT series (OpenAI 2024b). Consequently, firm𝑖pays a total of𝑝 𝐹𝑉𝑖 to the provider.
The fine-tuned model is deployed and hosted on the provider’s computing infrastructure. To access the
model, firms utilize the provider’s inference service. During inference, firms submit queries to the fine-
tuned model, which processes the input, generates responses, and returns the results. The provider typically
charges firms on a pay-per-use basis for inference, with a price of𝑝𝐼 per unit of data usage, which includes
both the input data and the output generated by the model. For example, OpenAI charges $12 per million
tokens for inference on its Davinci model (OpenAI 2024b). Since downstream firms develop AI-powered
products based on the fine-tuned model, each consumer interaction with the product triggers a request for the
inference service. For example, each query submitted by a lawyer to an AI-powered legal assistant invokes
the fine-tuned model to generate a response, thereby incurring inference usage. For simplicity, we assume
that answering a consumer’s query requires one unit of data usage for inference. Therefore, the total data
usage for inference is equal to the consumer demand, denoted by𝑑 𝑖. Consequently, firm𝑖pays𝑝 𝐼𝑑𝑖 to the
provider for inference services.
The objective of the foundation model provider is to maximize total profits by strategically setting prices
for both fine-tuning and inference services. The provider’s profit function is given by:
𝜋𝑀=
2∑︁
𝑖=1

𝑝𝐼𝑑𝑖+𝑝 𝐹𝑉𝑖−𝑐𝐹𝑉 2 𝑖

.(1)
In this expression, the first term (𝑝 𝐼𝑑𝑖) represents revenue generated from the inference service, where𝑑 𝑖
denotes the inference demand for firm𝑖. The second term (𝑝 𝐹𝑉𝑖) corresponds to revenue from fine-tuning
services, while the third term (𝑐𝐹𝑉 2 𝑖 ) captures the computational costs associated with fine-tuning.
3.2. Firms
Firms must preprocess their domain-specific data to address potential problems in raw data and ensure
its suitability for fine-tuning (Huizenga 2025). For example, de-duplication, one of the key preprocessing
steps, involves identifying and removing duplicate data points (Huizenga 2025). Although essential, data
preprocessing represents a significant burden for firms. For instance, Thomson Reuters reportedly invested
4,000 hours of effort from a multidisciplinary team of lawyers, domain experts, and AI engineers to curate and
refine 30,000 legal questions for fine-tuning (Kardach 2024). The workload associated with preprocessing
increases with the volume of data used for fine-tuning (𝑉 𝑖), as larger preprocessed datasets require more
12

Figure 4 Model Timeline
Pricing by the Foundation
Model Provider
The provider decides (𝑝𝐹, 𝑝𝐼).
Data Preprocessing and
Model Fine-tuning
Firms 1and 2 decide (𝑉1, 𝑉2).
Product Pricing by
Downstream Firms
Firms 1and 2 decide ( 𝑝1, 𝑝2).
Demand Realization
by Consumers
Stage 0 Stage 1 Stage 2 Stage 3
raw data and greater processing complexity. For example, the de-duplication process involves pairwise
comparisons and thus exhibits quadratic computational complexity with respect to the dataset size (Munappy
et al. 2022). Accordingly, we model the cost of data preprocessing as𝑐𝑉𝑉 2 𝑖 .
To model price and quality competition in the downstream market, we build on prior research (Tsay and
Agrawal 2000, Banker et al. 1998) by assuming that aggregate consumer demand is linearly influenced by
both price and product quality. We further assume that the quality of an AI-powered product corresponds to
the quality of the fine-tuned model, denoted by𝑞𝑖. Specifically, consumer demand for firm𝑖is given by:
𝑑𝑖=1−𝑝 𝑖−𝜃 𝑝(𝑝𝑖−𝑝 𝑗)+𝑞 𝑖+𝜃𝑞(𝑞𝑖−𝑞 𝑗),
where𝑖,𝑗∈{1,2}and𝑖≠𝑗. Under this formulation, lowering a firm’s price or improving its product quality
increases its own demand while reducing that of its competitor,ceteris paribus. The parameters𝜃 𝑝>0and
𝜃𝑞>0capture the intensity of price and quality competition in the consumer market, respectively. As firms
generate revenue (𝑝𝑖𝑑𝑖) by selling AI-powered products to consumers, they simultaneously incur inference
costs (𝑝𝐼𝑑𝑖) paid to the provider when consumers interact with the underlying model.
Accordingly, the profit of firm𝑖equals its sales revenue minus the costs of inference, fine-tuning, and data
preprocessing. The resulting profit function for firm𝑖is given by:
𝜋𝑖=(𝑝 𝑖−𝑝 𝐼)𝑑𝑖−𝑝 𝐹𝑉𝑖−𝑐𝑉𝑉 2 𝑖.(2)
3.3. Model Timeline
The game unfolds in four stages, as illustrated in Figure 4, which depicts the interactions among the key
stakeholders, namely the foundation model provider, downstream firms, and consumers. In Stage 0, the
provider sets the fine-tuning price (𝑝 𝐹) and the inference price (𝑝 𝐼), both of which are observable to the
firms. In Stage 1, Firms 1 and 2 simultaneously choose their respective data volumes for fine-tuning (𝑉 𝑖,
where𝑖∈{1,2}), preprocess their domain-specific data, and fine-tune the foundation model accordingly.
Once fine-tuning is complete, the firms develop AI-powered products based on the fine-tuned model,
resulting in product quality denoted by𝑞 𝑖. In Stage 2, after observing each other’s product quality, the
13

firms simultaneously set their product prices (𝑝𝑖) and offer their AI-powered products to consumers. Finally,
in Stage 3, consumer demand is realized. This sequential structure, in which quality decisions precede
pricing, aligns with established models of quality and price competition in the literature (Banker et al.
1998, Demirhan et al. 2005). The underlying rationale is that quality decisions are typically more difficult
to modify than pricing decisions; thus, firms often determine product quality before setting prices (Banker
et al. 1998, Demirhan et al. 2005).
4. Equilibrium Analysis
In this section, we employ backward induction to derive the subgame-perfect Nash equilibrium (SPNE) for
the players’ actions at each stage of the game, highlighting our key findings. Following the sequence outlined
in Figure 4, we first determine the product prices and data volumes chosen by the downstream firms, based
on the fine-tuning and inference pricing decisions made by the foundation model provider. We then analyze
the provider’s equilibrium choices with respect to these upstream decisions.
4.1. Downstream Firms’ Decisions
In this subsection, we focus on the subgame starting at Stage 1, where the provider’s inference price (𝑝 𝐼)
and fine-tuning price (𝑝 𝐹) are treated as given. Using backward induction, we begin our analysis at Stage
2, where downstream firms determine their product prices to maximize their respective profit functions, as
specified in Equation (2). In this stage, firms take as given the realized product qualities, along with the
previously set prices for fine-tuning and inference. We then proceed to derive the best-response function of
firm𝑖for Stage 2 as:
𝑝𝑖(𝑉𝑖,𝑉𝑗,𝑝 𝐼)= 𝑝𝐼(1+𝜃 𝑝)(2+3𝜃 𝑝)+2(1+𝛼+𝑉 𝑖+𝜃𝑞(𝑉𝑖−𝑉𝑗))+𝜃 𝑝(3+3𝛼+2𝑉 𝑖+𝑉𝑗+𝜃𝑞(𝑉𝑖−𝑉𝑗)) (2+𝜃 𝑝)(2+3𝜃 𝑝) ,
(3)
where𝑖≠𝑗∈{1,2}.
By substituting the above expressions for prices into the firms’ profit functions from Equation (2), we
derive the firms’ profits in Stage 1. In this stage, each firm selects its data volume (𝑉 𝑖) for fine-tuning to
maximize its profit. Solving the first-order condition yields the SPNE data volume for firm𝑖(denoted as
𝑉𝑖(𝑝𝐹,𝑝 𝐼)).3 The corresponding product prices (𝑝𝑖(𝑝𝐹,𝑝 𝐼)) can be obtained by substituting𝑉𝑖(𝑝𝐹,𝑝 𝐼)into
Equation (3). The following lemma summarizes the firms’ equilibrium decisions in this subgame at Stage 1.
3 For a pure strategy equilibrium to exist, the reaction functions of the two firms must intersect exactly once.
To ensure this condition, we impose the following assumption:|𝜕2𝜋1
𝜕𝑉12|≥| 𝜕2𝜋1 𝜕𝑉1𝜕𝑉2 |(Tirole 1988, Banker et al.
1998, Demirhan et al. 2005).
14

LEMMA1(Equilibrium Decisions of the Firms in the Subgame).Given the inference price𝑝 𝐼 and
fine-tuning price𝑝 𝐹 set by the foundation model provider, the equilibrium data volumes and product prices
for Firm𝑖(𝑖∈{1,2}) in the subgame at Stage 1 are as follows:
𝑉𝑖(𝑝𝐼,𝑝 𝐹)= 2(1+𝜃 𝑝)(1+𝛼−𝑝 𝐼)(2(1+𝜃 𝑞)+𝜃 𝑝(2+𝜃 𝑞))−(2+𝜃 𝑝)2(2+3𝜃 𝑝)𝑝𝐹 2𝑐𝑉(2+𝜃 𝑝)2(2+3𝜃 𝑝)−2(1+𝜃 𝑝)(2(1+𝜃 𝑞)+𝜃 𝑝(2+𝜃 𝑞)) ,(4)
𝑝𝑖(𝑝𝐼,𝑝 𝐹)=
2𝑐𝑉(2+𝜃 𝑝)(2+3𝜃 𝑝)(1+𝛼)+2𝑝 𝐼(1+𝜃 𝑝)(𝑐𝑉(2+𝜃 𝑝)(2+3𝜃 𝑝)
−𝜃𝑝𝜃𝑞−2(1+𝜃 𝑝+𝜃𝑞))−(2+𝜃 𝑝)(2+3𝜃 𝑝)𝑝𝐹
2𝑐𝑉(2+𝜃 𝑝)2(2+3𝜃 𝑝)−2(1+𝜃 𝑝)(2(1+𝜃 𝑞)+𝜃 𝑝(2+𝜃 𝑞)) .(5)
Accordingly, we can rewrite Firm𝑖’s profit function by substituting the above prices and data volumes
into Equation (2), yielding the following expression:
𝜋𝑖= 𝑝𝑖(𝑝𝐼,𝑝 𝐹)−𝑝 𝐼  1+𝛼+𝑉 𝑖(𝑝𝐼,𝑝 𝐹)−𝑝 𝑖(𝑝𝐼,𝑝 𝐹)−𝑝 𝐹𝑉𝑖(𝑝𝐼,𝑝 𝐹)−𝑐 𝑉𝑉 2 𝑖(𝑝𝐼,𝑝 𝐹)(6)
As established in Lemma 1, the equilibrium data volumes and product prices in the subgame are influenced
by the intensity of the downstream competition, captured by the parameters𝜃 𝑝 (price competition) and𝜃 𝑞
(quality competition). Specifically, an increase in price competition leads to reductions in both data volumes
and product prices (i.e., 𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑝 <0, 𝜕𝑝𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑝 <0). In contrast, an increase in quality competition
results in higher data volumes and product prices (i.e., 𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑞 >0, 𝜕𝑝𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑞 >0). The underlying
mechanism is as follows: As price competition intensifies, firms are prompted to lower their product prices
(i.e., 𝜕𝑝𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑝 <0), thereby diminishing the marginal returns to quality improvements through increased
consumer demand. Consequently, firms decrease the volume of data used for fine-tuning (i.e.,𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑝 <0).
In contrast, heightened quality competition incentivizes firms to enhance product quality by increasing data
volumes for fine-tuning (i.e.,𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑞 >0). This improvement in quality enables firms to command higher
prices (i.e., 𝜕𝑝𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑞 >0), since consumers are willing to pay a premium for the superior quality of the
product resulting from more extensive data use. We now proceed to examine the provider’s decision-making
in Stage 0.
4.2. Foundation Model Provider’s Decisions
In this subsection, we analyze the the foundation model provider’s equilibrium pricing decisions. To this
end, we substitute SPNE prices and data volumes into the provider’s profit function, as specified in Equation
(1). This allows us to rewrite the provider’s profit function as:
𝜋𝑀=
2∑︁
𝑖=1

𝑝𝐼𝑑𝑖(𝑝𝐼,𝑝 𝐹)+𝑝 𝐹𝑉𝑖(𝑝𝐼,𝑝 𝐹)−𝑐 𝐹𝑉 2 𝑖(𝑝𝐼,𝑝 𝐹)  ,(7)
where𝑑 𝑖(𝑝𝐼,𝑝 𝐹)=1+𝛼+𝑉 𝑖(𝑝𝐼,𝑝 𝐹)−𝑝 𝑖(𝑝𝐼,𝑝 𝐹). The provider chooses the inference price (𝑝𝐼) and the
fine-tuning price (𝑝𝐹) to maximize profit, such that𝜋∗ 𝑀=max𝑝𝐼,𝑝𝐹𝜋𝑀.
15

By solving the corresponding first-order conditions, we obtain the equilibrium inference and fine-tuning
prices, denoted by𝑝∗ 𝐼 and𝑝∗ 𝐹, respectively.4 These results are summarized in the following lemma.
LEMMA2(Equilibrium Pricing Decisions of the Provider).In equilibrium, the foundation model
provider sets the inference and fine-tuning prices as follows:
𝑝∗ 𝐼=
2(1+𝛼)(𝑐 𝐹(2+𝜃 𝑝)3(2+3𝜃 𝑝)2+2𝑐𝑉(2+𝜃 𝑝)3(2+3𝜃 𝑝)2
−(1+𝜃 𝑝)(2+2𝜃 𝑝+2𝜃𝑞+𝜃 𝑝𝜃𝑞)(8+12𝜃 𝑝+3𝜃 2 𝑝+2(2+𝜃 𝑝)𝜃𝑞))
4𝑐𝐹(2+𝜃 𝑝)3(2+3𝜃 𝑝)2+8𝑐𝑉(2+𝜃 𝑝)3(2+3𝜃 𝑝)2−(1+𝜃 𝑝)(8+12𝜃 𝑝+3𝜃 2𝑝+2(2+𝜃 𝑝)𝜃𝑞)2,
𝑝∗ 𝐹= 2(1+𝜃 𝑝)(2+𝜃 𝑝)(2+3𝜃 𝑝)(1+𝛼)(4𝑐 𝐹+4𝑐𝐹𝜃𝑝−4𝑐𝑉𝜃𝑝−3𝑐𝑉𝜃2 𝑝+2(𝑐 𝐹+𝑐𝑉)(2+𝜃 𝑝)𝜃𝑞) 4𝑐𝐹(2+𝜃 𝑝)3(2+3𝜃 𝑝)2+8𝑐𝑉(2+𝜃 𝑝)3(2+3𝜃 𝑝)2−(1+𝜃 𝑝)(8+12𝜃 𝑝+3𝜃 2𝑝+2(2+𝜃 𝑝)𝜃𝑞)2.
Accordingly, the equilibrium data volumes and product prices, denoted by𝑉 ∗ 𝑖 and𝑝 ∗ 𝑖 , are obtained by
substituting𝑝∗ 𝐼 and𝑝∗ 𝐹 into Equations (4) and (5), respectively. As shown in Lemma 2, the equilibrium prices
of the provider depend on the parameters of the downstream market(𝜃 𝑝,𝜃𝑞). Therefore, we examine how
the intensity of downstream price and quality competition affects the provider’s optimal pricing decisions,
as summarized in the following lemmas.
LEMMA3(Effects of Downstream Competition on the Fine-Tuning Price).
a. The fine-tuning price decreases with the intensity of downstream price competition (i.e.,
𝑑𝑝∗ 𝐹
𝑑𝜃𝑝 <0).
b. The fine-tuning price increases with the intensity of downstream quality competition (i.e.,
𝑑𝑝∗ 𝐹
𝑑𝜃𝑞 >0).
Lemma 3 demonstrates that the fine-tuning price decreases with downstream price competition (𝜃𝑝) and
increases with downstream quality competition (𝜃𝑞). As price competition intensifies, firms reduce the data
volumes used for fine-tuning, as explained following Lemma 1. This reduction lowers not only fine-tuning
revenue but also inference revenue (due to the resulting degradation in product quality). The provider
therefore has an incentive to lower the fine-tuning price to stimulate data volume, leading to
𝑑𝑝∗ 𝐹
𝑑𝜃𝑝 <0.
In contrast, as quality competition intensifies, firms increase data volume, as discussed after Lemma 1,
prompting the provider to raise the fine-tuning price.
The next lemma examines how downstream price and quality competition affect the inference price.
LEMMA4(Effects of Downstream Competition on Inference Price).
a. The inference price increases with the intensity of downstream price competition (
𝑑𝑝∗ 𝐼
𝑑𝜃𝑝 >0) when
𝑐𝐹+2𝑐𝑉>𝑐 1 and decreases otherwise.
b. The inference price decreases with the intensity of downstream quality competition (
𝑑𝑝∗ 𝐼
𝑑𝜃𝑞 <0) when
𝑐𝐹+2𝑐𝑉>𝑐 2 and increases otherwise.
4 We focus on non-negative interior solutions for(𝑝∗ 𝐼,𝑝∗ 𝐹,𝑝∗ 𝑖,𝑉∗ 𝑖)to ensure a non-trivial equilibrium. In addi-
tion to the pure-strategy equilibrium conditions specified in Footnote 3, we impose the technical constraints
𝑐𝐹≥𝑐𝐹 and𝑐 𝑉≥𝑐𝑉, with expressions for𝑐𝐹 and𝑐 𝑉 provided in the Appendix.
16

For brevity, the expressions for𝑐 1 and𝑐 2 are provided in the Online Appendix.
In contrast to the fine-tuning price, both downstream price and quality competition have non-monotonic
effects on the inference price, as indicated by Lemma 4. The outcome arises because price competition
influences inference prices in two distinct ways. First, intensified price competition reduces product prices,
which, in turn, increases inference demand, prompting the provider to raise the inference price. Second,
lower product prices, resulting from heightened price competition, reduce the marginal benefits of product
quality, leading firms to invest less in quality improvement. This is achieved by decreasing the data volume
used for fine-tuning. The reduction in data volume diminishes the provider’s revenue, prompting a decrease
in the inference price, which increases the marginal benefit of quality improvement and thereby stimulates
data volume. However, the magnitude of this effect depends on the firms’ marginal cost of data volume.
Specifically, it can be shown that when𝑐𝐹 or𝑐 𝑉 is relatively high (i.e.,𝑐𝐹>𝑐 1−2𝑐𝑉 or𝑐 𝑉>(𝑐 1−𝑐𝐹)/2),
the marginal cost of data volume is also high. In such cases, increasing the data volume by reducing the
inference price becomes more difficult. Consequently, the provider may not reduce the inference price
substantially, leading to an overall increase in the inference price. Conversely, when the marginal cost of data
volume is relatively low, the second effect dominates. A similar reasoning applies to the impact of increased
quality competition on the inference price.
5. Consumer Surplus and Policy Implications
With the growing use of AI-enabled products, consumer welfare faces significant risks, such as the difficulty
of assessing product quality (Ngo 2025). In light of these concerns, policymakers are increasingly focused on
preserving consumer welfare in the context of AI (Robinson 2025). However, the complex interdependencies
between upstream providers and downstream markets, as discussed in Section 4, highlight the regulatory
challenges inherent to the AI supply chain (Cen et al. 2024b). This section addresses these issues by evalu-
ating the effectiveness of existing regulatory frameworks and providing guidance for selecting appropriate
policy instruments. We focus on two prominent approaches: promoting downstream market competition and
providing compute subsidies (Competition Bureau 2024, Wu 2024). Our analysis proceeds in two parts: first,
we assess the impact of pro-competitive policies on consumer surplus; second, we evaluate the effectiveness
of compute subsidy policies. We conclude by discussing the conditions under which each policy instrument
most effectively enhances consumer surplus.
5.1. Pro-Competitive Policies in Downstream Markets
For policymakers, pro-competitive regulation has long been a key strategy to enhance consumer welfare,
primarily by lowering prices and improving product quality (Tucker 2024). To reduce prices, a key component
of pro-competitive policies is promoting price competition in the consumer market (hereafter referred to as the
pro-price-competitive policy). This can be achieved through measures such as enhancing price transparency
17

or facilitating product price comparisons. One prominent instance is the Federal Trade Commission’s (FTC)
Rule on Unfair or Deceptive Fees. This rule requires companies to disclose the total price in advance,
avoiding hidden or misleading fees (FTC 2025d). In a recent case, the FTC accused Ticketmaster, a leading
online ticketing platform, of violating this rule by failing to provide complete price transparency. As a result,
the company was required to adjust its pricing system to ensure that consumers could see the total cost
before making a purchase (Boggs 2025). Similarly, the U.S. Federal Communications Commission (FCC)
has implemented regulations requiring Internet service providers to display their base monthly prices on
standardized labels. This rule aims to improve consumer decision-making by making it easier for individuals
to compare prices across providers, thus enhancing market transparency and fostering more competitive
pricing (FCC 2025).
Another key component of pro-competitive policies is fostering quality competition in consumer markets
(hereafter referred to as thepro-quality-competitive policy), often by increasing transparency about product
quality. A notable example is the FTC’sTrade Regulation Rule on the Use of Consumer Reviews and
Testimonials, which aims to prevent deceptive practices such as fake reviews and the suppression of negative
feedback (FTC 2025a). In one case, the FTC alleged that Fashion Nova misrepresented its product reputation
by concealing customer reviews with ratings below four stars, thus misleading consumers about the true
quality of its products (FTC 2025c).
In the context of the AI supply chain, policymakers are increasingly advocating for the development of
similar pro-competitive policies (Competition Bureau 2024). The FTC, for example, has issued guidance
that prohibits companies from exaggerating or misrepresenting the capabilities of their AI-based products
(Leblanc et al. 2025). Companies found guilty of overstating the capabilities of their AI products, such
as DoNotPay, have faced FTC complaints and proposed settlements for deceptive claims (FTC 2025b).
Similarly, the European Union’sConsumer Rights Actrequires businesses to disclose the total price of
digital content or services, including AI-based products, and prohibits hidden fees (CCPC 2025). Together,
these policies promote greater transparency regarding both price and quality, thereby fostering more intense
competition in the downstream segment of the AI supply chain. 5
Recent research and policy analyses highlight that increased competition in product markets can benefit
consumers by driving down prices or encouraging quality improvements (Government of Canada 2024, Tyagi
1999, Wu and Zhu 2022). However, the existing literature also points to potential downsides, suggesting that
intensified price competition may diminish firms’ incentives to invest in product quality (Tsay and Agrawal
2000), ultimately leading to lower product quality and reduced consumer surplus. A similar concern arises in
quality competition, where research indicates that aggressive competitive pressures may lead to a decrease
5 Studies show that greater market transparency often leads to increased competition, ultimately benefiting
consumers (Schultz 2009).
18

in product quality (Armstrong and Chen 2009). In the context of the AI supply chain, it remains unclear
which of these opposing effects dominates, raising questions about whether pro-competitive policies in
downstream markets ultimately enhance or reduce consumer surplus.
To address this issue, we first define consumer surplus, denoted by𝐶𝑆, within the framework of our model.
Following the literature (Singh and Vives 1984, Wang et al. 2024), we consider a representative consumer
and derive𝐶𝑆from the corresponding utility function (i.e.,𝑈(𝑑 𝑖,𝑑 𝑗)= ˝2 𝑖=1  𝜇𝑖𝑑𝑖− 𝛽𝑖𝑑2 𝑖+𝛾𝑑𝑖𝑑𝑗 2 −𝑝 𝑖𝑑𝑖  ,
where the first term represents the direct benefit of consuming the products, the second term accounts for the
diminishing returns, and the third term reflects the payment made by the consumer. The resulting expression
for𝐶𝑆and its derivation are provided in the Online Appendix. In equilibrium, this expression simplifies to:
𝐶𝑆=
2∑︁
𝑖=1
1
2(1+𝛼+𝑉 ∗ 𝑖−𝑝∗ 𝑖)2,(8)
which indicates that consumer surplus is jointly determined by product quality (𝑞∗ 𝑖 =𝛼+𝑉 ∗ 𝑖 ) and prices (𝑝∗ 𝑖 ).
Based on Equation (8), we analyze the effects of pro-price-competitive and pro-quality-competitive poli-
cies in the downstream market on consumer surplus. The results are summarized in the following proposition.
PROPOSITION1(Impact of Pro-competitive Policies on Consumer Surplus).
a. As price competition in downstream markets intensifies, consumer surplus decreases if𝑐 𝐹+2𝑐𝑉<˜𝑐,
and increases otherwise.
b. As quality competition in downstream markets intensifies, consumer surplus increases.
The explicit expression for˜𝑐is algebraically complex and is thus provided in the Online Appendix.
As shown in Proposition 1a, while pro-competitive policies may intensify price competition and reduce
product prices, consumer surplus can paradoxically decline when compute costs (i.e.,𝑐 𝐹) or data prepro-
cessing costs (i.e.,𝑐 𝑉) are relatively low. This counter-intuitive result can be explained as follows.
As price competition intensifies, firms are incentivized to lower their product prices, which benefits
consumers (i.e.,
𝑑𝑝∗ 𝑖
𝑑𝜃𝑝 <0). However, the impact on product quality is more nuanced, as it can move in either
direction due to the co-creation dynamics inherent in the AI supply chain. The direct effect of increased price
competition is a reduction in product quality (i.e., 𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑝

 𝑝∗ 𝐼,𝑝∗ 𝐹 <0): Lower prices reduce the marginal
benefit of offering higher quality, thus diminishing firms’ incentives to invest in product quality.
In contrast, the indirect effect operates through the provider’s pricing response (i.e., 𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝑝𝐼 𝑑𝑝∗ 𝐼 𝑑𝜃𝑝 +
𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹)
𝜕𝑝𝐹
𝑑𝑝∗ 𝐹
𝑑𝜃𝑝
|𝑝∗ 𝐼,𝑝∗ 𝐹). Specifically, as price competition intensifies, the provider lowers the fine-tuning
price (i.e.,
𝑑𝑝∗ 𝐹
𝑑𝜃𝑝 <0), while the inference price may rise or fall (i.e.,
𝑑𝑝∗ 𝐼
𝑑𝜃𝑝 can take either sign), as shown
in Lemmas 3 and 4. A higher inference price reduces the marginal benefit of product quality, leading to a
decrease in data volumes (𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝑝𝐼

 𝑝∗ 𝐼,𝑝∗ 𝐹 <0), while a lower fine-tuning price reduces the marginal cost
of data volume, thus increasing data volumes ( 𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝑝𝐹

 𝑝∗ 𝐼,𝑝∗ 𝐹 <0). Even if the inference price increases
19

and suppresses data volumes, the effect of the reduction in the fine-tuning price dominates, resulting in an
overall increase in product quality (𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝑝𝐼 𝑑𝑝∗ 𝐼 𝑑𝜃𝑝 + 𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝑝𝐹 𝑑𝑝∗ 𝐹 𝑑𝜃𝑝 

 𝑝∗ 𝐼,𝑝∗ 𝐹 >0). Taken together, intensified
price competition indirectly encourages higher product quality by enhancing the provider’s co-creation
incentives by lowering the fine-tuning price (and sometimes the inference price). However, as explained in
the following, when the coefficients for the data preprocessing costs and the compute costs (i.e.,𝑐𝑉 and𝑐 𝐹)
are relatively low, this indirect effect is outweighed by the direct effect. In this case, the net result is a decline
in product quality, thereby reducing consumer surplus.
When𝑐 𝑉 increases, the firms’ marginal cost of quality improvement rises, which reduces the direct effect
on product quality (i.e., 𝑑 𝑑𝑐𝑉 𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑝

 𝑝∗ 𝐼,𝑝∗ 𝐹 >0). A similar effect arises when𝑐 𝐹 increases: Increased
compute costs lead to a higher fine-tuning price, which in turn increases the marginal cost of quality
improvement, further diminishing the direct effect (i.e., 𝑑 𝑑𝑐𝐹 𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑝

 𝑝∗ 𝐼,𝑝∗ 𝐹 >0). Thus, when𝑐 𝑉 or𝑐 𝐹 is
relatively high, the negative direct effect of intensified price competition on product quality is dominated,
leading to increased consumer surplus as𝜃 𝑝 increases. In contrast, when both𝑐 𝑉 and𝑐 𝐹 are relatively low
(i.e.,𝑐 𝐹+2𝑐𝑉<˜𝑐), the direct effect on product quality dominates, leading to a decline in product quality
and, consequently, consumer surplus as𝜃 𝑝 increases.
Proposition 1b further demonstrates that consumers always benefit as quality competition in the down-
stream market intensifies. At first glance, this may seem intuitive, as increased quality competition encourages
firms to enhance product quality (i.e.,
𝑑𝑉∗ 𝑖
𝑑𝜃𝑞 >0). However, our analysis uncovers an additional, more nuanced
mechanism: In certain cases, intensified quality competition also leads to lower product prices (i.e.,
𝑑𝑝∗ 𝑖
𝑑𝜃𝑞 <0
if𝑐 𝐹+2𝑐𝑉 >
(1+𝜃𝑝)(3𝜃 2𝑝+4(2+𝜃𝑞)+2𝜃𝑝(6+𝜃𝑞)) 2
4(2+𝜃𝑝)(2+3𝜃 𝑝)(𝜃 2𝑝+2(1+𝜃𝑝)(2+𝜃 𝑝)𝜃𝑞) ), which in turn benefits consumers. This outcome arises
from indirect effects driven by the strategic pricing behavior of the foundation model provider within the AI
supply chain. Specifically, as quality competition intensifies, the provider may lower the inference price (as
established in Lemma 4), which in turn incentivizes firms to reduce their product prices. Thus, the increase
in consumer surplus from intensified quality competition is not solely driven by higher product quality; it
can also stem from lower product prices. This challenges the conventional view that higher-quality products
always command higher prices, as suggested in the literature (e.g., Tirole 1988, Sharma and Mehra 2021).
5.2. Compute Subsidies
In addition to pro-competitive policies, subsidizing access to computing power (hereafter referred to as
compute subsidies) is a widely used regulatory tool employed by policymakers. By reducing compute costs,
these subsidies incentivize firms to leverage more data for model fine-tuning, ultimately improving product
quality and increasing consumer surplus (Sastry et al. 2024). In China, the government has implemented
this approach within the AI supply chain. For example, the Beijing municipal government allocates annual
compute subsidies totaling 100 million RMB to firms involved in large-scale AI model services. These
subsidies can offset up to 30% of computing expenses, including those associated with fine-tuning (Wu
20

2024). Similarly, the Shenzhen municipal government has introduced an annual compute subsidy program
worth 500 million RMB, covering up to 50% of compute costs. Comparable initiatives have also been
launched by the Shanghai and Chengdu municipal governments (Wu 2024).
To analyze the impact of this policy on consumer surplus, we consider a scenario in which policymakers
offer compute subsidies that reduce compute costs by a proportion𝑥. Here,𝑥denotes the subsidy rate, defined
as the fraction of compute costs covered by policymakers. Under this policy, the foundation model provider
incurs fine-tuning costs of𝑐 𝐹(1−𝑥)𝑉 2 1+𝑐𝐹(1−𝑥)𝑉 2 2 , rather than the full cost𝑐 𝐹𝑉 2 1+𝑐𝐹𝑉 2 2 . Let𝑉 ′ 1 and
𝑉′ 2 denote the resulting equilibrium data volumes, and𝐶𝑆 ′ represent the corresponding consumer surplus
under the compute subsidy. The total subsidy expenditure under this policy is given by𝑥𝑐 𝐹𝑉′2 1 +𝑥𝑐 𝐹𝑉′2 2 .
We then compare the consumer surplus with and without the policy and present the results in the following
lemma.
LEMMA5(Impact of Compute Subsidies on Consumer Surplus).When compute subsidies are pro-
vided, consumer surplus increases compared to the scenario without them (i.e.,∀𝑥∈[0,1],𝐶𝑆′(𝑥)>𝐶𝑆(𝑥)).
Lemma 5 shows that, although compute subsidies are granted to the foundation model provider, they
ultimately benefit consumers. This can be explained as follows: When policymakers subsidize compute
costs, the foundation model provider faces a lower marginal compute cost, which leads to a reduction in the
fine-tuning price. The lower fine-tuning price encourages firms to increase their data volumes for fine-tuning,
thereby improving product quality and enhancing consumer surplus.
Although compute subsidies increase consumer surplus, it is essential to assess whether the policy is
cost-effective, particularly given the substantial public funds involved. To do so, we adopt the framework
from the literature (Anderson et al. 2022) and definecost-effectiveness(𝐶𝐸) as the net benefits of compute
subsidies, which are measured by the difference between the incremental consumer surplus obtained from
compute subsidies and the subsidy expenditure, and can be expressed as𝐶𝑆 ′−𝐶𝑆−𝑥𝑐 𝐹𝑉′2 1 −𝑥𝑐 𝐹𝑉′2 2 . A
positive value indicates that the policy is cost-effective in enhancing consumer surplus. We formally analyze
this effectiveness metric and present the results in the following proposition.
PROPOSITION2(Cost-Effectiveness of Compute Subsidies).Compute subsidies are cost-effective
only when𝑐 𝐹+2𝑐𝑉<ˆ𝑐. The explicit expression forˆ𝑐is algebraically complex and is thus provided in the
Online Appendix.
Although consumer surplus increases with compute subsidies (as shown in Lemma 5), Proposition 2
indicates that such subsidies are cost-ineffective in enhancing consumer surplus when compute and data
preprocessing costs are relatively high. This counter-intuitive result can be explained as follows: While
compute subsidies improve product quality and thus enhance consumer surplus (as discussed following
Lemma 5), they also incur substantial costs. When these costs outweigh the increase in consumer surplus,
21

the subsidies become cost-ineffective. When the coefficient of data preprocessing costs (𝑐 𝑉) is relatively
high, firms face substantial marginal costs in expanding data volumes for fine-tuning, limiting their ability
to improve product quality even with subsidized compute costs. As a result, the increase in consumer
surplus is less than the subsidy expenditure. Similarly, when the coefficient of compute costs (𝑐 𝐹) is high,
the provider still faces significant marginal costs despite the subsidy and is thus incentivized to maintain
relatively high fine-tuning prices. This results in high marginal costs for firms that attempt to improve
product quality, thereby limiting the policy’s cost-effectiveness. Therefore, when𝑐𝐹 or𝑐𝑉 is relatively high,
compute subsidies are cost-ineffective in improving consumer surplus.
As shown in Proposition 2, compute subsidies can be cost-effective when compute costs and data pre-
processing costs are relatively low. Specifically, when𝑐 𝐹+2𝑐 𝑉 <ˆ𝑐, there exists a subsidy rate (i.e.,𝑥)
such that the net benefits of compute subsidies are positive (i.e.,𝐶𝐸>0). This indicates that whether these
subsidies are cost-effective also depends on the choice of the subsidy rate. Thus, we examine the relationship
between cost-effectiveness and the subsidy rate for computing power under the condition (𝑐 𝐹+2𝑐𝑉 <ˆ𝑐),
and summarize our findings in the following corollary.
COROLLARY1(Relationship between Cost-Effectiveness and Subsidy Rate for Compute Costs).
As the subsidy rate for compute costs (i.e.,𝑥) increases, cost-effectiveness improves if𝑥<𝑥 ′, and decreases
if𝑥>𝑥 ′. Additionally, if𝑥>𝑥 ′′ (with𝑥′′>𝑥′), compute subsidies become cost-ineffective; otherwise, they
become cost-effective.
For brevity, the explicit expressions for𝑥′ and𝑥′′ are provided in the Online Appendix.
Corollary 1 demonstrates that the net benefits of compute subsidies do not increase monotonically with the
subsidy rate𝑥. Instead, the net gain in consumer surplus relative to the subsidy costs initially rises and then
falls as𝑥increases, with cost-effectiveness peaking at𝑥 ′. This non-monotonic pattern can be explained by
the fine-tuning behavior of downstream firms: At low subsidy rates, increasing𝑥encourages firms to expand
data volumes for fine-tuning, which improves product quality, increases consumer surplus, and enhances
cost-effectiveness. This explains the initial upward trend for values of𝑥below𝑥′. However, once the subsidy
rate exceeds this threshold (i.e.,𝑥>𝑥 ′), the provider responds by lowering the fine-tuning price excessively,
which incentivizes firms to engage in more aggressive fine-tuning. Although this improves product quality
and further increases consumer surplus, it also substantially increases data volume, thereby driving up
subsidy costs (𝑥𝑐𝐹𝑉′2 1 +𝑥𝑐 𝐹𝑉′2 2 ). As a result, the gains in consumer surplus are eventually outweighed by
the increase in subsidies when𝑥>𝑥 ′, thereby reducing the cost-effectiveness of compute subsidies. If the
subsidy rate𝑥exceeds𝑥 ′′, the cost-effectiveness may even turn negative. Therefore, under the condition
𝑐𝐹+2𝑐𝑉<ˆ𝑐, compute subsidies remain cost-effective only if the subsidy rate is not too high (i.e.,𝑥<𝑥 ′′).
Proposition 2 offers valuable regulatory insights for policymakers. The findings suggest that compute
subsidies must be implemented with caution, as their effectiveness in enhancing consumer surplus depends
22

Figure 5 Policy Effectiveness under Different Cost Regions
Compute Subsidies
Ƹ𝑐 ǁ𝑐
𝑐𝐹 + 2𝑐𝑉
Pro-price-competitive
Policy
Pro-quality-competitive
Policy
effective
ineffective
ǁ𝑐 Ƹ𝑐
𝑐𝐹 + 2𝑐𝑉
( Ƹ𝑐 < ǁ𝑐) ( Ƹ𝑐 > ǁ𝑐)
Region I Region II Region III Region I Region II Region III
heavily on the cost environment. Specifically, when data preprocessing costs or compute costs are relatively
high, such subsidies yield limited benefits to consumer surplus and may even fail to cover the subsidy
expenditures. Additionally, to ensure the effectiveness of compute subsidies, it is also crucial to carefully
calibrate the subsidy rate. If the rate is set too high, it could encourage downstream firms to overinvest
in fine-tuning, leading to disproportionately high subsidy expenditures and diminishing, or even negative,
returns in terms of net consumer surplus gains.
5.3. Comparing Policies
Building on the previous analysis, this subsection compares the effectiveness of each policy in enhancing
consumer surplus across different cost regions. Unlike compute subsidies, which impose a direct cost on the
policymaker, the pro-competitive policy incurs no government expenditure. Thus, the effectiveness of the
pro-competitive policy is assessed solely by its ability to increase consumer surplus. In contrast, compute
subsidies are deemed effective only when the increase in consumer surplus exceeds the costs incurred in
providing the subsidy. Figure 5 illustrates the effective and ineffective policy regimes for compute subsidies,
the pro-price-competitive policy, and the pro-quality-competitive policy. We divide the cost space into three
distinct regions. When the compute and data preprocessing costs are relatively low (𝑐𝐹+2𝑐𝑉<min{˜𝑐,ˆ𝑐}),
the cost condition falls into Region I. When the costs are moderate (min{˜𝑐,ˆ𝑐}<𝑐𝐹+2𝑐𝑉<max{˜𝑐,ˆ𝑐}), this
corresponds to Region II. Finally, when the costs are relatively high (𝑐 𝐹+2𝑐𝑉>max{˜𝑐,ˆ𝑐}), this scenario
falls into Region III. The regions are depicted differently depending on the relationship betweenˆ𝑐and˜𝑐:
The left panel shows the case whereˆ𝑐<˜𝑐, while the right panel illustrates the case whereˆ𝑐>˜𝑐.
As shown in Figure 5, the results of Proposition 1 and 2 reveal a complementarity between the pro-price-
competitive policy and compute subsidies: When one is ineffective, the other is effective. Specifically, in
Region I, where the costs are relatively low (𝑐𝐹+2𝑐𝑉<min{˜𝑐,ˆ𝑐}), the pro-price-competitive policy does
not improve consumer surplus, whereas compute subsidies are cost-effective in doing so. Conversely, in
Region III, where the costs are relatively high, compute subsidies are cost-ineffective, while the pro-price-
competitive policy becomes effective.
23

Our research provides important policy implications for policymakers seeking to enhance consumer
surplus in the AI supply chain, offering structured policy recommendations under varying cost conditions.
As illustrated by the green lines in Region I of Figure 5, where the compute and data preprocessing costs
are relatively low (0<𝑐 𝐹+2𝑐𝑉<min{ˆ𝑐,˜𝑐}), policymakers should focus solely on promoting competition
in downstream markets, whether in quality or price. In this case, as indicated by the red line in Region
I, compute subsidies are not cost-effective because firms are already engaging in aggressive fine-tuning,
leading to excessive public expenditure on subsidies with limited additional benefit to consumer surplus.
When these costs are relatively high (𝑐𝐹+2𝑐𝑉>max{ˆ𝑐,˜𝑐}), as illustrated by the green lines in Region III of
Figure 5, policymakers should instead consider compute subsidies and pro-quality-competition policies. In
this case, promoting price competition would reduce consumer surplus by discouraging firms from investing
in data for fine-tuning, which in turn lowers product quality. When these costs fall within an intermediate
range (min{ˆ𝑐,˜𝑐}<𝑐𝐹+2𝑐𝑉<max{ˆ𝑐,˜𝑐}), policymakers should consider adopting pro-quality-competitive
policy ifˆ𝑐<˜𝑐, as illustrated by the green line in Region II of the left panel; otherwise (ˆ𝑐>˜𝑐), they should
consider all three policies, as illustrated by the green lines in Region II of the right panel.
6. Effect of Different Regulatory Policies on Profits
In addition to consumer surplus, it is crucial to understand how pro-competitive policies and compute
subsidies impact the profitability of both foundation model providers and downstream firms, as the success
of any regulatory policy ultimately hinges on its acceptance by industry participants. A policy that not only
enhances consumer surplus but also improves the profitability of both providers and downstream firms is
more likely to gain traction, thereby creating a “win–win–win” scenario in which all stakeholders benefit.
In this section, we begin by conducting a comparative statics analysis to assess how policies that promote
competition in downstream markets impact the profits of both the foundation model provider and downstream
firms, followed by an analysis of the effects of compute subsidies.
Understanding the effect of downstream competition on the profitability of both upstream and downstream
firms remains a central concern in the study of industrial organization (Basak et al. 2023). The conventional
view holds that increased competition among downstream firms reduces their profitability while enhancing
the profits of upstream firms (Basak et al. 2023, Tyagi 1999). This perspective is based on the concept of
double marginalization, which suggests that the increased competition among downstream firms weakens
their pricing power, resulting in lower product prices (i.e., reduced double marginalization) and, in turn,
increased demand for the product (Tyagi 1999). As a result, upstream firms are expected to see higher profits
from the increase in sales to downstream firms, whereas downstream firms face shrinking margins and
lower profitability. However, our analysis challenges this conventional wisdom, revealing that these typical
outcomes do not necessarily hold in our setting. We summarize our findings in the following proposition
and corollary.
24

PROPOSITION3(Impact of Pro-competitive Policies on the Foundation Model Provider’s Profits).
a. As price competition intensifies, the profits of the foundation model provider decrease if𝜃 𝑞> ˜𝜃𝑞, and
increase otherwise.
b. As quality competition intensifies, the foundation model provider’s profits always increase.
For brevity, the expression for ˜𝜃𝑞 is provided in the Online Appendix.
This result highlights that intensified price competition in the downstream market can, under certain
conditions, reduce the foundation model provider’s profits. To better understand how downstream price
competition affects the provider’s profitability, we apply the chain rule to analyze𝑑𝜋𝑀 𝑑𝜃𝑝

 𝑝∗ 𝐼,𝑝∗ 𝐹 and present the
simplified expression below, with the complete derivation available in the Online Appendix:
𝑑𝜋𝑀
𝑑𝜃𝑝

𝑝∗ 𝐼,𝑝∗ 𝐹
=
2∑︁
𝑖=1
𝜕𝜋𝑀
𝜕𝑝𝑖
𝜕𝑝𝑖(𝑝𝐼,𝑝 𝐹)
𝜕𝜃𝑝
+𝜕𝜋𝑀
𝜕𝑉𝑖
𝜕𝑉𝑖(𝑝𝐼,𝑝 𝐹)
𝜕𝜃𝑝


𝑝∗ 𝐼,𝑝∗ 𝐹
,(9)
where the expression for𝜋𝑀 is provided in Equation (7), with𝜕𝜋𝑀 𝜕𝑝𝑖

 𝑝∗ 𝐼,𝑝∗ 𝐹 =−𝑝∗ 𝐼 and 𝜕𝜋𝑀 𝜕𝑉𝑖

 𝑝∗ 𝐼,𝑝∗ 𝐹 =𝑝∗ 𝐼+𝑝∗ 𝐹−
2𝑐𝐹𝑉∗ 𝑖 .
Equation (9) demonstrates that intensified price competition influences provider profits by shaping down-
stream firms’ decisions regarding both pricing and data usage for finetuning. On the one hand, consistent
with conventional wisdom (i.e., reduced double marginalization), increased price competition prompts
firms to lower their product prices ( 𝜕𝑝𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑝

 𝑝∗ 𝐼,𝑝∗ 𝐹 <0), which stimulates product demand and, in turn,
increases the provider’s inference revenue (𝜕𝜋𝑀 𝜕𝑝𝑖 𝜕𝑝𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑝

 𝑝∗ 𝐼,𝑝∗ 𝐹 =−𝑝∗ 𝐼 𝜕𝑝𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑝

 𝑝∗ 𝐼,𝑝∗ 𝐹 >0). On the other
hand, intensified price competition encourages downstream firms to reduce their data usage for fine-tuning
(𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑝

 𝑝∗ 𝐼,𝑝∗ 𝐹 <0), as discussed following Lemma 1. This decline in fine-tuning demand not only reduces
fine-tuning revenue (𝑝∗ 𝐹 𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑝

 𝑝∗ 𝐼,𝑝∗ 𝐹 <0), but also degrades product quality, which in turn reduces infer-
ence revenue (𝑝∗ 𝐼 𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑝

 𝑝∗ 𝐼,𝑝∗ 𝐹 <0). Additionally, reduced data usage lowers the compute costs associated
with fine-tuning (2𝑐𝐹𝑉∗ 𝑖 𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑝

 𝑝∗ 𝐼,𝑝∗ 𝐹 <0). However, despite the savings in compute costs, the overall
effect of reduced data usage is a net decrease in provider profits (𝜕𝜋𝑀 𝜕𝑉𝑖 𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑝

 𝑝∗ 𝐼,𝑝∗ 𝐹 <0). The magnitude
of this effect is shaped by the intensity of quality competition (i.e.,𝜃 𝑞). Specifically, as explained below, a
higher𝜃 𝑞 amplifies the effect of reduced data volume.
When𝜃 𝑞 increases, the provider is incentivized to raise the fine-tuning price, as shown in Lemma 3. This
increase in𝑝 ∗ 𝐹 amplifies the loss of fine-tuning revenue caused by the reduced data volume resulting from
intensified price competition (𝑝 ∗ 𝐹 𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑝

 𝑝∗ 𝐼,𝑝∗ 𝐹 <0). Consequently, the effect of reduced data volume
becomes more pronounced as𝜃 𝑞 rises. When𝜃 𝑞 is relatively high (i.e.,𝜃 𝑞> ˜𝜃𝑞), the negative effect of
reduced data volume outweighs the positive effect of increased demand, ultimately leading to a decrease
in the provider’s profits. This outcome, in which the provider’s profits decrease in response to intensified
downstream price competition within the context of the AI supply chain, contrasts with established insights
from traditional supply chains involving manufacturers and retailers (Tyagi 1999, Yenipazarli 2021). The key
25

distinction lies in a novel mechanism we identify in the AI supply chain: Intensified price competition reduces
data usage for fine-tuning, which in turn diminishes both fine-tuning and inference revenues for the provider.
In contrast to the effects of price competition, Proposition 3b indicates that intensified quality competition
always benefits the foundation model provider. To analyze this effect, we also apply the chain rule to analyze
𝑑𝜋𝑀
𝑑𝜃𝑞

𝑝∗ 𝐼,𝑝∗ 𝐹 and present the simplified expression below, with the complete derivation available in the Online
Appendix:
𝑑𝜋𝑀
𝑑𝜃𝑞

𝑝∗ 𝐼,𝑝∗ 𝐹
=
2∑︁
𝑖=1
𝜕𝜋𝑀
𝜕𝑉𝑖
𝜕𝑉𝑖(𝑝𝐼,𝑝 𝐹)
𝜕𝜃𝑞
+𝜕𝜋𝑀
𝜕𝑝𝑖
𝜕𝑝𝑖(𝑝𝐼,𝑝 𝐹)
𝜕𝜃𝑞


𝑝∗ 𝐼,𝑝∗ 𝐹
,
where 𝜕𝜋𝑀 𝜕𝑉𝑖

 𝑝∗ 𝐼,𝑝∗ 𝐹 =𝑝 ∗ 𝐼+𝑝 ∗ 𝐹−2𝑐 𝐹𝑉∗ 𝑖 and 𝜕𝜋𝑀 𝜕𝑝𝑖

 𝑝∗ 𝐼,𝑝∗ 𝐹 =−𝑝 ∗ 𝐼. As quality competition intensifies, firms
increase their data usage for fine-tuning to enhance product quality (𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑞

 𝑝∗ 𝐼,𝑝∗ 𝐹 >0). This rise in fine-
tuning demand not only boosts fine-tuning revenue (𝑝 ∗ 𝐹 𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑞

 𝑝∗ 𝐼,𝑝∗ 𝐹 >0) but also increases inference
demand due to improvements in product quality, leading to higher inference revenue (𝑝∗ 𝐼 𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑞

 𝑝∗ 𝐼,𝑝∗ 𝐹 >
0). Although the increase in data volume raises the provider’s compute costs, the net effect on prof-
its remains positive because ((𝑝 ∗ 𝐼+𝑝∗ 𝐹−2𝑐 𝐹𝑉∗ 𝑖)𝜕𝑉𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑞

 𝑝∗ 𝐼,𝑝∗ 𝐹 >0). Additionally, as product quality
improves, firms are incentivized to raise product prices, leading to increased double marginalization
(𝜕𝑝𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑞

 𝑝∗ 𝐼,𝑝∗ 𝐹 >0). This price increase can reduce the inference demand and thereby reduce the provider’s
profits (−𝑝∗ 𝐼 𝜕𝑝𝑖(𝑝𝐼,𝑝𝐹) 𝜕𝜃𝑞

 𝑝∗ 𝐼,𝑝∗ 𝐹 <0). However, the positive impact on profitability from increased data vol-
ume always outweighs the negative impact from higher prices. Consequently, the provider’s profits always
increase as quality competition intensifies in the downstream market.
Next, we examine how increases in the intensity of price and quality competition, as measured by higher
values of𝜃 𝑝 and𝜃 𝑞, respectively, affect downstream firms’ profits and summarize our findings in the
following corollary.
COROLLARY2(Impact of Downstream Competition on Firms’ Profits).
a. Intensified price competition may lead to an increase in downstream firms’ profits.
b. Intensified quality competition always results in a decrease in downstream firms’ profits.
Corollary 2 reveals that intensified price competition in the downstream market can actually increase the
profits of downstream firms. This finding challenges the conventional view that greater price competition
always reduces profitability (Tyagi 1999). The intuition behind this result is as follows. On the one hand,
consistent with conventional wisdom, intensified price competition prompts firms to lower their product
prices, which typically reduces revenues. On the other hand, in response to increased price competition, the
upstream provider can lower both fine-tuning and inference prices, as shown in Lemmas 3 and 4. These
price reductions reduce the costs of downstream firms to use provider services. When the savings from these
cost reductions exceed the revenue losses from lower product prices, downstream firms can experience an
increase in profits.
26

Corollary 2 further indicates that intensified quality competition always reduces downstream firms’ profits,
which aligns with conventional expectations. As quality competition intensifies, firms must invest more in
product quality to remain competitive, resulting in higher fine-tuning costs. Additionally, as established in
Lemmas 3 and 4, the foundation model provider responds by increasing both fine-tuning and potentially
inference prices, further diminishing downstream profitability.
Proposition 3 and Corollary 2 offer key insights for foundation model providers, downstream firms, and
policymakers. First, these results help both foundation model providers and downstream firms anticipate
how their profits may evolve when pro-competitive policies are implemented in the downstream market.
Such projections, given the resulting shifts in competitive dynamics, provide valuable guidance for strategic
planning (Rami Ali 2025). Second, these findings assist policymakers by clarifying how different pro-
competitive interventions affect industry participants, thereby supporting more informed decision-making
in AI supply chain regulation. In particular, policymakers should be aware of the potential downsides of pro-
quality-competitive policies. While Proposition 1 demonstrates that such policies are robust in improving
consumer surplus, Corollary 2 reveals that they simultaneously reduce profitability for downstream firms,
complicating their practical implementation. In contrast, Proposition 3 and Corollary 2 suggest that pro-
price-competitive policies may benefit both foundation model providers and downstream firms. To assess
whether such policies can deliver a “win–win–win” outcome that benefits consumers, downstream firms,
and foundation model providers, we examine this possibility in the following corollary.
COROLLARY3(Win–Win–Win Outcome of Pro-price-competitive Policy).There exist cases in
which a pro-price-competitive policy increases consumer surplus while simultaneously boosting the profits
of both the foundation model provider and downstream firms.
Corollary 3 indicates that a pro-price-competitive policy can generate a “win–win–win” outcome, ben-
efiting all stakeholders. In contrast, a pro-quality-competitive policy typically increases consumer surplus
at the cost of reduced firm profitability. This highlights the potential advantage of prioritizing price com-
petition over quality competition, suggesting that policymakers should weigh the broader benefits of pro-
price-competitive policies, even though pro-quality-competitive policies are always effective in enhancing
consumer surplus.
In addition to pro-competitive policies, we now examine another key policy instrument—compute subsi-
dies—to explore how subsidizing access to computing power affects the profitability of both the foundation
model provider and downstream firms. The main result is summarized in Proposition 4.
PROPOSITION4(Impact of Compute Subsidies on Profits).
a. Downstream firms’ profits decrease due to compute subsidies only when𝑐 𝐹>ˆ𝑐𝐹.
b. The foundation model provider’s profits always increase when compute subsidies are provided.
For brevity, the expression forˆ𝑐𝐹 is provided in the Online Appendix.
27

Proposition 4 highlights that while compute subsidies reduce compute costs for providers, they can
unexpectedly decrease downstream firms’ profits under certain conditions. This counter-intuitive outcome
arises from two opposing sets of effects. On the one hand, compute subsidies reduce the fine-tuning price,
as discussed following Lemma 5. This price reduction lowers the fine-tuning fees paid by downstream
firms, potentially boosting their profits. Additionally, the lower price encourages firms to use more data for
fine-tuning, thereby improving product quality. The resulting quality improvement drives the demand for
the product, which in turn increases downstream firms’ revenues. On the other hand, the increase in data
volume has two negative consequences for downstream firms. First, it directly raises their data preprocessing
costs. Second, improvements in product quality stimulate inference demand, prompting the provider to raise
the inference price. As a result, downstream firms face higher inference fees. Their profits decline when
the increase in data preprocessing costs and inference fees combined exceeds the savings from reduced
fine-tuning fees and the additional revenue from increased product sales. This outcome is especially likely
when the coefficient of compute costs (i.e.,𝑐 𝐹) is relatively high. A high𝑐 𝐹 results in a high fine-tuning
price, which in turn limits data volume (i.e.,𝑉 𝑖). As a result, the savings in fine-tuning fees induced by
the lower fine-tuning price (i.e.,𝑉𝑖·Δ𝑝 𝐹) due to compute subsidies are minimal, and the positive effect of
the subsidy is outweighed by the higher data preprocessing costs and inference fees, ultimately reducing
downstream firms’ profits.
In contrast to downstream firms’ profits, the foundation model provider’s profits always increase when
compute subsidies are introduced. This is because subsidies directly reduce the compute costs for the fine-
tuning service. In addition, they lower the fine-tuning price, encouraging downstream firms to invest more
in product quality through fine-tuning. As product quality improves, the demand for inference services rises.
Overall, the combination of reduced compute costs and increased inference revenue enhances the foundation
model provider’s profits. Since Proposition 4 indicates that subsidies can enhance the profitability of both
the provider and downstream firms, this regulatory instrument may lead to a ”win-win-win” outcome. We
summarize the condition for this outcome in the following corollary.
COROLLARY4(Win–Win–Win Outcome of Compute Subsidies).If𝑐 𝐹<ˆ𝑐𝐹, the provision of com-
pute subsidies boosts consumer surplus and increases the profits of both the foundation model provider and
downstream firms.
Corollary 4 indicates that compute subsidies can create a “win–win–win” outcome, benefiting all stake-
holders when compute costs are relatively low. The mechanism behind this outcome has been discussed
following Lemma 5 and Proposition 4. Specifically, compute subsidies reduce the provider’s compute costs
(which benefits the provider), prompting the provider to lower the fine-tuning price. This reduction, in turn,
reduces the costs of downstream firms (which benefits downstream firms) and strengthens their incentives
to co-create and improve quality, ultimately benefiting consumers.
28

Our findings have important policy implications for the AI supply chain. Corollary 4 and Proposition 2
suggest that policymakers should consider implementing compute subsidies when compute costs are rel-
atively low (i.e.,𝑐 𝐹 <min{ˆ𝑐𝐹,ˆ𝑐−2𝑐 𝑉}). In such cases, compute subsidies not only effectively enhance
consumer surplus but also simultaneously improve the profitability of both providers and downstream firms,
making them a desirable policy intervention.
Beyond this specific recommendation, synthesizing the findings of Sections 5 and 6 reveals a fundamental
trade-off in policy design: balancing the robustness of consumer benefits with the feasibility of achieving
gains throughout the AI supply chain. This underscores the need for carefully calibrated interventions.
We identify two policy classes, each with distinct strengths and limitations: First, pro-quality-competitive
policies are guaranteed to effectively enhance consumer surplus, but they cannot achieve a “win-win-win”
outcome because they reduce downstream firms’ profitability. Second, pro-price-competitive policies and
compute subsidies follow a different pattern. While they are not guaranteed to effectively enhance consumer
surplus, they have the potential to create a ”win-win-win” outcome that benefits all stakeholders. This
potential for broad buy-in across the AI supply chain makes these policies more practical to implement, even
if their benefits to consumers are conditional. From this perspective, policymakers face a trade-off: Policies
that robustly benefit consumers may fail to benefit participants across the entire AI supply chain, whereas
policies that can benefit both upstream and downstream participants may only deliver consumer benefits
under certain conditions.
7. Effect of Declining Compute Costs on Profits and Consumer Surplus
Beyond assessing the immediate impacts of regulatory policies, it is crucial to account for how their adoption
may need to evolve over time in response to the rapidly changing landscape of AI markets. A key factor driving
this shift is the ongoing reduction in compute costs, largely due to advancements in graphics processing
units (GPUs), which are central to fine-tuning AI models (NVIDIA 2024, Diehl 2025). To better understand
these dynamics, we conduct a comparative statics analysis to examine how declining compute costs affect
consumer surplus, as well as the profits of both the foundation model provider and downstream firms. We
also examine how regulatory policies should adapt to maintain consumer-surplus-enhancing outcomes.
Intuitively, lower compute costs should enhance profitability across the AI ecosystem and benefit con-
sumers (Osman 2024). However, prior research suggests that reductions in IT costs can reshape competitive
dynamics, potentially eroding profits for firms in settings with only downstream participants (Demirhan
et al. 2005). In our setting, which involves an AI supply chain comprising foundation model providers,
downstream firms, and consumers, the competitive dynamics are more complex. As a result, it is unclear how
declining compute costs will impact profits at different layers of the supply chain, and whether the impacts
on providers and downstream firms will differ. Additionally, in the AI supply chain, where downstream
firms co-create value with foundation model providers through fine-tuning, these effects from declining
29

compute costs can influence firms’ incentives to invest in quality, which in turn affects consumer surplus.
This underscores the need for a careful examination of how changes in compute costs impact both consumer
surplus and the profitability of providers and downstream firms within the AI supply chain. The findings of
this analysis are presented in Proposition 5.
PROPOSITION5(Impact of Compute Costs).As the coefficient of compute costs (i.e.,𝑐 𝐹) declines:
a. Downstream firms’ profits decrease if𝑐 𝐹>ˆ𝑐𝐹 and increase otherwise;
b. The foundation model provider’s profits and consumer surplus always increase.
For brevity, the expression forˆ𝑐𝐹 is provided in the Online Appendix.
Contrary to intuition, our results reveal that a decrease in𝑐𝐹 can reduce firms’ profits. This counter-intuitive
effect arises from the following mechanism. Using the chain rule, we analyze 𝑑𝜋𝑖 𝑑𝑐𝐹

 𝑝∗ 𝐼,𝑝∗ 𝐹 as follows:
𝑑𝜋𝑖
𝑑𝑐𝐹

𝑝∗ 𝐼,𝑝∗ 𝐹
=
𝜕𝜋𝑖
𝜕𝑝𝐹
𝑑𝑝∗ 𝐹
𝑑𝑐𝐹
+ 𝜕𝜋𝑖
𝜕𝑝𝐼
𝑑𝑝∗ 𝐼
𝑑𝑐𝐹
+𝜕𝜋𝑖
𝜕𝑉𝑖
𝑑𝑉∗ 𝑖
𝑑𝑐𝐹
+𝜕𝜋𝑖
𝜕𝑝𝑖
𝑑𝑝∗ 𝑖
𝑑𝑐𝐹


𝑝∗ 𝐼,𝑝∗ 𝐹
,
where the expression for𝜋𝑖 is given in Equation (6).
As𝑐 𝐹 decreases, two opposing forces shape its impact on downstream firms’ profits. On the one hand, a
lower𝑐𝐹 reduces the marginal cost of fine-tuning for the foundational model provider, leading to a decrease in
the fine-tuning price (−
𝑑𝑝∗ 𝐹
𝑑𝑐𝐹 <0). This reduction reduces the firms’ fine-tuning expenses, thereby increasing
their profits (− 𝜕𝜋𝑖 𝜕𝑝𝐹 𝑑𝑝∗ 𝐹 𝑑𝑐𝐹 

 𝑝∗ 𝐼,𝑝∗ 𝐹 >0). On the other hand, lower compute costs also affect profits through
changes in the inference price, firms’ product prices, and the data volume used for fine-tuning. The combined
effect of these three channels is negative, i.e.,−𝜕𝜋𝑖 𝜕𝑝𝐼 𝑑𝑝∗ 𝐼 𝑑𝑐𝐹 +𝜕𝜋𝑖 𝜕𝑉𝑖 𝑑𝑉∗ 𝑖 𝑑𝑐𝐹 +𝜕𝜋𝑖 𝜕𝑝𝑖 𝑑𝑝∗ 𝑖 𝑑𝑐𝐹 

 𝑝∗ 𝐼,𝑝∗ 𝐹 <0. This occurs because
a lower fine-tuning price intensifies quality competition, which prompts firms to increase their investment
in quality, which raises their expenditures (i.e., data preprocessing costs and fine-tuning fees) and directly
reduces their profits. Furthermore, improvements in product quality increase consumer demand, which, in
turn, raises the provider’s inference demand. In response, the provider may increase the inference price
charged to the firms, further eroding their profits. Together, these negative effects, combined with the positive
effect from the lower fine-tuning price, generate a non-monotonic relationship between𝑐𝐹 and downstream
firms’ profitability. When𝑐𝐹 is relatively high, the high compute cost of fine-tuning prompts the provider to
set a correspondingly high fine-tuning price, which ultimately results in a low data volume. Given this low
data volume, the reduction in the fine-tuning price resulting from declining compute costs leads to only a
small profit gain for firms (𝜕𝜋𝑖 𝜕𝑝𝐹

 𝑝∗ 𝐼,𝑝∗ 𝐹 =−𝑉∗ 𝑖 ), resulting in a weak positive effect. Consequently, the negative
effects dominate, causing the profits of downstream firms to decrease as compute costs decline.
These findings contribute to the literature on the implications of declining IT costs in competitive markets.
Early work by Demirhan et al. (2005) shows that declining IT costs generally benefit firms by enabling greater
investment, which in turn enhances product quality and increases profits. However, Demirhan et al. (2007)
30

find that when the switching costs between competing firms’ products are sufficiently high, declining IT costs
can reduce firm profitability. This occurs because lower IT costs prompt firms to engage in aggressive quality
competition, thereby eroding their profits. This result is consistent with our finding that firms may also be
worse off under declining compute costs. However, our model introduces a different mechanism behind this
outcome. In Demirhan et al. (2007), overinvestment arises from intertemporal competition, in which high
switching costs lock consumers into future purchases, incentivizing firms to overinvest in the initial period
to secure long-term demand. In contrast, in our model, the pricing behavior of the foundation model provider
plays a central role. Specifically, as compute costs fall, the provider lowers the fine-tuning price, encouraging
firms to increase their investment in product quality. This mechanism reflects the co-creation dynamics of
the AI supply chain, which, to our knowledge, has not been identified in the existing literature.
Proposition 5b further shows that the foundation model provider’s profits always increase as𝑐𝐹 decreases.
This occurs because lower compute costs (𝑐 𝐹) reduce the provider’s expenses for delivering fine-tuning
services, which in turn reduces the fine-tuning price. The lower price incentivizes downstream firms to
increase data volumes and enhance product quality, thereby boosting inference demand and increasing
inference revenue. Taken together, the reduction in fine-tuning costs and the increase in inference revenue
result in higher provider profits as compute costs decline. Similarly, consumer surplus increases as compute
costs decline. This is because lower compute costs lead to a reduction in the provider’s fine-tuning price,
which enhances downstream firms’ incentives to engage in the co-creation process and improve product
quality. The resulting improvements in product quality ultimately increase consumer surplus.
While Proposition 5 demonstrates that consumer surplus increases as compute costs decline, it remains
unclear whether regulatory interventions that are effective under current cost structures will continue to be
appropriate as costs decrease further. To address this, we examine how declining compute costs affect the
conditions for effective policy, as outlined in Proposition 1 and Proposition 2. The results are summarized
in the following corollary.
COROLLARY5(Impact of Declining Compute Costs on Policies).As compute costs decline, (i) com-
pute subsidies are more likely to be effective in enhancing consumer surplus, (ii) the pro-price-competitive
policy becomes less likely to be effective in enhancing consumer surplus, and (iii) the pro-quality-competitive
policy remains consistently effective.
Recall that compute subsidies are effective only when compute and data preprocessing costs are relatively
low, while the pro-price-competitive policy is effective only when these costs are relatively high. Thus,
Corollary 5 suggests that as compute costs decline, compute subsidies may shift from being ineffective
to effective. This implies that policymakers should consider adopting this policy in the future, even if it
appears ineffective under current cost conditions. In contrast, as compute costs continue to fall, the pro-
price-competitive policy may shift from being an effective tool for enhancing consumer surplus to one that
31

harms it. Therefore, policymakers should exercise caution with this policy and consider phasing it out once
compute costs fall to a relatively low level. Finally, the declining trend in compute costs does not significantly
affect the effectiveness of the pro-quality-competitive policy. This policy consistently increases consumer
surplus, regardless of compute cost levels, making it a robust tool for enhancing consumer surplus. Overall,
since compute costs are expected to continue declining, our findings highlight the importance of ongoing
monitoring and adaptive policymaking.
8. Conclusion
Rapid innovation in AI has brought regulatory concerns to the forefront, driven by fears that companies
might exploit AI technologies to consolidate market power and capture an outsized share of consumer
surplus. This study examines these concerns from a systemic perspective, focusing on the emerging AI
supply chain and the interactions between upstream and downstream participants. We analyze two types
of policies within this supply chain and evaluate their effectiveness. To protect consumers, pro-competitive
policies are commonly used; however, the specific approach to promoting competition is critical. Promoting
downstream quality competition consistently enhances consumer surplus, whereas promoting downstream
price competition is beneficial only when either compute costs or data preprocessing costs (or both) are
high. Importantly, these cost conditions relate to both the foundation model provider’s compute costs and
the downstream firms’ data preprocessing costs, highlighting the co-creation nature of the AI supply chain.
Furthermore, we introduce a new class of policy aimed at enhancing surplus within the AI supply chain:
compute subsidies. Our analysis shows that compute subsidies, which can effectively enhance consumer
surplus when both the compute and data preprocessing costs are low, complement pro-price-competitive
policies. We also examine how these policies affect the participants in the AI supply chain. We find that
while pro-quality-competitive policies tend to reduce downstream firms’ profits, they increase the profits
of the foundation model provider. In contrast, both pro-price-competitive policies and compute subsidies
can boost consumer surplus and increase profits for both providers and downstream firms, creating a “win-
win-win” outcome where all stakeholders benefit. Finally, we explore the implications of declining compute
costs. As these costs continue to fall, pro-price-competitive policies may shift from being an effective tool
for enhancing consumer surplus to a harmful one that diminishes it. In contrast, compute subsidies may
transition from an ineffective policy to an effective one as compute costs decline.
8.1. Theoretical Contributions
Our study makes significant theoretical contributions. Specifically, we take a crucial first step in characteriz-
ing regulation within the AI supply chain by systematically analyzing the interactions between upstream and
downstream participants. This is particularly important given the limited theoretical research on regulation in
traditional supply chain contexts. Furthermore, our study highlights the distinctive features of the AI supply
chain, setting it apart from existing research on traditional supply chains and software markets (which is
32

relevant because fine-tuning and inference of foundation models are delivered as software-enabled services).
First, unlike traditional supply chains, the development of fine-tuned models involves co-creation between
foundation model providers and downstream firms. Additionally, the provider generates revenue through
two streams: inference and fine-tuning, whereas manufacturers in traditional supply chains typically rely on
wholesale revenue. Second, the co-creation process in the AI supply chain differs from other well-known
co-creation processes among firms. In traditional settings, co-creation typically occurs independently across
participants, with each party contributing autonomously to enhance the final product. Examples include
vendor–client collaborations for enterprise systems (e.g., ERP), cases in the computer industry where one
firm develops the central processor while another develops the operating system, and scenarios in the smart-
phone industry where one firm designs the device and operating platform, while others develop applications
for it (Demirezen et al. 2020, Puyang et al. 2025, Gupta et al. 2023, Ceccagnoli et al. 2012). In contrast,
fine-tuning foundation models involves a mutually dependent form of co-creation. The foundation model
provider not only supplies the base model but also provides the computational infrastructure needed for
downstream firms to use their domain-specific data to improve the model. As downstream firms contribute
more data to enhance model performance, they increase the compute demand, thus raising the provider’s
compute costs. This interdependence in the co-creation process is largely absent from traditional co-creation
settings. Third, the customization process in the AI supply chain differs significantly from that in traditional
software markets. In conventional settings, software providers sell licenses to users, who then customize and
deploy the software on their own infrastructure, usually for a fixed one-time fee (Ma and Seidmann 2015,
Zhang et al. 2020). In contrast, fine-tuned AI models are typically hosted on the provider’s cloud infrastruc-
ture and offered through a pay-as-you-go pricing model. Fourth, this deployment mechanism and pricing
structure place both fine-tuning and inference services within the broader SaaS category. However, these
services differ significantly from traditional SaaS in terms of customization flexibility. While traditional
SaaS applications often offer limited customization options (CompTIA 2025, Zhang et al. 2020), fine-tuning
services enable users to adapt AI models with much greater flexibility to meet specialized needs.
In the AI supply chain, we also identify several novel mechanisms through which policy interventions affect
consumers and other participants, arising from its unique co-creation structure. First, pro–price-competitive
policies in downstream markets increase the provider’s incentive to engage in co-creation, leading the
provider to lower the fine-tuning price. This, in turn, improves product quality and enhances consumer sur-
plus. In contrast, pro–quality-competitive policies reduce the provider’s co-creation incentives, leading to an
increase in the fine-tuning price, negatively impacting product quality. Second, while pro–price-competitive
policies reduce product prices and are therefore expected—according to conventional wisdom—to increase
provider profits through reduced double marginalization, they also diminish downstream firms’ incentives
to improve quality. This results in less domain-specific data being used for fine-tuning, reducing fine-tuning
and inference revenue, and ultimately lowering the provider’s profits. Third, the introduction of compute
33

subsidies or a decline in compute costs strengthens the provider’s incentives to engage in co-creation. This,
in turn, encourages the provider to lower the fine-tuning price, motivating downstream firms to invest more in
product quality. This mechanism reflects the unique co-creation dynamics of the AI supply chain, which are
not captured in existing studies on the implications of declining compute costs (Demirhan et al. 2005, 2007).
8.2. Policy Implications
From a practical standpoint, our research provides valuable insights for policymakers seeking to enhance
consumer surplus within the AI supply chain. First, we demonstrate that pro-price-competitive policies and
compute subsidies are not universally effective; their effectiveness depends on the underlying cost conditions
(as shown in Proposition 1 and Proposition 2). This allows policymakers to tailor interventions to specific
market conditions. Importantly, these two policies can complement each other, as each tends to be effective
in situations where the other is not. For instance, in downstream markets dealing with complex, sensitive, and
high-stakes data—such as healthcare and finance (Reddit 2025)—where firms incur high data preprocessing
costs, pro-price-competitive policies may be ineffective or even harmful to consumer welfare, whereas
compute subsidies are likely to provide substantial benefits. In contrast, in markets with relatively low data
preprocessing costs, such as e-commerce, where retailers typically use structured data formats for product
details, offers, pricing, and reviews, making the data easier to preprocess (AWS 2025, van Haasteren 2025),
pro-price-competitive policies can effectively enhance consumer surplus, whereas compute subsidies may
have a more limited impact.
Second, many governments already provide compute subsidies at varying rates. For example, Beijing
offers subsidies covering up to 30% of compute costs, while Shenzhen covers up to 50%. Our results show
that excessively high subsidy rates can be counterproductive: Their effectiveness diminishes and may even
become negative once the subsidy rate exceeds a certain threshold (as shown in Corollary 1). Therefore, our
results offer clear guidance to policymakers on effective subsidy design, suggesting that a moderate subsidy
rate leads to the greatest net increase in consumer surplus.
Third, we find that pro-price-competitive policies and compute subsidies are generally more viable and
more likely to gain support across the AI supply chain than pro-quality-competitive policies (as shown in
Proposition 3). This is because both pro-price-competitive policies and compute subsidies have the potential
to create a “win–win–win” outcome for consumers, downstream firms, and foundation model providers.
While pro-quality-competitive policies always improve consumer welfare, they consistently reduce down-
stream firms’ profits and thus cannot deliver such a mutually beneficial outcome—an important consideration
for regulatory adoption.
Fourth, our analysis highlights the importance of dynamic and adaptive policymaking. As GPUs improve
and compute costs decline, the effectiveness of specific policy tools may evolve (as shown in Corollary 5):
pro-price-competitive policies may shift from effective to ineffective, while compute subsidies may become
34

effective after initially being ineffective. Policymakers should therefore closely monitor cost trends and adjust
their regulatory strategies accordingly, using our framework to navigate evolving technological conditions.
Finally, as compute costs continue to fall, our findings suggest that policymakers should increasingly
emphasize compute subsidies (as shown in Corollary 4 and Proposition 2). In future low-cost environ-
ments, compute subsidies not only effectively increase consumer surplus but also help create a robust
“win–win–win” outcome, making them a particularly promising tool for fostering socially beneficial AI
supply chains.
References
Acemoglu D (2021) Harms of AI. Working paper, National Bureau of Economic Research.
AI Now Institute (2023) Chatgpt and more: Large scale ai models entrench big tech power. Accessed August 11, 2023,
https://ainowinstitute.org/publication/large-scale-ai-models#footnote-list-2.
Anderson A, Hong HG, Jacobs E (2022) Are e-bike subsidies cost effective in mitigating carbon emissions? Working
paper, National Bureau of Economic Research.
Armstrong M, Chen Y (2009) Inattentive consumers and product quality.Journal of the European Economic Association
7(2-3):411–422.
Assad S, Clark R, Ershov D, Xu L (2024) Algorithmic pricing and competition: Empirical evidence from the german
retail gasoline market.Journal of Political Economy132(3):723–771.
Austrian Federal Competition Authority (2024) Artificial intelligence, data and competition – note by austria. Technical
report, Organisation for Economic Co-operation and Development.
AWS (2025) What’s the difference between structured data and unstructured data? Accessed Nov 27, 2025,
https://aws.amazon.com/compare/the-difference-between-structured-data-and-unstructured-data/.
Banker RD, Khosla I, Sinha KK (1998) Quality and competition.Management science44(9):1179–1192.
Basak D, Marjit S, Mukherjee A (2023) Competition and profit in a supply chain. Preprint, submitted August 30,
http://dx.doi.org/10.2139/ssrn.4557289.
Bhati D (2024) Google AI boss says company is investing more than $100 billion in AI to be ahead of its competitors.
Accessed November 30, 2024, https://www.indiatoday.in/technology/news/story/google-ai-boss-says-company-
is-investing-more-than-100-billion-in-ai-to-be-ahead-of-its-competitors-2528722-2024-04-18.
Boggs J (2025) New ftc rule forces ticketmaster to display all prices upfront. Accessed Oct 12, 2025,
https://www.scrippsnews.com/life/money/new-ftc-rule-forces-ticketmaster-to-display-all-prices-upfront.
Bohlmann JD, Golder PN, Mitra D (2002) Deconstructing the pioneer’s advantage: Examining vintage effects and
consumer valuations of quality and variety.Management Science48(9):1175–1195.
Cajueiro DO, Celestino VRR (2025) A comprehensive review of artificial intelligence regulation: Weighing ethical
principles and innovation.Journal of Economy and Technology4:77–91.
35

CCPC (2025) Digital content / services. Accessed Oct 9, 2025, https://www.ccpc.ie/business/help-for-
business/guidelines-for-business/digital-content-services/.
Ceccagnoli M, Forman C, Huang P, Wu D (2012) Cocreation of value in a platform ecosystem! the case of enterprise
software.MIS quarterly263–290.
Cen SH, Hopkins A, Ilyas A (2024a) AI supply chains (and why they matter). Accessed November 7, 2024,
https://aipolicy.substack.com/p/supply-chains-2.
Cen SH, Hopkins A, Struckman I, Videgaray L (2024b) Three proposals for regulating AI. Accessed November 7,
2024, https://aipolicy.substack.com/p/supply-chains-5.
Chen H, Chen H, Zhao Z, Han K, Zhu G, Zhao Y, Du Y, Xu W, Shi Q (2026) An overview of domain-specific foundation
model: key technologies, applications and challenges.Science China Information Sciences69(1):111301.
Competition and Markets Authority (2023) AI Foundation Models: Initial Report. Accessed June 21, 2025,
https://assets.publishing.service.gov.uk/media/65081d3aa41cc300145612c0/Full report .pdf.
Competition Bureau (2024) Artificial intelligence and competition. Accessed August 30, 2024, https://competition-
bureau.canada.ca/en/how-we-foster-competition/education-and-outreach/artificial-intelligence-and-
competition.
Competition Bureau Canada (2025) Report on summit 2024: Competition in the ai era. Accessed Oct
12, 2025, https://competition-bureau.canada.ca/en/how-we-foster-competition/education-and-outreach/report-
summit-2024-competition-ai-era.
CompTIA (2025) What is SaaS? Accessed May 15, 2025, https://www.comptia.org/content/articles/what-is-saas.
Demirezen EM, Kumar S, Shetty B (2020) Two is better than one: A dynamic analysis of value co-creation.Production
and operations management29(9):2057–2076.
Demirhan D, Jacob VS, Raghunathan S (2005) Information technology investment strategies under declining technology
cost.Journal of Management Information Systems22(3):321–350.
Demirhan D, Jacob VS, Raghunathan S (2007) Strategic it investments: The impact of switching cost and declining it
cost.Management Science53(2):208–226.
Design Gurus (2025) Is OpenAI a SaaS company? Accessed Feb 24, 2025,
https://www.designgurus.io/answers/detail/is-openai-a-saas-company.
Diehl S (2025) Introduction to fine-tuning large language models. Accessed June 1, 2025,
https://www.stephendiehl.com/posts/training llms/?utm source=chatgpt.com.
Dreyer C (2025) 15 best legal ai tools in 2025: Features, pricing & how to choose. Accessed Oct 12, 2025,
https://rankings.io/blog/legal-ai-tools/.
Eldridge M (2025) The limitations of ai in legal operations: Why technology alone won’t solve all legal challenges.
Accessed Oct 12, 2025, https://www.acc.com/resource-library/limitations-ai-legal-operations-why-technology-
alone-wont-solve-all-legal.
36

FCC (2025) Fcc requires broadband providers to display labels to help consumers. Accessed Oct 12, 2025,
https://www.fcc.gov/document/fcc-requires-broadband-providers-display-labels-help-consumers.
Fisher S (2024) 10 top ai companies in law. Accessed November 30, 2024, https://www.vktr.com/ai-market/10-top-ai-
companies-in-law/.
FTC (2025) Anticompetitive practices. Accessed May 30, 2025, https://www.ftc.gov/enforcement/anticompetitive-
practices#.
FTC (2025a) Federal trade commission announces final rule banning fake reviews and testimonials. Accessed Oct
12, 2025, https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-
final-rule-banning-fake-reviews-testimonials.
FTC (2025b) Ftc announces crackdown on deceptive ai claims and schemes. Accessed May
30, 2025, https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-
claims-schemes.
FTC (2025c) Ftc sends refunds to consumers affected by fashion nova’s deceptive review practices. Accessed Oct
12, 2025, https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-sends-refunds-consumers-affected-
fashion-novas-deceptive-review-practices.
FTC (2025d) The rule on unfair or deceptive fees: Frequently asked questions. Accessed Oct 12, 2025,
https://www.ftc.gov/business-guidance/resources/rule-unfair-or-deceptive-fees-frequently-asked-questions.
Government of Canada (2024) Promotion and advocacy. Accessed November 7, 2024, https://competition-
bureau.canada.ca/how-we-foster-competition/promotion-and-advocacy.
Guo P (2009) A survey of software as a service delivery paradigm.TKK T-110.5190 Seminar on Internetworking, 1–3.
Guo Z, Ma D (2018) A model of competition between perpetual software and software as a service.MIS Quarterly
42(1):101–120.
Gupta S, Roy A, Kumar S, Mudambi R (2023) When worse is better: Strategic choice of vendors with differentiated
capabilities in a complex cocreation environment.Management Science69(5):2833–2851.
Hrdy AS, Ceccio J, Zeytoomian C (2025) FTC Moves to Expand AI Deployment Oversight with Operation AI Com-
ply. Accessed May 30, 2025, https://www.morganlewis.com/pubs/2024/10/ftc-moves-to-expand-ai-deployment-
oversight-with-operation-ai-comply.
Huizenga E (2025) Fine-tuning gemini: Best practices for data, hyperparameters, and evaluation. Accessed
May 16, 2025, https://medium.com/google-cloud/fine-tuning-gemini-best-practices-for-data-hyperparameters-
and-evaluation-65f7c7b6b15f.
Insights A (2024) Training AI Models with OpenAI API: How to Handle Large Datasets and GPU Usage.
Accessed November 30, 2024, https://medium.com/muthoni-wanyoike/training-ai-models-with-openai-api-how-
to-handle-large-datasets-and-gpu-usage-9f1bbcfba38f.
37

ITSoli (2025) The future of custom llm fine-tuning: Trends to watch. Accessed Apr 29, 2025, https://itsoli.ai/the-future-
of-custom-llm-fine-tuning-trends-to-watch/.
Jiang Z, Qu XS, Jain DC (2019) Optimal market entry timing for successive generations of technological innovations1.
MIS quarterly43(3):787–806.
Karanika V (2013) The cloud, mobility and beyond. Accessed January 28, 2023,
https://www.cisco.com/c/dam/global/el gr/assets/connect2013/pdfs/015 idc evangelos karanikas.pdf.
Kardach J (2024) Fine-tuning LLMs for Your Industry: Optimal Data Labeling Strategies. Accessed November 30,
2024, https://www.toptal.com/artificial-intelligence/llm-data-labeling.
Kim B, Chen P, Mukhopadhyay T (2009) An economic analysis of the software market with a risk-sharing mechanism.
International Journal of Electronic Commerce14(2):7–40, ISSN 1086-4415.
Leblanc T, Dailard S, Leavy K, Velez N (2025) FTC Warns to ‘Keep Your AI Claims in Check’ in New AI Guidance.
Accessed May 30, 2025, https://cdp.cooley.com/ftc-warns-to-keep-your-ai-claims-in-check-in-new-ai-guidance/.
Ma D, Kauffman RJ (2014) Competition between software-as-a-service vendors.IEEE Transactions on Engineering
Management61(4):717–729.
Ma D, Seidmann A (2015) Analyzing software as a service with per-transaction charges.Information Systems Research
26(2):360–378.
Mahari R, Pentland A (2024) Regulation by design: A new paradigm for regulating ai systems. Preprint, submitted
April 2, https://ssrn.com/abstract=4753029.
Matsushima N (2006) Industry profits and free entry in input markets.Economics Letters93(3):329–336.
Menear H (2024) Large language models could drive the next industrial revolution. Accessed August 30, 2024,
https://interface.media/blog/2024/05/07/large-language-models-could-drive-the-next-industrial-revolution/.
Mohammadi B, Malik N, Derdenger T, Srinivasan K (2024) Regulating explainable artificial intelligence (xai) may
harm consumers.Marketing Science.
Muller J, Kruger J, Enderlein S, Helmich M, Zeier A (2009) Customizing enterprise software as a service applica-
tions: Back-end extension in a multi-tenancy environment.Enterprise Information Systems: 11th International
Conference, ICEIS 2009, Milan, Italy, May 6-10, 2009. Proceedings 11, 66–77 (Springer).
Munappy AR, Bosch J, Olsson HH, Arpteg A, Brinne B (2022) Data management for production quality deep learning
models: Challenges and solutions.Journal of Systems and Software191:111359.
Narayanan D, Shoeybi M, Casper J, LeGresley P, et al. (2021) Efficient large-scale language model training on gpu
clusters using megatron-lm.Proceedings of the International Conference for High Performance Computing,
Networking, Storage and Analysis, 1–15.
Ngo V (2025) Challenges of product analytics in the era of generative ai. Accessed Oct 12, 2025,
https://medium.com/@vuongngo/challenges-of-product-analytics-in-the-era-of-generative-ai-3abf42a44e76.
38

NVIDIA (2024) Artificial intelligence. Accessed November 7, 2024, https://www.nvidia.com/en-us/glossary/artificial-
intelligence/.
OpenAI (2023) Fine-tuning. Accessed August 11, 2024, https://platform.openai.com/docs/guides/fine-tuning.
OpenAI (2024a) Harvey. Accessed November 30, 2024, https://openai.com/index/harvey/.
OpenAI (2024b) Pricing. Accessed August 22, 2024, https://openai.com/api/pricing/.
Osman J (2024) Can Nvidia’s ‘Hyper Moore’s Law’ Spark An AI Revolution? Forbes (November 7),
https://www.forbes.com/sites/jimosman/2024/11/07/can-nvidias-hyper-moores-law-spark-an-ai-revolution/.
Precedence Research (2025) Artificial Intelligence (AI) Market Size. Accessed August 11, 2025,
https://www.precedenceresearch.com/artificial-intelligence-market.
Puyang X, Gu Z, Chen RR, Li J (2025) Vertical competition on a common platform.Marketing Science.
Rami Ali (2025) Profitability forecasts: What they are and how to create them. Accessed Apr 25, 2025,
https://www.netsuite.com/portal/resource/articles/financial-management/profitability-forecast.shtml.
Reddit (2025) What industry has the worst data? Accessed Nov 27, 2025,
https://www.reddit.com/r/MachineLearning/comments/1eyj7vq/d what industry has the worst data/.
Reuters T (2024) Gpt-4 alone is not a reliable legal solution—but it does enable one. Accessed
November 30, 2024, https://casetext.com/blog/cocounsel-harnesses-gpt-4s-power-to-deliver-results-that-legal-
professionals-can-rely-on/.
Robinson B (2025) Consumer protection in the age of ai: The ftc’s approach to ai regulation. Accessed Oct 9, 2025,
https://iapp.org/news/a/consumer-protection-in-the-age-of-ai-the-ftcs-approach-to-ai-regulation.
Sastry G, Heim L, Belfield H, Anderljung M, Brundage M, Hazell J, O’Keefe C, Hadfield GK, Ngo R, Pilz K, et al.
(2024) Computing power and the governance of artificial intelligence.arXiv preprint arXiv:2402.08797.
Schneier B (2015) Should companies do most of their computing in the cloud? (part 1). Accessed June 28, 2025,
https://www.schneier.com/blog/archives/2015/06/should companie.html.
Schultz C (2009) Transparency and product variety.Economics Letters102(3):165–168.
Sharma S, Mehra A (2021) Entry of platforms into complementary hardware access product markets.Marketing
Science40(2):325–343.
Shaver N (2025) The use of large language models in legaltech. Accessed Mar 26, 2025,
https://www.legaltechnologyhub.com/contents/the-use-of-large-language-models-in-legaltech/.
Singh N, Vives X (1984) Price and quantity competition in a differentiated duopoly.The Rand journal of economics
546–554.
Singh S (2024) Beginner’s Guide: Using Foundation Models in ML Projects. Accessed November 30, 2024,
https://www.labellerr.com/blog/beginners-guide-using-foundation-models-in-ml-projects/.
39

Stryker C (2025) What is a pretrained model? Accessed July 20, 2025, https://www.ibm.com/think/topics/pretrained-
model.
Sun C, Ji Y, Geng X (2023) Which enemy to dance with? a new role of software piracy in influencing antipiracy
strategies.Information Systems Research34(4):1711–1727.
Sun C, Shi Z, Liu X, Ghose A (2025) The effect of voice ai on digital commerce.Information Systems Research
36(2):1147–1166.
Sun W, Zhang X, Guo CJ, Sun P, Su H (2008) Software as a service: Configuration and customization perspectives.
2008 ieee congress on services part ii (services-2 2008), 18–25 (IEEE).
Tirole J (1988)The theory of industrial organization(MIT Press).
Tsay AA, Agrawal N (2000) Channel dynamics under price and service competition.Manufacturing & Service
Operations Management2(4):372–391.
Tucker C (2024) How does competition policy need to change in a world of artificial intelligence?Oxford Review of
Economic Policy40(4):834–842.
Tyagi RK (1999) On the effects of downstream entry.Management science45(1):59–73.
van Haasteren R (2025) The 9 essential ecommerce structured data types. Accessed Nov 27, 2025,
https://www.siteguru.co/seo-academy/ecommerce-structured-data?utm source=chatgpt.com.
Vijairaghavan V, Hidaji H, Nault BR (2025) Consequences of resorting to fines and investments to regulate data
portability.Management Science.
Vohra DK (2024) 5 Real-world Applications of Large AI Models. Accessed November 30, 2024,
https://www.hyperstack.cloud/blog/case-study/real-world-applications-of-large-ai-models.
Wang Q, Huang Y, Jasin S, Singh PV (2023) Algorithmic transparency with strategic users.Management Science
69(4):2297–2317.
Wang Z, Guo H, Liu D (2024) Economics of analytics services on a marketplace platform.MIS Quarterly48(2).
Wikipedia (2023) GPT-4. Accessed August 10, 2023, https://en.wikipedia.org/wiki/GPT-4#citenote-30.
Wu D (2024) Chinese cities offer subsidies to boost access to the computing power needed for AI. South China
Morning Post (December 27), https://www.scmp.com/economy/china-economy/article/3292478/chinese-cities-
offer-subsidies-boost-access-computing-power-needed-ai.
Wu Y, Zhu F (2022) Competition, contracts, and creativity: Evidence from novel writing in a platform market.
Management Science68(12):8613–8634.
Yanbc (2024) How are GPU infrastructures managed at OpenAI. Accessed November 30, 2024,
https://www.yanbc.info/how-are-gpu-infrastructures-managed-at-openai.
Yang M, Jacob VS, Raghunathan S (2021) Cloud service model’s role in provider and user security investment
incentives.Production and Operations Management30(2):419–437.
40

Yenipazarli A (2021) Downstream entry revisited: Economic effects of entry in vertically-related markets.Omega
103:102428, ISSN 0305-0483.
Zhang Z, Nan G, Tan Y (2020) Cloud services vs. on-premises software: Competition under security risk and product
customization.Information Systems Research31(3):848–864.
Zhao S, Liu B, Wang F, Feng D (2021) Bridging the gap between memory and communication efficiency on distributed
deep learning systems.IEEE Access9:57075–57088.
41
