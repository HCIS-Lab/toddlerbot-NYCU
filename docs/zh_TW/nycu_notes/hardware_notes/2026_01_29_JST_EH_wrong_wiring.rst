.. _2026_01_29_JST_EH_wrong_wiring:

2026-01-29 JST-EH 解決加長線線序錯誤
====================================

本文件記錄了 2026/01/23 解決 JST-EH 加長線線序錯誤的過程。


前情提要
--------

官方 BOM 表上要我們購買 JST-EH Cable 與 JST-EH Housing（塑膠殼）。但為了一條 3-pin 的 JST-EH 加長線花臺幣 40 元左右不合成本，所以我試著買了 `已經壓好的線 <https://item.taobao.com/item.htm?spm=tbpc.boughtlist.suborder_itemtitle.1.4f042e8dWKZ1rw&id=836918236262&mi_id=0000tZcB8VwUKXtTJHIoAc6yD3BiWi1BaVFyF69piPlywUY>`_。
    
.. raw:: html

    <div style="display: flex; flex-flow: row wrap; justify-content: space-around;">
        <img src="../../../_static/jst_eh_back.jpg" style="flex: 15em; width: 15em;">
        <img src="../../../_static/jst_eh_front.jpg" style="flex: 15em; width: 15em;">
    </div>

不過如圖所示，如果我們將各膠殼的 pin 以 1, 2, 3 命名，想當然有兩種連結方式。我們很不幸地買到 1-3' 2-2' 3-1'，但 Dynamixel 要用 1-1' 2-2' 3-3'。


解決方法
--------

如果不想重買，就要想辦法退其中一端的 1 & 3 pin 再重插回去。以下是我們的做法——當時我坐在地上，但你可以想一個更優雅的方法。

1.  抓住一端端子塑膠殼。
2.  選 3 號 pin 的線一腳踩住（或某種方式固定住），另外兩根不要踩。

3.  將塑膠殼往自己這邊拉，同時用減號螺絲起子輕翹最右邊的塑膠片。

    *   請小心不要太大力，以免塑膠形變而影響插入後重新固定。
    *   成功的話，可以把線帶著金屬接頭拉出。

4.  對 1 號 pin 也做一樣的事情。
5.  把線照正確的順序插。登登～完成！

.. dropdown:: 本頁面貢獻記錄

    *   操作者與撰寫者：潘仰祐 Kevin Pan（@XiaoPanPanKevinPan）




