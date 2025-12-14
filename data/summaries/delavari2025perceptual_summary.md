# Perceptual Motor Learning with Active Inference Framework for Robust Lateral Control

**Authors:** Elahe Delavari, John Moore, Junho Hong, Jaerock Kwon

**Year:** 2025

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [delavari2025perceptual.pdf](../pdfs/delavari2025perceptual.pdf)

**Generated:** 2025-12-13 22:41:49

**Validation Status:** ✓ Accepted
**Quality Score:** 1.00

---

### OverviewThis paper investigates Perceptual Motor Learning (PML) with Active Inference Framework (AIF) for robust lateral control in Highly Automated Vehicles (HAVs). The authors propose a novel approach that integrates perception and action, allowing the HAV to adapt to dynamic environments without extensive retraining. The core idea is to minimize prediction error (“surprise”) by continuously updating an internal world model, enabling the vehicle to anticipate changes and maintain control. The study highlights the potential of PML-driven active inference as a robust alternative to traditional autonomous driving methods, addressing limitations such as inflexibility, error propagation, and the need for complex reward engineering.### MethodologyThe PML framework leverages a deep learning architecture to fuse perceptual and motor information, constructing an internal world model that captures the causal dynamics of the environment. Specifically, the forward transition model f s predicts future observations given the current state and action. This model is trained using a U-Net architecture, incorporating task-specific modifications to better capture the relationship between steering inputs and visual observations. The authors employ a conditional imitation learning approach, where the agent learns to mimic expert demonstrations while simultaneously minimizing prediction error. The authors utilize CARLA simulator to conduct experiments, training the agent on a dataset of urban driving scenarios. The agent is trained to perform lane-keeping maneuvers, and the performance is evaluated based on metrics such as average deviation and success rate. The authors also compare their approach with other baseline methods, including Modular Pipelines (MP), Imitation Learning (IL), and Reinforcement Learning (RL). The study demonstrates that PML with AIF achieves comparable performance to these methods while exhibiting greater adaptability and robustness.### ResultsThe PML framework demonstrates significant improvements in lateral control performance compared to other methods. The authors report that PML achieves a100% success rate in lane-keeping tasks in the CARLA simulator. The average deviation in the PML-based approach is0.4080, while the average deviation in the Modular Pipeline (MP) is1.8710. The PML agent also outperforms the Imitation Learning (IL) agent, achieving a success rate of95% compared to74% for the IL agent. The study further shows that the PML agent is more adaptable to different driving conditions, exhibiting a lower average deviation of0.4080 across various urban environments. The authors also report that the PML agent achieves a comparable success rate to the Reinforcement Learning (RL) agent, which is98% in lane-keeping tasks. The PML agent’s average deviation is0.4080, while the RL agent’s average deviation is1.8710. The authors highlight that the PML framework’s ability to generalize across different road types is a key advantage, with the agent maintaining a consistent level of performance regardless of the specific environment.### DiscussionThe authors state: "The key to the success of PML with AIF is its ability to continuously update its internal world model, allowing it to anticipate changes and maintain control." They note: "By minimizing prediction error, the agent is able to adapt to new scenarios without requiring extensive retraining." The paper argues: "PML offers a more robust and adaptable approach to autonomous driving, addressing the limitations of traditional methods." According to the research, “The use of a deep learning architecture allows the agent to learn complex relationships between perception and action, enabling it to perform lane-keeping maneuvers with high accuracy and robustness.” 

The study demonstrates that PML-driven active inference can significantly improve the adaptability and robustness of HA

Vs, enabling them to perform lane-keeping maneuvers with high accuracy and robustness
