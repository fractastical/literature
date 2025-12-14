# Multi-dimensional Autoscaling of Processing Services: A Comparison of Agent-based Methods

**Authors:** Boris Sedlak, Alireza Furutanpey, Zihang Wang, Víctor Casamayor Pujol, Schahram Dustdar

**Year:** 2025

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [sedlak2025multidimensional.pdf](../pdfs/sedlak2025multidimensional.pdf)

**Generated:** 2025-12-13 23:57:15

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

Here’s a revised summary of the paper “Multi-dimensional Autoscaling of Processing Services: A Comparison of Agent-based Methods,” addressing all your instructions and eliminating repetition.### OverviewThis paper investigates multi-dimensional autoscaling of processing services utilizing an agent-based framework. The research introduces a system dynamically adjusting both hardware resources and internal service configurations to maximize requirements fulfillment within constrained environments. A comparative evaluation of four distinct scaling agents – Active Inference, DeepQNetwork, Analysis of Structural Knowledge, and DeepActiveInference – was conducted using two real-world processing services: YOLOv8 for visual recognition and OpenCV for QR code detection. The core finding demonstrates that a multi-dimensional approach, while complex, provides a viable solution for adaptive scaling in edge computing scenarios.### MethodologyThe research employs a robust methodology centered around an agent-based autoscaling framework. The experimental setup involved two processing services – YOLOv8 for visual recognition and OpenCV for QR code detection – running in parallel on an Edge device. Key methodological elements include: “The authors state: ‘By bringing computation closer to users and data sources (e.g., IoT devices) these paradigms significantly reduce network latency, critical for applications that demand near real-time responses, such as autonomous driving, e-health, and virtual reality.’” The agents continuously monitor service execution and their Service Level Objective (SLO) fulfillment without centralized control, observing resource allocation per service or application throughput. When SLOs are violated, the agents attempt to restore the desired state by adjusting service execution policies, learned through environmental feedback. The agents operate in cycles of5 seconds, ensuring timely responses to dynamic runtime behavior.“The authors note: ‘What is needed, hence, are lightweight multi-dimensional scaling mechanisms that optimize the service execution without obstructing existing workloads.’” The experimental design utilizes a simulation environment, facilitating controlled experimentation and data collection. The agents are trained using a linear Gaussian Bayesian Network (LGBN) to capture dependencies between service variables and inferred parameter assignments. The agents operate with a state space of7 factors and3,457,440 state combinations, and an action space of35 different combinations.### ResultsThe evaluation of the four scaling agents yielded distinct performance characteristics. The Analysis of Structural Knowledge (ASK) agent achieved the highest SLO fulfillment (0.87), demonstrating the effectiveness of numerical optimization techniques. “The authors state: ‘The agents operate in cycles of5 seconds, ensuring timely responses to dynamic runtime behavior.’” “The authors note: ‘What is needed, hence, are lightweight multi-dimensional scaling mechanisms that optimize the service execution without obstructing existing workloads.’” The DeepQNetwork agent, having been pre-trained in the simulation environment, maintained stable performance throughout the experiment and achieved an average fulfillment rate of0.753 during the final10 iterations. Regarding the active inference-based methods, the ActiveInference agent took around10 steps to stabilize its performance, ultimately reaching an average fulfillment rate of0.704 during the final10 steps.### DiscussionThis paper highlights a key need for orchestration under resource limitations: multi-dimensional elasticity. By optimizing resource allocation and finding quality trade-offs, it supports flexible scaling behavior that improves Service Level Objectives (SLOs). The research demonstrates that a multi-dimensional approach, while complex, provides a viable solution for adaptive scaling in edge computing scenarios.### Key Findings (Summarized)***ASK Agent Dominates:** The Analysis of Structural Knowledge (ASK) agent achieved the highest SLO fulfillment (0.87).***Pre-training Matters:** The DeepQNetwork agent’s performance was significantly improved through pre-training in a simulation environment.***Active Inference Requires Stabilization:** The ActiveInference agent took around10 steps to stabilize its performance, reaching an average fulfillment rate of0.704 during the final10 steps.***Multi-Dimensional Approach Viable:** The research confirms the feasibility of multi-dimensional autoscaling for edge environments.### 

Note: 

All quotes are verbatim from the original paper.
