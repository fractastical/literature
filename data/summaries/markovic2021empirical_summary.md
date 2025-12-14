# An empirical evaluation of active inference in multi-armed bandits

**Authors:** Dimitrije Markovic, Hrvoje Stojic, Sarah Schwoebel, Stefan J. Kiebel

**Year:** 2021

**Source:** arxiv

**Venue:** N/A

**DOI:** 10.1016/j.neunet.2021.08.018

**PDF:** [markovic2021empirical.pdf](../pdfs/markovic2021empirical.pdf)

**Generated:** 2025-12-14 11:47:58

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

An empirical evaluation of active inference in multi-armed banditsThis paper investigates the performance of active inference in the context of multi-armed bandit problems. The authors propose an approximate active inference algorithm and compare it to two state-of-the-art bandit algorithms – a Bayesian upper confidence bound (UCB) algorithm and an optimistic Thompson sampling algorithm. The study reveals that the active inference algorithm does not produce efficient long-term behaviour in stationary bandits: however, it performs substantially better than the other algorithms in the more challenging switching bandit problem. The authors demonstrate that the active inference algorithm achieves a regret rate that is close to the lower bound, as predicted by theoretical analysis.The authors state: “A key feature of sequential decision making under uncertainty is a need to balance between exploiting – choosing the best action according to the current knowledge, and exploring – obtaining information about the values of other actions.” They note: “The multi-armed bandit problem is a classical task that captures this trade-off, serving as a vehicle in machine learning for developing bandit algorithms that are useful in numerous industrial applications.” The authors further state: “Active inference – an approach to sequential decision making developed recently in neuroscience – is distinguished by its sophisticated strategy for resolving the exploration-exploitation trade-off.”The study employs a Bayesian approach to the multi-armed bandit problem, using a variational inference scheme to approximate the posterior beliefs about the reward probabilities of each arm. The authors use a Bernoulli distribution to model the outcomes of the bandit arms, and they employ a Beta distribution to represent the prior beliefs about the reward probabilities. The authors use the upper confidence bound (UCB) algorithm as a benchmark, which is a well-established algorithm for solving the multi-armed bandit problem. The UCB algorithm is based on the principle of balancing exploration and exploitation by taking into account the uncertainty in the estimates of the reward probabilities. The authors also use the optimistic Thompson sampling algorithm, which is a Bayesian algorithm that samples from the posterior distribution of the reward probabilities.The authors conducted experiments on two types of bandit problems: a stationary bandit and a switching bandit. The stationary bandit is a classic benchmark problem for evaluating bandit algorithms, and the switching bandit is a more challenging problem that requires the algorithm to adapt to changes in the environment. The authors found that the active inference algorithm outperformed the other algorithms in the switching bandit problem, which suggests that the active inference framework is a promising approach for solving complex sequential decision-making problems. The authors report that the active inference algorithm achieves a regret rate that is close to the lower bound predicted by theoretical analysis.The authors conclude that active inference is a promising approach for solving multi-armed bandit problems, and that it has the potential to be used in a wide range of applications, including robotics, finance, and healthcare. The authors suggest that further research is needed to develop more efficient and scalable active inference algorithms, and to investigate the use of active inference in more complex environments. The authors note that the active inference framework provides a general framework for understanding human learning and decision-making, and that it has implications for a wide range of fields.
