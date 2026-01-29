.. _nycu_notes_hardware:

硬體筆記
=========================

本章節包含馬達設定、組裝過程中的常見問題排除。

Q: 在組裝之前，馬達要先做設定嗎？
----------------------------

應該不用先設定。裝好再依序設定也可以！但是，**一次只將一顆馬達連接至 U2D2**，否則多顆預設 ID = 1 的馬達會衝突！

操作流程概覽如下：

1.  安裝 `Dynamixel Wizard 2.0 <https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_wizard2/>`_，然後把馬達連結到電腦。
2.  根據 :ref:`assembly_manual` 那個 for toddlerbot 1.0 的 PDF，

    *   要把 baudrate 設定成 2 Mbps。
    *   根據馬達在機器人上的位置設定 ID
    *   在 Wizard 中的右側 Enable Torque，然後中間點擊 Target Position 並把值設為 0。

Q: 要把 Dynamixel 馬達插到筆電上設定，要怎麽供電？
--------------------------------------------
*   Ref: `(YouTube) How To: Connect power to U2D2 Power Hub Board for DYNAMIXEL <https://www.youtube.com/watch?v=FIj_NULYOKQ>`_
*   使用 U2D2（有透明塑膠殼），然後把 U2D2 插到 U2D2 Power Hub 上。

    *   Power Hub 吃 12V 電壓輸入，我們用了 iMax B6 Mini 電池充電器隨附的變壓器供電。


其他常見問題與解決方案
------------------

1. 3D 列印孔洞大小與公差問題
~~~~~~~~~~~~~~~~~~~~~

*   **問題**：如果運氣不好，買到的螺絲頭可能過大，無法放入 3D 列印件的孔洞中。或者列印時有公差，也可能是 Bearing 塞不進去的原因。
*   **解決方案**：

    *   嘗試改用 Dynamixel 馬達隨附的螺絲，它們的頭通常較小。
    *   若是 3D 列印公差導致孔洞過小，可以使用打火機稍微加熱螺絲（注意通風與配戴口罩），利用熱熔方式擠入。
    *   若誤差過大，請重新列印。

2. U2D2 供電
~~~~~~~~~~~~

*   **問題**：要在設定馬達與組裝時為馬達供電。
*   **解決方案**：使用 **U2D2 Power Hub**。將 U2D2 插在 Power Hub 上，並使用變壓器（如 iMax B6 Mini 隨附的）連接至 Power Hub 供電。

.. toctree::
   :maxdepth: 1
   :caption: 詳細組裝紀錄

   hardware_notes/2026_01_23_Jetson_Assembly
   hardware_notes/2026_01_29_JST_EH_wrong_wiring

