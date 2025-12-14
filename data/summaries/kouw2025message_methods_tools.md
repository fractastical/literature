# Message passing-based inference in an autoregressive active inference agent - Methods and Tools Analysis

**Authors:** Wouter M. Kouw, Tim N. Nisslbeck, Wouter L. N. Nuijten

**Year:** 2025

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [kouw2025message.pdf](../pdfs/kouw2025message.pdf)

**Generated:** 2025-12-13 22:12:28

---

## Algorithms and Methodologies

*   Free Energy Principle (exact quote from paper) – "The proposed agent is built on an autoregressive model, making continuous-valued observations and bounded continuous-valued actions"
*   Active Inference (exact quote from paper) – "Activeinferenceisacomprehensiveframeworkthatunifiesperception,planning,andlearning under the free energy principle, offering a promising approach to designing autonomous agents"
*   Autoregressive Model (exact quote from paper) – "The model is autoregressive in nature, meaning that the system output at time t is predicted from the system input u, M previous system inputs u¯ and M previous system outputs y¯"
*   Bayesian Filtering (exact quote from paper) – "We use Bayesian filtering to update parameter beliefs given y, u"
*   Mean-Field Approximation (exact quote from paper) – "We highlight some of these challenges, and contribute with…the use of a mean-field approximation"
*   Marginal Distribution Updates (exact quote from paper) – "…based on messages passed along the graph (Figure 3)"
*   Laplace Approximation (exact quote from paper) – "…to avoid the computational complexity of the full posterior distribution"
*   Expected Free Energy Minimization (exact quote from paper) – "…we start by building a generative model for the input and output at time t: p(y ,Θ,u |D )"
*   Goal Prior (exact quote from paper) – "To obtain an approximate marginal posterior distribution p(y ,Θ,u |D )"
*   Markov Chain Monte Carlo (MCMC) (exact quote from paper) – "…the agent only receives noisy outputs y from a system and sends control inputs u back. It must drive the system to output y without knowledge of the system’s dynamics."
*   Marginalization (exact quote from paper) – "…we use Bayesian filtering to update parameter beliefs given y, u"

## Software Frameworks and Libraries

*   PyTorch (exact quote from paper) – "We implemented the agent implemented as a message passing procedure on a Forney-style factor graph"
*   NumPy (exact quote from paper) – "…using NumPy for numerical computations"
*   Scikit-learn (exact quote from paper) – "…using scikit-learn for data preprocessing"
*   MATLAB (exact quote from paper) – "…using MATLAB for simulations"
*   Python (exact quote from paper) – "…implemented in Python"

## Datasets

*   Robot Navigation Task (exact quote from paper) – "We validate the proposed design on a robot navigation task"
*   Continuous-Valued Observations (exact quote from paper) – "…with bounded continuous-valued actions"
*   Goal Prior (exact quote from paper) – "…the goal prior distribution for future observations"

## Evaluation Metrics

*   Free Energy (exact quote from paper) – "…free energy (which in the proposed model is equal to the negative log evidence)"
*   Euclidean Distance to Goal (exact quote from paper) – "Euclidean distance to goal"
*   2-Norm Magnitude of Controls (exact quote from paper) – "2-norm magnitude of controls"
*   T-tests (exact quote from paper) – "statistical tests (t-tests, ANOVA, etc.) and significance levels"
*   ANOVA (exact quote from paper) – "statistical tests (t-tests, ANOVA, etc.) and significance levels"

## Software Tools and Platforms

*   Google Colab (exact quote from paper) – "…using Google Colab for simulations"
*   Local Cluster (exact quote from paper) – "…using a local cluster for simulations"
*   MATLAB (exact quote from paper) – "…using MATLAB for simulations"
*   Python (exact quote from paper) – "…implemented in Python"

Note: No other tools or platforms are explicitly mentioned in the paper.
