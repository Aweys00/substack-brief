---
title: "Intel: Why Didn’t We See This Coming?"
source: "Vik's Newsletter"
author: "Vikram Sekar"
url: "https://www.viksnewsletter.com/p/intel-why-didnt-we-see-this-coming"
published: "2026-11-04T09:32:33+00:00"
words: 1307
preview_only: true
---

# Intel: Why Didn’t We See This Coming?

A lot of people had faith in Intel’s turnaround story. Investors trusted that Lip-Bu Tan would turn this ship around and re-write the future of Intel. However, recent management commentary indicated that is not happening yet. At least not for another year.

Intel’s stock ~30% at close wiping out nearly $140B in market value — its worst collapse in its entire history. It is down 57% from its all-time high.

There has been plenty of commentary around the earnings call which we will not repeat here. I suggest you listen to the [whole earnings call](https://www.google.com/finance/quote/INTC:NASDAQ?tab=earnings). Intel did post good earnings results in Q3 and even beat expectations. What dropped the stock was the story that came after — about what Q4’26 and Q1’27 and beyond would look like.

Here, we will ask the question: Why didn’t we see this coming? A post-mortem analysis often provides valuable insights and learnings on the AI trade, and in this case, it is a particularly expensive lesson.

In this post, I’ll first present the causes of INTC stock death from what was said at the Q3 earnings call, and then present some clues from the Q2 earnings call that were tell-tale signs which we missed. The idea is not to be an Intel bull or bear but instead turn failures into teaching moments that we can carry forward into the future.

By reading this post, you agree to the [terms and conditions](https://www.viksnewsletter.com/p/terms-and-conditions). Also see the [full ethics statement](https://www.viksnewsletter.com/p/ethics).

I analyze the tech and business around AI semiconductors. Sign up below, or upgrade to access over 200+ articles written over the course of the greatest semi buildout ever. You can expense the subscription too!

Check out the [Semi Doped podcast](https://www.viksnewsletter.com/about#§semi-doped-podcast), and [our daily free newsletter](https://daily.semidoped.com/) with latest semi news. For institutional research, contact me at [SemiExponent](https://www.viksnewsletter.com/about#§semiexponent).

#### Causes of Death

Any good post-mortem requires a cause of death. Intel provided three:

1. PC market decelerating rapidly

High memory prices and limited availability were making PCs expensive and straining IT budgets. Simply put, too many customers decided to not upgrade due to high system cost. On the Q3 call, the Intel CFO David Zinsner quantified this: client and edge revenue would fall more than 20% sequentially in Q4.

2. Server CPU supply did not meet demand

Client PC market wouldn’t matter if Intel could make it up by selling more server CPUs. Intel could just redirect wafers allocated to client CPUs, which had weak demand, to server CPUs which were in high demand. Simple right? No.

LBT explained that shortages of substrates used in EMIB packaging did not allow Intel to ship as many server CPUs as they expected. LBT said that he is demanding substantial execution from the team to improve Intel 3 yield and cycle times.

3. A tragic accident shut down the Israel factory

On Oct 14, 2026, the explosion of a gas cylinder at Intel Fab 28 in Kiryat Gat, Israel, killed two people and injured a third. The manufacturing plant was shut down for two weeks impacting revenue by $300M in the upcoming Q4’26, and a further $300M or more in Q1’27. The estimated financial impact on Q4 gross margins was anticipated to be 2%.

The real impact is that two people actually died. That is a truly tragic event and matters much more than financial calculations around Intel earnings.

All three of these events have a teaching moment within them, and reveals our blind spots when it comes to this industry. Let’s start with how Stacy Rasgon, analyst at Bernstein Research, sniffed out the PC market problem early.

#### Detective Rasgon Smells a Rat

Earlier this year, Intel renamed their client PC segment to “Client Computing and Physical-AI Group” (CCPG) possibly in an effort to bolster the declining PC market with robot AI in the future. They have embraced a Qualcomm-esqe “AI at the edge” story, but I digress. The Q&A at every earnings call this year had giveaways to what was coming, that only because clearer in hindsight.

The point is that in Q2, Zinsner reported that CCPG revenue was up 15% sequentially and better than Intel’s expectations. Here is the exact quote:

“CCPG revenue was $8.9 billion, up 15% sequentially and better than our expectations. The client TAM continued to hold up well despite broad component constraints and price inflation. Our AI PC revenue grew 26% sequentially and now represents 2/3 of our client revenue mix.”

David Zinsner, CFO, Intel Q2 Earnings Call.

While most other analysts were laser focused on CapEx, foundry customers, and server CPU competition from ARM and AMD, Rasgon hit the nail on the head. Here’s the question (emphasis mine):

“I wanted to ask about clients. I think everybody kind of had an inkling that data center was going to be pretty strong. I was surprised at the client strength. And I know you talked about demand holding up pretty well. I know you’re ramping Panther on some of the new products.

But I guess, was it all pricing that drove that revenue strength? Or was there something else going on? And I guess, if you could maybe comment on what your expectations are for client in the second half relative to an end market that sounds like it’s going to be worse than typical as we move into Q3 and Q4.”

Stacy Rasgon, Bernstein Research, Intel Q2 Earnings Call.

Rasgon saw that the client strength did not have demand, yet Intel is reporting 15% sequential growth. The only reason should be that Intel is charging more. Rasgon noted that things are going to get worse in the second half of the year and asks what Intel’s expectation is.

I won’t post Zinsner’s entire response here, but he essentially said:

-

Yes, client revenue was largely ASP driven. Intel saw that high memory cost is causing price inflation and passed that on to customers.

-

CPU sales is tight — aka, nobody is buying at this price, and that the market will go soft in Q4.

This is an instance of the right question extracting exactly what we need to hear — that the PC market is going to go soft, and it did. In the Q3 call, Zinsner said that PC unit TAM in 2026 is set to decline 12%, just H2 units down more than 20%. 2027 is going to decline another 10%, with it supposedly getting better in H2 2027.

Rasgon continues to hammer on the client segment recovery in the Q3 call. He asks Zinsner:

It sounds like you think things get better in the second half as, I suppose, memory supply [sic]. What gives you confidence that memory supply is actually going to improve? If you listen to memory guys, they seem to be suggesting that it won't.

Stacy Rasgon, Bernstein Research, Intel Q3 Earnings Call.

Another headshot. Zinsner waffles about a bit, and then lays it straight. This time, I’ll post the quote so we don’t miss anything by paraphrasing.

But make no mistake, we are not optimistic about next year in terms of memory. We think that it is going to impact the TAM. We think TAM will be down 10% on a unit basis next year.

And then we’ll have to see in ‘28 whether things improve. But our expectation is that it does not improve in ‘27.

David Zinsner, CFO, Intel Q3 Earnings Call.

The PC segment has no hope in 2027 because the memory situation is not expected to improve. And, 2028 is a toss up: maybe things will improve, maybe it won’t. That’s not the kind of certainty investors are looking for.

#### PCs Be Damned. Server CPUs FTW.

With all the negativity around PCs, why was everybody so relaxed about Intel? Simple: CPUs for Agentic AI. Zinsner explained this in response to Rasgon’s Q2 earnings call question. He said:
