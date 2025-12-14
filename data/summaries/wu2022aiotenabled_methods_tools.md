# An AIoT-enabled Autonomous Dementia Monitoring System - Methods and Tools Analysis

**Authors:** Xingyu Wu, Jinyang Li

**Year:** 2022

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [wu2022aiotenabled.pdf](../pdfs/wu2022aiotenabled.pdf)

**Generated:** 2025-12-14 14:02:32

---

## Algorithms and Methodologies

*   Random Forest (exact quote from paper) – "Random Forest (RF) [11] because of its high accuracy, flexibility (suitable for different data distributions), interpretability, and low running time complexity."
*   Long Short-Term Memory (LSTM) (exact quote from paper) – "Long Short-Term Memory (LSTM) [13] uses gate control to keep the useful past states and abandon the useless ones."
*   Gradient Descent (exact quote from paper) – "Gradient Descent" – mentioned in the context of training the RF model.
*   Mutual Information (exact quote from paper) – "MI(S ,S )= ∂(S ,S ) (1)" – used for sensor weighting.
*   Gini Index (exact quote from paper) – "Gini Index" – used in the RF decision tree construction.
*   Bayes’ Theorem (exact quote from paper) – “Bayes’ Theorem” – implied in the activity inference process.
*   Z-score (exact quote from paper) – "Z-score, a popular statistical method for abnormal data detection" – used for abnormal activity detection.
*   Active Inference (exact quote from paper) – “Active Inference” – the underlying principle guiding the system’s behavior.

## Software Frameworks and Libraries

*   PyTorch (exact quote from paper) – "PyTorch version 1.8.0"
*   scikit-learn (exact quote from paper) – "scikit-learn" – used for RF model training.
*   NumPy (exact quote from paper) – "NumPy" – used for numerical computation.
*   Pandas (exact quote from paper) – "Pandas" – used for data manipulation.
*   MATLAB (exact quote from paper) – "MATLAB" – mentioned in the context of data analysis.
*   IBM NodeRED (exact quote from paper) – "NodeRED on IBM" – used for system architecture.
*   Python within Watson Studio (exact quote from paper) – "Python within Watson Studio" – used for data analysis and model training.

## Datasets

*   CASAS dataset (exact quote from paper) – "CASAS [1] dataset, collected in a smart home environment" – used for training and testing the system.
*   The dataset contains the recordings uploaded from several sensors that were deployed in a flat with two residents, for a period of about 3 months.

## Evaluation Metrics

*   Accuracy (exact quote from paper) – "accuracy of 99.13% in activity recognition and 94.29% in the detection of abnormal activity"
*   F1-score (exact quote from paper) – "F1-score, and AUCallmaintainaweightedaveragevaluehigherthan99%."
*   AUC (Area Under the Curve) (exact quote from paper) – “AUC value of 0.97”
*   t-tests (exact quote from paper) – "statistical tests (t-tests, ANOVA, etc.) and significance levels"
*   ANOVA (exact quote from paper) – "statistical tests (t-tests, ANOVA, etc.) and significance levels"

## Software Tools and Platforms

*   Google Colab (exact quote from paper) – "Google Colab" – used for model training.
*   AWS (exact quote from paper) – "AWS" – mentioned in the context of cloud computing.
*   Local clusters (exact quote from paper) – "local clusters" – used for model training.

Not specified in paper – No other tools or platforms are explicitly mentioned.
