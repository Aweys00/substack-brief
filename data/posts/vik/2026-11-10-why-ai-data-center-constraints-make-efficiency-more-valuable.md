---
title: "Why AI Data Center Constraints Make Efficiency More Valuable"
source: "Vik's Newsletter"
author: "Vikram Sekar"
url: "https://www.viksnewsletter.com/p/why-ai-data-center-constraints-make"
published: "2026-11-10T09:45:00+00:00"
words: 1682
preview_only: false
---

# Why AI Data Center Constraints Make Efficiency More Valuable

AI data center infrastructure has already been constrained by component supply and the availability of skilled workers to build new capacity fast enough. Following the US midterm elections, opposition to new data center construction has gained momentum, particularly in Texas.

Datacenter deployment is typically measured in GWs of capacity, but this tells us little about how much useful compute each GW produces. As AI demand grows, and power availability and construction approvals become more restrictive, there is a stronger incentive to maximize the output of existing facilities. This means increasing compute density, improving power delivery efficiency, and deploying accelerators that generate more tokens per watt. This post examines how these changes create new opportunities for AI infrastructure in 2027–28 and beyond.

By reading this post, you agree to the [terms and conditions](https://www.viksnewsletter.com/p/terms-and-conditions). Also see the [full ethics statement](https://www.viksnewsletter.com/p/ethics).

If you’re new, check out the [About page](https://www.viksnewsletter.com/about). A lot of readers expense the subscription to this newsletter as it helps their professional work. Group subscriptions (3+) are 20% off. If you have any questions, reply to this email and let me know!

For the full post, upgrade to a paid subscription

Check out the [Semi Doped podcast](https://www.viksnewsletter.com/about#§semi-doped-podcast), and [our daily free newsletter](https://daily.semidoped.com/) with latest semi news. For institutional research, contact me at [SemiExponent](https://www.viksnewsletter.com/about#§semiexponent).

#### Permit vs Power Constraints

The underlying tension in the AI buildout is whether we are site-approval-limited or power-limited, or both.

##### Power Limited Scenario

If we are limited by available power to energize the currently approved datacenter campuses, then the proposed moratoriums on datacenters have little impact. In other words, if we don’t have enough available on-site power (via generator lead-times or power-permitting delays), then delays to site approvals does not matter if we cannot energize them.

The clearest example of site-approvals running ahead of available power is in Santa Clara. Santa Clara had 13 data centers approved or under construction in 2023, but its grid needed major upgrades to supply them. Those projects had already reserved all the extra power the upgrades would provide. In October 2026, the city said the upgrades would come online between 2028 and 2030.

##### Site-Approval Limited Scenario

If site-approvals are the limiting factor and we have more than sufficient sanctioned power to energize those datacenters, then we become site-limited on the AI buildout. The recent AI stock selloff reflects concern that tighter approvals will reduce or delay AI infrastructure deployment. The question is how much additional delay these restrictions create beyond the power constraints already facing the industry.

The Jones Road project in Spartanburg, South Carolina, shows how this can happen. Its developer had paid $4 million for a utility commitment to supply 60 MW by September 2026. But when the county proposed a 12-month pause on new data center approvals, the developer began discussing a later power-delivery date with the utility. Power had been contracted, but uncertainty over permission to build was now disrupting the project’s plans.

These two counterexamples show that it is difficult to separate power availability and site approvals because it heavily depends on the region a campus is being deployed, and the local bylaws in effect there.

#### The Case for Better Power Efficiency

Regardless of which constraint dominates, there is strong incentive to extract more useful tokens from a datacenter campus.

-

When power is limited but site approvals are not, the objective is to increase useful tokens per megawatt. Improving power conversion efficiency, cooling efficiency, and compute performance per watt allows operators to deploy more compute within the same power budget.

-

When site approvals are limited but power is available, the objective is to increase compute density within approved facilities. Higher rack power density allows more accelerators to occupy the same physical footprint, provided the electrical and cooling infrastructure can support them.

Both scenarios create opportunities for semiconductor technologies that improve power efficiency or enable higher power density. The value of these technologies increases when the alternative is building another data center that may take years to energize or approve.

#### The Limits of Rack Densification

Packing more GPUs into each rack seems like the obvious solution when data center construction is constrained. But scale-up networking and cooling impose practical limits. Connecting hundreds of GPUs requires enormous network bandwidth, while removing 600 kW–1 MW of heat from a single rack requires advanced liquid cooling.

For example, NVIDIA’s NVL576 connects eight Oberon NVL72 racks through optical and copper links rather than concentrating the GPUs into fewer, denser Kyber racks. Kyber supports 144 GPUs per rack, but its deployment has reportedly been delayed by manufacturing challenges with its high-speed copper midplane. AMD is also moving toward optical scale-up with MI500.

Optics enables larger scale-up domains across multiple racks, but spreading GPUs across more racks increases the physical footprint. The additional space needed for power distribution, networking, and cooling makes this trade-off even more important.

The objective is not to maximize GPUs per rack, but useful compute per square meter of data center space. Power distribution architecture plays an important role in achieving this.

#### 800 VDC: Higher Power Density, Lower Losses

Today’s AI racks typically use 48–54 VDC power distribution within the rack. As rack power increases, the resulting currents become increasingly difficult to manage. We covered this physics in our earlier article on power delivery.

Construction constraints make the transition to 800 VDC more valuable because it can improve both compute density and power efficiency within existing facilities.

This happens in two ways:

-

Higher power density: 800 VDC enables rack designs targeting 600 kW to 1 MW, compared with the roughly 200–250 kW rack designs available today. More compute can be packed into the same data hall, provided sufficient electrical and cooling capacity exists.

-

Better power efficiency: Higher-voltage distribution reduces current and resistive losses. Newer architectures can also eliminate intermediate power conversion stages, allowing more of the available power to reach the GPUs.

We expect to see 800VDC deployment in various stages across the AI datacenter.

Near term: Rack-level upgrades. Dedicated power sidecars sit next to compute racks in the white space of existing data centers. They convert existing AC supplies to high-voltage DC without necessarily requiring changes to upstream electrical infrastructure. This offers a relatively straightforward upgrade path for facilities with sufficient power and cooling capacity. The downside is that power racks occupy valuable real estate in a datacenter hall.

Medium term: Row-level upgrades. Larger power centers can serve multiple compute racks through DC busways. This allows operators to move conversion equipment away from individual racks, potentially into the grey space outside the data hall. These upgrades require more extensive electrical modifications but improve space utilization and power distribution. Aggregating 800VDC at the row level unlocks more floor space for compute racks.

Longer term: Solid-state transformers. SSTs can convert medium-voltage AC directly to 800 VDC, eliminating several intermediate conversion steps found in conventional architectures, and increasing overall power efficiency from source to load. They can also integrate with battery storage and DC backup systems to simplify the overall electrical architecture.

Early commercial deployment has already begun for SSTs. [Envision recently announced](https://www.envision-group.com/news-detail?id=6af182c9351e2d0031d11f3e&lang=en) the world’s first commercial deployment of an 800V DC power system in its Galaxy AI data center campus in Ulanqab, China. The SST enables conversion directly from 10 kV medium voltage to an 800V DC bus running across the facility.

The limitation is that SSTs require more extensive changes to the facility’s electrical infrastructure, including medium-voltage connections, protection systems, and permitting. Human safety remains the biggest concern to be addressed in all 800VDC approaches.

The investment implication is that 800 VDC creates opportunities at different stages of adoption. Near-term demand comes from rack-level conversion and distribution equipment that can be installed in existing facilities. Longer term, the opportunity shifts toward high-voltage power electronics and facility-scale conversion architectures. I have discussed power semis related to sidecar deployments in quite some depth already, if you’re interested.

800 VDC reduces the losses and physical space needed to deliver power to compute hardware, increasing end-to-end efficiency. The next important aspect is how efficiently that power is converted into useful computation.

#### More Tokens from the Same Power

Purpose-built inference accelerators offer another way to increase the output of existing data centers.

OpenAI’s Jalapeño inference accelerator reports 1.5–1.9× higher inference throughput per watt than the NVIDIA systems it tested across three public models. These early, company-reported results show the promise of purpose-built inference architectures. d-Matrix and Qualcomm are taking a memory-centric approach, reducing energy spent moving data between memory and compute through on-chip memory and stacked compute-memory technologies.

You can watch my deep dive discussion about d-Matrix’s memory architecture here, on the Semi Doped podcast.

Taalas HC1 (bought by AMD) is the most radical architectural example. Hardwiring a model into silicon removes substantial memory movement, but sacrifices flexibility. It is an interesting indication of how far specialization could go when power becomes scarce.

As construction constraints tighten, getting more tokens from every GW becomes increasingly valuable.

Inference at the edge remains the holy grail, where running hardware on-prem or local AI on devices would substantially decrease the need for datacenters and put intelligence into the hands of devices that people already own. Getting useful results from edge AI for the kinds of workloads we run today, has proved to be challenging so far.

#### Conclusion

The AI buildout has largely been measured in GWs of deployed capacity. But as power availability and construction approvals become harder to secure, the more important question is how much useful compute each campus can produce.

800 VDC delivers power more efficiently to compute hardware, while more efficient accelerators reduce the energy required to produce each token. Together, they can increase data center output without additional grid capacity. There are also various options to increase efficiency via networking, cooling, memory, and software optimizations.

For investors, the opportunity is shifting beyond simply building more AI infrastructure toward making better use of what is already available. Technologies that increase useful compute per megawatt or per square meter of data center space stand to benefit, particularly if new construction becomes more difficult through 2030.
