---
title: "800VDC: Mapping the Power Semi Space for Sidecar Deployments"
source: "Vik's Newsletter"
author: "Vikram Sekar"
url: "https://www.viksnewsletter.com/p/800vdc-mapping-the-power-semi-space"
published: "2026-10-03T12:30:02+00:00"
words: 637
preview_only: true
---

# 800VDC: Mapping the Power Semi Space for Sidecar Deployments

Anthropic’s [S1 filing](https://www.reuters.com/business/anthropics-518-billion-ai-buildout-hinges-largely-deals-that-cannot-be-canceled-2026-09-29/) reveals an important number for the AI buildout: they expect to spend $518B in building out AI infrastructure over the next decade. What is more terrifying is that 80% is non-cancellable, requiring payments regardless of actual amount spent. If AI continues on this trajectory, we will see this spend levels increase to past $1T levels because Anthropic believes we will be “principally limited by the availability of compute.”

The massive deployment of compute over the next decade will require deployment of enormous amounts of power. [NERC](https://www.nerc.com/globalassets/our-work/assessments/nerc_ltra_2025.pdf#page=8.76) puts the 10-year projected peak power demand in the US at 245 GW. However, utility buildouts however operate on different time scales than the semiconductor industry, where shifts happen in the time frame of years instead of months.

If you’re new, check out the [About page](https://www.viksnewsletter.com/about). A lot of readers expense the subscription to this newsletter as it helps their professional work.

For the full post, upgrade to a paid subscription

By reading this post, you agree to the [terms and conditions](https://www.viksnewsletter.com/p/terms-and-conditions). Also see the [full ethics statement](https://www.viksnewsletter.com/p/ethics). Each paid subscription is for one person, not a company. Group subscriptions (3+) are 20% off if you need a few subs. Reach out to me if you want an institutional seat, we’ll work it out.

Check out the [Semi Doped podcast](https://www.viksnewsletter.com/about#§semi-doped-podcast), and [our daily free newsletter](https://daily.semidoped.com/) with latest semi news. For institutional research, contact me at [SemiExponent](https://www.viksnewsletter.com/about#§semiexponent).

The chart below from a16z for example, shows 20% of all invested AI capex flowing into power. The secular demand for power infrastructure and the high dollar content across the power ecosystem makes it more of a long-term play for investors, especially given its long deployment timeframes.

The entire gamut of the power semiconductor industry spans from the grid to the rack, and involves a variety of technologies that are difficult to comprehend in a broad sense; grid-side power electronics often deal with hundreds if not thousands of volts, while rack-side power is more “semiconductor-like” since it only deals with a few tens of volts. It requires many vendors, standards, and supply chains to work in lock-step if we were to make changes to how power should be distributed to AI infrastructure.

We’ve discussed the need to move to 800VDC power delivery before. If you want the basics physics behind it, check it out below.

Today’s GPUs consume about 200kW per rack. If we were to double the number of chips, the power problem quickly gets out of hand. Most racks today use 48/50V DC to distribute power within the rack. If the power per rack gets too high, then the rack needs to support >10,000A in its distribution system. This is infeasible, and the solution is to go to 800VDC, which would drop the current levels for the same level of power.

#### 800VDC: AI Power Delivery Done Right

One principal NVIDIA engineer I spoke to recently was of the opinion that we may not see racks go beyond 200-250kW in the industry; he believed that the cooling and power delivery challenges outweighed the benefits. In the Rubin Ultra (VR300) era, if we are hooking up eight Oberon racks in a 576 GPU scale up domain due to networking limitations, do we really need MW-level racks in the future? Even if the Kyber rack does get deployed, will we see more companies push towards such power levels? If not, what does that mean for the 800VDC ecosystem if we stay at current rack-power levels?

In the rest of this article:

-

Why 800VDC still matters even if rack power stops scaling aggressively.

-

What the sidecar architecture changes inside the datacenter.

-

Where the near-term 800VDC semiconductor opportunities actually sit.

-

How SiC, GaN and silicon divide the power-conversion stack.

-

Which companies are exposed across systems, switching, protection and control.
