# Active Inference through Incentive Design in Markov Decision Processes

**Authors:** Xinyi Wei, Chongyang Shi, Shuo Han, Ahmed H. Hemida, Charles A. Kamhoua, Jie Fu

**Year:** 2025

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [wei2025active.pdf](../pdfs/wei2025active.pdf)

**Generated:** 2025-12-13 23:01:33

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

### OverviewThis paper investigates active inference through incentive design in Markov decision processes. The authors present a method for active inference with partial observations in stochastic systems, employing incentive design to improve inference accuracy and efficiency. The core problem involves a leader attempting to infer a follower’s type given partial observations and side payments, aiming to balance information gain with the cost of incentives. The research focuses on formulating this problem as a bi-level optimization, utilizing a single-level optimization with a hidden Markov model constructed from the set of policies of different potential follower types. The key contribution lies in reducing the problem to a single-level optimization, enabling a gradient-based solution.### MethodologyThe authors formulate the problem as a bi-level optimization, where the leader’s objective is to minimize the entropy of the estimated follower’s type given partial observations and the cost of side payments. The bi-level optimization problem is solved using a gradient-based algorithm. The algorithm leverages observable operators within the hidden Markov model (HMM) to compute the necessary gradients. The HMM is constructed from the set of policies of different potential follower types. The HMM is defined as⟨S,A,P,µ,γ,R¯⟩, where S is the set of states, A is the set of actions, P is the probabilistic transition function, µ is the initial state distribution, γ is the discount factor, and R¯ is the reward function. The authors utilize a single-level optimization approach, reducing the problem to a single-level optimization. The key is to reduce the problem to a single-level optimization, enabling the solution with gradient descent methods. The authors use observable operators in the HMM to compute the necessary gradients.### ResultsThe authors demonstrate the effectiveness of their approach through experiments in a stochastic grid world environment. In the first experiment, they use a fire rescue task with two types of robots (Type1 and Type2). Type1 robots have superior hardware compared to Type2 robots. The side payment is1 for a certain action at the target state. The conditional entropy converges to0.390, while the initial conditional entropy is0.945. The authors show that as the side payment increases, the conditional entropy decreases. The authors demonstrate that the optimal policy is achieved by minimizing the entropy of the estimated follower’s type given partial observations and the cost of side payments. The authors show that the optimal policy is achieved by minimizing the entropy of the estimated follower’s type given partial observations and the cost of side payments.### DiscussionThe authors’ approach offers a novel method for active inference through incentive design. By leveraging conditional entropy and gradient-based optimization, they achieve a balance between information gain and incentive costs. 

The results highlight the effectiveness of this approach in distinguishing between different robot types, even with partial observations and stochastic environments. 

The authors’ approach offers a novel method for active inference through incentive design
