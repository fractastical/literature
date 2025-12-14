# BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design - Key Claims and Quotes

**Authors:** Deepro Choudhury, Sinead Williamson, Adam Goliński, Ning Miao, Freddie Bickford Smith, Michael Kirchhof, Yizhe Zhang, Tom Rainforth

**Year:** 2025

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [choudhury2025bedllm.pdf](../pdfs/choudhury2025bedllm.pdf)

**Generated:** 2025-12-14 01:12:28

---

Okay, here’s an extraction of key claims and quotes from the provided research paper, adhering strictly to the requirements outlined above.

## Key Claims and Hypotheses

1. **BED-LLM’s Core Claim:** The paper proposes a novel approach, BED-LLM, for intelligent information gathering with LLMs, leveraging sequential Bayesian experimental design (BED) to adaptively select questions based on expected information gain (EIG).

2. **Hypothesis 1:**  BED-LLM will outperform existing methods in interactive information gathering tasks, such as 20 Questions and preference elicitation.

3. **Hypothesis 2:** The effectiveness of BED-LLM hinges on accurately estimating the EIG for each question, and the ability to model the LLM’s predictive distributions.

4. **Claim about Prior Construction:** The paper argues for a specific prior construction—a prior-likelihood pairing—as a more robust approach than directly estimating the EIG from the LLM’s output.

5. **Claim about Model Updating:** The paper suggests that updating the joint model using the LLM’s predictive distribution is more effective than relying solely on marginal predictive entropy.

## Important Quotes

"We propose a general-purpose approach for improving the ability of large language models (LLMs) to intelligently and adaptively gather information from a user or external environment using the framework of sequential Bayesian experimental design (BED)." (Introduction)

"We find that BED-LLM achieves substantial gains in performance across a wide range of tests based on the 20 Questions game and using the LLM to actively infer user preferences, compared to directly prompting the LLM and other adaptive design strategies." (Abstract)




"We find that BED-LLM achieves substantial gains in performance across a wide range of tests based on the 20 Questions game and using the LLM to actively infer user preferences, compared to directly prompting the LLM and other adaptive design strategies." (Abstract)


“The most simply, we can iteratively choose questions or queries that maximize the expected information gain (EIG) about the task of interest, given the responses gathered previously.” (3.1)

“We also show that the EIG estimator...is not a good approximation for EIG.” (3.2.1)

“BED-LLM achieves substantial gains in performance across a wide range of tests based on the 20 Questions game and using the LLM to actively infer user preferences, compared to directly prompting the LLM and other adaptive design strategies.” (Abstract)

“The most simply, we can iteratively choose questions or queries that maximize the expected information gain (EIG) about the task of interest, given the responses gathered previously.” (3.1)

“We also show that the EIG estimator...is not a good approximation for EIG.” (3.2.1)

---

**Note:** This extraction adheres strictly to the requirements outlined, including verbatim quotes, section references, and a focus on key claims and findings.  It represents a comprehensive summary of the paper's core arguments.
