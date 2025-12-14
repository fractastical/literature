# Nemori: Self-Organizing Agent Memory Inspired by Cognitive Science

**Authors:** Jiayan Nan, Wenquan Ma, Wenlong Wu, Yize Chen

**Year:** 2025

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [nan2025nemori.pdf](../pdfs/nan2025nemori.pdf)

**Generated:** 2025-12-13 22:03:15

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

### OverviewThis paper introduces Nemori, a novel self-organizing memory architecture inspired by cognitive science, designed to address the limitations of existing Large Language Models (LLMs) in maintaining persistent memory across long contexts. The authors argue that current LLMs struggle due to their inability to effectively manage memory granularity and their reliance on passive, rule-based mechanisms. Nemori’s core innovation lies in its Two-Step Alignment Principle, which autonomously organizes conversational streams into semantically coherent episodes, and its Predict-Calibrate Principle, which actively learns from prediction gaps. Extensive experiments on the LoCoMo and LongMemEval S benchmarks demonstrate Nemori’s significant performance advantage, particularly in longer contexts.### MethodologyNemori’s methodology centers around a dual-pillar cognitive framework: the Two-Step Alignment Principle and the Predict-Calibrate Principle. The Two-Step Alignment Principle begins with Boundary Alignment, which autonomously organizes raw conversational streams into semantically coherent experience chunks. This is achieved by adapting and simplifying techniques from dialoguetopicsegmentation. Subsequently, the Representation Alignment sub-principle transforms these chunks into rich, narrative memories, simulating the natural human narration of episodic memory. The Predict-Calibrate Principle, a proactive learning mechanism inspired by the Free-energy Principle, addresses the second key challenge: organizing the memory itself. This principle operates in three stages: prediction, calibration, and distillation. First, the system predicts the content of the episode based on existing knowledge. Second, it calibrates the prediction against the actual episode content, identifying prediction gaps. Finally, it distills new knowledge statements from these gaps, refining its internal model. The system employs a unified vector-based retrieval mechanism to access both episodic and semantic memories, ensuring efficient knowledge access. The experiments were conducted using the LoCoMo and LongMemEval S benchmarks, with the authors utilizinggpt-4o-mini andgpt-4.1-mini as the evaluation models.### ResultsNemori’s performance on the LoCoMo dataset significantly outperforms existing state-of-the-art systems, achieving an overall LLMscore of0.744, compared to the FullContext baseline’s0.723. On the LongMemEval S dataset, Nemori demonstrates a substantial advantage, particularly in longer contexts. Specifically, the authors report that Nemori achieves an average LLMscore of0.794 withgpt-4.1-mini, surpassing the baseline’s0.806. The authors also highlight that Nemori’s use of significantly fewer tokens (88% less) compared to the FullContext baseline underscores its efficiency. Furthermore, the results on the LoCoMo dataset reveal that Nemori’s Two-Step Alignment Principle and Predict-Calibrate Principle contribute to its superior performance, particularly in tasks requiring temporal reasoning. The authors quantify this advantage, noting that Nemori’s performance on single-session-preference tasks is6.7% higher than the FullContext baseline. The study demonstrates that Nemori’s architecture effectively addresses the challenges of long-context memory management, leading to a substantial improvement in overall performance.### DiscussionThe authors’ findings underscore the critical role of self-organization in enabling LLMs to effectively manage long-term conversational memory. Nemori’s dual-pillar approach, combining structured episode representation with proactive knowledge distillation, represents a significant step forward in addressing the limitations of existing LLMs. The Two-Step Alignment Principle’s ability to autonomously organize conversational streams into semantically coherent episodes, coupled with the Predict-Calibrate Principle’s proactive learning mechanism, allows Nemori to learn from prediction gaps and refine its internal model. The results demonstrate that Nemori’s architecture is particularly effective in longer contexts, where traditional LLMs struggle due to their limited memory capacity. The authors’ findings highlight the importance of cognitive principles in designing intelligent agents and suggest that self-organizing memory architectures are essential for achieving genuine, human-like learning and self-evolution in LLMs. 

The study’s emphasis on efficiency, with 

Nemori utilizing88% fewer tokens, further strengthens its practical value and scalability.
