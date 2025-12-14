# Multi-Modal MPPI and Active Inference for Reactive Task and Motion Planning

**Authors:** Yuezhe Zhang, Corrado Pezzato, Elia Trevisan, Chadi Salmi, Carlos Hernández Corbato, Javier Alonso-Mora

**Year:** 2023

**Source:** arxiv

**Venue:** N/A

**DOI:** 10.1109/LRA.2024.3426183

**PDF:** [zhang2023multimodal.pdf](../pdfs/zhang2023multimodal.pdf)

**Generated:** 2025-12-14 01:43:08

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

=== IMPORTANT: ISOLATE THIS PAPER ===You are revising a summary for ONLY the paper below. Do NOT reference or use content from any other papers.Paper Title: Multi-Modal MPPI and Active Inference for Reactive Task and Motion PlanningCitation Key: zhang2023multimodalREMEMBER: Extract quotes, claims, and findings ONLY from the text provided below.Issues to fix:1. Too short:151 words (minimum200)Current draft:### OverviewThis summary of “Multi-Modal MPPI and Active Inference for Reactive Task and Motion Planning” synthesizes the paper’s key contributions, methods, and findings. The research addresses the challenge of robust task execution in dynamic environments by combining an Active Inference planner (AIP) with a Model Predictive Path Integral controller. This approach enables reactive action selection and low-level motion planning during task execution, allowing the system to adapt to unforeseen geometric constraints and disturbances.### MethodologyThe authors introduce a novel Multi-Modal MPPI (M3P2I) controller that samples in parallel different plan alternatives to achieve a goal. The AIP generates alternative symbolic plans, each linked to a cost function for M3P2I. The cost functions are evaluated by sampling control input sequences using importance sampling.The M3P2I controller then computes one coherent control input that minimizes the given costs.The AIP computes N alternative symbolic plans based on the current symbolic state and the available symbolic actions. 

The AIP computes N alternative symbolic plans based on the current symbolic state and the available symbolic actions. 

The AIP computes N alternative symbolic plans
