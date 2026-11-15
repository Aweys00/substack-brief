---
title: "Qualcomm’s Adreno X2 GPU"
source: "Chips and Cheese"
author: "Chester Lam"
url: "https://chipsandcheese.com/p/qualcomms-adreno-x2-gpu"
published: "2026-09-19T18:03:20+00:00"
words: 3952
preview_only: false
---

# Qualcomm’s Adreno X2 GPU

Integrated GPUs have become a crucial component in recent laptop chips, thanks to a push for better graphics performance in ultraportable devices. AMD and Intel have both launched impressive iGPU implementations in recent years. Qualcomm’s laptop push needs a powerful iGPU in this landscape, and that’s where the Snapdragon X2 Elite’s Adreno X2-90 enters the picture.

Adreno X2 expands on the foundation set by the Snapdragon X Elite’s Adreno X1, but brings an enhanced architecture that aims for higher throughput. Shader Processors (SPs) act as the basic building block for Qualcomm’s Adreno GPUs. Each SP contains a pair of Micro Shader Processor Texture Processor (uSPTPs), which have execution units, register files, and private texture caches. At a higher level, Qualcomm groups pairs of SPs into slices. A fully enabled X2-90 part has eight SPs grouped into four slices, compared to six SPs in three slices on Adreno X1. Qualcomm also scaled up clock speeds from 1.5 to 1.85 GHz. A larger, higher clocked GPU will put more pressure on the memory subsystem, so Qualcomm scaled up cache sizes and increased bandwidth throughout the memory hierarchy.

With all these changes, Adreno X2 has nearly twice the theoretical compute throughput of its predecessor. It’s dwarfed by AMD’s highest end iGPU offering, which brings in more of everything. AMD’s more standard “Strix Point” chip may be a better comparison, but I don’t have that on hand, so I’ll be doing performance comparisons across a smattering of interesting devices. A special thanks goes out to ASUS for supplying the Zenbook A16 for testing.

## Shader Processor and uSPTP

Qualcomm’s Adreno line traditionally emphasizes high throughput for basic FP32 and FP16 operations. Adreno X2’s uSPTPs continue that emphasis, with 128 FP32 lanes that appear to be arranged in two execution unit partitions. FP16 benefits from double rate execution like on many modern GPUs.

Other instruction categories don’t necessarily enjoy the same high throughput, but Adreno X2 improves over its predecessor in several areas. INT32 adds appear to execute at full rate, though it’s hard to approach theoretical throughput on them compared to FP32 operations. 32-bit integer multiplies execute at half rate, which compares well to Intel and AMD’s GPU architectures, and aligns with Nvidia. Integer performance overall is a huge improvement over the rather poor situation on Adreno X1, where even basic integer operations executed at less than half rate. Better INT32 units help 64-bit integer performance too, since GPUs carry those out using multiple INT32 operations. Like previous Adreno GPUs, Adreno X2 lacks FP64 support.

Testing with Nemes’s Vulkan-based suite shows substantial compute improvements compared to Adreno X1. Adreno X2 also compares well to older iGPUs. AMD’s Radeon 780M can achieve higher FP32 throughput if AMD can use VOPD dual-operation instructions or wave64 mode, but Adreno X2 isn’t far off even in that case. However, Adreno X2 seems to need a lot of work in flight to approach theoretical compute throughput, even compared to larger GPUs like AMD’s Strix Halo.

OpenCL experimentation with varying dispatch sizes shows that Adreno X2 can reach beyond TFLOPS with FP32 adds, or 6 TFLOPS with multiply-adds. Adreno X2 just needs roughly 8x more parallelism to reach its maximum throughput. Further testing with OpenCL with large dispatches shows Adreno X2 getting close to theoretical throughput in floating point operations. However, INT32 throughput barely improves over Vulkan.

Adreno X2 continues to lack hardware fused multiply-add (FMA) capability like its predecessor. FMA avoids intermediate rounding between the multiply and add, reducing numerical error. Asking for that using OpenCL’s fma() built-in function results in very poor throughput. AMD, Intel, and Nvidia’s GPUs all have native FMA hardware and can provide FMA behavior without throughput loss.

### Feeding the Execution Units

Each Adreno X2 uSPTP has 128 KB of register file capacity, down from 192 KB on Adreno X1. Register file design tends to be difficult because they have to provide immense bandwidth to feed a GPU’s wide vector units. Smaller register files might have let Qualcomm increase clock speeds while keeping power and area under control. Adreno X2 also ditches Adreno X1’s wave128 mode, and only supports wave64. Smaller wave sizes can let register file capacity go further because each thread can allocate more registers before impacting theoretical occupancy.

With the register file capacity change, Adreno X2’s occupancy should behave like Adreno 730’s.

Qualcomm didn’t disclose Adreno X2’s theoretical occupancy, but I tried to guess by running a DRAM latency test with different dispatch sizes, and the same access pattern used across all workitems. If the GPU can keep all workitems in flight, latency shouldn’t be much higher than with a single workitem. However, running out of wave slots would force some workitems to wait until another finishes and its wave slot frees up, increasing observed runtime.

I suspect each Adreno X2 uSPTP partition has somewhere between 6 to 8 wave slots, with 8 being a more likely figure. Latency starts increasing with a 12288 workitem dispatch (6x wave64 per uSPTP partition), and more than doubles when going from 16384 to 18432 workitems.

Qualcomm also did not disclose instruction cache capacity, but basic testing with increasingly large loops shows that throughput from a single thread stays high with up to 8192 FP32 add statements in the loop. Absolute throughput figures suggest Adreno X2 can’t dual-issue FP32 adds from a single thread, possibly because each wave64 thread is locked to a single uSPTP partition. Throughput remains reasonable at larger instruction footprints.

## Cache and Memory Access

Adreno X2 gets a beefed up memory hierarchy compared to its predecessor, but continues to inherit Adreno-style memory subsystem features that make it unusual next to other modern GPUs. uSPTPs continue to have texture caches that don’t serve compute global memory accesses. These texture caches are now 4 KB in size, but that’s still very small. The smallest texture cache I’ve seen outside of Qualcomm’s Adreno GPUs is the 8 KB one on AMD’s Terascale.

Global memory accesses go straight to Adreno X2’s 128 KB cluster caches. Cluster cache accesses have slightly higher latency than texture cache hits, but remains reasonable in an absolute sense. However, that means Qualcomm has higher minimum latency for global memory accesses than AMD. The gap is especially wide if AMD can carry out scalar optimizations. Qualcomm does not have a separate scalar cache hierarchy. Even if I use the constant memory type, that appears to be backed by the same cluster cache. The cluster cache does fine in bandwidth terms, and can deliver 64B/cycle to each uSPTP.

A 2 MB L2 cache sits after the cluster caches, and matches AMD’s 2 MB L2 on Strix Halo and Strix Point. L2 latency is reasonably good, and better than AMD’s. L2 capacity is small next to what Intel has been doing, but Qualcomm does have a system level cache to catch L2 misses, making them less reliant on L2 capacity. AMD’s Strix Halo uses a similar strategy.

L2 bandwidth appears to be a bit above 1 TB/s, or just over 32B/cycle per uSPTP. Like upper level caches on many GPUs, Adreno X2’s cluster cache is either write-through or read-only. Writes go to L2, which services them at about half the read rate.

Atomic operations are often handled at L2 because it’s the first cache level shared across the GPU. Adreno X2 provides decent throughput for INT32 atomic adds. Counting each add as two 4B accesses (read-modify-write) gives 632.64 GB/s of effective bandwidth.

Testing cross-thread latency using atomic_cmpxchg on global memory shows excellent performance from Adreno X2, and a big improvement over Adreno X1. “Core to core” latency on Adreno X2 is on par with AMD’s latest GPU architectures, and better than on Intel Meteor Lake’s iGPU.

The Snapdragon X2 Elite’s 8 MB system level cache (SLC) has rather high latency at just over 200 ns, or roughly 150 ns above L2 hit latency. SLC bandwidth appears to be around 380 GB/s, which is comfortably higher than DRAM bandwidth. AMD’s high end Radeon 8060S has both higher bandwidth and lower latency to its 32 MB SLC.

For DRAM, Qualcomm has a rather aggressive setup with a 192-bit LPDDR5X-9523 configuration. I could get just over 150 GB/s of DRAM bandwidth from the GPU. That’s better than what a typical 128-bit LPDDR5X setup can achieve, but sits under 70% of theoretical. A potential positive there is that GPU bandwidth demands can’t pressure CPU-side accesses to the same degree as other iGPU implementations, where the iGPU can gobble up a larger fraction of theoretical DRAM bandwidth.

Adreno X2’s DRAM latency situation is a bit strange. Latency plateaus at around 274 ns with moderate test sizes, but heads for the hills when test coverage exceeds 64 MB. Testing with a 128B stride doubles apparent cluster cache capacity, suggesting Adreno X2’s cluster cache has 64B lines. Apparent L2 capacity remains unchanged until stride length exceeds 4 KB, after which larger strides push out both the L2 and 64 MB inflection points. My interpretation is that Adreno X2 has a virtually addressed L2, and uses 4 KB pages for address translation with a 16K entry TLB placed after the L2. High latencies at large test sizes imply very high L2 TLB miss penalties. Raw DRAM access latency, excluding address translation penalties, is likely around that reasonable 274 ns figure. However, applications making accesses with poor locality over a large memory footprint may experience much higher latency.

### Adreno High Performance Memory (HPM)

Qualcomm has a long history of embracing tiled rendering, and Adreno X2 doubles down on that with a massive 21 MB block of on-chip storage called “Adreno High Performance Memory”. This HPM fills the same function as GMEM (Graphics Memory) in prior Adreno GPUs, and holds render targets to contain intermediate tile state while a tile is being rasterized. For scale, Adreno X1 had 3 MB of GMEM, while the Snapdragon 8+ Gen 1’s Adreno 730 had 2 MB of GMEM. Qualcomm says they sized HPM to handle QHD+ frames, and the math checks out. A 1440P frame with 32 bits per pixel (RGBA, 8 bits per channel) would occupy 14.7 MB. ASUS equipped the Zenbook A16 with a 2880x1800 OLED screen. Doing the same math would give 20.7 MB per frame, which should barely fit within HPM.

Rather than doing tiled rendering in the traditional sense with perhaps a dozen or so tiles per frame, Qualcomm seems to be throwing a curveball by trying to make the whole screen one tile. Tiled rendering comes with potential inefficiencies. For example, a triangle that overlaps two tiles will have to go through the rasterizer twice, creating extra rasterizer work. As one tile finishes, wave slots might start freeing up across the shader array. The GPU might have extra pixel work available, but has to hold it back because the whole point of tiled rendering is to serialize the rasterization process at the tile level. Those potential inefficiencies suddenly go away if the entire screen is one tile. At the same time, Qualcomm would still get the advantage of being able to contain intermediate tile state in on-chip memory. A large cache could do this naturally of course, but a cache requires extra power and area for tag and state arrays.

HPM is an excellent move if applications stick to the conventional rasterization API, but I’m worried that HPM’s applicability might be limited for general purpose compute. While rasterization remains the bedrock of PC gaming and likely will for the foreseeable future, the modern rasterization process sometimes includes a compute component. Newer rendering engines often have features that leverage compute, like Unreal Engine 5’s Nanite. HPM isn’t useless in these scenarios, because Qualcomm can allocate some HPM for use as a software managed scratchpad. Then, HPM can take on the same role as AMD’s Local Data Share or Nvidia’s Shared Memory.

I tried to see how many workgroups the GPU could run simultaneously with different amounts of OpenCL local memory allocated. From those experiments, Adreno X2 only appears capable of allocating 1 MB of HPM as local memory. Local memory allocations that aren’t a power of two bring that down further. 1 MB of local memory isn’t bad for a GPU of Adreno X2’s size. Adreno X1 could only allocate 384 KB of local memory across the GPU. AMD’s Radeon 8060S has 2.5 MB of Local Data Share (LDS) across the GPU, which makes sense considering its larger size. Still, having 21 MB of storage and only being able to use a small fraction of it for compute doesn’t feel great.

Local memory latency improves over Adreno X1, which is impressive because HPM is seven times larger than Adreno X1’s GMEM. However, AMD, Intel, and Nvidia’s latest GPUs still provide better latency to local memory. It’s easier to do that when accesses don’t have to traverse a cross-GPU interconnect.

Thread-to-thread latency through local memory also improves on Adreno X2. But again, AMD’s core-private LDS on their latest GPUs is faster.

Atomic adds on local memory usually enjoy higher throughput than ones through global memory, because most GPUs have dedicated atomic ALUs implemented at per-core local memory instances. That’s not the case for Adreno X2, which is able to sustain 32 INT32 atomic adds per cycle across the entire GPU, or 4 per cycle on a SP basis. For comparison, AMD’s RDNA3.5 can do 32 INT32 atomic adds per cycle at each WGP’s Local Data Share. Intel’s Xe-LPG in Meteor Lake also provides high throughput, with 16 INT32 atomic adds per Xe Core cycle.

Local memory bandwidth testing shows that HPM can deliver as much bandwidth as the GPU’s texture or cluster caches.

## CPU to GPU Data Movement

Software conventionally uses copy APIs to get data to and from the GPU. With OpenCL’s clEnqueueReadBuffer and clEnqueueWriteBuffer, copying data to the GPU is much faster than going the other way around. Prior Adreno GPUs acted like this too. Curiously, pinning the workload to different cores changes measured bandwidth, but only affects movement from CPU to GPU memory. Qualcomm might be using a CPU core to do the transfer, rather than offloading data movement to DMA engines like many other GPUs.

Newer APIs can enable zero-copy behavior. OpenCL’s Shared Virtual Memory (SVM) API is one example, and also maintains the same virtual addresses to let CPU and GPU code use the same pointers. Adreno X2 advertises atomics support with SVM, meaning that the CPU and GPU can theoretically exchange data while a GPU kernel is running. However, I wasn’t able to get the GPU and CPU to see each other’s writes with atomic operations.

I was able to test with fine grained sharing, which lets the CPU see the GPU’s writes after the GPU kernel finishes. Making writes visible between the CPU and GPU is fast enough to show that Qualcomm isn’t copying the entire 256 MB test buffer under the hood. However, kernel launch and synchronization overhead is higher than on other platforms especially if the test is run from an E-Core.

## Compute Performance

FluidX3D simulates fluid behavior using the lattice Boltzmann method (LBM), and has historically been a challenging workload for Adreno GPUs. FluidX3D uses FMA operations in its default configuration, resulting in poor performance on Adreno compared to just about anything else. FluidX3D can be modified to use a “legacy_fma” setting, which uses multiply-add operations instead of fused multiply-add. But even with that modification, Adreno X2 still struggles. It regresses compared to Adreno X1, and is worlds away from last generation iGPUs.

Memory capacity and memory bandwidth tend to be persistent constraints for FluidX3D. Therefore, FluidX3D can be built to use FP16S and FP16C modes, which use 16-bit floating point formats for storage. These 16-bit storage formats are converted back to FP32 for computation to minimize precision loss, effectively increasing compute pressure to reduce pressure on the memory subsystem. FP16S uses the standard FP16 format, letting format conversions take advantage of fast-path hardware on most GPUs. FP16C is a custom format and needs software format conversion, but provides better precision for the typical values that FluidX3D sees.

Neither of these modes help Adreno X2, indicating that compute is the limitation rather than bandwidth. FP16C puts more pressure on compute because of the extra instructions required for format conversion, and actually regresses compared to the full FP32 mode. I’ve included the GTX 1050 3 GB as a comparison because it’s the kind of older, lower-midrange discrete GPU that newer iGPUs should easily beat. Adreno X2 has more than twice as much compute throughput, memory bandwidth, and cache capacity than the GTX 1050 3 GB, so losing to it is disappointing.

### FAHBench

Folding at Home runs protein folding simulations. The project has a rather dated benchmark called FAHBench, which I’m running under binary translation. I briefly tried to build an arm64 version, but it seems like the time investment to do so isn’t worth it. Adreno X2 turns in a passable result on the default dhfr (dihydrofolate reductase) workitem, though losing to the GTX 1050 3 GB is again not a good look.

FAHBench also includes a larger nav (voltage gated sodium channel) workload that tends to place more pressure on the memory subsystem, compared to the more compute bound dhfr workload. I had several GPUs fail the accuracy check in this workload. I’m showing their performance anyway because their calculation results only differ in the 5th or 6th significant digits (for the GTX 1050 and Adreno X2 respectively). They weren’t off by orders of magnitude, indicating that they were making a good faith effort at the work involved.

Nvidia’s GTX 1050 3 GB is 36% faster than the Adreno X2 with the nav workitem, while it was just 13.7% faster with dhfr. Adreno X2 seems to struggle with memory bound workloads. I wonder if its relatively low TLB coverage (for a GPU) combined with high TLB miss costs hold it back in less cache-friendly compute workloads.

## Graphics Performance

3DMark’s Wild Life Extreme should be a familiar workload for Qualcomm, because it’s a Vulkan-based test that targets mobile devices. Adreno X2 performs very well in Wild Life Extreme, pulling comfortably ahead of Meteor Lake’s iGPU and taking up a reasonable position relative to AMD’s largest iGPU. Fire Strike Extreme is a heavy DirectX11 workload, which I had to run under binary translation. I’m only presenting the graphics score for that test. Fire Strike Extreme is a tougher challenge for Adreno X2, but it still manages a comfortable lead over Intel’s older iGPU.

Adreno X2 also does well in Cyberpunk 2077’s built-in benchmark, where it provides twice the performance of Intel’s Meteor Lake iGPU and Nvidia’s old GTX 1050 3 GB.

Cyberpunk 2077 performance is vastly better on Adreno X2 compared to the prior Adreno X1, which [achieved 24.3 FPS at 1080P](https://chipsandcheese.com/p/the-snapdragon-x-elites-adreno-igpu) with the low preset. Adreno X2 easily beats this at the medium preset, which I’m using because Cyberpunk 2077’s CPU-side load isn’t trivial like in 3DMark’s graphics test. High framerates could bring binary translation overhead into the picture, and I wanted to avoid that. Overall Qualcomm seems to be doing well in rasterization, in contrast to the poor performance in GPGPU workloads.

### Raytracing

3DMark’s Solar Bay test showcases raytraced reflections in a simple scene. It’s a lighter workload meant to fit within the capabilities of typical cell phones while still using raytraced effects. Adreno X2 turns in an exceptional performance here. It outperforms Meteor Lake’s iGPU and AMD’s Radeon 780M by more than a factor of two, and isn’t too far off AMD’s Radeon 8060S. It’s also a huge improvement over Adreno X1.

Adreno X2 brings DirectX Raytracing (DXR) 1.1 to Qualcomm’s GPU line, letting a wide range of PC games tap into Adreno’s hardware raytracing accelerators. 3DMark has a more demanding Port Royal test that uses DXR, which targeted high end gaming PCs from a few generations ago. Compared to Solar Bay, Port Royal makes heavier use of compute shaders and places less emphasis on the conventional rasterization pipeline.

Curiously, Adreno X2 achieves the same score as Meteor Lake’s iGPU in Port Royal. Qualcomm also loses ground relative to Strix Halo’s massive iGPU, and only achieves 50.8% of the Radeon 8060S’s score compared to 74.5% in Solar Bay. It’s also fun to note that a score of 1678 corresponds to 7.77 average FPS, which isn’t ideal for most games.

Cyberpunk 2077 is something of a raytracing showcase title. I’m testing that by taking the medium preset above, enabling raytraced reflections, and setting the raytraced lighting slider to medium. Bringing those raytraced effects into the picture destroys performance on all three iGPUs. None of them deliver a comfortably playable framerate, but there is a concerning shift in placement. Adreno X2 no longer ties or beats Meteor Lake’s iGPU, and now loses by a large margin.

There’s certainly potential in Qualcomm’s raytracing implementation, as 3DMark’s tests show. Qualcomm’s slides indicate that each uSPTP has a raytracing unit (RTU) with vaguely similar capabilities to Intel’s RTAs. Both implementations accelerate BVH traversal and intersection testing, and both embed a L0 cache into the raytracing unit.

I wonder what holds Qualcomm back in Cyberpunk 2077 with raytracing enabled. I doubt it’s a CPU-side bottleneck, because the GPU stays at or near 100% throughout the benchmark run. Maybe it’s because Cyberpunk 2077 has a huge BVH that covers the entire city. When profiling with AMD’s tools on RDNA2, Cyberpunk 2077’s BVH had over 59K nodes, compared with 11.6K nodes in 3DMark Port Royal. Or, maybe Cyberpunk 2077’s raytraced effects put a higher burden on the compute pipelines. I haven’t done the profiling necessary to figure out why Adreno X2 behaves the way it does.

## Final Words

Adreno X2 is a step forward for Qualcomm’s GPU line in many respects. General performance benefits from higher clocks, more SPs, and a beefier memory subsystem. Specific classes of workloads can stand to benefit more thanks to Adreno X2’s huge HPM block and improved raytracing units. Adreno X2 subjectively feels good enough to not hold Qualcomm’s laptop push back. I tried a few games that I’ve been playing recently, and performance felt appropriate for a mainstream iGPU.

However, Qualcomm’s latest iGPU still contains a lot of glass jaw performance cases for a modern GPU. Adreno X2 inherits Adreno X1’s tendency to fall over in GPGPU compute. Architectural improvements are certainly evident in compute microbenchmarks, but those observations don’t translate into good performance in the compute workloads I tried. It feels like Qualcomm took a specific set of graphics workloads and optimized for them, while AMD, Intel, and Nvidia set out to build more general purpose designs with robust performance characteristics across a broader range of use cases.

For now, I think Qualcomm has bigger fish to fry. Binary translation overhead was the biggest issue I faced when trying to game on the device, because it’s easy to get bound by CPU performance when running x86-64 binaries. When playing back an Age of Empires II game through CaptureAge for example, the Snapdragon X2 Elite Extreme couldn’t provide enough CPU performance to maintain realtime playback, while Strix Halo had enough spare CPU power to fast forward. But in the years to come, Qualcomm’s GPU will have a tough matchup on their hands. Today’s iGPU landscape is characterized by brutal competition. AMD’s Radeon 8060S and Intel’s Arc B390 can approach the performance of lower-midrange mobile discrete GPUs in both graphics and compute. The thin and light laptop trend will likely continue, and drive AMD and Intel to create ever more ambitious designs. I look forward to seeing what Qualcomm has in store for their future designs, and hope they’ll challenge the best that AMD and Intel have to offer.
