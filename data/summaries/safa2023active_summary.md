# Active Inference in Hebbian Learning Networks

**Authors:** Ali Safa, Tim Verbelen, Lars Keuninckx, Ilja Ocket, André Bourdoux, Francky Catthoor, Georges Gielen, Gert Cauwenberghs

**Year:** 2023

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [safa2023active.pdf](../pdfs/safa2023active.pdf)

**Generated:** 2025-12-14 10:36:15

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

### OverviewThis paper investigates the application of active inference within neural ensembles equipped with local Hebbian plasticity for controlling dynamical agents. The authors demonstrate that this approach outperforms Q-learning while avoiding the need for replay buffers, suggesting a novel pathway for designing active inference networks.### MethodologyThe authors propose a Hebbian AIF system composed of two distinct Hebbian ensembles: a posterior network, which infers latent states given observations and actions, and a state-transition network, which predicts the next expected latent state given current state-action pairs. The core of the system relies on Hebbian learning, where the weight dictionary used to project input signals into sparse codes is learned via a combination of the weight’s input and the neuron’s output (w ←−w +η f(y ,x )). The authors employ a variational free-energy minimization approach, utilizing the Kullback-Leibler divergence between the inferred posterior and the predicted state transition. The state-transition network is implemented as an auto-regressive Hebbian network, taking as input a sequence of state-and-action history and inferring the next states via sparse coding. The authors use a time-lag buffer length to store past latent states, which is used by the state-transition network to estimate the next expected state. The authors employ a variational free-energy minimization approach, utilizing the 

Kullback-

Leibler divergence between
