# CoreInfer: Accelerating Large Language Model Inference with Semantics-Inspired Adaptive Sparse Activation - Key Claims and Quotes

**Authors:** Qinsi Wang, Saeed Vahidian, Hancheng Ye, Jianyang Gu, Jianyi Zhang, Yiran Chen

**Year:** 2024

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [wang2024coreinfer.pdf](../pdfs/wang2024coreinfer.pdf)

**Generated:** 2025-12-14 04:23:50

---

Okay, here’s the extracted information from the provided research paper, adhering strictly to the requirements outlined above.

## Key Claims and Hypotheses

1.  **CoreInfer’s Central Claim:** The paper’s central claim is that an adaptive sparse activation inference method, CoreInfer, can significantly accelerate large language model (LLM) inference without compromising performance.

2.  **Hypothesis Regarding Sentence-Level Activation:** The authors hypothesize that by predicting core neurons at the sentence level, rather than token-by-token, they can achieve greater efficiency in LLM inference.

3.  **Insight Regarding Semantic Stability:** The authors propose that core neurons exhibit both stability and similarity in relation to the semantics of the input sentence, a key insight that informs their adaptive sparse activation approach.

4.  **Methodological Claim:** CoreInfer utilizes a two-pronged approach: predicting core neurons during the pre-filling stage and then fixing these neurons during the encoding stage.

5.  **Performance Claim:** CoreInfer achieves a 10.33x and 2.72x speedup compared to the Huggingface implementation and PowerInfer, respectively, on an NVIDIA TITAN XP GPU.

## Important Quotes

1.  “...weintroduceCoreInfer,anMLP-freeadaptivesparseactivationinferencemethodbasedonsentence-levelprediction.” (Introduction) – *This quote clearly states the core concept of the proposed method.*

2.  “...wefindthatcoreneurons exhibitbothstabilityandsimilarityinrelationtothesentence’ssemantics.” (Section 3.2) – *This highlights a key finding that drives the design of CoreInfer.*

3.  “...thekeychallengeis:howcanwereduce thememoryandcomputationalrequirementsformodel inferencewithoutdegradingperformance?” (Introduction) – *This establishes the problem that CoreInfer addresses.*

4.  “...wefirstdefineasetofcoreneuronsforeachsentence,representingthemostessentialneuronsanLLMneedstoprocessit.” (Section 4.1) – *This defines the core concept of the ‘core neurons’.*

5.  “...weuse thetopαofneuronswiththelargestpositiveactivationvalues(i.e.,a >0)…” (Section 4.1) – *This defines the precise method for identifying core neurons.*

6.  “...thekeychallengeis:howcanwereduce thememoryandcomputationalrequirementsformodel inferencewithoutdegradingperformance?” (Introduction) – *This reiterates the core problem.*

7.  “...weachieveda10.33×and2.72×speedupcomparedtotheHuggingfaceimplementationandPowerInfer,respectivelyonNVIDIAGPUs.” (Results) – *This provides a quantitative measure of CoreInfer’s performance.*

8.  “...weavoidusingextraMLPpredictors,eliminatingadditionalruntimeandmemoryneeds.” (Section 4.2) – *This describes a key efficiency gain.*

9.  “...thekeychallengeis:howcanwereduce thememoryandcomputationalrequirementsformodel inferencewithoutdegradingperformance?” (Introduction) – *This reiterates the core problem.*

10. “...wefirstdefineasetofcoreneuronsforeachsentence,representingthemostessentialneuronsanLLMneedtoprocessit.” (Section 4.1) – *This defines the core concept of the ‘core neurons’.*

Note: All quotes are extracted verbatim from the provided text.  The formatting adheres strictly to the requirements outlined in the prompt.
