---
title: "An Investor’s Handbook I - AI Optics"
source: "Nutty"
author: "Nutty"
url: "https://nuttycld.substack.com/p/an-investors-handbook-i-ai-optics"
published: "2026-06-19T08:09:24+00:00"
words: 2860
preview_only: true
---

# An Investor’s Handbook I - AI Optics

### Information Needs No Mass

When we talk about “sending” something from A to B, the method changes completely depending on what, exactly, we are sending.

To send goods, you need a truck. To send power, you need a wire. To transmit force, you need gears or pulleys. They share one thing. Something with mass has to physically move.

Sending information is fundamentally different.

Late at night, blink a flashlight at someone standing far away. Short, long, short. That is Morse code. The ancient signal fires worked the same way. Light a fire on a mountaintop, and the next beacon tens of kilometers away sees it and lights its own. No matter with mass flew from peak to peak. What traveled was a pattern of light that the sender and receiver had agreed on in advance.

Here is the key insight. To carry information, no massive substance has to travel. All you need is a medium to carry the signal and an agreed way to read it. And the lighter, the faster, and the less energy that medium uses, the better.

Is there a medium that has no mass, moves at the fastest speed in the universe, and barely interferes with itself?

It is light.

To be precise, a photon has zero rest mass, but it still carries energy and momentum. Making light takes energy, and optical fiber has its own losses. Light is not magic. As a medium for sending information far, fast, and in great volume, though, its physical properties are overwhelmingly favorable.

### 1. The Steel Ball and the Laser

So what medium do today’s data centers actually use to send information? Picture two pipes.

#### The first pipe: steel balls.

You fire steel balls fast down a steel pipe. The balls have mass. They lose energy as they slam into the walls, and that energy turns into heat. The faster you fire them, the harder the collisions and the more heat you get. If another pipe runs alongside, the vibration in one leaks into the other. The longer the pipe and the faster the balls, the worse everything gets.

This is a signal inside a copper wire. The electrons themselves do not actually fly down the wire at data speed like steel balls. Information propagates as a changing electromagnetic field around the conductor, while the electrons drift along very slowly. The real problems in copper are resistance, the skin effect, dielectric loss, reflections, and crosstalk with the wiring next door. As the frequency rises, current crowds toward the surface of the conductor, each bit occupies less time, and the smear from the previous bit lingers into the next. The margin for telling a 0 from a 1 keeps shrinking.

#### The second pipe: a laser.

Now picture a glass tube whose inner wall behaves like a mirror. You fire a laser into it. The light stays trapped inside a thin channel as it travels. In a well-designed tube, it can go a long way with very little loss. Even with another tube right beside it, the light stays confined in the core, and because optical frequencies are so high, it does not couple electrically with neighboring lines the way copper does, so there is almost no interference.

Light has one more property worth pausing on.

Imagine a class of children running a race. Normally you have to cap it at fewer than ten at a time, because they collide. But what if those children could simply pass straight through each other? Then thirty, even a hundred, could run together at once. That is exactly what light does. Beams of different wavelengths pass through the same space while barely disturbing one another. The principle is called wavelength-division multiplexing, or WDM. You send several wavelengths, think of red, blue, and green, down a single strand of fiber together, then split them apart again at the receiving end.

The performance gap is overwhelming. A single copper line, with today’s technology, tops out at 100 to 200 gigabits per lane. Put WDM on one fiber strand and you get tens of terabits, hundreds of times more than copper.

Physics is overwhelmingly on the side of light. Which narrows the question to one.

Why are we still using copper?

### 2. Light Advances, Copper Retreats, and Then Came AI

There was no upset. Light has already beaten copper. Just from the long distances first.

In 1988, when the first fiber-optic cable, TAT-8, was laid across the floor of the Atlantic, it delivered ten times the capacity of the previous generation of copper cable in a single step. Light’s territory has widened steadily ever since. In the 1980s, thousands of kilometers between continents. In the 1990s, hundreds of kilometers between cities, led by WDM and optical amplifiers. In the 2000s, a few kilometers between data centers. In the 2010s, the tens to hundreds of meters between racks inside a data center.

Light always wins the long distances first, then works its way inward to shorter and shorter ones, taking the outer rings of a set of concentric circles toward the center, one at a time.

But copper still holds the short distances. There is an old saying in the networking business.

“If you can do it in copper, do it in copper.”

For a few hundred gigabits over a few meters, copper is cheap. It installs easily, and the installed base is vast. Optics needs a module that turns electricity into light at the sending end and light back into electricity at the receiving end. A laser, conversion circuitry, a transceiver. Because of all that cost, optics had to cede the short distances to copper.

Then this balance started to crack. Because of AI.

What AI changed was not simply “more data.” It was that tens of thousands of accelerators now have to work as one giant brain. That is the fundamental shift. In the early 2010s, four or five accelerators in a single server were enough. Today tens of thousands are bound together as one body. Those accelerators never go quiet for a moment until training ends. At every step they have to exchange results, and if that exchange is late, the next computation cannot begin. In synchronized training, a single link dropping for even a moment can leave thousands of accelerators idling, all waiting on that one.

So at some point the power a data center spends on computing and the power it spends on moving data drew dangerously close. Expensive accelerators increasingly sat idle, waiting for the chip next door to hand over data. The bottleneck had moved from computation to movement.

The era when rolling a hundred steel balls would do is over. Now copper’s front line is shaking.

### 3. Four Generations That Pull Light Toward the Chip

What does it actually mean for light to push toward the chip? It means moving the optical engine, the part that converts light to electricity, closer and closer to the chip that does the computing. This has unfolded across four generations.

#### First generation, pluggable.

A module you can plug into and pull out of the front of the equipment. The optical engine sits farthest from the chip, out on the front panel. The distance is the longest, and it holds a heavy signal-recovery DSP chip, so it also draws the most power. The upside is that when one fails, you just pull it and swap in another on the spot. It carries the strong advantages of standardization, hot-swap, and multiple vendors, and most of today’s optical-component revenue comes from here.

#### Second generation, LPO and NPO.

As signals get faster, that long electrical path from the front panel to the switch chip becomes more and more of a burden. So a design appears that drops the heavy recovery chip and hands its job to the SerDes on the switch side. This form, called LPO, brings the power of an 800-gigabit module down from around 13 watts to about 8. It gives up a little distance and signal margin in exchange for saving power. NPO, which takes the optical engine off the front panel and sets it on the board near the ASIC, is a step further in.

#### Third generation, CPO.

This places the optical engine right beside the switch chip package, shrinking the stretch where the signal travels as electricity down to millimeters. The power drops dramatically. The cost is that the expensive switch chip and the optical engine are now fused into one body, which makes servicing hard. That single fact comes back to haunt it again and again.

#### Fourth generation, Optical I/O.

Literally, the stage where a chip handles its input and output to the outside world directly with light rather than through electrical pins. The optical engine becomes a chiplet, a small tile that sits next to the accelerator, talking to the electrical chip over the shared interface between chiplets. The electrical distance between the light and the chip shrinks to the thickness of a few strands of hair. This is an attempt to carry light past the switch and all the way inside the accelerator package.

There is something here that has to be made clear.

CPO and Optical I/O are not the same thing.

Because the market uses these words interchangeably, many people see only the shared fact that they “use light” and treat them as one theme. But they merely point in the same direction; they are not the same stage of technology. Pluggable and LPO are today’s revenue. CPO is a medium-term transition becoming visible on the switch side. Optical I/O is a long-term platform aimed at chiplets and the inside of the package. Three clocks run at different speeds. Draw them as a single straight line and you misread the entire timeline.

And one more thing. As light moves closer to the chip, the hard part is not the light itself. It is attaching the light to the chip. Packaging, heat, optical alignment, and how you fix it when it breaks. The new battlefield has moved here.

### 4. But Silicon Cannot Make Light

The name “silicon photonics” invites a misunderstanding, because it sounds as if silicon makes all the light. It does not. Silicon barely makes light at all.

This is a matter of physics, not marketing. Picture a ball on a high shelf. When it drops to the floor, it releases energy equal to its height. In a semiconductor too, when an electron falls from a high energy state to a low one, that difference can come out as light. This is the principle behind LEDs and lasers.

The catch is that the shape of the shelf differs by material. In a direct-bandgap material like indium phosphide (InP) or gallium arsenide (GaAs), the ball drops straight off the edge and gives off a clean photon. In an indirect-bandgap material like silicon, the ball is caught on a lip at the corner of the shelf. It becomes a low-probability process that has to satisfy not only energy but a momentum condition too, and that needs a lattice vibration, a phonon, to step in. So no matter how hard you push silicon to give off light, it barely does.

Strictly speaking, “silicon can never make light” is an overstatement. Workarounds such as silicon-based emission, III-V-on-silicon, and quantum-dot lasers are under research. But in 2026, the core materials that make light for large-scale data-center optical links are still InP and GaAs. InP in particular is the workhorse light source for the 1,310-nanometer and 1,550-nanometer bands, where fiber loss is lowest.

So why use silicon at all? Because even though it cannot make light, it is superb at handling light. Its high refractive index lets it confine light inside a waveguide a few hundred nanometers wide; you can build modulators, filters, and detectors on top of it; and above all, you can mass-produce it with existing semiconductor processes. On top of that, the size of an optical device is set by the wavelength of light, not by the transistor, so there is no need to chase ever-finer geometries. That is why many photonic integrated circuits (PICs) are made on mature nodes like 45 and 65 nanometers. Old fabs pushed out of the race for finer process nodes find new life in optics.

So the real-world solution is a division of labor. III-V materials make the light; silicon guides it, modulates it, and integrates it. You bring the light source in from outside and gather everything else onto silicon.

Hold on to this one sentence. It becomes the most important point in the back half of this piece. It is not silicon that makes the light.

### 5. Inside and Outside: Why Copper Has Not Lost Yet

To see how far light has come, you have to split a data center’s connections into three zones.

The closest zone is scale-up, the connections that bind accelerators together inside a single rack. The distances are shortest and the bandwidth demands are the most ferocious. Interestingly, this is exactly the zone where copper still has the edge. For pushing enormous bandwidth over short distances at the lowest cost and power, nothing beats copper yet. The backplane inside the latest generation of racks is, in fact, woven from thousands of copper wires.

This zone has a clock on it too. The bandwidth a single accelerator sends and receives doubles each generation, climbing from 7.2 terabits per second to 14.4. As bandwidth grows, so does the pressure to pack more accelerators into one group, and copper’s reach caps how big that group can be. At the 224-gigabit-per-lane generation, the distance passive copper can cover shrinks to around a meter. So active electrical cables (AECs), which put a small recovery circuit at the head of the cable, appear to stretch the reach back out. The Annapurna retimer that MaxLinear ($MXL) unveiled in 2026 is a chip that keeps copper backplanes and AECs alive at 224 gigabits per lane. The company puts it precisely: optics is essential at long range, but at short range copper still holds the advantage in power, latency, and cost. The industry’s gaze points one way. Even this innermost ring will have to cross over to light a generation or two from now. Just not “now.”

Next is scale-out, the links between racks. The moment the distance grows, copper steps back and light moves in. Each accelerator carries several optical transceivers. This is already light’s territory. Choosing copper for scale-up does not shrink scale-out optics. As the number of accelerators and the throughput inside a rack rise, so does the data flowing out of it.

Last is a relatively new idea, scale-across. It binds building to building, stitching separate data centers into one giant training fabric. As AI infrastructure grows too large to fit on a single power grid, this zone is expanding fast. It calls for more sophisticated coherent optics, narrow-linewidth lasers, and optical amplifiers.

To sum up: light is advancing, yes, but copper is not retreating overnight. The market’s center of gravity has already shifted from “optics for everything” to “the right tool for each zone.” So you should not read the news that “NVIDIA ($NVDA) used copper inside the rack” as bad news for optics as a whole. There is more than one front line.

### 6. The Map So Far, and the Question That Changes

Let me retrace the path so far.

Information travels without mass. Light has no mass, no charge, and barely interferes with itself. Physics is overwhelmingly on the side of light.

Light won the far distances first, and it keeps coming closer. From the ocean to the city, to the data center, to the rack, to the server. AI sharply accelerated that advance.

The technology that pulls light toward the chip is evolving across four generations. Pluggable and LPO are up against a power wall, CPO against a wall of heat and serviceability, and Optical I/O is still at the threshold.

But in the closest zone, copper is still holding on. Light’s advance and copper’s retreat move at different speeds.

The technical terrain is now drawn. From here, the question changes.

In years past, this is where we would ask “who stands where on this map.” But the real story of 2026 is not where everyone is looking. It is not the flashy CPO switch, nor the chiplet roadmap. It is one layer down, at the place where light is “made.”

One of the most cash-rich companies in the world stopped ordering optical components and started buying the factories that make them.

An order places a bet on demand. Buying a factory means paying up front to make sure that factory exists at all. They are entirely different acts. When the smartest deep pocket in the room starts buying factories instead of placing orders, it tells you one thing. Whatever comes out of those factories is a real bottleneck, the kind money alone cannot easily buy.

What that something is, who holds it, and where the smart money quietly flowed while everyone else argued over CPO. This is where the real heart of the piece begins.
