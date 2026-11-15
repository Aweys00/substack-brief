---
title: "Clouded Judgement 8.14.26 - Useful Life"
source: "Clouded Judgement (Jamin Ball)"
author: "Jamin Ball"
url: "https://cloudedjudgement.substack.com/p/clouded-judgement-81426-useful-life"
published: "2026-08-14T13:05:29+00:00"
words: 1412
preview_only: false
---

# Clouded Judgement 8.14.26 - Useful Life

Every week I’ll provide updates on the latest trends in cloud software companies. Follow along to stay up to date!

Useful Life

A few weeks ago I wrote an article “[The Second Life of a GPU](https://cloudedjudgement.substack.com/p/clouded-judgement-52926-the-second).” In that post I discussed a (hypothetical) scenario where GPUs retained value past their (presumed) 4-5 year useful life. What impacts would this have on clouds / neoclouds or the broader compute complex? Could compute contracts be “re-contracted” after their useful life? All some version of the same question - is the useful life of these chips actually much longer than 4-5 years.

Well, this week on Coreweave’s earnins call we got a great nugget related to this.

“What we are seeing today is that the upside of recontracting is real as we remain largely sold out of prior generations of NVIDIA GPUs in addition to the current SKUs. So as our earlier generation fleets roll off their original contract, they offer the potential to deliver strong returns in the subsequent years. We are seeing this across our Ampere and Hopper fleet.

As an example, we recently signed an A100 contract that extends into 2029 at an attractive price. As a reminder, this SKU was introduced in 2020. Clusters of prior generations of architecture of our installed, energized production-grade compute already running at scale. They come with a proven ROI for customers.”

Then Jensen tweeted this:

Of course, both Coreweave and Nvidia have a vested interested in the useful life of chips elongating. However - I believe them. And we now have some concrete data to demonstrate these chips do have a useful life that (for now!) extends to 9 (and maybe more) years.

One one hand you can say this is just representative of the current moment we’re in. Compute constraints still exist everywhere, so why not take any form of compute, regardless of how old it is. While true, you still wouldn’t sign a contract for an A100 chip if you thought it was worthless. And for someone like Coreweave a recontracting deal like this is (probably) meaningfully profitable. The initial purchase (ie debt used to fund the purchase) probably was amortized over the useful life of the chip. My guess is that debt is now fully paid off, and incremental revenue from the re-contracting comes without a heavy financing (interest) cost.

I really believe we’ll see more and more of this - chips contracting well beyond their useful life. One reason - the types of inference requests will continue to spread out in complexity. We’ll start seeing the most complex inference workloads become even more complex. And these probably require the latest generation of chips. However, the long tail will also grow. And some of these requests will be incredibly trivial. Those won’t require the latest and greatest. There will be a lot of value created in a software layer that can understand the request coming in and route to the right chip in real time.

Another reason - I continue to believe that the “compute constraints” will last much much longer than people think. So far, the risk has repeatedly been to the upside!

Here’s an analogy I like. The market has been pricing GPUs like a melting ice cube. Turns out, they may have a freezer! And that freezer is an exponentially growing curve of inference (and heterogeneity of inference requests)

Quarterly Reports Summary

Top 10 EV / NTM Revenue Multiples

Top 10 Weekly Share Price Movement

Update on Multiples

SaaS businesses are generally valued on a multiple of their revenue - in most cases the projected revenue for the next 12 months. Revenue multiples are a shorthand valuation framework. Given most software companies are not profitable, or not generating meaningful FCF, it’s the only metric to compare the entire industry against. Even a DCF is riddled with long term assumptions. The promise of SaaS is that growth in the early years leads to profits in the mature years. Multiples shown below are calculated by taking the Enterprise Value (market cap + debt - cash) / NTM revenue.

Overall Stats:

-

Overall Median: 4.4x

-

Top 5 Median: 36.1x

-

10Y: 4.6%

Bucketed by Growth. In the buckets below I consider high growth >22% projected NTM growth, mid growth 15%-22% and low growth <15%. I had to adjusted the cut off for “high growth.” If 22% feels a bit arbitrary, it’s because it is…I just picked a cutoff where there were ~10 companies that fit into the high growth bucket so the sample size was more statistically significant

-

High Growth Median: 18.1x

-

Mid Growth Median: 6.7x

-

Low Growth Median: 4.0x

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

Median Operating Margin 3%

-

Median FCF Margin: 20%

-

Median Net Retention: 110%

-

Median CAC Payback: 36 months

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
