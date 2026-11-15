---
title: "Hot Chips 2026: Interviewing IBM's Christian Zoellin & Christian Jacobi"
source: "Chips and Cheese"
author: "George Cozma"
url: "https://chipsandcheese.com/p/hot-chips-2026-interviewing-ibms"
published: "2026-08-30T17:31:05+00:00"
words: 2273
preview_only: false
---

# Hot Chips 2026: Interviewing IBM's Christian Zoellin & Christian Jacobi

Hello you fine Internet folks,

Today we're at Hot Chips 2026! We join IBM to talk about their just revealed Dual-ISA z/ architecture + ARM design with Christian Zoellin, the Core Design Team Leader and Christian Jacobi, the CTO of Systems Development!

Hope y’all enjoy!

The transcript below has been edited for conciseness and readability.

George Cozma: Hello, you fine internet folks. We’re here at Stanford during Hot Chips 2026. And the very first Hot Chips presentation this year was from IBM, talking about their next-generation z/Architecture, along with the really, really cool thing that they did there, which we’ll get to in a second. But I have two folks from IBM here. If you’d like to introduce yourselves.

Christian Jacobi: Hey, I’m Christian Jacobi. I’m an IBM Fellow and the CTO for Systems Development.

Christian Zoellin: My name is Christian Zoellin. I’m a Distinguished Engineer and I was the leader of the core design team for this generation.

George Cozma: Awesome. So what is so cool about z—I’ll call it z18 for this conversation, but the next-generation z?

Christian Zoellin: That it supports both the z/Architecture instruction set and the Arm instruction set.

George Cozma: So I think the last time we’ve seen something like this, I believe, was the original Itanium. What you guys did was slightly different. You guys actually integrated the decoders into the core. Tell me a bit about how are the decoders a single unit with multiple modes, or is it two separate decoders?

Christian Zoellin:It is a decode pipeline. Let me start there. There’s a decode pipeline, and a lot of details of the decode pipeline are shared between the two instruction set architectures. But then the individual decoders that do the actual decoding from the 16 to 48 bits in the z/Architecture or the 32-bit instructions in the Arm architecture, those are separate decoders that we construct.

George Cozma: Okay, awesome. Now, what is really interesting to me is that z is a big-endian ISA, which means that the most significant byte is first and least significant byte is last, excuse me. But Arm is little-endian, or really bi-endian, but has a little-endian mode. How did you guys deal with that swap of endians?

Christian Zoellin: In the load-store unit, basically the data cache is organized in words anyway, but we support unaligned accesses on any byte boundary. So there is a structure there that formats these word accesses out of the cache into the actual word that was requested by the load instruction. And in there, we just add all of the swapping to support big-endian versus little-endian.

George Cozma: Okay. So there’s no software that has to be implemented; the hardware will do it automatically?

Christian Zoellin: Correct.

George Cozma: Awesome. And speaking of sort of the load and store unit, something that z has is what’s known as strong ordering, whereas Arm is weak ordering. So that means it’s easy to implement, but does that mean that all load and store instructions are strong when they leave the core?

Christian Zoellin: Correct. They’re always strongly ordered. We have a lot of infrastructure to speculate across these ordering boundaries, and so for us, from a performance point of view, we have all the hardware to do this efficiently and quickly. And so, we simply reuse that hardware and stay strongly ordered. As a matter of fact, there’s a feature in the Arm architecture to enforce strong ordering, and for us, that bit basically does nothing.

George Cozma: I believe that is TSO, correct?

Christian Zoellin: Correct.

George Cozma: Yes, so you guys have TSO automatically then. So, moving on to how much sort of area/extra transistors did this use? Was it much, or was it not a ton?

Christian Zoellin: It definitely wasn’t a ton. But we already talked about the decoders, how those are separate decoders; there’s certainly transistors in that. There’s also certain features that we added that the z/Architecture did not have, but we had to implement. One example is the BF16 and FP16 floating-point formats, and for those, we also added new data flows, and those are extra transistors. But if you look at the overall floor plan, these things are small, tiny specks compared to our huge BTB branch prediction structures or to our large instruction and data caches.

George Cozma: And so speaking of what can be shared and reused, how many structures are being reused? I assume it’s the vast majority, correct?

Christian Zoellin: All of those big ones especially. That’s key. The translation lookaside buffers, the caches, the physical register files for the GPRs and vector registers, all of those are exactly the same and used as-is.

George Cozma: Cool. So moving sort of more into a business case use, why did you guys add Arm to z?

Christian Jacobi: So, the Arm software ecosystem has grown really rapidly over the last loosely decade, driven a lot by the hyperscalers deploying Arm in their data centers, right? So, for us, it’s a huge opportunity to bring all of that software closer to the mission-critical data and transactions that our clients are running. So it’s a huge expansion in terms of flexibility of where clients place that workload. In many cases, it does make sense to have that workload close latency-wise to the data and transactions, but also in the same sort of operational environment, so that from a security, from an availability perspective, it kind of all ties together. That, I would say, is one important use case.

The other important use case is we have clients who do massive workload consolidation projects, in particular on LinuxONE, sometimes running thousands of, for example, MongoDB databases on a single mainframe footprint, LinuxONE footprint. But if you look at these projects, they don’t consist just of like the main database, right? They have endpoint security software, they have backup software, monitoring, observability—a lot of software in a total solution stack.

And we have a great ecosystem team that would work with ISVs to port software from wherever it was initially coded onto Linux on z, but of course, there’s so much software out there, so many ISVs out there, we really can’t win them all to come to the platform. So, it’s been complex sometimes to get the ISVs to support our platform whenever a client wanted to do such a big consolidation project. Having the Arm ecosystem natively available on our platform solves a lot of that, so we believe we can see many more of these large-scale consolidation scenarios just because we have so much more of a sort of complete software ecosystem through the adoption of Arm technology into our platform.

George Cozma: And speaking of that, have you considered adding a third ISA? I know a lot of people have been talking about RISC-V, that was a big thing yesterday during the tutorials. But what about POWER? What about implementing POWER as a third ISA?

Christian Jacobi: Yeah, well, I mean right now we’re working on this project to integrate Arm. We’ve learned a lot in this experience. But if you also look at the use cases that we have for different enterprise systems, IBM does have our Power Systems, IBM has our Mainframe Systems; they are sort of in separate swim lanes going after different kinds of workloads. There’s really no good business case for us to bring the Power architecture into the mainframes and then try to compete with ourselves on the Power Systems. That wouldn’t really make any sense for us.

George Cozma: Absolutely. And I believe during the presentation, you made a comment about the amount of instructions in Arm. Really sort of going back into the hardware, what’s the real difference between CISC and RISC because, as you said, they’re kind of misnomers?

Christian Zoellin: So let me get to the most extreme CISC instructions right away. We have CISC instructions that as part of the instruction have a parameter block in memory that has 15 different parameters that get consumed by the instruction to produce the right result. That’s how we implement compression, that’s how we implement crypto on the mainframe. We have instructions that have sub-instructions and function codes, and they’re library routines in some sense.

RISC does not have that. RISC has to do all the operations on the register set, and as such, they just have many more instructions for all these substeps, and things that for us are one large instruction in a RISC instruction set architecture are usually programs that execute hundreds of instructions to do the same task. And so that’s how you get to this instruction inflation to a certain degree.

George Cozma: Well, I guess the other thing that was talked about beyond just next-generation Telum, is your next-generation Spyre—so not Spyre 2, but next-generation Spyre. You guys have added HBM to that. I know that there was a Meta paper, I believe about two or three years ago, talking about how many errors HBM would sort of not create, but would have. IBM is all about ultra-reliability. How are you guys sort of dealing with that new memory that may have higher errors?

Christian Zoellin: I’m actually not familiar with the details of that. Are you?

Christian Jacobi: Yeah, to a degree. I’m not the super deep expert, but first of all, it’s important to note we’re not on the bleeding edge of HBM technology, so we’re consuming a technology that has matured and has a lot lower error rate than at the bleeding edge. We’re also not running it at the highest speed levels, right? That’s another component in designing for reliability.

And then we do a lot of testing. We’re really focusing on shipped product quality in terms of really finding those production failures early. We do things like very deep tests for the processors. For example, we do a lot of burn-in to actually run the processors in an oven at a very high temperature to find the early failures before we even ship them. If the processor breaks on our manufacturing floor, that’s much better than if it breaks in a client’s data center, right? So that’s the kind of things we do for reliability. It’s not only about error correction and error checking; it’s also how you weed out the errors in your manufacturing processes.

George Cozma: Okay. And I guess the move over to HBM has sort of increased the amount of business case that you can now target. What are the broader cases that you’re looking at now?

Christian Jacobi: Yeah, it’s actually the other way around. It’s how the business cases, the use cases evolve that informs how we need to adapt the design and the architecture, basically, right? So when we introduced Telum 1 and Telum 2 with the on-chip AI acceleration, it was really a lot about relatively small models doing fraud detection inside transactions with very low latency so that you wouldn’t hold up a credit card swipe, for example.

Then when we introduced Spyre, it was a lot about how we do enhanced protection in such use cases where you use slightly more complex models, but then you could also run, I’d say, small language models on a group of cards to get some generative AI going. As this has evolved over the last few years, we’re really seeing use cases come up for things like document processing when you’re adjudicating insurance claims, for example. So that’s just one example of how a business process can benefit from large language model utilization.

The same is true when we’re thinking about AI ops where you use sort of an agentic workflow to actually have the system monitor itself, self-heal, self-optimize, those kinds of things. So, we’ve seen this shift from relatively small models for risk and fraud detection to more complex models for risk and fraud detection, small language models, and now we’re seeing the shift even in the enterprise space towards more agentic loops. And so that has determined that we need to invest more heavily in memory bandwidth to be able to run these models.

We haven’t talked about the details, I won’t talk about the details today, but of course that’s not only about a single chip; it’s really about designing a system consisting of many of those chips. We’ve talked about the 4 terabytes per second of memory bandwidth on a single chip; that system will of course then use multiple chips to get to significantly more than that 4 terabytes so that we can run many models in a heterogeneous environment, and large models, and very good output tokens per second performance to support these agentic workloads that we see on the horizon.

George Cozma: Awesome. You’ve been asked this question, so you’re going to be asked a different question. But CZ, what’s your favorite type of cheese to end this interview with?

Christian Zoellin: Roquefort. That’s a blue cheese, a French blue cheese made out of sheep’s milk. Goes very well with red wine.

George Cozma: Ooh. And Christian, what new cheeses have you tried?

Christian Jacobi: Right now I’m on a Gruyère kick.

George Cozma: Ooh! Just Gruyère or sort of the Gruyère family?

Christian Jacobi: Um, I really like Gruyère right now.

George Cozma: Okay. Okay. Well, thank you so much for sitting down with me. Good luck with your new chips, as always. Would love to test them one day, but thank you so much for sitting down.

Christian Jacobi: Our pleasure. Thank you.

Christian Zoellin: Thank you.
