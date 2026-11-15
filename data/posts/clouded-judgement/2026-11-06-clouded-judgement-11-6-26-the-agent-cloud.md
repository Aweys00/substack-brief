---
title: "Clouded Judgement 11.6.26 - The Agent Cloud"
source: "Clouded Judgement (Jamin Ball)"
author: "Jamin Ball"
url: "https://cloudedjudgement.substack.com/p/clouded-judgement-11626-the-agent"
published: "2026-11-06T14:06:32+00:00"
words: 1644
preview_only: false
---

# Clouded Judgement 11.6.26 - The Agent Cloud

Every week I’ll provide updates on the latest trends in cloud software companies. Follow along to stay up to date!

The Agent Cloud

I think we’re starting to see the core pillars of “agent cloud infrastructure” emerge, and it’s starting to look a whole lot bigger than what traditional cloud infrastructure became.

If you started a SaaS company in the earlier days of the public cloud (say ~2012), the public cloud guys (AWS, Azure, GCP) probably sold you a pretty simple bundle. Some virtual servers (EC2), a place to put files (S3, ie storage), a managed database (RDS) and some kind of load balancer to spread traffic across your servers (and of course all the bells and whistles of autoscaling, backup, recover, etc). Later on as the cloud got more mature we got containers and services like Lambda, but the design center didn’t change that much - you had an application, serving lots of users, running 24/7. On top of this, the app tier was stateless so you could copy it, state go pushed down into the database, and in general things were optimized for throughput and utilization. You’d rent a box, and the box ran your code, and a lot of it existed to squeeze more human requests through fewer machines. So in essence the core cloud stack was:

-

Virtual servers (EC2)

-

File storage (S3)

-

Managed Database (RDS)

-

Load balancer

Now, however, agents have flipped and evolved the needs of classic cloud infrastructure. A new “agent cloud infrastructure” is emerging. The simple way I can try and describe this shift - the old cloud was built with the intention of allowing one app to serve millions of people. The agent cloud has to let millions of agents each run their own little app (and the type of workload is very diverse). Sometimes these little apps run for a few seconds, or a few days, or anything in-between. On top of this, each app needs its own machine rather than a piece of a broader machine (because the code that is being run was written by a model a few seconds ago most likely). Every one needs to store it’s state, remember where it left off so it can start / stop, etc. And the workloads are unpredictable and arrive in bursts! Jensen framed it well at the Vera launch earlier this year when he said the old CPUs were designed around lots of rentable cores, but an agent doesn’t want to rent a core, it wants the task finished quickly. Earlier I mentioned cloud infra workloads were more about optimizing utilization / throughput per app. Now for agent cloud infra what’s being optimized for is isolation, memory and clod start times, etc. Now the agent cloud stack is starting to look like:

-

Sandboxes: This is the new virtual server. They are disposable, isolated computers per agent task

-

Persistent state: This is the new file storage. A filesystem that lives longer than the individual task so agents can pause, snapshot, fork, etc. Shoutout to Tigris who was acquired this week by Dropbox!

-

Inference: The obvious one! Inference clouds like Baseten / Fireworks / Modal are taking off.

-

Router / Gateway: This is the new load balancer. Instead of spreading traffic across identical servers (ie the cloud infra stack pillar) you now want to spread workloads across different models.

-

RL and training loops. Infra to turn open weight models into customized ones. You need environments and evals and many other services.

-

CPUs, storage and network underneath. Boring stuff, but still needed! And need in a much bigger way than what was needed in more simple cloud infra

These are just the initial core pillars. There’s also another ring of agent cloud infra forming around this. Workflows / durable execution, browser infrastructure so agentc can use the web, CI/CD and test compute for all of the code that is written, new git backends that can store petabytes per day (shoutout Pierre Computer Company on their acquisition by OpenAI), identity and payent rails, all of the classic observability but now an order of magnitude greater given all the metric data agents spit off, memory stores, etc.

Net net - I think all of this agent cloud infra ends up dwarfing the size of classic cloud infra (and when I say classic cloud infra I’m referring more towards cloud application infra). The first cloud was compute / network / storage for applications humans were running. But the new cloud has the same core primitives , but rebuilt for agents, with a lot more underlying units.

I’m very excited to see how agent cloud infra evolves over the next 12 months - I think we’re due for an explosion!

Quarterly Reports Summary

Top 10 EV / NTM Revenue Multiples

Top 10 Weekly Share Price Movement

Update on Multiples

SaaS businesses are generally valued on a multiple of their revenue - in most cases the projected revenue for the next 12 months. Revenue multiples are a shorthand valuation framework. Given most software companies are not profitable, or not generating meaningful FCF, it’s the only metric to compare the entire industry against. Even a DCF is riddled with long term assumptions. The promise of SaaS is that growth in the early years leads to profits in the mature years. Multiples shown below are calculated by taking the Enterprise Value (market cap + debt - cash) / NTM revenue.

Overall Stats:

-

Overall Median: 4.5x

-

Top 5 Median: 25.2x

-

10Y: 4.8%

Bucketed by Growth. In the buckets below I consider high growth >22% projected NTM growth, mid growth 15%-22% and low growth <15%. I had to adjusted the cut off for “high growth.” If 22% feels a bit arbitrary, it’s because it is…I just picked a cutoff where there were ~10 companies that fit into the high growth bucket so the sample size was more statistically significant

-

High Growth Median: 15.9x

-

Mid Growth Median: 5.6x

-

Low Growth Median: 3.8x

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

Median LTM growth rate: 17%

-

Median Gross Margin: 76%

-

Median Operating Margin 4%

-

Median FCF Margin: 21%

-

Median Net Retention: 109%

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
