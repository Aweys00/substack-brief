---
title: "Optical Switches for AI: Competition Beyond Mirrors"
source: "Nutty"
author: "Nutty"
url: "https://nuttycld.substack.com/p/optical-switches-for-ai-competition"
published: "2026-09-22T13:04:11+00:00"
words: 1194
preview_only: true
---

# Optical Switches for AI: Competition Beyond Mirrors

Industry and technology analysis, not investment advice · The author may hold positions in the securities mentioned

#### Executive Summary (Preview)

-

An optical circuit switch (OCS) changes connections between fibers without converting light to electricity. It can remove equipment and power consumption associated with intermediate optical-electrical conversion and packet processing.

-

Packet switches offer flexibility when communication partners change frequently. OCS suits high-volume traffic that can use the same connection for longer. Its economics depend on how many electrical switching stages it removes and how well the resulting circuits are utilized.

-

The OCS can remain in service when the transceivers at either end are upgraded. Cluster expansion and adoption in new applications matter more to its suppliers than rising link speeds alone.

-

Lumentum ($LITE) expects July–September OCS revenue to be meaningfully above $100 million. Beyond the technology’s potential, investors now need to consider how far the early manufacturers’ advantage extends and who can compete for the next generation of products.

On its August earnings call, Lumentum ($LITE) said July–September optical circuit switch (OCS) revenue would exceed $100 million for the first time, and by a meaningful amount. The midpoint of its total revenue guidance for the same quarter was $1.25 billion. On that outlook, OCS would account for more than 8% of revenue. For an optical-components supplier, this has moved beyond introducing a new technology: delivery schedules for the product now matter to quarterly results.

Laying more fiber does not solve every connectivity problem. The network still needs to decide where data should go and connect the equipment that needs to communicate.

Lumentum’s OCS redirects light with mirrors. But ensuring that a signal passes reliably through any chosen connection among hundreds of fibers requires precision optics, controls, and manufacturing processes. Lumentum is meeting this demand with manufacturing experience accumulated in optical switches for telecommunications. An advantage that helps it ship sooner is not necessarily a moat that protects pricing once competitors qualify.

Those competitors are doing more than building similar mirror-based systems. Some put optical connections on a chip; others combine their own optical devices with a specialist manufacturer’s packaging and assembly. Proven systems have an advantage in current build-outs, but the next network design may use a different technology or supplier. A growing OCS market and stable market shares for its current suppliers are separate propositions.

### Redirecting Light Without Electrical Conversion

A conventional data-center switch receives small bundles of data called packets, reads their destination addresses, and forwards them to the next link. If the signal arrives over fiber, the switch converts the light to electricity for processing on a chip, then converts it back to light. An optical circuit switch skips this intermediate conversion and connects the incoming light to another fiber.

Lumentum’s MEMS design makes that connection by tilting tiny mirrors. An input mirror sends light to an output mirror, which directs it into the destination fiber. Removing some of the equipment that converts light to electrical signals and reads them can save power and equipment cost.

Control software chooses which fibers to connect. The OCS executes an instruction to keep one fiber connected to another for a while. The mirrors move when the connection changes; they do not move each time data passes through. Choosing a destination for each packet and changing the physical connections are separate functions.

The same capability can help when compute hardware fails. Google ($GOOGL) said its TPU 8t, unveiled in 2026, has 9,600 chips in a superpod, with OCS automatically reconfiguring the surrounding connections after a failure. The design reroutes connections around failed equipment so that computation can continue on the remaining hardware.

#### Upgrade the Transceivers, Reuse the OCS

The transceivers at either end, which convert between electrical and optical signals, can be upgraded to faster products while the OCS between them stays in service. In its May 2026 technical overview, Lumentum said the same MEMS OCS platform can support current and future optical interfaces. Wavelength compatibility, optical loss, and the required port count still have to match.

Selling faster transceivers does not generate replacement revenue for the OCS supplier if the existing switch remains in place. Incremental OCS demand depends more on how many connections need to pass through an OCS than on how fast those connections run. That makes expansion of OCS-equipped clusters and adoption in new applications important.

### Where Packet Switches and OCS Work Together

A packet switch reads the destination of each packet and decides where to send it. Data headed to different destinations can share a link, and temporary storage called a buffer holds traffic during bursts while the switch schedules transmission. These functions allow a network to operate without knowing in advance which devices will communicate or when.

That flexibility requires the switch chip and memory to keep processing data. Each electrical switching stage connected by fiber also repeats the optical-electrical conversion. Even when large volumes of traffic keep flowing between the same groups of devices, the intermediate processing cost remains. A buffer can temporarily absorb incoming traffic, but it cannot increase the capacity of an output link. As incoming traffic accumulates, packets spend longer waiting in the buffer.

OCS saves that equipment cost and power by removing intermediate conversion and packet-processing stages. It is particularly useful where large volumes of traffic repeatedly flow between the same groups of devices and the required connections can stay in place for a time. Once a circuit is set, light simply passes through it. Repetitive exchanges in AI training clusters and large traffic flows in the upper network create more opportunities for this approach. Some links can connect directly through optics instead of requiring more equipment to process every packet.

An OCS cannot decide for itself which devices to connect or how much capacity is needed. Control software has to make those decisions. If communication partners change frequently, the network must reconfigure the circuits or use other paths. An idle circuit cannot lend its capacity to a different destination on a packet-by-packet basis. Provisioning many spare circuits to accommodate this reduces the savings from removing equipment. Having no queue inside the OCS does not mean the network has no congestion.

The more likely form of wider adoption therefore keeps the devices needed for packet processing and uses OCS for some of the connections between them. A switch close to the servers might handle destination selection and congestion, while OCS reduces conversion stages higher in the network. OCS economics depend on the electrical switching stages that can be removed and the actual utilization of the new optical circuits. Suppliers need more deployments that meet those conditions for revenue to keep growing.

[PhotonCapIs a Slow Mirror Fast Enough? OCS Technology Economics and Market FlowTL;DR Lumentum’s OCS (optical circuit switch) revenue went from zero to more than $100 million a quarter in one year, counting from August 2025 when it recognized its first OCS revenue…Read more2 months ago · 17 likes · 1 comment · PhotonCap](https://photoncap.net/p/is-a-slow-mirror-fast-enough-ocs?utm_source=substack&utm_campaign=post_embed&utm_medium=web&embedding_publication_id=915696)

Coming Up

The next sections examine what makes OCS difficult to manufacture at scale, how durable the early suppliers’ lead may be, and where more compact designs could give new competitors an opening.
