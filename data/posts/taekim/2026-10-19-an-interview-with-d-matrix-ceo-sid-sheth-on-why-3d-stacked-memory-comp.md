---
title: "An Interview with d-Matrix CEO Sid Sheth on Why 3D-Stacked Memory Compute Is a Game Changer"
source: "Key Context (Tae Kim)"
author: "Tae Kim"
url: "https://taekim.substack.com/p/an-interview-with-d-matrix-ceo-sid"
published: "2026-10-19T12:46:44+00:00"
words: 2745
preview_only: false
---

# An Interview with d-Matrix CEO Sid Sheth on Why 3D-Stacked Memory Compute Is a Game Changer

Startups are where much of the technology industry’s innovation happens.

One of the AI industry’s biggest current problems is the so-called “memory wall,” which is the growing gap between how fast AI chips can perform computations and how fast they can be fed the data to compute on.

d-Matrix, a small startup founded in 2019, may have one of the most intriguing solutions to the memory wall. According to industry sources, the company is ahead of the competition with its 3D-DRAM technology, which will be incorporated into its next-generation Raptor product slated for the end of next year.

Key Context spoke with Sid Sheth, founder and CEO of d-Matrix, at the OCP Global Summit. We discussed the early days of his company, the key pivots the startup was forced to make, the importance of memory-centric compute, and the potential of 3D-DRAM and why AI inference needs it.

Key Context by Tae Kim is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

At the summit last week, d-Matrix announced Squadron, a multi-rack compute cluster for data center inference developed in partnership with Arista, Broadcom, and Supermicro. In September, the company also announced it will adopt NVLink Fusion, Nvidia’s rack-scale architecture, for its Raptor XPUs. Initial availability of d-Matrix Raptor Nvidia MGX AI server racks is expected in the fourth quarter of 2027.

Of course, d-Matrix must execute and meet its schedule and milestones. But if it comes through, it may be an industry game changer.

Here are lightly edited highlights from our conversation.

Tae: What is the early story background of d-Matrix?

Sid: Let’s take a step back. Here’s a little bit about how we even got started. Inference was not in everyone’s vocabulary back in 2019. It wasn’t a very well-understood word. Where inference was really being used, it was being used inside the hyperscalers for the most part.

It was not necessarily being done on GPUs. It was done on CPUs at the time. GPUs were just coming in for inference. Actually, GPUs were primarily being used for training at the time.

This was the backdrop against which we thought of going off and building a company for inference and the deployment of inference at scale. Cloud-scale inference. Data center-scale inference. So it wasn’t a very obvious thing in 2019. Pretty much everyone I talked to was like, I’m not quite sure why you need a solution like yours. Why would GPUs not be good enough? They’re just transitioning to GPUs.

Our thesis was, just thinking of it at a very fundamental level, if you look at what inference is all about, it’s just making a bunch of decisions. You need computing, you need data, and when people want to make decisions, they want to make them quickly, so at some point speed is going to matter.

What are the most critical bottlenecks? Well, it’s memory bandwidth, and eventually it’s memory capacity. There’s plenty of compute. The amount of compute flops that Nvidia was incorporating in its GPUs was already doubling every year and a half to two years, right?

We said nobody’s solving the memory bandwidth and memory capacity problem in conjunction with compute. And that is what became the thesis of d-Matrix. If we go solve that problem, there comes a time in the future when inference really goes global. It’s not just inside the domain of hyperscalers. It’s really a consumer problem.

Guess what, everyone is going to care about how quickly they can interact with AI. They’re going to want to easily crunch through all the data available. And so memory capacity and memory bandwidth in conjunction with compute will become a very, very prominent problem.

And we should go build a memory-centric compute solution today. We don’t know what that looks like, but we should go work on that and build it today, because that would make the company super relevant.

That was the thesis when the company got started, and history has been kind. To a certain extent, it was 50% insight and 50% luck, but we are in the right place now.

Can you talk about the current product, Corsair? What is it good for? What trade-offs did you make? And then there’s the upcoming product, Raptor, with its 3D DRAM. What excites you about Raptor and how would you describe the evolution from Corsair?

We basically said we’re going to reimagine the compute substrate. This has to be a memory-integrated compute substrate, right?

First of all, let’s look at what the options are for what kind of memory. There were companies doing flash-based in-memory compute, and there were companies doing other exotic memories, mostly non-volatile memories.

And we said, well, for data center use, that won’t work, because when these accelerators get deployed, people are going to be constantly programming them, and a data center environment is very dynamic.

We had to pick a memory that’s very programmable, so that was one. Number two, we realized that whatever we picked had to be a digital memory. It could not be an analog memory, because in a data center setting, people care a lot about the predictability and accuracy of compute, and anything analog is going to have some amount of probabilistic results in the compute. So it’s not as predictable.

So we said, we’re going to have to pick some digital memory, and that led to SRAM. SRAM is the most ubiquitous memory, and it is digital.

We felt that if there was a way to integrate SRAM with compute, that would be the right solution. So that became Corsair. Corsair was the first compute substrate that we created with SRAM. It addressed a lot of the customer feedback we were getting at the time. You’ve got to be all digital, you’ve got to be ubiquitous, you’ve got to be programmable. That addressed all those problems.

But building the compute substrate is one piece. That’s just the chip. That was the big learning for the company because we spent the first few years staffing up a really good chip team and building the software to go along with the chip. But the world was not looking to deploy chips, it was looking to deploy racks. So we had to make the transition from chip scale to rack scale, and that is what we announced at OCP. We are announcing full rack-scale GA [general availability] on Corsair.

We can just roll in racks and deploy them at scale. So that was really the journey on Corsair, creating the SRAM-based compute substrate, taking it to production, and scaling it up and scaling it out through partnerships with Arista, Supermicro, Broadcom, etc.

Now, fast forward to 2024. We realized the world was obviously going to rack scale. Why? Because models were getting bigger, context lengths were getting bigger, and inference was no longer the domain of just the hyperscalers. It was truly post-ChatGPT. It had gone global, consumers were using it everywhere, and multiple applications were coming in. Our entire thesis, that you’re going to need more memory and more bandwidth, started coming true, and we were like, wow, we don’t have the right memory anymore.

We have SRAM memory, which is not scaling.

And why doesn’t it scale? Is it just too expensive? Why can’t you scale SRAM?

First of all, it’s in a logic process. There is no difference between SRAM memory and the logic process at TSMC or any fab out there. That is the memory that is part of the logic process. And look at logic processes. People talk about Moore’s Law being dead or what not. There is just a limited amount of transistor scaling available, and SRAMs are not immune to that.

Size wise you can’t scale?

You can’t scale. Size wise. You can’t scale your transistors beyond a certain point, and the same thing applies to SRAM. It’s not scaling beyond a certain point, and that directly ties to the amount of capacity you can get in the next generation.

If Moore’s Law were still active, you would be 2X-ing the number of transistors every generation, and you would just be doubling SRAM capacity. That’s not happening anymore. Now it’s 10% or 20% incremental gains in SRAM capacity.

That won’t work when models are doubling in size every six to nine months and SRAM is increasing by 10% to 20% every two years. So clearly, this is not how it works. We had to come up with something totally different, out of the box, and that’s where we came up with a way to co-package DRAM, custom DRAM.

So this is not HBM. Essentially, we built a DRAM tile that can be 3D stacked along with our SRAM compute tile.

We already had the SRAM compute tile from Corsair, but we said, okay, now how do we increase capacity? Maybe there is a tier of memory [where] we can place [compute] directly on top. And that solves two problems. One is that we add more capacity, because we added another tier of memory.

The other is the way we package it. Placing the compute tile and the memory tile on top of each other opens up the surface area of the memory tile. Now we can expose all the memory on top and drop data down into the compute, so you have a lot more surface area to access the data. Compare that with what is happening today with GPUs and HBM. You really only have the beachfront of the HBM or the beachfront of the GPU to access the data, and that restricts the amount of bandwidth you can have between the GPU and the HBM.

Who are you using to make this?

TSMC makes the logic tile. There are two tiles. A logic tile and a DRAM tile.

The DRAM tile is made by a company in Taiwan called Powerchip, PSMC, and the logic tile is made by TSMC. Then we go to a packaging house, an OSAT, that packages the DRAM tile and the compute tile using a process called chip-on-wafer technology, which is very prevalent in HBM today. All HBM stacks use chip-on-wafer technology.

And how long have you been working on this?

Four years.

I hear this would be a great idea, but I don’t hear about many other companies that are far along on it yet.

Yes. I mean, people have started working on it. There are other companies that have embraced this and acknowledged that this is probably the holy grail for AI inference.

But you’re a few years ahead.

We are a few years ahead.

Who are the others? Samsung? SK hynix?

Samsung and SK will be offering the DRAM memory technology to co-package with the logic tile. So they are working with, say, TSMC. Samsung is probably doing it themselves, because they also own a logic process.

We are a few years ahead because we came up with a recipe for taking a DRAM tile and a logic tile, packaging them, and getting to market quickly.

And the aim is the end of 2027?

By the end of 2027, we’ll have silicon powering up inside an Nvidia rack. That’s the goal, yeah.

Talk about how important the NVLink Fusion partnership with Nvidia is. It gets you up to speed much more quickly because you don’t have to do all that other stuff, right?

That’s right. That is exactly the reason we did it. As you said, we are a few years ahead, right?

We don’t want to squander that lead by having to go reinvent stuff that somebody has already invented. I could go build our own rack-scale infrastructure with liquid cooling and all that, but that would take me another two or three years, and somebody’s already done it. So the NVLink Fusion partnership is really about solving two problems.

One is time to market. How quickly can I take my Raptor technology, the 3D-stacked technology where I have a few years of lead, and integrate it into a rack-scale infrastructure that is fully deployed at scale. So one is just time to market. Let me take advantage of somebody who’s already done the work. Number two is scale. How quickly can I deploy it across a large portion of the market and make it really frictionless for customers to use this technology in a very meaningful way?

From the perspective of an outside observer just getting up to speed, it sounds like Corsair is nice, but the company is a bet on scaling Raptor and 3D-DRAM and becoming a much bigger success, because you’ll have a larger technological advantage.

That’s absolutely right. We’ll have a much bigger footprint and a technological advantage. Corsair proves out our thesis. Memory-centric compute is very relevant for inference, because a lot of applications that need low-latency compute and high levels of interactivity need that type of compute, and that has been proven out. Look at the Groq acquisition and the Cerebras IPO. They are all SRAM-based solutions. We have an SRAM-based solution, and it is still very relevant in the market today. There are lots and lots of customers and applications that don’t have enough of this fast compute.

Let’s say, theoretically, you hit your milestones and Raptor comes out at the end of next year. Why would it be so much better than Cerebras, Groq or GPUs? There’s a ton of inference work going on. OpenAI is working on Jalapeño. Why 3D-DRAM, and which use cases will work best for it?

Because there are so many different inference solutions out there, the easiest way to understand the inference world is to tie it to the memory technology. Again, it goes back to what I just told you. For inference, you need memory capacity and memory bandwidth.

The first question I typically ask is for your inference acceleration technology to be successful, what kind of memory technology are you dependent on? If it is HBM, there is a whole slew of companies betting on HBM, and that is solving for a certain point on the inference Pareto curve.

If you look at the curve, there’s throughput on one end and interactivity on the other. Throughput and interactivity pull in opposite directions, right? Throughput is the amount of work, and you need more time to do more work. Interactivity is how quickly you can do it, which means you probably can’t do as much of it.

You can’t have a solution that does both equally well. It’s impossible; it’s just physically not possible. HBM-based solutions do very well on throughput. GPUs have been HBM solutions, and they do extremely well on throughput. And there’s a whole bunch of HBM accelerators that are very good on throughput.

We are not in that bucket. We are not necessarily the high-throughput guys. We are playing on the very high-interactivity side.

So we don’t use HBM. We use SRAM and 3D-stacked DRAM. We are intently focused on optimizing for memory bandwidth as the first problem and then memory capacity. The point on the Pareto curve where we are playing is very different.

There aren’t many companies playing there today. It’s really us, Groq and Cerebras. Those are the three you can think of. Then there are a few others using LPDDR technology, for instance, to optimize for a totally different point on the Pareto curve around cost.

But that’s still a throughput play. So you have all these different points, and we are not at those other points, because we are heavily focused on optimizing for interactivity. The kinds of use cases that benefit are anything where someone is looking for a highly interactive AI experience. That’s anything agentic. Coding agents, cybersecurity agents.

The way we see it, the bulk of AI applications will care about interactivity and latency. That’s where we play.

Personal digital agents over voice are a great use case.

That’s right, voice agents are a use case. Anywhere humans get involved, latency matters. I would say 70% to 80% of applications are going to be latency sensitive.

We see this becoming the largest portion of the inference market over time. Not so much today. Today it’s heavily batched, throughput-type applications, but over time it’s going to be latency.

Thanks for your time.

Key Context by Tae Kim is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.
