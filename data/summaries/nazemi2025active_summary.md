# Active Inference for Energy Control and Planning in Smart Buildings and Communities

**Authors:** Seyyed Danial Nazemi, Mohsen A. Jafari, Andrea Matta

**Year:** 2025

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [nazemi2025active.pdf](../pdfs/nazemi2025active.pdf)

**Generated:** 2025-12-13 20:46:28

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

### OverviewThis paper investigates Active Inference (AIF) as a framework for energy control and planning in smart buildings and communities. The authors propose a dual-layer AIF architecture, combining building-level and community-level agents to address the inherent challenges of managing complex, partially observable, and non-stationary systems. The core of AIF lies in minimizing the free energy, which involves inferring latent states and adapting to evolving conditions without relying on extensive sensor data or intrusive data collection. The paper highlights the advantages of AIF over traditional methods, such as Model Predictive Control (MPC) and Reinforcement Learning (RL), particularly in scenarios involving high uncertainty, partial observability, and dynamic interactions. The authors emphasize the privacy-preserving nature of AIF, allowing for inference of hidden states from readily observable data, such as building power consumption and occupancy patterns.### MethodologyIn the Introduction, the authors state: "Active Inference (AIF) is emerging as a powerful struggle with inaccuracies in forecasts, and RL models, which require significant computational resources for training." They note that many engineering systems are not fully observable and they are subject to underlying hidden uncertainties. The authors further state: "many real-life systems are hybrid and demonstrate both time- and event-based dynamics." The paper outlines the key components of the dual-layer AIF architecture. The building AIF agent tracks a preferred target, namely, “optimal” cooling conditions for its occupants. This is accomplished by controlling the heating, ventilation, and air conditioning (HVAC) resources amid internal hidden dynamics and uncertainties, such as occupancy and infiltration airflow. The agent uses noisy measurements of indoor temperature (𝑇(𝑡)) to refine its beliefs about the hidden states, namely, occupancy level (𝑂𝐶𝐶(𝑡)) and infiltration airflow (𝑚̇(𝑡)). The agent’s control actions are HVAC airflow (𝑎 =𝑚̇) and supply air temperature (𝑎 =𝑇). The community AIF agent operates over a24-hour horizon, which is divided into15-minute intervals using a short-horizon EFE minimization. The discrete AIF agent coordinates power flows, battery usage, and external market interactions. The authors state: “The model structure allows the aggregator to infer their respective hidden states and ensure that the performance targets are tracked and achieved.” The authors also highlight that the AIF framework is organic in maintaining a perception model that can best describe a real process amid the observed outcomes.### ResultsThe authors demonstrate the AIF framework’s ability to track occupancy profiles against the original occupancy profile. The authors state: “The AIF model effectively tracks fluctuations in occupancy, household appliance usage, HVAC power consumption, and/or other factors that drive building loads.” The authors report that the model can maintain room temperature within the desired range. The authors report that the model can maintain room temperature within the desired range. 

The authors state: “

The model structure allows the aggregator to infer their respective hidden states and ensure that
