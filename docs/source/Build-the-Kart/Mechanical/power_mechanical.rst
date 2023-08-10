==================================
Power Mechanical Assembly
==================================


Safety disclaimer:  
=================

.. warning::

   Especially when connected in series, these batteries create very high voltages. When
   connected accidentally in certain configurations (such as through a human body, via your arms),
   you can close the loop and short the circuit, withstanding 48V. It is highly recommended that
   you exercise caution, namely by (1) wearing electrically-insulating gloves, (2) touching only 
   one part at a time, and (3) avoiding wire clutter and/or damage.

The go-kart is powered by six (nominally) 12V LiPo batteries. Specifically, 4 batteries are arranged in series to supply 48V powering all the motors, and 2 batteries are connected in series powering everything else; for more on this, see the Electrical section (TODO Insert Link) We chose to use LiPo batteries since they are lighter, and have higher capacity than lead acid batteries as suggested by TopKart.

Please find all CAD in the /CAD/Battery_Box folder. Namely you will find the SolidWorks part file (.SLDPRT) as well as engineering drawings (.SLDDRW and .PD) for all four unique components (described below). These components started as raw rectangular Aluminum sheet metal stock (1mm thick), then in a university machine shop, we cut the sheets to size and manually drilled the holes. Note that for repeated parts (namely the two vertical sheets, which are 4x each), it can save you time to drill through all 4 sheets at once. In addition, t-slot frames are needed, and must be cut to length (imprecise tolerances are okay here). Recall our general tips for working with t-slots (TODO Insert link here) 


LEFT SIDE: BATTERY BOX

Step 1: Locate the "floor sheet left" sheet metal part. Oriented flat, attach it to the corresponding chassis component using four standard M5 nuts and screws.
Step 2: Cut four t-slots to 6" each, and attach them vertically to the floor sheet left, as shown in the image below. Only two t-slots are visible, but the other two follow trivially by symmetry.
Step 3: Cut two t-slots to 10" each, and attach them horizontally to the t-slots from Step 2, as shown in the image below.
Step 4: Locate two "vertical sheet front and back" sheet metal parts, and screw them in to the t-slots from Step 3, as shown in the image below. You should then apply a layer of duct tape over the top of the sheet, to ensure it doesn't create electrical interference later on. At this point, your assembly should look exactly like the image below.

TODO insert image power_left_1

Step 5: Cut two t-slots to 19" each, and attach them horizontally to the t-slots from Step 3, as shown in the image below.
Step 6: Locate two "vertical sheet sides" sheet metal parts, and screw them in to the t-slots from Step 5, as shown in the image below. You should then apply a layer of duct tape, just like before. At this point, your assembly should look exactly like the image below.

TODO insert image power_left_2

RIGHT SIDE: BATTERY BOX



LEFT SIDE: LIPO BATTERIES


Word of advice:  
=================

.. warning::
Before assembling the six batteries themselves, make sure its sensible given your immediate goals. The batteries total more than 60lb, which is over 1/3 of the gokart's total weight when fully assembled. So if you will need to physically pick up the car, doing so without the batteries will make your job easier (and require only 2 people instead of 3). Also, once you connect the batteries in series, the resulting 48V potential difference creates a safety hazard, which you might want to prefer whenever you're working without running tests.

Step 7: Locate one LiPo battery, and using its rubber handle, place it with the red terminal in the very back left corner, as shown in the image below.

TODO insert image power_left_3

Step 8: Locate two more batteries, and while still offboard, connect them as shown in the image below. Simply screw that battery terminal's screw back in, over the corresponding wire's circular terminal. You can keep this very short connection forever moving forward, besides while charging individual batteries, which saves one step during all subsequent battery installation/removal processes.

TODO insert image power_left_4

Step 9: Place these two batteries (while still connected) into the battery box, as shown in the image below. Make sure the available terminals are on the right (inner) side, for smoother in-series connection with the right side batteries.

TODO insert image power_left_5

Step 10: For the top two batteries, connect each one's remaining terminal to its corresponding wire, as laid out in the Electric section of this documentation (TODO Insert link here). Note that the voltages shown below will be generated as a result, so be very careful. Make sure to 

Step 11: Connect the two terminals from the bottom battery, to their corresponding wires. 

TODO insert image power_left_6


Make sure to mention order of battery installation and removal


Mention importance of routing wires through battery handles and
through aluminum profile slots, to avoid clutter and EMI interference

Mention washers under screws

Mention switch for supplemental components

Include overhead diagram of voltage across batteries, from 0 to 48V



RIGHT SIDE

Mention assymetry of left vs right bottom plate

Mention vertical t-slot, for wire routing

Mention avoiding conflict with narrow end of chain

Commentary on disconnecting out of order