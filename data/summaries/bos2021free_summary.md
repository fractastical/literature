# Free Energy Principle for State and Input Estimation of a Quadcopter Flying in Wind

**Authors:** Fred Bos, Ajith Anil Meera, Dennis Benders, Martijn Wisse

**Year:** 2021

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [bos2021free.pdf](../pdfs/bos2021free.pdf)

**Generated:** 2025-12-13 18:56:39

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

### OverviewThis paper investigates the application of the free energy principle (FEP) for state and input estimation of a quadcopter flying in wind. The authors aim to provide the first experimental confirmation of DEM’s usefulness as a state and input estimator for real robots. Through a series of quadrotor flight experiments under unmodelled wind dynamics, they demonstrate that DEM can leverage the information from colored noise for accurate state and input estimation through the use of generalized coordinates. The paper highlights the similarities in performance of DEM and Unknown Input Observer (UIO) for input estimation, and shows the influence of prior beliefs in shaping the accuracy-complexity trade-off during DEM’s estimation.### MethodologyThe authors introduce an experimental design with real robots to provide the proof of concept for DEM as a state and input observer. The experimental setup consists of a Parrot AR.drone2.0 quadrotor hovering in wind produced by a blower in a controlled lab. The key concept is the use of generalized coordinates for noise color handling, which involves keeping track of the trajectory of all time-varying quantities (instead of only its point estimates) through a vector of derivatives. The noise is assumed to be the result of a white noise signal that has been convoluted using a Gaussian filter of the form: K(t) = √1 exp(−1(t)2) , which provides an easy computation of the covariance of the noise derivatives. The authors use a Laplace approximation to simplify the free energy calculation. The system dynamics are modeled using a linear parameter estimator, and the DEM observer is designed using the equations given in [6]. The experimenter uses a PWM signal to control the quadrotor’s thrust, and the DEM observer estimates the input based on the measured output. The DEM observer is set with the order of generalized motion of states and inputs to be p=6 and d=2 respectively. The authors use a9th experiment to tune the noise smoothness to σ =0.006.### ResultsThe authors demonstrate that DEM can leverage the information from colored noise for accurate state and input estimation through the use of generalized coordinates. They show that DEM outperforms other benchmarks like KF, SMIKF and SA for state estimation with minimal estimation errors. The authors highlight the similarities in the performance of DEM and UIO for input estimation. The authors demonstrate that the noise precision Πw = e3I and Πz =8.1·10−9. The authors show that the influence of prior beliefs in shaping the accuracy-complexity trade-off during DEM’s estimation. The authors demonstrate that the input estimates move from a wrong prior of ηv =1 to the measured input (inblue), mediated by the prior precision Pv.### DiscussionThe authors conclude by showing the influence of prior beliefs in shaping the accuracy-complexity trade-off during estimation. The DEM observer’s state and input estimates lie on top of the variational free energy surface, indicating that the DEM observer maximizes V(t). The authors show that the noise precision Πw = e3I and Πz =8.1·10−9. 

The authors demonstrate that the input estimates move from a wrong prior of ηv =1 to the measured input (inblue), mediated by the prior precision 

Pv
