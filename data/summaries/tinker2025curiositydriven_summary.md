# Curiosity-Driven Development of Action and Language in Robots Through Self-Exploration

**Authors:** Theodore Jerome Tinker, Kenji Doya, Jun Tani

**Year:** 2025

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [tinker2025curiositydriven.pdf](../pdfs/tinker2025curiositydriven.pdf)

**Generated:** 2025-12-14 00:07:12

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

### OverviewThis paper investigates the development of action and language in robots through self-exploration, driven by curiosity. The authors demonstrate that robots can learn complex behaviors by actively seeking novel sensory experiences and integrating intrinsic rewards. This approach, based on the free energy principle and active inference, offers a powerful account of how intelligent systems can acquire competencies without explicit supervision.### MethodologyThe core methodology centers on a robot equipped with a forward model, which predicts future sensory observations based on motor commands. The forward model is trained using a variational recurrent neural network (VRNN) to minimize the KL divergence between the predicted and actual sensory observations. The robot’s behavior is governed by an actor-critic network, which learns to generate motor commands to maximize expected free energy. The experimental setup involved training the robot with three levels of curiosity, measured by the relative importance of sensory-motor and feedback rewards. The robot was trained on a set of tasks involving manipulating objects and achieving goals, guided by imperative sentences. The experiments were conducted using a simulated environment, allowing for precise control and data collection.### ResultsThe key findings of the study are as follows:1.Generalization improves markedly as the scale of compositional elements increases. The robots exhibited significantly better generalization performance when trained on larger vocabularies of verbs, adjectives, and nouns.2.Curiosity combined with motor entropy enhances developmental learning. Robots equipped with both curiosity and motor entropy consistently outperformed those trained with only one of these components.3.In the early phase, actions are generated only for exactly learned imperative sentences, but in later phases, the system generalizes to novel, unlearned compositions. This suggests a hierarchical learning process, where simpler prerequisites are acquired before more complex actions.4.Primitive actions develop earlier, followed by more complex, prerequisite-dependent actions. This indicates a staged learning process, where simpler actions are mastered before more complex ones.5.Exception-handling rules can be acquired through exploratory learning, exhibiting U-shaped developmental performance similar to human children. When trained with exceptions, the robots initially produced incorrect actions but eventually recovered, demonstrating an ability to reorganize their internal representations.The authors observed a U-shaped performance curve when robots were trained with exception-handling rules, indicating that the robots initially produced incorrect actions but eventually recovered, demonstrating an ability to reorganize their internal representations.### DiscussionThe authors argue that the findings support a computational account of human development, suggesting that curiosity-driven exploration and active inference provide a powerful framework for understanding how intelligent systems acquire competencies. The results align with the free energy principle, which posits that intelligent systems minimize their surprise by actively seeking novel experiences. The authors highlight the importance of hierarchical learning, where simpler actions are mastered before more complex ones.The authors state: "The authors state: "This suggests that hierarchical learning is a key mechanism for acquiring complex behaviors."The authors conclude: "

The authors state: "

This provides a powerful account of how intrinsic motivation and hierarchical sensorimotor learning can jointly support scalable compositional generalization and exception handling in both humans and artificial agents."
