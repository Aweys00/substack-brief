---
title: "Clouded Judgement 10.9.26 - Cache Is the New Egress"
source: "Clouded Judgement (Jamin Ball)"
author: "Jamin Ball"
url: "https://cloudedjudgement.substack.com/p/clouded-judgement-10926-cache-is"
published: "2026-10-09T13:04:50+00:00"
words: 1572
preview_only: false
---

# Clouded Judgement 10.9.26 - Cache Is the New Egress

Every week I’ll provide updates on the latest trends in cloud software companies. Follow along to stay up to date!

Highlight of the Week - Cache Is the New Egress

In the early days of the cloud era, when dissecting costs most people just looked at the basic price of compute and storage (for services like EC2 and S3). Overtime, the real focus shifted to egress. In today’s AI world, the initial focus is on the input/output pricing per 1M tokens, but the real focus is on the cache read rate. What is the cache read rate? The cache read rate is what a model provider charges to essentially re-reat input tokens it processed / stored from a prior call. If you think about an agent loop with the same system prompt, same tool definitions, etc, all of this history / context doesn’t need to be resent and reprocessed every time (and this turns out to be a majority of input tokens).

Here’s some data on the headline prices everyone looks at (just a blended input/ouput of the vanilla pricing). I use 80/20 input / output ratio because that’s a reasonable approximation of a normal chat workload.

As you can see above, Astra / Fable (those are thought of as the true frontier) both price at $10 / 1m input tokens and $50 / 1m output tokens (blended to $18). Another takeaway is a “mid tier” has emerged in the $2 / $10 range (~$4 blended). And again, this chart is just the vanilla pricing.

In the next chart below I try to look at a more reasonable workload - a 40 turn agent session with a 85% cache hit. The order doesn’t really change, but a couple call outs. Fable comes in ~16% under the Astra pricing (when vanilla list is the same). Grok 4.7 is the cheapest flagship model on vanilla pricing, but is more expensive than Sol and Terra (xAI charges $0.50 per cached token while OpenAI charges $0.10)

How I interpret these two charts - all the model providers are running a price war on the acquisition price, when in reality they’re actually competing on the retention price (and gives us a peak at what the models may be more optimized for). The vanilla list price will attract users, top of funnel, etc. Cache hit price is what actually gent’s spend. Astra, for instance, is $1 per million cached tokens. That feels more priced for chat. Fable at $0.25 is more for agents. Luna at $0.01 is priced to run in a loop.

So bringing this all back to the egress analogy. Egress really mattered because it created real switching costs. Your data lived in one cloud, and moving it out was EXPENSIVE. A cache is kind of similar. Swapping out models mid session means building that cache over again. Now, the natural push back is “well who’s switching models mid session…” Fair, but an entire category was built on just this! Model routers have the pitch of “send every call to the cheapest model that can handle the task appropriately.” Just looking at the vanilla pricing - that’s smart! But under cache pricing this can become a trap - because the cache is keyed to one model / one provider. So every model switch is a “full vanilla price re-read” of the whole context. Looking at the 40-turn agent session I talked about earlier - All on Fable at a 95% cache hit rate: ~$4.90. But if you keep alternating turns between Fable and Sol (which btw is 1/5 the vanilla price), and you get to $18! Routing to the cheaper model ends up costing ~4x than not routing and hitting the cache. Per-call multiplexing is probably dead for agents, as routing only really makes sense at the session level. So there is some switching costs built in here…Take it one step further…

…I also deeply believe the future is very long running agents. Or agents that are perpetually running in a loop (think AI employees just continuously doing their job running 24x7). Then the context and the cost and all the cached info starts to really matter! This may be too far-fetched of a conclusion to draw, but I think there is a world where lock in emerges from the cache-hit pricing as agents start running longer and longer.

Top 10 EV / NTM Revenue Multiples

Top 10 Weekly Share Price Movement

Update on Multiples

SaaS businesses are generally valued on a multiple of their revenue - in most cases the projected revenue for the next 12 months. Revenue multiples are a shorthand valuation framework. Given most software companies are not profitable, or not generating meaningful FCF, it’s the only metric to compare the entire industry against. Even a DCF is riddled with long term assumptions. The promise of SaaS is that growth in the early years leads to profits in the mature years. Multiples shown below are calculated by taking the Enterprise Value (market cap + debt - cash) / NTM revenue.

Overall Stats:

-

Overall Median: 4.3x

-

Top 5 Median: 37.3x

-

10Y: 5.2%

Bucketed by Growth. In the buckets below I consider high growth >22% projected NTM growth, mid growth 15%-22% and low growth <15%. I had to adjusted the cut off for “high growth.” If 22% feels a bit arbitrary, it’s because it is…I just picked a cutoff where there were ~10 companies that fit into the high growth bucket so the sample size was more statistically significant

-

High Growth Median: 19.3x

-

Mid Growth Median: 7.0x

-

Low Growth Median: 3.4x

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
