---
title: "Optical, Round Two: The Mispriced, the Conditional, and the Worth Paying Up For"
source: "Damnang Research"
author: "Damnang"
url: "https://www.damnang.com/p/optical-round-two-the-mispriced-the"
published: "2026-09-04T08:10:58+00:00"
words: 2031
preview_only: true
---

# Optical, Round Two: The Mispriced, the Conditional, and the Worth Paying Up For

Redrawing the optical investment map with technology direction, valuation, and market expectation all converted into factors.

The last Optical Investing Round Two piece covered why this is a good moment to look at optics again, and roughly how the names sort out.

This one redraws the map as of September 2026, converting the direction of optical technology, the valuation of each stock, and the expectations already priced in into factors.

Optics is still out of the spotlight, so I go through it in detail:

the stocks that can produce good returns from here,

the ones worth picking up if they fall a bit further,

and the ones worth owning now even at a slightly higher price.

Disclaimer

This article is for information only and does not recommend buying or selling any security. Prices and multiples are as of the September 3, 2026 close and go stale with time. Earnings estimates are market consensus and may differ from actual results. The author may hold positions in the securities discussed, and those positions can change without notice. All investment decisions and their outcomes are the reader’s own responsibility.

NFA / DYOR.

### 1. The Correction Came From the Multiple, Not the Numbers

#### Why optical stocks are falling now

As of September 3, the 13 names in the optical map are down 42% on average from their 52-week highs, while the S&P 500 sits 0.8% below its high and NVIDIA 3.4%, so this was not a market-wide sell-off.

Yet all 11 names that reported in the August earnings season grew revenue more than 20% year over year, and Corning was the only one whose next-quarter guidance came in below consensus.

When results hold or improve and only the price falls, the problem is not the companies but what the market will pay for them.

The first force cutting that price is rates.

In optics the profits from CPO, NPO, ELS, and OCS land in 2027 and 2028 rather than 2026, and the further out the profit, the more its present value shrinks when long rates rise. On the same move in rates, optical multiples get cut before the rest of AI hardware.

The second is the money being spent today to earn those distant profits.

AAOI, AXT, and Sivers funded expansion and operations with equity, and even Coherent, which did no offering, spent $1.1B on FY26 capex against $79.5M of operating cash flow, for roughly negative $1.02B of free cash flow. Once several companies were growing revenue at double digits while cash only went out, the market began applying capital-intensive-cycle multiples across optics.

If rates cut the multiple, cash burn pushes out the date it comes back.

Three pieces of news then made a multiple reset look like broken fundamentals.

NVIDIA’s CPO switch uses fewer lasers, Fabrinet lost datacom volume at its largest customer, and Credo’s GAAP gross margin came down. Those happened in three different layers, light sources, assembly, and connectivity ICs, but the market read them as one signal that optical dollars and margins were shrinking together. Taken apart, they show optical dollars moving between layers rather than disappearing.

What I Track: 30-year yield · AAOI remaining ATM capacity · FCF conversion at the major optical names · share reaction after guidance raises

### 2. The Dollars Did Not Shrink. They Moved.

#### Why optics still deserves attention

Where those dollars go starts with money changing seats inside the AI system. As I laid out in HBM Density Peak in August, the lower HBM stack count in the Rubin Ultra generation does not mean HBM demand is rolling over; it means we have crossed into a stretch where how fast the data moves matters more than how much memory sits next to the GPU. Cutting capacity per GPU is absorbed by a scale-up domain that ties 576 of them together, and the money that gets freed goes to the NPO and switching that bind the racks.

The same budget now buys less HBM and more of what connects the racks, so what matters in optics is not how many transceivers get sold but how much of the money that used to go to memory ends up in interconnect and optics.

Which companies that money reaches shows up in the supply chain NVIDIA disclosed. In the June production disclosure for Spectrum-X Ethernet Photonics, TSMC handles silicon photonics fabrication, SPIL packaging, assembly, and test, TFC the laser modules, and Foxconn system assembly. A later NVIDIA production update named Lumentum as a core partner.

NVIDIA’s developer blog describes a broader silicon photonics ecosystem in which Lumentum, Sumitomo, and Coherent supply ELS lasers and subassemblies, Corning and Coherent supply fiber and connectors, and Foxconn and Fabrinet handle system assembly. Coherent is ramping ultra-high-power CW lasers for CPO under its NVIDIA partnership in Texas and expects revenue recognition to begin in the December quarter. Within one program, in other words, the kind of dollars a company collects depends on which layer it stands in.

The timing differs by layer too.

1.6T pluggables are already ramping, OCS and scale-out CPO start showing revenue in 2H26, and DCI shows up in Ciena’s backlog and Fabrinet’s telecom revenue, while NPO and scale-up CPO matter more from 2H27 on.

Because the layers that hit today’s results and the layers that hit 2027 are separate, buying optics means choosing which year’s profits you are paying for.

Put those together and optical dollars are not shrinking; they are moving from front-panel module assembly toward light sources, materials, OCS, DCI, and scale-up interconnect.

So the names have to be picked by which side of that move they stand on, not by how far they have fallen.

What I Track: OCS revenue recognition · Coherent’s first CPO revenue · first ELS shipment · Rubin/NVL576 shipping schedule

#### Technology direction as of September 2026: seven shifts and their weight

Sorting names by which side they stand on means first setting out what changes. I use only what has been confirmed in public materials since the April map and the March CPO specials.

Each shift is described in the same order: what changes, why now, when, and who wins and loses. Each shift gets a weight from 1 to 3. The criteria are the dollars that move by 2028 and how far the shift has been confirmed by orders or production. I start with shift zero, the 1.6T pluggable ramp (S0, weight 3), which is the largest dollar pool today.

200G EML and SiPh pluggables produce most of the revenue in 2026 and 2027, yet in the first shift below they stand on the losing side. That is the starting point of this piece, and the stock judgments start from this direction.

1. The electrical-to-optical boundary moves from the switch front panel into the package (S1, weight 3).

Today the signal leaves the switch chip as electricity and turns into light in a pluggable module at the front panel. At 200G per lane, the distance copper can carry a clean signal becomes shorter than the board, and the power spent restoring the electrical signal becomes a large share of total switch power. So the conversion point moves next to the chip (NPO) or into the same package (CPO).

NVIDIA formalized full production of its scale-out CPO switch in June, with a partner update in August, and for the scale-up links between GPUs, Lumentum and Coherent talk about 2H27 shipments and 2028 deployment. Winners are light sources, InP, fiber attach, and test. Losers are front-panel module assembly and, after 2028, in-rack copper. The checkpoints are the first shipment of scale-up light sources and the date the 448G electrical standard is fixed.

2. The light source leaves the module (S2, weight 3).

CPO cuts the number of lasers per switch to a quarter, but the remaining laser has to feed light to many channels, so its output rises to hundreds of milliwatts and reliability requirements rise with it. The laser stops being a part inside a module and becomes a separate, replaceable product called an external light source (ELS). Count falls; price per unit and InP consumption rise. Winners are high-power CW lasers and InP substrates, and the ELS suppliers NVIDIA names in its documents are Lumentum, Sumitomo, and Coherent. Coherent has 6-inch InP today; Lumentum’s arrives in 2028. Losers are businesses that sell many low-power lasers. Checkpoints are the first ELS delivery (2H27) and AXT’s quarterly capacity.

3. Optical circuit switches remove one electrical switching tier (S3, weight 2).

A network converts light to electricity at every tier, switches it, and converts it back. OCS steers the light path directly with mirrors (Lumentum, MEMS) or liquid crystal (Coherent), removing that conversion. The market opened when Google moved from in-house development to external sourcing; Lumentum guides to its first $100M-plus quarter in fiscal Q1 and Coherent talks about a market above $4B. The winners are those two companies; the losers are the electrical switch at that tier and the transceivers on either side of it.

4. Not dropping the link matters as much as speed (S4, weight 2).

In a training job that ties together tens of thousands of GPUs, one dropped link stalls the whole job. The market splits two ways. LPO removes the DSP from the module to cut power by 30% to 50% and leans instead on the precision of analog ICs such as TIAs and drivers (Semtech, MACOM). DSP companies sell features that keep links from dropping (Credo’s ZeroFlap). CPO moves toward removing the DSP entirely, so merchant DSP content per port shrinks, and Marvell answers with scale-up optics and Photonic Fabric. Winners are analog ICs and reliability products; losers are merchant DSP content per port.

5. Scale-up spreads across racks and scale-across links data centers (S5, weight 3).

This is the layer where the budget shift from memory density to connectivity shows up as physical wiring. Copper cannot leave the rack, so fiber takes the rack-to-rack links and coherent optics take the links between data centers. Corning’s form-factor-agnostic claim is not a slogan but a fiber-count calculation, and Ciena’s $8.5B backlog and Hyper-Rail are the first orders in this flow. Losers are copper interconnects built around a single rack.

6. Yield and test become the real bottleneck (S6, weight 1).

Once optics are inside the package, one defective optical die scraps the whole GPU package. Burn-in at the wafer stage (known good die) enters the process before packaging, and there is no standard yet. Aehr followed repeat orders from its lead SiPh customer with a second major SiPh customer in 2026, and a follow-on production order from that customer as well. The dollar pool is still small, but the production proof already exists. Losers are assembly margins in the parts of the flow where standards are absent.

Running through all seven shifts is one move:

the point where signals turn into light travels toward the chip, and in that move light sources, fiber, and test survive while front-panel assembly and merchant DSP content per port come under pressure.

S6 gets a weight of 1 not because it is a lesser bottleneck but because the dollars moving inside optics are small. Section 3 multiplies these weights by each company’s exposure to build the direction exposure score.

That was the technical direction for optical as a whole.

Knowing the direction, though, is not the same as knowing the investment. Even when the optical direction is right, it means little if that business is a small share of a company’s total results, and even a real bottleneck leaves limited upside once valuation already reflects the expectation. The average drawdown in this correction reached 42%, and that is why only three names still read as cheap to me.

From here I run the core optical names one at a time through my own optical investment model: what has actually been confirmed on the technology side, and how much the market has already paid for it. Six factors score each name, and they sort into three buckets: Mispriced, Conditional, and Worth paying up.

Read through to the end and you should come away with a clear investment view on how to prepare for the second round in optical.
