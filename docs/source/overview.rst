==================================
Overview
==================================

.. |Link1| raw:: html

   <a href="https://github.com/mlab-upenn/gokart-sensor/tree/ros2_foxy_purepursuit">ROS2 Foxy setup and autonomous code</a>

.. |Link2| raw:: html

   <a href="https://github.com/mlab-upenn/gokart-sensor/tree/ros2_humble_purepursuit">ROS2 Humble setup and autonomous code</a>

.. |Link3| raw:: html

   <a href="https://github.com/mlab-upenn/gokart-mechatronics/tree/main/STM32%20Control">STM32 nucleo controller code</a>

Get ready to get hands on experience with one of the coolest technology stacks for racing and research!

Autonomous operation
=========
.. raw:: html

 <iframe width="560" height="315" src="https://www.youtube.com/embed/6IgGBG_flno" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


Remote operation
=========
.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/dP3PGr-Ddmg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Manual operation
=========
.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/cA9_ItmdoMk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

.. note::
    
   The Gokart features multiple modes and can be operated in manual, remote and autonomous mode. Deep dive into the documentation to get to know how to run this.

Preface 
=========
As extensive research has been done with autonomous vehicle related modules such as perception, localization, planning, control, and prediction , human-in-the-loop end-to- end approaches such as deep learning (DL) and imitation learning (IL) still have open research challenges for safety- critical operation. On one hand, the problem with the modular algorithm design is that each individual module in the pipeline may not be aware of the ”high-level” task required, and result in an omission of information and a lack of coordination. An end-to-end approach, on the contrary, considers the autonomous system as a whole, and maps directly from the raw sensory input to the control output (throttle, steering, brake). This approach not only has merits in the racing field but can also be extended to make meaningful real road applications

Why do we need the Go-Kart AVEV?
==================================
Imitation Learning has shown itself as an effective end-to-end method which could be trained effectively using expert demonstrations such as existing models or human participation, but the safety aspects require much to be validated. One way of evaluation is to use an open-source driving simulator, for instance, the TORCS Simulator, the Udacity Simulator , and the CARLA Simulator . While a simulator provides support for easy development and effective validation of algorithms, it lacks the connection to the real world and needs to be further tested on physical platforms. Another popular approach is to use reduced scale vehicles. For example, Cai et al. combined reinforcement learning (RL) and IL called deep imitative reinforcement learning and tested the algorithms on a 1:20 scale autonomous RC car . Sun et. al. assessed four IL algorithms using pure pursuit as the expert on a one-tenth scale racing platform called F1Tenth and achieved promising results . A problem with these reduced scale platforms is that they have very limited computing power, sensing capability, and are significantly different from full scale vehicles. It is also possible to develop and experiment the  learning algorithms on a real car. However, such platform setup generally requires a non-trivial financial commitment, cumbersome reverse engineering, and many not be accessible to many universities and institutions due to the large safety risks.

AV4EV
=========
As a solution to the above problem, we propose an open design of a one-third scale autonomous go-kart platform based on an existing chassis provided by the company Topkart USA. Our modified go-kart platform supports a flexible range of sensing and computing, is capable of carrying a human driver, and is technically and financially friendly to universities and research institutions. This platform fills the gap between RC cars and full scale vehicular platforms,  while extending the research scope from modular pipeline development in racing competitions to end-to-end sensing and control outputs. In addition, it is paramount to provide not only a physical platform but also a development workflow that bridges this same gap. If a bridge platform’s software and workflow is too far removed from its full scale counterpart, the resources necessary vis-`a-vis developer effort, porting time, testing overhead, etc. can reduce inherent value provided by the bridge platform. As such, this work focuses on supporting repeatable development, testing, and deployment workflows for the go-kart platform software, including the base sys- tem, middleware and packages, the application layers and a simulation environment. This is achieved by focusing on modular containerized solutions which provide rich configu- ration options to citizen developers for a variety of use cases. This software-defined vehicle (SDV) approach is such that an application deployed on the go-kart can be used on another physical platform entirely (e.g. scooter, forklift, automobile) without having to build new applications from the ground up. 

This works makes the following contributions -

1. It is the first attempt in an effort of establishing a standardized open design for modular electrical vehicle platforms. 
2. It provides a complete sensing solution and open-source software to perform autonomous vehicle related perception, localization, planning, and control tasks.
3. It provides an open-standard hardware solution to adapt a one-third scale go-kart chassis to fulfill the gap between autonomous RC cars and full size vehicles.

Overview
=========
The go-kart mechatronics system is designed as a modular system, consisting of several subsystems that are responsible for different tasks. There are seven major subsystems: Power Distribution (PD), Main Control (MC), User Interface (UI), Throttle-by-Wire (TBW), Brake-by-Wire (BBW), and Steer- by-Wire (SBW), Rear-Shelf Design (RSD). The “x-by-wire” system design approach has been gaining popularity in the automotive industry which is to replace conventional mechanical and hydraulic control systems with electronic signals . The elimination of traditional mechanical components could increase control stability, in- crease design flexibility, reduce cost, and improve efficiency . In our go-kart drive-by-wire design, all subsystems except the PD and the RSD use an STM32 Nucleo development board on a standalone PCB as the electronic control unit (ECU). Like modern vehicle design, communication is achieved using the controller area network (CAN) to allow efficient information exchange between nodes . These modular control systems are integrated with the original go-kart chassis in a non- intrusive manner and are easy to understand, build, and modify. 

As described above the Gokart is a complex system with many subsystems. We will go into detail about the following subsytems in the Build-the-Kart section. We have linked the subsystems to their respective subpages for your convenience. 

.. note::
    
   The best way to go through the documentation is to read this Overview section first and then go through the Tutorial section. The Tutorial section will guide you through the process of building the Gokart in a step-by-step manner. 

* Power Distribution
* Upper Steer-by-Wire
* Lower Steer-by-Wire
* Brake-by-Wire
* Throttle-by-Wire

.. note::

   You can at any time delve deeper into the Build-the-Kart section for more information about the subsystems.

Github
==========
The Gokart is an open source project. The code is hosted on Github. You can find the repositories here.


* |Link1|
* |Link2|
* |Link3|


