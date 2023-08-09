==================================
Throttle-by-Wire
==================================

The Throttle-by-Wire subsystem ensures that the Go-Kart can be controlled using control inputs on a wire. The TBW controls the go-kart’s main drive motor. The TBW’s Nucleo receives the desired speed from the CAN bus and sends out the measured speed. Speed measurement is achieved using a hall effect wheel speed sensor mounted close to the go-kart’s rear shaft. Speed control is performed using a closed PID loop. The output of the Nucleo is a PWM signal with a varying duty cycle which is then converted into a 0-5V analog voltage. This is supplied to the VESC 75_300 controller which in turn drives the motor. The system also gets feedback from the internal sin-cosin encoder which is fed into the comm port of the VESC 75_300.
Another design is a remote kill switch which allows the operator to remotely cut off the power if an emergency occurs.
This is implemented using a remote relay that can disconnect the switch to the motor contact which instantly stops power
delivery to the main power. This part is independent from the MC and will continue functioning in a worst-case system
failure.

.. note::

    Assemble the mechanical system first and then the electrical system.    

Mechanical Assembly
=========
Link mechanical


Electrical Assembly
=========

:doc:`Build-the-Kart/Electrical/TBW_electrical`