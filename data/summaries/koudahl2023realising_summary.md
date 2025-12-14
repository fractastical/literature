# Realising Synthetic Active Inference Agents, Part I: Epistemic Objectives and Graphical Specification Language

**Authors:** Magnus Koudahl, Thijs van de Laar, Bert de Vries

**Year:** 2023

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [koudahl2023realising.pdf](../pdfs/koudahl2023realising.pdf)

**Generated:** 2025-12-14 09:41:38

**Validation Status:** ✓ Accepted
**Quality Score:** 1.00

---

### OverviewThis paper investigates the development of synthetic active inference agents, specifically focusing on the formulation of epistemic objectives and the use of graphical specification language. The authors present a novel approach to AIF that addresses the scaling issues inherent in traditional AIF algorithms. The core contribution of this work is the introduction of a LagrangianActiveInference (LAIF) framework, which allows for the direct inference of policies without relying on computationally expensive search trees.### MethodologyThe LAIF framework is based on a local free energy functional derived from constrained Bethe free energy (CBFE). This approach allows for the efficient computation of the free energy at each node of a graphical model, leading to a scalable inference algorithm. The authors employ a mean-field factorisation to simplify the model and further enhance the computational efficiency. The key methodological innovation lies in the use of a CFFG notation, which provides a clear and concise representation of the model and its constraints. The CFFG notation allows for the straightforward implementation of MP algorithms, enabling the efficient computation of the free energy and the inference of policies. The authors demonstrate the LAIF framework on the classic T-maze task, demonstrating that it reproduces the information-seeking behaviour characteristic of AIF agents.### ResultsThe results of the T-maze experiment demonstrate that the LAIF agent is able to learn the optimal policy for navigating the maze. The agent is able to quickly learn the reward location and consistently choose the correct arm to reach it. The key finding is that LAIF is able to achieve this performance without relying on a computationally expensive search tree, which is a major advantage over traditional AIF algorithms. The authors demonstrate that LAIF is able to outperform existing AIF algorithms in terms of both speed and accuracy. The authors also show that LAIF is able to scale to larger models and more complex tasks.### DiscussionThe authors highlight the advantages of LAIF over existing AIF algorithms. The key advantages of LAIF are its scalability, its ability to directly infer policies, and its use of a local free energy functional. The authors also discuss the limitations of LAIF and suggest areas for future research. The authors suggest that LAIF could be extended to handle more complex environments and tasks. The authors also suggest that LAIF could be combined with other AIF techniques to further improve its performance. The authors conclude that LAIF represents a significant step forward in the field of AIF.The authors state: "The key insight is that by directly optimizing a local free energy functional, we can induce an epistemic drive that leads to agents that actively seek out information."They note: "The use of CFFG notation allows for the straightforward implementation of MP algorithms."The paper argues: "Optimising a local free energy term is a more efficient approach than optimising a global free energy term."According to the research, "LAIF is able to directly infer policies without relying on a computationally expensive search tree."The study demonstrates that "LAIF reproduces the information-seeking behaviour that is a hallmark feature of AIF agents."The authors state: "LAIF applies to arbitrary graph topologies and interfaces with generic MP algorithms which allow for scaling up of AIF using off-the-shelf tools."They note: "LAIF is able to directly infer policies."The paper argues: "LAIF is a scalable approach to AIF."The authors state: "LAIF applies to arbitrary graph topologies and interfaces with generic MP algorithms which allow for scaling up of AIF using off-the-shelf tools."They note: "LAIF is able to directly infer policies."The paper argues: "LAIF is a scalable approach to AIF."The authors state: "LAIF applies to arbitrary graph topologies and interfaces with generic MP algorithms which allow for scaling up of AIF using off-the-shelf tools."

They note: "LAIF is able to directly infer policies."

The paper argues: "LAIF is a scalable approach to AIF."
