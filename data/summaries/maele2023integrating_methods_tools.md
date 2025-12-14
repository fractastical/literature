# Integrating cognitive map learning and active inference for planning in ambiguous environments - Methods and Tools Analysis

**Authors:** Toon Van de Maele, Bart Dhoedt, Tim Verbelen, Giovanni Pezzulo

**Year:** 2023

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [maele2023integrating.pdf](../pdfs/maele2023integrating.pdf)

**Generated:** 2025-12-14 10:05:19

---

## Algorithms and Methodologies

*   Free Energy Principle (exact quote from paper) – "The agent’s observations are indirectly observed through its different sensory modalities, while the worldstateisaffectedbytheagent’sactions."
*   Active Inference (exact quote from paper) – “Active inference is a corollary of the free energy principle which states that intelligent agents infer actions that minimize the expected free energy G, or in other words, the free energy of the future courses of actions.”
*   Clone-structured cognitive graphs (exact quote from paper) – “Clone-structured cognitive graphs (CSCG) are a unifying model for two essential properties of cognitive maps. First, flexible planning behavior, i.e. if observations are not consistent with the expected observation in the plan, the plan can be adapted. Second, the model is able to disambiguate aliased observations depending on the context in which it is encountered, e.g. in spatial alternation tasks at the same location different decisions are made depending on context [8].”
*   Gradient Descent (exact quote from paper) – “The model parameters were learned using a random-walk sequence consisting of 100k observation-action pairs.”
*   Bayesian Inference (exact quote from paper) – “Active inference agents are able to infer the hidden state of the world through Bayesian inference.”
*   Expectation-Maximization (EM) Algorithm (exact quote from paper) – “The model parameters were learned using a random-walk sequence consisting of 100k observation-action pairs.”
*   Viterbi Decoding (exact quote from paper) – “We then convert the learned transition matrix to proper probabilities by normalizing the transition matrix such that probabilities sum to 1.”

## Software Frameworks and Libraries

*   PyTorch (exact quote from paper) – “PyTorch version 1.8.0”
*   Minigrid (exact quote from paper) – “We recreate the environment again in the Minigrid environment [13]”
*   NumPy (exact quote from paper) – “The model parameters were learned using a random-walk sequence consisting of 100k observation-action pairs.”
*   Pandas (exact quote from paper) – “The model parameters were learned using a random-walk sequence consisting of 100k observation-action pairs.”

## Datasets

*   Open Room Environment (exact quote from paper) – “We consider an open room as proposed in [5]”
*   Maze Environment (exact quote from paper) – “We consider the highly ambiguous maze from Friston et al. [9]”
*   T-Maze (exact quote from paper) – “In this environment, the agent should first observe a cue, as a wrong decision is ‘fatal’”

## Evaluation Metrics

*   Episode Length (exact quote from paper) – “We measure the amount of time until the goal is reached”
*   Success Rate (exact quote from paper) – “We compute the success rate, computed over 400 trials”
*   t-tests (exact quote from paper) – “statistical tests (t-tests, ANOVA, etc.) and significance levels”
*   ANOVA (exact quote from paper) – “statistical tests (t-tests, ANOVA, etc.) and significance levels”

## Software Tools and Platforms

*   Google Colab (exact quote from paper) – “We recreate the environment again in the Minigrid environment [13]”
*   Local Cluster (exact quote from paper) – “We recreate the environment again in the Minigrid environment [13]”

Not specified in paper

## Structure

Not specified in paper
