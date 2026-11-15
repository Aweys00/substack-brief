---
title: "10 Semiconductor Equipment Stories That Matter in 2026"
source: "Nutty"
author: "Nutty"
url: "https://nuttycld.substack.com/p/10-semiconductor-equipment-stories"
published: "2026-10-13T06:53:14+00:00"
words: 7576
preview_only: false
---

# 10 Semiconductor Equipment Stories That Matter in 2026

This article analyzes industry and technology structures and is not investment advice. The author may hold positions in the companies mentioned.

### Executive Summary

-

The semiconductor equipment industry’s competitiveness increasingly depends on productivity, yield, and manufacturing costs, not just technological capabilities. Ten major developments in 2026 highlight how advances in chipmaking create new business opportunities as manufacturers work to translate technical progress into efficient, cost-effective mass production.

-

ASML’s pricing power and advances in High-NA technology highlight two distinct growth drivers in lithography. Higher replacement parts prices demonstrate the revenue potential of the installed base, while larger mask development aims to improve the productivity and economics of next-generation lithography.

-

AI-driven demand is reshaping investment priorities in HBM and advanced packaging. Supply constraints could push HBM manufacturers toward shorter stacks, while CoWoS capacity expansion requires coordinated investment across interposer manufacturing, bonding, assembly, and testing.

-

Increasing complexity in advanced manufacturing is creating new opportunities for equipment suppliers. 400-layer NAND and GAA transistors demand more precise etching and deposition. Meanwhile, the Applied Materials–BESI partnership, KLA’s advanced packaging inspection initiatives, and FormFactor’s optical testing technologies highlight the growing importance of precision and process integration across semiconductor manufacturing.

-

Technical achievements do not necessarily translate into economic success. China’s progress in DUV-based advanced manufacturing illustrates how additional processing steps and yield challenges can undermine cost competitiveness. For equipment investors, the key is to distinguish technology announcements from actual production adoption, equipment orders, and measurable improvements in manufacturing economics.

There are two easy ways to deal with semiconductor equipment news.

First, do not read it.

Second, read the headline and check the company’s share price. If it has barely moved, close the tab with relief. Another difficult subject successfully avoided.

Understandable enough. Just as EUV starts to sound familiar, along come ALE and high-aspect-ratio etching. Look up one term and three more unfamiliar ones appear. The stock chart is much friendlier.

Put the processes and equipment suppliers used in chipmaking on one map, and this is what you get.

Design the circuit, make the mask, and form the circuits on a wafer. Cut the finished wafer into individual chips, assemble and connect them, then test whether they work. All of this takes equipment. Along the way, cleaning repeatedly removes residue and particles, while inspection checks defects and dimensions before and after key steps. You searched for one company and somehow ended up with an entire industry to study.

Understanding semiconductor processes and equipment does not have to begin with memorizing this enormous map. It is enough to understand how a piece of news changes manufacturing or costs, and what that means for the companies involved.

I have also received several requests recently for phone interviews seeking an industry practitioner’s perspective on semiconductor equipment. My work is mainly in circuit design, so receiving these requests gives me a sense of the interest building around equipment and processes. Recent news offers plenty of examples of efforts to change how chips are patterned, stacked, and packaged.

### 1. ASML’s Reported 10% Increase in Replacement Parts Prices

October 10, 2026 · [TheElec: ASML raises replacement parts prices](https://www.thelec.kr/news/articleView.html?idxno=63515)

ASML is raising prices for replacement parts supplied to Samsung Electronics($005930.KS) and SK hynix($000660.KS) for DUV and EUV lithography systems by 10%, effective for deliveries from January 2027, according to the report. TheElec also reported that price increases for new systems were being negotiated separately. The account is based on industry reporting.

Parts inside a machine have different replacement cycles. Some need replacing while the machine itself still has years of useful life. Customers negotiate parts prices with ASML to keep existing machines running, as well as negotiating when they order new ones.

ASML sells lithography systems, which transfer circuit patterns using light. A wafer, the round disk on which many chips are made together, is coated with a light-sensitive material. The system exposes that material to light in the desired pattern.

Even if you have no plans to buy a new car, higher replacement parts prices raise your maintenance bill. A chip factory can similarly face higher parts costs for its existing lithography systems in a year when it orders no new ones.

#### From Selected Parts to a Blanket Increase

According to TheElec, ASML previously adjusted prices for selected parts when raw-material costs rose sharply or procurement became difficult. This time, the report described a blanket 10% increase for DUV and EUV replacement parts supplied in South Korea. ASML’s [2022 annual report](https://www.sec.gov/Archives/edgar/data/937966/000093796623000014/asml-20221231.htm) also discusses sharing higher material, freight, and labor costs with customers. Negotiating to pass on costs is not new; the notable change in this report is the range of parts covered.

The same report cited industry accounts of tight equipment and parts supply as AI memory and foundry capacity expansions coincide. Customers trying to raise production cannot easily postpone purchases of parts needed to keep their machines running. If the report is accurate, ASML is using its existing bargaining power to apply price increases across a wider range of parts. How much that adds to profit, however, depends on both selling prices and procurement costs.

#### The Price Increase and the Actual Cost

Suppose the total annual cost of a process is 100, and purchases of the affected parts account for 5. If purchasing volumes stay the same and those parts become 10% more expensive, their cost rises to 5.5. Total cost increases from 100 to 100.5, or 0.5%.

The cost burden on customers depends on both the price increase and the affected parts’ share of total costs. Applying 10% to all of Samsung Electronics’ or SK hynix’s capital spending would exaggerate the effect.

The same applies on ASML’s side. Revenue from installed systems includes services and upgrades as well as parts. Applying a price increase for a specific category of purchases by Korean customers to worldwide installed-base revenue would inflate revenue that is not covered by the increase. If procurement costs have also risen, some of the higher selling price goes toward covering those costs.

The disclosed financial results for services and upgrades combine several categories and regions, making it difficult to isolate the profit effect of this increase. The change to watch is the broader range of parts subject to higher prices. Whether increases extend to other customers and regions will indicate how widely ASML is exercising that bargaining power.

### 2. Developing a Larger Mask for High-NA

September 8, 2026 · [ASML and TSMC($TSM): joint development of larger masks](https://pr.cld.tsmc.com/english/news/3338)

ASML and TSMC announced plans to develop larger masks, targeting a pilot line in 2031 and system readiness for leading-edge processes in 2033. An [ASML and](https://www.asml.com/en/news/press-releases/2026/intel-foundry-and-asml-collaborate-to-accelerate-industry-readiness-for-high-na-euv)[Intel](https://www.asml.com/en/news/press-releases/2026/intel-foundry-and-asml-collaborate-to-accelerate-industry-readiness-for-high-na-euv)[($INTC) announcement](https://www.asml.com/en/news/press-releases/2026/intel-foundry-and-asml-collaborate-to-accelerate-industry-readiness-for-high-na-euv) on the same day specified a 6 × 12-inch format.

In the same announcement, TSMC said it expected to use High-NA in leading-edge volume production from 2030 and expand its use thereafter. Circuit devices and wiring are built in multiple layers, with light used to print the required pattern for each layer. The idea is to start with High-NA on layers requiring the finest patterning, then use it on more layers. Larger masks are intended to improve productivity after that initial adoption by increasing the area printed in one exposure. A major customer’s attention is shifting from testing equipment performance toward preparing for volume production.

The light-sensitive coating on a wafer reacts differently in exposed and unexposed areas. A mask is a plate that controls where light reaches the coating to form the circuit pattern. In DUV, it transmits or blocks light; in EUV, reflective and absorbing regions create the pattern. The lithography system reduces this image and transfers it onto the coating. Subsequent processing forms the actual circuit in the wafer.

The object being enlarged here is the mask. The round silicon wafer on which many chips are made is not getting bigger. The aim is to enlarge the region that can be printed in one exposure on the same wafer. That region is called the field. It can contain several small chips, or a single large chip can occupy most of it.

High-NA EUV uses larger mirrors to resolve finer patterns. Larger mirrors, however, increase the angles at which light strikes the mask, making it harder for the mask to reflect the light properly. ASML addressed this incidence-angle problem with optics that reduce the image more in one direction than the other. The circuit pattern on the mask is reduced to one-quarter of its size in one direction and one-eighth in the other.

Conventional EUV reduces the image to one-quarter in both directions. Because High-NA reduces it more in one direction, the printed field is half as long along that axis. With the other dimension unchanged, the area printed in one exposure is also halved. The maximum field goes from 26 × 33 mm to 26 × 16.5 mm.

#### Mask Size and Exposure Area

Moving from a 6 × 6-inch mask to a 6 × 12-inch mask doubles one side and the area. A longer circuit pattern along the direction with 8× reduction is intended to enlarge the field printed on the wafer.

If a large chip will not fit inside a smaller exposure field, its design must fit that field or the pattern must be exposed in sections whose boundaries are joined precisely. This joining of separately exposed patterns into a single circuit is called stitching. A larger mask and exposure field could ease those design and stitching requirements.

A larger mask changes the manufacturing requirements for the blank, its underlying material. A blank is a glass substrate coated with multiple films; it becomes a mask once the circuit pattern is fabricated on it. Flatness and film thickness must remain uniform across the larger plate, and defects must be controlled. Blank suppliers AGC($5201.T) and HOYA($7741.T) are relevant companies to follow.

DNP($7912.T) is among the mask makers that fabricate circuits on these blanks. [DNP has announced the supply of masks for High-NA evaluation](https://www.global.dnp/en/news/detail/2024/12/1212_20176139/). IMS Nanofabrication supplies electron-beam mask-writing equipment, while Lasertec($6920.T) supplies inspection equipment that uses EUV wavelengths to find pattern defects. All need ways to handle a larger plate precisely. Having an existing High-NA product is not the same as having completed preparations for the 6 × 12-inch format.

Masks are reused across many wafers, rather than discarded after one use. Doubling their area therefore does not double sales volumes. The opportunity lies in making and inspecting larger plates without defects. Suppliers that can deliver reliable larger masks can compete for orders under the new format. Blank prototypes, mask-fabrication yields, and inspection equipment for the larger format will show how far preparations have progressed.

#### Equipment Prices and Cost per Chip

Customers want the ability to make many competitive chips more than they want an elaborate machine for its own sake. Suppose allocated equipment costs and operating costs over the same period rise from 100 to 110, while the number of good products rises from 100 to 120. Cost per product falls from 1 to about 0.92.

The denominator is the number of good products that can be sold. It depends on processing speed, uptime, and how many products are defective. Unlike the replacement parts price increase discussed earlier, new equipment can offer the possibility of producing a desired pattern with fewer steps or obtaining more good products.

For High-NA to spread in volume production, it needs to print fine patterns accurately while lowering cost per chip. TSMC’s stated sequence is to adopt it with existing masks, then improve productivity with larger ones. Changing the format for mask fabrication, inspection, and handling creates development needs beyond the lithography machine itself. More detail on the production processes and layers where TSMC will use High-NA, along with progress toward the larger-mask pilot schedule, will indicate how the plan is advancing.

### 3. Considering 8-High HBM amid Supply Constraints

September 29, 2026 · [TrendForce: supply and cost constraints prompt consideration of 8-high HBM](https://www.trendforce.cn/presscenter/news/20260929-13254.html)

TrendForce reported that GPU and custom AI chip designers were considering reducing HBM stack heights from 12 to 8 dies in some products. It attributed this to limited supply and system costs. This was not an announcement of finalized specifications for individual customers’ products.

You might expect a better AI chip to require taller memory stacks. Supply shortages can push the choice in the opposite direction. Customers may accept a little less memory in each system to ship more systems overall.

HBM consists of multiple DRAM chips, which temporarily store data, stacked and connected vertically through many electrical paths. One such group is called a stack. It exchanges large amounts of data close to the compute chip. The terms “8-high” and “12-high” refer to the number of DRAM dies in that stack.

#### Allocating 96 DRAM Dies

For illustration, suppose there are 96 good DRAM dies of equal capacity and no assembly losses. Stacking 12 at a time produces 8 HBM stacks; stacking 8 at a time produces 12. If the number of stacks per GPU stays the same, memory can be allocated to more GPUs. Each GPU, however, has less memory capacity.

Memory capacity and data-transfer speed also need to be distinguished. Reducing the number of stacked DRAM dies does not reduce the width of the connections and their operating speed in the same proportion. It does, however, leave less room for large models and working data. Customers must weigh the capacity their workloads need against the number of GPUs they can obtain.

A move to lower specifications can itself be a consequence of strong demand. When supply is constrained, customers may choose several systems with sufficient specifications over one with the highest specifications. If actual 8-high products launch and shipments expand, that would confirm a product-level choice to distribute scarce memory across more AI systems.

On October 11, Elon Musk also posted a brief reply on X: [“Problem is RAM supply”](https://x.com/elonmusk/status/2109260288314806434). He did not specifically identify HBM. Achieving the desired AI performance and securing enough memory to supply that product widely are separate problems.

#### Assembly and Test Demand for 8-High HBM

A base die sits beneath the DRAM, connecting it to external circuitry. In the example above, increasing the number of stacks from 8 to 12 also increases the number of base dies from 8 to 12. Handling and testing operations performed once per completed stack may increase as well.

Workload changes differently depending on what a tool handles. Cutting and moving individual DRAM dies still involves 96 dies. If each finished HBM stack is tested individually, however, the number of test objects rises from 8 to 12. A 50% increase in stack count does not mean 50% more of every type of equipment is needed. Test time and spare capacity on existing tools also matter when estimating expansion needs.

The same distinction applies to cost. As TrendForce noted, a base die is still needed even when fewer DRAM dies are stacked. The purchase price of one stack may fall without the price per GB falling as well.

Shorter stacks can ease the pressure to make dies extremely thin. Warped or uneven dies are still difficult to bond, however. [Applied Materials](https://www.appliedmaterials.com/us/en/newsroom/press-releases/062526-applied-materials-introduces-new-systems-accelerate-dram-adv-pkg-ai-chips.html)[($AMAT) products announced on June 25](https://www.appliedmaterials.com/us/en/newsroom/press-releases/062526-applied-materials-introduces-new-systems-accelerate-dram-adv-pkg-ai-chips.html) address precisely these issues: die warpage, bonding-surface flatness, and copper-plating uniformity.

If customers choose to produce more 8-high HBM using an existing process, they may buy more of their existing bonders while postponing the adoption of next-generation ones. Stack height alone cannot tell us the direction of equipment demand.

### 4. Making CoWoS Interposers and Assembling the Package

October 8, 2026 · [GlobalFoundries($GFS): agreement to make silicon interposers for TSMC](https://gf.com/news-and-events/news/globalfoundries-reaches-agreement-to-establish-us-based-supply-of-silicon-interposers-for-advanced-ai-packaging/)

GlobalFoundries agreed to manufacture silicon interposers for TSMC‘s CoWoS in the United States. It will expand capacity at its Malta, New York, facility, targeting the start of a production ramp in the first half of 2028.

“If GF is taking on CoWoS, isn’t it taking work away from Amkor($AMKR)?” That is a reasonable question after reading the headline. Both companies participate in advanced packaging. Under this agreement, however, GF’s job is to manufacture the interposer, the plate that connects the chips.

HBM stacks memory dies vertically. In CoWoS, completed HBM stacks and compute chips sit side by side on an interposer. They exchange data through its dense wiring. Making that plate and attaching chips to it to produce a finished package are different jobs.

[Amkor announced an agreement with TSMC on June 16 for advanced packaging and testing services in the United States](https://amkortech.gcs-web.com/news-releases/news-release-details/tsmc-and-amkor-technology-announce-long-term-partnership). GF’s interposer manufacturing and Amkor’s assembly and testing occupy different production stages.

Suppose an assembly line is waiting because interposers are in short supply. More interposers would allow the assembly provider to produce more finished packages. Capacity added at an earlier stage can support work at a later one. Competitive concerns would arise if GF also took on the same assembly and testing work and TSMC reduced the volume allocated to Amkor. The two disclosed agreements instead suggest a plan to secure both packaging components and assembly capacity in the United States.

Taken together, the announcements show TSMC securing component manufacturing separately from assembly and testing in the United States. GF’s expansion could relieve a shortage of interposers and help downstream shipments. How much of that becomes Amkor revenue depends on the products and volumes TSMC actually allocates to it.

Applied Materials supplies the processing equipment needed for this manufacturing work. It sells machines used to make the products, such as the HBM plating and planarization tools discussed earlier. The phrase “participating in CoWoS” therefore does not tell us where revenue comes from. We need to know whether a company supplies interposers, provides assembly services, or sells equipment to the factory.

Expanding advanced packaging involves more than adding an assembly line. Interposer production, assembly, and testing all need to expand for finished-product shipments to grow. The GF agreement is a concrete investment in securing those interposers in the United States. Equipment demand can arise at factories processing these components as well as at final assembly providers.

#### Copper Wiring and Plating Equipment

At its [April 22 technology event](https://pr.tsmc.com/english/news/3302), TSMC said it was producing CoWoS at 5.5 times the area of a conventional lithography field. More compute chips and HBM require more wiring area beneath them. This does not mean the lithography machine’s single-exposure area has grown.

Copper plating is one way to create that wiring. A patterned mold is formed over a thin metal layer, and copper grows in its openings. Removing the mold and the exposed thin metal layer leaves separate copper traces. If thickness differs between the center and edges of a large plate, subsequent connection steps become harder.

Applied’s [May announcement of its](https://www.appliedmaterials.com/us/en/newsroom/press-releases/050326-applied-materials-broadens-advanced-packaging-portfolio-nexx.html)[NEXX](https://www.appliedmaterials.com/us/en/newsroom/press-releases/050326-applied-materials-broadens-advanced-packaging-portfolio-nexx.html)[acquisition](https://www.appliedmaterials.com/us/en/newsroom/press-releases/050326-applied-materials-broadens-advanced-packaging-portfolio-nexx.html) concerns this work. It added plating equipment for large panels to its existing wafer-plating offering. The transaction [closed on June 3](https://www.hkexnews.hk/listedco/listconews/sehk/2026/0604/2026060400142.pdf). As the plates connecting chips grow larger, equipment that can process a large area at once becomes more valuable. The NEXX acquisition can be read as an investment in the plating capability needed as large AI package production expands from wafers to panels.

This manufacturing shift also connects to TSMC’s packaging expansion. [ASE](https://www.aseglobal.com/press-room/310x310)[($ASX) announced development of a panel production line for AI and high-performance computing in May](https://www.aseglobal.com/press-room/310x310). Applied’s opportunity spans a shift toward larger formats by multiple manufacturers, rather than depending on one particular fab.

If interposers are ready but assembly is delayed, or vice versa, finished-product shipments must wait. That is why GF’s 2028 production schedule and Amkor’s factory start-up need to be tracked separately. Even a factory that starts first may be unable to run at sufficient volume while it waits for the next stage.

### 5. Applied and BESI Develop Bonding Processes Together

October 1, 2026 · [Applied Materials and BESI: expanded packaging partnership](https://www.appliedmaterials.com/us/en/newsroom/press-releases/100126-applied-besi-expand-partnership.html)

BESI is joining AMAT‘s EPIC research and development center as a partner. The companies said they would expand their existing hybrid-bonding collaboration to include thermocompression bonding, new assembly architectures, and photonics-related technologies.

Forming circuits on wafers is known as front-end manufacturing; assembling and connecting the resulting chips is back-end manufacturing. AMAT makes a range of front-end processing tools and packaging surface-treatment equipment. BESI makes tools that place and bond chips precisely. This collaboration addresses both preparing and cleaning flat bonding surfaces and aligning those surfaces for bonding.

Accurate placement alone is insufficient when chips need very dense connections. Surface condition, cleanliness, and the height of metal contacts must also be right. The next tool receives and bonds a surface made by the preceding process. Two tools can each meet their own specifications without producing a good result when used together.

Hybrid bonding directly joins copper contacts and the surrounding insulating surfaces. It allows denser connections, but demands correspondingly flat, clean surfaces before bonding. AMAT’s equipment must level and clean the bonding surfaces so that the two faces can make full contact when BESI’s equipment bonds them.

The announcement’s research scope includes improvements to conventional thermocompression bonding, which uses heat and pressure, alongside advanced hybrid bonding. A new method does not make the existing one disappear immediately. Customers choose technologies according to connection spacing, productivity, yield, and cost.

As connections between chips become denser, selecting equipment increasingly means coordinating adjacent processes. Once a bonding surface has been flattened and cleaned, its condition must be maintained during transfer to the next tool. Waiting time or contamination in transit can affect bonding quality. The two companies aim to validate this connected manufacturing sequence together and offer it to customers.

Once customers achieve acceptable yields with that combination, replacing only the bonder can become difficult. A new bonder requires the conditions of the preceding and following processes to be adjusted again. Joint validation can help adoption while also raising switching costs. Customer adoption in volume production and repeat orders will show whether that effect translates into business.

#### HBM Stack Height and Packaging Investment

Shorter HBM stacks ease the challenge of squeezing dies into a fixed height, reducing the urgency of switching to a new bonding technology. Customers can still make more of today’s products with existing thermocompression tools while developing hybrid bonding for the next generation. By researching both approaches, AMAT and BESI are responding to these different investment schedules.

Vertical stack height and the area needed for side-by-side connections are separate issues. Even with shorter HBM stacks, larger compute chips or more HBM stacks placed side by side require a larger interposer. That creates a need for equipment to plate copper uniformly and flatten surfaces over a wider area.

Delaying taller stacks can therefore postpone next-generation bonder adoption without pushing expansion of existing bonder capacity or investment in equipment for larger interposers in the same direction. Whether an order expands output of current products or introduces a new bonding method determines which equipment makers have an opportunity.

### 6. Equipment for Narrow, Deep Holes in 400-Layer NAND

August 5, 2026 · [Samsung Electronics: unveiling V10 NAND with more than 400 layers](https://news.samsung.com/global/samsung-unveils-next-gen-3d-memory-vision-at-fms-2026-charting-the-future-of-ai-infrastructure)

Samsung Electronics unveiled V10 BV-NAND with more than 400 layers and said it used wafer-bonding technology.

The number 400 is memorable. The work equipment does underneath that headline is less visible. NAND is memory that retains information when power is off, and it is used in SSDs. 3D NAND stacks storage structures vertically to fit more data into a limited area.

Adding layers first requires deposition tools to build repeated thin layers of material. Etch tools then remove material where needed to create very deep, narrow holes. Coating the inner walls of those holes forms vertical current paths connecting storage cells across the layers. Distorting a hole’s shape therefore affects the current path formed inside it. Both deposition to build the tall structure and etching to penetrate it are necessary.

#### Controlling a Deep Hole’s Width and Shape

As a narrow hole is etched deeper, its width at the entrance, middle, and bottom must stay within the desired range. Bulging in the middle, narrowing toward the bottom, or drifting off-axis changes electrical characteristics.

The ratio of depth to width is called the aspect ratio. High-aspect-ratio etching creates these narrow, deep holes in the required shape. Fast material removal alone is insufficient; shape and damage must also be controlled.

This is where companies such as Lam Research and Tokyo Electron($8035.T) enter the picture. Lam’s cryogenic etching also addresses deep structures by controlling temperature, plasma, and surface reactions together.

As layer counts rise from 200 to 400, layer thickness may change, the structure may be processed in separate sections, and new tools may do the same work faster. Layer count gives a sense of processing difficulty, but does not directly reveal equipment order volumes.

#### Bonding Storage Cells to Peripheral Circuits

Samsung Electronics explained that it builds the storage cells and the peripheral circuits that operate them on separate wafers, then aligns and bonds the two surfaces precisely. It says manufacturing conditions better suited to the peripheral circuits can improve performance and power consumption.

After the deep holes on the storage-cell side are etched, wafer bonding adds another operation. The bonding surfaces must be flattened and kept clean for the two faces to make uniform contact.

The process of polishing a surface to level it is called CMP. Small irregularities or particles left on the surfaces can prevent proper contact. Even if etching has gone well, failure at the bonding step means no finished product.

The HBM discussed earlier stacks individual memory dies. Here, wafers containing separately manufactured cells and peripheral circuits are bonded together. Different objects being bonded require different equipment.

The race for NAND capacity demands both the ability to etch deep holes and the ability to precisely bond circuits made under different conditions. Planarization, cleaning, and bonding-surface control join etching as increasingly integral parts of realizing the product architecture. As V10 ramps, the question is not just whether it sets another layer-count record, but how reliably this bonded structure can be manufactured.

### 7. Precision Deposition Equipment for GAA

April 8, 2026 · [Applied Materials: deposition systems for GAA](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-introduces-deposition-systems-angstrom-era)

Applied Materials introduced Trillium ALD and Precision Selective Nitride equipment for GAA transistors. The company also said leading-edge logic customers were adopting the systems for processes at 2 nm and below.

One addresses coating complex structures uniformly; the other selectively protects areas that need it. Both deposit material, but they solve different problems.

A transistor is a tiny switch that turns current on and off. The path carrying current is the channel, and the part controlling that flow is the gate. GAA surrounds the channel with the gate on all sides for better control of current. A nanosheet is a channel shaped as a thin sheet.

Coating a flat floor is different from covering the top, bottom, and sides of several thin sheets stacked together. Material arriving from above does not automatically coat the undersides to the same thickness. The gaps between sheets are narrow, too: an overly thick coating in one place leaves less room for the next material.

#### ALD Uniformity and Throughput

ALD, or atomic layer deposition, creates thin films through repeated surface reactions. It uses the self-limiting nature of each reaction at the surface, with thickness controlled by the number of repetitions.

This is useful in complex three-dimensional structures because it can form uniform films on interior surfaces as well as on top. Sufficient reaction time and suitable conditions are needed for material to reach those interior surfaces. Customers must weigh the precision of the film against the throughput they can achieve.

An important part of AMAT’s Trillium description is the precise formation of several metal films and the integration of multiple deposition steps on one platform. Changing gate materials and thickness can adjust the voltage needed to turn the switch on. This gives designers room to tailor transistors within the same chip to areas where speed matters and areas where lower power consumption matters.

Connecting multiple steps in a vacuum environment also matters. Making one film, removing the wafer from vacuum, and then performing the next step can introduce contamination and alter the surface. Making each thin film well must be accompanied by control over the interfaces where films meet.

#### Selective Deposition to Protect Insulating Structures

The Precision equipment announced alongside Trillium addresses a different area. Insulating structures between transistors reduce unwanted electrical effects. Even after these structures have been made, subsequent processing can gradually erode them, changing their intended height and shape.

AMAT described a method of selectively forming a protective nitride film where needed. As circuits shrink, parts that have already been made correctly must be protected from damage in later steps.

Printing a smaller pattern with a lithography machine still leaves the job of making the actual switch. Which materials go where inside the three-dimensional structure and how uniformly they are deposited change how current flows.

Space for those films must first be created. Removing temporary material between nanosheets must not etch away the channels as well. Lam Research‘s selective etching addresses this task of removing only the intended material.

ASM International($ASM.AS) also has a major ALD business. Competition plays out in the particular materials and locations being coated, and in how well the process fits adjacent steps, rather than under the broad label of ALD alone. A platform connecting multiple deposition steps allows customers to validate those conditions together.

Control over materials and interfaces is becoming more important to realizing the benefits of scaling. A new transistor architecture cannot easily deliver its intended power and performance if uniform films cannot actually be made. This announcement already cited adoption by leading-edge customers. Growth in 2 nm production and broader adoption across customers and applications will show how that translates into an expanding deposition business.

### 8. KLA’s Packaging and Optical Inspection Research

September 25, 2026 · [SG Semiconductor: KLA and A*STAR collaboration](https://sgsemiconductor.sg/news/sg-semiconductor-launches-at-innovate-together-2026/)

KLA and A*STAR IME announced a three-year collaboration on process control for advanced packaging and silicon photonics. Research areas include bonding defects, chip-placement accuracy, and measurement of optical structures.

The more expensive chips a large package contains, the greater the loss when a defect is found late. The bonding surfaces and chip positions KLA plans to study are where those losses can arise. Inspection matters increasingly at the connections between chips as well as within them.

Chips go through repeated rounds of material deposition and removal. If something goes wrong in the first few steps and is found only at the end, all the subsequent time and material have been spent on an already defective structure.

The bigger problem is the wafers produced afterward under the same conditions. Finding an abnormality early allows process adjustments or equipment checks. Finding it late means more material has been produced under faulty conditions. Inspection equipment finds defects while also shortening the time manufacturers need to understand and correct their causes.

#### Defect Inspection and Dimensional Metrology

Inspection looks for unwanted particles and pattern abnormalities. Metrology measures whether line widths, film thicknesses, and relative layer positions are on target. Even without an obvious scratch, a gradual change in film thickness can provide an early clue that conditions need adjusting before major defects develop.

If the most precise inspection of every corner of every wafer takes too long, the next process must wait. That is why factories need both tools that examine tiny areas closely and tools that scan broad areas quickly. Deciding where to look and how often is itself part of process control.

KLA’s role is to combine detection capability, measurement precision, speed, and data into information a factory can act on. The ability to see smaller defects alone does not establish that a customer’s total inspection cost has fallen. It also matters which defects the results help prevent earlier.

#### The Cost of Defects Found after Assembly

Imagine bonding two chips. Both may have been made correctly, yet a particle trapped at the bonding surface or a placement error can cause the connection to fail. If the problem is discovered after assembly, assembly costs have been added to the costs already invested in each chip. Whether recovery is possible varies by product and process.

Before bonding, surfaces are checked for particles. During bonding, positions are aligned. Afterward, the bond is checked for gaps. Identifying the stage where a defect arises helps determine which process needs fixing.

In silicon photonics, which carries data with light, fabricated structures and alignment can also affect optical performance. Small differences in component shape can change optical behavior, making structural measurements during manufacturing necessary.

KLA’s [fiscal 2026 annual report](https://ir.kla.com/sec-filings/annual-reports/content/0000319201-26-000027/klac-20260630.htm) says customer adoption of advanced-packaging products has already contributed to growth in its process-control business. Building on packaging inspection products already being sold, this research targets more difficult bonding and optical structures.

Packaging inspection is becoming more important as a way to find problems before more expensive chips are attached, beyond sorting out defects after completion. Slowly inspecting everything would block production, so precision and throughput must improve together. Adoption can broaden if customers add inspection steps while maintaining shipments. Performance on a production line matters alongside defect-detection capability.

### 9. Optical Probe Alignment and Measurement Error

September 23, 2026 · [FormFactor: Pharos optical probe technology](https://www.formfactor.com/blog/2026/pharos-optical-probe-series-for-silicon-photonics-and-co-packaged-optics/)

FormFactor described alignment and automatic calibration features for optical probes used in silicon photonics and CPO. By aligning the position where light enters for each measurement, the technology aims to distinguish component performance from measurement-system error.

Optical interconnect news tends to emphasize data-transfer speeds or laser performance. In volume production, it also matters whether repeated measurements of the same chip produce the same result.

Silicon photonics sends and controls light within a chip. CPO integrates optical engines with compute or switching chips within the same package, shortening the electrical connections between them. This requires precise fabrication and connection of the optical components.

A probe connects test equipment to a chip; an optical probe sends light into the chip or collects it from the chip. A small change in connection position can change the amount of light coupled into it. If a good chip measures poorly because the probe is misaligned, a test intended to identify defects instead creates a false failure.

The automatic calibration and alignment emphasized by FormFactor aim to reduce this measurement variation. A developer manually achieving good alignment once is a different task from measuring many chips under consistent conditions on a production line.

[Coherent](https://www.globenewswire.com/news-release/2026/09/21/3365854/11543/en/coherent-launches-photonlink-integrated-optics-platform-for-ai-infrastructure.html)[($COHR) announced PhotonLink on September 21](https://www.globenewswire.com/news-release/2026/09/21/3365854/11543/en/coherent-launches-photonlink-integrated-optics-platform-for-ai-infrastructure.html), saying it would supply optical assemblies that had undergone precision assembly and testing, in addition to individual components. It expected the revenue ramp to begin in the fourth quarter of 2026. Selling a collection of components as a complete interconnect requires repeated checks that light enters and exits correctly after assembly. As optical suppliers broaden their businesses, alignment and testing increasingly shape product costs and delivery schedules.

[TRITON, which FormFactor introduced in March](https://www.formfactor.com/blog/2026/triton-scaling-silicon-photonics-wafer-test-for-high-volume-manufacturing/), integrates Pharos and works with Advantest‘s electrical test equipment. Tokyo Electron also participated in the joint development. Chips that communicate optically still operate using electrical signals, so both kinds of testing are needed. Expanding optical interconnects creates new test applications for existing electrical test suppliers as well.

#### Assembly Error and Measurement Error

KLA‘s September announcement included measuring optical structures and placement during processing. The October AMAT and BESI collaboration included surface processing and precision bonding. FormFactor addresses connecting to fabricated optical chips and testing their performance consistently. Assembly, inspection, and testing each need to improve for reliable volume production of optical interconnects.

Suppose measured light intensity is weaker than expected after an optical component is attached. Is the component misaligned, or is the probe that injects light during testing misaligned? The first requires a fix to assembly; the second requires a fix to the test connection. Unstable measurements can lead to scrapping good products and adjusting the wrong manufacturing process.

Volume production of optical interconnects needs equipment that assembles parts well, along with the ability to distinguish actual product variation from measurement error. Measurements must be stable before we can tell whether changing assembly conditions has improved performance. Better test equipment can therefore support efforts to improve manufacturing yield.

Precision and speed must be considered together when evaluating these tools. Hypothetically, doubling the test time for one chip halves the number that can be tested in a given period. Faster automatic alignment or testing multiple chips at once can ease that burden. Repeat orders, shorter test times on production lines, and lower retest rates will indicate progress in volume-production adoption.

### 10. China’s DUV Scaling and Volume-Production Costs

March 17, 2026 · [TechInsights: analysis of advanced chip manufacturing in China](https://www.techinsights.com/blog/analysis-can-china-even-build-data-center-ai-chips)

TechInsights said SMIC($0981.HK) had implemented its N+3 process in a smartphone chip using DUV lithography. In the same article, it expressed skepticism about the economics of applying that approach to larger data-center AI chips.

A technically functioning product still needs separate proof that it can be mass-produced at a competitive cost. This is why TechInsights could recognize the commercial chip while questioning the economics of larger AI chips.

DUV and EUV refer to the light used in lithography. EUV’s shorter wavelength makes it better suited to resolving small patterns. Patterns that DUV cannot easily make in a single pass can be divided into multiple operations.

Imagine dense parallel lines that are difficult to print all at once. Print the odd-numbered lines separately from the even-numbered ones. Each set is more widely spaced and easier to resolve. Actual multipatterning has several implementations, but the illustration below shows the basic idea of splitting a pattern.

Dividing the work means precisely aligning each later step with the previous pattern. Depending on the implementation, extra deposition, etching, and cleaning may be required alongside lithography. Other processes and additional work compensate for DUV’s limits. Overcoming a technical barrier and potentially raising processing costs can happen at the same time.

#### Node Names and Actual Manufacturing Conditions

The numbers attached to process generations are difficult to compare directly across companies. In its late-2025 teardown of the Kirin 9030, which underpinned this analysis, TechInsights described N+3 as an evolution of existing 7 nm-class technology, while saying it did not achieve the same degree of scaling as leading suppliers’ commercial 5 nm processes. Measurements of actual structures are therefore more useful than placing node labels side by side.

A teardown can reveal which structures a product contains. Buying and analyzing one chip that reached the market, however, cannot tell us how many of all the chips made at the factory passed. That passing fraction is yield.

For illustration, suppose processing one wafer costs 1,000. If it produces 80 saleable chips, each bears a processing cost of 12.5. If the same spending produces only 50, the cost is 20. Fewer good chips raise cost per chip by 60%.

If extra process steps also raise the cost of processing the wafer itself, the burden can increase further. Conversely, costs fall as a process stabilizes and yields improve over time. A first product launch and sustained expansion of supply therefore need to be read separately.

#### Yield for Smartphone Chips and Large AI Chips

At the same defect density, a larger chip has a greater chance of encountering a defect. That is why yields must be reassessed when a process proven on smaller products is applied to larger ones. Designs that tolerate defects or include repair mechanisms also affect the result.

TechInsights based its outlook for large AI chip economics on these manufacturing issues. The smartphone chip was confirmed through product analysis; the production costs and yields of larger AI chips remain to be established.

A path to advanced products exists even with restricted access to EUV, with the burden shifting to additional processing, alignment, and yield control. The commercial smartphone chip is a real result of that path. The next test is whether it can consistently produce many saleable chips at larger sizes.

In follow-up news, the types of products actually supplied and sustained supply expansion matter more than another claim of reaching a particular node. Repeated deliveries of large AI chips to customers would demonstrate a broader range of applications. Disclosed processing costs and yields would also allow comparison of the cost to make one saleable chip.

Splitting a pattern that is difficult to make in one exposure into multiple operations gives deposition, etching, and process control more work to do. The presence or absence of the most advanced lithography machine alone cannot explain a fab’s technical capability.

### Conclusion

What equipment companies are paid for extends beyond machine precision. It includes keeping customers’ production equipment running and making new structures with fewer defects. Customers keep buying parts after purchasing a machine, and adopting a new bonding method requires validation of the processes before and after it as well.

As the work of improving semiconductor performance expands from fine processing inside chips to connections between them, equipment makers’ roles expand along that boundary. Applied‘s plating acquisition, its joint development with BESI, and KLA‘s packaging inspection all address the challenge of making connected structures reliably, time after time. This is why shorter HBM stacks and investment in packaging manufacturing can emerge together. Customer validation and volume-production adoption determine how quickly the opportunity becomes actual business.

Supplying parts to existing fabs and developing new manufacturing methods generate revenue on different schedules. Next year’s parts price increase cannot be counted as the same revenue as a larger-mask plan several years away. Identifying the manufacturing problem behind an acquisition, product launch, or development partnership helps explain which equipment and technologies customers intend to invest in.

An unfamiliar acronym in the next article is now less reason to close the tab immediately. “Which task becomes difficult without this machine?” Answer that before opening the stock chart, and at least you will no longer be waiting for the chart to interpret the news for you.

### Appendix: Equipment Share Prices and P/E by Process

This groups representative companies from the processes discussed above: ASML in lithography; Applied Materials, Lam Research, Tokyo Electron, and ASM International in processing equipment; KLA in process control; BESI and DISCO in assembly and wafer processing; and Advantest and Teradyne($TER) in electrical testing. Companies spanning multiple processes appear once, under their main business role.

DISCO supplies equipment for thinning and cutting chips. Advantest and Teradyne supply equipment that applies electrical signals to test chip operation. KLA’s structural and defect inspection answers different questions from electrical testing.

Prices are the latest available closes as of October 12, 2026. US and Amsterdam listings use October 12 closes. Japanese listings use October 9 because the market was closed on October 12. Returns are measured against October 10, 2025, the preceding trading day because the one-year comparison date fell on a Sunday. They use each stock’s local currency, exclude dividends, and reflect stock splits. ASML’s Amsterdam ordinary shares are used in this chart.

The P/E ratios on the right divide share prices by the most recently reported 12 months of earnings per share. Basic EPS from company filings is summed across periods, mostly through the end of June 2026; Applied’s period ends July 26. These are approximations because the periods use different weighted-average share counts. They do not use adjusted earnings or next year’s earnings forecasts.

Share-price returns and P/E ratios answer different questions. A stock can rise sharply while its P/E falls if earnings grow faster. Conversely, weak earnings can make the P/E look high even after a smaller share-price gain. ASM International’s earnings here include a reversal of an impairment related to ASMPT, while Advantest’s include gains from remeasuring financial instruments. Neither company’s P/E should be read as a multiple of recurring operating earnings alone. The chart is a starting point for looking at business roles alongside market prices. How much the manufacturing changes in the news will alter future earnings is a separate judgment.

### Key References

#### Lithography, Pricing and China

-

TheElec: [ASML replacement parts repricing](https://www.thelec.kr/news/articleView.html?idxno=63515) · 2026-10-10

-

TSMC and ASML: [Larger masks for High-NA](https://pr.cld.tsmc.com/english/news/3338) · 2026-09-08

-

TechInsights: [China’s DUV-based AI chips and production economics](https://www.techinsights.com/blog/analysis-can-china-even-build-data-center-ai-chips) · 2026-03-17

#### Memory and Materials Processing

-

TrendForce: [Considering 8-high HBM amid supply constraints](https://www.trendforce.cn/presscenter/news/20260929-13254.html) · 2026-09-29

-

Samsung Electronics: [V10 BV-NAND beyond 400 layers and wafer bonding](https://news.samsung.com/global/samsung-unveils-next-gen-3d-memory-vision-at-fms-2026-charting-the-future-of-ai-infrastructure) · 2026-08-05

-

Applied Materials: [Processing equipment for HBM and advanced packaging](https://www.appliedmaterials.com/us/en/newsroom/press-releases/062526-applied-materials-introduces-new-systems-accelerate-dram-adv-pkg-ai-chips.html) · 2026-06-25

-

Applied Materials: [Precision deposition systems for GAA](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-introduces-deposition-systems-angstrom-era) · 2026-04-08

#### Advanced Packaging and Bonding

-

GlobalFoundries: [US silicon-interposer manufacturing for TSMC](https://gf.com/news-and-events/news/globalfoundries-reaches-agreement-to-establish-us-based-supply-of-silicon-interposers-for-advanced-ai-packaging/) · 2026-10-08

-

Amkor and TSMC: [US advanced packaging and testing partnership](https://amkortech.gcs-web.com/news-releases/news-release-details/tsmc-and-amkor-technology-announce-long-term-partnership) · 2026-06-16

-

Applied Materials: [NEXX acquisition and expansion into panel plating](https://ir.appliedmaterials.com/node/29141/pdf) · 2026-05-03

-

Applied Materials and BESI: [Expanded development of bonding and assembly technologies](https://www.appliedmaterials.com/us/en/newsroom/press-releases/100126-applied-besi-expand-partnership.html) · 2026-10-01

-

ASE: [Panel production-line development for AI and high-performance computing](https://www.aseglobal.com/press-room/310x310) · 2026-05-26

#### Inspection, Metrology and Optical Interconnects

-

SG Semiconductor: [KLA and A*STAR research on packaging and photonics process control](https://sgsemiconductor.sg/news/sg-semiconductor-launches-at-innovate-together-2026/) · 2026-09-25

-

FormFactor: [Pharos optical probe alignment and calibration](https://www.formfactor.com/blog/2026/pharos-optical-probe-series-for-silicon-photonics-and-co-packaged-optics/) · 2026-09-23

-

Coherent: [PhotonLink optical assembly and test platform](https://www.globenewswire.com/news-release/2026/09/21/3365854/11543/en/coherent-launches-photonlink-integrated-optics-platform-for-ai-infrastructure.html) · 2026-09-21

Disclaimer. This article provides informational analysis of industry and technology structures and is not investment advice. It contains no price targets or recommendations to buy or sell. Figures and company outlooks are as of the dates stated in the text. Illustrative cost calculations and P/E ratios calculated from reported earnings include assumptions and estimates. Reported parts-price negotiations and company plans for technology adoption and development may differ from actual outcomes. The author may hold positions in the companies mentioned. Readers are responsible for their investment decisions and the resulting outcomes.

Copyright. This article is content for paid subscribers. Unauthorized copying or redistribution is prohibited. Short quotations and links with attribution are welcome. © Nutty’s Research
