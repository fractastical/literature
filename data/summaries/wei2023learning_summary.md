# Learning An Active Inference Model of Driver Perception and Control: Application to Vehicle Car-Following

**Authors:** Ran Wei, Anthony D. McDonald, Alfredo Garcia, Gustav Markkula, Johan Engstrom, Matthew O'Kelly

**Year:** 2023

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [wei2023learning.pdf](../pdfs/wei2023learning.pdf)

**Generated:** 2025-12-14 10:30:21

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

### OverviewThis paper investigates learning an active inference model of driver perception and control using a partially observable Markov decision process (POMDP) framework. The authors propose a novel approach to modeling human behavior by jointly estimating the reward function, internal model of the environment, and state transition probabilities from observed trajectories. The core of the model is based on the principle of free energy minimization, where the agent minimizes “surprise” by adjusting its actions to align with its preferred state distribution. The study compares the proposed model with behavior cloning (BC) and the intelligent driver model (IDM) using a dataset of car-following behavior.### MethodologyThe authors develop a POMDP model for car-following behavior, which consists of a state transition probability, an observation probability, and a reward function. The state transition probability describes how the state of the vehicle evolves over time, given the action taken by the driver. The observation probability describes how the driver perceives the state of the environment, given the state of the vehicle. The reward function specifies the driver’s preference over different states of the environment. The model is trained using maximum a posteriori (MAP) estimation, which involves maximizing the posterior distribution of the model parameters given the observed data. The authors employ a stochastic gradient algorithm to optimize the model parameters. The model is implemented using a two-layer neural network for the state transition probability and a Gaussian mixture model for the observation probability. The model is trained using a batch size of100 and a learning rate of0.001.### ResultsThe authors evaluate the performance of the proposed model, BC, and IDM using a dataset of car-following behavior. The results show that the proposed model outperforms BC and IDM in terms of prediction accuracy. Specifically, the proposed model achieves a mean absolute error (MAE) of0.1 m/s2, while BC and IDM achieve MAE values of0.2 m/s2 and0.8 m/s2, respectively. 

The authors also find that the proposed model is more robust to variations in the dataset. 

The authors demonstrate that the model can accurately predict the behavior of drivers in a wide range of driving conditions
