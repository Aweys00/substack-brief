---
title: "Hot Chips 2026: Intel’s Diamond Rapids"
source: "Chips and Cheese"
author: "George Cozma"
url: "https://chipsandcheese.com/p/hot-chips-2026-intels-diamond-rapids"
published: "2026-08-25T06:20:03+00:00"
words: 851
preview_only: false
---

# Hot Chips 2026: Intel’s Diamond Rapids

Hello you fine Internet folks,

Intel unveiled their upcoming Diamond Rapids Server CPU at Computex where they said that Diamond Rapids has twice the memory bandwidth, PCIe Gen 6, and 50% more cores than Granite Rapids.

However, it looks like in the 3 or so months since Computex, Intel has changed at least one key specification of Diamond Rapids.

### Rome Wasn’t Built in a Day

At last year’s Hot Chips, Intel talked about Clearwater Forest where they showed off their first 3D stacked server processor.

Clearwater Forest took the same 2 I/O dies plus 3 compute die layout that Granite Rapids had and moved the compute into dedicated dies with just the cores and L2 cache stacked on top of the base dies with the L3 cache on it. Diamond Rapids changes this layout in a significant way.

The layout of Diamond Rapids’ different dies look quite similar to AMD Venice’s layout with the Compute Dies on the edges of the IO dies. However, there are some large differences with the packaging.

Firstly, all Diamond Rapids CPUs have 3D stacked L3 cache, 320 MB per base tile, on the base tile with just the cores and L2 cache on the core chiplets.

This is different to AMD which has cores, L2 cache, and L3 cache on the CCD with an optional V-Cache die to expand the capacity of the L3 cache. With DMR, this is not an option, if you want a L3 cache you have to 3D stack the core chiplets onto the base die.

Secondly, unlike Venice or Xeon 6, Diamond Rapids doesn’t use 2.5D packaging. Intel chose to eschew 2.5D packaging with Diamond Rapids and connecting the 4 Base Dies and 2 I/O Tiles with UCIe-S (Standard) packaging.

The reason for this was so that Intel could connect the base tiles to both of the IO dies which 2.5D packaging would have precluded due to the short range of the wires.

Moving to the specifications of Diamond Rapids, at Computex Intel said that DMR had 50% more cores than Granite Rapids which would have been 192 cores. At Hot Chips it looks like Intel has revised this figure up from 192 to 256 cores which puts Diamond Rapids at core count parity to AMD’s Venice which launched last month.

As for the memory bandwidth, just like Intel promised it has double the memory bandwidth of Granite Rapids at 1.6 TB/s again putting it at parity to AMD’s Venice on the SP7 platform. However, Diamond Rapids does have an advantage over SP7 Venice in terms of PCIe lanes with 128 PCIe Gen 6 lanes compared to SP7’s 96 lanes.

Diamond Rapids is also bringing in two new key extensions to the x86 ISA.

The first of these extensions is AVX10.2 which is folding in all of the different AVX512 flavors found in Granite Rapids then adding in new instructions. AVX10.2 will also be supported on Intel’s upcoming client CPU series, Nova Lake, which will finally bring back the same capabilities that Intel had back in 2020 with Tiger Lake and Rocket Lake.

The other new extension is APX or Advanced Performance Extensions which is the first really large addition to the scalar side of x86 since AMD64 was introduced.

APX adds 16 more general purpose registers so now x86 will have 32 general purpose registers similar to Aarch64, RISC-V, and Power ISA. It is also adding three operand instructions, conditionals, expanded branch support, and other nice to haves in an ISA.

### Final Words

Diamond Rapids looks like Intel finally showing up to the server fight with a full plate, at least on paper. Between Computex and Hot Chips, the core count quietly climbed from 192 to 256, which puts Intel at core parity with AMD's Venice with Intel keeps the edge in I/O, with 128 PCIe Gen 6 lanes against SP7's 96 and the 1.6 TB/s of memory bandwidth doubles Granite Rapids and matches Venice on the SP7 platform. In a few months, DMR’s spec sheet went from “clearly behind” to “very well could be a serious competitor”.

The one open question that the Hot Chips slides showed but didn’t really answer is how well the UCIe-S packaging works.

With UCIe-S running at 16 Gigatransfers per second, each base die would need approximately 400 pins to the IO die to be able to read or write at the full 1.6 TB/s that the memory subsystem can provide. Equally, each I/O die would need approximately 1800 pins between the two dies to be able to read or write half of the total memory and PCIe bandwidth.

Regardless, Diamond Rapids really does looks like Intel throwing almost everything it has at the high-end server market: 3D stacking, disaggregated dies, more cores, more I/O, and some nice updates to the ISA. The remaining questions are the ones Intel did not answer at Hot Chips, including clock speeds, power, pricing, and how well the package performs once all 256 cores are loaded. Regardless, I can't wait for more details along with eventually getting silicon in-house to test hopefully sometime in 2027.
