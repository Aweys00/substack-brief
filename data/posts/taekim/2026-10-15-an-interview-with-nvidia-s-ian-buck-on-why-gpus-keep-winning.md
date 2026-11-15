---
title: "An Interview with Nvidia’s Ian Buck on Why GPUs Keep Winning"
source: "Key Context (Tae Kim)"
author: "Tae Kim"
url: "https://taekim.substack.com/p/an-interview-with-nvidias-ian-buck-975"
published: "2026-10-15T00:02:22+00:00"
words: 3781
preview_only: false
---

# An Interview with Nvidia’s Ian Buck on Why GPUs Keep Winning

Agentic AI is changing everything including at Nvidia.

Key Context spoke with Ian Buck, Nvidia’s vice president of hyperscale and high-performance computing, on Tuesday at the OCP Global Summit in San Jose. We discussed why companies continue to choose GPUs over rival chips, how agentic AI is changing the industry, the dynamic between open and frontier AI models, and how service providers can fit 30% more GPUs into the same data center footprint.

As the inventor of CUDA, Buck is one of the most important figures in Nvidia’s history. He oversees the company’s AI hardware and software products deployed with hyperscalers and other customers.

I love nerding out with the most brilliant people in the AI industry and once again, this Q&A is packed with technical details and insightful nuggets. I’ve bolded the remarks I found most important.

Here are lightly edited highlights from our conversation.

Tae: Every year brings another wave of hyperscaler ASICs. Just this week, Microsoft announced Maia 300, and there’s also Amazon’s next Trainium and OpenAI’s Jalapeno. How is Nvidia competing with these new chip rivals?

Ian: Every generation, we deliver more tokens. We are more capable on a larger, more diverse set of models. On top of that, it’s not just about performance, but about dollar per token and bringing down token cost, as well as performance for the next generation.

That’s why we do benchmarks like [SemiAnalysis] AgentX and InferenceX, and MLPerf. Artificial Analysis has gotten in the game.

You can see the performance over time. It’s a continuously improving platform. I think we’ve improved our performance on Blackwell fourfold since we first launched it.

With Vera Rubin, OpenAI’s Sachin [Katti] said the first time they ran Astra on Vera Rubin, they immediately saw, out of the box, that it was 3X faster. Then, 72 hours later, they let Astra optimize itself in a fun little agentic way, and they got another 2X. So 6X total, compared to Blackwell.

That immediately turns into more tokens, more capabilities, lower costs for the existing services, and new, more thoughtful, intelligent, token-consuming agents brought to market in an economical way, so they can make money and help other people across the industry make money.

That’s Nvidia’s mission, and we’re now doing it every year with Vera Rubin, Vera Rubin Ultra, then Feynman, Feynman Ultra, and beyond. We do it end-to-end. We’re one AI company that talks to every other AI company, because their business is to bring their latest capabilities, models, and technology stack at reduced cost, within a fixed power envelope in a constrained data center environment.

We’re taking all those ideas and integrating them into the roadmap quickly. We don’t tell you what Feynman is because we’re still inventing it and still integrating all those technologies. We can incorporate, adopt, or improve the design and roadmap.

At OCP, the goal is to build a rack and hardware infrastructure platform, MGX, that gives everyone in the supply chain a platform to invest in, invent on, and build up manufacturing. And it’s forward-compatible with those future systems.

The stuff I talked about yesterday, 800-volt power, supports the racks today. It improves efficiency, resiliency, and reliability, but it can also scale up to one-megawatt racks when we get there. Liquid cooling, plumbing, and connectors. I’ve learned a lot about connectors. That’s how we do innovation, and where we can guide this industry.

It’s not just Nvidia. We do it with AMD, we do it with Google, we do it with Microsoft, we do it with Meta, to lay out a future and give flexibility for a platform of innovation.

In terms of the broader computing market and how we think about everyone building on silicon, Nvidia has three [points].

One is the productivity of our platform. The second is the fungibility of that platform. And the third would be the durability of the platform. So let’s take those three.

Productivity. Immediate productivity, gen over gen over gen over gen, because we still run those CUDA 1.0s. The productivity is immediate. Not to mention there are 20 years of accelerated computing to draw from in terms of papers and research. The latest techniques get implemented on our platform, and they immediately get transformed into libraries or common knowledge among AI researchers, or integrated into software stacks like PyTorch, JAX, Dynamo, vLLM, or SGLang.

And now they’re being incorporated into agents, so the agents now have 20 years’ worth of knowledge to apply to mapping and getting the most token efficiency. It’s extremely productive.

Fungibility. The Nvidia platform is used for training. It can be used for reinforcement learning, pre-training, and post-training. It can be used for inference and it can be used for accelerated computing. Agents are now trying to run simulations to figure things out for industrial use cases. It’s the same GPU that’s running the inference for the agent as well as running the latest Ansys or Blender software.

Accelerated computing is used everywhere in computing. And that asset, when you buy a billion-dollar data center and fill it with billions of dollars and hundreds of megawatts of GPUs, is a fungible, tangible asset that can be used for the broadest market of computing.

That gives us resiliency, gives us confidence for investment, and makes it easy to finance. That is one of the reasons why you’re seeing this explosion of new NCP cloud players that can serve the market.

The third is durability. The GPUs are going to be contributing value even long after Nvidia stops manufacturing or selling them. CoreWeave is still serving and using Volta GPUs, the original GPUs they bought in 2019, to serve the market. They use them for things like call transcription, and they are also using them for acoustic modeling for one of their customers.

They’re sold out. Their value has grown by X-factors in terms of what they’re able to charge as a service to those companies, and that usefulness continues for a GPU they bought back in 2019.

So that productivity, that fungibility, and that durability are among the things that establish us in the market. And every hyperscaler, every cloud company, and every AI company knows and appreciates that, and knows that when they’re buying a data center full of Nvidia GPUs, it’s an investment for the entire company.

Key Context by Tae Kim is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Tae: Personal and enterprise digital agents are a big focus right now. How are these agents changing AI demand today and how will they shape AI infrastructure over the next year?

How we measure the productivity of AI infrastructure has changed demonstrably. A year ago, you would ask me, what is the token performance of Blackwell on GPT-OSS? And you’d say, yeah, for 1K worth of input tokens and 8K of output tokens. Just the token speed of a model. You can’t ask that question anymore, because with agents, every question is different. The workload is flying all over the place. The input and output tokens are totally different.

With agents, context memory is way more important. When you’re asking an agent to be your person, it needs to know everything about you, all your history, so that you don’t start from scratch every time you open up a new ChatGPT session. And as it’s learning about your interactions, it’s actually getting smarter, so the next time I ask it that question, it can build on that. Context really matters.

You have to benchmark and understand inference at an agentic scale. That’s why we have AgentX and the Artificial Analysis agent benchmarks. They model diverse token loads, query patterns, and also KV cache management and movement.

This is why Dynamo, our software that started as a disaggregated inference serving solution, has actually become like an operating system for managing inference, KV, and agents across the entire data center. It smartly moves KV and replicates it across the data center when it schedules work. It knows which model is running on which GPU, which ones are going to finish quickly, and which have more load because of their input, output, and KV length.

Actually, all the optimizations you run in the model are a function of KV size plus the input size plus the likely output size. So it’s not just one version of the model that’s been coded up in CUDA. Inference got a hell of a lot harder when we got personal agents, and it actually gave us a whole new landscape to optimize.

Tae: Does that also include CPU and storage racks?

Yeah, so we now have to bring all that together. Storage has gotten super hot again because we want to be able to smartly and quickly pull your KV directly out of a storage plane into the right node that needs it, and also put it back smartly so you’re not wasting time. You also have to do that securely, so the information has to be secured and sandboxed safely.

If you are an AI lab, you’ve got to make sure that your storage plane is secure so you’re not leaking your customer information or your model information out.

And then with agents, of course, you now have to call the CPU to do tooling. CPUs matter a lot now. It’s not like the old dollar per CPU that the cloud has been pushing for the last decade, where it’s all about cost. How many can I serve? The dollar per CPU core hasn’t gone up all that much. What clouds are really good at is reducing costs. That means throwing more cores onto those chips. And if you make performance better, that’s nice, but the number one thing is dollar per core.

Agents flip that over again. In order to have a fast agent, you want your answer, you want a timely solution. You care about how fast your PCB layout tool runs, your compiler job runs, and your database search runs, because that would be the limiter.

You don’t want your GPU sitting idle, and your service is a function of your SLA. So Vera is not just for Rubin. It’s also for standalone use. We’re seeing huge adoption of our CPU across the board. It’s designed to be fast for single-threaded work, with every single core being utilized so you get high throughput.

You can run all the cores at 100% performance, the same performance as just one core. Agents don’t have to compromise. The old cloud ones were designed to deal with the web.

They’d have a hot core ready for when a web request came in. They weren’t cranking math problems. They were just there for latency, so that your web business could grow and scale. So you optimized for cost and just made sure you had a hot core everywhere.

But man, if you turned on all those cores and actually had them do compute and fetch memory, they would immediately logjam in the memory subsystem. You’d hit that memory wall, or they’d start having to fly over those chiplet domains and slow down.

None of that happens with Vera. With Vera, we super-invested in the fabric connecting all the cores and the memory subsystem. So every core has over two terabytes a second of memory bandwidth to the core, which is crazy. You’d actually saturate the whole memory system with just 12 cores, and it’ll keep on scaling all the way up. Agents can safely and confidently use every core. The system can load up all of the cores without having to worry about the whole agent service slowing down.

OpenAI has already announced they are deploying Vera. There’s Anthropic, SpaceXAI, OCI, CoreWeave, and all the OEMs, and in fact, we now have liquid-cooled racks with Vera, with 256 CPUs fully connected. It has BlueField for all the security and OpenShell containment, so you have the safety of front-door protection as all the agents run on these Vera CPUs.

Tae: Have you seen a shift in the mix of demand across hyperscalers, neoclouds, sovereigns, and enterprises? Is any segment ramping faster than the others?

Oh, they’ve all been ramping [laughs]. They’ve all been going up. Hyperscalers obviously want to serve the market, and they can serve it at very large scale. And they have a geographical footprint around the world. As AI has been growing and agentic has been growing with those lead customers, their demand has been growing, as have their data centers. They’re also using our GPUs and our CPUs more internally for their own services, some of which they talk about and some of which they don’t. We bring a platform. They’re accelerating databases, they’re accelerating their model serving, they’re accelerating their ad serving, their customer management, and safety and monitoring, all using our GPUs and our CPUs to make this work. There’s a lot of internal consumption.

The exciting growth has also been those NCPs [neoclouds]. The market has matured enough, and we’ve supported it with a lot of our open software. In this new market, it’s not just CoreWeave. There are a hundred different NCP partners all around the world that are able to bring Nvidia infrastructure and capability to the AI labs, the startups, and even the enterprises, both as infrastructure as a service (rent a GPU, rent a CPU, rent a rack) and as inference as a service.

Tae: How do you respond to those who say AI is now advanced enough to write kernels, so the CUDA moat is shrinking? Or that AI can design chips, so Nvidia no longer needs to?

First off, we’re huge consumers of AI internally, both for developing and accelerating all of our platforms. There isn’t one team at Nvidia that doesn’t use AI to write software, make it better, make it faster, make a new kernel, make a new computer build.

In fact, we were one of the first to adopt this internally, and we’ve talked about that. We use it for our silicon, we use it to improve our yields, we use it to improve our entire software stack, and we use it to help our customers. To the point that now we’re actually building open models, Nemotron and other things, and helping OpenAI with Astra and others to build better code and capability to accelerate applications holistically.

AI doesn’t do that in a vacuum. It’s actually learning from all of the other skills and all the other work that’s been done to make our platform even faster. All GPUs and all architectures are not the same.

We’re obviously deeply working and innovating, and the craftsmanship that goes into creating that performance per watt makes Vera Rubin 45 times more token efficient. That is an end-to-end optimization of all the stuff that we’re doing.

GPUs are coming out even faster now because of AI. Nvidia is a consumer of that. Absolutely all the stuff you’re seeing us build, and our ability to accelerate our roadmap, is because of our own use of AI.

To go back to the sustainability part of it, in this business, the productivity, the fungibility, the durability of it, and the knowledge that is going to perpetuate there are just phenomenal.

I think there are lots of places where companies can contribute and develop their own niche accelerators for their own workloads. We’re no stranger to having partners who also build their own silicon, and they profit from our stack and value it immensely. We all agree.

Tae: Nvidia has guided to 70% revenue growth next year but has also said demand will be up 100%. That suggests demand far exceeds what Nvidia can supply. What bottlenecks are holding Nvidia back right now, and where can it loosen things up to meet that demand? Is it memory, power, land, shells, or wafers?

You should listen to [Jensen’s keynote next week in Berlin](https://www.nvidia.com/en-eu/gtc/). You can do it remotely. He will absolutely talk to these aspects of the things we’re doing.

I’ll give you one thing I talked about. The intelligent use of the power data centers are provisioned with. I still sadly run into people who decide, I have 100 megawatts, how many GPUs can I put in, how many racks can I put in? Well, what’s the power spec of the rack? And they do a simple divide. That works, but it’s extremely conservative.

In fact, it’s excessively conservative, because not every workload consumes the full max TDP of the rack. Often, in cases where you’re optimizing for revenue, you may want to dial in how many tokens per second per user and optimize. We also know that across pre-training, mid-training, post-training, and inference, the power consumption is never 100% all the time. That’s true for any data center. The thing is, that’s an opportunity.

We can tap into that provisioned power and use it more smartly. In collaboration with the grid, we should put more GPUs in that data center than the simple divide would tell you to. We’ve talked about doing things at a max-Q or max-efficiency power point, where maybe the rack is 120 kilowatts of total theoretical power, but a more efficient point would be 80 kilowatts. If you power-capped the rack and fixed it there, you should put in more racks, and you would actually increase your total throughput.

We can go even smarter. What if we actually looked at the power of a rack? It’s only consuming 80% or 60% of its total power from this port right now, for the next five seconds. We could set that cap there. If we had more racks, the CPUs are being used, the memory’s being consumed, everything’s humming, then we can drop in more GPU racks beyond just a max-Q cap, if we manage it all dynamically.

That’s what we’ve been doing. Both Lambda and, recently, Nscale did that. They basically ran a power profile using new software that we wrote and put in our DSX open library, called MaxLPS. It taps directly into the power monitor BMCs at every GPU, every compute tray, and every rack, actively monitors the rack power, and then sets it, so that when you put additional racks in that row and additional rows in that data center, you never exceed the total power of a row or the total power of the entire data center.

They were able to increase the number of GPUs in the data center by 33%. Thirty percent more GPUs is 30% more revenue straight out of the box. In fact, what they did was add this 30% to the most valuable use cases, and they netted out a total of 50% more revenue for the data center where they did this work.

MaxLPS will actually dynamically move work around. It taps into the scheduler to route work to where there’s power, so as to maximize total revenue.

We’ve done this before in supercomputing and in one-offs. Now we’ve open-sourced all that software, and pretty much every NCP is now adopting a MaxLPS strategy where they’re dynamically routing power and dynamically managing the fleet, so they can pack in even a third more GPUs, increase revenue by 50%, and serve more tokens. In fact, Meta just published a paper on their strategy for how they do this, which is very similar, with their own software. We’ve just open-sourced it, and it’s part of MaxLPS.

It’s pretty cool, and actually, I don’t think it’s been fully recognized by your audience [He means investors!] that the opportunity for incremental demand in existing data centers today, without retiring any GPUs, is another 30% to 40% of GPUs. Whether that’s been modeled in, I doubt it.

Tae: At GTC earlier this year, I attended several sessions where companies talked about using fine-tuned versions of Nvidia’s Nemotron. How do you see the dynamic between open-source and frontier models playing out? What are customers doing now, and what do you expect them to do in the future?

We’re still traveling at light speed to find the frontier. You can see that with the innovations coming from those AI labs, and they are absolutely world class at what they do. They’re bringing it to market through services, through products. It’s amazing.

Open models are also providing an opportunity for the entire enterprise to take advantage of the AI revolution, and they are delivering at the frontier. You can see that. They may be a quarter, two quarters, or three behind, but they’re just as fast moving.

And Nemotron comes at a perfect time in the market as enterprises are expanding. People want to own their own data, they want to be able to build their own models and have their own IP, but they want to build it off an open model, one that’s built in the U.S., one that is actually fully open. If you look at our open scores, we are the most open model out there around the world that has that level of intelligence, and we’re investing in building new models. We’ll hear more about the next Nemotron.

In addition, we open source the full training recipe and all the data, so if you want to build it from scratch, you can. We take our existing weights, and then we release all the software tools for you to fine-tune it, guardrail it, and attach it to an agent, and all that software is also open source.

Some companies have the expertise and talent to take the tools and libraries and build their own internal stacks.

Or the NCPs, and now the inference service providers, are actually taking our stack and turning around and building a service out of it, so that companies that may not have machine learning or AI teams that know how to do this can immediately work with CoreWeave. They use the NeMo stack, plus their own innovations and tooling, for helping enterprises get from point A to point B to build a service.

So open models are a great way to expand the footprint of AI. This is a rising tide. I work with all the AI labs out there, and they’re amazing. The products they’re building are incredible.

There won’t be one model that rules them all, obviously, and open models right now are allowing a thousand flowers to bloom. Nemotron is certainly one of them. We’re super excited about our U.S. model that is completely open for folks to use.

Thanks for your time.

Key Context by Tae Kim is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.
