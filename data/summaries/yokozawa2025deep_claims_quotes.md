# Deep Active Inference with Diffusion Policy and Multiple Timescale World Model for Real-World Exploration and Navigation - Key Claims and Quotes

**Authors:** Riko Yokozawa, Kentaro Fujii, Yuta Nomura, Shingo Murata

**Year:** 2025

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [yokozawa2025deep.pdf](../pdfs/yokozawa2025deep.pdf)

**Generated:** 2025-12-13 22:01:00

---

Okay, let’s begin extracting the key claims and quotes from the provided research paper.

## Key Claims and Hypotheses

*   **Claim 1:** The paper proposes a deep active inference (AIF) framework that integrates a diffusion policy as the policy model and a multiple timescale recurrent state-space model (MTRSSM) as the world model for real-world exploration and navigation.
*   **Hypothesis 1:** Combining a diffusion policy with an MTRSSM will enable the robot to balance exploration and goal-directed navigation more effectively than traditional approaches.
*   **Claim 2:** The framework leverages the generative capabilities of diffusion models to produce diverse candidate action sequences, while the MTRSSM predicts long-horizon state transitions through latent imagination, thereby enhancing the robot’s ability to handle uncertainty.
*   **Hypothesis 2:** The hierarchical temporal structure of the MTRSSM, combined with the generative power of the diffusion policy, will improve the robot’s ability to accurately predict future states and plan accordingly.
*   **Claim 3:** The EFE minimization approach, incorporating both epistemic and extrinsic values, allows the robot to adaptively balance exploration and goal-directed behavior based on the current situation.
*   **Hypothesis 3:** The integration of epistemic and extrinsic values within the EFE framework will lead to more robust and adaptive navigation behavior, particularly in complex and uncertain environments.
*   **Claim 4:** The experimental results demonstrate that the proposed framework achieves higher success rates and fewer collisions compared to baseline methods, particularly in exploration-demanding scenarios.

## Important Quotes

**Context:** Introduction
**Significance:** This quote establishes the core concept of the proposed AIF framework and its key components.

**Quote 2:** "Active inference (AIF) based on the free-energy principle [20]–[23] provides a unified framework for these behaviors by minimizing the expected free energy (EFE), thereby combining epistemic and extrinsic values."
**Context:** Introduction
**Significance:** This quote defines AIF and its fundamental principle of minimizing EFE, which is central to the paper’s approach.

**Context:** Fig. 1
**Significance:** This quote describes the diffusion policy’s core mechanism – iterative denoising – which is key to generating diverse action sequences.

**Quote 4:** “The diffusion policy generates diverse candidate action sequences while the MTRSSM predicts their long-horizon consequences through latent imagination, enabling action selection that minimizes EFE.”
**Context:** Fig. 1
**Significance:** This quote highlights the synergistic relationship between the diffusion policy and the MTRSSM, where the former generates actions and the latter predicts their consequences.

**Quote 5:** “At each time step, the EFE is calculated using latent imagination.”
**Context:** Discussion
**Significance:** This quote emphasizes the role of latent imagination in the EFE calculation, which is crucial for long-horizon prediction.

**Quote 6:** “The MTRSSM predicts their long-horizon consequences through latent imagination.”
**Context:** Fig. 1
**Significance:** This quote reiterates the importance of the MTRSSM’s ability to predict long-horizon states.

**Quote 7:** “In summary, the proposed framework achieves a success rate of 75%, outperforming RSSM (64%) and OnlyExtrinsic (53%). The improvement was most pronounced in exploration-demanding scenarios, where our framework achieved 78% compared with 61% for RSSM and only 28% for OnlyExtrinsic.”
**Context:** Results
**Significance:** This quote presents the key quantitative results of the experiments, demonstrating the effectiveness of the proposed framework.

**Quote 8:** “To address long-horizon prediction, we adopt the MTRSSM, which extends the recurrent state-space model [30] by incorporating hierarchical temporal structures.”
**Context:** Discussion
**Significance:** This quote explains the rationale behind using the MTRSSM to improve long-horizon prediction.

**Quote 9:** “The stochastic states are sampled from either the prior distributions ph,pl or the approximate posterior distributions qh,pl.”
**Context:** Discussion
**Significance:** This quote describes the sampling process of the stochastic states within the MTRSSM.

**Quote 10:** “The EFE comprises two terms: epistemic value, which naturally encourages exploration; and extrinsic value, which accounts for goal-directed behavior.”
**Context:** Introduction
**Significance:** This quote defines the two components of the EFE and their respective roles in guiding the robot’s behavior.

I have extracted and formatted the key claims and quotes as requested.  Do you want me to refine any of these, or perhaps extract additional information based on a specific focus (e.g., methodological details, experimental setup, or a particular aspect of the results)?
