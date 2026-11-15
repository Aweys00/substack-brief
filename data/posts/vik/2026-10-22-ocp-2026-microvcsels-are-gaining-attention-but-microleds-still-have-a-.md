---
title: "OCP 2026: MicroVCSELs are gaining attention, but microLEDs still have a case"
source: "Vik's Newsletter"
author: "Vikram Sekar"
url: "https://www.viksnewsletter.com/p/ocp-2026-microvcsels-are-gaining"
published: "2026-10-22T23:49:47+00:00"
words: 1501
preview_only: true
---

# OCP 2026: MicroVCSELs are gaining attention, but microLEDs still have a case

A lot of excitement at OCP Global Summit 2026 was around Credo’s pivot to microVCSELs (Vertical Cavity Surface Emitting Lasers), despite having acquired the microLED (Light Emitting Diode) company Hyperlume for $92 million. This move has left people confused about the future of microLEDs as an interconnect technology.

My view from OCP2026 is that microVCSELs have made it hard to justify microLEDs for cable interconnectrs. MicroVCSELs make slow-and-wide optics compelling over longer short-reach links, while microLEDs need to justify themselves through advantages elsewhere in the system. The interesting question is where that boundary falls, and what implications that has for companies building in the interconnect space.

The [Short Reach MicroEmitter Optics (SRMO) workstream](https://www.opencompute.org/projects/semi-private-workstreams/short-reach-micro-emitter-optics-srmo/) at OCP has been set in motion to define specifications around short-reach optics. Grouping LEDs and VCSELs under “microemitters” leaves room for companies to choose the light source based on the application.

In this post, we will sort through the trade-offs to understand why Credo chose microVCSELs, where microLEDs still make sense, and what remains to be proven. Motivation and underlying physics are free subscriber content; industry implications are for paid subscribers.

Table of Contents:

-

Why Short-Reach Optics? What is changing between racks, and why are familiar interconnect technologies being reconsidered?

-

microVCSELs vs microLEDs The device physics behind their differences in speed, reach and scaling—and what headline specifications leave out.

-

Inside Credo’s Change of Direction The engineering and commercial considerations behind one of OCP’s most discussed announcements.

-

Where microLEDs Still Have a Case Could a different application change how we judge this technology?

-

What Remains Unproven The questions about reliability and lifetime cost that a successful demonstration cannot answer.

-

Can Microemitters Become ams OSRAM’s Next Growth Engine? Its technology choices, competitive position and the milestones investors should watch.

By reading this post, you agree to the [terms and conditions](https://www.viksnewsletter.com/p/terms-and-conditions). Also see the [full ethics statement](https://www.viksnewsletter.com/p/ethics).

If you’re new, check out the [About page](https://www.viksnewsletter.com/about). A lot of readers expense the subscription to this newsletter as it helps their professional work. Group subscriptions (3+) are 20% off. If you have any questions, reply to this email and let me know!

For the full post, upgrade to a paid subscription

Check out the [Semi Doped podcast](https://www.viksnewsletter.com/about#§semi-doped-podcast), and [our daily free newsletter](https://daily.semidoped.com/) with latest semi news. For institutional research, contact me at [SemiExponent](https://www.viksnewsletter.com/about#§semiexponent).

#### Why Short Reach Optics

We have already discussed in a previous post how power and networking limitations are pushing the scale up domain to multi-rack configurations, and how that opened up an opportunity for active copper cables.

As lane rates and distance increase between racks, copper’s capabilities are becoming more limited. At 200G/lane, Active Electrical Cables (AECs) today can push to about 7m of reach. But this is insufficient to connect scale up domains like NVIDIA’s NVL576 that has 8 Oberon racks, for which the required reach can easily reach 10-20m. Speed is another limiting factor. As a rule of thumb, copper’s reach halves when lane rates double, which makes it hard to scale copper interconnect solutions. Finally, power consumption and latency in the scale up domain needs to be low, which limits the use of expensive and power hungry DSPs. The industry is trying to push copper with PAM6 modulation, while developing PAM4 in parallel for the 400G/lane era. We discussed this in the last post.

On the other hand, the InP laser-based optics is arguably overkill for applications under 50m because optical fiber is capable of carrying light across continents. Add to the fact that InP is already in short supply, and optical pluggables are often power hungry. Companies like NVIDIA, AMD, and Amazon are pushing CPO/NPO solutions to extend reach and lane speeds using low power laser-based optics, but those bring their own challenges concerning reliability and supply at scale. For links spanning only a few tens of meters at most, the question is whether we can deliver the required bandwidth with simpler, lower-power optics.

This opens the door to new optical technologies like microemitters that work for short reach (<50m), are not InP based, consume low power, and have the ability to scale lane speeds. Instead of pushing each optical lane faster, they distribute data across many slower lanes. Both microLEDs and microVCSELs follow this approach, but their device characteristics lead to different trade-offs in speed, reach, and integration.

My expectation is that the choice will depend on where the link sits. Across racks, reach becomes a stronger argument for microVCSELs. Closer to the compute, microLEDs have an opportunity to compete on dense integration, power, and thermal performance.

#### MicroVCSELs vs MicroLEDs

The choice between microVCSELs and microLEDs starts with what the link needs to do: how much data it must carry, over what distance, and within what power budget. Both technologies spread data across many slower optical lanes, but the properties of their light sources determine how fast each lane can run and how far it can reach. Understanding those differences helps explain where each technology fits.

##### Material and wavelength

MicroLEDs use GaN-based emitters that produce blue light around 420 nm, while microVCSEL approaches use GaAs-based material systems, with designs targeting wavelengths such as 850 nm and 1060 nm. Both can be manufactured using at least 6”-8” wafer sizes and are widely available in the supply chain, compared to 3”-6” wafers used in InP lasers.

VCSELs have an established history in optical communications, particularly in 850 nm multimode datacom links. That gives microVCSEL developers a foundation of device and manufacturing experience to build on. MicroLED interconnects are newer to this application. While that experience is an advantage, it does not establish that dense microVCSEL arrays are ready for deployment at scale.

##### How they emit light

MicroLEDs produce light through spontaneous emission: electrons and holes recombine and release photons without a fixed phase relationship between them. MicroVCSELs are lasers. Above a threshold current, stimulated emission sustains lasing within the optical cavity. In this process, light already present stimulates the emission of additional photons into the same optical mode.

VCSELs offer both a narrower emission spectrum and higher modulation bandwidth. The narrower spectrum reduces chromatic pulse spreading, while the higher modulation bandwidth allows each lane to carry more data. MicroLEDs compensate for their slower speeds by using more of them, but adding lanes does not extend their reach. This is why microVCSELs have a stronger case as the required distance increases.

##### Spectral Linewidth

Neither light source emits at exactly one wavelength. Its output spans a range around the center wavelength, and the width of that range is called its spectral width. While the exact linewidth depends on device design, microLEDs have a broad emission spectrum, spanning 20-40nm around 420nm while VCSELs emit over a much narrower range of 1nm or below around 850nm/1060nm. Linewidth has direct implications on how far along a fiber a light pulse travels.

##### Chromatic and Modal Dispersion

Pulse spreading caused by wavelength-dependent propagation is called chromatic dispersion. It occurs because refractive index (which determines how fast light travels through the fiber) changes with wavelength. The farther light travels through the fiber, the more the different wavelength components separate in arrival time. Eventually, neighboring pulses overlap enough to make the transmitted bits difficult to distinguish.

Slowing the data rate gives each bit more time, allowing the link to tolerate more spreading. Shortening the fiber reduces the spreading itself. This is why a demonstration at a high data rate over a short distance does not establish that the same rate will work across racks.

The narrower emission spectrum of VCSELs helps them reach farther before chromatic dispersion becomes limiting. However, spectral width is only part of the comparison: the fiber’s dispersion also depends on the operating wavelength. In multimode fibers, differences in arrival time between optical modes introduce another constraint called modal dispersion.

For a deeper explanation of the relationship between spectral width and reach, see my earlier article (free post).

##### Data rates

Most microLED links demonstrated in the industry for interconnect applications operate between 1-3 Gbps. I covered this in more detail in my field trip notes to Avicena, a leading manufacturer of microLED based interconnects. In the report, I also show an 8 Gbps demonstration through a free space link showing that microLEDs are capable of higher data rates, but I anticipate that transmission through fiber will limit its reach at that data rate.

VCSELs offer more per-lane speed. They can easily run at 50 Gbps, and arguably up to 200 Gbps. Running speeds an order of magnitude higher than microLEDs provides microVCSELs a natural advantage of running fewer parallel lanes for the same overall speed. This simplifies the attachment of fiber arrays and also allows the use of multi-core fiber (LightXcelerate demonstrated this at OCP). For slow-and-wide interconnects, the opportunity is to operate each VCSEL lane comfortably below its maximum capability.

#### Why the industry is moving toward microVCSELs

MicroVCSELs offer three advantages for near-term optical cable products: greater reach, more operating margin, and more options to scale bandwidth.
