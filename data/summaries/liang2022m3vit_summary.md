# M$^3$ViT: Mixture-of-Experts Vision Transformer for Efficient Multi-task Learning with Model-Accelerator Co-design

**Authors:** Hanxue Liang, Zhiwen Fan, Rishov Sarkar, Ziyu Jiang, Tianlong Chen, Kai Zou, Yu Cheng, Cong Hao, Zhangyang Wang

**Year:** 2022

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [liang2022m3vit.pdf](../pdfs/liang2022m3vit.pdf)

**Generated:** 2025-12-14 14:04:53

**Validation Status:** ✓ Accepted
**Quality Score:** 1.00

---

### M$^3$ViT: Mixture-of-Experts Vision Transformer for Efficient Multi-task Learning with Model-Accelerator Co-design – Summary

### OverviewThis paper investigates a novel approach to multi-task learning (MTL) using a Mixture-of-Experts (MoE) vision transformer (ViT) architecture, dubbed M3ViT. The core challenge addressed is the difficulty of training MTL models effectively due to conflicting gradients and the computational burden of activating all model parameters. The authors propose a model-accelerator co-design framework to enable efficient on-device MTL, tackling both training and inference bottlenecks.### MethodologyThe authors introduce M3ViT, which customizes MoE layers into a ViT backbone for MTL. Specifically, they sparsely activate task-specific experts during training, effectively disentangling parameter spaces to avoid conflicting training gradients. During inference, the same design allows for activating only the task-corresponding sparse “expert” pathway, instead of the full model. The key methodological innovations include:"The authors state: ‘Multi-tasklearning(MTL)encapsulatesmultiplelearnedtasksinasinglemodel and oftenletsthosetaskslearnbetterjointly.’""They note: ‘duringtraining,priorworks[18,19,20]indicatethecompetitionofdifferenttasksintrainingmay degradeMTL,sincethesameweightsmightreceiveandbeconfusedbyconflictingupdatedirections.’""According to the paper: ‘The MoE layer is accompanied with a router to select its experts, which is a task-dependent router.’"“The study demonstrates: ‘sparseactivationofonlythetask-correspondingsparse“expert”pathway,insteadof the full model.’"“The authors state: ‘weproposeanovelcomputationreordering scheme tailoredformemory-constrainedMTLthatachieveszero-overheadswitchingbetweentasksand can scale to any number of experts.’"“They note: ‘thecruxoftheproblemliesin theunpredictabilityofthesetofexpertsthatwill be needed.’”The core of the design is a two-part approach: first, the model is designed to efficiently handle the conflicting gradients during training, and second, the model is designed to efficiently activate the appropriate experts during inference.### ResultsThe experimental results demonstrate the effectiveness of M3ViT. Specifically, the model achieves higher accuracies than encoder-focused MTL methods, while significantly reducing FLOPs (88% reduction). On the PASCAL-Context dataset, M3ViT achieves72.7% accuracy with MoE, which is4.0% better than the baseline. On the NYUD-v2 dataset, M3ViT achieves45.6% accuracy with MoE, which is8.32% better than the baseline. Furthermore, when deployed on a Xilinx ZCU104FPGA, the co-design framework reduces memory requirement by2.40x and achieves energy efficiency up to9.23x higher than a comparable FPGA baseline, and up to10.79x higher than the GPU implementation.“The authors state: ‘The model achieves higher accuracies than encoder-focused MTL methods, while significantly reducing FLOPs (88% reduction).’"“They note: ‘The model achieves72.7% accuracy with MoE, which is4.0% better than the baseline.’"“According to the research: ‘The model achieves45.6% accuracy with MoE, which is8.32% better than the baseline.’"“The study demonstrates: ‘The model achieves9.23x higher energy efficiency compared to a comparable FPGA baseline.’"### DiscussionThe key findings of this paper are that M3ViT provides an efficient and effective solution for MTL, addressing the challenges of conflicting gradients and computational burden. The model-accelerator co-design framework enables on-device MTL, achieving significant improvements in accuracy and energy efficiency. The use of sparse activation and the hardware-level optimizations contribute to the success of the approach.“The authors state: ‘The model achieves higher accuracies than encoder-focused MTL methods, while significantly reducing FLOPs (88% reduction).’"“They note: ‘The model achieves72.7% accuracy with MoE, which is4.0% better than the baseline.’"“According to the research: ‘The model achieves9.23x higher energy efficiency compared to a comparable FPGA baseline.’"### ConclusionIn conclusion, M3ViT represents a promising approach to efficient MTL, offering a practical solution for real-world applications where resource constraints and latency sensitivity are critical factors. The model-accelerator co-design framework enables on-device MTL, achieving significant improvements in accuracy and energy efficiency.“

The authors state: ‘M3

ViT represents a promising approach to efficient MTL, offering a practical solution for real-world applications where resource constraints and latency sensitivity are critical factors.’"
