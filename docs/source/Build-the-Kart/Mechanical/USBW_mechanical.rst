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

It's most convenient to almost-entirely assemble this component first offboard, then attach it together to the existing GoKart. The steps can be laid out as follows:

Step 1:

Step 2:




All 3D printed


