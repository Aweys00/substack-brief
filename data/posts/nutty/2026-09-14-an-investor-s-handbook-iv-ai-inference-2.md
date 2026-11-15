---
title: "An Investor's Handbook IV - AI Inference (2)"
source: "Nutty"
author: "Nutty"
url: "https://nuttycld.substack.com/p/an-investors-handbook-iv-ai-inference-220"
published: "2026-09-14T05:09:38+00:00"
words: 831
preview_only: true
---

# An Investor's Handbook IV - AI Inference (2)

This is an analysis of industry and technology structure, not investment advice. The author may hold positions in securities mentioned.

Imagine asking an AI in a shopping app, “Can you find me a vacuum that handles pet hair well?” As the AI looks through product information and answers, servers keep performing calculations. This use of an already-trained AI model is called inference.

Inference chips are the semiconductors that perform those calculations. Part 1 explored whether handing some of a GPU’s work to chips designed for that work could reduce waste. Here, the question is what happens for the customer buying those chips: does better performance translate into lower operating costs?

Amazon’s ($AMZN) AI shopping assistant offers a real example. It answers product questions and helps shoppers decide what to buy. In an operating case study published in 2024, AWS said the service used its own Inferentia and Trainium chips. Consumers see a shopping feature. Behind it sits a decision about which semiconductors should run the service.

Now consider a hypothetical shopping company that offers a similar assistant and operates its own GPU servers. As customer numbers grow and server bills become harder to absorb, a semiconductor company proposes a new inference chip. Its pitch is that a chip designed to generate answers can run faster and use less power than a GPU built for many kinds of calculations, allowing the retailer to serve the same customers at a lower cost.

A demonstration that produces recommendations and explanations quickly is likely to attract attention. Before buying, though, the operator needs to know whether costs still fall when questions surge during a sale or servers sit quiet overnight. The system must handle both simple product questions and requests to compare reviews across several products. The equipment also needs to remain useful if the company switches to a better AI model next month.

The demonstration shows how quickly the chip generates an answer. The shopping company also pays to retrieve product information, connect equipment and keep the service running when customers arrive in large numbers. A retailer renting another company’s AI service would leave the hardware choice to that provider. Here, we will follow the company responsible for its own servers and operating bills.

The economic test for an inference chip is whether it lowers the cost of the whole service while maintaining the quality and response speed customers expect. Even a fast, power-efficient chip may save less than expected if it requires more equipment or additional operating staff. The business opportunity for the chipmaker and its suppliers begins when customers have a reason to adopt the product after accounting for those costs.

### 1. The Answer Is Faster, but the Customer Is Still Waiting

A chip that generates answers faster can lower operating costs only if it addresses the work the servers actually do and the reasons customers are waiting.

A customer asks, “I have a long-haired cat. Will this vacuum do the job?” The shopping assistant retrieves the product description and relevant reviews, compares other products, then writes an answer. Even if the chip writes that answer faster, the customer still waits if retrieving the product information takes too long.

Think of asking ChatGPT to do something simple, then spending more time correcting its answers than it would have taken to do the task yourself. Something similar happens when a shopping assistant’s recommendation misses the question. The customer spends time explaining again and checking the answer; the service runs its servers longer to repeat the search and generate another response. There are two costs here: the company’s operating expense and the customer’s time and effort. Each follow-up also increases the amount the AI reads and writes, measured in tokens. A faster individual answer may therefore do little to reduce the total burden, and that burden can even grow.

In other cases, the recommendation is fine, but the answer appears on screen frustratingly slowly. A chip that writes the same answer faster can help. The customer waits less, and the server can move on to the next customer’s question sooner. Whether faster performance helps the business depends on where that performance is used.

Idle time matters too. Purchased equipment has already cost money, and rented equipment carries a bill. If there are too few requests and the servers spend long periods idle, an additional faster chip has little work to do. The situation is different for a company planning to buy more equipment to handle demand. If the new chip can process the same requests with fewer machines, it can reduce the next purchase.

The rest of this article uses company examples and reported figures to examine which inference chips customers might choose, and whose orders and profits can follow from that choice. It compares GPUs working alongside dedicated chips with Jalapeño’s different approach, then examines the roles of memory, connectivity, chip-design and server-manufacturing companies. For investors interested in inference chips, these distinctions help assess business progress beyond performance demonstrations and partnership announcements.
