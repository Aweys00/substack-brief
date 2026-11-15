---
title: "ECOC 2026: Important Product Announcements Around Optical Scale-Up"
source: "Vik's Newsletter"
author: "Vikram Sekar"
url: "https://www.viksnewsletter.com/p/ecoc-2026-important-product-announcements"
published: "2026-09-21T19:23:57+00:00"
words: 1171
preview_only: true
---

# ECOC 2026: Important Product Announcements Around Optical Scale-Up

In my infinite wisdom, I decided not to attend ECOC 2026 even though there were a multitude of reasons to do so: (1) I had registered for it, (2) It is held in Malaga, Spain, which is quite lovely and by the beach, (3) It is on a topic that I think about a lot: optics. I was just tired from my 3 week trip to the Bay Area for Hot Chips and OCP APAC, and I will have to go again in October for OCP. Each time, it is a trip around the world. So I passed.

Big mistake. As a friend put it — “We will always have fomo dude.” Instead, I’ve been living vicariously through product announcements and pictures from friends and acquaintances on texts and forums, and there have been a few important ones especially as related to optical scale-up.

Let’s cover them and their implications:

-

Teradyne Iris 100 for microLEDs

-

ams OSRAM thin-film VCSEL

-

🔒 Lumentum DWDM ELSFP

-

🔒 Lumentum + Qualcomm 1060nm VCSEL

-

🔒 Coherent Photonlink

By reading this post, you agree to the [terms and conditions](https://www.viksnewsletter.com/p/terms-and-conditions). Also see the [full ethics statement](https://www.viksnewsletter.com/p/ethics).

If you’re new, check out the [About page](https://www.viksnewsletter.com/about). A lot of readers expense the subscription to this newsletter as it helps their professional work. Group subscriptions (3+) are 20% off. If you have any questions, reply to this email and let me know!

For the full post, upgrade to a paid subscription.

Check out the [Semi Doped podcast](https://www.viksnewsletter.com/about#§semi-doped-podcast), and [our daily free newsletter](https://daily.semidoped.com/) with latest semi news. For institutional research, reach out at [SemiExponent](https://www.viksnewsletter.com/about#§semiexponent).

#### Teradyne Introduces Iris 100: Production-Proven Test System for MicroLED Devices

The news:

Teradyne Iris 100 brings semiconductor-grade optical test to microLED manufacturing, measuring every individual emitter in an array and integrating directly with the Teradyne [UltraFLEXplus](https://cts.businesswire.com/ct/CT?id=smartlink&url=https%3A%2F%2Fwww.teradyne.com%2Fproducts%2Fultraflexplus%2F&esheet=54606199&newsitemid=20260920750507&lan=en-US&anchor=UltraFLEXplus&index=3&md5=7517e6d7a35a11b87a679d03fcba62e1) platform for combined optical and electrical test.

MicroLED technology underpins two of the fastest-moving areas in advanced electronics, augmented reality (AR) microdisplays and optical data interconnects for AI data center architectures. Both depend on devices that contain hundreds of thousands to millions of individual emitters, each of which must be characterized with production-level precision and throughput.

"MicroLED is shifting from lab to volume production for both AR microdisplays and, increasingly, optical interconnects, which are becoming foundational to how AI data centers scale beyond copper," said Shannon Poulin, president of the Semiconductor Test division at Teradyne.

([Businesswire](https://www.businesswire.com/news/home/20260920750507/en/Teradyne-Introduces-Iris-100-Production-Proven-Test-System-for-MicroLED-Devices))

Why it matters:

Product test equipment announcements are notable because they indicate that there is a need to test microLEDs at scale. Of course, they can be for AR displays, but the real moneymaker business case would be optical interconnect. Realistically, Teradyne would have had conversations with the microLED makers (Credo, ams OSRAM, … ) to understand if there will ever be a need to go to production. Now that the product is here, the answer seems to have been yes. This bodes well for microLED interconnect overall.

That is right up until …

#### ams OSRAM unveils breakthrough Thin-Film VCSEL for AI Scale-Up

The News:

ams OSRAM is expanding its Digital Photonics strategy to address this emerging opportunity. Building on its leadership in intelligent light emitters, optical sensors and advanced semiconductor manufacturing and assembly, the company is unveiling key photonic building blocks required for next-generation AI infrastructure. These include addressable micro-emitter arrays based on both LED and VCSEL technologies, as well as matching micro-photodiode arrays that together form the optical foundation of future ultra-high-bandwidth interconnect architectures.

ams OSRAM continues to expand its photonics portfolio through the development of a next-generation 850 nm Thin-Film VCSEL platform specifically designed for AI scale-up interconnects.

The platform combines several differentiating technologies in a single architecture, including top-emission Thin-Film VCSELs, dense 25 µm pitch microVCSEL arrays with addressability, silicon TSV integration and compatibility with standard multimode fiber infrastructure. This enables highly parallel optical links with exceptional packaging density and ultra-low-power operation.

The company has successfully completed microVCSEL integration on silicon TSV substrates and demonstrated error-free 32 Gb/s NRZ operation. The platform achieves an energy efficiency of approximately 0.25 pJ/bit while maintaining compatibility with scalable manufacturing approaches. This level of efficiency highlights the potential of highly parallel optical architectures to support future bandwidth scaling while minimizing power consumption.

In addition, reliability testing has shown no failures after more than 2,000 hours under elevated junction temperatures and current overstress conditions.

([ams OSRAM](https://ams-osram.com/news/press-releases/ecoc-datacom))

Why it matters:

Apart from the stock price bump, ams OSRAM announced their entry into the world of ‘wide-but-slow’ optical interconnects. The internet has been expecting this ever since [Ashkan Seyedi](https://www.linkedin.com/in/m-ashkan-seyedi-2358b66/) left NVIDIA to join ams OSRAM three months ago, but coming out with some real tech seals the deal.

Before we get all into microVCSELs, notice that the press release states that their Digital Photonics platform comprises of addressable arrays of both microLEDs and VCSELs. Clearly ams OSRAM is hedging their bets here: why pick one over the other when you have the expertise to do both. They could, after all, serve different speed generations at different price points and offer TCO options to the customer.

They describe their microVCSEL arrays as “thin-film” and have “silicon TSV” integration. I am not sure what the device structure is and what that has to do with “thin-film,” but the presence of TSVs likely means that the silicon chip is flipped onto a host board, and then the microVCSELs integrated right on top. If you think about it, this configuration requires TSVs. In addition, the flip-chip approach will reduce parasitics — which is excellent for the electro-optical bandwidth of the microVCSELs.

The microVCSELs are running at 32 Gbps/lane, which is believable speed for this technology. It is not so fast (like 50-100 Gbps) that now each lane requires heavy equalization via CTLE/DFE, which is a real problem in running VCSELs too fast because they start to require more power. Keeping speeds tame means that they can achieve 0.25 pJ/bit, but it is unclear if this involves the driver circuits and stuff too.

There is no mention of reach in the press announcement, but I am hoping it is at least 3-5m to stay competitive. There was a mention of [1,024 emitters in the array](https://x.com/vikramskr/status/2101953863083528461?s=20), but shortly after, the press release was [edited to exclude it](https://x.com/vikramskr/status/2101984439941362133?s=20). It was probably a mistake because running 1,024 emitters at 32 Gbps in wide and slow would make this 30x faster than Avicena’s link. Think about it; it’s too good to be true. My guess is that they are using about 50-ish parallel links to get 1.6 Tbps of bandwidth.

Finally, there is some mention of reliability testing over temperature and electrical stress which is important because VCSELs are still lasers. Not InP lasers, which is good for the supply chain. The device is likely built with GaAs.

Takeaway: Wide-but-slow optics in either LED or VCSEL form is becoming a strong signal. Optics for scale-up can take these forms, and not just CPO/NPO. CPO/NPO will take market share, but will have to compete with these other approaches as well for scale-up.
