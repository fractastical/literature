# Deep Active Inference for Partially Observable MDPs

**Authors:** Otto van der Himst, Pablo Lanillos

**Year:** 2020

**Source:** arxiv

**Venue:** N/A

**DOI:** 10.1007/978-3-030-64919-7_8

**PDF:** [himst2020deep.pdf](../pdfs/himst2020deep.pdf)

**Generated:** 2025-12-14 14:12:36

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

### Deep Active Inference for Partially Observable MDPs – Summary

### OverviewThis paper investigates a deep active inference (DAIF) model designed to tackle partially observable Markov decision processes (POMDPs). The authors propose a novel approach that leverages variational autoencoders (VAEs) to encode high-dimensional sensory inputs, enabling the agent to learn successful policies directly from visual data. The core of the model is based on the free-energy principle, originally proposed by Friston [9], which posits that agents minimize their free energy by predicting and acting upon their environment. The key innovation lies in the model’s ability to handle the inherent uncertainty of POMDPs, where the true state is not directly observable. The paper demonstrates the model’s effectiveness through experiments on the OpenAI CartPole-v1 benchmark, achieving comparable or superior performance compared to deep Q-learning (DQN).### MethodologyThe DAIF model is built upon a variational free-energy (VFE) formulation, as described by Friston [9] and extended by Parr et al. [16]. The authors state: "The authors state: “The agents objective is to minimize its variational free energy (VFE) at time t, which can be expressed as: −F =D [q(s,a)(cid:107)p(o ,s ,a )] (1)" – This highlights the fundamental principle of minimizing free energy to guide action. The model employs a VAE to encode the visual features, capturing the relevant information for reconstructing the input images. The encoder network, q (s |o ), transforms observations into a latent state representation, and the decoder network, p (o |z ), reconstructs the original input from this representation. The authors note: “The authors state: “We capture this objective with a variational autoencoder (VAE).” – This indicates the use of a VAE to learn the latent state space. The transition model, p(s |s ,a ), is used to model the dynamics of the environment, and the model utilizes a precision parameter, γ, to account for uncertainty. The authors further state: “The authors state: “Transition-network Fully connected network using an Adam optimizer with a learning rate of10−3, of the form: (2N +1)×64×N.” – This describes the architecture of the transition network. The model incorporates a discount factor, β, to account for future rewards. The authors also detail the use of a precision parameter, γ, to account for uncertainty in the transition model.### ResultsThe experimental results on the CartPole-v1 benchmark demonstrate the effectiveness of the DAIF approach. The authors state: “The authors state: “The authors note: “We capture this objective with a variational autoencoder (VAE).” – This indicates the use of a VAE to learn the latent state space.” – The model achieved comparable or better performance than DQN. The moving average reward (MAR) was used to evaluate the performance of the agents. The model’s standard deviations were also significantly lower than those of the DQN agent, indicating greater consistency in its performance. The model’s ability to learn directly from high-dimensional sensory inputs, combined with its reliance on the free-energy principle, offers a promising alternative to traditional reinforcement learning methods. The model’s success in the 

Cart

Pole-v1 benchmark suggests that DAIF could be applied to a wide range of robotic control and navigation tasks
