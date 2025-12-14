# Efficient search of active inference policy spaces using k-means

**Authors:** Alex B. Kiefer, Mahault Albarracin

**Year:** 2022

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [kiefer2022efficient.pdf](../pdfs/kiefer2022efficient.pdf)

**Generated:** 2025-12-14 12:59:04

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

### OverviewThis paper investigates efficient policy selection within active inference models, specifically leveraging k-means clustering to create a structured policy representation. The authors propose a hierarchical search scheme that combines pruning with vector space embeddings to dramatically reduce the computational complexity of exhaustive policy search. The core idea is to map each policy to its embedding in a vector space, sample the expected free energy of representative points in the space, and then perform a more thorough policy search around the most promising candidate, followed by a local search. The authors demonstrate that this approach can achieve accuracy comparable to exhaustive policy search with drastically lower time complexity.### MethodologyThe authors’ approach centers around k-means clustering to select representative points in the policy space. They state: "We consider various approaches to creating the policy embeddingspace, and proposeusingk-meansclusteringtoselectrepresentativepoints." The k-means algorithm is used to group policies based on their similarity, creating clusters of policies that are proximal to one another in the vector space. The authors explain: “We applyourtechniquetoagoal-orientedgraph-traversalproblem,forwhichnaive policy selection is intractable for even moderately large graphs.” The k-means algorithm is used to identify the cluster centers, which represent the most representative policies within each cluster. The authors further elaborate: “In general, it is to be expected that there would be a correlation between the degree to which two policies are structurally related (hence their location in embeddingspace) and theirenergy.” The authors incorporate this into their free energy calculation, stating: “We combinepruningwiththeuseofvectorspaceembeddings [20] to create a structured policy representation in which qualitatively similar policies are proximal to one another.” The k-means clustering is performed on the policy space, and the resulting cluster centers are used to guide the policy search.### ResultsThe authors tested their approach on a graph-navigation problem, demonstrating that it is possible to achieve accuracy comparable to exhaustive policy search with drastically lower time complexity. They report: “We show that it is possible to achieve accuracy comparable to exhaustive policy search with drastically lower time complexity.” The experimental results show that the hierarchical policy selection scheme reduces the computation time by an order of magnitude. The authors state: “The key difference between active inference and other POMDP models and in particular reinforcement learning models lies in the function used to compute the value of the policies [18].” The authors also found that the degree to which two policies are structurally related (hence their location in embeddingspace) and theirenergy.### DiscussionThe authors’ work highlights the potential of vector space embeddings and k-means clustering to improve the efficiency of active inference policy selection. They note: “The point of constructing an embedding, for present purposes, is to avoid having to compute the expected free energy of every possible policy.” The authors’ approach offers a scalable solution to the computational bottleneck associated with exhaustive policy search. They conclude: “

The authors state: ‘

We show that it is possible to achieve accuracy comparable to exhaustive policy search with drastically lower time complexity.’”
