Control Systems 
================

Except the Power Distrubtion System, we still have five control unit, Main Control (MC), User Interface (UI),
Throttle-by-Wire (TBW), Brake-by-Wire (BBW), and Steerby-Wire (SBW), they make up our control system. 

.. image:: vertopal_89473492f87843d38ce69ba576e4f6e0/media/Control_System_Main.png


The MC handles all the driving requests from the high-level end and sends out those commands (throttle, steering, brake)
on the CAN bus. It serves as an interface between the go-kart mechatronic system and the end user. Three different operation
modes are supported: manual, remote, and autonomous. In the manual mode, input is read from the steering wheel, throttle,
and brake pedals of a driver just like in any conventional vehicle. In the remote mode, the operator uses a Spektrum
DX6 2.4GHz radio to send the driving commands, which are received by the MC using an AR6200 receiver. In the
autonomous mode, the command is transmitted from a highlevel computing unit such as a laptop or a specialized onboard computer, 
through a USB to TTL communication. 
                    
 
User Interface Subsystem
~~~~~~~~~~~~~~~~~~~~~~~~~~

                    The UI is a customized PCB mounted on the side of the driver’s seat. 
                    It allows the user to select the desired operating mode using the toggle switches. 
                    Meanwhile, it collects real- time go-kart state information, including its speed, steering, and 
                    brake and display them on an LCD panel. It plays no role in mechanical control and is solely 
                    used for user monitoring and interaction.

Throttle-by-Wire Subsystem
~~~~~~~~~~~~~~~~~~~~~~~~~~~

                    The UI is a customized PCB mounted on the side of the driver’s seat. 
                    The TBW controls the go-kart’s main drive motor. The TBW’s Nucleo receives 
                    the desired speed from the CAN bus and sends out the measured speed. Speed 
                    measurement is achieved using a hall effect wheel speed sensor mounted 
                    close to the go-kart’s rear shaft. Speed control is performed using a 
                    closed PID loop. The output of the Nucleo is a PWM signal with a varying 
                    duty cycle which is then converted into a 0-5V analog voltage. This analog 
                    voltage is passed into the Alltrax SR48300 DC Motor Controller for speed control.
                    Another design is a remote kill switch which allows the operator to remotely cut off 
                    the power if an emergency occurs. This is implemented using a remote relay that can 
                    disconnect the switch to the motor contact which instantly stops power delivery to 
                    the main power. This part is independent from the MC and will continue functioning 
                    in a worst-case system failure.

Steer-by-Wire Subsystem
~~~~~~~~~~~~~~~~~~~~~~~~

                    The original unmodified go-kart platform uses an alloy shaft to connect the steering wheel 
                    and the front wheel. Steering is made possible entirely through the driver’s torque input. 
                    In order to provide an autonomous mode, a motor must be added to actuate the steering. Several 
                    design ideas have been composed: one attempt was to mount the motor parallel to the steering shaft 
                    and use a belt or chain for motion transmission.
