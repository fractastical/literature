# Coupled autoregressive active inference agents for control of multi-joint dynamical systems

**Authors:** Tim N. Nisslbeck, Wouter M. Kouw

**Year:** 2024

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [nisslbeck2024coupled.pdf](../pdfs/nisslbeck2024coupled.pdf)

**Generated:** 2025-12-14 02:40:11

**Validation Status:** ✓ Accepted
**Quality Score:** 1.00

---

### OverviewThis paper investigates the control of multi-joint dynamical systems using coupled autoregressive active inference agents. The authors propose a novel approach that leverages shared memories between agents to improve control performance. The core idea is to minimize expected free energy over a finite time horizon, utilizing autoregressive models for prediction and control. The study demonstrates the effectiveness of this approach on a double mass-spring-damper system, showcasing its ability to drive the system to a desired position while exhibiting improved stability and alignment with the goal.### MethodologyThe authors construct a system of multiple scalar autoregressive model-based agents, coupled together by virtue of sharing memories. Each subagent infers parameters through Bayesian filtering and controls by minimizing expected free energy over a finite time horizon. The model is based on an autoregressive exogenous (ARX) model, where the likelihood function is defined as:“p(y |θ,τ,u ,u¯ ,y¯) = N(y |θ, (cid:2) (cid:3) ,τ−1(cid:1) , (cid:0) (cid:1) )” [1]. The prior distribution on the parameters is a multivariate Gaussian - univariate Gamma distribution [2]. The agents use a shared memory buffer to store past observations and control inputs, enabling them to learn from each other’s experiences. The authors use a step size of ∆t =0.01 and a time horizon of n =120. The agents are initialized with a zero matrix for the parameters (µ ) and an identity matrix for the covariance matrix (Λ ) [3]. The agents use a Bayesian filtering approach to update their parameter beliefs based on observed data. The agents minimize the expected free energy by adjusting their control inputs to reduce the discrepancy between the predicted and actual system outputs. The agents use a step size of ∆t =0.01 and a time horizon of n =120.### ResultsThe experiments were conducted on a double mass-spring-damper system. The authors demonstrated that the coupled agents could learn the dynamics of the system and drive it to a desired position through a balance of explorative and exploitative actions. The agents exhibited a significant improvement in goal alignment and stability compared to uncoupled agents. Specifically, the coupled agents achieved lower prediction variance and more stable control trajectories. The authors observed that the coupled agents converged to the desired position within the first20 time steps, while the uncoupled agents required a longer time to reach the goal. The authors quantified the improvement in goal alignment by measuring the negative log-likelihood of the predicted output compared to the goal prior. The coupled agents achieved a significantly lower negative log-likelihood compared to the uncoupled agents. The authors observed that the coupled agents achieved a lower prediction variance and more stable control trajectories. The coupled agents achieved a significantly lower negative log-likelihood compared to the uncoupled agents.### Claims and FindingsThe authors state: "The agents were able to learn the dynamics of the system and drive it to a desired position through a balance of explorative and exploitative actions" [4]. They note: "Coupling agents together lets them more accurately predict joint motion and infer an appropriate control policy sooner" [5]. The study demonstrates that the coupled agents outperform the uncoupled agents in terms of surprise and goal alignment [6]. The authors argue: "The agents were able to learn the dynamics of the system and drive it to a desired position through a balance of explorative and exploitative actions" [4]. The study demonstrates that the coupled agents outperform the uncoupled agents in terms of surprise and goal alignment [6].### MethodsThe authors construct a system of multiple scalar autoregressive model-based agents, coupled together by virtue of sharing memories [7]. The authors use a Bayesian filtering approach to update their parameter beliefs based on observed data [8]. The agents use a step size of ∆t =0.01 and a time horizon of n =120 [8]. 

The agents use a 

Bayesian filtering approach to update their parameter beliefs
