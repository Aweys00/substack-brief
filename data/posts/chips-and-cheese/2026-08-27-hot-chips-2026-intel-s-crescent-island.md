---
title: "Hot Chips 2026: Intel’s Crescent Island"
source: "Chips and Cheese"
author: "George Cozma"
url: "https://chipsandcheese.com/p/hot-chips-2026-intels-crescent-island"
published: "2026-08-27T05:12:31+00:00"
words: 763
preview_only: false
---

# Hot Chips 2026: Intel’s Crescent Island

Hello you fine Internet folks,

At Hot Chips, Intel talked a bit more about their upcoming Datacenter GPU codenamed Crescent Island.

Crescent Island’s party piece is the ultra-high memory capacity curtesy of the LPDDR5X memory subsystem.

### Making Room for Whales

That LPDDR5X subsystem can support up to 480 GB of DRAM which, at the time of writing, is the single highest capacity memory subsystem found on any “GPU”/AI accelerator.

This means that a single Crescent Island can easily run Deepseek-V4 Flash straight out of the VRAM which is an achievement that no other non-HBM “GPU” can claim. However, the all-important memory bandwidth of Crescent Island is still unknown and when asked Intel’s response was “We are not disclosing that information at this time.”

Realistically, there is only one possible memory bus width, 1280 bit, because of both the memory capacity along with the leaked PCB photos. And with a 1280-bit LPDDR5X memory subsystem using LPDDR5X-9600, Crescent Island would have over 1.5 TB/s of memory bandwidth.

### Shooting for the Stars

Crescent Island also incorporates Intel’s brand new Xe3P IP which makes it part of the Celestial series of GPUs.

Xe3P has mostly improved the XMX units by both making them 4 times larger than the units found in Xe2 and Xe3 as well as adding FP8 and FP4 support to the XMX units. Other changes to the Xe core include increasing the L1/SLM up from 384 KB per Xe Core in Xe3 to 512 KB per Xe Core in Xe3P as well as doubling the Register File to 1 MB per Xe3P Core.

There were rumors about Xe3P doubling the number of ALUs in an XVE, however it looks like Xe3P is still SIMD16 for the XVEs.

Crescent Island consists of 32 Xe3P cores backed by 32 MB of L2 as the last level cache. 32 MB of last level cache is less than either NVIDIA’s Blackwell or AMD’s RDNA3/4; however, those GPUs are multi-purpose and are used for tasks where a greater than 32 MB LLC is beneficial to those workloads. Crescent Island being an “AI GPU” means that it was largely designed for AI and compute tasks which don’t require a large LLC due to being mostly memory bandwidth bound.

Something else of note is that Crescent Island has full rate FP64 which equates to 2,048 FMA operations across the whole GPU. At 2.5 GHz, this would give Crescent Island approximately 10 Teraflops of FP64 compute which is well above the competition which don’t support full rate FP64 on this class of GPU.

However, next generation CPUs such as Venice and Diamond Rapids will have more FP64 compute as well as more memory bandwidth and capacity which makes those quite tantalizing for many HPC use cases.

Speaking of compute numbers, Intel also didn’t provide these numbers so if we run with the assumption that Intel will clock Crescent Island to approximately 2.5 GHz and that Intel quadrupled the rate of matrix operations while not changing the datatype ratios of matrix operations, we get the following approximate compute numbers:

-

- 10.2 TFLOP/s FP64 vector

-

- 20.5 TFLOP/s FP32 vector

-

- 41 TFLOP/s FP16 vector

-

- 328 TFLOP/s TF32 XMX

-

- 655 TFLOP/s FP16/BF16 XMX

-

- 1.3 PFLOP/s FP8 XMX

-

- 2.6 PFLOP/s FP4/MXFP4 XMX

This puts Crescent Island about 30% ahead of NVIDIA’s RTX PRO 6000 Blackwell for matrix compute and over 5x for FP64 operations while the RTX PRO 6000 has over 6x the FP32 compute and 3x the FP16 vector compute.

### Final Words

Crescent Island is an innovative GPU with quite an interesting product definition caused by the unrivaled memory capacity from the LPDDR5X subsystem. With the current highest memory capacity of any dGPU paired with class-leading FP64 compute and beefed-up matrix units that surpass the current generation RTX PRO 6000 in terms of compute.

However, the elephant in the room is when this GPU is launching. At OCP 2025 Intel announced that Crescent Island would be sampling at the end of this year. However, with the lack of details that Intel was willing to disclose at Hot Chips along with the rocky history that Intel’s Datacenter GPU lineup has had, it’s possible that the timeline has slipped into 2027.

Regardless, this is a very interesting offering from Intel that could serve a market that really only Apple is serving at the moment which cares about memory capacity per dollar above all other considerations. It also could serve parts of the very underserved HPC community with its full rate FP64 capability.
