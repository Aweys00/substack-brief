---
title: "An Investor's Handbook II - AI Power (1)"
source: "Nutty"
author: "Nutty"
url: "https://nuttycld.substack.com/p/an-investors-handbook-ii-ai-power"
published: "2026-07-07T17:26:10+00:00"
words: 1436
preview_only: true
---

# An Investor's Handbook II - AI Power (1)

This article is an informational analysis of industrial and technology structure. It is not investment advice. It does not contain buy/sell recommendations or price targets for any security. The author may hold positions in companies mentioned.

### GPUs arrive in 18 months. Power arrives in 61.

Most discussions of electricity begin with generation: reactors, gas turbines, gigawatts. So when AI datacenters are described as power-hungry, the answer can sound straightforward. Build more supply.

The construction schedule says otherwise. A new GPU generation arrives in roughly 18 months. A completed U.S. generation interconnection now takes about 61 months from request to commercial operation. Between those two clocks is a 43-month gap.

This is a story about the market starting to put a price on those 43 months.

Hyperscalers can buy land. They can buy GPUs. They can sign power contracts. What they cannot simply buy is the front of the generation-interconnection queue captured by the 61-month figure. Approved interconnection rights, gas-turbine production slots already sold years out, and the drying time and test halls required by a 500-ton transformer do not appear just because capital has arrived.

Electricity is usually sold by the kilowatt-hour. In 2026, an AI datacenter is buying something more specific: when that electricity can actually be delivered.

That distinction has split the market over the past year. The power shortage is real. In public markets, the price of scarcity has already hit a regulatory ceiling. Yet the companies selling electricity itself were not always the biggest winners. The larger moves came from names such as Caterpillar($CAT), GE Vernova($GEV), Bloom Energy($BE), Vertiv($VRT), Eaton($ETN), Monolithic Power($MPWR), and Murata($6981.T): companies that help power arrive sooner, leak less, or move closer to the GPU.

Why did one side of “AI power” run while another lagged?

The answer is buried in the route from power plant to transistor. Electricity does not travel straight into a GPU. It moves across transmission lines at hundreds of thousands of volts, steps down near cities, steps down again at the building, converts again inside the rack, and finally falls below one volt on the board.

From 765,000 volts to 0.7 volts: a six-digit voltage waterfall.

At every stage of that descent, the same questions come back. How much power leaks along the way? When can the equipment be delivered? Who can shorten the wait?

Start with the reason electricity has to move through such a long chain. The physics explains why the market’s product shifted from capacity to time.

### 1. Electricity leaks before it arrives

Power plants send electricity out at very high voltage. The highest-voltage transmission lines in the United States run at 765,000 volts. At the other end of the chain, the transistor switches at less than one volt, around 0.7 volts.

That drop exists because loss is governed by current. For the same amount of power, higher voltage means lower current. Lower current means less energy lost as heat. So power plants raise voltage for long-distance transmission. Near cities, voltage steps down. At the building, it steps down again. Inside the server, it is converted again. Beside the chip, it falls below one volt.

This is not a single conversion. It happens at the grid, inside the datacenter electrical room, inside the rack, on the board, and finally inside the chip package. The scale changes. The engineering problem does not. From the power plant to the GPU, the system is trying to manage voltage without wasting too much energy as heat.

The chain is leaky. In NVIDIA($NVDA)’s discussion of the Rubin platform, the company estimated that roughly 30% of the power entering an AI factory is consumed by power conversion, distribution, and cooling before it becomes GPU compute. In a 1-gigawatt datacenter, that implies roughly 300 megawatts supporting the path to computation rather than producing computation itself.

The missing power does not vanish. Much of it becomes heat. Heat requires cooling. Cooling consumes power. That power becomes more heat. Loss compounds.

This is where the simple answer, “just build more generation,” starts to break down. If the pipe leaks, a larger reservoir only pushes more water into the leak. A 1% loss is not small at this scale. In a 1-gigawatt datacenter, 1% is 10 megawatts, roughly the size of a small generator.

AI did not create a problem because the reservoir was empty. It created one because the kitchen suddenly demanded water at fire-hose pressure. The pipe between them was never built for that load.

The AI power problem, then, is not only about generation. It is a problem of the entire path electricity takes. Every link in that path asks two questions: how do we lose less, and when can we get the equipment?

The first question is physics. The second is markets. They first collided at an old datacenter standard: the 48-volt rack.

### 2. When 48 volts broke, 800 volts returned

Datacenter racks have long relied on 48V-class power distribution, often implemented around 54VDC. That architecture works until rack power starts moving toward megawatt scale. At roughly 48 to 54 volts, delivering 1 megawatt requires tens of thousands of amps. High current means thicker copper, more heat, and more loss. The rack begins to fill with enormous copper busbars.

Power engineering has a familiar answer: raise the voltage.

At 800 volts, the same 1 megawatt requires roughly 1,250 amps. Lower current reduces copper and loss. But why 800 volts, rather than 900 or 1,000?

The answer came from electric vehicles, not datacenters. Over the past decade, EV battery systems moved from 400 volts toward 800 volts to charge faster and use thinner cables. That shift built an ecosystem of 800-volt SiC semiconductors, connectors, fuses, and busbars.

Datacenters adopted 800 volts not because it was the mathematically perfect number, but because the component ecosystem already existed. Physics pointed the direction. Supply chains chose the number.

The old lesson from the power war returns here. AC won for so long because changing voltage with transformers was easy. DC used to be hard to transform. As semiconductor switches such as IGBTs, SiC, and GaN improved, the range of places where DC could win expanded.

The physics did not change. The components did.

But 800 volts is only one link in the chain. Change rack voltage, and building distribution has to change. Protection equipment has to change. Board-level power semiconductors have to change. Push on one link and the links above and below move with it.

AI did not stress one point in the chain. It pressed on the entire path from the plant to the chip. Once the whole chain had to be rebuilt at the same time, the real bottleneck became visible.

The issue was not whether something could be made. It was when it could be received.

### 3. Same AI power, different stocks

If the shortage is so clear, electricity sellers should have been the first and biggest winners. AI uses more power. The grid is tight. Reliable peak-time supply becomes more valuable. The simple trade would be to buy generation owners first.

That is not how the market behaved.

Over the past year, companies inside the same “AI power” basket split in unusual ways. They did not move as one group.

Equipment and component makers generally jumped above the 1x line. Bloom Energy did not merely double; at one point it moved close to tenfold. GE Vernova, Vertiv, Monolithic Power, and Murata also re-rated sharply. The companies selling electrons were cooler. Vistra($VST) and Constellation($CEG) grew revenue, yet sat near the lower part of the chart. Another odd case: Navitas($NVTS) saw revenue fall, while its stock jumped on the 800-volt option.

So this was not a clean split between growers and non-growers. Something else separated the top from the bottom.

The market calls all of this “AI power,” as if it were one trade. The chart argues otherwise. Companies that sell electricity, help it arrive faster, reduce loss, or push power through the last centimeters before the chip were assigned different prices. To read the chart, start with the company’s position in the chain, not the ticker.

In what looks like a random scatter of dots, the task is to find the rule hiding underneath.

That search raises the next set of questions. If time has become valuable, how much is it worth? Why did the shortage signal not stay inside electricity prices? What is a power-equipment company really selling when customers fund factories with deposits on products not yet delivered? And how should we understand a company whose revenue fell while its stock rose?

From here, we follow those questions layer by layer.
