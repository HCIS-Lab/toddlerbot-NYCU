.. _nycu_notes_hardware:

硬體筆記
=========================

.. warning::

   本頁面由 LLM 輔助生成，尚未經過人工審核，請謹慎使用。

本章節包含馬達設定、組裝過程中的常見問題排除 (Troubleshooting)。

Q: 在組裝之前，馬達要先做設定嗎？
----------------------------

應該不用先設定。裝好再依序設定也可以！但是，**一次只將一顆馬達連接至 U2D2**，否則多顆預設 ID = 1 的馬達會衝突！

操作流程概覽如下：

1.  安裝 `Dynamixel Wizard 2.0 <https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_wizard2/>`，然後把馬達連結
2.  根據 :ref:`assembly_manual` 那個 for toddlerbot 1.0 的 PDF，

    *   要把 baudrate 設定成 2 Mbps。
    *   根據馬達在機器人上的位置設定 ID
    *   在 Wizard 中的右側 Enable Torque，然後中間點擊 Target Position 並把值設為 0。

Q: 要把 Dynamixel 馬達插到筆電上設定，要怎麽供電？
--------------------------------------------
*   Ref: `(YouTube) How To: Connect power to U2D2 Power Hub Board for DYNAMIXEL <https://www.youtube.com/watch?v=FIj_NULYOKQ>`_
*   使用 U2D2（有透明塑膠殼），然後把 U2D2 插到 U2D2 Power Hub 上。
    *   Power Hub 吃 12V 電壓輸入，我們用了 iMax B6 Mini 電池充電器隨附的變壓器供電。

馬達歸零校正 (Motor Calibration)
--------------------------------

腳本 ``toddlerbot/tools/calibrate_zero.py`` 是用於組裝完成後的 **軟體歸零校正 (Software Zero-point Calibration)** 以調整些微誤差，**並不是** 用來初始化所有馬達 ID 的。

常見問題與解決方案
------------------

1. 螺絲過大與公差問題
~~~~~~~~~~~~~~~~~~~~~

*   **問題**：Leg/Hip Assembly 的螺絲頭可能過大，無法放入 3D 列印件的孔洞中。
*   **解決方案**：
    *   嘗試改用 Dynamixel 馬達隨附的螺絲，它們的頭通常較小。
    *   若是 3D 列印公差導致孔洞過小，可以使用打火機稍微加熱螺絲（注意通風與配戴口罩），利用熱熔方式擠入。
    *   若誤差過大，請重新列印。

2. 散熱膏缺件
~~~~~~~~~~~~~

*   **問題**：將 Jetson Orin NX 模組轉移至 DevKit 時發現缺少散熱膏。
*   **解決方案**：建議購買 **PTM7950 0.25mm 相變導熱膠**。舊的散熱膏可用 75% 酒精擦拭清潔（建議使用不掉屑的拭紙）。

3. JST-EH 線材方向錯誤
~~~~~~~~~~~~~~~~~~~~~~

*   **問題**：市售加長版 JST-EH 線材的腳位順序可能與 Dynamixel 不符（例如 1-2-3 對應到另一端的 3-2-1）。
*   **解決方案**：需要手動退 Pin 重插。
    1.  固定住線材與端子。
    2.  使用細的一字起子輕輕挑起塑膠卡榫，同時將線拉出。
    3.  依照正確順序 (1對1, 2對2, 3對3) 重新插入。

4. U2D2 供電
~~~~~~~~~~~~

*   **問題**：要在設定馬達與組裝時為馬達供電。
*   **解決方案**：使用 **U2D2 Power Hub**。將 U2D2 插在 Power Hub 上，並使用變壓器（如 iMax B6 Mini 隨附的）連接至 Power Hub 供電。

.. toctree::
   :maxdepth: 1
   :caption: 詳細組裝紀錄

   hardware_notes/2026_01_20_Assembly

