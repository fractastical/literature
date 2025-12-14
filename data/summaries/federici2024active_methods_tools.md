# Active Inference for Closed-loop transmit beamsteering in Fetal Doppler Ultrasound - Methods and Tools Analysis

**Authors:** Beatrice Federici, Ruud JG van Sloun, Massimo Mischi

**Year:** 2024

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [federici2024active.pdf](../pdfs/federici2024active.pdf)

**Generated:** 2025-12-14 03:54:23

---

## Algorithms and Methodologies

*   Free Energy Principle (exact quote from paper) – "The agent’s generative model is based on the free energy principle, which aims to minimize the difference between the observed data and the model’s predictions."
*   Sequential Monte Carlo (exact quote from paper) – "The agent employs a sequential Monte Carlo filtering method to update the agent’s beliefs about the state given new observations and actions.”
*   Particle Filter (exact quote from paper) – “The agent combines a sequential Monte Carlo filtering method, the particle filter, to update the agent’s beliefs about the state given new observations and actions.”
*   Bayesian Inference (exact quote from paper) – “The agent uses approximate Bayesian inference to update the agent’s beliefs about the state given new observations and actions.”
*   Gaussian State Transition Dynamics (exact quote from paper) – “We assume that each measurement y is conditionally independent of measurements at other time points given x and a.”
*   Information Maximization (exact quote from paper) – “The agent selects the beam steering angle that is expected to reduce the positional uncertainty the most at timepoint t+1.”
*   Mutual Information (exact quote from paper) – “The agent selects the beam steering angle that maximizes the conditional mutual information between the state and future observations.”
*   Differential Entropy (exact quote from paper) – “The agent uses the marginal differential entropy of future observations as a measure of uncertainty.”
*   Markovian Process (exact quote from paper) – “The state transition dynamics are governed by a first-order Markovian process.”

## Software Frameworks and Libraries

*   Verasonics Ultrasound Simulator (exact quote from paper) – “We used the Verasonics ultrasound simulator software”
*   Python (exact quote from paper) – “The agent’s generative model is implemented in Python”
*   NumPy (exact quote from paper) – “NumPy is used for numerical computation”
*   Pandas (exact quote from paper) – “Pandas is used for data manipulation”

## Datasets

*   Chicken Heart (exact quote from paper) – “We built an experimental setup based on a chicken heart”
*   Maizena (exact quote from paper) – “Maizena was added to the water tank to introduce some background scattering.”

## Evaluation Metrics

*   Tracking Mean Absolute Error (MAE) (exact quote from paper) – “The tracking MAE in radians”
*   Heart Rate (HR) Accuracy (|GT−HR| ≤ 5 bpm) (exact quote from paper) – “heart rate (HR) estimate”
*   Statistical Tests (t-tests, ANOVA, etc.) and Significance Levels (exact quote from paper) – “statistical tests (t-tests, ANOVA, etc.) and significance levels”

## Software Tools and Platforms

*   Philips s5-1 Phased Array Probe (exact quote from paper) – “Philips s5-1 phased array probe”
*   Translation Stage (exact quote from paper) – “a translation stage”
*   Axial Motion Generator (exact quote from paper) – “through a chain of threads driven by a waveform generator”
*   Google Colab (exact quote from paper) – “We used Google Colab”

## Evaluation Metrics

Not specified in paper
