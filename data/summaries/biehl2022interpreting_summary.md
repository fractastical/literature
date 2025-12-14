# Interpreting systems as solving POMDPs: a step towards a formal understanding of agency

**Authors:** Martin Biehl, Nathaniel Virgo

**Year:** 2022

**Source:** arxiv

**Venue:** N/A

**DOI:** 10.1007/978-3-031-28719-0_2

**PDF:** [biehl2022interpreting.pdf](../pdfs/biehl2022interpreting.pdf)

**Generated:** 2025-12-14 08:29:05

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

## Interpreting systems as solving POMDPs: a step towards a formal understanding of agencyThis paper investigates the possibility of interpreting systems as solving Partially Observable Markov Decision Processes (POMDPs). We propose a method for achieving this, where a system’s state is interpreted as the probability of a hidden state being equal to one, and the system’s state is interpreted as the belief probability of the hidden state being equal to1. This approach provides a formal framework for understanding agency.The core of this approach involves a Markov Decision Process (MDP) and its solution. An MDP is defined as a tuple (X,A,ν,r) where X is the state space, A is the action space, ν is the transition kernel, and r is the reward function. The transition kernel takes a state x∈X and an action a∈A to a probability distribution ν(x,a) over next states and the reward function returns a real-valued instantaneous reward r(x,a) depending on the hidden state and an action. A solution to a given MDP is a control policy. As the goal of the MDP we here choose the maximization of expected cumulative discounted reward for an infinite time horizon (an alternative would be to consider finite time horizons). This means an optimal policy maximizes(cid:34) ∞ (cid:35)(cid:88)E γt−1r(x ,a ) . (28)t tt=1where0 < γ < 1 is a parameter called the discount factor. This specifies the goal.To express the optimal policy explicitly we can use the optimal value function V∗ :X →R. This is the solution to the Bellman equation [10]:(cid:32) (cid:33)(cid:88)V∗(x)=max r(x,a)+γ β(x′,a,x)V∗(x′) . (29)a∈Ax′∈XThe optimal policy is then [9]:(cid:88) (cid:88)π∗(x)=argmax r(x,a)+γ κ(x′,s|x,a)b(x)V∗(x′) . (42)a∈As∈Sh,x′∈HThis is the expression we used in eq. (4). The optimal policy for the belief state MDP is then [9]:(cid:88) (cid:88)π∗(x)=argmaxr(x,a)+γ κ(x′,s|x,a)b(x)V∗(x′). (5).The key to this approach is the Markov Decision Process (MDP) and its solution. (4). (5).Note that if eq. (14) is not true and the probability of an input i is impossibleaccording to the POMDP transition function, the kernel ψ, and the optimalpolicy ω then eq. (13) puts no constraint on the machine kernel µ since bothsides are zero. So the behavior of the stochastic Moore machine in this caseis arbitrary. 

This makes sense since according to the POMDP that we use tointerpret the machine this input is impossible, so our interpretation should tellus nothing about this situation.
