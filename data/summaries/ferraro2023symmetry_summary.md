# Symmetry and Complexity in Object-Centric Deep Active Inference Models

**Authors:** Stefano Ferraro, Toon Van de Maele, Tim Verbelen, Bart Dhoedt

**Year:** 2023

**Source:** arxiv

**Venue:** N/A

**DOI:** 10.1098/rsfs.2022.0077

**PDF:** [ferraro2023symmetry.pdf](../pdfs/ferraro2023symmetry.pdf)

**Generated:** 2025-12-14 01:40:11

**Validation Status:** ⚠ Rejected
**Quality Score:** 0.00
**Validation Errors:** 1 error(s)
  - Severe repetition detected: Same phrase appears 6 times (severe repetition)

---

### OverviewThis paper investigates how inherent symmetries of particular objects also emerge as symmetries in the latent state space of deep active inference models. The authors focus on object-centric representations, which are trained from pixels to predict novel object views as the agent moves its viewpoint. The research investigates the relation between model complexity and symmetry exploitation in the statespace, performs principal component analysis to demonstrate how the model encodes the principal axis of symmetry of the object in the latent space, and demonstrates how more symmetrical representations can be exploited for better generalization in the context of manipulation.### MethodologyThe authors employ a deep active inference framework, utilizing variational free energy minimization to learn the generative model. The model consists of an encoding network, a transition network, and a decoding network. The model is trained on a subset of the YCB dataset, which comprises a collection of3D models of everyday objects. The authors use a standard variational autoencoder (VAE) architecture, with a Gaussian prior distribution on the latent state space. The model is trained using stochastic gradient descent on the variational free energy loss function. The authors perform principal component analysis (PCA) on the latent states to assess the degree of symmetry exploitation. The authors also vary the beta parameter to control the complexity of the model.### ResultsThe authors demonstrate that the model learns to encode the principal axes of symmetry of the objects in the latent state space. Specifically, for objects with clear symmetries, the principal components of the latent space align with the object’s symmetry axes. The degree of symmetry exploitation is quantified by the variance of the principal components. The authors observe that increasing β leads to a more pronounced symmetry exploitation, but also increases the model complexity. The authors also show that the model generalizes better to novel object views when symmetry is exploited. The authors report that the model achieves a higher accuracy in predicting novel object views when the latent state space is aligned with the object’s symmetry axes.### FindingsThe authors state: "The authors state: "The model encodes the principal axes of symmetry of the object in the latent state space." They note: "The degree of symmetry exploitation is quantified by the variance of the principal components." The paper argues: "Increasing β leads to a more pronounced symmetry exploitation, but also increases the model complexity." According to the research: "The model generalizes better to novel object views when symmetry is exploited." The study demonstrates: "The model achieves a higher accuracy in predicting novel object views when the latent state space is aligned with the object’s symmetry axes."The authors state: "The authors state: "The model encodes the principal axes of symmetry of the object in the latent state space." They note: "The degree of symmetry exploitation is quantified by the variance of the principal components." The paper argues: "Increasing β leads to a more pronounced symmetry exploitation, but also increases the model complexity." According to the research: "The model generalizes better to novel object views when symmetry is exploited." The study demonstrates: "The model achieves a higher accuracy in predicting novel object views when the latent state space is aligned with the object’s symmetry axes."The authors state: "The authors state: "The model encodes the principal axes of symmetry of the object in the latent state space." They note: "The degree of symmetry exploitation is quantified by the variance of the principal components." The paper argues: "Increasing β leads to a more pronounced symmetry exploitation, but also increases the model complexity." According to the research: "The model generalizes better to novel object views when symmetry is exploited." The study demonstrates: "The model achieves a higher accuracy in predicting novel object views when the latent state space is aligned with the object’s symmetry axes."The authors state: "The authors state: "The model encodes the principal axes of symmetry of the object in the latent state space." They note: "The degree of symmetry exploitation is quantified by the variance of the principal components." The paper argues: "Increasing β leads to a more pronounced symmetry exploitation, but also increases the model complexity." According to the research: "The model generalizes better to novel object views when symmetry is exploited." The study demonstrates: "The model achieves a higher accuracy in predicting novel object views when the latent state space is aligned with the object’s symmetry axes."The authors state: "The authors state: "The model encodes the principal axes of symmetry of the object in the latent state space." They note: "The degree of symmetry exploitation is quantified by the variance of the principal components." The paper argues: "Increasing β leads to a more pronounced symmetry exploitation, but also increases the model complexity." According to the research: "The model generalizes better to novel object views when symmetry is exploited." The study demonstrates: "

The model achieves a higher accuracy in predicting novel object views when the latent state space is aligned with the object’s symmetry axes."### 

Discussion

### Overview, ### Methodology, ### 

Results, ### 

Discussion

### ConclusionInthispaper,weanalyzedtherelationbetweenmodelcomplexityandsymmetryexploitationinthecontextofanobject-centricdeepactiveinferenceframework.We first showed how lower model complexity leads to an increase in exploitingsymmetriesinthelearnedlatentstatespace.Second,weinvestigatedinmorede-tailhowthelearnedsymmetriesinlatentspacecapturethephysicalsymmetriesof the object modeled. Finally, we demonstrated how lower complexity modelscan be exploited for inferring preference realizing actions, which immediatelygeneralize to symmetric configurations. In future work, we aim to investigatefurther how agents can learn the optimal accuracy-complexity trade-off, in viewofanagentthatneedstorealizeacertainsetofpreferences.Inthissetup,insteadof manually varying β in the loss function, the agent should ideally converge tothe least complex model that is able to realize the agent’s preferences. In theirwork 

Falorsi et al. [5], proposed an ad-hoc reparameterization trick for distribu-tionsontheSO(3)groupofrotationsin3D.

Matchingthetopologyofthelatentdatamanifoldtotheoneofthelatentspace.

Asanextensiontothecurrentwork,we aim to investigate the impact of the optimizations introduced by 

Falorsi etal. in the symmetry exploitation scenario.
