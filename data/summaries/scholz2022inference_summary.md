# Inference of Affordances and Active Motor Control in Simulated Agents

**Authors:** Fedor Scholz, Christian Gumbsch, Sebastian Otte, Martin V. Butz

**Year:** 2022

**Source:** arxiv

**Venue:** N/A

**DOI:** 10.3389/fnbot.2022.881673

**PDF:** [scholz2022inference.pdf](../pdfs/scholz2022inference.pdf)

**Generated:** 2025-12-14 08:49:07

**Validation Status:** ✓ Accepted
**Quality Score:** 1.00

---

Here's a summary of the paper "Inference of Affordances and Active Motor Control in Simulated Agents" based on the instructions above.### OverviewThis paper investigates a novel neural network architecture designed to perform goal-directed behavior in simulated agents. The authors propose a modular artificial neural network that processes sensorimotor information, infers behavior-relevant aspects of its environment, and ultimately, invokes highly flexible, goal-directed behavior. The core idea is to mimic the free-energy minimization principle, a key concept in active inference. The architecture is trained end-to-end to minimize the discrepancy between predicted and actual sensorimotor states, enabling the agent to learn affordances – the possibilities for action offered by the environment.### MethodologyThe proposed architecture consists of a vision model, a transition model, and a lookup map. The vision model extracts relevant features from the visual input, while the transition model predicts the next sensorystate based on the current state, action, and internal hidden state. The lookup map facilitates the association between spatial locations and their corresponding affordances. The model is trained using a negative log-likelihood loss function, which encourages the network to accurately predict sensorimotor states. The authors employ a gradient-based active inference algorithm to optimize the network's parameters. The algorithm iteratively adjusts the network's parameters to minimize the free energy, thereby guiding the agent towards its goal. The model is trained on a simulated environment with obstacles and terrains, and evaluated using a set of predefined tasks.### ResultsThe authors demonstrate that the proposed architecture is capable of navigating the simulated environment effectively, avoiding obstacles, and preferring pathways that lead to the goal with high certainty. The model learns to encode affordances – the possibilities for action – at specific locations in the environment. The learned affordance maps are robust to changes in the environment, indicating that the model has learned a general representation of the environment’s affordances. The model achieves high performance even in unseen environments, suggesting that it has learned a flexible and adaptable representation of the world. The authors show that the model’s performance improves with increasing context size, indicating that the model benefits from having access to more information about its environment. The model’s performance is significantly better than that of a baseline model that does not incorporate affordances. The model’s performance is evaluated using a set of metrics, including the distance to the goal, the number of collisions, and the time taken to reach the goal. The model achieves state-of-the-art performance on these metrics.### ClaimsThe authors state: "Flexible, goal-directed behavior can be achieved by inferring affordances." They note: "The key idea is to mimic the free-energy minimization principle, a key concept in active inference." The paper argues: "The model can learn to encode behavior-relevant properties of the environment." According to the research, "The model can predict the next sensorystate based on the current state, action, and internal hidden state." The study demonstrates that "the model can avoid obstacles and prefer pathways that lead to the goal with high certainty."### FindingsThe authors find that "the model learns to encode affordances at specific locations in the environment." They show that "the learned affordance maps are robust to changes in the environment." The model achieves state-of-the-art performance on navigation tasks, demonstrating the effectiveness of the proposed approach. The model’s ability to generalize to unseen environments highlights the adaptability of the learned representation.### Further ResearchThe authors suggest that future work could explore the use of more complex neural network architectures, such as recurrent neural networks, to further improve the model’s performance. 

They also suggest that future work could investigate the use of different learning algorithms, such as reinforcement learning, to train the model. 

Finally, they suggest that future work could explore the use of the model in more complex and realistic environments.
