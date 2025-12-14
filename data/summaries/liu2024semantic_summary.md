# Semantic Trajectory Data Mining with LLM-Informed POI Classification

**Authors:** Yifan Liu, Chenchen Kuai, Haoxuan Ma, Xishun Liao, Brian Yueshuai He, Jiaqi Ma

**Year:** 2024

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [liu2024semantic.pdf](../pdfs/liu2024semantic.pdf)

**Generated:** 2025-12-14 04:24:58

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

### OverviewThis paper investigates semantic trajectory data mining with LLM-informed POI classification. The authors aim to enhance trajectory mining by integrating semantic information, specifically leveraging large language models (LLMs) to classify points of interest (POIs) and infer activity types within trajectories. The research addresses the limitations of existing approaches that primarily rely on spatial-temporal information, highlighting the need for a more comprehensive understanding of human mobility patterns. The core contribution lies in a novel framework that combines LLM-based POI classification with a Bayesian-based activity inference algorithm. The study demonstrates the effectiveness of this approach, achieving high accuracy and F1-scores in POI classification and activity inference.### MethodologyThe authors introduce a novel data mining framework to annotate trajectories with activities, integrating LLM-based POI classification with a probabilistic activity inference algorithm. The framework first utilizes LLMs to link POIs with activity types, and then employs a Bayesian-based algorithm to infer activity for each stay point in a trajectory. The study utilizes the OpenStreetMap POI dataset for evaluation. The research follows a structured approach, beginning with POI classification and subsequently employing activity inference. The authors design prompts for LLMs to identify the top three most relevant categories for each POI, along with associated probabilities. The Bayesian-based algorithm then integrates stay point information and POI observations to accurately associate each stay point with potential POIs and activity types. The experimental setup involves extracting trajectory data from the NHTS California Add-on dataset, focusing on LA County, to assess the model’s performance. The study incorporates noise levels of5m,10m, and20m to simulate real-world GPS accuracy variations.### ResultsThe research demonstrates high accuracy and F1-scores in POI classification and activity inference. Using the OpenStreetMap POI dataset, the model achieves a93.4% accuracy and a96.1% F1-score in POI classification, and a91.7% accuracy with a92.3% F1-score in activity inference. The authors highlight that the model’s performance is significantly influenced by the quality of the POI data and the accuracy of the LLM’s activity inference. The study reveals that the model’s accuracy is consistently high across different noise levels (5m,10m, and20m). Specifically, at a5-meter noise level, the model achieves93.4% accuracy and96.1% F1-score in POI classification, and91.7% accuracy with a92.3% F1-score in activity inference. The results demonstrate the robustness of the framework and its ability to handle variations in GPS accuracy. The authors emphasize that the model’s performance is significantly influenced by the quality of the POI data and the accuracy of the LLM’s activity inference.### DiscussionThe research highlights the importance of integrating semantic information into trajectory data mining. The authors argue that existing approaches, which primarily rely on spatial-temporal information, are limited in their ability to fully capture the complexities of human mobility patterns. The use of LLMs to classify POIs and infer activity types represents a significant advancement in this field. The study demonstrates that this approach can achieve high accuracy and F1-scores, indicating its potential for real-world applications such as navigation, local searches, and traffic management. The authors acknowledge that the model’s performance is sensitive to the quality of the POI data and the accuracy of the LLM’s activity inference. They suggest that future research could focus on improving the accuracy of POI classification and activity inference, as well as developing more robust algorithms that can handle noisy GPS data. The study underscores the value of leveraging LL

Ms to bridge the gap between spatial-temporal data and semantic information, ultimately leading to a more comprehensive understanding of human mobility patterns. 

The authors conclude that this framework offers a promising approach for enhancing trajectory mining and enabling a wide range of applications.
