# Discovering Novel Actions from Open World Egocentric Videos with Object-Grounded Visual Commonsense Reasoning

**Authors:** Sanjoy Kundu, Shubham Trehan, Sathyanarayanan N. Aakur

**Year:** 2023

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [kundu2023discovering.pdf](../pdfs/kundu2023discovering.pdf)

**Generated:** 2025-12-14 11:35:10

**Validation Status:** ✓ Accepted
**Quality Score:** 1.00

---

### Discovering Novel Actions from Open World Egocentric Videos with Object-Grounded Visual Commonsense Reasoning – Summary

### OverviewThis paper investigates discovering novel actions from open-world egocentric videos using a neuro-symbolic framework called ALGO. The authors propose a two-step process: first, grounding objects in the video through evidence-based reasoning using CLIP, and second, discovering plausible activities driven by prior commonsense knowledge and an energy-based symbolic pattern theory framework. The goal is to enable autonomous systems to understand and interpret visual data without explicit supervision.### MethodologyThe core of ALGO is a neuro-symbolic framework that combines the strengths of deep learning (CLIP) and symbolic reasoning (ConceptNet). The system employs a two-step process: (1) object grounding, where CLIP is used to identify objects in the video, and (2) activity discovery, where an energy-based symbolic pattern theory framework is used to infer activities based on the grounded objects and prior knowledge. The system uses a multi-layered approach, combining CLIP for visual feature extraction with a symbolic knowledge base (ConceptNet) to provide context and constraints. The authors use a two-stream convolutional network to extract features from the video and a graph-based representation to model the relationships between objects and actions. The system employs an energy-based framework to represent the activity space, with nodes representing possible activities and edges representing the relationships between them. The system uses a Markov Chain Monte Carlo (MCMC) algorithm to explore the activity space and find the most likely activity.### Key Claims and FindingsThe authors state: "Humans display a remarkable ability to recognize unseen concepts (actions, objects, etc.) by associating known concepts gained through prior experience and reasoning over their attributes." They note: "In this work, we aim to develop a computational framework that tackles open-world activity understanding." The authors claim: "The open-world learning paradigm is an effective inference mechanism to distill commonsense knowledge from symbolic knowledge bases." The paper demonstrates that ALGO achieves competitive performance on the Charades-Ego dataset, achieving an accuracy of16.8% on unseen actions. The authors report that the system achieves a match accuracy of1.8 on the Gaze dataset and3.5 on the Gaze+ dataset. The paper shows that the system can learn to recognize actions with no labels, and that VLMs can benefit from ALGO. The authors report that the system achieves a match accuracy of0.9 on the Gaze dataset and4.1 on the Gaze+ dataset.### ResultsThe paper demonstrates that ALGO achieves competitive performance on the Charades-Ego dataset, achieving an accuracy of16.8% on unseen actions. The authors report that the system achieves a match accuracy of0.9 on the Gaze dataset and4.1 on the Gaze+ dataset.### DiscussionThe authors highlight the importance of grounding objects and using prior knowledge to understand activities. They emphasize that the combination of deep learning and symbolic reasoning is a promising approach for open-world activity understanding. The authors report that the system achieves a match accuracy of0.9 on the Gaze dataset and4.1 on the Gaze+ dataset.### ConclusionThe authors conclude that ALGO is a promising framework for open-world activity understanding. The system's ability to learn to recognize actions with no labels and its competitive performance on benchmark datasets demonstrate the potential of this approach. 

The authors state: "

The open-world learning paradigm is an effective inference mechanism to distill commonsense knowledge from symbolic knowledge bases."
