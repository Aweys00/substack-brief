---
title: "Anthropic: Benchmarking the S-1 Data"
source: "Clouded Judgement (Jamin Ball)"
author: "Jamin Ball"
url: "https://cloudedjudgement.substack.com/p/anthropic-benchmarking-the-s-1-data"
published: "2026-10-26T15:58:04+00:00"
words: 2889
preview_only: false
---

# Anthropic: Benchmarking the S-1 Data

Recently Anthropic their [initial S1 statement](https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm). A S-1 is a document companies file with the SEC in preparation for listing their shares on an exchange like the NYSE or NASDAQ. The document contains a plethora of information on the company including a general overview, up to date financials, risk factors to the business, cap table highlights and much more. The purpose of the detailed information is to help investors (both institutional and retail) make informed investment decisions. There’s a lot of info to digest, so in the sections below I’ll try and pull out the relevant financial information and benchmark it against current cloud businesses. As far as an expected timeline - typically companies launch their roadshow ~2-3 weeks after filing their initial S-1 (the roadshow launches with an updated S-1 that contains a price range). After the roadshow launch there’s typically ~1.5 weeks before the stock starts trading. So we’re looking at roughly ~4 weeks before any retail investor can buy the stock.

Anthropic Overview:

From the S-1: “For the first time in history, intelligence is something humans can build. The cognitive capability to reason, analyze, synthesize, decide, and create is producible at scale and accessible on demand. We believe this abundance of AI will rapidly transform every sector of the global economy in ways greater than the impact of industrialization, electricity, semiconductors, and the internet. AI that truly delivers on its potential—with the risks well managed—could significantly accelerate global growth and dramatically improve quality of life for people around the world.

Anthropic was founded in 2021 by a team of researchers responsible for many of the breakthroughs that define AI. We are first and foremost a research lab—our mission is the responsible development and maintenance of advanced AI for the long-term benefit of humanity. This mission directs our focus—along with our talent and culture, our frontier and safety research, our approach to compute, and our enterprise strategy, it is one of the core advantages that set us apart. These advantages enable us to continuously advance frontier AI and shape the standards for its safe and responsible development. Our frontier AI, Claude, is delivered to customers through our models, platform, and applications. Claude has experienced the fastest enterprise adoption of any technology in history, as demonstrated by revenue growing from $0 at commercial launch in the first quarter of 2023 to $[not filled in yet] for the three months ended September 30, 2026. This rapid and growing adoption generates two self-reinforcing dynamics—an improvement loop that advances Claude and an investment loop that helps fund our continued research in frontier AI.”

Models

From the S-1: “We are building at every layer of frontier AI. Our Claude model family provides the underlying intelligence. Our Claude Platform makes that intelligence available as a set of composable primitives that developers and enterprises can assemble into their own solutions. Our applications draw on those same primitives, packaged into products customers can deploy directly. Because we build these layers cohesively, improvements at any layer compound across the stack and benefit our customers. We believe this integrated approach has made us a partner of choice for customers transforming their business through AI. Customers can adopt, govern, and scale our technology immediately, and each new primitive and application we release expands the range of workflows they can run on Claude.”

“The Claude model family is currently composed of four model classes: Mythos (including Fable), Opus, Sonnet, and Haiku. Our model classes can be used individually for certain tasks or in combination with one another. They offer broad flexibility to choose the ideal performance, cost, and speed for each use case. All models support text, code, and multimodal inputs.

-

Mythos (including Fable). Our most capable model class, delivering frontier performance across all domains and solving problems AI has not reliably handled before, especially in coding and long-running agentic tasks. Given its advanced capabilities in sensitive areas like software vulnerability discovery and biology, we deploy this underlying model in two distinct configurations. Fable is generally available and runs with our production safeguards, which block or limit performance on certain sensitive topics, including by routing requests to a less capable Claude model. Mythos runs with safeguards calibrated for vetted organizations and individuals doing cybersecurity and life sciences work, and is available through our trusted-access programs, including our Cyber Verification Program. We first made the class available in April 2026 as Claude Mythos Preview through Project Glasswing, made Fable 5 generally available and offered Mythos 5 to Project Glasswing participants in June 2026, and released Mythos 5.1 and Fable 5.1 in September 2026.

•Opus. Our powerful workhorse model class for reasoning-intensive tasks. Our most recent Opus release, Claude Opus 5.5, is designed to serve as the enterprise daily driver, powering agents that run projects end to end and advancing capabilities across agentic coding, computer use, and knowledge work. Opus models consistently rank among leading models on key industry benchmarks.

•Sonnet. Our versatile model class for everyday tasks, providing a balance of performance, cost, and speed for the widest set of general-purpose use cases, including high-volume sub-agents in multi-agent orchestration setups.

•Haiku. Our lowest-cost and fastest model class. Haiku models are designed for high-volume workloads like customer service agents and large-scale document processing.

Platform

From the S-1: “Our platform unifies frontier intelligence with the harnesses, connectors, governance, and orchestration that are all required to put that intelligence into production. As customers build on the primitives we provide, Claude becomes an integral part of their data, workflows, and institutional knowledge, and the relationship deepens with each integration. We open our platform to all builders because we believe enabling a wide range of companies to build on Claude generates more innovation and value than we could create on our own.”

Applications

From the S-1: “We build first-party applications to demonstrate where frontier models are heading and to deliver fully integrated solutions where we have a distinct viewpoint on the workflow. Applications like Claude Code and Claude Cowork are early examples of what the future of agentic work might look like; they put our latest AI capabilities directly into the hands of users while accelerating the market’s understanding of AI’s possibilities. Because our research and product teams work side by side, new model capabilities inform our products and customer feedback on those products informs our research priorities. This allows us to build products for where we believe model capabilities are going, not just where they are today. For example, we designed Claude Code around the agentic coding capabilities we expected our models to achieve, which positioned it to scale rapidly as those capabilities arrived. We have taken a similar approach with Claude Cowork.

We also design our products to close the gap between what Claude can do and how fully customers use it, which we believe is important to helping customers realize the value of frontier intelligence. Rather than requiring customers to learn how the underlying models work, we build products that allow them to interact with Claude as they would with a colleague, simply and naturally, so they can adopt new capabilities as they become available. We believe that as we extend the frontier and broaden our application surfaces, customers realize value faster, embed Claude more deeply into their operations, and increasingly rely on us as a primary provider for their AI transformation.”

-

Claude Code. A coding agent, available as a terminal tool, desktop app, web interface, and mobile app, with native integrations for GitHub and popular IDEs (Integrated Development Environments). Claude Code handles multi-step software development tasks—planning, writing, editing, testing, debugging, and committing code—across large codebases with sustained context and supports parallel agent sessions, so a single developer can keep multiple tasks moving in parallel.

-

Claude Cowork. A knowledge work agent on desktop, web, and mobile, built on Claude Code’s agentic architecture. Users describe a task in plain language and Claude breaks it into steps and completes them across local files, connected apps, Chrome, and the desktop itself, clicking and typing through native applications when no integration exists. It returns finished documents, spreadsheets, presentations, and organized folders, with no terminal or code required. An open-source plugin system lets users install or build packages bundling skills, data connectors, and workflows.

•Claude.ai. Our flagship conversational product, available on desktop, web, and mobile. Claude.ai is the broadest entry point to Claude, available to enterprises, teams, and individuals, offering access across our Claude model family with support for file uploads, projects for persistent context across conversations, memory, web search, and artifacts for real-time code and document rendering.

Claude.ai delivers top-of-funnel demand generation for enterprise adoption. In September 2026, we began merging Claude Cowork and Claude.ai into a unified application, such that any request is automatically handled using the appropriate tools, drawing on Claude Cowork’s capabilities.

•Claude Security. A defensive cybersecurity product, available in public beta to Claude Enterprise customers, that puts frontier vulnerability detection and patching into the hands of security teams. Claude Security reasons about code the way a security researcher does, tracing data flows and examining how components interact across a codebase to uncover complex, context-dependent

vulnerabilities that pattern-based scanners can miss. Each finding is surfaced with a confidence rating, severity assessment, and reproduction steps. Users can move directly into Claude Code to review and apply the proposed patch, compressing the time from scan to fix.

•Claude Tag. A collaborative agent that works alongside teams in productivity tools like Slack where users tag Claude into any channel or thread and delegate work in plain language. With the context of the surrounding conversation, enterprise software tools, shared documents, and channel-scoped memory, Claude returns answers, drafts, analyses, and pull requests directly in-thread, operating as an ambient teammate that knows when to proactively join the conversation. Claude Tag brings Claude into the multiplayer workflows where teams already coordinate, extending adoption from individuals to entire organizations.

•Claude Design. Enables users to create polished designs, prototypes, presentations, and other visual work through natural language conversation and direct editing. Claude Design extends our platform into visual and creative work, broadening the range of professional tasks for which designers, marketers, founders, and go-to-market professionals can utilize Claude.

•Claude Science. An AI workbench for scientific research that brings literature analysis, data processing, and manuscript preparation into a single desktop environment. Researchers describe an analysis in plain language, and Claude Science queries more than 60 scientific databases to complete it end-to-

end. Claude Science executes computationally intensive workloads on a lab’s own machines, institutional computing clusters, or on-demand cloud resources, without requiring researchers to manage the underlying infrastructure. It returns publication-ready figures and manuscripts—with natively rendered scientific outputs, fully reproducible code, agent-powered verification, and traceable results. Claude Science extends Claude into scientific research, putting frontier capabilities directly in the hands of researchers working on some of the world’s hardest problems.”

Financial Model

From the S-1: “Our financial model is built on four primary drivers that define the trajectory of our results:

•Adoption of Claude. The advancing intelligence and capabilities of each successive version of a Claude model drive the diffusion of Claude across the global economy. As new customers adopt Claude and existing customers expand their usage into new workflows, our revenue grows.

•Compute Efficiency. We are focused on increasing the intelligence produced and revenue generated per dollar of compute invested and have delivered significant efficiency improvements.

•Operating Efficiency. Our high talent density, efficient go-to-market, and how extensively our teams leverage Claude in their work help to drive improved operating margin, Adjusted Operating Margin, and revenue per employee.

•Compute Investments. Investing in compute is critical to support our long-term growth, and we intend to continue making substantial investments in compute.

The drivers of our financial model materialize on different timelines. The adoption of Claude and associated revenue growth, compute efficiency, and operating efficiency have each increased rapidly over time. Compute is procured and committed in advance and the expense is incurred as it is brought online and added to our fungible pool, often in large, discrete steps. The fungible pool can support all workloads dynamically, including research, model development, serving customers, and internal usage of Claude. As a result, there is a lag between when investment is committed and when the full revenue associated with such investment is realized.

This dynamic has produced a financial model in which our operating margin and Adjusted Operating Margin for the nine months ended September 30, 2026 have expanded significantly year over year. As significant incremental compute is brought online in future periods, the associated expense will be recognized in advance of the full revenue that the compute will ultimately support, and we expect operating margin and Adjusted Operating Margin may compress in those periods. At our current stage, this cycle is an inherent aspect of our business and will cause operating margins to fluctuate from period to period, at times meaningfully, even if the underlying economics of the business continue to improve.

In addition, the majority of our compute is contracted under multi-year commitments that we typically procure 12 to 18 months in advance of availability. When customer demand or research needs exceed this long-term capacity, we procure short-term compute, which typically carries a higher cost per unit of compute. We expect our use of short-term compute to increase in the near term and to in turn compress our operating margin and Adjusted Operating Margin as a result.”

How Anthropic Generates Revenue

From the S-1: “Pay-for-intelligence, our consumption-based revenue model, is our primary revenue model and currently represents the substantial majority of our total revenue. Under this model, customers pay for usage, which is metered in tokens and priced according to the model selected. Our pay-for-intelligence revenue is primarily generated from customers building applications incorporating Claude or utilizing our first-party applications. In addition, we offer certain of our applications on a subscription basis, serving both enterprises and prosumers. Under this model, customers pay a subscription fee for a specified level of usage and capabilities during the subscription term, which is generally 12 months or less.

Depending on the model, platform, or applications chosen by our customers, they enter into pay-for- intelligence pricing, subscription-based pricing, or both. For example, when subscribers approach or exhaust the usage capacity included in their tier, they may utilize a higher subscription tier or purchase more intelligence directly, creating a seamless bridge from subscription to incremental pay-for-intelligence revenue.

A growing number of enterprise customers agree to non-cancelable annual or multi-year contracts with minimum spend commitments in exchange for a committed price list. These contracts result primarily in consumption-based revenue.”

#### Benchmark Data

The data shown below depicts how the Anthropic data compares to the operating metrics of current public SaaS businesses.

Here’s a summary of their financial output:

Last Twelve Months (LTM) Revenue

Anthropic did over $19b LTM revenue (for period ending June 30th)

Quarterly YoY Revenue Growth Trends

Here’s a fun one. Including because of how ridiculous the chart looks. Anthropic grew 1,368% YoY in Q2. Here’s how that compares to the public cloud universe

Gross Margin

Anthropic had 85% gross margins in the 6 months ending June 30, 2026. This would put them sixth highest on the chart. What is graphed is last 12 months

LTM GAAP Operating Margin

Anthropic’s LTM operating margins were (34%). However, it has been trending up. In Q2 ‘26 it was 8%

LTM FCF Margin

Anthropic had 11% FCF margins over the last 12 months and 21% FCF margins over the last 6 months

The information presented in this newsletter is the opinion of the author and does not necessarily reflect the view of any other person or entity, including Altimeter Capital Management, LP (”Altimeter”). The information provided is believed to be from reliable sources but no liability is accepted for any inaccuracies. This is for informational purposes and should not be construed as an investment recommendation or legal advice. Past performance is no guarantee of future performance. Altimeter is an investment adviser registered with the U.S. Securities and Exchange Commission. Registration does not imply a certain level of skill or training. Altimeter and its clients trade in public securities and have made and/or may make investments in or investment decisions relating to the companies referenced herein. The views expressed herein are those of the author and not of Altimeter or its clients, which reserve the right to make investment decisions or engage in trading activity that would be (or could be construed as) consistent and/or inconsistent with the views expressed herein.

This post and the information presented are intended for informational purposes only. The views expressed herein are the author’s alone and do not constitute an offer to sell, or a recommendation to purchase, or a solicitation of an offer to buy, any security, nor a recommendation for any investment product or service or legal advice. While certain information contained herein has been obtained from sources believed to be reliable, neither the author nor any of his employers or their affiliates have independently verified this information, and its accuracy and completeness cannot be guaranteed. Accordingly, no representation or warranty, express or implied, is made as to, and no reliance should be placed on, the fairness, accuracy, timeliness or completeness of this information. The author and all employers and their affiliated persons assume no liability for this information and no obligation to update the information or analysis contained herein in the future.
