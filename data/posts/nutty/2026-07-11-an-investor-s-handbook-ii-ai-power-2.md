---
title: "An Investor's Handbook II - AI Power (2)"
source: "Nutty"
author: "Nutty"
url: "https://nuttycld.substack.com/p/an-investors-handbook-ii-ai-power-3ae"
published: "2026-07-11T04:01:06+00:00"
words: 2333
preview_only: true
---

# An Investor's Handbook II - AI Power (2)

This article is an informational analysis of industrial and technology structure. It is not investment advice. It does not contain buy/sell recommendations or price targets for any security. The author may hold positions in companies mentioned.

### The electricity has arrived. The last few centimeters remain.

Part 1 began at the power plant. We followed electricity that left at 765,000 volts, rode transmission towers into the city, stepped down through transformers, and arrived at the front of the building. The lesson along the way was a single one: AI did not just increase the demand for power. It changed what the power industry sells, from capacity to time. Five years for a grid interconnection, several years on the turbine calendar, one to two years of transformer lead time. Hyperscaler capital can buy almost anything, but it could not buy those years forward. So the real product upstream stopped being the kilowatt-hour and became the schedule.

Now the electricity is inside the building. But it still has not reached the GPU. The remaining distance is a few centimeters: from the building’s switchboard to the rack, from the rack to the board, from the board to the chip. This last stretch is the shortest segment of the chain and the most crowded. The electricity has crossed a country, and the hardest fight happens in the final few centimeters.

Inside the rack, the nature of the bottleneck changes. Upstream, the scarce thing was time. Here, the scarce thing is the right to supply a part. Each GPU generation draws more power, pulls more current, and demands tighter control of voltage ripple, so more components get packed onto the board, next to the chip, and even inside the chip package, generation after generation. And which company supplies those components is not decided in an open market, order by order. It is decided the moment the board is designed, fixed into the drawing. A company that wins the design-in ships its part with every rack for the life of that generation, and the competition reopens when the next generation’s board is drawn. The industry calls this design-win position a socket. Inside the rack, the money grows with the part count and gets divided by the sockets.

But a growing part count is not the end of the story. If a component is something anyone can replicate by building a factory, supply catches up with demand and the price settles right back down. So the question downstream narrows to one:

Who holds the socket, and can a latecomer buy their way into it?

Part 2 carries that question all the way down to the rack floor, to the transistor’s 0.7 volts. At every layer we will check three things. Does the company hold a material others cannot make? Does it keep winning its place on the drawing each time a new board is designed? And is the set of companies qualified to supply this part a small one? However fast the part count grows, at least one of these three has to hold for that revenue to survive as profit.

The story starts with a component that did not exist two generations ago.

### 1. Storage in the rack: a new component that saves a five-year interconnection

The power draw of a GPU cluster swings violently, on millisecond timescales. Tens of thousands of chips compute in lockstep and pause in lockstep, so the whole cluster yanks and releases the line together. The problem is that the interconnection capacity, and every breaker, switchboard, and cable behind it, must be sized to the momentary peak, even though the average sits at roughly half of it. In effect, half the equipment is built to sit idle most of the time, and that cost is paid whether the peak arrives or not. Shaving the peak means shrinking that idle equipment. It is not a story about saving a few dollars on the power bill.

The mechanism is simple. Put a small energy-storage element inside the rack. Charge it when the load dips, discharge it when the load spikes, and the curve the grid sees smooths out toward the average instead of the peak. Then the interconnection can be contracted at the average rather than the peak. That means running more racks on capacity you already have, or applying for less capacity in the first place. (This is not a grid battery selling power back to the market. It shapes the load curve of a single rack. Different scale, different job.)

The numbers run like this. The previous generation’s storage-equipped power shelf (GB300) cuts peak grid demand by up to 30 percent (disclosed July 2025), and the next generation (Rubin) cuts peak current by up to 25 percent (disclosed March 2026).

Why this storage element matters becomes clear if you look in both directions, up and down. Upward, toward the grid, it directly relieves the Part 1 bottleneck. Cut the peak by 30 percent and you can run that many more racks on interconnection capacity you already secured, so a single component substitutes for part of a grid connection that takes five years to win. Downward, toward the component market, it is revenue born from zero. The last generation was the first time energy storage went into a GPU rack at all, and the quantity jumps from 65 joules per GPU to 400 joules in the next generation, six times over. The storage elements take up roughly half the volume of the power shelf. And this is not an optional feature. Plug in a rack without storage and you must reserve interconnection capacity at the full peak, and that reservation is the five-year queue. It is a component you have to buy to turn the rack on.

There is already a signal that this new revenue is moving through real orders. In June 2026, the Japanese companies that make the bulk capacitors used in these storage shelves raised prices 10 to 15 percent across their entire product lines, and some orders exceeded production capacity. Raising prices on everything, not on one product, is what suppliers do when demand outruns capacity, and the fact that price moved before it showed up in reported earnings makes it a live signal. Which companies collect this money is a question for the component chapters ahead.

Before that, this one component previews the question that runs through all of Part 2: a new component market being born and the money earned there being defended are two separate problems. A rising part count only explains why the pie grows. Who eats it, and how long they keep their share, is not yet decided by anything. That is the next chapter’s question: why do component makers grow faster than their customers, and in whose hands does that growth stay?

### 2. Why component makers grow faster than their customers

One structure runs through everything inside the rack: component-maker revenue always grows faster than the capital spending of its datacenter customers. Last quarter, Texas Instruments($TXN) grew datacenter revenue 90 percent year over year, Monolithic Power($MPWR) grew enterprise-data revenue 98 percent, and Infineon($IFX.DE) tripled its AI power revenue in a year. Meanwhile the capex growth of their hyperscaler customers ran at roughly 50 to 80 percent. Component revenue was doubling and tripling while customer spending grew about half as fast.

Why the gap? Because two variables set a component maker’s revenue: how many more racks the customer buys, and how many of its parts ride on each rack. While customer spending grows by half, the parts-per-rack count also rises every generation, and the product of the two always outruns the customer.

Two components show this is not an abstraction. The first is the multilayer ceramic capacitor (MLCC), the small capacitor that buffers instantaneous current swings right next to the chip. Industry estimates put the MLCC count in one rack (NVIDIA NVL72) at about 440,000 in the last GB300 generation, with estimates of a further rise of tens of percent in the Rubin generation. Yet the companies that can actually make this grade can be counted on one hand. The high-capacitance grades used in AI servers come almost entirely from four companies (Murata, Samsung Electro-Mechanics, Taiyo Yuden, Kyocera), and within that wall, Murata($6981.T) holds 45 percent and Samsung Electro-Mechanics($009150.KS) 39 percent, over 80 percent between the two (shares are industry estimates).

Split this growth into units and price and its real character shows. Murata’s server-capacitor revenue jumped more than 80 percent in a year, but its selling prices rose only 5 to 10 percent over the same period. Most of the growth came not from charging more but from selling more. That is the parts-per-rack story confirming itself in reported numbers. But the same number cuts both ways. Read in reverse, it says that even with this much demand pouring in, prices barely moved. Contrast HBM memory, riding the same AI demand, where supply ran short and prices multiplied. So far, MLCC has been a market where everything made gets sold, not a market where prices surge because nothing more can be made. Volume-led growth has to be sustained by building factories; price-led growth drops straight into margins. That is why the two are not worth the same to an investor, and which side this growth tips toward is a question we settle in chapter 6, against the capacity timetable.

The second component is a case of a layer being born from nothing: the in-rack storage from the last chapter, where the energy stored per GPU jumped from zero to 400 joules in two generations and a whole revenue layer appeared. Power semiconductors follow the same pattern. As the current a GPU draws climbs past 1,000 amps each generation, the number of power stages that split and feed that current grows with it. The parts list for one rack gets longer every generation, and the count next to each line item gets bigger.

And it is not just the count. The technical bar for each component also rises every generation. Take MLCC again. In the top grades, a single ceramic dielectric layer is now down to around 0.5 micrometers (the Chinese suppliers’ mainstream runs about twice that), hundreds of those layers get stacked into one part, and the capacitance packed into the same case size keeps climbing. In 2025, Murata announced an industry first: 47 microfarads in an 0402 case less than a millimeter long. And as boards move to 48 volts, new higher-voltage grades became necessary on top. In short, this is not a market where the same part simply sells in bigger numbers. It is a market where a harder part sells in bigger numbers every generation.

But rising counts and rising difficulty do not guarantee the revenue is defended to the end. Memory semiconductors spent decades proving that. DRAM density rose without fail every generation, and DRAM prices collapsed on a cycle anyway. Any company’s DRAM can be swapped for any other’s as long as the spec matches, so it trades at one market price, and when capacity expands, that one price sinks across the board. Which is why the exception happening inside memory right now is the instructive part. AI-grade HBM, far from collapsing, sold out its 2026 production, and NVIDIA’s volumes are locked in multi-year contracts. That is not because density rose. It is because HBM stopped being swappable. The logic die at the bottom of the stack became a custom part designed separately for each customer, and volumes are sold on contract, not spot. So the lesson from memory narrows to one line: selling more parts does not defend the price. The price is defended when the part cannot be swapped for another company’s.

The components inside the rack face the same test. For a growing part count to harden into profit, the part has to be hard to swap out, and that difficulty usually comes from one of three places.

-

Material: does the company hold a material or process others cannot make, the way Murata mills its own dielectric ceramic powder several times finer than its competitors’?

-

Socket: does it keep winning the design-in that reopens every generation? Win it, and the part ships for the life of that generation.

-

Supply structure: is the set of companies qualified to supply this part a small one?

If none of the three applies, that is, if the part can be made from common materials by any factory that expands, then the price rides the DRAM cycle no matter how fast the part count grows.

That is the map of the rack. Why part counts rise every generation, why that growth outruns customer capex, and what has to protect supply for the growth to harden into price. You now hold three yardsticks. From here on, we press them against each layer in turn.

-

NVIDIA has named exactly fourteen semiconductor companies as 800-volt partners. They should all be winners, yet over the past year their stocks went in opposite directions. The same list contains a price-to-sales ratio of 85 and one of 6, side by side, and the 85 belongs to a company whose revenue fell 45 percent.

-

A materials company that led on technology went through bankruptcy protection and came out, and the market is paying up for it again. That company has now taken a fellow member of the same list to court.

-

The last component seat feeding the GPU core has had three different protagonists in the last three generations. There is even an estimate that the company that was pushed out last generation returns with a 70 percent share in the next. A seat whose holder changes every generation: is that a seat worth buying?

The answers are not in memorizing more tickers. They are in telling apart which layer is scarce in what, whether a latecomer can buy that scarcity away, and whether the market has already put it in the price. Let’s go down one layer at a time.
