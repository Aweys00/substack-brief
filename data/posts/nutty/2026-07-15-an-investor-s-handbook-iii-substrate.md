---
title: "An Investor's Handbook III - Substrate"
source: "Nutty"
author: "Nutty"
url: "https://nuttycld.substack.com/p/an-investors-handbook-iii-substrate"
published: "2026-07-15T08:03:22+00:00"
words: 3247
preview_only: true
---

# An Investor's Handbook III - Substrate

This article is an informational analysis of industry and technology structure. It is not investment advice. It does not contain buy/sell recommendations or price targets for any security. The author may hold positions in securities mentioned.

### Three Headlines Pointing at the Same Place

In the first two weeks of July, three seemingly unrelated stories went by.

Samsung Electro-Mechanics ($009150.KS) is starting a glass company. Together with an affiliate of Japan’s Sumitomo Chemical ($4005.T), it committed to a joint venture that will make glass for semiconductor substrates: board-approved, capital and all. A few days earlier, a report had surfaced about the next flagship AI chip NVIDIA ($NVDA) was preparing: a product originally designed to join four large compute dies in one package would reportedly ship as a two-die design instead (unconfirmed by NVIDIA)1. The reason the reports pointed to wasn’t the chips themselves but what sits beneath them: the warpage and assembly difficulty the package would face with four dies attached. And in early July came news that Samsung Electronics ($005930.KS) and SK hynix ($000660.KS) were pushing the adoption of the most advanced bonding technique for next-generation memory back by a generation2.

A glass company in the making. A chip cut in half. A bonding technology postponed. The common denominator of the three stories isn’t the transistor. None of them is about making chips. All three are about what holds chips up and ties them together.

For half a century, the semiconductor industry obsessed over one thing: smaller. Shrink transistors to 10 nanometers, then 5, then 3, and you fit more of them in the same area. Miniaturization was the technology, and the process-node number was the league table. That blade has dulled. What’s being sharpened instead is the needle and thread that stitch chips together. The performance of the next generation is now set less by the circuits inside a chip than by the “land” that carries it and the “bridges” that connect it. The war of nanometers is ending. The war of micrometers has begun.

This piece comes in two halves. The front half deals in physics that won’t change with time: why the substrate, of all things, has come to decide the next generation — and why now. The back half confronts that physics with the reality of July 2026: who holds the board, where the money has actually gone, and where the map everyone calls “glass substrates are coming” gets it wrong. Why those three headlines are one story is where we’ll end up.

### 1. Why Chips Can’t Get Any Bigger — Two Limits

Bigger AI models need more transistors on the chip. Fitting more means growing the chip, and there are limits you cannot cross.

#### The First Limit — How Much You Can Draw in One Shot

The first limit is light. Semiconductor circuits are printed with it: light passes through a patterned mask and exposes the wafer. There is a hard cap on the area that light can cover in a single exposure. The maximum a lithography tool can draw at once is called the reticle limit: 26 by 33 millimeters, roughly 858 square millimeters. Anything larger can’t be printed in one shot. You can stitch multiple exposures together, but stitching adds seams and complexity.

The compute die of NVIDIA’s H100 data-center GPU (the GH100, unveiled in 2022) already measured 814 square millimeters and carried 80 billion transistors, or 95 percent of the ceiling. So the next generation, Blackwell (B200), announced in 2024, simply placed two reticle-sized dies side by side. Two hundred billion transistors won’t fit on one die, so two dies talk to each other over a 10-terabyte-per-second link and behave as one chip. When one sheet wasn’t enough, they sewed two together.

#### The Second Limit — The Sharper the Tool, the Smaller the Shot

The second limit squeezes from the opposite direction. On the layers that adopt the next generation of lithography, High-NA, the tool covers only half the area per exposure. To print finer features, its optics compress the image harder: the horizontal axis shrinks by a factor of four as before, but the vertical axis shrinks by eight, twice as much. The result is that a single shot from the same mask covers half the height: 26 by 16.5 millimeters, about 429 square millimeters. Any circuit taller than 16.5 millimeters must be stitched — not at 858, but already at 429.

The very tool you adopt to make things smaller makes the chip you can draw in one shot smaller too.

Miniaturization (finer) and enlargement (bigger) collide head-on inside the same lithography tool. So the pressure to “split the chip into pieces and reconnect them” doesn’t ease as miniaturization advances; it grows with it. The newer the node, the harder a big chip becomes, and the stronger the case for splitting and stitching. That collision is the hidden half of “why now.”

### 2. Split It, Stitch It — and the Price You Pay

Even setting size limits aside, there’s another problem: yield.

Picture a large sheet of paper ruled into a grid, each square one chip. Now dip a brush in paint and flick it across the sheet once. Any square hit by paint is defective. If the squares are small, plenty survive untouched. Draw the squares large, though, and a single stray droplet ruins the whole square.

A semiconductor wafer works exactly like this. However refined the process, defects scatter across the wafer at some density. The bigger the die, the higher the odds a fatal defect lands inside it, and survival rates fall off fast. Under a yield model for a mature process, a fingernail-sized 100-square-millimeter chip survives about nine times in ten, while an 858-square-millimeter chip that fills the reticle survives around four in ten. Grow the area eightfold and the survival rate is cut to less than half.

Then time compounds the problem. A newly ramped leading-edge process starts with high defect density and improves over years. Assume an early process with twice the defects: small chips still survive eight in ten, but the 858-square-millimeter giant falls below two in ten. And yet peak performance demands exactly that newest process. Making big chips on the newest process, right where performance needs them most, is doubly punished.

So the industry’s answer was to go the other way.

Instead of building one giant chip, split it into small pieces and reconnect them. Each piece is called a chiplet. Print a castle whole on a 3D printer and one flaw scraps the entire castle; build it from Lego bricks and you swap out the one bad brick. Small chips yield better, cost less, and never hit the reticle cap. Each piece can even use a different process: compute cores on the expensive leading edge, I/O circuits on cheap mature nodes. Marble for the living room, brick for the storeroom: a sensible allocation. One large Intel processor combines 47 functional pieces built on five different processes; NVIDIA’s Blackwell stitches two reticle-limit dies together. Splitting is now the default.

But the split exacts a decisive price.

When there was one chip, every conversation ran over on-chip wiring: fast, wide, energy-efficient. The moment you split the chip, conversations that used to happen inside must now travel outside it. A team that met face-to-face in one building is scattered across several, doing everything by video call, and the quality of the video call now sets the whole team’s productivity. If the links between chiplets aren’t as fast and wide as on-chip wiring, splitting loses its point.

Making chips well is no longer enough. The era belongs to whoever connects them well. And the stage where that connecting happens is the substrate.

One company, worth a footnote here, looks like an exception to the yield law. Cerebras ($CBRS) uses an entire wafer as a single chip. The trick is repetition. The chip is an array of hundreds of thousands of identical small cores, so wherever a defect lands, that core is switched off and the wiring routes around it. The latest generation (WSE-3) fabricates roughly 970,000 cores and activates about 900,000, a design that doesn’t avoid defects but lives with them3. Flip that around and you see why it works only for repeated arrays. An ordinary chip like a GPU, with distinct function blocks interlocked, can’t pre-plan for every place a defect might land, so for normal chips, the bigger-means-lower-yield law holds. The exception proves the rule.

### 3. The Second Semiconductor — the Land and the Bridge

The structure that binds split chips together is a three-story building. Let’s fix the vocabulary here, because the rest of this piece is built on these three floors.

The bottom floor is the substrate: the land that carries everything. It feeds the chips power, connects them to the motherboard outside, and physically supports the whole package. It used to be treated as a mere plastic pedestal.

The top floor is the chips: the GPU and, stacked beside it, high-bandwidth memory (HBM), the parts that actually compute and store.

When there was one chip, you just set it on the land. With the chiplet era, the chip pieces upstairs need to talk to each other at extreme speed, so a new floor slid in between: the interposer, the intermediate connecting layer. It lays wiring less than one-fiftieth the width of a human hair, cutting wide, fast passages between chiplets. Of the “land and bridge” in this section’s title, the bridge is this layer. From here on, “substrate” means the bottom floor, “interposer” means the connecting layer, and the “bridge” you’ll meet later refers to a small piece of silicon that does the interposer’s job locally.

This three-layer stack is the archetype of 2.5D advanced packaging. Its flagship implementation is CoWoS from Taiwan’s TSMC ($TSM): Chip-on-Wafer-on-Substrate: chips on a wafer (the interposer), that wafer on a substrate. The name is the structure.

Within this structure, the central question narrows to one: what do you make the interposer and the substrate out of? That material choice sets performance, cost, and how many AI chips can be produced at all. The layers below the chip are no longer a pedestal. They are a giant circuit in their own right, a second semiconductor that sets the ceiling on system performance.

And there’s an unexpected bottleneck in making that connecting layer. The material used for interposers today is silicon, the same stuff as the chips. Silicon interposers are made on semiconductor wafers. The process isn’t as advanced as chipmaking (TSMC runs dedicated backend fabs for it), but the money, tools, and engineers that expand those fabs come out of the same company’s pocket. Linking two dies at 10 terabytes per second takes wiring density organic wiring alone can’t offer, so silicon enters the connecting layer somewhere (as a full-area interposer, or as the local bridges we’ll meet later). And however fast demand explodes, this capacity grows only as fast as a semiconductor fab can be built and filled. The capacity to make the connecting layer has itself become the scarce resource. That is the essence of the bottleneck.

The cost is nothing to shrug off either. A single large silicon interposer claims a hefty share of packaging cost by itself, and because silicon comes from round wafers, the yield problem we just saw applies in full: the bigger the interposer, the fewer per wafer and the higher the defect rate.

With AI chip demand exploding, the best connecting layer has become the biggest bottleneck. So people went looking for other materials.

### 4. Three Kinds of Ground — There Is No Perfect Material

Three materials can plausibly serve as substrate and interposer. Their strengths and weaknesses are near-opposites, so no single one beats the other two outright. Understand these three characters and everything that follows reads easily.

#### Organic — 25 Years on the Throne, Two Cracks

First, the organic substrate, the incumbent king. Built by laminating resin and glass fiber layer upon layer, it’s cheap and dependable. After displacing ceramic substrates in the late 1990s, it spent 25 years as the quiet cornerstone of semiconductors. In that time transistors shrank from hundreds of nanometers to three, and chips grew thousands of times more capable; the substrate simply did its job on the same material. The trouble is that, faced with AI chips, this quiet reliability has started failing two tests at once.

One is heat. Materials expand when heated, each at its own rate, called the coefficient of thermal expansion. When an AI accelerator heats up under hundreds of watts, the chip above (silicon, roughly 2.6) and the substrate below (organic, 14 to 18) both stretch, the substrate five to six times faster. Two runners with ankles tied together, taking different strides. In small packages you could ignore it; at AI-package scale, the mismatch bows the substrate, and in the worst case cracks the joints between chip and board. Warpage grows roughly with the square of package size, so the problem worsens sharply, not linearly, as packages grow.

The other is signal. As electrical signals cross the substrate, the material soaks up a little of their energy. Think of a car on an unpaved road: fine at low speed, but at the extreme speeds AI chips demand, the signal smears beyond recognition. Restoring a smeared signal takes circuitry working furiously, which burns power, which makes heat, which degrades the signal further. The road didn’t get worse; the required speed got faster. And at that speed, the same bumps become walls.

#### Silicon — the Best Connecting Layer, and the Most Expensive

Second is silicon, the interposer material from chapter 3. The two tests that trip organic, silicon passes at the starting line. Same material as the chip, so thermal expansion mismatch is essentially nil; wiring drawn with semiconductor lithography packs passages tens of times denser than an organic substrate. If two chips need a 10-terabyte-per-second conversation, silicon, whether laid as a full sheet or embedded as slivers, is the material that actually carries it today.

The problem is the bill. As chapter 3 showed, a silicon interposer builds what is, functionally, a wiring board out of scarce, expensive semiconductor-fab capacity; and being cut from round wafers, its yield worsens as it grows. Yet silicon remains today’s answer for obvious reasons: it’s proven, it’s in volume production, and it remains the densest connection anyone has qualified at scale. So the question about silicon isn’t “can we use it?” but “for how long, at what size, and at what price?” That question is one of the main threads of what follows.

#### Glass — the Physics Says Yes, the Track Record Isn’t There Yet

Third is glass. On precisely the two tests organic fails, it scores well. Tune the composition and its thermal expansion nearly matches silicon: adding or removing certain oxides tightens or loosens the atomic network, adjusting how fast it swells. Its signal loss is far below organic’s too.

It carries two more traits organic can’t imitate. One is the surface: glass is smooth at the atomic scale. If an organic surface is a dirt road, glass is a skating rink.

The value of that smoothness shows up in next-generation bonding. Today, chips attach to the layers beneath them through tiny solder balls, and ball size and spacing cap how dense the connections can get. The answer is hybrid bonding — no solder, copper faces joined directly to copper faces. Between silicon dies, it’s already in commercial use. The conditions are brutal: mating surfaces must be polished to the sub-nanometer class (generally below 0.5 nanometers; leading-edge processes push 0.1 to 0.2), and a speck-sized undulation ruins the joint. Bringing this down to the chip-to-substrate level requires the substrate to hold that flatness and dimensional stability across a large area. The actual bonding faces are made by precision-finished copper and dielectric layers on top of the substrate. But on an organic base that’s rough and warps with heat, polishing those layers to atomic flatness is a struggle. A glass core provides that foundation: neither a precondition for the bonding nor, by itself, an enabler of it, but a stronger starting point as areas grow. If this technology reaches the substrate level, connection pitch shrinks from tens of micrometers to a tenth of that, packing tens of times more passages into the same area. Here lies the strongest answer to the era’s assignment: the more you split, the better you must connect. This thread returns later, when it collides with the reality of 2026.

The other trait is transparency. Light passes through, which means light guides could one day be embedded in the substrate itself, linking chips with photons instead of electrons.

Glass also enters the package through two doors, not one. Door one: replace the silicon interposer (a glass interposer). The aim is cost: build the connecting layer without an expensive semiconductor fab. Door two: swap the substrate’s core from organic to glass (a glass-core substrate); the insulating films and copper wiring stacked above and below the core stay. The aim is performance: break past organic’s physical limits of warpage and signal loss. Same material, different layer, opposite economics. Which door each company in the “glass camp” actually stands at, as we’ll see, defines its character.

Up to here, glass sounds like a cure-all. But reading glass as simply “the better material” is a mistake. Glass is not a material you can grade with a single score. The same property is an asset in one use and a liability in another.

The very trait of absorbing almost none of the signal’s energy turns into a weakness in power delivery. In a noisy café, the next table’s chatter gets swallowed; in an empty concert hall, one cough rings through the room. Low-loss glass is the empty hall, where faint noise in the power circuits rings on instead of dying out. Its ability to pull heat away is also about one-hundredth of silicon’s. That weakness has a twist, though: if the “substrate that carries light” becomes real, the transmission itself generates almost no heat (the lasers and driver circuits still do), so low thermal conductivity weighs less: a system-level trade-off to manage, not a built-in advantage. Weakness and strength trade places by application.

And above all, glass breaks. Micro-cracks from cutting, drilling, and handling can spread fatally as the chip heats and cools through tens of thousands of cycles. The industry suppresses this with edge finishing and strengthening, but while component-level test data exists, long-term data showing thousands of thermal cycles at the board and system level has not been made public in any depth.

To sum up: organic is cheap and mature but is starting to fail AI-scale physics tests; silicon is the top performer but claims the most expensive production resources; glass has seductive physics but no track record, and its merits invert by application. No material wins every row. The question is not “which is best” but “which layer changes first, when, and in what order.”

That’s the physics. Knowing the three characters, the real questions remain. As of July 2026, which of the three is actually used where? Where did the trillions of won staked on this transition actually go? And where exactly does everyone’s story, “the age of the glass substrate is coming,” misread the map?

The short answer: where the market is looking and where the money pools are two different places. That mismatch is the rest of this piece.
