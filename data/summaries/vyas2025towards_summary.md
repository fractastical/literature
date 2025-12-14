# Towards smart and adaptive agents for active sensing on edge devices

**Authors:** Devendra Vyas, Nikola Pižurica, Nikola Milović, Igor Jovančević, Miguel de Prado, Tim Verbelen

**Year:** 2025

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [vyas2025towards.pdf](../pdfs/vyas2025towards.pdf)

**Generated:** 2025-12-14 00:08:14

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

### OverviewThis paper investigates the development of smart and adaptive agents for active sensing on edge devices. The authors present a novel system combining deep learning perception with active inference planning, enabling real-time, memory-efficient operation on resource-constrained devices. The core innovation lies in grounding the agent’s decision-making within the Free Energy Principle, allowing it to actively reduce uncertainty and adapt to dynamic environments. The system is demonstrated through a saccade agent deployed on an Nvidia Jetson platform, showcasing its potential for surveillance and robotic applications.### MethodologyThe authors’ approach centers on a two-module system: a deep learning-based perception module and an active inference planning module. The perception module utilizes YOLOv10, a state-of-the-art object detection model, to identify objects in the environment. The active inference module, based on the Free Energy Principle, plans the agent’s subsequent actions, minimizing free energy and dynamically adjusting the camera’s field of view. The agent operates in a discrete state space, with each state representing a fixation point, and uses a Bayesian approach to update its beliefs about the hidden states. The system is designed to handle uncertainty and adapt to changing environments by actively reducing ambiguity or exploring the environment for new information. The authors employ a workflow to export the YOLOv10n model to ONNX and compile it with different inference engines, optimizing performance and memory usage.### ResultsThe experimental results demonstrate the feasibility of the proposed system. The authors showcase the system’s performance through a saccade agent deployed on an Nvidia Jetson platform. The system achieves a throughput of947 Hz with YOLOv10, enabling rapid feature extraction. The authors demonstrate the system’s ability to adapt to dynamic environments, showcasing its potential for surveillance and robotic applications. The system operates in a discrete state space, with each state representing a fixation point, and uses a Bayesian approach to update its beliefs about the hidden states.### DiscussionThe authors’ findings highlight the effectiveness of combining deep learning for perception with active inference for planning in edge-based intelligent agents. The system’s ability to adapt to dynamic environments is a key advantage, allowing it to maintain situational awareness and make informed decisions in complex scenarios. The use of the Free Energy Principle provides a robust framework for grounding the agent’s decision-making within the environment’s underlying dynamics and inherent uncertainty. 

The authors’ approach offers a promising solution for developing smart and adaptive agents for active sensing on edge devices, paving the way for new applications in surveillance, robotics, and other domains. 

The system’s memory footprint of as little as300 MB further enhances its suitability for deployment on resource-constrained devices.
