---
title: "Vicor Deep Dive"
source: "Nutty"
author: "Nutty"
url: "https://nuttycld.substack.com/p/vicor-deep-dive"
published: "2026-10-01T05:19:12+00:00"
words: 888
preview_only: true
---

# Vicor Deep Dive

Industry and technology analysis, not investment advice · The author may hold positions in the securities mentioned

#### Executive Summary · Free Preview

-

In September, one license led to two increases in revenue guidance. Citing higher royalties, Vicor raised its Q3 revenue growth outlook to “more than 30%” sequentially.

-

Vicor works to reduce power losses directly beneath AI chips. By lowering voltage close to the chip and placing power components underneath it, the company shortens the path that carries high current.

-

Good technology does not guarantee a place in the next generation’s supply chain. Vicor said it lost its role in the H100 power system because the customer chose multiple suppliers.

-

The new agreement lets customers pay Vicor royalties while buying modules from other suppliers. Buying Vicor products as well can reduce those royalties.

-

Why is a company expanding its patent income also building more factories? Whether this strategy merely compensates for weaknesses in product competition or supports a much larger manufacturing business is central to understanding Vicor.

Among companies supplying power technology for AI, Vicor ($VICR) stood out in September. Its stock rose 56.4% from September 14 to September 30. What had happened at this maker of components that deliver power to AI chips?

At the close of regular U.S. trading on September 16, Vicor announced a license agreement with an AI equipment maker. Vicor’s corporate website posted the announcement on September 17. The customer pays Vicor a patent fee and gains the right to buy third-party power modules covered by Vicor patents. Buying Vicor’s high-performance modules as well can earn a discount on the royalties attached to third-party modules. On September 17, the day after the announcement, the stock rose 17.7% from the previous close.

On September 21, Vicor raised its Q3 revenue growth outlook from “nearly 10%” to “more than 20%” sequentially. The company attributed the increase to royalties from the new license. The stock rose 19.8% the next day. On September 30, Vicor raised the outlook again to “more than 30%,” expecting higher royalties from the same agreement. Its plan to turn patents into income was already changing the current quarter’s revenue outlook.

But if Vicor is confident it can grow by selling its own products, why sell the right to buy competing ones? Vicor has said it was the sole supplier of the power solution for NVIDIA’s ($NVDA) A100, but lost that power-system role in the H100 when the customer chose multiple suppliers. Is broader licensing a growth strategy that captures more of the technology’s value, or a defensive move to replace lost product sales with patent fees?

The answer depends on how difficult it is to avoid Vicor’s patents while building the power modules customers want, and what it costs to use a different design. Those costs give customers a reason to pay royalties and influence how much Vicor can charge. To understand the future of a company also expanding its factories, we need to assess how much profit licensing and product sales can each generate. That begins with the tight space directly beneath an AI chip.

### Power Delivery Beneath the Chip

As discussed in “The Economics of the Last 1 cm” and the AI Power Handbook, AI processors consume substantial power while operating at very low voltages.

Supplying the same power at a lower voltage requires more current. Delivering 1,000W at 0.8V, for example, requires 1,250A. Even if the resistance of the wiring carrying that current is just 40 microohms, 62.5W is lost as heat. Double the current and the loss in the same wiring quadruples. This is why designers try to carry power at a high voltage close to the chip before reducing the voltage at the final stage.

Vertical power delivery, or VPD, moves the voltage-conversion components from beside the processor to beneath it. Instead of traveling a long distance across the board, the high current passes straight up through the circuit board, reducing losses. But the space beneath a chip is not empty. It also needs capacitors, which store energy briefly and release it when the chip suddenly demands more. Power components and capacitors must fit together in a tight space, with paths for both current and heat.

Vicor’s approach simplifies the job of the final component. An upstream circuit regulates voltage, while the module near the chip concentrates on reducing it by a fixed ratio. This is Factorized Power Architecture, or FPA. Ignoring losses, a module with a 48:1 conversion ratio takes 48V and delivers 1V. When the chip needs a different voltage, the upstream circuit adjusts the voltage entering the module. Lowering the voltage makes more current available, which is why Vicor calls the final module a current multiplier.

FPA separates voltage regulation from transformation; VPD describes where the power components sit. A competitor can place a different type of circuit beneath the chip. It still has to connect a large current to the chip within that limited space. Vicor’s patents have value because they protect not just voltage-conversion circuits but also structures that solve this connection problem.

Next, we use patent drawings and actual disputes to examine what competitors would need to change to avoid Vicor’s patents. We then assess royalty contracts and factory expansion together to calculate the growth needed to meet the company’s revenue and margin goals.
