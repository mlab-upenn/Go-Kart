Vehicle Assembly
===================

The document describes the assembly of the TopKart vehicle. The assembly is divided into the following sections:


1. Build the TopKart
-------------------
The main chassis that we will be using will be from TopKart. You can find additional data and which compenents you would be needing in the BOM section. The assembly of the chassis is pretty straight forward and can be done by following the instructions in the manual. There are also videos from the manufacturer and it is advised that you watch them before starting the assembly.

TopKart setup guide - Go to http://topkartusa.net/adult-setup-guide/

`How to videos <https://www.youtube.com/playlist?list=PLrHWloGpgEJ33L9B9TJtqOFAmeYjiv5M->`_

2. Test manual control
-------------------

It is important to test out the manual control of the vehicle before starting the assembly of the autonomous system. This will help you understand the vehicle better and also help you debug any issues that you might face during the assembly of the autonomous system. It removes the assumption that there could be a potential fault in the base setup. We have unit tests designed for each of our subsystem so this should be a good way to test out the manual control.

By driving manual you can also get a good idea about tuning, oiling and other maintenance that you might need to do on the vehicle.


3. Remove the motor
-------------------

.. note:: 

    This step is only required if you are using the TopKart brushed motor. If you are directly working on the BLDC motor that we are suggesting then you can skip this step.

Dismount the Brushed motor from the setup. You can follow the instructions in the manual to do this. You will need to remove the chain and the sprocket from the motor. You can also remove the chain guard and the motor mount. You can keep the motor mount as we will be using it for mounting the BLDC motor.

4. Remove the front and rear plastic bumps
-------------------

Removing the front and rear plastic bumps will give you more space to mount the electronics. This step should be trivial.


5. Remove steering system
-------------------

Steering system will be modified and broken down into 2 sections i.e. Upper steer by wire and Lower steer by wire. Remove the steering system by following the reverse steps mentioned in the setup manual pointed to above.