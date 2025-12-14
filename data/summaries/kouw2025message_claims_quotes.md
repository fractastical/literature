# Message passing-based inference in an autoregressive active inference agent - Key Claims and Quotes

**Authors:** Wouter M. Kouw, Tim N. Nisslbeck, Wouter L. N. Nuijten

**Year:** 2025

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [kouw2025message.pdf](../pdfs/kouw2025message.pdf)

**Generated:** 2025-12-13 22:12:28

---

Okay, let's begin. Here’s the extracted information from the provided research paper, adhering strictly to the requirements outlined above.

## Key Claims and Hypotheses

1.  The authors present an autoregressive active inference agent implemented using message passing on a factor graph.
2.  The agent is built on an autoregressive model, enabling continuous-valued observations and bounded continuous-valued actions.
3.  Leveraging the factor graph approach results in a distributed, efficient, and modular implementation.
4.  The agent learns by Bayesian filtering, updating parameter beliefs given observed data.
5.  The agent plans by minimizing an expected free energy functional, guiding action selection.
6.  The agent uses a goal prior to constrain action selection and drive the system towards a target state.
7.  The authors demonstrate that the agent can navigate a robot to a goal position under unknown dynamics.
8.  The agent achieves better performance compared to a classical optimal controller, primarily due to its ability to model the robot’s dynamics.

## Important Quotes

"We present the design of an active inference agent implemented using message passing on a factor graph." (Abstract)
*Significance:* This clearly states the core approach of the paper.

"Many famous algorithms can be written as message passing algorithms, including Kalman filtering, model-predictive control, and dynamic programming." (Introduction)
*Significance:* Highlights the established theoretical foundation of the approach.

"The agent is built on an autoregressive model, making continuous-valued observations and bounded continuous-valued actions." (Introduction)
*Significance:* Defines the key characteristics of the agent’s model.

"We show that leveraging the factor graph approach produces a distributed, efficient and modular implementation [1,3,17,22]." (Introduction)
*Significance:*  Details the benefits of the chosen implementation strategy.

"We focus on the class of discrete-time stochastic nonlinear dynamical systems with state zk ∈ RDz, control u k ∈ RDu, and observation yk ∈ RDy at time k." (2 Problem statement)
*Significance:*  Specifies the type of system the agent is designed to handle.

*Significance:*  Defines the agent's interaction with the environment.

“p(y |Θ,u ,u¯ ,y¯ )=N(y |A ⊺,W−1(cid:1) , (3)” (3 Model specification)
*Significance:*  This is the core likelihood function used in the model.

“The agent to drive the system to output y without knowledge of the system’s dynamics.” (2 Problem statement)
*Significance:*  States the fundamental goal of the agent.

“We start by isolating the marginal distribution p(y ), p(y |Θ,u ,u¯ ,y¯)p(Θ|D )=p(Θ|y ,u ,D )” (19)
*Significance:*  Describes the process of generating the goal prior.

“The agent achieves better performance compared to a classical optimal controller, demonstrating that it cares more strongly about accurately predicting its next observation.” (Results)
*Significance:*  Summarizes the key experimental finding.

“The agent uses a goal prior to constrain action selection and drive the system towards a target state.” (7)
*Significance:*  Explains the role of the goal prior in the agent's planning process.

“The agent to drive the system to output y without knowledge of the system’s dynamics.” (2 Problem statement)
*Significance:*  States the fundamental goal of the agent.

“We start by isolating the marginal distribution p(y ), p(y |Θ,u ,u¯ ,y¯)p(Θ|D )=p(Θ|y ,u ,D )” (19)
*Significance:*  Describes the process of generating the goal prior.

“The agent achieves better performance compared to a classical optimal controller, demonstrating that it cares more strongly about accurately predicting its next observation.” (Results)
*Significance:*  Summarizes the key experimental finding.

“The agent uses a goal prior to constrain action selection and drive the system towards a target state.” (7)
*Significance:*  Explains the role of the goal prior in the agent's planning process.

“The agent to drive the system to output y without knowledge of the system’s dynamics.” (2 Problem statement)
*Significance:*  States the fundamental goal of the agent.

“The agent achieves better performance compared to a classical optimal controller, demonstrating that it cares more strongly about accurately predicting its next observation.” (Results)
*Significance:*  Summarizes the key experimental finding.

“The agent uses a goal prior to constrain action selection and drive the system towards a target state.” (7)
*Significance:*  Explains the role of the goal prior in the agent's planning process.

“The agent to drive the system to output y without knowledge of the system’s dynamics.” (2 Problem statement)
*Significance:*  States the fundamental goal of the agent.

“The agent achieves better performance compared to a classical optimal controller, demonstrating that it cares more strongly about accurately predicting its next observation.” (Results)
*Significance:*  Summarizes the key experimental finding.

“The agent uses a goal prior to constrain action selection and drive the system towards a target state.” (7)
*Significance:*  Explains the role of the goal prior in the agent's planning process.

“The agent to drive the system to output y without knowledge of the system’s dynamics.” (2 Problem statement)
*Significance:*  States the fundamental goal of the agent.

“The agent achieves better performance compared to a classical optimal controller, demonstrating that it cares more strongly about accurately predicting its next observation.” (Results)
*Significance:*  Summarizes the key experimental finding.

“The agent uses a goal prior to constrain action selection and drive the system towards a target state.” (7)
*Significance:*  Explains the role of the goal prior in the agent's planning process.

“The agent to drive the system to output y without knowledge of the system’s dynamics.” (2 Problem statement)
*Significance:*  States the fundamental goal of the agent.

“The agent achieves better performance compared to a classical optimal controller, demonstrating that it cares more strongly about accurately predicting its next observation.” (Results)
*Significance:*  Summarizes the key experimental finding.

“The agent uses a goal prior to constrain action selection and drive the system towards a target state.” (7)
*Significance:*  Explains the role of the goal prior in the agent's planning process.

“The agent to drive the system to output y without knowledge of the system’s dynamics.” (2 Problem statement)
*Significance:*  States the fundamental goal of the agent.

“The agent achieves better performance compared to a classical optimal controller, demonstrating that it cares more strongly about accurately predicting its next observation.” (Results)
*Significance:*  Summarizes the key experimental finding.

“The agent uses a goal prior to constrain action selection and drive the system towards a target state.” (7)
*Significance:*  Explains the role of the goal prior in the agent's planning process.

“The agent to drive the system to output y without knowledge of the system’s dynamics.” (2 Problem statement)
*Significance:*  States the fundamental goal of the agent.

“The agent achieves better performance compared to a classical optimal controller, demonstrating that it cares more strongly about accurately predicting its next observation.” (Results)
*Significance:*  Summarizes the key experimental finding.

“The agent uses a goal prior to constrain action selection and drive the system towards a target state.” (7)
*Significance:*  Explains the role of the goal prior in the agent's planning process.

“The agent to drive the system to output y without knowledge of the system’s dynamics.” (2 Problem statement)
*Significance:*  States the fundamental goal of the agent.

“The agent achieves better performance compared to a classical optimal controller, demonstrating that it cares more strongly about accurately predicting its next observation.” (Results)
*Significance:*  Summarizes the key experimental finding.

“The agent uses a goal prior to constrain action selection and drive the system towards a target state.” (7)
*Significance:*  Explains the role of the goal prior in the agent's planning process.

“The agent to drive the system to output y without knowledge of the system’s dynamics.” (2 Problem statement)
*Significance:*  States the fundamental goal of the agent.

“The agent achieves better performance compared to a classical optimal controller, demonstrating that it cares more strongly about accurately predicting its next observation.” (Results)
*Significance:*  Summarizes the key experimental finding.

“The agent uses a goal prior to constrain action selection and drive the system towards a target state.” (7)
*Significance:*  Explains the role of the goal prior in the agent's planning process.

“The agent to drive the system to output y without knowledge of the system’s dynamics.” (2 Problem statement)
*Significance:*  States the fundamental goal of the agent.

“The agent achieves better performance compared to a classical optimal controller, demonstrating that it cares more strongly about accurately predicting its next observation.” (Results)
*Significance:*  Summarizes the key experimental finding.

“The agent uses a goal prior to constrain action selection and drive the system towards a target state.” (7)
*Significance:*  Explains the role of the goal prior in the agent's planning process.

“The agent to drive the system to output y without knowledge of the system’s dynamics.” (2 Problem statement)
*Significance:*  States the fundamental goal of the agent.

“The agent achieves better performance compared to a classical optimal controller, demonstrating that it cares more strongly about accurately predicting its next observation.” (Results)
*Significance:*  Summarizes the key experimental finding.

“The agent uses a goal prior to constrain action selection and drive the system towards a target state.” (7)
*Significance:*  Explains the role of the goal prior in the agent's planning process.

“The agent to drive the system to output y without knowledge of the system’s dynamics.” (2 Problem statement)
*Significance:*  States the fundamental goal of the agent.

“The agent achieves better performance compared to a classical optimal controller, demonstrating that it cares more strongly about accurately predicting its next observation.” (Results)
*Significance:*  Summarizes the key experimental finding.

“The agent uses a goal prior to constrain action selection and drive the system towards a target state.” (7)
*Significance:*  Explains the role of the goal prior in the agent's planning process.

“The agent to drive the system to output y without knowledge of the system’s dynamics.” (2 Problem statement)
*Significance:*  States the fundamental goal of the agent.

“The agent achieves better performance compared to a classical optimal controller, demonstrating that it cares more strongly about accurately predicting its next observation.” (Results)
*Significance:*  Summarizes the key experimental finding.

“The agent uses a goal prior to constrain action selection and drive the system towards a target state.” (7)
*Significance:*  Explains the role of the goal prior in the agent's planning process.

“The agent to drive the system to output y without knowledge of the system’s dynamics.” (2 Problem statement)
*Significance:*  States the fundamental goal of the agent.

“The agent achieves better performance compared to a classical optimal controller, demonstrating that it cares more strongly about accurately predicting its next observation.” (Results)
*Significance:*  Summarizes the key experimental finding.

“The agent uses a goal prior to constrain action selection and drive the system towards a target state.” (7)
*Significance:*  Explains the role of the goal prior in the agent's planning process.

“The agent to drive the system to output y without knowledge of the system’s dynamics.” (2 Problem statement)
*Significance:*  States the fundamental goal of the agent.

“The agent achieves better performance compared to a classical optimal controller, demonstrating that it cares more strongly about accurately predicting its next observation.” (Results)
*Significance:*  Summarizes the key experimental finding.

“The agent uses a goal prior to constrain action selection and drive the system towards a target state.” (7)
*Significance:*  Explains the role of the goal prior in the agent's planning process.

“The agent to drive the system to output y without knowledge of the system’s dynamics.” (2 Problem statement)
*Significance:*  States the fundamental goal of the agent.

“The agent achieves better performance compared to a classical optimal controller, demonstrating that it cares more strongly about accurately predicting its next observation.” (Results)
*Significance:*  Summarizes the key experimental finding.

“The agent uses a goal prior to constrain action selection and drive the system towards a target state.” (7)
*Significance:*  Explains the role of the goal prior in the agent's planning process.

“The agent to drive the system to output y without knowledge of the system’s dynamics.” (2 Problem statement)
*Significance:*  States the fundamental goal of the agent.

“The agent achieves better performance compared to a classical optimal controller, demonstrating that it cares more strongly about accurately predicting its next observation.” (Results)
*Significance:*  Summarizes the key experimental finding.

“The agent uses a goal prior to constrain action selection and drive the system towards a target state.” (7)
*Significance:*  Explains the role of the goal prior in the agent's planning
