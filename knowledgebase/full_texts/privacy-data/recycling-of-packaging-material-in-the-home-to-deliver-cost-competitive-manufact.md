---
title: Recycling of Packaging Material in the Home to Deliver Cost Competitive Manufacturing Inputs Empowering
  Householders to Contribute to &amp; Benefit from the Circular Economy
url: https://doi.org/10.65569/kway1609
category: privacy-data
subcategory: case-study
date: 2026-01
venue: ''
authors:
- Aldous Hicks
- Phil Sanders
- Robin Verbruggen
source: openalex-oa
pdf_url: https://remadeinstitute.org/mp-files/2026-32-recycling-of-packaging-material-in-the-home-to-deliver-cost-competitive-manufacturing-inputs-empowering-householders-to-contribute-to-benefit-from-the-circular-economy.pdf/
pages: 10
chars: 41863
fetched_at: '2026-11-08T17:05:27+00:00'
kb_version: 1
---

# Recycling of Packaging Material in the Home to Deliver Cost Competitive Manufacturing Inputs Empowering Householders to Contribute to &amp; Benefit from the Circular Economy

Recycling of Packaging Material in the Home to Deliver Cost
Competitive Manufacturing Inputs Empowering Householders to
Contribute to and Benefit from the Circular Economy

Aldous Hicks, President & Founder, Lasso Loop Recycling LLC
amh@lassoloop.com +1 650 888 9660
Phil Sanders, CTO, Lasso Loop Recycling LLC
Robin Verbruggen, E&E Engineer, Lasso Loop Recycling LLC
Tobias Van Eeckhout, Full-stack IT solutions architect Lasso Loop Recycling LLC

Abstract
Post-consumer recycling (PCR) packaging must meet strict manufacturing input speciﬁcations and remain price-competitive with
virgin materials produced through extraction and mining in the linear economy.

This paper demonstrates how close loop recycling (CLR) of plastics, glass, and metals can be achieved in the home or other
decentralized locations. It outlines the engineering solution, including equipment design. and the integration of AI, machine vision,
machine learning and spectroscopy to identify materials, capture label information, and ensure product purity across the supply
chain.

The proposed in-home appliance scans and validates used items, processes them to precise speciﬁcations, and stores six distinct
material streams. An on-demand collection service then delivers these high-quality recyclates to manufacturers. This system
empowers households to contribute to and directly beneﬁt from the circular economy.

CLR generates three revenue streams: (i) sale of recycled materials, (ii) provision of DRS and EPR services, and (iii) ﬁrst-party
data for omnichannel marketing and advertising platforms. Compared to virgin inputs, CLR materials used in remanufacturing can
reduce energy consumption by 35–95% and lower CO2e emissions signiﬁcantly, depending on the energy mix.

Recent advances enhance CLR system viability, including AI-driven MV/ML models with GPU-CPU-RAM accelerators for rapid
material recognition, and at-home parcel delivery services developed through online shopping. Together, these technologies enable
accurate substance identiﬁcation, eﬃcient logistics, and scalable deployment.

While industry stakeholders are setting ambitious recycled content and emissions reduction targets—often backed by legislation
such as California Assembly Bill 793—CLR appliances can meet these requirements without new regulatory mandates.
Beyond single-family homes, CLR units can be adapted for multi-family dwellings, educational institutions, and other sites, though
additional mechanisms are needed to address operational complexities.

This paper will detail the enabling technologies, processes, and business model underpinning household CLR, showing how they
can accelerate packaging circularity and expand consumer participation in the circular economy.

Introduction and Motivation
Inputs to manufacturing process to produce packaging for consumer products are still predominantly delivered by mining and
extraction of virgin raw materials. At the end-of-life the packaging produced and consumed predominantly ends up in landfill or
as pollution contaminating the natural environment. This system represents a linear economy.

Used materials that are closed loop recycled to become manufacturing inputs or post-consumer recycling (PCR) require a lower
amount of energy compared with virgin raw materials1. Consequentially closed loop recycled manufacturing inputs to a first order
of magnitude should be more competitive, both financially and environmentally, as inputs to manufacturing than those sourced
from virgin raw material processes. Mostly to date in the US and around the world, delivering closed loop recycled manufacturing
inputs competitively has not been achieved. Closed loop recycling is a key requirement of a circular economy.

The first motivation for this paper is to understand why the existing curb side recycling system, after fifty plus years of development
and commercial operation, has not delivered significant closed recycling materials for manufacture and why that situation is
unlikely to change in the near, medium or distant future. The second and more important motivation is to offer an alternative

recycling system that has a sensible and reasonably likelihood of producing the maximum practically possible closed loop recycled
materials. It is centered on a recycling appliance in the home, office or other places and supported by an efficient logistic system to
transport the close recycled materials to manufacturers, which focuses on a decentralized system empowering householders, office
workers and others to contribute to and benefit from the circular economy. They contribute by producing recycled materials and
reducing their carbon footprint. They benefit by knowing they are doing the right thing with the environment and being reimbursed
for delivering environmentally valuable and cost competitive manufacturing inputs.

In this paper, specific word meaning and usage is in place. The term “waste” refers to material that has no further use and no further
value. This is material that should be delivered straight to landfills. It is at its “end-of-life”. This process describes a linear economy.
“End-of-use” is used instead of “end-of-life” to describe used materials or products at the end of use, since most materials or
products have significant additional life through reuse or recycling into equivalent products. This process describes a circular
economy.

The current recycling system including the bin being emptying at the curb side, the contents transported to a materials recovery
facility (MRF) for sorting of materials into bales before being transported to recycling or processing or recovery plants or factories
is called a “collection for recycling” system. Recycling or processing or recovery plants are called “recycling plants”. The bales of
used PET or HDPE plastic containers output by MRFs when processed to PET or HDPE flakes respectively is called “recycling”.
The processes that precede “recycling” are called “collection for recycling”.

“Used materials” are the inputs to an alternate recycling system. The outputs are materials to exact technical specifications suitable
to be inputs to manufacturing processes as far down the manufacturing process as possible. To clearly differentiate between near
zero value inputs to and high value outputs from the alternative recycling system, inputs to are called “used materials” and outputs
from are called “products”.

The alternative recycling system is an optimized decentralized closed loop recycling system (CLRS). The phrases “closed loop
recycled” and “closed loop recycling” are used regularly in the paper. CLR will be the acronym for these two phrases.

Bottle deposit systems or deposit return schemes are one in the same thing and will be called DRSes.

Current State of the Technology Industry Uses
There is little information available indicating the amount of used material that is currently closed loop recycled (CLR) by the
existing curb side recycling systems in developed western countries.

In the US there are numerous industry reports 2, 3 & 4 with information about the amount of material collected for recycling. For
the US the International Aluminum Institute (IAI) states that approximately 42% of aluminum cans are recycled and a Recycling
Partnership Report states 30%5. From information in NAPCOR’s 2020 PET Recycling Report it is possible to estimate that US
PET closed loop recycling rate is below 10%6. The Ellen Macarthur Institute’s 2020 Plastic Agenda for Business advised that
“globally only around 15% of plastic is recycled”7. In an EU presentation, the presenter displayed the slide depicted in Figure 1
below indicating that in the EU in 2024 8.7 million tonnes or 15% of used plastics was recycled into new plastics8.
Figure 1
These reports don’t specifically provide CLR metrics. The International Aluminum Institute (IAI) states that world-wide 33% of
aluminum cans, 20% of glass bottles and 7% of PET containers are can-to-can recycled or CLR5. These results come after five

decades of the western world developing and implementing systems that improve the recycling of plastics, glass, metals, paper and
cardboard. Aluminum cans are the most recycled packaging in the US, achieving a 42% can-to-can recycling rate.

Purportedly, improved collection for recycling results are achieved where there are bottle deposit or deposit return schemes (DRS)9.
And industry representatives claim that extended producer responsibility (EPR) systems also help10. Industry reports or peer
reviewed literature do not provide the CLR key performance indicators (KPIs) for these regions and systems. For example, the
percentage of Californian’s CRVs (container return values) collected for recycling PET containers that are closed loop recycled is
not provided by CalRecycle’s published KPIs.

The solutions proposed by governments and industry to improve the performance of curbside recycling are more DRSes, more
EPR systems, more infrastructure spending for material recovery facilities (MRF)11, and more education of householders and
consumers. The solution proposed by the Ellen Macarthur Foundation is for businesses to “collectively shape wider market
conditions”12, in other words influence government policy.

Attempts at implementing DRSes and EPR systems by US State governments in the last twenty years have not been successful.
The State of Washington has had four failed attempts. The last DRS system enacted in the US was in 2002, 23 years ago! The first
US EPR system enacted was in Maine in 2021. California’s SB 54 Plastic Pollution Prevention and Packaging Producer
Responsibility Act was passed on June 30, 2022. However, recently the Californian Governor has called for a reassessment of SB
54 and it is not yet clear whether this is a delay or a skuttling of the Californian EPR bill. No material wide EPR system is in
operation in a US State. Further, the current US Federal political environment is not receptive to supporting government
administered systems.

A recent US EPA report estimates an investment of $36.5 to $43.4 billion is needed to improve US curbside collection, drop-off,
and processing infrastructure11. However, the EPA Solid Waste Infrastructure for Recycling (SWIFR) funding is concluding.
Delivering the funding called for by stakeholders could be years off if not decades.

This current “State of the Technology” relying on the enacting DRS and EPR systems and significant government funding is one
recycling solution.  The last round of US EPA administered Solid Waste Infrastructure for Recycling (SWIFR) grants ends at the
end of 2025. There does not seem to be funding available to educate householders who, from the industry’s perspective, are always
seemingly in need of more education.  Without these industry requests being delivered so their solutions can be implemented, the
existing recycling system can be expected to struggle to improve its performance

The low recycling outcomes have many causes. One is the historical and continued industry focus on the collection of recyclables
and calling the activity “recycling”. Reports on collection, as mentioned previously, are numerous. Reports in the public arena,
whether industry or peer-reviewed literature, providing CLR metrics are difficult to find. NAPCOR in the US and PETCORE in
the EU12 produce annual reports that enable CLR metrics to be estimated. However, the recent NAPCOR and PETCORE reports
are not publicly available. Collection is an important first step in any recycling chain. Though the focus should be on the required
recycling systems outcomes. Also, if there is validity in Peter Drucker’s statement "What gets measured gets managed", when the
focus is on measuring collection, it is understandable that since CLR outcomes are not the focus of measurements and reports, then
they don’t get managed.

There are alternative technological approaches, which do not focus on collection, which could sensibly and reasonably be a
practical, deliverable and financially viable CLR solution.

Technology Approach
A technological approach would be defined by the required solution. That solution is to produce high-purity high-volume
manufacturing inputs as quickly and efficiently as possible. Household appliances provide technological solutions to clean and dry
our dirty clothes, wash our used dishes, preserve our food, cool our drinks and assist with other household tasks. The alternate
technology hypothesis was that a decentralized CLR home appliance could perform household recycling.

It has been generally accepted by stakeholders that source-separation of used containers and items produces higher quality
recyclables. In Figure 1 on the previous page, please note the diagonal text “Plastic recycling 13X higher when collected
separately”. Despite this seemingly accepted metric, source-separation for the existing recycling system has not been implemented.
The current curb side collection-for-recycling system has focused on centralized collection capturing the maximum volume at

minimal cost. Because source-separatiin adds to collection costs, it has not found favor with industry stakeholders.

However, a smart household recycling appliance incorporating a sensor chamber which sets out to guarantee mistake-free source-
separating decisions by substance and color for used-packaging items is technically viable today. Such a decision-making system
removes the need for public education programs for householders. AI models trained by machine vision and learning to provide
accurate used container information are a timely and potentially a cost-reducing technological development. Used material size
reduction equipment, which processes or size reduces plastic containers to flakes, glass bottles to cullet, and metal cans to shreds,
can have their dimensions and manufacturing-cost reduced. Size reduced containers are volume-efficient materials for storage and
transport. Label material, glue, tamper ring and any remaining content contamination can be removed by washing, drying and
classifying. The product storage container (PSC) includes six small bins, one for each of the six sperate products. They are PET
and HDPE plastic flakes, clear, grean and brown glass cullet, and steel and aluminum shreds. The PSC is located at the bottom of
the appliance. For product collection from the home, the PSC is disengaged from the appliance and wheeled to the curb. The six
products are transferred separately into the correct bins in the collection vehicle. During transfer, the products are separately
weighed for supply chain verification and auditing. At-home on-demand logistics systems are now reliable and cost effective
primarily due to the Amazon-styled on-line shopping administered from apps on smart phones, pads or notebooks.

Manufacture ready input specifications and product collection at home
The overarching principle of a CLRS is to eliminate the risk of cross contamination between recyclable materials from the point of
generation by the consumer through to the final product arriving at a remanufacturer. By analyzing the current process flow for
recyclable materials from curbside collection through the MRF, onwards to the processing facility before finally arriving at a
remanufactures and following the typical product design process, the CLR appliance development team has taken the processes
that work well in the current system, reimagined those that do not and miniaturized them to be suitable for a working TRL 5
domestic appliance prototype of moderate dimensions 47”(H) x 36” (W) x 26” (D) which compares with the dimensions of an
average US top-loading washing machine of 44” (H), x 27” (W) x 28” (D).

Before loading a used container into the appliance any closures, caps, neck rings, or foils are removed by the user using simple
mechanisms recessed into the front of the appliance. This initial step simplifies the need for separation of dissimilar materials from
the core substrate later in the process. The used container is then loaded into the front of the appliance via the loading hatch with
the container orientated so that the base, in the case of containers, or unobstructed side in the case of thermoforms, is presented
correctly to the sensor array for material analysis. At this stage if closures, caps, neck rings, or foils are not removed, the container
will not be accepted and returned to the operator. Once the container has been confirmed as one of the six acceptable material
streams it is accepted into the appliance and directed to one of the three processors where it is size reduced. Glass is converted into
cullet, plastics into flakes and aluminum cans into shreds. As the containers still retain their labels at this point the processors all
operate without screens to mitigate the risk of blockages and post processing residue causing cross contamination. The size reduced
materials are fed into agitation chambers to be cleaned with a combination of hot water and surfactants which separate any
remaining label and organic material from the core material. The use of selective buffers between the processors and agitation
chambers ensures that the appliance can keep accepting containers rather than causing a bottle neck whilst a particular material
stream is undergoing the washing process. Once cleaned the material is dried and any remaining label debris driven off in a
classifier. Waste water containing organic matter and suspended adhesive from the cleaning process is filtered before being
recycled back into the system to limit water usage.

The clean, dry, size reduced material, now called a product, is then released from the agitation chamber to the product storage
container (PSC). The individual bays of the PSC, one for each material type accepted, are sized to allow uniform filling to maximize
the storage capacity of the PSC and therefore maximize the time between collections.

Through modification of specific geometries within the crusher, granulator and shredder the output cullet, flake and shred
dimensions respectively can be tuned to reliably meet industry standards whilst the preparation and treatment of the materials pre-
and post-processing ensure that the contamination levels of the final product also fall within allowable industry standards. A
comparison of the Industry and CLRS standards for recycled PET (rPET) is given in Table 1 below.

T
able 1
rPET Industry Standard   Closed Loop Recycling (CLR) Standard
Source Post consumer PET containers   Post consumer PET containers
Colour Transparent   Transparent

When the PSC is full using an app a user schedules an at-home collection.  Recycling figures per household per annum from the
Recycling Partnership’s national report2 and bulk density of processed material allows the PSC to be appropriately sized, to fill
evenly, and be collected approximately 8 times per year. When the user ejects the PSC from the appliance for collection the PSC
bays close and lock to prevent environmental and user interference with the stored products. The user hinges out the PSC handle
and moves the wheeled PSC to the curbside, orientating it correctly, the same as is required for the current curbside bins. The Lasso
trailer arrives for the collection and deploys a hydraulic arm to interface and capture the PSC. The geometry of the mating parts
indexes the PSC to the collection arm so that when it is raised the six material bays align with the corresponding manifold inputs
on the collection trailer. An electronic handshake is performed between the PSC and trailer to confirm its correct association with
a registered appliance before the bays are unlocked, and products are allowed to flow into individual hoppers. The products are
weighed and recorded before being released to the bulk storage bins within the trailer. The PSC bays are closed and locked and the
PSC returned to the curbside for the user to collect and return to the bottom of the appliance.

When the collection trailer is full it returns to a product onforwarding depot (POD) where the products are removed from the trailer,
cross checked by weight, aggregated and stored ready for sale and bulk transport direct to remanufacturers.

The Sensor Chamber
A CLR appliance sensor chamber is the key technology which sets this CLR system apart from the current and traditional curbside
recycling system. It has the capability to accurately identify a used container’s or item’s substance, its color, whether it is DRS
qualifying or not, linking the container’s consumer with the brand owner to enable delivery of  EPR, and the reading of label image
and text information for omnichannel marketing and advertising platform use.

The chamber is the first and critical function to guarantee each of the recycled products produced are to the CLR specification. The
householder’s “which bin does this item go in” common dilemma is resolved removing the need for householder recycling
education. The label image information and sensor chamber software deliver the maximum realizable value of each container. A
container’s CLR material value represents only one sixth of each used container’s potential realizable value.

NIR spectroscopy in the sensor chamber
Near-infrared (NIR) spectroscopy is an analytical technique that uses light in the near-infrared range to identify the chemical
composition of materials. For plastics, this is particularly valuable because different polymers—such as PET, PE, PP, PVC, and
PS—have unique spectral “fingerprints.” When NIR light interacts with a plastic material, specific wavelengths are absorbed
depending on the molecular bonds present. By analyzing the reflected or transmitted light, it becomes possible to determine quickly
and reliably which type of plastic is being processed.

A Hamamatsu compact FT-NIR spectrometer based on Fourier-transform infrared analysis uses near-infrared light to measure
characteristic absorption patterns of materials. The device is capable of reliably distinguishing different types of plastics based on
their unique spectral signatures. The spectrometer is small with low energy consumption and is suitable for integration into a CLR
appliance.

Distinguishing between different plastics is crucial for efficient sorting in CLR appliances. Traditional methods, such as manual
sorting or density separation are slow and error prone. Moreover, these classical techniques are difficult or even entirely unfeasible
in a space and cost-constrained context, such as an appliance in a home. Also, they require large equipment, significant amounts
of water or chemicals, or manual labor. Such processes simply do not fit into a domestic environment, where space, time, safety
and cost constraints are given. On the other hand, NIR spectroscopy systems offer compact, rapid, non-contact cost-effective and
automated identification, making them suitable for small-scale, home-based or similar recycling applications.

NIR spectroscopy plays an important role in CLR appliances when plastic items are first inputted. By identifying plastics quickly
Property High Value Target Value Unit   High Value Target Value Unit
Density 300 - 450 300 - 450 g/l   300 - 450 300 - 450 g/l
Fines content <0.5mm < 0.1 < 0.1 % < 10mm   < 0.1 < 0.1 % < 10mm
Oversize flakes content < 0.5 < 0.5 % > 12mm   < 0.5 < 0.5 % > 12mm
Content of light blue flakes < 2 < 1 %   < 2 < 1 %
Content of colored flakes < 500 < 100 ppm   < 50 < 25 ppm
Moisture < 1 < 1 %   < 1 < 1 %
Intrinsic viscosity IV TBD TBD     TBD TBD

and accurately at source, material streams are kept separate from the start, reducing cross-contamination and increasing purity, the
key requirement to deliver competitive manufacturing inputs.

AI Decision Models from Machine Vision + Machine Leaning
In addition to identifying container characteristics, image data is used to read barcodes, labels and print on containers using optical
character recognition (OCR) technology which extracts text from images. The extracted text helps to identify the container and is
specifically used to determine DRS qualification.

Multiple sensor fusion algorithms (SFA) create consensus about container identification and recyclability.  Each SFA has its own
container characteristics to identify, make decisions, or leverage specific AI models for the task. Some SFAs run in parallel while
others use previous SFA outputs as their inputs to form a consensus over all available sensor, image and SFA data. SFA’s are
designed for strictness, certainty and accuracy, rejecting a container rather than risking product contamination. The SFA algorithms
decision is made, and a container will be accepted or rejected.

All relevant sensor chamber data, such as sensor and image data and SFA consensus data, is stored and will be used for quality
control, container traceability and accountability for DRS and EPR systems. The data is also used extensively for testing, improving
and re-training the Lasso AI models by extending and enhancing the Lasso datasets by performing quality control and annotation
and inference verification. This ensures proper working of the sensor chamber and its algorithms and continual improvement of
the container characteristics identification. Figure 2 displays a sensor fusion algorithm for a sensor chamber for a CLR appliance.
Figure 2

Recent advancements in computation and artificial intelligence technology have enhanced the accuracy and speed of algorithms.
AI accelerators, such as GPUs and other specialized chips, are engineered to perform complex computations at a faster rate,
improving the overall throughput of the sensor chamber while significantly lowering its energy footprint and cost. Advancements
in AI models have led to lightweight architectures, such as EfficientNet a convolutional neural network. These lightweight AI
models facilitate faster inference speeds, decrease energy and computational requirements at lower costs.

Discussion
 Implications resulting from research and developing a working close loop recycling appliance and supporting logistics system to
TRL 5 prototypes are discussed below. The next step is to produce an engineering prototype (EP) from which, in a pilot project,
100 appliances will be manufactured to be trialed in homes.  The discussion recognizes that empirical pilot project data is not yet
available and is based on a digital model which produces simulation data rather than empirical data.

Labor and Infrastructure Costs
Up until the CLR collection vehicle at the curb empties the product storage container (PSC), householders have provided labor at
zero cost. By comparison, the touch points or labor requirements to produce manufacturing ready inputs in the existing recycling
system are multiples of those required in a CLR appliance system.  Please refer to Figure 3 which shows the flow of glass cullet in

the existing curb-side system.  Note the touch points and the process steps in the window at the top right of the figure.
Figure 3

Figure 4 below is a flow chart for a glass CLR system based on an appliance in the home. The three separate clear, green and brown
streams of glass cullet are produced by the appliance in the home. Note the reduction in touch points, a proxy for labor costs, by a
factor of two (2X) and the reduction in process steps, a proxy for infrastructure costs, by a factor of thirteen (13X).
Figure 4

Process flow diagrams for plastics and aluminum similarly also deliver multiple times reductions in labor touch points and
infrastructure process steps.

Product Quality, Energy, and Carbon Footprint
In Figures 3 & 4 above, the three streams of brown, green and clear glass cullet produced by the appliance are depicted as the same
as those produced at the end of the traditional recycling system. This is not the case. The cullet color quality is lower in the current
recycling system than that proposed for the CLR system. This lower product quality also applies to plastic and metals.

The main justification for recycling is that manufacturing inputs produced from recycled material should have the same quality
though lower energy input and consequentially lower environmental footprint than inputs sourced from virgin raw materials. The
current recycling system energy use and carbon footprint will be lower than inputs sourced from virgin raw materials. A preliminary
LCA-styled study on rPET production by the Mississippi Polymer Institute compares the existing centralized system from
collection to flake with the Lasso system from appliance to flake (using the Lasso digital model).  The Lasso decentralized system

is forecast to produce lower CO2e GHG emissions per unit weight of rPET produced compared to the traditional recycling system.

Transport Costs and Product Sale Prices
An aggregated bulk product delivery system to manufacturers is viable, especially with the CLR system, since it only transports
size-reduced valuable products. The per weight sale value of the products produced by the appliance are factors higher than the
contents of bales produced by MRFs. Clean washed plastics PET and HDPE flakes ready to be pelletized have a five to ten times
higher sale value than baled containers output by an MRF. Over a five-year period, MRFs paid $22 per ton on average to have
their collected mixed-colored glass transported from MRFs13. Three separate streams of color-pure brown, green and clear glass
cullet as produced by a CLR appliance will be each sold for hundreds of dollars per ton. Consequently, long-distant transport of
cullet to remelt furnaces will become much less of a disincentive to recycle glass. The physical properties of recycling metal cans
make for ease of producing recycled products, hence the premium for closed loop recycled metal shreds compared with compacted
MRF bales is lower than plastics and glass. Closed loop recycled shredded aluminum cans, which are 100% free of contaminating
plastic containers or bags, will receive a sale price premium.

Additional Revenue Streams
Appliance-centric CLR technology delivers high quality and cost competitive manufacturing inputs equal to that sourced from
virgin raw materials. Today’s recycled product sales prices provide a financial margin. Though further and significant profitable
revenue is preferrable. And the recycling appliance’s sensor chamber provides the key to delivering that additional revenue. By
taking an image of each container, its label and bar code, the sensor chamber gains valuable information. The DRS identification
characters can be read qualifying the container for a deposit to be returned. In addition, because each container is size reduced, the
appliance “cancels” each container, guaranteeing that that container never fraudulently re-enters the DRS system to receive more
than one deposit. When allowed by regulations in those US States that have DRSes, the appliance owner will have the bottle deposit
returned to them as easily and simply as when they purchased the product, that is without the need to leave home. In this situation,
the deposit will be returned to the right person, that is the person who paid for the deposit in the first place and not to companies
nor governments. For the low percentage of households that make time-consuming trips to the recycling centers or reverse vending
machines to recover their deposits, a recycling appliance at home will provide them with a convenient time-saving alternative. The
sensor chamber links the consumer, who is closed loop recycling the used container in their recycling appliance, to the brand owner.
The appliance delivers EPR for each container on behalf of the brand owner, a small additional C2B revenue stream for the
householder. Potentially the most valuable revenue stream will result from omnichannel marketing and advertising platforms.

Production Value Chain Comparison
Table 2 below provides a graphical Production Value Chain comparison of the three sources of manufacturing inputs, those sourced
from virgin raw materials, those sourced from the current curb side recycling system and those projected to be sourced from the
proposed CLR system. Energy use, material quality and revenue streams for the three supply chains are compared. The bottom
row provides a forecasted average per container revenue stream comparison.

Table 2

Taking into account a close recycling systems multi-factor (2X – 13X) decrease in labor and infrastructure costs (see Section Labor
and Infrastructure Costs above), add in the multi-factor increase in the sale price of CLR products (see Section Transport Costs

and Product Sale Prices above), include the additional revenue from DRS, EPR and omnichannel marketing and advertising
platforms (see Section Additional Revenue Streams above) the over-all value-add is forecast to more than compensate for the
small-scale amount of product delivered from each appliance in a home or office compared to high traffic locations.

Industry and Stakeholder Solutions
Industry and stakeholder organizations continually call for US States to enact DRSes along with EPR schemes. However, in the
last twenty plus years responses from US State governments to the calls to enact DRSes do not give encouragement. Despite
numerous attempts, the most recent in Texas last year, the last DRS system enacted in the US was in 2002. EPR systems are seen
as positive contributors. However, these take years to implement. Organizing regulations and setting up Producer Responsibility
Organizations (PRO) is time consuming. As previously mentioned, the Californian Bull SB 54 is being re-assessed causing delays.

Industry and Government organizations keep calling for increased infrastructure spending11 in the tens to hundreds of billions of
dollars.  Over decades there have been consistent calls for more community outreach or communication or education of
householders. It is questionable if this money is sensibly spent.  The Ellen MacArthur Foundation’s recent report “2030 Plastics
Agenda for Business” indicates that “Policy and/or collaborative action are required”14 through influencing governments.  The
outlook is that DRSes and EPR systems will not get enacted by State Governments, infrastructure funding from the US Federal
Government is unlikely, and calls for businesses to collectively influence government policies could continue to fall on deaf ears.
In summary, the viability of industry stakeholder calls to improve the performance of the current recycling system is questioned.

A Closed Loop Recycling Solution with privately administered DRSes and EPR Systems
A smart CLR appliance at home supported by an efficient at-home on-demand product collection, aggregation and transport
logistics system can deliver high-quality cost competitive manufacturing inputs. In addition, in the appliance’s sensor chamber, an
image of each container and its label is taken. Assuming the container is accepted by the appliance, that container cannot be
accessed by humans again, unless humans willfully damage the appliance. The image ensures the characters can be read that qualify
a container for a deposit to be returned. After the image is taken and container is accepted it is size reduced, ensuring the container
is cancelled. It’s a simple process to return the bottle deposit associated with the cancelled container to the bank account of the
appliance owner. This process will occur without the householder leaving home. With this process the appliance keeps an
information trail of each container for DRS auditing and guaranteeing the quality of the products delivered by the supply chain.

These features and the data collected exist as a matter of course when operating a CLR system based on a smart appliance enabling
the possibility for privately administered DRSes and EPR systems. It is a simple matter of data transfer between participants. And
privately administered systems don’t need US State regulations.  Such DRSes and EPR systems can also be implemented by
plastic, glass, and metal packaging industries and private companies collectively or separately at a national, state, county, city, town,
postcode or street level.

A Pilot Project for a Closed Loop Recycling Solution
A CLR pilot project based on an appliance in the home, office or other places can be sited in a city or town. It requires approximately
100 willing homeowners to trial an appliance in their home. An estimation of the cost of a pilot project is US$ 4 million.

The following full-scale CLR appliance and logistic system rollout will be funded by the CLR system commercial business case.
There will be no need to call on US taxpayers. Extending ZEV or EnergyStar styled programs to CLR appliances will increase the
rate of CLR impact if desired.

Conclusions & Recommendations
A CLR system based on an appliance in the home, office or other places supported by an efficient at-home on-demand collection
system sets two goals:
• to deliver high-quality high-volume cost competitive manufacturing inputs, and
• to empower householders and users of the appliance to contribute to and benefit from the circular economy. They will
contribute via delivering recycled material to the supply chain while reducing their carbon footprint. They will benefit by
receiving financial reimbursement for their recycling performance.

This paper has technically described an appliance based CLR system and concludes that technically the two goals are sensible,
reasonable and deliverable.

The paper recommends that an appliance based CLR system be considered for pilot projects in several US cities or towns to test
the business model and commercial viability. Testing the business model includes delivering KPIs for closed loop recycling, carbon
footprint reduction and the contribution to the circular economy.

Acknowledgements

References
1. U.S. Environmental Protection Agency Office of Resource Conservation and Recovery Documentation for
Greenhouse Gas Emission and Energy Factors Used in the Waste Reduction Model (WARM) Containers,
Packaging, and Non-Durable Good Materials Chapters December 2023 EPA-530-R-23-021:
- Exhibit 1-2: Process and Transportation Energy for Manufacture of Glass Using Virgin and Recycled Inputs
– page 1.2
- Exhibit 5-8: Process Energy GHG Emissions Calculations for Virgin Production of Plastics –  page 5.7
- Exhibit 5-12: Process Energy GHG Emissions Calculations for Recycled Production of Plastics – page 5.8
2. The Recycling Partnership report, State of Recycling. The Present and Future of Residential Recycling in the
U.S. | 2024 – page 24
3. RSS report Economic Impact of Beverage Container Deposits On Municipal Recycling Processing Costs
Prepared for The National Waste & Recycling Association | January 2022
4. US EPA National Recycling Strategy, Part One of a Series on Building a Circular Economy for All
5. Can-To-Can Recycling: Performance, Potential and Pathways, International Aluminum Institute. September
2025 – Page 5 and, State of Recycling. The Present and Future of Residential Recycling in the U.S. | 2024, The
Recycling Partnership – page 24
6. NAPCOR’s 2020 PET Recycling Report, November 2, 2021 – page 3
7. 2030 Plastic Agenda for Business, Ellen Macarthur Institute November 2025 - page 13, paragraph 2
8. “Calculation of recycled plastic content in the context of the Single-Use Plastics Directive” at the International
Sustainability and Carbon Certification (ISCC) Technical Stakeholder Meeting 25 September 2025 – slide 3
9. “It’s Time to Drive Aluminum Beverage Cans Towards Full Circularity”, Climate Week NYC, 24 September
2024, International Aluminum Institute, Roland Berger - Slide 15
10. Washington State Case Study: Impact of EPR vs. EPR+RR, Ball 50 States of Recycling, Case Study,
International Aluminum Institute. September 2024, – Pages 30 – 33
11.  US EPA Recycling Infrastructure Assessment https://www.epa.gov/smm/us-recycling-infrastructure-
assessment-and-state-data-collection-reports
12. Pet Market in Europe State of Play 2022 Production, Collection and Recycling, Plastics Recyclers Europe (PRE)
for PETCORE, page 8
13. RSS report Economic Impact of Beverage Container Deposits On Municipal Recycling Processing Costs
Prepared for the National Waste & Recycling Association | January 2022, Blended Value Revenue (ACR) For
Average MRF Ton, Price/ton (5-year avg.) – slide 10
14. 2030 Plastic Agenda for Business, Ellen Macarthur Institute November 2025 - page 13, paragraph 2

About the Author(s)
Phil Sanders graduated with a mechanical engineering honors degree from Birmingham City University. He worked 20+ years in
product design and development as a mechanical engineer for Hella Manufacturing as a Lead Designer of automotive lighting on
Jaguar and Land Rovers, then ten years with Electrolux as a senior R&D Project Manager, joining Lasso as CTO in 2017.

Robin Verbruggen graduated in 2018 Summa cum laude as an electrical engineer from Vrij Universiteit Brussels (VUB), Belgium.
He specializes in electronics and rapid prototyping, is part-time lab manager and guest lecturer at the VUB. He has been Lasso’s
electrical and electronics engineer since 2020.

Tobias Van Eeckhout has 10+ years’ experience as full-stack software engineer, and 15+ years as a musician and audio
engineer. He graduated summa cum laude as software engineer at Erasmushoge School, Brussels where he also was a teacher. He
has been Lasso’s full-stack IT solutions architect since 2020.

Aldous Hicks (presenter at conference) has science and mechanical engineering degrees from Sydney University with over 40
years business experience as a technology and software developer, project manager and mechanical engineer, including developing
water and material recycling technology. He holds multiple international patents. He is president and founder of Lasso.
