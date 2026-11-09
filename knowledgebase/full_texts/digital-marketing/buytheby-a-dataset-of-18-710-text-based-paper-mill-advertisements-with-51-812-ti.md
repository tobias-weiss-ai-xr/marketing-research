---
title: 'BuyTheBy: A dataset of 18,710 text-based paper mill advertisements with 51,812 timestamped prices'
url: https://arxiv.org/abs/2604.24576
category: digital-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Reese AK Richardson
- Spencer S Hong
- Anna Abalkina
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.24576
pages: 23
chars: 30913
fetched_at: '2026-11-08T12:57:31+00:00'
kb_version: 1
---

# BuyTheBy: A dataset of 18,710 text-based paper mill advertisements with 51,812 timestamped prices

BuyTheBy: A dataset of 18,710 text-based paper mill
advertisements with 51,812 timestamped prices
Reese AK Richardson1*, Spencer S Hong2, and Anna Abalkina3
1Center for Science of Science and Innovation, Kellogg School of Management,
Northwestern University, Evanston, Illinois, USA
2Department of Engineering Sciences and Applied Mathematics,
Northwestern University, Evanston, Illinois, USA
3Institute for East European Studies, Freie Universit¨at Berlin, Berlin, Germany
*To whom correspondence should be addressed: reese.richardson@northwestern.edu
April 28, 2026
Abstract
The study of paper mills and similar businesses operating in the market for academic and
education fraud services is frustrated by the lack of market price data on their various offerings.
Here, we assemble BuyTheBy, a large, annotated dataset of timestamped, text-based paper mill
advertisements from seven businesses operating out of seven different countries. The dataset
consists of 18,710 individual advertisements, of which 15,839 have prices listed. Among these
there are 20,598 positions listed as for sale on 5,567 unique products in 14 different product
categories with 51,812 timestamped price data points. We perform elementary analysis of this
dataset to demonstrate its utility for quantitative understanding of markets for academic fraud
services and suggest future use cases.
Introduction
Recent years have seen the apparent emergence of “paper mills”, typically understood to be commer-
cial organizations that sell authorship positions on pre-written scientific manuscripts and collude with
editors to have these manuscripts published without undergoing a rigorous peer review process [1–5].
Paper mill products are suspected to represent an increasing proportion of the published scientific
literature [3, 6–8]. We and others have recently suggested that paper mills should be conceptualized
as just one aspect of the broader global market for academic fraud services, wherein many actors
concurrently offer services related to diploma milling, essay milling, contract cheating, admissions
fraud and patent milling [9–12]. Despite ongoing scholarship and journalism enhancing the detec-
tion of paper mill products [13–17] and describing paper mill operations [3, 18–23], there are many
unknowns about paper mill operations and the market for paper mill products [7, 24].
One gap in knowledge concerns the market pricing of paper mill products. Thus far, most of
the data made available on the market prices of paper mill products has been sparse, anecdotal in
nature or indirect. For instance, a 2013 investigation found authorship positions in articles in journals
1
arXiv:2604.24576v1  [cs.CY]  21 Apr 2026

indexed by Web of Science being sold by a Chinese firm for 1,600 United States dollars (USD) to
26,300 USD [20]. A Russian company was found to advertise authorship positions for between 180
euros (EUR) to 5,000 EUR between 2019 to 2021 [18]. A 2024 investigation found that one editor
had been offered 3,000 USD for every paper they accepted in their journal originating from one paper
mill [3], implying prices for authorship slots roughly at this level. A 2025 investigation detailing the
operations of several paper mills lists prices for authorship positions between 20 USD and 1,500 USD
[21].
To aid in the quantitative economic study of paper mill operations, here we assemble BuyTheBy,
dataset of structured price data from largely unstructured text-based paper mill advertisements for a
variety of services related to publishing and credential fraud.
Data and methods
To assemble BuyTheBy v1.0, we collected advertisements made in “channels” on messaging app
Telegram from three businesses, using Telegram’s “Export chat history” feature. We selected these
channels because they were publicly accessible channels where many text-based advertisements writ-
ten mostly in English featuring price data were posted. We prioritized such datasets to assemble
as large a dataset as possible with minimal manual cleanup and redaction. Only text-based messages
were downloaded; any advertisements contained within PDF or image files attached to messages were
not processed. From an additional four businesses, we collected advertisements posted on the paper
mill’s website.
Business 1 (B1)apparently operates in India and primarily caters to academics in India. In its
Telegram channel, all messages are written in English and prices are listed in Indian rupees (INR).
1,101 messages were sent in this channel from 16 March 2022 to 16 July 2024. The channel was
exported on July 16, 2024, after which the channel owner disabled the “Export chat history feature”.
We considered each message to be equivalent to one advertisement. An example advertisement is
shown inFigure 4.
Business 2 (B2)apparently operates in Iraq and primarily caters to academics in Iraq. In its
Telegram channel, all messages are written in English and prices are listed in USD. Messages spanned
two channels, one in which 31 messages were sent by B2 from 20 December 2023 to 26 February
2024 and one in which 53 messages were sent by B2 from 26 February 2024 to 15 June 2024. These
channels were exported on 14 August 2024 and 26 June 2024, respectively. We considered each
message to be equivalent to one advertisement. An example advertisement is shown inFigure 5.
Business 3 (B3)apparently operates in Uzbekistan and primarily caters to academics around
Central Asia and the Middle East. In its Telegram channel, most messages are written in English
with some messages written in Uzbek. Prices are listed mostly in USD with some prices listed in
Uzbekistani sum (UZS). 1,126 messages were sent from 26 March 2020 to 16 March 2026. This
channel was exported on 12 March 2025 and 16 March 2026. We considered each message to be
equivalent to one advertisement. An example advertisement is shown inFigure 6.
Business 4 (B4)is registered in Latvia and appears to cater to academics around Eastern Europe
and Central Asia. It has previously been described elsewhere [21]. On its website, B4 lists 178 article
topics in English in a searchable table. Each entry lists up to eight authorship slots with prices listed
in USD and a button labeled “BUY”, which prompts the user to submit a form with their contact
information. We archived the state of this website on 11 November 2023. We considered each entry
in this table to be equivalent to one advertisement. An example advertisement is shown inFigure 7.
Business 5 (B5)is registered in Russia and appears to primarily cater to academics in Russia and
2

Kazakhstan. It has previously been described elsewhere [18, 22]. On its former website, B5 hosted
“publication service agreement” pages that list an article topic, an authorship position on that article
and a price for this single authorship slot in Russian rubles (RUB). A button on the bottom of each
contract redirects the user to a payment page. We archived the state of these pages on 1 October
2021. However, prior to this date, B5 had become aware that its services were being monitored by us
and added 17,763 fake contracts where article titles were derived from previously published articles.
We were able to discriminate between fake and real contracts because fake contracts did not have a
functional purchase button and uniformly listed the price of advertised authorship slot as zero. We
exclude these contracts from our dataset. We considered each of the remaining 7,907 pages, with one
authorship slot each, to be equivalent to one advertisement. An example advertisement is shown in
Figure 8.
On a different, newer website, B5 lists article topics and characteristics of target journals alongside
available authorship slots with prices in RUB. We archived the state of this page on 13 dates between
14 April 2024, when it listed 85 topics, and 4 April 2026, when it listed 491 topics. We considered
each listed topic to be one advertisement. An example advertisement is shown inFigure 9.
Business 6 (B6)apparently operates in Ukraine and primarily caters to academics in Ukraine.
B6’s website, available in English, Ukrainian and Russian, has pages advertising authorship slots on
articles, textbooks and “abstracts” (which we take to refer abstracts in conference proceedings). Prices
are listed in USD and Ukrainian hryvnias (UAH). The pages advertising articles were organized by
field (e.g., “Pedagogy/Education”, “Medical Sciences”, etc.). We archived the state of the Russian
version of these pages on 7 September 2024, 13 December 2025 and 21 March 2026 (on 7 September
2024, the “Humanities” page was only available in Ukrainian). We archived the state of the Russian
version of the page advertising textbooks on six dates between 7 October 2024 and 25 March 2026.
We archived the state of the Ukrainian version of the page advertising abstracts on five dates between
23 August 2024 and 1 April 2026. We decided to process the Russian version of the article pages,
the Ukrainian version of the textbook page and the Russian version of the abstract pages because
these were the languages in which the greatest number of past versions of each page were available
on webpage archiving services. Many topics are listed in English even on the Russian and Ukrainian
versions of each product page. We consider each listed topic to be one advertisement. An example
advertisement is shown inFigure 10.
Business 7 (B7)apparently operates in Kazakhstan and primarily caters to academics in Kaza-
khstan. B7’s website, available in English, Kazakh and Russian, features nearly identical branding
and layout to B6’s website. Despite this, the two sites list different addresses (in Ukraine and Kaza-
khstan, respectively) and phone numbers, link to different social media profiles and do not link to one
another. We consider B6 and B7 to be separate paper mills because their offerings are largely distinct.
B7’s website only advertises authorship slots on articles, also organized by field. We archived the
state of the English version of these pages on 28 March 2025 and 21 March 2026. Prices are listed in
USD. We consider each listed topic to be one advertisement. An example advertisement is shown in
Figure 11.
Metadata and prices from these advertisements were obtained using a combination of automated
and manual extraction and validation. Product titles were only extracted from advertisements fea-
turing prices. To allow for qualitative analysis of these datasets, we provide the text of these adver-
tisements with business names, websites, phone numbers, social media links and individuals’ names
redacted. These redactions were made with custom regular expressions. Prices were converted to
USD based on historical exchange rate data provided by the United States Department of the Trea-
sury [25].
The processed BuyTheBy dataset is available on Zenodo [26] under a CC BY 4.0 license alongside
3

a README file and data dictionary describing data fields. Code for reproducing figures and summary
statistics is available at github.com/reeserich/buytheby [27].
Summary and analysis
Summary data for advertisements from each business are provided inTable 1.
Table 1:Summary data for collected paper mill advertisements. Two products were considered the
same unique product if they were advertised by the same business in the same product category and
their titles matched exactly (insensitive to case or punctuation).
Business B1 B2 B3 B4 B5 B6 B7
Platform Telegram Telegram Telegram Website Website Website Website
Earliest
advertise-
ment
16 Mar
2022
20 Dec
2023
26 Mar
2020
11 Nov
2023
1 Oct
2021
23 Aug
2024
28 Mar
2025
Latest
advertise-
ment
16 Jul
2024
15 Jun
2024
16 Mar
2026
11 Nov
2023
4 Apr
2026
1 Apr
2026
21 Mar
2026
Number of
advertise-
ments
1,101 84 1,126 178 12,915 2,957 349
Product
types listed
13 1 1 1 1 3 1
Number of
advertise-
ments with
price(s)
listed
694 49 332 178 11,283 2,954 349
Number
of unique
products
listed with
price
692 26 259 178 2,543 1,605 264
Number
of unique
positions
listed with
price
2,061 102 779 784 9,551 6,109 1,212
Number
of times-
tamped
price data
points
15,578 142 952 785 21,089 11,678 1,588
Each business’ advertisements differ markedly from one another. For instance, while B1 and B6
4

advertise a diversity of products, including authorship positions on academic articles and textbooks,
editor positions on textbooks and inventorship positions on patents, the remaining five businesses
only advertise authorship positions on academic articles as for sale. B1’s offerings are summarized in
Table 2
Table 2:Types of products offered by B1. Only advertisements/products/positions with prices are
listed. Products are considered the same unique product if they are in the same product category and
their titles matched exactly (insensitive to case or punctuation).
Type of product Number of
advertise-
ments
Number of
unique prod-
ucts
Number of
unique posi-
tions
Number of
timestamped
prices
Authorship of “inter-
national” textbook
234 257 637 6,865
Authorship of article 99 88 210 1,667
India utility patent 98 80 522 3,143
Editorship of “inter-
national” textbook
88 28 141 604
United Kingdom de-
sign registration (ad-
vertised as “UK de-
sign patent” [11])
41 18 112 615
India copyright regis-
tration
29 6 19 108
India design regis-
tration (advertised as
“India design patent”
[11])
28 15 63 210
Canada copyright
registration
21 9 54 492
Authorship of “inter-
national” textbook
chapter
21 173 173 955
Germany utility
patent
18 3 24 79
South Africa utility
patent
8 1 8 55
Australia design reg-
istration (advertised
as “Australia design
patent” [11])
7 12 96 680
“National” award 2 2 2 4
Among advertisements for academic articles, B1, B2 and B3 typically name the target journal,
while B4, B5, B6 and B7 never name the target journal but do frequently indicate its indexing status
and approximate rank (e.g., “Scopus Q1”, “WoS Emerging Sources Citation Index Q4”, “Category
5

B”). While B2 and B3 advertise authorship positions on articles that they imply will be published
in indexed journals published by large, well-regarded international publishers like Springer Nature
and Elsevier, B1 almost exclusively advertises authorship positions in Institute of Electrical and Elec-
tronics Engineers (IEEE) conference proceedings and articles in journals belonging to small, regional
publishers, many of which have likely been hijacked [28, 29]. The representation of publishers among
advertisements that do name the target venue is summarized inTable 3. The representation of selected
indexing services and journal lists among all advertisements is summarized inTable 4.
Table 3:Representation of publishers among advertisements that name the targeted publication
venue.
Publisher Number of
advertise-
ments
Number
of unique
products
listed with
price
Elsevier 112 76
IEEE 101 54
Springer Nature 86 78
European Economics Letters 22 6
Wiley 22 20
Lutheran University of Brazil 20 7
Taylor & Francis 14 9
MDPI 8 4
De Gruyter Brill 8 5
Royal Society of Chemistry 7 6
Other 74 100
Table 4:Representation of select indexing services and journal lists among all advertisements. Ad-
vertisements either contained the name of the service (e.g., “Web of Science”), a sub-index (e.g., “Arts
& Humanities Citation Index”) or a metric closely related to the service (e.g., “Impact factor”).
Indexing service or journal list Number of adver-
tisements
Number of unique
products listed
with price
Scopus 12,012 3,220
Web of Science 5,136 1,294
Category B (Ukraine) 97 96
Australian Business Deans Council
(ABDC) Journal Quality List
27 6
PubMed/MEDLINE 21 10
KKSON (Kazakhstan) 15 11
UGC CARE list (India, discontinued) 12 0
6

From here, we provide some elementary exploratory data analysis to demonstrate the BuyTheBy’s
potential utility.
One unique feature of this dataset is that it allows for comparison of movement in market prices
over time. For instance, between June and December 2022, the median price advertised for first
authorship on an “international” textbook by B1 dropped several times from about 15,000 INR (about
180 USD) to about 7,000 INR (about 84 USD), as shown inFigure 1. Similarly, in the single month
when B1 was advertising authorship positions on IEEE conference proceeding articles captured in our
dataset (in June/July 2024), the going rate for each authorship position apparently increased twice, as
shown inFigure 2.
Figure 1:The median listed price for sole authorship, first authorship and sole authorship of a single
chapter of an “international” textbook changed over time in advertisements posted by B1. Prices were
converted from INR to USD at a static exchange rate of 0.012 USD to 1 INR.
7

Figure 2:The median listed price for authorship positions on IEEE conference proceeding articles
changed over time in advertisements posted by B1. Prices were converted from INR to USD at a
static exchange rate of 0.012 USD to 1 INR.
This dataset also allows for comparison of prices for similar products in different markets, as
demonstrated for authorship positions on academic articles among the seven businesses included in
the dataset inFigure 3. Although our selection of markets is limited, it is clear that prices vary con-
siderably between businesses and countries, likely as a function of the income level of each business’
targeted clientele.
Figure 3:Distributions of prices for authorship positions on academic articles advertised by each
business. Only the most recently-advertised price for a given authorship position is included and only
authorship slots one through five are shown. Boxplots show median as a horizontal line, interquartile
range as boxes, 2.5th and 97.5th percentiles as whiskers, and outliers as diamonds. Prices were
converted to USD based on historical exchange rate data provided by the United States Department
of the Treasury [25]. The y-axis is truncated at 2,500 USD. B5 advertised 438 first author positions
and three other positions above this price. The most expensive price listed by B5 was 5,631 USD.
Extended versions of this figure are shown inFigure 12through18.
8

Context-dependence, extreme variability in prices and unclear representativeness notwithstand-
ing, this dataset does allow for central estimates for prices to be made for the first time. Across all
advertisements included in this dataset, the median price for a first author position on an academic
article is 788 USD (see other central estimates inTable 5).
Table 5:Descriptive statistics of prices per authorship slot on academic articles (in USD). Estimates
are taken across all advertisements from all seven businesses. Only the most recently-advertised price
for a given authorship position is included.
Authorship slot Count Median Mean Min Max
1 4,206 788.41 1,031.85 56.87 5,631.48
2 4,376 675.78 760.88 53.985 5,068.33
3 4,397 570.00 676.81 47.987 4,505.19
4 2,995 560.00 636.48 41.99 3,378.89
5 1,618 420.00 464.47 36.00 1,800.00
6 154 462.76 460.67 48.00 1,550.00
7 35 450.00 514.71 200.00 1,500.00
8 28 450.00 539.11 250.00 1,650.00
9 16 350.00 454.69 150.00 1,200.00
10 5 250.00 246.00 130.00 350.00
Discussion
Here, we provide a first-of-its-kind annotated dataset of paper mill advertisements. Elementary analy-
sis of the dataset confirms that having such rich datasets is important for the quantitative understanding
of paper mill operations: prices can fluctuate considerably over time and vary wildly across different
markets and contexts, even within a single business’ portfolio of offerings.
Future studies using BuyTheBy might interrogate how prices vary based on the perceived qual-
ity of product being offered (e.g., indexing status or ranking of a journal), based on the perceived
reward for purchasing the product (e.g., by linking the dataset with corresponding points-based met-
rics in widely adopted institutional tenure and promotion criteria) or based on academic discipline.
Publishers and indexing services might also use BuyTheBy to augment internal assessments of their
portfolios’ exposure to paper mill operations (similar to how previous works have linked paper mill
advertisements to eventually published articles [18]). BuyTheBy also provides opportunities for in-
depth qualitative study of the advertising and communications strategies employed by paper mills.
This dataset does bear some limitations. First, we only extract text-based advertisements and make
no attempt to extract information from any image- or video-based advertisements posted in these or
other channels or websites. Second, our selection of which channels or websites to include is not
systematic, having mostly been motivated by informal selection criteria intended to ease assembly
and distribution of the dataset. Third, our dataset has limited coverage, geographically and in time.
Finally, we make no attempt to link any of these advertisements to products that were eventually
published (although many advertisements contain sufficient information to do so). Those interested
in making these links should be aware that paper mills are known to change the text of articles from
the posted advertisement to frustrate efforts to identify published paper mill products and protect
9

clients [21]. Moreover, paper mill products that are eventually published often do not appear in the
same venue that was initially advertised. Finally, users should note that advertised topics are often
modeled after or directly plagiarize previously-published articles.
Acknowledgements
We thank Nick Wise for providing data and feedback for this project and participants in the 2025
Calgary Colloquium for valuable discussions. The play on words “Buy the ‘By”’ was borrowed from
the title ofNature’s print version of a 2025 investigation by Christine Ro and Jack Leeming [21].
RR contributed to this work independently of his work as a postdoctoral researcher at Northwestern
University.
Data availability
The processed BuyTheBy dataset is available on Zenodo [26] alongside a README file and data
dictionary describing data fields.
Code availability
Code for reproducing figures and summary statistics is available at github.com/reeserich/buytheby
[27].
Abbreviations
United States dollars (USD); Euro (EUR); Indian rupees (INR); Ukrainian hryvnias (UAH); Uzbek-
istani sum (UZS); Russian rubles (RUB); Institute of Electrical and Electronics Engineers (IEEE).
References
[1]Paper Mills — Research report from COPE and STM. Tech. rep. COPE and STM, 2022.URL:
https://doi.org/10.24318/jtbG8IHL.
[2] Jennifer A Byrne, Yasunori Park, Reese AK Richardson, Pranujan Pathmendra, Mengyi Sun,
and Thomas Stoeger. “Protection of the human gene research literature from contract cheat-
ing organizations known as research paper mills”. In:Nucleic Acids Research50.21 (2022),
pp. 12058–12070.
[3] Frederik Joelving. “Paper trail”. In:Science383.6680 (2024), pp. 252–255.
[4] Jeffrey Brainard. “Fake scientific papers are alarmingly common”. In:Science(2023).
[5] Jana Christopher. “The raw truth about paper mills”. In:FEBS letters595.13 (2021), pp. 1751–
1757.
[6] Richard Van Noorden. “How big is science’s fake-paper problem?” In:Nature623.7987 (2023),
pp. 466–467.
10

[7] Anna Abalkina, Ren ´e Aquarius, Elisabeth Bik, David Bimler, Dorothy Bishop, Jennifer Byrne,
Guillaume Cabanac, Adam Day, Cyril Labb ´e, and Nick Wise. “‘Stamp out paper mills’ —
science sleuths on how to fight fake research”. In:Nature637 (2025), pp. 1047–1050.
[8] Reese AK Richardson, Spencer S Hong, Jennifer A Byrne, Thomas Stoeger, and Lu ´ıs A
Nunes Amaral. “The entities enabling scientific fraud at scale are large, resilient, and growing
rapidly”. In:Proceedings of the National Academy of Sciences122.32 (2025), e2420092122.
[9] Sarah Elaine Eaton and Jamie J Carmichael. “Fake degrees and credential fraud, contract cheat-
ing, and paper mills: Overview and historical perspectives”. In:Fake Degrees and Fraudulent
Credentials in Higher Education. Springer, 2023, pp. 1–22.
[10] Allen Ezell. “Yesterday, today, and tomorrow: A tour of Axact, the “world’s largest diploma
mill””. In:Fake Degrees and Fraudulent Credentials in Higher Education. Springer, 2023,
pp. 49–94.
[11] Reese AK Richardson, Nick H Wise, Spencer S Hong, Michael J Draper, and Sarah Fackrell.
“Exploitation of intellectual property systems for the manipulation of academic reputations”.
In:International Journal for Educational Integrity21.1 (2025), p. 15.
[12] Cathleen O’Grady. “‘Patent mills’ sell scientists inventorship of bizarre medical devices”. In:
Science(2025).
[13] Guillaume Cabanac, Cyril Labb ´e, and Alexander Magazinov. “The ‘Problematic Paper Screener’
automatically selects suspect publications for post-publication (re) assessment”. In:arXiv e-
prints(2022), arXiv–2210.
[14] Reese AK Richardson, Jeonghyun Moon, Spencer S Hong, and Lu ´ıs A Nunes Amaral. “Widespread
misidentification of scanning electron microscope instruments in the peer-reviewed materials
science and engineering literature”. In:PLOS One20.7 (2025), e0326754.
[15] Simon J Porter and Leslie D McIntosh. “Identifying fabricated networks within authorship-for-
sale enterprises”. In:Scientific Reports14.1 (2024), p. 29569.
[16] Danielle J Oste, Pranujan Pathmendra, Reese AK Richardson, Gracen Johnson, Yida Ao, Maya
D Arya, Naomi R Enochs, Muhammed Hussein, Jinghan Kang, Aaron Lee, et al. “Misspellings
or “miscellings”—Non-verifiable and unknown cell lines in cancer research publications”. In:
International journal of cancer155.7 (2024), pp. 1278–1289.
[17] Yasunori Park, Rachael A West, Pranujan Pathmendra, Bertrand Favier, Thomas Stoeger, Amanda
Capes-Davis, Guillaume Cabanac, Cyril Labb´e, and Jennifer A Byrne. “Identification of human
gene research articles with wrongly identified nucleotide sequences”. In:Life Science Alliance
5.4 (2022).
[18] Anna Abalkina. “Publication and collaboration anomalies in academic papers originating from
a paper mill: Evidence from a Russia-based paper mill”. In:Learned Publishing36.4 (2023),
pp. 689–702.
[19] Pawel J Matusz, Anna Abalkina, and Dorothy VM Bishop. “The Threat of Paper Mills to
Biomedical and Social Science Journals: The Case of the Tanu. pro Paper Mill in Mind, Brain,
and Education”. In:Mind, Brain, and Education19.2 (2025), pp. 90–100.
[20] Mara Hvistendahl. “China’s publication bazaar”. In:Science342 (2013).
[21] Christine Ro and Jack Leeming. “Authorship for sale: Nature investigates how paper mills
work”. In:Nature(2025).
11

[22]Alexandr Litoy. Фокус-Scopus. Как за деньги купить место среди соавторов западного
научного журнала. URL: https://theins.ru/obshestvo/165368.
[23] Frederik Joelving. “‘Article broker’ in China trying to hook journal editors with fishy pub-
lishing deals”. In:Retraction Watch(2025).URL:https://retractionwatch.com/
2025 / 09 / 08 / article - broker - a - techo - china - journal - editors -
publishing-deals/.
[24] Jennifer A Byrne, Anna Abalkina, Olufolake Akinduro-Aje, Jana Christopher, Sarah E Eaton,
Nitin Joshi, Ulf Scheffler, Nick H Wise, and Jennifer Wright. “A call for research to address
the threat of paper mills”. In:PLoS Biology22.11 (2024), e3002931.
[25]Treasury Reporting Rates of Exchange. Accessed: 2026-04-09.URL:https://fiscaldata.
treasury.gov/datasets/treasury-reporting-rates-exchange/treasury-
reporting-rates-of-exchange.
[26]BuyTheBy Dataset. Accessed: 2026-04-20.URL:https://doi.org/10.5281/zenodo.
19684277.
[27]BuyTheBy Analytical Code. Accessed: 2026-04-20.URL:https://github.com/reeserich/
buytheby.
[28] Anna Abalkina. “Challenges posed by hijacked journals in Scopus”. In:Journal of the Associ-
ation for Information Science and Technology(2023).
[29] Anna Abalkina. “Detecting a network of hijacked journals by its archive”. In:Scientometrics
126.8 (2021), pp. 7123–7148.
12

Figure 4:An example advertisement from B1 (posted on 26 June 2024, id tag “message3806”).
13

Figure 5:An example advertisement from B2 (posted on 19 March 2024, id tag “message23”).
14

Figure 6:An example advertisement from B3 (posted on 21 March 2025, id tag “message7180”).
15

Figure 7:An example advertisement from B4 (archived on 11 November 2023, id tag
“231111 176”).
16

Figure 8:An example advertisement from B5’s “publication service agreement” pages (archived on
1 November 2021, id tag “1439.3”).
Figure 9:An example advertisement from B5’s new wewsbite pages (archived on 7 August 2025,
id tag “4063 250807”).
17

Figure 10:An example advertisement from B6 (archived on 21 March 2026, id tag “260321Педа-
гогика/Образование43”).
18

Figure 11:An example advertisement from B7 (archived on 21 March 2026, id tag ‘260321 Eco-
nomic Sciences 5”).
19

Figure 12:Distributions of prices for authorship positions on academic articles advertised by B1.
Only the most recently-advertised price for a given authorship position is included. Boxplots show
median as a horizontal line, interquartile range as boxes, 2.5th and 97.5th percentiles as whiskers, and
outliers as diamonds.
Figure 13:Distributions of prices for authorship positions on academic articles advertised by B2.
Only the most recently-advertised price for a given authorship position is included. Boxplots show
median as a horizontal line, interquartile range as boxes, 2.5th and 97.5th percentiles as whiskers, and
outliers as diamonds.
20

Figure 14:Distributions of prices for authorship positions on academic articles advertised by B3.
Only the most recently-advertised price for a given authorship position is included. Boxplots show
median as a horizontal line, interquartile range as boxes, 2.5th and 97.5th percentiles as whiskers, and
outliers as diamonds.
Figure 15:Distributions of prices for authorship positions on academic articles advertised by B4.
Only the most recently-advertised price for a given authorship position is included. Boxplots show
median as a horizontal line, interquartile range as boxes, 2.5th and 97.5th percentiles as whiskers, and
outliers as diamonds.
21

Figure 16:Distributions of prices for authorship positions on academic articles advertised by B5.
Only the most recently-advertised price for a given authorship position is included. Boxplots show
median as a horizontal line, interquartile range as boxes, 2.5th and 97.5th percentiles as whiskers, and
outliers as diamonds.
Figure 17:Distributions of prices for authorship positions on academic articles advertised by B6.
Only the most recently-advertised price for a given authorship position is included. Boxplots show
median as a horizontal line, interquartile range as boxes, 2.5th and 97.5th percentiles as whiskers, and
outliers as diamonds.
22

Figure 18:Distributions of prices for authorship positions on academic articles advertised by B7.
Only the most recently-advertised price for a given authorship position is included. Boxplots show
median as a horizontal line, interquartile range as boxes, 2.5th and 97.5th percentiles as whiskers, and
outliers as diamonds.
23
