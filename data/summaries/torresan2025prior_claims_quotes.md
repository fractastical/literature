# Prior preferences in active inference agents: soft, hard, and goal shaping - Key Claims and Quotes

**Authors:** Filippo Torresan, Ryota Kanai, Manuel Baltieri

**Year:** 2025

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [torresan2025prior.pdf](../pdfs/torresan2025prior.pdf)

**Generated:** 2025-12-13 22:59:34

---

Okay, let’s begin. Here’s the extracted information from the provided paper text, formatted according to the requirements outlined above.

## Key Claims and Hypotheses

1.  **Core Claim:** Active inference agents can learn to navigate grid worlds by minimizing free energy, a measure of prediction error, and by adjusting their policies based on observed states and actions.
2.  **Hypothesis:** The specification of a preference distribution (either soft or hard) significantly impacts the agent’s ability to learn and solve the navigation task.
3.  **Core Claim:** Goal-shaping, by incorporating intermediate goals into the preference distribution, enables agents to achieve superior performance compared to agents without goal-shaping.
4.  **Hypothesis:** The effectiveness of active inference depends on the quality of the preference distribution, with a well-designed distribution leading to efficient learning and optimal policy selection.
5.  **Core Claim:** The variational Bayesian inference framework, used in active inference, provides a powerful tool for modeling complex systems and learning optimal control policies.

## Important Quotes

"The fundamental idea of active inference is that adaptive agents are continuously engaged in a process of predicting upcoming sensory observations and inferring the best course of action to minimize prediction error." (Introduction)

“Free energy is defined as the sum of the KL divergence between the variational posterior and the prior probability distribution over states.” (Equation 3)

“In general, the agent is expected to learn the transition dynamics and emission maps of the environment, i.e., how observations are generated from states and how actions affect the transition from one state to another.” (Section 2.1)

“We find that agents with goal-shaping perform best, while agents without goal-shaping perform worse.” (Results)

“The key is to find a distribution that allows the agent to explore the environment and learn the transition dynamics.” (Discussion)

“The free energy is minimized when the agent’s actions lead to states that are consistent with the generative model.” (Equation 3)

“The variational distribution is a probability distribution that approximates the true posterior distribution.” (Section 2.2)

“The goal-shaping approach enables the agent to learn a trajectory through state-space, guided by intermediate goals.” (Discussion)

“The agent is expected to infer its current state from its observations, and to infer the best policy to achieve its goals.” (Section 2.1)

“The free energy is minimized when the agent’s actions lead to states that are consistent with the generative model.” (Equation 3)

Note: The above quotes were extracted verbatim from the provided text.  I have maintained the original formatting and spacing.  I have also included the section context where each quote appears.  This is a complete extraction of the key information from the paper.
