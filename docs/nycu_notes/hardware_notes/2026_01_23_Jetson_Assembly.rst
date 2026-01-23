.. _2026_01_23_Jetson_Assembly_en:

2026-01-23 Jetson Assembly Log
==============================

.. warning::
   This page is translated by LLM and may contain some inaccuracies.
   `中文版 (Chinese Version) <../../zh_TW/nycu_notes/hardware_notes/2026_01_23_Jetson_Assembly.html>`_

This document records the process of replacing the Jetson Orin SOM (GPU) during 2026/01/19~21, and reproduces the earlier SSD installation record.

Background
----------

The official ToddlerBot design uses the reComputer J4012. However, due to national security regulations, it is difficult for our university to purchase ICT products from mainland Chinese companies/factories. Therefore, we opted for the **Nvidia Jetson Orin Nano Super Developer Kit** and manually replaced the module with a **Jetson Orin NX 16GB**.

.. dropdown:: Hardware References

    Based on the following reasons:

    *   Jetson Orin Nano Super DevKit Carrier Board is compatible with Jetson Orin NX: `Nvidia Forum <https://forums.developer.nvidia.com/t/original-nvidia-board-for-orin-nx/285333>`_
    *   Carrier Board dimensions are 100 x 79 x 21mm: `Carrier Board Spec <https://developer.nvidia.com/embedded/downloads#?search=Jetson%20Orin%20Nano%20Developer%20Kit%20Carrier%20Board%20Specification>`_
    *   reComputer J4012 has similar layout and dimensions: `reComputer Open Source Hardware Repo <https://github.com/Seeed-Studio/OSHW-Jetson-Series/tree/main/reComputer%20Jetson%20carrier%20board/reComputer%20J401>`_

    We purchased this alternative solution:

    *   Jetson Orin NX 16GB SOM (USD $699): `Arrow <https://www.arrow.com/en/products/900-13767-0000-001/nvidia>`_

        *   900-13767-0000-001 and 900-13767-0000-000 are basically identical, likely just different batches.

    *   Jetson Orin Nano Super DevKit (USD $249): `Arrow <https://www.arrow.com/en/products/945-13766-0000-000/nvidia>`_

        *   945-13766-0000-000, 945-13766-0000-005, 945-13766-0000-007 seem identical.
        *   No need to buy M.2 CB375NF Wifi Card as DevKit comes pre-installed.

    *   WD BLACK SN7100 500G Gen4 NVMe SSD (WDS500G4X0E) (~USD $49)

        *   reComputer comes with 128GB, so buy at least this capacity.

    *   PTM7950 0.25mm Phase Change Thermal Pad, cut to approx 22 x 20mm (~USD $13).

SSD Installation
----------------

Preparation
^^^^^^^^^^^

Please prepare:

*   A PH1 Phillips screwdriver.
*   The M.2 PCIe SSD to be installed.

Assembly Process
^^^^^^^^^^^^^^^^

It's simple, just 3 steps:

1.  Unscrew the screw corresponding to the M.2 slot.

    .. image:: ../../_static/jetson_ssd_prepare.jpg

2.  Insert the SSD into the M.2 slot. Keep it flat for easier insertion. It acts springy and stays diagonal after insertion, which is normal.

    .. image:: ../../_static/jetson_ssd_inserted.jpg

3.  Lock the screw, and you are done!

    .. image:: ../../_static/jetson_ssd_locked.jpg

SOM Replacement
---------------

Disassembly is just the reverse of assembly, so here we only record the assembly process.

Preparation
^^^^^^^^^^^

Please prepare the thermal pad mentioned in "Hardware References", the SOM, the DevKit, some alcohol, lint-free cloth, a T7 Torx screwdriver, and a PH1 Phillips screwdriver.

*   Thermal Pad: Can be refrigerated (not frozen) to help with cutting and application.
*   Disassemble the DevKit and old SOM in reverse order.

    *   Use at least 75% alcohol to clean old thermal paste from the fan.
    *   Use lint-free cloth (e.g., lens cloth) to wipe off the paste. If unavailable, sturdy paper towel or alcohol-soaked A4 paper is better than tissue paper.

Assembly Process
^^^^^^^^^^^^^^^^

1.  Take a 20 x 20 x 0.25mm PTM 7950 thermal pad and apply it to the center 22 x 20mm platform of the SOM.
    
    .. image:: ../../_static/jetson_som_with_ptm7950.jpg
    
2.  Clean the fan, align the four holes on the SOM and the back of the fan, and stick them together using the thermal pad's adhesiveness.

    .. raw:: html

        <div style="display: flex; flex-flow: row wrap; justify-content: space-around;">
            <img src="../../_static/jetson_som_on_fan_back.jpg" style="flex: 15em; width: 15em;">
            <img src="../../_static/jetson_som_on_fan_front.jpg" style="flex: 15em; width: 15em;">
        </div>

3.  Attach the ``>-<`` shaped bracket and screws.

    *   Tip: The bracket is slightly elastic, so tighten diagonal screws halfway first, then tighten all the way.

    .. raw:: html

        <div style="display: flex; flex-flow: row wrap; justify-content: space-around;">
            <img src="../../_static/jetson_som_fan_unlocked.jpg" style="flex: 15em; width: 15em;">
            <img src="../../_static/jetson_som_fan_locked.jpg" style="flex: 15em; width: 15em;">
        </div>

4.  Insert the SOM's gold fingers into the carrier board. It is designed to sit diagonally.

    .. raw:: html

        <img src="../../_static/jetson_som_inserted_unlocked.jpg" style="max-height: 80vh; width: 100%; object-fit: contain;">

    Notice the latches on the left and right.

    *   To lock: Press the SOM down until both latches click.
    *   To unlock: Pull latches outward slightly, and the SOM will pop up.

    .. raw:: html

       <div style="display: flex; flex-flow: row wrap; justify-content: space-around;">
           <img src="../../_static/jetson_som_inserted_unlocked_left.jpg" style="flex: 15em; width: 15em;">
           <img src="../../_static/jetson_som_inserted_unlocked_right.jpg" style="flex: 15em; width: 15em;">
       </div>

    Locked state:

    .. raw:: html

        <img src="../../_static/jetson_som_locked.jpg" style="max-height: 80vh; width: 100%; object-fit: contain;">

5.  Screw in the screws to secure the SOM.

    *   Tip: If screws don't go in easily, push the SOM tighter into the slot and press it down closer to the screw posts.

    .. raw:: html

        <img src="../../_static/jetson_som_locked_unscrewed.jpg" style="max-height: 80vh; width: 100%; object-fit: contain;">

6.  Plug the fan cable back in. Done!

    .. raw:: html

        <div style="display: flex; flex-flow: row wrap; justify-content: space-around;">
            <img src="../../../_static/jetson_devkit_assembled_1.jpg" style="flex: 15em; width: 15em;">
            <img src="../../../_static/jetson_devkit_assembled_2.jpg" style="flex: 15em; width: 15em;">
        </div>

        <div style="display: flex; flex-flow: row wrap; justify-content: space-around;">
            <img src="../../../_static/jetson_devkit_assembled_3.jpg" style="flex: 15em; width: 15em;">
            <img src="../../../_static/jetson_devkit_assembled_4.jpg" style="flex: 15em; width: 15em;">
        </div>
