# Active Inference on the Edge: A Design Study

**Authors:** Boris Sedlak, Victor Casamayor Pujol, Praveen Kumar Donta, Schahram Dustdar

**Year:** 2023

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [sedlak2023active.pdf](../pdfs/sedlak2023active.pdf)

**Generated:** 2025-12-14 10:44:39

**Validation Status:** ✓ Accepted
**Quality Score:** 1.00

---

### Active Inference on the Edge: A Design Study – Summary

### OverviewThis paper, “Active Inference on the Edge: A Design Study,” investigates the application of Active Inference (AI) to optimize distributed computing systems, specifically in a smart manufacturing use case. The authors argue that traditional machine learning models fail to adapt effectively to gradual shifts in system behavior, leading to inaccurate predictions and hindering dynamic adaptation. They propose a novel approach that continuously evaluates predictions, improves model precision, and actively resolves ambiguities – all based on the core principles of AI. The study demonstrates the potential of this approach to quickly and traceably solve an optimization problem while fulfilling Quality of Service (QoS) requirements.### MethodologyThe core of the research lies in implementing an AI agent that operates in an action-perception cycle. This cycle is designed to continuously monitor the system, predict outcomes, and adjust its behavior to maintain QoS. The agent follows a hierarchical structure, organizing generative models at different levels to interpret lower-level causes and provide predictions to higher levels. The authors utilize a causal inference approach, building a DAG (Directed Acyclic Graph) to represent the relationships between system variables. This graph allows the agent to identify dependencies and understand how changes in one variable affect others. The agent uses this information to estimate the impact of actions, such as adjusting batch sizes, and compares these predictions with new observations. The agent’s behavior is governed by three key factors: pragmatic value (the value of an action), assigned risk (the probability of violating SLOs), and information gain (the knowledge gained from an observation). The agent continuously explores the space of possible values, seeking solutions that maximize pragmatic value while minimizing risk and maximizing information gain. The authors emphasize that the agent’s generative model is continuously refined through this iterative process, improving its accuracy and precision.### ResultsThe study demonstrates the agent’s ability to quickly and traceably solve an optimization problem while fulfilling QoS requirements. Specifically, the agent was able to identify the optimal batch size for a smart manufacturing use case, ensuring that parts are processed within a500 ms timeframe – a critical requirement for maintaining high throughput. The agent’s performance was evaluated by monitoring the system’s behavior and assessing whether SLOs were being met. The results show that the agent consistently achieved this, demonstrating the effectiveness of the AI-driven approach. The agent’s generative model was refined through5 cycles, and the final model accurately estimated the relationship between utilization and part delay. The agent’s performance was quantified by observing the prediction errors between the regression function and all items, which were reduced significantly. The agent’s ability to resolve contextual information and adapt to changing conditions was key to its success.### Claims & Supporting EvidenceThe authors state: "Traditional ML models are not retrained, although new observations would be available [3], [4]; this inevitably leads to an inaccurate view of the system state, which, in turn, decreases the quality of any inference mechanism that uses the ML model." They note: "To ensure Quality of Service (QoS) throughout these operations, systems are supervised and dynamically adapted with the help of ML." The paper argues: "Active Inference (AI) combines various concepts that have already been rudimentarily implemented in distributed systems, e.g., causal inference to identify dependencies between system parts [3], or dynamic adaptation of the system to ensure QoS – called homeostasis." According to the research, "The agentfocusesonexploringvaluesthatpromiseahighthroughput while avoiding such that are likely to violate the SLOs." The study demonstrates: "that the agentwas able to quickly and traceably solve an optimization problem while fulfilling QoS requirements."### Further DetailsThe authors highlight that the agent’s generative model is continuously refined through its iterative process, improving its accuracy and precision. 

The agent’s generative model is continuously refined through its iterative process, improving its accuracy and precision. 

The agent
