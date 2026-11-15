---
title: "Hot Chips: Google 8th Generation TPU Presentation"
source: "Key Context (Tae Kim)"
author: "Tae Kim"
url: "https://taekim.substack.com/p/hot-chips-google-8th-generation-tpu"
published: "2026-09-03T00:24:56+00:00"
words: 1799
preview_only: false
---

# Hot Chips: Google 8th Generation TPU Presentation

Note: I’ll be taking my first vacation of the year next Labor Day week, September 7 to 11. -Tae

Presenters: Norman Jouppi and Sridhar Lakshmanamurthy at Hot Chips conference on Tuesday, August 25, 2026.

Here are the most important distilled parts of the presentation. I manually chose and pulled the quotes:

Prior to Google, Norman was one of the principal architecture and designers of MIPS. He’s been the tech lead for TPU since 2013. Sridhar is a senior director in the AI and infrastructure group at Google where he leads the TPU chip architecture team.

First speaker: Norman

“The first TPU was optimized for inference and it was just a PCIe card.”

“Over the years, up until recently, we’ve generated or provided a million-fold increase in performance. So we’ve roughly alternated between inference TPUs that also work well on training and training-optimized TPUs that also work well on inference.”

“So what’s new about the 8th generation TPUs? Well, in the past, we’ve come out with one chip a year, one for inference, the next year for training .. but now we’re introducing two chips a year. Due to the wider range of applications, we’re seeing needs for more differentiation between the inference optimized design and the training optimized design.”

“Some of the examples are large scale pre-training with a hundred thousand or more chips, down to small models for inference with just a couple of chips, distillation in the middle, sampling mixtures of experts and agentic models. Now, the last two things are very important because mixture of experts requires a lot more communication than we’ve seen in earlier models. So it’s relatively easy to scale the flops, but it’s harder to scale the interconnects. So we spent a lot of work on scaling the interconnects in this generation.”

“And, of course, the agentic models is the buzzword. And what that basically means is that ML systems become part of a larger data center system.”

“You need to compile things on the CPU, for example, if you’re generating code. So it’s a much more complicated problem than just building a fast accelerator or a fast accelerator rack. You’ve got to think at the data center level now. We’ve built this generation to handle long context windows for agentic AI. And again, we need that better high-performance connectivity to both storage and CPU compute.”

Key Context by Tae Kim is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

“Inference needs more HBM bandwidth per compute.”

“Inference needs more SRAM, a higher percentage of SRAM than compute.”

“So [TPU] 8i is the powerhouse for low latency inference.”

“If you look at pricing models for serving on various platforms, the price goes up dramatically as the latency goes down. Users want results really fast. If you’re doing a search, you want the Gemini answers as fast as you got the regular old-style Google results, but with a lot more intelligence and links to references.

So in order to do that, we have a much larger SRAM than we ever had before, 384 megabytes. We increased the HBM capacity and also the bandwidth. And we’ve doubled the ICI bandwidth. And that’s important when we have mixtures of experts.”

“3D tori are better for training because in training bandwidth is what really matters.”

“And so if you look at the diagram on the lower right, you can see that when you put them into a kind of a rectangular prism, that there’s huge bisection bandwidths created in the different directions. And this is really good for training.”

“Whereas the boardfly networks in general, have lower latency. So that’s really important for the inference. As an example, the boardfly network for TPU8i has a maximum of 7 hops, whereas the 3D Torus could have, depending on its size, for example, 16 hops. So we want to minimize the number of hops.”

“And then we also want to minimize the time that each hop takes. So the reason for that is we want to perform in network collectives efficiently. And we have an IO die and two compute dies, which are mostly SRAM.

And in the past, we’ve done what the figure on the lower right-hand corner is, where we go from the comms die at the bottom across potentially the whole package, access some data from an HBM, and come back out.”

“So we do the actual collectives in the IO die itself, and that saves us the time of transferring the data all the way up, potentially to the top of the package and back, and it saves us the time of doing the HBM access. So that reduces the on-chip latency by 5x. So we have fewer hops and 5x faster on-chip reductions.”

Point of emphasis: Reducing the latency and number of hops allows the TPU 8i to server mixture of experts models faster, a key deficiency of the prior TPU 7 - Tae

Second speaker: Sridhar

“Training is really hard. It’s really hard. But at Google, we’ve always taken on the hardest challenge head on. Last year, we were here on stage, and we talked about Ironwood, 9,216 chips in a super pod. Guess what? As we speak today, our customers are training their largest frontier models on tens of Ironwood super pods. It’s happening today.”

“And we didn’t want to just rest on our laurels, we wanted to raise the bar. Why? Because as we look ahead in the next year plus, our customers want to train even bigger models, trillion parameter, tens of trillion parameter models, and do it efficiently and do it in a very timely manner.”

Tens of trillions parameter models!? -Tae

“A chip just dedicated for training so that we don’t have any dark silicon that we regret and say, oh my God, I put this in, but I’m not using it when I’m training. I put this other feature in, and I’m not using it when I’m serving. Because what happens is we are limited by the power budget. We are limited by the packet size. So we want to really optimize the area that we have to essentially build the best chip possible.”

“Our customers’ ambitions are even bigger. They want to be able to train 5, 10, 20 trillion parameter models over the next few years, and they want to train over a million TPU chips. So what this meant was really we had to reimagine the scale-out network that we were using for our TPUs.”

“8t, we are introducing the Virgo network. This is a purpose-built, ML-optimized scale-out network that can support up to 14 AT super pods. So basically one single fabric, non-blocking, that essentially supports a staggering 134,400 TPUs in a single domain. And since it’s purpose-built for ML, we’ve essentially created a two-layer switch network that is the most optimal for latency because in a large training job, what you really need is any two nodes across two pods to really communicate at the lowest latency possible.”

“So this Virgo network also supports redundancy and reliability and seamlessly scales to WAN so that we can actually connect multiple data center sites to be able to really train, allow our customers to train at planet scale.”

“Once our customers invest this much infrastructure, they want to make sure that this system is reliable and is available. And so that’s been a key priority for us. So again, these chips are going to be flaky. So essentially, we’ve spent a lot of innovation in improving things that fall apart very quickly. And HBM is one of them.”

“At Google on the ML supercomputers, we’ve been deploying liquid cooling for almost a decade now. And what we’ve learned over this last decade is that liquid cooling not only helps us with performance, but it also helps with reliability. How many of you here have heard of the Arrhenius equation?”

“Our customers really care about Arrhenius equation. You know why? Because what it says is the failure rates exponentially increase with temperature. For example, semiconductor devices like HBM memories and so on, their failure rates can double or sometimes even triple, even with a 10 to 15 degree increase in temperature.”

“So although it may be tempting to kind of skimp and cut corners on your chillers, we believe the right thing to do is really to essentially co-invest in the best infrastructure and ensure that we deliver the best reliability adjusted for TCO for our customers.”

Q&A

Question: From the network topology standpoint, is there a reason why you have kept it as 3D Torus for training chip? Because there are hops or more. I saw that for the inference chip you have changed it, the network topology.

Answer: Well, it’s 3D Torus for the training. Right, that’s right. In training, bandwidth is what matters, and so it’s not latency. So that’s why we’re using the fly for inference, because latency is important. And when you have a large rectangular prism, the bisection bandwidth is ginormous.

And also compared to our Ironwood generation, we’ve doubled the ??? speed. So essentially that helps us to kind of keep up with the bandwidth demand of the new MOE models.

Question: For TPU v8, is Google’s internal workload still the primary design target or are external customer requirements now a major design consideration?

Answer: I would say both. We’re essentially building for the world.

Question: My question was regarding the training chip. What drove the decision to stay on HBM3E for that chip and not HBM4? Was it a supply or cost consideration? And do you think that the HBM bandwidth is currently not the limiting factor? Do we expect the 8t to have an intergenerational move up to HBM4, or do we have to wait for next year?

Answer: Think about the training problem, right? The training problem is running on not just one chip or four chips or eight chips. It’s running on 200,000, 400,000 chips. So at that aggregate, I think what matters is the connectivity across those number of chips, not the bandwidth per chip.

And that’s exactly why, as Norm showed the picture, right, so we actually built a chip that doesn’t have to push on every vector. Because if you build just one chip, yes, we’ll have to push on every vector. But when you’re building two chips, we can decide how to optimize each chip for that specific use case.

Tae: If you want to know what the Hot Chips presentations mean for investors, [read my Hot Chips conference key takeaways post](https://taekim.substack.com/p/hot-chips-conference-initial-5-takeaways) from last week.

Key Context by Tae Kim is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.
