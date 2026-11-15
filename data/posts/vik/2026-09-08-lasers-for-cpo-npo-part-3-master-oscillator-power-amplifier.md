---
title: "Lasers for CPO/NPO: Part 3 – Master Oscillator, Power Amplifier"
source: "Vik's Newsletter"
author: "Vikram Sekar"
url: "https://www.viksnewsletter.com/p/lasers-for-cponpo-part-3-master-oscillator"
published: "2026-09-08T03:11:13+00:00"
words: 722
preview_only: true
---

# Lasers for CPO/NPO: Part 3 – Master Oscillator, Power Amplifier

This is the third article in the series on UHP lasers for CPO/NPO. If you want to understand why these external UHP lasers are needed for CPO, see this post for background.

In Part 1 of this series, we built up the fundamental physics of ultra high power (UHP) lasers. We concluded by identifying the four walls that make it challenging to implement a UHP laser: managing heat, maintaining narrow linewidth, getting light out, and catastrophic optical damage.

In Part 2, we explored how Lumentum overcame these challenges via their [2007 paper as JDS Uniphase](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/6485/64850G/Very-high-power-1310nm-InP-single-mode-distributed-feed-back/10.1117/12.701321.short), and via their later [2022 CLEO paper](https://www.lumentum.com/sites/default/files/2025-12/high_power_cw_laser_for_co-packaged_optics_2022.pdf) on UHP lasers. We also looked at how defensible their high power laser platform is.

In Part 3, we will look at the use of a Semiconductor Optical Amplifier (SOA) in conjunction with a lower power laser (~100 mW) to generate UHP laser power levels of ~400 mW. This architecture is called the Master Oscillator (the laser diode), Power Amplifier (or the SOA) approach – aka, MOPA. We will contrast it to the single-cavity UHP laser approach to highlight the pros and cons of each.

Contents:

-

The MOPA Concept (free)

-

Integrated Semiconductor Optical Amplifiers (SOAs)

-

Operating Principle

-

Amplified Spontaneous Emission (ASE)

-

Back Reflection into the SOA

-

MOPA High Power Lasers

-

Sumitomo’s SOA-Integrated DFB Laser

-

Nanjing University’s 12-Channel MOPA Array

-

Single Cavity vs MOPA: Lumentum vs Sumitomo

-

Who is Actually Shipping?

-

Which Bet Wins

By reading this post, you agree to the [terms and conditions](https://www.viksnewsletter.com/p/terms-and-conditions). Also see the [full ethics statement](https://www.viksnewsletter.com/p/ethics).

If you’re new, check out the [About page](https://www.viksnewsletter.com/about). A lot of readers expense the subscription to this newsletter as it helps their professional work. Group subscriptions (3+) are 20% off. If you have any questions, reply to this email and let me know!

For the full post, upgrade to a paid subscription

Check out the [Semi Doped podcast](https://www.viksnewsletter.com/about#§semi-doped-podcast) and [our daily free newsletter](https://daily.semidoped.com/) with latest semi news. Reach out for institutional research at [SemiExponent](https://www.viksnewsletter.com/about#§semiexponent).

## The MOPA Concept

The idea is simple: instead of making a single-cavity high power laser that is prone to issues like spatial hole burning and optical damage like we’ve discussed in previous articles, use a low power seed laser, and then put a power amplifier after it to boost up the power.

Source: Coherent

Example: A MOPA UHP laser can run the MO at ~100 mW and have the PA multiply that power by a factor of 4x, or 6 dB, to produce a total of ~400 mW at the output.

It is far simpler to make a low power laser with good spectral qualities due to the photon field in the cavity being low. A lot of the issues we discussed earlier in making UHP lasers are greatly mitigated at low laser power. Most laser manufacturers can make them at high yield.

The challenge in MOPA lasers comes from designing a power amplifier (SOA) that is good enough to boost the power to the levels needed for CPO, without degrading the spectral properties of the signal. High power amplification, whether it is radio waves or light, is no laughing matter.

When amplifiers are driven to deliver high power, they unintentionally degrade the quality of light output unless they are designed well. Having two components instead of one introduces other problems: (1) the interface between the two matter, and (2) the combination of the MO and PA should work reliably at high yield over a range of temperatures.

The concept of MOPA amplifiers is not new as they have been widely used in precision cutting, lidar and medical imaging. Those systems use discrete laser and amplifier components, along with isolators, focusing lenses and mirrors. The isolator exists to prevent the reflected light from the input of the PA from affecting the operation of the MO. This is important to remember when we discuss integrated MOPA lasers. Fibers doped with rare earths like Erbium or Ytterbium perform the power amplification, which themselves require pumping with lasers to amplify light. Mirrors and lenses guide the light across the system.

Source: [em-smart.com](http://em-smart.com)

Discrete MOPAs are too bulky for use as light sources for CPO. They will need to be integrated into the same InP substrate to deliver a compact light source. We will discuss integrated SOAs next.
