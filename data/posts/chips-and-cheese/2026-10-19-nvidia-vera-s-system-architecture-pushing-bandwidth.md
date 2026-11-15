---
title: "Nvidia Vera’s System Architecture: Pushing Bandwidth"
source: "Chips and Cheese"
author: "Chester Lam"
url: "https://chipsandcheese.com/p/nvidia-veras-system-architecture"
published: "2026-10-19T18:26:50+00:00"
words: 1762
preview_only: false
---

# Nvidia Vera’s System Architecture: Pushing Bandwidth

Nvidia’s Vera server chip aims for high per-core performance. Its Olympus cores have massive out-of-order structures and use high per-clock throughput to meet that goal within a high core count server chip. Core design however is only one part of the equation. Off-core memory access can heavily impact core performance, and higher core counts complicate interconnect design. The task of feeding Vera’s Olympus cores falls to Nvidia’s second generation Scalable Coherency Fabric, or SCF. SCF plays a similar role as Arm or Intel’s mesh interconnect, acting as a large chip-wide network that connects cores, cache, and off-chip IO. Like the first generation SCF used in Nvidia’s Grace chip, Vera’s SCF probably uses a mesh topology.

SCF is built from several node types. Coherency Switch Nodes (CSNs) host cores and cache, acting a bit like Intel’s mesh stops. Unlike Intel’s mesh stops, Nvidia has each CSN host a pair of cores. Doing so helps keep node count under control, and is a tactic also used by [Ampere’s Altra Max](https://www.researchgate.net/publication/382824827_Exploring_the_ARM_Coherent_Mesh_Network_Topology). Ampere uses Arm’s CMN-600, and has each fully coherent request node (RN-F) host an Arm DynamIQ Shared Unit (DSU) containing a pair of Neoverse N1 cores.

Memory Switch Nodes (MSNs) serve as a bridge from SCF to Vera’s LPDDR5X memory controllers. Vera has a 1024-bit LPDDR5X-9600 setup, so the MSNs can move up to 1.228 TB/s of bandwidth. Bridge Switch Nodes (BSNs) host PCIe controllers and the cross-socket link. Vera has 88 PCIe lanes, which together can provide 665.5 GB/s of bandwidth to peripherals. NVLink C2C serves as the cross-socket link, and provides 1.8 TB/s of theoretical bandwidth.

## Bandwidth, Tons of Bandwidth

Grace broke ground in the server scene by using LPDDR5X memory, but had [mediocre](https://chipsandcheese.com/p/grace-hopper-nvidias-halfway-apu) DRAM performance compared to its peers. On Grace, memory latency was high at over 200 ns. Grace’s memory bandwidth was fine in an absolute sense, but fell a bit short compared to contemporary DDR5-based server chips. Vera turns everything around. The massive 1024-bit LPDDR5X interface now gives Nvidia’s server chip more bandwidth than its peers. Latency has been fixed and is now comparable to that of DDR5-based setups. Vera also adopts SOCAMM2 modules, making its memory setup field serviceable and potentially upgradeable. Grace by contrast used soldered memory, so memory chip failures could be problematic.

Vera maintains excellent control over latency under increasing bandwidth load. A pointer chasing thread doesn’t observe more than 200 ns of latency, even with other threads pushing the chip’s memory bandwidth limits. Other server platforms show a more distinct “hockey stick” pattern, where latency rises sharply as bandwidth load approaches the memory controller’s limits.

Nvidia’s combination of high bandwidth and low latency under load should let it control noisy neighbor effects better than other servers. Another way of looking at it is that Vera can out-scale other chips in DRAM-bound workloads, even if Vera has fewer cores.

## L3 Cache

Even a massive LPDDR5X subsystem won’t come close to being able to handle every program memory access, so Vera tackles the memory wall with large caches like other high performance CPUs. Vera’s caching strategy resembles the ones used on other large mesh-based designs. A 164 MB L3 cache is shared across all cores, and maintains a non-inclusive relationship with core-private L2 caches. This arrangement gives Vera up to 340 MB of effective last level cache capacity if there’s no data duplication across the L2 caches. For addresses that are frequently accessed by different cores, the L3 can economize cache capacity by only keeping one copy of the data at a shared address. Vera’s L3 read bandwidth comes out to about 3.35 TB/s, or 33.1 GB/s per core. A single core can achieve 88.5 GB/s without contention from its peers, so 33.1 GB/s represents a significant drop. However, that’s still a reasonable amount of bandwidth in an absolute sense, and is likely to be adequate because the 2 MB L2 caches should reduce L3 bandwidth requirements.

Nvidia’s caching strategy contrasts with AMD’s, which emphasizes cache capacity across the chip while delivering very high L3 bandwidth. AMD’s Genoa-X for example can give a single core 90 GB/s of L3 bandwidth, and only drops that to 85 GB/s when loading all cores in the die. Dividing Genoa-X (and other AMD server chips) into octa-core clusters means that each L3 instance only has to deliver high bandwidth to eight cores. Genoa-X’s 1248 MB of L2+L3 capacity could also be advantageous for multithreaded applications that work primarily on thread-private data, or when running many different jobs in parallel. However, a workload that shares a lot of data between threads could end up using that cache capacity inefficiently because shared data may be duplicated across multiple L3 instances. Finally, a single thread can only allocate into its 96 MB L3 instance on Genoa-X, while Vera can theoretically let one thread use its entire 164 MB L3.

## Cross-Socket Link

NVLink C2C acts as a point-to-point link between sockets, and lets Vera scale to dual socket configurations. A dual socket Vera system has two NUMA nodes, each of which represents a socket and its directly attached memory. Cross-node memory accesses have 309.27 ns of load-to-use latency, which is 177.41 ns more than a local memory access. Achieving that 309.27 ns figure curiously requires generating a few dozen GB/s of bandwidth on the link. A pointer chasing test run in isolation measures over 370 ns of latency, suggesting that NVLink C2C only transitions to a higher performance state if there’s enough bandwidth demand and requests start backing up in front of it.

NVLink C2C delivers very high bandwidth for a cross-socket link. Reads achieve just over 587 GB/s, while a read-modify-write pattern that moves data in both directions can reach 780 GB/s. Vera not only has more cross-socket bandwidth than any other dual-socket configuration I’m aware of, but also has more cross-socket bandwidth than most servers have bandwidth to directly attached memory. However, NVLink C2C falls behind in latency terms. AMD’s Genoa-X for comparison has 222.7 ns load-to-use latency for cross-socket memory accesses. Vera also doesn’t maintain the same tight control over NVLink C2C latency that it does for local DRAM accesses. Latency spikes at high bandwidth demand, and funnily enough, reach 780 ns when using a read-modify-write pattern to achieve 780 GB/s of cross-socket bandwidth.

## Core to Core Latency

Interconnects have to present a coherent view of memory by making a core’s writes globally visible, even if written data may only be present in that core’s private cache. A “core to core” latency test bounces a value between two threads using atomic operations, and measures an average of 148.5 ns on core pairs in the same socket. Latencies range from 87.5 to 199.3 depending on the tested core pair, and on which agent owns the tested cache line. SMT siblings have less than 10 ns of latency, indicating that a core can maintain coherency across its SMT threads without involving the slower cross-core interconnect.

Latency between cores on different sockets is approximately 660 ns, which is unfortunately high. I remember Anandtech measured similar figures in a dual-socket Ampere Altra system, but latency above 600 ns isn’t typical.

AMD’s Genoa-X (EPYC 9V33X) achieves much better cross-socket core to core latency, at roughly 209 ns. Amazon’s Graviton 4 is even better, with cross-socket latency on par with older, lower core count designs.

Vera’s intra-socket latency is consistent, matching an advantage mentioned in Nvidia’s whitepaper. However, that latency is also consistently high, and worse than on Nvidia’s older Grace chip. It’s also worse on average than Amazon’s Graviton 4 and AMD’s Genoa-X.

## Compute Throughput: SPEC CPU2026

SPEC’s CPU rate suite can be used to measure throughput by running multiple copies of each workload. When running one copy per hardware thread, Vera has no trouble beating Graviton 5 node-for-node. Unsurprisingly, Vera also beats a lower core count Zen 5 part that was curiously configured to have [one NUMA node spanning both sockets](https://chipsandcheese.com/p/evaluating-uniform-memory-access).

However, Vera falls behind Graviton 5 at the socket level. It’s not a completely fair comparison because Graviton 5 can’t expose the entire socket as a single NUMA node, but it does show a tradeoff between core count and having more powerful cores. A density optimized design with less powerful cores can often provide higher throughput, assuming there’s work available to bring all those cores into play. SMT helps close the gap, but it’s still hard for Vera to take on a design with more than twice as many cores.

Vera still has an advantage even against Graviton 5 in a socket-for-socket comparison in workloads with high memory bandwidth demands. 749.fotonik3d tends to be very heavy on DRAM bandwidth even when running a single copy on the Ryzen 7 9800X3D.

Performance monitoring data wasn’t collected from the socket-wide Vera and Graviton 5 runs, but it’s safe to assume 749.fotonik3d is DRAM bandwidth bound for both of those chips. Running multiple copies will mean less cache capacity on average for each copy, and bandwidth demands from each copy will stack. Despite having a much lower core count than Graviton 5, Vera achieves nearly a 20% performance lead over Graviton 5 in 749.fotonik3d. That advantage extends to several other SPEC CPu2026 floating point tests. On the flip side, Graviton 5 has an overwhelming advantage in more cache friendly workloads.

## Final Words

Vera is a very strong contender in today’s server landscape, with exceptionally strong per-core performance backed by tremendous memory bandwidth. It’s a far more convincing offering than Nvidia’s older Grace chip, which suffered from having small 1 MB L2 caches and very high L2 miss latency. Compared to other server chips from Arm, and even AMD and Intel, Vera trades core count for per-core performance. In use cases where individual tasks need to be finished quickly and workloads may not fill all cores, Vera will be hard to beat.

For the Arm server landscape as a whole, Vera’s entrance brings a welcome increase in diversity. When Arm first gained a foothold in the server market, Arm chips competed purely on density. Cores like Neoverse N1 couldn’t match their AMD or Intel counterparts head-to-head, so chips like Ampere Altra competed by offering higher core counts. Arm server chips today still compete on that density focused front with chips like AmpereOne, but chips based on Arm’s Neoverse V series cores have expanded Arm’s boundaries. Vera pushes that boundary even further in the per-core and per-thread performance direction. More diversity and more competition in the server scene is always a good thing, and Vera’s strength is a sign of more to come.
