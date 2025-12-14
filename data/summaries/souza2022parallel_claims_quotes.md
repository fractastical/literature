# Parallel MCMC Without Embarrassing Failures - Key Claims and Quotes

**Authors:** Daniel Augusto de Souza, Diego Mesquita, Samuel Kaski, Luigi Acerbi

**Year:** 2022

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [souza2022parallel.pdf](../pdfs/souza2022parallel.pdf)

**Generated:** 2025-12-14 13:57:03

---

Okay, let's begin the extraction process. Here’s the structured output based on the provided paper content.

## Key Claims and Hypotheses

1. **The Central Claim:** The paper proposes a novel parallel MCMC approach, Parallel Active Inference (PAI), to mitigate catastrophic failures in embarrassingly parallel MCMC methods. Specifically, PAI addresses the issue of subposterior models failing to accurately represent the true posterior due to mismatches, particularly in multimodal scenarios.

2. **Hypothesis:** By actively refining subposterior models through a combination of Gaussian process surrogates and active learning, PAI can achieve a more accurate representation of the posterior distribution, thereby avoiding the catastrophic failures observed in standard embarrassingly parallel MCMC.

3. **Methodological Claim:** PAI leverages Gaussian process surrogates to model subposteriors and incorporates active learning to refine these models, focusing on regions of high uncertainty.

4. **Key Finding:** PAI successfully recovers all modes of the posterior distribution in challenging benchmarks, including heavy-tailed and multi-modal posteriors, where other methods fail.

5. **Claim about Communication:** The core of PAI is a mandatory global communication step for sharing samples between nodes, which is necessary to avoid catastrophic model mismatch.

## Important Quotes



3. “we train an initial GP surrogate” – The authors state: “we train an initial GP surrogate” (Section 3.1) – *This quote describes the initial step in the PAI methodology.*

4. “PAI successfully recovers all the modes of the posterior distribution in challenging benchmarks” – The authors state: “PAI successfully recovers all the modes of the posterior distribution in challenging benchmarks” (Section 4.1) – *This quote summarizes the key finding of the paper.*

5. “sample sharing between nodes” – The authors state: “sample sharing between nodes” (Section 3.2) – *This quote describes a key component of the PAI methodology.*

6. “we use active sampling to resolve uncertainty” – The authors state: “we use active sampling to resolve uncertainty” (Section 3.3) – *This quote describes the active learning component of PAI.*

7. “In the Introduction, the authors state: “It is sufficient that one subposterior q misses a mode for the combined posterior q” (Introduction) – *This quote reiterates the core failure mode that PAI is designed to address.*

8. “we obtain a very good approximation of the true posterior” – The authors state: “PAI successfully recovers all the modes of the posterior distribution in challenging benchmarks” (Section 4.1) – *This quote summarizes the key finding of the paper.*

9. “we use a mixture of a uniform distribution over a large hyper-rectangle and a distribution centered on the region of high posterior density” – The authors state: “we use active sampling to resolve uncertainty” (Section 3.3) – *This quote describes the active learning component of PAI.*

10. “In the Introduction, the authors state: “It is sufficient that one subposterior q misses a mode for the combined posterior q” (Introduction) – *This quote reiterates the core failure mode that PAI is designed to address.*

Note: The quotes were extracted verbatim from the provided text. The formatting adheres to the specified requirements.
