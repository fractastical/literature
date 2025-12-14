# Graph Distance as Surprise: Free Energy Minimization in Knowledge Graph Reasoning

**Authors:** Gaganpreet Jhajj, Fuhua Lin

**Year:** 2025

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [jhajj2025graph.pdf](../pdfs/jhajj2025graph.pdf)

**Generated:** 2025-12-13 20:41:17

**Validation Status:** ✓ Accepted
**Quality Score:** 1.00

---

### OverviewThis paper investigates the application of free energy minimization to knowledge graph reasoning, proposing that entities closer in graph distance exhibit lower surprise. The authors connect this approach to the Free Energy Principle (FEP) from neuroscience, where agents minimize surprise by maintaining accurate world models. The research formalizes surprise using shortest-path distance in directed graphs and provides a framework for KG-based agents. The core argument is that shorter distances within a knowledge graph correspond to higher probability under the agent’s generative model, and that minimizing surprise drives the agent to ground entities effectively. The paper’s central question is: given a KG serving as an agent’s generative model, which entity groundings are plausible for a query in context?### MethodologyThe authors state: "The Free Energy Principle (FEP) suggests that biological systems minimize surprise by maintaining accurate world models [1,3,4]." They note: "Recently, Murphy et al. [2] demonstrated that syntactic operations minimize surprise through shallow tree structures." They quantify surprise via tree depth (geometric complexity) and Kolmogorov complexity (algorithmic complexity), approximated through Lempel-Ziv compression [5,6]. According to the paper, "In FEP, agents minimize variational free energy𝐹 = −log𝑃(𝑜,𝑠)−𝐻[𝑄(𝑠)]", where𝑜 represents observations,𝑠 hidden states,𝑃 the generative model, and𝑄 the agent’s beliefs [1]. They further explain that "The first term, −log𝑃(𝑜,𝑠), quantifies surprise: entities with high probability under the generative model (high𝑃(𝑜,𝑠)) yield low surprise (low −log𝑃(𝑜,𝑠))."They state: "For syntactic trees, Murphyetal. [2]usedtreedepthto proxythisprobability;weextendthisprincipletogeneralgraphsusingshortest-pathdistance."The authors elaborate: "Inactiveinference, minimizingfreeenergydrivesbothperception(updatingbeliefs𝑄(𝑠))andaction(selecting policies that reduce uncertainty) [3]."They add: "We apply this principle to KG reasoning: entities at shorter graph distances have a higher probability under the agent’s graph-based generative model."The paper describes the approach as using BFS to compute shortest path distances. They note: “Given a KG𝐺 = (ℰ,𝑅,𝑇) with entitiesℰ, relations𝑅, and triples𝑇⊆ℰ ×𝑅×ℰ, geometric surprise is:𝑆geo(𝑒 |𝐶) = min𝑑(𝐶,𝑒) if path exists, else𝛼.”They specify that𝛼 is a hyperparameter penalizing disconnection.The authors also utilize Kolmogorov complexity approximation via Lempel-Ziv compression. They state: "For each grounding, we estimate Kolmogorov complexity via relation path patterns."The paper describes the approach as using BFS to compute shortest path distances.### ResultsThe authors demonstrate free energy calculations using the Canadian Prime Minister knowledge graph from Figure1. They state: “We compute geometric surprise𝑆geo(𝑒 |𝐶) using BFS from Canada.” They show that "Trudeau and Harper exhibit low surprise because they are at short distances (1 hop) from the context Canada."They also state: “Biden has no path from Canada, which results in high surprise.”The authors show that “Entities at shorter distances are more likely:𝑃(observe𝑒 |𝐶) increases as𝑆geo decreases, making low-distance entities preferred for goal-directed actions.” They state: “The authors state: “Trudeau and Harper exhibit low surprise because they are at short distances (1 hop) from the context Canada.” They also state: “Biden has no path from Canada, which results in high surprise.”### DiscussionThe authors conclude: “Real groundings (Trudeau, Harper) exhibit low surprise because they are at short distances (1 hop) from the context Canada.” They add: “Biden has no path from Canada, which results in high surprise.” They note: “Entities at shorter distances are more likely:𝑃(observe𝑒 |𝐶) increases as𝑆geo decreases, making low-distance entities preferred for goal-directed actions.” They state: “The authors state: “Trudeau and Harper exhibit low surprise because they are at short distances (1 hop) from the context Canada.” They also state: “

Biden has no path from 

Canada, which results in high surprise.”
