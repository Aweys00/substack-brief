---
title: "Co-Packaged, Near-Packaged, Always Tested"
source: "Damnang Research"
author: "Damnang"
url: "https://www.damnang.com/p/co-packaged-near-packaged-always"
published: "2026-10-02T02:41:30+00:00"
words: 1369
preview_only: true
---

# Co-Packaged, Near-Packaged, Always Tested

The optical sector’s stocks surged early this year amid AI optical interconnect demand and CPO expectations, but after a research firm published a CPO shipment delay report in early June, they plunged across the sector.

After that, as doubts grew over how fast CPO mass production would expand, attention gathered on NPO, which had been seen as merely an intermediate step before CPO.

The market’s question has also changed.

Now, rather than whether CPO comes, the interest is which comes first and who benefits in the meantime as CPO and NPO grow together, and for the optical test companies that drew attention together with CPO, the key is whether their growth can continue whichever path leads.

In two articles in April and May, I treated optical test as a key watch point of optical interconnect investment, and I keep that view no matter which of CPO and NPO comes first. That is because whether the optical interconnect is pluggable, NPO or CPO, optical test is a process it must go through.

This article first scores the watch points I presented in April, then examines what new test demand NPO creates and how it carries that demand while CPO is late. It then presents how much more testing scale-up CPO needs than scale-out CPO when it comes, which numbers show that timing first, and which companies benefit and when in this process.

I am confident that after reading this article, you will gain the overall flow of optics and investment insights from the perspective of CPO testing.

This article is for informational purposes and is not a recommendation to buy or sell any specific stock. Prices and multiples are based on September 30, 2026 closing prices (FormFactor’s one-year return and forward multiple are as of September 29). I may hold the stocks mentioned and my positions may change, and investment decisions and responsibility rest with the reader. NFA / DYOR.

Damnang Research is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

### 1. April’s five watch points: how far have they come

Of the five watch points I presented in April, production schedules and equipment orders moved in the expected direction. TSMC announced its 2026 production plan for COUPE on substrate, and news of the full production of NVIDIA’s Spectrum-X Ethernet Photonics came out on August 14. Aehr’s second-half bookings were also $97.9 million, above the expected $60 million to $80 million.

In contrast, there was no acquisition of an optical test company by Advantest.

Open CPX 1.0, released on September 17, also only set the module’s structural, electrical, optical connection, thermal management and control requirements, and did not unify the test items and conditions of the preceding wafer and optical engine stages.

### 2. CPO is late, and NPO comes first

Scale-out CPO has already entered mass production with NVIDIA’s Quantum-X and Spectrum-X Photonics, but a research report released in early June lowered the scale-out CPO shipment forecast through 2027 below the previous one and pushed the introduction of scale-up CPO to 2029.

The delay reasons the report cited were optical engine assembly yield, the difficulty of integrating optical components directly into switch and GPU packages, and cost, and all three stem from CPO’s structure of attaching the optical engine directly to the package.

When the optical engine is attached to the same package as the switch chip, repair after assembly is impossible, unlike pluggables where only the defective module can be pulled out and replaced, so the whole package can be lost because of a single optical engine. In a configuration that uses 18 optical engines together, like Quantum-X, even assuming each optical engine is good with 99% probability, the probability that all 18 are good is only about 83.5%, and if each is 98%, it falls to about 69.5%.

NPO avoids this risk by plugging the optical engine into a socket right next to the chip instead of putting it inside the chip package.

It is a form in which the optical module that used to plug into the front panel is moved next to the chip and the signal correction chip inside the module (DSP) is removed, so even if a defect occurs, only the optical engine needs to be pulled out and replaced, and the manufacturing and test equipment of pluggables can be used almost as is.

That is why it has emerged now as a realistic alternative for scale-up, before the supply chain can handle the mass production of CPO.

On September 17, Huawei unveiled a SuperPoD using Hi-ONE (7.2Tb/s), the first NPO optical engine to enter mass production, explaining that NPO is the most realistic choice given today’s supply chain maturity, and in the field too, first shipments of NPO for hyperscalers in 2027 and volume expansion in 2028 are being discussed.

NVIDIA’s scale-up roadmap follows the same flow.

The 2027 Rubin Ultra NVL576 connects copper inside the rack and optics only between racks. The official announcement presented CPO, but in the supply chain, it is said that an NPO configuration is also being prepared for maintainability and securing volume, while CPO is the priority.

In the 2028 Feynman generation, the NVLink8 CPO switch is on the roadmap, and even then systems can choose between copper and CPO NVLink.

So, as I have always argued, I see the introduction of scale-up CPO in 2028, but I expect ramp-up volume to increase in earnest after the second half of 2029.

### 3. NPO also creates new test demand

I covered the basic structure of optical testing in Everything You Need to Know About CPO Testing, which I wrote in April, so if you want to study the details, I recommend reading that article.

While electrical testing contacts terminals with probes to send and receive signals, optical testing adds the alignment of a fiber with a core of about 9µm to a silicon waveguide about 0.5µm wide and the checking of operation across temperature, so it takes a long time.

A test point is called an insertion, and the process of applying temperature or electrical stress for a set time to screen out devices that would fail early is called burn-in.

Every path goes through PIC (a photonic integrated circuit that handles light) wafer test, laser burn-in and link bit error rate validation, but where and how much testing happens differs by structure.

The figure above shows, for each test item, in which structure the burden grows.

NPO implementations vary slightly by company, and this article compares test items with pluggable and CPO based on the socketed optical engine of Open CPX, whose specification came out in September.

In NPO, the share of optical engine test, electrical validation together with the host chip, socket contact test and temperature test grows, and in CPO, full wafer testing, final testing together with the switch chip and pre-assembly burn-in increase greatly.

Pluggables test the finished module to standard specifications and replace the whole module when a defect appears, but in NPO the optical engine itself is the unit of replacement, so the optical engine test before plugging into the socket takes that role.

Also, many NPO designs remove the module DSP, so optical engine performance depends on the ASIC’s SerDes and the board and socket channel between them, and a new validation that checks link margin together with the host chip is needed.

Because there is no test equipment that handles signals of 400G and above cheaply, in mass production the chip handles electrical validation itself, so this demand goes to high-speed instruments in the development stage and to test boards and sockets in mass production.

Since the optical engine is pressed into a socket next to the chip, socket contact and board warpage must be checked separately, and because it sits right next to a chip that generates a lot of heat, one must also check whether it operates over a wide temperature range.

These tests grow with volume from 2027, when NPO mass production starts, so even if CPO is late, demand for optical engine test, host chip validation and socket test arises first in NPO.

### 4. While CPO is late, NPO carries the demand
