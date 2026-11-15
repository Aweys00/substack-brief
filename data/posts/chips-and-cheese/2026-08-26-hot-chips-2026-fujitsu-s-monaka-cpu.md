---
title: "Hot Chips 2026: Fujitsu’s Monaka CPU"
source: "Chips and Cheese"
author: "Chester Lam"
url: "https://chipsandcheese.com/p/hot-chips-2026-fujitsus-monaka-cpu"
published: "2026-08-26T01:20:30+00:00"
words: 2173
preview_only: false
---

# Hot Chips 2026: Fujitsu’s Monaka CPU

Fujitsu’s A64FX was a pivotal core. For the Arm ecosystem, it introduced SVE. SVE continues to define Arm’s vector execution strategy to this day, with newer extensions like SME adopting a similar vector length agnostic approach. For Fujitsu, A64FX marked a shift away from SPARC and towards the 64-bit Arm ISA (aarch64). Adopting aarch64 let Fujitsu take advantage of a stronger, better supported software ecosystem. Because there’s a lot more Arm software out there than SPARC software, the shift also opened up market opportunities beyond Fujistu’s core competency.

However, A64FX was not well suited to general purpose workloads. It ran at a low 2 GHz clock speed, had a small out-of-order engine, and fed that using a comparatively basic branch predictor. That was great for regular HPC code that primarily wants to feed the core’s two 512-bit vector pipes, but would likely not compete well with AMD, Arm, or Intel’s top-of-the-line cores. The latest cores from those manufacturers have large out-of-order engines running far beyond 2 GHz, fed by sophisticated branch predictors. A variety of other design choices would put A64FX further behind.

Fujistu’s new Monaka core seeks to address many of these shortcomings, creating a processor better suited to general purpose workloads. At the same time, Fujitsu keeps focus on the HPC front with high chip-wide vector throughput.

On the branch prediction front, Monaka has a “three-level” TAGE predictor. TAGE uses multiple tables indexed using different history lengths, and is the state-of-the-art prediction algorithm. “Three-level” is more difficult to parse. Fujistu might have implemented a TAGE predictor with three overriding levels, where hitting in a table indexed with longer history can override a prediction made by a table indexed using shorter history in a previous stage. It’s reasonable to imagine a TAGE predictor with a base component that makes a quick prediction in a first stage, then a couple tables indexed using a dozen or so history bits in the second stage, and finally tables using several times as many history bits in the last stage.

A64FX by comparison had a 2048 entry Branch Weight Table, used to implement a perceptron-like algorithm. Perceptron predictors can scale to long history lengths with less growth in history storage (like the Branch Weight Table), but have fallen out of fashion. For perspective, AMD first used a perceptron predictor in Piledriver over 10 years ago, and stopped using perceptrons as the primary prediction method after Zen 1.

Other branch predictor details haven’t been disclosed at this time. A64FX could not do back-to-back taken branches in the general case, and had a rather small 8 entry return stack. Monaka hopefully improves in these areas too.

Monaka’s branch predictor drives a decoupled fetch pipeline, which has a 64 KB instruction cache. Instructions are fetched, decoded, and then allocated into the backend. Fujitsu didn’t disclose Monaka’s core width. However, the core’s backend resources include six ALUs. That implies the core is at least 6-wide, because otherwise there’d be no way to feed those ALUs in a sustained manner. A64FX was 4-wide, and had four ALUs.

Monaka’s backend uses a similar scheduler layout to A64FX, with familiar Fujitsu naming. RSE0 and RSE1 continue to feed both ALU and vector pipelines. Fujitsu’s diagram suggests predicate operations (PRX) are now executed down a separate port. Predicate operations include instructions like WHILE*, which update predicate registers that subsequent predicated SVE operations would depend on. Resolving predicates quickly avoids delaying predicated operations, and helps keep the vector pipelines fed.

The six ALU ports are another mystery. Fujitsu’s diagram shows four ALU pipes (EXA, EXB, EXC, EXD) being fed by RSE0 and RSE1. I suspect the last two ALU pipes are fed by RSA, just like in A64FX.

Monaka’s two vector/FP pipes are 256 bits wide, compared to A64FX’s two 512-bit vector pipes. Narrower vector pipelines might be surprising, but they make sense considering the vast majority of Arm software out there probably isn’t written with wide vector units in mind. Leveraging wider vector units can be difficult. [Geekbench 6 for example](https://chipsandcheese.com/p/evaluating-geekbench-6) only has a small subset of workloads that use AVX-512, and not all AVX-512 instructions use the full vector length. When targeting a wider set of general purpose workloads, I suspect Fujistu saw that many could not take advantage of more vector throughput. Then, moving to 256-bit vector units provides power and area savings, while simplifying core design because datapaths can be narrower.

Vector units are power hungry, so Monaka uses several techniques to reduce power draw. Fujitsu places a register cache in front of the floating point register file, which seems to act like the register reuse caches often found on GPUs. Recently read FP/vector registers can be held in the cache, and can service instructions that try to read the same values soon after. Unlike GPUs, which use register caching to avoid hiccups from register bank conflicts, Monaka likely uses the register cache purely to save power.

Even though each predicated SVE instruction has to read a predicate register to determine which lanes to enable, code often runs for a long time with all lanes enabled (predicate register contains all 1s). For example, a loop traversing an array would re-calculate the predicate register with each iteration, but will only have some lanes disabled when the last iteration hits the end of the array. Monaka records when the predicate register has common patterns like all 1s, and can avoid predicate register file reads when predicated instructions execute. It’s like having a value-based register cache that handles the most common predicate value.

Another power saving opportunity applies for code that doesn’t fully utilize Monaka’s 256-bit vector width. A lot of general purpose Arm code uses NEON, which has been widely supported on Arm cores going back a decade. NEON is limited to 128-bit vector width, and many cases can’t even fully utilize that. For those cases, Monaka’s renamer can remember that a vector register’s upper bits are zeroed. Later instructions that access the register can avoid uselessly reading or writing zeroes to/from the upper bits, reducing power.

On the performance front, Monaka carries forward the gather optimizations present on A64FX. Gather operations load each lane element from a different memory location, rather than loading the entire vector register from a contiguous address. If two lanes read from the same 64B aligned block, Monaka can return data for both lanes without needing a separate L1D load flow. Fujitsu calls this a “combined gather” capability. A64FX’s “combined gather” was actually more flexible, and worked on larger 128B blocks. Monaka is likely limited to doing combine gather on 64B blocks because that’s the largest block that’ll fit within a cache line. As a reminder, A64FX used 256 byte cache lines.

Another feature inherited from A64FX is full bandwidth for unaligned vector loads. Most CPUs execute unaligned loads using two accesses under the hood, meaning that cacheline crossing loads result in lower software-visible bandwidth. That’s not the case on A64FX or Monaka.

### System Level Design and Physical Aspects

Monaka’s chiplets use a hub-and-spoke setup with some parallels to AMD’s server chips. A 5nm IO die connects compute dies to IO and memory. The IO die is flanked by 2nm compute dies that each contain 36 Monaka cores. Compute dies are stacked on 5nm dies that contain Monaka’s last level cache. Fujitsu notes that SRAM scaling has slowed down, so putting SRAM on an older node helps remove cost.

The stacking arrangement parallels to AMD’s Zen 5 VCache setup. Both AMD and Fujitsu place the hotter compute die on top, putting it closer to cooling. Analog power delivery logic also doesn’t scale well with newer process nodes, so Fujitsu places LDOs on the 5nn SRAM die too.

Moving power delivery logic to the base die lets Fujitsu place LDOs where they’re most needed. For example, putting a LDO close to FMA logic can ensure clean power delivery to that power hungry block.

On the physical side, Fujitsu wanted to reduce voltage to save power. However, SRAM is often a limiter for how low voltage can go while keeping the chip functional. Therefore, Fujitsu created a custom SRAM macro that can operate at lower voltage.

From older slides at ICS 2024, the low voltage SRAM design uses an assist circuit. Details are scarce, but perhaps it boosts the VDD (voltage) during an access.

### NUMA Options

A64FX had 52 cores, organized into four clusters (CMGs) that each contain 12 compute cores and 1 assist core. Each cluster was attached to 8 GB of HBM, and was exposed to software as a NUMA node. That arrangement was great for well-optimized HPC software, but general purpose code that’s not NUMA aware would find it difficult to scale beyond a cluster.

Monaka aligns with most server chips today and offers a set of NUMA modes, enabling different tradeoffs uniform memory access and low latency. Monaka offers a set of NUMA modes to create tradeoffs between making memory access more uniform and optimizing for low latency. The most latency-optimized mode divides a 144 core Monaka chip into eight NUMA nodes. Each compute die gets split into two NUMA nodes, each with 18 cores and a private half of the L3 cache on the base die. Doing so exploits how some cores will be closer to certain parts of the L3 cache on the base die.

A more balanced mode splits Monaka into four NUMA nodes along compute die boundaries. Each compute die get associated with the closest memory controllers in the IO die, much like how NPS4 mode works on AMD’s EPYC. Finally, the whole Monaka chip can be exposed as a single NUMA node, letting applications scale across the entire chip without worrying about NUMA.

Monaka uses DDR5, which also aligns it with other server platforms. A64FX’s HBM setup gave it plenty of bandwidth at low power, but the chip only had 32 GB of memory in total. Worse, each NUMA node had a rather restrictive 8 GB. With DDR5, Monaka can be set up with much higher memory capacities. Because DDR5 modules are removable, Monaka can be set up with different memory configurations, and can accept memory upgrades down the road.

### Confidential Compute and Security

Moving beyond the HPC market may mean getting hardware deployed into locations with less than ideal physical security. Monaka handles that with a large suite of security features that align with what cloud providers might want to see. A hardware root of trust (i.e. TPM) helps software ensure it’s not running on compromised infrastructure code. Encrypting data in memory helps guard against cold boot attacks.

Further up the stack, Monaka may have to deal with untrusted code, as well as buffer overflow or spectre-style attacks. On that front, Monaka brings in newer Arm ISA features. Pointer authentication helps mitigate the return-oriented programming attack vector by letting code check a signed pointer before jumping to it. CLRBHB, alongside other features, help mitigate Spectre attacks.

### Reliability

Monaka gets “mainframe” level RAS features, likely inherited from Fujitsu’s long history of designing supercomputer chips where reliability is of paramount importance. Besides standard features like ECC at caches, Fujitsu mentions a hardware instruction retry feature that can recover from transient errors. Details are scarce, but the same hardware instruction retry feature is present on Fujitsu’s SPARC-era cores, and is described in older Hot Chips presentations.

If the core detects an error, it flushes its pipeline from the commit stage. Doing so keeps bad data from the affected instruction away from known-good architectural state. The core then reloads known-good architectural state, a bit like recovering a branch mispredict. Then, it retries the error-ing instruction with single step execution. Likely, that means the core only lets a single instruction move through the pipeline at a time. If re-execution proceeds without error, the core can go back to full-speed out-of-order execution with many instructions in flight.

## Final Words

Monaka is an ambitious move from Fujitsu. The new core is undoubtedly better suited to general purpose applications than A64FX. Monaka also remains competent at HPC applications at the chip level, thanks to higher core counts and clock speeds. Unfortunately, a lot of important Monaka details are still undisclosed. Fujitsu isn’t giving Monaka’s L3 capacity at this time. Key core structure sizes, like CSE or register file entries, are also unknown.

From what Fujitsu presented though, I suspect Monaka will offer reasonable performance per clock. Its biggest shortcoming will likely be its low clock speeds. 2.9 GHz is well off what AMD, Intel, and even Arm’s cores can achieve in servers, and will limit the core’s single thread performance. Fujitsu is likely most competitive when it comes to providing high vector throughput in a density-optimized design. At 1.47 mm2, Monaka is only slightly larger than Arm’s Neoverse N2, which is 1-1.3 mm2 depending on L2 capacity. At the same time, it has twice as much vector throughput as N2. I hope to see more details on Monaka going forward, and hope to see Fujitsu find success in their general purpose computing push.
