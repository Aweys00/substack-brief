---
title: "Can AMD Beat NVIDIA? part2: Vera Rubin's HBM4 Pin Speed Downgrade"
source: "Damnang Research"
author: "Damnang"
url: "https://www.damnang.com/p/can-amd-beat-nvidia-part2-vera-rubins"
published: "2026-10-27T09:30:32+00:00"
words: 1756
preview_only: true
---

# Can AMD Beat NVIDIA? part2: Vera Rubin's HBM4 Pin Speed Downgrade

As NVIDIA lowered Vera Rubin’s official specs, AMD now leads in memory bandwidth, where Rubin had been ahead at the January announcement.

So, once again, we are asking like this,

“Can AMD beat NVIDIA?”

On April 17, I wrote an article with this question as its title, and in that piece I split the question into three and analyzed them.

-

Whether AI infrastructure demand is growing faster than what NVIDIA alone can supply

-

Whether there are enough large customers who deliberately want to avoid NVIDIA

-

Whether AMD avoids execution setbacks from the second half of 2026 through 2027

And now that we are in the second half, AMD is starting mass production of the Helios rack.

Damnang’s take

As readers of my previous article will know, when I talk about AMD beating NVIDIA, I don’t mean overtaking NVIDIA in market share to become number one. I mean whether AMD can create the conditions to grow meaningfully by competing on its own terms.

This article sets out to analyze AMD’s competitiveness again, based on the joint Meta and AMD paper “[Architecting for Hardware Diversity](https://arxiv.org/pdf/2610.22230v1)” posted on arXiv in October.

In this paper, Meta reported, with numbers from a customer’s data center, the speed, failures, and software issues it saw while training production recommendation models on tens of thousands of MI350X GPUs and comparing them with B200.

In this article, after explaining this paper in an easy-to-understand way, I go further and compare MI455X and Rubin, whose specs recently changed, including price and power, and then analyze the share AMD will gain through 2028 together with the expectations already reflected in the stock price.

If you read this article and also read my analysis of AMD’s earnings coming up on November 3, I am confident it will become clearer how to view the competition between NVIDIA and AMD going forward and what investment insights can be drawn from it.

This article is written for informational purposes and does not recommend buying or selling any particular stock. Stock prices and multiples are based on closing prices on October 23, 2026, and estimates are based on market consensus and public materials. I may hold the stocks mentioned in this article, and my positions may change. Investment decisions and responsibility rest with the reader. NFA/DYOR.

Damnang Research is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

### 1. Meta runs large-scale training on AMD GPUs

In training, tens to hundreds of GPUs must align their results at every step, which makes it a complex process, so even slight instability in hardware or software can stop the entire job.

That is why Meta has used AMD GPUs first for inference rather than training since 2024.

And this Meta and AMD paper said this is the first case report of a hyperscaler running large-scale training on AMD GPUs.

According to the paper, Meta currently operates hundreds of thousands of AMD GPUs, and by resource usage, more than 60% of its production model types are already compatible with AMD GPUs.

In other words, this paper can be called a good case for understanding how competitive AMD can become in large-scale training, the market where NVIDIA is strongest, and what that means for AMD’s revenue and market share.

In this article, I will first analyze and understand this paper in detail.

### 2. MI350X has 1.6 times more HBM than B200

The figure above is a simplified drawing of the structure of the two GPUs.

MI350X uses a chiplet approach, making several small chips and bundling them instead of one large chip, and stacks 8 compute chiplets (XCDs) that handle calculation on top of 2 I/O dies.

B200 attaches two large compute dies side by side. Both GPUs attach 8 HBM stacks right next to them. MI350X uses 12-high HBM3E with 12 DRAM dies stacked, and B200 uses 8-high HBM3E with 8 dies stacked.

Note

In March 2024, when NVIDIA announced B200, 12-high HBM3E was not yet in mass production. SK hynix started mass production of 12-high HBM3E in September 2024, and NVIDIA also began using 12-high stacks from B300 to reach 288GB per GPU. The 1.6x capacity difference is a figure for the B200 that Meta compared.

The figure above redraws the spec table of the Meta paper as the ratio MI350X ÷ B200.

Compute performance is nearly the same at 2,300 vs 2,250 TFLOPS in BF16 format, which is mainly used for AI training.

HBM bandwidth, the speed of reading and writing data from HBM, is also the same at 8TB per second for both. MI350X has 1.6 times more HBM capacity, and B200 is 1.7 times faster in the speed at which the 8 GPUs within one server exchange data (scale-up bandwidth).

Power, based on Meta’s servers, is 1,000W for MI350X and 750W for B200.

According to the paper, B200 is originally a chip that uses 1,000W, but it generates a lot of heat relative to its chip area, so Meta said it lowered B200’s power cap to 750W to handle the heat in air-cooled servers.

### 3. Same number of GPUs, same batch: a 10-model average of 101.2%

In this paper, the Meta training models are recommendation models called DLRM (Deep Learning Recommendation Model). These are models that decide which posts and ads to show in the feed, so they are directly tied to Meta’s revenue.

The paper picked 10 production models and compared the number of data samples MI350X and B200 train per second with the same number of GPUs and the same batch size. Model sizes range from 100 million to 3.6 trillion parameters. A batch is the size of the bundle of data a GPU trains on at once.

As in the figure above, MI350X delivered 82% to 130% of B200’s speed depending on the model, and the 10-model average is 101.2%.

The GPUs used in the comparison range from 8 to 128 depending on the model. Because 75% of the recommendation model training jobs running at Meta run on 64 GPUs or fewer and 99% on 128 or fewer, this comparison covers most of the typical scale of Meta’s recommendation model training jobs.

Damnang’s Note

However, the B200 that Meta compared is a product with its power limited to 750W. Compared with a regular B200 that uses the full 1,000W, B200’s speed goes up, so I expect MI350X’s 101.2% to come out lower than this.

### 4. AI cut the time to refine NVIDIA-tuned kernels for AMD to one-tenth

One of NVIDIA’s strengths is software that has been refined for NVIDIA GPUs over many years. Because AI training code is tuned for NVIDIA, using another GPU takes time and people to move the code and refine it again.

In the paper, Meta says it greatly reduced the cost of this work by using AI agents, and that AI agents have fundamentally lowered the cost of switching from NVIDIA to AMD. In other words, MI350X reaching a speed similar to B200 can also be seen as thanks to software fixed in this way.

So what did Meta change, and how?

Understanding the full paper requires a lot of engineering knowledge, but in this article I will try to explain it with a simple example.

A representative example is the atomic operation.

Let’s think about the vote counting process after an election.

Imagine 1 million vote counters calling headquarters to report their results. Each person needs to add their votes to one shared tally board. Only one person can update it at a time, so everyone else has to wait.

On B200, that board sits in a cache shared by the entire GPU. Think of it as everyone lining up at the same office. Each update stays within that shared system, so the line can move quickly.

MI350X spreads its compute across eight chiplets. Think of them as eight separate buildings. When an update requires coordination between buildings, information has to travel over the connection between chiplets, called Infinity Fabric. That extra communication can make the line move much more slowly.

For workloads where many threads repeatedly update the same value, this can create a large performance gap. However, a slowdown of more than 10 times, should be tied to a specific benchmark rather than treated as a general rule.

To solve this, Meta created a new computation method (kernel) for MI350X.

Just as each polling station first adds up its votes and reports only the total to headquarters, Meta changed it so that each thread group (block) first computes a total inside the chiplet and then adds only that total to the tally board once (tree reduction).

As in the figure above, the number of additions to the tally board dropped from about 1 million to about 1,000, and the kernel became more than 4 times faster.

The paper says that under conditions where additions pile up, it was even 1.75 times faster than B200.

In Meta’s actual full training code, there are kernels like this that must be optimized for MI350X separately for each model, so fixing them all one by one by hand is not easy.

In the paper, Meta says it improved this process using AI agents. The agent runs the kernel to measure where time is leaking, picks the right technique and fixes the code, and then checks whether the answer stays the same and it actually got faster, repeating this process on its own to improve performance.

As seen in the figure above, Meta said it applied this method to dozens of kernels in production using this AI agent and succeeded more than 80% of the time. The kernels fixed by the agent delivered performance close to that of real experts,

and development time was cut to about one-tenth.

NVIDIA’s CUDA ecosystem has become NVIDIA’s strong moat as AI has advanced. But ironically, that moat is now being torn down by advanced AI. I see the results of this Meta and AMD paper as a meaningful real-world case showing that NVIDIA’s software moat can crumble. The lower the cost of moving code to another GPU, the more customers can choose GPUs based on price, memory capacity, and supply rather than software.

From the section below, I analyze in detail which direction the competition between the two companies could take going forward, based on what was reported in this paper.

Damnang Research is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.
