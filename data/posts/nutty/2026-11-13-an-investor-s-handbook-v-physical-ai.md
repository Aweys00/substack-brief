---
title: "An Investor’s Handbook V - Physical AI"
source: "Nutty"
author: "Nutty"
url: "https://nuttycld.substack.com/p/an-investors-handbook-v-physical"
published: "2026-11-13T06:42:12+00:00"
words: 1385
preview_only: true
---

# An Investor’s Handbook V - Physical AI

Industry and technology analysis, not investment advice. The author may hold positions in the companies mentioned.

The robot is on site. The model calculating its next move is in the cloud.

When robot AI developer Physical Intelligence introduced its [Pi API beta](https://www.pi.website/blog/api-beta) in October 2026, it said most of the applications it showed ran their models in the cloud. Developers upload task data, fine-tune a model for the job, and receive actions from a server when the robot operates.

Then why not bring a robot home and say, “Clear the dishes after dinner. Fold the laundry, too.” It could ask a more capable model on a server about unfamiliar tasks and get better as new models arrive. It seems the robot would not need to have mastered everything on the day we buy it.

It is an appealing thought. There is still much for a machine to learn before a server’s decision becomes physical action. Recognizing an object, moving a hand, and adjusting force after contact are different problems. A robot therefore needs more than a model that chooses actions: it also needs parts that move its joints and sensors that detect contact.

### Robots in Factories and Warehouses

A factory robot arm can know in advance where a part will be. A fixture holds it in place, and a conveyor brings it in from a set direction. People stay out of the robot’s working area. Factory design does some of the work of making the machine intelligent.

This approach has brought the global operating stock of industrial robots to about 5.08 million, according to IFR’s count for 2025. Learning models are now taking on some of the work that people find harder to arrange in advance.

Think of clothes returned to an online retailer. They do not arrive neatly laid out in the same shape. European fashion retailer Zalando (Xetra: ZAL) uses robot arms and AI models together to process returns. Universal Robots (UR) supplies the arm, while robotics AI company Sereact supplies the model that looks at an item and chooses a grasp. An established robot-arm design gains the ability to handle objects whose positions and shapes change each time.

Digit, deployed by logistics company GXO (NYSE: GXO), stands on two legs and carries totes. The starting point here is also a defined task, rather than a machine that does every job in the warehouse. Customers can measure throughput and downtime, while developers collect recurring failures from the same process. Learning models can start with carrying and sorting tasks that customers already pay robots to perform.

### Five Seconds We Can Wait

Imagine asking a robot to clear the table. It spends five seconds looking around before it moves. The dishes stay where they are, and you go off to do something else. A brief wait can be acceptable, just as it is when we ask ChatGPT a question.

A car traveling at 50 km/h covers about 69 meters in the same five seconds. When it must respond to a vehicle braking suddenly, those seconds mean something very different. A dishwashing robot also cannot wait for the server’s next answer once a glass begins to slip from its hand.

What matters is not just how many seconds the model takes, but what can change during those seconds. A model that plans the task sequence can run in the cloud, while the robot handles the fast control needed for contact and balance.

### From Language Models to Action Models

“Put away the stationery on the desk.” A language model may recognize the pencils and erasers and understand the request. A robot needs the next step: where its hand is, which part of the pencil to grasp, and how far to close the gripper.

A vision-language-action model, or VLA, learns this connection. It receives images, an instruction, and information such as current joint positions, then outputs actions. Instead of ending with a verbal explanation, it produces numbers such as target hand positions or gripper movements.

Gemini Robotics, developed by Google DeepMind, part of Alphabet (NASDAQ: GOOGL), is an example of adding action outputs to Gemini. The image below comes from Google’s public demonstration. The robot uses its understanding to pick up objects on a desk, going beyond naming them.

Physical Intelligence’s [π₀, or pi-zero](https://www.pi.website/blog/pi0), also builds robot-action learning on a pretrained vision-language model. Knowledge of objects and language from the internet provides a starting point. A photograph, however, usually does not record where the robot’s joints were, which motor commands it issued, or what happened next. Those records have to be collected by operating robots.

A different body requires different actions. Joint angles learned with a short arm cannot simply be applied to a longer one. Training on data from different robots and tasks aims to use shared understanding of objects while producing movements suited to different bodies.

This shows both the advantage of language-model companies such as OpenAI and Anthropic and the challenge robotics specialists are working on. The former have strong image and language understanding and task reasoning. The latter collect data on actual movements and failures. Google’s example combines these capabilities within a model family; other systems connect several models.

In Anthropic’s [July 2026 experiments](https://www.anthropic.com/research/claude-plays-robotics), the choice of interface made a substantial difference. Consider a quadruped. One approach asks a language model to choose the force for each leg joint directly. Another lets it tell a controller already trained to walk, “Move forward at this speed and turn in this direction.” In the second approach, the language model uses camera images to choose a direction, while the locomotion model coordinates the four legs and balance. The models performed much better when using those pretrained controllers.

The work of moving an arm can also be divided. An action model sets the next target, while a lower-level controller reads the actual joint state from sensors and adjusts motor output. If the model sends a short sequence of movements at once, it can calculate the next sequence while the robot executes the current one. Physical Intelligence’s RTC accounts for the movements already made so that new instructions follow smoothly.

Bottom line

Deciding where to go and coordinating four legs to get there do not have to be the same model’s job. Language-model knowledge can be used alongside an action model trained on robot data and a controller responsible for execution.

### The Judgment Hidden in Housework

“Clear the desk” requires more than picking things up. Can the crumpled receipt be thrown away? Can a charging cable be unplugged and put in a drawer? People draw on habits and an understanding of what objects are for. A robot may need to ask about the user’s intent or remember an earlier instruction. A task objective fixed in advance at a factory becomes part of a conversation at home.

What happens after a failure matters too. If a drawer will not open fully, should the robot pull harder or first remove something caught inside? Repeating the same movement does not resolve the question. Trying again with the same force can make matters worse. Identifying the cause and changing the sequence are part of what makes household robotics difficult.

Humanoid developer Figure demonstrated Helix 02 performing dishwasher tasks and moving between locations for roughly four minutes. Another developer, 1X, combines its home robot NEO with scheduled remote expert assistance for tasks it has not yet learned. While a customer feels that the robot has taken over a chore, a person may still be working on the supplier’s side.

Recording a person’s movements to teach a robot creates a different cost structure from having a person complete each customer task. Training data may be used by many robots later. Remote support needed for each job can add to staffing requirements as more machines are sold. If the same task requires fewer remote interventions, the manufacturer can reduce the labor cost of supporting each additional customer.

Coming Up

Does every new skill have to be taught on a physical machine? If one learned movement can be shared across thousands of robots, where does more of the value lie: in the body or in the software that moves it?

And how can we distinguish a company whose share price already anticipates that future from one whose profits still come from other businesses?
