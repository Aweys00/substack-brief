---
title: "An Interview with Microsoft’s Scott Guthrie on Azure’s New AI Chip, ‘Insatiable’ AI Demand and Today’s AI Model Price War"
source: "Key Context (Tae Kim)"
author: "Tae Kim"
url: "https://taekim.substack.com/p/an-interview-with-microsofts-scott"
published: "2026-10-12T13:48:56+00:00"
words: 3215
preview_only: false
---

# An Interview with Microsoft’s Scott Guthrie on Azure’s New AI Chip, ‘Insatiable’ AI Demand and Today’s AI Model Price War

Microsoft is amping up its AI chip game.

On Monday, the company announced plans to expand its Azure Maia AI chip program to multi-gigawatt-scale deployments starting next year. Microsoft also said its next-generation Maia 300 chip will deliver 40% more tokens per megawatt than leading GPU-based competitors and will begin production deployments in 2027.

Microsoft is a giant hyperscaler and one of the world’s largest buyers of semiconductors and AI servers.

Key Context recently spoke with Scott Guthrie, Microsoft’s executive vice president of Cloud and AI, about the insatiable demand for AI infrastructure, the new Maia 300 AI chip, CPU demand and the current frontier AI model price war.

Perhaps no one understands what is happening in the AI industry today better than Guthrie. When I last interviewed him at Barron’s about a year ago, he was remarkably prescient about the explosive infrastructure buildout to come and the rise of agentic AI.

I fully expect that a year from now, we will look back on this conversation the same way, particularly his comments on AI cybersecurity trends and the rising demand for various components. I highly recommend reading the whole interview.

Here are lightly edited highlights from our conversation. I bolded the remarks I found most important:

Tae: What is the significance of the Maia 300 announcement?

Scott: We’re super excited about Maia 300 and the Maia program overall.

Stepping back, I think the key thing we’re trying to do as a company is how to be multi model. We’re supporting multiple models, including OpenAI, Anthropic, and our own first-party models. We have infrastructure around the world, including in all the countries that need sovereignty. There are more countries than ever in the world that want that.

We want to both embed the models in our applications and solutions. Enable customers to build their own applications with them, and then you know have a common, consistent security and compliance control plane, and really provide that trust that customers expect, which is their data is their data. They can build applications safely. They can deploy this AI safely and with sovereignty.

Ultimately, we want to make sure we have the capacity. And then importantly, the tokens per dollar from a TCO perspective to be leading price performance, and from an overall ROI perspective.

That’s where the silicon program in Maia comes into play because the more we can drive down the cost of inference, the more we can pass on savings to our customers. The more throughput we can get per watt, then ultimately the more capacity that we can deliver as well.

We have Maia 200 in production today. We’re super excited because we finished the tape out, and are announcing Maia 300, which is the next major evolution. That’ll start to go into broad scale deployment next year. Maia 300 is really when we’re expanding the program in a big, big way.

We do healthy volumes on Maia 200, but Maia 300 is when we will take it up a level. We will use it for our first-party offerings, which we’re already using with Maia 200. But then also for third-party with Foundry and our API service. An awful lot of people that are using the APIs from us and will ultimately be using Maia chips under the covers, benefiting both from the performance as well as the improved ROI and TCO benefits that it provides.

Tae: Is multi-gigawatt for next year, or is that broader over several years?

Starting next year. I think for Maia 300 in particular, we’re going to start deploying it next year. It’ll be a ramp. So I don’t know the exact time frame for when we’ll get to multi gigawatt. But basically from a supply chain perspective, we’re ordering a lot of Maia 300 chips. The supply chain is going to be seeing this in earnest, which is partly why we felt comfortable sharing the number.

And then, Maia 400 will come after 300, and 500 will be coming after 400. This is an ongoing program.

Tae: How do you think about using the different AI chips? Obviously, Microsoft is a big buyer of NVIDIA chips. AMD is in the picture. Is it whatever the customer asks for?

Yeah, we’re big partners of NVIDIA and AMD, and we’ll continue to be big partners of them. We’ve had great success with them and that partnership is multifaceted on many different elements.

Similarly, we’ve had a great partnership with Intel and AMD on the CPU side. Cobalt is our equivalent. CPUs, I would say are even a year ahead. We’re starting the ramp this year on Cobalt in a big way and getting to hundreds of millions of cores with Cobalt. But we’re still going to buy a bunch of AMD and Intel CPUs as well.

The same is going to be true for Nvidia and AMD. Even with OpenAI, we do partner with them on their own first party silicon program. We are trying to make sure that we are big tent in the same way that we’re multi model, we are multi silicon.

But we think there are unique things that we can do with our first-party silicon both from a capability perspective and in particular from a cost perspective that gives us some good advantages. It’s one of the reasons why we’re going so big with Maia.

Tae: There is a lot of debate about chip architecture between disaggregation and more flexible generalized chips. Where does Maia fit in? What were the tradeoffs that were made?

Well, from a Maia perspective, we are using AI heavily to build Maia. We’re big believers, obviously, in AI to build things. And then we really optimized Maia for large language model AI.

I think there we’ve seen, if you look at the latest models and the reasoning models, a heavy memory footprint. They use a lot of memory and the throughput is often one of the limiters. So it’s not just how much memory you have, but the aggregate throughput per second to memory makes an enormous difference in terms of the overall performance and subsequent TCO.

Because if you’re stalled on throughput, your tokens per dollar goes down, and if you have a tremendous amount of throughput, it goes up. And that’s one of the reasons why in the press release you might have noticed we quoted some of the statistics in terms of terabytes per second of memory bandwidth and the amount of memory that we have in terms of latest HBM. Both of those are part of the contributors for why we have such great performance and TCO with Maia, and are one of the key differentiators for it versus others in the market.

Similarly, the network and the scale up is another area that we’re going big on with Maia that we are finding really helps with large models.

And the Maia silicon instruction set is fairly generalized, so it can be used for both prefill and decode. And it supports a broader set of scenarios than say a TPU, as an example, and is not tied to any single model. We already have both OpenAI models as well as our Microsoft AI models running natively on top of it.

Key Context by Tae Kim is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Tae: I noticed in the blog post you said less data movement is a critical part of the improvements. Can you expand upon that?

I think from an architecture perspective. The extent that you don’t need to move data between nodes, and instead you can get more density in a single place and do more computation on top of that. That does translate directly in terms of improvements on tokens per dollar, and then rough raw token throughput period.

If you look at the memory capabilities, both in terms of total amount, but then especially the throughput between the compute and the memory. And then also the scale up networking specs. I think those are probably two of the biggest areas where we’ve been able to minimize data movement and ultimately directly improve raw throughput and TCO.

Tae: What are you seeing in the CPU space? Demand for CPU seems to be taking off because of agentic AI. How are you managing that?

We’re seeing certainly with the agentic and long running agents in particular, we’re seeing a huge rise in terms of the need for CPUs. You’re also going to see from a security sandboxing perspective, a need for quickly spinning up and spinning down workloads on top of CPUs.

And so we’re investing very heavily, not just with Cobalt in general, but from an architecture perspective, how do we get to sub-second hypervisor-based VM activation teardown, so that you can actually have a very secure perimeter around the agents that’s hypervisor-based. As the models get richer, you’re going to really want to have VM level isolation around that workload that’s protected by a hypervisor with a very small API footprint surface area. The speed to create and tear those down is going to matter and how close can you can get them to the silicon is also going to matter.

Similarly, we’re seeing a tremendous amount of demand for storage. I think you’re going to see hard drives and SSDs be in short supply over the next couple years because these agentic workloads love data, they love storage, they love to be able to create data, and you know more and more is going to be logged in terms of prompts and outputs and so forth. And so, I think you’re going to see an insatiable demand for storage and compute and GPUs, all of which need data centers and power.

It is very much an end-to-end infrastructure problem, and we’re trying to design really the end-to-end system to do that. And so, with Azure obviously being the software control plane fabric that kind of orchestrates it all, and then within our hardware programs, we do have distinct teams for Cobalt and Maia, but they’re part of the same broader hardware team. And on the supply chain team, we have one supply chain team for all of our server components, and that is allowing us to get synergies across our organization and across the design, so that we really build it as one integrated system.

Tae: One year ago, you predicted there’s this wave of AI infrastructure demand and the supply demand imbalance where demand was much higher than supply. What’s your outlook over the next year? What you’re seeing in the AI infrastructure and Azure pipeline?

Yeah, it’s still, we’re definitely seeing a lot. We continue to see that that growth. So from that perspective, I don’t think there’s really been any change, other than you know a year later we have a lot more in the denominator already.

But from an overall growth perspective, I think the world still has a fairly insatiable demand for more capabilities. And I think a big change is the models have gotten a lot better in the last 12 months.

When you have reasoning models that can complete more tasks autonomously or complete more end-to-end tasks. You also find if you need to have a human approve something twelve steps of the way. You’re then gated on the humans to do stuff.

To the extent the model can do all those twelve steps and then show the finished result, you know you can do a lot more, and more importantly, you get a lot better return on investment if you’re automating a specific task or a business process. And that, in turn, with Jevons paradox creates yet more demand.

Because if the return is that much better for automating things, you tend to automate more. And so, I do think we’re also finding that as the intelligence gets better, the business outcomes get stronger, the demand increases.

Tae: What is going to happen over the next six to twelve months from the AI model and AI model vendor side? Give us a flavor of how you expect the capabilities to advance?

Today everyone would say if you look at engineering and coding, clearly AI has broken through, and pretty much every organization is looking to leverage AI for coding and for engineering. And people sort of just assume it’s a given from a productivity perspective.

You’ll see in the next few months ahead, the same is true for security and cyber security. I think every organization is either using AI today for security or will be shortly. As more bad actors use AI, the only way to defend against that will be actually to use AI more on the defense as well.

I expect similarly to kind of how coding is a horizontal across every organization. I think you’ll definitely see cyber being another horizontal that is going to drive a lot of demand, and then I do think you know you’re starting to see other areas, whether it’s mathematical problems, which obviously can then translate into things like forecasting or financial services or supply chain or other workloads.

We’ve seen tremendous amount of adoption of AI in healthcare, both in terms of clinical documentation when doctors talk to patients, but also things like radiology. We’re starting to see it being used more heavily in pharmaceutical research and drug discovery.

We’re seeing it used more and more in the creative space. Whether you know, including for videos and music and things like that. So, I do think you’re going to continue to see both what I call like horizontal use cases, like coding, like cyber, that every organization adopts and then I think you’ll see more vertical scenarios that are industry specific that’ll become standard as well.

As these models get richer, and as with agents, you can just give it a task and it goes off and works and a few hours later, you get a polished, finished, high quality response.

You will find that the demand keeps increasing because as long as there’s a good return, as long as you get more than a dollar’s worth of value out of putting a dollar into the system.

Tae: How do you think the personal and enterprise digital agents OpenClaw, Muse and now Microsoft Autopilot will ramp? What is the potential?

I do think it’ll take off. The trick will be what’s the use case that delivers a business return. AI is expensive, it’s not free.

Different businesses gravitate towards the use cases that help them automate and do things. For example, we’re using it in a variety of internal workloads.

Where historically we would have to wait on someone in the organization to do something and either we didn’t fix things, we weren’t able to take advantage of an opportunity as fast. To the extent that we can have an immediate response, and it’s a really good response, that makes us provide better services and ultimately get more revenue for the business.

I think you’re going to find that organizations increasingly adopt more of those types of use cases, and they’ll gravitate towards the use cases that give them the most differentiation or the most return.

And again, I think coding is a good example where people are doing it today. And I think cyber is a good example where most large organizations are now using these models to look for cyber vulnerabilities in their estate before an attacker finds them.

If you can fix the vulnerability before a bad adversary exploits it, you know that saves you like a thousand to one return versus having an attacker point out the problem for you in a cyber incident.

There’s good examples where we’re seeing these this type of productivity and this type of win. And I think you’re only going to continue with things like Autopilot and the OpenClaw like scenarios.

Those are all examples. I think of the technologies that enable these next generation use cases. Where the ROI is even more significant than a traditional chat scenario.

Tae: How does Microsoft think through when you’re selling Azure AI services, using OpenAI versus Anthropic versus internal? How is that decision made for each customer?

In some cases, customers have specific asks in mind or specific use case, and one model is better than the other. I think also you’re seeing this is a dynamic space.

And if you go back over the last 12 months, I think the world thought that OpenAI was the best model out there. I think if you looked in November [of 2025], December, a lot of people say, Hey, Gemini looks like it maybe is now the best model and lapped OpenAI.

Fast forward to March, people are like, no, no, Anthropic’s the best model.

And I think if you look in the last six weeks, people are saying, hey, [OpenAI] Astra and GPT 6.1 seems like a really good model, and maybe that’s now the best again.

So you’re definitely seeing, at any point in time, in a twelve month period, who has the best model is fairly dynamic more so than any, almost anything I’ve seen in tech in the last twenty or thirty years. Who’s in first, second, and third is just adjusting very, very quickly.

So I always tell customers and partners the nice thing about Microsoft is we’re betting on all of them, and so when you buy Copilot, you can use OpenAI, Anthropic, and our own first-party models. And I think you should expect that the market is going to remain dynamic on the frontier, and what is best for what task is probably going to be somewhat dynamic. And by betting on a harness that’s open and betting on a multi-model solution you can take advantage of whatever the best model is out there.

Then also I think the thing that you’re seeing in particular the last few months is there’s a real price war going on where model costs are coming down, and so again to the extent that you have that flexibility to be able to use multiple models like you do with Copilot and with Microsoft solutions, you benefit from that price war versus if you’re locked into a specific tool or locked into a specific model. You might still benefit from some price wars, but not as directly as if you have switching ability.

And you know we have ability to do auto, and we pick the model for you, and you have the ability to pick the specific model. And we think of that as a feature and a capability. Then with our own Microsoft AI models, we’re going to go after these use cases where we think we can provide even more differentiation from a cost perspective.

And then tying it back to Maia, Maia supports all the models. It’s another example where we’re looking to the price curve and deliver the best AI in an open way that’s multi-model with the best TCO.

Thanks for your time.

Key Context by Tae Kim is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.
