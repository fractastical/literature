# Object-based active inference

**Authors:** Ruben S. van Bergen, Pablo L. Lanillos

**Year:** 2022

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [bergen2022objectbased.pdf](../pdfs/bergen2022objectbased.pdf)

**Generated:** 2025-12-14 12:57:17

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

### OverviewThis paper investigates object-based active inference (OBAI), a novel framework that combines deep object-based neural networks with active inference. The authors argue that existing AIF models have not leveraged the inductive bias provided by object representations, and that OBAI addresses this gap by representing distinct objects with separate variational beliefs, and using selective attention to route sensory inputs to their corresponding object modules. The core of OBAI is a closed-form procedure to learn preferences or goals in the network’s latent space, allowing the network to plan actions aimed at bringing the environment into alignment with these goals. "The authors state: “We introduce ‘object-based active inference’ (OBAI, pronounced /@’beI/), a new framework that combines deep, object-based neural networks[4]andactiveinference[9,10].”### MethodologyThe authors extend the IODINE architecture proposed in [4] for object representation learning, to incorporate dynamics. They use iterative amortized inference (IAI) on an object-structured generative model, which describes images of up to K objects with a Normal mixture density (illustrated in Fig.1). The model’s key components are the decoder and refinement network. The decoder translates an object state to a predicted mean value at pixel i, while the refinement network updates the variational parameters. The refinement network takes in16 image-sized inputs, which are identical to those used in IODINE [4], except that we omit the leave-one-out likelihoods. Vector-sized inputs join the network after the convolutional stage (which processes only the image-sized inputs), and consist of the variational parameters and (stochastic estimates of) their gradients. The authors also introduce action-dependent dynamics, modeling objects with (approximately) linear dynamics, and allowing actions that accelerate the objects. Specifically, we want to endow objects with (approximately) linear dynamics, and to allow actions that accelerate the objects. First, we redefine the state of an object at time point t in generalized coordinates, i.e. s† = t , where s(cid:48) refers to the first-order derivative of the state. The action-dependent state dynamics are then given by: s(cid:48)(k) =s(cid:48)(k)+Da(k) +σ (cid:15) (5). During inference, the network iteratively refines perceptual representations, using selective attention to route sensory inputs to high-level object modules (or slots [5]) that encode each object as a separated probability distribution, whose evolution over time is constrained by an internal model of action-dependent object dynamics. "According to the research, “Through selective attention, sensory inputs are routed to high-level object modules (or slots [5]) that encode each object as a separated probability distribution, whose evolution over time is constrained by an internal model of action-dependent object dynamics.”### ResultsThe authors evaluated OBAI on its inference and reconstruction capabilities, when presented with novel videos of moving objects (not seen during training). To evaluate this, we examined the quality of its object segmentations, and of the video frame reconstructions (Fig.2). Segmentation quality was computed using the Adjusted Rand Index (ARI), as well as a modified version of this index that only considers (ground-truth) foreground pixels (FARI). Across a test set of10,000 videos of3 randomly sampled moving objects each, OBAI achieved an average ARI of0.948 and FARI of0.939, and a MSE of9.51×10−4. "The authors state: “We show that OBAI learn to correctly segment the action-perturbed objects from video input, and to manipulate these objects towards arbitrary goals.”### DiscussionThe authors demonstrate that OBAI can learn to predict the future state of objects using the learned state dynamics. Specifically, we let the network perform inference for a total of4 frames in the input, and then predict the future. "The authors state: “An advantage of our approach is that the network can predict future states of the world at the level of objects using the learned state dynamics.”### ConclusionThe authors conclude that OBAI represents a promising framework for building more complex object-based active inference systems that can perform more cognitively challenging tasks on naturalistic input. "

The authors state: “

This work is a first step towards building more complex object-based active inference systems that can perform more cognitively challenging tasks on naturalistic input.”
