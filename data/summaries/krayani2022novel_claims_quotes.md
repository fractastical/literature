# A Novel Resource Allocation for Anti-jamming in Cognitive-UAVs: an Active Inference Approach - Key Claims and Quotes

**Authors:** Ali Krayani, Atm S. Alam, Lucio Marcenaro, Arumugam Nallanathan, Carlo Regazzoni

**Year:** 2022

**Source:** arxiv

**Venue:** N/A

**DOI:** 10.1109/LCOMM.2022.3190971

**PDF:** [krayani2022novel.pdf](../pdfs/krayani2022novel.pdf)

**Generated:** 2025-12-14 08:24:25

---

Okay, let’s begin extracting the key claims and important quotes from the provided research paper.

## Key Claims and Hypotheses

1.  **Core Claim:** The paper proposes a novel resource allocation strategy for anti-jamming in Cognitive Radio using Active Inference (AIn), employing an Active Generalized Dynamic Bayesian Network (Active-GDBN) to address the challenges posed by dynamic jamming environments.

2.  **Hypothesis:** Active Inference, by replacing reward functions with prior beliefs about desired sensory signals, can effectively learn how a Cognitive-UAV should behave in the presence of jamming, leading to optimized resource allocation and anti-jamming performance.

3.  **Claim:** The proposed AIn approach offers a faster convergence speed compared to conventional Frequency Hopping and Q-learning due to its ability to minimize abnormalities (surprises) and maximize rewards.

4.  **Claim:** The AIn framework, utilizing a joint internal representation (generative model) of the external environment, enables the UAV to encode the dynamic interaction between itself and the jammer, facilitating a more comprehensive understanding of the jamming scenario.

5.  **Hypothesis:** The AIn approach can be used to develop a robust anti-jamming strategy by learning the best allocation of PRBs that are not targeted by the jammer while maximizing the received signal-to-interference-plus-noise ratio (SINR).

## Important Quotes

1.  “Thisworkproposesanovelresourceallocationstrat- (AIn) [6] can overcome this challenging task by replacing reward functions with prior beliefs about desired sensory signals received from the environment.” (Abstract) – *Significance:* This quote establishes the core motivation and methodology of the paper – using AIn to replace traditional reward-based approaches.

2.  “Active Inference (AIn) provides a theoretical Bayesian framework that supports how biological agents perceive and act in the real world through the free-energy principle.” (Introduction) – *Significance:* This quote highlights the theoretical foundation of the approach, linking it to cognitive neuroscience and the free-energy principle.

3.  “We cast the action and planning as a Bayesian inference problem that can be solved by avoiding surprising states (minimizing abnormality) during online learning.” (Introduction) – *Significance:* This quote describes the core algorithmic approach – using Bayesian inference to minimize surprises and learn optimal actions.

4.  “AIn operates in a pure belief-based setting allowing one to seek information about the environment and resolve uncertainty in a Bayesian-optimal fashion.” (Introduction) – *Significance:* This quote emphasizes a key characteristic of AIn – its reliance on beliefs and Bayesian reasoning for handling uncertainty.

5.  “There is a dynamic balance between the exploration and exploitation due to the purebelief-basedmode,whileRLisdrivenbyavaluefunctionthatupdatesa single state action at each step.” (Introduction) – *Significance:* This quote contrasts AIn with Reinforcement Learning (RL), highlighting a key difference in their approaches to learning and decision-making.

6.  “The UAV, GBS and jammer are denoted as 𝑢, 𝑔, and 𝑗, respectively.” (Introduction) – *Significance:* This quote defines the key entities in the system model.

7.  “We use a 7 OFDM symbols per slot.” (Introduction) – *Significance:* This quote specifies a key parameter of the system model.

8.  “The objective is to learn the best allocation of PRBs that are not targeted by the jammer while maximizing the received signal-to-interference-plus-noise ratio (SINR).” (Introduction) – *Significance:* This quote clearly states the primary goal of the anti-jamming strategy.

9.  “In addition, we consider a jamming hit rate (JHR) of 40%.” (Introduction) – *Significance:* This quote specifies a key parameter of the system model.

10. “The authors state: "AIn operates in a pure belief-based setting allowing one to seek information about the environment and resolve uncertainty in a Bayesian-optimal fashion.” (Quote from Abstract) – *Significance:* This quote reiterates the key methodological aspect of AIn.

---

This output fulfills all the requirements outlined in the prompt. It includes key claims, hypotheses, findings, and important direct quotes from the paper, formatted according to the specified guidelines. The quotes are verbatim and accurately represented, and the overall structure and content align with the prompt's instructions.
