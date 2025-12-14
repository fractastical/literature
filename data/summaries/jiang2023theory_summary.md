# A Theory of Human-Like Few-Shot Learning

**Authors:** Zhiying Jiang, Rui Wang, Dongbo Bu, Ming Li

**Year:** 2023

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [jiang2023theory.pdf](../pdfs/jiang2023theory.pdf)

**Generated:** 2025-12-14 09:26:00

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

### OverviewThis paper investigates the theory of human-like few-shot learning, proposing a novel framework that addresses the gap between common-sense learning and current deep learning models. The authors argue that existing models fail to capture the diversity and adaptability observed in human and animal learning. They derive a theory based on von-Neuman-Landauer’s principle, emphasizing the importance of compression and information distance in few-shot learning. The core idea is that the brain learns by minimizing the discrepancy between its internal model and the external environment, and this can be formalized through a universal compressor. The paper demonstrates that a hierarchical variational autoencoder (VAE) can approximate this theory and achieve significantly better performance than traditional deep learning models on image recognition, low-resource language processing, and character recognition.### MethodologyThe authors’ theoretical framework is built upon the principle of irreversible processing of1 bit of information costing1kT, as proposed by von Neumann and Landauer. They define few-shot learning as minimizing the objective function: E(x,y) = max{K(x|y),K(y|x)}+O(1), where K(x|y) represents the Kolmogorov complexity of x given y, which is the shortest program that outputs x given input y. This framework is implemented using a hierarchical VAE, where the encoder learns a compressed representation of the input data, and the decoder reconstructs the original data from this compressed representation. The hierarchical structure allows the model to capture complex relationships between data points and to adapt to new data points more effectively. The experimental setup involves training the VAE on unlabeled data and then evaluating its performance on several benchmark datasets, including MNIST, KMNIST, FashionMNIST, STL-10, and CIFAR-10. The authors compare the performance of the VAE with that of several other deep learning models, including convolutional neural networks (CNNs), variational autoencoders (VAEs), and transformers.### ResultsThe experimental results demonstrate that the proposed VAE-based framework significantly outperforms other deep learning models on few-shot learning tasks. Specifically, the VAE achieves77.6% accuracy on the MNIST dataset,55.4% accuracy on the KMNIST dataset,74.1% accuracy on the FashionMNIST dataset, and39.6% accuracy on the STL-10 dataset, while achieving35.3% accuracy on the CIFAR-10 dataset. These results are substantially better than those obtained by traditional deep learning models, which typically achieve accuracies in the range of20-40% on these datasets with5-shot learning. The authors also show that the VAE can learn a compressed representation of the data that is invariant to variations in the input data, such as changes in lighting or viewpoint. Furthermore, the VAE can be used to generate new data points that are similar to the training data. The authors also highlight the importance of the “interestingness” concept, which emerges as a key component of the model’s learning process. This concept reflects the model’s ability to identify and prioritize the most relevant information in the data.### DiscussionThe authors’ findings have important implications for the field of machine learning. They demonstrate that a simple, compression-based approach can achieve human-like few-shot learning performance. This suggests that current deep learning models may be over-parameterized and that a more efficient approach is needed. The authors’ theory also provides a theoretical framework for understanding how the brain learns, emphasizing the role of compression and information distance. The concept of “interestingness” is particularly noteworthy, as it suggests that the brain may be actively seeking out the most relevant information in the data. The authors’ work opens up new avenues for research in areas such as unsupervised learning, representation learning, and artificial intelligence. 

The ability to compress information and to learn from limited data has significant implications for a wide range of applications, including robotics, computer vision, and natural language processing. 

The authors conclude that their theory provides a fundamental understanding of human-like few-shot learning, and that their VAE-based framework represents a promising approach for achieving human-level intelligence.
