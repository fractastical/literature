# Realising Synthetic Active Inference Agents, Part II: Variational Message Updates

**Authors:** Thijs van de Laar, Magnus Koudahl, Bert de Vries

**Year:** 2023

**Source:** arxiv

**Venue:** N/A

**DOI:** 10.1162/neco_a_01713

**PDF:** [laar2023realising.pdf](../pdfs/laar2023realising.pdf)

**Generated:** 2025-12-14 01:25:58

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

### OverviewThis paper investigates synthetic active inference agents using a variational message-passing approach. The authors present a scalable framework for constructing agents that can autonomously explore and exploit their environment, driven by a free-energy objective. The core contribution is a detailed analysis of the message-passing algorithm, demonstrating its ability to induce epistemic behaviour in the agents. The paper highlights the importance of constrained factor graphs for representing the generative model and provides a practical implementation of the algorithm.### MethodologyThe authors employ a variational message-passing (VMP) algorithm to solve the free-energy objective. The algorithm is implemented on a constrained factor graph (CFFG), which visually represents the relationships between the variables in the generative model. The CFFG allows for the efficient computation of the message updates, which are the core of the VMP algorithm. The authors use a Bethe free-energy approximation, which is a local approximation of the full free-energy. The algorithm is implemented in two phases: a forward pass, where the messages are computed from the observations to the latent states, and a backward pass, where the messages are computed from the latent states to the observations. The authors use a discrete-variable model for the T-maze simulation, which is a classic benchmark problem for active inference. The model consists of two facing nodes, one representing the perception and the other the control. The message passing algorithm is then applied to update the beliefs about the reward location.### ResultsThe simulation results demonstrate that the VMP algorithm can successfully induce epistemic behaviour in the agents. The agents learn to explore the T-maze and exploit the reward location. The authors show that the agents’ behaviour is consistent with the theoretical predictions of active inference. The authors also show that the VMP algorithm is scalable, as it can be applied to complex environments. The authors provide quantitative results, including the accuracy of the agents’ predictions and the efficiency of the algorithm. The authors show that the agents’ performance improves as the number of iterations increases. The authors also show that the VMP algorithm is robust to noise and uncertainty. The authors provide statistical analysis of the results, including confidence intervals and p-values. The results are presented in tables and figures. The authors demonstrate that the VMP algorithm can be used to solve complex problems in a scalable manner.### DiscussionThe authors discuss the implications of their findings for the development of synthetic active inference agents. They highlight the importance of the CFFG representation for modelling complex environments. They discuss the challenges of implementing VMP algorithms in practice. They discuss the limitations of the Bethe free-energy approximation. They discuss the potential applications of synthetic active inference agents in robotics, control, and decision-making. The authors argue that the VMP approach is a promising tool for building intelligent agents that can autonomously explore and exploit their environment. They suggest that future research should focus on developing more efficient and robust VMP algorithms. 

They also suggest that future research should explore the use of VMP in other domains, such as neuroscience and economics. 

The authors conclude that synthetic active inference agents have the potential to revolutionise the way we design and control intelligent systems.
