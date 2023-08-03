==================================
Compute
==================================

.. |Link1| raw:: html

   <a href="https://github.com/mlab-upenn/gokart-sensor/tree/ros2_foxy_purepursuit">ROS2 Foxy setup and autonomous code</a>

.. |Link2| raw:: html

   <a href="https://github.com/mlab-upenn/gokart-sensor/tree/ros2_humble_purepursuit">ROS2 Humble setup and autonomous code</a>


Introduction
============

The Go-Kart project has significant planning and other high level navigation components which require understanding of the compute system and how it's setup.

Laptop
=========
The Laptop is the main compute system for the Go-Kart. It is used for running the high level navigation stack and connects to the Nucleo using a USB interface for low level control stack. The laptop is connected to the Go-Kart via ethernet and is powered by a 12V battery. There is also a provision from the PDU to provide power to the laptop's battery so that it can run on high performance as well as not run out at any given time. We are using the MSI __ with GPU ___. The laptop is mounted on the Go-Kart using a laptop mount. The laptop mount is mounted on the rear shelf of the Go-Kart. Below is the system overview. \

.. image:: ../imgs/Software/compute.png
   :width: 600

Sensors
=========
The Go-Kart has a variety of sensors which are used for navigation, control and perception. This section will describe the sensors specifically used for navigation and perception. They are : 

LIDAR
--------------
The Go-Kart system has an Ouster LIDAR which is used for perception and navigation. The LIDAR is mounted on the rear shelf of the Go-Kart and is used for obstacle detection and avoidance. The LIDAR is also used for localizing the Go-kart on the track by working with SLAM algorithms such as EKF SLAM, GRAPH SLAM and more. The LIDAR is connected to the compute system (aka Laptop) via ethernet.

Camera
--------------
We use the OAK-D camera to run perception related tasks on the Go-Kart. It connects to the main compute system using USB.
GNSS
--------------
The Go-Kart system has a GNSS system which is used for localization. The GNSS system is mounted on the rear shelf of the Go-Kart and is used for localization of the Go-Kart on the track. The GNSS system is connected to the compute system (aka Laptop) via USB. The interface and how to setup the communication is described in the readme of the github. Please find the links at the bottom of this page.


Software system
===============

The sensor system enables research and development in perception, sensor fusion and localization for autonomous racing. Through its position at the beginning of the pipeline for autonomous vehicles, perception plays an essential role and directly influences the performance of all subsequent systems. To enable safe and predictable behavior for different use cases, the go-kart platform offers multiple capabilities to detect and track objects, lanes, and markers in its environment and determines its current position reliably. This section introduces some of the sensing capabilities in the go-kart and their accompanying algorithms

Single-Modality Object Detection
YOLO offers object detection, segmentation, and classifi- cation in one algorithm. Additional benefits include a good generalization, fewer false positives for backgrounds, and the potential of real-time processing. To run object detection, we deploy multiple versions on the go-kart, including Darknet YOLOv3 and YOLOv8. 

Single-Modality Object Detection
----------------------------------

                    YOLO offers object detection, segmentation, and classifi- cation in one algorithm. 
                    Additional benefits include a good generalization, fewer false positives for backgrounds, 
                    and the potential of real-time processing. To run object detection, we deploy multiple versions 
                    on the go-kart, including Darknet YOLOv3 and YOLOv8.The UI is a customized PCB mounted on 
                    the side of the driver’s seat. 





Working tips
=================

.. warning::

   Always ensure your remote system is working well before getting into working with the autonomous stack.

Github
==========

Here you can find information about the pre-developed algorithms for the navigation of the Go-kart by the mlab at the University of Pennsylvania.

* |Link1|
* |Link2|
