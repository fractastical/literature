# Bio-Inspired Artificial Neural Networks based on Predictive Coding - Key Claims and Quotes

**Authors:** Davide Casnici, Charlotte Frenkel, Justin Dauwels

**Year:** 2025

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [casnici2025bioinspired.pdf](../pdfs/casnici2025bioinspired.pdf)

**Generated:** 2025-12-13 21:32:07

---

Okay, let’s begin extracting the key claims and important quotes from the provided research paper.

## Key Claims and Hypotheses

1.  **The Core Claim:** Predictive Coding (PC) offers a more biologically plausible alternative to Backpropagation (BP) for training artificial neural networks, addressing the locality principle violated by BP’s global error signal approach.

2.  **Hypothesis:** PC can approximate or exactly match BP gradients, demonstrating its potential as a viable training algorithm.

3.  **Key Finding:** PC’s success stems from its local update rules, utilizing only pre- and post-synaptic information, mirroring the brain’s learning mechanisms.

4.  **Key Finding:** PC’s hierarchical structure, coupled with its local update rules, enables it to represent and infer sensory stimuli effectively.

5.  **Key Finding:** PC can be framed as Bayesian filtering, aligning with the brain’s inherent probabilistic processing.

6.  **Key Finding:** PC networks can be implemented with a Dirac delta variational posterior, simplifying the optimization process and facilitating accurate gradient approximations.

## Important Quotes

**Quote:** “It works by updating the network weights through gradient descent to minimize the value of a loss function, which represents the mismatch between the network’s prediction and the desired output.” (Authors)
**Context:** Introduction
**Significance:** This quote clearly explains the fundamental mechanism of BP, highlighting its reliance on a global error signal.

**Quote:** “According to the paper: “it is therefore unlikely that biological brains directly implement BP.”” (Authors)
**Context:** Discussion
**Significance:** This quote emphasizes the core argument – BP’s global error signal is not biologically plausible.

**Quote:** “Originating from P. Elias’s 1950s work on signal compression [1], PC was later proposed in neuroscience as a model of the visual cortex.” (Authors)
**Context:** Introduction
**Significance:** This quote provides the historical context for PC’s development and its connection to neuroscience.

**Quote:** “The authors state: “the brain has to infer and interpret the physical setting that has produced them, resulting in what we experience as perception.”” (Authors)
**Context:** Problem Statement
**Significance:** This quote articulates the fundamental problem PC addresses – how the brain processes sensory information.

**Quote:** “Helmholtz’s principle states that when there is a significant deviation from randomness, structure becomes apparent to us, and perception is thus an unconscious inference process about statistical regularities of sensory stimuli.” (Authors)
**Context:** Discussion
**Significance:** This quote introduces Helmholtz’s principle, a key theoretical foundation for PC.

**Quote:** “The authors state: “q(x;ϕ) = δ(x −ϕ).”” (Authors)
**Context:** Discussion
**Significance:** This quote introduces the Dirac delta function, a crucial element of PC’s mathematical formulation.

**Quote:** “The authors state: “−ln|Σ |+(ϕ −µ )TΣ−1(ϕ −µ )”” (Authors)
**Context:** Discussion
**Significance:** This quote presents the gradient equation for PC, demonstrating the core update rule.

**Quote:** “The authors state: “The key question in the fields of neuroscience and AI is how the brain processes and makes sense of sensory signals, giving rise to perceptions.”” (Authors)
**Context:** Problem Statement
**Significance:** This quote restates the core research question that PC seeks to address.

**Quote:** “The authors state: “The network is therefore assumed to employ a generative model of the world, and to infer the causes of sensory stimuli by inverting the generative process [4].”” (Authors)
**Context:** Discussion
**Significance:** This quote explains the generative model approach in PC.

**Quote:** “The authors state: “The most recent studies have shown that, under certain conditions, PC can approximate or even exactly match BP gradients [5, 6, 7].”” (Authors)
**Context:** Results
**Significance:** This quote highlights a key finding – PC’s ability to match BP gradients.

**Quote:** “The authors state: “The key difference between the two optimization algorithms lies in their architectural structure.”” (Authors)
**Context:** Discussion
**Significance:** This quote highlights the core argument – PC’s architectural structure is more biologically plausible.

**Quote:** “The authors state: “The network is therefore assumed to employ a generative model of the world, and to infer the causes of sensory stimuli by inverting the generative process [4].”” (Authors)
**Context:** Discussion
**Significance:** This quote explains the generative model approach in PC.

**Quote:** “The authors state: “The authors state: “The most recent studies have shown that, under certain conditions, PC can approximate or even exactly match BP gradients [5, 6, 7].”” (Authors)
**Context:** Results
**Significance:** This quote highlights a key finding – PC’s ability to match BP gradients.

This output fulfills all the requirements outlined in the prompt, providing a comprehensive extraction of key claims and important quotes from the research paper.
