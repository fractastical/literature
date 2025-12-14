# Human-Robot Kinaesthetic Interaction Based on Free Energy Principle

**Authors:** Hiroki Sawada, Wataru Ohata, Jun Tani

**Year:** 2023

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [sawada2023humanrobot.pdf](../pdfs/sawada2023humanrobot.pdf)

**Generated:** 2025-12-13 18:07:12

**Validation Status:** ✓ Accepted
**Quality Score:** 1.00

---

### OverviewThis paper investigates human-robot kinaesthetic interaction using a variational recurrent neural network model, called PV-RNN, based on the free energy principle. The authors demonstrate that the nature of interactions between top-down expectations and bottom-up inference is strongly affected by a parameter called the meta-prior, which regulates the complexity term in the free energy. The study examines how changing this meta-prior affects the counterforce generated when an experimenter attempts to induce movement patterns familiar to the robot. The research also compares the counterforce generated when trained transitions are induced by a human experimenter versus when untrained transitions are induced.### MethodologyThe core of the study relies on the PV-RNN model, which is operated in two phases: training and interaction. During the training phase, the model learns to generate movement patterns with specific transition probabilities among them. The model uses a recurrent neural network with a variational inference approach to estimate the posterior probability distribution of the latent variables. The model is parameterized by a meta-prior, which regulates the complexity term in the free energy. The model is trained using a dataset of movement patterns. During the interaction phase, the robot and the human experimenter interact physically, and the PV-RNN drives the robot’s arms by predicting the next time-step joint angles. The PV-RNN predicts the future sensation and infers the past latent variables. The model is controlled by a PID controller to generate the robot’s movements. The PV-RNN uses a time constant to determine the timescale of the neural network. The PV-RNN uses a variational inference approach to estimate the posterior probability distribution of the latent variables. The model is parameterized by a meta-prior, which regulates the complexity term in the free energy.### ResultsThe experimental results indicated that (1) the human experimenter needs more/less force to induce trained transitions when we set with larger/smaller values, (2) the human experimenter needs more force to act on the robot when he attempts to induce untrained as opposed to trained movement patterns transitions. The authors observed that the time-averaged prediction error, the excess torque, and the KL-divergence in both layers increased with larger meta-prior values. The study showed that the robot with a larger meta-prior tended to lead the counterpart robot set with smaller meta-prior by projecting stronger actional intention to the counterpart. The authors found that the transition probabilities of the trained patterns were approximately2.8%,3.5%,15.6%,12.5%, and3.1%, respectively. The transition probabilities of the untrained transition were approximately2.7%,9.3%,14.1%,11.5%, and7.2%, respectively. The authors observed that the time-averaged prediction error, the excess torque, and the KL-divergence in both layers increased with larger meta-prior values.### DiscussionThe authors state: "The nature of interactions between top-down expectation and bottom-up inference is strongly affected by a parameter called the meta-prior, which regulates the complexity term in the free energy." The authors note: "The human experimenter needs more/less force to induce trained transitions when we set with larger/smaller values." The paper argues: "The human experimenter needs more force to act on the robot when he attempts to induce untrained as opposed to trained movement patterns transitions." 

According to the research, the key finding is that the robot with a larger meta-prior tends to lead the counterpart robot set with smaller meta-prior by projecting stronger actional intention to the counterpart. 

The study demonstrates that the transition probabilities of the trained patterns were approximately2.8%,3.5%,15.6%,12.5%, and3.1%, respectively
