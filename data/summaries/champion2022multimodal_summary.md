# Multi-Modal and Multi-Factor Branching Time Active Inference

**Authors:** Théophile Champion, Marek Grześ, Howard Bowman

**Year:** 2022

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [champion2022multimodal.pdf](../pdfs/champion2022multimodal.pdf)

**Generated:** 2025-12-14 13:01:19

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

### Multi-Modal and Multi-Factor Branching Time Active Inference

### OverviewThis paper investigates a novel approach to active inference, termed Multi-Modal and Multi-Factor Branching Time Active Inference (BTAI). The authors address the exponential complexity inherent in traditional active inference frameworks by introducing a method that allows for the modelling of several observations, each with its own likelihood mapping, and several latent states, each with its own transition mapping. The core innovation lies in the factorisation of the likelihood and transition mappings, which significantly accelerates the computation of the posterior. The paper demonstrates that BTAI outperforms existing approaches on the dSprites environment, a benchmark task for active inference models.### MethodologyThe authors present BTAI as a framework for modelling complex neuro-cognitive phenomena. The key methodological elements of BTAI include:1) the use of variational message passing (VMP) to compute the posterior over latent states,2) the use of forward predictions to compute the posterior over future observations, and3) the use of a Monte-Carlo tree search (MCTS) algorithm to plan actions. The authors also highlight the importance of the factorisation of the likelihood and transition mappings, which significantly accelerates the computation of the posterior. The authors use a numerical simulation of the dSprites environment to evaluate the performance of BTAI.### ResultsThe authors demonstrate that BTAI can solve96.9% of the dSprites task in5.1 seconds, which is significantly better than the performance of the existing BTAI and VMP approaches. Specifically, BTAI achieves a98.6% success rate in17.5 seconds, while the original BTAI achieves88.5% success rate in100 trials in1.286 seconds. The authors also show that BTAI can model several observations and latent states, and that the performance of BTAI improves as the number of latent states increases. The authors report that the key to BTAI’s success is the ability to model multiple observations and latent states, and the factorisation of the likelihood and transition mappings.### DiscussionThe authors conclude that BTAI represents a significant advance in active inference, offering a tractable solution to the exponential complexity challenges associated with traditional approaches. 

The ability to model multiple observations and latent states, coupled with the factorisation of the likelihood and transition mappings, enables BTAI to achieve high performance on complex tasks. 

The authors suggest that BTAI could be applied to a wide range of neuro-cognitive phenomena, such as habit formation, dopaminergic discharge, and curiosity.
