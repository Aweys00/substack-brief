---
title: "2026 OCP APAC: Full Conference Report"
source: "Vik's Newsletter"
author: "Vikram Sekar"
url: "https://www.viksnewsletter.com/p/2026-ocp-apac-full-conference-report"
published: "2026-08-23T04:01:12+00:00"
words: 1194
preview_only: true
---

# 2026 OCP APAC: Full Conference Report

Previously, we discussed some mixed messaging around the copper-optics transition. You can find the whole report below. In this report, we will discuss other networking themes from the conference, and a short section on the evolution of power architectures.

The major themes at OCP APAC 2026 orbited around how power constraints are driving technology innovations, and how those problems can be solved in the networking and power domains. We will cover the networking aspect at this conference to keep tabs on the copper versus optics transition, and closely monitor developments in optical technology.

Key takeaways:

-

Copper will continue to dominate within the rack at 200G/lane speeds. 400G/lane PAM4 seems challenging in copper; either PAM6 will be needed, or the transition to optics with NRZ/PAM4.

-

Pluggables and integrated optics (CPO/NPO) will continue to exist as datacenters use increasing optical content. The use cases will closely dictate which approach is best suited.

-

LPO has its challenges at high lane rates, and the DSP plays a key role in telemetry capture. Link data is important at scale, and underscores the importance of DSPs in the communication link whether it is a separate component or part of the host silicon.

-

XPO is being looked at for 400G/lane; simulation results shown by Arista, and measurement results are expected soon.

-

Power delivery at 800V is rolling out and sidecar implementations are simpler to certify. SSTs are the end-game with its own set of challenges; expected past 2030.

By reading this post, you agree to the [terms and conditions](https://www.viksnewsletter.com/p/terms-and-conditions). Also see the [full ethics statement](https://www.viksnewsletter.com/p/ethics).

If you’re new, check out the [About page](https://www.viksnewsletter.com/about). A lot of readers expense the subscription to this newsletter as it helps their professional work. Group subscriptions (3+) are 20% off. If you have any questions, reply to this email and let me know!

For the full post, upgrade to a paid subscription

Also check out the [Semi Doped podcast](https://www.viksnewsletter.com/about#§semi-doped-podcast) with and myself, and [our daily free newsletter](https://daily.semidoped.com/) with latest semi news. For my institutional work, check out [SemiExponent](https://www.viksnewsletter.com/about#§semiexponent).

Table of Contents

-

Power Constraints as a Technology Driver

-

State of the Copper Interconnect

-

Copper lives on within the rack

-

The Copper Wall at 400G/lane

-

State of the Optical Interconnect

-

Panel: CPO vs LPO vs Pluggables

-

Discussion about CPO and lasers

-

Discussion about GlobalFoundries’ Photonics

-

Discussion about Lane Rates/Modulation Speeds

-

Challenges in Implementing LPO

-

XPO form-factor at 400G/lane

-

Panel: AI Power Delivery - 800V Insights, SSTs

#### Power Constraints as a Technology Driver

A constant theme across the conference was the need for power and cooling technologies as compute scales in the future. Networking and power delivery discussions were targeted towards improving efficiency and lower component power across the AI stack.

Nearly every keynote in the conference started with power as the underlying motivator.

-

Microsoft (Gohar Waqar/Sushant Gupta, CVP Cloud Hardware): Investing in solid-state transformers (SSTs) and advanced cooling solutions.

-

Nvidia (Gilad Shainer, SVP Networking): Industry is converging towards 800V power delivery, and is improving power cost of networking by pushing co-packaged optics across scale-up and scale-out.

-

Arm (Michael Wong, President Taiwan): Massive demand for GWs, and supply is nowhere near enough. Agent workloads swamp CPU demand, and Arm AGI CPU provides a low TCO solution.

-

AMD (Ravi Kupuswamy, SVP): Power and cooling must be built from the ground up. Open standards are key to composable datacenters that can be optimized across a variety of axes, finely tuning compute, power, and networking to suit the workload.

-

NTT (Masahisa Kawashima, AICC): Power across large datacenter campuses will drive smaller buildouts, and they will need scale-across networking to unify their operation.

-

Google (Greg Moore, Cloud Platforms): Mentioned they are building a low-voltage direct-current (LVDC, another way of saying 800V systems) datacenters, and showed the latest developments from Project Deschutes, their coolant distribution system. Project Brazos is a liquid-cooled sidecar solution that will bring liquid cooling to currently air-cooled datacenters in operation.

-

ASE (CP Hung): Advanced packaging will be important to bring power delivery to the point-of-load. Vertical power delivery solutions integrating conversion at the point of compute contributes to efficiency improvements.

A few of the keynotes addressed themes outside of power as well; both Applied Materials and TSMC noted that system, not component optimization will drive future design principles. Broadcom reiterated that the network is the computer, and that open ethernet fabrics are the way forward.

#### State of the Copper Interconnect

The industry is at a fork in the road where copper reach is becoming questionable as lane rates increase. The event had many optics-centric discussions, but there was talk of copper continuing to exist as long as physics will allow. We will discuss where copper is headed.

##### Copper lives on within the rack

The SemiAnalysis view of copper interconnect is that it will continue to exist in the scale-up domain across Rubin Ultra (RU) NVL576, Feynman NVL1152, Trainium 4, and TPU v9. We should clarify what scale-up means in this context: intra-rack will remain copper, while cross-rack will likely go to integrated optics. Few additional points were mentioned:

-

Trainium 4 and RU NVL576 will both use copper within the rack and use NPO to scale-up across racks. RU Oberon racks with 2-die RU will use copper within the rack and NPO. The industry remains divided on the state of 4-die RU and its use within the Kyber rack.

-

TPU v9 is additive to the copper backplane with copper actually coming in, instead of being replaced by optics.

SemiAnalysis sees an increase in the amount of scale-up networking content if the HBM is de-speced going from 12-hi HBM4E to 8-hi HBM4 in RU NVL572. The decrease in the memory content per rack drives the utilization of a higher number of racks, which in turn increases the networking content. Some numbers were shown in the de-spec scenario: if memory cost goes from 41% to 28% of BoM, the cost is reallocated to scale-up networking which goes from 4% to 12%. This is visually represented in the rightmost two columns in the chart below.

We believe that copper interconnects will remain within the rack for the 200G/lane generation (uni- or bi-di). The reach of copper is 1-2m at this speed, and is sufficient to connect the compute and switch trays. There is no need for optical upgrades if this reach is sufficient for the architecture in use, unless the speed gets higher.

We covered this in the previous OCP APAC note in some more detail.

##### The Copper Wall at 400G/lane

As a rough estimate, when lane speeds double, the reach of copper interconnect halves. By this measure, at 400G/lane, intra-rack connections will no longer be possible with copper alone; the copper wall becomes real. However, this will become an issue only in the 3.2T era of networking which is at least two years away from early production deployments. Astera Labs pointed out that the use of DSPs to fix reach issues in scale up will add unacceptable latency and break power budgets. The transition to integrated optics is the only way going forward.
