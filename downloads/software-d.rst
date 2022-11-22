Software
========

Software - подраздел в котором вы сможете найти прошивки автопилота, параметры автопилота, тестовые Lua-скрипты, версии НСУ Pioneer Station.

Прошивка автопилота (АП) представляет собой набор математических моделей (формул), которые определяют поведение квадрокоптера. Параметры автопилота являются "аргументами x, y, z", которые подставляются в "уравнения".

Правильная комбинация прошивки АП и параметров АП критически важна для правильной работы квадрокоптера и безопасного полета.

.. warning:: Внимание тестовые прошивки находятся на этапе проверки и являются нестабильными. Применять на свой страх и риск. Рекомендуется использовать только те комбинации, что прописаны в инструкции.


Прошивки АП
-----------

Прошивки автопилота "Pioneer Base"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Стабильные:**

* |fw_ap_base|

**Тестовые:**

**Устаревшие:**

* `Pioneer Base 1.5.6173 <https://disk.yandex.ru/d/WPgcrfgPKFpHBg>`__
* `Pioneer Base 1.4.4922 <https://disk.yandex.ru/d/amKrbOJ686VDVA>`__

________

Прошивки дополнительных модулей для "Pioneer Base"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Стабильные:**


* Прошивка платы подключения дополнительных модулей v4.0 - |fw_opt_board|
* Прошивка модуля навигации в помещении USNav - |fw_USNav|


**Тестовые:**

**Устаревшие:**

______

Прошивки aвтопилота "Pioneer Mini"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


**Стабильные:**

* |fw_ap_mini|

**Тестовые:**


* `Бета обновление ПО для Пионера Мини от 24.06.21 <https://disk.yandex.ru/d/zXTAyxGHrJBoDA>`__

Для доступа к тестовым прошивкам пишите в `телеграмм аккаунт <https://t.me/geoscan_edu>`__

**Устаревшие:**

* `Pioneer Mini 1.6.7747 <https://disk.yandex.ru/d/xdrsPzICMUQgPw>`__

* `Pioneer Mini 1.6.7482 <https://disk.yandex.ru/d/2lt2YDFPGsik-w?w=1>`__

* `Pioneer Mini 1.6.7257 <https://disk.yandex.ru/d/WPgcrfgPKFpHBg>`__

* `Pioneer Mini 1.6.7459 <https://disk.yandex.ru/d/vjykKgJVmepbZQ>`__ (Добавлена поддержка pioneer_sdk и программирования на Python)

* `Pioneer Mini 1.6.7011 <https://disk.yandex.ru/d/HqEswyY2PQRvrw>`__

* `Pioneer Mini 1.6.7009 <https://disk.yandex.ru/d/mvSrLNtjDdY_fw>`__

* `Pioneer Mini 1.6.7008 <https://disk.yandex.ru/d/rLFfxYVPOwPpNA>`__

* `Pioneer Mini 1.6.7007 <https://disk.yandex.ru/d/mmkbSU8OmG7KfA>`__

* `Pioneer Mini 1.6.7006 <https://disk.yandex.ru/d/IGOPr_vnh8XdgA>`__

* `Pioneer Mini 1.6.6977 <https://disk.yandex.ru/d/ndf7lhV3gSIhpA>`__


Прошивки ESP32 для "Pioneer Mini"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Стабильные:**

* ESPTOOL с прошивкой ESP 0.5.6 и параметрами автопилота 9202 - `ESPTool 0.5.6 <https://disk.yandex.ru/d/3IprqU238K4N_g>`__

**Устаревшие:**

* ESPTOOL с прошивкой ESP 0.4.5 и параметрами автопилота 0014 - `ESPTool 0.4.5 <https://disk.yandex.ru/d/ymscegzZ7uD4RA>`__

* ESPTOOL с прошивкой ESP 0.2.5 и параметрами автопилота 0007 - `ESPTool 0.2.5 <https://disk.yandex.ru/d/oWXwX4rLs-Fucw>`__

* ESPTOOL с прошивкой ESP 0.2.6 и параметрами автопилота 0007 - `ESPTool 0.2.6 <https://disk.yandex.ru/d/wslNfLDz23mE2g>`__

_______

Прошивки автопилота "Pioneer Max"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Стабильные:**

* |fw_ap_max|

* `Pioneer Max 1.6.7185 для ROS <https://drive.google.com/uc?export=download&confirm=no_antivirus&id=13Qm2YY8UcYd9dDmOfHSlHRpk7JiuzOxo>`_

**Тестовые:**


**Устаревшие:**

_______

Параметры автопилота
--------------------

Параметры автопилота (АП) это - аргументы (условно x,y,z...) которые подставляются в математическую модель автопилота. Параметры непосредственно влияют на поведение квадрокптера в полете.

Параметры автопилота "Pioneer Mini"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Стабильные:**

* `Параметры АП Pioneer Mini 1.0.9202 <https://disk.yandex.ru/d/fdTyvffNctHW3A>`__ (Для АП 1.6.9202 и новее)

* `Параметры АП Pioneer Mini 1.0.0014 <https://disk.yandex.ru/d/LOHZoIZ45vNV2Q>`__ (Для АП 1.6.7747 и новее)

* `Параметры АП Pioneer Mini 1.0.0012 <https://disk.yandex.ru/d/AKSr6SCzZXvziQ>`__ (Для работы с Python + Mavlink и АП 1.6.7482 и новее)

* `Параметры АП Pioneer Mini 1.0.0007 <https://disk.yandex.ru/d/Vt6cgbspvuj55Q>`__ (Для корректной работой с новой версией прошивки ESP 32)

**Тестовые:**

**Устаревшие:**

* `Параметры АП Pioneer Mini 1.0.0004 <https://disk.yandex.ru/d/OcaxquZ6LHq_2A>`__ (Изменены параметры АП влияющие на отключение моторов.)

* `Параметры АП Pioneer Mini 1.0.0003 <https://disk.yandex.ru/d/n9ZW5_KnBi_chA>`__

* `Параметры АП Pioneer Mini 1.0.0002 <https://disk.yandex.ru/d/1JZUIGoqLgltMw>`__

* `Параметры АП Pioneer Mini 1.0.0001 <https://disk.yandex.ru/d/MLrGnb5ovik-Rw>`__

______

Параметры автопилота "Pioneer Base"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Стабильные:**


* `Параметры АП для Pioneer Base 1.6.7178 (update) <https://disk.yandex.ru/d/Doq-oA6ZwtM9Tw>`__


**Тестовые:**


**Устаревшие:**

______

Параметры автопилота "Pioneer Max"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Стабильные:**

* `Параметры АП для Pioneer Max <https://disk.yandex.ru/d/IrWVG9xBmZaenw>`__ / Файл readme обязателен к прочтению!

* `Параметры АП для Pioneer Max <https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1h7_B2DjN7hiN_PCSxYsdqPgXFBfr_AHK>`_

**Тестовые:**


**Устаревшие:**

______

Тестовые Lua-скрипты для "Пионеров"
-----------------------------------

Данные скрипты представлены как есть, вы несете полную ответственность за их запуск на квадрокоптере.

*   :download:`Тест плавного свечения светодиодами<files/lua/nice_color.lua>`

Скрипт ниже тестировался с системой оптического позиционирования, для корректной работы читайте комментарий в начале.

*   :download:`Запуск скрипта по тумблеру<files/lua/rc8channel-Test.lua>`

Скрипт ниже тестировался с системой ИК HTC Lighthouse v2 (SteamVR v2), для корректной работы читайте комментарий в начале скрипта. Необходим ИК модуль на Пионере и базовая станция SteamVR v2.

*   :download:`Запуск скрипта по тумблеру<files/lua/goToPointRoofTest-3-lighthouse.lua>`


Pioneer Station
---------------

Актуальную версию установщика Вы можете скачать по ссылке - |dnld_ps| .













