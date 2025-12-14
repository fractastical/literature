# Learning Generative Models for Active Inference using Tensor Networks

**Authors:** Samuel T. Wauthier, Bram Vanhecke, Tim Verbelen, Bart Dhoedt

**Year:** 2022

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [wauthier2022learning.pdf](../pdfs/wauthier2022learning.pdf)

**Generated:** 2025-12-14 12:55:46

**Validation Status:** ✓ Accepted
**Quality Score:** 1.00

---

### OverviewThis paper investigates learning generative models for active inference using tensor networks. The authors state: “An active inference agent will attempt to minimize its variational free energy, defined in terms of beliefs over observations, internal states and policies.” They note: “Tensornetworks,asopposedtoneuralnetworks,arenetworksconstructedout ofcontractionsbetweentensors.” The paper argues: “The ability of tensor networks to represent the probabilistic nature of quantum states as well as to reduce large state spaces makes tensor networks a natural candidate for active inference. We show how tensor networks can be used as a generative model for sequential data. Furthermore, we show how one can obtain beliefs from such a generative model and how an active inference agent can use these to compute the expected free energy. Finally, we demonstrate our method on the classic T-maze environment.”### MethodologyThe authors describe a novel approach to learning state spaces, likelihood and transition dynamics using tensor networks. They explain: “A generative model is a statistical model of the joint probability P(X) of a set of variables X = (X ,X ,...,X ).” They further state: “Each tensor is contracted with the other tensors to form the tensor B(i,i+1). The update to B(i,i+1) is then computed using the loss function:” They note: “The singular value decomposition (SVD) is used to decompose the contracted tensor.” They explain: “The MPS (matrix product state) is a tensor network that can be used to represent a quantum state.” They state: “The ability of tensor networks to represent the probabilistic nature of quantum states as well as to reduce large state spaces makes tensor networks a natural candidate for active inference. Finally, we demonstrate our method on the classic T-maze environment.”### ResultsThe authors report: “The data set was constructed by including one of every possible path through the maze, i.e.202 sequences of actions and observations. The model was trained over500epochswithabatchsizeof10,whereoneepochconsistedofoneright-to-left-to-right sweep per batch. The learning rate was set to10−4 and was further reduced by10 % whenever the loss increased too much (i.e. by more than0.5). Additionally, bonds started with8 dimensions. The singular value cutoff point was set to10 % of the largest singular value.” They state: “The authors state: "X". They further note: "Y". The paper argues: "Z". The study demonstrates: "we show how tensor networks can be used as a generative model for sequential data. Finally, we demonstrate our method on the classic T-maze environment.”### DiscussionThe authors’ findings highlight the potential of tensor networks for active inference. They state: “The authors state: "X". Finally, we demonstrate our method on the classic T-maze environment.”### ConclusionThis paper introduced a generative model based on tensor networks that is able to learn from sequential data. In addition, we showed how one can obtain beliefs from such a generative model and how a (sophisticated) active inference agent can use these to compute the expected free energy. Demonstration on the T-maze environment pointed out that such an agent is able to correctly select actions.### AcknowledgmentsThis research received funding from the Flemish Government under the “OnderzoeksprogrammaArtificieëleIntelligentie(AI)Vlaanderen” programme.Thiswork has received support from the European Union’s Horizon2020 program through Grant 

No.863476 (ERC-

CoG SEQUAM).
