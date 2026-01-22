.. _nycu_notes:

NYCU Reproduction Notes
=======================

`切換至中文版 <../../zh_TW/sections/07_nycu_notes.html>`_

This section documents the specific challenges, solutions, and modifications encountered during the replication of ToddlerBot at National Yang Ming Chiao Tung University (NYCU).

.. note::
   These notes are specific to our lab's hardware setup and environment. They might not apply to the official build.

Hardware Notes
--------------

Motor ID Configuration
~~~~~~~~~~~~~~~~~~~~~~

**Critical Warning:** Do NOT assemble the motors before setting their IDs.
All new Dynamixel motors come with a default ID of 1. Connecting multiple motors with the same ID will cause conflicts.

**Correct Procedure:**

1. Connect one motor at a time to the U2D2.
2. Use **Dynamixel Wizard 2.0** to set the ID and change the Baudrate to **2000000** (2M).
3. Label the motor with its new ID.
4. Repeat for all motors *before* assembly.

Motor Calibration
~~~~~~~~~~~~~~~~~

The script ``toddlerbot/tools/calibrate_zero.py`` is intended for **software zero-point calibration** after assembly (to fine-tune offsets), not for initializing motor IDs.

Software Configuration
----------------------

ROG Ally X Setup
~~~~~~~~~~~~~~~~

The "USB Latency Timer" setting mentioned in the documentation refers to the COM port settings on the **Handheld PC (Windows)**, not the motors themselves.

*   **Goal:** Reduce latency from ~16ms to **1ms** for stable control loops.
*   **Method:** Device Manager -> Ports (COM & LPT) -> USB Serial Port -> Properties -> Port Settings -> Advanced -> Latency Timer.

NTP Synchronization
~~~~~~~~~~~~~~~~~~~

We configure the handheld PC as an NTP server to ensure the robot (Jetson) and the controller have synchronized clocks for accurate logging.

Updates & Fixes
---------------

*   (Pending) List any custom fixes or workarounds here.
*   (Pending) Link to any upstream PRs we have submitted.


Table of Contents
-----------------

.. toctree::
   :maxdepth: 1
   :caption: 內容索引

   ../nycu_notes/index