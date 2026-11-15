---
title: "The AI Memory Masterclass with Damnang"
source: "Damnang Research"
author: "Damnang"
url: "https://www.damnang.com/p/the-ai-memory-masterclass-with-damnang"
published: "2026-09-11T06:07:32+00:00"
words: 6198
preview_only: false
---

# The AI Memory Masterclass with Damnang

This article was written in collaboration with and summarizes a conversation and I had about memory that lasted nearly two hours. You can also read it on the their Substack.

Author: [Daniel Koss](https://open.substack.com/users/20964043-daniel-koss?utm_source=mentions) in collaboration with [Damnang](https://open.substack.com/users/329991097-damnang?utm_source=mentions).

Many of you will already know Damnang from [his writing on X](https://x.com/damnang2). I recently sat down with him for a conversation about one of the most important parts of the AI infrastructure stack: memory.

Damnang is a semiconductor engineer working in Silicon Valley. His background is in digital chip design, and he follows memory and the broader semiconductor industry closely.

We started with the basics. What is memory? Why do we need different types? And why does AI change the equation?

Then we moved to the questions that matter to investors. Can memory prices keep rising? Does more capacity inevitably mean another downcycle? How much power does NVIDIA have over its suppliers? And how should we think about the different memory companies?

What I found most valuable was where his engineering perspective challenged my investing perspective. He sees important technical advantages at Samsung, understands the appeal of SK hynix, and ultimately chooses Micron for his own circumstances.

To respect Damnang’s anonymity, this interview is being published in text only. No audio or video accompanies this article.

Below are my key takeaways, a company-by-company summary, and the edited interview.

Editorial note: This is an edited interview, not a verbatim transcript. The preliminary getting-to-know-you conversation, filler, repeated phrases, and off-topic digressions have been removed. Questions and answers have been tightened for readability, and clear transcription errors have been corrected. Several unclear figures and unverified anecdotes have been omitted. Forecasts, estimates, and industry commentary remain the speakers’ opinions at the time of the conversation. The takeaways and closing section are my interpretation, separate from Damnang’s answers.

Damnang Research is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

### Key Insights

#### 1. The question is not simply “HBM or NAND?”

Damnang’s starting point is the memory hierarchy. Different technologies serve different purposes, with trade-offs between speed, capacity, and cost. His view is that AI is forcing the industry to rethink how those layers fit together, rather than creating one memory technology that replaces everything else.

My takeaway: The better investment question is which architectures become widely adopted, and which companies supply the layers those architectures need. Being bullish on memory does not require believing that every memory product will benefit equally.

#### 2. Smaller models do not automatically mean less aggregate memory demand

He pushes back on the idea that model efficiency necessarily undermines the memory thesis. A smaller model can require less memory for an individual task, while more applications and more model calls increase aggregate demand.

My takeaway: We need to separate memory per workload from the total number of workloads. Efficiency is only one side of that equation. Whether usage grows enough to offset it is the question, not something that can be settled by looking at model size alone.

#### 3. His longer-term thesis is about quantity, not endlessly rising prices

One of his clearest formulations was the distinction between P, price, and Q, quantity. He does not expect memory prices to rise without limit. Customers have their own economics to protect, and NVIDIA has considerable negotiating power in his view.

My takeaway: A durable bull case should not depend entirely on another round of price increases. The more interesting question is whether suppliers can grow volumes while maintaining attractive pricing and customer relationships.

#### 4. HBM and custom memory may give suppliers more control over product mix

Damnang argues that today’s suppliers have more ways to allocate production than in earlier commodity-memory cycles. Producing more HBM absorbs capacity that could otherwise support conventional DRAM, while custom products offer another route away from undifferentiated supply.

My takeaway: His argument is not just that AI demand will rescue the industry. It is also that the supply side is changing. That is a reason to examine the old cycle framework more carefully, not a reason to declare that oversupply has become impossible.

#### 5. Manufacturing memory and controlling its design are different sources of value

Our discussion of custom HBM kept returning to the logic at the base of the memory stack. Who designs it? Who owns the relevant intellectual property? And how much of that value stays with the memory supplier rather than NVIDIA or another technology provider?

My takeaway: More sophisticated memory does not automatically mean all the incremental profit goes to the memory manufacturer. We also need to understand who controls the architecture and the design.

#### 6. The strongest technology is not automatically the best stock for every investor

He sees advantages in Samsung’s combination of memory, foundry, and logic capabilities. But we also discussed organizational complexity, internal incentives, and the difference between technical integration and pure exposure to the memory thesis. His personal choice was Micron, partly because of his U.S. circumstances and concerns about accessing Korean stocks.

My takeaway: Technology, business structure, and the security you actually buy are three separate questions. His Micron preference should not be misrepresented as a claim that Micron leads every technology category.

#### 7. The NAND thesis is broader than one new memory architecture

Damnang’s view is that persistent storage remains necessary even as the faster layers evolve. He sees HBF as potential additional upside for Sandisk, rather than the entire reason to care about NAND. Importantly, he also acknowledges other NAND suppliers. This is not a claim that Sandisk has no competitors.

My takeaway: Separate demand for a storage category from one company’s ability to capture it. Capacity, execution, contracting, competition, and the price paid for the stock still matter.

#### 8. His assessment of China is about equipment and execution, not just lithography

He believes concerns about Chinese memory supply often focus too narrowly on EUV and DUV. His argument also includes inspection, testing, and the wider equipment chain. He remains skeptical about how quickly that entire capability can be replicated, while explicitly acknowledging that CXMT is real and progressing.

My takeaway: Neither “China cannot do it” nor “China will immediately flood the market” is a sufficient analysis. His timing assessment is a forecast to test, not a certainty to build into a model without further work.

### The Companies, at a Glance

This summarizes Damnang’s views in the interview. It is not a valuation model, a ranking of expected returns, or a set of current trading recommendations.

### The Full Interview

#### 1. What Is Memory, and Why Does AI Need So Much of It?

Daniel: Let’s start very simply. What is memory? When people talk about memory companies, what do those companies actually do?

Damnang: Memory stores data. When a computer is doing something, it needs to store information so that it can use it for the next operation.

You can compare it to a human brain. When we do something, we remember information and use it again. Computers, processors, and AI accelerators also need somewhere to store the information they work with.

The reason we need much more memory now is that we are asking computers to perform increasingly complex tasks through AI. Our brains have a very efficient architecture. We can store information, and sometimes we ignore it or forget it. A computer works differently.

As we try to make computing behave more like human intelligence, the amount of information that has to be stored and handled becomes much larger. That is why memory is so important for AI.

Daniel: At a high level, how would you explain the different types of memory to someone who is completely new to the industry?

Damnang: The first concept to understand is the memory hierarchy.

Imagine you are studying in your room. You keep a book on your desk because you can reach it immediately when you need some information. But you cannot keep every book on your desk.

For more information, you might go to a library. The library has much more capacity, but going there and finding the book takes time.

Computers have the same problem. If you want very fast access, you keep a relatively small amount of memory close to the processor. If you want to store much more information, you use another layer, but accessing it takes longer.

That is the memory hierarchy. You can imagine it as a pyramid. Near the top is very fast memory such as SRAM, but the capacity is small because it is expensive. Other layers provide more capacity at different costs and speeds.

Daniel: SRAM stands for static random-access memory, and DRAM is dynamic random-access memory?

Damnang: Yes.

SRAM is implemented using the kind of logic technology used for processors. When you design and manufacture a CPU or GPU, SRAM can be implemented using that fabrication process. That is expensive.

DRAM has a different structure and its own fabrication process. A DRAM cell uses a transistor and a capacitor. That allows you to make much more memory at a lower cost than SRAM.

Then you have NAND flash, SSDs, and hard drives further through the storage hierarchy. The important point is that they do different jobs.

For AI, the traditional arrangement is no longer sufficient by itself. With a smartphone application or a game, you have a relatively familiar kind of workload. AI has a very large amount of data to handle, and different types of data need different treatment.

For example, some data, such as KV-cache data, needs very fast reads and writes. We can call that hot data.

Other information is warm or cold. Cold data may still be necessary, but you do not need it immediately. You still need to store it somewhere, and that amount of data is also growing quickly.

That is why I think the AI era is redefining the memory hierarchy. People are discussing HBF, using more HBM, or putting much larger amounts of SRAM into wafer-scale chips. There are many possible ways to address the problem, and the final architecture is not settled.

#### 2. Why More Efficient Models Can Still Mean More Memory Demand

Daniel: Presumably, the right architecture also depends on the use case.

As an extreme example, you could want an enormous context window and accept that it is very slow. Or you could want a much smaller context window with an almost instantaneous response. Those would imply different priorities for memory.

That makes the investment question harder, because both the use cases and the architectures are evolving. Is the broad point that AI is very data-hungry, even if it is difficult to predict the exact mix of memory it will use?

Damnang: Yes, that is a good way to explain it.

Some AI models are getting smaller. People look at more efficient open-weight models and ask whether we will still need so much memory.

I do not think that conclusion is right. This is related to Jevons paradox. Even if an individual model becomes smaller, the total amount of data that we need to handle can keep increasing.

When I talk to AI engineers, they point to the work being done in China to make models more efficient under resource constraints. They are trying to reduce model size.

But look at how those models are used. Each call can be relatively small, while the total number of calls involved in an inference workflow grows very quickly. So you cannot look only at the size of one call. You also have to look at the total number of calls.

We are also still at an early stage of AI adoption. Chatbots are only one use case. As AI expands into other applications, we will need to handle much more information.

Computing can become more efficient, but I still expect the total memory requirement to increase.

Daniel: Let me make that more concrete. AI-generated video has improved a lot. It is getting to the point where many people struggle to distinguish some clips from real footage.

Suppose AI-generated video becomes vastly more common. Video is much more data-intensive than text. You move from kilobytes to megabytes to gigabytes very quickly.

Which type of memory benefits most from that? NAND? HBM? Or all of them?

Damnang: My answer is all of them. It is very difficult to say that one type of memory is the only winner, because SRAM, DRAM, HBM, and NAND each have different roles.

Take enterprise SSDs in an AI data center. You cannot simply replace that storage layer with DRAM, because DRAM is much more expensive. Each layer exists for a reason.

My thesis is that demand across memory should grow. But I would change your question slightly. Rather than asking which memory type is the only winner, I would ask which memory hierarchy becomes established.

#### 3. HBF, Cerebras, and the Competition Between Memory Architectures

Daniel: What do you mean by a hierarchy becoming established?

Damnang: There are different proposed solutions to the same problem.

For example, Sandisk is working on HBF, high-bandwidth flash. The idea is to stack NAND and increase its bandwidth, creating another layer between HBM and SSDs.

Sandisk wants that approach to succeed because it creates another application for NAND flash.

NVIDIA can approach the problem differently, using DRAM, LPDDR, or other arrangements within its own ecosystem. Different companies have different technologies and different incentives.

The important question for investors is which of those approaches becomes widely adopted.

Some people dismiss HBF. Others think it could be an important innovation in the memory hierarchy because it offers a different combination of cost, capacity, and speed. We do not yet know which approach wins.

Cerebras is another example. SRAM is very fast, but ordinarily you have a limited amount of it because it is expensive.

Usually, a wafer is divided into many separate chips. Cerebras takes a different approach by using a wafer-scale chip, allowing it to use a much larger amount of SRAM.

It is another attempt to build a different memory hierarchy. Certain applications place a very high value on speed, so the best architecture can depend on the domain.

I do not know which one will win. That is why I want to follow which architectures become dominant rather than assume there is one universal solution.

Daniel: My approach as an investor is simpler. NVIDIA has such a strong grip on the industry and the supply chain that I would pay very close attention to whatever architecture it pushes.

Partly, that is because I trust NVIDIA to understand the technical trade-offs and to change direction if it learns something new. But it also has the scale to drive adoption.

SK hynix depends heavily on NVIDIA. There is a relationship in both directions, but NVIDIA has other potential suppliers, including Samsung and Micron. SK hynix cannot simply replace all of NVIDIA’s demand with AMD overnight.

So for the near future, my instinct would be to follow what NVIDIA is building. Do you agree?

Damnang: I agree. That is why so many people focus on what NVIDIA does.

There are other HBM customers and users across the AI industry, including companies working on their own accelerators. But NVIDIA is a very important customer for the memory suppliers.

Daniel: Do you know roughly how much HBM demand comes from NVIDIA?

Damnang: I do not know the exact number. I believe it is more than half, but I cannot give you a precise figure.

The point is that NVIDIA accounts for a very large share of HBM demand.

That is also how I interpret NVHBM. NVIDIA has the power to influence the memory vendors, and NVHBM is another way for it to define the architecture and the rules that suppliers need to follow.

If you want to supply that ecosystem, you need to work within those requirements. Because NVIDIA is such an important customer, memory vendors have a strong incentive to do that.

#### 4. The Memory Thesis: More Quantity, Not Unlimited Price Increases

Daniel: A lot of investors describe memory as the bottleneck. Could memory prices simply keep rising for the next several years?

I am asking about the price of memory itself, rather than just the stocks. Is there a fundamental reason that would prevent prices from continuing to go up?

Damnang: My belief is that the rate of price increases will eventually stabilize. NVIDIA and other customers will not be happy to accept unlimited increases.

That is why I keep saying this is a Q era, not a P era. P is price. Q is quantity.

If prices stabilize but quantities increase, suppliers can still grow revenue. That is also why memory vendors are interested in long-term agreements. They want more stable business and they want to keep their customers.

A higher price is not always better.

Daniel: Because at some point you are taking too much of your customers’ margin. They earn a lower return, and then the next round of investment becomes harder for both sides.

Damnang: Exactly. It also matters for hyperscalers’ capital spending.

Daniel: There is a parallel with NVIDIA. Part of the incentive for hyperscalers to develop their own custom chips is how much they pay for NVIDIA’s products.

Even if they like the products and the company, there is an economic incentive to find alternatives. The same principle should apply to memory suppliers. At some point, very high margins encourage customers to look for another solution.

So the healthier long-term outcome could be growing quantities, rather than pushing prices as high as possible.

Damnang: Right.

Further reading: For a concrete example of the trade-offs between memory specifications, production volumes, and supplier revenue, read Damnang’s [What Does Rubin Ultra’s 8-Hi HBM Mean?](https://www.damnang.com/p/what-does-rubin-ultras-8-hi-hbm-mean?utm_source=chatgpt.com), which examines the implications of a potential change in NVIDIA’s HBM configuration.

#### 5. Does More Supply Inevitably Mean Another Downcycle?

Daniel: But that creates another question. If the industry focuses on increasing quantity, could it build too much capacity and create the next downcycle?

From my perspective on AI infrastructure, I expect demand to grow much faster than supply. Even substantial improvements in efficiency might not keep up with how much AI usage expands.

How do you think about that balance in memory? How quickly can supply really grow, and how worried should we be about oversupply?

Damnang: This is one of the questions I hear most often from investors and other industry people.

Companies are building more fabrication capacity, and China is also trying to expand. Investors worry that more supply will arrive around 2028 and bring another memory downcycle.

I disagree with the idea that this automatically leads to the same outcome as previous cycles. There is an important difference in the product mix.

I am not going to base the entire argument on AI demand. We can expect AI demand to grow, but nobody knows exactly how much it will grow.

The other part of the argument is that memory vendors now have more ways to manage their supply.

They did not previously have today’s HBM business alongside their conventional DRAM business. Now they can allocate more production toward HBM. Producing HBM absorbs a large amount of DRAM production capacity, so the mix matters for how much conventional memory reaches the market.

That is also one reason they want a more differentiated portfolio and more custom memory. Custom memory is an important part of my thesis. It gives suppliers another way to move beyond the traditional commodity model.

I am working on a supply model, although it is not finished and I still need to check it.

At this stage, I see supply coming in below what the market consensus expects.

There are several reasons. One is that Chinese supply may grow more slowly than people assume. Another is that HBM affects how vendors allocate their memory capacity. Pricing and the HBM premium also influence those choices.

Then there is the move toward custom memory and memory-on-logic. The product mix is becoming more differentiated.

Taken together, I think those factors reduce the supply risk relative to what many investors expect.

#### 6. SK hynix: A Strong Memory Business, but Who Controls the Value?

Daniel: Let’s go through the individual companies, starting with SK hynix.

To me, SK hynix looks like a strong risk/reward candidate because it is closely tied to NVIDIA and has exposure across NAND, DRAM, and HBM. Some investors view that NVIDIA relationship mainly as a risk. I also see it as being close to the center of the industry.

There is debate about how the competitive position changes with HBM4, particularly versus Samsung. There is also the valuation comparison with Micron and the question of a Korean discount.

What stands out to you about SK hynix?

Damnang: The NVIDIA relationship is important, but it is also a risk.

I have heard industry rumors about NVIDIA trying to negotiate lower HBM prices with SK hynix. NVIDIA is a powerful customer and can work with Samsung, SK hynix, and Micron.

My understanding is that Samsung’s HBM4 has advantages in some specifications, such as bandwidth or pin speed, compared with SK hynix’s offering. That gives NVIDIA something it can use in negotiations.

It can say: look at the alternative, look at its performance, and explain why I should pay your price. I am describing the negotiating dynamic. The specific pricing conversations I have heard about are rumors.

The second issue is that SK hynix is a memory-focused company, like Micron. Samsung also has logic and foundry capabilities.

As memory becomes more customized, those capabilities become more important. Samsung wants to show that it can do more than manufacture memory. It can also contribute on the logic side.

I understand that SK hynix is also building its own logic and memory-on-logic capabilities in the United States. That understanding comes from industry conversations.

It also wants to diversify demand. I have heard about efforts to expand business with AMD and other customers.

Daniel: A stronger AMD would presumably be helpful to the memory suppliers because it would reduce their dependence on one dominant customer.

Damnang: Yes.

During the HBM3 period, SK hynix was in a very strong position relative to Samsung and Micron. Other customers wanted access to its supply.

The competitive situation is changing. So SK hynix has reasons to broaden both its customer base and its own capabilities.

The two risks I would emphasize are NVIDIA concentration and the need to strengthen its logic-design capabilities.

Daniel: Can you explain what you mean by logic-design capabilities? Why do those matter for a memory company?

Damnang: Think about custom HBM and the base die underneath the memory stack.

You can put more logic there, such as memory-controller and interface functions. That is different from making the memory cells themselves. It requires a different process and different design capabilities.

Samsung has its own foundry, so it can use that capability for the base die. SK hynix works with TSMC.

Daniel: But is that necessarily a disadvantage? Doing everything in-house means more vertical integration, but also more complexity.

Working with TSMC could be an advantage if it gives you access to a very strong foundry. Why is owning the foundry or the logic capability better?

Damnang: Those are two different issues.

First, TSMC has capacity constraints too. But more importantly, TSMC can manufacture the base die. Who designs the logic on it?

If the memory supplier can design and implement that logic and owns the relevant intellectual property, it can capture more value.

Think about a company such as Broadcom. A lot of its value comes from the design capabilities and intellectual property it contributes to custom chips.

Samsung has memory-related and logic-related intellectual property. SK hynix needs to strengthen its position there. Otherwise, it may need to rely more on NVIDIA’s intellectual property or third-party providers such as Synopsys and Cadence.

That affects how much value it captures from the logic side.

This is why I keep returning to the shift from commodity memory toward custom memory. It is not only about producing a more advanced memory stack. It is also about who contributes and owns the design.

Further reading: Damnang explores this question of design ownership and bargaining power in more detail in [What NVHBM Means: The Contest for Power Over HBM Begins](https://www.damnang.com/p/what-nvhbm-means-the-contest-for?utm_source=chatgpt.com).

#### 7. Micron: You Do Not Have to Be the Technology Leader to Benefit

Daniel: As an investor, Micron can look a bit like a U.S.-listed version of the memory thesis at a higher valuation than SK hynix.

I have also heard secondhand comments that its engineering culture and yields are very strong, but I do not know how reliable those comments are. How do you see Micron’s technology and its position in the market?

Damnang: My view is that Samsung and SK hynix are the strongest two technologically, and Micron is third. I do not expect that technology gap to disappear quickly.

But that does not mean Micron cannot do very well.

I would compare it with AMD. I do not expect AMD to overtake NVIDIA, but AMD can still grow significantly because the overall AI market is growing so quickly.

If the market expands enough, there are customers and opportunities that one supplier cannot serve on its own. Another supplier can grow substantially without becoming number one.

I think about Micron in a similar way.

Micron also has a geographic advantage from its U.S. position, in my view. So when I invest in Micron, I am not simply making a statement that it has the best technology.

I am expressing a bullish view on memory and a view on U.S. policy. Those are important parts of the investment case for me.

#### 8. Samsung: Technical Integration Versus Organizational Complexity

Daniel: From your comments, it sounds as though you see important technical advantages at Samsung. It has memory, foundry, and logic capabilities, which could mean more intellectual property and more potential value to capture.

But as an investor, Samsung’s diversification is also what I like least about it.

When I buy a memory stock, I want exposure to the memory thesis. Samsung also has phones, TVs, and a lot of other businesses. It is a very large organization, and I worry about the complexity and internal politics.

SK hynix feels like a more focused way to express the thesis. At the same time, I understand your argument about vertical integration.

How do you weigh those two sides?

Damnang: I agree with the concern. Samsung’s size and structure create risks.

One issue I hear about is compensation across different divisions. When memory performs very well, people in other businesses can feel that their compensation does not reflect their contribution.

Even within semiconductors, people working on logic or in the foundry can ask: we help make the custom HBM base die, so why do we not receive the same rewards as the memory business?

I hear those complaints from people in the industry. Some engineers are very unhappy with the internal policies and culture.

That is a risk because these teams need to work together.

Daniel: As a founder, I also see another side to that. When talented people become frustrated with internal politics, some of them leave and build something new. It can create opportunities for other companies and for innovation outside the organization.

Damnang: Yes. But for Samsung itself, it is a real concern.

I have heard examples where someone needed help from another team, but the person on that team did not want to take on more work because they felt their compensation was not fair.

If you need collaboration between memory, logic, and foundry teams, that kind of incentive problem matters.

So the technical ability to combine those businesses is one thing. Getting the people and the organization to work together is another.

#### 9. Sandisk: A Commodity Can Still Have a Supply Constraint

Daniel: Sandisk has surprised me. When I first started looking at memory, much of the discussion focused on the big three and HBM.

The argument was that HBM is difficult to make, only a few companies can produce it, and other types of memory are more like commodities. But Sandisk’s stock has had an enormous rally.

How do you think about the company and the idea that NAND is a commodity?

Damnang: There are a few parts to it.

First, memory vendors want to move toward more differentiated products. For Sandisk, HBF is one possible route. If HBF succeeds, that could provide additional upside.

Second, I understand the concern that the stock has already gone up a lot. There has been a lot of excitement, and I partly agree with people who say a substantial amount of upside may already be reflected in the price.

Another part of the story is long-term agreements. Because the existing product is more commodity-like, Sandisk can try to make the business more predictable through customer commitments.

One route is changing the product through something like HBF. Another is changing how the existing production is contracted.

My understanding from industry conversations is that Sandisk wants a much larger share of its business covered by long-term agreements, and that it does not want to add substantial new fabrication capacity without those commitments.

That is a way of managing the supply expansion rather than simply building more and hoping the demand is there.

Daniel: But how do we reconcile two ideas: that NAND is a commodity, and that customers do not have an immediate replacement?

To me, a commodity sounds like something that is easy to substitute. Where does the bargaining power come from?

Damnang: There are other NAND suppliers. Samsung and Kioxia, for example, can compete in this market.

The point is not that Sandisk is the only company that can do it. The point is that adding semiconductor supply takes time.

Even when we call something a commodity, it is not the same as saying that a competitor can immediately produce as much as the market needs. It still takes time and capability to build that supply.

Daniel: So the important distinction is the delay between demand arriving and competitors being able to add capacity.

Damnang: Yes.

There is another point about the memory hierarchy. Much of the architectural change is happening in the middle layers. You can debate HBF or different arrangements of faster memory, but there is still a need for fast, reliable SSD storage.

If you make the rest of the system more efficient, a lot of cold data or information that is not immediately being used still needs somewhere to go. That supports the need for NAND flash.

So I am interested not only in which new architecture wins, but also in the storage layer that remains necessary underneath it.

That is why I see the NAND layer benefiting across different possible architectures.

Further reading: For a deeper look at HBF’s technical trade-offs, adoption prospects, and potential financial impact on Sandisk, read Damnang’s [Will HBF Create Upside for Sandisk?](https://www.damnang.com/p/will-hbf-create-upside-for-sandisk).

#### 10. CXMT and China: Look Beyond EUV Versus DUV

Daniel: Let’s talk about CXMT, both as a company and as a potential source of competition for the other memory suppliers.

How do you think about it?

Damnang: I understand the concern. People hear that China is expanding memory production, and they worry that supply will increase enough to cause another downcycle.

But CXMT requires a different investment framework because of the Chinese government’s role. I expect it to receive support even if it does not make money.

That is different from evaluating a company only on its commercial economics.

On the technology side, my view is that there are still gaps between CXMT and the leading memory suppliers. I also think some of the discussion about the Chinese competitive threat is exaggerated.

Daniel: Personally, I do not invest in Chinese stocks. That is not about taking a political side. It is about the risks I am willing to accept as an investor.

I worry about government intervention and about whether the interests of outside shareholders are protected. I also worry that heavily subsidized supply can change the economics for the rest of the industry.

So I have concerns both about owning the stock and about the impact additional supply could have on competitors.

Damnang: I recently spoke with Chinese investors who also had concerns about investing in CXMT. They were looking at the technology and other investment risks, and some preferred other memory companies.

The point I especially want to make about the supply risk is that people focus too much on EUV and DUV.

They say: China does not have EUV, but it can build more DUV equipment, so memory capacity will increase.

But making memory chips requires far more than lithography equipment.

You need inspection, testing, and many other types of semiconductor equipment. Companies such as KLA and Applied Materials are part of that broader equipment ecosystem.

The equipment restrictions and limitations are not only about EUV. You have to look across the entire manufacturing process.

Some reports say China can make all of these tools itself. My view is that replacing that whole equipment chain takes a long time. It is not something that happens immediately.

In my view, Chinese supply will not affect the market before 2030.

Editor’s note: This is Damnang’s forecast, not a verified supply estimate. State support for a business also does not guarantee a positive return or protection against loss for its shareholders.

Daniel: That is the issue with jumping from “China is entering the market” straight to “everything becomes worthless.” You still have to understand the technical and manufacturing constraints.

Damnang: Exactly.

#### 11. Is the Rally Over? And Which One Stock Would He Choose?

Daniel: To finish, let’s talk about the stocks at the prices prevailing when we are having this conversation.

Are you still bullish on memory, or do you think the rally has run its course?

Damnang: I do not think it is over. I still strongly believe there is another leg to the memory rally.

If you believe the longer-term memory thesis, small differences in the entry price matter less than whether you believe the stocks can go much higher. I think there can still be substantial upside, potentially a doubling.

Daniel: So you are broadly bullish on SK hynix, Micron, Samsung, and Sandisk. What about CXMT?

Damnang: CXMT could also do well, but it is not something I am focused on for my own portfolio.

I also want to be clear that CXMT is not a scam. It is doing real work and progressing quickly. I just do not think its competitive impact is as large, as quickly, as some people currently argue.

For memory stocks more broadly, the market may need some time to digest the rally. Investors take profits, and then they may reinvest as the next view of the sector develops. But I remain bullish.

Daniel: Let’s make it a forced choice. If you could own only one memory stock, which would you choose?

Damnang: For my own circumstances, Micron.

Daniel: Why Micron?

Damnang: I am in the United States, and I do not want to deal with the Korean stocks right now.

As I said, Samsung and SK hynix have very strong technology and can be good investments. But there are other risks to consider, including the way you access the Korean stocks.

For example, I am concerned about premiums on depositary receipts. If those issues changed, I could reconsider. But given the situation as I see it, I would choose Micron.

I already have a substantial portion of my portfolio invested in it.

Daniel: Interesting. Thanks for the conversation.

### My Closing Takeaway

The most useful part of this conversation was not a single ticker. It was the distinction between several questions that often get treated as though they are the same.

What does AI need more of? Which technologies are best suited to those needs? Which companies control the relevant designs and capacity? And which stock is the best way to express that view for a particular investor?

Damnang can be bullish on the memory sector, see technical strengths at Samsung and SK hynix, and still prefer Micron for his own portfolio.

Likewise, we can believe that NAND demand grows without assuming Sandisk is a monopoly. We can take Chinese competition seriously without assuming that an entire semiconductor manufacturing ecosystem can be replicated overnight. And we can believe that HBM changes supply dynamics without concluding that memory will never experience another downcycle.

For me, the most important question to keep following is how the memory hierarchy evolves, and who captures the value as it does.

##### Disclaimer

This article reflects my personal opinions and is provided for informational and educational purposes only. It does not constitute financial, investment, legal, or tax advice, nor a recommendation to buy, sell, or hold any security. I may hold positions in companies mentioned and may change these positions at any time without notice. Past performance is not indicative of future results, and investing involves risk, including the possible loss of principal. Always do your own research and make your own independent investment decisions.
