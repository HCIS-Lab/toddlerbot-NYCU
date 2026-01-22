.. _nycu_notes_software:

軟體筆記 (Software Notes)
=========================

.. warning::

   本頁面由 LLM 輔助生成，尚未經過人工審核，請謹慎使用。


本章節包含手持控制器 (Handheld PC) 與機器人本體 (Jetson Orin NX) 的軟體環境架設。

手持控制器 (ROG Ally X)
-----------------------

USB Latency Timer 設定
~~~~~~~~~~~~~~~~~~~~~~

文件中提到的 "USB Latency Timer" 設定指的是 **COM Port 的屬性**，這是為了加快 USB 轉 TTL (U2D2) 的通訊速度。

*   **位置**：裝置管理員 (Device Manager)
*   **路徑**：連接埠 (COM & LPT) -> USB Serial Port -> 內容 -> 連接埠設定 -> 進階
*   **動作**：將 **Latency Timer (msec)** 從預設的 16 改為 **1**。

NTP 時間同步
~~~~~~~~~~~~

我們會將手持 PC 設定為 NTP Server，以確保機器人 (Jetson) 與控制器之間的時間同步，這對於資料記錄 (Logging) 的準確性至關重要。詳細步驟請參考官方文件中的 ``software/03_rog_ally_x`` 章節。

機器人本體 (Jetson Orin NX Setup)
---------------------------------

我們使用 **Jetson Orin Nano Super DevKit** 搭配 **Jetson Orin NX 16GB** 模組。

安裝系統 (Jetson Linux Image)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

官方推薦使用 reComputer 的映像檔，但針對 Nvidia 原廠 DevKit，我們使用 **Nvidia SDK Manager**。

**前置準備**：

1.  準備一台 Windows 電腦 (Linux 亦可，但虛擬機可能有 USB 直通問題)。
2.  下載並安裝 [Nvidia SDK Manager](https://developer.nvidia.com/sdk-manager)。
3.  **接線**：
    *   將 DevKit 的 **FC REC** 與 **GND** 腳位短路（使用杜邦線），以進入 Recovery Mode。
    *   先連接 USB Type-C 到電腦。
    *   最後接上電源。

**安裝步驟**：

1.  開啟 SDK Manager，選擇 **Target Hardware** 為 Jetson Orin NX。
2.  選擇 **JetPack 6.1** 或以上版本。
3.  勾選安裝 Jetson Linux, Runtime Components 等。
4.  在安裝過程中，軟體會提示輸入 Username 與 Password (預設建議設為 ``user`` / ``password``)。
5.  選擇儲存裝置為 **NVMe**。

連線與基本設定
~~~~~~~~~~~~~~

**SSH 連線**：

1.  將 DevKit 接上網路孔或連上 WiFi (DevKit 有內建天線)。
2.  使用 ``ssh user@<ip_address>`` 連線。
3.  或者嘗試 ``ssh user@ubuntu.local``。

**Oh-My-Zsh (選用)**：

為了提升終端機體驗，建議安裝 ZSH：

.. code-block:: bash

   sudo apt install zsh
   sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
   # 設為預設 Shell
   chsh -s "$(which zsh)"
   # 推薦主題
   omz theme set gallois

**必要的套件安裝**：

請依照 ToddlerBot 官方文件安裝：
1.  **Real-Time Kernel**: [連結](https://hshi74.github.io/toddlerbot/software/02_jetson_orin.html#set-up-real-time-rt-kernel)
2.  **Additional Packages**: [連結](https://hshi74.github.io/toddlerbot/software/02_jetson_orin.html#additional-packages)

.. note::
   如果 PyTorch 無法匯入，可能是 CUDA Toolkit 未正確安裝。請檢查 ``nvidia-smi`` 並手動安裝對應版本的 toolkit (如 ``sudo apt install cuda-toolkit-12-x``)。

無螢幕遠端 (Headless)
~~~~~~~~~~~~~~~~~~~~~
為了方便攜帶，建議設定：
1.  修改 Hostname: ``sudo hostnamectl hostname toddlerbot``，方便區分。
2.  安裝 RustDesk 以備不時之需 (如果需要 GUI)。

.. toctree::
   :maxdepth: 1
   :caption: 詳細安裝紀錄

   software_notes/2026_01_23_Jetson_OS
