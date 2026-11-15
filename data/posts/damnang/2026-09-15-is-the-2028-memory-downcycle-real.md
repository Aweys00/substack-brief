---
title: "Is the 2028 Memory Downcycle Real?"
source: "Damnang Research"
author: "Damnang"
url: "https://www.damnang.com/p/is-the-2028-memory-downcycle-real"
published: "2026-09-15T07:55:49+00:00"
words: 1138
preview_only: true
---

# Is the 2028 Memory Downcycle Real?

HBM is a core technology that made the AI revolution possible. Even though it is more expensive than other memory, chip designers put more and more HBM into their accelerators as a memory solution with high bandwidth and large capacity to process AI workloads. As a result, HBM’s share of total DRAM wafers continued to grow, creating the current DRAM shortage.

However, now in 2026, this trend is changing. There are reports from the industry that NVIDIA has lowered HBM per GPU in Rubin Ultra from 288GB to 192GB and is preparing 8 layers as the new standard. This is quite different from the structure of 16 layers or more that the industry expected a year ago. I have also been covering this HBM density peak while meeting experts working in the memory industry over the past two months.

This is what I ultimately want to address in this article.

Will a memory downcycle really begin in 2028?

Based on the technical details and conversations with people working in the industry, I analyzed how the trend toward fewer HBM layers and the situation in 2028, when supply expansion is planned, would affect the memory cycle from a structural perspective.

In particular, I divided this into two scenarios, HBM with 8 layers and 4 layers, examined the memory hierarchy that HBM despec would affect, and used calculations based on this to predict how a memory downcycle might actually develop in 2028.

Disclaimer

This article is for informational purposes and is not an investment recommendation. Its scope is DRAM (HBM and general purpose DRAM), and it does not cover NAND. The information was checked as of September 14, 2026. The author may hold the stocks mentioned or change positions. Investment decisions and responsibility lie with the reader.

Damnang Research is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

### 1. The HBM density peak is real

As I have said in several of my articles, the current trend is moving toward reducing HBM density and increasing bandwidth. Of course, this has not yet been officially announced, but reports from various parts of the industry are confirming this.

Of course, this decision is understood to be largely due to memory supply. This is because there are not enough HBM wafers to supply stacks with 12 layers in the quantities needed for the logic and CoWoS capacity NVIDIA has secured. The customer appears to have made this decision because moving to 8 layers instead increases yield and ultimately makes it possible to produce more HBM stacks.

Another reason is the increase in HBM prices in 2027. Even when GPU demand exceeds supply, NVIDIA has to give up some margin if component costs rise, and memory accounts for the largest share of those costs. NVIDIA has also notified major customers that it will raise server prices by more than 15% starting with shipments in early 2027.

However, the bigger issue is that this is not necessarily only because of supply and cost. There are also reports that customers reduced it because of power draw or thermal dissipation at the system level. Also, using NVLink to scale up after HBM density despec may have been, to some extent, the optimal configuration the customer wanted, both for processing AI workloads and at the system level. If this is true, it also means that the architecture and workloads are changing at the system level.

In fact, I have conveyed this to my paid subscribers several times on my Substack over the past month. NVIDIA has actually requested samples with 4 layers for HBM4 from memory vendors, and although they rejected this proposal, people in the industry currently think they may have to reconsider for HBM4E. There is also talk within the industry that the hardware team at a certain frontier lab is planning to use 4 layers starting with HBM4. It is reasonable to see this as a structural change that goes beyond a simple issue of supply and cost.

### 2. Memory suppliers decide allocation based on revenue per wafer

When memory suppliers decide whether to use wafers for HBM or general purpose DRAM, the number they look at is the revenue from one wafer. Currently, HBM uses about 3 to 4 times as many wafers as general purpose DRAM for the same 1GB. This is the figure Micron disclosed when comparing HBM3E with DDR5. The December 2025 report that Samsung Electronics would convert some HBM3E lines to DDR5 and LPDDR to secure around 80,000 wafers per month, and the June 2026 report that SK hynix would delay the conversion of HBM3E lines to HBM4 and use them for DDR5, are also in the same context.

Then why sell HBM when they could just sell DRAM?

The reason is contracts.

The HBM being sold now is the annual contract volume signed in the second half of 2025, before the price reversal, and it has volume commitments and prepayments attached. So suppliers fill the contracted volume but do not add beyond it, and converted to DDR5 only where they could. According to stories from the industry, suppliers are asking for +70 to 140% in the 2027 negotiations.

Another thing to know here is that memory companies’ contract structures are changing to long term supply agreements (LTAs). Samsung Electronics said it would tie up 60 to 70% of its total DRAM and NAND capacity, not just HBM, in long term supply agreements of 3 to 5 years. SK hynix is pursuing a contract for general purpose DRAM with Google for 5 years, and Micron is selling about 20% of its volume under contracts covering multiple years with a price floor. This long term supply agreement structure could also directly affect DRAM prices in 2028.

### 3. Three new fabs will increase wafer supply in 2028

The biggest reason many people say a memory downcycle could come in 2028 is the construction of new fabs.

Indeed, Yongin Y1 targets its first cleanroom opening in February 2027, Micron Idaho its first wafer in the second half of the same year, and Samsung P5 operation in 2028.

In the end, I think these three points will determine the memory downcycle in 2028.

First, how many HBM wafers are left over when the layer count is reduced? Does it will reducing the layer count really hurt memory vendors’ profits?

Second, what will happen to 2027 HBM contract prices? How will these HBM contract prices determine the downcycle in 2028?

Third, what will happen to general purpose DRAM supply and demand, and will the HBM premium offset this? What effect will this have in 2028?

From here, I will look at each point in detail and analyze each scenario to examine the memory downcycle in 2028 that many investors are worried about.
