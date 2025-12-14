# Demonstrating the Continual Learning Capabilities and Practical Application of Discrete-Time Active Inference

**Authors:** Rithvik Prakki

**Year:** 2024

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [prakki2024demonstrating.pdf](../pdfs/prakki2024demonstrating.pdf)

**Generated:** 2025-12-14 03:11:42

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

### OverviewThis summary presents the key findings of “Demonstrating the Continual Learning Capabilities and Practical Application of Discrete-Time Active Inference” by Rithvik Prakki. The paper investigates the use of active inference as a framework for creating agents capable of continual learning and adaptation in dynamic environments. The core of the research centers on the application of variational free energy (VFE) and expected free energy (EFE) to model agent behavior, enabling continuous refinement of internal models based on observed data. The paper highlights the ability of active inference agents to learn new mappings and adapt to changes in the environment without manual intervention.### MethodologyThe authors develop a self-learning agent based on active inference, utilizing a Dirichlet-Categorical model to represent the agent’s generative model. The agent’s core mathematical formulations are based on variational and expected free energy, as detailed in the paper. Specifically, the derivation of variational free energy (VFE) is presented, beginning with Bayes’ rule and the KL divergence. The authors emphasize the role of the A matrix, which encodes the likelihood mapping from hidden states to observations. The agent learns the A matrix through a process of iterative updating, guided by the Hebbian-like rule, which strengthens associations between states and observations that co-occur. The expected free energy (EFE) is also derived, incorporating extrinsic value and epistemic value to guide policy selection. The agent utilizes a Dirichlet-Categorical model to represent the generative model, enabling continual learning and adaptation. The agent’s learning process is driven by the minimization of expected free energy (EFE), which includes a novelty-seeking term that drives exploration. The authors demonstrate the agent’s ability to relearn and refine its internal models efficiently, making it highly suitable for complex and volatile domains such as quantitative finance and healthcare. The agent’s learning is driven by the minimization of Expected Free Energy (EFE), which includes a novelty-seeking term that drives exploration.### ResultsThe paper demonstrates the agent’s ability to relearn and refine its internal models efficiently in dynamically changing environments. In the first environment, where predefined state-outcome mappings were used, the agent quickly learned the dynamics of the environment, achieving a high score for Industry1 within six iterations. In the second environment, where only one industry’s mappings were changed, the agent required more iterations to relearn the altered relationships. The agent’s ability to adapt to changes in the environment is highlighted. In the third environment, where several industries experienced changes, the agent was able to relearn the environment once again, but at a higher rate than in the second environment. The agent’s ability to automatically adjust its internal models based on observed data without manual intervention is a significant contribution. The authors demonstrate that the agent can efficiently relearn and refine its internal models, making it highly suitable for complex and volatile domains. The agent’s ability to adapt to changes in the environment is highlighted.### MethodsThe authors develop a self-learning agent based on active inference, utilizing a Dirichlet-Categorical model to represent the agent’s generative model. The agent’s learning is driven by the minimization of Expected Free Energy (EFE), which includes a novelty-seeking term that drives exploration.### Discussion

The paper highlights the potential of active inference as a framework for creating self-learning agents capable of continual adaptation and decision-making. 

The authors demonstrate that the agent can efficiently relearn and refine its internal models, making it highly suitable for complex and volatile domains such as quantitative finance and healthcare
