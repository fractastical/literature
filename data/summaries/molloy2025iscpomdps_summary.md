# ISC-POMDPs: Partially Observed Markov Decision Processes with Initial-State Dependent Costs

**Authors:** Timothy L. Molloy

**Year:** 2025

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [molloy2025iscpomdps.pdf](../pdfs/molloy2025iscpomdps.pdf)

**Generated:** 2025-12-14 00:59:37

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

### ISC-POMDPs: Partially Observed Markov Decision Processes with Initial-State Dependent Costs - Summary

### OverviewThis paper introduces a class of partially observed Markov decision processes (POMDPs) – Initial-State Cost Partially Observed Markov Decision Processes (ISC-POMDPs) – that incorporate costs dependent on both the value and (future) uncertainty associated with initial states. The authors argue that this is necessary to address problems where controlling uncertainty about an initial state is a key objective, such as robot navigation, active sensing, and privacy-based applications. ISC-POMDPs enable the specification of objectives relative to a priori unknown initial states, which is useful in applications such as controlling a system to hinder inference of its initial state to preserve privacy in networked control systems, or the problem of controlling a system to improve inference of its initial state for active sensing and perception in target tracking and robotics. The authors state: "The key contribution of this paper is the introduction of ISC-POMDPs with costs that can depend on both the value and (future) uncertainty associated with initial states."### MethodologyThe ISC-POMDPs are formulated as POMDPs with augmented state processes consisting of both the original initial state and the current state. The authors define the augmented belief as the joint posterior pmf of the initial state and current state. The authors state: “The augmented state provides an invertible representation of the pair (X ,X ) in the sense that given (X ,X ), we can compute S via (8), and given S we can compute (X ,X )”. The authors define a cost function that depends on the value of the augmented state and the uncertainty associated with the initial state. The authors state: “The key contribution of this paper is the introduction of ISC-POMDPs with costs that can depend on both the value and (future) uncertainty associated with initial states.” The authors also introduce a recursive 

Bayesian fixed-point smoother to estimate the initial state that resembles the standard 

Bayesian filter
