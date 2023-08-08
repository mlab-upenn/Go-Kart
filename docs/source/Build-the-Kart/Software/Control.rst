Control
==============

In this section, we discuss examples of control algorithm that can be developed and tested on this platform. All algorithms mentioned in this section have been verified inside the simulation, and are ready to be tested on the physical go-kart
platform.

Pure Pursuit
-------------
We use this simple path-following algorithm do the initial testing of our platform. This is used as a benchmark to test the control performance of the hardware (steering, throttle, brake) in terms of accuracy and delay and to verify the success of hardware-software integration. This algorithm can also be used in the future as a baseline when developing other, more complex algorithms.

Model Predictive Control (MPC)
------------------------------
There are various types of MPC controllers, e.g., kinematic MPC, dynamic MPC, LMPC , GP-MPC (Gaussian process MPC) , etc. While some variations of these algorithms (e.g., linear kinematic MPC) can run fast enough on low- performance computers (e.g., NVIDIA Jetson NX), other algorithms (e.g., linear/nonlinear dynamic MPC, GP-MPC ) need more powerful computers that are bigger and heavier. Compared to the compact 1/10 scale cars, the go-kart platform can fit these units and compute heavier workloads.

Imitation Learning
------------------
IL can be achieved through direct human demonstration and intervention. In the manual mode, a driver can sit inside the go- kart and provide expert demonstration through normal driving. In the autonomous mode, the human driver still sits inside the go-kart but takes over whenever it runs into a critical condition. Demonstrations and takeovers are also available through teleportation but may not provide the necessary mo- tion feedback and prompt swift human action. These methods illustrated provide the capabilities of controlling the go-kart with interactive IL methods like Human-Gated DAgger (HG- DAgger) and Expert Intervention Learning (EIL) . As mentioned in , the interactive IL methods outperform traditional IL methods and improve RL performances via bootstrapping. The concepts can be furthered explored on the go-kart taking advantage of its increased scale and capability.

Open-source Platform Software
-----------------------------
All sensing, planning and control capabilities are devel- oped within the Robot Operating System v2 (ROS2) and are being integrated within the Autoware Universe open-source autonomous driving software stack . This allows for a stan- dardized set of interfaces so users can easily develop, modify and test the vehicle software. All design specifications, CAD models, assembly instructions, software code and algorithm implementations will be made available to the public in a free and open-source manner as it is our intention to support this line of research in autonomous racing. 
From a software standpoint, we design our applications in a modular fashion, lending well to a microservices-driven architecture based on images which are then orchestrated using kubernetes. This development mindset enables us to incorporate continuous integration (CI) and continuous de- ployment (CD) of our images making both our applications and workflows more aligned with production-level automobile application efforts.
Our current efforts are to develop a SDV approach for development and testing in the cloud with software updates for new capabilities. For our SDV efforts we use an AVA ARM64 development platform workstation with an Nvidia GPU. This platform permits our applications to be tested and evaluated on the same compute resources expected in an automobile. Furthermore, we employ the Edge Workload Abstraction and Orchestration Layer (EWAOL)  a reference implementa- tion of the Scalable Open Architecture for Embedded Edge (SOAFEE) . This not only enables verification of our applications on-premises and in the cloud, it also facilitates easier autonomous driving commissioning to a new platform and updates over the lifetime for existing platforms.