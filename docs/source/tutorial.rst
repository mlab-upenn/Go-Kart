Tutorial
==============

In this page, we will document the whole process on how to build the Gokart project from scratch. We will go through the whole Electrical & Mechanical pipeline and then move on to testing the stack by running pre-build software algorithms.
The tutorial is structured such that the researcher/student looking to build this platform has an overview of the whole system and at the same time deep dive into any particular category of interest at any point in time.

Versions 
-----------------

* 1.0: Initial version : Purchased from TopKart [Link]
* 2.0: 2022 version : Autonomous reactive Gokart 
* 3.0: 2023 version : Autonomous Gokart 

Following steps take you to individual sections of the tutorial:

1. **Step 1** :doc:`Bom`    
    
2. **Step 2** :doc:`soft_req`

    a. SolidWorks
    b. VSCode or editor of your choice
    c. STM32CubeIDE
    d. VESC tool
    e. Altium Designer
    f. 3D printer software like MakerBot
    
3. **Step 3** : :doc:`vehicle_assembly`
    
    a. Build the TopKart
    b. Test manual control
    c. Remove the motor
    d. Remove the front and rear plastic bumps
    e. Remove steering system

4. **Step 4** : Subsystem designs 
    a. :doc:`Build-the-Kart/TBW` (TBW) 
        * Mechanical assembly
        * Electrical assembly
        * Unit testing
    b. :doc:`Build-the-Kart/BBW` (BBW)
        * Mechanical assembly
        * Electrical assembly
        * Unit testing
    c. :doc:`Build-the-Kart/SBW` (SBW)
        * Upper Steer Assembly 
            + Mechanical assembly
            + Electrical assembly
            + Unit testing
        * Lower Steer Assembly
            + Mechanical assembly
            + Electrical assembly
            + Unit testing
    e. **Battery pack**
    f. Power Distribution Unit (PDU)
        * Electrical assembly
        * Unit testing
    g. Rear shelf design (RSD)
        * Mechanical assembly
        * Electrical assembly
        * Unit testing

5. **Step 5** : Vehicle System Integration - Putting it all together!
    a. :doc:`Build-the-Kart/Software/Compute`
    b. :doc:`Build-the-Kart/Software/Communication`
    c. :doc:`Build-the-Kart/Software/MCU`
    d. :doc:`Build-the-Kart/Software/Control`

6. **Step 6 : Testing**
