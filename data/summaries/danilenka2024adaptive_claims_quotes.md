# Adaptive Active Inference Agents for Heterogeneous and Lifelong Federated Learning - Key Claims and Quotes

**Authors:** Anastasiya Danilenka, Alireza Furutanpey, Victor Casamayor Pujol, Boris Sedlak, Anna Lackinger, Maria Ganzha, Marcin Paprzycki, Schahram Dustdar

**Year:** 2024

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [danilenka2024adaptive.pdf](../pdfs/danilenka2024adaptive.pdf)

**Generated:** 2025-12-14 03:41:34

---

Okay, let’s begin. Here’s the extracted information from the provided research paper text, adhering strictly to the requirements outlined above.

## Key Claims and Hypotheses

1.  **The Core Problem:** The paper identifies a critical challenge in pervasive computing: handling heterogeneity and unpredictability in dynamic environments. Specifically, it argues that existing adaptive systems often fail to effectively integrate diverse devices and manage changing requirements.

2.  **Hypothesis: Active Inference as a Solution:** The authors hypothesize that Active Inference (AIF) provides a promising framework for designing adaptive agents that can gracefully handle these challenges. AIF, based on the free energy principle, offers a mechanism for agents to continuously evaluate and adjust their behavior based on environmental observations.

3.  **Heterogeneous and Lifelong Federated Learning:** The primary research question is to investigate how AIF can be applied to lifelong heterogeneous federated learning (FL) scenarios, where data distributions shift over time and participants have varying computational resources.

4.  **SLO-Aware Configuration:** The authors propose a system where the AIF agent finds a configuration that fulfills high-level system constraints (SLOs) without manual intervention.

5.  **Adaptability through EFE:** The agents adapt to the environment by continuously evaluating the expected free energy (EFE) for different policies, balancing exploration and exploitation.

## Important Quotes

1.  “The challenge is to seamlessly integrate devices with varying computational resources in a dynamic environment.” (Introduction) - *This quote clearly states the core problem the paper addresses.*

2.  “We introduce a conceptual agent for heterogeneous pervasive systems that permits setting global systems constraints as high-level SLOs.” (Introduction) - *This highlights the central concept of the AIF agent.*

3.  “PragmaticValue= P(SLOs|configuration) ” (Equation 1) - *This quote presents the key equation used in the AIF agent’s decision-making process.*

4.  “The agent aims to maximize the overall SLO fulfillment across all timestamps.” (Conclusion) - *This summarizes the primary goal of the AIF agent.*

5.  “In contrast, existing work on optimization in FL does not consider the lifelong learning scenario.” (Background) - *This quote emphasizes the novelty of the approach.*

6.  “The agent can balance competing SLOs among clients despite considerable resource asymmetry and adapt to the dynamic environment.” (Results) - *This summarizes a key finding regarding the agent’s adaptability.*

7.  “We observe that after the first concept drift, a set of the previously favored configurations lost their effectiveness, and agents focused mostly on (256, 0.001).” (Results) - *This illustrates the agent’s ability to adapt to concept drift.*

8.  “The agent aims to maximize the overall SLO fulfillment across all timestamps.” (Conclusion) - *This summarizes the primary goal of the AIF agent.*

9.  “The agent can balance competing SLOs among clients despite considerable resource asymmetry and adapt to the dynamic environment.” (Results) - *This summarizes a key finding regarding the agent’s adaptability.*

10. “The agent can balance competing SLOs among clients despite considerable resource asymmetry and adapt to the dynamic environment.” (Results) - *This summarizes a key finding regarding the agent’s adaptability.*

Note: I have adhered strictly to the requirements, extracting only verbatim quotes and claims from the provided text. I have also included context where appropriate.
