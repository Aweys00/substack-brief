---
title: "Clouded Judgement 7.10.26 - Own Your Weights"
source: "Clouded Judgement (Jamin Ball)"
author: "Jamin Ball"
url: "https://cloudedjudgement.substack.com/p/clouded-judgement-71026-own-your"
published: "2026-07-10T13:04:29+00:00"
words: 2153
preview_only: false
---

# Clouded Judgement 7.10.26 - Own Your Weights

Every week I’ll provide updates on the latest trends in cloud software companies. Follow along to stay up to date!

Own Your Weights

Alex Karp had a pretty spicy [segment](https://x.com/MikeLongTerm/status/2072301831619817488) on CNBC last week talking about a lot of things (many of which took shots at the large AI labs). The part I want to focus on today was the concept he talked about of “owning your weights.” In summary: should enterprises “own” their models or rent them (ie buy from a large lab). Should you own your weights to give yourself more control, better cost management, maybe even better performance with with RL’s models, and ultimately remove a single point of failure (or reliance). This could come in the form of developing your own models, or RL’ing open weights models on your specific workflows / data. There’s a future version of this post that will focus more on “owning your harness” vs “renting a harness” from the large labs, but I’ll save that one for another time. At the end of the day enterprises want control.

The catch on the debate of “owning your weights” - a weight file is a melting ice cube that quickly becomes outdated. Taking ownership of model weights really just buys you a snapshot, or a frozen point-in-time artifact of the model. The quality of what you own doesn’t degrade in absolutes, but it does degrade in relative terms. The frontier models get better, the goalposts move, and what you have quickly becomes outdated. What you really want is not just a snapshot, but the training and RL pipeline engine to consistently improve, tweak, update, refine, evaluate and THEN own the weights of that assembly line output. So the broader point I want to make here is it’s not just the weights you want to own, but the data flywheel, RL infra and eval harness engine that creates the weights.

Saying this differently - the naive interpretation of “owning your weights” is simply grabbing an open weights model (like a GLM 5.2), deploying it, declaring model sovereignty, and calling it a day. I don’t think that will get folks as far as they’d like.

I do think RL starts to change the game, and I do expect to frontier labs to get more into this game. The frontier labs train on EVERYTHING. The training set these frontier labs trained on doesn’t include a companies specific workflows, edge cases, business definitions, KPIs, etc. If you take an open model and RL it against your actual workflows ( in your environments, with your reward signals, on top of your data topology, etc) you’re not just holding a static snapshot anymore. You have a “personalized” model, but also an engine to continue to “personalize.” And what I keep observing - a task-specific model tuned like this can a) beat a frontier model at the one thing it was trained for (ie have better performance), and b) come at a fraction of the inference cost (usually because it’s a smaller model). The frontier model is more of a generalist model carrying ALL weights. Your model only needs to do ONE job and be good and cost effective at it. The downside is you may pay a complexity task. Play this out, and any given enterprise could have thousands of smaller fine tuned models funning around that need to be governed, version controlled, audited, secured, etc. Someone is going to make a fortune playing that role for enterprises.

So back to what I said earlier - what people really mean when they say “own your weights” is so much more than owning the weights. It’s owning the engine and loop that builds the weights. So the real question for enterprises isn’t “frontier or open source.” It’s “which of my workloads justify building a loop?”

But of course, there are tradeoffs! Building these engines and loops requires a lot of technical expertise. Today there are two main options:

-

Use the frontier for everything. You have one (or a small number of model providers), require zero internal ML team, and you ride the capability curve for free - every time Anthropic or OpenAI ships, your product gets better and you did nothing. This will actually be quite appealing to many who don’t have the resources to do anything but this. But you’re probably going to pay a lot more (you’re a price taker with a single vendor), and you have a single dependency.

-

Own your weights and RL a fleet of smaller models. You can get task-specific models that are typically cheaper, have lower latency, and don’t come with a single point of failure (or dependency)...but you’re going to be running a larger internal ML org. And every frontier release resets the bar you have to beat to justify all of those internal resources you set up. It’s now a race! Can your loop compound faster than the frontier improves on your specific task?

For most tasks (most of the time) the answer is the complexity tax of owning your weights becomes too high (especially over time, this complexity tax compounds)... Which is why there’s generally a gap between what the headlines say and what enterprises actually do (some of that is because the headlines focus more on the bleeding edge enterprises). Everyone loves the idea of ownership and having model sovereignty. BUT - The spend data says enterprises keep writing bigger checks to the frontier labs every quarter. It’s a classic stated preference vs revealed preference conundrum. Most companies don’t have any kind of foundation of infrastructure or talent to run these loops.

What I get excited about is companies that can help close this gap. Take companies who don’t have the engineering resources, and give them tools to own their weights. Again, not just own a model, but own the engine to continually build / fine tune the weights.

Maybe it’s a new startup who does this, or maybe it’s someone like Databricks. Databricks has models, but not frontier models that compete with the latest OpenAI / Anthropic models. Someone who makes the bet that the durable asset here isn’t the model itself but the engine around it. The pitch for anyone here is pretty simple: bring your workload, we’ll help you build a task-specific model on your data, tuned to your tasks, running on infrastructure you control. You get the cost and control benefits of “owning your weights” without having the huge complexity cost and tax.

Now - This doesn’t mean at all that “Ah! The big labs are dead!” Quite the opposite… There will be a difference between who generates the most tokens and who generates the most revenue. There will ALWAYS be a meaningful portion of tasks that require frontier tokens. And those tasks / tokens will be the most expensive. So I think you could see a clear future where the percent of tokens generates really starts to skew open weights, but the closed weight models continue to generate more and mroe revenue as a) the size of the pie grows, and b) their share of “expensive” workloads grows and grows. I still believe the frontier will win huge amounts of revenue. The hard stuff, the reasoning-heavy work, the tasks still riding the capability curve - plus every company that can’t or won’t build the loop - that spend stays with the labs (AND comes with a lot of pricing power).

So should you own your weights? Not entirely the right question. The real question is should you own a loop - and for which tasks?

A follow up in the future I want to write about - simply “codifying” a workflow for a model to learn from is no easy task! I brushed this off in this post as something simple, but it’s far from simple to do.

Top 10 EV / NTM Revenue Multiples

Top 10 Weekly Share Price Movement

Update on Multiples

SaaS businesses are generally valued on a multiple of their revenue - in most cases the projected revenue for the next 12 months. Revenue multiples are a shorthand valuation framework. Given most software companies are not profitable, or not generating meaningful FCF, it’s the only metric to compare the entire industry against. Even a DCF is riddled with long term assumptions. The promise of SaaS is that growth in the early years leads to profits in the mature years. Multiples shown below are calculated by taking the Enterprise Value (market cap + debt - cash) / NTM revenue.

Overall Stats:

-

Overall Median: 3.5x

-

Top 5 Median: 31.8x

-

10Y: 4.6%

Bucketed by Growth. In the buckets below I consider high growth >22% projected NTM growth, mid growth 15%-22% and low growth <15%. I had to adjusted the cut off for “high growth.” If 22% feels a bit arbitrary, it’s because it is…I just picked a cutoff where there were ~10 companies that fit into the high growth bucket so the sample size was more statistically significant

-

High Growth Median: 20.3x

-

Mid Growth Median: 5.4x

-

Low Growth Median: 2.8x

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

Median Operating Margin 2%

-

Median FCF Margin: 21%

-

Median Net Retention: 110%

-

Median CAC Payback: 44 months

-

Median S&M % Revenue: 34%

-

Median R&D % Revenue: 23%

-

Median G&A % Revenue: 13%

Comps Output

Rule of 40 shows rev growth + FCF margin (both LTM and NTM for growth + margins). FCF calculated as Cash Flow from Operations - Capital Expenditures

GM Adjusted Payback is calculated as: (Previous Q S&M) / (Net New ARR in Q x Gross Margin) x 12. It shows the number of months it takes for a SaaS business to pay back its fully burdened CAC on a gross profit basis. Most public companies don’t report net new ARR, so I’m taking an implied ARR metric (quarterly subscription revenue x 4). Net new ARR is simply the ARR of the current quarter, minus the ARR of the previous quarter. Companies that do not disclose subscription rev have been left out of the analysis and are listed as NA.

Sources used in this post include Bloomberg, Pitchbook and company filings

The information presented in this newsletter is the opinion of the author and does not necessarily reflect the view of any other person or entity, including Altimeter Capital Management, LP (”Altimeter”). The information provided is believed to be from reliable sources but no liability is accepted for any inaccuracies. This is for information purposes and should not be construed as an investment recommendation. Past performance is no guarantee of future performance. Altimeter is an investment adviser registered with the U.S. Securities and Exchange Commission. Registration does not imply a certain level of skill or training. Altimeter and its clients trade in public securities and have made and/or may make investments in or investment decisions relating to the companies referenced herein. The views expressed herein are those of the author and not of Altimeter or its clients, which reserve the right to make investment decisions or engage in trading activity that would be (or could be construed as) consistent and/or inconsistent with the views expressed herein.

This post and the information presented are intended for informational purposes only. The views expressed herein are the author’s alone and do not constitute an offer to sell, or a recommendation to purchase, or a solicitation of an offer to buy, any security, nor a recommendation for any investment product or service. While certain information contained herein has been obtained from sources believed to be reliable, neither the author nor any of his employers or their affiliates have independently verified this information, and its accuracy and completeness cannot be guaranteed. Accordingly, no representation or warranty, express or implied, is made as to, and no reliance should be placed on, the fairness, accuracy, timeliness or completeness of this information. The author and all employers and their affiliated persons assume no liability for this information and no obligation to update the information or analysis contained herein in the future.
