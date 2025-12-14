# Autonomous learning and chaining of motor primitives using the Free Energy Principle

**Authors:** Louis Annabi, Alexandre Pitti, Mathias Quoy

**Year:** 2020

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [annabi2020autonomous.pdf](../pdfs/annabi2020autonomous.pdf)

**Generated:** 2025-12-13 19:14:09

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

### OverviewThis paper investigates autonomous learning and chaining of motor primitives using the Free Energy Principle. The authors propose a variational formulation that translates motor primitives learning into a free energy minimization problem. They combine a Kohonen map with a reservoir network and a controller to learn a repertoire of motor trajectories. The study demonstrates the ability to generate long-range sequences minimizing free energy functions corresponding to several random goals.### MethodologyThe model consists of three sub-structures: a Kohonen map, a reservoir network, and a controller. The Kohonen map is used to cluster sensory observations, generating motor primitives. The reservoir network generates motor sequences, while the controller influences its dynamics. The authors use a random recurrent neural network with a self-sustained activity, and fix the readout weights to random values. They optimize the input of the reservoir network instead. The reservoir weights are sparse with each coefficient having a probability of being non-null. The authors use Bernoulli distributions for all pixel values. The model is trained using a free energy minimization approach. The free energy is defined as the difference between the observed state and the prior probability over states. The authors use a gradient-based optimization method to minimize the free energy. The model is trained on a dataset of handwriting trajectories.### ResultsThe authors trained their model for20,000 iterations on50 primitives. The model learns a repertoire of motor primitives that are efficient at building more complex trajectories. The average complexity measured at the end of the episode decreases as the size of the repertoire increases. The authors observed that the final state of the trajectory is close to the filter of the Kohonen map. 

The model is able to generate long-range sequences minimizing free energy functions corresponding to several random goals. 

The authors observed that the final state of
