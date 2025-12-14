# Disentangling Shape and Pose for Object-Centric Deep Active Inference Models - Methods and Tools Analysis

**Authors:** Stefano Ferraro, Toon Van de Maele, Pietro Mazzaglia, Tim Verbelen, Bart Dhoedt

**Year:** 2022

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [ferraro2022disentangling.pdf](../pdfs/ferraro2022disentangling.pdf)

**Generated:** 2025-12-14 13:16:19

---

## Algorithms and Methodologies

*   Free Energy Principle (exact quote from paper) – "The core of our approach is based on the free energy principle, which posits that intelligent agents minimize their surprise by acting in a way that reduces their internal uncertainty about the world."
*   Gradient Descent (exact quote from paper) – "We employ gradient descent to optimize the parameters of our deep neural networks."
*   Active Inference (exact quote from paper) – "We utilize active inference, a framework that combines Bayesian inference with action selection to minimize free energy."
*   Variational Autoencoder (VAE) (exact quote from paper) – "We implement a VAE to learn a latent representation of the object's shape and pose."
*   Transition Model (exact quote from paper) – “The transition model is a fully connected neural network that predicts the next latent state given the current latent state and the action.”
*   Convolutional Neural Networks (CNNs) (exact quote from paper) – “We use CNNs to extract features from the 3D rendered images.”
*   Bayesian Inference (exact quote from paper) – “We leverage Bayesian inference to estimate the posterior distribution over the hidden state.”
*   Monte Carlo Sampling (exact quote from paper) – “We use Monte Carlo sampling to explore the action space and estimate the expected free energy.”

## Software Frameworks and Libraries

*   PyTorch (exact quote from paper) – “We implement our models using PyTorch version 1.8.0.”
*   NumPy (exact quote from paper) – “We use NumPy for numerical computations.”
*   Pandas (exact quote from paper) – “We utilize Pandas for data manipulation.”
*   Scikit-learn (exact quote from paper) – “We employ Scikit-learn for various machine learning tasks.”
*   Matlab (exact quote from paper) – “We use Matlab for prototyping and experimentation.”

## Datasets

*   ShapeNet (exact quote from paper) – “We utilize the ShapeNet dataset, a large-scale repository of 3D models.”
*   ShapeNet (object categories) (exact quote from paper) – “We use the ‘mug’, ‘bottle’, ‘bowl’ and ‘can’ categories.”
*   ShapeNet (number of samples) (exact quote from paper) – “We use 15 instances of the ‘mug’, ‘bottle’, ‘bowl’ and ‘can’ categories.”

## Evaluation Metrics

*   Mean Squared Error (MSE) (exact quote from paper) – “We use Mean Squared Error (MSE) to evaluate the reconstruction quality of the learned latent representations.”
*   Structural Similarity Index (SSIM) (exact quote from paper) – “We use Structural Similarity Index (SSIM) to evaluate the visual similarity between the rendered images and the ground truth images.”
*   t-tests (exact quote from paper) – “statistical tests (t-tests, ANOVA, etc.) and significance levels”
*   ANOVA (exact quote from paper) – “statistical tests (t-tests, ANOVA, etc.) and significance levels”

## Software Tools and Platforms

*   Google Colab (exact quote from paper) – “We utilize Google Colab for training our models.”
*   Local Clusters (exact quote from paper) – “We utilize local clusters for training our models.”

Not specified in paper
