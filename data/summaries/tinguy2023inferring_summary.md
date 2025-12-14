# Inferring Hierarchical Structure in Multi-Room Maze Environments

**Authors:** Daria de Tinguy, Toon Van de Maele, Tim Verbelen, Bart Dhoedt

**Year:** 2023

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [tinguy2023inferring.pdf](../pdfs/tinguy2023inferring.pdf)

**Generated:** 2025-12-14 11:23:43

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

### OverviewThis paper investigates inferring hierarchical structure in multi-room maze environments using a three-layer hierarchical active inference model. The authors propose a novel approach that combines curiosity-driven exploration with goal-oriented behaviour, enabling agents to efficiently learn and navigate complex environments. The model consists of a cognitive map, an allocentric model, and an egocentric model, each operating at different timescales. The key contribution of this work is the demonstration of a hierarchical approach to maze navigation, achieving superior performance compared to existing methods.### MethodologyThe authors introduce a hierarchical active inference model to address the challenge of inferring structure in pixel-based observations. The model comprises three layers: a cognitive map, an allocentric model, and an egocentric model, functioning at nested timescales. The cognitive map, operating at the coarsest timescale (T), creates a top-down topological map of all locations (l) and their connections, storing them in distinct nodes. Edges between nodes are added as the agent moves from one location to another, effectively capturing the maze’s connectivity. The allocentric model, operating at a finer timescale (t), constructs a belief over places (zT) by integrating sequences of observations (sT) and poses (pT), generating a coherent representation of the environment. This model is trained on random sequences of varying lengths within a single room, while the egocentric model, operating at the finest timescale (τ), manages motions by considering the current position (st), action (at τ), and possible actions (a) to infer the current observation (ot τ). The model’s transition model (p τ (st | st−1, aa1 )) incorporates action in its reasoning, the likelihood model (s τ | st) constructs pixel-based observations, and the posterior model (p τ | st) incorporates past events to future states. The authors trained the model using a dataset of400 environments, with100 environments per room size, and the model’s performance was evaluated using metrics such as the mean number of steps taken to reach the goal.### ResultsThe hierarchical active inference model demonstrated superior performance in navigating multi-room maze environments compared to existing methods. The model achieved an average of67 steps to complete the exploration task and34 steps to reach the goal, while other models required significantly more steps. The model’s ability to accurately predict observations from unvisited positions was particularly noteworthy, with an MSE of less than0.2. The model’s performance was attributed to its hierarchical approach, which allowed it to efficiently integrate information from different timescales and levels of abstraction. The model’s ability to learn the maze’s structure and establish connections between rooms was also a key factor in its success. The authors demonstrated that the model could solve larger environments it had never encountered during training, with an average of8 tiles wide rooms, and the model’s ability to accurately predict observations from unvisited positions was particularly noteworthy, with an MSE of less than0.2.### DiscussionThe authors conclude that their hierarchical active inference model provides a promising approach to inferring structure in multi-room maze environments. The model’s ability to combine curiosity-driven exploration with goal-oriented behaviour enables agents to efficiently learn and navigate complex environments. The model’s hierarchical approach, which allows it to integrate information from different timescales and levels of abstraction, is a key factor in its success. The authors highlight the model’s ability to accurately predict observations from unvisited positions, with an MSE of less than0.2, and its ability to solve larger environments it had never encountered during training. 

The authors suggest that their model could be applied to a wide range of other navigation tasks, and they plan to further investigate its capabilities in more complex environments. 

The authors also note that their model could be used as a building block for more sophisticated AI systems, and they are currently working on integrating it with other techniques, such as reinforcement learning.
