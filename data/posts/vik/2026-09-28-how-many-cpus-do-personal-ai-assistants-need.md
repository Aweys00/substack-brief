---
title: "How Many CPUs Do Personal AI Assistants Need?"
source: "Vik's Newsletter"
author: "Vikram Sekar"
url: "https://www.viksnewsletter.com/p/how-many-cpus-do-personal-ai-assistants"
published: "2026-09-28T12:56:37+00:00"
words: 1886
preview_only: true
---

# How Many CPUs Do Personal AI Assistants Need?

#### The Rise of Personal Agents

Agentic harnesses such as OpenClaw and Hermes were essentially for the ‘hacker-types’ who knew how to spin up VMs, secure SSH, and set AI keys to have their personal army of always-on agents. Grok Bot from xAI was the first to change that paradigm. It provided a simple chat interface that could spin up agents via an easy-to-use GUI. Grok Bot provided users with their Virtual Machines (VMs) that acted as a virtual cloud computer that the agent would use for autonomous tasks. Suddenly, agents were for everybody, not just the ones who knew how to hack it into existence.

Recently, another personal AI tool – Instinct – gained popularity in social media. Founded by Noam Shinn, [Techcrunch reports](https://techcrunch.com/2026/08/26/viral-ai-startup-instinct-has-raised-350-million-at-a-2-5-billion-valuation/) that they raised a total of $350M at a $2.5B valuation. Their launch has mostly been via private invites due to limitations in compute capacity. The rise of personal agents really took root with the announcement of Meta’s Muse personal AI. Meta advertised it as a free AI agent that can get your everyday tasks done. In its first two weeks, it had nearly 3 million installs across various devices. Underlying all these personal agents were VMs allocated to each user, so that their personal agents could kick off inference requests from within them.

With the release of Muse, the market finally woke up to CPU demand primarily driven by personal agents and sent stocks of CPU makers soaring. Funda has a [nice post](https://fundaai.substack.com/p/deepmeta-could-muse-be-the-inflection') explaining how Muse is being adopted. The month-to-date price change for INTC, AMD, and ARM were all up >25%. This price change is primarily on the basis that personal agents, if adopted by a wide user base due to its relative simplicity and usefulness, would drive CPU demand massively. We will test this assumption.

We made an [early report on CPUs for agentic AI](https://www.viksnewsletter.com/p/the-cpu-bottleneck-in-agentic-ai) back in February 2026, which explained the need for CPUs in a new class of workloads that included tool calls, database accesses, and web-search, in addition to LLM-based inference. Personal AI agents belong to the same class of workloads but the ease of use expands the end-user base much more than agentic harnesses.

In this article, we will examine if CPU-sensitive tasks are automatically proof of explosive CPU demand, and how that ties into memory needs.

By reading this post, you agree to the [terms and conditions](https://www.viksnewsletter.com/p/terms-and-conditions). Also see the [full ethics statement](https://www.viksnewsletter.com/p/ethics).

If you’re new, check out the [About page](https://www.viksnewsletter.com/about). A lot of readers expense the subscription to this newsletter as it helps their professional work. Group subscriptions (3+) are 20% off. If you have any questions, reply to this email and let me know!

For the full post, upgrade to a paid subscription

Check out the [Semi Doped podcast](https://www.viksnewsletter.com/about#§semi-doped-podcast), and [our daily free newsletter](https://daily.semidoped.com/) with latest semi news. This article is an example of the kind of institutional research clients of [SemiExponent](https://www.viksnewsletter.com/about#§semiexponent) get. Reach out using the contact form for more info.

#### What Runs a Personal Agent?

Personal agents require virtual machines (VMs) that are computers with an operating system running on them, from where an entire task can be performed from start to finish. Each VM is allocated a share of CPUs, RAM, and storage from a larger pool of resources. For example, users prompted Muse to reveal its VM configuration and identified that it is using 2 virtual CPUs (vCPUs), 8 GB of RAM, and 100 GB of SSD storage. While actual specs are unconfirmed by Meta, this often represents a typical VM deployed on the cloud.

A vCPU is a virtual CPU presented to a virtual machine. How vCPUs map to physical cores depends on the platform. On many cloud instances, one vCPU corresponds to one hardware thread. With simultaneous multithreading (SMT), two threads share a physical core’s execution resources. For CPUs without SMT, vCPUs align 1:1 with core counts. Thus, translating vCPUs into chip demand requires knowing the hardware mapping, among other things.

Take the example of an agent booking travel to maximize credit card points. A phone sends a message to a remote VM which uses a combination of CPU, RAM, storage, and GPU-based inference to complete a task. The process also involves accessing websites and logging in with credentials which needs computer use. All the data from search is sent to the LLM running on the GPU to interpret and plan next steps. The RAM stores working data including travel dates and current viable options, while storage is used to periodically store state, and outputs of the booking process. The figure below shows the data flow between various parts of hardware.

Most analysis today maps the rise of personal agents directly to increased CPU demand, which seems reasonable to the first order. Deeper nuance requires understanding how these VM resources are shared in a multi-user scenario to eventually size the physical fleet of compute hardware in a datacenter. We will cover three different VM deployment scenarios next.

#### How Many Agents Can Share a CPU Server?

To answer this, we must understand how the GPU and CPU work together. We know that a CPU should keep the GPU utilization high for good TCO, but the CPU utilization determines how many agents fit on a server. Although this really depends on the workload, three CPU deployment scenarios broadly apply.

-

Reserved VM: Each user has a continuously running VM with CPU capacity reserved, even when idle. The RAM is exclusive to the VM.

-

Shared CPU: Each user’s environment stays running, but CPU execution time is pooled across users as needed. RAM still holds the VM’s working memory, and only the CPU is shared.

-

On-demand VM: The environment starts or resumes when work arrives, then releases compute resources when idle while preserving saved state. CPU and RAM are shared. Every time a request comes in, the VM is spun up from the saved system state on the SSD.

Although Meta has not published their method of deployment on Muse, we can guess the likelihood each one is used.

Most likely → Scenario 2: Shared CPU. Each VM can retain its identity and state while its virtual CPUs execute when there is work. This fits intermittent agent activity.

When capacity constrained → Scenario 3: On Demand VM. If a user’s usage pattern suggests large periods of inactivity, their VM can be spun down, only to spin it up again before next use. This allows capacity to be released to others.

For special workloads → Scenario 1: Reserved VM. A dedicated VM makes sense for high availability use cases when latency is not acceptable. It will not be the default deployment case because it leaves a lot of capacity unused.

In cases 2 and 3, where the CPU is shared, there will be more agents resident on the CPU than hardware would otherwise allow. The difference between these two then comes down to resident memory usage – which is something we will discuss later. Assigning more vCPUs than physical cores is quantified by the oversubscription ratio which is defined as,

Oversubscription ratio = allocated vCPUs ÷ physical CPU cores

Initially, we assume no multithreading. In reality, two threads are less performant than two cores due to shared resources between them. We correct for this later by a factor between 1.5 and 2 (we assume 1.75).

For example, a 1:4 oversubscription ratio on a CPU with 128 cores and no multithreading would mean that 512 vCPUs can be allocated on the physical CPU. If two vCPUs are allocated per user, that implies that a 128 core CPU can host 256 VMs. Assuming each user of the personal agent platform gets a VM, that is 256 users. The oversubscription ratio used in practice depends on the cloud provider, and the utilization rates on their CPUs. A 25% utilization rate means that the provider can opt for a 1:4 subscription ratio.

We can extend this calculation to different server CPUs in the market today, and estimate how many CPUs are required for a million users for each one. We assume that each user gets 2 vCPUs per agentic VM, and that multithreading increases useful CPU capacity by 1.75×. From here onward, the CPU sharing factor applies after that multithreading adjustment; 4× sharing with a 1.75× benefit therefore implies seven allocated vCPUs per physical core.

#### Memory Constraints on Agentic VMs

The CPU calculation gives us a starting point for sizing the fleet. Each server must also have enough memory to support the environments assigned to it. An agent waiting for an inference response may consume little CPU time while its browser, operating system, and working data remain in RAM.

With a base assumption of a 256-core CPU, a 1.75× multithreading benefit, 4× CPU sharing after multithreading, and 2 vCPUs per environment, a total of 896 VMs can be allocated. If every VM actually occupied the model’s assumed 8 GB of RAM, those environments would require 7 TB of memory per processor.

If, for example, only 1.5 TB of RAM were available, at 8 GB per resident VM, 192 fully resident VMs fit before reserving memory for the host. Counting CPUs purely by core count would therefore overstate density unless the platform reduced how much memory remained resident.

This makes deployment architecture central to the demand estimate.

-

A running environment can retain memory while its CPU is idle.

-

An on-demand environment can release much of that memory by saving its state and resuming later.

The latter option increases the number of users the same hardware can support, but introduces resume latency and additional storage activity. Additionally, a VM might not use all of the RAM available to store its working set. Ultimately, what matters is how much memory remains occupied across the fleet, especially during busy periods.

Our CPU estimate therefore needs a second test: how many environments fit within the available RAM? Whichever resource reaches its limit first constrains deployment density. For this study, we will assume that SSD storage is not a limiting factor because a single QLC drive can provide 256TB of storage - which will allow >2,500 100GB VM environments. RAM is the fundamental limitation, not SSD storage.

#### From Agent VMs to CPU revenue

We can now connect personal-agent deployment to CPU purchases. Our model estimates the hardware and revenue implications of a large deployed agent population under explicit operating assumptions. The adoption path is a scenario, rather than a forecast supported by verified deployment data. We will show our calculations below.

After the paywall:

-

From a billion agent VMs to CPU revenue: Our deployment model through 2030, translating agent adoption into processor purchases and annual and cumulative revenue.

-

The assumptions that drive the result: How CPU sharing, hyperscaler discounts, price erosion and reuse of existing hardware affect the opportunity.

-

When memory becomes the bottleneck: Why RAM constraints can force operators to buy more servers—and how on-demand VMs could ease that pressure.

-

Which CPUs fit this workload best: A comparison of AMD, Intel, NVIDIA and Arm configurations, showing where core counts and supported memory are well matched.

-

What this means for the CPU investment thesis: How much personal agents could contribute to supplier revenue, and what evidence is still needed to support expectations of a much larger boom.
