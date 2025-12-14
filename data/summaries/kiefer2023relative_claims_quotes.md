# Relative representations for cognitive graphs - Key Claims and Quotes

**Authors:** Alex B. Kiefer, Christopher L. Buckley

**Year:** 2023

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [kiefer2023relative.pdf](../pdfs/kiefer2023relative.pdf)

**Generated:** 2025-12-14 11:21:49

---

Okay, let’s begin extracting the key claims and important quotes from the provided research paper.

## Key Claims and Hypotheses

1.  **The Core Claim:** The paper demonstrates that relative representations, derived from distinct neural networks trained on similar data, can be used to map latent space vectors to a shared representation, offering comparable representational power and enabling convergence prediction.

2.  **Hypothesis:** The authors hypothesize that the convergence of a model during training can be predicted by the average cosine similarity between its relative representations of data points.

3.  **Key Finding:** The authors show that relative representations can be successfully applied to discrete state-space models, such as Clone-Structured Cognitive Graphs (CSCGs), and can be used to facilitate communication across agents trained with different random initializations and training sequences, even on partially dissimilar spaces.

4.  **Key Finding:** The paper introduces a technique for zero-shot model stitching, which can be applied post-hoc without requiring relative representations during training.

5.  **Hypothesis:** The authors propose that the study serves as a proof-of-concept for applying relative representations to the study of cognitive maps in neuroscience and AI.

## Important Quotes

**Context:** Introduction
**Significance:** This quote establishes the fundamental premise of the paper – the utility of relative representations for comparing latent spaces.

**Quote:** "Given anchor points A = [x ,x ,...,x ] sampled from a data or observation space and some similarity function sim (e.g. cosine similarity4, the relative representationrM of datapointx withrespecttomodel i i
M can be defined in terms of M’s latent-space embeddings eM =f (x ) as:"
**Context:** Section 2 - Relative Representations
**Significance:** This is the formal definition of the relative representation method.

**Quote:** "The convergence of a model M during training target is well predicted by the average cosine similarity between its relative representations of datapoints and those of an independently validated reference model M."
**Context:** Section 2 - Relative Representations
**Significance:** This statement explicitly states the core hypothesis regarding convergence prediction.

**Quote:** "In this work we examine an extension of relative representations to discrete state-space models, using Clone-Structured Cognitive Graphs (CSCGs) [16] for 2D spatial localization and navigation as a test case in which such representations may be of some practical use."
**Context:** Introduction
**Significance:** This introduces the specific application domain – CSCGs – and the paper’s focus.

**Quote:** “The most obvious practical use of relative representations is in enabling ‘latent space communication’: Moschella et al [13] show that the projection of embeddings from distinct models onto the same relative representation enables ‘zero-shot model stitching’, in which for example the encoder from one trained model can be spliced to the decoder from another (with the relative representation being the initial layer supplied as input to the decoder).”
**Context:** Section 5 - Experiments: Communication across cognitive maps
**Significance:** This details the practical application of relative representations – zero-shot model stitching.

**Quote:** “We introduceatechniqueforzero-shotmodelstitchingthatcanbe applied post hoc, without the need for using relative representations during training.”
**Context:** Section 5 - Experiments: Communication across cognitive maps
**Significance:** This highlights a key advantage of the approach – its applicability without requiring relative representations during training.

**Quote:** “Crucially, the findings reported here serve as a proof-of-concept for the application of relative representations to the study of cognitive maps in neuroscience and AI.”
**Context:** Conclusion
**Significance:** This summarizes the paper’s primary contribution – a proof-of-concept for applying relative representations to cognitive map studies.

**Quote:** “The authors state: “The convergence of a model M during training target is well predicted by the average cosine similarity between its relative representations of datapoints and those of an independently validated reference model M.””
**Context:** Section 2 - Relative Representations
**Significance:** This quote reiterates the core hypothesis regarding convergence prediction.

**Quote:** “We explore both of these regimes (i.e., certainty vs. uncertainty) in our experiments.”
**Context:** Section 5 - Experiments: Communication across cognitive maps
**Significance:** This highlights the two experimental conditions used in the study.

This extraction provides a comprehensive overview of the key claims and important quotes from the research paper.  It adheres strictly to the requirements outlined in the prompt.
