.. _nycu_notes_software_en:

Software Notes
==============

.. warning::

   This page was assisted by LLM and has not been fully verified by humans. Use with caution.
   `中文版 (Chinese Version) <../zh_TW/nycu_notes/02_software.html>`_

This section contains software environment setup for the Handheld PC and the Robot (Jetson Orin NX).

Handheld Controller (ROG Ally X)
--------------------------------

USB Latency Timer Setting
~~~~~~~~~~~~~~~~~~~~~~~~~

The "USB Latency Timer" mentioned in the docs refers to the **COM Port Property**, which sets the communication speed for USB-to-TTL (U2D2).

*   **Location**: Device Manager
*   **Path**: Ports (COM & LPT) -> USB Serial Port -> Properties -> Port Settings -> Advanced
*   **Action**: Change **Latency Timer (msec)** from default 16 to **1**.

NTP Time Synchronization
~~~~~~~~~~~~~~~~~~~~~~~~

We configure the Handheld PC as an NTP Server to ensure time synchronization between the robot (Jetson) and the controller, which is crucial for data logging accuracy. Refer to the ``software/03_rog_ally_x`` section in the official docs for details.

Robot Mainboard (Jetson Orin NX Setup)
--------------------------------------

We use the **Jetson Orin Nano Super DevKit** with a **Jetson Orin NX 16GB** module.

System Installation (Jetson Linux Image)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The official guide recommends the reComputer image, but for the Nvidia original DevKit, we use **Nvidia SDK Manager**.

**Prerequisites**:

1.  Prepare a Windows PC (Linux is fine, but VM might have USB passthrough issues).
2.  Download and install [Nvidia SDK Manager](https://developer.nvidia.com/sdk-manager).
3.  **Connection**:
    *   Short the **FC REC** and **GND** pins on the DevKit (use a jumper wire) to enter Recovery Mode.
    *   Connect USB Type-C to the PC first.
    *   Connect power last.

**Installation Steps**:

1.  Open SDK Manager, select **Target Hardware** as Jetson Orin NX.
2.  Select **JetPack 6.1** or higher.
3.  Check Jetson Linux, Runtime Components, etc.
4.  During installation, create a Username and Password (default recommendation: ``user`` / ``password``).
5.  Select **NVMe** as storage.

Connection and Basic Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~

**SSH Connection**:

1.  Connect DevKit to Ethernet or WiFi (DevKit has built-in antenna).
2.  Connect via ``ssh user@<ip_address>``.
3.  Or try ``ssh user@ubuntu.local``.

**Oh-My-Zsh (Optional)**:

To improve terminal experience, installing ZSH is recommended:

.. code-block:: bash

   sudo apt install zsh
   sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
   # Set as default shell
   chsh -s "$(which zsh)"
   # Recommended theme
   omz theme set gallois

**Required Packages**:

Follow the official ToddlerBot documentation:
1.  **Real-Time Kernel**: [Link](https://hshi74.github.io/toddlerbot/software/02_jetson_orin.html#set-up-real-time-rt-kernel)
2.  **Additional Packages**: [Link](https://hshi74.github.io/toddlerbot/software/02_jetson_orin.html#additional-packages)

.. note::
   If PyTorch fails to import, CUDA Toolkit might be missing. Check ``nvidia-smi`` and manually install the matching toolkit version (e.g., ``sudo apt install cuda-toolkit-12-x``).

Headless Remote
~~~~~~~~~~~~~~~
For portability:
1.  Change Hostname: ``sudo hostnamectl hostname toddlerbot`` for easier identification.
2.  Install RustDesk for remote desktop GUI if needed.

.. toctree::
   :maxdepth: 1
   :caption: Detailed Installation Logs

   software_notes/2026_01_23_Jetson_OS
