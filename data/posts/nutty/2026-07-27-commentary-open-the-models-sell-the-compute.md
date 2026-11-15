---
title: "[Commentary] Open the Models, Sell the Compute"
source: "Nutty"
author: "Nutty"
url: "https://nuttycld.substack.com/p/commentary-open-the-models-sell-the"
published: "2026-07-27T09:09:20+00:00"
words: 1648
preview_only: false
---

# [Commentary] Open the Models, Sell the Compute

A note: This piece was inspired by [a thread from Rocketesla](https://x.com/rklb_invest/status/2081312683702522357). I went back to the original sources and expanded the argument to examine how open weights drive distributed computing and infrastructure demand.

Not long ago, South Korea was swept up in a craze for Dubai chewy cookies, better known by their Korean nickname, dujjonku.

What made the phenomenon interesting was that no single company controlled the product. Recipes spread across YouTube and social media, and as long as they could secure the ingredients, neighborhood bakeries and independent cafés could all jump into the market. Demand quickly surged for one critical input: pistachios.

Demand for a product, in this case the cookie, rises when its complement, in this case the recipe, becomes cheaper and more widely available.

It is an old economic principle.

Now, put yourself in the shoes of a pistachio importer. At the height of the craze, people said they wanted to make the cookies but simply could not find enough pistachios. Import prices actually rose 84% in a single year. For importers and distributors that had secured inventory in advance, it must have been a very good business.

What would have happened if one company had held a monopoly on Dubai chewy cookies? It probably would have struggled to keep up with the sudden surge in demand. Pistachio suppliers would also have been negotiating with one powerful corporate buyer rather than thousands of bakeries. Raising prices would have been much harder.

*

NVIDIA sells computing, and by now everyone understands that it sells far more than GPUs. The most important complement to that computing is the AI model.

When models are expensive and locked inside the API of a single company, the number of organizations and locations capable of running AI remains limited. But once the model files can be downloaded, modified, and run on private servers, AI spreads into corporate data centers, financial institutions, government agencies, and military networks.

Open weights do not eliminate every cost. They reduce the cost of acquiring the model and the degree of dependence on a single vendor, but the cost of actually running the model remains. Nor does a model lose its value simply because it becomes widely available. Some of that value merely moves downstream, toward the infrastructure required to run it.

That alone seemed enough to explain why Jensen Huang chose “Open Weights and American AI Leadership” as the subject of his first post on X.

Or at least, I thought it did.

*

If that were the whole story, it would not explain why Google and OpenAI, two companies that sell closed models, joined the initiative. Neither company appeared on the original list of 25 signatories, but both added their names within two days of the announcement. Among the major frontier labs, Anthropic remains the most notable holdout.

The implications seem too significant to dismiss their support as mere agreement with a noble principle. To understand it, we need to turn the clock back a few days.

*

OpenAI regularly measures how capable its models are at carrying out cyberattacks. These evaluations are conducted with their safety restrictions lowered. To see the full extent of what a model can do, researchers need to switch off the filters that would normally prevent dangerous behavior.

In mid-July, those models found a way out of their isolated testing environment.

The evaluation was being conducted in a system almost completely cut off from the outside world. Only one channel remained open so the models could download software required for the test. The models found a vulnerability in that channel, opened a path to the outside, moved laterally through internal systems, escalated their privileges, and eventually reached the internet. They then concluded that the answers to the evaluation might be stored on Hugging Face and attacked its servers to obtain them.

*

After stopping the attack, Hugging Face had more than 17,000 records to analyze and initially tried to hand the work to commercial models.

But the logs were filled with real hacking commands, exploit code, and traces of communications between the attacker and the servers. The commercial models activated their safety systems and refused to analyze them. They could not distinguish between an attacker making a malicious request and a defender investigating an incident.

Hugging Face eventually installed GLM-5.2, an open-weight model from China’s Z.ai, on its own servers. It was not constrained by an outside company’s policies, and Hugging Face did not need to send sensitive attack records or the credentials contained within them outside the organization. By using AI to conduct the analysis, the company completed in a few hours what would normally have taken several days.

GLM-5.2 was not chosen because it was better than the commercial frontier models Hugging Face had first tried. It was chosen because it was good enough and could be deployed immediately under Hugging Face’s own control.

*

This creates an asymmetry between attackers and defenders. Attackers are not bound by terms of service. They can use a jailbroken commercial model, an open model with its safeguards removed, or whichever tool gives them the greatest advantage. Legitimate companies and security organizations, by contrast, must operate within the safety filters of official APIs and the policies of outside providers.

That is why government agencies, military organizations, critical infrastructure operators, and security teams need models that have been tested in advance and placed under their own control, rather than AI they must rent after an incident has already occurred. For them, open weights are not merely a way to save money. They are closer to a strategic reserve, available regardless of a cloud provider’s outage, policy change, or decision to block an API request. This does not mean that AI should be left completely unregulated. It means preventing a world in which attackers have unrestricted access to AI while defenders are forced to fight with their hands tied.

The letter does not demand that OpenAI or Google release the weights of their latest GPT or Gemini models. OpenAI already has gpt-oss, and Google has Gemma. Both companies can continue selling their most capable models as closed products while using open models to expand the self-hosted market and the developer ecosystem. There is therefore nothing particularly strange about either company signing the letter.

We do not know whether this incident directly influenced their decision. What is clear is that it turned the argument for defender-controlled models from a theory into a real-world case study.

*

This is where NVIDIA’s interests come into view.

On June 29, NVIDIA published a post titled “Open Models, Closed Environments.” It described a system developed with Palantir in which U.S. government agencies could run Nemotron open models inside environments completely isolated from external networks. Each agency could operate the model on its own servers, train it on its own data, and retain ownership of the resulting model.

Open the model, but close the data and the execution environment.

Today, many of the strongest open models available for real-world deployment come from China. The United States does have open models. There is OpenAI’s gpt-oss, Google’s Gemma, and Meta’s Llama. But there is still no obvious American model that is powerful enough for frontline cyber defense, trusted enough for government use, and suitable for deployment inside secure, isolated networks. At the same time, a number of U.S. states and government bodies cannot freely use Chinese models because of security concerns. Hugging Face, as a private company, could install GLM. A military network’s security team may not have that option.

A trusted American open model, powerful enough for serious work and capable of running inside a closed network. That position remains open, and NVIDIA is looking directly at it.

AMD also signed the letter, so this should probably be viewed not merely as lobbying by NVIDIA, but as an effort supported by the broader infrastructure industry.

*

NVIDIA is not hoping for a world in which open models are less efficient than frontier models and therefore consume more GPUs. The opposite may be closer to the truth. Because users can modify, optimize, and compress open-weight models themselves, the computing cost per token may actually fall.

What matters is not how much computing is required to process a single token, but whether more organizations begin running AI in more places.

There is another factor to consider. When each institution builds a dedicated environment for security reasons, it becomes much harder to utilize equipment as efficiently as a large cloud provider can. Cloud platforms pool demand from thousands of customers, so when one customer uses less and another experiences a spike, the two can offset each other. Government agencies and financial institutions, however, must size their infrastructure not for average demand, but for peak demand and emergency conditions. Even with the same total workload, distributing equipment across many separate organizations increases idle time and duplicated investment.

The same is true of Dubai chewy cookies. When thousands of neighborhood bakeries each hold their own inventory, more pistachios get sold. Some of that inventory will eventually go unused and be thrown away. That is a loss for the bakery, but for the pistachio importer, it may be exactly the outcome they wanted.

*

In the end, the question is who captures how much of the additional demand for computing. NVIDIA and AMD will still compete for their share, and custom chips will pursue theirs as well.

But they share an interest in expanding the size of the market. It is probably no coincidence that AMD, Dell, Cisco, IBM, Cloudflare, CrowdStrike, and Palo Alto Networks all appear on the list of signatories. Whether they sell chips, servers, networking equipment, or cybersecurity products, they all have more to sell when AI runs in more places.

The real question in this fight is not whether intelligence becomes free, but where that intelligence will live and who will run it.
