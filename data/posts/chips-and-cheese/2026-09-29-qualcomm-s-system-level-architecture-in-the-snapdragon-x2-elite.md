---
title: "Qualcomm’s System Level Architecture in the Snapdragon X2 Elite"
source: "Chips and Cheese"
author: "Chester Lam"
url: "https://chipsandcheese.com/p/qualcomms-system-level-architecture"
published: "2026-09-29T16:07:30+00:00"
words: 2028
preview_only: false
---

# Qualcomm’s System Level Architecture in the Snapdragon X2 Elite

Laptop chips have gotten very powerful in recent years, with increasing CPU core counts, more powerful iGPUs, and higher DRAM bandwidth to feed that compute. All of that creates pressure on the chip’s system level architecture, which must deliver high bandwidth, service an increasing number of blocks, and keep latency under control. Qualcomm’s Snapdragon X2 Elite Extreme is a good example of how powerful recent laptop chips have become, with 18 CPU cores and an iGPU packing nearly as much compute as a Nvidia GeForce GTX 1070 Ti. It’s an aggressive entry into the laptop market, and needs a strong interconnect design to support everything packed into it.

Qualcomm simplifies the chip-level interconnect by splitting CPU cores into clusters, much like AMD. All cores within a cluster can be treated as a single client of the system level interconnect, reducing the number of clients that interconnect has to deal with. A shared cache within a cluster only has to concern itself with that cluster’s cores, simplifying cache design and making it easier to ensure fast cache access. Qualcomm uses 6-core clusters on the Snapdragon X2 Elite Extreme, compared to quad core clusters on the older Snapdragon X Elite. The first cluster contains E-Cores, or “Performance” cores in Qualcomm parlance, and has 12 MB of shared L2 cache. The two other clusters contain P-Cores, or “Prime” cores, and have 16 MB of shared L2 cache each.

## Intra-Cluster Characteristics

Qualcomm employs a caching strategy with parallels to the one used in Apple’s M1. Each cluster’s L2 is designed to provide very low latency and high bandwidth, while each CPU core comes with relatively large L1 caches. This combination lets Qualcomm dispense with the mid-level caches often found on AMD, Arm, and Intel designs. To deliver the required performance, Qualcomm runs the L2 caches at core clocks and tightly couples them to the cores. L2 latency comes out to 20-21 cycles on both the P-Core and E-Core clusters.

Curiously, a couple cores within each P-Core cluster have slightly higher latency at 22-23 cycles, while all E-Cores have the same L2 latency. I suspect Qualcomm uses a centralized crossbar design for their L2. The high 5 GHz might mean two P-Cores need a couple extra pipeline stages to get to L2 while meeting cycle time requirements. Perhaps the E-Cores didn’t need to make that concession because of their lower 3.6 GHz clock speed.

L2 bandwidth is 32B/cycle in both the read and write direction, so each core can achieve 64B/cycle of off-core bandwidth with a read-modify-write pattern. This is true even in the E-Core cluster, even though the load/store unit on Qualcomm’s E-Cores can only handle two 16 byte accesses per cycle. With a test where an E-Core only accesses half of each 64B cacheline’s data, it’s possible to infer that the interface to L2 can sustain 64B/cycle of fills and writebacks.

Bandwidth scales well with increasing active core counts. Each P-Core is able to get more than 100 GB/s of read bandwidth on average when hitting all cores in a cluster with a bandwidth test. AMD does come out ahead with a read-modify-write pattern, but Qualcomm should have more than enough shared cache bandwidth on hand for the vast majority of use cases.

## CPU DRAM Access

Going outside the cluster reveals an impressive level of external bandwidth. Each cluster appears to have a 32B/cycle path to the system, but cycle here is a cycle at the cluster’s clock. AMD’s Strix Halo for comparison has 32B/cycle read and write paths to the system, but that’s running at the chip’s 2 GHz Infinity Fabric clock (FCLK). The result is that Qualcomm’s CPU core clusters enjoy higher DRAM read bandwidth than Strix Halo clusters.

AMD again does well with a read-modify-write pattern that exercises both of the cluster’s external 32B/cycle paths. However, most applications will make far more reads than writes, so Qualcomm’s ability to get higher bandwidth with reads alone is a notable advantage.

DRAM latency on the Snapdragon X2 Elite Extreme is rather good for a LPDDR5X setup at 115 ns. It can’t compare with the sub-100 ns latencies typical on desktop DDR5 setups, but it’s up there with the best LPDDR5(X) implementations. As CPU bandwidth demands increase, Qualcomm’s system fabric maintains excellent control over latency and doesn’t let bandwidth-hungry threads excessively penalize a latency sensitive one. CPU read bandwidth in absolute terms is impressive too, surpassing even chips with 256-bit memory buses. AMD’s Strix Halo and Nvidia’s GB10 have 256 GB/s and 273 GB/s of theoretical DRAM bandwidth, respectively. The Snapdragon X2 Elite Extreme has 228 GB/s of DRAM bandwidth with a 192-bit bus. However, AMD and Nvidia’s CPU clusters don’t have enough external bandwidth to fully utilize their beefier DRAM setups.

Switching to a read-modify-write pattern lets Strix Halo’s CPU cores utilize more DRAM bandwidth, but hurts Qualcomm. Mixing reads and writes can challenge the memory controller, because the DDR memory bus can only be in read or write mode at any given time. Switching the bus between read and write mode (a turnaround) wastes bus cycles and therefore reduces achievable bandwidth. Perhaps Qualcomm suffers more from that, but getting to 68.5% of theoretical DRAM bandwidth is still a good result.

Cluster designs can experience contention at cluster boundaries, but that’s very well controlled on Qualcomm’s design. Latency stays under 200 ns from a CPU core regardless of how much DRAM bandwidth its peers are pulling through the off-cluster interface. It’s a better showing than [some of AMD’s designs](https://chipsandcheese.com/p/pushing-amds-infinity-fabric-to-its), which could let bandwidth-hungry threads squeeze out a latency sensitive one.

Adding in bandwidth demands from other clusters pushes latency up, but it never reaches unacceptable levels.

Qualcomm’s performance in this testing also compares well to [Nvidia’s GB10](https://chipsandcheese.com/p/inside-nvidia-gb10s-memory-subsystem), which could let latency creep over 200 ns when X925 cores contend with each other for off-cluster bandwidth.

## Core to Core Latency

Interconnects have to maintain cache coherency by ensuring that a write from one core can be made visible to another. A “core-to-core” latency test evaluates how long it takes for one core to observe another’s write using compare and exchange operations. Qualcomm probably handles transfers within a cluster through the L2 cache, which maintains an inclusive relationship with core-private caches within the cluster. Because the L2 includes L1 contents, it can easily tell when it might need to probe another core. Intra-cluster transfers enjoy very low latency, which is up there with the best of what Intel or AMD’s designs can achieve.

Cross-cluster accesses go through Qualcomm’s system level fabric and incur higher latency. However, that latency still remains well controlled and is similar to cross–cluster latency on AMD’s client designs. Latency to the E-Core cluster is somewhat higher than between the two P-Core clusters.

In all cases, Qualcomm’s newest design is a huge improvement over the older Snapdragon X Elite. Core clustering still means there’s a cross-cluster latency penalty, but it’s now much better controlled than on Qualcomm’s previous design.

Intel, and more recently Nvidia, have criticized cross-cluster penalties in their marketing publications. However, everything is a tradeoff, and focusing on uneven latencies misses the benefits of clustering. Clusters let Qualcomm deliver excellent shared cache latency and low core-to-core latency within a cluster, and that’s true of AMD’s designs too. I doubt Qualcomm could deliver L2 latencies in the low 20 cycle range if L2 accesses have to traverse an interconnect servicing 18 cores. Similarly, sub-20 ns core-to-core latencies would be hard to achieve with larger, logically monolithic interconnects.

I think Qualcomm’s clustering approach strikes a good balance. Worst case latencies aren’t much higher than average latency on a high core count, mesh-based server chip. Trying to build a big monolithic interconnect risks getting consistent core-to-core latency at the cost of making that core-to-core latency consistently bad. A monolithic interconnect would also impact cache performance for typical accesses that don’t need cross-cache transfers.

## Mixing in GPU Bandwidth Demands

GPUs can be huge bandwidth consumers on modern laptop chips. When mixing CPU and GPU bandwidth demands, the Snapdragon X2 Elite Extreme can let a CPU thread’s DRAM latency reach nearly 350 ns. It’s not too bad though. Worst case latency is on the same level as Meteor Lake, and achieved bandwidth is much higher than what a 128-bit LPDDR5(X) setup can hope to deliver.

CPU+GPU bandwidth doesn’t approach theoretical DRAM bandwidth as closely as it does on other chips. I achieved the highest bandwidth in this test run with the GPU using 74.86 GB/s and the CPU pulling 94.78 GB/s, for a total of 169.335 GB/s. That’s 74.2% of theoretical, and just short of the 176.98 GB/s (77.6% of theoretical) achievable with a CPU-only bandwidth test. For comparison, AMD's Strix Halo and Nvidia's GB10 can achieve 226.08 GB/s and 243.05 GB/s, or 88% and 81% of theoretical respectively.

Unlike Nvidia’s GB10 and AMD’s Strix Halo, the Snapdragon X2 Elite Extreme doesn’t let the GPU squeeze out the CPU. If I let the CPU and GPU grab as much bandwidth as they can get their hands on (very little compute relative to memory accesses), Qualcomm gives the CPU and GPU each about half of available bandwidth. Decreasing GPU bandwidth demands lets the CPU pick up whatever’s left. GB10 and Strix Halo can both give the CPU more bandwidth if the GPU isn’t asking for too much. However, they leave DRAM bandwidth on the table because their interconnects can’t deliver the same level of bandwidth to the CPU side.

Qualcomm’s bandwidth patterns under this test are closest to Meteor Lake’s, though the Core Ultra 7 155H has much lower bandwidth in general. It’s an older chip, and its 128-bit LPDDR5X-7467 configuration can’t hope to compete with a faster 192-bit one.

## Final Words

High CPU core counts and large iGPUs can challenge interconnect design, but Qualcomm’s interconnect is more than up to the task. The Snapdragon X2 Elite ensures its CPU cores can enjoy low latency and high bandwidth access to shared caches thanks to its clustered setup. Then, Qualcomm’s system level fabric offers a compelling combination of high bandwidth and well-controlled latency. It compares well against other mainstream laptop chips, though admittedly I only have Intel’s slightly dated Meteor Lake to compare against. More impressively, it beats out AMD’s Strix Halo and Nvidia’s GB10 in terms of CPU-side bandwidth. AMD’s Strix Halo and Nvidia’s GB10 both have larger 256-bit DRAM buses, but they can feel like large GPUs that happen to have a pile of CPU cores integrated. Qualcomm’s Snapdragon X2 Elite doesn’t give off the same vibes, and treats its CPU cores as first class citizens.

Qualcomm’s excellent interconnect performance and high bandwidth DRAM setup speak to the company’s ambitions. I remember when years ago, Gerard Williams III (who no longer works at Qualcomm today) mentioned at Hot Chips that architectural features can be built with a vision to enable advances in future designs, even if those features don’t deliver a huge benefit for a current product. Back then, he was talking about CPU core design, but the same principle can apply at the chip level too. The Snapdragon X2 Elite’s 192-bit LPDDR5X setup and system level fabric borders on being over-engineered considering its CPU and GPU setup. CPU cores typically hit cache for the vast majority of memory accesses provided the cache design is competent, so I expect typical CPU-side bandwidth demands to be well within what a 128-bit DRAM bus can deliver. GPU workloads often demand high sustained bandwidth, but Adreno X2 isn’t sized to deliver the level of performance that Strix Halo or GB10’s iGPUs can, and can’t consume the same level of bandwidth.

The Snapdragon X2 Elite Extreme’s system level design is something of a warning to Intel and AMD. For now, AMD’s Strix Halo and Intel’s Panther Lake stand out as halo-segment mobile chips. But no one designs an interconnect and memory subsystem as strong as the one in the Snapdragon X2 Elite if they haven’t at least thought about building a monster to take on AMD and Intel’s halo-segment products. With that in mind, I’m excited to see what Qualcomm comes up with next, on both the CPU and GPU side.
