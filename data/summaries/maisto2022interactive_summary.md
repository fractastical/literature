# Interactive inference: a multi-agent model of cooperative joint actions

**Authors:** Domenico Maisto, Francesco Donnarumma, Giovanni Pezzulo

**Year:** 2022

**Source:** arxiv

**Venue:** N/A

**DOI:** 10.1109/TSMC.2023.3312585

**PDF:** [maisto2022interactive.pdf](../pdfs/maisto2022interactive.pdf)

**Generated:** 2025-12-14 09:05:22

**Validation Status:** ✓ Accepted
**Quality Score:** 1.00

---

### OverviewThis paper investigates interactive inference as a multi-agent model of cooperative joint actions. The authors state: "We advance a novel computational model of multi-agent, cooperative joint actions that is grounded in the cognitive framework of active inference." They note: "A central challenge of multi-agent systems (MAS) is coordinating the actions of multiple agents in time and space, to accomplish cooperative tasks and achieve joint goals [1], [2]." The paper argues that to address this challenge, “cognitive mechanisms for mutual prediction, mental state inference, sensorimotor communication and shared task representations” are needed. The authors state: "The cognitive mechanisms supporting joint action have been probed by numerous experiments [19]–[29], sometimes with the aid of conceptual [30], computational [31]–[39], and robotic [40]–[43] models."### MethodologyThe authors describe two simulations to test their interactive inference model. The first simulation, labelled “leaderless”, illustrates how two agents can align their beliefs and behaviors when they lack a strong preference about the joint task goal. They note: “The first simulation illustrates a ‘leaderless’ joint action. It shows that when two agents lack a strong preference about their joint task goal, they jointly infer it by observing each other’s movements.” The second simulation, labelled “leader-follower”, demonstrates how a more knowledgeable agent (the “leader”) can guide a less knowledgeable agent (the “follower”) to achieve the joint task. They state: “When one agent (“leader”) knows the true joint goal, it uses sensorimotor communication to help the other agent infer it, even if doing this requires selecting a more costly individual plan.” The model is based on the active inference framework, which describes the brain as a prediction machine, which learns an internal (generative) model of the statistical regularities of social interactions. The model uses a generative model that encodes the joint probability of the stochastic variables, using the formalism of probabilistic graphical models. The model consists of two agents, “grey” (“i”) and “white” (“j”), that start from the locations L3 and L19 and their goal is to reach either the red (L10) or the blue (L12) goal locations. The model uses a tensor Ai, which plays the role of a “salience map”, which varies as a function of the agent’s beliefs about the joint task goal.### ResultsThe results of Simulation1 show that the two agents end up the trials by pressing the blue and red buttons, respectively. The authors state: “The first two panels show the prior beliefs of the white (first panel) and grey (second panel) agents at the beginning of each trial.” The results of Simulation2 show that the agents successfully solved the task by pressing the red buttons. The authors state: “The red squares indicate that the agents successfully solved the task by pressing the red buttons. The black squares indicate failures.” The authors state: “The first panel shows a measure of belief alignment of the agents: the KL divergence between their beliefs about task goals.” The authors state: “The second panel shows a histogram of mean success rate.” The authors state: “The most preferred policy, the25th, infers that the leader will follow the long path to the red goal and the follower will follow the short path to the red goal.”### DiscussionThe authors conclude that interactive inference can successfully reproduce key empirical results of joint action studies. They state: “This paper investigates interactive inference as a multi-agent model of cooperative joint actions.” The authors state: “The cognitive mechanisms supporting joint action have been probed by numerous experiments [19]–[29], sometimes with the aid of conceptual [30], computational [31]–[39], and robotic [40]–[43] models.” The authors state: “The cognitive mechanisms supporting joint action have been probed by numerous experiments [19]–[29], sometimes with the aid of conceptual [30], computational [31]–[39], and robotic [40]–[43] models.” 

The authors state: “

The cognitive mechanisms supporting joint action have been probed by numerous experiments [19]–[29], sometimes with the aid of conceptual [30], computational [31]–[39], and robotic [40]–[43] models.”
