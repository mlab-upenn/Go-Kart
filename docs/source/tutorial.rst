Tutorial
==============

In this page, we will document the whole process on how to build the Gokart project from scratch. We will go through the whole Electrical & Mechanical pipeline and then move on to testing the stack by running pre-build software algorithms.
The tutorial is structured such that the researcher/student looking to build this platform has an overview of the whole system and at the same time deep dive into any particular category of interest at any point in time.

Verions:
- 1.0: Initial version : Purchased from TopKart [Link]
- 2.0: 2022 version : Autonomous reactive Gokart 
- 3.0: 2023 version : Autonomous Gokart 

Following steps take you to individual sections of the tutorial:

1. Bill of Materials (BOM)
2. Software Requirements
    a. SolidWorks
    b. VSCode or editor of your choice
    c. STM32CubeIDE
    d. VESC tool
    e. Altium Designer
    f. 3D printer software like MakerBot
3. Vechicle Restructure
    a. Remove the motor
    b. Remove the front and rear plastic bumps
    c. Remove steering system
4. Subsystem designs
    a. Throttle-by-Wire (TBW)
        * Mechanical assembly
        * Electrical assembly
    b. Brake-by-Wire (BBW)
        * Mechanical assembly
        * Electrical assembly
    c. Steering-by-Wire (SBW)
        * Upper Steer Assembly 
            + Mechanical assembly
            + Electrical assembly
        * Lower Steer Assembly
            + Mechanical assembly
            + Electrical assembly
    e. Battery pack
    f. Power Distribution Unit (PDU)
        * Electrical assembly
    g. Rear shelf design (RSD)
        * Mechanical assembly
        * Electrical assembly

5. High level system design
    a. Sensor Assembly
    b. Communication 
    c. Control System 
    d. MCU

6. Testing
