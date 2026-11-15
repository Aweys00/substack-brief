---
title: "The PAM4 vs PAM6 Dilemma for 448G Copper Interconnects"
source: "Vik's Newsletter"
author: "Vikram Sekar"
url: "https://www.viksnewsletter.com/p/the-pam4-vs-pam6-dilemma-for-448g"
published: "2026-10-11T16:57:26+00:00"
words: 1730
preview_only: true
---

# The PAM4 vs PAM6 Dilemma for 448G Copper Interconnects

It’s been an interesting week in the networking world. I was at a meeting organized by the Ethernet Alliance called Technology Exploration Forum (TEF), and a bunch of smart people were trying to figure out how to make copper work at the 448 Gbps speeds.

Signal modulation and its impact on interconnects is often discussed in academic circles and industry research, but we might be at a time where the industry is seriously considering PAM6 as an alternative to make copper work in the next speed generation.

We’ll walk through this idea in a step-by-step fashion, starting with NRZ and ending with PAM6, and discuss what its implications for copper interconnects are.

By reading this post, you agree to the [terms and conditions](https://www.viksnewsletter.com/p/terms-and-conditions). Also see the [full ethics statement](https://www.viksnewsletter.com/p/ethics).

If you’re new, check out the [About page](https://www.viksnewsletter.com/about). A lot of readers expense the subscription to this newsletter as it helps their professional work. Group subscriptions (3+) are 20% off. If you have any questions, reply to this email and let me know!

For the full post, upgrade to a paid subscription

Check out the [Semi Doped podcast](https://www.viksnewsletter.com/about#§semi-doped-podcast), and [our daily free newsletter](https://daily.semidoped.com/) with latest semi news. For institutional research, contact me at [SemiExponent](https://www.viksnewsletter.com/about#§semiexponent).

#### Pushing Copper’s Limits

Copper has largely been declared dead in the era of 448 Gbps interconnects.

The impact of skin effect losses, where current crowds on the periphery of a conductor carrying fast moving signals, is too debilitating at these speeds. As a result, a signal degrades rapidly within a short distance.

At 224 Gbps speed, this distance was a little lesser than 2m. Doubling the speed roughly cuts the reach in half: 448 Gbps is limited to about 1m, or less, depending on the signal quality you are looking for. This is too short to connect hardware within an AI rack.

The speed limitation is tied to what the losses of a copper cable are at a given frequency, called the Nyquist frequency, which is then tied to the modulation of the signal being carried by the wire. Time to explain the word salad.

#### NRZ Modulation

When you say 448 Gbps, you think of sending one bit at a time (0 or 1, low or high voltage) 448 billion times in a single second along a wire. You would be right if you were using Non-Return-to-Zero (NRZ) modulation: a fancy way of saying let’s take the 0 bit and send 0 volts and take the 1 bit and send some fixed higher voltage that is not zero. If you overlap all the 0s and 1s passing through a window of time, you get the eye diagram shown below.

You think of each bit as a symbol in NRZ (we’ll understand why next, hang on), and in this case, symbol rate = data rate. Symbol rate is measured in Baud. So, 448 GBaud in this case.

There is a magical frequency called the Nyquist frequency, which is defined as half the symbol rate, where the loss of the signal cannot be too heavy. If it is, the signal is not recoverable anymore. So for a 448 GBaud symbol rate, the losses at Nyquist frequency of 224 GHz should be acceptable.

Running a copper cable at 224 GHz is laughable. At these frequencies, there is a good reason why RF engineers use waveguides. Skin effect from copper will obliterate a signal at the end of a 1m long cable at 224 GHz.

So what do we do?

#### Pulse Amplitude Modulation 4-Level (PAM4)

Let’s try and get clever about this and take two bits at a time: this gives four possibilities — 00, 01, 10, 11. Then you say, instead of mapping that to two voltages, you map it to four: 0V, 0.33V, 0.66V, 1V. You just “modulated” the signal into a 4-amplitude levels.

Now you’re going to work out for yourself how the problem gets better. Ready?

Think about it. Where you were sending 1 bit in a symbol, now you’re sending 2 bits to a symbol. To get 448 Gbps by running 2 bits per symbol, you need to only send half the number of symbols per second. If you selected 224 GBaud, you are correct. If not, now you know. The next question should be easier if you remember Nyquist frequency is half the symbol rate.

If you are running a 224 GBaud symbol rate, Nyquist frequency is half that, or 112 GHz. Can you send a PAM4 signal at 112 GHz along a copper wire? Yes — to about a distance of 1m.

TE Connectivity showed how you can use co-packaged copper (CPC) cables to get from the ASIC to the front panel (about 0.3m), through a direct-attached-copper (DAC) cable (1m), through another CPC cable (0.3m) to the next ASIC. A total of about 1.6m, or if you count only the DAC, 1m.

The loss is shown on the top left plot in the grid below. You can see that the signal has -35 dB loss at 112 GHz, after which the loss craters. Note that -30 dB is already only 0.1% of the original signal. Every 3 dB below that is half that signal power. At -36 dB, you’re looking at 0.025% of the original signal. That’s low, but recoverable.

What does recoverable mean? A way to characterize the quality of a recovered signal is to measure the Bit-Error-Rate (BER) of the signal — aka, how many bits recovered are flat out wrong compared to what was originally sent. If you detect a 0 where it should have been a 1, that’s a bit error.

TE Connectivity’s graph is shown below, and provides a few more interesting details. The plot on the left with the green color is what we just looked at, for a 1m DAC cable but “end-to-end’ — including the end connectors and CPC. It gives a loss of -46 dB and BER of 1.4e-6. About 1 in a million bits go bad. That’s passable because there advanced techniques like error correction that can push it to lower BER.

The green curve on the right is for a 2m DAC cable. The loss is -63 dB at 112 GHz, which means that there is almost no signal power left. That’s about 2 million times lower power than what was sent; copper losses have obliterated everything. The BER is 1.2e-1, or about 1 in 10 bits are bad. That is a terrible outcome considering how much data we will be sending in an AI cluster (we are talking Terabits, and you can’t have 100 Gigabits go bad.) No amount of error correction can fix something so bad.

All hope is not lost if you can put a circuit called a “re-driver” on the receiving side that takes the weak signal and boosts it before trying to recover the bits. That’s a logical approach, and TE Connectivity shows this as the blue curves in the plots above. They use a simulation model of a Semtech re-driver. You can see that the losses get better: -32 dB for 1m, and -49 dB for 2m, and the corresponding BER values also improve to 5.8e-6 to 1e-7 (or lower).

The price of doing is that now you are burning some power to have this re-driver chip. Nothing is free. You went from a purely passive copper cable, to using an active cable. Hyperscalers are pretty adamant about not using extra power though, and not having more components like re-drivers that need a supply-chain and can fail. How can we keep this purely passive?

Enter PAM6, and if you’ve been following so far, now things get a bit … funny. Try and answer this:

Next, we will discuss the madness that is PAM6.

#### Pulse Amplitude Modulation 6-level (PAM6)

If you grouped 2 bits together, you got PAM4. If you group 3 bits together, you get 2^3 = 8 levels, or PAM8. To get 6-amplitude levels or PAM6, you need to group log2(6)=2.585 bits together. Let’s just say 2.5 bits for now. How do you group half a bit?

Well, you don’t. The most practical and common approach to generate PAM6 is to map 5 bits across two symbols, which effectively maps to 2.5 bits/symbol. Mapping 5-levels involves 2^5 = 32 signal levels, which is quite a jump from four. Instead, what engineers do is to use 2-dimensional mapping. You take the signal, multiply it by a cosine signal and call that the “in-phase” signal. Similarly, you also multiple it by a sine signal and call it the “quadrature” signal. Now you can represent 32 points across a plane in what is called “Quadrature Amplitude Mapping” or QAM-32.

The constellation of points for QAM-32 is shown below.

The random number ordering you see is to keep adjacent levels far away from each other in the constellation so that you don’t mistake one adjacent level for the other. Notice how many levels there are across any row or column. There are a maximum of 6 levels, which fits nicely into 6-level amplitude modulation, or PAM6.

Skip on first read: Its also a good thing the corner symbols are missing because those represent the highest energy symbols which we don’t have to transmit. There is another technique called Probabilistic Amplitude Shaping (PAS) that optimizes the most used bits in the center of the constellation so that energy used is lowest, but we won’t get much into it here.

The QAM-32 constellation shown above is called Cross32, and there are other options like Framed-Cross32 and Holed-Cross32.

Now we have 6 levels to send data at 448G, so what should the Baud rate be? Nyquist frequency?

By now you’ve probably guessed that the odd decimals correspond to PAM6, and you’d be right. Let’s calculate anyway. Baud rate is 448G/2.585 bits/symbol = 173.4 GBaud, and Nyquist frequency is half that, or 86.7 GHz. This means that if the loss of a copper cable is low enough at 86.7 GHz, PAM6 will be able to extend the reach of copper.

TE Connectivity showed a PAM6 modulation on a 1m DAC cable, but we will see that it is not as trivial as it seems, and additional measures will likely be required to make PAM6 work for copper. The figure below shows where the authors considered adding a re-driver in addition to a purely passive cable.

The results are shown below.
