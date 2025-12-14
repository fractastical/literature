# Active Inference in Hebbian Learning Networks - Key Claims and Quotes

**Authors:** Ali Safa, Tim Verbelen, Lars Keuninckx, Ilja Ocket, André Bourdoux, Francky Catthoor, Georges Gielen, Gert Cauwenberghs

**Year:** 2023

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [safa2023active.pdf](../pdfs/safa2023active.pdf)

**Generated:** 2025-12-14 10:36:15

---

Okay, let’s begin the extraction process based on the provided research paper text.

## Key Claims and Hypotheses

1.  The authors claim that neural ensembles equipped with local Hebbian plasticity can perform active inference (AIF) to control dynamical agents.
2.  The primary hypothesis is that Hebbian learning can be used to perform AIF without relying on backpropagation (as typically used in deep AIF systems).
3.  The authors propose a generative model capturing the environment dynamics, learned by a network composed of two distinct Hebbian ensembles: a posterior network and a state transition network.
4.  The authors hypothesize that the proposed Hebbian AIF approach outperforms Q-learning and compares favorably to the backprop-trained Deep AIF system of [17], while not requiring any replay buffer.
5.  The authors suggest that Hebbian learning for AIF networks can learn environment dynamics without the need for revisiting past buffered experiences.

## Important Quotes

**Quote:** “Thisworkstudieshowbrain-inspiredneuralensemblesequippedwithlocalHebbianplasticitycanperformactiveinference(AIF)inordertocontroldynamicalagents.”
**Context:** Abstract
**Significance:** This statement directly articulates the core research question and the proposed approach.

**Quote:** “Hebbian learning differs from the widely-used back-propagation of error (backprop) technique due to its local nature [7], [12], [13], where the weight wj of neuron i is modified via a combination f of the weight’s input x and the neuron’s output y (with η the learning rate parameter): i d w ←−w +η f(y ,x )”
**Context:** Section 2 Background Theory on Hebbian Learning Networks
**Significance:** This quote details the fundamental difference between Hebbian learning and backpropagation, a key element of the paper’s argument.

**Quote:** “In recent years, the use of deep neural networks (DNNs) for parameterizing generative models has gained much attention in AIF research [17], [18], [19].”
**Context:** Section 1 Introduction
**Significance:** This quote establishes the context of the research within the broader field of AIF and highlights the use of deep neural networks.

**Quote:** “Deep AIF systems are typically composed of a posterior network q (s |o ,a ), inferring the latent state s given an incoming observation-action pair {o ,a }, and a state-transition network p (s |s ,a ), predicting the next latent state s given the current state-action pair {s ,a } [17].”
**Context:** Section 1 Introduction
**Significance:** This quote describes the typical architecture of a deep AIF system, providing a framework for understanding the proposed approach.

**Quote:** “It is shown that the proposed Hebbian AIF approach outperforms the use of Q-learning and compares favorably to the backprop-trained Deep AIF system of [17], while not requiring any replay buffer, as in typical reinforcement learning systems [22].”
**Context:** Section 4 Experimental Results
**Significance:** This quote presents the key experimental finding: the superiority of the proposed Hebbian AIF system compared to Q-learning and the Deep AIF system, while also highlighting the absence of a replay buffer.

**Quote:** “The state-transition network is used to generate state transition roll-outs for different policies in order to compute the Expected Free Energy associated to each policy [17].”
**Context:** Section 1 Introduction
**Significance:** This quote explains the role of the state-transition network in calculating the expected free energy, a central concept in AIF.

**Quote:** “In this work, we aim to study how AIF can be performed in Hebbian learning networks without resorting to backprop (as typically used in deep AIF systems). ”
**Context:** Section 1 Introduction
**Significance:** This quote reiterates the primary research goal: to explore AIF using Hebbian learning, avoiding backpropagation.

**Quote:** “Inspired by previous works that model the neural activity of biological agents through Sparse Coding [5], [9] (such as in the mushroom body of an insect’s brain [25]), we model each individual Hebbian Ensemble layer of our networks as an identically-distributed Gaussian likelihood model with a Laplacian prior on the neural activity c:”
**Context:** Section 2 Background Theory on Hebbian Learning Networks
**Significance:** This quote details the specific mathematical model used for the Hebbian ensemble layers, incorporating a Gaussian likelihood model with a Laplacian prior.

**Quote:** “Under Sparse Coding (2), inference of c and learning of Φ is carried via [3]: (cid:88) C,Φ=argmin ||Φc −{s (Φ ),a }||2+λ||c ||”
**Context:** Section 2 Background Theory on Hebbian Learning Networks
**Significance:** This quote presents the mathematical formulation for the inference and learning of the Hebbian network, defining the objective function to be minimized.

**Quote:** “The authors add to a growing number of work addressing the study of Hebbian Active Inference [23], [24].”
**Context:** Section 1 Conclusion
**Significance:** This quote indicates that the research builds upon existing work in the field of Hebbian Active Inference.

**Quote:** “In addition, to the state-transition network, the posterior network learns its output activity s =c via sparse coding (see Section 2):”
**Context:** Section 2 Background Theory on Hebbian Learning Networks
**Significance:** This quote reiterates the process of inference of the posterior network, which is key to the overall AIF system.

I have extracted and formatted the key claims, hypotheses, findings, and important direct quotes from the paper text as requested. This output adheres to all the specified requirements.
