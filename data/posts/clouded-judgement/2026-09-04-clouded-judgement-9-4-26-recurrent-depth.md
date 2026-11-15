---
title: "Clouded Judgement 9.4.26 - Recurrent Depth"
source: "Clouded Judgement (Jamin Ball)"
author: "Jamin Ball"
url: "https://cloudedjudgement.substack.com/p/clouded-judgement-9426-recurrent"
published: "2026-09-04T13:04:29+00:00"
words: 2300
preview_only: false
---

# Clouded Judgement 9.4.26 - Recurrent Depth

Every week I’ll provide updates on the latest trends in cloud software companies. Follow along to stay up to date!

Recurrent Depth

This week we got a peak into OpenAIs new model Astra. I thought this was an important model because it’s rumored to use a new technique called recurrent depth. In this post I want to discuss what that means and what the implications are. But first - a quick timeline of some of the larger breakthroughs in model architecture:

-

2017: The Transformer era. The leap here was self-attention mechanism. Before 2017 recurrent neural networks (RNNs) processed text word-by-word. The now famous paper Attention is Al You Need introduced the Transformer architecture which made parallel training possible

-

2018-2020: Decoder-Only Architectures. The leap here was autoregressive scaling and in-context learning. Early on transformers used a encoder-decoder setup (like BERT). OpenAI flipped this by scaling decoder only models (GPT-1 to GPT-3). The result of this technique was that by just predicting the next token (when scaled across billions of parameters) naturally created emergent capabilities like in-context learning.

-

2023: Sparse Mixture-of-Experts (MoE). The leap here was conditional routing. The learning was that as models grew larger and larger in parameter count, it became economically infeasible to activate every single parameter for every single token. The result was to not activate every single parameter for every token. Instead, models would route tokens to a specialized network of “expert” subnetworks / parameters. This allowed huge models (and huge intelligence) to only run compute against a smaller subset (ie made a huge model’s cost mirror more of a smaller model). Kimi K3 has 2.8T total parameters, but only ~2% are “active.” Some of these much larger models (Like DeepSeek V4 have similar sparsity ratios of low / mid single digits. These sparce models are in contrast to dense models - like Gemma 27B, which activates all 27B parameters for each token.

-

2024: Test-Time Compute / Chain-of-Thought / Reasoning. The leap here was explicit inference scaling and “thinking models.” This was the flagship OpenAI o1 (and o-series) of models. OpenAI introduced scaling compute at inference time rather than only at training time.

-

2026: Recurrent Depth / Looped Transformers. Could this be the next leap?? The potential leap here (we’ll discuss) is implicit latent space reasoning. Let’s dig in more on this new architecture!

Let me caveat all of this - as far as I know, it’s still “rumored” that the Astra model series uses Recurrent Depth (great reporting from [The Information](https://x.com/steph_palazzolo/status/2094954680765829533)!). I don’t believe OpenAI has confirmed anything. But still fun to dig into what this new technology means!

I’ve been doing a lot of research on recurrent depth the last few days (so I’m by no means an expert), and the most simplistic way I can describe it is this. A transformer architecture is made up of a stack of layers, and a token will go through each layer once. At each layer the model will look at the token alongside everything around it, and will then refine it’s understanding a bit more. So by the time the token exits the last layer it has been through many rounds (ie layers) of refinement. Said a bit more complexly, each layer takes the tokens current mathematical representation (big list of numbers in a vector), looks at the tokens around it, and then slightly tweaks the representation (ie numbers) a bit. And this happens over and over again at each layer, where once it comes out the last layer it’s fully refined.

What changes in a recurrent depth (or “looped transformers”) architecture is that the token will go through the same block of layers multiple times. Said another way, the token isn’t just refined through each layer once, it’s refined through multiple layers multiple times. This then changes the trajectories of models. Before this architecture, the normal way to build a more capable model was to just add more layers (or to make individual layers wider). Add more periods of refinement (or make the period of refinement more detailed). Imagine dirty water passing through many layers of paper filters. The more paper filters you add, the cleaner the water comes out at the end. And the water just passes through one layer, one at a time. The looped approach doesn’t need to add more layers of paper filters, it can just run the water through a smaller number of filters, but do it over and over again. To complete the analogy, it’s like putting water in a water wheel, and running it around and through the same filter multiple times.

If I can take a stab at a slightly more technical explanation. Depth in a transformer is typically described as the number of layers, where each layer has it’s own weights. By scaling depth the “old” way - parameters, memory and compute all go up (or down) in unison. By contrast, when you loop, parameters and memory can stay flat, but the compute doubles (if you’re passing through same block of layers twice, or triples if you go through 3 times, etc). There’s not tons of public research out there (yet), but from my understanding the sweet spot of re-passes is ~2. There was a pretty cool research paper published on [Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation](https://arxiv.org/abs/2507.10524) that adds a smaller “learned router” that decides (per token) how many loops to run. More basic computations might run through a layer once. As complexity grows, the number of loops grow. “Adaptive compute” at the token level is another way to describe this.

So why does this matter? A couple I can think of.

First, memory is a real constraint right now for inference. With recurrent depth / loops, a model can get 2x as effective depth without needing more memory (what I described above, you don’t have to scale all of parameters / memory / compute together, you can do them separately to drive similar results). Second, it also might move some of the thinking from output tokens into what looks like more hidden computations. If a model can do more work “internally” inside the model layers (before spitting out the output tokens, and then iterating on the outputs), it may require less reasoning tokens to get to the same output. This starts to matter for models that denominate pricing with input / output token pricing. Will we need a new 3rd vector of pricing? input / output / internal tokens?

Then there’s an entirely different takeaway. That all of this really isn’t that big of a deal… A lot of people are saying this breakthrough isn’t actually that much of a breakthrough, and we can’t really attribute all of Astra’s performance gains to recurrent depth architecture. That paper I referenced earlier was written over a year ago. This isn’t something brand new. Reasoning / chain of thought felt like a huge deal. Recurrent depth / loops feel like more of a modest architectural tweak. It’s not necessarily faster to train or run. My naive quick takeaway is - is this architecture tweak similar to when Snowflake separated compute / storage? Before Snowflake, Redshift forced you to scale storage / compute in unison.

I’ll end with a shoutout back to the Information piece, and something they brought up. What the article discussed was how this new technique may actually obfuscate the models reasoning / chain of through. The implication is that the chain of thought is the best “peak under the hood” on how the model is working, and by making this more opaque it may make the models less auditable. And with that new safety / control problems arise. This got enough traction that Jakub Pachocki (OpenAI’s chief scientist) [commented](https://x.com/merettm/status/2095023204993490967). To summarize (full tweet linked), he said the depth of Astra’s computation graph is ~2x of GPT-4, so nothing really changes how much hidden computation happens per token. He also slightly countered the initial Information claim by saying chain-of-thought monitoring isn’t as useful as people think anyway.

Sam Altman also went on Bloomberg yesterday, interviewed by [Ed Ludlow](https://x.com/EdLudlow) who asked him a question about the model observability. I was watching live, so this quote is more of a paraphrase on Sam’s response:

We have talked for a long time about the importance of monitorability…We also believe in defense in depth…there’s sandboxing, alignment, and a number of things that come together to make the models safe…Monitorability is an important thing we’ve been talking about for a while, the importance of chain of thought monitoring…We’ve made lots of decisions to preserve chain of thought observability. It’s important. I also want to be clear that it’s not the only thing that matters.

Quarterly Reports Summary

Top 10 EV / NTM Revenue Multiples

Top 10 Weekly Share Price Movement

Update on Multiples

SaaS businesses are generally valued on a multiple of their revenue - in most cases the projected revenue for the next 12 months. Revenue multiples are a shorthand valuation framework. Given most software companies are not profitable, or not generating meaningful FCF, it’s the only metric to compare the entire industry against. Even a DCF is riddled with long term assumptions. The promise of SaaS is that growth in the early years leads to profits in the mature years. Multiples shown below are calculated by taking the Enterprise Value (market cap + debt - cash) / NTM revenue.

Overall Stats:

-

Overall Median: 4.4x

-

Top 5 Median: 31.0x

-

10Y: 4.8%

Bucketed by Growth. In the buckets below I consider high growth >22% projected NTM growth, mid growth 15%-22% and low growth <15%. I had to adjusted the cut off for “high growth.” If 22% feels a bit arbitrary, it’s because it is…I just picked a cutoff where there were ~10 companies that fit into the high growth bucket so the sample size was more statistically significant

-

High Growth Median: 18.1x

-

Mid Growth Median: 6.7x

-

Low Growth Median: 3.9x

EV / NTM Rev / NTM Growth

The below chart shows the EV / NTM revenue multiple divided by NTM consensus growth expectations. So a company trading at 20x NTM revenue that is projected to grow 100% would be trading at 0.2x. The goal of this graph is to show how relatively cheap / expensive each stock is relative to its growth expectations.

EV / NTM FCF

The line chart shows the median of all companies with a FCF multiple >0x and <100x. I created this subset to show companies where FCF is a relevant valuation metric.

Companies with negative NTM FCF are not listed on the chart

Scatter Plot of EV / NTM Rev Multiple vs NTM Rev Growth

How correlated is growth to valuation multiple?

Operating Metrics

-

Median NTM growth rate: 13%

-

Median LTM growth rate: 16%

-

Median Gross Margin: 76%

-

Median Operating Margin 4%

-

Median FCF Margin: 21%

-

Median Net Retention: 110%

-

Median CAC Payback: 31 months

-

Median S&M % Revenue: 34%

-

Median R&D % Revenue: 22%

-

Median G&A % Revenue: 13%

Comps Output

Rule of 40 shows rev growth + FCF margin (both LTM and NTM for growth + margins). FCF calculated as Cash Flow from Operations - Capital Expenditures

GM Adjusted Payback is calculated as: (Previous Q S&M) / (Net New ARR in Q x Gross Margin) x 12. It shows the number of months it takes for a SaaS business to pay back its fully burdened CAC on a gross profit basis. Most public companies don’t report net new ARR, so I’m taking an implied ARR metric (quarterly subscription revenue x 4). Net new ARR is simply the ARR of the current quarter, minus the ARR of the previous quarter. Companies that do not disclose subscription rev have been left out of the analysis and are listed as NA.

Sources used in this post include Bloomberg, Pitchbook and company filings

The information presented in this newsletter is the opinion of the author and does not necessarily reflect the view of any other person or entity, including Altimeter Capital Management, LP (”Altimeter”). The information provided is believed to be from reliable sources but no liability is accepted for any inaccuracies. This is for information purposes and should not be construed as an investment recommendation. Past performance is no guarantee of future performance. Altimeter is an investment adviser registered with the U.S. Securities and Exchange Commission. Registration does not imply a certain level of skill or training. Altimeter and its clients trade in public securities and have made and/or may make investments in or investment decisions relating to the companies referenced herein. The views expressed herein are those of the author and not of Altimeter or its clients, which reserve the right to make investment decisions or engage in trading activity that would be (or could be construed as) consistent and/or inconsistent with the views expressed herein.

This post and the information presented are intended for informational purposes only. The views expressed herein are the author’s alone and do not constitute an offer to sell, or a recommendation to purchase, or a solicitation of an offer to buy, any security, nor a recommendation for any investment product or service. While certain information contained herein has been obtained from sources believed to be reliable, neither the author nor any of his employers or their affiliates have independently verified this information, and its accuracy and completeness cannot be guaranteed. Accordingly, no representation or warranty, express or implied, is made as to, and no reliance should be placed on, the fairness, accuracy, timeliness or completeness of this information. The author and all employers and their affiliated persons assume no liability for this information and no obligation to update the information or analysis contained herein in the future.
