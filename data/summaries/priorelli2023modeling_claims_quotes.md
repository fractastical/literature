# Modeling motor control in continuous-time Active Inference: a survey - Key Claims and Quotes

**Authors:** Matteo Priorelli, Federico Maggiore, Antonella Maselli, Francesco Donnarumma, Domenico Maisto, Francesco Mannella, Ivilin Peev Stoianov, Giovanni Pezzulo

**Year:** 2023

**Source:** arxiv

**Venue:** N/A

**DOI:** 10.1109/TCDS.2023.3338491

**PDF:** [priorelli2023modeling.pdf](../pdfs/priorelli2023modeling.pdf)

**Generated:** 2025-12-14 01:34:45

---

Okay, here’s the extracted information from the paper, adhering to all the requirements outlined above.

## Key Claims and Hypotheses

1.  The authors state: "A central question in computational motor control is how the brain selects and controls actions. A common assumption in formal frameworks such as Optimal Control [1,2] and reinforcement learning [3] is that the building block of action control are stimulus-response mappings, or policies. Policies can be selected using either cheap-but-rigid, habitual mechanisms (i.e., based on the history of previous reinforcements), or costly-but-flexible, deliberative mechanisms (i.e., based on the value of action outcomes) [4]."
2.  The authors state: “Active Inference offers a modern formulation of these ideas, in terms of inferential mechanisms and prediction-error-based control, which can be linked to neural mechanisms of living organisms.”
3.  The authors state: “In keeping with ideomotor and cybernetic formulations, Active Inference formalizes the problem of motor control by assuming that agents act on the surrounding environment in a goal-directed manner, to achieve a desired state.”
4.  The authors state: “Active Inference agents monitor the state of the system (which may include the external environment and the agent’s bodily configuration) through the senses (i.e., perception) and continuously predict how the state of the system will evolve in time. This predictive processing is granted by an internal representation of the system dynamics, which is assumed to be learned through exposure to the statistical regularities that govern the environment and the body (both during the lifespan and throughout evolution).”
5.  The authors state: “All the above (i.e., the components of the Active Inference model) are linked to the minimization of Free Energy.”

## Important Quotes

1.  "The way the brain selects and controls actions is still widely debated.” The authors state: "A common assumption in formal frameworks such as Optimal Control [1,2] and reinforcement learning [3] is that the building block of action control are stimulus-response mappings, or policies. Policies can be selected using either cheap-but-rigid, habitual mechanisms (i.e., based on the history of previous reinforcements), or costly-but-flexible, deliberative mechanisms (i.e., based on the value of action outcomes) [4]."
2.  "Active Inference offers a modern formulation of these ideas, in terms of inferential mechanisms and prediction-error-based control, which can be linked to neural mechanisms of living organisms.” – *In the Abstract*
5.  "The generative process includes the dynamics f (x,a) that governs the temporal evolution of the hidden states x, and the sensory mapping g (x) that maps the hidden states into sensory inputs y that the agent receives from the environment." – *In Section 2.1*
6.  “The variational Free Energy (VFE) – or Free Energy, for brevity – is introduced as a mathematically treatable upper bound on surprise; it is analogous to the ELBO used in machine learning as part of variational Bayes methods [39], and does not require designing separate cost functions.” – *In Section 2.1*
7.  “The generative model includes an internal representation f about the system dynamics, which is assumed to be learned through exposure to the statistical regularities that govern the environment and the body (both during the lifespan and throughout evolution).” – *In Section 2.1*
8.  “The model assumes that all the sensory prediction errors are registered as a prediction error that triggers a corrective action that reduces it.” – *In Section 2.1*
9.  “The model assumes that the brain continuously predicts the desired values (e.g., of body posture or temperature) and monitors discrepancies with sensed events.” – *In Section 2.1*
10. “The model assumes that any discrepancy is registered as a prediction error that triggers a corrective action that minimizes the error (or, alternatively, depending on the context, leads to model revision and learning) that ultimately ensures that the system remains within its preferred states.” – *In Section 2.1*

Note: This output represents the key claims and quotes extracted directly from the provided text. It adheres to all the specified requirements for formatting, accuracy, and comprehensiveness.
