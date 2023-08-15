Upper Steer By Wire (U-SBW) Assembly
==================================

This is the assembly of the Upper Steer By Wire (U-SBW) Assembly in CAD. The assembly is shown below:

.. image:: ../imgs/Mechanical/usbw.png
    :width: 100%
    :align: center
    :alt: Upper Steer By Wire Assembly

You can also view the exploded video view of the Assembly `here <https://drive.google.com/file/d/1NHFZQ1OP3V632oppj7N01TcItQowJsK4/view?usp=sharing>`_

This is the real life assembly of the L-SBW Assembly:

.. image:: ../imgs/Mechanical/SBW_3.jpg
    :width: 100%
    :align: center
    :alt: Upper Steer By Wire Assembly

.. image:: ../imgs/Mechanical/SBW_4.jpg
    :width: 100%
    :align: center
    :alt: Upper Steer By Wire Assembly

The Upper Steer-By-Wire is critical in order to interface with a human driver. The subsystem relies heavily on its steering wheel, which accepts user rotational input, captured by a quadrature encoder, and subsequently transmitted via the U-SBW Nucleo to the main GoKart nucleo. Within the parallel L-SBW subsystem, this signal then maps to some rotation of the front wheels, steering the car. Importantly, the encoder is actually nested within a Pololu motor (TODO Insert link), allowing the GoKart to actuate steering wheel rotation even without human input.

This features creates potential for future "hybrid-autonomy" mode implementation, where the GoKart used higher-level sensor input (LiDAR, camera, etc) to perceive its environment then plan and follow a path autonomously, but emply an onboard human driver for assistance. Since the steering wheel movements correspond with the car turns, a human driver can manually override these signals if necessary, for example if their intuition suggests that a more of less aggressive maneuver is necessary. By collecting this data, reinforcement learning can be implemented to teach the GoKart these intuitive maneuvers and improve the fully-autonomous mode moving forward.

Note that almost all components of this subsystem are 3D printed from plastic; Strong metal materials are unnecessary since this components carries a very small load, plus this subassembly is hanging in the air, so we prioritized weight reduction. In terms of assembly, it's most convenient to almost-entirely assemble this component first offboard, then attach it together to the existing GoKart. The steps can be laid out as follows:

Step 1: First, you will assemble the two primary structural components. These are called "beam" and "Pololu mount," both 3D printed, STL files coming soon, and both are circled in red and highlighted in light blue below. To attach them, simply use 8 screws (TODO figure out screw type) and nuts, fixturing through the provided 8 holes.

TODO Insert image USBW_CAD_1

Step 2: Locate the Pololu DC motor (TODO attach link), and attach it to the Pololu mount using 6 screws (TODO identify screw type). TODO Figure out rotor connection mechanism

TODO Insert image USBW_IRL_2.jpeg

Step 3: Locate the two identical "beam link" parts, 3D printed with STL coming soon, and attach them to the beam using four screws (two per side), TODO determine screw type. Note that the other, larger three holes are still vacant, these will be connected at a later step.

TODO Insert image USBW_CAD_3

Step 4: In a separate subassembly, connect the "coupler" (3D printed, STL coming soon) and the "D-shaft hub" (purchased, link coming soon). This can be done using four screws (type TBD). Note that you will have to thread the 3D printed coupler part, which can simply be done using the screw itself, after 3D printing a slightly undersized hole (TODO confirm this, check CAD for the part)

TODO Insert image USBW_IRL_4.jpeg

Step 5: Connect the two subassemblies from the previous steps. This can be done by inserting the hub around the motor's shaft, then screwing it in using two (TODO insert screw name) screws. Note that the coupler subassembly is not yet secure, so be extra careful until it accepts the steering wheel shaft.

TODO Insert USBW_IRL_5.HEIC

Step 6: Locate the "shaft mount" part (3D printed, STL coming soon), and using a single (TODO) screw and nut with several spacing features, attach it in between the two beam mounts, via their back top hole. Note that the shaft mount still has 1 degree of freedom; don't worry, this will be removed shortly.

Step 7: Locate the "sw shaft" part (metal pipe, engineering drawing coming soon), and connect it into the assembly. Slide it first into the shaft mount, then into the coupler. Next, use a (TODO) screw and nut to attach the coupler and pipe.

Step 8: In a new subassembly, connect the "steering wheel" to the "steering wheel mount," both parts provided by TopKart (TODO check they're both provided, and check the material). This can be done using three (TODO) screws and nuts.

Step 9: Connect this new steering wheel assembly to the remaining assembly by passing the steering wheel mount around the sw shaft, and connecting them via a single screw and nut. 

Step 10: Create a new subassembly for the boards. For this, you'll need the USBW PCB (custom designed, see Electrical section of documentation), the Pololu motor driver (comes with motor purchase), and the "PCB mount" (custom, 3D printed, STL link coming soon). First, make sure all components necessary are soldered to the PCB. Note that the Pololu driver is soldered to the back, but everything else (including nucleo, CAN bus ports, etc) is on the front. It is recommended that you use some black solder elevation/bridge parts in between parallel components, as we did. After the electronics are all assembled, attach them (via the USBW PCB) to the PCB mount, via 4 screws, nuts, and standoffs. The motor driver will fit nicely into the mount's large rectangular pocket. Your result should look similar to the next two images below.

TODO: Insert image USBW_IRL_10.jpeg

Step 11: Connect this new PCB subassembly with the remaining assembly using 4 screws and nuts (TODO get type of screw) near the bottom. 

TODO: Insert image USBW_IRL_11.jpeg

Step 12: Now you're ready to connect the full USBW assembly into the preexistent GoKart assembly. This will require three final connections to be made

Step 12a: Place 

Steps 12b and 12c:


