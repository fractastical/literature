# Hybrid Recurrent Models Support Emergent Descriptions for Hierarchical Planning and Control

**Authors:** Poppy Collis, Ryan Singh, Paul F Kinghorn, Christopher L Buckley

**Year:** 2024

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [collis2024hybrid.pdf](../pdfs/collis2024hybrid.pdf)

**Generated:** 2025-12-14 04:19:12

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

### OverviewThis paper investigates the use of hybrid recurrent models, specifically recurrent switching linear dynamical systems (rSLDS), to support emergent descriptions for hierarchical planning and control. The authors propose a novel hierarchical agent (HHA) that leverages the representations learned by rSLDS to achieve effective system identification and control, particularly in challenging tasks such as the Continuous Mountain Car environment. The core contribution lies in demonstrating how rSLDS can generate useful abstractions of the state-space, facilitating rapid planning and control through integrated exploration and information-theoretic rewards.### MethodologyThe HHA algorithm is built upon the foundation of rSLDS, which are characterized by their ability to discretize continuous dynamics into a set of linear dynamical systems. The authors employ a Bayesian Markov Decision Process (MDP) framework, incorporating the learned representations of the rSLDS as a model for the environment. The HHA utilizes a receding-horizon approach, generating a discrete action at each time step based on the state and the learned rSLDS. The key components of the HHA include: (1) the rSLDS, which learns the underlying dynamics of the system; (2) a discrete planner, which generates a sequence of abstract sub-goals; (3) a linear-quadratic regulator (LQR) controller, which implements closed-loop control; and (4) an information-gain incentive, which drives exploration. The rSLDS is trained using Bayesian updates, allowing the model to adapt to the observed trajectories. The algorithm incorporates a softmax regression model to map continuous states to discrete modes, and a Gaussian distribution to model the transition dynamics between modes. The authors use a computationally efficient method to estimate the transition probabilities, and a receding-horizon approach to implement the LQR controller. The system is trained using Monte Carlo sampling, and the results are evaluated using a standard performance metric.### ResultsThe HHA demonstrates significant improvements in performance compared to other reinforcement learning baselines, including a Soft Actor-Critic with2Q-functions and an Actor-Critic model. Specifically, the HHA achieves a higher reward and capitalizes on its experiences significantly quicker than the other models. The authors report that the HHA competes with the state-space coverage achieved by model-based algorithms with exploratory enhancements in the discrete Mountain Car task. The HHA successfully identifies the key regions of the state-space and navigates to the goal state efficiently. The authors provide specific numerical results, including the average reward (+/- std) over6 runs for the Continuous Mountain Car task, and the parameters of the rSLDS. The HHA’s performance is attributed to its ability to learn a rich representation of the state-space and to exploit the information-theoretic exploration bonus. The authors state: "The authors state: "The HHA achieves a higher reward and capitalizes on its experiences significantly quicker than the other models."### DiscussionThe research highlights the potential of hybrid recurrent models to support emergent descriptions for hierarchical planning and control. The authors argue that rSLDS can generate useful abstractions of the state-space, facilitating rapid system identification and control. The use of the information-theoretic exploration bonus drives the agent to explore the state-space effectively. The authors note: "The authors state: "

The HHA’s performance is attributed to its ability to learn a rich representation of the state-space and to exploit the information-theoretic exploration bonus." 

The study demonstrates that the HHA can outperform other reinforcement learning algorithms, even when incorporating model-based exploration techniques
