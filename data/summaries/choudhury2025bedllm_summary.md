# BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design

**Authors:** Deepro Choudhury, Sinead Williamson, Adam Goliński, Ning Miao, Freddie Bickford Smith, Michael Kirchhof, Yizhe Zhang, Tom Rainforth

**Year:** 2025

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [choudhury2025bedllm.pdf](../pdfs/choudhury2025bedllm.pdf)

**Generated:** 2025-12-14 01:12:28

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

### BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design – Summary

### OverviewThis paper investigates the application of Bayesian Experimental Design (BED) with Large Language Models (LLMs) to intelligently gather information. The authors propose BED-LLM, a novel approach that addresses the limitations of existing LLM-based information-gathering systems. The core idea is to iteratively select questions or queries that maximize the expected information gain (EIG) about the target quantity of interest, given the responses gathered previously. The paper demonstrates that BED-LLM achieves substantial performance gains across a wide range of test problems, including the20 Questions game and preference elicitation tasks.### MethodologyThe BED-LLM framework leverages the generative capabilities of LLMs while incorporating a rigorous experimental design methodology. The key components of the approach include: (1) formulating the problem as an EIG optimization problem; (2) estimating the EIG for each candidate question; (3) iteratively selecting the question that maximizes the EIG; and (4) updating the belief state based on the received responses. The authors employ a prior-likelihood pairing, where the joint distribution of the target quantity and the responses is modeled using an LLM. They also implement a filtering mechanism to ensure that the belief state remains consistent with the observed data. The experimental setup involves running the BED-LLM algorithm on two distinct problem sets: the20 Questions game and preference elicitation.### ResultsThe results of the experiments demonstrate that BED-LLM significantly outperforms existing baselines, including Naive and Split approaches. Specifically, BED-LLM achieves a5.8x gain in success rate on the20 Questions game when guessing celebrity names with a small model (Llama-3.1-8B). Furthermore, BED-LLM improves performance on preference elicitation, showing noticeable gains even when the LLM’s predictive model differs from the user’s response. The authors highlight the importance of maximizing the EIG and updating the belief state based on the received responses. The key findings are summarized as follows: (1) BED-LLM achieves substantial performance gains across a wide range of test problems; (2) BED-LLM’s success rate is more than double that of the Naive baseline; (3) BED-LLM’s performance is comparable to the Split baseline; (4) BED-LLM’s performance is robust to model mismatch; (5) BED-LLM’s performance is consistent across different LLMs.### Problem Formulation and BackgroundThe authors frame the problem of interactive information gathering as an experimental design problem, drawing inspiration from Bayesian experimental design. They argue that the key to effective information gathering with LLMs is to iteratively select questions that maximize the expected information gain (EIG) about the target quantity, given the responses gathered previously. The authors also discuss the challenges of designing effective experiments with LLMs, including the need to account for uncertainty in the LLM’s predictions and the need to avoid overfitting to the data. They highlight that existing approaches often fail to adequately address these challenges, leading to suboptimal performance. The authors also discuss the importance of defining a clear objective function for the experimental design process, which in this case is the EIG. They show how the EIG can be formulated as the expected value of the information gain, given the current state of knowledge.### Key FindingsThe authors identify several key findings from their work. First, they show that BED-LLM can significantly improve the performance of LLMs on information-gathering tasks. Second, they show that BED-LLM is a generalizable approach that can be applied to a wide range of tasks. Third, they show that BED-LLM is robust to model mismatch. Finally, they show that BED-LLM is computationally efficient.### ConclusionIn conclusion, this paper presents a novel approach for intelligent information gathering with LLMs. The BED-LLM framework provides a rigorous and principled way to design experiments with LLMs, leading to substantial performance gains across a wide range of tasks. The authors highlight the importance of maximizing the expected information gain and updating the belief state based on the received responses. 

The BED-LLM framework represents a significant step forward in the field of intelligent information gathering with LL

Ms.
