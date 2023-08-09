==================================
Brake-by-Wire
==================================

The base go-kart frame converts the movement from the driver pressing the brake pedal through the push rod to the
master cylinder and reservoir to create a hydraulic braking pressure without the assistance of any additional servos.
In order to build a system that supports effective autonomous braking without human input, an electro-hydraulic braking
system needs to be designed. However, designing such as system can be mechanically challenging and
restricted by the existing go-kart structure. 
An alternate design proposed is a linear actuator (LA) which is mounted at the end of the hydraulic push rod and creates
a linear movement mimicking the driver pressing the pedal. This approach is inexpensive and easy-to-add. In our design,
an LA with a 2-inch stroke & 50 lbs force LA from Progressive Automation is used, which can hold its position and withstand
up to 1500 lbs of force. This allows the LA to hold a certain braking state without additional current input, thus avoiding
overheating problems. The system is non-intrusive, which means that the driver (if any) can always press the brake pedal
regardless of the LA state and stop the go-kart. 
Automatic braking control is achieved using the LA’s built-in position potentiometer and an external brake pressure sen-
sor. Due to the nature of a hydraulic braking system, there is a non-linear relationship between the pedal press and the
pressure generated. Therefore, empirical data were collected for different LA positions and the corresponding braking
pressures and approximated using a piecewise function. In a brake control loop, an LA position is computed based on the desired braking pressure and then controlled like a regular
motor.

.. note::

    Assemble the mechanical system first and then the electrical system.    

Mechanical Assembly
=========
Link mechanical


Electrical Assembly
=========
:doc:`Build-the-Kart/Electrical/BBW_electrical`
