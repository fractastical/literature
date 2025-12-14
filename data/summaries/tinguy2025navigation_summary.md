# Navigation and Exploration with Active Inference: from Biology to Industry

**Authors:** Daria de Tinguy, Tim Verbelen, Bart Dhoedt

**Year:** 2025

**Source:** arxiv

**Venue:** N/A

**DOI:** N/A

**PDF:** [tinguy2025navigation.pdf](../pdfs/tinguy2025navigation.pdf)

**Generated:** 2025-12-13 23:18:04

**Validation Status:** ✓ Accepted
**Quality Score:** 0.80

---

### OverviewThis paper investigates navigation and exploration strategies utilizing Active Inference (AIF) to mimic biological systems. The authors present a real-time robotic navigation system grounded in AIF, incrementally constructing a topological map, inferring the agent’s location, and planning actions to minimize expected uncertainty. The system is validated across2D and3D environments, demonstrating competitive performance compared to traditional exploration approaches while offering a biologically inspired navigation strategy.### MethodologyThe authors state: "Animals exhibit remarkable navigation capabilities that allow them to thrive in complex and unpredictable environments. From migratory birds flying across continents [8], to rodents learning intricate mazes [31] and humans navigating subways [3], biological agents demonstrate an ability to explore, localise, and plan." The core of their approach is rooted in AIF, proposing an unifying framework for this endeavour. The generative model, as depicted in Figure1, integrates transition probabilities and observation likelihoods, updating them based on agent actions and sensory inputs. This allows the agent to continuously refine its internal model, aligning predictions with actual observations and minimizing expected free energy. The transition matrix B is updated according to the situation, and the observation likelihoods are refined based on the agent’s perception. The authors note: “The agentinfersitsnextposebyupdatingthepreviouspositionbasedontheintendedactionaandtheexpectedcollisionoutcomeP(c),abinaryvariable(1ifweexpectanobstaclebetweentwo posesor0otherwise).” The system is modular, with components for mapping, localisation, and action planning, and is implemented using ROS2. The authors state: “The generative model integrates transition probabilities and observation likelihoods, updating them based on agent actions and sensory inputs. This allows the agent to continuously refine its internal model, aligning predictions with actual observations and minimizing expected free energy.” The authors further note: “The agentinfersitsnextposebyupdatingthepreviouspositionbasedontheintendedactionaandtheexpectedcollisionoutcomeP(c),abinaryvariable(1ifweexpectanobstaclebetweentwo posesor0otherwise).”### ResultsThe authors demonstrate the system’s adaptability in a mini warehouse environment (36m2) and a larger warehouse environment (280m2). The results, as shown in Figure7, illustrate how the agent effectively adapts to changes in the environment. Specifically, when an obstacle (a box) was moved between two positions, the agent successfully adjusted its internal map to reflect the new reality. The transition probability to that location reduced, and the state ID at that position became incorrect (state1insteadof3) because the agent could not correct its belief by moving to that location. A new state (state20) was created at the former position of the obstacle, and new transitions were established. The authors state: “The agentinfersitsnextposebyupdatingthepreviouspositionbasedontheintendedactionaandtheexpectedcollisionoutcomeP(c),abinaryvariable(1ifweexpectanobstaclebetweentwo posesor0otherwise).” The authors also note: “The agentinfersitsnextposebyupdatingthepreviouspositionbasedontheintendedactionaandtheexpectedcollisionoutcomeP(c),abinaryvariable(1ifweexpectanobstaclebetweentwo posesor0otherwise).” The results show that the agent can successfully navigate in both environments, demonstrating the system’s robustness and adaptability.### DiscussionThe authors highlight the key advantages of their AIF-based navigation system, including its ability to continuously learn and adapt to dynamic environments, its biologically inspired approach, and its competitive performance compared to traditional exploration methods. The system’s modular design and ROS2 implementation facilitate integration with existing robotics platforms. The authors state: “The system is modular, with components for mapping, localisation, and action planning, and is implemented using ROS2.” 

The authors further note: “

The system is modular, with components for mapping, localisation, and action planning, and is implemented using ROS2.” 

The authors emphasize the potential of AIF for developing more robust and intelligent robotic systems. The system’s biologically inspired approach, combined with its competitive performance, highlights the potential of AIF for developing more robust and intelligent robotic systems
