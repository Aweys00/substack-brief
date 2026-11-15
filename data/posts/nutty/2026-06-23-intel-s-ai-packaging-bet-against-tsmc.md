---
title: "Intel's AI Packaging Bet Against TSMC"
source: "Nutty"
author: "Nutty"
url: "https://nuttycld.substack.com/p/intels-ai-packaging-bet-against-tsmc"
published: "2026-06-23T17:08:00+00:00"
words: 2163
preview_only: true
---

# Intel's AI Packaging Bet Against TSMC

Intel ($INTC) closed at $140.94 on June 22, a fresh all-time high. That is roughly +570% from a year ago, more than six times the price. A stock that briefly fell to $19 within the past year carried a market value of around $700 billion at that June 22 close, pushing Intel beyond its dot-com-era peak. Everyone says Intel is back. That is fair enough, but if you look closely at what brought it back, the company’s single largest opportunity is still sitting outside all the cheering.

### What lifted the stock, and what didn’t

The biggest force was simply that money came in. In August 2025 the U.S. government converted CHIPS Act grants into equity and took a 9.9% stake in Intel (about $8.9 billion), and SoftBank invested another $2 billion. In September, Nvidia added roughly $5 billion (a stake of around 4%). What that near-$16 billion did was simple. It erased the question of whether Intel might go under. Only half a year earlier the market was doubting Intel’s very survival, and once the government and its biggest customer both walked in holding equity, that risk vanished. The mere fact that this was no longer a company that could fail was enough to re-rate the stock sharply.

The second force was that the CPU genuinely came back to life. Underneath it sits a shift in perception: in the AI era, GPUs are not the only thing that matters. Training a model is almost all GPU, but the moment you move to inference, running a finished model to produce answers, and to the “agentic” stage where many AIs are chained together to do work, CPU demand rises again. Intel CEO Lip-Bu Tan put numbers on it. If the CPU-to-GPU ratio in training was 1 to 8, in inference and agentic work he sees 1 to 4, maybe even 1 to 1.

“Right now the demand is very high for my CPU.”

And it is not just talk. Data-center CPU revenue grew 22% year over year, and Intel beat market expectations for six straight quarters. On the day of the first-quarter results in April the stock jumped 24% in a single session, its best day since 1987, and that month it rose 114% for the best month in its 55 years on the Nasdaq. One caveat is worth flagging, though: this “CPU revival” is not Intel’s win alone. The same current lifted rival AMD and the ARM camp just as much. AMD rose about 46% in May alone, and its server revenue share hit a record high.

What is striking is that foundry barely appears on the list of forces behind this rally. Intel’s contract foundry, where it makes other companies’ chips, and the advanced packaging this piece is about, carry some expectations in the price, but they are hard to call the main engine of this run. The numbers make that obvious. Of Intel Foundry’s $17.8 billion in 2025 revenue, only $307 million came from external customers, about 1.7% of the segment, while the rest was mostly internal billing Intel paid itself to make its own chips. That segment lost $10.3 billion last year. It is a business with almost nothing yet to call revenue.

This is exactly where the piece begins. The fact that foundry and packaging are not fully reflected in the stock means, flipped around, that if this business reaches full stride it becomes a second growth axis the current price has not really counted. Some expectation is mixed in, but with revenue only just beginning it is too early to price seriously, and if the business does take hold, Intel shifts from “a company that makes CPUs” to “a company that also assembles and fabricates other people’s advanced chips.” That is a rather different company from the one the stock is drawing today.

So this piece looks at that second possibility: exactly what Intel is trying to do in packaging and memory, and whether the attempt can work.

### It can’t win head-on, so it opens a side door

Start with the man leading the attack. Lip-Bu Tan is both an engineer and an investor. He ran the chip-design software company Cadence ($CDNS) for twelve years and lifted its stock more than thirtyfold, and through his venture fund he has backed hundreds of semiconductor startups, so he is more at home reading the board and deploying capital than building chips by hand. A line he relayed from a customer on the No Priors podcast (June 18, 2026) compresses this whole story into one sentence.

“Some of the customer ask me give me the whole rack.”

Not a single chip, but an entire server rack with chip, memory, packaging, and system assembled into one block. For thirty years the industry split this work into specialized pieces, and now, in the AI era, a customer is asking the CEO directly to bundle those pieces back into one. Who reassembles what has been scattered? Intel is moving for exactly that seat.

It helps to be clear about what Intel cannot do. Intel and Samsung both pour money into foundry, aiming to take share in the “leading node” that TSMC nearly monopolizes, the newest generation that prints the smallest and fastest transistors. Taking that head-on does not happen quickly. Tan admitted as much himself.

“We are very distant from TSMC in term of their performance. We have to be humble looking at building the building block.”

He puts Intel’s real ascent at 2030 to 2032. This is a business the CEO himself prices for after 2030, not now. A frontal node fight will not pay off within the next few years.

Here Intel makes a clever move. The bottleneck in chipmaking is not only the leading node. Packaging, the back-end step that joins finished chip pieces into one assembled product, is just as jammed. In the AI-accelerator era packaging suddenly went short, and Tan, in the same interview, pointed straight at it: the other part that has also become the bottleneck is the advanced packaging. And packaging is an area Intel has honed for nearly twenty years, one where it can genuinely compete. It trails TSMC badly at the leading node, but in packaging it can hold its own.

So Intel’s strategy reads like this: instead of breaking through the front at the leading node, go through the side door of packaging first. TSMC’s real strength is not the smallest transistor alone but the fact that the leading node, the packaging (CoWoS), and one key memory layer (the HBM base die) are tied together in a single bundle. A customer who wants only one of them finds the rest already there and ends up locked to TSMC. Intel means to unpick the weakest link in that bundle, packaging, first. Make customers take their packaging at Intel, then use that as a foothold to pull in the most expensive leading-node fabrication, a detour route. The front is blocked, so go in the side door and widen the path from inside.

This story does not end with Intel alone. If Intel’s EMIB, and especially its next-generation EMIB-T, relieves even part of TSMC’s packaging bottleneck, the companies that supply that packaging, in substrate, assembly, and equipment, ride the same current. So this piece does not look at Intel only.

### The three chokepoints TSMC holds

Think of TSMC’s moat as the world’s smallest transistor and you have seen only half of it. The real moat is not one node but three things interlocked, arranged so that a customer who borrows one ends up taking the other two from TSMC as well. Read the three from top to bottom, because that order is also the size of the gap Intel can pry open: hard at the top, looser toward the bottom.

-

The first is the leading logic node. This is the ability to print the compute die, the heart that actually runs the math inside a GPU, with the smallest and fastest transistors. Nvidia and AMD only design their chips and leave the making of that design into real silicon to TSMC, queuing up by reserving capacity a quarter at a time. TSMC’s share here is effectively a monopoly, and not only because the transistors are small. The yield to pull the same design out in volume without defects, the ecosystem of tools and proven circuit blocks designers lean on, and years of trust that “hand it over and it comes out” are all bound together. This is the hardest of the three to crack, and it is exactly where Intel said a frontal fight takes time.

-

The second is CoWoS packaging. This is the back-end step that joins the divided compute dies and memory stacks inside one package at very high speed, and Nvidia’s H100, Blackwell, and Rubin all sit on it. TSMC alone supplies this seat in volume, demand runs well ahead of supply, and a new line takes years to lay, so it cannot be expanded overnight. CoWoS is therefore chronically short, to the point that Nvidia alone is estimated to have booked more than half of 2026 capacity. You can borrow the node cleanly, but with no seat to mount it the chip does not ship. The weakest link in the bundle is this second one, and because the shortage is chronic, a gap opens for someone to slip in.

-

The third is the HBM base die. A new chokepoint appeared recently. HBM is a stack of DRAM layers (high-bandwidth memory, more on it below), and at the very bottom sits a single logic chip called the base die, which organizes and relays signals between the memory above and the GPU outside. From the HBM4 generation this base die grew complex enough to be built on a leading logic-foundry process rather than a memory fab’s DRAM process, so one layer of memory suddenly became foundry work. SK hynix ($000660.KS) in fact has TSMC make this base die, which means even the world’s top memory maker buys one layer of its own memory from TSMC.

Hold all three at once and the customer is effectively locked in. Want only the node and the packaging is there; want the packaging and there is no seat. That is the power of the bundle. Intel aims not at the first, which is hard to take head-on, but at the relatively weak second (packaging) and third (memory). Hence the two fronts.

### Why packaging became the bottleneck

Chips were once better the bigger they were, since cramming in more transistors made them faster. With AI accelerators that formula stopped working, for two reasons. One, you cannot make a bigger chip even if you want to: the lithography tools that etch a chip have a physical ceiling on how large an area they can print at once, and Nvidia’s latest compute die is already up against it. Two, bigger means more waste: as a chip grows, the odds of a defect landing inside it rise, and a single defect ruins the whole large chip, so the share thrown away climbs steeply with size.

So the industry took the path of chiplets, splitting one giant chip into several smaller ones by function. Smaller chips yield better and dodge the size ceiling. But a new task appears: the divided chips must be joined back into what behaves like one chip, and as fast as signals once moved inside a single die.

The two best-known pieces being split and rejoined are the GPU and HBM. The compute die is broken into smaller chiplets, while HBM is stacked vertically and placed right beside them in the same package. AI has made memory the bottleneck: the model has to stay close, and data has to feed the compute engine continuously.

That only works if HBM and the compute die are connected at extremely high bandwidth. Advanced packaging, such as CoWoS, is the bridge that makes this possible. In Tan’s own words, memory is now the bigger shortage, and adding fab capacity takes years. Memory is scarce, and so is the packaging seat needed to mount it.

The fight over this “rejoining” seat has become the hottest battlefield in semiconductors. It is the bundle’s second chokepoint.

### Who sits on which layer

Here is the whole story on one page: an AI-accelerator package dissected top to bottom, with the companies sitting on each layer. The two seams Intel is prying into are marked in red, EMIB in packaging and ZAM in memory.

Three questions hang over the map. The rest of this piece works through them one at a time.

- Intel lost the node race, so what kind of moat does it actually hold in packaging, and is it enough to shake TSMC?

- The technology has been around for twenty years. Why did its opening come only now?

- A company that no longer makes memory cells, how deep into the HBM business is it really trying to go?
