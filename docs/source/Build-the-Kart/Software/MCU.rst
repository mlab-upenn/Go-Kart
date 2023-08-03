==================================
MCU
==================================

.. |Link1| raw:: html

   <a href="https://github.com/mlab-upenn/gokart-mechatronics/tree/main/STM32%20Control">STM32 nucleo controller code</a>

Introduction
============

The Go-Kart project involved a bunch of different microcontrollers. Majority of them are from the family of NUCLEO boards.


Architecture
=========
The whole microcontroller architecture is setup using CAN bus communication. There is a main nucleo which communicates with all the other nucleos and relays data according to the high level planning algorithms running on the laptop as well as decisions based on the High level sensors such as the LIDAR and the camera.

NUCELO F439ZI
--------------
The following file has in depth discussion about the NUCELOF439ZI board.
.. include:: NUCELOF439ZI.rst

NUCLEO L423KC
--------------
The following file has in depth discussion about the NUCLEOL423KC board.
.. include:: NUCLEOL423KC.rst


Working tips
=================

.. warning::

   Be sure to check that you have the write code flashed on each individual board. 

Github
==========
All the code required to be flashed on each nucleo is available on our mlab github repository and is maintained by the AVEV team at the University of Pennsylvania.


* |Link1|
