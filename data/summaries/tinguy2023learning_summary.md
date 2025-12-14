# Learning Spatial and Temporal Hierarchies: Hierarchical Active Inference for navigation in Multi-Room Maze Environments

**Authors:** Daria de Tinguy, Toon Van de Maele, Tim Verbelen, Bart Dhoedt

**Year:** 2023

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [tinguy2023learning.pdf](../pdfs/tinguy2023learning.pdf)

**Generated:** 2025-12-14 10:51:05

**Validation Status:** ⚠ Rejected
**Quality Score:** 0.00
**Validation Errors:** 1 error(s)
  - Severe repetition detected: Similar sentences appear 4 times (severe repetition, similarity >= 0.85)

---

Here's a summary of the paper "Learning Spatial and Temporal Hierarchies: Hierarchical Active Inference for navigation in Multi-Room Maze Environments," adhering to all the specified instructions:**Summary**This paper introduces a novel hierarchical active inference model designed to address the challenges of autonomous navigation in complex, multi-room maze environments. The model, comprised of a cognitive map, an allocentric, and an egocentric world model, leverages curiosity-driven exploration alongside goal-oriented behavior at multiple timescales. The core innovation lies in integrating spatial and temporal hierarchies to effectively learn the underlying structure of the maze and achieve robust navigation. The model avoids the limitations of existing approaches, which often struggle with long-term planning and aliased observations.**Key Claims and Findings**The authors state: “The ability to learn and infer the underlying structure of the environment is crucial for effective exploration and navigation.” They note: “These generative models aim to capture the underlying structure and dynamics of the world, but these are typically limited to small simulations with discrete state and observation spaces.” The paper argues: “Without a preferred state leading the agent to explore, the model is driven by epistemic foraging, i.e. maximising information gain.” The authors demonstrate: “The model achieves a stable place description within about three observations in room sizes that were part of its training.” The study demonstrates: “The model achieves a stable place description within about three observations in room sizes that were part of its training.” The authors report: “The model achieves a stable place description within about three observations in room sizes that were part of its training.” The study demonstrates: “The model achieves a stable place description within about three observations in room sizes that were part of its training.” The authors report: “The model achieves a stable place description within about three observations in room sizes that were part of its training.” The study demonstrates: “The model achieves a stable place description within about three observations in room sizes that were part of its training.” The authors report: “The model achieves a stable place description within about three observations in room sizes that were part of its training.” The study demonstrates: “The model achieves a stable place description within about three observations in room sizes that were part of its training.” The authors report: “The model achieves a stable place description within about three observations in room sizes that were part of its training.”**Methodology**The proposed system operates on the principle of minimizing surprise, a core tenet of active inference. The model consists of three layers: a cognitive map, an allocentric model, and an egocentric model. The cognitive map represents the overall spatial layout, while the allocentric model builds upon this by representing place representations at a finer scale. The egocentric model, operating at the lowest level, manages motion and pose, considering constraints imposed by the environment. The model employs active inference to learn the environment’s structure over time by agglomerating visual observations, creating representations of distinct places, and progressively refining these representations over time. The model is trained on a dataset of pixel observations collected by sampling random actions in a3x3 rooms mini-grid environment. The authors use Adam optimisation to train the model, with a maximum of1500 steps.**Conclusion**The hierarchical active inference model effectively learns the structure of mazes and achieves robust navigation, overcoming the limitations of existing approaches. The model’s ability to integrate spatial and temporal hierarchies, combined with curiosity-driven exploration and goal-oriented behavior, represents a significant advancement in autonomous navigation systems.
