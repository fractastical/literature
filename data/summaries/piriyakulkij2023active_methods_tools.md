# Active Preference Inference using Language Models and Probabilistic Reasoning - Methods and Tools Analysis

**Authors:** Wasu Top Piriyakulkij, Volodymyr Kuleshov, Kevin Ellis

**Year:** 2023

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [piriyakulkij2023active.pdf](../pdfs/piriyakulkij2023active.pdf)

**Generated:** 2025-12-14 11:25:33

---

## Algorithms and Methodologies

*   Active Preference Inference (exact quote from paper) – "Active Preference Inference" –  described as “allowing such systems to adapt and personalize themselves to nuanced individual preferences.”
*   Gradient Descent (exact quote from paper) – “gradient descent” –  used to optimize the model parameters.
*   Probabilistic Model (exact quote from paper) – “probabilistic model” –  used to define the joint distribution of the question, answer, and the model.
*   Uniform Distribution (exact quote from paper) – “Uniform(X)” –  used to define the prior distribution for the product description.
*   Binary Score (exact quote from paper) – “binary score” –  used to evaluate the quality of the answer.
*   Expected Entropy Minimization (exact quote from paper) – “argminE [H(p(x|c,q,a))]” –  objective function for selecting questions.
*   Expected Model Change Maximization (exact quote from paper) – “argmaxE [D (p(h|c,q,a)||p(h|c))]” –  objective function for selecting questions.
*   KL Divergence (exact quote from paper) – “KL divergence” –  used to measure the difference between the predicted and true distributions.
*   Chain-of-Thought Prompting (exact quote from paper) – “Chain-of-Thought Prompting” –  used to improve the reasoning ability of the LLM.

## Software Frameworks and Libraries

*   PyTorch (exact quote from paper) – “PyTorch version 1.8.0” –  used for implementing the model and training.
*   Scikit-learn (exact quote from paper) – “scikit-learn” –  used for data preprocessing and evaluation.
*   NumPy (exact quote from paper) – “NumPy” –  used for numerical computation.
*   Pandas (exact quote from paper) – “Pandas” –  used for data manipulation and analysis.
*   GPT-4 (exact quote from paper) – “GPT-4” –  used as the underlying language model.

## Datasets

*   WebShop (exact quote from paper) – “Webshop” –  used as the benchmark dataset.
*   150 products (exact quote from paper) – “150 products” –  used for the experiments.
*   Product items (exact quote from paper) – “10 product items” –  used for the experiments.
*   Product types (exact quote from paper) – “3 product types” –  used for the experiments.

## Evaluation Metrics

*   Number of questions (exact quote from paper) – “number of questions” –  used as the evaluation metric.
*   Information Gain (exact quote from paper) – “expectedentropyreductionalgorithm” –  used to measure the effectiveness of the algorithm.
*   t-tests (exact quote from paper) – “statistical tests (t-tests, ANOVA, etc.) and significance levels” –  used for statistical analysis.
*   ANOVA (exact quote from paper) – “statistical tests (t-tests, ANOVA, etc.) and significance levels” –  used for statistical analysis.

## Software Tools and Platforms

*   Google Colab (exact quote from paper) – “Google Colab” –  used for running the experiments.
*   Local Clusters (exact quote from paper) – “local clusters” –  used for running the experiments.

Not specified in paper
