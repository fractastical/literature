# Disentangling Shape and Pose for Object-Centric Deep Active Inference Models

**Authors:** Stefano Ferraro, Toon Van de Maele, Pietro Mazzaglia, Tim Verbelen, Bart Dhoedt

**Year:** 2022

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [ferraro2022disentangling.pdf](../pdfs/ferraro2022disentangling.pdf)

**Generated:** 2025-12-14 13:16:19

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

This paper investigates the problem of disentangling shape and pose representations for object-centric deep active inference models. The authors hypothesize that a model that explicitly factors shape and pose will perform better than a model that learns a single, entangled latent space. The research focuses on the ShapeNet dataset and proposes a model that factors object shape, pose, and category, while still learning a representation for each factor using a deep neural network. The key finding is that models with better disentanglement perform best when adopted by an active agent in reaching preferred observations.The methodology details the creation of a model that factors object shape, pose, and category, while still learning a representation for each factor using a deep neural network. The model consists of an encoder, a transition model, and a decoder. The encoder consists of6 convolutional layers with a kernel size of3, a stride of2 and padding of1. The features for each layer are doubled every time, starting with4 for the first layer. After each convolution, a LeakyReLU activation function is applied to the data. Finally, two linear layers are used on the flattened output from the convolutional pipeline, to directly predict the mean and log variance of the latent distribution. The decoder architecture is a mirrored version of the encoder. It consists of6 convolutional layers with kernel size3, padding1 and stride1. The layers have32,8,16,32 and64 output features respectively. After each layer the LeakyReLU activation function is applied. The data is doubled in spatial resolution before each such layer through bi-linear upsampling, yielding a120 by120 image as final output. A transition model is used to predict the expected latent after applying an action. This model is parameterized through a fully connected neural network, consisting of three linear layers, where the output features are64,128 and128 respectively. The input is the concatenation of a latent sample, and a7D representation of the action (coordinate and orientation quaternion). The output of this layer is then again through two linear layers transformed in the predicted mean and log variance of the latent distribution. This model has474.737 trainable parameters.The results section demonstrates that models with better disentanglement perform best when adopted by an active agent in reaching preferred observations. Specifically, the authors state: "The authors state: "The model with better disentanglement performs best when adopted by an agent in reaching preferred observations"." The authors report that the VAEsp model achieves a mean squared error (MSE) of0.471±0.0824 for the ‘bottle’ category,0.486±0.141 for the ‘bowl’ category,0.707±0.1029 for the ‘can’ category, and0.656±0.0918 for the ‘mug’ category. They also report that the model achieves a mean squared error (MSE) of0.471±0.0824 for the ‘bottle’ category,0.486±0.141 for the ‘bowl’ category,0.707±0.1029 for the ‘can’ category, and0.656±0.0918 for the ‘mug’ category.The discussion section concludes that disentangling shape and pose representations is crucial for building effective object-centric deep active inference models. As future work, the authors will further their study on the impact of disentanglement, and how to better enforce disentanglement in their model. They believe that this line of work is important for robotic manipulation tasks, i.e. where a robot learns to pick up a cup by the handle, and can then generalize to pick up any cup by reaching to the handle.
