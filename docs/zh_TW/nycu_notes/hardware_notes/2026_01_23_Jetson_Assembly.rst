.. _2026_01_23_Jetson_Assembly:

2026-01-23 Jetson 組裝記錄
======================

本文件記錄了 2026/01/19~21 更換 Jetson Orin SOM (GPU) 的過程，以及復現了更早之前安裝 SSD 的記錄。


前情提要
--------

ToddlerBot 官方設計上，使用的是 reComputer J4012。但是由於我國的國安規定，學校難以買大陸公司與工廠產的資通訊產品。所以我們退而求其次，使用了 Nvidia 的 Jetson Orin Nano Super Developer Kit 並手動換上 Jetson Orin NX 16GB。

.. dropdown:: 硬體參考資料

    基於以下原因：

    *   Jetson Orin Nano Super DevKit 的載板（Carrier Board）與 Jetson Orin NX 相容： `Nvidia 論壇 <https://forums.developer.nvidia.com/t/original-nvidia-board-for-orin-nx/285333>`_
    *   該載板的大小是 100 x 79 x 21mm： `Carrier Board Spec <https://developer.nvidia.com/embedded/downloads#?search=Jetson%20Orin%20Nano%20Developer%20Kit%20Carrier%20Board%20Specification>`_
    *   reComputer J4012 具有類似的佈局與尺寸： `reComputer 開源硬體 Repo <https://github.com/Seeed-Studio/OSHW-Jetson-Series/tree/main/reComputer%20Jetson%20carrier%20board/reComputer%20J401>`_

    我們購買了這個替代方案：

    *   Jetson Orin NX 16GB SOM (USD $699): `Arrow <https://www.arrow.com/en/products/900-13767-0000-001/nvidia>`_

        *   900-13767-0000-001 和 900-13767-0000-000 基本上是一樣的，似乎只是批次不同。

    *   Jetson Orin Nano Super DevKit (USD $249): `Arrow <https://www.arrow.com/en/products/945-13766-0000-000/nvidia>`_

        *   945-13766-0000-000, 945-13766-0000-005, 945-13766-0000-007 似乎是一樣的。
        *   不必購買 M.2 CB375NF Wifi Card，因為 DevKit 會預裝。

    *   WD威騰 BLACK 黑標 SN7100 500G Gen4 NVMe SSD固態硬碟 (WDS500G4X0E) (TWD $1460 :math:`\approx` USD $49)

        *   reComputer 附的是 128GB，故請至少買這個容量。

    *   裁一片 PTM7950 0.25mm 相變導熱膠，大小約 22 x 20mm。原尺寸 40 x 80mm (TWD $390 :math:`\approx` USD $13): `Shopee <https://shopee.tw/user/purchase/order/222510203299548?type=3>`_


安裝 SSD
--------

前置作業
^^^^^^^^

請準備好

*   一支 PH1 十字螺絲起子。
*   一條你要安裝上去的 M.2 PCIe SSD。


組裝過程
^^^^^^^^

組裝很簡單，只有三步驟

1.  請把該 M.2 插槽對應的螺絲解開

    .. image:: ../../../_static/jetson_ssd_prepare.jpg

2.  將 SSD 插入 M.2 插槽。儘量平地插比較好插入，插入後自動彈起而斜斜的是正常的。

    .. image:: ../../../_static/jetson_ssd_inserted.jpg

3.  將螺絲鎖上，就大功告成啦！

    .. image:: ../../../_static/jetson_ssd_locked.jpg

更換 SOM
--------

由於拆卸跟組裝只是相反的操作（或甚至你運氣好可以找到無 Jetson Orin Nano 8GB SOM 的載板），所以這裡只記錄組裝的過程。


前置作業
^^^^^^^^

請準備好「硬體參考資料」提到的導熱膠、SOM 與 DevKit 本體，並準備一些酒精和不掉屑的布，與 T7 內梅花、PH1 十字螺絲起子各一把。

*   導熱膠：可以先放置在冰箱冷藏（非冷凍），有助於裁剪與粘貼時不破碎。
*   DevKit 與舊的 SOM 請依照組裝過程反向拆卸。
    *   使用至少 75% 的酒精清除風扇上的舊導熱膠。
    *   使用不掉屑的布（例如棉布或眼鏡布）擦除風扇上的舊導熱膠。萬一真的沒有，強韌的再生紙、廚房紙巾、甚至酒精沾溼的 A4 紙也比衛生紙好。


組裝過程
^^^^^^^^

1.  請取一塊 20 x 20 x 0.25mm 的 PTM 7950 相變導熱膠，並把它妥善粘著至 SOM 中央那塊 22 x 20mm 的平臺上。
    
    .. image:: ../../../_static/jetson_som_with_ptm7950.jpg
    
2.  請將風扇清潔乾淨，然後對齊 SOM 與風扇背面的四個孔位，藉導熱膠的粘性貼合他們。以下是背面與正面。

    .. raw:: html

        <div style="display: flex; flex-flow: row wrap; justify-content: space-around;">
            <img src="../../../_static/jetson_som_on_fan_back.jpg" style="flex: 15em; width: 15em;">
            <img src="../../../_static/jetson_som_on_fan_front.jpg" style="flex: 15em; width: 15em;">
        </div>

3.  將長得像 ``>-<`` 的固定架與螺絲鎖上。

    *   小訣竅：由於固定架有點彈性，可以先鎖對角線的兩根螺絲。鎖的時候先各鎖一半，再一起鎖到底。

    以下是未鎖上與鎖上的樣子：

    .. raw:: html

        <div style="display: flex; flex-flow: row wrap; justify-content: space-around;">
            <img src="../../../_static/jetson_som_fan_unlocked.jpg" style="flex: 15em; width: 15em;">
            <img src="../../../_static/jetson_som_fan_locked.jpg" style="flex: 15em; width: 15em;">
        </div>

4.  將 SOM 的金手指插入載板。呈現斜斜的狀態是它的設計。

    .. raw:: html

        <img src="../../../_static/jetson_som_inserted_unlocked.jpg" style="max-height: 80vh; width: 100%; object-fit: contain;">

    你可以注意到，左側與右側各有一個卡榫。所以

    *   當你要固定 SOM 時，直接將 SOM 往下壓，直到兩側的卡榫都扣住 SOM 為止即可。
    *   當你要拆卸 SOM 時，先將兩側的卡榫左右扳開，則 SOM 會自然仰起。

    .. raw:: html

       <div style="display: flex; flex-flow: row wrap; justify-content: space-around;">
           <img src="../../../_static/jetson_som_inserted_unlocked_left.jpg" style="flex: 15em; width: 15em;">
           <img src="../../../_static/jetson_som_inserted_unlocked_right.jpg" style="flex: 15em; width: 15em;">
       </div>

    以下是下壓固定後的樣子：

    .. raw:: html

        <img src="../../../_static/jetson_som_locked.jpg" style="max-height: 80vh; width: 100%; object-fit: contain;">

5.  將螺絲鎖上，固定 SOM。以下是未鎖上的樣子，你可以注意到風扇角落旁、SOM 上有兩個螺絲孔。

    *   小訣竅：如果你覺得螺絲鎖不進去，不要硬鎖。請把 SOM 往金手指插入的方向再插更緊，以及稍微把 SOM 用手下壓、靠近螺絲柱。

    .. raw:: html

        <img src="../../../_static/jetson_som_locked_unscrewed.jpg" style="max-height: 80vh; width: 100%; object-fit: contain;">

6.  最後請將風扇的排線插回去，然後就完成了。以下是四張不同角度的成品圖：

    .. raw:: html

        <div style="display: flex; flex-flow: row wrap; justify-content: space-around;">
            <img src="../../../_static/jetson_devkit_assembled_1.jpg" style="flex: 15em; width: 15em;">
            <img src="../../../_static/jetson_devkit_assembled_2.jpg" style="flex: 15em; width: 15em;">
        </div>

        <div style="display: flex; flex-flow: row wrap; justify-content: space-around;">
            <img src="../../../_static/jetson_devkit_assembled_3.jpg" style="flex: 15em; width: 15em;">
            <img src="../../../_static/jetson_devkit_assembled_4.jpg" style="flex: 15em; width: 15em;">
        </div>




