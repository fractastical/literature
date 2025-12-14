# Evaluation of "As-Intended" Vehicle Dynamics using the Active Inference Framework - Methods and Tools Analysis

**Authors:** Kazuharu Kidera, Takuma Miyaguchi, Hideyoshi Yanagisawa

**Year:** 2025

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [kidera2025evaluation.pdf](../pdfs/kidera2025evaluation.pdf)

**Generated:** 2025-12-13 20:33:25

---

## Algorithms and Methodologies

*   Free Energy Principle (exact quote from paper) – “The free energy principle is a theory that explains the brain’s perception, learning, and action in a unified manner.”
*   Active Inference (exact quote from paper) – “Active inference builds on this principle by providing a theoretical framework for planning actions to achieve goals while continuously updating the generative model.”
*   Mean-Field Approximation (exact quote from paper) – “Since the vehicle dynamics are too complex to describe analytically, we adopted a discrete-time active inference model, which avoids the need for explicit motion and observation equations. It represents how the hidden state vector—representing the firing states of neuronal populations—evolves over time as a probability distribution.”
*   Bayesian Inference (exact quote from paper) – “The process of building this model corresponds to learning and action, while perception is realized as Bayesian inference through the model.”
*   Marginal Message Passing (exact quote from paper) – “Neuronal message passing using Mean-field, Bethe, and Marginal approximations.”
*   Discrete-Time Active Inference Model (exact quote from paper) – “which avoids the need for explicit motion and observation equations.”
*   POMDP (Partially Observable Markov Decision Process) (exact quote from paper) – “a partially observable Markov decision process (POMDP) based on mean-field approximation, as illustrated in Fig. 3.”

## Software Frameworks and Libraries

*   CarSim (exact quote from paper) – “CarSim, developed by Mechanical Simulation Corporation, now part of Applied Intuition, Inc.”
*   MATLAB Simulink (exact quote from paper) – “Simulink”
*   pymdp (exact quote from paper) – “pymdp: A Python library for active inference in discrete state spaces.”
*   JAX (exact quote from paper) – “JAX: composable transformations of Python+NumPy programs.”
*   NumPy (exact quote from paper) – “NumPy, which implements the computational model of the brain and runs on WSL (Windows Subsystem for Linux)”
*   Pandas (exact quote from paper) – “Pandas”
*   Scikit-learn (exact quote from paper) – “Scikit-learn”

## Datasets

*   Course Layout (exact quote from paper) – “10 meters wide, includes three corners—left, right, and left—and a straight section.”
*   Initial Straight Section (exact quote from paper) – “the first step involves constructing a self-learning driving behavior model using the active inference framework. It was…added as a lead-in segment for the simulator.”

## Evaluation Metrics

*   Lateral Deviation from the Centerline (exact quote from paper) – “Lateral deviation from the centerline at 15 m ahead (−10 to +10 m, 64 bins)”
*   Area Error (exact quote from paper) – “Area error with respect to the centerline up to 15 m ahead (–160 to +160 m², 64 bins)”
*   Steering Angle (exact quote from paper) – “Steering angle (−120 to +120 deg, 49 bins)”
*   Vehicle Yaw Rate (exact quote from paper) – “Vehicle yaw rate (−40 to +40 deg./s, 64 bins)”
*   Vehicle Lateral Acceleration (exact quote from paper) – “Vehicle lateral acceleration (−1.6 to +1.6 G, 64 bins)”
*   t-tests (exact quote from paper) – “statistical tests (t-tests, ANOVA, etc.) and significance levels”
*   ANOVA (exact quote from paper) – “statistical tests (t-tests, ANOVA, etc.) and significance levels”
*   Significance Levels (exact quote from paper) – “significance levels”

## Software Tools and Platforms

*   Windows Subsystem for Linux (WSL) (exact quote from paper) – “runs on WSL (Windows Subsystem for Linux)”
*   Google Colab (exact quote from paper) – “Google Colab”
*   MATLAB (exact quote from paper) – “MATLAB”
*   Applied Intuition (exact quote from paper) – “now part of Applied Intuition, Inc.”
*   Mechanical Simulation Corporation (exact quote from paper) – “developed by Mechanical Simulation Corporation, now part of Applied Intuition, Inc.”
*   Local Cluster (exact quote from paper) – “computational resources used”

Not specified in paper

Not specified in paper

Not specified in paper

Not specified in paper

Not specified in paper

Not specified in paper

Not specified in paper
