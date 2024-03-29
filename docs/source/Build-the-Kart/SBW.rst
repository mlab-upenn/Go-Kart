==================================
Steer-by-Wire
==================================

The original unmodified go-kart platform uses an alloy shaft to connect the steering wheel and the front wheel. Steering is made possible entirely through the driver’s torque input. In order to provide an autonomous mode, a motor must be added to actuate the steering. Several design ideas have been composed: one attempt was to mount the motor parallel to the steering shaft and use a belt or chain for motion transmission. However, it was found that the belt was unable to support the large force which exposed several problems such as slipping. A chain connection was also tried but had the problem of vibration and velocity fluctuation. An alternative design is the SBW, which disconnects the mechanical connection between the hand wheel (HW) and road wheel (RW) and allows each part to be actuated by its
own motor and ECU. The SBW design generally supports modular design and easy assembly while reducing weight, space, and cost. It also increases the availability of steering functions such as variable steering feedback and dynamic stabilization. However, communication delays and system failures could raise safety concerns. After leveraging the pros and cons, the go-kart team decided to adopt the SBW design. 

Steer-by-Wire overview video
--------------

.. raw:: html 
    
    <iframe width="560" height="315" src="https://www.youtube.com/embed/nCdZjO_2pxI?si=AlTs6Dbcry8a-N60" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Upper Steer by wire system
--------------

The HW module uses a Popolu 12V Brushed DC motor with a built-in quadrature encoder for angle measurement to co- axially drive the steering wheel. In the manual mode, the driver could turn the steering wheel while the position is measured,
sent on the CAN bus, captured by MC, and forwarded to the RW. In the autonomous mode, the HW receives the steering command from the MC, performs the closed-loop PID control, and sends back the measured data. 

Upper Steer-by-Wire overview video
=========

.. raw:: html 
    
    <iframe width="560" height="315" src="https://www.youtube.com/embed/5dmrL_rOtRQ?si=X3oYoBTCYW2YxNoT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


Mechanical Assembly
=========
:doc:`Mechanical/USBW_mechanical`


Electrical Assembly
=========
:doc:`Electrical/USBW_electrical`

Lower Steer by wire system 
--------------

The RW module is designed to drag or push the steering tie rods to drive the front wheels. We use a NEO1650 Brushless Motor with a 240:1 ratio gearbox to provide sufficient torque output. The motor is driven by a VESC 6 Controller and takes up to 50 amps. Sensing is implemented using an AP5074 Magnetic Position Sensor mounted at the end of the steering shaft and provides the absolute angle data at a precision of 0.1 degrees. As with the HW module, angle adjustment is achieved using a closed-loop PID controller.

Lower Steer-by-Wire overview video
=========

.. raw:: html 
    
    <iframe width="560" height="315" src="https://www.youtube.com/embed/Uqq-4NhJrEY?si=eAUtd78mEmjvrFnB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


.. note::

    Assemble the mechanical system first and then the electrical system.    

Mechanical Assembly
=========
:doc:`Mechanical/LSBW_mechanical`


Electrical Assembly
=========
:doc:`Electrical/LSBW_electrical`
