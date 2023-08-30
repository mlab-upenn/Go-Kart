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

The Lower Steer-By-Wire subsystem is critical since it solely holds the power to redirect the car's motion left or right, in each of the three possible modes: manual, remote, and autonomous. It does so by rotating the rotor of a `BLCD motor,<https://www.revrobotics.com/rev-21-2100/>`_ which axially translates two tie rods, which simultaneously angles both front wheels left or right. In addition, the LSBW system gathers feedback on its rotation, enabling a PID controller to ensure convergence to the desired angle. The sensor chosen is the `AS5047P Magnetic Rotary Position Sensor,<https://www.digikey.com/en/products/detail/ams-osram/AS5047P-TS-EK-AB/5452344>`_ which tracks angular motion of the rotor via a locally fixed magnet, and sends that information by wire directly to the LSBW nucleo. (TODO Insert links here!). In order for all these active components to assemble cleanly with each other, then with the existing GoKart chassis, various mounting components, including several t-slot frames, were designed. Instructions for full assembly of this system can be found below. Note that the entire system is perfectly symmetrical about the vertical front-facing plane of the car. For convenience, I will often simplify explanations by focusing on the right side (from the car's perspective) of the LSBW assembly, with the implication that the left side is a mirror image. I'll first describe assembly of the bottom half, which is composed primarily of t-slot frames and serves mostly as mechanical support for the top half's more active components:

You can view the full CAD assembly at `this link <https://drive.google.com/file/d/1bHC2BbAlqdqfvbhz8IPRuZGqOGFy7LD8/view?usp=drive_link>`_

TODO Update this after making some necessary changes!

BOTTOM HALF ASSEMBLY

Step B1: First, build the base level of the mount. You'll have to cut four t-slots, two of length 165mm and two of length 56mm, and arrange them horizontally as shown in the image below. This subassembly allows for the active components above to connect to the provided blue TopKart chassis on either side; although this connection itself will take place in a later step.

.. image:: ../imgs/Mechanical/LSBW_CAD_B1
    :width: 100%
    :align: center
    :alt: Lower Steer By Wire Assembly Step B1

Step B2: Next, cut six t-slots of length 60mm, and attach them vertically around the outer perimeter of the base. Specific position dimensions can be found in the assembly linked above, although they're easily adjustable later and imprecision is fine.

.. image:: ../imgs/Mechanical/LSBW_CAD_B2
    :width: 100%
    :align: center
    :alt: Lower Steer By Wire Assembly Step B2

Step B3: Now cut four more t-slots, two of length 70mm and two of length 56mm, and assemble them as shown below. Note that the 70mm t-slots are on the GoKart's left and right (i.e. touching the vertical t-slots from Step 2), and the 55mm t-slots are in between them in the front and back. Note also that the backmost t-slot is not a critical component, so you can bypass this if assembly proves too difficult. Once you have this subassembly complete, attach it just inside of the vertical t-slots.

.. image:: ../imgs/Mechanical/LSBW_CAD_B3
    :width: 100%
    :align: center
    :alt: Lower Steer By Wire Assembly Step B3

Step B4: Cut four more 4 t-slots, two of length 260mm and two of length 56mm, then arrange them in a rectangle as shown below. Then attach them to the four vertical t-slots near the front. For now, ignore the U-bolts shown in the CAD, unless this long rectangle starts to act as a bending cantilever, in which case you should skip to steps 5 and 6 (bottom half) and step 2 (full assembly) to attach the complete LSBW bottom half to the blue TopKart chassis frame.

.. image:: ../imgs/Mechanical/LSBW_CAD_B4
    :width: 100%
    :align: center
    :alt: Lower Steer By Wire Assembly Step B4

Step B5: Cut four more t-slots, each of length 60mm, and assemble them as two "L" pairs, as shown below. Then using four custom machined t-slot brackets, `two copies <https://github.com/mlab-upenn/gokart-mechatronics/blob/main/Mechanical/SBW%20-%20lower/Drawings/L_Pair_Bottom_Mount.pdf>`_ of "L-Pair Bottom Mount" and `two copies <https://github.com/mlab-upenn/gokart-mechatronics/blob/main/Mechanical/SBW%20-%20lower/Drawings/L_Pair_Top_Mount.pdf>`_ of "L-Pair Top Mount," attach both L pairs to the t-slot base from Step 1. You will also need five M5 nuts and bolts per bracket for t-slot mounting, and the left and right sides are perfectly symmetric.

.. image:: ../imgs/Mechanical/LSBW_CAD_B5a
    :width: 100%
    :align: center
    :alt: Lower Steer By Wire Assembly Step B5
.. image:: ../imgs/Mechanical/LSBW_CAD_B5b
    :width: 100%
    :align: center
    :alt: Lower Steer By Wire Assembly Step B5
.. image:: ../imgs/Mechanical/LSBW_CAD_B5c
    :width: 100%
    :align: center
    :alt: Lower Steer By Wire Assembly Step B5

Step B6: Also, you should add an extra support for the BLCD near its front, namely a long t-slot connector screwed in with two M5 screws. We used a rectangular t-slot connector, similar to `these from Amazon <https://www.amazon.com/4040-Aluminum-Extrusion-Connector-Included/dp/B09Y1PC4FN/ref=sr_1_1_sspa?crid=3PMOGEU95L2V2&keywords=t-slot%2Bbracket&qid=1692302964&sprefix=t-slot%2Bbracket%2Caps%2C94&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1>`_ except for the shape, but unfortunately cannot find these of precise dimensions anywhere online, so you might have to custom machine it, using this engineering drawing. However this part is purely a safety measure which isn't strictly necessary, so you can optionally skip it entirely.

TODO Mock up some CAD, and link from here and within assembly, 100mm by 22.3mm, with spacing of 25mm between holes, 4 holes in total, 5mm thick material, copy the material from the other t-slot brackets
TODO Get a picture of this!



TOP HALF ASSEMBLY

Step T1: Attain welded shalf, see subassembly (TODO add CAD link). This consists of four metal parts: (1) "steering shaft," a hollow metal pipe, (2) "tie_rod_turner," 2x, provided by TopKart (TODO double check this, and think about shaft assembly), and (4) "hexagonal shaft" (provided by motor company, TODO double check this). You can probably get a local machine shop to weld these parts for you.

.. image:: ../imgs/Mechanical/Welded_part
    :width: 100%
    :align: center
    :alt: Lower Steer By Wire Assembly Step T1

Step T2: Locate 2 `heim joints <https://shop.topkartusa.net/products/heim-joints>`_, two screws (link coming shortly) and several spacing features such as washers. Separately on both sides of the LSBW assembly, attach one heim join right in between, with the nut facing out. To do so, get it in position, surrounded by all necessary spacing features, then pass the screw in from one end, then tighten it from the other with a nut.

.. image:: ../imgs/Mechanical/Heim_connection
    :width: 100%
    :align: center
    :alt: Lower Steer By Wire Assembly Step T2

Step T3: Press fit the "sleeve front" and "sleeve back," both 3D printed, STL coming soon, from either end of the shaft, so each is flush with the tie_rod_turners.

Step T4: Attain four parts: two bearings (purchased, link coming soon), and two copies of "bearing mount," a custom metal part. Then press fit the bearings into the bearing mounts, separately.

Step T5: Press fit the bearing pockets around the welded shalf, until they're touching the 3d printed sleeves.

.. image:: ../imgs/Mechanical/LSBW_IRL_T5.jpeg
    :width: 100%
    :align: center
    :alt: Lower Steer By Wire Assembly Step T5

Step T6: From the AS5047P sensor kit, locate the magnet, and also attain the 3d printed (STL coming soon) "magnet mount" part. Insert the magnet into its mount using some tape, then insert its mount into the welded shalf using a pin.

.. image:: ../imgs/Mechanical/LSBW_IRL_T6.jpeg
    :width: 100%
    :align: center
    :alt: Lower Steer By Wire Assembly Step T6

Step T7: Locate the motor, and attach the welded shaft into it, via its hexagonal shaft. This might require using a pin, and/or temporarily dissembling a portion of the motor. Note that our CAD is slightly off, since it includes only 3 gearboxes, whereas in real life we used 4 gearboxes.

.. image:: ../imgs/Mechanical/LSBW_IRL_T7.jpeg
    :width: 100%
    :align: center
    :alt: Lower Steer By Wire Assembly Step T7

Step T8: Locate the "BLDC Mount - V9" custom machined part, engineering drawing coming soon. Then using 3 screws per side, connect it from underneath to the motor.

.. image:: ../imgs/Mechanical/LSBW_IRL_T8.jpeg
    :width: 100%
    :align: center
    :alt: Lower Steer By Wire Assembly Step T8

Step T9: Attain the "AS5047P mount," 3D printed with STL coming soon. Also attain the AS5047P sensor board, and extract whatever wires will connect this to the nucleo, passing them through the mount's rectangular pocket; then screw that sensor onto the outer (i.e. further from the base holes) side of the mount, using 4 small screws. Then attain the LSBW PCB (including its nucleo MCU), and after completing the aforementioned connections, screw this onto the inner side of the mount, using 4 small screws; you might need to leave a small gap for the nuts from the AS5047P mounting, this is fine. Note also that the part from this Step 9 is unconnected to those from Steps 1-8, which are themselves all connected.

.. image:: ../imgs/Mechanical/LSBW_IRL_T9a.jpeg
    :width: 100%
    :align: center
    :alt: Lower Steer By Wire Assembly Step 
.. image:: ../imgs/Mechanical/LSBW_IRL_T9b.jpeg
    :width: 100%
    :align: center
    :alt: Lower Steer By Wire Assembly Step 

FULL ASSEMBLY

Step F1: To attach the entire top half assembly to the entire bottom half assembly, simply locate twelve M5 screws, nuts, and washers, then screw in everything as shown below. Note that the AS5047P magnet and board must be between 0.5mm and 3mm apart.

.. image:: ../imgs/Mechanical/LSBW_IRL_F1.jpeg
    :width: 100%
    :align: center
    :alt: Lower Steer By Wire Assembly Step F1

Step F2: To attach the entire LSBW assembly to the GoKart chassis in the front, recreate the two connection shown in the first image below. The first two are circled near the front, and each contains one U-bolt and one mount plates (links coming shortly), with two nuts for tightening. In accordance with the second image below (but notably missing in our CAD), you should also insert a long t-slot connector (link coming soon) as shown below, below the very front of the LSBW assembly, held in place by the weight on top of it.

.. image:: ../imgs/Mechanical/LSBW_IRL_F2.jpeg
    :width: 100%
    :align: center
    :alt: Lower Steer By Wire Assembly Step F2

Step F3: To attach the entire LSBW assembly to the GoKart chassis in the back, recreate the connection circled in the image below (and its mirror image), involving press fitting the LSBW system into the chassis via these two t-slot "arms" so to speak. We also used a large black rubber washer on either tight, to deform and facilitate tight connection. Assembly might require some wiggling around, and/or temporary removal of some t-slot connections.

.. image:: ../imgs/Mechanical/LSBW_IRL_F3.jpeg
    :width: 100%
    :align: center
    :alt: Lower Steer By Wire Assembly Step F3

Step F4: Connect the two `tie rods <https://sharkshifter.com/products/tie-rods-alum-hex-8mm-go-kart?variant=37384922628262>'_ to the heim joins on either side, by simply screwing them in. As the end, screwing in to the wheel connector should notably occur on the outermost of the two holes, as shown below. TODO insert some more tips on calibrating the tie rod length, based on what George taught me.

.. image:: ../imgs/Mechanical/LSBW_IRL_F4.jpeg
    :width: 100%
    :align: center
    :alt: Lower Steer By Wire Assembly Step F4
