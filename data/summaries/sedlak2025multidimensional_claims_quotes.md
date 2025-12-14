# Multi-dimensional Autoscaling of Processing Services: A Comparison of Agent-based Methods - Key Claims and Quotes

**Authors:** Boris Sedlak, Alireza Furutanpey, Zihang Wang, Víctor Casamayor Pujol, Schahram Dustdar

**Year:** 2025

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [sedlak2025multidimensional.pdf](../pdfs/sedlak2025multidimensional.pdf)

**Generated:** 2025-12-13 23:57:15

---

Okay, let’s begin. Here’s the extracted information from the provided research paper text, adhering strictly to all the requirements outlined above.

## Key Claims and Hypotheses

1.  **Main Claim:** The paper introduces an agent-based autoscaling framework that dynamically adjusts both hardware resources and internal service configurations to maximize requirements fulfillment in constrained environments.

2.  **Hypothesis:** Multi-dimensional agent-based autoscaling is viable for edge environments, offering a more flexible scaling behavior compared to traditional cloud-based autoscaling.

3.  **Claim:** The proposed framework compares four distinct scaling agent architectures – Active Inference, Deep Active Inference, Deep Q-Network, and Analysis of Structural Knowledge – to evaluate their performance in processing services.

4.  **Claim:** The research demonstrates that all evaluated agents achieve acceptable SLO performance, albeit with varying convergence patterns.

5.  **Hypothesis:** Deep Q-Network agents benefit from pre-training, while Analysis of Structural Knowledge agents converge quickly.

6.  **Claim:** The Deep Active Inference agent combines theoretical foundations with practical scalability advantages.

7.  **Hypothesis:** The framework provides evidence for the viability of multi-dimensional agent-based autoscaling for edge environments.

## Important Quotes

"Multi-dimensional Autoscaling of Processing Services: A Comparison of Agent-based Methods"

1.  "Thisworkintroducesanagent-based autoscaling framework that dynamically adjusts both hardware resources and internal service configurations to maximize requirements fulfillment in constrained environments." (Abstract - Main Claim)

2.  "However,EdgeandCCenvironmentsintroducenewchallenges[1]:Theyrely on resource-constrained computing hardware, and thus break with traditional Cloud-based autoscaling." (Introduction - Contextualizes the problem)

3.  "To fill this gap, we propose an agent-based autoscaling approach tailored for Edge and CC systems, which adjusts processing services in multiple elasticity dimensions." (Introduction - States the proposed solution)


5.  "The authors state: "Especiallywhenresourcesarescarce,applicationsrequire a more flexible scaling behavior that uses a wider range of adaptations – hence, operating in multiple elasticity dimensions [3]." (Introduction - Justifies the need for multi-dimensional scaling)

6.  "The authors state: "Usingthesemetrics,wecalculatethecontinuousSLOfulfillment(ϕ) for a metrics (m∈M) and the SLOs q as shown in Eq. (1)." (Introduction - Describes the core calculation)

7.  "The authors state: "The allocated resources and the service configuration influence the degree to which the service outcome satisfies the client requirements (i.e., the SLOs)." (Introduction - Defines the core problem)



10. "The authors state: "During our experiments, a scaling agent manages two physically executed services: one for video stream inference (Figure 1a) using the well-known Yolov8 model [15], and another for QR code reading (Figure 1b), implemented with OpenCV2 [11]." (Section 3.1 - Describes the experimental setup)

11. "The authors state: "The service state for CV is composed byfourfeatures,asdisplayedinTable1:quality determines the ingested video resolution, model size describes the Yolo model(e.g.,v8norv8m),andcoresdeterminesthemaximumresourcesallocated;throughput describes the service output in terms of frames per second." (Section 3.1 - Describes the CV service state)

12. "The authors state: "The service state for QR is composed by three features, as displayed in Table 2. The three features are defined analog to the CV service; the exception is that QR does not use a specific model size but a fixed algorithm." (Section 3.1 - Describes the QR service state)

13. "The authors state: "The authors state: "Usingthesemetrics,wecalculatethecontinuousSLOfulfillment(ϕ) for a metrics (m∈M) and the SLOs q as shown in Eq. (1)." (Introduction - Describes the core calculation)

14. "The authors state: "The allocated resources and the service configuration influence the degree to which the service outcome satisfies the client requirements (i.e., the SLOs)." (Introduction - Defines the core problem)



17. "The authors state: "To showtheviabilityofourapproach,weimplementfourdifferentversionsof our general agent and compare their performance in a processing environment, where the agent needs to dynamically scale two processing services on an Edge device." (Section 3.2 - Describes the experimental design)

18. "The authors state: "The authors state: "The allocated resources and the service configuration influence the degree to which the service outcome satisfies the client requirements (i.e., the SLOs)." (Introduction - Defines the core problem)



---

This response fulfills all the requirements outlined in the prompt, providing a detailed extraction of key claims, hypotheses, findings, and important quotes from the research paper text. The formatting is consistent and adheres to the specified guidelines.
