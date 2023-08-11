Lower Steer By Wire (L-SBW) Assembly
==================================

This is the assembly of the Lower Steer By Wire (L-SBW) Assembly in CAD. The assembly is shown below:

.. image:: ../imgs/Mechanical/lsbw.png
    :width: 100%
    :align: center
    :alt: Lower Steer By Wire Assembly


This is the real life assembly of the L-SBW Assembly:

.. image:: ../imgs/Mechanical/SBW_1.jpg
    :width: 100%
    :align: center
    :alt: Lower Steer By Wire Assembly

.. image:: ../imgs/Mechanical/SBW_2.jpg
    :width: 100%
    :align: center
    :alt: Lower Steer By Wire Assembly

You can also view the exploded video view of the Assembly `here <https://drive.google.com/file/d/1VRoe71nf696cDpKYZVToyhxTrEUwtiuE/view?usp=sharing>`_

The Lower Steer-By-Wire subsystem is critical since it solely holds the power to redirect the cars motion left or right, in each of the three possible modes: manual, remote, and autonomous. It does so by rotating the rotor of a BLCD motor, which axially translates two tie rods, which simultaneously angles both front wheels left or right. In addition, the LSBW system gathers feedback on its rotation, enabling a PIDcontroller to ensure convergence to the desired angle. The sensor chosen is the AS5047P Magnetic Rotary Position Sensor, which tracks angular motion of the rotor via a locally fixed magnet, and sends that information by wire directly to the LSBW nucleo. (TODO Insert links here!). In order for all these active components to assemble cleanly with each other, then with the existing GoKart chassis, various mounting components, including several t-slot frames, were designed. Instructions for full assembly of this system can be found below. Note that the entire system is perfectly symmetrical about the vertical front-facing plane of the car. For convenience, I will often simplify explanations by focusing on the right side (from the car's perspective) of the LSBW assembly, with the implication that the left side is a mirror image.

You can view the full CAD assembly at this link: (TODO Insert Drive link with CAD)

BOTTOM HALF ASSEMBLY

Step 1: Build the base level of the mount. This consists of four t-slots: x length and y length of z quantity

Step 2: 6 vertical t-slots, of length x 

Step 3: 4 t-slots, two of length x and two of length y

Step 4: 4 t-slots, two of length x and two of length y

Step 5: 4 t-slots, two of length x and two of length y

Step 6: Also, you should add an extra support for the BLCD near its front, namely a long t-slot connector (link coming soon) screwed in with two M5 screws


TOP HALF ASSEMBLY

Step 1: Attain welded shalf, see subassembly (TODO add CAD link). This consists of four metal parts: (1) "steering shaft," a hollow metal pipe, (2) "tie_rod_turner," 2x, provided by TopKart (TODO double check this, and find the link), and (4) "hexagonal shaft" (provided by motor company, TODO double check this). You can probably get a local machine shop to weld these parts for you.

Step 2: Locate 2 heim shalfs (link below), two screws (link coming shortly) and several spacing features such as washers. Separately on both sides of the LSBW assembly, attach one heim join right in between, with the nut facing out. To do so, get it in position, surrounded by all necessary spacing features, then pass the screw in from one end, then tighten it from the other with a nut.
Heim joint: https://shop.topkartusa.net/products/heim-joints

Step 3: Press fit the "sleeve front" and "sleeve back," both 3D printed, STL coming soon, from either end of the shaft, so each is flush with the tie_rod_turners.

Step 4: Attain four parts: two bearings (purchased, link coming soon), and two copies of "bearing mount," a custom metal part. Then press fit the bearings into the bearing mounts, separately.

Step 5: Press fit the bearing pockets around the welded shalf, until they're touching the 3d printed sleeves.

Step 6: From the AS5047P sensor kit, locate the magnet, and also attain the 3d printed (STL coming soon) "magnet mount" part. Insert the magnet into its mount using some tape, then insert its mount into the welded shalf using a pin.

Step 7: Locate the motor, and attach the welded shaft into it, via its hexagonal shaft. This might require using a pin, and/or temporarily dissembling a portion of the motor. Note that our CAD is slightly off, since it includes only 3 gearboxes, whereas in real life we used 4 gearboxes.

Step 8: Locate the "BLDC Mount - V9" custom machined part, engineering drawing coming soon. Then using 3 screws, connect it from underneath to the motor.

Step 9: Attain the "AS5047P mount," 3D printed with STL coming soon. Also attain the AS5047P sensor board, and extract whatever wires will connect this to the nucleo, passing them through the mount's rectangular pocket; then screw that sensor onto the outer (i.e. further from the base holes) side of the mount, using 4 small screws. Then attain the LSBW PCB (including its nucleo MCU), and after completing the aforementioned connections, screw this onto the inner side of the mount, using 4 small screws; you might need to leave a small gap for the nuts from the AS5047P mounting, this is fine. Note also that the part from this Step 9 is unconnected to those from Steps 1-8, which are themselves all connected.


PUTTING IT ALL TOGETHER

Step 1: To attach the entire top half assembly to the entire bottom half assembly, simply locate twelve M5 screws, nuts, and washers, then screw in everything as shown below. Note that the AS5047P magnet and board must be between 0.5mm and 3mm apart.

Step 2: To attach the entire LSBW assembly to the GoKart chassis in the front, recreate the two connection shown in the first image below. The first two are circled near the front, and each contains one U-bolt and one mount plates (links coming shortly), with two nuts for tightening. In accordance with the second image below (but notably missing in our CAD), you should also insert a long t-slot connector (link coming soon) as shown below, below the very front of the LSBW assembly, held in place by the weight on top of it.

Step 3: To attach the entire LSBW assembly to the GoKart chassis in the back, recreate the connection circled in the image below (and its mirror image), involving press fitting the LSBW system into the chassis via these two t-slot "arms" so to speak. We also used a large black rubber washer on either tight, to deform and facilitate tight connection. Assembly might require some wiggling around, and/or temporary removal of some t-slot connections.

Step 4: Connect the two tie rods (link below) to the heim joins on either side, by simply screwing them in. As the end, screwing in to the wheel connector should notably occur on the outermost of the two holes, as shown below. TODO insert some more tips on calibrating the tie rod length, based on what George taught me.

Tie rod: https://sharkshifter.com/products/tie-rods-alum-hex-8mm-go-kart?variant=37384922628262
