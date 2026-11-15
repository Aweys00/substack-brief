---
title: "Clouded Judgement - 8.28.26 - Zero Data Retention"
source: "Clouded Judgement (Jamin Ball)"
author: "Jamin Ball"
url: "https://cloudedjudgement.substack.com/p/clouded-judgement-82826-zero-data"
published: "2026-08-28T13:13:44+00:00"
words: 2181
preview_only: false
---

# Clouded Judgement - 8.28.26 - Zero Data Retention

Every week I’ll provide updates on the latest trends in cloud software companies. Follow along to stay up to date!

Zero Data Retention

FT recently dropped [an article](https://www.ft.com/content/5ee49718-c258-4f01-aa32-7e5b76ae5245?syn-25a6b1a6=1) showing the spend split between different Anthropic models (indexed back to June). What was interesting about this chart (below) was that the recent growth across July wasn’t driven by Fable, but by Opus 5.

Many people asked questions about this. Why isn’t Fable 5 driving more adoption? [Martin](https://x.com/martin_casado) threw out a tweet that listed a number of potential rationales (I won’t summarize all of them, tweet is pasted below).

The overwhelming response to the question of “why has Fable 5 seen more lackluster adoption” was zero data retention (or ZDR). This topic has been front and center this summer. OpenAI wrote a [blog post](https://openai.com/index/offering-zero-data-retention-for-frontier-models/) about it a few weeks ago. In my opinion, it’s becoming increasingly clear that users have a preference when it comes to data retention policies, and if you believe the majority of responses to Martin’s tweet, the labs have some decisions to make!

So what is Zero Data Retention? Typically, the standard API terms of service / arrangements has been the same for the last few years. The prompts / responses are held for some period of time (~30 days) to monitor for abuse. Abuse could be something like is the model used for hacking, or some other harmful intent. The labs want to know if the models were used this way so they could either do something about it, or use it as forensic evidence.

Of course, there are some models / customer contracts where nothing persists after the response is generated. No logs, no traces, no review queue. Nothing to leak, nothing for an employee to spy on, nothing for someone who steals employees credentials to see, nothing to subpoena, etc. Quick flag- zero doesn’t literally mean zero. Safety flags still exist even in this case (ie data that is flagged as harmful can be stored for much longer, but unflagged deleted immediately).

One distinction on this entire topic is policy vs architecture. A 30 day deletion policy in many ways is a “promise” (ie a policy). ZDR is more of an architecture. Policies / promises can be amended, terms of service can be updated, breaches can render it all irrelevant, etc. Architecture, on the other hand, has none of that. You can’t retroactively amend it. And we’ve seen a practical example demonstrating the policy vs architecture issue. In May 2025 a federal judge ordered OpenAI to preserve a lot of logs (I believe output logs). This included chats users had deleted. This was part of the New York Times copyright case. All of a sudden, the policy of “we delete after 30 days” became “we delete after 30 days unless someone says otherwise” (in this case the someone was a federal judge). For ZDR customers? There was nothing this judge’s order could do. There was nothing for OpenAI to preserve (for ZDR customers) because that data was deleted (architecturally) from the get go.

Ok circling back to Fable 5. When Anthropic launched it this summer (in June), they launched it with a 30 day retention policy - basically a 30 day retention of every prompt and output. AND everywhere the model is offered (their API, Bedrock, Foundry, Copilot, coding tools, etc). No ZDR exceptions, and existing ZDR agreements specifically did not apply to Fable 5 traffic. It’s easy to read that and think “huh, why, that seems weird.” But it’s actually reflects a very consistent viewpoint Anthropic has (which I don’t necessarily think is wrong!). The Fable series of models is by far the most capable model class ever created. And because it’s so powerful, it can be used in quite negative ways (cyber attacks, bio, etc). Anthropic would say the most serious misuse patterns only become visible (and thus truly block-able) when you can correlate across many interactions. On top of that, you can’t investigate something you never stored in the first place. If you take catastrophic risk seriously (which Anthropic clearly does), this data retention policy makes sense.

However, the rest of the market quickly reacted to this. Microsoft reportedly restricted its employees from using Fable 5. GitHub disabled it by default in CoPilot. And back to the chart (and tweet) I mentioned at the beginning of this post, the ramp data suggests the rest of the market did the same thing - routed traffic away from Fable 5. Of course, the rationale for the lower Fable 5 adoption is just a hypothesis. The cost of Fable 5 (relative to their other models or competing models) is clearly also a consideration for customers. Fable 5 is expensive, at $10 per million input tokens, roughly double GPT-5.6. Most workloads don't necessarily need the frontier (I've written before about the token bifurcation - the majority of tokens may flow to cheap, good-enough models while a thin slice of frontier tokens drives a majority the revenue). Opus 5 at half the price of Fable 5 always had the potential to cannibalize Fable.

However, the cost-only explanation (for the “lackluster” Fable 5 adoption) has some holes in it. Frontier models often complete the task in fewer tokens and fewer attempts. They’re more token efficient - expensive per token doesn’t mean the same thing as expensive per task (or per output). I do think (and hear very similarly) that the lower than expected usage of Fable 5 was more about the data retention policy (and remember, policy is different from architecture!). Ramp's own economist told the FT the retention requirement was a drag on adoption (in addition to price).

In the OpenAI piece I mentioned earlier, [Offering Zero Data Retention for Frontier Models](https://openai.com/index/offering-zero-data-retention-for-frontier-models/), they previewed something called Private Safety Processing. Customers can keep their data on infrastructure that they control (or sits encrypted under keys only the customer holds), and OpenAI runs automated misuse classifiers that scans for misuse patterns. OpenAI only receives an alert category and severity (not the actual data / prompt / response). I do think there’s some signal here. It’s not common to see a big launch-style blog post about retention policies…unless those policies are driving (or pushing away!) revenue. This is definitely a important topic, that will only become more important as the models get more capable.

So what does this all mean? Couple things come to mind. For one, the data flywheel inverted a bit. Some of the highest-value customers are now saying they’ll pay extra specifically to have their data “forgotten.” (so labs can’t learn from this to improve their products). The new improvement loop gets built from purpose-built data (RL environments, evals, opt-in partnerships), not from the data the customers spit out. Now the asset is that RL factory, not just the data traces.

One interesting thing for founders - your retention posture is now (in some ways) inherited from your vendor’s retention policies. “What does your model provider retain, and for how long?” is something I’d expect to show up on just about every security questionnaire you fill out. Companies using these models will want to get ZDR passthrough into your own contracts so you can pass that on. If not, architect for model portability, OR you’ll have to build that trust infrastructure yourself. There will definitely be demand for confidential inference, customer-held keys, audit tooling for AI traffic, etc.

For the labs: unilateral retention is appearing like a tax customers just aren’t willing to pay. Safety-through-retention either is something that starts to become an industry-wide standard, or it gets rebuilt cryptographically so retention isn’t required at all. My bet is the latter...

Two things I’ll end with. 1) the CISO is starting to become a lot more important constituent in the buying process. 2) For many years a strong pitch in software was “your data makes our product better.” The strongest pitch in AI might turn out to be something entirely different: “we never saw your data at all.”

Quarterly Reports Summary

Top 10 EV / NTM Revenue Multiples

Top 10 Weekly Share Price Movement

Update on Multiples

SaaS businesses are generally valued on a multiple of their revenue - in most cases the projected revenue for the next 12 months. Revenue multiples are a shorthand valuation framework. Given most software companies are not profitable, or not generating meaningful FCF, it’s the only metric to compare the entire industry against. Even a DCF is riddled with long term assumptions. The promise of SaaS is that growth in the early years leads to profits in the mature years. Multiples shown below are calculated by taking the Enterprise Value (market cap + debt - cash) / NTM revenue.

Overall Stats:

-

Overall Median: 4.4x

-

Top 5 Median: 32.7x

-

10Y: 4.7%

Bucketed by Growth. In the buckets below I consider high growth >22% projected NTM growth, mid growth 15%-22% and low growth <15%. I had to adjusted the cut off for “high growth.” If 22% feels a bit arbitrary, it’s because it is…I just picked a cutoff where there were ~10 companies that fit into the high growth bucket so the sample size was more statistically significant

-

High Growth Median: 17.3x

-

Mid Growth Median: 7.6x

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
