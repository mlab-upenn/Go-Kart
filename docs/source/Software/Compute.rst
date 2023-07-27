==================================
Compute
==================================

Introduction
============

The Go-Kart project has significant planning and other high level navigation components which require understanding of the compute system and how it's setup.

Laptop
=========
Add data here

Sensors
=========
Add data here

LIDAR
--------------
Add data here

Camera
--------------
Add data here

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

Here you can find information about the pre-developed algorithms for the navigation of the Go-kart by the mlab at the University of Pennsylvania
