---
title: "Clouded Judgement 8.7.26 - Custom Tokens"
source: "Clouded Judgement (Jamin Ball)"
author: "Jamin Ball"
url: "https://cloudedjudgement.substack.com/p/clouded-judgement-8726-custom-tokens"
published: "2026-08-07T13:03:38+00:00"
words: 2455
preview_only: false
---

# Clouded Judgement 8.7.26 - Custom Tokens

Every week I’ll provide updates on the latest trends in cloud software companies. Follow along to stay up to date!

Custom Tokens

I strongly believe there will be 3, very large, markets that emerge in the “model / token” market:

-

Frontier tokens (ie from the large labs like OpenAI and Anthropic)

-

Vanilla open weight tokens (Deepseet, Moonshot, etc)

-

Customized (RL / SFT) open weight tokens

So much talk recently makes these seem zero sum… And of course, they do take share from each other. If open weight models never existed closed models would take it all! BUT - zero sum assumes the size of the pie is constant…which it isn’t. The market is growing much faster than any one group can steal market share from the other. So everyone grows! This won’t happen for ever. Eventually the market will mature and we’ll settle on a more “stable” market share. But for now (and for longer than people will expect), hypergrowth persists!

I wanted to talk a bit today about the third bucket - customized open weight tokens. It’s a very common theme to hear these days - take an open weight model, customize it for your data / workflows, and then serve that specific model instead of a more general purpose frontier model. The hope is you get a cheaper and more specialized model. In many cases this is true! And I believe it. However, it’s not nearly as easy as anyone thinks.

There are broadly 3 main ways to customize a model.

-

Custom pre- training (the heaviest lift). Training a model from scratch on your own data

-

SFT (Supervised Fine Tuning). You show the model examples of what “good” looks like (prompt + response, in basic terms), and the model learns to imitate it

-

RL (reinforcement learning). Instead of showing the model examples of what good looks like, you let it try the task, grade the answers, and then let it learn from which answers scored well

Most people stick to the second and third options. Someone much smarter than me described 3 main pillars of this (lots of “lists of 3” in this post…):

-

Training infrastructure. This is all of the compute and distributed training that’s needed to run a training job. This includes many things like orchestrating GPUs, sharding models across them, managing the sampling loops for RL, keeping GPU utilization high, shuttling updated model weights from trainers to samplers after each training step, etc. It’s HIGHLY complex and takes real distributed systems engineers to make it work. Tinker from Thinking Machines makes this seamless.

-

Data. Proprietary data is the reason you want to customize a model in the first place. BUT - the data doesn’t come “training ready.” Someone has to convert the raw data (this could be support transcripts, agent traces, logs, etc) into a format a model can actually learn from. Today, this burden largely falls on the customer. There are companies like Applied Compute or Trajectory that help out with this part of the workflow. Or Handshake / Mercor / Micro1 who source data and deliver it “training ready.” This part of the workflow is hard to “productize.” Every companies data is different and is messy in it’s own way. For SFT you can usually just convert data to a JSON file, but the hard part then is the judgement - deciding what “good data” looks like (and then filtering out the bad data). For RL there isn’t a standard data format, but more of a “environment plus reward function” settup, which is even more bespoke / customized (and thus hard to productize)

-

Evals. This is how you ultimately measure whether the customized model is actually good at the workflow / task you want it to complete. For RL specifically, evals happen at each step (this is the reward function grading each attempt, so the eval runs inside the training loop)

Then you have some version of a “training recipe” that sits across each of these 3 pillars. You can think of this as more of a blueprint for the whole job. How you manage and sequence each step, which training method you use (SFT or a version of RL like GRPO, PPO, DAPO, etc or a combo of both SFT and then RL), which base model you start from, how you design the reward function and the hyperparameters (learning rate, batch size, etc), etc. The training recipe is the design work that connects all of the steps of “customization.” There’s definitely a gap in the market here. There are different products (or more commonly services) that help at each of the three pillars I listed above, but not a lot of solutions that stich everything together. A big reason for this is it’s hard to “productize” all of this. It’s naturally more bespoke for each company, and thus a better fit for services.

I’m quite excited to see the innovation that will come from this field in the next few years.

One implied point I’m making - it sounds nice to talk about “customizing models” but it’s actually very difficult. And what I laid out above is only one part of the difficulty… There are two more challenges! How you then ultimately serve and deploy these models, and then how you upgrade them over time (upgrade on new base model, or upgrade with new data, etc)

On challenge number 1 - serving the model. IF you’re able to get through all the steps I outlined above, you now have a customized model! But so what? What do you do now? How do you get it serving production traffic? A lot of the training platforms I listed above aren’r inference platforms (at least not yet! I expect that to evolve..). Some of them (like Tinker) have a sampling API you can hit directly, but I think of this more as a “test” vs anything that can serve production traffic / scale. So you can then either spin up your own inference stack on top of something like vLLM (again, very hard to do yourself), or hand the model to someone like Baseten / Fireworks to serve it (this is what vast majority of folks do, and both Baseten / Fireworks are getting more and more into the RL / SFT stages as well). Good news is serving a customized model on one of these inference clouds isn’t that hard. Generally the customized model keeps the base model’s architecture (whatever open weight model you started with), so all of the inference optimizations those platforms built for those open weight models transfer over to your customized model. The “downside” (if you can call it that) are the economics. You pay a tax for someone else removing complexity for you. This next part I’m a little squishier on (so someone from Baseten / Fireworks please correct me if I’m wrong!), but when those platforms serve “vanilla” open weight models they get to share GPUs with thousands of customers at a time serving that same model. Utilization of those GPUs are high, so per token costs can be lower. For the custom models - it’s yours alone. There is no sharing of GPUs or spreading out the costs. You need dedicated GPUs (a parallel might be single tenant vs multi tenant SaaS deployments?) This is largely (again, I think) why customized models make sense for high volume, repetitive, specific tasks, where the model can be running constantly and you’re not implicitly paying for idle GPUs.

Then there’s challenge number 2 - upgrading your model. This is definitely an underrated challenge… A customized model is a point in time snapshot, but unfortunately there are two “upgrade” cycles running at the same time, The first is your data. Your business changes, your customers ask for new things, you build new products, etc. The model you a few months back becomes stale quickly. So someone needs to be doing all of the customization steps I discussed in the first half of this post consistently (collect data, re-train, re-eval, re-deploy, etc). There is no “one time” cost to customize a model, it’s very much a recurring cost and recurring complexity.

The second upgrade cycle is new base models. Open weight models are improving so fast. Kimi K3, GLM 5.2, Deepseek v4 Flash. Whether it’s a new open weight model, or the next version of an existing one, there are CONSTANTLY new base models coming out. This means that you’ll spend time, energy and expenses customizing a model, only to go through it all again (in very short windows) when the next best open weight model comes out and you want to customize from a “stronger” base. The frontier labs will tell you it’s not worth it. Why go through all of this pain consistently vs just buying frontier tokens direct?

There’s certainly a lot of product gaps to make open weight model customization more efficient. But I believe we’ll get there. Baseten / Fireworks / Together and other inference clouds are attacking this market from their inference starting point. Thinking Machines is attacking this market from the training infrastructure side. Applied Compute / Trajectory are more “pure play” RL shops. Handshake / Mercor / Micro1 are attacking it from the data side. Neoclouds like Coreweave are entering this space. Evals players like Braintrust and Vals.ai attacking it from the evals starting point.

All of this to say, there are a lot of people going after this opportunity, all from very different starting points. I have no doubt we will see some massive platform companies emerge here shortly!

Quarterly Reports Summary

Top 10 EV / NTM Revenue Multiples

Top 10 Weekly Share Price Movement

Update on Multiples

SaaS businesses are generally valued on a multiple of their revenue - in most cases the projected revenue for the next 12 months. Revenue multiples are a shorthand valuation framework. Given most software companies are not profitable, or not generating meaningful FCF, it’s the only metric to compare the entire industry against. Even a DCF is riddled with long term assumptions. The promise of SaaS is that growth in the early years leads to profits in the mature years. Multiples shown below are calculated by taking the Enterprise Value (market cap + debt - cash) / NTM revenue.

Overall Stats:

-

Overall Median: 4.1x

-

Top 5 Median: 31.8x

-

10Y: 4.7%

Bucketed by Growth. In the buckets below I consider high growth >22% projected NTM growth, mid growth 15%-22% and low growth <15%. I had to adjusted the cut off for “high growth.” If 22% feels a bit arbitrary, it’s because it is…I just picked a cutoff where there were ~10 companies that fit into the high growth bucket so the sample size was more statistically significant

-

High Growth Median: 19.3x

-

Mid Growth Median: 5.8x

-

Low Growth Median: 3.5x

EV / NTM Rev / NTM Growth

The below chart shows the EV / NTM revenue multiple divided by NTM consensus growth expectations. So a company trading at 20x NTM revenue that is projected to grow 100% would be trading at 0.2x. The goal of this graph is to show how relatively cheap / expensive each stock is relative to its growth expectations.

EV / NTM FCF

The line chart shows the median of all companies with a FCF multiple >0x and <100x. I created this subset to show companies where FCF is a relevant valuation metric.

Companies with negative NTM FCF are not listed on the chart

Scatter Plot of EV / NTM Rev Multiple vs NTM Rev Growth

How correlated is growth to valuation multiple?

Operating Metrics

-

Median NTM growth rate: 12%

-

Median LTM growth rate: 16%

-

Median Gross Margin: 76%

-

Median Operating Margin 3%

-

Median FCF Margin: 21%

-

Median Net Retention: 110%

-

Median CAC Payback: 35 months

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
