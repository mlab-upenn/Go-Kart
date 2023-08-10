Brake By Wire (BBW) Assembly
==================================


TODO Insert image here: BBW_labelled.png

The brake-by-wire subsystem builds upon TopKart's original manual braking, by enabling the car to brake whenever necessary from autonomous mode. The higher level controller always sends some braking signal downstream to the BBW nucleo, which then runs a PID controller to quickly achieve the desired value. The system's sensor is a M3041-000006-500PG Pressure Sensor, which closes the loop enabling PID feedback control to take place.

M3041-000006-500PG Pressure Sensor: https://www.digikey.com/en/products/detail/te-connectivity-measurement-specialties/M3041-000006-500PG/274609

The system's actuator is a Linear Electric Actuator DC Motor (clean up link, pasted below), which transmits motion via direct contact with the braking fluid reservoir lever, displacing it just as the left foot brake pedal would. The original TopKart braking mechanism then transfers (via the original braking fluid pipe) this hydraulic pressure to the rear axle, compressing its brake calipers and decelerating the car.

Linear Electric Actuator DC Motor:
https://www.amazon.com/PROGRESSIVE-AUTOMATIONS-Electric-Actuator-PA-14P-4-35/dp/B00Q74I8TI/ref=sr_1_2?keywords=PA-14P-4-35%2Blinear%2Bactuator&qid=1662603873&sr=8-2&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0&th=1

This motor gets mounted 







TODO Insert paragraphs here

Reference the driver and nucleo, which are mounted onto the other things, as described in the "Miscellaneous" section.

Mention that we used some big rubber washers and small metal washers, to ensure tightness