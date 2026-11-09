---
title: Industry Influence in High-Profile Social Media Research
url: https://arxiv.org/abs/2601.11507
category: social-media
subcategory: empirical
date: 2026-01
venue: ''
authors:
- Joseph Bak-Coleman
- Jevin West
- Cailin O'Connor
- Carl T. Bergstrom
source: arxiv
pdf_url: https://arxiv.org/pdf/2601.11507
pages: 11
chars: 38664
fetched_at: '2026-11-08T13:06:04+00:00'
kb_version: 1
---

# Industry Influence in High-Profile Social Media Research

INDUSTRYINFLUENCE INHIGH-PROFILESOCIALMEDIA
RESEARCH
A PREPRINT
Joseph Bak-Coleman1,2,3,4,5∗, Jevin West6,7,
Cailin O’Connor8,9, andCarl T. Bergstrom 1,2,7
1Department of Biology, University of Washington, Seattle, W A, USA
2Santa Fe Institute, Santa Fe, NM, USA
3Centre for the Advanced Study of Collective Behavior, University of Konstanz, Germany
4Department of Collective Behavior, Max Planck Institute of Animal Behavior, Germany
5Berkman Klein Center, Harvard University, Cambridge, MA, USA
6Information School, University of Washington, Seattle, W A, USA
7Center for an Informed Public, University of Washington, Seattle, W A, USA
8Department of Logic and Philosophy of Science, UC Irvine, Irvine, CA, USA
9Center for Socially Engaged Philosophy, UC Irvine, Irvine, CA, USA
∗To whom correspondence should be addressed; E-mail:jbakcoleman@gmail.com
January 19, 2026
ABSTRACT
To what extent is social media research independent from industry influence? Leveraging openly
available data, we show that half of the research published in top journals has disclosable ties to
industry in the form of prior funding, collaboration, or employment. However, the majority of
these ties go undisclosed in the published research. These trends do not arise from broad scientific
engagement with industry, but rather from a select group of scientists who maintain long-lasting
relationships with industry. Undisclosed ties to industry are common not just among authors, but
among reviewers and academic editors during manuscript evaluation. Further, industry-tied research
garners more attention within the academy, among policymakers, on social media, and in the news.
Finally, we find evidence that industry ties are associated with a topical focus away from impacts of
platform-scale features. Together, these findings suggest industry influence in social media research
is extensive, impactful, and often opaque. Going forward there is a need to strengthen disclosure
norms and implement policies to ensure the visibility of independent research, and the integrity of
industry supported research.
KeywordsSocial Media·Industry Influence·Metascience
Introduction
The proliferation and infusion of social media into daily life has raised concerns about its wide-ranging, and at
times harmful, psychological and sociological effects [1–6]. Scientists studying those effects are largely dependent
on platforms for access to data, on-platform experiments, and even basic information about platform design and
functionality [7–9]. This relationship between science and industry raised fears among early computational social
scientists of a future in which the field was characterized by, “a privileged set of academic researchers presiding over
private data from which they produce papers that cannot be critiqued or replicated [10].” Such a scenario, the authors
argued, would make it difficult to accumulate knowledge and verify findings. These fears are especially salient for
arXiv:2601.11507v1  [cs.SI]  16 Jan 2026

Industry Influence in High-Profile Social Media ResearchA PREPRINT
research into potential harms of social media, where industry may have incentives to suppress inconvenient discoveries
or redirect scientific attention away from fraught topics [6, 9].
Historically, industries producing products that cause harm have successfully redirected scientific research through
various techniques [11–15]. At the scale of individual studies, evidence across a wide range of scientific contexts
has consistently demonstrated that research linked to industry exhibits bias towards industry-preferred outcomes [11,
16–19]. Notably, this biasing effect can occur without fraudulent research or nefarious industry interference, emerging
instead from simple misalignment of incentives [9]. For example, industry actors may selectively supports scientists
whose research topics and methods tend to yield findings favorable to industry, biasing the larger scientific record [9,
20, 21].
Despite the potential for industry influence on the study of social media, its extent of such remains poorly character-
ized. Here, we leverage public data to evaluate these influences in high-profile social media research. We begin by
characterizing the degree to which published research is tied to industry, and whether such ties are made visible by
competing interests policies. We further examine the relative impact of industry connected and independent research in
terms of citations and public attention. Next, we examine authors’ ties to industry, quantifying the breadth of industry
ties, the degree to which firms selectively invest in specific researchers, and the independence of high profile scientists
in the field. We then examine how ties to industry enter the process of evaluating manuscripts by way of editors and
peer-reviewers. Finally, we reveal topical biases in research associated with industry.
Methods
We queried OpenAlex [22] to identify a core corpus of research articles on social media published inScience,Nature,
andPNAS, as well as their common transfer journals (i.e.PNAS Nexus,Science Advances,Nature Communications
andNature Human Behavior). We focused on these journals given their broad readership and role as hubs for
interdisciplinary research on the effects of social media. Narrowing our focus to specific journals also enabled us to
tailor our analyses to their specific competing interest policies and to manually validate industry ties (See SI Sec. S2).
We searched for all articles mentioning Social Media, LinkedIn, Facebook, Instagram, Youtube, WhatsApp, or Twitter
in their title or abstract, leveraging the bibliographic coupling network to identify a core corpus of research articles (See
SI Sec. S1 ) Our corpus comprises 295 articles published by 1210 unique authors.
For each author, we identified any year in which they received funding from, collaborated with employees of, or were
employed by one of four technology companies that own and operate one or more social media platforms: Meta, X,
Google, and Microsoft (Supplementary Information Table S1). We identified these ties using data from OpenAlex as
well as through industry-announced RFPs and fellowships. We manually validated every funding and employment
tie using sources independent from OpenAlex. Details can be found in our supplement (Sec. S2). We refer to these
industry links as “disclosable ties” throughout, as it enables us to distinguish them from competing interests, which may
be more expansive.
We categorized an article as possessing a disclosable tie if at least one of the authors had a detected connection to
industry within the journal’s specified period for competing interests: three years forNature, four years forPNAS,
and five years forScience[23–25]. We note that under this definition, funding from one firm would be considered
a disclosable tie regardless of whether that firms’ platform is explicitly mentioned in the paper. This definition is
appropriate as studies about a competitor’s products would warrant disclosure, and discussions of social media generally
may impact all firms. To evaluate impact, we combined our data from OpenAlex with data from Altmetrics. Finally, to
evaluate whether journal editors had disclosable interests, we applied the detection methods above and further examined
their publicly posted CVs when available.
Although modest in size, our corpus has had a large impact. As of November 6th, 2025, papers therein have garnered a
cumulative Altmetric attention score of 154623. Within the academy, the work has been cited 53120 times, averaging
180 citations per paper. Among the public, the literature in our corpus has been mentioned in 15708 news articles,
resulting in 100863 mentions on social media. This body of work has been mentioned 418 times on Wikipedia and
has been referenced in 745 policy documents. The authors within the corpus are influential as well, with a cumulative
7.1 million citations. As such, the research and researchers examined here likely play an out-sized role in shaping the
direction of the field, and broader understandings of social media.
2

Industry Influence in High-Profile Social Media ResearchA PREPRINT
Results
Literature
Social media firms possess an outsize capacity for internally producing scientific research, given their access to data,
sole capacity to run platform-wide experiments, and teams of scientists on staff [9]. Consequently, research they
produce alone or in collaboration with academic researchers often provides novel insights and appears in high-profile
venues [7, 26]. In our corpus, 8% (95% CR: [5%, 12%]) of articles indicate industry-affiliated employees among the
authors (Fig. 1A).
Competing interests statements are a key mechanism by which authors with academic employment can transparently
report relevant ties to industry. Our manual review of the literature reveals that explicit declarations of competing
interests are uncommon, appearing in 13% [10%, 17%] of the publications in our corpus (Fig. 1A). Beyond competing
interest statements, some authors disclose ties to industry elsewhere such as in funding or acknowledgment statements.
We refer to ties that can be identified anywhere in a published article as “identifiable.” Between affiliations, competing
interest statements, and other locations in the manuscript 20% [15%, 25%] of papers were identifiably linked to industry
(Fig. 1A).
However, these transparency mechanisms rely entirely on voluntary disclosure by authors, raising the possibility that
some ties go undisclosed. Based on public data, we found disclosable ties for 49% [43%, 55] of published work,
meaning fewer than half of works with diclosable ties in fact disclosed them (Fig. 1A). Even among the 227 publications
in our corpus which explicitly declared no competing interests, we found that 42% [36%, 49%] nonetheless did have
disclosable ties to industry (SI Fig S1, Table S4).
Competing interests vary in nature. We categorized disclosable ties into employment, collaboration, and funding. Of
these types, prior collaboration was most common, followed by funding, with employment being relatively rare (Fig.
1B). Similar frequencies of connection type were observed among both research that identified existing links to industry
and papers which failed to do so. This suggests that failures to disclose are not related to norms surrounding the type of
tie, such as disclosing funding yet not collaboration or employment (Fig. S2). Viewed over time, our data reveal an
overall increase in the volume of social media research, with an uptick in proportion of papers tied to industry beginning
in 2020 (Fig, 1C). We find no clear indication that the probability of disclosure for competing interests has increased
over time (Bayesian Binomial Regression,β=0.01 [-0.107, 0.133], SI Fig. S3).
To further assess the impact of industry on both scientific and public belief, we leveraged Altmetric data, which
tracks online engagement with scientific papers within and beyond the academy. This approach revealed that industry-
connected research garners approximately twice the impact of independent work on average (Fig. 1D, SI Table S7).
Industry-connected work receives more citations within the academy, is more frequently referenced in policy documents,
more often discussed on social media and the news, and is more likely to be referenced on Wikipedia. It is unclear
the degree to which this impact is attributable to unique access to data, industry PR campaigns, characteristics of the
funded researchers, or some other cause. Nevertheless, these results indicate that industry-tied research has an outsized
influence on our understanding of social media.
Authors
We next evaluated how these patterns of industry connection are reflected among authors in the field. A total of 1210
distinct authors were listed among the publications in our corpus. While half of publications have discernable links to
industry, most individiual authors do not, with only 21% [19, 23] having one or more found disclosable tie (SI Table
S14). In our author-scale analysis, as with the paper-level analysis, collaboration and funding were more common as
sources of disclosable ties than were current or past employment (Fig 2A).
Our analysis additionally revealed differences across firms in their breadth of engagement with the academy (Fig 2C, SI
Table S15). Ties to Meta were most common among authors in our corpus (14% [12, 16], Fig 2B). Google (8% [7, 10])
and Microsoft (6% [5, 7]) trailed behind, and very few authors had connections to X (1 % [0, 2]). Finally, 7 % [6, 8] of
authors engaged with more than one firm.
Historically, industries seeking to influence science have invested selectively and heavily in industry-favorable re-
searchers, or those who work on industry-favorable topics [11, 27]. There is evidence that large technology companies,
like Google, have attempted to select and groom friendly academics to push research in favorable directions [6]. To
evaluate whether industry invests broadly or selectively, we calculated the number of years each author was funded by
or collaborated with industry, summed across firms (See SI Sec. S3.2). This metric provides an estimate of the longevity
and breadth of industry support an individual scientist received. Across our 1210 authors, the average company-years of
support was 1.27[1.05, 1.55] years with a maximum of 33 company-years. For this metric, the Gini coefficient is 0.919,
3

Industry Influence in High-Profile Social Media ResearchA PREPRINT
Figure 1: Article-level descriptive statistics.A)Disclosable ties that were either indicated by author affiliation
(Industry), indicated in competing interest statements (Disclosed), found somewhere in the manuscript (Identifiable),
found through our broader search (Found), or any combination of the above (Any).B)Percentage of papers with various
sorts of disclosable industry connectionsC)Time-series of total articles with various disclosable tiesD)Comparison of
altmetric and citation impact. Values indicate the relative impact of papers with disclosable ties compared to research
presumed to be independent. Vertical lines indicate 95% credible regions.
4

Industry Influence in High-Profile Social Media ResearchA PREPRINT
suggesting consistent industry collaboration and funding is highly concentrated among a small number of academics
(Fig. 2C). Indeed, the top 10% of authors account for 79.0% of total industry investment by this metric.
Figure 2: Author-level descriptive statistics.A)The percentage of authors possessing a given type of tie to industry.B)
The percentage of authors engaging with each firmC)Lorenz curve showing inequality in access to industry funding
and collaboration, as measured in total years of funding and collaboration per firmD)Rate of disclosure as a function
of the number of years in which an author was employed by, funded by, or collaborated with industry. Shaded bands
correspond to the 50, 75, 89, and 95% credible regions for the expected probability.E)The probability of an author
having at least one disclosable tie as a function of the number of papers on social media published in high-profile
journals.
We found little indication that authors with longer-standing ties to industry have higher per-paper probabilities of
declaring relevant ties as competing interests (β= 0.161 [-0.026, 0.366] (Fig. 2D, SI Table S17). For example, ten
years of industry funding and collaboration are associated with a per-paper disclosure rate of around 58% [53, 63]: an
absolute increase of 6% [-2, 14] above the disclosure rates of researchers with a single year’s association.
Finally, we examined the association between academic profile in the field, proxied by number of high-profile
publications on social media research, and relationships to industry. A Bayesian logistic regression indicated authors
with 3 or more papers in these journals are likely to have disclosable ties, and authors with six or more almost invariably
do (β= 0.71 [0.56, 0.87], Fig. 2E, SI Table S18). As such, there appear to be few fully independent researchers whose
work on social media is routinely accepted and published in top journals.
5

Industry Influence in High-Profile Social Media ResearchA PREPRINT
Editors and Reviewers
High-profile scientists within a discipline serve as important gatekeepers in positions as academic editors and peer
reviewers. Our results above suggest high-profile authors in social media research typically have longstanding ties to
one or more social media companies. To the extent that these authors’ perspectives, preferences and priorities align with
industry interests, their gatekeeper roles could extend industry influence to research produced by independent authors.
To prevent such effects, editors and reviewers are typically required to disclose competing interests before handling a
manuscript; conflicts may warrant recusal.
Figure 3:A)The probability that an editor has a disclosable tie to industry as a function of the number of social media
papers handledB)For papers, the probability that a paper with an academic editor has editor ties, author ties, both, or
either
Given the lax disclosure norms in this area, we sought to determine whether industry ties go undisclosed in evaluating
manuscripts. We identified 80 academics serving as editors for 167 manuscripts (See SI Sec. S3.3). Editors were nearly
twice as likely as authors in the field more broadly to have at least one disclosable tie, at 34% [23, 43]. Moreover,
editors who handled a larger number of social media papers in our corpus were more likely to possess a disclosable tie
to industry (β=0.311 [0.084,0.589], Fig. 3A, SI Table S19). Overall, a third (35% [27, 42]) of papers with academic
editors in our corpus were handled by an editor with ties to industry that occurred within the journals’ time-frame for
disclosure. None these ties were formally disclosed in the published research.
Combined with our data on authors, we find that only a minority of research published (34% [27, 42]) is entirely
free from disclosable ties by authors or editors, where as the majority (66% [58, 73]) possess editorial or authorial
disclosable ties, or both (Fig. 3B, table to add).
Beyond ties to industry, editors are expected to recuse themselves from handling collaborators’ research. In our dataset,
however, 11% [5, 18] of papers handled by industry-tied editors were written by their ongoing (i.e., published the
same-year) or recent (i.e., within four years) co-authors. Handling of co-author manuscripts appears to be exclusive
to industry-tied editors (β= 1.641 [0.424, 2.95]). We identified no examples of independent editors handling their
co-authors’ research.
Our data on the literature and authors relied solely on identification of funding ties through past disclosures in
published research as well as public annoucements of awards from two platforms (Meta and Google). This approach is
conservative; some academics may receive funding that is neither made public by companies nor disclosed in resultant
publications. Our data on editors, however, is supplemented with CVs, which can include funding not awarded through
an RFP and which does not result in linked published work. As such, comparing the CVs to public data can provide an
estimate of the degree to which received funding is indicated in public data and detectable through our approach.
Overall, only 14% [5, 25] of years in which academic editors were funded by a given company were identifiable through
published funding declarations or in public lists of recipients of industry awards. This remarkably low sensitivity
suggests that the saturation we reconstruct from public data is highly conservative, and potentially based on only a
fraction of total industry influence. However, the high concentration of industry support among a select set of authors
may render many of these undetected ties as redundant for the purposes of our analyses above. Most of the years of
funding not found in public data most were attributable to Meta and Google (Meta: 61% [46, 76] and Google: 32% [18,
47]). Only a small portion of missing years were funded by Microsoft 8% [1, 16] and none were funded by X.
6

Industry Influence in High-Profile Social Media ResearchA PREPRINT
Peer reviewer identities are not typically made public. However, some publications listed reviewers who were willing to
disclose their identities in the interests of transparency. Such disclosures are uncommon in our corpus, with 82 named
reviewers across 49 papers. We were able to identify disclosable ties with reviewers’ CVs, when available. Overall,
29.9% [19.9, 39.9] of these reviewers had sufficiently recent ties to industry to warrant disclosure per journal policies. It
is unclear whether these ties were disclosed to editors during peer review, however none were disclosed in the published
literature.
Combining our findings throughout this paper we can estimate theindustrial saturationof the literature—the proportion
of papers with ties to industry either through authorship or evaluation process. Of the 295 papers in our corpus, 194
have known ties via authors or editors. For the remaining, we can leverage the rates of disclosable ties among named
reviewers to estimate the probability that at least one (of two, conservatively) anonymous reviewers has a disclosable
tie. Doing so leads to a corpus-wide estimate of 79.9%[74.05, 85.43] saturation. In other words, no more than one out
of every five high profile social media publication is expected to be independent of industry influence in production and
evaluation.
Topical Bias
A key risk of industry influence is the redirection of research priorities towards industry-preferred topics, methods,
causal mechanisms, or perspectives [20, 21]. In the case of social media research, one worry is that industry directs
attention to other potential causes of harms created by their platforms, especially by focusing on user choices rather
than algorithmic or platform design effects [9]. To evaluate the potential for redirection of this general sort, we applied
community detection to the bibliographic coupling network, and identified five communities ranging from 31 to 82
papers (SI Sec. S3.4). Topical analysis indicated that each community corresponded to distinct themes in social media
research which we have labeled misinformation sharing, platform dynamics, mental health, social network analysis, and
political behavior (SI Table S20).
Our results above suggest that 49% of published research in this area is tied to industry. In the absence of topical
bias by industry, we’d anticipate similar proportions across each of these domains. For mental health, social network
analysis, and political behavior, the relative abundance of independent and industry-tied work is consistent with this
expectation (Fig 4A, SI Table S21). We find an over-abundance of industry connection in the cluster of research focused
on misinformation sharing. By contrast, industry connections are sparse in the the cluster related to platform dynamics.
In a supplemental analysis we examined relative word frequencies within abstracts and found that the community with
stronger ties to industry tended to focus on more on experiments related to people sharing false news headlines (SI Fig.
S4). By contrast, terms emphasizing network structure and dynamics were linked to the comparatively independent
topic.
Figure 4:A)Proportion of papers with ties to industry across the five topical communities identified by bibliographic
couplingB)Dots indicate per-paper relative impact of the industry-connected misinformation sharing group and the
more independent platform dynamics group. Vertical lines indicate 95% Credible regions.
7

Industry Influence in High-Profile Social Media ResearchA PREPRINT
While we cannot definitively show that industry funding in this area is redirecting attention from products to consumers,
our results are consistent with this possibility. It is especially notable that research into platform dynamics—which
should be likely to reveal potential harms from platforms themselves—is underfunded by industry.
Additionally, we find that work within the misinformation sharing cluster garners half as many per-paper citations as
that in the platform dynamics cluster. This suggests that this work is of lesser interest within the scientific community
(Fig. 4B). However, there are nearly twice as many papers in the misinformation sharing category, possibly as a result
of industry funding disparities (Table S28). As a result the misinformation cluster ends up with similar total number of
academic citations as the platform dynamics cluster. In addition, in part due to the volume of papers, the total sum of
public engagement is considerably larger for the misinformation sharing topic (SI Table S20, S29). In other words,
industry support may be translating to impact both within and without the academy for research on misinformation
sharing.
Discussion
Within high profile social media literature only one in five papers indicate any ties to industry. However, we find that
half of this body of literature has discernible ties to industry. Once we consider ties from reviewers and editors as well
as authors, we find precisely the opposite of what disclosure statements suggest: only one in five papers are likely to
have remained independent of industry throughout the entire production and evaluation process. These findings indicate
that industry influence in high-profile media research is widespread but under-disclosed. Furthermore, research linked
to industry exhibits topical bias, and has outsized impact within and beyond the academy. As the field’s founders feared,
these patterns of influence arise from long-lasting relationships between a small group of selected scientists and social
media firms. These industry-tied academics disproportionately publish in high profile venues and are represented in key
gatekeeping roles as editors and peer-reviewers.
In this social media research, weak disclosure norms and failures to adhere to existing disclosure policies not only
obscure industry influence but also make it difficult to identify independent research. In other disciplines where
collaboration between industry and academia is commonplace, strong disclosure norms are recognized as essential for
mitigating bias, improving trust in science, and ensuring the integrity of manuscript evaluation [28–32]. Disclosures
also allow funding agencies to offset industry bias by targeting independent researchers, and empower editors to
solicit independent evaluations of industry-tied research [27]. At a minimum, our results highlight a need to correct
the existing scientific literature and strengthen disclosure norms going forward [6]. Authors and journals may wish
to issue corrections to address failed disclosures in the existing literature. Independent authors may choose to go
beyond boilerplate statements such as “the authors declare no competing interests" and explicit describe their lack
of entanglements, for example “the authors have no competing interests in the form of funding, collaboration, or
employment with any social media company."
By focusing on a modestly-sized corpus of high profile research we were able to ensure the accuracy of our data by
manually verifying all industry ties. However, this approach comes with several limitations. In particular, it is unclear
whether these results extend to lower profile, discipline-specific venues. In computer science, existing research suggests
extensive industry influence, yet little is known for other fields [6, 33, 34]. Another limitation is that our approach
is unable to address causal questions about the mechanisms underlying the patters we have observed. It is unclear,
for example, whether a scientist’s high profile leads to the formation of industry ties, or vice versa. Similarly, it is
not clear whether topical bias arises because industry connections shift individual scientists’ research priorities, or
because industry selectively supports scientists whose preexisting priorities and commitments are well aligned with
their interests [27]. Moreover, our analysis of bias is limited to broad topical bias. Future work is needed to provide
more fine-grained analysis of bias among framings and findings, particularly within, rather than across, topics.
Finally, we stress that our reliance on public data limits our ability to detect ties not surfaced in that data, such as
unrestricted gifts, stock ownership, employment that does not produce publications, board membership, unpublished
collaborations, and consulting. As such, our estimates should be viewed as a conservative lower bound of industry
influence in high profile social media research. It is likely that total influence is greater than our results indicated.
Declarations
Ethics Approval
University of Washington’s HSD determined that this study does not constitute research, as defined by federal and state
regulations.
8

Industry Influence in High-Profile Social Media ResearchA PREPRINT
LLM Use Statement
Beyond basic orthographic and thesaural queries, generative AI was not used in drafting any part of this manuscript’s
text.
Data A vailability Statement
While our data are drawn entirely from publicly available sources, we are not releasing the data set because it is not
possible to adequately de-identify individuals represented therein.
Code A vailability Statement
The core of our code is sufficient to reproduce our data, raising the same concerns. To balance these concerns with
transparency, we provide extensive descriptions of all statistical models sufficient to recreate them in the supplement.
Competing Interests
J.B. has engaged in paid consulting for the United Nations on topics related to social media and technology and declares
no competing interests with regard to any company that owns or operates a social media platform. C.B. and J.W.
attended the Social SciFoo conference in 2021 and J.W. attended Social SciFoo conference in 2023; Google and Meta,
respectively, covered the accommodations for participants. In 2022, C.B. and J.W. gave a paid talk at Amazon’s finance
division about data reasoning. J.W. was senior personnel on a $50k Meta grant in 2018 supporting crisis informatics in
conflict zones, but he received no funding for this work. The Center for an Informed Public at UW, of which J.W. and
C.B. are affiliated, has received funding and Azure credits from Microsoft. The authors declare no other competing
interests in the form of funding, collaboration and employment with any firm that owns or operates a social media
platform or their related philanthropic organizations.
References
[1] Philipp Lorenz-Spreen et al. “A systematic review of worldwide causal and correlational evidence on digital media
and democracy”. In:Nature Human Behaviour 2022 7:17.1 (Nov. 2022), pp. 74–101.ISSN: 2397-3374.DOI:
10.1038/s41562-022-01460-1.URL:https://www.nature.com/articles/s41562-022-01460-1.
[2] Amy Orben et al. “Mechanisms linking social media use to adolescent mental health vulnerability”. In:Nature
Reviews Psychology(2024), pp. 1–17.
[3] Patti M Valkenburg, Adrian Meier, and Ine Beyens. “Social media use and its impact on adolescent mental health:
An umbrella review of the evidence”. In:Current opinion in psychology44 (2022), pp. 58–68.
[4] Daniel Allington et al. “Health-protective behaviour, social media usage and conspiracy belief during the COVID-
19 public health emergency”. In:Psychological Medicine(2020).DOI:10.1017/s003329172000224x.
[5] Paolo Gerbaudo et al. “Angry posts mobilize: Emotional communication and online mobilization in the
Facebook pages of Western European right-wing populist leaders”. In:Social Media+ Society9.1 (2023),
p. 20563051231163327.
[6] Mohamed Abdalla and Moustafa Abdalla. “The grey hoodie project: Big tobacco, big tech, and the threat on
academic integrity”. In:Proceedings of the 2021 AAAI/ACM Conference on AI, Ethics, and Society. 2021,
pp. 287–297.
[7] Michael W. Wagner. “Independence by permission”. In:Science381.6656 (July 2023), pp. 388–391.ISSN:
10959203.DOI: 10.1126/SCIENCE.ADI2430.URL: https://www.science.org/doi/10.1126/science.
adi2430.
[8] Nicole M. Krause, Isabelle Freiling, and Dietram A. Scheufele. “Our changing information ecosystem for science
and why it matters for effective science communication”. In:Proceedings of the National Academy of Sciences
122.27 (2025), e2400928121.DOI: 10.1073/pnas.2400928121. eprint: https://www.pnas.org/doi/pdf/
10.1073/pnas.2400928121.URL:https://www.pnas.org/doi/abs/10.1073/pnas.2400928121.
[9] Joseph Bak-Coleman et al.The Risks of Industry Influence in Tech Research. 2025. arXiv:2510.19894 [cs.SI].
URL:https://arxiv.org/abs/2510.19894.
[10] David Lazer et al. “Computational social science”. In:Science323.5915 (2009), pp. 721–723.
[11] Naomi Oreskes and Erik Conway.Merchants of Doubt: How a Handful of Scientists Obscured the Truth on
Issues from Tobacco Smoke to Global Warming. London: Bloomsbury Press, 2010, 355 pp.
9

Industry Influence in High-Profile Social Media ResearchA PREPRINT
[12] Robert N Proctor.Golden holocaust: origins of the cigarette catastrophe and the case for abolition. Univ of
California Press, 2012.
[13] Cailin O’Connor and James Owen Weatherall.The misinformation age: How false beliefs spread. New Haven:
Yale University Press, Jan. 2019, pp. 1–266.ISBN: 9780300234015.
[14] Nicholas Chartres, Alice Fabbri, and Lisa A. Bero. “Association of Industry Sponsorship With Outcomes
of Nutrition Studies: A Systematic Review and Meta-analysis”. In:JAMA Internal Medicine176.12 (Dec.
2016), pp. 1769–1777.ISSN: 2168-6106.DOI: 10 . 1001 / JAMAINTERNMED . 2016 . 6721.URL: https : / /
jamanetwork.com/journals/jamainternalmedicine/fullarticle/2575884.
[15] Alice Fabbri et al. “The influence of industry sponsorship on the research agenda: A scoping review”. In:American
Journal of Public Health108.11 (Nov. 2018), e9–e16.ISSN: 15410048.DOI: 10.2105/AJPH.2018.304677.
URL:https://ajph.aphapublications.org/doi/10.2105/AJPH.2018.304677.
[16] Leonardo M. Siena et al. “Industry Involvement and Transparency in the Most Cited Clinical Trials, 2019-
2022”. In:JAMA Network Open6.11 (Nov. 2023), e2343425–e2343425.ISSN: 2574-3805.DOI: 10.1001/
jamanetworkopen . 2023 . 43425. eprint: https : / / jamanetwork . com / journals / jamanetworkopen /
articlepdf/2811814/siena_2023_oi_231263_1699303085.84457.pdf .URL: https://doi.org/10.
1001/jamanetworkopen.2023.43425.
[17] Joel Lexchin et al. “Pharmaceutical industry sponsorship and research outcome and quality: systematic review”.
In:BMJ326.7400 (2003), pp. 1167–1170.ISSN: 0959-8138.DOI: 10.1136/bmj.326.7400.1167 . eprint:
https://www.bmj.com/content/326/7400/1167.full.pdf .URL: https://www.bmj.com/content/
326/7400/1167.
[18] Deborah E. Barnes and Lisa A. Bero. “Why Review Articles on the Health Effects of Passive Smoking Reach
Different Conclusions”. In:JAMA279.19 (May 1998), pp. 1566–1570.ISSN: 0098-7484.DOI: 10.1001/jama.
279.19.1566 . eprint: https://jamanetwork.com/journals/jama/articlepdf/187551/jrv71060.
pdf.URL:https://doi.org/10.1001/jama.279.19.1566.
[19] Alice Fabbri, Taylor J Holland, and Lisa A Bero. “Food industry sponsorship of academic research: investigating
commercial bias in the research agenda”. In:Public Health Nutrition21.18 (2018), pp. 3422–3430.DOI:
10.1017/S1368980018002100.
[20] Bennett Holman and Justin Bruner. “Experimentation by Industrial Selection”. In:Philosophy of Science84.5
(Dec. 2017), pp. 1008–1019.ISSN: 0031-8248.DOI: 10.1086/694037 .URL: https://www.cambridge.
org/core/journals/philosophy- of- science/article/abs/experimentation- by- industrial-
selection/B009EF87417750846FA393346CE9D181.
[21] David Freeborn and Cailin O’Connor.Industrial Distraction. 2025.
[22] Jason Priem, Heather Piwowar, and Rirchard Orr. “OpenAlex: A fully-open index of scholarly works, authors,
venues, institutions, and concepts”. In:arXiv(2022). arXiv: 2205.01833 [cs.DL] .URL: https://arxiv.
org/abs/2205.01833.
[23] Springer Nature.Editorial Policies: Competing Interests. Accessed: January 14, 2025. 2025.URL: https :
//www.springer.com/gp/editorial-policies#competing-interests.
[24] National Academy of Sciences.PNAS Editorial and Journal Policies. Accessed: January 14, 2025. 2025.URL:
https://www.pnas.org/author-center/editorial-and-journal-policies.
[25] American Association for the Advancement of Science.Science Journals: Editorial Policies. Accessed: January
14, 2026. 2026.URL: https://www.science.org/content/page/science- journals- editorial-
policies.
[26] Mark MacCarthy. “Transparency requirements for digital social media platforms: Recommendations for policy
makers and industry”. In:Transatlantic Working Group(2020).
[27] Manuela Fernández Pinto and Daniel Fernández Pinto. “Epistemic diversity and industrial selection bias”. In:
Synthese201.5 (May 2023), pp. 1–18.ISSN: 15730964.DOI: 10.1007/S11229-023-04158-7/FIGURES/6 .
URL:https://link.springer.com/article/10.1007/s11229-023-04158-7.
[28] Arnold S Relman. “Dealing with conflicts of interest”. In:New England Journal of Medicine310.18 (1984),
pp. 1182–1183.
[29] Francisco G Cigarroa, Bettie Sue Masters, and Dan Sharphorn. “Institutional conflicts of interest and public
trust”. In:JAMA320.22 (2018), pp. 2305–2306.
[30] Catherine D DeAngelis. “Conflict of interest and the public trust”. In:Jama284.17 (2000), pp. 2237–2238.
[31] David B Resnik and Susan A Elmore. “Ensuring the quality, fairness, and integrity of journal peer review: A
possible role of editors”. In:Science and Engineering Ethics22.1 (2016), pp. 169–188.
10

Industry Influence in High-Profile Social Media ResearchA PREPRINT
[32] Manuela Fernández Pinto. “Commercial Interests and the Erosion of Trust in Science”. In:Philosophy of Science
87.5 (Dec. 2020), pp. 1003–1013.ISSN: 0031-8248.DOI: 10.1086/710521.URL: https://www.cambridge.
org/core/journals/philosophy- of- science/article/abs/commercial- interests- and- the-
erosion-of-trust-in-science/AB15D5413168D086451D331FCB40550E.
[33] Maarten Bosten and Bennett Kleinberg.Conflicts of Interest in Published NLP Research 2000-2024. 2025. arXiv:
2502.16218 [cs.CL].URL:https://arxiv.org/abs/2502.16218.
[34] Stanisław Gizi´nski et al. “Big Tech influence over AI research revisited: Memetic analysis of attribution of ideas
to affiliation”. In:Journal of Informetrics18.4 (Nov. 2024), p. 101572.ISSN: 1751-1577.DOI: 10.1016/j.joi.
2024.101572.URL:http://dx.doi.org/10.1016/j.joi.2024.101572.
11
