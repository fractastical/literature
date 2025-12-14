# R-AIF: Solving Sparse-Reward Robotic Tasks from Pixels with Active Inference and World Models

**Authors:** Viet Dung Nguyen, Zhizhuo Yang, Christopher L. Buckley, Alexander Ororbia

**Year:** 2024

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [nguyen2024raif.pdf](../pdfs/nguyen2024raif.pdf)

**Generated:** 2025-12-14 03:19:00

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

Okay, here’s a summary of the paper “R-AIF: Solving Sparse-Reward Robotic Tasks from Pixels with Active Inference and World Models” following all your instructions.### OverviewThis paper introduces R-AIF, a novel framework for solving sparse-reward robotic tasks directly from pixel observations using active inference and world models. The authors address the challenges of applying active inference to POMDPs, particularly those involving continuous action spaces and sparse rewards. R-AIF leverages a contrastive recurrent state prior preference (CRSPP) model to learn a dynamic, adaptive prior over the environment’s hidden state, guiding the agent’s actions towards preferred states while minimizing the discrepancy between its predictions and the observed reality. The authors demonstrate R-AIF’s superior performance compared to existing state-of-the-art models across multiple benchmark environments, including the MountainCar and Meta-World tasks.### MethodologyThe core of R-AIF is its CRSPP model, which learns a prior over the hidden state of the environment. This model utilizes a gated recurrent unit (GRU) to capture temporal dependencies in the observed data. The CRSPP model is trained using a contrastive objective, encouraging the model to predict the preferred state based on the current observation. 

The model incorporates a key element: a dynamically updated prior preference, which is shaped by the agent’s interactions with the environment. 

The authors also employ an actor-critic framework, utilizing a neural network to estimate the value function and a policy network to select actions
