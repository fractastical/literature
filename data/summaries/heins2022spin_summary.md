# Spin glass systems as collective active inference

**Authors:** Conor Heins, Brennan Klein, Daphne Demekas, Miguel Aguilera, Christopher Buckley

**Year:** 2022

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [heins2022spin.pdf](../pdfs/heins2022spin.pdf)

**Generated:** 2025-12-14 12:45:03

**Validation Status:** ✓ Accepted
**Quality Score:** 0.70

---

### OverviewThis paper investigates the relationship between individual and collective inference in multi-agent Bayesian systems, using spin glass models as a sandbox system. The authors demonstrate that the collective dynamics of a specific type of active inference agent is equivalent to sampling from the stationary distribution of a spin glass system. This equivalence is fragile, breaking upon simple modifications to the generative models of the individual agents or the nature of their interactions. The paper highlights the implications of this correspondence for the study of emergent Bayesian inference in multiscale systems.### MethodologyThe authors construct a generative model for a single Bayesian agent, which describes the agent’s internal model of how the local environment generates its sensory data. This generative model is parameterized by a sensory precision parameter γ and a prior precision parameter ζ. The authors show that the Bayesian posterior over hidden states z can be calculated exactly, given the observations σ˜ and the generative model parameters γ,ζ. The authors demonstrate that this Bayesian inference process is equivalent to sampling from the stationary distribution of a spin glass system. The authors also show that the model can be used to generate spin states by sampling from the posterior belief over the hidden state z. The authors use a Boltzmann machine as a generative model, where the nodes are connected via symmetric couplings and biases. The authors use a forward model to describe the relationship between hidden states and actions.### Results

The authors show that the collective dynamics of the active inference agents can be described as sampling from the stationary distribution of a spin glass system. 

The authors show that the model can be used to generate spin states by sampling from the posterior
