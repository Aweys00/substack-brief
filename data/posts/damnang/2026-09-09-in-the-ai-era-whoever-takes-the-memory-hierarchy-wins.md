---
title: "In the AI Era, Whoever Takes the Memory Hierarchy Wins"
source: "Damnang Research"
author: "Damnang"
url: "https://www.damnang.com/p/in-the-ai-era-whoever-takes-the-memory"
published: "2026-09-09T09:44:50+00:00"
words: 2090
preview_only: true
---

# In the AI Era, Whoever Takes the Memory Hierarchy Wins

As the AI era arrives, the memory hierarchy is becoming more varied and more complex. The clearest example is that over the past few months a DRAM maker, a NAND maker, and an accelerator maker each announced plans to add new memory next to HBM. When it became hard to fit all the data AI computation needs into expensive HBM, they set out to supplement capacity with other memory.

What deserves attention here is not simply that the AI era uses a lot of memory.

It is which memory hierarchy will become mainstream in the AI era, and which company will end up leading that structure.

Memory now accounts for a larger share of AI system cost, so taking the lead in deciding how the memory that computation needs is connected, and who can supply it, can become a new form of power.

This article starts with why the memory hierarchy is growing more layers in the AI era. It then goes through the technologies and companies competing at each tier, the changes expected through 2030, and the events to check over the next 12 months, and offers an outlook on each.

Disclaimer

This article is for information only and does not recommend buying or selling any particular stock. Data is as of September 8, 2026. Company announcements, supply-chain estimates, and the author’s own assumptions are kept separate, and estimates may differ from market consensus. The author may hold positions in the companies mentioned and may change them without notice. Investment decisions and their consequences are the reader’s responsibility.

### 1. The simplified memory hierarchy before the AI era

As a rule, faster memory is more expensive and holds less.

So a computer uses several kinds together: SRAM inside the processor, DRAM as working space, and NAND SSDs for long-term storage. Data that is used often goes on the fast side, and data that is not needed right now goes on the cheap side.

The familiar library analogy makes this easy to picture. When you study, you keep the material you need right now on your desk where you can reach it, but the desk cannot hold much, while the vast amount of other material sits in the library, which takes time to reach. The way a computer uses memory is not much different.

Until now, the memory hierarchy has been as simple as the figure below, and the amount of computation to be done was handled reasonably well within that simple structure. DRAM interfaces such as DDR were defined jointly through JEDEC, the semiconductor standards body, and memory makers supplied products to those standards. There were differences in process and yield, but what moved commodity DRAM prices was the supply and demand cycle. When demand rose it was a supercycle, and when supply rose it suddenly turned into a downcycle. Memory has been a commodity in the fullest sense.

### 2. The problem HBM solved, and the problem that remains

With the AI era, this simple hierarchy started to change.

In the library analogy, it used to be enough to keep the few books you needed on the desk (DRAM) and leave the rest in the library (SSD). Large AI models are different. Producing each character of an answer is like rereading every book in the library from cover to cover, so the entire collection has to be on the desk, and it has to be flipped through quickly every time. Conventional DRAM had room to hold the books, but not the speed to flip through them.

So a new tier was inserted into the hierarchy. HBM is memory made by stacking DRAM chips vertically, tying them together with a wide path, and placing them right next to the GPU. It is as if the desk were pulled up beside the GPU and rebuilt so that several books could be flipped through at once. How much data can be moved at a time is called bandwidth, and HBM’s bandwidth is far larger than that of ordinary DRAM modules. That is what let GPUs cope with rereading the whole model every token, and the HBM attached to each GPU has grown with every GPU generation.

The problem is capacity and price. The number of HBM stacks that can be placed around a GPU is limited by package area. To keep the same design, the stack height or the capacity of each DRAM die has to grow, but taller stacks worsen heat and yield, and adding more stacks means redesigning the GPU and the package. HBM also consumes far more wafers than commodity DRAM for the same capacity.

On top of that, HBM prices rose sharply in 2026, making the approach of putting all the needed data in HBM a heavier burden. There is a limit to how far the desk can be widened, its price is going up, and the pile of books that has to sit on it keeps growing. So the next question became whether every book really needs to be on the desk.

### 3. Data used often and data that waits

The data an AI model handles falls into two broad kinds.

One is the weights, the numbers that hold what the model learned; in the analogy, the books.

The other is the context, the content of the question and conversation being processed right now. In the analogy, the notes spread out on the desk.

Both split into a part that is used often and a part that is not.

Let’s see the weights first.

In a dense model that uses every weight every time, each token (the unit in which the model processes text) requires reading every book, so the whole collection must be on the desk. But most large models today use an MoE structure. The model holds several groups of experts, and for each token it picks only the ones it needs. DeepSeek V4 Pro, released in April 2026, has 1.6 trillion parameters in total but uses 49 billion per token ([DeepSeek release](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/commit/0e1a0e5e52aea73055f50fef6f2423db370265b6)). The model still has to own the whole collection, but producing one token opens only about 3% of it.

That splits the weights into two groups.

Experts selected often are hot weights, and experts selected rarely are cold weights. The frequently used ones stay on the desk, that is, in HBM, and the rarely used ones can move to cheaper memory.

That does not mean every expert unused in one token can be pushed down to slow memory. The next token, or another request, may need that expert. When many requests are processed at once, the range of experts needed widens. How much can actually be moved depends on selection frequency and on how fast the data can be brought back.

Next is context.

Context is stored in the form of a KV cache. It holds the intermediate results produced while processing tokens, so the model does not recompute the context it has already read from scratch each time; in the analogy, the notes on the desk. One is created for each request that has its own context, such as a single conversation or a single agent task. Broadly, the longer the context and the more requests there are, the more storage is needed.

The KV cache can also be divided by usage state. The cache of a request that is generating an answer right now is read often and has to be quickly accessible. In typical GPU inference, HBM plays that role.

By contrast, a request that is waiting for a tool to run or for a person to reply does not read its cache until the next turn. Keeping it in HBM leaves less room for other requests; discarding it means recomputing the context later. So the cache is kept outside HBM and brought back when needed. This is called KV cache offloading. NVIDIA also described moving rarely used context to host memory and storage in its August 24 material ([NVIDIA](https://blogs.nvidia.com/blog/vera-rubin-nvl72-efficiency-ai-agents/)).

### 4. How to use capacity outside HBM

Model designs that compress the KV cache are also advancing, so storage per token is trending down. But if context length and the number of concurrent requests grow faster than that, total storage still increases. The more requests are waiting, the stronger the case for keeping their context somewhere cheaper than HBM.

The “attached memory” discussed here means memory outside the GPU package: the HBM of other GPUs, host DRAM attached to the CPU, DRAM expanded over the CXL interface standard, and SSDs that exchange data directly with the GPU. The communication paths that link them are the interconnect.

Being connected does not make all of it as fast as a GPU’s own HBM. Reaching memory on another GPU or another rack means going through links and switches. Optical links extend the reach, but actual bandwidth and latency depend on link speed and topology. So which data sits on which GPU and in which memory becomes important.

The figure above shows the direction in which this kind of placement is spreading. As I said in the introduction, the once simple memory hierarchy is heading toward something more layered. The middle tiers in the figure are still contested, in both technology and in how they will be adopted.

Recent industry announcements also suggest that a trend toward less HBM capacity per GPU package is close to settled. This is the so-called HBM density despec. I have covered it in several articles, and readers who are not yet familiar with it may want to read those first.

To sum up, the industry is shifting the money that would have gone into HBM capacity toward the interconnect, and, looked at more broadly, it is fighting a quiet war to build out a memory hierarchy that has not yet been formalized.

### 5. The same rack can hold more context

As we saw in Section 3, let me do a simple calculation of why moving the context of waiting requests to cheaper memory outside HBM lowers cost. The numbers below are example assumptions meant to show the method; they are not measurements of any product or service. Changing the assumptions changes the absolute figures, but the ratios move the same way.

Take one NVL72 rack with 20.7 TB of HBM, and use 0.8 TB for model weights, leaving 19.9 TB. The 0.8 TB is a simple calculation of 1.6 trillion parameters all stored at 4 bits. In a real deployment, of course, more is needed for metadata, working space, replicas, and so on.

If the KV cache of one 200K-token request is 2 GB, the remaining space can hold about 10,000 contexts. That assumes 10 KB per token and is not a measurement of any particular model.

Now assume that only 20% of requests are generating an answer and the other 80% are waiting. This ratio is an assumption about how much of an agent’s time is spent waiting, and it is the least certain assumption in this calculation. Move the caches of the waiting requests to host DRAM or SSD, and only the caches of active requests remain in HBM. The same HBM can then keep about 50,000 contexts.

This 5x is a ratio of how many contexts can be kept, not of processing speed. It is also an upper bound based on capacity alone, leaving out compute and transfer latency. If the time to bring a cache back exceeds what the service can tolerate, the full 5x cannot be used. If the cache were 100 KB per token, both request counts would fall to one tenth, but under the same assumptions the ratio stays at 5x.

Offloading can reduce the burden of buying more racks for lack of capacity, or of repeatedly recomputing discarded context. Services whose agents spend long stretches waiting in the middle of a task have the most to gain.

In exchange, more host DRAM, SSDs, controllers, and interconnect are needed. Part of the money saved moves to those parts. On NVIDIA’s platform, the configurations and certifications NVIDIA sets have a large say in which suppliers are chosen. On shared standards, customers have more room to combine modules and SSDs from several suppliers.

From here, the article looks at who captures this new demand: the standards competing at each tier, the technologies that become products first, the conditions under which memory makers' bargaining power changes, and finally the size of the demand and the events to check.

Damnang Research is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.
