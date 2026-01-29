..
   :sync_target: ../zh_TW/nycu_notes/01_hardware.rst
   :sync_hash: caf7213519c96c727b407b2c38673daf505409ba



.. _nycu_notes_hardware_en:


Hardware Notes
==============

.. warning::

   This page was assisted by LLM and has not been fully verified by humans. Use with caution.
   `中文版 (Chinese Version) <../zh_TW/nycu_notes/01_hardware.html>`_

This section contains troubleshooting guides for motor configuration and assembly process.

Q: Should I configure the motors before assembly?
-----------------------------------------------

Probably not necessary. You can configure them sequentially after assembly! However, **connect only one motor to the U2D2 at a time**, otherwise multiple motors with the default ID = 1 will conflict!

The procedure is as follows:

1.  Install `Dynamixel Wizard 2.0 <https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_wizard2/>`_ and connect the motor to the computer.
2.  According to the :ref:`assembly_manual` PDF for toddlerbot 1.0:

    *   Set the baudrate to **2 Mbps**.
    *   Set the ID according to the motor's position on the robot.
    *   Enable Torque in the Wizard, then click Target Position in the center and set it to 0.

Q: How to power the Dynamixel motor to configure it on a laptop?
---------------------------------------------------------------
*   Ref: `(YouTube) How To: Connect power to U2D2 Power Hub Board for DYNAMIXEL <https://www.youtube.com/watch?v=FIj_NULYOKQ>`_
*   Use the U2D2 (with the transparent plastic case), and plug the U2D2 into the U2D2 Power Hub.
    *   The Power Hub requires 12V input. We used the power adapter included with the iMax B6 Mini battery charger.


Other Common Issues and Solutions
---------------------------------

1. 3D Printing Hole Size and Tolerance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*   **Issue**: If unlucky, the screw head for the Leg/Hip Assembly might be too large to fit into the countersunk hole of the 3D printed part. Or due to printing tolerance, the bearing might not fit.
*   **Solution**:

    *   Try using the screws included with the Dynamixel motors (they usually have smaller heads).
    *   If the hole is too small due to 3D printing tolerance, you can heat the screw slightly with a lighter (ensure ventilation and wear a mask) and melt it in.
    *   Last resort: Reprint the part.

2. U2D2 Power Supply
~~~~~~~~~~~~~~~~~~~~

*   **Issue**: Powering the motors during configuration and assembly.
*   **Solution**: Use the **U2D2 Power Hub**. Plug the U2D2 into the Power Hub and use a power adapter (like the one from iMax B6 Mini) to power the Hub.

.. toctree::
   :maxdepth: 1
   :caption: Detailed Assembly Logs

   hardware_notes/2026_01_23_Jetson_Assembly
   hardware_notes/2026_01_29_JST_EH_wrong_wiring
