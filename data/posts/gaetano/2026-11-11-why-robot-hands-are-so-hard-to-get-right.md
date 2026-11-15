---
title: "Why Robot Hands Are So Hard to Get Right"
source: "Gaetano"
author: "Gaetano"
url: "https://gaetanoresearch.substack.com/p/why-robot-hands-are-so-hard-to-get"
published: "2026-11-11T04:48:47+00:00"
words: 1254
preview_only: true
---

# Why Robot Hands Are So Hard to Get Right

With this packed earnings period we’ve spent so much time going through company results.

Let’s take a step back for a bit and dig into some humanoid research.

I want to spend this one on the hands.

In [the earlier humanoid article](https://gaetanoresearch.substack.com/p/when-do-humanoid-robots-actually) we went through what could get these robots from a few units being tested to hundreds of them actually working.

And a lot of it comes back to something that seems pretty basic. Can the robot pick something up and do the job with it? Keep doing it, all day, with someone coming over to help only occasionally?

The hands are so intricate. Think about it. Pick up a pen and turn it around in your hand. You probably moved a few fingers, loosened your grip in one spot and tightened it somewhere else. It takes almost no thought. Now try to describe all of that to someone building a hand from scratch. Where do the motors go? How does it feel the pen starting to slide? How hard should it squeeze? There is a lot going on in this tiny space, and the decisions start affecting each other pretty quickly.

Some of the companies we’ve been talking about are already working on pieces of this. ALGM, NVEC, VPG. We have named integrations, customer orders and sensor development to look at.

First, look at this. A Shadow hand holding a light bulb, photographed in 2007. All that hardware coming through the wrist and these fingers wrapped around thin glass. People have been at this for a long time! Just getting the fingers to close around something took a lot of work. Then you start asking the hand to use it.

### Picking it up, then doing something with it

Back to the pen. Picking it up gets it off the table. To write with it, you have to settle it between your fingers, turn the point toward the paper and hold it there as you move. The object moves around inside your grip. Some fingers let it slide while others keep it from falling. Your thumb comes across from another direction and helps hold the whole thing together.

‘Dexterous manipulation’.

For plenty of factory jobs, the part shows up in the same spot and just needs to be moved somewhere else. Look at Baxter’s two-finger gripper below. Close around the part, move it, release it. If you can do the whole job that way, you have fewer moving pieces to buy and keep working. A customer can get quite a lot out of a setup like this.

But say that same robot is going to open a drawer, take a tool out and then use the tool. Now the grip changes as the job changes. A hand with more movement has more ways to get through that sequence. And we already have drawers, handles, tools and workstations everywhere that were built around people using them. Getting a robot to work with what is already there would save a lot of redesigning around the robot. I think it’s quite easy to see the appeal, but you can also see how quickly the hand itself gets complicated.

### How the fingers move

Let’s start with how a finger bends. Some of the muscles moving your own fingers sit back in your forearm, and tendons carry the force through the wrist. Follow them in the drawing below. They have quite a distance to travel before they reach the finger.

So you can put the motors farther back and run tendons out to the fingers, much like our own hands. Lighter fingers, more room at the tips. Makes sense.

But now you have this tendon running from the motor out to the joint and it stretches a bit. It rubs against the guides. The tension changes as the finger bends, and you keep doing that over and over. Eventually it wears and someone has to replace it. Then get the tension right again. Even the decision to move a motor farther back follows you all the way through to the person fixing the hand later.

Or you can fit more of the machinery into the hand itself, using gears and rigid links to move the joints. We’ve talked about actuators before. For an electric hand, think of the motor and the mechanism carrying its movement out to the joint. Put that assembly close to the finger and the finger carries more hardware. Move it farther back and you have to get the movement out there somehow.

There are different movements to account for too. Curl your index finger. Then spread it sideways. Your thumb can come across your palm and meet the other fingers, which is especially helpful for holding little things. These independent ways of moving are called degrees of freedom (DoF). A hand might have a big DoF number, but the placement of those movements tells you a lot more about what it can do. Having a thumb that can get around an object changes the grip available to the whole hand.

You can also use a single motor to bend several joints together. Pull a tendon, the finger closes, and when one section hits the object the other joints can keep wrapping around it. That’s called underactuation. Fewer actuators than degrees of freedom. It’s a way to get a useful grasp while saving some hardware. For moving the pen around inside the hand, separately controlled joints give you more options. Then the software has to coordinate those options.

Here’s an example from [a 2021 research paper](https://www.nature.com/articles/s41467-021-27261-0). The researchers built the motors, links and sensing into the hand, which they call ILDA. You can see the whole assembly on its own and attached to an arm.

And here is one finger opened up. Look at the little links connecting the joints. All of that has to fit inside something narrow enough to work alongside the other fingers.

Want a stronger grip? A bigger motor can help, and gears can turn fast motor rotation into slower, stronger movement. Then you have the weight of that motor, the heat it makes and the friction in the gears. There’s a little play in the mechanism too. Add the bearings, wires and sensors, then put a cover around everything. Even if you get it all to fit, the arm still has to lift it. So a change that looks pretty straightforward at the motor can end up affecting the whole robot.

MinebeaMitsumi showed [a hand prototype at CES 2026](https://tech.minebeamitsumi.com/en/pickup/humanoidrobot/index.html) with 85 miniature and small bearings and 11 actuators. It developed the drive unit with Harmonic Drive Systems.

85 bearings in one hand.

That makes the mechanical side of this easier to picture. Every joint has to move smoothly in a small space, over and over. This is a prototype, so it gives us an example of the hardware being developed. As these designs get into production, the particular parts that survive all that testing are the ones a customer would keep ordering.

Even the stiffness is something you can design around. Let a finger give a little when it bumps into an object and it can absorb some of that unexpected contact.

‘Compliance’.

Researchers at the German Aerospace Center have [a tendon-driven hand with adjustable stiffness](https://www.dlr.de/en/rm/research/robotic-systems/hands/david-hand).

It can be firmer for one task and more forgiving for another. Think about first reaching for the bulb, then holding it while the arm moves. Those are different demands on the same fingers.

### Getting the finger to the right place
