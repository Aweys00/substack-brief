---
title: "The Advanced Packaging Primer"
source: "Nutty"
author: "Nutty"
url: "https://nuttycld.substack.com/p/the-advanced-packaging-primer"
published: "2026-09-06T02:24:05+00:00"
words: 3472
preview_only: true
---

# The Advanced Packaging Primer

Along with my friend of Crack The Market, we put his top-down view of market structure and capital allocation next to my bottom-up view of how chips are actually built, to take apart the layer that has quietly become the allocation mechanism for the entire AI buildout: advanced packaging.

owns the market structure, the economics and the investment judgment; I own the process and the physics. One argument runs through the whole piece: yield, not capacity, is what the AI build is short of, and whoever owns the loop that learns it collects the rent, until the format changes.

I write about the semiconductor and AI infrastructure supply chain from the physics up: chips, equipment, materials, packaging, memory, optics and networking, and the power and cooling built around them. The aim in every piece is the same as here, to find where the next constraint lands before the market prices who solves it.

[Join Nutty](https://nuttycld.substack.com/subscribe)

[Join Crack The Market](https://crackthemarket.substack.com/subscribe)

Before this deep dive, four earlier pieces it builds on, two from me and two from Ozeco:

-

An Investor’s Handbook III: Substrate, the layer under everything. How an ABF substrate is built, why its warpage sets the ceiling on package size, who makes it, and where glass core fits. Sections 2 and 7 of this primer stand on it.

-

Intel’s AI Packaging Bet Against TSMC, EMIB-T versus CoWoS. The same bridge answer with the risk parked in the substrate instead of the interposer, and what that means for who learns yield first. The case study in section 5 picks up where it left off.

-

How to invest in the $6-7tn AI Supercycle, a once in a lifetime investment opportunity, and where the chokepoints across the value chain sit.

[Crack The MarketAI Investment Supercycle: How to Invest in the $6-7tn RaceRead more2 months ago · 51 likes · 7 comments · Ozeco](https://crackthemarket.substack.com/p/ai-investment-supercycle-how-to-invest-845?utm_source=substack&utm_campaign=post_embed&utm_medium=web&embedding_publication_id=915696)

-

The semiconductor equipment primer, the picks and shovels of the most important sector in the world. That piece covers the front-end tools; today’s piece covers what happens after the wafer leaves the fab.

[Crack The MarketSemiconductor Equipment Primer: $1.3 Trillion of Market Cap Monopoly and One Problem Nobody Wants to Talk AboutRead more9 months ago · 113 likes · Ozeco and Strategist](https://crackthemarket.substack.com/p/semiconductor-equipment-primer-13?utm_source=substack&utm_campaign=post_embed&utm_medium=web&embedding_publication_id=915696)

## Executive Summary

-

The AI build is short of packaging yield, not wafer capacity, and CoWoS allocation has become the mechanism that rations AI compute.

-

Published market sizes for advanced packaging differ by multiples because they count different things. For an investor in equipment and materials the right denominator is what packagers spend, not what they earn, and that flow is now $20bn plus a year.

-

Margin has moved twice, from the OSATs to the foundry, and now into the tools, consumables and materials the packager cannot get enough of. Once a tool is qualified into a yield-critical step, replacing it means re-opening years of yield learning, which is why supplier lists are short and sticky.

-

Behind the paywall: the architecture map read as a chain of constraints, not a line of succession, and what each move of the bottleneck forces the industry to buy.

-

The three physical limits that forced every bonding transition so far, and the one number that tells you when HBM finally switches.

-

The hidden manufacturing stack, mapped layer by layer with sizes, shares and margins: grinding, lithography, wet process, molding, inspection and test, where several of the best franchises in semiconductors sit unexamined by generalist investors.

-

The panel transition as an equipment reset: which qualifications survive the move to square, which are re-opened, and the three-bucket strategy that falls out of it.

## 1. Why packaging became the binding constraint

### Why chips stopped getting bigger

Open up any recent AI accelerator and one thing repeats. The most expensive chips in the world are all built from several pieces, called chiplets, joined back together. A few compute dies sit side by side, and towers of memory stand around them. If you wanted more performance, why not simply make one bigger chip? The answer sits in how chips are printed.

A chip is made by a lithography scanner projecting circuit patterns onto a wafer with light, and the largest area that scanner can expose in one shot is fixed at 26 × 33 mm, roughly 858 mm². A die has to fit inside that single exposure, so 858 mm² is the physical ceiling on how big one chip can get. Nvidia’s flagship GPUs have been pressed up against that ceiling for years.

TSMC is already in volume production with CoWoS packages 5.5 times the exposure field, carrying up to twelve HBM stacks and a reported yield above 98%. The roadmap it laid out at its North America Technology Symposium in April 2026 runs through 9.5 exposure fields in 2027 to a 14-field package in 2028, which TSMC describes as roughly ten large compute dies plus twenty HBM stacks. The reticle caps the size of one die, and the industry has broken through that wall by binding many dies into one package, which is what packaging has become.

### The yield arithmetic: splitting alone only breaks even

The second reason usually given for splitting chips is yield, and there is a widespread misunderstanding in it. Manufacturing defects land on a wafer more or less at random, so a wider die is simply a bigger target. Take an illustrative defect density of 0.1 per cm² and run the numbers: a large 800 mm² die comes out good about 45% of the time, a small 200 mm² die about 82%. So is cutting the big die into four a winning trade? All four pieces have to be good, which means multiplying 0.82 by itself four times, and the product lands back at 45%. Splitting on its own is exactly break-even.

The real gain comes from being able to test the pieces before assembly. Small dies can be probed one by one on the wafer and the bad ones discarded in advance. A piece that passes is called a known good die, KGD for short. Where one defect used to scrap an entire 800 mm² processor, it now costs you one 200 mm² part. The unit of loss dropped from the whole product to a single component, and that is the center of chiplet economics.

Chip designers had in fact been playing this game inside a single die all along. The H100 physically carries 144 compute units, but Nvidia sold it with 132 enabled: spare capacity planted so that wherever a defect lands, that unit is switched off and the rest still ships as a full product. Cerebras, which uses an entire wafer as one chip, takes the principle to its extreme and shrinks each core to 0.05 mm², so that a defect’s damage stops at exactly that size. Chiplets generalize the same principle beyond the die boundary, and two more advantages come along. The parts that do not need a leading-edge process, such as I/O or cache, can be built on cheaper mature nodes, and a piece verified once can be reused in other products. The reticle limit is what forced the chiplet transition; KGD sorting and node mixing are what made it pay.

### The problem did not disappear. It moved into the package

Splitting the die did not make the engineering easier, though. Four jobs a monolithic chip used to handle internally now fall to the package. It must run thousands of signal connections short and dense enough that the pieces still behave like one chip, deliver hundreds of amps without the voltage dropping on the way, pull kilowatts of heat out, and hold together materials with mismatched thermal expansion, silicon, copper, organic substrate and mold, through every temperature swing.

Heat in particular gets worse with every die stacked on top of another. A simulation published in late 2025 by imec, the Belgian semiconductor research institute, makes the point: with HBM stacked directly on top of a GPU (3D) and no mitigation, the hotspot reached 141.7°C, while the same silicon under the same cooling, placed side by side (2.5D), stayed at 69.1°C. The moment you stack, the lower die’s heat has to pass through the one above it. This is not only a simulation. The zHBM concept Samsung presented at Hot Chips 2026 removes the interposer and stacks the DRAM directly on the processor, which puts it squarely against this heat problem, and Samsung is attempting to get through it by keeping the stack low, around four dies high, specifically because of heat, and by spreading the I/O across the die face so that no single hotspot forms. The same conference brought attempts at the concentrated-heat problem from another angle, Samsung’s Heat Path Block and SK hynix’s iHBM, both of which cut a dedicated heat path through the interface region where heat piles up. All of these are attempts rather than products, and Samsung gave no timeline for zHBM.

The bottleneck never disappears. It moves, and wherever it lands becomes the next equipment market.

The first move of the bottleneck born at the reticle and in yield arithmetic is the wiring between chiplets. It keeps moving after that, and each move brings with it the question of whose equipment and materials the industry had to start buying.

### The commercial consequence

For fifty years packaging was the uninteresting and low margin part of the semiconductor value chain. A wafer left the fab worth tens of thousands of dollars, was probed, ground thin, diced, and handed to an assembly house in Penang (Malaysia) or Kaohsiung (Taiwan) that bonded a few wires, moulded a plastic body around the die, tested it and shipped it for a fee that rounded to nothing. The whole assembly equipment market was worth roughly $5bn in 2025, inside a wafer fab equipment market now guided at $150-160bn for 2026. Nobody wrote research on it because there was nothing to write.

The physics above ended that. A single die cannot economically grow past one exposure field, and the closer it gets to that ceiling, the more of it is scrap. The only workaround is printing several smaller chips and stitching them together on a single base, a process called advanced packaging. Because the speed of that connection now dictates how powerful the chip is, packaging has shifted from cheap wrapping into one of the most critical technologies in AI. And because only one manufacturer (TSMC) can reliably assemble them at scale, that single factory decides who gets to sell AI chips.

[Crack The MarketTSMC: Manufacturing the World’s AI ComputeWelcome to the 53rd investment case, 43rd Resilience & Quality, 30th Reshoring & Sovereignty, 26th AI & Technology idea on Crack the Market (and the most comprehensive TSMC investment case you will find online)! Join me as I dissect the…Read more9 months ago · 59 likes · 1 comment · Ozeco](https://crackthemarket.substack.com/p/tsmc-manufacturing-the-worlds-ai?utm_source=substack&utm_campaign=post_embed&utm_medium=web&embedding_publication_id=915696)

The back end has become the allocation mechanism for global AI compute.

-

CoWoS allocation is how compute is rationed: Nvidia is estimated to hold more than half of TSMC’s CoWoS allocation, around 630k wafers in 2026 rising toward 1.0m in 2027 on supply chain checks, with Broadcom second and MediaTek, AMD and the hyperscalers dividing the rest. TSMC says it does not pick and choose between customers and that it leaves no business on the table, and still describes supply as very tight while pulling in every tool it can. Estimates of the demand-supply gap run from 10% to 20% during 2026 depending on definition, a June figure counting accelerators only against a July one that adds server CPU demand pulled into the same queue. If you cannot get CoWoS slots you cannot ship AI chips, and no amount of wafer capacity changes that.

-

Packaging is now a first-order revenue line for the most important company in the world: TSMC’s back-end revenue went from roughly $2.5bn in 2023 to $7.5bn in 2024 and around $12bn in 2025-26, and advanced packaging is expected to grow from about 9% of TSMC sales in 2026 to 16-18% by 2030. TSMC is already the largest packaging company in the world and it is compounding that position at a 50% growth rate.

-

The money has moved: ASE raised its 2026 capex twice, to $10.5bn, with 70% of the equipment portion going to leading-edge packaging and test. Amkor is spending $7bn on Arizona. Intel asked customers to prepay for EMIB-T substrates and, in its own words, they jumped on it, in the billions. At the August semiconductor conferences the clearest message from compute names was that supply, not demand, is the binding constraint, that Nvidia has moved aggressively to lock up substrates and DRAM, and that AMD’s server share gains owe as much to substrate capacity it booked during the pandemic as to its Venice architecture on N2. Supply chain equals revenue and packaging is the supply chain.

The volume behind this is not an Nvidia story:

-

Roughly 518k wafers per month used some form of stacking in 2025, about 8% of all wafers.

-

By 2030 that is projected at around 3.5m wafers per month, or 38% of everything the industry makes, with HBM, NAND CBA and DRAM CBA carrying the volume and logic carrying the value.

-

The tool and consumable companies serving this are not riding a cycle but a replatforming of how the entire industry assembles its products.

### What is advanced packaging? Why the published numbers disagree by several times

Published estimates for the same market span from under $20bn to over $50bn for the current year, and growth rates from 11% to 59% a year. Why such a wide range? They are counting different things, so let’s map the advanced packaging value chain.

The layer you look at determines which companies look like the winners:

-

The revenue basis makes TSMC the story.

-

The unit basis makes the OSAT floor look bigger than it is.

-

The wafer basis makes Disco look inevitable.

-

The equipment basis makes the whole thing look small, which is precisely why generalist investors have ignored it.

Conclusion: the number that matters is capex, not revenue

For an investor in the equipment and materials layer the right denominator is what the packagers spend, not what they earn, because that is where the tool vendors get paid and it moves earlier and harder than revenue. The two large OSATs alone are spending around $13bn this year, TSMC directs 10-20% of a capex envelope it raised mid-year toward advanced packaging, Intel has earmarked a large portion of its increased capex for EMIB-T, and the memory makers are expanding HBM TSV capacity toward roughly 760kwpm by end-2027. Advanced packaging capex is comfortably a $20bn plus annual flow, growing faster than wafer fab equipment, and concentrated on a short list of suppliers. That flow, not the revenue TAM, is what the rest of this primer sizes.

## 2. The value chain from substrate to system

It’s important to understand that market share numbers in packaging have a shelf life of about a year because of how fast the industry is growing.

### The map

The simplest way to see the chain is as five tiers that a die passes through on its way to becoming a system, plus the design layer that sits across all of them. Each tier has its own economics, its own concentration and its own qualification clock.

-

Materials: Ajinomoto’s ABF build-up film sits under nearly every high-performance package with a share above 95%, and gave notice in May of a 30% price increase. Nittobo’s T-glass cloth manages warpage in the substrate core. The ABF substrate itself is made by Ibiden (70-80% of Blackwell substrates), Unimicron, Shinko, Nan Ya PCB, AT&S and Kinsus. Resonac supplies dicing die attach film and Kao holds around 60% of substrate cleaners. The glass names, Absolics, Samsung Electro-Mechanics with Sumitomo Chemical, Corning, AGC and NEG, are covered in Nutty’s substrate handbook.

-

Foundries doing packaging: TSMC’s 3DFabric platform, CoWoS, SoIC, InFO and WMCM, is the reference architecture and the bottleneck. Intel Foundry offers EMIB, EMIB-T and Foveros. Samsung offers turnkey HBM plus foundry packaging and has its own glass interposer programme.

-

OSATs: ASE with SPIL is the largest and the only one with foundry-scale advanced capex. Amkor is the US-anchored alternative and Intel’s first external EMIB assembler. JCET, Tongfu and Huatian are the Chinese tier. KYEC, Sigurd and Ardentec are the test specialists.

-

Equipment: Bonders from Besi, Hanmi, ASMPT, Kulicke & Soffa, SEMES, Hanwha, Shinkawa and Shibaura. Grinders and dicers from Disco and Tokyo Seimitsu. Wafer-to-wafer bonders from EV Group, Tokyo Electron and SUSS MicroTec. Packaging lithography from Canon, Ushio and Nikon. Wet process from GPTC and Scientech. Molding from Towa, Yamaha Robotics and Besi. TSV etch and plating from Lam Research and Applied Materials, CMP from Applied and Ebara, temporary bond and debond from SUSS, Tazmo and Tokyo Electron. Dispensing and thermal attach from All Ring, Nordson and Musashi.

-

Inspection, metrology and test. KLA, Onto Innovation and Camtek lead inspection, with Chroma, Comet and PVA Tepla in the newer modalities. Advantest and Teradyne make the testers, Tokyo Electron and Tokyo Seimitsu the probers, Cohu and Advantest the handlers, Aehr the wafer-level burn-in. Technoprobe, FormFactor and Micronics Japan make the probe cards that touch every wafer.

-

Design and yield software. Cadence and Synopsys for multi-die design and thermal analysis, PDF Solutions for die-level traceability across the stack, and the IP houses whose interconnect standards (UCIe) decide whether chiplets from different vendors can talk at all.

Among the materials in the list above, the one that earns a paragraph of its own is the substrate. It is the layer that fans wiring out from the package toward the system board and carries the whole assembly mechanically, and for decades the standard has been organic: resin reinforced with glass fiber, the ABF family. As packages grew and the wiring above them tightened, the weaknesses of resin, warpage and dimensional instability, started charging real money, and glass-core substrates are aimed at exactly that opening. By Intel’s published comparison, glass shows half the pattern distortion of organic cores, which matters when many wiring layers are built up on top of each other across a very large package and each layer has to line up with the one below.

### Where the margin pools sit, and how they have moved

Amkor earned a 14% gross margin in 2025 doing what OSATs have always done. ASE earns 21% consolidated but has guided its IC assembly and test margin above 30% for Q4 2026, and its leading-edge business is expected to approach 40% next year as full-process CoWoS scales. TSMC earns around 60% at the corporate level and has said advanced packaging is approaching that from below. Besi runs at 64-68% and Disco above 70%. Technoprobe, a consumables company, earned a 32% EBITDA margin in 2025 and is heading toward 50%.

Margin pools in this packaging value chain have moved twice:

-

The first move, from 2020 to 2024, was from the OSAT floor to the foundry, as TSMC pulled the highest-value assembly steps into its own fabs and priced them like wafers (the move to Foundry 2.0).

-

The second move is happening now and it is the squeeze across the value chain that investors have not yet noticed: from the packager into the tools, the consumables and the materials the packager cannot get enough of. ABF prices are up 30%. Wet process tool ASPs guided up 50% or more for the next format. A high-end vertical MEMS probe card up from around $200k to over $500k in five years. Hybrid bonders at $2-3m against a $0.45m flip chip tool. Every one of those is a price increase passed up the chain by a customer who is capacity constrained.

Conclusion: the OSAT tier is splitting, not rising

Packaging margins are not rising as a group. The OSAT tier is bifurcating and they now look like two very different businesses. ASE is spending $10.5bn to become a second source for CoWoS-class full-process work and is being rewarded with leading-edge margins that will exceed its historic ceiling. Amkor is spending $7bn on Arizona to reach break-even there in 2029 and a 30% margin only if the fab fills in 2030, while its advanced packaging projects sum to just over $1bn across their lifetime. One OSAT is buying a seat at the foundry’s table, the other is buying geographic insurance and hoping the customers follow.

Above them, the reason equipment and consumable margins sit where they do is not pricing power in the abstract. It is that a tool qualified into a yield-critical step cannot be swapped without re-opening the yield learning that took two to three years to close, and the customer knows it.
