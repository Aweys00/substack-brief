---
title: "An Investor's Handbook IV - AI Inference (1)"
source: "Nutty"
author: "Nutty"
url: "https://nuttycld.substack.com/p/an-investors-handbook-iv-ai-inference"
published: "2026-08-27T20:12:15+00:00"
words: 2233
preview_only: true
---

# An Investor's Handbook IV - AI Inference (1)

This is an analysis of industry and technology structure, not investment advice. The author may hold positions in securities mentioned.

This post has bonus content for paid subscribers. Upgrade to get full access.

This has been a noisy week, courtesy of Hot Chips. Vera Rubin, LPX, Jalapeño, zHBM… familiar names and unfamiliar acronyms poured out all at once across X, Substack, and the trade press. The GPU era is ending and the inference era is here, the rack is what matters now, memory is splitting into tiers. It feels like a change too big to keep up with, and yet the substance stays vague, hard to get your hands around. It seems like one good study session would clear it all up, if only you knew where to start.

That is what this handbook is for. Read it once, keep one picture in your head, and the flood of news that follows should become much easier to place. The story starts with Groq.

Groq has argued since its founding that “GPUs are not suited to inference” (that is Groq, not xAI’s Grok). It is hardly alone. Most companies building inference ASICs (chips hardened around one job) say the same thing. Rather than charging head-on at the GPU, the general-purpose brain of AI, they target inference: demand is growing fast, the barriers to entry are comparatively low, and it is a market small companies and teams can actually attack. That no architectural ‘standard’ has settled yet is part of the opportunity, a contest of designs still up for grabs. It is the era of neighborhood coffee shops, each trading on its own personality, before the franchises move in. And out of that uncertainty grows the heterogeneous system: many different kinds of chips mixed and running inside one system.

Groq’s approach is simple. Inference, unlike training, demands far more trips to memory per handful of compute. The reason is simple too. If training is a process of shoving vast amounts of data through in parallel all at once (a description about a hundred times too crude, but close enough), inference is the LLM answering our question. It emits one word, then the next word conditioned on that word and everything before it, over and over: an endless series of memory lookups. Having to keep fetching from memory, that is the deepest difference from training. When data moves that often, the closer memory sits to the compute, the better. So Groq packed the chip with all the SRAM it could fit, the fastest and most expensive memory there is. That is how a chip was born that might be a luxury for training, but fits inference exactly.

And the king of GPUs saw the value. On December 24, 2025, NVIDIA ($NVDA) signed the largest deal in its history with Groq (about $20 billion by press accounts). Interpretations split at the time. Some went as far as suggesting NVIDIA was buying a future threat early, to keep the market from ever forming, or at least slow it. After all, the prevailing view was that the GPU and Groq’s inference-only LPU (Language Processing Unit) would sooner or later end up competitors.

Eight months later, August 24, the opening day of Hot Chips. The most important announcement of the day came from off the stage, in a press release. NVIDIA announced that the Groq 3 LPX rack had entered mass production, named the cloud provider Nebius ($NBIS) as its first customer, and noted that the cloud business of Groq, the very company that sold the technology, would be among the early buyers. Buying back a product built from the technology you sold. The dedicated on-stage talk on the LPU came only the next afternoon. NVIDIA set the LPX rack beside the Rubin GPU and drew the picture plainly: the GPU reads the question, the LPU writes the answer. The ecosystem is heading toward interlocking parts rather than mutually exclusive competition, and the biggest beneficiary of the GPU era demonstrated it firsthand.

But if the story stops at “the heterogeneous future is coming,” it becomes the kind of dull claim anyone can make. First, a common misreading needs correcting.

Do not read the inference era as an era that shrinks the GPU’s place.

The point is that inference is being decomposed. Prefill (reading the question), decode (writing the answer), KV cache (the memory of the conversation), agentic orchestration (directing the work). The pieces have grown identities too distinct to keep filing under the single name ‘inference,’ and we have reached the moment when optimizing each piece separately is worth doing. Read the market as phase-specific infrastructure, not as GPU vs ASIC.

Inference is not becoming an ASIC market. It is becoming a heterogeneous systems market.

And in that heterogeneous system, if you trace what actually separates piece from piece, you arrive at memory.

Memory is no longer something attached to the accelerator. The memory architecture determines what the accelerator is.

Workload decomposition → compute divergence → memory divergence → rack reintegration. This essay walks those forks in order.

### Two Clocks Inside One Token

The moment you send a prompt, the model does two very different jobs in sequence. First it reads the entire input at once. This is prefill. Thousands of tokens are processed simultaneously, so the math becomes matrix-times-matrix, and tens of thousands of compute units run with no gaps. Classic compute-bound, the very reason the GPU was born. The clock a user feels here is TTFT (time to first token), the time from sending the question to the first word appearing.

Then the model writes the answer. This is decode. The ‘memory lookup’ loop from the top of this essay, emitting one word and joining the next to it, happens here. To make each token, the model has to haul its weights out of memory in their entirety, yet the actual math is just that giant matrix multiplied by a single-column vector. Most of the compute sits idle. The clock changes too. What matters now is TBT (time between tokens), the gap between one token and the next. The speed at which the answer flows.

Think of a library. Prefill is dozens of readers going through one open book at the same time; the pace is set by the number of seats. Decode is reading one line, returning the book to the stacks, and fetching it again for the next line. What holds you back is not the seats but the speed of the trips to the stacks.

Time per token is roughly ‘bytes to read ÷ memory bandwidth.’ It is an idealized best case that real systems can only fall short of, but it is plenty for intuition. Put 2023’s standard equipment, the H100 with its 3.35TB/s, together with a 70-billion-parameter model in FP16. About 140GB of weights must be read in full for every token, which works out to about 42ms of pure memory reading. In that time the compute units could have done trillions of operations; instead they wait, starved of data. The most expensive waiting room in the world.

Run the same division with 2026’s latest numbers and 42ms falls to 1.6ms. The newest GPUs carry nearly seven times that machine’s bandwidth, and pressing the model into FP4 (a 4-bit-per-parameter format) cuts the bytes to read to a quarter. A 26x improvement in three years (though 4x of it belongs to the number format, not the hardware). So is the inference-latency problem solved?

No. The bottleneck moved.

The library of 2026 has a new headache. While writing the answer, the model has to hold every intermediate result produced from the context so far. This is the KV cache, the pile of sticky notes stacking up on the desk as you read. On a 70B-class model (using the configuration of Llama 3.1 70B), a single 128K-token context produces about 40GB of notes. One user’s long conversation eats half the memory of an H100 (80GB). And in the agent era, inputs are growing from thousands of tokens toward hundreds of thousands. Techniques that share identical content between requests claw back a good share of the notes’ cost, but the underlying question, where the notes live and how they travel, does not go away. Now it is not just the trips to the stacks that slow you down; it is where to pile the notes, and the notes’ own round trips.

There is another problem. A production service does not handle requests one at a time; it batches hundreds of them together. The model weights then get read once and shared by the whole batch, so the per-request cost of reading weights drops sharply. The problem is the KV cache. Each request’s conversation history is its own, so KV must be read separately for every request. As batches grow and conversations lengthen, KV reads, rather than weights, become the biggest cost. Requests also sit waiting for their batch to fill, which delays each individual reply. Lowering cost slows the answers: solving that underlying tension is the first job of inference infrastructure design.

So “decode is memory-bound” is not a fixed property stamped on a chip. It is a conditional state that appears and disappears with the model, the batch, the context, and the SLO. An SLO (service level objective) is the response promise a service commits to keeping, say ‘first word within a second, token gap under 100ms.’ The same hardware hits different bottlenecks depending on how tightly that promise is drawn, which is why the term keeps returning to the end of this essay.

FP4 cuts the bytes to read to a quarter. MoE, the split-expert architecture, wakes only a few experts per token and cuts them again. In exchange, long contexts grow the KV, and the moment experts scatter across many chips, the bottleneck migrates from memory to the network. Solve one spot and another clogs: this list is the to-do list of inference architecture, and new architecture proposals keep arriving aimed at exactly these items. Bottlenecks never disappear; they only move.

A good architecture does not remove every jam. It just moves the jam to the cheapest, most predictable place it can afford.

Finally, the thing that scales every one of these problems up at once is the agent. An ordinary chat asks once and answers once, but an agent plans, searches, runs code, reads the result, and reasons again. One task becomes hundreds of inference calls. A 200ms delay per step looks trivial until it repeats 300 times and becomes a minute. And token prices are still racing toward the floor. The query price of a model producing GPT-3.5-quality answers falling from $20 per million tokens in November 2022 to $0.07 in October 2024 was only the start; as of August 2026, the light model of OpenAI’s newest 5.6 generation (gpt-5.6-luna) sells for $0.20 per million input tokens. A far better model than GPT-3.5 of four years ago, at one hundredth of the price. In a world where tokens get this cheap, the yardstick of competition does not stop at cost per token. What users buy is not tokens but the solved query, the finished code. The metric the agent era’s hardware will eventually be graded on is cost per completed task, the total cost of finishing one job.

### This Did Not Start in Silicon

This divergence did not actually start with 2026’s chip announcements. Software research showed the economics of the crack, in numbers, two years earlier.

In 2024, two studies reached the same conclusion: Splitwise, from the University of Washington and Microsoft ($MSFT), and DistServe, led by Peking University. Stop forcing two different jobs into one line; separate prefill and decode into different machine pools outright. Splitwise reported 2.35x the throughput within the same power and cost budget, and DistServe up to 7.4x per-GPU throughput while holding the same latency terms. The Sarathi line of work showed that without splitting hardware at all, scheduling alone, chunking prefill finely and interleaving it between decode steps, can cut the interference dramatically. “The two phases are different” and “you must have two kinds of chips” are not the same sentence. Today’s inference software stacks, in fact, use both approaches together.

The research since then moved in five steps, and the hardware announcements of 2026 are the final step made physical.

Separation has a price. The moment you split the hardware, the tens of gigabytes of KV cache the prefill machine produced must move to the decode machine, the two pools must be load-balanced, and when one side dies it must be recovered. It is a tug-of-war between the costs specialization saves and the costs coordination creates. Whether inference’s future really goes heterogeneous depends on how that tug-of-war ends, and it has not ended. What we are watching now is its first large-scale experiment.

And tens of billions of dollars are already riding on this experiment. If inference is beginning to split across different kinds of chips, the important question is no longer which chip is faster. It is where the bottleneck moves, who controls it, and where value and margin migrate as a result.

NVIDIA and Groq are the best place to start reading that shift. If parts of the GPU’s job can move elsewhere while NVIDIA remains at the center, why? The answer becomes a framework for judging where value is likely to accumulate next across GPUs, memory, networking, and software.
